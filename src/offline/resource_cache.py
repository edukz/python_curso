#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Resource Cache - Sistema completo de cache para modo offline
"""

import os
import json
import hashlib
import shutil
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Union, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import pickle
import gzip


@dataclass
class CacheEntry:
    """Entrada do cache"""
    key: str
    data_type: str  # 'json', 'binary', 'text', 'file'
    size_bytes: int
    created_at: datetime
    last_accessed: datetime
    access_count: int
    expiry_date: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class ResourceCache:
    """Cache inteligente para recursos offline"""
    
    def __init__(self, cache_dir: str = ".cache", max_size_mb: int = 500):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        
        # Diretórios específicos
        self.data_dir = self.cache_dir / "data"
        self.files_dir = self.cache_dir / "files"
        self.temp_dir = self.cache_dir / "temp"
        
        for directory in [self.data_dir, self.files_dir, self.temp_dir]:
            directory.mkdir(exist_ok=True)
            
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.db_path = self.cache_dir / "cache_index.db"
        
        # Inicializa banco de dados
        self._init_database()
        
        # Estatísticas
        self.hits = 0
        self.misses = 0
        
    def _init_database(self):
        """Inicializa banco de dados SQLite para índice do cache"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache_entries (
                    key TEXT PRIMARY KEY,
                    data_type TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    size_bytes INTEGER NOT NULL,
                    created_at TEXT NOT NULL,
                    last_accessed TEXT NOT NULL,
                    access_count INTEGER DEFAULT 0,
                    expiry_date TEXT,
                    metadata TEXT
                )
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_last_accessed 
                ON cache_entries(last_accessed)
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_expiry_date 
                ON cache_entries(expiry_date)
            """)
            
    def store(self, key: str, data: Any, data_type: str = 'auto', 
              ttl_hours: Optional[int] = None, metadata: Optional[Dict] = None) -> bool:
        """Armazena dados no cache"""
        try:
            # Auto-detecta tipo se necessário
            if data_type == 'auto':
                data_type = self._detect_data_type(data)
                
            # Gera hash do key para nome do arquivo
            file_hash = hashlib.md5(key.encode()).hexdigest()
            
            # Determina extensão baseada no tipo
            extensions = {
                'json': '.json',
                'binary': '.bin',
                'text': '.txt',
                'file': '.cache'
            }
            extension = extensions.get(data_type, '.cache')
            
            file_path = self.data_dir / f"{file_hash}{extension}"
            
            # Serializa e salva dados
            size_bytes = self._serialize_data(data, file_path, data_type)
            
            if size_bytes == 0:
                return False
                
            # Calcula data de expiração
            expiry_date = None
            if ttl_hours:
                expiry_date = datetime.now() + timedelta(hours=ttl_hours)
                
            # Registra no banco
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT OR REPLACE INTO cache_entries 
                    (key, data_type, file_path, size_bytes, created_at, 
                     last_accessed, access_count, expiry_date, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, 0, ?, ?)
                """, (
                    key, data_type, str(file_path), size_bytes,
                    datetime.now().isoformat(), datetime.now().isoformat(),
                    expiry_date.isoformat() if expiry_date else None,
                    json.dumps(metadata) if metadata else None
                ))
                
            # Verifica se precisa fazer limpeza
            self._cleanup_if_needed()
            
            return True
            
        except Exception as e:
            print(f"Erro ao armazenar no cache: {e}")
            return False
            
    def retrieve(self, key: str) -> Optional[Any]:
        """Recupera dados do cache"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT data_type, file_path, expiry_date, metadata
                    FROM cache_entries WHERE key = ?
                """, (key,))
                
                row = cursor.fetchone()
                
            if not row:
                self.misses += 1
                return None
                
            data_type, file_path_str, expiry_str, metadata_str = row
            file_path = Path(file_path_str)
            
            # Verifica se arquivo existe
            if not file_path.exists():
                self._remove_entry(key)
                self.misses += 1
                return None
                
            # Verifica expiração
            if expiry_str:
                expiry_date = datetime.fromisoformat(expiry_str)
                if datetime.now() > expiry_date:
                    self._remove_entry(key)
                    self.misses += 1
                    return None
                    
            # Deserializa dados
            data = self._deserialize_data(file_path, data_type)
            
            if data is not None:
                # Atualiza estatísticas de acesso
                with sqlite3.connect(self.db_path) as conn:
                    conn.execute("""
                        UPDATE cache_entries 
                        SET last_accessed = ?, access_count = access_count + 1
                        WHERE key = ?
                    """, (datetime.now().isoformat(), key))
                    
                self.hits += 1
                return data
            else:
                self.misses += 1
                return None
                
        except Exception as e:
            print(f"Erro ao recuperar do cache: {e}")
            self.misses += 1
            return None
            
    def exists(self, key: str) -> bool:
        """Verifica se chave existe no cache"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT 1 FROM cache_entries 
                    WHERE key = ? AND (expiry_date IS NULL OR expiry_date > ?)
                """, (key, datetime.now().isoformat()))
                
                return cursor.fetchone() is not None
                
        except Exception:
            return False
            
    def remove(self, key: str) -> bool:
        """Remove entrada do cache"""
        return self._remove_entry(key)
        
    def clear_all(self) -> bool:
        """Limpa todo o cache"""
        try:
            # Remove todos os arquivos
            shutil.rmtree(self.data_dir)
            shutil.rmtree(self.files_dir)
            self.data_dir.mkdir(exist_ok=True)
            self.files_dir.mkdir(exist_ok=True)
            
            # Limpa banco
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("DELETE FROM cache_entries")
                
            # Reset estatísticas
            self.hits = 0
            self.misses = 0
            
            return True
            
        except Exception as e:
            print(f"Erro ao limpar cache: {e}")
            return False
            
    def get_size_info(self) -> Dict[str, Any]:
        """Retorna informações sobre tamanho do cache"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT COUNT(*), SUM(size_bytes), AVG(size_bytes)
                    FROM cache_entries
                """)
                
                count, total_size, avg_size = cursor.fetchone()
                
            return {
                "entries": count or 0,
                "total_size_mb": (total_size or 0) / (1024 * 1024),
                "average_size_kb": (avg_size or 0) / 1024,
                "max_size_mb": self.max_size_bytes / (1024 * 1024),
                "usage_percent": ((total_size or 0) / self.max_size_bytes) * 100
            }
            
        except Exception:
            return {"entries": 0, "total_size_mb": 0, "average_size_kb": 0}
            
    def get_statistics(self) -> Dict[str, Any]:
        """Retorna estatísticas do cache"""
        size_info = self.get_size_info()
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            **size_info,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "total_requests": total_requests
        }
        
    def cleanup_expired(self) -> int:
        """Remove entradas expiradas"""
        try:
            current_time = datetime.now().isoformat()
            
            # Busca entradas expiradas
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT key, file_path FROM cache_entries 
                    WHERE expiry_date IS NOT NULL AND expiry_date <= ?
                """, (current_time,))
                
                expired_entries = cursor.fetchall()
                
            # Remove arquivos e entradas
            removed_count = 0
            for key, file_path in expired_entries:
                if self._remove_entry(key):
                    removed_count += 1
                    
            return removed_count
            
        except Exception as e:
            print(f"Erro na limpeza de expirados: {e}")
            return 0
            
    def cache_course_data(self, progress_data: Dict, modules_data: Dict, 
                         exercises_data: Dict) -> bool:
        """Cacheia dados essenciais do curso"""
        essential_data = {
            "progress": progress_data,
            "modules": modules_data,
            "exercises": exercises_data,
            "cached_at": datetime.now().isoformat()
        }
        
        return self.store(
            "course_essential_data",
            essential_data,
            data_type="json",
            ttl_hours=72,  # 3 dias
            metadata={"type": "essential", "priority": "high"}
        )
        
    def get_course_data(self) -> Optional[Dict]:
        """Recupera dados essenciais do curso"""
        return self.retrieve("course_essential_data")
        
    def cache_user_settings(self, theme: str, preferences: Dict) -> bool:
        """Cacheia configurações do usuário"""
        settings_data = {
            "theme": theme,
            "preferences": preferences,
            "cached_at": datetime.now().isoformat()
        }
        
        return self.store(
            "user_settings",
            settings_data,
            data_type="json",
            metadata={"type": "settings", "priority": "medium"}
        )
        
    def preload_common_resources(self, resources: List[Tuple[str, Any]]) -> int:
        """Pré-carrega recursos comuns"""
        loaded_count = 0
        
        for key, data in resources:
            if self.store(key, data, ttl_hours=24):
                loaded_count += 1
                
        return loaded_count
        
    def _detect_data_type(self, data: Any) -> str:
        """Auto-detecta tipo de dados"""
        if isinstance(data, (dict, list)):
            return "json"
        elif isinstance(data, str):
            return "text"
        elif isinstance(data, bytes):
            return "binary"
        else:
            return "binary"  # Usa pickle para outros tipos
            
    def _serialize_data(self, data: Any, file_path: Path, data_type: str) -> int:
        """Serializa dados para arquivo"""
        try:
            if data_type == "json":
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    
            elif data_type == "text":
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(data))
                    
            elif data_type == "binary":
                # Usa pickle com compressão
                with gzip.open(file_path, 'wb') as f:
                    pickle.dump(data, f)
                    
            elif data_type == "file":
                # Copia arquivo existente
                if hasattr(data, 'read'):
                    with open(file_path, 'wb') as f:
                        shutil.copyfileobj(data, f)
                else:
                    shutil.copy2(str(data), file_path)
                    
            return file_path.stat().st_size
            
        except Exception as e:
            print(f"Erro na serialização: {e}")
            return 0
            
    def _deserialize_data(self, file_path: Path, data_type: str) -> Any:
        """Deserializa dados do arquivo"""
        try:
            if data_type == "json":
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
                    
            elif data_type == "text":
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
                    
            elif data_type == "binary":
                with gzip.open(file_path, 'rb') as f:
                    return pickle.load(f)
                    
            elif data_type == "file":
                return file_path
                
        except Exception as e:
            print(f"Erro na deserialização: {e}")
            return None
            
    def _remove_entry(self, key: str) -> bool:
        """Remove entrada específica do cache"""
        try:
            # Busca caminho do arquivo
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT file_path FROM cache_entries WHERE key = ?
                """, (key,))
                
                row = cursor.fetchone()
                
                if row:
                    file_path = Path(row[0])
                    
                    # Remove arquivo
                    if file_path.exists():
                        file_path.unlink()
                        
                    # Remove entrada do banco
                    conn.execute("DELETE FROM cache_entries WHERE key = ?", (key,))
                    return True
                    
            return False
            
        except Exception as e:
            print(f"Erro ao remover entrada: {e}")
            return False
            
    def _cleanup_if_needed(self):
        """Faz limpeza se necessário"""
        size_info = self.get_size_info()
        
        if size_info["usage_percent"] > 90:  # Acima de 90% do limite
            self._cleanup_lru(target_percent=70)  # Limpa até 70%
            
    def _cleanup_lru(self, target_percent: float = 70):
        """Limpa entradas menos recentemente usadas"""
        try:
            target_size = self.max_size_bytes * (target_percent / 100)
            
            # Busca entradas ordenadas por último acesso
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("""
                    SELECT key, size_bytes FROM cache_entries 
                    ORDER BY last_accessed ASC
                """)
                
                entries = cursor.fetchall()
                
            current_size = sum(size for _, size in entries)
            
            # Remove entradas até atingir tamanho alvo
            for key, size in entries:
                if current_size <= target_size:
                    break
                    
                if self._remove_entry(key):
                    current_size -= size
                    
        except Exception as e:
            print(f"Erro na limpeza LRU: {e}")


class OfflineResourceManager:
    """Gerenciador de recursos para modo offline"""
    
    def __init__(self, cache: ResourceCache):
        self.cache = cache
        self.essential_resources = [
            "course_modules",
            "exercise_templates", 
            "theme_data",
            "progress_schemas",
            "help_content"
        ]
        
    def prepare_offline_mode(self, course_data: Dict) -> bool:
        """Prepara sistema para modo offline"""
        try:
            # Cacheia dados essenciais
            success_count = 0
            
            # Módulos do curso
            if "modules" in course_data:
                if self.cache.store("course_modules", course_data["modules"], ttl_hours=168):
                    success_count += 1
                    
            # Templates de exercícios
            if "exercise_templates" in course_data:
                if self.cache.store("exercise_templates", course_data["exercise_templates"], ttl_hours=168):
                    success_count += 1
                    
            # Dados de temas
            if "themes" in course_data:
                if self.cache.store("theme_data", course_data["themes"], ttl_hours=720):  # 30 dias
                    success_count += 1
                    
            # Conteúdo de ajuda
            if "help_content" in course_data:
                if self.cache.store("help_content", course_data["help_content"], ttl_hours=168):
                    success_count += 1
                    
            return success_count >= 2  # Pelo menos 2 recursos essenciais
            
        except Exception as e:
            print(f"Erro ao preparar modo offline: {e}")
            return False
            
    def is_offline_ready(self) -> bool:
        """Verifica se sistema está pronto para modo offline"""
        essential_count = 0
        
        for resource in self.essential_resources[:4]:  # Verifica 4 principais
            if self.cache.exists(resource):
                essential_count += 1
                
        return essential_count >= 3  # Pelo menos 3 dos 4 essenciais
        
    def get_offline_status(self) -> Dict[str, Any]:
        """Retorna status detalhado do modo offline"""
        available_resources = []
        missing_resources = []
        
        for resource in self.essential_resources:
            if self.cache.exists(resource):
                available_resources.append(resource)
            else:
                missing_resources.append(resource)
                
        cache_stats = self.cache.get_statistics()
        
        return {
            "ready": self.is_offline_ready(),
            "available_resources": available_resources,
            "missing_resources": missing_resources,
            "cache_size_mb": cache_stats["total_size_mb"],
            "cached_items": cache_stats["entries"],
            "last_sync": self._get_last_sync_time()
        }
        
    def _get_last_sync_time(self) -> Optional[str]:
        """Retorna timestamp da última sincronização"""
        sync_data = self.cache.retrieve("last_sync_time")
        return sync_data.get("timestamp") if sync_data else None