#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerenciador de Configurações
Carrega e gerencia configurações do arquivo settings.json
"""

import json
import os
from typing import Dict, Any, Optional
from .performance import CacheManager, cached


class ConfigManager:
    """Gerencia as configurações do curso"""
    
    def __init__(self, config_file: str = "data/settings.json"):
        self.config_file = config_file
        self._cache = CacheManager(max_size=100, default_ttl=300)  # Cache por 5 minutos
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Carrega as configurações do arquivo JSON"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Erro ao carregar configurações: {e}")
                return self._get_default_config()
        else:
            # Cria arquivo de configuração padrão se não existir
            default_config = self._get_default_config()
            self._save_config(default_config)
            return default_config
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Retorna configurações padrão"""
        return {
            "course": {
                "name": "Curso Interativo de Python",
                "version": "2.0",
                "author": "Sistema de Ensino Python",
                "language": "pt-BR"
            },
            "display": {
                "use_colors": True,
                "use_emojis": True,
                "ascii_mode": False,
                "animation_speed": 0.03,
                "clear_screen_between_modules": True,
                "show_hints_delay": 3
            },
            "scoring": {
                "points_per_correct_answer": 10,
                "points_per_module_completion": 100,
                "bonus_streak_3": 20,
                "bonus_streak_5": 50,
                "bonus_streak_10": 100,
                "max_score": 2000
            },
            "features": {
                "save_progress": True,
                "show_module_timer": True,
                "enable_achievements": True,
                "enable_review_mode": True,
                "enable_glossary": True,
                "enable_shortcuts": True,
                "enable_certificate": True
            },
            "paths": {
                "progress_file": "progress.json",
                "log_file": "course.log",
                "certificate_template": "certificate_template.html",
                "glossary_file": "glossary.json"
            },
            "keyboard_shortcuts": {
                "next_module": "n",
                "previous_module": "p",
                "repeat_module": "r",
                "show_progress": "s",
                "toggle_hints": "h",
                "quit": "q"
            },
            "logging": {
                "enabled": True,
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "max_file_size_mb": 10
            },
            "modules": {
                "time_limit_minutes": 30,
                "min_score_to_pass": 70,
                "allow_skip": False,
                "show_solutions": True
            }
        }
    
    def _save_config(self, config: Dict[str, Any]) -> None:
        """Salva as configurações no arquivo JSON"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Erro ao salvar configurações: {e}")
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Obtém um valor de configuração usando notação de ponto
        Exemplo: config.get('display.use_colors')
        """
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any) -> None:
        """
        Define um valor de configuração usando notação de ponto
        Exemplo: config.set('display.use_colors', False)
        """
        keys = key_path.split('.')
        config = self.config
        
        # Navega até o penúltimo nível
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        # Define o valor
        config[keys[-1]] = value
        self._save_config(self.config)
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """Obtém uma seção inteira de configuração"""
        return self.config.get(section, {})
    
    def reload(self) -> None:
        """Recarrega as configurações do arquivo"""
        self.config = self._load_config()
    
    def reset_to_defaults(self) -> None:
        """Reseta as configurações para os valores padrão"""
        self.config = self._get_default_config()
        self._save_config(self.config)