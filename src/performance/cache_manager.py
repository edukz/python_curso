#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Cache e Otimização de Performance
Implementa cache em memória com TTL e lazy loading
"""

import time
import json
import pickle
from typing import Any, Optional, Dict, Callable, Union
from functools import wraps
from collections import OrderedDict
import hashlib


class CacheManager:
    """Gerenciador de cache com suporte a TTL e limite de tamanho"""
    
    def __init__(self, max_size: int = 1000, default_ttl: int = 3600):
        """
        Inicializa o gerenciador de cache
        
        Args:
            max_size: Número máximo de itens no cache
            default_ttl: Tempo de vida padrão em segundos
        """
        self.cache: OrderedDict[str, Dict[str, Any]] = OrderedDict()
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.hits = 0
        self.misses = 0
    
    def _generate_key(self, *args, **kwargs) -> str:
        """Gera chave única para os argumentos"""
        key_data = str(args) + str(sorted(kwargs.items()))
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Any]:
        """
        Obtém valor do cache
        
        Args:
            key: Chave do cache
            
        Returns:
            Valor se encontrado e válido, None caso contrário
        """
        if key not in self.cache:
            self.misses += 1
            return None
        
        entry = self.cache[key]
        
        # Verifica TTL
        if entry['expires_at'] and time.time() > entry['expires_at']:
            self.invalidate(key)
            self.misses += 1
            return None
        
        # Move para o final (LRU)
        self.cache.move_to_end(key)
        self.hits += 1
        
        return entry['value']
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Armazena valor no cache
        
        Args:
            key: Chave do cache
            value: Valor a armazenar
            ttl: Tempo de vida em segundos
        """
        # Remove item mais antigo se necessário
        if len(self.cache) >= self.max_size and key not in self.cache:
            self.cache.popitem(last=False)
        
        expires_at = None
        if ttl is not None or self.default_ttl:
            expires_at = time.time() + (ttl or self.default_ttl)
        
        self.cache[key] = {
            'value': value,
            'expires_at': expires_at,
            'created_at': time.time()
        }
    
    def invalidate(self, key: str) -> bool:
        """Remove item do cache"""
        if key in self.cache:
            del self.cache[key]
            return True
        return False
    
    def clear(self) -> None:
        """Limpa todo o cache"""
        self.cache.clear()
        self.hits = 0
        self.misses = 0
    
    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do cache"""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            'size': len(self.cache),
            'max_size': self.max_size,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate,
            'total_requests': total_requests
        }
    
    def cleanup_expired(self) -> int:
        """Remove entradas expiradas"""
        current_time = time.time()
        expired_keys = [
            key for key, entry in self.cache.items()
            if entry['expires_at'] and current_time > entry['expires_at']
        ]
        
        for key in expired_keys:
            self.invalidate(key)
        
        return len(expired_keys)


def cached(cache_manager: Optional[CacheManager] = None, 
          ttl: Optional[int] = None,
          key_prefix: str = ""):
    """
    Decorator para cache de funções
    
    Args:
        cache_manager: Instância do CacheManager
        ttl: Tempo de vida do cache
        key_prefix: Prefixo para a chave do cache
    """
    def decorator(func):
        # Cria cache manager local se não fornecido
        local_cache = cache_manager or CacheManager()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Gera chave do cache
            cache_key = f"{key_prefix}{func.__name__}_{local_cache._generate_key(*args, **kwargs)}"
            
            # Tenta obter do cache
            cached_value = local_cache.get(cache_key)
            if cached_value is not None:
                return cached_value
            
            # Executa função e armazena resultado
            result = func(*args, **kwargs)
            local_cache.set(cache_key, result, ttl)
            
            return result
        
        # Adiciona métodos úteis
        wrapper.cache_clear = lambda: local_cache.clear()
        wrapper.cache_stats = lambda: local_cache.get_stats()
        wrapper.cache_invalidate = lambda *args, **kwargs: local_cache.invalidate(
            f"{key_prefix}{func.__name__}_{local_cache._generate_key(*args, **kwargs)}"
        )
        
        return wrapper
    return decorator


class LazyLoader:
    """Implementa carregamento lazy de recursos"""
    
    def __init__(self):
        self._loaders: Dict[str, Callable] = {}
        self._loaded: Dict[str, Any] = {}
        self._loading: Dict[str, bool] = {}
    
    def register(self, name: str, loader: Callable) -> None:
        """
        Registra um loader para um recurso
        
        Args:
            name: Nome do recurso
            loader: Função que carrega o recurso
        """
        self._loaders[name] = loader
    
    def get(self, name: str) -> Any:
        """
        Obtém um recurso, carregando se necessário
        
        Args:
            name: Nome do recurso
            
        Returns:
            Recurso carregado
        """
        # Se já carregado, retorna
        if name in self._loaded:
            return self._loaded[name]
        
        # Evita carregamento duplicado
        if self._loading.get(name):
            raise RuntimeError(f"Carregamento circular detectado para {name}")
        
        # Carrega recurso
        if name not in self._loaders:
            raise KeyError(f"Loader não registrado para {name}")
        
        self._loading[name] = True
        try:
            self._loaded[name] = self._loaders[name]()
            return self._loaded[name]
        finally:
            self._loading[name] = False
    
    def is_loaded(self, name: str) -> bool:
        """Verifica se recurso já foi carregado"""
        return name in self._loaded
    
    def unload(self, name: str) -> bool:
        """Descarrega um recurso da memória"""
        if name in self._loaded:
            del self._loaded[name]
            return True
        return False
    
    def preload(self, names: list) -> Dict[str, bool]:
        """Pré-carrega múltiplos recursos"""
        results = {}
        for name in names:
            try:
                self.get(name)
                results[name] = True
            except Exception:
                results[name] = False
        return results


class FileCache:
    """Cache persistente em arquivo"""
    
    def __init__(self, cache_dir: str = "cache", format: str = "json"):
        """
        Inicializa cache em arquivo
        
        Args:
            cache_dir: Diretório para arquivos de cache
            format: Formato de serialização (json ou pickle)
        """
        self.cache_dir = cache_dir
        self.format = format
        
        # Cria diretório se não existir
        import os
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_path(self, key: str) -> str:
        """Gera caminho do arquivo de cache"""
        import os
        safe_key = key.replace('/', '_').replace('\\', '_')
        extension = 'json' if self.format == 'json' else 'pkl'
        return os.path.join(self.cache_dir, f"{safe_key}.{extension}")
    
    def get(self, key: str) -> Optional[Any]:
        """Obtém valor do cache em arquivo"""
        import os
        
        cache_path = self._get_cache_path(key)
        if not os.path.exists(cache_path):
            return None
        
        try:
            # Verifica idade do arquivo
            if hasattr(self, 'ttl'):
                age = time.time() - os.path.getmtime(cache_path)
                if age > self.ttl:
                    os.remove(cache_path)
                    return None
            
            # Carrega dados
            with open(cache_path, 'rb' if self.format == 'pickle' else 'r') as f:
                if self.format == 'json':
                    return json.load(f)
                else:
                    return pickle.load(f)
                    
        except Exception:
            return None
    
    def set(self, key: str, value: Any) -> bool:
        """Armazena valor no cache em arquivo"""
        try:
            cache_path = self._get_cache_path(key)
            
            with open(cache_path, 'wb' if self.format == 'pickle' else 'w') as f:
                if self.format == 'json':
                    json.dump(value, f, indent=2)
                else:
                    pickle.dump(value, f)
            
            return True
            
        except Exception:
            return False
    
    def invalidate(self, key: str) -> bool:
        """Remove arquivo de cache"""
        import os
        
        cache_path = self._get_cache_path(key)
        if os.path.exists(cache_path):
            try:
                os.remove(cache_path)
                return True
            except:
                pass
        return False
    
    def clear(self) -> int:
        """Limpa todos os arquivos de cache"""
        import os
        import glob
        
        pattern = os.path.join(self.cache_dir, f"*.{self.format}")
        files = glob.glob(pattern)
        
        removed = 0
        for file in files:
            try:
                os.remove(file)
                removed += 1
            except:
                pass
        
        return removed