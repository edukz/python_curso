#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modo de Revisão do Curso
Permite revisar módulos já completados e praticar exercícios
"""

import random
from typing import List, Dict, Any, Optional
from .progress_manager import ProgressManager
from .visual_feedback import VisualFeedback
from .utils import PythonCourseUtils


class ReviewMode:
    """Gerencia o modo de revisão do curso"""
    
    def __init__(self, progress_manager: ProgressManager):
        self.progress_manager = progress_manager
        self.visual_feedback = VisualFeedback()
        self.utils = PythonCourseUtils()
        self.review_exercises = self._load_review_exercises()
    
    def _load_review_exercises(self) -> Dict[str, List[Dict[str, Any]]]:
        """Carrega exercícios de revisão para cada módulo"""
        return {
            "modulo_1": [
                {
                    "question": "O que é Python?",
                    "options": [
                        "Uma linguagem de programação",
                        "Um tipo de cobra",
                        "Um sistema operacional",
                        "Um navegador web"
                    ],
                    "correct": 0,
                    "explanation": "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral."
                }
            ],
            "modulo_2": [
                {
                    "question": "Qual função usamos para exibir texto na tela?",
                    "options": ["show()", "display()", "print()", "write()"],
                    "correct": 2,
                    "explanation": "A função print() é usada para exibir saída na tela."
                }
            ],
            "modulo_3": [
                {
                    "question": "Como declaramos uma variável em Python?",
                    "options": [
                        "var nome = 'valor'",
                        "nome = 'valor'",
                        "declare nome = 'valor'",
                        "let nome = 'valor'"
                    ],
                    "correct": 1,
                    "explanation": "Em Python, simplesmente atribuímos um valor usando o operador ="
                }
            ],
            "modulo_4": [
                {
                    "question": "Qual tipo de dado representa números decimais?",
                    "options": ["int", "str", "float", "bool"],
                    "correct": 2,
                    "explanation": "float representa números com casas decimais."
                }
            ],
            "modulo_5": [
                {
                    "question": "Qual função usamos para receber entrada do usuário?",
                    "options": ["get()", "input()", "read()", "scan()"],
                    "correct": 1,
                    "explanation": "A função input() lê entrada do usuário."
                }
            ],
            "modulo_6": [
                {
                    "question": "Qual operador usamos para exponenciação?",
                    "options": ["^", "**", "exp", "pow"],
                    "correct": 1,
                    "explanation": "O operador ** é usado para exponenciação (ex: 2**3 = 8)."
                }
            ],
            "modulo_7": [
                {
                    "question": "Qual palavra-chave inicia uma condição?",
                    "options": ["when", "if", "case", "check"],
                    "correct": 1,
                    "explanation": "if é a palavra-chave para condições em Python."
                }
            ],
            "modulo_8": [
                {
                    "question": "Qual loop repete um número específico de vezes?",
                    "options": ["while", "for", "repeat", "loop"],
                    "correct": 1,
                    "explanation": "for é ideal para repetir um número específico de vezes."
                }
            ],
            "modulo_9": [
                {
                    "question": "Como acessamos o primeiro elemento de uma lista?",
                    "options": ["lista[1]", "lista[0]", "lista.first()", "lista.get(0)"],
                    "correct": 1,
                    "explanation": "Listas em Python começam no índice 0."
                }
            ],
            "modulo_10": [
                {
                    "question": "Qual palavra-chave define uma função?",
                    "options": ["function", "func", "def", "define"],
                    "correct": 2,
                    "explanation": "def é a palavra-chave para definir funções."
                }
            ]
        }
    
    def start_review_session(self) -> None:
        """Inicia uma sessão de revisão"""
        self.utils.limpar_tela()
        self.utils.titulo("MODO DE REVISÃO")
        
        completed_modules = self.progress_manager.progress_data["modules_completed"]
        
        if not completed_modules:
            print("❌ Você ainda não completou nenhum módulo!")
            print("Complete pelo menos um módulo antes de usar o modo revisão.")
            self.utils.pausar()
            return
        
        print("📚 Módulos disponíveis para revisão:")
        for i, module_id in enumerate(completed_modules, 1):
            module_num = module_id.split('_')[1]
            print(f"{i}. Módulo {module_num}")
        
        print("\n0. Revisão aleatória de todos os módulos")
        print("V. Voltar ao menu principal")
        
        try:
            choice = input("\n👉 Escolha uma opção: ").strip().lower()
        except KeyboardInterrupt:
            return  # Sai silenciosamente do modo revisão
        
        if choice == 'v':
            return
        elif choice == '0':
            self._random_review(completed_modules)
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(completed_modules):
                    self._review_module(completed_modules[idx])
                else:
                    print("❌ Opção inválida!")
            except ValueError:
                print("❌ Digite um número válido!")
    
    def _review_module(self, module_id: str) -> None:
        """Revisa um módulo específico"""
        self.utils.limpar_tela()
        module_num = module_id.split('_')[1]
        self.utils.titulo(f"REVISÃO - MÓDULO {module_num}")
        
        exercises = self.review_exercises.get(module_id, [])
        if not exercises:
            print("❌ Não há exercícios de revisão para este módulo ainda.")
            self.utils.pausar()
            return
        
        score = 0
        total = len(exercises)
        
        for i, exercise in enumerate(exercises, 1):
            print(f"\n📝 Questão {i}/{total}")
            print(f"\n{exercise['question']}")
            
            for j, option in enumerate(exercise['options']):
                print(f"{j + 1}. {option}")
            
            while True:
                try:
                    answer = int(input("\n👉 Sua resposta (número): ")) - 1
                    if 0 <= answer < len(exercise['options']):
                        break
                    print("❌ Digite um número válido!")
                except ValueError:
                    print("❌ Digite apenas números!")
                except KeyboardInterrupt:
                    print("\n\n⚠️ Revisão interrompida. Voltando ao menu...")
                    return
            
            if answer == exercise['correct']:
                self.visual_feedback.success_animation("Correto! 🎯")
                score += 1
                self.visual_feedback.add_score(10, "Questão de revisão")
            else:
                self.visual_feedback.error_animation()
                print(f"\n💡 {exercise['explanation']}")
            
            self.utils.pausar()
            self.utils.limpar_tela()
        
        # Mostra resultado final
        percentage = (score / total) * 100
        print(f"\n📊 RESULTADO DA REVISÃO")
        print(f"Acertos: {score}/{total} ({percentage:.0f}%)")
        
        if percentage == 100:
            self.visual_feedback.celebration()
            self.visual_feedback.unlock_achievement("Revisão Perfeita!")
        elif percentage >= 80:
            print("\n✨ Excelente! Você domina bem este conteúdo!")
        elif percentage >= 60:
            print("\n👍 Bom trabalho! Continue praticando!")
        else:
            print("\n💪 Continue estudando! A prática leva à perfeição!")
        
        self.utils.pausar()
    
    def _random_review(self, completed_modules: List[str]) -> None:
        """Revisão aleatória de todos os módulos completados"""
        self.utils.limpar_tela()
        self.utils.titulo("REVISÃO ALEATÓRIA")
        
        # Coleta todos os exercícios dos módulos completados
        all_exercises = []
        for module_id in completed_modules:
            exercises = self.review_exercises.get(module_id, [])
            for ex in exercises:
                all_exercises.append((module_id, ex))
        
        if not all_exercises:
            print("❌ Não há exercícios disponíveis para revisão.")
            self.utils.pausar()
            return
        
        # Embaralha e seleciona 10 questões
        random.shuffle(all_exercises)
        selected = all_exercises[:min(10, len(all_exercises))]
        
        print(f"📝 Preparando {len(selected)} questões aleatórias...")
        self.visual_feedback.countdown(3)
        
        score = 0
        for i, (module_id, exercise) in enumerate(selected, 1):
            self.utils.limpar_tela()
            module_num = module_id.split('_')[1]
            print(f"📚 Questão {i}/{len(selected)} - Módulo {module_num}")
            
            print(f"\n{exercise['question']}")
            
            for j, option in enumerate(exercise['options']):
                print(f"{j + 1}. {option}")
            
            while True:
                try:
                    answer = int(input("\n👉 Sua resposta: ")) - 1
                    if 0 <= answer < len(exercise['options']):
                        break
                except ValueError:
                    pass
                except KeyboardInterrupt:
                    print("\n\n⚠️ Revisão interrompida. Voltando ao menu...")
                    return
            
            if answer == exercise['correct']:
                self.visual_feedback.success_animation()
                score += 1
            else:
                self.visual_feedback.error_animation()
                print(f"\n💡 {exercise['explanation']}")
            
            self.utils.pausar()
        
        # Resultado final
        self.utils.limpar_tela()
        percentage = (score / len(selected)) * 100
        print(self.visual_feedback.get_score_summary())
        print(f"\nAcertos na revisão: {score}/{len(selected)} ({percentage:.0f}%)")
        
        if percentage == 100:
            self.visual_feedback.unlock_achievement("Mestre da Revisão!")
        
        self.utils.pausar()
    
    def get_review_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de revisão"""
        completed = self.progress_manager.progress_data["modules_completed"]
        total_exercises = sum(
            len(self.review_exercises.get(mod, [])) 
            for mod in completed
        )
        
        return {
            "modules_available": len(completed),
            "total_exercises": total_exercises,
            "review_score": self.visual_feedback.score
        }