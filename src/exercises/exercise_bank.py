#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Banco de Exercícios Ricos - Coleção organizada por módulo e dificuldade
"""

from .rich_exercises import Exercise, ExerciseType


class ExerciseBank:
    """Banco de dados de exercícios organizados por módulo"""
    
    @staticmethod
    def get_exercises_by_module(module_number: int) -> list:
        """Retorna exercícios para um módulo específico"""
        
        if module_number == 1:  # Introdução ao Python
            return ExerciseBank._module_1_exercises()
        elif module_number == 2:  # Primeiro Programa
            return ExerciseBank._module_2_exercises()
        elif module_number == 3:  # Variáveis
            return ExerciseBank._module_3_exercises()
        elif module_number == 4:  # Tipos de Dados
            return ExerciseBank._module_4_exercises()
        elif module_number == 7:  # Condições
            return ExerciseBank._module_7_exercises()
        elif module_number == 8:  # Loops
            return ExerciseBank._module_8_exercises()
        elif module_number == 9:  # Listas
            return ExerciseBank._module_9_exercises()
        elif module_number == 10:  # Funções
            return ExerciseBank._module_10_exercises()
        else:
            return []
            
    @staticmethod
    def _module_1_exercises():
        """Exercícios do Módulo 1 - Introdução"""
        return [
            Exercise(
                id="intro_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Primeiro Print",
                description="Corrija o erro neste primeiro programa Python",
                code='print("Olá, Mundo!"',  # Missing closing parenthesis
                difficulty=1,
                points=10,
                hints=["Verifique os parênteses", "Todo print() precisa ser fechado"],
                solution='print("Olá, Mundo!")',
                explanation="O erro era a falta do parênteses de fechamento na função print()",
                tags=["sintaxe", "print", "parênteses"]
            ),
            
            Exercise(
                id="intro_output_1",
                type=ExerciseType.OUTPUT_PREDICTION,
                title="Output: Múltiplos Prints",
                description="O que será impresso?",
                code='''print("Python")
print("é")
print("incrível!")''',
                difficulty=1,
                points=15,
                hints=["Cada print() cria uma nova linha"],
                solution="Python\né\nincrível!",
                explanation="Cada comando print() imprime em uma linha separada",
                tags=["print", "output", "quebra de linha"]
            )
        ]
        
    @staticmethod
    def _module_2_exercises():
        """Exercícios do Módulo 2 - Primeiro Programa"""
        return [
            Exercise(
                id="prog_completion_1",
                type=ExerciseType.CODE_COMPLETION,
                title="Complete: Programa de Saudação",
                description="Complete o programa que cumprimenta o usuário",
                code='''nome = _____("Qual é o seu nome? ")
_____(f"Olá, {nome}!")''',
                difficulty=1,
                points=15,
                hints=["Use input() para ler dados", "Use print() para exibir"],
                placeholders={"blank1": "input", "blank2": "print"},
                solution={"blank1": "input", "blank2": "print"},
                explanation="input() lê dados do usuário e print() exibe mensagens",
                tags=["input", "print", "f-string"]
            )
        ]
        
    @staticmethod
    def _module_3_exercises():
        """Exercícios do Módulo 3 - Variáveis"""
        return [
            Exercise(
                id="var_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Troca de Variáveis",
                description="Corrija o código que deveria trocar os valores de duas variáveis",
                code='''a = 10
b = 20
print(f"Antes: a={a}, b={b}")
a = b
b = a  # Bug aqui!
print(f"Depois: a={a}, b={b}")''',
                difficulty=2,
                points=20,
                hints=["Você precisa de uma variável temporária", "O valor original de 'a' se perde"],
                solution='''a = 10
b = 20
print(f"Antes: a={a}, b={b}")
temp = a
a = b
b = temp
print(f"Depois: a={a}, b={b}")''',
                explanation="Sem variável temporária, o valor original de 'a' se perde quando a=b",
                tags=["variáveis", "atribuição", "troca"],
                bug_line=5
            ),
            
            Exercise(
                id="var_refactor_1",
                type=ExerciseType.CODE_REFACTORING,
                title="Refatore: Nomes de Variáveis",
                description="Melhore os nomes das variáveis neste código",
                code='''x = "João"
y = 25
z = 1.75
print(f"{x} tem {y} anos e {z}m de altura")''',
                difficulty=2,
                points=25,
                hints=["Use nomes descritivos", "Evite x, y, z para dados reais"],
                solution='''nome = "João"
idade = 25
altura = 1.75
print(f"{nome} tem {idade} anos e {altura}m de altura")''',
                explanation="Nomes descritivos tornam o código mais legível e manutenível",
                tags=["variáveis", "nomenclatura", "legibilidade"],
                refactoring_criteria=["Nomes descritivos", "Sem variáveis genéricas"]
            )
        ]
        
    @staticmethod
    def _module_4_exercises():
        """Exercícios do Módulo 4 - Tipos de Dados"""
        return [
            Exercise(
                id="types_output_1",
                type=ExerciseType.OUTPUT_PREDICTION,
                title="Output: Concatenação vs Soma",
                description="Preveja o resultado das operações",
                code='''a = "5"
b = "3"
c = 5
d = 3
print(a + b)
print(c + d)
print(type(a))
print(type(c))''',
                difficulty=2,
                points=20,
                hints=["String + String = concatenação", "Int + Int = soma matemática"],
                solution="53\n8\n<class 'str'>\n<class 'int'>",
                explanation="Strings se concatenam ('5' + '3' = '53'), números se somam (5 + 3 = 8)",
                tags=["tipos", "string", "int", "concatenação"]
            ),
            
            Exercise(
                id="types_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Conversão de Tipos",
                description="Corrija o erro de tipos neste calculador",
                code='''num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
soma = num1 + num2  # Bug!
print(f"A soma é: {soma}")''',
                difficulty=2,
                points=20,
                hints=["input() sempre retorna string", "Use int() ou float() para converter"],
                solution='''num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma é: {soma}")''',
                explanation="input() retorna string, então '5' + '3' = '53' ao invés de 8",
                tags=["tipos", "conversão", "input", "int"],
                bug_line=3
            )
        ]
        
    @staticmethod
    def _module_7_exercises():
        """Exercícios do Módulo 7 - Condições"""
        return [
            Exercise(
                id="if_completion_1",
                type=ExerciseType.CODE_COMPLETION,
                title="Complete: Verificador de Idade",
                description="Complete o código que verifica se alguém é maior de idade",
                code='''idade = int(input("Digite sua idade: "))
_____ idade >= 18:
    print("Você é maior de idade")
_____:
    print("Você é menor de idade")''',
                difficulty=2,
                points=20,
                hints=["Use 'if' para condição", "Use 'else' para alternativa"],
                placeholders={"blank1": "if", "blank2": "else"},
                solution={"blank1": "if", "blank2": "else"},
                explanation="if testa condição, else executa quando condição é falsa",
                tags=["condicionais", "if", "else"]
            ),
            
            Exercise(
                id="if_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Nota do Aluno",
                description="Corrija a lógica de classificação das notas",
                code='''nota = float(input("Digite a nota: "))
if nota >= 9:
    print("Excelente!")
if nota >= 7:  # Bug aqui!
    print("Bom!")
if nota >= 5:
    print("Razoável")
else:
    print("Insuficiente")''',
                difficulty=3,
                points=25,
                hints=["Use elif para condições mutuamente exclusivas", "Apenas uma classificação deve aparecer"],
                solution='''nota = float(input("Digite a nota: "))
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
elif nota >= 5:
    print("Razoável")
else:
    print("Insuficiente")''',
                explanation="Sem elif, múltiplas condições podem ser verdadeiras simultaneamente",
                tags=["condicionais", "elif", "lógica"],
                bug_line=4
            )
        ]
        
    @staticmethod
    def _module_8_exercises():
        """Exercícios do Módulo 8 - Loops"""
        return [
            Exercise(
                id="loop_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Loop Infinito",
                description="Corrija este loop que nunca termina",
                code='''contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    # Bug: falta incrementar contador!
print("Fim da contagem")''',
                difficulty=2,
                points=20,
                hints=["O contador precisa ser modificado", "Use contador += 1"],
                solution='''contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1
print("Fim da contagem")''',
                explanation="Sem incrementar o contador, a condição sempre será verdadeira",
                tags=["loops", "while", "incremento"],
                bug_line=3
            ),
            
            Exercise(
                id="loop_refactor_1",
                type=ExerciseType.CODE_REFACTORING,
                title="Refatore: For em While",
                description="Converta este while em um for mais elegante",
                code='''i = 0
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1''',
                difficulty=3,
                points=25,
                hints=["Use range() com for", "For é mais limpo para contagens"],
                solution='''for i in range(10):
    if i % 2 == 0:
        print(i)''',
                explanation="For com range() é mais conciso e menos propenso a erros",
                tags=["loops", "for", "range", "refatoração"],
                refactoring_criteria=["Usar for", "Usar range()", "Código mais conciso"]
            )
        ]
        
    @staticmethod
    def _module_9_exercises():
        """Exercícios do Módulo 9 - Listas"""
        return [
            Exercise(
                id="list_output_1",
                type=ExerciseType.OUTPUT_PREDICTION,
                title="Output: Operações com Lista",
                description="Preveja o estado final da lista",
                code='''frutas = ["maçã", "banana"]
frutas.append("laranja")
frutas.insert(1, "uva")
frutas.remove("banana")
print(frutas)
print(len(frutas))''',
                difficulty=3,
                points=25,
                hints=["insert(1, x) adiciona na posição 1", "remove() elimina primeira ocorrência"],
                solution="['maçã', 'uva', 'laranja']\n3",
                explanation="Após todas operações: ['maçã', 'uva', 'laranja'] com 3 elementos",
                tags=["listas", "métodos", "append", "insert", "remove"]
            ),
            
            Exercise(
                id="list_completion_1",
                type=ExerciseType.CODE_COMPLETION,
                title="Complete: List Comprehension",
                description="Complete a list comprehension para números pares",
                code='''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x _____ x _____ numeros _____ x % 2 == 0]
print(pares)''',
                difficulty=4,
                points=30,
                hints=["Formato: [expressão for item in lista if condição]"],
                placeholders={"blank1": "for", "blank2": "in", "blank3": "if"},
                solution={"blank1": "for", "blank2": "in", "blank3": "if"},
                explanation="List comprehension: [expressão for item in lista if condição]",
                tags=["listas", "list comprehension", "filtros"]
            )
        ]
        
    @staticmethod
    def _module_10_exercises():
        """Exercícios do Módulo 10 - Funções"""
        return [
            Exercise(
                id="func_refactor_1",
                type=ExerciseType.CODE_REFACTORING,
                title="Refatore: Código Repetitivo",
                description="Elimine a repetição criando uma função",
                code='''# Cálculo do perímetro de três retângulos
largura1, altura1 = 5, 3
perimetro1 = 2 * (largura1 + altura1)
print(f"Perímetro 1: {perimetro1}")

largura2, altura2 = 7, 4
perimetro2 = 2 * (largura2 + altura2)
print(f"Perímetro 2: {perimetro2}")

largura3, altura3 = 2, 8
perimetro3 = 2 * (largura3 + altura3)
print(f"Perímetro 3: {perimetro3}")''',
                difficulty=3,
                points=35,
                hints=["Crie função calcular_perimetro()", "Use parâmetros largura e altura"],
                solution='''def calcular_perimetro(largura, altura):
    """Calcula o perímetro de um retângulo"""
    return 2 * (largura + altura)

# Testando com três retângulos
print(f"Perímetro 1: {calcular_perimetro(5, 3)}")
print(f"Perímetro 2: {calcular_perimetro(7, 4)}")
print(f"Perímetro 3: {calcular_perimetro(2, 8)}")''',
                explanation="Função elimina repetição e torna código mais legível e reutilizável",
                tags=["funções", "DRY", "refatoração", "reutilização"],
                refactoring_criteria=["Criar função", "Eliminar repetição", "Adicionar docstring"]
            ),
            
            Exercise(
                id="func_debug_1",
                type=ExerciseType.DEBUGGING,
                title="Debug: Escopo de Variável",
                description="Corrija o erro de escopo nesta função",
                code='''def calcular_area(raio):
    pi = 3.14159
    area = pi * raio ** 2
    return area

resultado = calcular_area(5)
print(f"Área: {area}")  # Bug: 'area' não existe aqui!''',
                difficulty=3,
                points=25,
                hints=["Variáveis dentro da função só existem lá", "Use a variável 'resultado'"],
                solution='''def calcular_area(raio):
    pi = 3.14159
    area = pi * raio ** 2
    return area

resultado = calcular_area(5)
print(f"Área: {resultado}")''',
                explanation="Variáveis locais (como 'area') só existem dentro da função",
                tags=["funções", "escopo", "variáveis locais", "return"],
                bug_line=7
            )
        ]