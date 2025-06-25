#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulos do Curso de Python
"""

try:
    from .course_modules import CourseModules
    from .advanced_modules import AdvancedModules
except ImportError:
    # Fallback para quando executado diretamente
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from course_modules import CourseModules
    from advanced_modules import AdvancedModules

__all__ = ['CourseModules', 'AdvancedModules']