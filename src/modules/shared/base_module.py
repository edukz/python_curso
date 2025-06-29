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
    
    def print_concept(self, concept: str, description: str, emoji: str = "💡") -> None:
        """Imprime um conceito importante com destaque colorido"""
        if self.ui:
            concept_color = self.ui.get_color("warning")  # Amarelo para conceitos
            desc_color = self.ui.get_color("text")
            reset = self.ui.get_color("reset")
            print(f"\n{concept_color}{emoji} {concept}:{reset}")
            print(f"{desc_color}{description}{reset}")
        else:
            print(f"\n{emoji} {concept}:")
            print(description)
    
    def print_tip(self, tip: str, emoji: str = "💫") -> None:
        """Imprime uma dica com cor especial"""
        if self.ui:
            tip_color = self.ui.get_color("info")  # Azul/Ciano para dicas
            reset = self.ui.get_color("reset")
            print(f"\n{tip_color}{emoji} DICA: {tip}{reset}")
        else:
            print(f"\n{emoji} DICA: {tip}")
    
    def print_warning(self, warning: str, emoji: str = "⚠️") -> None:
        """Imprime um aviso importante"""
        if self.ui:
            warning_color = self.ui.get_color("error")  # Vermelho para avisos
            reset = self.ui.get_color("reset")
            print(f"\n{warning_color}{emoji} ATENÇÃO: {warning}{reset}")
        else:
            print(f"\n{emoji} ATENÇÃO: {warning}")
    
    def print_success(self, message: str, emoji: str = "✅") -> None:
        """Imprime mensagem de sucesso"""
        if self.ui:
            success_color = self.ui.get_color("success")  # Verde para sucesso
            reset = self.ui.get_color("reset")
            print(f"\n{success_color}{emoji} {message}{reset}")
        else:
            print(f"\n{emoji} {message}")
    
    def print_code_section(self, title: str, code: str) -> None:
        """Imprime uma seção de código com cores simples"""
        if self.ui:
            title_color = self.ui.get_color("accent")
            code_color = self.ui.get_color("primary")
            reset = self.ui.get_color("reset")
            print(f"\n{title_color}{'═' * 50}{reset}")
            print(f"{title_color}📝 {title.upper()}{reset}")
            print(f"{title_color}{'═' * 50}{reset}")
            print(f"{code_color}{code}{reset}")
            print(f"{title_color}{'═' * 50}{reset}")
        else:
            print(f"\n📝 {title.upper()}")
            print("═" * 50)
            print(code)
            print("═" * 50)
    
    def exemplo(self, codigo: str) -> None:
        """Exibe um exemplo de código com cores"""
        self.print_code_section("EXEMPLO", codigo)
    
    def executar_codigo(self, codigo: str) -> None:
        """Executa um código de exemplo com output colorido"""
        if self.ui:
            exec_color = self.ui.get_color("success")
            output_color = self.ui.get_color("info")
            error_color = self.ui.get_color("error")
            reset = self.ui.get_color("reset")
            
            print(f"\n{exec_color}{'▶' * 25}{reset}")
            print(f"{exec_color}▶️  EXECUTANDO CÓDIGO:{reset}")
            print(f"{exec_color}{'▶' * 25}{reset}")
            
            # Mostra o código com cores simples
            code_color = self.ui.get_color("primary")
            print(f"{code_color}{codigo}{reset}")
            
            print(f"\n{output_color}{'─' * 25} OUTPUT {'─' * 25}{reset}")
            
            try:
                # Captura o output
                import io
                import sys
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                
                exec(codigo)
                
                output = buffer.getvalue()
                sys.stdout = old_stdout
                
                if output:
                    print(f"{output_color}{output}{reset}", end='')
                    
                print(f"{output_color}{'─' * 58}{reset}")
                
            except Exception as e:
                sys.stdout = old_stdout
                print(f"{error_color}❌ Erro: {e}{reset}")
                print(f"{error_color}{'─' * 58}{reset}")
                
        else:
            # Fallback sem cores
            print("\n▶️  EXECUTANDO:")
            print("-" * 40)
            try:
                exec(codigo)
            except Exception as e:
                print(f"❌ Erro: {e}")
            print("-" * 40)
    
    def exercicio(self, descricao: str, resposta_esperada: Union[str, List[str]], dica: str = "") -> bool:
        """Propõe um exercício ao aluno com feedback colorido"""
        if self.ui:
            # Cores para exercícios
            question_color = self.ui.get_color("accent")
            hint_color = self.ui.get_color("info")
            input_color = self.ui.get_color("warning")
            success_color = self.ui.get_color("success")
            error_color = self.ui.get_color("error")
            reset = self.ui.get_color("reset")
            
            # Cabeçalho do exercício
            print(f"\n{question_color}{'🎯' * 25}{reset}")
            print(f"{question_color}🎯 EXERCÍCIO:{reset}")
            print(f"{question_color}{descricao}{reset}")
            
            if dica:
                print(f"\n{hint_color}💡 Dica: {dica}{reset}")
            
            print(f"{question_color}{'🎯' * 25}{reset}")
            
            # Input colorido
            resposta = input(f"\n{input_color}👉 Sua resposta: {reset}").strip()
            
            if isinstance(resposta_esperada, str):
                respostas_validas = [resposta_esperada]
            else:
                respostas_validas = resposta_esperada
            
            correto = any(resposta.lower() == resp.lower() for resp in respostas_validas)
            
            if correto:
                print(f"\n{success_color}{'✅' * 25}{reset}")
                print(f"{success_color}✅ PARABÉNS! Resposta correta!{reset}")
                print(f"{success_color}🌟 Excelente trabalho!{reset}")
                print(f"{success_color}{'✅' * 25}{reset}")
                
                # Adiciona pontos se utils estiver disponível
                if self.utils and hasattr(self.utils, 'adicionar_pontos'):
                    self.utils.adicionar_pontos(10, "Resposta correta no quiz")
                # Não faz nada se não houver sistema de pontos - é opcional
                    
                return True
            else:
                print(f"\n{error_color}{'❌' * 25}{reset}")
                print(f"{error_color}❌ Ops! Resposta incorreta.{reset}")
                
                if len(respostas_validas) == 1:
                    print(f"{hint_color}💡 A resposta correta era: {respostas_validas[0]}{reset}")
                else:
                    print(f"{hint_color}💡 Respostas possíveis: {', '.join(respostas_validas)}{reset}")
                    
                print(f"{error_color}{'❌' * 25}{reset}")
                print(f"\n{hint_color}💪 Não desista! Tente novamente!{reset}")
                
                return False
        else:
            # Fallback sem UI
            return self.utils.exercicio(descricao, resposta_esperada, dica) if self.utils else False
    
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
    
    def interactive_practice_section(self, title: str, exercises: List[Dict[str, Any]]) -> None:
        """Cria uma seção de prática interativa completa"""
        if self.ui:
            practice_color = self.ui.get_color("success")
            menu_color = self.ui.get_color("accent")
            reset = self.ui.get_color("reset")
            
            print(f"\n{practice_color}{'✨' * 30}{reset}")
            print(f"{practice_color}🎯 {title.upper()}{reset}")
            print(f"{practice_color}{'✨' * 30}{reset}")
            print(f"\n{menu_color}Escolha um exercício para praticar:{reset}")
            
            # Mostrar menu de exercícios
            for i, exercise in enumerate(exercises, 1):
                status = "✅" if exercise.get('completed', False) else "⏳"
                print(f"{status} {i}. {exercise['title']}")
            
            print(f"\n{menu_color}0. Voltar ao conteúdo{reset}")
            print(f"{menu_color}{'─' * 40}{reset}")
            
            while True:
                choice = input(f"\n{menu_color}👉 Escolha (1-{len(exercises)} ou 0): {reset}").strip()
                
                if choice == "0":
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(exercises):
                    idx = int(choice) - 1
                    self._run_practice_exercise(exercises[idx])
                    exercises[idx]['completed'] = True
                else:
                    print(f"{self.ui.get_color('error')}❌ Opção inválida!{reset}")
        else:
            # Fallback sem cores
            print(f"\n{'✨' * 30}")
            print(f"🎯 {title.upper()}")
            print(f"{'✨' * 30}")
            self._run_practice_exercises_simple(exercises)
    
    def _run_practice_exercise(self, exercise: Dict[str, Any]) -> None:
        """Executa um exercício prático individual"""
        if self.ui:
            self.ui.clear_screen()
            title_color = self.ui.get_color("warning")
            code_color = self.ui.get_color("primary")
            reset = self.ui.get_color("reset")
            
            print(f"{title_color}🏋️ EXERCÍCIO: {exercise['title']}{reset}")
            print(f"{title_color}{'═' * 50}{reset}")
            print(f"\n{exercise['description']}")
            
            if 'starter_code' in exercise:
                print(f"\n{code_color}💻 CÓDIGO INICIAL:{reset}")
                print(f"{code_color}{exercise['starter_code']}{reset}")
            
            print(f"\n{title_color}📝 SUA TAREFA:{reset}")
            print(exercise['task'])
            
            if 'hints' in exercise:
                show_hint = input("\n💡 Deseja ver uma dica? (s/n): ").lower()
                if show_hint == 's':
                    print(f"\n{self.ui.get_color('info')}💡 DICA: {exercise['hints']}{reset}")
            
            # Área para o aluno escrever código
            print(f"\n{title_color}✍️ ESCREVA SEU CÓDIGO:{reset}")
            print("(Digite 'fim' em uma linha vazia para terminar)")
            
            user_code = []
            while True:
                line = input()
                if line.lower() == 'fim':
                    break
                user_code.append(line)
            
            # Executar código do aluno
            code_to_run = '\n'.join(user_code)
            if code_to_run.strip():
                print(f"\n{title_color}🚀 EXECUTANDO SEU CÓDIGO:{reset}")
                try:
                    exec(code_to_run)
                    self.print_success("\n✅ Código executado com sucesso!")
                except Exception as e:
                    self.print_warning(f"\n❌ Erro: {e}")
            
            # Mostrar solução
            show_solution = input("\n🔍 Deseja ver a solução? (s/n): ").lower()
            if show_solution == 's':
                print(f"\n{code_color}💡 SOLUÇÃO:{reset}")
                print(f"{code_color}{exercise['solution']}{reset}")
                print(f"\n{self.ui.get_color('info')}📖 EXPLICAÇÃO:{reset}")
                print(exercise['explanation'])
            
            input("\n🔸 Pressione ENTER para continuar...")