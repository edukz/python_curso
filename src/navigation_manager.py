#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Navigation Manager - Gerencia navegação com breadcrumbs e botão voltar
"""

from typing import List, Tuple, Optional, Callable
from dataclasses import dataclass


@dataclass
class NavigationItem:
    """Representa um item na pilha de navegação"""
    name: str
    description: str
    level: int  # 0=main, 1=module, 2=submenu
    callback: Optional[Callable] = None


class NavigationManager:
    """Gerencia a navegação do curso com histórico"""
    
    def __init__(self):
        self.navigation_stack: List[NavigationItem] = []
        self.max_breadcrumb_length = 60
        
    def push(self, name: str, description: str = "", level: int = 0, callback: Optional[Callable] = None) -> None:
        """Adiciona item à pilha de navegação"""
        item = NavigationItem(name, description, level, callback)
        self.navigation_stack.append(item)
        
    def pop(self) -> Optional[NavigationItem]:
        """Remove e retorna último item da pilha"""
        if len(self.navigation_stack) > 0:
            return self.navigation_stack.pop()
        return None
        
    def clear(self) -> None:
        """Limpa toda a pilha de navegação"""
        self.navigation_stack.clear()
        
    def get_breadcrumbs(self, ascii_mode: bool = False) -> str:
        """Retorna string de breadcrumbs formatada"""
        if not self.navigation_stack:
            return ""
            
        separator = " > " if ascii_mode else " ▸ "
        home = "Menu Principal" if ascii_mode else "🏠 Menu Principal"
        
        parts = [home]
        for item in self.navigation_stack:
            if item.name:
                parts.append(item.name)
                
        breadcrumb = separator.join(parts)
        
        # Trunca se muito longo
        if len(breadcrumb) > self.max_breadcrumb_length:
            breadcrumb = "..." + breadcrumb[-(self.max_breadcrumb_length-3):]
            
        return breadcrumb
        
    def can_go_back(self) -> bool:
        """Verifica se pode voltar"""
        return len(self.navigation_stack) > 0
        
    def get_current_level(self) -> int:
        """Retorna nível atual de navegação"""
        if self.navigation_stack:
            return self.navigation_stack[-1].level
        return 0
        
    def get_back_option(self, ascii_mode: bool = False) -> str:
        """Retorna string formatada da opção voltar"""
        if not self.can_go_back():
            return ""
            
        if ascii_mode:
            return "B. <- Voltar"
        else:
            return "B. ↩️ Voltar"
            
    def execute_back(self) -> Optional[Callable]:
        """Executa ação de voltar e retorna callback se houver"""
        item = self.pop()
        if item and item.callback:
            return item.callback
        return None