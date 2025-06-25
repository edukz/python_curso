#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sync Manager - Sistema de sincronização offline/online
"""

import json
import os
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path

from .connectivity_manager import ConnectivityManager, ConnectionEvent
from .resource_cache import ResourceCache


class SyncStatus(Enum):
    """Status de sincronização"""
    IDLE = "idle"
    SYNCING = "syncing"
    SUCCESS = "success"
    ERROR = "error"
    CONFLICT = "conflict"


@dataclass
class SyncOperation:
    """Operação de sincronização"""
    id: str
    operation_type: str  # 'upload', 'download', 'merge'
    resource_type: str   # 'progress', 'settings', 'analytics', etc
    data: Any
    timestamp: datetime
    priority: int = 1    # 1=alta, 2=média, 3=baixa
    retry_count: int = 0
    max_retries: int = 3


@dataclass
class SyncResult:
    """Resultado de sincronização"""
    operation_id: str
    status: SyncStatus
    message: str
    timestamp: datetime
    data_synced: Optional[Dict[str, Any]] = None
    conflicts: Optional[List[str]] = None


class OfflineOnlineSync:
    """Sistema de sincronização entre dados offline e online"""
    
    def __init__(self, connectivity_manager: ConnectivityManager, 
                 cache: ResourceCache, data_dir: str = ".sync"):
        self.connectivity = connectivity_manager
        self.cache = cache
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # Filas de sincronização
        self.pending_operations: List[SyncOperation] = []
        self.completed_operations: List[SyncResult] = []
        
        # Estado da sincronização
        self.current_status = SyncStatus.IDLE
        self.last_sync_time: Optional[datetime] = None
        self.auto_sync_enabled = True
        self.sync_interval_minutes = 15
        
        # Threading
        self.sync_thread: Optional[threading.Thread] = None
        self.stop_sync = threading.Event()
        
        # Callbacks
        self.sync_callbacks: List[Callable[[SyncResult], None]] = []
        
        # Arquivos de estado
        self.pending_file = self.data_dir / "pending_operations.json"
        self.state_file = self.data_dir / "sync_state.json"
        
        # Carrega estado persistente
        self._load_pending_operations()
        self._load_sync_state()
        
        # Registra observer de conectividade
        self.connectivity.add_observer(self._on_connectivity_change)
        
    def start_auto_sync(self):
        """Inicia sincronização automática"""
        if self.sync_thread and self.sync_thread.is_alive():
            return
            
        self.auto_sync_enabled = True
        self.stop_sync.clear()
        self.sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
        self.sync_thread.start()
        
    def stop_auto_sync(self):
        """Para sincronização automática"""
        self.auto_sync_enabled = False
        self.stop_sync.set()
        
        if self.sync_thread:
            self.sync_thread.join(timeout=5)
            
    def queue_sync_operation(self, operation_type: str, resource_type: str, 
                           data: Any, priority: int = 1) -> str:
        """Adiciona operação à fila de sincronização"""
        operation_id = f"{operation_type}_{resource_type}_{int(time.time())}"
        
        operation = SyncOperation(
            id=operation_id,
            operation_type=operation_type,
            resource_type=resource_type,
            data=data,
            timestamp=datetime.now(),
            priority=priority
        )
        
        # Insere na fila ordenada por prioridade
        self.pending_operations.append(operation)
        self.pending_operations.sort(key=lambda x: x.priority)
        
        # Salva estado
        self._save_pending_operations()
        
        return operation_id
        
    def sync_now(self, force: bool = False) -> List[SyncResult]:
        """Executa sincronização imediata"""
        if not self.connectivity.is_online() and not force:
            return [SyncResult(
                operation_id="immediate_sync",
                status=SyncStatus.ERROR,
                message="Sem conexão com a internet",
                timestamp=datetime.now()
            )]
            
        return self._execute_sync_operations()
        
    def sync_progress_data(self, progress_data: Dict) -> str:
        """Sincroniza dados de progresso"""
        return self.queue_sync_operation(
            operation_type="upload",
            resource_type="progress",
            data=progress_data,
            priority=1  # Alta prioridade
        )
        
    def sync_user_settings(self, settings: Dict) -> str:
        """Sincroniza configurações do usuário"""
        return self.queue_sync_operation(
            operation_type="upload", 
            resource_type="settings",
            data=settings,
            priority=2  # Média prioridade
        )
        
    def sync_analytics_data(self, analytics: Dict) -> str:
        """Sincroniza dados de analytics"""
        return self.queue_sync_operation(
            operation_type="upload",
            resource_type="analytics", 
            data=analytics,
            priority=2  # Média prioridade
        )
        
    def download_course_updates(self) -> str:
        """Baixa atualizações do curso"""
        return self.queue_sync_operation(
            operation_type="download",
            resource_type="course_content",
            data={"request_type": "updates"},
            priority=3  # Baixa prioridade
        )
        
    def get_sync_status(self) -> Dict[str, Any]:
        """Retorna status atual da sincronização"""
        return {
            "current_status": self.current_status.value,
            "last_sync": self.last_sync_time.isoformat() if self.last_sync_time else None,
            "pending_operations": len(self.pending_operations),
            "auto_sync_enabled": self.auto_sync_enabled,
            "connectivity_status": self.connectivity.current_status.value,
            "sync_interval_minutes": self.sync_interval_minutes,
            "total_synced": len(self.completed_operations)
        }
        
    def get_pending_operations(self) -> List[Dict[str, Any]]:
        """Retorna operações pendentes"""
        return [
            {
                "id": op.id,
                "type": op.operation_type,
                "resource": op.resource_type,
                "timestamp": op.timestamp.isoformat(),
                "priority": op.priority,
                "retry_count": op.retry_count
            }
            for op in self.pending_operations
        ]
        
    def get_sync_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Retorna histórico de sincronizações"""
        recent_operations = sorted(
            self.completed_operations, 
            key=lambda x: x.timestamp, 
            reverse=True
        )[:limit]
        
        return [
            {
                "id": result.operation_id,
                "status": result.status.value,
                "message": result.message,
                "timestamp": result.timestamp.isoformat(),
                "has_conflicts": bool(result.conflicts)
            }
            for result in recent_operations
        ]
        
    def resolve_conflict(self, operation_id: str, resolution: str) -> bool:
        """Resolve conflito de sincronização"""
        # Encontra operação com conflito
        for result in self.completed_operations:
            if (result.operation_id == operation_id and 
                result.status == SyncStatus.CONFLICT):
                
                # Re-adiciona à fila com resolução
                for op in self.pending_operations:
                    if op.id == operation_id:
                        op.data["conflict_resolution"] = resolution
                        return True
                        
        return False
        
    def add_sync_callback(self, callback: Callable[[SyncResult], None]):
        """Adiciona callback para eventos de sincronização"""
        self.sync_callbacks.append(callback)
        
    def remove_sync_callback(self, callback: Callable[[SyncResult], None]):
        """Remove callback"""
        if callback in self.sync_callbacks:
            self.sync_callbacks.remove(callback)
            
    def _sync_loop(self):
        """Loop principal de sincronização automática"""
        while self.auto_sync_enabled and not self.stop_sync.is_set():
            try:
                if self.connectivity.is_online() and self.pending_operations:
                    self._execute_sync_operations()
                    
                # Aguarda próximo ciclo
                self.stop_sync.wait(self.sync_interval_minutes * 60)
                
            except Exception as e:
                print(f"Erro no loop de sincronização: {e}")
                self.stop_sync.wait(60)  # Aguarda 1 minuto em caso de erro
                
    def _execute_sync_operations(self) -> List[SyncResult]:
        """Executa operações de sincronização pendentes"""
        if self.current_status == SyncStatus.SYNCING:
            return []
            
        self.current_status = SyncStatus.SYNCING
        results = []
        
        try:
            # Processa operações por prioridade
            operations_to_process = self.pending_operations.copy()
            
            for operation in operations_to_process:
                result = self._process_single_operation(operation)
                results.append(result)
                
                # Remove da fila se bem-sucedido ou excedeu tentativas
                if (result.status in [SyncStatus.SUCCESS, SyncStatus.CONFLICT] or
                    operation.retry_count >= operation.max_retries):
                    self.pending_operations.remove(operation)
                else:
                    # Incrementa contador de tentativas
                    operation.retry_count += 1
                    
                # Chama callbacks
                for callback in self.sync_callbacks:
                    try:
                        callback(result)
                    except Exception:
                        pass
                        
            # Atualiza estado
            self.last_sync_time = datetime.now()
            self.current_status = SyncStatus.SUCCESS if results else SyncStatus.IDLE
            
            # Salva estado persistente
            self._save_pending_operations()
            self._save_sync_state()
            
        except Exception as e:
            self.current_status = SyncStatus.ERROR
            error_result = SyncResult(
                operation_id="sync_batch",
                status=SyncStatus.ERROR,
                message=f"Erro na sincronização: {str(e)}",
                timestamp=datetime.now()
            )
            results.append(error_result)
            
        # Adiciona ao histórico
        self.completed_operations.extend(results)
        
        # Limita histórico
        if len(self.completed_operations) > 1000:
            self.completed_operations = self.completed_operations[-1000:]
            
        return results
        
    def _process_single_operation(self, operation: SyncOperation) -> SyncResult:
        """Processa uma operação individual"""
        try:
            if operation.operation_type == "upload":
                return self._handle_upload(operation)
            elif operation.operation_type == "download":
                return self._handle_download(operation)
            elif operation.operation_type == "merge":
                return self._handle_merge(operation)
            else:
                return SyncResult(
                    operation_id=operation.id,
                    status=SyncStatus.ERROR,
                    message=f"Tipo de operação desconhecido: {operation.operation_type}",
                    timestamp=datetime.now()
                )
                
        except Exception as e:
            return SyncResult(
                operation_id=operation.id,
                status=SyncStatus.ERROR,
                message=f"Erro ao processar operação: {str(e)}",
                timestamp=datetime.now()
            )
            
    def _handle_upload(self, operation: SyncOperation) -> SyncResult:
        """Processa upload de dados"""
        # Simula upload (em implementação real, faria request HTTP)
        
        # Cacheia dados localmente como backup
        cache_key = f"uploaded_{operation.resource_type}_{operation.timestamp.isoformat()}"
        self.cache.store(cache_key, operation.data, ttl_hours=168)  # 1 semana
        
        # Simula latência de rede
        time.sleep(0.1)
        
        return SyncResult(
            operation_id=operation.id,
            status=SyncStatus.SUCCESS,
            message=f"Upload de {operation.resource_type} concluído",
            timestamp=datetime.now(),
            data_synced={"resource_type": operation.resource_type, "size": len(str(operation.data))}
        )
        
    def _handle_download(self, operation: SyncOperation) -> SyncResult:
        """Processa download de dados"""
        # Simula download de atualizações
        
        # Em implementação real, faria request para servidor
        downloaded_data = {
            "content_version": "2.1.0",
            "last_updated": datetime.now().isoformat(),
            "new_exercises": [],
            "updated_modules": []
        }
        
        # Cacheia dados baixados
        cache_key = f"downloaded_{operation.resource_type}"
        self.cache.store(cache_key, downloaded_data, ttl_hours=24)
        
        return SyncResult(
            operation_id=operation.id,
            status=SyncStatus.SUCCESS,
            message=f"Download de {operation.resource_type} concluído",
            timestamp=datetime.now(),
            data_synced=downloaded_data
        )
        
    def _handle_merge(self, operation: SyncOperation) -> SyncResult:
        """Processa merge de dados conflitantes"""
        # Lógica de merge dependeria do tipo de recurso
        # Para dados de progresso: manter valores máximos
        # Para configurações: priorizar mais recentes
        
        local_data = operation.data.get("local", {})
        remote_data = operation.data.get("remote", {})
        
        # Exemplo de merge simples para progresso
        if operation.resource_type == "progress":
            merged_data = self._merge_progress_data(local_data, remote_data)
        else:
            merged_data = {**local_data, **remote_data}  # Remote sobrescreve local
            
        return SyncResult(
            operation_id=operation.id,
            status=SyncStatus.SUCCESS,
            message=f"Merge de {operation.resource_type} concluído",
            timestamp=datetime.now(),
            data_synced=merged_data
        )
        
    def _merge_progress_data(self, local: Dict, remote: Dict) -> Dict:
        """Merge específico para dados de progresso"""
        merged = local.copy()
        
        # Manter valores máximos para scores e progresso
        if "total_score" in remote:
            merged["total_score"] = max(
                local.get("total_score", 0),
                remote.get("total_score", 0)
            )
            
        if "modules_completed" in remote:
            local_modules = set(local.get("modules_completed", []))
            remote_modules = set(remote.get("modules_completed", []))
            merged["modules_completed"] = list(local_modules | remote_modules)
            
        # Soma tempo total de estudo
        if "total_time_spent" in remote:
            merged["total_time_spent"] = (
                local.get("total_time_spent", 0) + 
                remote.get("total_time_spent", 0)
            )
            
        return merged
        
    def _on_connectivity_change(self, event: ConnectionEvent):
        """Responde a mudanças de conectividade"""
        if event.new_status.value == "online" and self.pending_operations:
            # Conectou - inicia sincronização se houver operações pendentes
            if not self.sync_thread or not self.sync_thread.is_alive():
                threading.Thread(
                    target=self._execute_sync_operations,
                    daemon=True
                ).start()
                
    def _load_pending_operations(self):
        """Carrega operações pendentes do arquivo"""
        if not self.pending_file.exists():
            return
            
        try:
            with open(self.pending_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            self.pending_operations = []
            for item in data:
                item['timestamp'] = datetime.fromisoformat(item['timestamp'])
                self.pending_operations.append(SyncOperation(**item))
                
        except Exception as e:
            print(f"Erro ao carregar operações pendentes: {e}")
            
    def _save_pending_operations(self):
        """Salva operações pendentes no arquivo"""
        try:
            data = []
            for op in self.pending_operations:
                op_dict = asdict(op)
                op_dict['timestamp'] = op.timestamp.isoformat()
                data.append(op_dict)
                
            with open(self.pending_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Erro ao salvar operações pendentes: {e}")
            
    def _load_sync_state(self):
        """Carrega estado da sincronização"""
        if not self.state_file.exists():
            return
            
        try:
            with open(self.state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            if "last_sync_time" in data:
                self.last_sync_time = datetime.fromisoformat(data["last_sync_time"])
                
            self.auto_sync_enabled = data.get("auto_sync_enabled", True)
            self.sync_interval_minutes = data.get("sync_interval_minutes", 15)
            
        except Exception as e:
            print(f"Erro ao carregar estado de sincronização: {e}")
            
    def _save_sync_state(self):
        """Salva estado da sincronização"""
        try:
            data = {
                "last_sync_time": self.last_sync_time.isoformat() if self.last_sync_time else None,
                "auto_sync_enabled": self.auto_sync_enabled,
                "sync_interval_minutes": self.sync_interval_minutes,
                "saved_at": datetime.now().isoformat()
            }
            
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Erro ao salvar estado de sincronização: {e}")