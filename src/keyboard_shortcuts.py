#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Atalhos de Teclado
Permite navegação rápida e ações através de teclas de atalho
"""

import sys
import os
from typing import Dict, Callable, Optional, Any

# Tenta importar bibliotecas para captura de teclas
try:
    if os.name == 'nt':  # Windows
        import msvcrt
    else:  # Unix-based
        import termios
        import tty
except ImportError:
    pass


class KeyboardShortcuts:
    """Gerencia atalhos de teclado do curso"""
    
    def __init__(self, config: Dict[str, str]):
        self.shortcuts = config
        self.actions: Dict[str, Callable] = {}
        self.enabled = True
        self.help_text = self._generate_help_text()
    
    def _generate_help_text(self) -> str:
        """Gera texto de ajuda para atalhos"""
        help_lines = ["⌨️  ATALHOS DE TECLADO:"]
        for action, key in self.shortcuts.items():
            readable_action = action.replace('_', ' ').title()
            help_lines.append(f"  [{key.upper()}] - {readable_action}")
        return '\n'.join(help_lines)
    
    def register_action(self, shortcut_name: str, action: Callable) -> None:
        """Registra uma ação para um atalho"""
        if shortcut_name in self.shortcuts:
            key = self.shortcuts[shortcut_name]
            self.actions[key.lower()] = action
    
    def get_key(self) -> Optional[str]:
        """Captura uma tecla pressionada de forma não-bloqueante"""
        try:
            if os.name == 'nt':  # Windows
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    # Converte bytes para string
                    return key.decode('utf-8', errors='ignore').lower()
            else:  # Unix-based
                # Configuração para leitura não-bloqueante
                old_settings = termios.tcgetattr(sys.stdin)
                try:
                    tty.setraw(sys.stdin.fileno())
                    sys.stdin.settimeout(0.1)
                    key = sys.stdin.read(1)
                    return key.lower()
                except:
                    return None
                finally:
                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        except:
            return None
        return None
    
    def wait_for_key(self) -> str:
        """Espera por uma tecla ser pressionada (bloqueante)"""
        if os.name == 'nt':  # Windows
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    return key.decode('utf-8', errors='ignore').lower()
        else:  # Unix-based
            old_settings = termios.tcgetattr(sys.stdin)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1)
                return key.lower()
            finally:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
    def process_shortcuts(self, context: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        Processa atalhos de teclado e executa ações
        Retorna a tecla pressionada ou None
        """
        if not self.enabled:
            return None
        
        key = self.get_key()
        if key and key in self.actions:
            # Executa a ação associada
            action = self.actions[key]
            if context:
                action(context)
            else:
                action()
            return key
        
        return key
    
    def show_help(self) -> None:
        """Exibe ajuda de atalhos disponíveis"""
        print("\n" + self.help_text)
    
    def toggle(self) -> None:
        """Ativa/desativa atalhos"""
        self.enabled = not self.enabled
        status = "ativados" if self.enabled else "desativados"
        print(f"\n⌨️  Atalhos {status}")
    
    def create_shortcut_bar(self) -> str:
        """Cria uma barra de status com atalhos principais"""
        # Atalhos principais atualizados para 2024
        main_shortcuts = [
            ("[0]", "Sair"),
            ("[H]", "Ajuda"),
            ("[P]", "Progresso"),
            ("[Q]", "Code Review"),
            ("[T]", "Temas")
        ]
        
        shortcuts_display = []
        for shortcut, label in main_shortcuts:
            shortcuts_display.append(f"{shortcut}{label}")
        
        return " | ".join(shortcuts_display)
    
    def is_quit_key(self, key: str) -> bool:
        """Verifica se a tecla é o atalho de sair"""
        quit_key = self.shortcuts.get('quit', 'q').lower()
        return key.lower() == quit_key
    
    def is_help_key(self, key: str) -> bool:
        """Verifica se a tecla é o atalho de ajuda"""
        help_key = self.shortcuts.get('help', 'h').lower()
        return key.lower() == help_key


class ShortcutManager:
    """Gerenciador de contexto para atalhos durante módulos"""
    
    def __init__(self, shortcuts: KeyboardShortcuts):
        self.shortcuts = shortcuts
        self.context = {}
    
    def __enter__(self):
        """Ativa monitoramento de atalhos"""
        self.shortcuts.enabled = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Desativa monitoramento de atalhos"""
        self.shortcuts.enabled = False
    
    def set_context(self, **kwargs) -> None:
        """Define contexto para as ações"""
        self.context.update(kwargs)
    
    def check_shortcuts(self) -> Optional[str]:
        """Verifica e processa atalhos"""
        return self.shortcuts.process_shortcuts(self.context)