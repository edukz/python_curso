#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Exercícios Adaptativos
Gera exercícios personalizados baseados no desempenho e dificuldades do aluno
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum


class DifficultyLevel(Enum):
    """Níveis de dificuldade"""
    MUITO_FACIL = 1
    FACIL = 2
    MEDIO = 3
    DIFICIL = 4
    MUITO_DIFICIL = 5


class ExerciseType(Enum):
    """Tipos de exercícios"""
    MULTIPLE_CHOICE = "multipla_escolha"
    CODE_COMPLETION = "completar_codigo"
    ERROR_DETECTION = "detectar_erro"
    CODE_OUTPUT = "prever_saida"
    VARIABLE_TRACE = "rastrear_variavel"
    CONCEPT_APPLICATION = "aplicar_conceito"


class AdaptiveExerciseGenerator:
    """Gerador de exercícios adaptativos"""
    
    def __init__(self, progress_manager, analytics_manager):
        self.progress = progress_manager
        self.analytics = analytics_manager
        self.exercise_templates = self._load_exercise_templates()
        self.user_performance = self._load_user_performance()
        
    def _load_exercise_templates(self) -> Dict[str, List[Dict[str, Any]]]:
        """Carrega templates de exercícios organizados por tópico"""
        return {
            "variaveis": [
                {
                    "type": ExerciseType.MULTIPLE_CHOICE,
                    "difficulty": DifficultyLevel.FACIL,
                    "template": "Qual é a forma CORRETA de criar uma variável em Python?",
                    "options": [
                        "nome = 'João'",
                        "var nome = 'João'",
                        "string nome = 'João'",
                        "nome := 'João'"
                    ],
                    "correct": 0,
                    "explanation": "Em Python, criamos variáveis simplesmente com: nome = valor"
                },
                {
                    "type": ExerciseType.ERROR_DETECTION,
                    "difficulty": DifficultyLevel.MEDIO,
                    "template": "Encontre o erro neste código:",
                    "code": "2nome = 'Ana'\nprint(2nome)",
                    "error": "Nome de variável não pode começar com número",
                    "correction": "nome2 = 'Ana'\nprint(nome2)"
                },
                {
                    "type": ExerciseType.CODE_OUTPUT,
                    "difficulty": DifficultyLevel.FACIL,
                    "template": "Qual será a saída deste código?",
                    "code": "x = 10\ny = 20\nprint(x + y)",
                    "output": "30",
                    "explanation": "x (10) + y (20) = 30"
                }
            ],
            
            "tipos_dados": [
                {
                    "type": ExerciseType.MULTIPLE_CHOICE,
                    "difficulty": DifficultyLevel.MEDIO,
                    "template": "Qual o tipo da variável: idade = 25",
                    "options": ["int", "float", "str", "bool"],
                    "correct": 0,
                    "explanation": "25 é um número inteiro, portanto tipo 'int'"
                },
                {
                    "type": ExerciseType.CODE_COMPLETION,
                    "difficulty": DifficultyLevel.DIFICIL,
                    "template": "Complete o código para converter string em número:",
                    "code": "texto = '42'\nnumero = ___(texto)\nprint(numero + 8)",
                    "completion": "int",
                    "explanation": "Use int() para converter string em número inteiro"
                }
            ],
            
            "condicionais": [
                {
                    "type": ExerciseType.CODE_OUTPUT,
                    "difficulty": DifficultyLevel.MEDIO,
                    "template": "Qual será a saída?",
                    "code": "idade = 16\nif idade >= 18:\n    print('Adulto')\nelse:\n    print('Menor')",
                    "output": "Menor",
                    "explanation": "16 < 18, então executa o 'else'"
                },
                {
                    "type": ExerciseType.ERROR_DETECTION,
                    "difficulty": DifficultyLevel.DIFICIL,
                    "template": "Encontre o erro:",
                    "code": "if x = 10:\n    print('x é 10')",
                    "error": "Usar '=' ao invés de '==' na comparação",
                    "correction": "if x == 10:\n    print('x é 10')"
                }
            ],
            
            "loops": [
                {
                    "type": ExerciseType.VARIABLE_TRACE,
                    "difficulty": DifficultyLevel.DIFICIL,
                    "template": "Qual o valor de 'soma' após o loop?",
                    "code": "soma = 0\nfor i in range(3):\n    soma += i\nprint(soma)",
                    "trace": [
                        "i=0: soma = 0 + 0 = 0",
                        "i=1: soma = 0 + 1 = 1", 
                        "i=2: soma = 1 + 2 = 3"
                    ],
                    "final_value": "3"
                }
            ],
            
            "listas": [
                {
                    "type": ExerciseType.MULTIPLE_CHOICE,
                    "difficulty": DifficultyLevel.MEDIO,
                    "template": "Como acessar o primeiro item de uma lista?",
                    "options": ["lista[1]", "lista[0]", "lista.first()", "lista.get(0)"],
                    "correct": 1,
                    "explanation": "Em Python, índices começam em 0"
                },
                {
                    "type": ExerciseType.CODE_COMPLETION,
                    "difficulty": DifficultyLevel.FACIL,
                    "template": "Complete para adicionar item na lista:",
                    "code": "frutas = ['maçã', 'banana']\nfrutas.___('laranja')",
                    "completion": "append",
                    "explanation": "append() adiciona item no final da lista"
                }
            ],
            
            "funcoes": [
                {
                    "type": ExerciseType.CODE_OUTPUT,
                    "difficulty": DifficultyLevel.MEDIO,
                    "template": "Qual será a saída?",
                    "code": "def dobrar(x):\n    return x * 2\n\nresult = dobrar(5)\nprint(result)",
                    "output": "10",
                    "explanation": "dobrar(5) retorna 5 * 2 = 10"
                }
            ]
        }
    
    def _load_user_performance(self) -> Dict[str, Any]:
        """Carrega histórico de performance do usuário"""
        try:
            with open("adaptive_performance.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {
                "topic_scores": {},  # Pontuação por tópico
                "difficulty_preferences": {},  # Preferência de dificuldade
                "exercise_history": [],  # Histórico de exercícios
                "weak_areas": [],  # Áreas fracas identificadas
                "mastered_topics": [],  # Tópicos dominados
                "repetition_schedule": {}  # Agendamento de repetição espaçada
            }
    
    def _save_user_performance(self) -> None:
        """Salva performance do usuário"""
        with open("adaptive_performance.json", 'w', encoding='utf-8') as f:
            json.dump(self.user_performance, f, indent=2, ensure_ascii=False)
    
    def analyze_user_level(self, topic: str) -> DifficultyLevel:
        """Analisa nível do usuário em um tópico específico"""
        topic_score = self.user_performance["topic_scores"].get(topic, 0)
        
        # Considera também dados do analytics
        error_count = self.analytics.analytics_data["concepts_difficulty"].get(topic, 0)
        help_requests = self.analytics.analytics_data["help_requests"].get(topic, 0)
        
        # Calcula score combinado
        combined_score = topic_score - (error_count * 10) - (help_requests * 5)
        
        # Determina nível baseado no score
        if combined_score >= 80:
            return DifficultyLevel.MUITO_DIFICIL
        elif combined_score >= 60:
            return DifficultyLevel.DIFICIL
        elif combined_score >= 40:
            return DifficultyLevel.MEDIO
        elif combined_score >= 20:
            return DifficultyLevel.FACIL
        else:
            return DifficultyLevel.MUITO_FACIL
    
    def identify_weak_areas(self) -> List[str]:
        """Identifica áreas onde o usuário tem mais dificuldade"""
        weak_areas = []
        
        # Analisa erros frequentes
        error_patterns = self.analytics.analytics_data["error_patterns"]
        concepts_difficulty = self.analytics.analytics_data["concepts_difficulty"]
        
        for topic, difficulty_score in concepts_difficulty.items():
            if difficulty_score >= 3:  # 3+ erros/ajudas
                weak_areas.append(topic)
        
        # Analisa scores baixos
        for topic, score in self.user_performance["topic_scores"].items():
            if score < 40:  # Score baixo
                weak_areas.append(topic)
        
        return list(set(weak_areas))  # Remove duplicatas
    
    def generate_adaptive_exercise(self, focus_topic: Optional[str] = None) -> Dict[str, Any]:
        """Gera exercício adaptativo baseado no perfil do usuário"""
        
        # Identifica áreas fracas se não especificado tópico
        if not focus_topic:
            weak_areas = self.identify_weak_areas()
            if weak_areas:
                focus_topic = random.choice(weak_areas)
            else:
                # Escolhe tópico aleatório se não há áreas fracas
                focus_topic = random.choice(list(self.exercise_templates.keys()))
        
        # Analisa nível do usuário no tópico
        user_level = self.analyze_user_level(focus_topic)
        
        # Filtra exercícios do nível apropriado
        topic_exercises = self.exercise_templates.get(focus_topic, [])
        suitable_exercises = [
            ex for ex in topic_exercises 
            if abs(ex["difficulty"].value - user_level.value) <= 1
        ]
        
        if not suitable_exercises:
            suitable_exercises = topic_exercises  # Fallback
        
        # Escolhe exercício
        exercise_template = random.choice(suitable_exercises)
        
        # Gera variação do exercício
        exercise = self._generate_exercise_variation(exercise_template, focus_topic)
        
        # Adiciona metadata
        exercise.update({
            "topic": focus_topic,
            "user_level": user_level.name,
            "generated_at": datetime.now().isoformat(),
            "adaptive_score": self.user_performance["topic_scores"].get(focus_topic, 0)
        })
        
        return exercise
    
    def _generate_exercise_variation(self, template: Dict[str, Any], topic: str) -> Dict[str, Any]:
        """Gera variação do exercício baseada no template"""
        exercise = template.copy()
        
        # Adiciona variações baseadas no tópico
        if topic == "variaveis" and template["type"] == ExerciseType.MULTIPLE_CHOICE:
            # Varia nomes de variáveis
            names = ["nome", "idade", "cidade", "produto", "cliente"]
            values = ["'Python'", "25", "'São Paulo'", "'Notebook'", "'Ana'"]
            
            name = random.choice(names)
            value = random.choice(values)
            
            exercise["template"] = f"Qual é a forma CORRETA de criar uma variável '{name}'?"
            exercise["options"] = [
                f"{name} = {value}",
                f"var {name} = {value}",
                f"string {name} = {value}",
                f"{name} := {value}"
            ]
        
        elif topic == "tipos_dados" and template["type"] == ExerciseType.CODE_OUTPUT:
            # Varia operações matemáticas
            operators = ["+", "-", "*"]
            op = random.choice(operators)
            a, b = random.randint(1, 20), random.randint(1, 20)
            
            exercise["code"] = f"x = {a}\ny = {b}\nprint(x {op} y)"
            exercise["output"] = str(eval(f"{a} {op} {b}"))
            exercise["explanation"] = f"x ({a}) {op} y ({b}) = {exercise['output']}"
        
        elif topic == "condicionais" and template["type"] == ExerciseType.CODE_OUTPUT:
            # Varia condições
            age = random.randint(10, 25)
            limit = random.choice([16, 18, 21])
            
            exercise["code"] = f"idade = {age}\nif idade >= {limit}:\n    print('Permitido')\nelse:\n    print('Não permitido')"
            exercise["output"] = "Permitido" if age >= limit else "Não permitido"
            exercise["explanation"] = f"{age} {'≥' if age >= limit else '<'} {limit}, então executa {'if' if age >= limit else 'else'}"
        
        return exercise
    
    def record_exercise_result(self, exercise: Dict[str, Any], user_answer: str, 
                             correct: bool, time_taken: int) -> None:
        """Registra resultado do exercício para adaptação futura"""
        
        # Registra no histórico
        result = {
            "exercise_id": f"{exercise['topic']}_{datetime.now().timestamp()}",
            "topic": exercise["topic"],
            "difficulty": exercise["difficulty"].name,
            "type": exercise["type"].value,
            "user_answer": user_answer,
            "correct": correct,
            "time_taken": time_taken,
            "timestamp": datetime.now().isoformat()
        }
        
        self.user_performance["exercise_history"].append(result)
        
        # Atualiza score do tópico
        topic = exercise["topic"]
        current_score = self.user_performance["topic_scores"].get(topic, 50)  # Score inicial médio
        
        if correct:
            # Aumenta score baseado na dificuldade
            difficulty_bonus = exercise["difficulty"].value * 10
            new_score = min(100, current_score + difficulty_bonus)
        else:
            # Diminui score
            penalty = exercise["difficulty"].value * 5
            new_score = max(0, current_score - penalty)
        
        self.user_performance["topic_scores"][topic] = new_score
        
        # Atualiza áreas fracas
        if not correct:
            weak_areas = self.user_performance.get("weak_areas", [])
            if topic not in weak_areas:
                weak_areas.append(topic)
                self.user_performance["weak_areas"] = weak_areas
        
        # Verifica se dominou o tópico
        if new_score >= 90 and topic not in self.user_performance.get("mastered_topics", []):
            mastered = self.user_performance.get("mastered_topics", [])
            mastered.append(topic)
            self.user_performance["mastered_topics"] = mastered
        
        # Agenda repetição espaçada para tópicos fracos
        if not correct:
            self._schedule_spaced_repetition(topic)
        
        # Limita histórico a últimos 100 exercícios
        if len(self.user_performance["exercise_history"]) > 100:
            self.user_performance["exercise_history"] = self.user_performance["exercise_history"][-100:]
        
        self._save_user_performance()
    
    def _schedule_spaced_repetition(self, topic: str) -> None:
        """Agenda repetição espaçada para reforçar aprendizado"""
        schedule = self.user_performance.get("repetition_schedule", {})
        
        # Intervalos de repetição espaçada (em dias)
        intervals = [1, 3, 7, 14, 30]
        
        current_interval = schedule.get(topic, {}).get("interval", 0)
        next_interval_index = min(len(intervals) - 1, intervals.index(current_interval) + 1 if current_interval in intervals else 0)
        
        next_review = datetime.now() + timedelta(days=intervals[next_interval_index])
        
        schedule[topic] = {
            "next_review": next_review.isoformat(),
            "interval": intervals[next_interval_index],
            "reviews_count": schedule.get(topic, {}).get("reviews_count", 0) + 1
        }
        
        self.user_performance["repetition_schedule"] = schedule
    
    def get_due_reviews(self) -> List[str]:
        """Retorna tópicos que precisam de revisão baseado na repetição espaçada"""
        due_topics = []
        schedule = self.user_performance.get("repetition_schedule", {})
        
        now = datetime.now()
        
        for topic, review_data in schedule.items():
            next_review = datetime.fromisoformat(review_data["next_review"])
            if now >= next_review:
                due_topics.append(topic)
        
        return due_topics
    
    def generate_practice_session(self, duration_minutes: int = 15) -> List[Dict[str, Any]]:
        """Gera sessão de prática personalizada"""
        exercises = []
        target_count = max(3, duration_minutes // 3)  # ~3 min por exercício
        
        # Prioriza revisões pendentes
        due_reviews = self.get_due_reviews()
        weak_areas = self.identify_weak_areas()
        
        # Mistura tópicos: 50% revisões, 30% áreas fracas, 20% aleatório
        topics_to_practice = []
        
        # Adiciona revisões pendentes
        topics_to_practice.extend(due_reviews)
        
        # Adiciona áreas fracas
        topics_to_practice.extend(weak_areas[:2])
        
        # Completa com tópicos aleatórios
        all_topics = list(self.exercise_templates.keys())
        while len(topics_to_practice) < target_count:
            topic = random.choice(all_topics)
            if topic not in topics_to_practice:
                topics_to_practice.append(topic)
        
        # Gera exercícios
        for i in range(min(target_count, len(topics_to_practice))):
            topic = topics_to_practice[i] if i < len(topics_to_practice) else random.choice(all_topics)
            exercise = self.generate_adaptive_exercise(topic)
            exercises.append(exercise)
        
        return exercises
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Gera relatório de performance do usuário"""
        history = self.user_performance.get("exercise_history", [])
        
        if not history:
            return {"status": "no_data", "message": "Nenhum exercício realizado ainda"}
        
        # Estatísticas gerais
        total_exercises = len(history)
        correct_answers = sum(1 for ex in history if ex["correct"])
        accuracy = (correct_answers / total_exercises) * 100 if total_exercises > 0 else 0
        
        # Performance por tópico
        topic_stats = {}
        for exercise in history:
            topic = exercise["topic"]
            if topic not in topic_stats:
                topic_stats[topic] = {"total": 0, "correct": 0, "avg_time": 0}
            
            topic_stats[topic]["total"] += 1
            if exercise["correct"]:
                topic_stats[topic]["correct"] += 1
            topic_stats[topic]["avg_time"] += exercise.get("time_taken", 0)
        
        # Calcula médias
        for topic, stats in topic_stats.items():
            stats["accuracy"] = (stats["correct"] / stats["total"]) * 100
            stats["avg_time"] = stats["avg_time"] // stats["total"]
        
        # Exercícios recentes
        recent_exercises = history[-10:] if len(history) >= 10 else history
        
        return {
            "status": "success",
            "total_exercises": total_exercises,
            "overall_accuracy": accuracy,
            "topic_performance": topic_stats,
            "weak_areas": self.user_performance.get("weak_areas", []),
            "mastered_topics": self.user_performance.get("mastered_topics", []),
            "due_reviews": len(self.get_due_reviews()),
            "recent_streak": self._calculate_recent_streak(recent_exercises),
            "recommended_focus": self._get_recommended_focus()
        }
    
    def _calculate_recent_streak(self, recent_exercises: List[Dict[str, Any]]) -> int:
        """Calcula sequência de acertos recentes"""
        streak = 0
        for exercise in reversed(recent_exercises):
            if exercise["correct"]:
                streak += 1
            else:
                break
        return streak
    
    def _get_recommended_focus(self) -> List[str]:
        """Recomenda tópicos para focar baseado na performance"""
        recommendations = []
        
        # Áreas fracas
        weak_areas = self.identify_weak_areas()
        if weak_areas:
            recommendations.extend(weak_areas[:2])
        
        # Revisões pendentes
        due_reviews = self.get_due_reviews()
        if due_reviews:
            recommendations.extend(due_reviews[:2])
        
        # Remove duplicatas mantendo ordem
        seen = set()
        unique_recommendations = []
        for item in recommendations:
            if item not in seen:
                seen.add(item)
                unique_recommendations.append(item)
        
        return unique_recommendations[:3]  # Top 3 recomendações


class AdaptiveExerciseSession:
    """Sessão interativa de exercícios adaptativos"""
    
    def __init__(self, generator: AdaptiveExerciseGenerator, ui_components):
        self.generator = generator
        self.ui = ui_components
        self.session_results = []
    
    def start_session(self, session_type: str = "mixed") -> None:
        """Inicia sessão de exercícios"""
        self.ui.header("EXERCÍCIOS ADAPTATIVOS", "Treinamento Personalizado", "🎯")
        
        if session_type == "mixed":
            exercises = self.generator.generate_practice_session(15)
        elif session_type == "weak_areas":
            weak_areas = self.generator.identify_weak_areas()
            if weak_areas:
                exercises = [self.generator.generate_adaptive_exercise(topic) for topic in weak_areas[:5]]
            else:
                exercises = self.generator.generate_practice_session(10)
        elif session_type == "reviews":
            due_reviews = self.generator.get_due_reviews()
            if due_reviews:
                exercises = [self.generator.generate_adaptive_exercise(topic) for topic in due_reviews]
            else:
                print("📚 Nenhuma revisão pendente!")
                return
        else:
            exercises = self.generator.generate_practice_session(10)
        
        print(f"🎯 Sessão com {len(exercises)} exercícios personalizados")
        print("💡 Dificuldade ajustada ao seu nível de conhecimento\n")
        
        for i, exercise in enumerate(exercises, 1):
            self._present_exercise(exercise, i, len(exercises))
        
        self._show_session_summary()
    
    def _present_exercise(self, exercise: Dict[str, Any], current: int, total: int) -> None:
        """Apresenta um exercício ao usuário"""
        self.ui.section(f"EXERCÍCIO {current}/{total}", "📝")
        
        print(f"📚 Tópico: {exercise['topic'].replace('_', ' ').title()}")
        print(f"🎯 Nível: {exercise['user_level']}")
        print()
        
        start_time = datetime.now()
        
        if exercise["type"] == ExerciseType.MULTIPLE_CHOICE:
            result = self._handle_multiple_choice(exercise)
        elif exercise["type"] == ExerciseType.CODE_OUTPUT:
            result = self._handle_code_output(exercise)
        elif exercise["type"] == ExerciseType.ERROR_DETECTION:
            result = self._handle_error_detection(exercise)
        elif exercise["type"] == ExerciseType.CODE_COMPLETION:
            result = self._handle_code_completion(exercise)
        else:
            result = self._handle_generic_exercise(exercise)
        
        time_taken = int((datetime.now() - start_time).total_seconds())
        
        # Registra resultado
        self.generator.record_exercise_result(
            exercise, result["user_answer"], result["correct"], time_taken
        )
        
        self.session_results.append({
            "exercise": exercise,
            "result": result,
            "time_taken": time_taken
        })
        
        # Feedback
        if result["correct"]:
            self.ui.alert("✅ Correto! Muito bem!", "success")
        else:
            self.ui.alert(f"❌ Incorreto. {exercise.get('explanation', '')}", "error")
        
        if current < total:
            input("\n⏭️ Pressione ENTER para próximo exercício...")
    
    def _handle_multiple_choice(self, exercise: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com exercício de múltipla escolha"""
        print(f"❓ {exercise['template']}")
        print()
        
        for i, option in enumerate(exercise["options"], 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                answer = int(input("\n👉 Sua resposta (número): ")) - 1
                if 0 <= answer < len(exercise["options"]):
                    break
                else:
                    print("❌ Opção inválida!")
            except ValueError:
                print("❌ Digite um número!")
        
        correct = answer == exercise["correct"]
        user_answer = exercise["options"][answer]
        
        return {
            "user_answer": user_answer,
            "correct": correct,
            "expected": exercise["options"][exercise["correct"]]
        }
    
    def _handle_code_output(self, exercise: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com exercício de prever saída"""
        print(f"❓ {exercise['template']}")
        print("\n📝 Código:")
        print("```python")
        print(exercise["code"])
        print("```")
        
        user_answer = input("\n👉 Qual será a saída? ").strip()
        correct = user_answer.lower() == exercise["output"].lower()
        
        return {
            "user_answer": user_answer,
            "correct": correct,
            "expected": exercise["output"]
        }
    
    def _handle_error_detection(self, exercise: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com exercício de detectar erro"""
        print(f"❓ {exercise['template']}")
        print("\n📝 Código:")
        print("```python")
        print(exercise["code"])
        print("```")
        
        user_answer = input("\n👉 Qual é o erro? ").strip()
        
        # Verifica se a resposta contém palavras-chave do erro
        error_keywords = exercise["error"].lower().split()
        answer_words = user_answer.lower().split()
        
        matches = sum(1 for word in error_keywords if word in answer_words)
        correct = matches >= len(error_keywords) // 2  # Pelo menos metade das palavras-chave
        
        return {
            "user_answer": user_answer,
            "correct": correct,
            "expected": exercise["error"]
        }
    
    def _handle_code_completion(self, exercise: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com exercício de completar código"""
        print(f"❓ {exercise['template']}")
        print("\n📝 Código:")
        print("```python")
        print(exercise["code"])
        print("```")
        
        user_answer = input("\n👉 Complete o código (substitua ___): ").strip()
        correct = user_answer.lower() == exercise["completion"].lower()
        
        return {
            "user_answer": user_answer,
            "correct": correct,
            "expected": exercise["completion"]
        }
    
    def _handle_generic_exercise(self, exercise: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com exercícios genéricos"""
        print(f"❓ {exercise['template']}")
        
        if "code" in exercise:
            print("\n📝 Código:")
            print("```python")
            print(exercise["code"])
            print("```")
        
        user_answer = input("\n👉 Sua resposta: ").strip()
        
        # Verificação genérica (pode ser melhorada)
        expected = exercise.get("expected_answer", "")
        correct = user_answer.lower() == expected.lower()
        
        return {
            "user_answer": user_answer,
            "correct": correct,
            "expected": expected
        }
    
    def _show_session_summary(self) -> None:
        """Mostra resumo da sessão"""
        if not self.session_results:
            return
        
        self.ui.header("RESUMO DA SESSÃO", "Seus Resultados", "📊")
        
        total_exercises = len(self.session_results)
        correct_count = sum(1 for result in self.session_results if result["result"]["correct"])
        accuracy = (correct_count / total_exercises) * 100
        
        total_time = sum(result["time_taken"] for result in self.session_results)
        avg_time = total_time // total_exercises
        
        # Estatísticas gerais
        self.ui.card(
            "Estatísticas da Sessão",
            f"✅ Acertos: {correct_count}/{total_exercises} ({accuracy:.1f}%)\n"
            f"⏱️ Tempo Total: {total_time//60}min {total_time%60}s\n"
            f"🕐 Tempo Médio: {avg_time}s por exercício",
            "📈",
            "success" if accuracy >= 70 else "warning" if accuracy >= 50 else "error"
        )
        
        # Performance por tópico
        topic_performance = {}
        for result in self.session_results:
            topic = result["exercise"]["topic"]
            if topic not in topic_performance:
                topic_performance[topic] = {"total": 0, "correct": 0}
            
            topic_performance[topic]["total"] += 1
            if result["result"]["correct"]:
                topic_performance[topic]["correct"] += 1
        
        if len(topic_performance) > 1:
            print("\n📚 PERFORMANCE POR TÓPICO:")
            for topic, stats in topic_performance.items():
                topic_accuracy = (stats["correct"] / stats["total"]) * 100
                status = "✅" if topic_accuracy >= 70 else "⚠️" if topic_accuracy >= 50 else "❌"
                print(f"{status} {topic.replace('_', ' ').title()}: {stats['correct']}/{stats['total']} ({topic_accuracy:.0f}%)")
        
        # Recomendações
        if accuracy < 70:
            print(f"\n💡 RECOMENDAÇÃO:")
            print(f"Continue praticando! Foque nos tópicos com menor acerto.")
            print(f"Use o Assistente Python (A) para tirar dúvidas.")
        else:
            print(f"\n🎉 EXCELENTE TRABALHO!")
            print(f"Você está dominando bem os conceitos!")
        
        input("\n⏭️ Pressione ENTER para continuar...")