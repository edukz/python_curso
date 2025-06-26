#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerenciador de Menus
Responsável por exibir e gerenciar todos os menus do sistema
"""

from typing import Dict, List, Optional, Tuple, Any
from ..ui_components import UIComponents
from ..progress_manager import ProgressManager
from ..keyboard_shortcuts import KeyboardShortcuts
from ..navigation_manager import NavigationManager


class MenuManager:
    """Gerencia todos os menus do sistema"""
    
    def __init__(self, ui: UIComponents, progress: ProgressManager, 
                 shortcuts: KeyboardShortcuts):
        self.ui = ui
        self.progress = progress
        self.shortcuts = shortcuts
        self.navigation = NavigationManager()
        self.ascii_mode = False  # Será configurável depois
    
    def display_main_menu(self, menu_options: Dict[str, Tuple[Any, str]]) -> None:
        """Exibe o menu principal do curso"""
        # Calcula estatísticas
        total_modules = 35
        completed_modules = len([
            m for m in self.progress.progress_data["modules_completed"]
            if m.startswith("modulo_") and m.replace("modulo_", "").isdigit()
            and int(m.replace("modulo_", "")) <= 35
        ])
        
        # Obtém informações do progresso
        user_name = self.progress.progress_data.get("user_name", "Aluno")
        completion_percentage = self.progress.get_completion_percentage()
        
        # Exibe breadcrumbs se houver
        breadcrumbs = self.navigation.get_breadcrumbs(self.ascii_mode)
        if breadcrumbs:
            print(f"\n📍 {breadcrumbs}\n")
        
        # Exibe cabeçalho
        self.ui.header(
            "🐍 CURSO INTERATIVO DE PYTHON 2.0 🐍",
            f"Bem-vindo(a), {user_name}! | Progresso: {completion_percentage:.1f}% | Módulos: {completed_modules}/{total_modules}"
        )
        
        # Prepara opções de módulos
        module_options = self._prepare_module_options(menu_options)
        
        # Exibe seções de módulos
        self._display_module_sections(module_options)
        
        # Exibe recursos especiais
        self._display_special_features()
        
        # Exibe opções do sistema
        self._display_system_options()
        
        # Exibe opção voltar se disponível
        if self.navigation.can_go_back():
            print(f"\n{self.navigation.get_back_option(self.ascii_mode)}")
        
        # Exibe barra de atalhos
        print(f"⌨️  {self.shortcuts.create_shortcut_bar()}")
        print()
    
    def _prepare_module_options(self, menu_options: Dict[str, Tuple[Any, str]]) -> List[Dict[str, Any]]:
        """Prepara as opções de módulos com status"""
        module_options = []
        
        for opcao, (_, descricao) in sorted(menu_options.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999):
            if not opcao.isdigit():
                continue
            
            module_id = f"modulo_{opcao}"
            is_completed = module_id in self.progress.progress_data["modules_completed"]
            
            if is_completed:
                option_status = "completed"
                icon = "✅"
            else:
                option_status = "pending"
                icon = "📘"
            
            module_options.append({
                "key": opcao,
                "text": descricao,
                "icon": icon,
                "status": option_status
            })
        
        return module_options
    
    def _display_module_sections(self, module_options: List[Dict[str, Any]]) -> None:
        """Exibe módulos organizados por categoria"""
        self.ui.section("MÓDULOS DO CURSO", "📚")
        
        # Organiza módulos por categoria
        basic_modules = [opt for opt in module_options if int(opt['key']) <= 11]
        intermediate_modules = [opt for opt in module_options if 12 <= int(opt['key']) <= 17]
        advanced_modules = [opt for opt in module_options if 18 <= int(opt['key']) <= 23]
        essential_modules = [opt for opt in module_options if 24 <= int(opt['key']) <= 30]
        enterprise_modules = [opt for opt in module_options if 31 <= int(opt['key']) <= 35]
        
        # Exibe cada categoria com cores específicas
        self._display_module_category("📚 BÁSICO (1-11):", basic_modules, "info")
        
        if intermediate_modules:
            self._display_module_category("\n🎓 INTERMEDIÁRIO (12-17):", intermediate_modules, "primary")
        
        if advanced_modules:
            self._display_module_category("\n🚀 AVANÇADO (18-23):", advanced_modules, "warning")
        
        if essential_modules:
            self._display_module_category("\n⚡ ESSENCIAIS (24-30):", essential_modules, "success")
        
        if enterprise_modules:
            self._display_enterprise_modules(enterprise_modules)
    
    def _display_module_category(self, title: str, modules: List[Dict[str, Any]], color_theme: str = "primary") -> None:
        """Exibe uma categoria de módulos em duas colunas com cores"""
        color = self.ui.get_color(color_theme)
        reset = self.ui.get_color("reset")
        
        print(f"{color}{title}{reset}")
        
        for i in range(0, len(modules), 2):
            left = modules[i]
            right = modules[i + 1] if i + 1 < len(modules) else None
            
            left_text = f"  {left['icon']} {left['key']:<2}. {left['text']:<28}"
            
            if right:
                right_text = f"{right['icon']} {right['key']:<2}. {right['text']}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
    
    def _display_enterprise_modules(self, enterprise_modules: List[Dict[str, Any]]) -> None:
        """Exibe módulos enterprise com destaque especial"""
        accent = self.ui.get_color("accent")
        primary = self.ui.get_color("primary")
        secondary = self.ui.get_color("secondary")
        reset = self.ui.get_color("reset")
        
        # Título destacado para Enterprise
        print(f"\n{accent}{'=' * 60}{reset}")
        print(f"{accent}🏢 MÓDULOS ENTERPRISE (31-35) - ARQUITETURA PROFISSIONAL{reset}")
        print(f"{accent}{'=' * 60}{reset}")
        
        # Descrição dos módulos enterprise
        enterprise_descriptions = {
            "31": ("🏗️ Design Patterns & SOLID", "Padrões de design e princípios fundamentais"),
            "32": ("🏛️ Clean Architecture & DDD", "Arquitetura limpa e design orientado ao domínio"),
            "33": ("🚀 DevOps Completo", "Docker, CI/CD, Kubernetes e Cloud"),
            "34": ("🗄️ Database Design", "Design de banco de dados e performance"),
            "35": ("🎓 Capstone Project", "Projeto final integrando todos os conceitos")
        }
        
        for module in enterprise_modules:
            key = module['key']
            icon = module['icon']
            status_color = primary if module['status'] == 'completed' else secondary
            
            if key in enterprise_descriptions:
                title, description = enterprise_descriptions[key]
                print(f"  {status_color}{icon} {key}. {title:<35}{reset} {accent}│{reset} {description}")
            else:
                print(f"  {status_color}{icon} {key}. {module['text']:<35}{reset}")
        
        print(f"{accent}{'─' * 60}{reset}")
        print(f"{accent}💡 Módulos para desenvolvimento enterprise e arquitetura avançada{reset}")
        print(f"{accent}🎯 Prepare-se para projetos de grande escala!{reset}")
    
    def _display_special_features(self) -> None:
        """Exibe recursos especiais do curso"""
        print("\n🌟 RECURSOS ESPECIAIS:")
        
        features = [
            ("V", "🎪 Demos Interativas", "Visualizações educativas"),
            ("E", "🧠 Exercícios Adaptativos", "Prática personalizada"),
            ("D", "🔍 Debugger Visual", "Debug passo a passo"),
            ("J", "🚀 Projetos Graduais", "3 projetos evolutivos"),
            ("M", "🚀 Galeria Mini Projetos", "18 projetos práticos"),
            ("B", "🧠 Debugging Metodológico", "Framework RSAD científico")
        ]
        
        for i in range(0, len(features), 2):
            left = features[i]
            right = features[i + 1] if i + 1 < len(features) else None
            
            left_text = f"  {left[0]}. {left[1]:<28}"
            
            if right:
                right_text = f"{right[0]}. {right[1]}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
    
    def _display_system_options(self) -> None:
        """Exibe opções do sistema"""
        print("\n⚙️ SISTEMA:")
        
        options = [
            ("R", "♻️ Modo Revisão", "Revise módulos completados"),
            ("G", "📖 Glossário", "Termos e definições"),
            ("P", "📊 Progresso", "Estatísticas detalhadas"),
            ("C", "🎓 Certificado", "Gere seu certificado"),
            ("S", "📊 Analytics Dashboard", "Relatórios avançados"),
            ("O", "🌐 Status Offline/Online", "Conectividade e sync"),
            ("Q", "🔍 Code Review", "Análise de código"),
            ("T", "🎨 Temas", "Personalização visual"),
            ("A", "🤖 Assistente IA", "Tutor interativo"),
            ("H", "❓ Ajuda", "Atalhos e comandos")
        ]
        
        for i in range(0, len(options), 2):
            left = options[i]
            right = options[i + 1] if i + 1 < len(options) else None
            
            left_text = f"  {left[0]}. {left[1]:<23}"
            
            if right:
                right_text = f"{right[0]}. {right[1]}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
        
        # Seção separada para opção de sair (mais visível)
        print(f"\n🚪 SAIR:")
        print(f"  0. 🚪 Sair do Curso")
    
    def get_user_choice(self, prompt: str = "👉 Escolha uma opção: ") -> str:
        """Obtém a escolha do usuário"""
        try:
            return input(f"\n{prompt}").strip()
        except KeyboardInterrupt:
            return "0"
        except EOFError:
            return "0"
    
    def display_help_menu(self, shortcuts: Dict[str, str]) -> None:
        """Exibe menu de ajuda com atalhos"""
        self.ui.clear_screen()
        self.ui.header("❓ AJUDA - ATALHOS E COMANDOS", "Sistema de Ajuda")
        
        print("📋 ATALHOS DISPONÍVEIS:")
        print("-" * 50)
        
        for key, description in shortcuts.items():
            print(f"  {key:<10} - {description}")
        
        print("\n💡 DICAS:")
        print("• Use números para acessar os módulos")
        print("• Tecle 0 para sair a qualquer momento")
        print("• Ctrl+C interrompe a execução atual")
        
        input("\n🔸 Pressione ENTER para voltar...")