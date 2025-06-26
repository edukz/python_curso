#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module Loader - Sistema de carregamento lazy para módulos
"""

import importlib
import sys
from typing import Dict, Any, Optional, Callable
from functools import wraps
import time


class LazyModuleLoader:
    """Carrega módulos sob demanda para melhor performance"""
    
    def __init__(self):
        self._loaded_modules: Dict[str, Any] = {}
        self._module_paths: Dict[str, str] = {
            # Controladores
            "MenuManager": "src.controllers.menu_manager",
            "CourseController": "src.controllers.course_controller",
            "SessionManager": "src.controllers.session_manager",
            
            # Sistemas
            "ProgressManager": "src.progress_manager",
            "VisualFeedback": "src.visual_feedback",
            "ReviewMode": "src.review_mode",
            "Glossary": "src.glossary",
            "CertificateGenerator": "src.certificate_generator",
            
            # Recursos avançados
            "InteractiveDemoSession": "src.interactive_demos",
            "AdaptiveExerciseGenerator": "src.adaptive_exercises",
            "AdaptiveExerciseSession": "src.adaptive_exercises",
            "DebugSession": "src.visual_debugger",
            "TutorAssistant": "src.tutor_assistant",
            "LearningAnalytics": "src.learning_analytics",
            "GamificationSystem": "src.gamification_system",
            "CodePlayground": "src.code_editor",
            
            # Infraestrutura
            "SyncManager": "src.sync_manager",
            "ErrorTracker": "src.error_tracker",
            "ErrorHandler": "src.error_handler",
            "SecureInput": "src.security",
            "CourseLogger": "src.logger",
            
            # Utilitários
            "PythonCourseUtils": "src.utils"
        }
        
        self._load_times: Dict[str, float] = {}
        
    def get_module(self, module_name: str) -> Any:
        """Carrega e retorna um módulo sob demanda"""
        if module_name in self._loaded_modules:
            return self._loaded_modules[module_name]
            
        if module_name not in self._module_paths:
            raise ValueError(f"Módulo '{module_name}' não configurado para lazy loading")
            
        start_time = time.time()
        
        # Importa o módulo
        module_path = self._module_paths[module_name]
        module = importlib.import_module(module_path)
        
        # Obtém a classe/função do módulo
        if hasattr(module, module_name):
            module_class = getattr(module, module_name)
        else:
            # Tenta encontrar a classe principal do módulo
            module_class = self._find_main_class(module, module_name)
            
        self._loaded_modules[module_name] = module_class
        self._load_times[module_name] = time.time() - start_time
        
        return module_class
        
    def _find_main_class(self, module: Any, expected_name: str) -> Any:
        """Tenta encontrar a classe principal em um módulo"""
        # Lista todos os atributos do módulo
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            # Verifica se é uma classe e tem nome similar
            if isinstance(attr, type) and expected_name.lower() in attr_name.lower():
                return attr
                
        # Se não encontrar, retorna o módulo inteiro
        return module
        
    def preload_essentials(self) -> None:
        """Pré-carrega módulos essenciais para início rápido"""
        essentials = [
            "MenuManager",
            "CourseController", 
            "SessionManager",
            "ProgressManager",
            "UIComponents"
        ]
        
        for module_name in essentials:
            if module_name in self._module_paths:
                self.get_module(module_name)
                
    def get_load_stats(self) -> Dict[str, float]:
        """Retorna estatísticas de carregamento"""
        return {
            "total_modules": len(self._loaded_modules),
            "total_time": sum(self._load_times.values()),
            "average_time": sum(self._load_times.values()) / len(self._load_times) if self._load_times else 0,
            "modules": self._load_times
        }
        
    def lazy_property(self, module_name: str):
        """Decorador para criar propriedades lazy"""
        def decorator(func):
            attr_name = f"_lazy_{func.__name__}"
            
            @wraps(func)
            def wrapper(self):
                if not hasattr(self, attr_name):
                    module_class = self.get_module(module_name)
                    setattr(self, attr_name, module_class())
                return getattr(self, attr_name)
                
            return property(wrapper)
        return decorator


# Instância global do loader
module_loader = LazyModuleLoader()


def lazy_import(module_name: str) -> Callable:
    """Função helper para importação lazy"""
    def get_module():
        return module_loader.get_module(module_name)
    return get_module