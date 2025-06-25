#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tratador de Interrupções
Gerencia interrupções por Ctrl+C de forma elegante
"""

import signal
import sys
from typing import Optional, Callable


class InterruptHandler:
    """Gerencia interrupções do sistema de forma elegante"""
    
    def __init__(self, cleanup_function: Optional[Callable] = None):
        self.cleanup_function = cleanup_function
        self.original_handler = None
        self.interrupted = False
    
    def __enter__(self):
        """Ativa o tratador de interrupções"""
        self.original_handler = signal.signal(signal.SIGINT, self._signal_handler)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restaura o tratador original"""
        if self.original_handler:
            signal.signal(signal.SIGINT, self.original_handler)
    
    def _signal_handler(self, signum, frame):
        """Trata o sinal SIGINT (Ctrl+C)"""
        self.interrupted = True
        
        if self.cleanup_function:
            try:
                self.cleanup_function()
            except Exception as e:
                print(f"⚠️ Erro durante limpeza: {e}")
        
        print("\n\n⚠️ Programa interrompido pelo usuário (Ctrl+C)")
        print("💾 Dados salvos com segurança.")
        print("🐍 Obrigado por usar o Curso de Python!")
        
        sys.exit(0)
    
    def check_interrupted(self) -> bool:
        """Verifica se houve interrupção"""
        return self.interrupted
    
    def reset(self) -> None:
        """Reseta o estado de interrupção"""
        self.interrupted = False


def safe_input(prompt: str = "", default: str = "") -> str:
    """
    Input seguro que trata Ctrl+C graciosamente
    Retorna string vazia se interrompido
    """
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n⚠️ Entrada cancelada")
        return default
    except EOFError:
        return default


def safe_pause(message: str = "\n🔸 Pressione ENTER para continuar...") -> None:
    """
    Pausa segura que trata Ctrl+C graciosamente
    """
    try:
        input(message)
    except KeyboardInterrupt:
        print("\n⚠️ Continuando...")
        pass
    except EOFError:
        pass