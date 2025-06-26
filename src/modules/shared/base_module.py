#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Classe Base para Módulos do Curso
Fornece funcionalidades comuns para todos os módulos
"""

import os
import time
from typing import Optional, Dict, Any, Union, List
from abc import ABC, abstractmethod

try:
    from ...utils import PythonCourseUtils
    from ...ui_components import UIComponents
    from ...progress_manager import ProgressManager
except ImportError:
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from utils import PythonCourseUtils
    from ui_components import UIComponents
    from progress_manager import ProgressManager


class BaseModule(ABC):
    """Classe base para todos os módulos do curso"""
    
    def __init__(self, module_id: str, module_name: str):
        """
        Inicializa o módulo base
        
        Args:
            module_id: ID do módulo (ex: "modulo_01")
            module_name: Nome do módulo (ex: "Introdução ao Python")
        """
        self.module_id = module_id
        self.module_name = module_name
        self.utils = PythonCourseUtils()
        self.ui: Optional[UIComponents] = None
        self.progress: Optional[ProgressManager] = None
        
        # Configurações do módulo
        self.has_mini_project = False
        self.mini_project_points = 50
        self.completion_points = 100
        
    def set_dependencies(self, ui: UIComponents, progress: ProgressManager):
        """Define dependências necessárias"""
        self.ui = ui
        self.progress = progress
        
        # Conecta utils aos gerenciadores
        if hasattr(self.utils, 'set_managers'):
            self.utils.set_managers(progress, None)
    
    @abstractmethod
    def execute(self) -> None:
        """
        Executa o módulo principal
        Deve ser implementado por cada módulo específico
        """
        pass
    
    def show_menu(self, options: Dict[str, str], title: str = None) -> str:
        """
        Exibe menu padrão e retorna escolha do usuário
        
        Args:
            options: Dicionário com opções {key: description}
            title: Título do menu (opcional)
            
        Returns:
            Escolha do usuário
        """
        if not self.ui:
            raise RuntimeError("UI components não foram configurados")
            
        self.ui.clear_screen()
        
        if title:
            self.ui.header(title)
        else:
            self.ui.header(f"📚 {self.module_name.upper()}")
        
        print("Escolha uma opção:")
        for key, description in options.items():
            if key == "0":
                print(f"\n{key}. {description}")
            else:
                print(f"{key}. {description}")
        
        return input("\n👉 Sua escolha: ").strip()
    
    def complete_module(self, points: int = None) -> None:
        """
        Marca o módulo como completo
        
        Args:
            points: Pontos a serem atribuídos (padrão: self.completion_points)
        """
        if points is None:
            points = self.completion_points
            
        if self.utils and hasattr(self.utils, 'complete_module'):
            self.utils.complete_module(self.module_id, points)
        elif self.progress:
            self.progress.complete_module(self.module_id, points)
        else:
            print(f"\n🎉 MÓDULO {self.module_id.upper()} CONCLUÍDO!")
            print(f"⭐ Pontos ganhos: {points}")
    
    def complete_mini_project(self, project_name: str, points: int = None) -> None:
        """
        Marca mini projeto como completo
        
        Args:
            project_name: Nome do mini projeto
            points: Pontos a serem atribuídos (padrão: self.mini_project_points)
        """
        if points is None:
            points = self.mini_project_points
            
        if self.utils and hasattr(self.utils, 'mini_projeto_completo'):
            self.utils.mini_projeto_completo(self.module_id, project_name, points)
        else:
            print(f"\n🎉 MINI PROJETO CONCLUÍDO!")
            print(f"📚 Módulo: {self.module_id}")
            print(f"🚀 Projeto: {project_name}")
            print(f"⭐ Pontos ganhos: {points}")
    
    def pausar(self) -> None:
        """Pausa a execução e espera o usuário"""
        if self.utils:
            self.utils.pausar()
        else:
            input("\n🔸 Pressione ENTER para continuar...")
    
    def print_colored(self, text: str, color: str = "primary") -> None:
        """Imprime texto com cor se UI estiver disponível"""
        if self.ui:
            color_code = self.ui.get_color(color)
            reset = self.ui.get_color("reset")
            print(f"{color_code}{text}{reset}")
        else:
            print(text)
    
    def print_section(self, title: str, emoji: str = "📌", color: str = "accent") -> None:
        """Imprime uma seção destacada"""
        if self.ui:
            color_code = self.ui.get_color(color)
            reset = self.ui.get_color("reset")
            separator = "─" * 50
            print(f"\n{color_code}{separator}{reset}")
            print(f"{color_code}{emoji} {title.upper()}{reset}")
            print(f"{color_code}{separator}{reset}")
        else:
            print(f"\n{emoji} {title.upper()}")
            print("─" * 50)
    
    def exemplo(self, codigo: str) -> None:
        """Exibe um exemplo de código"""
        if self.utils:
            self.utils.exemplo(codigo)
        else:
            print("\n📝 EXEMPLO:")
            print("-" * 40)
            print(codigo)
            print("-" * 40)
    
    def executar_codigo(self, codigo: str) -> None:
        """Executa um código de exemplo"""
        if self.utils:
            self.utils.executar_codigo(codigo)
        else:
            print("\n▶️  EXECUTANDO:")
            print("-" * 40)
            try:
                exec(codigo)
            except Exception as e:
                print(f"❌ Erro: {e}")
            print("-" * 40)
    
    def exercicio(self, descricao: str, resposta_esperada: Union[str, List[str]], dica: str = "") -> bool:
        """Propõe um exercício ao aluno"""
        if self.utils:
            return self.utils.exercicio(descricao, resposta_esperada, dica)
        else:
            print(f"\n🎯 EXERCÍCIO: {descricao}")
            if dica:
                print(f"💡 Dica: {dica}")
            
            resposta = input("\n👉 Sua resposta: ").strip()
            
            if isinstance(resposta_esperada, str):
                respostas_validas = [resposta_esperada]
            else:
                respostas_validas = resposta_esperada
            
            correto = any(resposta.lower() == resp.lower() for resp in respostas_validas)
            
            if correto:
                print("✅ Correto! Muito bem!")
                return True
            else:
                print("❌ Resposta incorreta!")
                if len(respostas_validas) == 1:
                    print(f"💡 A resposta correta era: {respostas_validas[0]}")
                else:
                    print(f"💡 Respostas possíveis: {', '.join(respostas_validas)}")
                return False
    
    def error_handler(self, func, *args, **kwargs):
        """Executa função com tratamento de erro padrão"""
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n\n⚠️ Operação interrompida pelo usuário")
            return False
        except Exception as e:
            if self.ui:
                self.ui.error(f"Erro no módulo {self.module_id}: {str(e)}")
            else:
                print(f"❌ Erro no módulo {self.module_id}: {str(e)}")
            return False
    
    def __str__(self) -> str:
        return f"{self.module_id}: {self.module_name}"
    
    def __repr__(self) -> str:
        return f"BaseModule(id='{self.module_id}', name='{self.module_name}')"
    
    @property
    def name(self) -> str:
        """Propriedade para acessar o nome do módulo (compatibilidade)"""
        return self.module_name