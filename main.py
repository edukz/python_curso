#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CURSO INTERATIVO DE PYTHON PARA INICIANTES
Versão Refatorada - Arquitetura modular e organizada

Autor: Sistema de Ensino Python
Versão: 3.0 - Refatorado com arquitetura limpa
"""

import sys
import os
from typing import Dict, Any

# Adicionar o diretório src ao path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Imports essenciais (sempre carregados)
from src.controllers import MenuManager, CourseController, SessionManager
from src.config_manager import ConfigManager
from src.progress_manager import ProgressManager
from src.ui_components import UIComponents, ThemeManager
from src.keyboard_shortcuts import KeyboardShortcuts
from src.logger import CourseLogger
from src.error_tracker import ErrorTracker
from src.error_handler import ErrorHandler
from src.security import SecureInput
from src.theming import AdvancedThemeManager, ThemeCustomizer

# Lazy imports (carregados sob demanda)
from src.module_loader import module_loader, lazy_import

# Essential Modules
from src.modules.essential_modules import EssentialModules

# Analytics e Offline imports
from src.analytics.advanced_analytics import AdvancedAnalytics
from src.analytics.analytics_dashboard import AnalyticsDashboard
from src.offline.connectivity_manager import ConnectivityManager
from src.offline.resource_cache import ResourceCache, OfflineResourceManager
from src.offline.sync_manager import OfflineOnlineSync

# Code Review imports
from src.code_review.analysis_engine import CodeAnalysisEngine
from src.code_review.code_review_dashboard import CodeReviewDashboard
from src.code_review.exercise_integration import ExerciseCodeReviewer


class PythonCourse:
    """Classe principal do curso de Python - Versão Refatorada"""
    
    def __init__(self):
        """Inicializa todos os componentes do curso"""
        # Inicializa componentes básicos
        self._initialize_core_components()
        
        # Inicializa sistemas avançados
        self._initialize_advanced_systems()
        
        # Configura integrações
        self._setup_integrations()
        
        # Define opções do menu ANTES dos controladores
        self._setup_menu_options()
        
        # Inicializa controladores
        self._initialize_controllers()
    
    def _initialize_core_components(self) -> None:
        """Inicializa componentes básicos do sistema"""
        self.config = ConfigManager()
        
        # Inicializa sistema avançado de temas
        self.advanced_theme_manager = AdvancedThemeManager()
        
        # Carrega tema salvo
        saved_theme = self.config.get("display.current_theme", "light")
        self.advanced_theme_manager.set_theme(saved_theme)
        
        # Verifica se modo ASCII está ativado na configuração
        ascii_mode = self.config.get("display.ascii_mode", False)
        self.ui = UIComponents(ascii_mode=ascii_mode, theme_manager=self.advanced_theme_manager)
        
        # Inicializa customizador de temas
        self.theme_customizer = ThemeCustomizer(self.advanced_theme_manager, self.ui)
        
        # Componentes básicos
        self.theme_manager = ThemeManager()  # Mantém compatibilidade
        self.progress = ProgressManager()
        self.logger = CourseLogger()
        self.error_tracker = ErrorTracker()
        self.error_handler = ErrorHandler(self.logger, self.error_tracker)
        self.secure_input = SecureInput()
    
    def _initialize_advanced_systems(self) -> None:
        """Inicializa sistemas avançados com lazy loading"""
        # Sistemas essenciais (carregados imediatamente)
        VisualFeedback = module_loader.get_module("VisualFeedback")
        self.visual = VisualFeedback()
        self.shortcuts = KeyboardShortcuts(self.config.get_section('keyboard_shortcuts'))
        
        # Propriedades lazy (carregados sob demanda)
        self._lazy_modules_initialized = False
        self._lazy_analytics = None
        self._lazy_gamification = None
        self._lazy_review = None
        self._lazy_glossary = None
        self._lazy_certificate = None
        self._lazy_tutor = None
        self._lazy_code_playground = None
        self._lazy_interactive_demos = None
        self._lazy_adaptive_generator = None
        self._lazy_adaptive_session = None
        self._lazy_debug_session = None
        self._lazy_sync_manager = None
        self._lazy_modules = None
        self._lazy_advanced_modules = None
        self._lazy_essential_modules = None
        self._lazy_utils = None
        
        # Sistemas avançados
        self._lazy_advanced_analytics = None
        self._lazy_analytics_dashboard = None
        self._lazy_connectivity_manager = None
        self._lazy_resource_cache = None
        self._lazy_offline_manager = None
        self._lazy_offline_sync = None
        
        # Code Review
        self._lazy_code_analysis_engine = None
        self._lazy_code_review_dashboard = None
        self._lazy_exercise_code_reviewer = None
    
    # Propriedades lazy
    @property
    def analytics(self):
        if self._lazy_analytics is None:
            LearningAnalytics = module_loader.get_module("LearningAnalytics")
            self._lazy_analytics = LearningAnalytics(self.progress)
        return self._lazy_analytics
    
    @property
    def gamification(self):
        if self._lazy_gamification is None:
            GamificationSystem = module_loader.get_module("GamificationSystem")
            self._lazy_gamification = GamificationSystem(self.progress)
        return self._lazy_gamification
    
    @property
    def review(self):
        if self._lazy_review is None:
            ReviewMode = module_loader.get_module("ReviewMode")
            self._lazy_review = ReviewMode(self.progress)
        return self._lazy_review
    
    @property
    def glossary(self):
        if self._lazy_glossary is None:
            Glossary = module_loader.get_module("Glossary")
            self._lazy_glossary = Glossary()
        return self._lazy_glossary
    
    @property
    def certificate(self):
        if self._lazy_certificate is None:
            CertificateGenerator = module_loader.get_module("CertificateGenerator")
            self._lazy_certificate = CertificateGenerator()
        return self._lazy_certificate
    
    @property
    def modules(self):
        if self._lazy_modules is None:
            CourseModules = module_loader.get_module("CourseModules")
            self._lazy_modules = CourseModules()
            # Configura integrações
            self._lazy_modules.visual_feedback = self.visual
            self._lazy_modules.progress_manager = self.progress
        return self._lazy_modules
    
    @property
    def advanced_modules(self):
        if self._lazy_advanced_modules is None:
            AdvancedModules = module_loader.get_module("AdvancedModules")
            self._lazy_advanced_modules = AdvancedModules()
        return self._lazy_advanced_modules
    
    @property
    def essential_modules(self):
        if self._lazy_essential_modules is None:
            self._lazy_essential_modules = EssentialModules()
            self._lazy_essential_modules.set_dependencies(self.ui, self.progress)
        return self._lazy_essential_modules
    
    @property
    def tutor(self):
        if self._lazy_tutor is None:
            TutorAssistant = module_loader.get_module("TutorAssistant")
            self._lazy_tutor = TutorAssistant()
        return self._lazy_tutor
    
    @property
    def interactive_demos(self):
        if self._lazy_interactive_demos is None:
            InteractiveDemoSession = module_loader.get_module("InteractiveDemoSession")
            self._lazy_interactive_demos = InteractiveDemoSession(self.ui)
        return self._lazy_interactive_demos
    
    @property
    def adaptive_session(self):
        if self._lazy_adaptive_session is None:
            if self._lazy_adaptive_generator is None:
                AdaptiveExerciseGenerator = module_loader.get_module("AdaptiveExerciseGenerator")
                self._lazy_adaptive_generator = AdaptiveExerciseGenerator(self.progress, self.analytics)
            AdaptiveExerciseSession = module_loader.get_module("AdaptiveExerciseSession")
            self._lazy_adaptive_session = AdaptiveExerciseSession(self._lazy_adaptive_generator, self.ui)
        return self._lazy_adaptive_session
    
    @property
    def debug_session(self):
        if self._lazy_debug_session is None:
            DebugSession = module_loader.get_module("DebugSession")
            self._lazy_debug_session = DebugSession(self.ui)
        return self._lazy_debug_session
    
    @property
    def sync_manager(self):
        if self._lazy_sync_manager is None:
            SyncManager = module_loader.get_module("SyncManager")
            self._lazy_sync_manager = SyncManager()
        return self._lazy_sync_manager
    
    @property
    def utils(self):
        if self._lazy_utils is None:
            PythonCourseUtils = module_loader.get_module("PythonCourseUtils")
            self._lazy_utils = PythonCourseUtils()
            self._lazy_utils.set_managers(self.progress, self.gamification)
        return self._lazy_utils
    
    @property
    def advanced_analytics(self):
        if self._lazy_advanced_analytics is None:
            self._lazy_advanced_analytics = AdvancedAnalytics()
        return self._lazy_advanced_analytics
    
    @property
    def analytics_dashboard(self):
        if self._lazy_analytics_dashboard is None:
            self._lazy_analytics_dashboard = AnalyticsDashboard(self.advanced_analytics, self.ui)
        return self._lazy_analytics_dashboard
    
    @property
    def connectivity_manager(self):
        if self._lazy_connectivity_manager is None:
            self._lazy_connectivity_manager = ConnectivityManager()
            self._lazy_connectivity_manager.start_monitoring()
        return self._lazy_connectivity_manager
    
    @property
    def resource_cache(self):
        if self._lazy_resource_cache is None:
            self._lazy_resource_cache = ResourceCache()
        return self._lazy_resource_cache
    
    @property
    def offline_manager(self):
        if self._lazy_offline_manager is None:
            self._lazy_offline_manager = OfflineResourceManager(self.resource_cache)
        return self._lazy_offline_manager
    
    @property
    def offline_sync(self):
        if self._lazy_offline_sync is None:
            self._lazy_offline_sync = OfflineOnlineSync(self.connectivity_manager, self.resource_cache)
            self._lazy_offline_sync.start_auto_sync()
        return self._lazy_offline_sync
    
    @property
    def code_analysis_engine(self):
        if self._lazy_code_analysis_engine is None:
            self._lazy_code_analysis_engine = CodeAnalysisEngine()
        return self._lazy_code_analysis_engine
    
    @property
    def code_review_dashboard(self):
        if self._lazy_code_review_dashboard is None:
            self._lazy_code_review_dashboard = CodeReviewDashboard(self.code_analysis_engine, self.ui)
        return self._lazy_code_review_dashboard
    
    @property
    def exercise_code_reviewer(self):
        if self._lazy_exercise_code_reviewer is None:
            self._lazy_exercise_code_reviewer = ExerciseCodeReviewer(self.code_analysis_engine, self.progress)
        return self._lazy_exercise_code_reviewer
    
    def _initialize_controllers(self) -> None:
        """Inicializa controladores do sistema"""
        # Inicializa menu manager primeiro
        self.menu_manager = MenuManager(self.ui, self.progress, self.shortcuts)
        self.menu_manager.ascii_mode = self.config.get("display.ascii_mode", False)
        
        # Prepara componentes para controladores
        components = {
            'progress': self.progress,
            'visual': self.visual,
            'logger': self.logger,
            'gamification': self.gamification,
            'ui': self.ui,
            'error_tracker': self.error_tracker,
            'review': self.review,
            'glossary': self.glossary,
            'certificate': self.certificate,
            'interactive_demos': self.interactive_demos,
            'adaptive_session': self.adaptive_session,
            'debug_session': self.debug_session,
            'analytics': self.analytics,
            'tutor': self.tutor,
            'sync_manager': self.sync_manager,
            'secure_input': self.secure_input,
            'menu_options': self.menu_options,
            'navigation': self.menu_manager.navigation,
            'advanced_analytics': self.advanced_analytics,
            'analytics_dashboard': self.analytics_dashboard,
            'connectivity_manager': self.connectivity_manager,
            'offline_manager': self.offline_manager,
            'offline_sync': self.offline_sync,
            'code_analysis_engine': self.code_analysis_engine,
            'code_review_dashboard': self.code_review_dashboard,
            'exercise_code_reviewer': self.exercise_code_reviewer
        }
        
        # Inicializa outros controladores
        self.course_controller = CourseController(components)
        self.session_manager = SessionManager(components)
    
    def _setup_integrations(self) -> None:
        """Configura integrações entre componentes"""
        # Integrações serão feitas sob demanda quando os módulos forem carregados
        pass
    
    def _setup_menu_options(self) -> None:
        """Configura opções do menu principal"""
        self.menu_options = {
            # Módulos Básicos (1-11)
            "1": (self.modules.modulo_1_introducao, "Introdução ao Python"),
            "2": (self.modules.modulo_2_primeiro_programa, "Seu Primeiro Programa"),
            "3": (self.modules.modulo_3_variaveis, "Variáveis"),
            "4": (self.modules.modulo_4_tipos_dados, "Tipos de Dados"),
            "5": (self.modules.modulo_5_entrada_dados, "Entrada de Dados"),
            "6": (self.modules.modulo_6_operacoes, "Operações Matemáticas"),
            "7": (self.modules.modulo_7_condicoes, "Condições (if/else)"),
            "8": (self.modules.modulo_8_loops, "Repetições (loops)"),
            "9": (self.modules.modulo_9_listas, "Listas"),
            "10": (self.modules.modulo_10_funcoes, "Funções"),
            "11": (self.modules.projeto_final, "PROJETO: Calculadora Básica"),
            
            # Módulos Intermediários (12-17)
            "12": (self.advanced_modules.modulo_12_dicionarios, "Dicionários e Sets"),
            "13": (self.advanced_modules.modulo_13_funcoes_avancadas, "Funções Avançadas & Lambda"),
            "14": (self.advanced_modules.modulo_14_comprehensions, "List/Dict Comprehensions"),
            "15": (self.advanced_modules.modulo_15_arquivos, "Manipulação de Arquivos"),
            "16": (self.advanced_modules.modulo_16_excecoes, "Tratamento de Erros"),
            "17": (self.advanced_modules.modulo_17_modulos, "Módulos e Packages"),
            
            # Módulos Avançados (18-23)
            "18": (self.advanced_modules.modulo_18_oop_basico, "Programação Orientada a Objetos"),
            "19": (self.advanced_modules.modulo_19_oop_avancado, "Herança e Polimorfismo"),
            "20": (self.advanced_modules.modulo_20_decorators, "Decorators e Context Managers"),
            "21": (self.advanced_modules.modulo_21_geradores, "Generators e Iterators"),
            "22": (self.advanced_modules.modulo_22_regex, "Regular Expressions (Regex)"),
            "23": (self.advanced_modules.modulo_23_debugging, "Debugging e Profiling"),
            
            # Módulos Essenciais (24-30)
            "24": (self.essential_modules.modulo_24_git_github, "🐙 Git e GitHub Essencial"),
            "25": (self.essential_modules.modulo_25_terminal_cli, "🐧 Terminal e Command Line"),
            "26": (self.essential_modules.modulo_26_ambientes_virtuais, "📦 Ambientes Virtuais e Dependências"),
            "27": (self.essential_modules.modulo_27_testes_tdd, "🧪 Testes e TDD"),
            "28": (self.essential_modules.modulo_28_estrutura_projetos, "🏗️ Estrutura de Projetos Python"),
            "29": (self.essential_modules.modulo_29_apis_web_requests, "🌐 APIs e Web Requests"),
            "30": (self.essential_modules.modulo_30_seguranca_basica, "🛡️ Segurança Básica"),
        }
    
    def run(self) -> None:
        """Executa o curso principal"""
        try:
            # Inicializa sessão
            if not self.session_manager.initialize_session():
                return
            
            # Loop principal
            while self.session_manager.is_session_active():
                try:
                    self._main_loop()
                except KeyboardInterrupt:
                    if not self.session_manager.handle_interruption():
                        break
                except Exception as e:
                    self.error_handler.handle_error(e, "main_loop", "high")
                    if self.error_tracker.has_critical_errors():
                        self.ui.error("Erro crítico detectado. Encerrando...")
                        break
        
        finally:
            # Limpeza da sessão
            self.session_manager.cleanup_session()
            self.session_manager.show_exit_message()
    
    def _main_loop(self) -> None:
        """Loop principal do menu"""
        # Limpa tela e exibe menu
        self.ui.clear_screen()
        self.menu_manager.display_main_menu(self.menu_options)
        
        # Obtém escolha do usuário
        escolha = self.menu_manager.get_user_choice()
        
        if not escolha:
            return
        
        # Processa escolha
        if not self._process_user_choice(escolha):
            self.session_manager.end_session()
    
    def _process_user_choice(self, escolha: str) -> bool:
        """
        Processa a escolha do usuário
        
        Args:
            escolha: Opção escolhida pelo usuário
            
        Returns:
            True se deve continuar, False se deve sair
        """
        escolha = escolha.upper()
        
        # Sair
        if escolha == "0":
            return False
            
        # Voltar (se disponível)
        if escolha == "B" and self.menu_manager.navigation.can_go_back():
            callback = self.menu_manager.navigation.execute_back()
            if callback:
                callback()
            return True
        
        # Módulos do curso
        if escolha in self.menu_options:
            return self.course_controller.execute_module(escolha)
        
        # Recursos especiais
        if self.course_controller.handle_special_features(escolha):
            return True
        
        # Galeria de mini projetos
        if escolha == "M":
            self._mostrar_galeria_mini_projetos()
            return True
        
        # Code Review
        if escolha == "Q" and escolha != "0":  # Q para Code Review, não para quit
            self._show_code_review()
            return True
        
        # Temas e Personalização
        if escolha == "T":
            self._open_theme_customizer()
            return True
            
        # Ajuda
        if escolha == "H":
            shortcuts_dict = {
                "1-30": "Acessar módulos do curso",
                "V": "Demos interativas",
                "E": "Central de Exercícios (Ricos + Adaptativos)", 
                "D": "Debugger visual",
                "M": "Galeria mini projetos",
                "R": "Modo revisão",
                "G": "Glossário",
                "P": "Ver progresso",
                "C": "Gerar certificado",
                "A": "Assistente tutor interativo",
                "S": "📊 Analytics Dashboard",
                "O": "🌐 Status Offline/Online",
                "Q": "🔍 Code Review",
                "T": "Temas e Personalização",
                "H": "❓ Ajuda (este menu)",
                "0": "Sair do curso"
            }
            self.menu_manager.display_help_menu(shortcuts_dict)
            return True
        
        # Opção inválida
        self.ui.warning(f"❌ Opção '{escolha}' não reconhecida. Tente novamente.")
        self.ui.pause()
        return True
    
    def _mostrar_galeria_mini_projetos(self) -> None:
        """Exibe galeria de mini projetos"""
        self.ui.clear_screen()
        self.ui.header("🚀 GALERIA DE MINI PROJETOS", "18 Projetos Práticos Disponíveis")
        
        # Dados dos mini projetos organizados por categoria
        mini_projetos_data = {
            "basicos": {
                "titulo": "📚 BÁSICOS (1-6)",
                "projetos": [
                    {"modulo": "modulo_1", "nome": "Calculadora de IMC", "pontos": 25},
                    {"modulo": "modulo_2", "nome": "Gerador de Mensagens", "pontos": 25},
                    {"modulo": "modulo_3", "nome": "Conversor de Unidades", "pontos": 25},
                    {"modulo": "modulo_4", "nome": "Analisador de Dados Pessoais", "pontos": 25},
                    {"modulo": "modulo_5", "nome": "Quiz Interativo", "pontos": 25},
                    {"modulo": "modulo_6", "nome": "Calculadora Científica", "pontos": 25}
                ]
            },
            "intermediarios": {
                "titulo": "🎯 INTERMEDIÁRIOS (7-11 e 12-17)",
                "projetos": [
                    {"modulo": "modulo_7", "nome": "Sistema de Notas", "pontos": 50},
                    {"modulo": "modulo_8", "nome": "Gerador de Senhas", "pontos": 50},
                    {"modulo": "modulo_9", "nome": "Analisador de Texto", "pontos": 50},
                    {"modulo": "modulo_10", "nome": "Biblioteca de Funções", "pontos": 50},
                    {"modulo": "modulo_11", "nome": "Calculadora Completa", "pontos": 50},
                    {"modulo": "modulo_12", "nome": "Sistema de Cadastro", "pontos": 75}
                ]
            },
            "avancados": {
                "titulo": "🚀 AVANÇADOS (13-23)",
                "projetos": [
                    {"modulo": "modulo_13", "nome": "Processador de Dados", "pontos": 75},
                    {"modulo": "modulo_14", "nome": "Analisador de Performance", "pontos": 75},
                    {"modulo": "modulo_15", "nome": "Gerenciador de Arquivos", "pontos": 75},
                    {"modulo": "modulo_16", "nome": "Sistema de Logs", "pontos": 75},
                    {"modulo": "modulo_17", "nome": "Framework Personalizado", "pontos": 75},
                    {"modulo": "modulo_18", "nome": "Sistema de Gestão de Funcionários", "pontos": 75}
                ]
            }
        }
        
        # Obtém projetos completos
        completed_mini_projects = self.progress.progress_data.get("mini_projetos_completos", [])
        total_projects = sum(len(cat["projetos"]) for cat in mini_projetos_data.values())
        completed_count = len(completed_mini_projects)
        completion_percentage = (completed_count / total_projects) * 100 if total_projects > 0 else 0
        
        # Exibe estatísticas
        self.ui.info_box(
            "Estatísticas da Galeria",
            f"📊 Projetos Completos: {completed_count}/{total_projects}\n"
            f"📈 Progresso: {completion_percentage:.1f}%\n"
            f"💰 Pontos Disponíveis: {sum(sum(p['pontos'] for p in cat['projetos']) for cat in mini_projetos_data.values())} pts\n"
            f"🏆 Pontos Conquistados: {sum(p['pontos'] for cat in mini_projetos_data.values() for p in cat['projetos'] if p['modulo'] + '_mini_projeto' in completed_mini_projects)} pts",
            "📊",
            "info"
        )
        
        # Menu de opções
        print("\n🎯 MENU DE OPÇÕES:")
        print("1. 📋 Ver Todos os Projetos")
        print("2. ✅ Ver Apenas Completos")
        print("3. ⏳ Ver Apenas Pendentes")
        print("0. 🔙 Voltar ao Menu Principal")
        
        escolha = input("\n👉 Escolha uma opção: ").strip()
        
        if escolha == "1":
            self._exibir_projetos_filtrados(mini_projetos_data, completed_mini_projects, "todos")
        elif escolha == "2":
            self._exibir_projetos_filtrados(mini_projetos_data, completed_mini_projects, "completos")
        elif escolha == "3":
            self._exibir_projetos_filtrados(mini_projetos_data, completed_mini_projects, "pendentes")
        # Escolha "0" ou inválida volta automaticamente
    
    def _exibir_projetos_filtrados(self, projetos_data: dict, completos: list, filtro: str) -> None:
        """Exibe projetos com filtro aplicado"""
        self.ui.clear_screen()
        
        titulo_filtro = {
            "todos": "TODOS OS PROJETOS",
            "completos": "PROJETOS COMPLETOS",
            "pendentes": "PROJETOS PENDENTES"
        }
        
        self.ui.header(f"🚀 {titulo_filtro[filtro]}", "Galeria de Mini Projetos")
        
        for categoria, dados in projetos_data.items():
            print(f"\n{dados['titulo']}")
            print("=" * 50)
            
            projetos_exibidos = 0
            for projeto in dados['projetos']:
                projeto_completo = f"{projeto['modulo']}_mini_projeto" in completos
                
                # Aplica filtro
                if filtro == "completos" and not projeto_completo:
                    continue
                elif filtro == "pendentes" and projeto_completo:
                    continue
                
                # Exibe projeto
                status_icon = "✅" if projeto_completo else "⏳"
                status_text = "COMPLETO" if projeto_completo else "PENDENTE"
                
                print(f"  {status_icon} {projeto['nome']:<35} | "
                      f"📘 {projeto['modulo'].replace('modulo_', 'Módulo '):<12} | "
                      f"⭐ {projeto['pontos']:>3} pts | "
                      f"{status_text}")
                
                projetos_exibidos += 1
            
            if projetos_exibidos == 0:
                print("  📝 Nenhum projeto nesta categoria para o filtro selecionado.")
        
        input("\n🔸 Pressione ENTER para voltar...")
    
    def _open_theme_customizer(self) -> None:
        """Abre o customizador de temas"""
        # Salva tema atual antes de abrir customizador
        current_theme = self.advanced_theme_manager.current_theme_name
        
        # Abre interface de customização
        self.theme_customizer.show_theme_menu()
        
        # Salva tema selecionado na configuração
        new_theme = self.advanced_theme_manager.current_theme_name
        if new_theme != current_theme:
            self.config.set("display.current_theme", new_theme)
            
            # Atualiza modo ASCII baseado no tema
            theme = self.advanced_theme_manager.get_current_theme()
            self.config.set("display.ascii_mode", theme.ascii_mode)
            self.menu_manager.ascii_mode = theme.ascii_mode
            
    def _toggle_ascii_mode(self) -> None:
        """Alterna entre modo ASCII e modo com emojis (método legado)"""
        current_theme = self.advanced_theme_manager.get_current_theme()
        new_mode = not current_theme.ascii_mode
        
        # Atualiza tema atual
        self.advanced_theme_manager.toggle_emojis(self.advanced_theme_manager.current_theme_name)
        
        # Atualiza configuração
        self.config.set("display.ascii_mode", new_mode)
        
        # Atualiza componentes
        self.ui.ascii_converter.ascii_mode = new_mode
        self.menu_manager.ascii_mode = new_mode
        
        # Feedback ao usuário
        if new_mode:
            self.ui.success("Modo ASCII ativado! [OK]")
        else:
            self.ui.success("Modo ASCII desativado! ✅")
        
        self.ui.pause()
    
    def _show_analytics_dashboard(self) -> None:
        """Abre o dashboard de analytics avançados"""
        try:
            # Inicia sessão de analytics se não ativa
            current_module = getattr(self, 'current_module_id', None)
            if current_module and not hasattr(self.advanced_analytics, 'current_session_start'):
                self.advanced_analytics.start_session(current_module, "dashboard_access")
            
            # Abre dashboard
            self.analytics_dashboard.show_main_dashboard()
            
        except Exception as e:
            self.ui.error(f"Erro ao abrir analytics: {str(e)}")
            self.ui.pause()
    
    def _show_offline_status(self) -> None:
        """Mostra status do modo offline e conectividade"""
        self.ui.clear_screen()
        self.ui.header("🌐 STATUS DE CONECTIVIDADE", "Modo Offline e Sincronização")
        
        # Status de conectividade
        conn_quality = self.connectivity_manager.get_connection_quality()
        status_icon = {
            "online": "🟢",
            "offline": "🔴", 
            "limited": "🟡",
            "unknown": "⚪"
        }
        
        print(f"\n🌐 CONECTIVIDADE:")
        print(f"  Status: {status_icon.get(conn_quality['status'], '❓')} {conn_quality['status'].upper()}")
        print(f"  Qualidade: {conn_quality['quality']:.1f}%")
        if conn_quality.get('avg_latency_ms'):
            print(f"  Latência: {conn_quality['avg_latency_ms']:.0f}ms")
        print(f"  Estabilidade: {conn_quality['stability']:.1f}%")
        
        # Status do cache offline
        offline_status = self.offline_manager.get_offline_status()
        print(f"\n💾 MODO OFFLINE:")
        ready_icon = "✅" if offline_status['ready'] else "⚠️"
        print(f"  Status: {ready_icon} {'Pronto' if offline_status['ready'] else 'Não configurado'}")
        print(f"  Recursos disponíveis: {len(offline_status['available_resources'])}/5")
        print(f"  Cache: {offline_status['cache_size_mb']:.1f}MB ({offline_status['cached_items']} itens)")
        
        # Status de sincronização
        sync_status = self.offline_sync.get_sync_status()
        print(f"\n🔄 SINCRONIZAÇÃO:")
        print(f"  Status: {sync_status['current_status'].upper()}")
        print(f"  Operações pendentes: {sync_status['pending_operations']}")
        print(f"  Auto-sync: {'✅ Ativado' if sync_status['auto_sync_enabled'] else '❌ Desativado'}")
        if sync_status['last_sync']:
            from datetime import datetime
            last_sync = datetime.fromisoformat(sync_status['last_sync'])
            print(f"  Última sync: {last_sync.strftime('%d/%m/%Y %H:%M')}")
        
        # Menu de opções
        print(f"\n⚙️ OPÇÕES:")
        print("1. 🔄 Sincronizar agora")
        print("2. 💾 Preparar modo offline")
        print("3. 📊 Ver histórico de sync")
        print("4. ⚡ Forçar modo offline")
        print("0. 🔙 Voltar")
        
        escolha = input("\n👉 Escolha: ").strip()
        
        if escolha == "1":
            self._force_sync()
        elif escolha == "2":
            self._prepare_offline_mode()
        elif escolha == "3":
            self._show_sync_history()
        elif escolha == "4":
            self._force_offline_mode()
    
    def _force_sync(self) -> None:
        """Força sincronização imediata"""
        print("\n🔄 Sincronizando dados...")
        
        # Sincroniza dados essenciais
        progress_data = self.progress.progress_data
        user_settings = {
            "theme": self.advanced_theme_manager.current_theme_name,
            "ascii_mode": self.config.get("display.ascii_mode", False)
        }
        
        self.offline_sync.sync_progress_data(progress_data)
        self.offline_sync.sync_user_settings(user_settings)
        
        results = self.offline_sync.sync_now()
        
        success_count = sum(1 for r in results if r.status.value == "success")
        print(f"✅ Sincronizadas {success_count}/{len(results)} operações")
        
        self.ui.pause()
    
    def _prepare_offline_mode(self) -> None:
        """Prepara sistema para modo offline"""
        print("\n💾 Preparando modo offline...")
        
        # Dados essenciais do curso
        course_data = {
            "modules": {k: v for k, v in self.menu_options.items() if k.isdigit()},
            "themes": [t.name for t in self.advanced_theme_manager.themes.values()],
            "help_content": "Conteúdo de ajuda local"
        }
        
        if self.offline_manager.prepare_offline_mode(course_data):
            print("✅ Modo offline preparado com sucesso!")
        else:
            print("❌ Falha ao preparar modo offline")
        
        self.ui.pause()
    
    def _show_sync_history(self) -> None:
        """Mostra histórico de sincronização"""
        history = self.offline_sync.get_sync_history(20)
        
        print("\n📊 HISTÓRICO DE SINCRONIZAÇÃO:")
        print("=" * 60)
        
        if not history:
            print("📝 Nenhuma sincronização realizada ainda.")
        else:
            from datetime import datetime
            for entry in history:
                status_icon = {
                    "success": "✅",
                    "error": "❌",
                    "conflict": "⚠️"
                }.get(entry['status'], "❓")
                
                timestamp = datetime.fromisoformat(entry['timestamp'])
                print(f"{status_icon} {timestamp.strftime('%d/%m %H:%M')} - {entry['message']}")
        
        self.ui.pause()
    
    def _force_offline_mode(self) -> None:
        """Força modo offline"""
        confirm = input("\n⚠️ Forçar modo offline? (s/N): ").lower().strip()
        if confirm == 's':
            self.connectivity_manager.force_offline_mode()
            print("🔌 Modo offline ativado forçadamente")
        else:
            print("❌ Operação cancelada")
        
        self.ui.pause()
    
    def _show_code_review(self) -> None:
        """Abre o dashboard de code review"""
        try:
            self.code_review_dashboard.show_main_dashboard()
        except Exception as e:
            self.ui.error(f"Erro ao abrir code review: {str(e)}")
            self.ui.pause()


def main():
    """Função principal"""
    try:
        curso = PythonCourse()
        curso.run()
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro crítico: {str(e)}")
        print("📧 Reporte este erro para melhorarmos o curso!")
    finally:
        print("\n🐍 Obrigado por usar o Curso de Python!")


if __name__ == "__main__":
    main()