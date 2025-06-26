#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Controlador do Curso
Gerencia a lógica principal de execução do curso
"""

import time
from typing import Dict, Any, Optional, Callable, Tuple
from datetime import datetime

from ..progress_manager import ProgressManager
from ..visual_feedback import VisualFeedback
from ..logger import CourseLogger
from ..gamification_system import GamificationSystem
from ..ui_components import UIComponents
from ..error_tracker import ErrorTracker
from ..review_mode import ReviewMode
from ..glossary import Glossary
from ..certificate_generator import CertificateGenerator
from ..interactive_demos import InteractiveDemoSession
from ..adaptive_exercises import AdaptiveExerciseSession
from ..visual_debugger import DebugSession
from ..learning_analytics import LearningAnalytics
from ..exercises.interactive_exercises import InteractiveExerciseSession


class CourseController:
    """Controla a execução e lógica do curso"""
    
    def __init__(self, components: Dict[str, Any]):
        """Inicializa com componentes necessários"""
        self.progress = components['progress']
        self.visual = components['visual']
        self.logger = components['logger']
        self.gamification = components['gamification']
        self.ui = components['ui']
        self.error_tracker = components['error_tracker']
        self.review = components['review']
        self.glossary = components['glossary']
        self.certificate = components['certificate']
        self.interactive_demos = components['interactive_demos']
        self.adaptive_session = components['adaptive_session']
        self.debug_session = components['debug_session']
        self.analytics = components['analytics']
        self.tutor = components['tutor']
        self.progressive_projects = components.get('progressive_projects')
        self.methodical_debugging = components.get('methodical_debugging')
        
        # Novos componentes avançados
        self.advanced_analytics = components.get('advanced_analytics')
        self.analytics_dashboard = components.get('analytics_dashboard')
        self.connectivity_manager = components.get('connectivity_manager')
        self.offline_manager = components.get('offline_manager')
        self.offline_sync = components.get('offline_sync')
        
        # Code Review components
        self.code_analysis_engine = components.get('code_analysis_engine')
        self.code_review_dashboard = components.get('code_review_dashboard')
        self.exercise_code_reviewer = components.get('exercise_code_reviewer')
        
        # Error handler
        self.error_handler = components.get('error_handler')
        
        self.menu_options = components['menu_options']
        self.navigation = components.get('navigation')
    
    def execute_module(self, module_key: str) -> bool:
        """
        Executa um módulo do curso
        
        Args:
            module_key: Chave do módulo (ex: "1", "2", etc)
            
        Returns:
            True se deve continuar, False se deve sair
        """
        if module_key not in self.menu_options:
            return True
        
        module_id = f"modulo_{module_key}"
        nome_modulo = self.menu_options[module_key][1]
        
        # Adiciona à navegação se disponível
        if self.navigation:
            self.navigation.push(nome_modulo, f"Módulo {module_key}", level=1)
        
        # Log e marca início do módulo
        self.logger.log_module_start(module_id, nome_modulo)
        self.error_tracker.start_module(module_id)
        start_time = time.time()
        
        # Executa o módulo
        funcao, _ = self.menu_options[module_key]
        funcao()
        
        # Mostrar projeto graduais se disponível
        if self.progressive_projects and module_key.isdigit():
            module_number = int(module_key)
            if 1 <= module_number <= 30:
                self._show_progressive_project(module_number)
        
        # Remove da navegação ao terminar
        if self.navigation:
            self.navigation.pop()
        
        # Calcula tempo gasto
        time_spent = int(time.time() - start_time)
        self.progress.update_module_progress(module_id, time_spent, 1)
        
        # Verifica se o módulo foi realmente completado (não marca automaticamente)
        # A marcação como completo deve ser feita explicitamente pelo próprio módulo
        # quando o usuário termina todas as seções
        
        # Apenas atualiza estatísticas do error_tracker
        module_stats = self.error_tracker.end_module(module_id)
        
        return True
    
    def mark_module_completed(self, module_key: str) -> None:
        """
        Marca um módulo como completo explicitamente
        Deve ser chamado apenas quando o usuário termina todas as seções
        """
        module_id = f"modulo_{module_key}"
        
        # Verifica se já está completo
        if module_id in self.progress.progress_data["modules_completed"]:
            return
        
        # Marca como completo
        pontos = 100  # Pontos por completar módulo
        self.progress.mark_module_completed(module_id, pontos)
        self.visual.celebration()
        self.visual.add_score(pontos, "Módulo completo!")
        self.logger.log_module_completion(module_id, pontos, 0)
        
        # Sistema de gamificação
        xp_result = self.gamification.adicionar_xp(pontos, f"Módulo {module_key} completo")
        
        # Verifica badges por completar módulo
        badges_novos = self.gamification.verificar_conquistas_modulo(
            module_id, 
            sem_erros=True,  # Assumir sem erros se completou
            tempo_segundos=0
        )
        
        # Exibe notificações
        self._show_notifications(xp_result, badges_novos)
    
    def _show_progressive_project(self, module_number: int) -> None:
        """Mostra o passo do projeto gradual correspondente ao módulo"""
        try:
            print("\n" + "="*60)
            print("🚀 PROJETO PRÁTICO DO MÓDULO")
            print("="*60)
            
            choice = input("\nDeseja ver o projeto prático deste módulo? (s/N): ").strip().lower()
            if choice in ['s', 'sim', 'y', 'yes']:
                self.progressive_projects.show_project_step(module_number)
            else:
                print("Você pode acessar os projetos a qualquer momento no menu principal!")
                input("Pressione ENTER para continuar...")
                
        except Exception as e:
            self.logger.error(f"Erro ao mostrar projeto gradual: {e}")
            print("Erro temporário ao carregar projeto. Continuando...")
    
    def _show_projects_menu(self) -> None:
        """Mostra menu dos projetos graduais"""
        if not self.progressive_projects:
            print("❌ Sistema de projetos não disponível.")
            return
            
        while True:
            self.ui.clear_screen()
            self.ui.header("🚀 PROJETOS GRADUAIS", "Projetos Reais do Curso")
            
            print("📚 PROJETOS DISPONÍVEIS:")
            print("=" * 50)
            print("1. 📖 Sistema de Biblioteca Pessoal (Módulos 1-10)")
            print("2. 🛒 E-commerce Simples (Módulos 11-20)")
            print("3. 📊 API e Dashboard Analytics (Módulos 21-30)")
            print()
            print("4. 📈 Ver progresso geral dos projetos")
            print("5. 🎯 Ir para módulo específico")
            print("0. 🔙 Voltar ao menu principal")
            
            choice = input("\nEscolha uma opção: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._show_project_overview("biblioteca_pessoal", "Sistema de Biblioteca", 1, 10)
            elif choice == "2":
                self._show_project_overview("ecommerce_simples", "E-commerce Simples", 11, 20)
            elif choice == "3":
                self._show_project_overview("api_dashboard", "API Dashboard", 21, 30)
            elif choice == "4":
                self._show_all_projects_progress()
            elif choice == "5":
                self._go_to_specific_module()
            else:
                print("❌ Opção inválida!")
                input("Pressione ENTER para continuar...")
    
    def _show_project_overview(self, project_id: str, project_name: str, start_module: int, end_module: int):
        """Mostra visão geral de um projeto específico"""
        self.ui.clear_screen()
        self.ui.header(f"📋 {project_name.upper()}", f"Módulos {start_module}-{end_module}")
        
        progress = self.progressive_projects.user_progress[project_id]
        total_steps = len(self.progressive_projects.projects[project_id])
        completed = len(progress.completed_steps)
        completion_percentage = (completed / total_steps) * 100 if total_steps > 0 else 0
        
        print(f"📊 Progresso: {completed}/{total_steps} passos ({completion_percentage:.1f}%)")
        print(f"⏱️ Tempo gasto: {progress.total_time_spent} minutos")
        print(f"✅ Status: {'Completo' if progress.is_completed else 'Em andamento'}")
        print()
        
        print("📋 PASSOS DO PROJETO:")
        print("=" * 40)
        
        for i, step in enumerate(self.progressive_projects.projects[project_id]):
            status = "✅" if step.step_id in progress.completed_steps else "⏳"
            module_num = start_module + i
            print(f"{status} Módulo {module_num}: {step.title}")
        
        print("\n🎮 OPÇÕES:")
        print("1. Ver próximo passo")
        print("2. Ir para módulo específico")
        print("0. Voltar")
        
        choice = input("\nEscolha: ").strip()
        if choice == "1":
            next_module = start_module + progress.current_step
            if next_module <= end_module:
                self.progressive_projects.show_project_step(next_module)
            else:
                print("🎉 Projeto já foi completado!")
                input("Pressione ENTER...")
        elif choice == "2":
            try:
                module = int(input(f"Qual módulo ({start_module}-{end_module})? "))
                if start_module <= module <= end_module:
                    self.progressive_projects.show_project_step(module)
                else:
                    print("❌ Módulo fora do range!")
                    input("Pressione ENTER...")
            except ValueError:
                print("❌ Digite um número válido!")
                input("Pressione ENTER...")
    
    def _show_all_projects_progress(self):
        """Mostra progresso geral de todos os projetos"""
        self.ui.clear_screen()
        self.ui.header("📊 PROGRESSO GERAL DOS PROJETOS", "Visão Completa")
        
        projects_info = [
            ("biblioteca_pessoal", "📖 Sistema de Biblioteca", 1, 10),
            ("ecommerce_simples", "🛒 E-commerce Simples", 11, 20),
            ("api_dashboard", "📊 API Dashboard", 21, 30)
        ]
        
        total_completed = 0
        total_steps = 0
        
        for project_id, name, start, end in projects_info:
            progress = self.progressive_projects.user_progress[project_id]
            project_steps = len(self.progressive_projects.projects[project_id])
            completed = len(progress.completed_steps)
            percentage = (completed / project_steps) * 100 if project_steps > 0 else 0
            
            print(f"{name}")
            print(f"  📊 {completed}/{project_steps} passos ({percentage:.1f}%)")
            print(f"  ⏱️ {progress.total_time_spent} minutos")
            print(f"  🎯 Status: {'Completo ✅' if progress.is_completed else 'Em andamento ⏳'}")
            print()
            
            total_completed += completed
            total_steps += project_steps
        
        overall_percentage = (total_completed / total_steps) * 100 if total_steps > 0 else 0
        
        print("=" * 50)
        print(f"🏆 PROGRESSO TOTAL: {total_completed}/{total_steps} ({overall_percentage:.1f}%)")
        
        if overall_percentage >= 100:
            print("🎉 PARABÉNS! Você completou todos os projetos graduais!")
        elif overall_percentage >= 66:
            print("💪 Excelente progresso! Continue assim!")
        elif overall_percentage >= 33:
            print("👍 Bom progresso! Você está no caminho certo!")
        else:
            print("🚀 Comece seus projetos práticos para acelerar o aprendizado!")
        
        input("\nPressione ENTER para continuar...")
    
    def _go_to_specific_module(self):
        """Permite ir diretamente para um módulo específico"""
        try:
            module = int(input("Digite o número do módulo (1-30): "))
            if 1 <= module <= 30:
                project_info = self.progressive_projects.get_project_for_module(module)
                if project_info:
                    self.progressive_projects.show_project_step(module)
                else:
                    print("❌ Projeto não encontrado para este módulo.")
                    input("Pressione ENTER...")
            else:
                print("❌ Módulo deve estar entre 1 e 30!")
                input("Pressione ENTER...")
        except ValueError:
            print("❌ Digite um número válido!")
            input("Pressione ENTER...")
    
    def _show_notifications(self, xp_result: Dict[str, Any], badges: list) -> None:
        """Exibe notificações de XP e badges"""
        # Notificação de nível
        if xp_result["subiu_nivel"]:
            self.ui.alert(
                f"🎉 LEVEL UP! Agora você é {xp_result['nivel_atual']}!\n"
                f"✨ Novo título: {xp_result['titulo']}\n"
                f"🎯 XP para próximo nível: {xp_result['xp_para_proximo']}",
                "⬆️",
                "success"
            )
        
        # Notificações de badges
        for badge in badges:
            self.ui.alert(
                f"🏆 NOVA CONQUISTA DESBLOQUEADA!\n"
                f"{badge['emoji']} {badge['nome']}\n"
                f"📝 {badge['descricao']}",
                "🎖️",
                "achievement"
            )
    
    def show_progress(self) -> None:
        """Exibe o progresso detalhado do aluno"""
        self.ui.clear_screen()
        summary = self.progress.get_detailed_progress_summary()
        
        # Cabeçalho
        self.ui.header(
            "📊 SEU PROGRESSO DETALHADO",
            f"Aluno: {summary['user_name']} | Total: {summary['completion_percentage']:.1f}%"
        )
        
        # Estatísticas gerais
        self._display_general_stats(summary)
        
        # Progresso por módulo
        self._display_module_progress()
        
        # Estatísticas de gamificação
        self._display_gamification_stats()
        
        # Mini projetos
        self._display_mini_projects_progress(summary)
        
        # Analytics
        self._display_analytics()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _display_general_stats(self, summary: Dict[str, Any]) -> None:
        """Exibe estatísticas gerais"""
        stats_box = self.ui.create_box(
            "Estatísticas Gerais",
            f"📚 Módulos Completos: {summary['modules_completed']}/{summary['total_modules']}\n"
            f"🎯 Pontuação Total: {summary['total_score']} pontos\n"
            f"🏆 Conquistas: {summary['achievements']}\n"
            f"⏱️ Tempo Total: {summary['total_time_spent'] // 60} minutos",
            "📊"
        )
        print(stats_box)
    
    def _display_module_progress(self) -> None:
        """Exibe progresso detalhado por módulo"""
        print("\n📚 PROGRESSO POR MÓDULO:")
        print("=" * 60)
        
        try:
            modules_progress = self.progress.progress_data.get("modules_progress", {})
            
            if not modules_progress:
                print("📝 Nenhum progresso de módulo registrado ainda.")
                return
            
            for module_id in sorted(modules_progress.keys(), 
                                   key=lambda x: int(x.split('_')[1]) if x.split('_')[1].isdigit() else 999):
                if not module_id.startswith("modulo_"):
                    continue
                    
                module_data = modules_progress[module_id]
                module_num = module_id.replace("modulo_", "")
                
                if module_data.get("completed", False):
                    status = "✅ Completo"
                    color = "green"
                else:
                    status = "⏳ Pendente"
                    color = "yellow"
                
                print(f"{module_num:>3}. {status:<15} "
                      f"Pontos: {module_data.get('score', 0):>4} | "
                      f"Tentativas: {module_data.get('attempts', 0):>2}")
        except Exception as e:
            print(f"❌ Erro ao exibir progresso dos módulos: {str(e)}")
            print("📝 Dados de progresso não disponíveis no momento.")
    
    def _display_gamification_stats(self) -> None:
        """Exibe estatísticas de gamificação"""
        try:
            if self.gamification:
                game_stats = self.gamification.get_estatisticas()
                
                game_box = self.ui.create_box(
                    "Sistema de Gamificação",
                    f"🎮 Nível: {game_stats['nivel']} - {game_stats['ranking']}\n"
                    f"⭐ XP: {game_stats['xp_atual']}/{game_stats['xp_proximo_nivel']}\n"
                    f"📊 Progresso do Nível: {game_stats['progresso_nivel']:.1f}%\n"
                    f"🏅 Badges Conquistados: {game_stats['badges']}",
                    "🎮"
                )
                print(game_box)
            else:
                print("\n🎮 Sistema de gamificação não disponível no momento.")
        except Exception as e:
            print(f"\n❌ Erro ao exibir estatísticas de gamificação: {str(e)}")
            print("🎮 Dados de gamificação não disponíveis no momento.")
    
    def _display_mini_projects_progress(self, summary: Dict[str, Any]) -> None:
        """Exibe progresso dos mini projetos"""
        if "mini_projetos_completos" in summary:
            projects_box = self.ui.create_box(
                "Mini Projetos",
                f"🚀 Projetos Completos: {summary['mini_projetos_completos']}/{summary.get('total_mini_projects', 18)}\n"
                f"📈 Progresso: {summary.get('mini_projetos_percentage', 0):.1f}%",
                "🚀"
            )
            print(projects_box)
    
    def _display_analytics(self) -> None:
        """Exibe analytics de aprendizado"""
        try:
            if self.analytics:
                insights = self.analytics.get_learning_insights()
                
                if insights.get('strongest_topics'):
                    print("\n💪 SEUS PONTOS FORTES:")
                    for topic in insights['strongest_topics'][:3]:
                        print(f"  • {topic}")
                
                if insights.get('needs_practice'):
                    print("\n📚 PRECISA PRATICAR:")
                    for topic in insights['needs_practice'][:3]:
                        print(f"  • {topic}")
            else:
                print("\n📊 Analytics não disponível no momento.")
        except Exception as e:
            print(f"\n❌ Erro ao exibir analytics: {str(e)}")
            print("📊 Dados de analytics não disponíveis no momento.")
    
    def handle_special_features(self, choice: str) -> bool:
        """
        Gerencia recursos especiais
        
        Args:
            choice: Escolha do usuário
            
        Returns:
            True se tratou a opção, False caso contrário
        """
        choice = choice.upper()
        self.logger.debug(f"Processing special feature: '{choice}'")
        
        try:
            if choice == "V":
                self.logger.info("User accessed Interactive Demos")
                self.interactive_demos.start_demo_session()
                return True
            elif choice == "E":
                self.logger.info("User accessed Adaptive Exercises")
                self._show_exercise_menu()
                return True
            elif choice == "D":
                self.logger.info("User accessed Visual Debugger")
                self.debug_session.start_debug_session()
                return True
            elif choice == "R":
                self.logger.info("User started Review Mode")
                self.review.start_review_session()
                return True
            elif choice == "G":
                self.logger.info("User accessed Glossary")
                self.glossary.show_glossary_menu()
                return True
            elif choice == "P":
                self.logger.info("User accessed Progress display")
                self.show_progress()
                return True
            elif choice == "C":
                self.logger.info("User requested Certificate generation")
                self._generate_certificate()
                return True
            elif choice == "A":
                self.logger.info("User accessed AI Tutor Assistant")
                self.tutor.sessao_ajuda()
                return True
            elif choice == "J":
                self.logger.info("User accessed Progressive Projects")
                self._show_projects_menu()
                return True
            elif choice == "S":
                self.logger.info("User accessed Analytics Dashboard")
                self._show_analytics_dashboard()
                return True
            elif choice == "O":
                self.logger.info("User accessed Offline Status")
                self._show_offline_status()
                return True
            elif choice == "Q":
                self.logger.info("User accessed Code Review Dashboard")
                self._show_code_review_dashboard()
                return True
            elif choice == "T":
                self.logger.info("User accessed Theme Manager")
                self._show_theme_manager()
                return True
            elif choice == "M":
                self.logger.info("User accessed Mini Projects Gallery")
                self._show_mini_projects_gallery()
                return True
            elif choice == "B":
                self.logger.info("User accessed Methodical Debugging")
                self._show_methodical_debugging()
                return True
            else:
                self.logger.debug(f"Unhandled special feature choice: '{choice}'")
                return False
                
        except Exception as e:
            self.logger.error(f"Error in handle_special_features with choice '{choice}': {str(e)}")
            self.error_handler.handle_error(e, f"handle_special_features({choice})", "high")
            return False
    
    def _generate_certificate(self) -> None:
        """Gera certificado se elegível"""
        completion = self.progress.get_completion_percentage()
        
        if completion >= 80:
            user_name = self.progress.progress_data.get("user_name", "")
            if not user_name:
                user_name = input("Digite seu nome completo para o certificado: ")
                self.progress.set_user_name(user_name)
            
            filename = self.certificate.generate(
                user_name,
                completion,
                self.progress.progress_data["total_score"]
            )
            
            self.ui.success(
                f"🎓 Certificado gerado com sucesso!\n"
                f"📄 Arquivo: {filename}"
            )
        else:
            self.ui.warning(
                f"⚠️ Você precisa completar pelo menos 80% do curso.\n"
                f"📊 Progresso atual: {completion:.1f}%\n"
                f"📚 Continue estudando!"
            )
            
    def _show_exercise_menu(self) -> None:
        """Mostra menu de tipos de exercícios"""
        self.ui.clear_screen()
        self.ui.header("🧠 CENTRAL DE EXERCÍCIOS", "Escolha seu tipo de treino")
        
        print("\n📚 TIPOS DE EXERCÍCIOS DISPONÍVEIS:")
        print("1. 🔥 Exercícios Ricos (Debugging, Completion, Output, Refactoring)")
        print("2. 🎯 Exercícios Adaptativos (Sistema clássico)")
        print("3. 📋 Exercícios por Módulo")
        print("0. 🔙 Voltar")
        
        escolha = input("\n👉 Escolha o tipo de exercício: ").strip()
        
        if escolha == "1":
            # Exercícios ricos
            rich_session = InteractiveExerciseSession(self.ui, self.progress, self.visual)
            rich_session.start_rich_exercise_session()
        elif escolha == "2":
            # Sistema adaptativo original
            self.adaptive_session.start_session()
        elif escolha == "3":
            self._show_module_exercises()
        # Escolha "0" ou inválida volta automaticamente
        
    def _show_module_exercises(self) -> None:
        """Mostra exercícios organizados por módulo"""
        from ..exercises.exercise_bank import ExerciseBank
        
        self.ui.clear_screen()
        self.ui.header("📋 EXERCÍCIOS POR MÓDULO", "Pratique conceitos específicos")
        
        print("\n📚 MÓDULOS DISPONÍVEIS:")
        modules = [
            (1, "Introdução ao Python"),
            (2, "Primeiro Programa"),
            (3, "Variáveis"),
            (4, "Tipos de Dados"),
            (7, "Condições (if/else)"),
            (8, "Repetições (loops)"),
            (9, "Listas"),
            (10, "Funções")
        ]
        
        for num, name in modules:
            exercises = ExerciseBank.get_exercises_by_module(num)
            count = len(exercises)
            print(f"{num:2d}. {name} ({count} exercícios)")
            
        print("0. 🔙 Voltar")
        
        try:
            escolha = int(input("\n👉 Escolha o módulo: "))
            if escolha in [m[0] for m in modules]:
                self._practice_module_exercises(escolha)
        except ValueError:
            pass  # Volta ao menu automaticamente
            
    def _practice_module_exercises(self, module_num: int) -> None:
        """Pratica exercícios de um módulo específico"""
        from ..exercises.exercise_bank import ExerciseBank
        from ..exercises.rich_exercises import RichExerciseEngine
        
        exercises = ExerciseBank.get_exercises_by_module(module_num)
        if not exercises:
            self.ui.error("Nenhum exercício disponível para este módulo ainda.")
            self.ui.pause()
            return
            
        engine = RichExerciseEngine(self.ui)
        current_exercise = 0
        
        while current_exercise < len(exercises):
            exercise = exercises[current_exercise]
            
            self.ui.clear_screen()
            self.ui.header(f"📝 MÓDULO {module_num} - EXERCÍCIO {current_exercise + 1}/{len(exercises)}", 
                          exercise.title)
            
            # Executa exercício baseado no tipo
            if exercise.type.value == "debugging":
                success = self._do_single_debugging(exercise, engine)
            elif exercise.type.value == "code_completion":
                success = self._do_single_completion(exercise, engine)
            elif exercise.type.value == "output_prediction":
                success = self._do_single_output(exercise, engine)
            elif exercise.type.value == "code_refactoring":
                success = self._do_single_refactoring(exercise, engine)
            else:
                success = False
                
            # Navegação
            print("\n" + "="*50)
            print("🔄 OPÇÕES:")
            if current_exercise > 0:
                print("P. ← Exercício anterior")
            if current_exercise < len(exercises) - 1:
                print("N. → Próximo exercício")
            print("M. 📋 Voltar ao menu de módulos")
            print("Q. 🏠 Voltar ao menu principal")
            
            nav = input("\n👉 Escolha: ").upper()
            
            if nav == "P" and current_exercise > 0:
                current_exercise -= 1
            elif nav == "N" and current_exercise < len(exercises) - 1:
                current_exercise += 1
            elif nav == "M":
                break
            elif nav == "Q":
                return
            else:
                current_exercise += 1  # Avança por padrão
                
    def _do_single_debugging(self, exercise, engine) -> bool:
        """Executa um exercício de debugging único"""
        print(f"🐛 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty} | 💰 {exercise.points} pontos")
        
        print("\n📄 CÓDIGO COM BUG:")
        print("=" * 40)
        self._display_code_lines(exercise.code)
        print("=" * 40)
        
        print("\n✏️ Digite o código corrigido (linha vazia para terminar):")
        user_code = self._get_multiline_input()
        
        if user_code.strip():
            correct, feedback, points = engine.evaluate_exercise(exercise, user_code)
            print(f"\n📊 RESULTADO: {feedback}")
            
            if correct:
                self.progress.add_points("rich_exercises", points)
                return True
                
        return False
        
    def _do_single_completion(self, exercise, engine) -> bool:
        """Executa um exercício de code completion único"""
        print(f"📝 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty} | 💰 {exercise.points} pontos")
        
        # Mostra código com placeholders numerados
        display_code = exercise.code
        for i, (key, _) in enumerate(exercise.placeholders.items(), 1):
            display_code = display_code.replace("_____", f"__[{i}]__", 1)
            
        print("\n📄 CÓDIGO INCOMPLETO:")
        print("=" * 40)
        self._display_code_lines(display_code)
        print("=" * 40)
        
        # Coleta respostas
        print("\n✏️ COMPLETE OS ESPAÇOS:")
        user_answers = {}
        for i, (key, _) in enumerate(exercise.placeholders.items(), 1):
            answer = input(f"  [{i}] → ").strip()
            user_answers[key] = answer
            
        correct, feedback, points = engine.evaluate_exercise(exercise, user_answers)
        print(f"\n📊 RESULTADO: {feedback}")
        
        if points > 0:
            self.progress.add_points("rich_exercises", points)
            return correct
            
        return False
        
    def _do_single_output(self, exercise, engine) -> bool:
        """Executa um exercício de output prediction único"""
        print(f"🔮 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty} | 💰 {exercise.points} pontos")
        
        print("\n📄 CÓDIGO:")
        print("=" * 40)
        self._display_code_lines(exercise.code)
        print("=" * 40)
        
        print("\n✏️ QUAL SERÁ O OUTPUT? (linha vazia para terminar)")
        user_output = self._get_multiline_input()
        
        correct, feedback, points = engine.evaluate_exercise(exercise, user_output)
        print(f"\n📊 RESULTADO: {feedback}")
        
        if correct:
            self.progress.add_points("rich_exercises", points)
            return True
            
        return False
        
    def _do_single_refactoring(self, exercise, engine) -> bool:
        """Executa um exercício de refactoring único"""
        print(f"🔧 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty} | 💰 {exercise.points} pontos")
        
        print("\n📄 CÓDIGO ORIGINAL:")
        print("=" * 40)
        self._display_code_lines(exercise.code)
        print("=" * 40)
        
        print("\n🎯 CRITÉRIOS:")
        for criterion in exercise.refactoring_criteria:
            print(f"  • {criterion}")
            
        print("\n✏️ Digite o código refatorado (linha vazia para terminar):")
        user_code = self._get_multiline_input()
        
        if user_code.strip():
            correct, feedback, points = engine.evaluate_exercise(exercise, user_code)
            print(f"\n📊 RESULTADO: {feedback}")
            
            if points > 0:
                self.progress.add_points("rich_exercises", points)
                return correct
                
        return False
        
    def _display_code_lines(self, code: str):
        """Exibe código com numeração"""
        for i, line in enumerate(code.strip().split('\n'), 1):
            print(f"{i:3d} | {line}")
            
    def _get_multiline_input(self) -> str:
        """Coleta input de múltiplas linhas"""
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        return '\n'.join(lines)
    
    def _show_analytics_dashboard(self) -> None:
        """Mostra dashboard de analytics avançados"""
        if self.analytics_dashboard:
            try:
                self.analytics_dashboard.show_main_dashboard()
            except Exception as e:
                self.ui.error(f"Erro ao abrir analytics: {str(e)}")
                self.ui.pause()
        else:
            self.ui.error("Sistema de analytics não disponível")
            self.ui.pause()
    
    def _show_offline_status(self) -> None:
        """Mostra status de conectividade e modo offline"""
        if not self.connectivity_manager or not self.offline_manager:
            self.ui.error("Sistemas offline não disponíveis")
            self.ui.pause()
            return
            
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
        
        # Status de sincronização (se disponível)
        if self.offline_sync:
            sync_status = self.offline_sync.get_sync_status()
            print(f"\n🔄 SINCRONIZAÇÃO:")
            print(f"  Status: {sync_status['current_status'].upper()}")
            print(f"  Operações pendentes: {sync_status['pending_operations']}")
            print(f"  Auto-sync: {'✅ Ativado' if sync_status['auto_sync_enabled'] else '❌ Desativado'}")
            if sync_status['last_sync']:
                from datetime import datetime
                last_sync = datetime.fromisoformat(sync_status['last_sync'])
                print(f"  Última sync: {last_sync.strftime('%d/%m/%Y %H:%M')}")
        
        print(f"\n💡 DICA: Use 'O' no menu principal para acessar opções de sincronização")
        self.ui.pause()
    
    def _show_methodical_debugging(self) -> None:
        """Mostra sistema de debugging metodológico"""
        if self.methodical_debugging:
            try:
                self.methodical_debugging.start_debugging_course()
            except Exception as e:
                self.ui.error(f"Erro ao abrir debugging metodológico: {str(e)}")
                self.ui.pause()
        else:
            self.ui.error("Sistema de debugging metodológico não disponível")
            self.ui.pause()
    
    def _show_mini_projects_gallery(self) -> None:
        """Mostra galeria de mini projetos"""
        self.ui.clear_screen()
        self.ui.header("🚀 GALERIA DE MINI PROJETOS", "18 projetos práticos")
        
        print("🎯 MINI PROJETOS DISPONÍVEIS:")
        print("=" * 50)
        print("📝 Esta funcionalidade está sendo desenvolvida!")
        print("🔜 Em breve você terá acesso a 18 mini projetos práticos.")
        print()
        print("💡 Por enquanto, use os 'Projetos Graduais' (opção J)")
        print("   que oferecem 3 projetos completos e evolutivos!")
        
        self.ui.pause()
    
    def _show_theme_manager(self) -> None:
        """Mostra gerenciador de temas"""
        self.ui.clear_screen() 
        self.ui.header("🎨 GERENCIADOR DE TEMAS", "Personalização visual")
        
        print("🎨 TEMAS DISPONÍVEIS:")
        print("=" * 50)
        print("📝 Esta funcionalidade está sendo desenvolvida!")
        print("🔜 Em breve você poderá personalizar:")
        print("   • Cores do terminal")
        print("   • Esquemas de cores (dark/light)")
        print("   • Fonts e estilos")
        print("   • Animações e efeitos")
        
        self.ui.pause()
    
    def _show_code_review_dashboard(self) -> None:
        """Mostra dashboard de code review"""
        try:
            if hasattr(self, 'code_review_dashboard') and self.code_review_dashboard:
                self.code_review_dashboard.show_main_dashboard()
            else:
                self.ui.clear_screen()
                self.ui.header("🔍 CODE REVIEW DASHBOARD", "Análise de código Python")
                
                print("🔍 ANÁLISE DE CÓDIGO PYTHON:")
                print("=" * 50)
                print("📝 Esta funcionalidade está sendo desenvolvida!")
                print("🔜 Em breve você terá acesso a:")
                print("   • Análise automática de código")
                print("   • Sugestões de melhorias")
                print("   • Detecção de code smells")
                print("   • Verificação de boas práticas")
                print("   • Relatórios detalhados de qualidade")
                print()
                print("💡 Por enquanto, use o 'Debugging Metodológico' (opção B)")
                print("   que oferece técnicas avançadas de debugging!")
                
                self.ui.pause()
        except Exception as e:
            self.ui.clear_screen()
            self.ui.header("🔍 CODE REVIEW DASHBOARD", "Erro")
            print(f"❌ Erro ao abrir code review: {str(e)}")
            print("💡 Tente novamente mais tarde ou use outras funcionalidades.")
            self.ui.pause()