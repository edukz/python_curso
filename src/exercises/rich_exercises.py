#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Exercícios Ricos - Debugging, Code Completion, Output Prediction, Refactoring
"""

from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass
from enum import Enum
import ast
import sys
import io
import contextlib
import traceback
import difflib
import re


class ExerciseType(Enum):
    """Tipos de exercícios disponíveis"""
    DEBUGGING = "debugging"
    CODE_COMPLETION = "code_completion"
    OUTPUT_PREDICTION = "output_prediction"
    CODE_REFACTORING = "code_refactoring"
    MULTIPLE_CHOICE = "multiple_choice"  # Tipo clássico mantido


@dataclass
class Exercise:
    """Estrutura de um exercício"""
    id: str
    type: ExerciseType
    title: str
    description: str
    code: str
    difficulty: int  # 1-5
    points: int
    hints: List[str]
    solution: Any  # Pode ser string, dict, list dependendo do tipo
    explanation: str
    tags: List[str]
    
    # Campos específicos por tipo
    bug_line: Optional[int] = None  # Para debugging
    placeholders: Optional[Dict[str, str]] = None  # Para completion
    expected_output: Optional[str] = None  # Para output prediction
    refactoring_criteria: Optional[List[str]] = None  # Para refactoring


class RichExerciseEngine:
    """Motor de avaliação para exercícios ricos"""
    
    def __init__(self, ui_components=None):
        self.ui = ui_components
        self.current_exercise: Optional[Exercise] = None
        
    def evaluate_exercise(self, exercise: Exercise, user_answer: Any) -> Tuple[bool, str, int]:
        """
        Avalia a resposta do usuário
        
        Returns:
            (correto, feedback, pontos_ganhos)
        """
        if exercise.type == ExerciseType.DEBUGGING:
            return self._evaluate_debugging(exercise, user_answer)
        elif exercise.type == ExerciseType.CODE_COMPLETION:
            return self._evaluate_completion(exercise, user_answer)
        elif exercise.type == ExerciseType.OUTPUT_PREDICTION:
            return self._evaluate_output(exercise, user_answer)
        elif exercise.type == ExerciseType.CODE_REFACTORING:
            return self._evaluate_refactoring(exercise, user_answer)
        else:
            return self._evaluate_multiple_choice(exercise, user_answer)
            
    def _evaluate_debugging(self, exercise: Exercise, user_answer: str) -> Tuple[bool, str, int]:
        """Avalia exercício de debugging"""
        try:
            # Verifica se o código fornecido pelo usuário executa sem erros
            exec_globals = {}
            exec(user_answer, exec_globals)
            
            # Verifica se a correção está na linha esperada (se especificada)
            if exercise.bug_line:
                user_lines = user_answer.strip().split('\n')
                original_lines = exercise.code.strip().split('\n')
                
                if exercise.bug_line <= len(user_lines):
                    if user_lines[exercise.bug_line - 1] != original_lines[exercise.bug_line - 1]:
                        # Linha foi modificada, provavelmente corrigida
                        return True, "✅ Excelente! Você encontrou e corrigiu o bug!", exercise.points
                        
            # Se não há linha específica, verifica se o código funciona
            return True, "✅ Código corrigido com sucesso!", exercise.points
            
        except Exception as e:
            return False, f"❌ O código ainda contém erros: {str(e)}", 0
            
    def _evaluate_completion(self, exercise: Exercise, user_answer: Dict[str, str]) -> Tuple[bool, str, int]:
        """Avalia exercício de completar código"""
        correct_count = 0
        total_count = len(exercise.placeholders)
        feedback_parts = []
        
        for placeholder, expected in exercise.solution.items():
            user_value = user_answer.get(placeholder, "").strip()
            expected_value = expected.strip()
            
            # Verifica correspondência exata ou similar
            if user_value == expected_value:
                correct_count += 1
                feedback_parts.append(f"✅ {placeholder}: Correto!")
            elif user_value.replace(" ", "") == expected_value.replace(" ", ""):
                correct_count += 1
                feedback_parts.append(f"✅ {placeholder}: Correto (espaçamento diferente)")
            else:
                feedback_parts.append(f"❌ {placeholder}: Esperado '{expected_value}'")
                
        # Calcula pontuação parcial
        score = int((correct_count / total_count) * exercise.points)
        
        if correct_count == total_count:
            return True, "✅ Perfeito! Código completado corretamente!\n" + "\n".join(feedback_parts), score
        else:
            return False, f"Parcialmente correto ({correct_count}/{total_count})\n" + "\n".join(feedback_parts), score
            
    def _evaluate_output(self, exercise: Exercise, user_answer: str) -> Tuple[bool, str, int]:
        """Avalia predição de output"""
        # Executa o código para obter output real
        actual_output = self._capture_output(exercise.code)
        
        # Normaliza outputs para comparação
        user_output = user_answer.strip()
        expected_output = actual_output.strip()
        
        if user_output == expected_output:
            return True, "✅ Perfeito! Você previu o output corretamente!", exercise.points
        
        # Verifica se é similar (ignora espaços extras)
        if user_output.replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", ""):
            return True, "✅ Correto! (pequenas diferenças de formatação)", exercise.points
            
        # Fornece feedback detalhado
        diff = difflib.unified_diff(
            user_output.splitlines(keepends=True),
            expected_output.splitlines(keepends=True),
            fromfile='Sua resposta',
            tofile='Output esperado'
        )
        
        feedback = "❌ Output incorreto.\n\nDiferenças:\n" + ''.join(diff)
        return False, feedback, 0
        
    def _evaluate_refactoring(self, exercise: Exercise, user_answer: str) -> Tuple[bool, str, int]:
        """Avalia exercício de refatoração"""
        criteria_met = []
        criteria_failed = []
        
        try:
            # Verifica se o código refatorado funciona
            original_output = self._capture_output(exercise.code)
            refactored_output = self._capture_output(user_answer)
            
            if original_output != refactored_output:
                return False, "❌ O código refatorado não produz o mesmo resultado!", 0
                
            # Avalia critérios de refatoração
            for criterion in exercise.refactoring_criteria:
                if self._check_refactoring_criterion(user_answer, criterion):
                    criteria_met.append(criterion)
                else:
                    criteria_failed.append(criterion)
                    
            # Calcula pontuação
            total_criteria = len(exercise.refactoring_criteria)
            met_count = len(criteria_met)
            score = int((met_count / total_criteria) * exercise.points)
            
            # Gera feedback
            feedback_parts = []
            for criterion in criteria_met:
                feedback_parts.append(f"✅ {criterion}")
            for criterion in criteria_failed:
                feedback_parts.append(f"❌ {criterion}")
                
            if met_count == total_criteria:
                return True, "✅ Excelente refatoração!\n" + "\n".join(feedback_parts), score
            else:
                return False, f"Refatoração parcial ({met_count}/{total_criteria})\n" + "\n".join(feedback_parts), score
                
        except Exception as e:
            return False, f"❌ Erro no código refatorado: {str(e)}", 0
            
    def _evaluate_multiple_choice(self, exercise: Exercise, user_answer: str) -> Tuple[bool, str, int]:
        """Avalia múltipla escolha (compatibilidade)"""
        correct = user_answer.upper() == exercise.solution.upper()
        if correct:
            return True, "✅ Correto!", exercise.points
        else:
            return False, f"❌ Incorreto. A resposta correta é: {exercise.solution}", 0
            
    def _capture_output(self, code: str) -> str:
        """Captura output de um código"""
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        try:
            exec(code)
            output = buffer.getvalue()
        except Exception as e:
            output = f"Erro: {str(e)}"
        finally:
            sys.stdout = old_stdout
            
        return output
        
    def _check_refactoring_criterion(self, code: str, criterion: str) -> bool:
        """Verifica se um critério de refatoração foi atendido"""
        criterion_lower = criterion.lower()
        
        # Critérios comuns
        if "função" in criterion_lower or "function" in criterion_lower:
            return "def " in code
        elif "list comprehension" in criterion_lower:
            return "[" in code and " for " in code and " in " in code
        elif "f-string" in criterion_lower:
            return re.search(r'f["\'].*{.*}.*["\']', code) is not None
        elif "constante" in criterion_lower or "constant" in criterion_lower:
            # Verifica se há variáveis em MAIÚSCULAS
            return bool(re.search(r'\b[A-Z_]+\b\s*=', code))
        elif "comentário" in criterion_lower or "comment" in criterion_lower:
            return "#" in code
        elif "docstring" in criterion_lower:
            return '"""' in code or "'''" in code
        elif "type hint" in criterion_lower:
            return "->" in code or ": " in re.findall(r'def\s+\w+\s*\([^)]*\)', code)[0] if "def" in code else False
            
        # Critério genérico: verifica se a palavra-chave está no código
        return criterion.lower() in code.lower()


class ExerciseGenerator:
    """Gerador de exercícios para diferentes módulos"""
    
    @staticmethod
    def generate_debugging_exercise(module: str, topic: str) -> Exercise:
        """Gera exercício de debugging para um tópico"""
        # Exemplo para variáveis
        if topic == "variables":
            return Exercise(
                id="debug_var_1",
                type=ExerciseType.DEBUGGING,
                title="Encontre o Bug: Variáveis",
                description="O código abaixo deveria calcular a média de 3 notas, mas está com erro. Corrija!",
                code="""nota1 = 8.5
nota2 = 7.0
nota3 = 9.5
media = nota1 + nota2 + nota3 / 3  # Bug aqui!
print(f"A média é: {media}")""",
                difficulty=2,
                points=15,
                hints=[
                    "Verifique a ordem das operações matemáticas",
                    "Lembre-se da precedência: divisão antes da soma",
                    "Você precisa de parênteses?"
                ],
                solution="""nota1 = 8.5
nota2 = 7.0
nota3 = 9.5
media = (nota1 + nota2 + nota3) / 3  # Corrigido!
print(f"A média é: {media}")""",
                explanation="O erro estava na precedência das operações. Sem parênteses, apenas nota3 era dividida por 3!",
                tags=["variáveis", "operadores", "precedência"],
                bug_line=4
            )
            
    @staticmethod
    def generate_completion_exercise(module: str, topic: str) -> Exercise:
        """Gera exercício de completar código"""
        if topic == "loops":
            return Exercise(
                id="complete_loop_1",
                type=ExerciseType.CODE_COMPLETION,
                title="Complete o Loop",
                description="Complete o código para imprimir apenas números pares de 1 a 10",
                code="""for i in _____(1, 11):
    if i % 2 == _____:
        print(i)""",
                difficulty=2,
                points=20,
                hints=[
                    "Use range() para gerar sequência",
                    "Números pares têm resto 0 na divisão por 2"
                ],
                placeholders={
                    "blank1": "range",
                    "blank2": "0"
                },
                solution={
                    "blank1": "range",
                    "blank2": "0"
                },
                explanation="range(1, 11) gera números de 1 a 10, e i % 2 == 0 verifica se é par",
                tags=["loops", "condicionais", "range"]
            )
            
    @staticmethod 
    def generate_output_exercise(module: str, topic: str) -> Exercise:
        """Gera exercício de prever output"""
        if topic == "lists":
            return Exercise(
                id="output_list_1",
                type=ExerciseType.OUTPUT_PREDICTION,
                title="Preveja o Output",
                description="O que será impresso pelo código abaixo?",
                code="""lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.pop(0)
print(lista[2])
print(len(lista))""",
                difficulty=3,
                points=25,
                hints=[
                    "append adiciona ao final",
                    "pop(0) remove o primeiro elemento",
                    "Índices começam em 0"
                ],
                solution="4\n5",
                expected_output="4\n5",
                explanation="Após append(6): [1,2,3,4,5,6]. Após pop(0): [2,3,4,5,6]. lista[2] = 4, len = 5",
                tags=["listas", "métodos", "índices"]
            )
            
    @staticmethod
    def generate_refactoring_exercise(module: str, topic: str) -> Exercise:
        """Gera exercício de refatoração"""
        if topic == "functions":
            return Exercise(
                id="refactor_func_1",
                type=ExerciseType.CODE_REFACTORING,
                title="Refatore o Código",
                description="Melhore este código seguindo boas práticas",
                code="""x = input("Digite um número: ")
y = input("Digite outro número: ")
x = int(x)
y = int(y)
resultado = x + y
print("O resultado é: " + str(resultado))""",
                difficulty=3,
                points=30,
                hints=[
                    "Crie uma função reutilizável",
                    "Use f-strings para formatação",
                    "Adicione tratamento de erros"
                ],
                solution="""def somar_numeros():
    '''Solicita dois números e retorna a soma'''
    try:
        x = int(input("Digite um número: "))
        y = int(input("Digite outro número: "))
        resultado = x + y
        print(f"O resultado é: {resultado}")
        return resultado
    except ValueError:
        print("Por favor, digite apenas números!")
        return None

somar_numeros()""",
                explanation="Código refatorado com função, docstring, f-string e tratamento de erros",
                tags=["funções", "refatoração", "boas práticas"],
                refactoring_criteria=[
                    "Usar função",
                    "Usar f-string",
                    "Adicionar docstring",
                    "Tratamento de erros"
                ]
            )