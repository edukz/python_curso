#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intelligent Cache Manager - Cache com expiration queue e batch operations
"""

import time
import heapq
import json
import pickle
from typing import Any, Optional, Dict, List, Tuple, Callable, Union
from functools import wraps
from collections import OrderedDict
import hashlib
from threading import Lock
from dataclasses import dataclass, field


@dataclass(order=True)
class CacheEntry:
    """Entrada de cache com prioridade para heap"""
    expiration_time: float
    key: str = field(compare=False)
    value: Any = field(compare=False)
    size: int = field(compare=False)
    access_count: int = field(default=0, compare=False)
    last_access: float = field(default_factory=time.time, compare=False)


class IntelligentCacheManager:
    """Cache inteligente com expiration queue e otimizações"""
    
    def __init__(self, max_size_mb: float = 100, default_ttl: int = 3600):
        """
        Inicializa o cache inteligente
        
        Args:
            max_size_mb: Tamanho máximo em MB
            default_ttl: TTL padrão em segundos
        """
        self.cache: Dict[str, CacheEntry] = {}
        self.expiration_queue: List[CacheEntry] = []
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.current_size_bytes = 0
        self.default_ttl = default_ttl
        self.lock = Lock()
        
        # Estatísticas
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        
    def _estimate_size(self, value: Any) -> int:
        """Estima o tamanho em bytes de um valor"""
        try:
            return len(pickle.dumps(value))
        except:
            # Fallback para estimativa básica
            return len(str(value))
            
    def get(self, key: str) -> Optional[Any]:
        """Obtém valor do cache com atualização de acesso"""
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None
                
            entry = self.cache[key]
            
            # Verifica se expirou
            if entry.expiration_time < time.time():
                self._remove_entry(key)
                self.misses += 1
                return None
                
            # Atualiza estatísticas
            entry.access_count += 1
            entry.last_access = time.time()
            self.hits += 1
            
            return entry.value
            
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Adiciona ou atualiza valor no cache"""
        ttl = ttl or self.default_ttl
        size = self._estimate_size(value)
        expiration = time.time() + ttl
        
        with self.lock:
            # Remove entrada antiga se existir
            if key in self.cache:
                self._remove_entry(key)
                
            # Verifica espaço e faz eviction se necessário
            self._ensure_space(size)
            
            # Cria nova entrada
            entry = CacheEntry(
                expiration_time=expiration,
                key=key,
                value=value,
                size=size
            )
            
            # Adiciona ao cache e heap
            self.cache[key] = entry
            heapq.heappush(self.expiration_queue, entry)
            self.current_size_bytes += size
            
    def batch_get(self, keys: List[str]) -> Dict[str, Optional[Any]]:
        """Obtém múltiplos valores de uma vez"""
        results = {}
        with self.lock:
            for key in keys:
                results[key] = self.get(key)
        return results
        
    def batch_set(self, items: Dict[str, Any], ttl: Optional[int] = None) -> None:
        """Define múltiplos valores de uma vez"""
        with self.lock:
            for key, value in items.items():
                self.set(key, value, ttl)
                
    def _remove_entry(self, key: str) -> None:
        """Remove entrada do cache"""
        if key in self.cache:
            entry = self.cache[key]
            self.current_size_bytes -= entry.size
            del self.cache[key]
            
    def _ensure_space(self, required_size: int) -> None:
        """Garante espaço suficiente fazendo eviction se necessário"""
        # Remove entradas expiradas primeiro
        self._cleanup_expired()
        
        # Se ainda precisar de espaço, remove LRU
        while (self.current_size_bytes + required_size > self.max_size_bytes 
               and self.cache):
            # Encontra entrada menos recentemente usada
            lru_key = min(self.cache.keys(), 
                         key=lambda k: self.cache[k].last_access)
            self._remove_entry(lru_key)
            self.evictions += 1
            
    def _cleanup_expired(self) -> None:
        """Remove entradas expiradas do cache"""
        current_time = time.time()
        
        # Remove do heap
        while self.expiration_queue and self.expiration_queue[0].expiration_time < current_time:
            entry = heapq.heappop(self.expiration_queue)
            if entry.key in self.cache:
                self._remove_entry(entry.key)
                
    def clear(self) -> None:
        """Limpa todo o cache"""
        with self.lock:
            self.cache.clear()
            self.expiration_queue.clear()
            self.current_size_bytes = 0
            
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do cache"""
        total_requests = self.hits + self.misses
        hit_rate = self.hits / total_requests if total_requests > 0 else 0
        
        return {
            "total_entries": len(self.cache),
            "size_mb": self.current_size_bytes / (1024 * 1024),
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "evictions": self.evictions,
            "avg_entry_size_kb": (self.current_size_bytes / len(self.cache) / 1024) 
                                if self.cache else 0
        }
        
    def cache_decorator(self, ttl: Optional[int] = None):
        """Decorador para cachear resultados de função"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Gera chave única para os argumentos
                key = f"{func.__name__}:{hashlib.md5(str((args, kwargs)).encode()).hexdigest()}"
                
                # Tenta obter do cache
                result = self.get(key)
                if result is not None:
                    return result
                    
                # Calcula resultado e cacheia
                result = func(*args, **kwargs)
                self.set(key, result, ttl)
                return result
                
            return wrapper
        return decorator
        

class BatchFileCache:
    """Cache otimizado para operações em lote de arquivos"""
    
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = cache_dir
        self.memory_cache = IntelligentCacheManager()
        
    def batch_read_files(self, file_paths: List[str]) -> Dict[str, Optional[str]]:
        """Lê múltiplos arquivos com cache"""
        results = {}
        files_to_read = []
        
        # Verifica cache primeiro
        for path in file_paths:
            cached = self.memory_cache.get(path)
            if cached is not None:
                results[path] = cached
            else:
                files_to_read.append(path)
                
        # Lê arquivos não cacheados
        if files_to_read:
            new_data = self._read_files_batch(files_to_read)
            self.memory_cache.batch_set(new_data)
            results.update(new_data)
            
        return results
        
    def _read_files_batch(self, paths: List[str]) -> Dict[str, str]:
        """Lê arquivos em lote"""
        results = {}
        for path in paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    results[path] = f.read()
            except Exception:
                results[path] = None
        return results
        
    def batch_write_files(self, file_data: Dict[str, str]) -> Dict[str, bool]:
        """Escreve múltiplos arquivos e atualiza cache"""
        results = {}
        
        for path, content in file_data.items():
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                # Atualiza cache
                self.memory_cache.set(path, content)
                results[path] = True
            except Exception:
                results[path] = False
                
        return results