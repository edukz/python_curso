#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Connectivity Manager - Sistema de detecção e gerenciamento de conectividade
"""

import socket
import threading
import time
import requests
from typing import Callable, Optional, List, Dict, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum


class ConnectionStatus(Enum):
    """Status de conectividade"""
    ONLINE = "online"
    OFFLINE = "offline"
    LIMITED = "limited"  # Conexão limitada/lenta
    UNKNOWN = "unknown"


@dataclass
class ConnectionEvent:
    """Evento de mudança de conectividade"""
    timestamp: datetime
    old_status: ConnectionStatus
    new_status: ConnectionStatus
    latency_ms: Optional[float] = None
    error_message: Optional[str] = None


class ConnectivityManager:
    """Gerenciador de conectividade com detecção automática"""
    
    def __init__(self, check_interval: int = 30):
        self.check_interval = check_interval
        self.current_status = ConnectionStatus.UNKNOWN
        self.last_check = None
        self.connection_history: List[ConnectionEvent] = []
        self.observers: List[Callable[[ConnectionEvent], None]] = []
        
        # URLs para teste de conectividade
        self.test_urls = [
            "https://www.google.com",
            "https://www.github.com", 
            "https://httpbin.org/get",
            "https://www.python.org"
        ]
        
        # Thread de monitoramento
        self.monitoring = False
        self.monitor_thread: Optional[threading.Thread] = None
        
        # Configurações
        self.timeout_seconds = 5
        self.max_latency_ms = 3000  # Conexão considerada lenta acima disso
        
    def start_monitoring(self):
        """Inicia monitoramento automático de conectividade"""
        if self.monitoring:
            return
            
        self.monitoring = True
        self.monitor_thread = threading.Thread(
            target=self._monitor_loop, 
            daemon=True
        )
        self.monitor_thread.start()
        
    def stop_monitoring(self):
        """Para o monitoramento automático"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1)
            
    def check_connectivity(self) -> ConnectionStatus:
        """Verifica conectividade atual"""
        # Teste básico de socket
        if not self._can_connect_to_host("8.8.8.8", 53):
            self._update_status(ConnectionStatus.OFFLINE)
            return self.current_status
            
        # Testa URLs reais
        latency_results = []
        successful_requests = 0
        
        for url in self.test_urls[:2]:  # Testa apenas 2 URLs para ser mais rápido
            try:
                start_time = time.time()
                response = requests.get(
                    url, 
                    timeout=self.timeout_seconds,
                    headers={'User-Agent': 'Python-Course-Connectivity-Check'}
                )
                
                if response.status_code == 200:
                    latency = (time.time() - start_time) * 1000
                    latency_results.append(latency)
                    successful_requests += 1
                    
            except Exception:
                continue
                
        # Determina status baseado nos resultados
        if successful_requests == 0:
            new_status = ConnectionStatus.OFFLINE
        elif successful_requests < len(self.test_urls) // 2:
            new_status = ConnectionStatus.LIMITED
        else:
            avg_latency = sum(latency_results) / len(latency_results)
            if avg_latency > self.max_latency_ms:
                new_status = ConnectionStatus.LIMITED
            else:
                new_status = ConnectionStatus.ONLINE
                
        # Atualiza status
        avg_latency = sum(latency_results) / len(latency_results) if latency_results else None
        self._update_status(new_status, avg_latency)
        
        return self.current_status
        
    def is_online(self) -> bool:
        """Verifica se está online"""
        return self.current_status == ConnectionStatus.ONLINE
        
    def is_offline(self) -> bool:
        """Verifica se está offline"""
        return self.current_status == ConnectionStatus.OFFLINE
        
    def has_limited_connection(self) -> bool:
        """Verifica se tem conexão limitada"""
        return self.current_status == ConnectionStatus.LIMITED
        
    def get_connection_quality(self) -> Dict[str, Any]:
        """Retorna informações sobre qualidade da conexão"""
        if not self.connection_history:
            return {"status": "unknown", "quality": 0}
            
        recent_events = [e for e in self.connection_history 
                        if e.timestamp >= datetime.now() - timedelta(minutes=10)]
        
        if not recent_events:
            return {"status": self.current_status.value, "quality": 0}
            
        # Calcula score de qualidade (0-100)
        online_time = sum(1 for e in recent_events if e.new_status == ConnectionStatus.ONLINE)
        quality_score = (online_time / len(recent_events)) * 100
        
        # Latência média
        latencies = [e.latency_ms for e in recent_events if e.latency_ms]
        avg_latency = sum(latencies) / len(latencies) if latencies else None
        
        return {
            "status": self.current_status.value,
            "quality": quality_score,
            "avg_latency_ms": avg_latency,
            "stability": self._calculate_stability_score(),
            "last_check": self.last_check.isoformat() if self.last_check else None
        }
        
    def add_observer(self, callback: Callable[[ConnectionEvent], None]):
        """Adiciona observador para mudanças de conectividade"""
        self.observers.append(callback)
        
    def remove_observer(self, callback: Callable[[ConnectionEvent], None]):
        """Remove observador"""
        if callback in self.observers:
            self.observers.remove(callback)
            
    def get_uptime_stats(self, hours: int = 24) -> Dict[str, float]:
        """Retorna estatísticas de uptime"""
        cutoff = datetime.now() - timedelta(hours=hours)
        recent_events = [e for e in self.connection_history if e.timestamp >= cutoff]
        
        if not recent_events:
            return {"uptime": 0, "downtime": 0, "limited_time": 0}
            
        total_minutes = 0
        online_minutes = 0
        limited_minutes = 0
        
        for i in range(len(recent_events)):
            if i == len(recent_events) - 1:
                # Último evento até agora
                duration = (datetime.now() - recent_events[i].timestamp).total_seconds() / 60
            else:
                # Duração até próximo evento
                duration = (recent_events[i+1].timestamp - recent_events[i].timestamp).total_seconds() / 60
                
            total_minutes += duration
            
            if recent_events[i].new_status == ConnectionStatus.ONLINE:
                online_minutes += duration
            elif recent_events[i].new_status == ConnectionStatus.LIMITED:
                limited_minutes += duration
                
        downtime_minutes = total_minutes - online_minutes - limited_minutes
        
        return {
            "uptime": (online_minutes / total_minutes * 100) if total_minutes > 0 else 0,
            "downtime": (downtime_minutes / total_minutes * 100) if total_minutes > 0 else 0,
            "limited_time": (limited_minutes / total_minutes * 100) if total_minutes > 0 else 0,
            "total_minutes": total_minutes
        }
        
    def force_offline_mode(self):
        """Força modo offline"""
        self._update_status(ConnectionStatus.OFFLINE, error_message="Forced offline mode")
        
    def _can_connect_to_host(self, host: str, port: int) -> bool:
        """Testa conexão básica com host"""
        try:
            socket.setdefaulttimeout(3)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception:
            return False
            
    def _update_status(self, new_status: ConnectionStatus, latency: Optional[float] = None, error_message: Optional[str] = None):
        """Atualiza status de conectividade"""
        old_status = self.current_status
        
        if old_status != new_status:
            event = ConnectionEvent(
                timestamp=datetime.now(),
                old_status=old_status,
                new_status=new_status,
                latency_ms=latency,
                error_message=error_message
            )
            
            self.connection_history.append(event)
            self.current_status = new_status
            self.last_check = datetime.now()
            
            # Notifica observadores
            for observer in self.observers:
                try:
                    observer(event)
                except Exception:
                    pass  # Falha silenciosa para não quebrar o sistema
                    
        # Limita histórico a últimas 1000 entradas
        if len(self.connection_history) > 1000:
            self.connection_history = self.connection_history[-1000:]
            
    def _monitor_loop(self):
        """Loop principal de monitoramento"""
        while self.monitoring:
            try:
                self.check_connectivity()
                time.sleep(self.check_interval)
            except Exception:
                time.sleep(self.check_interval)
                
    def _calculate_stability_score(self) -> float:
        """Calcula score de estabilidade baseado na frequência de mudanças"""
        recent_events = [e for e in self.connection_history 
                        if e.timestamp >= datetime.now() - timedelta(hours=1)]
        
        if len(recent_events) <= 1:
            return 100.0  # Muito estável
            
        # Penaliza mudanças frequentes de status
        changes_per_hour = len(recent_events)
        stability = max(0, 100 - (changes_per_hour * 10))
        
        return stability


class OfflineCapabilityChecker:
    """Verifica quais recursos estão disponíveis offline"""
    
    def __init__(self, connectivity_manager: ConnectivityManager):
        self.connectivity = connectivity_manager
        self.offline_features = {
            "course_modules": True,      # Módulos básicos sempre disponíveis
            "exercises": True,           # Exercícios locais disponíveis
            "progress_tracking": True,   # Progresso local sempre funciona
            "themes": True,              # Temas são locais
            "certificates": False,       # Requer conexão para validação
            "sync": False,               # Obviamente requer conexão
            "updates": False,            # Requer conexão
            "web_resources": False,      # Links externos
            "code_sharing": False        # Compartilhamento online
        }
        
    def check_feature_availability(self, feature: str) -> bool:
        """Verifica se uma funcionalidade está disponível"""
        if self.connectivity.is_online():
            return True  # Tudo disponível online
            
        return self.offline_features.get(feature, False)
        
    def get_available_features(self) -> List[str]:
        """Retorna lista de funcionalidades disponíveis no estado atual"""
        if self.connectivity.is_online():
            return list(self.offline_features.keys())
            
        return [feature for feature, available in self.offline_features.items() if available]
        
    def get_unavailable_features(self) -> List[str]:
        """Retorna lista de funcionalidades indisponíveis no estado atual"""
        if self.connectivity.is_online():
            return []
            
        return [feature for feature, available in self.offline_features.items() if not available]
        
    def show_offline_limitations(self) -> str:
        """Retorna string explicando limitações do modo offline"""
        unavailable = self.get_unavailable_features()
        
        if not unavailable:
            return "✅ Todas as funcionalidades estão disponíveis!"
            
        limitations = [
            "🔌 MODO OFFLINE ATIVO",
            "",
            "✅ Disponível:",
            "• Todos os módulos do curso",
            "• Sistema de exercícios", 
            "• Rastreamento de progresso",
            "• Personalização de temas",
            "",
            "❌ Indisponível:",
            "• Geração de certificados",
            "• Sincronização de dados",
            "• Atualizações automáticas",
            "• Recursos web externos",
            "",
            "💡 Seus dados serão sincronizados quando a conexão for restaurada."
        ]
        
        return "\n".join(limitations)