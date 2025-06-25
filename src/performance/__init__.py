#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo de Performance
Otimizações de cache e lazy loading
"""

from .cache_manager import CacheManager, LazyLoader, FileCache, cached

__all__ = ['CacheManager', 'LazyLoader', 'FileCache', 'cached']