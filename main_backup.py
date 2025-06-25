#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CURSO INTERATIVO DE PYTHON PARA INICIANTES
Desenvolvido para ensinar Python do zero

Autor: Sistema de Ensino Python
Versão: 2.0 - Com melhorias e novos recursos
"""

import time
import sys
import os
from datetime import datetime

# Adicionar o diretório src ao path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.utils import PythonCourseUtils
from src.modules import CourseModules
from src.progress_manager import ProgressManager
from src.visual_feedback import VisualFeedback
from src.config_manager import ConfigManager
from src.logger import CourseLogger
from src.review_mode import ReviewMode
from src.glossary import Glossary
from src.keyboard_shortcuts import KeyboardShortcuts
from src.certificate_generator import CertificateGenerator
from src.ui_components import UIComponents, ThemeManager
from src.tutor_assistant import TutorAssistant
from src.learning_analytics import LearningAnalytics
from src.gamification_system import GamificationSystem, AchievementNotifier, BadgeType
from src.code_editor import CodePlayground
from src.interactive_demos import InteractiveDemoSession
from src.sync_manager import SyncManager
from src.adaptive_exercises import AdaptiveExerciseGenerator, AdaptiveExerciseSession
from src.visual_debugger import DebugSession
from src.error_tracker import ErrorTracker
from src.security import SecureInput



class PythonCourse:
    """Classe principal do curso de Python"""
    
    def __init__(self):
        # Inicializa componentes básicos
        self.utils = PythonCourseUtils()
        self.modules = CourseModules()
        
        # Inicializa novos componentes
        self.config = ConfigManager()
        self.progress = ProgressManager()
        self.visual = VisualFeedback()
        self.logger = CourseLogger()
        self.review = ReviewMode(self.progress)
        self.glossary = Glossary()
        self.shortcuts = KeyboardShortcuts(self.config.get_section('keyboard_shortcuts'))
        self.certificate = CertificateGenerator()
        self.ui = UIComponents()
        self.theme_manager = ThemeManager()
        self.tutor = TutorAssistant()
        self.analytics = LearningAnalytics(self.progress)
        self.gamification = GamificationSystem(self.progress)
        self.code_playground = CodePlayground()
        self.interactive_demos = InteractiveDemoSession(self.ui)
        self.sync_manager = SyncManager()
        self.adaptive_generator = AdaptiveExerciseGenerator(self.progress, self.analytics)
        self.adaptive_session = AdaptiveExerciseSession(self.adaptive_generator, self.ui)
        self.debug_session = DebugSession(self.ui)
        self.error_tracker = ErrorTracker()
        self.secure_input = SecureInput()
        
        # Tempo de início da sessão
        self.session_start = datetime.now()
        
        # Integra visual feedback aos módulos
        self.modules.visual_feedback = self.visual
        self.modules.progress_manager = self.progress
        
        # Conecta utils com sistemas de progresso e gamificação
        self.utils.set_managers(self.progress, self.gamification)
        self.modules.utils.set_managers(self.progress, self.gamification)
        
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
            "12": (self.modules.modulo_12_dicionarios, "Dicionários e Sets"),
            "13": (self.modules.modulo_13_funcoes_avancadas, "Funções Avançadas & Lambda"),
            "14": (self.modules.modulo_14_comprehensions, "List/Dict Comprehensions"),
            "15": (self.modules.modulo_15_arquivos, "Manipulação de Arquivos"),
            "16": (self.modules.modulo_16_excecoes, "Tratamento de Erros"),
            "17": (self.modules.modulo_17_modulos, "Módulos e Bibliotecas"),
            
            # Módulos Avançados (18-23)
            "18": (self.modules.modulo_18_oop_basico, "Programação Orientada a Objetos"),
            "19": (self.modules.modulo_19_oop_avancado, "OOP Avançado: Herança e Polimorfismo"),
            "20": (self.modules.modulo_20_decorators, "Decorators e Context Managers"),
            "21": (self.modules.modulo_21_geradores, "Generators e Iterators"),
            "22": (self.modules.modulo_22_regex, "Expressões Regulares"),
            "23": (self.modules.modulo_23_debugging, "Debugging e Profiling"),
            
            # Projetos Práticos (24-26)
            "24": (self.modules.projeto_intermediario, "PROJETO: Sistema de Biblioteca"),
            "25": (self.modules.projeto_avancado, "PROJETO: Web Scraper"),
            "26": (self.modules.projeto_final_avancado, "PROJETO FINAL: API REST")
        }
        
        # Registra atalhos de teclado
        self._register_shortcuts()
    
    def _register_shortcuts(self) -> None:
        """Registra ações para atalhos de teclado"""
        self.shortcuts.register_action('show_progress', self._show_progress_summary)
        self.shortcuts.register_action('toggle_hints', self._toggle_hints)
    
    def _show_progress_summary(self, context=None) -> None:
        """Exibe resumo do progresso"""
        summary = self.progress.get_progress_summary()
        self.utils.limpar_tela()
        print(self.visual.get_score_summary())
        print(f"\n📊 Progresso Geral: {summary['completion_percentage']:.1f}%")
        print(f"📚 Módulos Completos: {summary['modules_completed']}/{summary['total_modules']}")
        self.utils.pausar()
    
    def _toggle_hints(self, context=None) -> None:
        """Alterna exibição de dicas"""
        current = self.config.get('display.show_hints_delay')
        new_value = 0 if current > 0 else 3
        self.config.set('display.show_hints_delay', new_value)
        status = "ativadas" if new_value > 0 else "desativadas"
        print(f"\n💡 Dicas {status}")
        time.sleep(1)
    
    def _check_first_time_user(self) -> None:
        """Verifica se é a primeira vez do usuário"""
        if not self.progress.progress_data['user_name']:
            self.utils.limpar_tela()
            self.utils.titulo("BEM-VINDO AO CURSO DE PYTHON!")
            print("Parece que é sua primeira vez aqui! 🎉")
            nome = input("\nComo posso te chamar? ").strip()
            if nome:
                self.progress.set_user_name(nome)
                self.logger.log_session_start(nome)
                print(f"\nÓtimo, {nome}! Vamos começar sua jornada Python! 🚀")
                self.visual.unlock_achievement("Primeira Vez no Curso!")
                self.progress.add_achievement("Primeira Vez no Curso!")
                self.utils.pausar()
        else:
            nome = self.progress.progress_data['user_name']
            self.logger.log_session_start(nome)
            print(f"\n👋 Bem-vindo de volta, {nome}!")
            time.sleep(1)
    
    def exibir_menu(self) -> None:
        """Exibe o menu principal do curso"""
        self.utils.limpar_tela()
        
        # Cabeçalho principal
        summary = self.progress.get_progress_summary()
        subtitle = f"Bem-vindo, {summary['user_name']}!" if summary['user_name'] else "Sistema de Ensino Interativo"
        
        self.ui.header(
            "CURSO INTERATIVO DE PYTHON 2.0",
            subtitle,
            "🐍"
        )
        
        # Barra de progresso geral
        if summary['completion_percentage'] > 0:
            self.ui.progress_bar(
                summary['modules_completed'],
                summary['total_modules'],
                f"📊 Progresso Geral - {summary['total_score']} pontos",
                40
            )
            print()
        
        # Menu de módulos
        module_options = []
        for opcao, (_, descricao) in self.menu_options.items():
            module_id = f"modulo_{opcao}"
            status = self.progress.get_module_status(module_id)
            
            if status.get('completed'):
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
        
        self.ui.section("MÓDULOS DO CURSO", "📚")
        
        # Organiza módulos por categoria
        basic_modules = [opt for opt in module_options if int(opt['key']) <= 11]
        intermediate_modules = [opt for opt in module_options if 12 <= int(opt['key']) <= 17]
        advanced_modules = [opt for opt in module_options if 18 <= int(opt['key']) <= 23]
        projects = [opt for opt in module_options if int(opt['key']) >= 24]
        
        # Módulos Básicos
        print("📚 BÁSICO (1-11):")
        for i in range(0, len(basic_modules), 2):
            left = basic_modules[i]
            right = basic_modules[i + 1] if i + 1 < len(basic_modules) else None
            
            left_text = f"  {left['icon']} {left['key']:<2}. {left['text']:<28}"
            
            if right:
                right_text = f"{right['icon']} {right['key']:<2}. {right['text']}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
        
        # Módulos Intermediários
        if intermediate_modules:
            print("\n🎓 INTERMEDIÁRIO (12-17):")
            for i in range(0, len(intermediate_modules), 2):
                left = intermediate_modules[i]
                right = intermediate_modules[i + 1] if i + 1 < len(intermediate_modules) else None
                
                left_text = f"  {left['icon']} {left['key']:<2}. {left['text']:<28}"
                
                if right:
                    right_text = f"{right['icon']} {right['key']:<2}. {right['text']}"
                    print(f"{left_text} {right_text}")
                else:
                    print(left_text)
        
        # Módulos Avançados
        if advanced_modules:
            print("\n🚀 AVANÇADO (18-23):")
            for i in range(0, len(advanced_modules), 2):
                left = advanced_modules[i]
                right = advanced_modules[i + 1] if i + 1 < len(advanced_modules) else None
                
                left_text = f"  {left['icon']} {left['key']:<2}. {left['text']:<28}"
                
                if right:
                    right_text = f"{right['icon']} {right['key']:<2}. {right['text']}"
                    print(f"{left_text} {right_text}")
                else:
                    print(left_text)
        
        # Projetos
        if projects:
            print("\n🛠️ PROJETOS (24-26):")
            for project in projects:
                print(f"  {project['icon']} {project['key']:<2}. {project['text']}")
        
        # Menu de recursos extras
        self.ui.section("RECURSOS EXTRAS", "⭐")
        extra_options = [
            {"text": "R. 🔄 Modo Revisão", "description": "Pratique o que aprendeu"},
            {"text": "G. 📖 Glossário de Termos", "description": "Dicionário Python"},
            {"text": "P. 📊 Ver Progresso Detalhado", "description": "Estatísticas completas"},
            {"text": "C. 🎓 Gerar Certificado", "description": "Seu diploma digital"},
            {"text": "M. 🚀 Galeria Mini Projetos", "description": "Todos os projetos práticos"},
            {"text": "T. 🎨 Mudar Tema", "description": "Personalizar cores"},
            {"text": "H. ❓ Ajuda e Atalhos", "description": "Guia de uso"},
            {"text": "A. 🤖 Assistente Python", "description": "Tire suas dúvidas"},
            {"text": "D. 📊 Dashboard Analytics", "description": "Análise de aprendizagem"},
            {"text": "F. 🎮 Perfil Gamer", "description": "Conquistas e gamificação"},
            {"text": "E. 📝 Editor de Código", "description": "Playground para experimentar"},
            {"text": "V. 🎥 Demos Interativas", "description": "Animações visuais de conceitos"},
            {"text": "S. 🔄 Sincronização", "description": "Backup e múltiplos perfis"},
            {"text": "B. 🎯 Exercícios Adaptativos", "description": "Treinamento personalizado"},
            {"text": "W. 🔬 Debug Visual", "description": "Analisador de código step-by-step"},
            {"text": "X. 🗑️ Resetar Progresso", "description": "Recomeçar do zero"}
        ]
        
        for i in range(0, len(extra_options), 2):
            left = extra_options[i]
            right = extra_options[i + 1] if i + 1 < len(extra_options) else None
            
            if right:
                print(f"{left['text']:<30} {right['text']}")
            else:
                print(left['text'])
        
        # Opção de sair
        self.ui.divider("─")
        print("0. 🚪 Sair do Curso")
        
        # Rodapé com atalhos
        self.ui.divider("─", "ATALHOS RÁPIDOS")
        print(f"⌨️  {self.shortcuts.create_shortcut_bar()}")
        print()
    
    def executar_opcao(self, escolha: str) -> bool:
        """Executa a opção escolhida pelo usuário"""
        escolha = escolha.upper()
        
        if escolha == "0":
            return self._sair_do_curso()
        
        # Opções de módulos
        if escolha in self.menu_options:
            module_id = f"modulo_{escolha}"
            nome_modulo = self.menu_options[escolha][1]
            
            # Log e marca início do módulo
            self.logger.log_module_start(module_id, nome_modulo)
            self.error_tracker.start_module(module_id)
            start_time = time.time()
            
            # Executa o módulo
            funcao, _ = self.menu_options[escolha]
            funcao()
            
            # Calcula tempo gasto
            time_spent = int(time.time() - start_time)
            
            # Atualiza progresso
            if not self.progress.get_module_status(module_id).get('completed'):
                pontos = 100  # Pontos por completar módulo
                self.progress.mark_module_completed(module_id, pontos)
                self.visual.celebration()
                self.visual.add_score(pontos, "Módulo completo!")
                self.logger.log_module_completion(module_id, pontos, time_spent)
                
                # Sistema de gamificação
                xp_result = self.gamification.adicionar_xp(pontos, f"Módulo {escolha} completo")
                
                # Verifica badges por completar módulo
                module_stats = self.error_tracker.end_module(module_id)
                badges_novos = self.gamification.verificar_conquistas_modulo(
                    module_id, 
                    sem_erros=module_stats["sem_erros"],
                    tempo_segundos=time_spent
                )
                
                # Exibe notificações de nível
                if xp_result["subiu_nivel"]:
                    self.ui.alert(
                        f"🎉 LEVEL UP! Agora você é {xp_result['nivel_atual']}!\n"
                        f"Bonus: +{xp_result.get('bonus_moedas', 0)} moedas",
                        "success"
                    )
                
                # Exibe badges novos
                for badge in badges_novos:
                    AchievementNotifier.notificar_conquista(badge, self.ui)
                
                # Verifica conquistas especiais do sistema antigo
                completed = len(self.progress.progress_data['modules_completed'])
                if completed == 1:
                    self.visual.unlock_achievement("Primeiro Módulo!")
                    self.progress.add_achievement("Primeiro Módulo!")
                elif completed == 5:
                    self.visual.unlock_achievement("Metade do Caminho!")
                    self.progress.add_achievement("Metade do Caminho!")
                elif completed == 11:
                    self.visual.unlock_achievement("Curso Completo!")
                    self.progress.add_achievement("Curso Completo!")
            
            self.progress.update_module_progress(module_id, time_spent, 1)
            
        # Recursos extras
        elif escolha == "R":
            self.review.start_review_session()
        elif escolha == "G":
            self.glossary.show_glossary_menu()
        elif escolha == "P":
            self._mostrar_progresso_detalhado()
        elif escolha == "C":
            self._gerar_certificado()
        elif escolha == "M":
            self._mostrar_galeria_mini_projetos()
        elif escolha == "T":
            self._mudar_tema()
        elif escolha == "H":
            self._mostrar_ajuda()
        elif escolha == "A":
            self._usar_assistente()
        elif escolha == "D":
            self._mostrar_dashboard_analytics()
        elif escolha == "F":
            self._mostrar_perfil_gamer()
        elif escolha == "E":
            self._abrir_editor_codigo()
        elif escolha == "V":
            self._abrir_demos_interativas()
        elif escolha == "S":
            self._abrir_sincronizacao()
        elif escolha == "B":
            self._abrir_exercicios_adaptativos()
        elif escolha == "W":
            self._abrir_debug_visual()
        elif escolha == "X":
            self._resetar_progresso()
        else:
            print("❌ Opção inválida! Tente novamente.")
            time.sleep(2)
        
        return True
    
    def _mostrar_progresso_detalhado(self) -> None:
        """Mostra progresso detalhado do aluno"""
        self.utils.limpar_tela()
        
        summary = self.progress.get_detailed_progress_summary()
        
        self.ui.header("RELATÓRIO DE PROGRESSO", f"Aluno: {summary['user_name']}", "📊")
        
        # Estatísticas principais
        self.ui.card(
            "Estatísticas Gerais",
            f"Progresso Módulos: {summary['completion_percentage']:.1f}%\n"
            f"Módulos Completos: {summary['modules_completed']}/{summary['total_modules']}\n"
            f"Mini Projetos: {summary['mini_projetos_completos']}/{summary['total_mini_projects']}\n"
            f"Progresso Projetos: {summary['mini_projetos_percentage']:.1f}%\n"
            f"Pontuação Total: {summary['total_score']} pontos\n"
            f"Conquistas: {summary['achievements']} desbloqueadas",
            "📈",
            "success" if summary['completion_percentage'] == 100 else "info"
        )
        
        # Progresso por módulo
        headers = ["Módulo", "Status", "Pontos", "Tentativas"]
        rows = []
        
        for i in range(1, 12):
            module_id = f"modulo_{i}"
            status_data = self.progress.get_module_status(module_id)
            
            if status_data.get('completed'):
                status = "✅ Completo"
                points = status_data.get('score', 0)
                attempts = status_data.get('attempts', 0)
            else:
                status = "⏳ Pendente"
                points = 0
                attempts = 0
            
            rows.append([f"Módulo {i}", status, str(points), str(attempts)])
        
        self.ui.table(headers, rows, "📚 Progresso por Módulo")
        
        # Mini Projetos Progress
        mini_projects_headers = ["Projeto", "Status", "Pontos"]
        mini_projects_rows = []
        
        # Define mini projects mapping
        mini_projects_info = {
            "modulo_1": "Cartão de Apresentação Python",
            "modulo_2": "Gerador de Mensagens",
            "modulo_3": "Calculadora de Variáveis",
            "modulo_4": "Conversor de Tipos",
            "modulo_5": "Quiz Interativo",
            "modulo_6": "Calculadora Científica",
            "modulo_12": "Sistema de Contatos",
            "modulo_13": "Processador de Dados",
            "modulo_14": "Analisador de Logs",
            "modulo_15": "Sistema de Backup",
            "modulo_16": "Monitor Robusto",
            "modulo_17": "Framework de Plugins",
            "modulo_18": "Gestão de Funcionários",
            "modulo_19": "Sistema RPG",
            "modulo_20": "Cache Inteligente",
            "modulo_21": "Pipeline de Dados",
            "modulo_22": "Analisador de Logs Avançado",
            "modulo_23": "Profiler de Performance"
        }
        
        completed_mini_projects = self.progress.progress_data.get("mini_projetos_completos", [])
        
        for module_id, project_name in mini_projects_info.items():
            mini_projeto_key = f"{module_id}_mini_projeto"
            if mini_projeto_key in completed_mini_projects:
                status = "✅ Concluído"
                module_data = self.progress.progress_data.get("modules_progress", {}).get(module_id, {})
                points = module_data.get("mini_projeto_score", 50)
            else:
                status = "⏳ Pendente"
                points = 0
            
            mini_projects_rows.append([project_name, status, str(points)])
        
        self.ui.table(mini_projects_headers, mini_projects_rows, "🚀 Mini Projetos")
        
        # Módulos pendentes
        pendentes = []
        for i in range(1, 12):
            module_id = f"modulo_{i}"
            if module_id not in self.progress.progress_data['modules_completed']:
                module_name = self.menu_options[str(i)][1]
                pendentes.append(f"• Módulo {i}: {module_name}")
        
        if pendentes:
            self.ui.card(
                "Próximos Passos",
                "\n".join(pendentes),
                "📝",
                "warning"
            )
        else:
            self.ui.alert("🎉 Parabéns! Você completou todos os módulos!", "success")
        
        self.utils.pausar()
    
    def _gerar_certificado(self) -> None:
        """Gera certificado de conclusão"""
        self.utils.limpar_tela()
        
        summary = self.progress.get_progress_summary()
        
        self.ui.header("GERAÇÃO DE CERTIFICADO", "Seu Diploma Digital", "🎓")
        
        if self.certificate.can_generate_certificate(summary):
            self.ui.alert(
                f"Parabéns! Você completou {summary['completion_percentage']:.1f}% do curso!",
                "success"
            )
            
            self.ui.spinner("Gerando seu certificado", 2.0)
            
            self.certificate.preview_certificate(summary)
            self.logger.log_achievement("Certificado Gerado", summary['total_score'])
            
            self.ui.card(
                "Certificado Gerado com Sucesso!",
                "• Arquivo HTML criado\n"
                "• Aberto no seu navegador\n"
                "• Use Ctrl+P para imprimir ou salvar como PDF\n"
                "• Compartilhe sua conquista!",
                "🏆",
                "success"
            )
        else:
            required = 80
            current = summary['completion_percentage']
            missing = required - current
            
            self.ui.alert(
                f"Você precisa completar {required}% do curso para gerar o certificado.",
                "warning"
            )
            
            self.ui.card(
                "Requisitos para Certificado",
                f"Progresso atual: {current:.1f}%\n"
                f"Necessário: {required}%\n"
                f"Faltam: {missing:.1f}%\n"
                f"Módulos completos: {summary['modules_completed']}/11",
                "📋",
                "info"
            )
            
            # Barra de progresso para certificado
            self.ui.progress_bar(
                int(current),
                required,
                "Progresso para o Certificado",
                30
            )
        
        self.utils.pausar()
    
    def _mostrar_galeria_mini_projetos(self) -> None:
        """Exibe galeria completa de mini projetos"""
        self.utils.limpar_tela()
        
        self.ui.header("GALERIA DE MINI PROJETOS", "Todos os projetos práticos do curso", "🚀")
        
        # Definição de todos os mini projetos organizados
        mini_projetos_data = {
            "básicos": {
                "titulo": "🌱 PROJETOS BÁSICOS (Módulos 1-6)",
                "projetos": [
                    {
                        "modulo": "modulo_1",
                        "numero": "1",
                        "nome": "Cartão de Apresentação Python",
                        "descricao": "Seu primeiro programa criando um cartão digital personalizado",
                        "tecnologias": "Print, Variáveis, Strings",
                        "aplicacoes": "Sites pessoais, perfis, assinaturas digitais",
                        "pontos": 50
                    },
                    {
                        "modulo": "modulo_2", 
                        "numero": "2",
                        "nome": "Gerador de Mensagens Motivacionais",
                        "descricao": "Sistema que cria mensagens inspiradoras personalizadas",
                        "tecnologias": "Print, Input, Concatenação",
                        "aplicacoes": "Apps de bem-estar, coaching, gamificação",
                        "pontos": 50
                    },
                    {
                        "modulo": "modulo_3",
                        "numero": "3", 
                        "nome": "Calculadora de Variáveis Inteligente",
                        "descricao": "Calculadora que armazena e reutiliza valores em memória",
                        "tecnologias": "Variáveis, Operações, Reutilização",
                        "aplicacoes": "Sistemas contábeis, calculadoras avançadas",
                        "pontos": 50
                    },
                    {
                        "modulo": "modulo_4",
                        "numero": "4",
                        "nome": "Conversor Universal de Tipos",
                        "descricao": "Sistema completo de conversão entre diferentes tipos de dados",
                        "tecnologias": "Type casting, Validação, Tipos de dados",
                        "aplicacoes": "ETL, importação de dados, APIs",
                        "pontos": 55
                    },
                    {
                        "modulo": "modulo_5",
                        "numero": "5", 
                        "nome": "Quiz Interativo Personalizado",
                        "descricao": "Sistema de perguntas e respostas com feedback inteligente",
                        "tecnologias": "Input, Validação, Feedback",
                        "aplicacoes": "E-learning, testes, gamificação educativa",
                        "pontos": 60
                    },
                    {
                        "modulo": "modulo_6",
                        "numero": "6",
                        "nome": "Calculadora Científica Avançada", 
                        "descricao": "Calculadora com funções matemáticas complexas e constantes",
                        "tecnologias": "Math, Operações avançadas, Constantes",
                        "aplicacoes": "Engenharia, ciência, pesquisa acadêmica",
                        "pontos": 65
                    }
                ]
            },
            "intermediários": {
                "titulo": "🎓 PROJETOS INTERMEDIÁRIOS (Módulos 12-17)",
                "projetos": [
                    {
                        "modulo": "modulo_12",
                        "numero": "12",
                        "nome": "Sistema de Contatos Inteligente",
                        "descricao": "CRM completo para gerenciamento de contatos empresariais",
                        "tecnologias": "Dicionários, Sets, Estruturas complexas",
                        "aplicacoes": "CRM, agenda corporativa, networking",
                        "pontos": 70
                    },
                    {
                        "modulo": "modulo_13", 
                        "numero": "13",
                        "nome": "Processador de Dados Avançado",
                        "descricao": "Sistema de análise usando funções lambda e processamento paralelo",
                        "tecnologias": "Lambda, map(), filter(), *args, **kwargs",
                        "aplicacoes": "Business intelligence, análise de vendas, ETL",
                        "pontos": 70
                    },
                    {
                        "modulo": "modulo_14",
                        "numero": "14",
                        "nome": "Analisador de Logs Inteligente", 
                        "descricao": "Sistema de análise de logs usando comprehensions avançadas",
                        "tecnologias": "List/Dict/Set Comprehensions, Condicionais",
                        "aplicacoes": "DevOps, monitoramento, análise de segurança",
                        "pontos": 75
                    },
                    {
                        "modulo": "modulo_15",
                        "numero": "15",
                        "nome": "Sistema de Backup Inteligente",
                        "descricao": "Backup automatizado com compressão e versionamento",
                        "tecnologias": "Arquivos, JSON, CSV, ZIP, Diretórios",
                        "aplicacoes": "Backup empresarial, versionamento, arquivamento",
                        "pontos": 75
                    },
                    {
                        "modulo": "modulo_16",
                        "numero": "16", 
                        "nome": "Sistema de Monitoramento Robusto",
                        "descricao": "Monitor de sistema com tratamento avançado de erros",
                        "tecnologias": "Try/except, finally, custom exceptions",
                        "aplicacoes": "IoT, monitoramento de servidores, sistemas críticos",
                        "pontos": 80
                    },
                    {
                        "modulo": "modulo_17",
                        "numero": "17",
                        "nome": "Framework de Plugins Modular",
                        "descricao": "Sistema extensível com carregamento dinâmico de plugins",
                        "tecnologias": "Imports dinâmicos, módulos, packages",
                        "aplicacoes": "Editores, IDEs, sistemas extensíveis",
                        "pontos": 80
                    }
                ]
            },
            "avançados": {
                "titulo": "🚀 PROJETOS AVANÇADOS (Módulos 18-23)",
                "projetos": [
                    {
                        "modulo": "modulo_18",
                        "numero": "18",
                        "nome": "Sistema de Gestão de Funcionários",
                        "descricao": "Sistema completo de RH usando programação orientada a objetos",
                        "tecnologias": "Classes, objetos, encapsulamento, métodos",
                        "aplicacoes": "RH corporativo, gestão empresarial, HRIS",
                        "pontos": 85
                    },
                    {
                        "modulo": "modulo_19",
                        "numero": "19", 
                        "nome": "Sistema de Jogos RPG",
                        "descricao": "Engine de RPG com herança e polimorfismo completos",
                        "tecnologias": "Herança, polimorfismo, classes abstratas",
                        "aplicacoes": "Game development, simulações, hierarquias complexas",
                        "pontos": 90
                    },
                    {
                        "modulo": "modulo_20",
                        "numero": "20",
                        "nome": "Sistema de Cache Inteligente",
                        "descricao": "Cache avançado com decorators e context managers",
                        "tecnologias": "Decorators, context managers, functools",
                        "aplicacoes": "Otimização web, APIs de alta performance",
                        "pontos": 90
                    },
                    {
                        "modulo": "modulo_21",
                        "numero": "21",
                        "nome": "Pipeline de Processamento de Dados",
                        "descricao": "Pipeline eficiente para big data usando generators",
                        "tecnologias": "Generators, yield, iterator protocol",
                        "aplicacoes": "Big data, ETL, processamento de streams",
                        "pontos": 95
                    },
                    {
                        "modulo": "modulo_22", 
                        "numero": "22",
                        "nome": "Analisador de Logs Avançado",
                        "descricao": "Sistema completo de análise usando expressões regulares",
                        "tecnologias": "Regex patterns, groups, lookahead",
                        "aplicacoes": "Segurança, auditoria, monitoramento avançado",
                        "pontos": 95
                    },
                    {
                        "modulo": "modulo_23",
                        "numero": "23",
                        "nome": "Profiler de Performance",
                        "descricao": "Sistema completo de profiling e debugging avançado",
                        "tecnologias": "Profiling, tracing, memory analysis",
                        "aplicacoes": "Otimização de código, debugging profissional",
                        "pontos": 100
                    }
                ]
            }
        }
        
        # Obtém projetos completos
        completed_mini_projects = self.progress.progress_data.get("mini_projetos_completos", [])
        
        # Exibe estatísticas gerais
        total_projects = sum(len(cat["projetos"]) for cat in mini_projetos_data.values())
        completed_count = len(completed_mini_projects)
        completion_percentage = (completed_count / total_projects) * 100 if total_projects > 0 else 0
        
        self.ui.card(
            "Estatísticas da Galeria",
            f"📊 Projetos Completos: {completed_count}/{total_projects}\n"
            f"📈 Progresso: {completion_percentage:.1f}%\n"
            f"💰 Pontos Disponíveis: {sum(sum(p['pontos'] for p in cat['projetos']) for cat in mini_projetos_data.values())} pts\n"
            f"🏆 Pontos Conquistados: {sum(p['pontos'] for cat in mini_projetos_data.values() for p in cat['projetos'] if p['modulo'] + '_mini_projeto' in completed_mini_projects)} pts",
            "📊",
            "info"
        )
        
        print("\n🎯 MENU DE OPÇÕES:")
        print("1. 📋 Ver Todos os Projetos")
        print("2. 🌱 Só Projetos Básicos")
        print("3. 🎓 Só Projetos Intermediários") 
        print("4. 🚀 Só Projetos Avançados")
        print("5. ✅ Só Projetos Completos")
        print("6. ⏳ Só Projetos Pendentes")
        print("7. 🔥 Executar um Projeto Específico")
        print("0. 🔙 Voltar")
        
        while True:
            try:
                escolha = input("\n👉 Sua escolha (0-7): ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._exibir_projetos_categoria(mini_projetos_data, "todos", completed_mini_projects)
                elif escolha == "2":
                    self._exibir_projetos_categoria({"básicos": mini_projetos_data["básicos"]}, "básicos", completed_mini_projects)
                elif escolha == "3":
                    self._exibir_projetos_categoria({"intermediários": mini_projetos_data["intermediários"]}, "intermediários", completed_mini_projects)
                elif escolha == "4":
                    self._exibir_projetos_categoria({"avançados": mini_projetos_data["avançados"]}, "avançados", completed_mini_projects)
                elif escolha == "5":
                    self._exibir_projetos_filtrados(mini_projetos_data, completed_mini_projects, True)
                elif escolha == "6":
                    self._exibir_projetos_filtrados(mini_projetos_data, completed_mini_projects, False)
                elif escolha == "7":
                    self._executar_projeto_especifico(mini_projetos_data)
                else:
                    print("❌ Opção inválida!")
                    continue
                    
                input("\n⏯️ Pressione ENTER para voltar ao menu...")
                self.utils.limpar_tela()
                self.ui.header("GALERIA DE MINI PROJETOS", "Todos os projetos práticos do curso", "🚀")
                
            except KeyboardInterrupt:
                break
    
    def _exibir_projetos_categoria(self, categorias_data: dict, nome_categoria: str, completed_projects: list) -> None:
        """Exibe projetos de uma categoria específica"""
        self.utils.limpar_tela()
        
        titulo = f"PROJETOS {nome_categoria.upper()}" if nome_categoria != "todos" else "TODOS OS PROJETOS"
        self.ui.header(titulo, "Detalhes dos projetos", "📋")
        
        for categoria, dados in categorias_data.items():
            print(f"\n{dados['titulo']}")
            print("=" * 60)
            
            for projeto in dados["projetos"]:
                modulo_key = f"{projeto['modulo']}_mini_projeto"
                status = "✅" if modulo_key in completed_projects else "⏳"
                
                self.ui.card(
                    f"{status} {projeto['nome']} (Módulo {projeto['numero']})",
                    f"📝 {projeto['descricao']}\n"
                    f"🛠️ Tecnologias: {projeto['tecnologias']}\n"
                    f"🎯 Aplicações: {projeto['aplicacoes']}\n"
                    f"⭐ Pontos: {projeto['pontos']}",
                    "🚀",
                    "success" if modulo_key in completed_projects else "info"
                )
    
    def _exibir_projetos_filtrados(self, categorias_data: dict, completed_projects: list, mostrar_completos: bool) -> None:
        """Exibe projetos filtrados por status de conclusão"""
        self.utils.limpar_tela()
        
        titulo = "PROJETOS COMPLETOS" if mostrar_completos else "PROJETOS PENDENTES"
        icon = "✅" if mostrar_completos else "⏳"
        self.ui.header(titulo, "Filtrados por status", icon)
        
        projetos_encontrados = 0
        
        for categoria, dados in categorias_data.items():
            projetos_categoria = []
            
            for projeto in dados["projetos"]:
                modulo_key = f"{projeto['modulo']}_mini_projeto"
                is_completed = modulo_key in completed_projects
                
                if is_completed == mostrar_completos:
                    projetos_categoria.append(projeto)
                    projetos_encontrados += 1
            
            if projetos_categoria:
                print(f"\n{dados['titulo']}")
                print("=" * 60)
                
                for projeto in projetos_categoria:
                    status_icon = "✅" if mostrar_completos else "⏳"
                    self.ui.card(
                        f"{status_icon} {projeto['nome']} (Módulo {projeto['numero']})",
                        f"📝 {projeto['descricao']}\n"
                        f"🛠️ Tecnologias: {projeto['tecnologias']}\n"
                        f"🎯 Aplicações: {projeto['aplicacoes']}\n"
                        f"⭐ Pontos: {projeto['pontos']}",
                        "🚀",
                        "success" if mostrar_completos else "warning"
                    )
        
        if projetos_encontrados == 0:
            mensagem = "Parabéns! Você completou todos os projetos!" if not mostrar_completos else "Você ainda não completou nenhum projeto."
            self.ui.alert(mensagem, "success" if not mostrar_completos else "info")
    
    def _executar_projeto_especifico(self, categorias_data: dict) -> None:
        """Permite executar um projeto específico"""
        self.utils.limpar_tela()
        self.ui.header("EXECUTAR PROJETO", "Escolha um projeto para executar", "🔥")
        
        # Lista todos os projetos numerados
        print("📋 PROJETOS DISPONÍVEIS:")
        all_projects = []
        counter = 1
        
        for categoria, dados in categorias_data.items():
            print(f"\n{dados['titulo']}")
            for projeto in dados["projetos"]:
                print(f"  {counter:2d}. {projeto['nome']} (Módulo {projeto['numero']})")
                all_projects.append(projeto)
                counter += 1
        
        print(f"\n  0. 🔙 Voltar")
        
        try:
            escolha = int(input("\n👉 Número do projeto para executar (0 para voltar): "))
            
            if escolha == 0:
                return
            elif 1 <= escolha <= len(all_projects):
                projeto_escolhido = all_projects[escolha - 1]
                modulo_numero = projeto_escolhido["numero"]
                
                # Executa o módulo correspondente
                if modulo_numero in self.menu_options:
                    self.ui.alert(f"🚀 Executando: {projeto_escolhido['nome']}", "info")
                    funcao, _ = self.menu_options[modulo_numero]
                    funcao()
                else:
                    self.ui.alert("❌ Módulo não disponível ainda!", "error")
            else:
                self.ui.alert("❌ Número inválido!", "error")
                
        except ValueError:
            self.ui.alert("❌ Digite um número válido!", "error")
        except KeyboardInterrupt:
            return
    
    def _mudar_tema(self) -> None:
        """Permite ao usuário mudar o tema visual"""
        self.utils.limpar_tela()
        
        self.ui.header("PERSONALIZAÇÃO VISUAL", "Escolha seu tema favorito", "🎨")
        
        themes = self.theme_manager.list_themes()
        
        self.ui.card(
            "Temas Disponíveis",
            "• python - Azul e amarelo clássico\n"
            "• matrix - Verde estilo Matrix\n"
            "• sunset - Cores quentes do pôr do sol",
            "🎭",
            "info"
        )
        
        print("\nTemas disponíveis:")
        for i, theme in enumerate(themes, 1):
            theme_data = self.theme_manager.get_theme(theme)
            print(f"{i}. {theme_data['name']}")
        
        print("0. Voltar ao menu")
        
        try:
            choice = input("\n👉 Escolha um tema (número): ").strip()
            
            if choice == "0":
                return
            
            theme_index = int(choice) - 1
            if 0 <= theme_index < len(themes):
                selected_theme = themes[theme_index]
                theme_data = self.theme_manager.get_theme(selected_theme)
                
                self.ui.alert(f"Tema '{theme_data['name']}' selecionado!", "success")
                
                # Aqui você poderia implementar a mudança de tema
                # Por exemplo, salvando a preferência nas configurações
                self.config.set('display.theme', selected_theme)
                
                self.ui.card(
                    "Tema Aplicado",
                    f"O tema '{theme_data['name']}' foi aplicado com sucesso!\n"
                    "Reinicie o programa para ver as mudanças completas.",
                    "✨",
                    "success"
                )
            else:
                self.ui.alert("Opção inválida!", "error")
        
        except ValueError:
            self.ui.alert("Digite apenas números!", "error")
        except KeyboardInterrupt:
            return
        
        self.utils.pausar()
    
    def _mostrar_ajuda(self) -> None:
        """Mostra ajuda e atalhos disponíveis"""
        self.utils.limpar_tela()
        self.utils.titulo("❓ AJUDA E INFORMAÇÕES")
        
        print("📚 SOBRE O CURSO:")
        print(f"   Versão: {self.config.get('course.version')}")
        print(f"   Autor: {self.config.get('course.author')}")
        print("\n✨ RECURSOS:")
        print("   • Sistema de pontuação e conquistas")
        print("   • Modo revisão para praticar")
        print("   • Glossário com termos importantes")
        print("   • Certificado de conclusão")
        print("   • Progresso salvo automaticamente")
        
        print("\n" + self.shortcuts.help_text)
        
        print("\n💡 DICAS:")
        print("   • Complete os módulos em ordem")
        print("   • Use o modo revisão para fixar o conteúdo")
        print("   • Consulte o glossário quando tiver dúvidas")
        print("   • Pratique os exercícios com calma")
        
        self.utils.pausar()
    
    def _usar_assistente(self) -> None:
        """Abre o assistente de ajuda com IA offline"""
        # Detecta módulo atual que o aluno está estudando
        modulo_atual = ""
        for i in range(1, 27):
            module_id = f"modulo_{i}"
            if module_id in self.progress.progress_data['modules_progress']:
                status = self.progress.progress_data['modules_progress'][module_id]
                if not status.get('completed', False) and status.get('attempts', 0) > 0:
                    modulo_atual = f"Módulo {i}: {self.menu_options.get(str(i), ('', ''))[1]}"
                    break
        
        # Se não encontrou módulo em progresso, pega o próximo não completo
        if not modulo_atual:
            for i in range(1, 27):
                module_id = f"modulo_{i}"
                if module_id not in self.progress.progress_data['modules_completed']:
                    modulo_atual = f"Módulo {i}: {self.menu_options.get(str(i), ('', ''))[1]}"
                    break
        
        # Inicia sessão do assistente
        self.tutor.sessao_ajuda(modulo_atual)
    
    def _mostrar_dashboard_analytics(self) -> None:
        """Exibe dashboard de análise de aprendizagem"""
        # Registra atividade do dia
        self.analytics.registrar_atividade_diaria()
        
        # Exibe dashboard
        self.analytics.exibir_dashboard(self.ui)
        
        print("\n🎯 AÇÕES DISPONÍVEIS:")
        print("1. 📊 Ver estatísticas detalhadas")
        print("2. 💡 Receber recomendações personalizadas")
        print("3. 🎯 Analisar padrões de erro")
        print("0. 🔙 Voltar ao menu")
        
        try:
            acao = input("\n👉 Escolha: ").strip()
            
            if acao == "1":
                relatorio = self.analytics.gerar_relatorio_completo()
                
                self.ui.section("ESTATÍSTICAS DETALHADAS", "📈")
                print(f"🎯 Taxa de sucesso média: {self._calcular_taxa_media():.1f}%")
                print(f"⏱️ Tempo médio por módulo: {self._calcular_tempo_medio_geral()} min")
                print(f"🔥 Streak mais longo: {relatorio['resumo_geral'].get('maior_streak', 0)} dias")
                
            elif acao == "2":
                insights = self.analytics.gerar_insights_personalizados()
                if insights:
                    self.ui.section("RECOMENDAÇÕES PERSONALIZADAS", "💡")
                    for insight in insights:
                        self.ui.alert(f"{insight['descricao']}\n💡 {insight['sugestao']}", "info")
                else:
                    print("📊 Continue estudando para gerar mais insights!")
            
            elif acao == "3":
                if self.analytics.analytics_data["error_patterns"]:
                    self.ui.section("ANÁLISE DE ERROS", "🔍")
                    for erro, count in list(self.analytics.analytics_data["error_patterns"].items())[:5]:
                        print(f"• {erro}: {count} ocorrências")
                        # Sugestão baseada no erro
                        if "NameError" in erro:
                            print("  💡 Dica: Sempre declare variáveis antes de usar")
                        elif "SyntaxError" in erro:
                            print("  💡 Dica: Verifique parênteses, aspas e dois pontos")
                        elif "IndentationError" in erro:
                            print("  💡 Dica: Use 4 espaços para indentação")
                else:
                    print("🎉 Nenhum erro registrado ainda!")
        
        except KeyboardInterrupt:
            pass
        
        self.utils.pausar()
    
    def _mostrar_perfil_gamer(self) -> None:
        """Exibe perfil de gamificação do usuário"""
        # Atualiza streak diário
        streak_info = self.gamification.verificar_e_atualizar_streak()
        
        if streak_info["manteve_streak"]:
            self.ui.alert(f"🔥 Streak mantido! {streak_info['streak_atual']} dias consecutivos!", "success")
        elif streak_info["quebrou_streak"]:
            self.ui.alert(f"💔 Streak quebrado... Vamos recomeçar!", "warning")
        
        # Exibe perfil
        self.gamification.exibir_perfil_gamer(self.ui)
        
        print("\n🎮 AÇÕES GAMER:")
        print("1. 🏪 Loja de Power-ups")
        print("2. 🎯 Desafio Diário")
        print("3. 🏆 Ver Todas as Conquistas")
        print("4. 📈 Histórico de XP")
        print("0. 🔙 Voltar ao menu")
        
        try:
            acao = input("\n👉 Escolha: ").strip()
            
            if acao == "1":
                self._mostrar_loja_powerups()
            elif acao == "2":
                self._mostrar_desafio_diario()
            elif acao == "3":
                self._mostrar_todas_conquistas()
            elif acao == "4":
                self._mostrar_historico_xp()
        
        except KeyboardInterrupt:
            pass
        
        self.utils.pausar()
    
    def _abrir_editor_codigo(self) -> None:
        """Abre o editor/playground de código"""
        self.code_playground.start_playground(self.ui)
    
    def _abrir_demos_interativas(self) -> None:
        """Abre sistema de demos interativas"""
        self.interactive_demos.start_demo_session()
    
    def _abrir_sincronizacao(self) -> None:
        """Abre sistema de sincronização"""
        self.sync_manager.show_sync_menu(self.ui)
    
    def _abrir_exercicios_adaptativos(self) -> None:
        """Abre sistema de exercícios adaptativos"""
        self.ui.header("EXERCÍCIOS ADAPTATIVOS", "Treinamento Personalizado", "🎯")
        
        print("🎯 OPÇÕES:")
        print("1. 📚 Sessão de Prática Mista")
        print("2. 🎪 Focar em Áreas Fracas")
        print("3. 📖 Revisões Pendentes")
        print("4. 📊 Relatório de Performance")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self.adaptive_session.start_session("mixed")
        elif choice == "2":
            self.adaptive_session.start_session("weak_areas")
        elif choice == "3":
            self.adaptive_session.start_session("reviews")
        elif choice == "4":
            self._mostrar_relatorio_exercicios()
    
    def _abrir_debug_visual(self) -> None:
        """Abre sistema de debug visual"""
        self.debug_session.start_debug_session()
    
    def _mostrar_relatorio_exercicios(self) -> None:
        """Mostra relatório de performance dos exercícios adaptativos"""
        report = self.adaptive_generator.get_performance_report()
        
        if report["status"] == "no_data":
            self.ui.alert("📭 Nenhum exercício realizado ainda", "info")
            return
        
        self.ui.header("RELATÓRIO DE EXERCÍCIOS", "Sua Performance", "📊")
        
        # Estatísticas gerais
        self.ui.card(
            "Performance Geral",
            f"Exercícios Realizados: {report['total_exercises']}\n"
            f"Taxa de Acerto: {report['overall_accuracy']:.1f}%\n"
            f"Sequência Atual: {report['recent_streak']} acertos\n"
            f"Revisões Pendentes: {report['due_reviews']}",
            "📈",
            "success" if report['overall_accuracy'] >= 70 else "warning"
        )
        
        # Performance por tópico
        if report['topic_performance']:
            print("\n📚 PERFORMANCE POR TÓPICO:")
            for topic, stats in report['topic_performance'].items():
                accuracy = stats['accuracy']
                status = "✅" if accuracy >= 70 else "⚠️" if accuracy >= 50 else "❌"
                print(f"{status} {topic.replace('_', ' ').title()}: {stats['correct']}/{stats['total']} ({accuracy:.0f}%)")
        
        # Áreas para focar
        if report['recommended_focus']:
            print(f"\n💡 ÁREAS RECOMENDADAS PARA FOCO:")
            for topic in report['recommended_focus']:
                print(f"  • {topic.replace('_', ' ').title()}")
        
        self.utils.pausar()
    
    def _mostrar_loja_powerups(self) -> None:
        """Mostra loja de power-ups"""
        self.ui.section("LOJA DE POWER-UPS", "🏪")
        
        power_ups = self.gamification.obter_power_ups_disponiveis()
        moedas_atual = self.gamification.game_data["moedas"]
        
        print(f"💰 Suas moedas: {moedas_atual}")
        print()
        
        for i, power_up in enumerate(power_ups, 1):
            status = "✅" if moedas_atual >= power_up["custo"] else "❌"
            print(f"{i}. {power_up['nome']} - {power_up['custo']} moedas {status}")
            print(f"   {power_up['descricao']}")
            print()
        
        try:
            escolha = int(input("Comprar qual power-up? (0 para cancelar): ")) - 1
            if 0 <= escolha < len(power_ups):
                power_up = power_ups[escolha]
                if self.gamification.comprar_power_up(power_up["id"]):
                    self.ui.alert(f"✅ {power_up['nome']} comprado com sucesso!", "success")
                else:
                    self.ui.alert("❌ Moedas insuficientes!", "error")
        except ValueError:
            pass
    
    def _mostrar_desafio_diario(self) -> None:
        """Mostra desafio diário"""
        desafio = self.gamification.criar_desafio_diario()
        
        self.ui.card(
            desafio["titulo"],
            f"{desafio['descricao']}\n\n"
            f"🎯 Meta: {desafio['meta']}\n"
            f"🏆 Recompensa: {desafio['recompensa_xp']} XP + {desafio['recompensa_moedas']} moedas",
            "🎯",
            "info"
        )
    
    def _mostrar_todas_conquistas(self) -> None:
        """Mostra todas as conquistas disponíveis e desbloqueadas"""
        self.ui.section("TODAS AS CONQUISTAS", "🏆")
        
        badges_desbloqueados = [b["id"] for b in self.gamification.game_data["badges_desbloqueados"]]
        
        for badge in BadgeType:
            status = "✅" if badge.name in badges_desbloqueados else "🔒"
            print(f"{status} {badge.value[0]} {badge.value[1]}")
            print(f"   {badge.value[2]}")
            print()
    
    def _mostrar_historico_xp(self) -> None:
        """Mostra histórico de ganho de XP"""
        historico = self.gamification.game_data.get("historico_xp", [])
        
        if historico:
            self.ui.section("HISTÓRICO DE XP", "📈")
            for entrada in historico[-10:]:  # Últimas 10
                timestamp = datetime.fromisoformat(entrada["timestamp"]).strftime("%d/%m %H:%M")
                print(f"{timestamp} - +{entrada['quantidade']} XP - {entrada['motivo']}")
        else:
            print("📭 Histórico vazio")
    
    def _calcular_taxa_media(self) -> float:
        """Calcula taxa de sucesso média"""
        total_modulos = len(self.progress.progress_data["modules_completed"])
        if total_modulos == 0:
            return 0.0
        
        total_tentativas = 0
        total_sucessos = 0
        
        for modulo_id in self.progress.progress_data["modules_completed"]:
            modulo_data = self.progress.progress_data["modules_progress"].get(modulo_id, {})
            tentativas = modulo_data.get("attempts", 1)
            total_tentativas += tentativas
            total_sucessos += 1  # Módulo foi completado
        
        return (total_sucessos / total_tentativas) * 100 if total_tentativas > 0 else 0.0
    
    def _calcular_tempo_medio_geral(self) -> int:
        """Calcula tempo médio geral em minutos"""
        total_tempo = 0
        total_modulos = 0
        
        for modulo_data in self.progress.progress_data["modules_progress"].values():
            if modulo_data.get("completed"):
                total_tempo += modulo_data.get("time_spent", 0)
                total_modulos += 1
        
        return (total_tempo // 60) if total_modulos > 0 else 0
    
    def _resetar_progresso(self) -> None:
        """Reseta todo o progresso do usuário com confirmação"""
        self.utils.limpar_tela()
        self.ui.header("RESETAR PROGRESSO", "⚠️ ATENÇÃO! Esta ação é irreversível!", "🗑️")
        
        summary = self.progress.get_progress_summary()
        
        # Mostra informações do progresso atual
        self.ui.card(
            "Progresso Atual que será PERDIDO",
            f"👤 Usuário: {summary['user_name']}\n"
            f"📈 Progresso: {summary['completion_percentage']:.1f}%\n"
            f"📚 Módulos Completos: {summary['modules_completed']}/{summary['total_modules']}\n"
            f"🏆 Pontuação Total: {summary['total_score']} pontos\n"
            f"🎯 Conquistas: {summary['achievements']} desbloqueadas",
            "📊",
            "warning"
        )
        
        self.ui.alert(
            "⚠️ AVISO: Todos os dados serão perdidos permanentemente!",
            "error"
        )
        
        print("🤔 MOTIVOS COMUNS PARA RESETAR:")
        print("• 👥 Múltiplos usuários no mesmo computador")
        print("• 🔄 Quero refazer o curso desde o início")
        print("• 📊 Dados corrompidos ou inconsistentes")
        print("• 🎯 Começar com metodologia diferente")
        
        print("\n💡 ALTERNATIVAS MENOS DRÁSTICAS:")
        print("• 🔄 Use o Modo Revisão para praticar")
        print("• 📂 Faça backup manual dos dados")
        print("• 👤 Crie outro perfil de usuário no sistema")
        
        self.ui.divider("─", "CONFIRMAÇÃO")
        
        try:
            # Primeira confirmação
            print("🔐 ETAPA 1: Confirmação básica")
            confirma1 = input("Digite 'RESETAR' (em maiúsculas) para continuar: ").strip()
            
            if confirma1 != "RESETAR":
                self.ui.alert("❌ Operação cancelada. Progresso mantido.", "info")
                self.utils.pausar()
                return
            
            # Segunda confirmação com nome do usuário
            print("\n🔐 ETAPA 2: Confirmação com nome")
            if summary['user_name']:
                nome_confirmacao = input(f"Digite o nome '{summary['user_name']}' para confirmar: ").strip()
                if nome_confirmacao != summary['user_name']:
                    self.ui.alert("❌ Nome incorreto. Operação cancelada.", "error")
                    self.utils.pausar()
                    return
            
            # Terceira confirmação final
            print("\n🔐 ETAPA 3: Confirmação final")
            print("⚠️ ÚLTIMA CHANCE! Esta ação é IRREVERSÍVEL!")
            confirma_final = input("Digite 'SIM' para resetar DEFINITIVAMENTE: ").strip().upper()
            
            if confirma_final != "SIM":
                self.ui.alert("❌ Operação cancelada. Progresso mantido.", "info")
                self.utils.pausar()
                return
            
            # Execução do reset
            self.ui.spinner("Resetando todos os dados", 3.0)
            
            # Reset do progresso
            self.progress.reset_progress()
            
            # Log da ação
            self.logger.log_user_action("Progresso resetado pelo usuário")
            
            # Feedback visual
            self.utils.limpar_tela()
            self.ui.alert("✅ PROGRESSO RESETADO COM SUCESSO!", "success")
            
            self.ui.card(
                "Reset Concluído",
                "• ✅ Todos os módulos marcados como não concluídos\n"
                "• ✅ Pontuação zerada\n"
                "• ✅ Conquistas removidas\n"
                "• ✅ Estatísticas de tempo resetadas\n"
                "• ✅ Nome de usuário removido\n"
                "• ✅ Histórico limpo",
                "🎯",
                "success"
            )
            
            print("\n🎉 RECOMEÇO TOTAL!")
            print("Na próxima execução, você será tratado como um novo usuário.")
            print("Poderá inserir um novo nome e começar sua jornada do zero!")
            
            print("\n🚀 DICAS PARA O RECOMEÇO:")
            print("• 📚 Aproveite para revisar conceitos que tinha dúvidas")
            print("• 🎯 Estabeleça metas de estudo diferentes")
            print("• ⏰ Experimente ritmos de aprendizado diferentes")
            print("• 📝 Tome notas durante o curso")
            
            self.ui.divider("─")
            print("🏁 Pressione ENTER para sair e reiniciar...")
            input()
            
            # Força saída para reinicialização
            sys.exit(0)
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Operação cancelada pelo usuário (Ctrl+C)")
            self.ui.alert("❌ Reset cancelado. Progresso mantido.", "info")
            self.utils.pausar()
            return
        except Exception as e:
            print(f"\n❌ Erro durante o reset: {e}")
            self.ui.alert("❌ Erro no reset. Progresso mantido por segurança.", "error")
            self.utils.pausar()
            return
    
    def _sair_do_curso(self) -> bool:
        """Finaliza o curso e salva progresso"""
        # Calcula tempo da sessão
        session_duration = int((datetime.now() - self.session_start).total_seconds())
        
        # Salva progresso final
        self.progress.save_progress()
        
        # Log de fim de sessão
        self.logger.log_session_end(session_duration)
        
        # Mensagem de despedida personalizada
        summary = self.progress.get_progress_summary()
        
        print("\n" + "=" * 50)
        if summary['user_name']:
            print(f"👋 Até logo, {summary['user_name']}!")
        else:
            print("👋 Obrigado por estudar Python conosco!")
        
        if summary['completion_percentage'] == 100:
            print("🎉 Parabéns por completar todo o curso!")
        elif summary['completion_percentage'] > 0:
            print(f"📊 Você completou {summary['completion_percentage']:.1f}% do curso.")
            print("Continue praticando e volte sempre que quiser!")
        
        print("🚀 Boa sorte na sua jornada Python!")
        print("=" * 50)
        
        return False
    
    def menu_principal(self) -> None:
        """Menu principal do curso"""
        # Verifica se é primeira vez
        self._check_first_time_user()
        
        while True:
            self.exibir_menu()
            
            # Processa atalhos de teclado
            print("\n👉 Escolha uma opção: ", end='', flush=True)
            try:
                escolha = input().strip()
            except KeyboardInterrupt:
                # Re-lança a exceção para ser tratada no nível superior
                raise
            
            if not self.executar_opcao(escolha):
                break


def main() -> None:
    """Função principal do programa"""
    course = None
    try:
        course = PythonCourse()
        course.menu_principal()
    except KeyboardInterrupt:
        # Tratamento para Ctrl+C
        print("\n\n⚠️  Interrompido pelo usuário (Ctrl+C)")
        
        if course:
            try:
                # Salva o progresso antes de sair
                print("💾 Salvando seu progresso...")
                course.progress.save_progress()
                
                # Log de interrupção
                session_duration = int((datetime.now() - course.session_start).total_seconds())
                course.logger.log_user_action("Sessão interrompida com Ctrl+C")
                course.logger.log_session_end(session_duration)
                
                # Mensagem de despedida
                summary = course.progress.get_progress_summary()
                if summary['user_name']:
                    print(f"\n👋 Até logo, {summary['user_name']}!")
                print("✅ Seu progresso foi salvo com segurança.")
                print("🔄 Você pode continuar de onde parou na próxima vez!")
                
            except Exception as e:
                print(f"⚠️  Erro ao salvar progresso: {e}")
        
        print("\n🐍 Obrigado por usar o Curso de Python!")
        sys.exit(0)
    except Exception as e:
        # Tratamento para outros erros
        print(f"\n❌ Erro inesperado: {e}")
        if course:
            try:
                course.progress.save_progress()
                print("💾 Progresso salvo antes de sair.")
            except:
                pass
        sys.exit(1)


if __name__ == "__main__":
    main()