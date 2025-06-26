#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulos do Curso de Python - Sistema Modular Independente
"""

# O sistema agora usa carregamento dinâmico via module_loader
# As classes legadas foram removidas para tornar o sistema 100% independente

from .module_loader import module_loader, load_module

__all__ = ['module_loader', 'load_module']