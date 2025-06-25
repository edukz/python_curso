#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema Interativo de Exercícios Ricos
"""

import os
import time
from typing import Dict, List, Optional, Any
from .rich_exercises import (
    Exercise, ExerciseType, RichExerciseEngine, 
    ExerciseGenerator
)


class InteractiveExerciseSession:
    """Sessão interativa para exercícios ricos"""
    
    def __init__(self, ui_components, progress_manager, visual_feedback):
        self.ui = ui_components
        self.progress = progress_manager
        self.visual = visual_feedback
        self.engine = RichExerciseEngine(ui_components)
        self.generator = ExerciseGenerator()
        
        # Estatísticas da sessão
        self.exercises_completed = 0
        self.total_points = 0
        self.start_time = None
        
    def start_rich_exercise_session(self, module: str = None):
        """Inicia sessão de exercícios ricos"""
        self.start_time = time.time()
        
        while True:
            self.ui.clear_screen()
            self.ui.header("🧠 EXERCÍCIOS INTERATIVOS AVANÇADOS", 
                          "Debugging | Completion | Output | Refactoring")
            
            # Menu de tipos de exercícios
            print("\n📚 TIPOS DE EXERCÍCIOS:")
            print("1. 🐛 Debugging - Encontre e corrija bugs")
            print("2. 📝 Code Completion - Complete o código")
            print("3. 🔮 Output Prediction - Preveja o resultado")
            print("4. 🔧 Code Refactoring - Melhore o código")
            print("5. 📊 Ver estatísticas da sessão")
            print("0. 🔙 Voltar ao menu principal")
            
            escolha = input("\n👉 Escolha o tipo de exercício: ").strip()
            
            if escolha == "0":
                self._show_session_summary()
                break
            elif escolha == "1":
                self._do_debugging_exercise()
            elif escolha == "2":
                self._do_completion_exercise()
            elif escolha == "3":
                self._do_output_exercise()
            elif escolha == "4":
                self._do_refactoring_exercise()
            elif escolha == "5":
                self._show_statistics()
            else:
                self.ui.error("Opção inválida!")
                self.ui.pause()
                
    def _do_debugging_exercise(self):
        """Exercício de debugging"""
        self.ui.clear_screen()
        self.ui.section("🐛 EXERCÍCIO DE DEBUGGING", "🔍")
        
        # Gera exercício (em produção, seria selecionado de um banco)
        exercise = self.generator.generate_debugging_exercise("module1", "variables")
        
        # Exibe exercício
        print(f"\n📋 {exercise.title}")
        print(f"📝 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty}")
        print(f"💰 Pontos: {exercise.points}")
        
        print("\n📄 CÓDIGO COM BUG:")
        print("=" * 50)
        self._display_code_with_line_numbers(exercise.code)
        print("=" * 50)
        
        # Permite edição
        print("\n✏️ CORRIJA O CÓDIGO:")
        print("Digite o código corrigido (termine com uma linha vazia):")
        
        user_code = self._get_multiline_input()
        
        if user_code.strip():
            # Avalia resposta
            correct, feedback, points = self.engine.evaluate_exercise(exercise, user_code)
            
            # Exibe resultado
            print("\n" + "=" * 50)
            print(feedback)
            
            if correct:
                self.exercises_completed += 1
                self.total_points += points
                self.visual.show_success(f"🎉 +{points} pontos!")
                
                # Mostra solução e explicação
                print("\n💡 SOLUÇÃO:")
                self._display_code_with_line_numbers(exercise.solution)
                print(f"\n📖 EXPLICAÇÃO: {exercise.explanation}")
            else:
                # Oferece dicas
                if exercise.hints:
                    print("\n💡 DICAS:")
                    for i, hint in enumerate(exercise.hints, 1):
                        print(f"  {i}. {hint}")
                        
            self.ui.pause()
            
    def _do_completion_exercise(self):
        """Exercício de completar código"""
        self.ui.clear_screen()
        self.ui.section("📝 EXERCÍCIO DE CODE COMPLETION", "✏️")
        
        exercise = self.generator.generate_completion_exercise("module2", "loops")
        
        # Exibe exercício
        print(f"\n📋 {exercise.title}")
        print(f"📝 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty}")
        print(f"💰 Pontos: {exercise.points}")
        
        print("\n📄 CÓDIGO INCOMPLETO:")
        print("=" * 50)
        # Mostra código com blanks numerados
        display_code = exercise.code
        for i, (key, _) in enumerate(exercise.placeholders.items(), 1):
            display_code = display_code.replace("_____", f"__[{i}]__", 1)
        self._display_code_with_line_numbers(display_code)
        print("=" * 50)
        
        # Coleta respostas
        print("\n✏️ COMPLETE OS ESPAÇOS:")
        user_answers = {}
        for i, (key, _) in enumerate(exercise.placeholders.items(), 1):
            answer = input(f"  [{i}] → ").strip()
            user_answers[key] = answer
            
        # Avalia
        correct, feedback, points = self.engine.evaluate_exercise(exercise, user_answers)
        
        print("\n" + "=" * 50)
        print(feedback)
        
        if points > 0:
            self.total_points += points
            if correct:
                self.exercises_completed += 1
                
        # Mostra código completo
        print("\n💡 CÓDIGO COMPLETO:")
        complete_code = exercise.code
        for key, value in exercise.solution.items():
            complete_code = complete_code.replace("_____", value, 1)
        self._display_code_with_line_numbers(complete_code)
        
        print(f"\n📖 EXPLICAÇÃO: {exercise.explanation}")
        self.ui.pause()
        
    def _do_output_exercise(self):
        """Exercício de prever output"""
        self.ui.clear_screen()
        self.ui.section("🔮 EXERCÍCIO DE OUTPUT PREDICTION", "🎯")
        
        exercise = self.generator.generate_output_exercise("module3", "lists")
        
        # Exibe exercício
        print(f"\n📋 {exercise.title}")
        print(f"📝 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty}")
        print(f"💰 Pontos: {exercise.points}")
        
        print("\n📄 CÓDIGO:")
        print("=" * 50)
        self._display_code_with_line_numbers(exercise.code)
        print("=" * 50)
        
        # Permite usar dicas
        use_hint = input("\n💡 Deseja uma dica? (s/n): ").lower() == 's'
        if use_hint and exercise.hints:
            print(f"💡 DICA: {exercise.hints[0]}")
            
        print("\n✏️ QUAL SERÁ O OUTPUT?")
        print("Digite exatamente o que será impresso:")
        user_output = self._get_multiline_input()
        
        # Avalia
        correct, feedback, points = self.engine.evaluate_exercise(exercise, user_output)
        
        print("\n" + "=" * 50)
        print(feedback)
        
        if correct:
            self.exercises_completed += 1
            self.total_points += points
            self.visual.show_success(f"🎉 +{points} pontos!")
            
        print(f"\n📖 EXPLICAÇÃO: {exercise.explanation}")
        
        # Permite executar o código
        run_code = input("\n▶️ Deseja executar o código para ver? (s/n): ").lower() == 's'
        if run_code:
            print("\n🖥️ EXECUTANDO:")
            print("-" * 30)
            exec(exercise.code)
            print("-" * 30)
            
        self.ui.pause()
        
    def _do_refactoring_exercise(self):
        """Exercício de refatoração"""
        self.ui.clear_screen()
        self.ui.section("🔧 EXERCÍCIO DE REFACTORING", "✨")
        
        exercise = self.generator.generate_refactoring_exercise("module4", "functions")
        
        # Exibe exercício
        print(f"\n📋 {exercise.title}")
        print(f"📝 {exercise.description}")
        print(f"⭐ Dificuldade: {'⭐' * exercise.difficulty}")
        print(f"💰 Pontos: {exercise.points}")
        
        print("\n📄 CÓDIGO ORIGINAL:")
        print("=" * 50)
        self._display_code_with_line_numbers(exercise.code)
        print("=" * 50)
        
        print("\n🎯 CRITÉRIOS DE REFATORAÇÃO:")
        for criterion in exercise.refactoring_criteria:
            print(f"  • {criterion}")
            
        print("\n✏️ REFATORE O CÓDIGO:")
        print("Digite o código melhorado (termine com uma linha vazia):")
        
        user_code = self._get_multiline_input()
        
        if user_code.strip():
            # Avalia
            correct, feedback, points = self.engine.evaluate_exercise(exercise, user_code)
            
            print("\n" + "=" * 50)
            print(feedback)
            
            if points > 0:
                self.total_points += points
                if correct:
                    self.exercises_completed += 1
                    
            # Mostra solução sugerida
            print("\n💡 SOLUÇÃO SUGERIDA:")
            self._display_code_with_line_numbers(exercise.solution)
            
            print(f"\n📖 EXPLICAÇÃO: {exercise.explanation}")
            
        self.ui.pause()
        
    def _show_statistics(self):
        """Mostra estatísticas da sessão"""
        self.ui.clear_screen()
        self.ui.section("📊 ESTATÍSTICAS DA SESSÃO", "📈")
        
        duration = int(time.time() - self.start_time) if self.start_time else 0
        minutes = duration // 60
        seconds = duration % 60
        
        print(f"\n⏱️ Tempo de sessão: {minutes}m {seconds}s")
        print(f"✅ Exercícios completados: {self.exercises_completed}")
        print(f"⭐ Pontos totais: {self.total_points}")
        
        if self.exercises_completed > 0:
            avg_points = self.total_points / self.exercises_completed
            print(f"📊 Média de pontos: {avg_points:.1f}")
            
        # Mostra progresso por tipo
        print("\n📈 PROGRESSO POR TIPO:")
        print("  🐛 Debugging: ████████░░ 80%")
        print("  📝 Completion: ██████░░░░ 60%")
        print("  🔮 Output: █████████░ 90%")
        print("  🔧 Refactoring: ███░░░░░░░ 30%")
        
        self.ui.pause()
        
    def _show_session_summary(self):
        """Mostra resumo ao sair"""
        if self.exercises_completed > 0:
            self.ui.clear_screen()
            self.ui.header("🎯 RESUMO DA SESSÃO", "Parabéns pelo esforço!")
            
            print(f"\n✅ Exercícios completados: {self.exercises_completed}")
            print(f"⭐ Pontos conquistados: {self.total_points}")
            
            # Salva progresso
            self.progress.add_points("rich_exercises", self.total_points)
            
            print("\n💾 Progresso salvo!")
            self.ui.pause()
            
    def _display_code_with_line_numbers(self, code: str):
        """Exibe código com números de linha"""
        lines = code.strip().split('\n')
        for i, line in enumerate(lines, 1):
            print(f"{i:3d} | {line}")
            
    def _get_multiline_input(self) -> str:
        """Coleta input de múltiplas linhas"""
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return '\n'.join(lines)