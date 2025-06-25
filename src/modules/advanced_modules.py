#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulos Avançados do Curso Interativo de Python
Contém os módulos mais complexos e profissionais
"""

try:
    from ..utils import PythonCourseUtils
except ImportError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils import PythonCourseUtils


class AdvancedModules:
    """Classe que contém os módulos avançados do curso"""
    
    def __init__(self):
        self.utils = PythonCourseUtils()

    def modulo_12_dicionarios(self) -> None:
        """Módulo 12: Dicionários e Sets"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 12: DICIONÁRIOS E SETS - ESTRUTURAS AVANÇADAS")
        
        print("📚 Vamos aprender sobre Dicionários e Sets!")
        print("🔑 Estruturas de dados fundamentais para programação avançada!")
        
        print("\n═══════════════════════════════════════════════")
        print("        DICIONÁRIOS - CHAVE:VALOR")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Dicionário = coleção de pares chave:valor")
        print("📋 Características:")
        print("• 🔑 Chaves únicas")
        print("• 📦 Valores podem ser qualquer tipo")
        print("• 🚀 Busca muito rápida")
        print("• 🔄 Mutável (pode ser modificado)")
        
        self.utils.pausar()
        
        codigo1 = '''# Criando e usando dicionários
# Diferentes formas de criar
dicionario1 = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
dicionario2 = dict(nome="Maria", idade=30, cidade="Rio de Janeiro")
dicionario3 = {}  # Dicionário vazio

print("Dicionário 1:", dicionario1)
print("Dicionário 2:", dicionario2)

# Acessando valores
print("\\nNome:", dicionario1["nome"])
print("Idade:", dicionario1["idade"])

# Método get() - mais seguro
print("Cidade:", dicionario1.get("cidade"))
print("País:", dicionario1.get("pais", "Brasil"))  # Valor padrão

# Adicionando/modificando
dicionario1["profissao"] = "Programador"
dicionario1["idade"] = 26  # Modifica valor existente

print("\\nDicionário atualizado:", dicionario1)'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🛠️ Métodos de Dicionários:")
        
        codigo2 = '''# Métodos importantes de dicionários
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira",
    "salario": 8000,
    "hobbies": ["leitura", "natação", "culinária"]
}

print("=== MÉTODOS DE DICIONÁRIOS ===")

# keys(), values(), items()
print("Chaves:", list(pessoa.keys()))
print("Valores:", list(pessoa.values()))
print("Itens:", list(pessoa.items()))

# Iterando sobre dicionário
print("\\n=== ITERAÇÃO ===")
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

print("\\n=== ITERAÇÃO COM ITEMS ===")
for chave, valor in pessoa.items():
    print(f"{chave} -> {valor}")

# Removendo elementos
print("\\n=== REMOÇÃO ===")
# pop() - remove e retorna valor
salario = pessoa.pop("salario")
print(f"Salário removido: {salario}")

# del - remove chave
del pessoa["hobbies"]
print("Após remoções:", pessoa)

# clear() - remove tudo
copia = pessoa.copy()
copia.clear()
print("Dicionário limpo:", copia)'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n📦 SETS - Conjuntos:")
        
        codigo3 = '''# Sets - conjuntos únicos
# Criando sets
set1 = {1, 2, 3, 4, 5}
set2 = set([2, 3, 4, 5, 6])
set3 = set("python")  # Set de caracteres

print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)

# Sets removem duplicatas automaticamente
numeros_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set_unicos = set(numeros_duplicados)
print("\\nNúmeros únicos:", set_unicos)

# Operações de conjuntos
print("\\n=== OPERAÇÕES DE CONJUNTOS ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A: {A}")
print(f"B: {B}")

# União
print(f"A ∪ B (união): {A | B}")
print(f"A ∪ B (union): {A.union(B)}")

# Interseção
print(f"A ∩ B (interseção): {A & B}")
print(f"A ∩ B (intersection): {A.intersection(B)}")

# Diferença
print(f"A - B (diferença): {A - B}")
print(f"B - A (diferença): {B - A}")

# Diferença simétrica
print(f"A △ B (dif. simétrica): {A ^ B}")

# Verificações
print(f"\\n4 está em A? {4 in A}")
print(f"9 está em B? {9 in B}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.exercicio(
            "Como acessar um valor de dicionário com segurança?",
            ["get()", "método get", ".get()"],
            "Use o método get() que retorna None se a chave não existir"
        )
        
        # Mini Projeto do Módulo 12
        self._mini_projeto_modulo_12()

    def modulo_13_funcoes_avancadas(self) -> None:
        """Módulo 13: Funções Avançadas & Lambda"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 13: FUNÇÕES AVANÇADAS & LAMBDA")
        
        print("⚡ Vamos dominar funcionalidades AVANÇADAS de funções!")
        print("🚀 Lambda, *args, **kwargs e muito mais!")
        
        print("\n═══════════════════════════════════════════════")
        print("        PARÂMETROS FLEXÍVEIS")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 *args = argumentos posicionais variáveis")
        print("🎯 **kwargs = argumentos nomeados variáveis")
        print("✨ Tornam funções muito mais flexíveis!")
        
        self.utils.pausar()
        
        codigo1 = '''# *args - argumentos posicionais variáveis
def somar_todos(*numeros):
    """Soma qualquer quantidade de números"""
    print(f"Recebido: {numeros}")  # É uma tupla
    total = 0
    for num in numeros:
        total += num
    return total

# Testando *args
print("=== TESTANDO *ARGS ===")
print("Soma de 1, 2, 3:", somar_todos(1, 2, 3))
print("Soma de 10, 20:", somar_todos(10, 20))
print("Soma de 1, 2, 3, 4, 5, 6:", somar_todos(1, 2, 3, 4, 5, 6))

# **kwargs - argumentos nomeados variáveis
def criar_perfil(nome, **informacoes):
    """Cria perfil com informações flexíveis"""
    print(f"\\n=== PERFIL DE {nome.upper()} ===")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

# Testando **kwargs
print("\\n=== TESTANDO **KWARGS ===")
criar_perfil("João", idade=25, cidade="São Paulo", profissao="Programador")
criar_perfil("Maria", idade=30, empresa="TechCorp", salario=8000, hobbies="Natação")

# Combinando tudo
def funcao_completa(obrigatorio, padrao="valor padrão", *args, **kwargs):
    """Função com todos os tipos de parâmetros"""
    print(f"\\nObrigatório: {obrigatorio}")
    print(f"Padrão: {padrao}")
    print(f"Args extras: {args}")
    print(f"Kwargs extras: {kwargs}")

print("\\n=== FUNÇÃO COMPLETA ===")
funcao_completa("necessário", "customizado", 1, 2, 3, nome="Python", ano=2023)'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n⚡ LAMBDA - Funções Anônimas:")
        
        codigo2 = '''# Lambda - funções anônimas
print("=== FUNÇÕES LAMBDA ===")

# Função normal vs Lambda
def quadrado_normal(x):
    return x ** 2

quadrado_lambda = lambda x: x ** 2

print(f"Quadrado normal de 5: {quadrado_normal(5)}")
print(f"Quadrado lambda de 5: {quadrado_lambda(5)}")

# Lambdas com múltiplos parâmetros
somar = lambda a, b: a + b
maior = lambda a, b: a if a > b else b

print(f"\\nSoma 10 + 20 = {somar(10, 20)}")
print(f"Maior entre 15 e 8 = {maior(15, 8)}")

# Lambdas em listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - aplica função a todos elementos
quadrados = list(map(lambda x: x**2, numeros))
print(f"\\nQuadrados: {quadrados}")

# filter() - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Exemplo prático - lista de dicionários
pessoas = [
    {"nome": "Ana", "idade": 25, "salario": 5000},
    {"nome": "Bruno", "idade": 30, "salario": 6000},
    {"nome": "Carlos", "idade": 35, "salario": 7000}
]

# Ordenar por idade
por_idade = sorted(pessoas, key=lambda p: p["idade"])
print(f"\\nPor idade: {[p['nome'] for p in por_idade]}")

# Ordenar por salário (decrescente)
por_salario = sorted(pessoas, key=lambda p: p["salario"], reverse=True)
print(f"Por salário: {[p['nome'] for p in por_salario]}")

# Filtrar salário > 5500
bem_pagos = list(filter(lambda p: p["salario"] > 5500, pessoas))
print(f"Bem pagos: {[p['nome'] for p in bem_pagos]}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.exercicio(
            "Como criar uma função lambda que multiplica dois números?",
            ["lambda a, b: a * b", "lambda x, y: x * y"],
            "lambda a, b: a * b"
        )
        
        # Mini Projeto do Módulo 13
        self._mini_projeto_modulo_13()

    def modulo_14_comprehensions(self) -> None:
        """Módulo 14: List/Dict Comprehensions"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 14: COMPREHENSIONS - PYTHON PYTHÔNICO")
        
        print("🐍 Agora vamos aprender o que torna Python REALMENTE elegante!")
        print("✨ Comprehensions = criar listas/dicts de forma CONCISA e PODEROSA!")
        
        print("\n═══════════════════════════════════════════════")
        print("        LIST COMPREHENSIONS")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Sintaxe: [expressão for item in iterável if condição]")
        print("💡 Substitui loops for + append de forma elegante!")
        
        self.utils.pausar()
        
        # List comprehensions básicas
        codigo1 = '''# Jeito tradicional vs Comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# MÉTODO TRADICIONAL
quadrados_tradicional = []
for n in numeros:
    quadrados_tradicional.append(n ** 2)

# LIST COMPREHENSION - mais elegante!
quadrados_comprehension = [n ** 2 for n in numeros]

print("Tradicional:", quadrados_tradicional)
print("Comprehension:", quadrados_comprehension)

# Mais exemplos
pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)

dobrados = [n * 2 for n in range(1, 6)]
print("Dobrados:", dobrados)

# Com strings
palavras = ["python", "java", "javascript", "go"]
maiusculas = [palavra.upper() for palavra in palavras]
print("Maiúsculas:", maiusculas)

# Filtrando strings
palavras_grandes = [palavra for palavra in palavras if len(palavra) > 4]
print("Palavras grandes:", palavras_grandes)'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔥 Comprehensions Complexas:")
        
        codigo2 = '''# Comprehensions mais avançadas
import math

# Nested loops em comprehension
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz 3x3:")
for linha in matriz:
    print(linha)

# Múltiplas condições
numeros = range(1, 21)
especiais = [n for n in numeros if n % 2 == 0 if n % 3 == 0]
print("\\nPares E divisíveis por 3:", especiais)

# Operações matemáticas
import math
raizes = [round(math.sqrt(n), 2) for n in range(1, 11)]
print("Raízes quadradas:", raizes)

# Trabalhando com dicionários na lista
pessoas = [
    {"nome": "Ana", "idade": 25, "salario": 5000},
    {"nome": "Bruno", "idade": 30, "salario": 6000},
    {"nome": "Carlos", "idade": 35, "salario": 7000}
]

nomes = [pessoa["nome"] for pessoa in pessoas]
print("\\nNomes:", nomes)

bem_pagos = [p["nome"] for p in pessoas if p["salario"] > 5500]
print("Bem pagos:", bem_pagos)'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n📚 DICT COMPREHENSIONS:")
        
        codigo3 = '''# Dictionary Comprehensions
numeros = [1, 2, 3, 4, 5]

# Criando dicionário com comprehension
quadrados_dict = {n: n**2 for n in numeros}
print("Dicionário de quadrados:", quadrados_dict)

# Com condição
pares_dict = {n: n**2 for n in numeros if n % 2 == 0}
print("Só números pares:", pares_dict)

# Transformando lista em dict
frutas = ["maçã", "banana", "laranja"]
tamanhos = {fruta: len(fruta) for fruta in frutas}
print("Tamanho das palavras:", tamanhos)

# Invertendo dicionário
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
print("Dicionário invertido:", invertido)

# Exemplo prático - contagem de caracteres
texto = "python"
contagem = {char: texto.count(char) for char in set(texto)}
print("Contagem de caracteres:", contagem)'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n🎭 SET COMPREHENSIONS:")
        
        codigo4 = '''# Set Comprehensions
texto = "programacao python"

# Vogais únicas
vogais = {char for char in texto if char in "aeiou"}
print("Vogais encontradas:", vogais)

# Números únicos de uma operação
numeros = [1, 2, 2, 3, 3, 4, 4, 5]
quadrados_unicos = {n**2 for n in numeros}
print("Quadrados únicos:", quadrados_unicos)

# Primeira letra de cada palavra
frase = "Python é uma linguagem incrível"
primeiras_letras = {palavra[0].lower() for palavra in frase.split()}
print("Primeiras letras:", primeiras_letras)'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n⚡ GENERATOR EXPRESSIONS:")
        
        codigo5 = '''# Generator Expressions - economizam memória!
import sys

# Lista normal (ocupa mais memória)
lista_normal = [n**2 for n in range(1000)]
print("Tamanho da lista:", sys.getsizeof(lista_normal), "bytes")

# Generator (ocupa menos memória)
generator = (n**2 for n in range(1000))
print("Tamanho do generator:", sys.getsizeof(generator), "bytes")

# Usando o generator
print("\\nPrimeiros 10 quadrados:")
for i, quadrado in enumerate(generator):
    if i >= 10:
        break
    print(quadrado, end=" ")

print("\\n\\n# Generator para grandes datasets")
# Útil para arquivos grandes ou cálculos pesados
grandes_numeros = (n for n in range(1, 1000000) if n % 123456 == 0)
print("Números divisíveis por 123456:")
for num in grandes_numeros:
    print(num, end=" ")
    
print("\\n\\n# Soma eficiente com generator")
soma_eficiente = sum(n**2 for n in range(1, 1001))
print(f"Soma dos quadrados de 1 a 1000: {soma_eficiente}")'''
        
        self.utils.exemplo(codigo5)
        self.utils.executar_codigo(codigo5)
        
        # Exercícios
        self.utils.exercicio(
            "Como criar uma lista dos quadrados de 1 a 5 com list comprehension?",
            ["[n**2 for n in range(1, 6)]", "[x*x for x in range(1,6)]"],
            "Use for com range e exponenciação"
        )
        
        self.utils.exercicio(
            "Qual a diferença entre [] e () em comprehensions?",
            ["lista vs generator", "list vs generator", "memória"],
            "[] cria lista, () cria generator"
        )
        
        # Mini Projeto do Módulo 14
        self._mini_projeto_modulo_14()

    def modulo_15_arquivos(self) -> None:
        """Módulo 15: Manipulação de Arquivos"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 15: MANIPULAÇÃO DE ARQUIVOS - PERSISTÊNCIA DE DADOS")
        
        print("📁 Agora vamos aprender a SALVAR e CARREGAR dados!")
        print("💾 Arquivos são fundamentais para guardar informações!")
        
        print("\n═══════════════════════════════════════════════")
        print("        LENDO E ESCREVENDO ARQUIVOS")
        print("═══════════════════════════════════════════════")
        
        print("\n📝 Modos de abertura:")
        print("• 'r' - Leitura (read)")
        print("• 'w' - Escrita (write) - APAGA o arquivo!")
        print("• 'a' - Anexar (append) - adiciona no final")
        print("• 'r+' - Leitura e escrita")
        
        self.utils.pausar()
        
        # Escrevendo arquivos
        codigo1 = '''# Escrevendo arquivos
# Método básico
arquivo = open("teste.txt", "w", encoding="utf-8")
arquivo.write("Olá, mundo!\\n")
arquivo.write("Este é meu primeiro arquivo em Python.\\n")
arquivo.close()

print("✅ Arquivo 'teste.txt' criado!")

# Método recomendado - with statement
with open("lista_compras.txt", "w", encoding="utf-8") as arquivo:
    compras = ["Arroz", "Feijão", "Açúcar", "Café", "Leite"]
    for item in compras:
        arquivo.write(f"- {item}\\n")

print("✅ Lista de compras salva!")

# Múltiplas linhas de uma vez
conteudo = """Este é um arquivo de múltiplas linhas.
Linha 2 do arquivo.
Linha 3 com alguns dados.
Final do arquivo."""

with open("multiplas_linhas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)

print("✅ Arquivo com múltiplas linhas criado!")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n📖 Lendo arquivos:")
        
        codigo2 = '''# Lendo arquivos
print("=== LENDO ARQUIVO COMPLETO ===")
try:
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("❌ Arquivo não encontrado! Vamos criar um.")
    with open("teste.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Arquivo de exemplo\\nSegunda linha\\n")
    print("✅ Arquivo criado. Lendo agora...")
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

print("\\n=== LENDO LINHA POR LINHA ===")
with open("teste.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas, 1):
        print(f"Linha {i}: {linha.strip()}")

print("\\n=== LENDO COM LOOP ===")
with open("teste.txt", "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, 1):
        print(f"{numero:02d}: {linha.rstrip()}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n💼 Exemplo Prático - Sistema de Cadastro:")
        
        codigo3 = '''# Sistema de cadastro em arquivo
import json
from datetime import datetime

def salvar_pessoa(nome, idade, email):
    """Salva dados de uma pessoa no arquivo"""
    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cadastrado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Lê pessoas existentes
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
    except FileNotFoundError:
        pessoas = []
    
    # Adiciona nova pessoa
    pessoas.append(pessoa)
    
    # Salva tudo de volta
    with open("pessoas.json", "w", encoding="utf-8") as arquivo:
        json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
    
    print(f"✅ {nome} cadastrado com sucesso!")

def listar_pessoas():
    """Lista todas as pessoas cadastradas"""
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
        
        print("\\n=== PESSOAS CADASTRADAS ===")
        for i, pessoa in enumerate(pessoas, 1):
            print(f"{i}. {pessoa['nome']} ({pessoa['idade']} anos)")
            print(f"   Email: {pessoa['email']}")
            print(f"   Cadastrado em: {pessoa['cadastrado_em']}")
            print()
    except FileNotFoundError:
        print("❌ Nenhuma pessoa cadastrada ainda.")

# Testando o sistema
salvar_pessoa("João Silva", 30, "joao@email.com")
salvar_pessoa("Maria Santos", 25, "maria@email.com")
salvar_pessoa("Pedro Costa", 35, "pedro@email.com")

listar_pessoas()'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n🛡️ Tratamento de Erros com Arquivos:")
        
        codigo4 = '''# Tratamento robusto de erros
def ler_arquivo_seguro(nome_arquivo):
    """Lê arquivo com tratamento completo de erros"""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
        return None
    except PermissionError:
        print(f"❌ Sem permissão para ler '{nome_arquivo}'!")
        return None
    except UnicodeDecodeError:
        print(f"❌ Erro de codificação no arquivo '{nome_arquivo}'!")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

def escrever_log(mensagem):
    """Escreve no arquivo de log com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha_log = f"[{timestamp}] {mensagem}\\n"
    
    try:
        with open("sistema.log", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha_log)
        print(f"📝 Log registrado: {mensagem}")
    except Exception as e:
        print(f"❌ Erro ao escrever log: {e}")

# Testando
conteudo = ler_arquivo_seguro("teste.txt")
if conteudo:
    print("Arquivo lido com sucesso!")

escrever_log("Sistema iniciado")
escrever_log("Usuário fez login")
escrever_log("Arquivo processado")

# Lendo o log
print("\\n=== CONTEÚDO DO LOG ===")
log_content = ler_arquivo_seguro("sistema.log")
if log_content:
    print(log_content)'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        # Exercícios
        self.utils.exercicio(
            "Qual é a forma mais segura de abrir arquivos em Python?",
            ["with open", "with statement", "context manager"],
            "Use 'with' para fechar automaticamente"
        )
        
        self.utils.exercicio(
            "Que modo usar para adicionar texto no final de um arquivo?",
            ["'a'", "append", "modo append"],
            "Modo 'a' adiciona no final sem apagar"
        )
        
        # Mini Projeto do Módulo 15
        self._mini_projeto_modulo_15()

    def modulo_16_excecoes(self) -> None:
        """Módulo 16: Tratamento de Erros e Exceções"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 16: TRATAMENTO DE ERROS - CÓDIGO ROBUSTO")
        
        print("🛡️ Erros acontecem! Vamos aprender a lidar com eles profissionalmente!")
        print("💪 Código robusto = código que não quebra facilmente!")
        
        print("\n═══════════════════════════════════════════════")
        print("        TIPOS COMUNS DE ERROS")
        print("═══════════════════════════════════════════════")
        
        print("\n🚨 Principais exceções em Python:")
        print("• SyntaxError - Erro de sintaxe")
        print("• NameError - Variável não definida") 
        print("• TypeError - Tipo incorreto")
        print("• ValueError - Valor incorreto")
        print("• IndexError - Índice fora do range")
        print("• KeyError - Chave não existe no dict")
        print("• FileNotFoundError - Arquivo não encontrado")
        print("• ZeroDivisionError - Divisão por zero")
        
        self.utils.pausar()
        
        # Try/except básico
        codigo1 = '''# Tratamento básico de exceções
print("=== DIVISÃO SEGURA ===")

def dividir_seguro(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("❌ Erro: Não é possível dividir por zero!")
        return None
    except TypeError:
        print("❌ Erro: Os valores devem ser números!")
        return None

# Testando
print("10 ÷ 2 =", dividir_seguro(10, 2))
print("10 ÷ 0 =", dividir_seguro(10, 0))
print("10 ÷ 'a' =", dividir_seguro(10, "a"))

print("\\n=== ACESSO SEGURO A LISTAS ===")
def acessar_lista_seguro(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"❌ Índice {indice} não existe na lista!")
        return None
    except TypeError:
        print("❌ Índice deve ser um número!")
        return None

frutas = ["maçã", "banana", "laranja"]
print("Índice 1:", acessar_lista_seguro(frutas, 1))
print("Índice 10:", acessar_lista_seguro(frutas, 10))
print("Índice 'a':", acessar_lista_seguro(frutas, "a"))'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔧 Try/Except/Else/Finally:")
        
        codigo2 = '''# Estrutura completa de tratamento
def processar_arquivo(nome_arquivo):
    arquivo = None
    try:
        print(f"🔄 Tentando abrir {nome_arquivo}...")
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        print("✅ Arquivo aberto com sucesso!")
        
        # Processamento dos dados
        linhas = arquivo.readlines()
        print(f"📊 Arquivo tem {len(linhas)} linhas")
        
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
        # Vamos criar um arquivo de exemplo
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("Linha 1\\nLinha 2\\nLinha 3\\n")
        print(f"✅ Arquivo '{nome_arquivo}' criado para demonstração!")
        return processar_arquivo(nome_arquivo)  # Tenta novamente
        
    except PermissionError:
        print(f"❌ Sem permissão para acessar '{nome_arquivo}'!")
        
    else:
        print("🎉 Processamento concluído sem erros!")
        return linhas
        
    finally:
        print("🧹 Limpeza final...")
        if arquivo and not arquivo.closed:
            arquivo.close()
            print("📄 Arquivo fechado.")

# Testando
resultado = processar_arquivo("exemplo.txt")
if resultado:
    print("Primeira linha:", resultado[0].strip())'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🎯 Criando Exceções Personalizadas:")
        
        codigo3 = '''# Exceções personalizadas
class IdadeInvalidaError(Exception):
    """Exceção para idade inválida"""
    def __init__(self, idade, mensagem="Idade inválida"):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente"""
    def __init__(self, saldo_atual, valor_tentativa):
        self.saldo_atual = saldo_atual
        self.valor_tentativa = valor_tentativa
        mensagem = f"Saldo insuficiente! Saldo: R${saldo_atual}, Tentativa: R${valor_tentativa}"
        super().__init__(mensagem)

def validar_idade(idade):
    """Valida se a idade está em um range válido"""
    if not isinstance(idade, int):
        raise TypeError("Idade deve ser um número inteiro")
    if idade < 0:
        raise IdadeInvalidaError(idade, "Idade não pode ser negativa")
    if idade > 150:
        raise IdadeInvalidaError(idade, "Idade muito alta (máximo 150)")
    return True

def sacar_dinheiro(saldo, valor):
    """Simula saque bancário"""
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    return saldo - valor

# Testando exceções personalizadas
print("=== VALIDAÇÃO DE IDADE ===")
idades_teste = [25, -5, 200, "abc", 30]

for idade in idades_teste:
    try:
        validar_idade(idade)
        print(f"✅ Idade {idade} é válida")
    except (IdadeInvalidaError, TypeError) as e:
        print(f"❌ {e}")

print("\\n=== SISTEMA BANCÁRIO ===")
saldo_conta = 1000

saques_teste = [200, 500, 1500, 300]
for valor in saques_teste:
    try:
        novo_saldo = sacar_dinheiro(saldo_conta, valor)
        saldo_conta = novo_saldo
        print(f"✅ Saque de R${valor} realizado. Saldo: R${saldo_conta}")
    except SaldoInsuficienteError as e:
        print(f"❌ {e}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n🔍 Debugging e Logging de Erros:")
        
        codigo4 = '''# Sistema completo de logging de erros
import logging
import traceback
from datetime import datetime

# Configurando logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('erros.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def calculadora_robusta(operacao, a, b):
    """Calculadora com logging completo"""
    try:
        logging.info(f"Iniciando operação: {a} {operacao} {b}")
        
        if operacao == "+":
            resultado = a + b
        elif operacao == "-":
            resultado = a - b
        elif operacao == "*":
            resultado = a * b
        elif operacao == "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero não permitida")
            resultado = a / b
        else:
            raise ValueError(f"Operação '{operacao}' não reconhecida")
        
        logging.info(f"Resultado: {resultado}")
        return resultado
        
    except Exception as e:
        # Log detalhado do erro
        logging.error(f"ERRO na operação {a} {operacao} {b}")
        logging.error(f"Tipo do erro: {type(e).__name__}")
        logging.error(f"Mensagem: {str(e)}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        
        # Retorna erro amigável para o usuário
        return f"Erro: {str(e)}"

# Testando calculadora
operacoes_teste = [
    ("+", 10, 5),
    ("-", 10, 3),
    ("*", 4, 7),
    ("/", 10, 2),
    ("/", 10, 0),  # Vai gerar erro
    ("^", 2, 3),   # Operação inválida
]

print("=== CALCULADORA ROBUSTA ===")
for op, num1, num2 in operacoes_teste:
    resultado = calculadora_robusta(op, num1, num2)
    print(f"{num1} {op} {num2} = {resultado}")

print("\\n📋 Verifique o arquivo 'erros.log' para ver os detalhes!")'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        # Exercícios
        self.utils.exercicio(
            "Qual bloco é executado SEMPRE, mesmo se não houver erro?",
            ["finally", "bloco finally", "finally block"],
            "Finally sempre executa"
        )
        
        self.utils.exercicio(
            "Como criar uma exceção personalizada?",
            ["class MinhaError(Exception)", "herdar de Exception"],
            "Herde da classe Exception"
        )
        
        # Mini Projeto do Módulo 16
        self._mini_projeto_modulo_16()

    def modulo_18_oop_basico(self) -> None:
        """Módulo 18: Programação Orientada a Objetos - Básico"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS - POO BÁSICO")
        
        print("🏗️ Bem-vindo ao mundo da Programação Orientada a Objetos!")
        print("🎯 POO = organizar código como no mundo real: OBJETOS com propriedades e ações!")
        
        print("\n═══════════════════════════════════════════════")
        print("        CONCEITOS FUNDAMENTAIS")
        print("═══════════════════════════════════════════════")
        
        print("\n🧱 CLASSE = molde/blueprint para criar objetos")
        print("🎭 OBJETO = instância concreta de uma classe")
        print("📦 ATRIBUTOS = características/propriedades do objeto")
        print("⚙️ MÉTODOS = ações/comportamentos que o objeto pode fazer")
        
        self.utils.pausar()
        
        # Primeira classe
        codigo1 = '''# Criando nossa primeira classe
class Pessoa:
    """Classe que representa uma pessoa"""
    
    def __init__(self, nome, idade):
        """Construtor - executado quando objeto é criado"""
        self.nome = nome      # Atributo
        self.idade = idade    # Atributo
        print(f"✨ Pessoa {nome} foi criada!")
    
    def apresentar(self):
        """Método para pessoa se apresentar"""
        print(f"Olá! Eu sou {self.nome} e tenho {self.idade} anos.")
    
    def fazer_aniversario(self):
        """Método para fazer aniversário"""
        self.idade += 1
        print(f"🎉 {self.nome} fez aniversário! Agora tem {self.idade} anos.")
    
    def eh_maior_idade(self):
        """Método que verifica se é maior de idade"""
        return self.idade >= 18

# Criando objetos (instanciando a classe)
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("João", 17)

print("\\n=== USANDO OS OBJETOS ===")
pessoa1.apresentar()
pessoa2.apresentar()

print(f"\\n{pessoa1.nome} é maior de idade? {pessoa1.eh_maior_idade()}")
print(f"{pessoa2.nome} é maior de idade? {pessoa2.eh_maior_idade()}")

print("\\n=== FAZENDO ANIVERSÁRIO ===")
pessoa2.fazer_aniversario()
print(f"Agora {pessoa2.nome} é maior de idade? {pessoa2.eh_maior_idade()}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🏦 Exemplo Prático - Conta Bancária:")
        
        codigo2 = '''# Classe mais complexa - Conta Bancária
class ContaBancaria:
    """Representa uma conta bancária"""
    
    # Atributo de classe (compartilhado por todas as instâncias)
    banco = "Banco Python"
    total_contas = 0
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []
        
        # Incrementa contador de contas
        ContaBancaria.total_contas += 1
        self.numero = ContaBancaria.total_contas
        
        self._adicionar_historico(f"Conta criada com saldo inicial: R${saldo_inicial}")
        print(f"🏦 Conta #{self.numero} criada para {titular}")
    
    def depositar(self, valor):
        """Deposita dinheiro na conta"""
        if valor > 0:
            self.saldo += valor
            self._adicionar_historico(f"Depósito: +R${valor}")
            print(f"✅ Depósito de R${valor} realizado!")
        else:
            print("❌ Valor de depósito deve ser positivo!")
    
    def sacar(self, valor):
        """Saca dinheiro da conta"""
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self._adicionar_historico(f"Saque: -R${valor}")
                print(f"✅ Saque de R${valor} realizado!")
            else:
                print(f"❌ Saldo insuficiente! Saldo atual: R${self.saldo}")
        else:
            print("❌ Valor de saque deve ser positivo!")
    
    def transferir(self, destino, valor):
        """Transfere dinheiro para outra conta"""
        if valor > 0 and valor <= self.saldo:
            self.sacar(valor)
            destino.depositar(valor)
            print(f"💸 Transferência de R${valor} realizada para {destino.titular}")
        else:
            print("❌ Transferência não realizada!")
    
    def _adicionar_historico(self, operacao):
        """Método privado para adicionar ao histórico"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historico.append(f"[{timestamp}] {operacao}")
    
    def extrato(self):
        """Mostra extrato da conta"""
        print(f"\\n{'='*40}")
        print(f"EXTRATO - {self.banco}")
        print(f"Conta: #{self.numero} - Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo}")
        print(f"{'='*40}")
        print("Histórico:")
        for operacao in self.historico[-5:]:  # Últimas 5 operações
            print(f"  {operacao}")
        print(f"{'='*40}")

# Testando o sistema bancário
conta_ana = ContaBancaria("Ana Silva", 1000)
conta_joao = ContaBancaria("João Santos", 500)

print(f"\\nTotal de contas criadas: {ContaBancaria.total_contas}")

# Operações
conta_ana.depositar(200)
conta_ana.sacar(150)
conta_ana.transferir(conta_joao, 300)

# Extratos
conta_ana.extrato()
conta_joao.extrato()'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🎮 Exemplo - Sistema de Jogos:")
        
        codigo3 = '''# Sistema de personagens de jogo
class Personagem:
    """Classe base para personagens de RPG"""
    
    def __init__(self, nome, vida=100, ataque=10):
        self.nome = nome
        self.vida_maxima = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.nivel = 1
        self.experiencia = 0
        print(f"⚔️ {nome} entrou no jogo!")
    
    def atacar(self, inimigo):
        """Ataca outro personagem"""
        dano = self.ataque
        print(f"⚔️ {self.nome} ataca {inimigo.nome}!")
        inimigo.receber_dano(dano)
    
    def receber_dano(self, dano):
        """Recebe dano de um ataque"""
        self.vida_atual -= dano
        print(f"💔 {self.nome} recebeu {dano} de dano!")
        
        if self.vida_atual <= 0:
            self.vida_atual = 0
            print(f"💀 {self.nome} foi derrotado!")
        else:
            print(f"❤️ {self.nome} tem {self.vida_atual}/{self.vida_maxima} de vida")
    
    def curar(self, quantidade=20):
        """Cura o personagem"""
        vida_antes = self.vida_atual
        self.vida_atual = min(self.vida_atual + quantidade, self.vida_maxima)
        curado = self.vida_atual - vida_antes
        print(f"💚 {self.nome} se curou em {curado} pontos!")
    
    def ganhar_experiencia(self, exp):
        """Ganha experiência e pode subir de nível"""
        self.experiencia += exp
        print(f"✨ {self.nome} ganhou {exp} XP!")
        
        # Verificar se subiu de nível
        exp_necessaria = self.nivel * 100
        if self.experiencia >= exp_necessaria:
            self.nivel += 1
            self.vida_maxima += 20
            self.vida_atual = self.vida_maxima
            self.ataque += 5
            self.experiencia = 0
            print(f"🌟 {self.nome} subiu para o nível {self.nivel}!")
    
    def status(self):
        """Mostra status do personagem"""
        print(f"\\n📊 STATUS DE {self.nome.upper()}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida_atual}/{self.vida_maxima}")
        print(f"Ataque: {self.ataque}")
        print(f"Experiência: {self.experiencia}")
        
        # Barra de vida visual
        vida_percent = (self.vida_atual / self.vida_maxima) * 20
        barra_vida = "█" * int(vida_percent) + "░" * (20 - int(vida_percent))
        print(f"HP: [{barra_vida}]")

# Criando personagens
heroi = Personagem("Aragorn", vida=120, ataque=15)
inimigo = Personagem("Orc", vida=80, ataque=12)

print("\\n=== BATALHA ===")
heroi.status()
inimigo.status()

# Simulando batalha
heroi.atacar(inimigo)
inimigo.atacar(heroi)
heroi.atacar(inimigo)
heroi.curar()
heroi.ganhar_experiencia(150)

print("\\n=== APÓS BATALHA ===")
heroi.status()'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "Qual método é executado automaticamente quando um objeto é criado?",
            ["__init__", "construtor", "init"],
            "O método especial __init__"
        )
        
        self.utils.exercicio(
            "O que representa 'self' nos métodos de uma classe?",
            ["o próprio objeto", "instância atual", "objeto"],
            "Refere-se à instância atual da classe"
        )
        
        # Mini Projeto do Módulo 18
        self._mini_projeto_modulo_18()

    def modulo_17_modulos(self) -> None:
        """Módulo 17: Módulos e Bibliotecas"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 17: MÓDULOS E BIBLIOTECAS - REUTILIZANDO CÓDIGO")
        
        print("📦 Agora vamos aprender a ORGANIZAR e REUTILIZAR código!")
        print("🔧 Módulos são a base da programação profissional!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO MÓDULOS?")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Módulo = arquivo .py com funções e classes")
        print("📚 Biblioteca = conjunto de módulos")
        print("🌟 Vantagens:")
        print("• ♻️  Reutilização de código")
        print("• 🗂️  Organização melhor")
        print("• 👥 Colaboração em equipe")
        print("• 🐛 Menos bugs")
        
        self.utils.pausar()
        
        print("\n🔍 Importando Módulos:")
        
        codigo1 = '''# Diferentes formas de importar
import math
import random
import datetime

print("=== USANDO MÓDULO MATH ===")
print(f"Pi: {math.pi}")
print(f"Raiz quadrada de 16: {math.sqrt(16)}")
print(f"Seno de 90°: {math.sin(math.radians(90))}")
print(f"Logaritmo de 100: {math.log10(100)}")

print("\\n=== USANDO MÓDULO RANDOM ===")
print(f"Número aleatório 1-10: {random.randint(1, 10)}")
print(f"Número float aleatório: {random.random()}")

cores = ["vermelho", "azul", "verde", "amarelo"]
print(f"Cor aleatória: {random.choice(cores)}")

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista embaralhada: {numeros}")

print("\\n=== USANDO MÓDULO DATETIME ===")
agora = datetime.datetime.now()
print(f"Data e hora atual: {agora}")
print(f"Só a data: {agora.date()}")
print(f"Só a hora: {agora.time()}")
print(f"Formatado: {agora.strftime('%d/%m/%Y %H:%M')}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n⚡ Importação Específica:")
        
        codigo2 = '''# Importando funções específicas
from math import pi, sqrt, sin, cos
from random import randint, choice
from datetime import datetime, date

print("=== IMPORT ESPECÍFICO ===")
print(f"Pi sem 'math.': {pi}")
print(f"Raiz sem 'math.': {sqrt(25)}")
print(f"Número aleatório: {randint(1, 100)}")

# Alias (apelidos) para módulos
print("\\n=== ALIASES COMUNS ===")
print("matplotlib.pyplot as plt - Gráficos")
print("pandas as pd - Análise de dados") 
print("numpy as np - Computação científica")

# From com alias
from datetime import datetime as dt
agora = dt.now()
print(f"\\nUsando alias: {agora}")

# Importando tudo (cuidado!)
from math import *
print(f"\\nTudo importado - pi: {pi}, e: {e}")
print("⚠️ Cuidado: pode sobrescrever variáveis!")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🔨 Criando Seus Próprios Módulos:")
        
        codigo3 = '''# Vamos criar funções que poderiam estar em um módulo separado
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return imc, categoria

def converter_temperatura(temp, de, para):
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin"""
    # Primeiro converte tudo para Celsius
    if de == "F":
        celsius = (temp - 32) * 5/9
    elif de == "K":
        celsius = temp - 273.15
    else:
        celsius = temp
    
    # Depois converte para o destino
    if para == "F":
        return celsius * 9/5 + 32
    elif para == "K":
        return celsius + 273.15
    else:
        return celsius

def gerar_senha(tamanho=8):
    """Gera uma senha aleatória"""
    import random
    import string
    
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Constantes do módulo
PI = 3.14159
VERSAO = "1.0"

print("=== TESTANDO NOSSAS FUNÇÕES ===")
imc, categoria = calcular_imc(70, 1.75)
print(f"IMC: {imc:.1f} - {categoria}")

temp_f = converter_temperatura(25, "C", "F")
print(f"25°C = {temp_f:.1f}°F")

senha = gerar_senha(12)
print(f"Senha gerada: {senha}")

print(f"\\nVersão: {VERSAO}")
print(f"Valor de PI: {PI}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n📚 Bibliotecas Úteis para Aprender:")
        
        codigo4 = '''# Principais bibliotecas Python
print("=== BIBLIOTECAS ESSENCIAIS ===")

libraries = {
    "Básicas (já instaladas)": [
        "os - Interação com sistema operacional",
        "sys - Configurações do sistema Python", 
        "json - Trabalhar com dados JSON",
        "re - Expressões regulares",
        "urllib - Requisições web básicas"
    ],
    "Análise de Dados": [
        "pandas - Manipulação de dados",
        "numpy - Computação numérica",
        "matplotlib - Gráficos e visualização",
        "seaborn - Gráficos estatísticos bonitos"
    ],
    "Web": [
        "requests - Requisições HTTP fáceis",
        "flask - Framework web simples",
        "django - Framework web completo",
        "beautifulsoup4 - Parsing de HTML"
    ],
    "Interface Gráfica": [
        "tkinter - Interface básica (já instalado)",
        "PyQt5/PySide2 - Interface profissional",
        "kivy - Apps mobile"
    ]
}

for categoria, libs in libraries.items():
    print(f"\\n🔹 {categoria}:")
    for lib in libs:
        print(f"  • {lib}")

print("\\n💡 DICA: Use 'pip install nome_biblioteca' para instalar!")
print("📖 Exemplo: pip install requests pandas matplotlib")'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        # Exercícios
        self.utils.exercicio(
            "Como importar apenas a função sqrt do módulo math?",
            ["from math import sqrt"],
            "Use 'from modulo import funcao'"
        )
        
        self.utils.exercicio(
            "Para que serve o comando 'pip install'?",
            ["instalar bibliotecas", "instalar pacotes", "instalar módulos"],
            "Instala bibliotecas externas no Python"
        )
        
        # Mini Projeto do Módulo 17
        self._mini_projeto_modulo_17()

    def modulo_19_oop_avancado(self) -> None:
        """Módulo 19: OOP Avançado - Herança e Polimorfismo"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 19: OOP AVANÇADO - HERANÇA E POLIMORFISMO")
        
        print("🧬 Agora vamos aprender os conceitos AVANÇADOS de OOP!")
        print("👑 Herança e Polimorfismo são o coração da programação orientada a objetos!")
        
        print("\n═══════════════════════════════════════════════")
        print("        HERANÇA - REUTILIZANDO CLASSES")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Herança = uma classe 'filha' herda de uma classe 'pai'")
        print("📚 Vantagens:")
        print("• ♻️  Reutilização de código")
        print("• 🏗️  Hierarquia organizada")
        print("• 🔧 Especialização de comportamentos")
        
        self.utils.pausar()
        
        codigo1 = '''# Exemplo de Herança - Sistema de Veículos
class Veiculo:
    """Classe pai - características gerais"""
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento=10):
        """Método que será herdado"""
        self.velocidade += incremento
        print(f"🚗 {self.marca} {self.modelo} acelerou para {self.velocidade} km/h")
    
    def frear(self, decremento=10):
        """Método que será herdado"""
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"🚗 {self.marca} {self.modelo} freou para {self.velocidade} km/h")
    
    def info(self):
        """Informações gerais"""
        print(f"Veículo: {self.marca} {self.modelo} ({self.ano})")

# Classe filha - herda de Veiculo
class Carro(Veiculo):
    """Especialização de Veiculo"""
    
    def __init__(self, marca, modelo, ano, portas):
        # Chama o construtor da classe pai
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def buzinar(self):
        """Método específico de Carro"""
        print("🔊 Beep beep!")
    
    def info(self):
        """Sobrescreve o método da classe pai"""
        super().info()  # Chama o método pai
        print(f"Portas: {self.portas}")

# Outra classe filha
class Moto(Veiculo):
    """Outra especialização de Veiculo"""
    
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def empinar(self):
        """Método específico de Moto"""
        print("🏍️ Empinando! Vroooom!")
    
    def acelerar(self, incremento=15):
        """Sobrescreve - motos aceleram mais"""
        super().acelerar(incremento)
        print("💨 Moto é mais rápida!")

print("=== TESTANDO HERANÇA ===")
carro = Carro("Toyota", "Corolla", 2023, 4)
moto = Moto("Honda", "CB600", 2023, 600)

print("\\nInformações:")
carro.info()
print()
moto.info()

print("\\n=== MÉTODOS HERDADOS ===")
carro.acelerar()
moto.acelerar()

print("\\n=== MÉTODOS ESPECÍFICOS ===")
carro.buzinar()
moto.empinar()'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🎭 POLIMORFISMO - Múltiplas Formas:")
        
        codigo2 = '''# Polimorfismo - mesma interface, comportamentos diferentes
class Animal:
    """Classe base para animais"""
    
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        """Método que será sobrescrito"""
        pass
    
    def mover(self):
        """Método que será sobrescrito"""
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
    
    def mover(self):
        return "correndo com as patas"

class Passaro(Animal):
    def fazer_som(self):
        return "Piu piu!"
    
    def mover(self):
        return "voando com as asas"

class Peixe(Animal):
    def fazer_som(self):
        return "... (silêncio)"
    
    def mover(self):
        return "nadando com as nadadeiras"

# Lista de animais diferentes
animais = [
    Cachorro("Rex", "Labrador"),
    Passaro("Piu", "Bem-te-vi"),
    Peixe("Nemo", "Palhaço")
]

print("=== POLIMORFISMO EM AÇÃO ===")
for animal in animais:
    print(f"\\n{animal.nome} ({animal.especie}):")
    print(f"  Som: {animal.fazer_som()}")
    print(f"  Movimento: {animal.mover()}")

# Função que funciona com qualquer animal
def apresentar_animal(animal):
    """Polimorfismo - funciona com qualquer Animal"""
    print(f"Este é {animal.nome}, ele faz {animal.fazer_som()}")

print("\\n=== FUNÇÃO POLIMÓRFICA ===")
for animal in animais:
    apresentar_animal(animal)'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🏛️ Classes Abstratas:")
        
        codigo3 = '''# Classes abstratas - não podem ser instanciadas
from abc import ABC, abstractmethod

class Forma(ABC):
    """Classe abstrata - modelo para outras formas"""
    
    def __init__(self, cor):
        self.cor = cor
    
    @abstractmethod
    def calcular_area(self):
        """Método abstrato - deve ser implementado nas filhas"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Outro método abstrato"""
        pass
    
    def info(self):
        """Método concreto - pode ser usado"""
        print(f"Forma de cor {self.cor}")

class Retangulo(Forma):
    """Implementa todos os métodos abstratos"""
    
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    """Outra implementação"""
    
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio

print("=== CLASSES ABSTRATAS ===")
retangulo = Retangulo("azul", 5, 3)
circulo = Circulo("vermelho", 4)

formas = [retangulo, circulo]

for forma in formas:
    forma.info()
    print(f"  Área: {forma.calcular_area():.2f}")
    print(f"  Perímetro: {forma.calcular_perimetro():.2f}")
    print()

# Isso daria erro - não pode instanciar classe abstrata:
# forma_generica = Forma("verde")  # TypeError!'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "O que é herança em programação orientada a objetos?",
            ["classe filha herda da pai", "reutilização de código", "herança"],
            "Uma classe filha herda atributos e métodos da classe pai"
        )
        
        # Mini Projeto do Módulo 19
        self._mini_projeto_modulo_19()

    def modulo_20_decorators(self) -> None:
        """Módulo 20: Decorators e Context Managers"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 20: DECORATORS E CONTEXT MANAGERS")
        
        print("🎭 Decorators são uma das funcionalidades mais PODEROSAS do Python!")
        print("🔧 Context managers garantem limpeza automática de recursos!")
        
        print("\n═══════════════════════════════════════════════")
        print("        DECORATORS - MODIFICANDO FUNÇÕES")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Decorator = função que modifica outra função")
        print("✨ Usado para:")
        print("• ⏱️  Medir tempo de execução")
        print("• 🔐 Autenticação e autorização")
        print("• 📝 Logs automáticos")
        print("• 🧪 Validação de entrada")
        
        self.utils.pausar()
        
        codigo1 = '''# Decorators básicos
import time
import functools

def cronometro(func):
    """Decorator que mede tempo de execução"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱️ {func.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

def log_chamadas(func):
    """Decorator que registra chamadas de função"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"📝 Chamando {func.__name__} com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"📝 {func.__name__} retornou: {resultado}")
        return resultado
    return wrapper

# Usando decorators
@cronometro
@log_chamadas
def calcular_fibonacci(n):
    """Calcula número de Fibonacci"""
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

@cronometro
def operacao_lenta():
    """Simula operação que demora"""
    time.sleep(1)
    return "Operação concluída!"

print("=== TESTANDO DECORATORS ===")
print("Fibonacci de 8:")
resultado = calcular_fibonacci(8)
print(f"Resultado: {resultado}\\n")

print("Operação lenta:")
resultado2 = operacao_lenta()
print(f"Resultado: {resultado2}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔧 Decorators com Parâmetros:")
        
        codigo2 = '''# Decorators parametrizados
def validar_tipos(*tipos):
    """Decorator que valida tipos dos argumentos"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Valida argumentos posicionais
            for i, (arg, tipo_esperado) in enumerate(zip(args, tipos)):
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(f"Argumento {i+1} deve ser {tipo_esperado.__name__}, recebido {type(arg).__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_resultados(max_size=100):
    """Decorator que cacheia resultados"""
    def decorator(func):
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Cria chave única para os argumentos
            chave = str(args) + str(kwargs)
            
            if chave in cache:
                print(f"💾 Cache hit para {func.__name__}")
                return cache[chave]
            
            print(f"🔄 Calculando {func.__name__}")
            resultado = func(*args, **kwargs)
            
            # Limita tamanho do cache
            if len(cache) >= max_size:
                cache.clear()
            
            cache[chave] = resultado
            return resultado
        return wrapper
    return decorator

# Usando decorators parametrizados
@validar_tipos(int, int)
@cache_resultados(max_size=5)
def somar(a, b):
    """Soma dois números"""
    time.sleep(0.1)  # Simula cálculo lento
    return a + b

@validar_tipos(str, int)
def repetir_string(texto, vezes):
    """Repete uma string"""
    return texto * vezes

print("=== DECORATORS PARAMETRIZADOS ===")

# Testando validação e cache
print("Primeira chamada:")
resultado1 = somar(5, 3)
print(f"5 + 3 = {resultado1}")

print("\\nSegunda chamada (mesmo valores - usa cache):")
resultado2 = somar(5, 3)
print(f"5 + 3 = {resultado2}")

print("\\nTerceira chamada (valores diferentes):")
resultado3 = somar(10, 20)
print(f"10 + 20 = {resultado3}")

print("\\nTestando validação de tipos:")
try:
    somar("5", 3)  # Vai dar erro!
except TypeError as e:
    print(f"❌ Erro capturado: {e}")

print("\\nFunção repetir_string:")
resultado4 = repetir_string("Python! ", 3)
print(f"Resultado: {resultado4}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🏠 Context Managers:")
        
        codigo3 = '''# Context Managers - with statement
import os
from contextlib import contextmanager

class GerenciadorArquivo:
    """Context manager customizado para arquivos"""
    
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self.arquivo = None
    
    def __enter__(self):
        """Chamado quando entra no bloco with"""
        print(f"📂 Abrindo arquivo {self.nome_arquivo}")
        self.arquivo = open(self.nome_arquivo, self.modo, encoding='utf-8')
        return self.arquivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Chamado quando sai do bloco with (mesmo com erro!)"""
        if self.arquivo:
            print(f"📁 Fechando arquivo {self.nome_arquivo}")
            self.arquivo.close()
        
        if exc_type:
            print(f"❌ Erro capturado: {exc_val}")
        
        return False  # Não suprime exceções

# Context manager usando decorator
@contextmanager
def cronometro_contexto():
    """Context manager que mede tempo"""
    print("⏱️ Iniciando cronômetro...")
    inicio = time.time()
    try:
        yield
    finally:
        fim = time.time()
        print(f"⏱️ Tempo decorrido: {fim - inicio:.4f} segundos")

print("=== CONTEXT MANAGERS ===")

# Usando context manager customizado
print("1. Context manager customizado:")
with GerenciadorArquivo("teste_context.txt", "w") as arquivo:
    arquivo.write("Olá do context manager!\\n")
    arquivo.write("Este arquivo será fechado automaticamente.")

# Verificando se arquivo foi fechado
print("\\n2. Cronômetro context manager:")
with cronometro_contexto():
    time.sleep(0.5)
    print("Fazendo alguma operação...")

print("\\n3. Context manager múltiplo:")
with cronometro_contexto():
    with open("teste_context.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo lido: {conteudo}")

# Context manager para recursos temporários
@contextmanager
def diretorio_temporario():
    """Cria e remove diretório temporário"""
    nome_dir = "temp_dir"
    print(f"📁 Criando diretório temporário: {nome_dir}")
    os.makedirs(nome_dir, exist_ok=True)
    
    try:
        yield nome_dir
    finally:
        print(f"🗑️ Removendo diretório temporário: {nome_dir}")
        if os.path.exists(nome_dir):
            os.rmdir(nome_dir)

print("\\n4. Diretório temporário:")
with diretorio_temporario() as temp_dir:
    print(f"Usando diretório: {temp_dir}")
    print(f"Diretório existe? {os.path.exists(temp_dir)}")
print(f"Diretório ainda existe? {os.path.exists('temp_dir')}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "Para que serve a função @functools.wraps em decorators?",
            ["preserva metadados", "wraps", "metadados"],
            "Preserva nome, docstring e outros metadados da função original"
        )
        
        # Mini Projeto do Módulo 20
        self._mini_projeto_modulo_20()

    def modulo_21_geradores(self) -> None:
        """Módulo 21: Generators e Iterators"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 21: GENERATORS E ITERATORS - EFICIÊNCIA MÁXIMA")
        
        print("⚡ Generators são uma das funcionalidades mais EFICIENTES do Python!")
        print("🔄 Iterators permitem percorrer sequências de forma elegante!")
        
        print("\n═══════════════════════════════════════════════")
        print("        ITERATORS - PERCORRENDO SEQUÊNCIAS")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Iterator = objeto que implementa __iter__ e __next__")
        print("🔄 Protocolo de iteração:")
        print("• __iter__(): retorna o próprio iterator")
        print("• __next__(): retorna próximo item ou StopIteration")
        
        self.utils.pausar()
        
        codigo1 = '''# Criando um Iterator customizado
class ContadorIterator:
    """Iterator que conta até um limite"""
    
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0
    
    def __iter__(self):
        """Retorna o próprio iterator"""
        return self
    
    def __next__(self):
        """Retorna próximo item"""
        if self.atual < self.limite:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration

class NumerosPares:
    """Iterator para números pares"""
    
    def __init__(self, maximo):
        self.maximo = maximo
        self.numero = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.numero < self.maximo:
            self.numero += 2
            if self.numero <= self.maximo:
                return self.numero
        raise StopIteration

print("=== ITERATORS CUSTOMIZADOS ===")

# Testando contador
print("Contador até 5:")
contador = ContadorIterator(5)
for numero in contador:
    print(numero, end=" ")

print("\\n\\nNúmeros pares até 10:")
pares = NumerosPares(10)
for par in pares:
    print(par, end=" ")

# Usando next() manualmente
print("\\n\\nUsando next() manualmente:")
contador2 = ContadorIterator(3)
print(f"Primeiro: {next(contador2)}")
print(f"Segundo: {next(contador2)}")
print(f"Terceiro: {next(contador2)}")

try:
    print(f"Quarto: {next(contador2)}")  # Vai dar StopIteration
except StopIteration:
    print("Fim do iterator!")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🌟 GENERATORS - Iterators Simplificados:")
        
        codigo2 = '''# Generators - muito mais simples que iterators!
def contador_generator(limite):
    """Generator function que conta até limite"""
    atual = 0
    while atual < limite:
        atual += 1
        yield atual  # yield torna isso um generator!

def fibonacci_generator(n):
    """Generator que produz números de Fibonacci"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def numeros_pares_generator(maximo):
    """Generator para números pares"""
    numero = 2
    while numero <= maximo:
        yield numero
        numero += 2

print("=== GENERATORS EM AÇÃO ===")

# Usando generators
print("Contador generator até 5:")
for num in contador_generator(5):
    print(num, end=" ")

print("\\n\\nFibonacci generator (10 números):")
for fib in fibonacci_generator(10):
    print(fib, end=" ")

print("\\n\\nPares até 20:")
for par in numeros_pares_generator(20):
    print(par, end=" ")

# Generator expressions - ainda mais conciso!
print("\\n\\n=== GENERATOR EXPRESSIONS ===")
quadrados = (x**2 for x in range(1, 6))
print("Quadrados:", list(quadrados))

# Exemplo prático - processando arquivo grande
def ler_linhas_grandes(nome_arquivo):
    """Generator para ler arquivo linha por linha (eficiente)"""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                yield linha.strip()
    except FileNotFoundError:
        yield "Arquivo não encontrado"

# Criando arquivo de teste
with open("teste_grande.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"Esta é a linha {i}\\n")

print("\\nLendo arquivo com generator:")
for linha in ler_linhas_grandes("teste_grande.txt"):
    print(f"  {linha}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n⚡ Vantagens dos Generators:")
        
        codigo3 = '''# Comparando memória: Lista vs Generator
import sys

def criar_lista_grande(n):
    """Cria lista com n números"""
    return [x**2 for x in range(n)]

def criar_generator_grande(n):
    """Cria generator com n números"""
    return (x**2 for x in range(n))

# Comparando uso de memória
n = 1000
lista = criar_lista_grande(n)
generator = criar_generator_grande(n)

print("=== COMPARAÇÃO DE MEMÓRIA ===")
print(f"Lista com {n} elementos: {sys.getsizeof(lista)} bytes")
print(f"Generator equivalente: {sys.getsizeof(generator)} bytes")

# Generators são preguiçosos (lazy evaluation)
def generator_infinito():
    """Generator que teoricamente nunca acaba"""
    num = 1
    while True:
        yield num
        num += 1

print("\\n=== LAZY EVALUATION ===")
infinito = generator_infinito()
print("Primeiros 10 números do generator infinito:")
for i, numero in enumerate(infinito):
    if i >= 10:
        break
    print(numero, end=" ")

# Generator com send() - comunicação bidirecional
def generator_comunicativo():
    """Generator que pode receber valores"""
    print("Generator iniciado!")
    while True:
        valor_recebido = yield "Aguardando..."
        if valor_recebido is not None:
            print(f"Recebi: {valor_recebido}")
            yield f"Processado: {valor_recebido.upper()}"

print("\\n\\n=== GENERATOR COM SEND ===")
comm = generator_comunicativo()
print(next(comm))  # Inicia o generator

resposta = comm.send("python")
print(f"Resposta: {resposta}")

print(next(comm))  # Continua o loop

# Pipeline de generators - muito poderoso!
def numeros(maximo):
    """Produz números de 1 até maximo"""
    for i in range(1, maximo + 1):
        yield i

def pares_apenas(numeros_gen):
    """Filtra apenas números pares"""
    for num in numeros_gen:
        if num % 2 == 0:
            yield num

def elevar_ao_quadrado(numeros_gen):
    """Eleva números ao quadrado"""
    for num in numeros_gen:
        yield num ** 2

print("\\n=== PIPELINE DE GENERATORS ===")
# Criando pipeline: números -> pares -> quadrados
pipeline = elevar_ao_quadrado(pares_apenas(numeros(10)))
resultado = list(pipeline)
print(f"Números de 1-10 -> pares -> quadrados: {resultado}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "Qual palavra-chave transforma uma função em generator?",
            ["yield"],
            "A palavra-chave 'yield' torna uma função um generator"
        )
        
        # Mini Projeto do Módulo 21
        self._mini_projeto_modulo_21()

    def modulo_22_regex(self) -> None:
        """Módulo 22: Expressões Regulares"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 22: EXPRESSÕES REGULARES - BUSCA AVANÇADA EM TEXTO")
        
        print("🔍 Regex é uma ferramenta PODEROSA para buscar padrões em texto!")
        print("⚡ Essencial para validação, extração e manipulação de dados!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO EXPRESSÕES REGULARES?")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Regex = padrão para encontrar texto específico")
        print("🔧 Usado para:")
        print("• ✅ Validar emails, telefones, CPFs")
        print("• 🔍 Buscar padrões em arquivos")
        print("• 🔄 Substituir texto complexo")
        print("• 📊 Extrair dados estruturados")
        
        self.utils.pausar()
        
        codigo1 = '''# Básico de expressões regulares
import re

texto = """
João Silva - joao@email.com - (11) 99999-1234
Maria Santos - maria.santos@empresa.com.br - (21) 88888-5678
Pedro Oliveira - pedro123@hotmail.com - (31) 77777-9012
Ana Costa - ana_costa@gmail.com - (41) 66666-3456
"""

print("=== BUSCA SIMPLES ===")
# Busca simples
emails = re.findall(r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', texto)
print("Emails encontrados:")
for email in emails:
    print(f"  • {email}")

telefones = re.findall(r'\\(\\d{2}\\) \\d{5}-\\d{4}', texto)
print("\\nTelefones encontrados:")
for telefone in telefones:
    print(f"  • {telefone}")

nomes = re.findall(r'^([A-Z][a-z]+ [A-Z][a-z]+)', texto, re.MULTILINE)
print("\\nNomes encontrados:")
for nome in nomes:
    print(f"  • {nome}")

print("\\n=== VERIFICAÇÃO COM MATCH ===")
# Verificando se string inteira corresponde ao padrão
email_teste = "usuario@dominio.com"
if re.match(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$', email_teste):
    print(f"✅ '{email_teste}' é um email válido")
else:
    print(f"❌ '{email_teste}' não é um email válido")

# Testando email inválido
email_invalido = "email.inválido"
if re.match(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$', email_invalido):
    print(f"✅ '{email_invalido}' é um email válido")
else:
    print(f"❌ '{email_invalido}' não é um email válido")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔧 Padrões e Metacaracteres:")
        
        codigo2 = '''# Metacaracteres e padrões importantes
test_strings = [
    "Python123",
    "python",
    "PYTHON",
    "Python-3.9",
    "123",
    "abc@def.com",
    "(11) 99999-1234",
    "12/03/2023",
    "2023-12-03",
    "CPF: 123.456.789-01"
]

print("=== METACARACTERES ===")
patterns = {
    r'\\d+': 'Números (um ou mais dígitos)',
    r'\\w+': 'Palavras (letras, números, _)',
    r'\\s+': 'Espaços em branco',
    r'^[A-Z]': 'Começa com letra maiúscula',
    r'\\d{3}': 'Exatamente 3 dígitos',
    r'[a-z]+@[a-z]+\\.[a-z]+': 'Email simples',
    r'\\(\\d{2}\\) \\d{5}-\\d{4}': 'Telefone brasileiro',
    r'\\d{2}/\\d{2}/\\d{4}': 'Data formato DD/MM/AAAA',
    r'\\d{4}-\\d{2}-\\d{2}': 'Data formato AAAA-MM-DD'
}

for string in test_strings:
    print(f"\\nTestando: '{string}'")
    for pattern, descricao in patterns.items():
        if re.search(pattern, string):
            print(f"  ✅ {descricao}")

print("\\n=== GRUPOS E CAPTURA ===")
# Grupos permitem extrair partes específicas
data_texto = "Nascimento: 15/08/1990, Casamento: 23/12/2015"
datas = re.findall(r'(\\d{2})/(\\d{2})/(\\d{4})', data_texto)
print("Datas encontradas (dia, mês, ano):")
for dia, mes, ano in datas:
    print(f"  Dia: {dia}, Mês: {mes}, Ano: {ano}")

# Grupos nomeados - ainda melhor!
cpf_texto = "Meus CPFs: 123.456.789-01 e 987.654.321-09"
cpfs = re.finditer(r'(?P<num1>\\d{3})\\.(?P<num2>\\d{3})\\.(?P<num3>\\d{3})-(?P<dig>\\d{2})', cpf_texto)
print("\\nCPFs encontrados:")
for match in cpfs:
    print(f"  {match.group('num1')}.{match.group('num2')}.{match.group('num3')}-{match.group('dig')}")
    print(f"    Números: {match.group('num1')} {match.group('num2')} {match.group('num3')}")
    print(f"    Dígitos: {match.group('dig')}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🛠️ Aplicações Práticas:")
        
        codigo3 = '''# Funções de validação usando regex
def validar_email(email):
    """Valida email com regex mais robusta"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validar_telefone_br(telefone):
    """Valida telefone brasileiro"""
    # Remove espaços e caracteres especiais
    telefone_limpo = re.sub(r'[^\\d]', '', telefone)
    
    # Verifica se tem 10 ou 11 dígitos
    if len(telefone_limpo) in [10, 11]:
        # Verifica formato (xx) xxxxx-xxxx ou (xx) xxxx-xxxx
        pattern = r'^\\(?\\d{2}\\)?\\s*\\d{4,5}-?\\d{4}$'
        return bool(re.match(pattern, telefone))
    return False

def validar_cpf(cpf):
    """Valida formato de CPF"""
    pattern = r'^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$'
    return bool(re.match(pattern, cpf))

def extrair_urls(texto):
    """Extrai URLs de um texto"""
    pattern = r'https?://[a-zA-Z0-9.-]+(?:/[^\\s]*)?'
    return re.findall(pattern, texto)

def limpar_html(html):
    """Remove tags HTML de um texto"""
    pattern = r'<[^>]+>'
    return re.sub(pattern, '', html)

def formatar_telefone(telefone):
    """Formata telefone para padrão brasileiro"""
    # Remove tudo que não é dígito
    digitos = re.sub(r'\\D', '', telefone)
    
    if len(digitos) == 11:
        # Formato: (xx) xxxxx-xxxx
        return re.sub(r'(\\d{2})(\\d{5})(\\d{4})', r'(\\1) \\2-\\3', digitos)
    elif len(digitos) == 10:
        # Formato: (xx) xxxx-xxxx
        return re.sub(r'(\\d{2})(\\d{4})(\\d{4})', r'(\\1) \\2-\\3', digitos)
    else:
        return telefone

print("=== VALIDAÇÕES PRÁTICAS ===")

# Testando validações
emails_teste = ["joao@email.com", "maria.silva@empresa.com.br", "email_inválido", "user@", "@domain.com"]
print("Validação de emails:")
for email in emails_teste:
    resultado = "✅ Válido" if validar_email(email) else "❌ Inválido"
    print(f"  {email} - {resultado}")

telefones_teste = ["(11) 99999-1234", "11999991234", "(21) 8888-5678", "123", "11 99999-1234"]
print("\\nValidação de telefones:")
for tel in telefones_teste:
    resultado = "✅ Válido" if validar_telefone_br(tel) else "❌ Inválido"
    print(f"  {tel} - {resultado}")

print("\\n=== FORMATAÇÃO ===")
telefones_desformatados = ["11999991234", "2188885678", "31777779012"]
print("Formatação de telefones:")
for tel in telefones_desformatados:
    formatado = formatar_telefone(tel)
    print(f"  {tel} -> {formatado}")

print("\\n=== EXTRAÇÃO DE DADOS ===")
texto_urls = "Visite https://python.org ou http://github.com para mais informações"
urls = extrair_urls(texto_urls)
print(f"URLs encontradas: {urls}")

html = "<h1>Título</h1><p>Este é um <b>parágrafo</b> com HTML.</p>"
texto_limpo = limpar_html(html)
print(f"\\nHTML: {html}")
print(f"Limpo: {texto_limpo}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "Qual metacaractere representa 'um ou mais dígitos'?",
            ["\\d+", "d+"],
            "\\d+ representa um ou mais dígitos"
        )
        
        # Mini Projeto do Módulo 22
        self._mini_projeto_modulo_22()

    def modulo_23_debugging(self) -> None:
        """Módulo 23: Debugging e Profiling"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 23: DEBUGGING E PROFILING - ENCONTRANDO E CORRIGINDO PROBLEMAS")
        
        print("🐛 Debugging é a arte de encontrar e corrigir bugs!")
        print("⚡ Profiling ajuda a otimizar performance do código!")
        
        print("\n═══════════════════════════════════════════════")
        print("        TÉCNICAS DE DEBUGGING")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Ferramentas de debugging:")
        print("• 📝 Print statements")
        print("• 🔍 Debugger (pdb)")
        print("• 📊 Logging")
        print("• 🧪 Assertions")
        print("• ⚡ Profilers")
        
        self.utils.pausar()
        
        codigo1 = '''# Técnicas básicas de debugging
import logging
import traceback
import sys

# Configurando logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def calcular_media_com_debug(numeros):
    """Função com várias técnicas de debugging"""
    logger.debug(f"Função chamada com parâmetros: {numeros}")
    
    # Assertion para validar entrada
    assert isinstance(numeros, list), "Parâmetro deve ser uma lista"
    assert len(numeros) > 0, "Lista não pode estar vazia"
    
    # Print debugging (removível facilmente)
    print(f"🔍 DEBUG: Processando {len(numeros)} números")
    
    try:
        # Validação com logging
        for i, num in enumerate(numeros):
            if not isinstance(num, (int, float)):
                logger.warning(f"Valor na posição {i} não é numérico: {num}")
                raise ValueError(f"Todos os valores devem ser números")
            
            logger.debug(f"Processando número {i}: {num}")
        
        # Cálculo da média
        soma = sum(numeros)
        media = soma / len(numeros)
        
        logger.info(f"Média calculada: {media}")
        print(f"✅ Resultado: {media}")
        
        return media
        
    except Exception as e:
        logger.error(f"Erro no cálculo: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise

# Função problemática para demonstrar debugging
def funcao_com_bug(x, y):
    """Função com bug intencional"""
    logger.debug(f"Dividindo {x} por {y}")
    
    # Bug: não verifica divisão por zero
    resultado = x / y  # Pode dar ZeroDivisionError!
    
    return resultado

print("=== DEMONSTRAÇÃO DE DEBUGGING ===")

# Testando função sem bugs
print("1. Função funcionando:")
try:
    media = calcular_media_com_debug([10, 20, 30, 40])
except Exception as e:
    print(f"Erro capturado: {e}")

# Testando com dados inválidos
print("\\n2. Testando com dados inválidos:")
try:
    media = calcular_media_com_debug([10, "20", 30])
except Exception as e:
    print(f"Erro capturado: {e}")

# Testando função com bug
print("\\n3. Função com bug:")
try:
    resultado = funcao_com_bug(10, 0)
except ZeroDivisionError as e:
    print(f"Bug encontrado: {e}")
    logger.error(f"Divisão por zero detectada!")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔍 Debugger Interativo (pdb):")
        
        codigo2 = '''# Usando o debugger pdb
import pdb

def bubble_sort_com_debug(lista):
    """Bubble sort com pontos de debug"""
    lista = lista.copy()  # Não modificar original
    n = len(lista)
    
    print(f"Iniciando ordenação de {n} elementos: {lista}")
    
    for i in range(n):
        # Inserir breakpoint aqui permite inspecionar variáveis
        # pdb.set_trace()  # Descomente para ativar debugger
        
        print(f"\\nIteração {i + 1}:")
        trocas = 0
        
        for j in range(0, n - i - 1):
            print(f"  Comparando {lista[j]} e {lista[j + 1]}")
            
            if lista[j] > lista[j + 1]:
                # Trocar elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                print(f"    Trocou! Nova lista: {lista}")
            else:
                print(f"    Sem troca")
        
        print(f"  Total de trocas na iteração: {trocas}")
        
        # Se não houve trocas, lista está ordenada
        if trocas == 0:
            print("  Lista já está ordenada!")
            break
    
    return lista

def demonstrar_pdb():
    """Demonstra comandos básicos do pdb"""
    print("=== COMANDOS BÁSICOS DO PDB ===")
    print("Quando estiver no debugger, use:")
    print("  • n (next): próxima linha")
    print("  • s (step): entrar em função")
    print("  • c (continue): continuar execução") 
    print("  • l (list): mostrar código")
    print("  • p <var>: imprimir variável")
    print("  • pp <var>: pretty print")
    print("  • w (where): mostrar stack")
    print("  • u (up): subir no stack")
    print("  • d (down): descer no stack")
    print("  • q (quit): sair do debugger")
    print()
    print("Para usar: descomente a linha 'pdb.set_trace()' no código")

print("=== BUBBLE SORT COM DEBUG ===")
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros}")

resultado = bubble_sort_com_debug(numeros)
print(f"\\nLista ordenada: {resultado}")

demonstrar_pdb()'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n⚡ Profiling - Medindo Performance:")
        
        codigo3 = '''# Profiling para otimização
import time
import cProfile
import timeit
from functools import wraps

def cronometrar(func):
    """Decorator para medir tempo de execução"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱️ {func.__name__} executou em {fim - inicio:.6f} segundos")
        return resultado
    return wrapper

# Três implementações diferentes de soma
@cronometrar
def soma_loop(n):
    """Soma usando loop"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

@cronometrar
def soma_compreensao(n):
    """Soma usando list comprehension"""
    return sum([i for i in range(1, n + 1)])

@cronometrar
def soma_formula(n):
    """Soma usando fórmula matemática"""
    return n * (n + 1) // 2

@cronometrar
def fibonacci_lento(n):
    """Fibonacci recursivo (ineficiente)"""
    if n <= 1:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)

@cronometrar
def fibonacci_rapido(n):
    """Fibonacci iterativo (eficiente)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def profile_memoria():
    """Demonstra como diferentes estruturas afetam memória"""
    import sys
    
    # Lista vs Generator
    lista_grande = [x**2 for x in range(1000)]
    generator_grande = (x**2 for x in range(1000))
    
    print("=== COMPARAÇÃO DE MEMÓRIA ===")
    print(f"Lista com 1000 elementos: {sys.getsizeof(lista_grande)} bytes")
    print(f"Generator equivalente: {sys.getsizeof(generator_grande)} bytes")
    
    # String concatenação vs join
    strings = [f"item_{i}" for i in range(1000)]
    
    # Método ineficiente
    start = time.time()
    resultado_concat = ""
    for s in strings:
        resultado_concat += s + ", "
    tempo_concat = time.time() - start
    
    # Método eficiente
    start = time.time()
    resultado_join = ", ".join(strings)
    tempo_join = time.time() - start
    
    print(f"\\nConcatenação com +: {tempo_concat:.6f} segundos")
    print(f"Join: {tempo_join:.6f} segundos")
    print(f"Join é {tempo_concat/tempo_join:.2f}x mais rápido!")

print("=== COMPARAÇÃO DE PERFORMANCE ===")

n = 10000
print(f"Calculando soma de 1 até {n}:")

# Testando diferentes implementações
resultado1 = soma_loop(n)
resultado2 = soma_compreensao(n)
resultado3 = soma_formula(n)

print(f"Todos os resultados são iguais: {resultado1 == resultado2 == resultado3}")

print("\\n=== FIBONACCI COMPARISON ===")
print("Fibonacci de 30:")

# Cuidado: fibonacci_lento pode demorar muito!
print("Fibonacci eficiente:")
resultado_rapido = fibonacci_rapido(30)

print("\\n=== USANDO TIMEIT PARA PRECISÃO ===")
# timeit é mais preciso para micro-benchmarks
tempo_formula = timeit.timeit(lambda: soma_formula(1000), number=1000)
tempo_loop = timeit.timeit(lambda: soma_loop(1000), number=1000)

print(f"Fórmula matemática (1000 execuções): {tempo_formula:.6f} segundos")
print(f"Loop simples (1000 execuções): {tempo_loop:.6f} segundos")

# Profile detalhado (comentado para não poluir output)
print("\\n=== PROFILE DETALHADO ===")
print("Para profile completo, use: cProfile.run('sua_funcao()')")

profile_memoria()'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exercícios
        self.utils.exercicio(
            "Qual comando do pdb mostra o valor de uma variável?",
            ["p", "print", "p variavel"],
            "Use 'p nome_da_variavel' no debugger pdb"
        )
        
        # Mini Projeto do Módulo 23
        self._mini_projeto_modulo_23()

    def projeto_intermediario(self) -> None:
        """Módulo 24: PROJETO - Sistema de Biblioteca"""
        self.utils.limpar_tela()
        self.utils.titulo("PROJETO INTERMEDIÁRIO: SISTEMA DE BIBLIOTECA")
        
        print("📚 Vamos criar um sistema COMPLETO de gerenciamento de biblioteca!")
        print("🏗️ Projeto que combina todos os conceitos aprendidos!")
        
        print("\n═══════════════════════════════════════════════")
        print("        ESPECIFICAÇÕES DO PROJETO")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Funcionalidades:")
        print("• 📖 Cadastro de livros")
        print("• 👥 Cadastro de usuários")
        print("• 🔄 Empréstimos e devoluções")
        print("• 🔍 Busca e relatórios")
        print("• 💾 Persistência em arquivo")
        print("• 🎨 Interface amigável")
        
        self.utils.pausar()
        
        codigo1 = '''# Sistema de Biblioteca - Versão Completa
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import re

class Livro:
    """Classe que representa um livro"""
    
    def __init__(self, id_livro: str, titulo: str, autor: str, ano: int, isbn: str = ""):
        self.id = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        self.disponivel = True
        self.data_cadastro = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Converte livro para dicionário"""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "isbn": self.isbn,
            "disponivel": self.disponivel,
            "data_cadastro": self.data_cadastro
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Cria livro a partir de dicionário"""
        livro = cls(data["id"], data["titulo"], data["autor"], data["ano"], data.get("isbn", ""))
        livro.disponivel = data.get("disponivel", True)
        livro.data_cadastro = data.get("data_cadastro", datetime.now().strftime("%Y-%m-%d"))
        return livro
    
    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.titulo} - {self.autor} ({self.ano}) - {status}"

class Usuario:
    """Classe que representa um usuário"""
    
    def __init__(self, id_usuario: str, nome: str, email: str, telefone: str = ""):
        self.id = id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.livros_emprestados: List[str] = []
        self.data_cadastro = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Converte usuário para dicionário"""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "livros_emprestados": self.livros_emprestados,
            "data_cadastro": self.data_cadastro
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Cria usuário a partir de dicionário"""
        usuario = cls(data["id"], data["nome"], data["email"], data.get("telefone", ""))
        usuario.livros_emprestados = data.get("livros_emprestados", [])
        usuario.data_cadastro = data.get("data_cadastro", datetime.now().strftime("%Y-%m-%d"))
        return usuario
    
    def __str__(self) -> str:
        emprestimos = len(self.livros_emprestados)
        return f"[{self.id}] {self.nome} - {self.email} ({emprestimos} empréstimos)"

class Emprestimo:
    """Classe que representa um empréstimo"""
    
    def __init__(self, id_usuario: str, id_livro: str, dias_prazo: int = 14):
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=dias_prazo)
        self.data_devolucao_real: Optional[datetime] = None
        self.ativo = True
    
    def to_dict(self) -> Dict:
        """Converte empréstimo para dicionário"""
        return {
            "id_usuario": self.id_usuario,
            "id_livro": self.id_livro,
            "data_emprestimo": self.data_emprestimo.isoformat(),
            "data_devolucao_prevista": self.data_devolucao_prevista.isoformat(),
            "data_devolucao_real": self.data_devolucao_real.isoformat() if self.data_devolucao_real else None,
            "ativo": self.ativo
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Cria empréstimo a partir de dicionário"""
        emprestimo = cls.__new__(cls)
        emprestimo.id_usuario = data["id_usuario"]
        emprestimo.id_livro = data["id_livro"]
        emprestimo.data_emprestimo = datetime.fromisoformat(data["data_emprestimo"])
        emprestimo.data_devolucao_prevista = datetime.fromisoformat(data["data_devolucao_prevista"])
        emprestimo.data_devolucao_real = datetime.fromisoformat(data["data_devolucao_real"]) if data["data_devolucao_real"] else None
        emprestimo.ativo = data.get("ativo", True)
        return emprestimo
    
    def esta_atrasado(self) -> bool:
        """Verifica se empréstimo está atrasado"""
        if not self.ativo:
            return False
        return datetime.now() > self.data_devolucao_prevista
    
    def dias_atraso(self) -> int:
        """Calcula dias de atraso"""
        if not self.esta_atrasado():
            return 0
        return (datetime.now() - self.data_devolucao_prevista).days

print("=== CLASSES DO SISTEMA ===")
print("✅ Livro - Representa um livro da biblioteca")
print("✅ Usuario - Representa um usuário cadastrado")
print("✅ Emprestimo - Representa um empréstimo de livro")

# Criando objetos de exemplo
livro1 = Livro("L001", "Python Cookbook", "David Beazley", 2013, "978-1449340377")
usuario1 = Usuario("U001", "João Silva", "joao@email.com", "(11) 99999-1234")
emprestimo1 = Emprestimo("U001", "L001")

print("\\n=== OBJETOS CRIADOS ===")
print(f"Livro: {livro1}")
print(f"Usuário: {usuario1}")
print(f"Empréstimo ativo: {emprestimo1.ativo}")
print(f"Data prevista: {emprestimo1.data_devolucao_prevista.strftime('%d/%m/%Y')}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n📚 Sistema Principal:")
        
        codigo2 = '''# Classe principal do sistema
class SistemaBiblioteca:
    """Sistema completo de gerenciamento de biblioteca"""
    
    def __init__(self, arquivo_dados: str = "biblioteca.json"):
        self.arquivo_dados = arquivo_dados
        self.livros: Dict[str, Livro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.emprestimos: List[Emprestimo] = []
        self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega dados do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                # Carregar livros
                for livro_data in dados.get("livros", []):
                    livro = Livro.from_dict(livro_data)
                    self.livros[livro.id] = livro
                
                # Carregar usuários
                for usuario_data in dados.get("usuarios", []):
                    usuario = Usuario.from_dict(usuario_data)
                    self.usuarios[usuario.id] = usuario
                
                # Carregar empréstimos
                for emp_data in dados.get("emprestimos", []):
                    emprestimo = Emprestimo.from_dict(emp_data)
                    self.emprestimos.append(emprestimo)
                
                print(f"✅ Dados carregados: {len(self.livros)} livros, {len(self.usuarios)} usuários")
            
            except Exception as e:
                print(f"⚠️ Erro ao carregar dados: {e}")
        else:
            print("📁 Arquivo de dados não existe. Iniciando sistema vazio.")
    
    def salvar_dados(self):
        """Salva dados no arquivo JSON"""
        try:
            dados = {
                "livros": [livro.to_dict() for livro in self.livros.values()],
                "usuarios": [usuario.to_dict() for usuario in self.usuarios.values()],
                "emprestimos": [emp.to_dict() for emp in self.emprestimos]
            }
            
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            
            print("💾 Dados salvos com sucesso!")
        
        except Exception as e:
            print(f"❌ Erro ao salvar dados: {e}")
    
    def gerar_id_livro(self) -> str:
        """Gera ID único para livro"""
        numero = len(self.livros) + 1
        while f"L{numero:03d}" in self.livros:
            numero += 1
        return f"L{numero:03d}"
    
    def gerar_id_usuario(self) -> str:
        """Gera ID único para usuário"""
        numero = len(self.usuarios) + 1
        while f"U{numero:03d}" in self.usuarios:
            numero += 1
        return f"U{numero:03d}"
    
    def cadastrar_livro(self, titulo: str, autor: str, ano: int, isbn: str = "") -> str:
        """Cadastra novo livro"""
        id_livro = self.gerar_id_livro()
        livro = Livro(id_livro, titulo, autor, ano, isbn)
        self.livros[id_livro] = livro
        self.salvar_dados()
        return id_livro
    
    def cadastrar_usuario(self, nome: str, email: str, telefone: str = "") -> str:
        """Cadastra novo usuário"""
        # Validar email
        if not re.match(r'^[^@]+@[^@]+\\.[^@]+$', email):
            raise ValueError("Email inválido")
        
        id_usuario = self.gerar_id_usuario()
        usuario = Usuario(id_usuario, nome, email, telefone)
        self.usuarios[id_usuario] = usuario
        self.salvar_dados()
        return id_usuario
    
    def buscar_livros(self, termo: str) -> List[Livro]:
        """Busca livros por título ou autor"""
        termo = termo.lower()
        resultados = []
        
        for livro in self.livros.values():
            if (termo in livro.titulo.lower() or 
                termo in livro.autor.lower() or 
                termo in livro.id.lower()):
                resultados.append(livro)
        
        return resultados
    
    def emprestar_livro(self, id_usuario: str, id_livro: str) -> bool:
        """Realiza empréstimo de livro"""
        # Verificações
        if id_usuario not in self.usuarios:
            print(f"❌ Usuário {id_usuario} não encontrado")
            return False
        
        if id_livro not in self.livros:
            print(f"❌ Livro {id_livro} não encontrado")
            return False
        
        livro = self.livros[id_livro]
        if not livro.disponivel:
            print(f"❌ Livro '{livro.titulo}' não está disponível")
            return False
        
        usuario = self.usuarios[id_usuario]
        if len(usuario.livros_emprestados) >= 3:
            print(f"❌ Usuário {usuario.nome} já tem 3 livros emprestados")
            return False
        
        # Realizar empréstimo
        emprestimo = Emprestimo(id_usuario, id_livro)
        self.emprestimos.append(emprestimo)
        
        livro.disponivel = False
        usuario.livros_emprestados.append(id_livro)
        
        self.salvar_dados()
        print(f"✅ Empréstimo realizado: {livro.titulo} para {usuario.nome}")
        return True

print("=== SISTEMA PRINCIPAL ===")
# Criando instância do sistema
biblioteca = SistemaBiblioteca("teste_biblioteca.json")

# Cadastrando livros
print("\\nCadastrando livros:")
id1 = biblioteca.cadastrar_livro("Python para Iniciantes", "João Santos", 2023)
id2 = biblioteca.cadastrar_livro("Algoritmos em Python", "Maria Silva", 2022)
id3 = biblioteca.cadastrar_livro("Web com Django", "Pedro Costa", 2023)

print(f"Livros cadastrados: {id1}, {id2}, {id3}")

# Cadastrando usuários
print("\\nCadastrando usuários:")
u1 = biblioteca.cadastrar_usuario("Ana Lima", "ana@email.com", "(11) 88888-1111")
u2 = biblioteca.cadastrar_usuario("Carlos Souza", "carlos@email.com")

print(f"Usuários cadastrados: {u1}, {u2}")

# Realizando empréstimos
print("\\nRealizando empréstimos:")
biblioteca.emprestar_livro(u1, id1)
biblioteca.emprestar_livro(u2, id2)

# Buscando livros
print("\\nBuscando livros com 'Python':")
resultados = biblioteca.buscar_livros("Python")
for livro in resultados:
    print(f"  📖 {livro}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n📊 Relatórios e Interface:")
        
        codigo3 = '''# Relatórios e interface do usuário
class RelatoriosBiblioteca:
    """Classe para gerar relatórios"""
    
    def __init__(self, sistema: SistemaBiblioteca):
        self.sistema = sistema
    
    def livros_disponiveis(self) -> List[Livro]:
        """Lista livros disponíveis"""
        return [livro for livro in self.sistema.livros.values() if livro.disponivel]
    
    def livros_emprestados(self) -> List[Livro]:
        """Lista livros emprestados"""
        return [livro for livro in self.sistema.livros.values() if not livro.disponivel]
    
    def emprestimos_atrasados(self) -> List[Emprestimo]:
        """Lista empréstimos atrasados"""
        return [emp for emp in self.sistema.emprestimos if emp.esta_atrasado()]
    
    def relatorio_geral(self):
        """Exibe relatório geral da biblioteca"""
        print("=" * 50)
        print("           RELATÓRIO GERAL DA BIBLIOTECA")
        print("=" * 50)
        
        total_livros = len(self.sistema.livros)
        disponiveis = len(self.livros_disponiveis())
        emprestados = len(self.livros_emprestados())
        total_usuarios = len(self.sistema.usuarios)
        atrasados = len(self.emprestimos_atrasados())
        
        print(f"📚 Total de livros: {total_livros}")
        print(f"✅ Disponíveis: {disponiveis}")
        print(f"📖 Emprestados: {emprestados}")
        print(f"👥 Total de usuários: {total_usuarios}")
        print(f"⚠️ Empréstimos atrasados: {atrasados}")
        
        if atrasados > 0:
            print("\\n⚠️ EMPRÉSTIMOS ATRASADOS:")
            for emp in self.emprestimos_atrasados():
                usuario = self.sistema.usuarios[emp.id_usuario]
                livro = self.sistema.livros[emp.id_livro]
                dias = emp.dias_atraso()
                print(f"  • {usuario.nome} - {livro.titulo} ({dias} dias de atraso)")
        
        print("=" * 50)

class InterfaceBiblioteca:
    """Interface de linha de comando para o sistema"""
    
    def __init__(self):
        self.sistema = SistemaBiblioteca()
        self.relatorios = RelatoriosBiblioteca(self.sistema)
    
    def menu_principal(self):
        """Exibe menu principal"""
        while True:
            print("\\n" + "=" * 40)
            print("      SISTEMA DE BIBLIOTECA")
            print("=" * 40)
            print("1. 📚 Cadastrar livro")
            print("2. 👤 Cadastrar usuário")
            print("3. 🔄 Emprestar livro")
            print("4. 📥 Devolver livro")
            print("5. 🔍 Buscar livros")
            print("6. 📊 Relatórios")
            print("7. 📋 Listar tudo")
            print("0. 🚪 Sair")
            print("=" * 40)
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "0":
                    print("👋 Obrigado por usar o sistema!")
                    break
                elif opcao == "1":
                    self.cadastrar_livro_interface()
                elif opcao == "2":
                    self.cadastrar_usuario_interface()
                elif opcao == "3":
                    self.emprestar_livro_interface()
                elif opcao == "6":
                    self.relatorios.relatorio_geral()
                elif opcao == "7":
                    self.listar_tudo()
                else:
                    print("❌ Opção inválida!")
            
            except KeyboardInterrupt:
                print("\\n\\n👋 Sistema encerrado pelo usuário")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
    
    def cadastrar_livro_interface(self):
        """Interface para cadastrar livro"""
        print("\\n📚 CADASTRO DE LIVRO")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        
        try:
            ano = int(input("Ano: ").strip())
            isbn = input("ISBN (opcional): ").strip()
            
            id_livro = self.sistema.cadastrar_livro(titulo, autor, ano, isbn)
            print(f"✅ Livro cadastrado com ID: {id_livro}")
        
        except ValueError:
            print("❌ Ano deve ser um número!")
    
    def cadastrar_usuario_interface(self):
        """Interface para cadastrar usuário"""
        print("\\n👤 CADASTRO DE USUÁRIO")
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        telefone = input("Telefone (opcional): ").strip()
        
        try:
            id_usuario = self.sistema.cadastrar_usuario(nome, email, telefone)
            print(f"✅ Usuário cadastrado com ID: {id_usuario}")
        
        except ValueError as e:
            print(f"❌ {e}")
    
    def emprestar_livro_interface(self):
        """Interface para emprestar livro"""
        print("\\n🔄 EMPRÉSTIMO DE LIVRO")
        id_usuario = input("ID do usuário: ").strip().upper()
        id_livro = input("ID do livro: ").strip().upper()
        
        self.sistema.emprestar_livro(id_usuario, id_livro)
    
    def listar_tudo(self):
        """Lista todos os itens do sistema"""
        print("\\n📚 TODOS OS LIVROS:")
        for livro in self.sistema.livros.values():
            print(f"  {livro}")
        
        print("\\n👥 TODOS OS USUÁRIOS:")
        for usuario in self.sistema.usuarios.values():
            print(f"  {usuario}")

# Demonstração do sistema
print("=== DEMONSTRAÇÃO DO SISTEMA COMPLETO ===")

# Criando sistema com dados de exemplo
sistema_demo = SistemaBiblioteca("demo_biblioteca.json")
relatorios_demo = RelatoriosBiblioteca(sistema_demo)

# Adicionando dados se necessário
if len(sistema_demo.livros) == 0:
    print("Adicionando dados de demonstração...")
    sistema_demo.cadastrar_livro("Clean Code", "Robert Martin", 2008)
    sistema_demo.cadastrar_livro("Python Tricks", "Dan Bader", 2017)
    sistema_demo.cadastrar_livro("Automate the Boring Stuff", "Al Sweigart", 2019)
    
    sistema_demo.cadastrar_usuario("Maria Silva", "maria@teste.com")
    sistema_demo.cadastrar_usuario("João Santos", "joao@teste.com")
    
    # Fazendo alguns empréstimos
    sistema_demo.emprestar_livro("U001", "L001")
    sistema_demo.emprestar_livro("U002", "L002")

# Exibindo relatório
relatorios_demo.relatorio_geral()

print("\\n💡 Para usar a interface completa, descomente:")
print("# interface = InterfaceBiblioteca()")
print("# interface.menu_principal()")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        print("\n🎉 Projeto de Sistema de Biblioteca concluído!")
        print("✨ Você implementou um sistema completo com:")
        print("• Classes e objetos")
        print("• Persistência de dados")
        print("• Validações e tratamento de erros")
        print("• Interface de usuário")
        print("• Relatórios e buscas")
        
        self.utils.pausar()

    def projeto_avancado(self) -> None:
        """Módulo 25: PROJETO - Web Scraper"""
        self.utils.limpar_tela()
        self.utils.titulo("PROJETO AVANÇADO: WEB SCRAPER DE NOTÍCIAS")
        
        print("🌐 Vamos criar um web scraper profissional!")
        print("🤖 Coletaremos e analisaremos notícias automaticamente!")
        
        print("\n═══════════════════════════════════════════════")
        print("        ESPECIFICAÇÕES DO PROJETO")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Funcionalidades:")
        print("• 🌐 Scraping de múltiplos sites")
        print("• 📰 Extração de notícias")
        print("• 📊 Análise de sentimentos")
        print("• 💾 Armazenamento em JSON/CSV")
        print("• 📈 Estatísticas e gráficos")
        print("• ⏰ Agendamento automático")
        
        self.utils.pausar()
        
        codigo1 = '''# Web Scraper de Notícias - Estrutura Base
import requests
import json
import csv
import re
from datetime import datetime
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse
import time

class Noticia:
    """Classe que representa uma notícia"""
    
    def __init__(self, titulo: str, link: str, resumo: str = "", fonte: str = "", data: str = ""):
        self.titulo = titulo
        self.link = link
        self.resumo = resumo
        self.fonte = fonte
        self.data = data or datetime.now().strftime("%Y-%m-%d %H:%M")
        self.palavras_chave: List[str] = []
        self.sentimento: Optional[str] = None
    
    def extrair_palavras_chave(self):
        """Extrai palavras-chave do título e resumo"""
        texto = f"{self.titulo} {self.resumo}".lower()
        
        # Remove pontuação e divide em palavras
        palavras = re.findall(r'\\b\\w+\\b', texto)
        
        # Palavras comuns a ignorar
        stop_words = {
            'que', 'de', 'do', 'da', 'para', 'com', 'em', 'na', 'no', 'por',
            'uma', 'um', 'o', 'a', 'os', 'as', 'e', 'ou', 'mas', 'se', 'não',
            'como', 'mais', 'muito', 'quando', 'onde', 'sobre', 'após', 'até'
        }
        
        # Filtra palavras relevantes (mais de 3 caracteres, não stop words)
        self.palavras_chave = [
            palavra for palavra in set(palavras) 
            if len(palavra) > 3 and palavra not in stop_words
        ]
    
    def analisar_sentimento(self):
        """Análise básica de sentimento"""
        texto = f"{self.titulo} {self.resumo}".lower()
        
        palavras_positivas = [
            'sucesso', 'vitória', 'conquista', 'melhoria', 'crescimento',
            'progresso', 'benefício', 'oportunidade', 'inovação', 'êxito'
        ]
        
        palavras_negativas = [
            'crise', 'problema', 'dificuldade', 'falha', 'erro', 'prejuízo',
            'queda', 'perda', 'conflito', 'tragédia', 'acidente'
        ]
        
        positivas = sum(1 for palavra in palavras_positivas if palavra in texto)
        negativas = sum(1 for palavra in palavras_negativas if palavra in texto)
        
        if positivas > negativas:
            self.sentimento = "positivo"
        elif negativas > positivas:
            self.sentimento = "negativo"
        else:
            self.sentimento = "neutro"
    
    def to_dict(self) -> Dict:
        """Converte notícia para dicionário"""
        return {
            "titulo": self.titulo,
            "link": self.link,
            "resumo": self.resumo,
            "fonte": self.fonte,
            "data": self.data,
            "palavras_chave": self.palavras_chave,
            "sentimento": self.sentimento
        }
    
    def __str__(self) -> str:
        return f"[{self.fonte}] {self.titulo} ({self.sentimento})"

class WebScraper:
    """Classe base para web scraping"""
    
    def __init__(self, base_url: str, nome_fonte: str):
        self.base_url = base_url
        self.nome_fonte = nome_fonte
        self.session = requests.Session()
        
        # Headers para parecer um navegador real
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def fazer_requisicao(self, url: str) -> Optional[str]:
        """Faz requisição HTTP com tratamento de erros"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao acessar {url}: {e}")
            return None
    
    def extrair_noticias(self, html: str) -> List[Noticia]:
        """Método abstrato - deve ser implementado por subclasses"""
        raise NotImplementedError("Subclasse deve implementar este método")

class ScraperSimulado(WebScraper):
    """Scraper simulado para demonstração"""
    
    def __init__(self):
        super().__init__("https://exemplo.com", "Portal de Notícias")
    
    def extrair_noticias(self, html: str = "") -> List[Noticia]:
        """Simula extração de notícias"""
        noticias_exemplo = [
            {
                "titulo": "Nova tecnologia revoluciona setor de energia",
                "resumo": "Pesquisadores desenvolvem método inovador para armazenamento de energia solar com eficiência 40% maior",
                "link": "https://exemplo.com/noticia-1"
            },
            {
                "titulo": "Crise econômica afeta mercado global",
                "resumo": "Instabilidade política gera incerteza nos investimentos e queda nas bolsas mundiais",
                "link": "https://exemplo.com/noticia-2"
            },
            {
                "titulo": "Descoberta científica promete avanço na medicina",
                "resumo": "Novo tratamento para doenças raras mostra resultados promissores em testes clínicos",
                "link": "https://exemplo.com/noticia-3"
            },
            {
                "titulo": "Conflito internacional gera preocupação",
                "resumo": "Tensões diplomáticas aumentam entre países e ameaçam acordos comerciais existentes",
                "link": "https://exemplo.com/noticia-4"
            },
            {
                "titulo": "Inovação em inteligência artificial conquista prêmio",
                "resumo": "Sistema de IA desenvolvido por universidade brasileira é reconhecido internacionalmente",
                "link": "https://exemplo.com/noticia-5"
            }
        ]
        
        noticias = []
        for item in noticias_exemplo:
            noticia = Noticia(
                titulo=item["titulo"],
                link=item["link"],
                resumo=item["resumo"],
                fonte=self.nome_fonte
            )
            
            # Processa a notícia
            noticia.extrair_palavras_chave()
            noticia.analisar_sentimento()
            noticias.append(noticia)
        
        return noticias

print("=== SISTEMA DE WEB SCRAPING ===")

# Criando scraper simulado
scraper = ScraperSimulado()

# Extraindo notícias
print("Extraindo notícias...")
noticias = scraper.extrair_noticias()

print(f"\\n📰 {len(noticias)} notícias extraídas:")
for i, noticia in enumerate(noticias, 1):
    print(f"{i}. {noticia}")
    print(f"   Palavras-chave: {', '.join(noticia.palavras_chave[:5])}...")
    print()'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n📊 Análise e Processamento:")
        
        codigo2 = '''# Sistema de análise de notícias
class AnalisadorNoticias:
    """Classe para análise estatística de notícias"""
    
    def __init__(self, noticias: List[Noticia]):
        self.noticias = noticias
    
    def estatisticas_sentimento(self) -> Dict[str, int]:
        """Calcula estatísticas de sentimento"""
        contadores = {"positivo": 0, "negativo": 0, "neutro": 0}
        
        for noticia in self.noticias:
            if noticia.sentimento in contadores:
                contadores[noticia.sentimento] += 1
        
        return contadores
    
    def palavras_mais_frequentes(self, top_n: int = 10) -> List[tuple]:
        """Encontra palavras-chave mais frequentes"""
        contador_palavras = {}
        
        for noticia in self.noticias:
            for palavra in noticia.palavras_chave:
                contador_palavras[palavra] = contador_palavras.get(palavra, 0) + 1
        
        # Ordena por frequência
        return sorted(contador_palavras.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    def noticias_por_fonte(self) -> Dict[str, int]:
        """Conta notícias por fonte"""
        contador_fontes = {}
        
        for noticia in self.noticias:
            fonte = noticia.fonte
            contador_fontes[fonte] = contador_fontes.get(fonte, 0) + 1
        
        return contador_fontes
    
    def relatorio_completo(self):
        """Gera relatório completo de análise"""
        print("=" * 60)
        print("                RELATÓRIO DE ANÁLISE DE NOTÍCIAS")
        print("=" * 60)
        
        # Estatísticas gerais
        total = len(self.noticias)
        print(f"📊 Total de notícias analisadas: {total}")
        
        # Análise de sentimento
        sentimentos = self.estatisticas_sentimento()
        print(f"\\n😊 Sentimento das notícias:")
        for sentimento, quantidade in sentimentos.items():
            percentual = (quantidade / total) * 100 if total > 0 else 0
            print(f"   {sentimento.capitalize()}: {quantidade} ({percentual:.1f}%)")
        
        # Palavras mais frequentes
        palavras_freq = self.palavras_mais_frequentes()
        print(f"\\n🔤 Top 10 palavras-chave:")
        for i, (palavra, freq) in enumerate(palavras_freq, 1):
            print(f"   {i:2d}. {palavra} ({freq}x)")
        
        # Notícias por fonte
        fontes = self.noticias_por_fonte()
        print(f"\\n📰 Notícias por fonte:")
        for fonte, quantidade in fontes.items():
            print(f"   {fonte}: {quantidade}")
        
        print("=" * 60)

class GerenciadorNoticias:
    """Classe para gerenciar coleta e armazenamento"""
    
    def __init__(self, arquivo_json: str = "noticias.json", arquivo_csv: str = "noticias.csv"):
        self.arquivo_json = arquivo_json
        self.arquivo_csv = arquivo_csv
        self.noticias: List[Noticia] = []
        self.carregar_noticias()
    
    def carregar_noticias(self):
        """Carrega notícias do arquivo JSON"""
        try:
            with open(self.arquivo_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
            for item in dados:
                noticia = Noticia(
                    titulo=item["titulo"],
                    link=item["link"],
                    resumo=item.get("resumo", ""),
                    fonte=item.get("fonte", ""),
                    data=item.get("data", "")
                )
                noticia.palavras_chave = item.get("palavras_chave", [])
                noticia.sentimento = item.get("sentimento")
                self.noticias.append(noticia)
            
            print(f"✅ {len(self.noticias)} notícias carregadas")
        
        except FileNotFoundError:
            print("📁 Arquivo não encontrado. Iniciando com lista vazia.")
        except Exception as e:
            print(f"❌ Erro ao carregar notícias: {e}")
    
    def salvar_noticias(self):
        """Salva notícias em JSON e CSV"""
        # Salvar em JSON
        try:
            dados = [noticia.to_dict() for noticia in self.noticias]
            with open(self.arquivo_json, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            print(f"💾 Notícias salvas em {self.arquivo_json}")
        except Exception as e:
            print(f"❌ Erro ao salvar JSON: {e}")
        
        # Salvar em CSV
        try:
            with open(self.arquivo_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Título', 'Link', 'Resumo', 'Fonte', 'Data', 'Sentimento'])
                
                for noticia in self.noticias:
                    writer.writerow([
                        noticia.titulo,
                        noticia.link,
                        noticia.resumo,
                        noticia.fonte,
                        noticia.data,
                        noticia.sentimento
                    ])
            
            print(f"📊 Notícias salvas em {self.arquivo_csv}")
        except Exception as e:
            print(f"❌ Erro ao salvar CSV: {e}")
    
    def adicionar_noticias(self, novas_noticias: List[Noticia]):
        """Adiciona novas notícias, evitando duplicatas"""
        links_existentes = {noticia.link for noticia in self.noticias}
        
        noticias_novas = [
            noticia for noticia in novas_noticias 
            if noticia.link not in links_existentes
        ]
        
        self.noticias.extend(noticias_novas)
        print(f"➕ {len(noticias_novas)} notícias adicionadas (sem duplicatas)")
        
        return len(noticias_novas)
    
    def buscar_noticias(self, termo: str) -> List[Noticia]:
        """Busca notícias por termo"""
        termo = termo.lower()
        resultados = []
        
        for noticia in self.noticias:
            if (termo in noticia.titulo.lower() or 
                termo in noticia.resumo.lower() or
                termo in noticia.palavras_chave):
                resultados.append(noticia)
        
        return resultados

# Demonstração do sistema completo
print("=== DEMONSTRAÇÃO DO SISTEMA DE ANÁLISE ===")

# Criando gerenciador e adicionando notícias do scraper
gerenciador = GerenciadorNoticias("demo_noticias.json", "demo_noticias.csv")

# Se não há notícias, adiciona as do scraper
if len(gerenciador.noticias) == 0:
    scraper = ScraperSimulado()
    noticias_novas = scraper.extrair_noticias()
    gerenciador.adicionar_noticias(noticias_novas)
    gerenciador.salvar_noticias()

# Criando analisador
analisador = AnalisadorNoticias(gerenciador.noticias)

# Gerando relatório
analisador.relatorio_completo()

# Demonstração de busca
print("\\n🔍 BUSCA POR 'tecnologia':")
resultados = gerenciador.buscar_noticias("tecnologia")
for noticia in resultados:
    print(f"  • {noticia.titulo}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n⚡ Sistema Completo com Agendamento:")
        
        codigo3 = '''# Sistema completo com agendamento e monitoramento
import threading
import schedule
import signal
import sys
from datetime import datetime, timedelta

class MonitorNoticias:
    """Sistema de monitoramento automático de notícias"""
    
    def __init__(self):
        self.gerenciador = GerenciadorNoticias()
        self.scrapers = [ScraperSimulado()]  # Lista de scrapers
        self.executando = False
        self.thread_monitoramento = None
        self.estatisticas = {
            "total_execucoes": 0,
            "noticias_coletadas": 0,
            "ultima_execucao": None,
            "erros": 0
        }
    
    def coletar_noticias(self):
        """Coleta notícias de todos os scrapers"""
        print(f"\\n🤖 [{datetime.now().strftime('%H:%M:%S')}] Iniciando coleta de notícias...")
        
        try:
            total_novas = 0
            
            for scraper in self.scrapers:
                print(f"   📡 Coletando de {scraper.nome_fonte}...")
                noticias = scraper.extrair_noticias()
                
                if noticias:
                    novas = self.gerenciador.adicionar_noticias(noticias)
                    total_novas += novas
                    time.sleep(1)  # Pausa entre requests
            
            # Salva dados
            if total_novas > 0:
                self.gerenciador.salvar_noticias()
            
            # Atualiza estatísticas
            self.estatisticas["total_execucoes"] += 1
            self.estatisticas["noticias_coletadas"] += total_novas
            self.estatisticas["ultima_execucao"] = datetime.now().strftime("%H:%M:%S")
            
            print(f"   ✅ Coleta concluída: {total_novas} notícias novas")
            
        except Exception as e:
            print(f"   ❌ Erro na coleta: {e}")
            self.estatisticas["erros"] += 1
    
    def gerar_relatorio_agendado(self):
        """Gera relatório automático"""
        print(f"\\n📊 [{datetime.now().strftime('%H:%M:%S')}] Gerando relatório automático...")
        
        if self.gerenciador.noticias:
            analisador = AnalisadorNoticias(self.gerenciador.noticias)
            
            # Relatório simplificado
            sentimentos = analisador.estatisticas_sentimento()
            total = len(self.gerenciador.noticias)
            
            print(f"   📰 Total de notícias: {total}")
            print(f"   😊 Positivas: {sentimentos.get('positivo', 0)}")
            print(f"   😐 Neutras: {sentimentos.get('neutro', 0)}")
            print(f"   😞 Negativas: {sentimentos.get('negativo', 0)}")
        else:
            print("   📭 Nenhuma notícia para analisar")
    
    def configurar_agendamentos(self):
        """Configura agendamentos automáticos"""
        # Coleta a cada 30 minutos (em produção seria menos frequente)
        schedule.every(30).minutes.do(self.coletar_noticias)
        
        # Relatório a cada 2 horas
        schedule.every(2).hours.do(self.gerar_relatorio_agendado)
        
        # Limpeza diária (remove notícias antigas)
        schedule.every().day.at("02:00").do(self.limpeza_diaria)
        
        print("⏰ Agendamentos configurados:")
        print("   • Coleta: a cada 30 minutos")
        print("   • Relatório: a cada 2 horas")
        print("   • Limpeza: diariamente às 02:00")
    
    def limpeza_diaria(self):
        """Remove notícias antigas"""
        print(f"\\n🧹 [{datetime.now().strftime('%H:%M:%S')}] Executando limpeza...")
        
        # Remove notícias com mais de 30 dias
        data_limite = datetime.now() - timedelta(days=30)
        noticias_antigas = []
        
        for noticia in self.gerenciador.noticias:
            try:
                data_noticia = datetime.strptime(noticia.data, "%Y-%m-%d %H:%M")
                if data_noticia < data_limite:
                    noticias_antigas.append(noticia)
            except:
                continue
        
        # Remove notícias antigas
        for noticia in noticias_antigas:
            self.gerenciador.noticias.remove(noticia)
        
        if noticias_antigas:
            self.gerenciador.salvar_noticias()
            print(f"   🗑️ {len(noticias_antigas)} notícias antigas removidas")
        else:
            print("   ✅ Nenhuma notícia antiga para remover")
    
    def executar_agendamentos(self):
        """Thread que executa agendamentos"""
        while self.executando:
            schedule.run_pending()
            time.sleep(1)
    
    def iniciar_monitoramento(self):
        """Inicia monitoramento automático"""
        print("🚀 Iniciando sistema de monitoramento...")
        
        self.configurar_agendamentos()
        self.executando = True
        
        # Primeira coleta imediata
        self.coletar_noticias()
        
        # Inicia thread de agendamentos
        self.thread_monitoramento = threading.Thread(target=self.executar_agendamentos)
        self.thread_monitoramento.daemon = True
        self.thread_monitoramento.start()
        
        print("✅ Monitoramento ativo! Pressione Ctrl+C para parar.")
    
    def parar_monitoramento(self):
        """Para monitoramento"""
        print("\\n🛑 Parando monitoramento...")
        self.executando = False
        if self.thread_monitoramento:
            self.thread_monitoramento.join(timeout=2)
        print("✅ Monitoramento parado")
    
    def mostrar_estatisticas(self):
        """Mostra estatísticas do sistema"""
        print("\\n📈 ESTATÍSTICAS DO SISTEMA:")
        print(f"   Execuções: {self.estatisticas['total_execucoes']}")
        print(f"   Notícias coletadas: {self.estatisticas['noticias_coletadas']}")
        print(f"   Última execução: {self.estatisticas['ultima_execucao']}")
        print(f"   Erros: {self.estatisticas['erros']}")
        print(f"   Notícias armazenadas: {len(self.gerenciador.noticias)}")

def interface_monitor():
    """Interface para o sistema de monitoramento"""
    monitor = MonitorNoticias()
    
    # Handler para Ctrl+C
    def signal_handler(sig, frame):
        monitor.parar_monitoramento()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        print("\\n" + "=" * 50)
        print("           SISTEMA DE MONITORAMENTO DE NOTÍCIAS")
        print("=" * 50)
        print("1. 🚀 Iniciar monitoramento automático")
        print("2. 📊 Coletar notícias agora")
        print("3. 📈 Ver estatísticas")
        print("4. 📋 Relatório completo")
        print("5. 🔍 Buscar notícias")
        print("0. 🚪 Sair")
        print("=" * 50)
        
        try:
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "0":
                monitor.parar_monitoramento()
                print("👋 Sistema encerrado!")
                break
            elif opcao == "1":
                monitor.iniciar_monitoramento()
                # Aguarda input para continuar
                input("\\nPressione ENTER para voltar ao menu...")
            elif opcao == "2":
                monitor.coletar_noticias()
            elif opcao == "3":
                monitor.mostrar_estatisticas()
            elif opcao == "4":
                if monitor.gerenciador.noticias:
                    analisador = AnalisadorNoticias(monitor.gerenciador.noticias)
                    analisador.relatorio_completo()
                else:
                    print("📭 Nenhuma notícia disponível")
            elif opcao == "5":
                termo = input("🔍 Digite o termo de busca: ").strip()
                resultados = monitor.gerenciador.buscar_noticias(termo)
                print(f"\\n📰 {len(resultados)} notícias encontradas:")
                for i, noticia in enumerate(resultados[:10], 1):  # Mostra apenas 10
                    print(f"{i}. {noticia}")
            else:
                print("❌ Opção inválida!")
        
        except KeyboardInterrupt:
            monitor.parar_monitoramento()
            print("\\n👋 Sistema encerrado pelo usuário!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

print("=== SISTEMA COMPLETO DE MONITORAMENTO ===")
print("🤖 Web Scraper com agendamento automático")
print("📊 Análise contínua de sentimentos")
print("💾 Armazenamento persistente")
print("📈 Relatórios e estatísticas")
print()
print("💡 Para executar o sistema completo, descomente:")
print("# interface_monitor()")
print()
print("🎉 Projeto de Web Scraper concluído!")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        print("\n🎉 Projeto de Web Scraper concluído!")
        print("✨ Você implementou um sistema avançado com:")
        print("• Web scraping automatizado")
        print("• Análise de sentimentos")
        print("• Agendamento de tarefas")
        print("• Threading e processamento assíncrono")
        print("• Persistência em múltiplos formatos")
        print("• Interface completa de usuário")
        
        self.utils.pausar()

    def projeto_final_avancado(self) -> None:
        """Módulo 26: PROJETO FINAL - API REST"""
        self.utils.limpar_tela()
        self.utils.titulo("PROJETO FINAL: API REST PARA GERENCIAMENTO DE TAREFAS")
        
        print("🚀 Vamos criar uma API REST completa!")
        print("⚡ Projeto final que demonstra domínio completo do Python!")
        
        print("\n═══════════════════════════════════════════════")
        print("        ESPECIFICAÇÕES DO PROJETO FINAL")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Funcionalidades da API:")
        print("• 🌐 Endpoints RESTful completos")
        print("• 🗄️ Banco de dados SQLite")
        print("• 🔐 Autenticação JWT")
        print("• ✅ Validação de dados")
        print("• 📝 Documentação automática")
        print("• 🧪 Testes automatizados")
        print("• 📊 Logs e monitoramento")
        
        self.utils.pausar()
        
        codigo1 = '''# API REST - Estrutura e Modelos
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import logging
import functools
import re
from typing import Dict, List, Optional, Tuple

# Configuração do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_super_forte_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco
db = SQLAlchemy(app)

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Modelos do banco de dados
class Usuario(db.Model):
    """Modelo de usuário"""
    
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)
    
    # Relacionamento com tarefas
    tarefas = db.relationship('Tarefa', backref='autor', lazy=True, cascade='all, delete-orphan')
    
    def set_senha(self, senha: str):
        """Define senha com hash"""
        self.senha_hash = generate_password_hash(senha)
    
    def verificar_senha(self, senha: str) -> bool:
        """Verifica senha"""
        return check_password_hash(self.senha_hash, senha)
    
    def gerar_token(self) -> str:
        """Gera token JWT"""
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    
    @staticmethod
    def verificar_token(token: str) -> Optional['Usuario']:
        """Verifica token JWT"""
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return Usuario.query.get(payload['user_id'])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def to_dict(self, incluir_tarefas: bool = False) -> Dict:
        """Converte para dicionário"""
        data = {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'data_criacao': self.data_criacao.isoformat(),
            'ativo': self.ativo
        }
        
        if incluir_tarefas:
            data['tarefas'] = [tarefa.to_dict() for tarefa in self.tarefas]
        
        return data

class Tarefa(db.Model):
    """Modelo de tarefa"""
    
    __tablename__ = 'tarefas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text)
    concluida = db.Column(db.Boolean, default=False)
    prioridade = db.Column(db.String(20), default='média')  # baixa, média, alta
    data_criacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    data_conclusao = db.Column(db.DateTime)
    data_vencimento = db.Column(db.DateTime)
    
    # Chave estrangeira
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    def marcar_concluida(self):
        """Marca tarefa como concluída"""
        self.concluida = True
        self.data_conclusao = datetime.datetime.utcnow()
    
    def esta_vencida(self) -> bool:
        """Verifica se tarefa está vencida"""
        if not self.data_vencimento or self.concluida:
            return False
        return datetime.datetime.utcnow() > self.data_vencimento
    
    def to_dict(self) -> Dict:
        """Converte para dicionário"""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'concluida': self.concluida,
            'prioridade': self.prioridade,
            'data_criacao': self.data_criacao.isoformat(),
            'data_conclusao': self.data_conclusao.isoformat() if self.data_conclusao else None,
            'data_vencimento': self.data_vencimento.isoformat() if self.data_vencimento else None,
            'usuario_id': self.usuario_id,
            'vencida': self.esta_vencida()
        }

# Validadores
class ValidadorDados:
    """Classe para validação de dados"""
    
    @staticmethod
    def validar_email(email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validar_senha(senha: str) -> Tuple[bool, str]:
        """Valida força da senha"""
        if len(senha) < 6:
            return False, "Senha deve ter pelo menos 6 caracteres"
        
        if not re.search(r'[A-Za-z]', senha):
            return False, "Senha deve conter pelo menos uma letra"
        
        if not re.search(r'\\d', senha):
            return False, "Senha deve conter pelo menos um número"
        
        return True, "Senha válida"
    
    @staticmethod
    def validar_prioridade(prioridade: str) -> bool:
        """Valida prioridade da tarefa"""
        return prioridade.lower() in ['baixa', 'média', 'alta']

# Decorador de autenticação
def token_obrigatorio(f):
    """Decorador que exige token válido"""
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'erro': 'Token de acesso é obrigatório'}), 401
        
        try:
            # Remove 'Bearer ' do início se presente
            if token.startswith('Bearer '):
                token = token[7:]
            
            usuario = Usuario.verificar_token(token)
            if not usuario:
                return jsonify({'erro': 'Token inválido ou expirado'}), 401
            
            g.usuario_atual = usuario
        
        except Exception as e:
            logger.error(f"Erro na validação do token: {e}")
            return jsonify({'erro': 'Token inválido'}), 401
        
        return f(*args, **kwargs)
    
    return decorator

print("=== ESTRUTURA DA API CRIADA ===")
print("✅ Modelos: Usuario, Tarefa")
print("✅ Validação de dados")
print("✅ Autenticação JWT")
print("✅ Sistema de logs")
print("✅ Decorador de autenticação")

# Criando banco de dados (simulado)
try:
    with app.app_context():
        # db.create_all()  # Descomentei para demonstração
        print("✅ Banco de dados configurado")
except Exception as e:
    print(f"⚠️ Erro ao configurar banco: {e}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🌐 Endpoints da API:")
        
        codigo2 = '''# Endpoints da API REST
from flask import make_response

# Endpoints de autenticação
@app.route('/api/registro', methods=['POST'])
def registrar_usuario():
    """Registra novo usuário"""
    try:
        dados = request.get_json()
        
        # Validação de dados
        if not dados or not dados.get('nome') or not dados.get('email') or not dados.get('senha'):
            return jsonify({'erro': 'Nome, email e senha são obrigatórios'}), 400
        
        # Validar email
        if not ValidadorDados.validar_email(dados['email']):
            return jsonify({'erro': 'Email inválido'}), 400
        
        # Validar senha
        senha_valida, mensagem = ValidadorDados.validar_senha(dados['senha'])
        if not senha_valida:
            return jsonify({'erro': mensagem}), 400
        
        # Verificar se usuário já existe
        if Usuario.query.filter_by(email=dados['email']).first():
            return jsonify({'erro': 'Email já cadastrado'}), 409
        
        # Criar usuário
        usuario = Usuario(
            nome=dados['nome'],
            email=dados['email']
        )
        usuario.set_senha(dados['senha'])
        
        db.session.add(usuario)
        db.session.commit()
        
        logger.info(f"Usuário registrado: {usuario.email}")
        
        return jsonify({
            'mensagem': 'Usuário registrado com sucesso',
            'usuario': usuario.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro no registro: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Autentica usuário"""
    try:
        dados = request.get_json()
        
        if not dados or not dados.get('email') or not dados.get('senha'):
            return jsonify({'erro': 'Email e senha são obrigatórios'}), 400
        
        # Buscar usuário
        usuario = Usuario.query.filter_by(email=dados['email']).first()
        
        if not usuario or not usuario.verificar_senha(dados['senha']):
            return jsonify({'erro': 'Credenciais inválidas'}), 401
        
        if not usuario.ativo:
            return jsonify({'erro': 'Usuário inativo'}), 401
        
        # Gerar token
        token = usuario.gerar_token()
        
        logger.info(f"Login realizado: {usuario.email}")
        
        return jsonify({
            'mensagem': 'Login realizado com sucesso',
            'token': token,
            'usuario': usuario.to_dict()
        }), 200
    
    except Exception as e:
        logger.error(f"Erro no login: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

# Endpoints de tarefas
@app.route('/api/tarefas', methods=['GET'])
@token_obrigatorio
def listar_tarefas():
    """Lista tarefas do usuário"""
    try:
        # Parâmetros de filtro
        concluida = request.args.get('concluida')
        prioridade = request.args.get('prioridade')
        vencidas = request.args.get('vencidas')
        
        # Query base
        query = Tarefa.query.filter_by(usuario_id=g.usuario_atual.id)
        
        # Aplicar filtros
        if concluida is not None:
            concluida_bool = concluida.lower() == 'true'
            query = query.filter_by(concluida=concluida_bool)
        
        if prioridade:
            query = query.filter_by(prioridade=prioridade.lower())
        
        # Filtro de vencidas
        if vencidas and vencidas.lower() == 'true':
            agora = datetime.datetime.utcnow()
            query = query.filter(
                Tarefa.data_vencimento < agora,
                Tarefa.concluida == False
            )
        
        # Ordenação
        query = query.order_by(Tarefa.data_criacao.desc())
        
        tarefas = query.all()
        
        return jsonify({
            'tarefas': [tarefa.to_dict() for tarefa in tarefas],
            'total': len(tarefas)
        }), 200
    
    except Exception as e:
        logger.error(f"Erro ao listar tarefas: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/tarefas', methods=['POST'])
@token_obrigatorio
def criar_tarefa():
    """Cria nova tarefa"""
    try:
        dados = request.get_json()
        
        if not dados or not dados.get('titulo'):
            return jsonify({'erro': 'Título é obrigatório'}), 400
        
        # Validar prioridade
        prioridade = dados.get('prioridade', 'média').lower()
        if not ValidadorDados.validar_prioridade(prioridade):
            return jsonify({'erro': 'Prioridade deve ser: baixa, média ou alta'}), 400
        
        # Validar data de vencimento
        data_vencimento = None
        if dados.get('data_vencimento'):
            try:
                data_vencimento = datetime.datetime.fromisoformat(dados['data_vencimento'])
            except ValueError:
                return jsonify({'erro': 'Data de vencimento inválida. Use formato ISO'}), 400
        
        # Criar tarefa
        tarefa = Tarefa(
            titulo=dados['titulo'],
            descricao=dados.get('descricao', ''),
            prioridade=prioridade,
            data_vencimento=data_vencimento,
            usuario_id=g.usuario_atual.id
        )
        
        db.session.add(tarefa)
        db.session.commit()
        
        logger.info(f"Tarefa criada: {tarefa.titulo} (usuário: {g.usuario_atual.email})")
        
        return jsonify({
            'mensagem': 'Tarefa criada com sucesso',
            'tarefa': tarefa.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao criar tarefa: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/tarefas/<int:tarefa_id>', methods=['GET'])
@token_obrigatorio
def obter_tarefa(tarefa_id):
    """Obtém tarefa específica"""
    try:
        tarefa = Tarefa.query.filter_by(
            id=tarefa_id,
            usuario_id=g.usuario_atual.id
        ).first()
        
        if not tarefa:
            return jsonify({'erro': 'Tarefa não encontrada'}), 404
        
        return jsonify({'tarefa': tarefa.to_dict()}), 200
    
    except Exception as e:
        logger.error(f"Erro ao obter tarefa: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
@token_obrigatorio
def atualizar_tarefa(tarefa_id):
    """Atualiza tarefa"""
    try:
        tarefa = Tarefa.query.filter_by(
            id=tarefa_id,
            usuario_id=g.usuario_atual.id
        ).first()
        
        if not tarefa:
            return jsonify({'erro': 'Tarefa não encontrada'}), 404
        
        dados = request.get_json()
        if not dados:
            return jsonify({'erro': 'Dados são obrigatórios'}), 400
        
        # Atualizar campos
        if 'titulo' in dados:
            tarefa.titulo = dados['titulo']
        
        if 'descricao' in dados:
            tarefa.descricao = dados['descricao']
        
        if 'prioridade' in dados:
            prioridade = dados['prioridade'].lower()
            if ValidadorDados.validar_prioridade(prioridade):
                tarefa.prioridade = prioridade
            else:
                return jsonify({'erro': 'Prioridade inválida'}), 400
        
        if 'concluida' in dados:
            if dados['concluida'] and not tarefa.concluida:
                tarefa.marcar_concluida()
            elif not dados['concluida']:
                tarefa.concluida = False
                tarefa.data_conclusao = None
        
        if 'data_vencimento' in dados:
            if dados['data_vencimento']:
                try:
                    tarefa.data_vencimento = datetime.datetime.fromisoformat(dados['data_vencimento'])
                except ValueError:
                    return jsonify({'erro': 'Data de vencimento inválida'}), 400
            else:
                tarefa.data_vencimento = None
        
        db.session.commit()
        
        logger.info(f"Tarefa atualizada: {tarefa.id} (usuário: {g.usuario_atual.email})")
        
        return jsonify({
            'mensagem': 'Tarefa atualizada com sucesso',
            'tarefa': tarefa.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao atualizar tarefa: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
@token_obrigatorio
def excluir_tarefa(tarefa_id):
    """Exclui tarefa"""
    try:
        tarefa = Tarefa.query.filter_by(
            id=tarefa_id,
            usuario_id=g.usuario_atual.id
        ).first()
        
        if not tarefa:
            return jsonify({'erro': 'Tarefa não encontrada'}), 404
        
        db.session.delete(tarefa)
        db.session.commit()
        
        logger.info(f"Tarefa excluída: {tarefa_id} (usuário: {g.usuario_atual.email})")
        
        return jsonify({'mensagem': 'Tarefa excluída com sucesso'}), 200
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao excluir tarefa: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

print("=== ENDPOINTS DA API CRIADOS ===")
print("✅ POST /api/registro - Registrar usuário")
print("✅ POST /api/login - Fazer login")
print("✅ GET /api/tarefas - Listar tarefas")
print("✅ POST /api/tarefas - Criar tarefa")
print("✅ GET /api/tarefas/<id> - Obter tarefa")
print("✅ PUT /api/tarefas/<id> - Atualizar tarefa")
print("✅ DELETE /api/tarefas/<id> - Excluir tarefa")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n📊 Endpoints Administrativos e Documentação:")
        
        codigo3 = '''# Endpoints administrativos e de monitoramento
@app.route('/api/stats', methods=['GET'])
@token_obrigatorio
def estatisticas_usuario():
    """Estatísticas do usuário"""
    try:
        usuario = g.usuario_atual
        
        # Contadores básicos
        total_tarefas = Tarefa.query.filter_by(usuario_id=usuario.id).count()
        concluidas = Tarefa.query.filter_by(usuario_id=usuario.id, concluida=True).count()
        pendentes = total_tarefas - concluidas
        
        # Tarefas vencidas
        agora = datetime.datetime.utcnow()
        vencidas = Tarefa.query.filter(
            Tarefa.usuario_id == usuario.id,
            Tarefa.data_vencimento < agora,
            Tarefa.concluida == False
        ).count()
        
        # Tarefas por prioridade
        prioridades = {}
        for prioridade in ['baixa', 'média', 'alta']:
            count = Tarefa.query.filter_by(
                usuario_id=usuario.id,
                prioridade=prioridade,
                concluida=False
            ).count()
            prioridades[prioridade] = count
        
        # Taxa de conclusão
        taxa_conclusao = (concluidas / total_tarefas * 100) if total_tarefas > 0 else 0
        
        # Tarefas criadas nos últimos 7 dias
        semana_atras = agora - datetime.timedelta(days=7)
        recentes = Tarefa.query.filter(
            Tarefa.usuario_id == usuario.id,
            Tarefa.data_criacao >= semana_atras
        ).count()
        
        return jsonify({
            'estatisticas': {
                'total_tarefas': total_tarefas,
                'concluidas': concluidas,
                'pendentes': pendentes,
                'vencidas': vencidas,
                'taxa_conclusao': round(taxa_conclusao, 2),
                'criadas_ultima_semana': recentes,
                'por_prioridade': prioridades
            }
        }), 200
    
    except Exception as e:
        logger.error(f"Erro ao obter estatísticas: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/exportar', methods=['GET'])
@token_obrigatorio
def exportar_tarefas():
    """Exporta tarefas do usuário"""
    try:
        formato = request.args.get('formato', 'json').lower()
        
        tarefas = Tarefa.query.filter_by(usuario_id=g.usuario_atual.id).all()
        dados_tarefas = [tarefa.to_dict() for tarefa in tarefas]
        
        if formato == 'csv':
            import io
            import csv
            
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=[
                'id', 'titulo', 'descricao', 'concluida', 'prioridade',
                'data_criacao', 'data_conclusao', 'data_vencimento'
            ])
            
            writer.writeheader()
            for tarefa_dict in dados_tarefas:
                # Remove campos que não queremos no CSV
                csv_data = {k: v for k, v in tarefa_dict.items() 
                           if k not in ['usuario_id', 'vencida']}
                writer.writerow(csv_data)
            
            response = make_response(output.getvalue())
            response.headers['Content-Type'] = 'text/csv'
            response.headers['Content-Disposition'] = 'attachment; filename=tarefas.csv'
            
            return response
        
        else:  # JSON
            return jsonify({
                'usuario': g.usuario_atual.to_dict(),
                'tarefas': dados_tarefas,
                'exportado_em': datetime.datetime.utcnow().isoformat()
            }), 200
    
    except Exception as e:
        logger.error(f"Erro na exportação: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/perfil', methods=['GET'])
@token_obrigatorio
def obter_perfil():
    """Obtém perfil do usuário"""
    return jsonify({'usuario': g.usuario_atual.to_dict(incluir_tarefas=True)}), 200

@app.route('/api/perfil', methods=['PUT'])
@token_obrigatorio
def atualizar_perfil():
    """Atualiza perfil do usuário"""
    try:
        dados = request.get_json()
        usuario = g.usuario_atual
        
        if 'nome' in dados:
            usuario.nome = dados['nome']
        
        if 'email' in dados:
            if not ValidadorDados.validar_email(dados['email']):
                return jsonify({'erro': 'Email inválido'}), 400
            
            # Verificar se email já existe (exceto o próprio usuário)
            existe = Usuario.query.filter(
                Usuario.email == dados['email'],
                Usuario.id != usuario.id
            ).first()
            
            if existe:
                return jsonify({'erro': 'Email já está em uso'}), 409
            
            usuario.email = dados['email']
        
        if 'senha' in dados:
            senha_valida, mensagem = ValidadorDados.validar_senha(dados['senha'])
            if not senha_valida:
                return jsonify({'erro': mensagem}), 400
            
            usuario.set_senha(dados['senha'])
        
        db.session.commit()
        
        logger.info(f"Perfil atualizado: {usuario.email}")
        
        return jsonify({
            'mensagem': 'Perfil atualizado com sucesso',
            'usuario': usuario.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao atualizar perfil: {e}")
        return jsonify({'erro': 'Erro interno do servidor'}), 500

# Endpoint de documentação
@app.route('/api/docs', methods=['GET'])
def documentacao():
    """Documentação da API"""
    docs = {
        'nome': 'API de Gerenciamento de Tarefas',
        'versao': '1.0.0',
        'descricao': 'API REST para gerenciar tarefas pessoais',
        'endpoints': {
            'autenticacao': {
                'POST /api/registro': 'Registrar novo usuário',
                'POST /api/login': 'Fazer login e obter token'
            },
            'tarefas': {
                'GET /api/tarefas': 'Listar tarefas (filtros: concluida, prioridade, vencidas)',
                'POST /api/tarefas': 'Criar nova tarefa',
                'GET /api/tarefas/{id}': 'Obter tarefa específica',
                'PUT /api/tarefas/{id}': 'Atualizar tarefa',
                'DELETE /api/tarefas/{id}': 'Excluir tarefa'
            },
            'usuario': {
                'GET /api/perfil': 'Obter perfil do usuário',
                'PUT /api/perfil': 'Atualizar perfil',
                'GET /api/stats': 'Estatísticas do usuário',
                'GET /api/exportar': 'Exportar dados (formatos: json, csv)'
            },
            'documentacao': {
                'GET /api/docs': 'Esta documentação',
                'GET /api/health': 'Status da API'
            }
        },
        'autenticacao': {
            'tipo': 'JWT Bearer Token',
            'header': 'Authorization: Bearer <token>',
            'expiracao': '24 horas'
        },
        'exemplo_uso': {
            '1_registro': {
                'url': 'POST /api/registro',
                'body': {
                    'nome': 'João Silva',
                    'email': 'joao@email.com',
                    'senha': 'senha123'
                }
            },
            '2_login': {
                'url': 'POST /api/login',
                'body': {
                    'email': 'joao@email.com',
                    'senha': 'senha123'
                }
            },
            '3_criar_tarefa': {
                'url': 'POST /api/tarefas',
                'headers': {
                    'Authorization': 'Bearer <token>'
                },
                'body': {
                    'titulo': 'Estudar Python',
                    'descricao': 'Completar curso de Python avançado',
                    'prioridade': 'alta',
                    'data_vencimento': '2024-12-31T23:59:59'
                }
            }
        }
    }
    
    return jsonify(docs), 200

# Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """Verifica status da API"""
    try:
        # Testa conexão com banco
        db.session.execute('SELECT 1')
        db_status = 'ok'
    except:
        db_status = 'erro'
    
    return jsonify({
        'status': 'ativo',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'banco_dados': db_status,
        'versao': '1.0.0'
    }), 200

# Handler de erros
@app.errorhandler(404)
def not_found(error):
    return jsonify({'erro': 'Endpoint não encontrado'}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'erro': 'Método não permitido'}), 405

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Erro interno: {error}")
    return jsonify({'erro': 'Erro interno do servidor'}), 500

print("=== API COMPLETA CRIADA ===")
print("✅ Endpoints administrativos")
print("✅ Sistema de exportação")
print("✅ Documentação automática")
print("✅ Health checks")
print("✅ Tratamento de erros")

# Função para executar a API
def executar_api():
    """Executa a API em modo de desenvolvimento"""
    with app.app_context():
        # Criar tabelas
        db.create_all()
        
        # Dados de exemplo
        if Usuario.query.count() == 0:
            usuario_demo = Usuario(nome="Demo User", email="demo@api.com")
            usuario_demo.set_senha("demo123")
            db.session.add(usuario_demo)
            db.session.commit()
            
            print("✅ Usuário demo criado: demo@api.com / demo123")
    
    print("\\n🚀 Iniciando API...")
    print("📝 Documentação: http://localhost:5000/api/docs")
    print("❤️ Health check: http://localhost:5000/api/health")
    print("\\n💡 Para testar:")
    print("1. Registre um usuário: POST /api/registro")
    print("2. Faça login: POST /api/login")
    print("3. Use o token para acessar endpoints protegidos")
    
    # app.run(debug=True, port=5000)  # Descomentei para demonstração

print("\\n💡 Para executar a API, descomente:")
print("# executar_api()")
print("\\n🎉 Projeto Final de API REST concluído!")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        print("\n🎊 PARABÉNS! CURSO COMPLETO!")
        print("✨ Você concluiu todos os 26 módulos do curso!")
        print()
        print("🚀 O que você aprendeu:")
        print("• Fundamentos sólidos do Python")
        print("• Programação orientada a objetos")
        print("• Manipulação de arquivos e dados")
        print("• Web scraping e APIs")
        print("• Expressões regulares e debugging")
        print("• Generators, decorators e conceitos avançados")
        print("• Projetos práticos complexos")
        print()
        print("🎯 Agora você está pronto para:")
        print("• Desenvolver aplicações Python profissionais")
        print("• Trabalhar com APIs e web services")
        print("• Automatizar tarefas complexas")
        print("• Contribuir para projetos open source")
        print("• Continuar aprendendo frameworks como Django, FastAPI")
        print()
        print("🌟 Continue praticando e explorando!")
        print("📚 O aprendizado nunca para!")
        
        self.utils.pausar()
    
    # ===============================================
    # MINI PROJETOS PRÁTICOS - MÓDULOS INTERMEDIÁRIOS (12-17)
    # ===============================================
    
    def _mini_projeto_modulo_12(self) -> None:
        """Mini Projeto - Módulo 12: Sistema de Gerenciamento de Contatos"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE CONTATOS")
        print("📱 Vamos criar um sistema completo de gerenciamento de contatos!")
        print("🛠️ Usando: Dicionários, Sets e Manipulação de Dados")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 📱 SISTEMA DE GERENCIAMENTO DE CONTATOS
# Projeto prático usando dicionários e sets

import json
from datetime import datetime

class SistemaContatos:
    def __init__(self):
        self.contatos = {}  # Dicionário principal
        self.grupos = {}    # Grupos de contatos
        self.historico = [] # Histórico de operações
    
    def adicionar_contato(self, nome, telefone, email=None, grupo="Geral"):
        """Adiciona um novo contato"""
        if nome in self.contatos:
            print(f"❌ Contato {nome} já existe!")
            return False
        
        # Criando contato como dicionário
        contato = {
            "telefone": telefone,
            "email": email or "Não informado",
            "grupo": grupo,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "tags": set()  # Set para tags únicas
        }
        
        self.contatos[nome] = contato
        
        # Adiciona ao grupo
        if grupo not in self.grupos:
            self.grupos[grupo] = set()
        self.grupos[grupo].add(nome)
        
        # Registra no histórico
        self.historico.append(f"Adicionado: {nome} em {contato['data_criacao']}")
        
        print(f"✅ Contato {nome} adicionado com sucesso!")
        return True
    
    def buscar_contato(self, termo):
        """Busca contatos por nome, telefone ou email"""
        resultados = []
        termo_lower = termo.lower()
        
        for nome, dados in self.contatos.items():
            if (termo_lower in nome.lower() or 
                termo in dados["telefone"] or 
                termo_lower in dados["email"].lower()):
                resultados.append((nome, dados))
        
        return resultados
    
    def listar_por_grupo(self, grupo):
        """Lista contatos de um grupo específico"""
        if grupo not in self.grupos:
            return []
        
        contatos_grupo = []
        for nome in self.grupos[grupo]:
            if nome in self.contatos:
                contatos_grupo.append((nome, self.contatos[nome]))
        
        return contatos_grupo
    
    def adicionar_tag(self, nome, tag):
        """Adiciona tag a um contato (usando set)"""
        if nome in self.contatos:
            self.contatos[nome]["tags"].add(tag)
            print(f"🏷️ Tag '{tag}' adicionada ao contato {nome}")
            return True
        return False
    
    def buscar_por_tags(self, tags_buscadas):
        """Busca contatos que tenham todas as tags especificadas"""
        tags_set = set(tags_buscadas)
        resultados = []
        
        for nome, dados in self.contatos.items():
            if tags_set.issubset(dados["tags"]):
                resultados.append((nome, dados))
        
        return resultados
    
    def estatisticas(self):
        """Mostra estatísticas do sistema"""
        total_contatos = len(self.contatos)
        total_grupos = len(self.grupos)
        
        # Conta contatos por grupo
        contatos_por_grupo = {}
        for grupo, nomes in self.grupos.items():
            contatos_por_grupo[grupo] = len(nomes)
        
        # Todas as tags únicas
        todas_tags = set()
        for dados in self.contatos.values():
            todas_tags.update(dados["tags"])
        
        return {
            "total_contatos": total_contatos,
            "total_grupos": total_grupos,
            "contatos_por_grupo": contatos_por_grupo,
            "tags_disponiveis": todas_tags,
            "total_operacoes": len(self.historico)
        }
    
    def exportar_dados(self):
        """Exporta contatos para formato JSON"""
        # Converte sets em listas para JSON
        dados_exportacao = {}
        for nome, dados in self.contatos.items():
            dados_copia = dados.copy()
            dados_copia["tags"] = list(dados_copia["tags"])
            dados_exportacao[nome] = dados_copia
        
        return json.dumps(dados_exportacao, indent=2, ensure_ascii=False)

# DEMONSTRAÇÃO DO SISTEMA
print("=== DEMONSTRAÇÃO: SISTEMA DE CONTATOS ===\\n")

# Criando instância
sistema = SistemaContatos()

# Adicionando contatos
print("📝 ADICIONANDO CONTATOS:")
sistema.adicionar_contato("João Silva", "(11) 99999-1111", "joao@email.com", "Trabalho")
sistema.adicionar_contato("Maria Santos", "(11) 88888-2222", "maria@email.com", "Família")
sistema.adicionar_contato("Pedro Costa", "(11) 77777-3333", "pedro@email.com", "Amigos")
sistema.adicionar_contato("Ana Lima", "(11) 66666-4444", "ana@email.com", "Trabalho")

print("\\n🏷️ ADICIONANDO TAGS:")
sistema.adicionar_tag("João Silva", "programador")
sistema.adicionar_tag("João Silva", "python")
sistema.adicionar_tag("Maria Santos", "família")
sistema.adicionar_tag("Pedro Costa", "faculdade")
sistema.adicionar_tag("Ana Lima", "gerente")
sistema.adicionar_tag("Ana Lima", "programador")

print("\\n🔍 BUSCANDO CONTATOS:")
resultados = sistema.buscar_contato("João")
for nome, dados in resultados:
    print(f"✅ Encontrado: {nome} - {dados['telefone']}")

print("\\n👥 CONTATOS DO GRUPO 'Trabalho':")
trabalho = sistema.listar_por_grupo("Trabalho")
for nome, dados in trabalho:
    print(f"💼 {nome}: {dados['telefone']} ({dados['email']})")

print("\\n🏷️ BUSCA POR TAGS 'programador':")
programadores = sistema.buscar_por_tags(["programador"])
for nome, dados in programadores:
    tags = ", ".join(dados["tags"])
    print(f"👨‍💻 {nome}: Tags [{tags}]")

print("\\n📊 ESTATÍSTICAS DO SISTEMA:")
stats = sistema.estatisticas()
print(f"📱 Total de contatos: {stats['total_contatos']}")
print(f"👥 Total de grupos: {stats['total_grupos']}")
print(f"🏷️ Tags disponíveis: {', '.join(stats['tags_disponiveis'])}")

print("\\n💾 DADOS EXPORTADOS (JSON):")
json_export = sistema.exportar_dados()
print(json_export[:200] + "..." if len(json_export) > 200 else json_export)

print("\\n🎉 Sistema de Contatos funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Dicionários para estruturar dados")
print("  • Sets para tags únicas e operações de conjunto")
print("  • Métodos de busca e filtragem")
print("  • Manipulação de dados complexos")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Você criou um sistema completo de contatos!")
        print("🎯 Aplicação real: CRM, agenda pessoal, sistema corporativo")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_12", "Sistema de Contatos Inteligente", 70)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_13(self) -> None:
        """Mini Projeto - Módulo 13: Sistema de Processamento de Dados com Lambda"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: PROCESSADOR DE DADOS AVANÇADO")
        print("🧮 Sistema de análise de dados usando funções lambda e avançadas!")
        print("🛠️ Usando: Lambda, map(), filter(), reduce(), *args, **kwargs")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🧮 SISTEMA DE PROCESSAMENTO DE DADOS AVANÇADO
# Projeto usando lambdas, map, filter, reduce e funções avançadas

from functools import reduce
import statistics
from datetime import datetime

class ProcessadorDados:
    def __init__(self):
        self.transformacoes = {}  # Armazena funções de transformação
        self.historico_operacoes = []
    
    def registrar_transformacao(self, nome, funcao):
        """Registra uma função de transformação personalizada"""
        self.transformacoes[nome] = funcao
        print(f"✅ Transformação '{nome}' registrada")
    
    def processar_vendas(self, *vendas, **configuracoes):
        """Processa dados de vendas com configurações flexíveis"""
        # Configurações padrão
        config = {
            "aplicar_desconto": False,
            "desconto_percentual": 0,
            "filtrar_minimo": 0,
            "moeda": "R$",
            "debug": False
        }
        config.update(configuracoes)  # Atualiza com parâmetros passados
        
        if config["debug"]:
            print(f"📊 Processando {len(vendas)} vendas com config: {config}")
        
        # Converter para lista se necessário
        dados_vendas = list(vendas)
        
        # Aplicar filtro de valor mínimo (usando filter + lambda)
        if config["filtrar_minimo"] > 0:
            dados_vendas = list(filter(
                lambda x: x >= config["filtrar_minimo"], 
                dados_vendas
            ))
        
        # Aplicar desconto (usando map + lambda)
        if config["aplicar_desconto"]:
            desconto = config["desconto_percentual"] / 100
            dados_vendas = list(map(
                lambda x: x * (1 - desconto), 
                dados_vendas
            ))
        
        # Registrar operação
        operacao = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "vendas_processadas": len(dados_vendas),
            "configuracao": config.copy()
        }
        self.historico_operacoes.append(operacao)
        
        return dados_vendas
    
    def analisar_dados(self, dados, *operacoes_customizadas):
        """Análise avançada de dados usando lambdas"""
        if not dados:
            return {"erro": "Dados vazios"}
        
        # Análises básicas com lambdas
        analises = {
            "total": reduce(lambda x, y: x + y, dados),
            "quantidade": len(dados),
            "maior_valor": reduce(lambda x, y: x if x > y else y, dados),
            "menor_valor": reduce(lambda x, y: x if x < y else y, dados),
            "media": sum(dados) / len(dados),
        }
        
        # Análises estatísticas
        if len(dados) > 1:
            analises.update({
                "mediana": statistics.median(dados),
                "desvio_padrao": statistics.stdev(dados)
            })
        
        # Categorização usando lambdas
        categorizar_venda = lambda x: ("Alta" if x > 1000 else 
                                     "Média" if x > 500 else "Baixa")
        
        analises["categorias"] = {
            "alta": len(list(filter(lambda x: x > 1000, dados))),
            "media": len(list(filter(lambda x: 500 <= x <= 1000, dados))),
            "baixa": len(list(filter(lambda x: x < 500, dados)))
        }
        
        # Aplicar operações customizadas se fornecidas
        for i, operacao in enumerate(operacoes_customizadas):
            if callable(operacao):
                try:
                    resultado = operacao(dados)
                    analises[f"custom_{i+1}"] = resultado
                except Exception as e:
                    analises[f"custom_{i+1}_erro"] = str(e)
        
        return analises
    
    def pipeline_transformacao(self, dados, *nomes_transformacoes):
        """Aplica pipeline de transformações registradas"""
        resultado = dados.copy()
        
        for nome in nomes_transformacoes:
            if nome in self.transformacoes:
                try:
                    # Aplica transformação
                    if isinstance(resultado, list):
                        resultado = list(map(self.transformacoes[nome], resultado))
                    else:
                        resultado = self.transformacoes[nome](resultado)
                    print(f"✅ Aplicada transformação: {nome}")
                except Exception as e:
                    print(f"❌ Erro na transformação {nome}: {e}")
                    break
            else:
                print(f"⚠️ Transformação '{nome}' não encontrada")
        
        return resultado
    
    def relatorio_detalhado(self, dados, titulo="Relatório de Dados"):
        """Gera relatório detalhado formatado"""
        print(f"\\n{'='*50}")
        print(f"📊 {titulo.upper()}")
        print(f"{'='*50}")
        
        analise = self.analisar_dados(dados)
        
        print(f"📈 Total: R$ {analise['total']:,.2f}")
        print(f"📊 Quantidade: {analise['quantidade']} itens")
        print(f"💰 Maior venda: R$ {analise['maior_valor']:,.2f}")
        print(f"💵 Menor venda: R$ {analise['menor_valor']:,.2f}")
        print(f"📊 Média: R$ {analise['media']:,.2f}")
        
        if 'mediana' in analise:
            print(f"📊 Mediana: R$ {analise['mediana']:,.2f}")
            print(f"📊 Desvio Padrão: R$ {analise['desvio_padrao']:,.2f}")
        
        print(f"\\n🎯 CATEGORIZAÇÃO:")
        cats = analise['categorias']
        print(f"  🔥 Vendas Altas (>R$1000): {cats['alta']}")
        print(f"  📊 Vendas Médias (R$500-1000): {cats['media']}")
        print(f"  📉 Vendas Baixas (<R$500): {cats['baixa']}")
        
        return analise

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE PROCESSAMENTO DE DADOS ===\\n")

# Criar instância
processor = ProcessadorDados()

# Dados de exemplo - vendas do mês
vendas_janeiro = [1200, 800, 450, 1500, 300, 950, 1800, 600, 750, 1100, 400, 2000]

print("📊 DADOS ORIGINAIS:")
print(f"Vendas Janeiro: {vendas_janeiro}")

# 1. PROCESSAMENTO BÁSICO
print("\\n🔧 PROCESSAMENTO COM CONFIGURAÇÕES:")

# Processar com desconto
vendas_com_desconto = processor.processar_vendas(
    *vendas_janeiro,
    aplicar_desconto=True,
    desconto_percentual=10,
    filtrar_minimo=500,
    debug=True
)

print(f"Vendas após desconto 10% e filtro >R$500: {[f'{v:.0f}' for v in vendas_com_desconto]}")

# 2. REGISTRAR TRANSFORMAÇÕES CUSTOMIZADAS
print("\\n⚙️ REGISTRANDO TRANSFORMAÇÕES:")

# Lambda para converter para dólar (cotação fictícia R$ 5,20)
processor.registrar_transformacao("para_dolar", lambda x: x / 5.2)

# Lambda para aplicar taxa de comissão
processor.registrar_transformacao("comissao_5", lambda x: x * 0.05)

# Lambda para arredondar
processor.registrar_transformacao("arredondar", lambda x: round(x, 2))

# 3. APLICAR PIPELINE DE TRANSFORMAÇÕES
print("\\n🔄 PIPELINE DE TRANSFORMAÇÕES:")
vendas_em_dolar = processor.pipeline_transformacao(
    vendas_com_desconto,
    "para_dolar",
    "arredondar"
)

print(f"Vendas em dólares: {vendas_em_dolar}")

# 4. ANÁLISES AVANÇADAS COM OPERAÇÕES CUSTOMIZADAS
print("\\n🧮 ANÁLISES CUSTOMIZADAS:")

# Operações customizadas usando lambdas
operacao_bonus = lambda dados: sum(v for v in dados if v > 1000) * 0.02
operacao_meta = lambda dados: len([v for v in dados if v > 800]) / len(dados) * 100

analise = processor.analisar_dados(
    vendas_janeiro,
    operacao_bonus,  # Bônus de 2% para vendas >1000
    operacao_meta    # Percentual que atingiu meta de 800
)

print(f"💰 Bônus total (2% vendas >R$1000): R$ {analise.get('custom_1', 0):.2f}")
print(f"🎯 Percentual que atingiu meta: {analise.get('custom_2', 0):.1f}%")

# 5. RELATÓRIO FINAL
processor.relatorio_detalhado(vendas_janeiro, "Vendas Janeiro 2024")

# 6. HISTÓRICO DE OPERAÇÕES
print(f"\\n📝 HISTÓRICO DE OPERAÇÕES ({len(processor.historico_operacoes)}):")
for i, op in enumerate(processor.historico_operacoes, 1):
    print(f"  {i}. {op['timestamp']} - {op['vendas_processadas']} vendas processadas")

print("\\n🎉 Sistema de Processamento funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Funções lambda para transformações rápidas")
print("  • map(), filter(), reduce() para processamento")
print("  • *args e **kwargs para flexibilidade")
print("  • Pipeline de transformações")
print("  • Análises estatísticas avançadas")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de processamento de dados criado!")
        print("🎯 Aplicação real: análise de vendas, business intelligence, ETL")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_13", "Processador de Dados Avançado", 70)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_14(self) -> None:
        """Mini Projeto - Módulo 14: Analisador de Logs com Comprehensions"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: ANALISADOR DE LOGS INTELIGENTE")
        print("📊 Sistema de análise de logs usando comprehensions e estruturas avançadas!")
        print("🛠️ Usando: List/Dict Comprehensions, Set Comprehensions, Expressões Condicionais")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 📊 ANALISADOR DE LOGS INTELIGENTE
# Projeto usando comprehensions para análise eficiente de dados

import re
from datetime import datetime, timedelta
from collections import Counter
import json

class AnalisadorLogs:
    def __init__(self):
        self.logs_raw = []
        self.logs_parsed = []
        self.patterns = {
            'apache': r'(\\S+) - - \\[(.*?)\\] "(.*?)" (\\d+) (\\d+)',
            'nginx': r'(\\S+) - \\S+ \\[(.*?)\\] "(.*?)" (\\d+) (\\d+) "(.*?)" "(.*?)"',
            'custom': r'\\[(.*?)\\] (\\w+): (.*)'
        }
    
    def carregar_logs_simulados(self):
        """Gera logs simulados para demonstração"""
        logs_exemplo = [
            '192.168.1.100 - - [2024/01/15:10:30:45 +0000] "GET /home HTTP/1.1" 200 1024',
            '10.0.0.50 - - [2024/01/15:10:31:12 +0000] "POST /login HTTP/1.1" 200 512',
            '192.168.1.150 - - [2024/01/15:10:32:05 +0000] "GET /dashboard HTTP/1.1" 200 2048',
            '172.16.0.30 - - [2024/01/15:10:33:18 +0000] "GET /api/users HTTP/1.1" 404 256',
            '192.168.1.100 - - [2024/01/15:10:34:22 +0000] "POST /api/data HTTP/1.1" 500 128',
            '10.0.0.75 - - [2024/01/15:10:35:33 +0000] "GET /about HTTP/1.1" 200 768',
            '192.168.1.200 - - [2024/01/15:10:36:44 +0000] "DELETE /api/users/123 HTTP/1.1" 403 64',
            '172.16.0.45 - - [2024/01/15:10:37:55 +0000] "GET /images/logo.png HTTP/1.1" 200 4096',
            '192.168.1.100 - - [2024/01/15:10:38:11 +0000] "GET /contact HTTP/1.1" 200 1536',
            '10.0.0.50 - - [2024/01/15:10:39:29 +0000] "POST /api/upload HTTP/1.1" 413 32'
        ]
        
        self.logs_raw = logs_exemplo
        print(f"✅ Carregados {len(logs_exemplo)} logs de exemplo")
        
    def parse_logs_apache(self):
        """Parse logs usando comprehensions"""
        # List comprehension com parsing de regex
        pattern = self.patterns['apache']
        
        self.logs_parsed = [
            {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'request': match.group(3),
                'status': int(match.group(4)),
                'size': int(match.group(5)),
                'method': match.group(3).split()[0] if len(match.group(3).split()) > 0 else 'UNKNOWN',
                'url': match.group(3).split()[1] if len(match.group(3).split()) > 1 else '/',
                'protocol': match.group(3).split()[2] if len(match.group(3).split()) > 2 else 'HTTP/1.1'
            }
            for log in self.logs_raw
            if (match := re.match(pattern, log))  # Walrus operator + comprehension
        ]
        
        print(f"✅ Parsed {len(self.logs_parsed)} logs com sucesso")
        return self.logs_parsed
    
    def analisar_ips(self):
        """Análise de IPs usando comprehensions"""
        if not self.logs_parsed:
            return {}
        
        # Set comprehension - IPs únicos
        ips_unicos = {log['ip'] for log in self.logs_parsed}
        
        # Dict comprehension - contador de acessos por IP
        contador_ips = {
            ip: len([log for log in self.logs_parsed if log['ip'] == ip])
            for ip in ips_unicos
        }
        
        # List comprehension - IPs suspeitos (>3 requests)
        ips_suspeitos = [
            ip for ip, count in contador_ips.items() if count > 3
        ]
        
        # Dict comprehension - análise por faixa de rede
        analise_redes = {
            f"{'.'.join(ip.split('.')[:3])}.0/24": len([
                log for log in self.logs_parsed 
                if log['ip'].startswith('.'.join(ip.split('.')[:3]))
            ])
            for ip in ips_unicos
        }
        
        return {
            'total_ips_unicos': len(ips_unicos),
            'contador_por_ip': contador_ips,
            'ips_suspeitos': ips_suspeitos,
            'analise_redes': analise_redes,
            'ips_mais_ativos': sorted(contador_ips.items(), key=lambda x: x[1], reverse=True)[:3]
        }
    
    def analisar_status_codes(self):
        """Análise de códigos de status usando comprehensions"""
        if not self.logs_parsed:
            return {}
        
        # Dict comprehension - contador de status codes
        status_count = {
            status: len([log for log in self.logs_parsed if log['status'] == status])
            for status in {log['status'] for log in self.logs_parsed}
        }
        
        # List comprehensions - categorização de status
        sucessos = [log for log in self.logs_parsed if 200 <= log['status'] < 300]
        redirecionamentos = [log for log in self.logs_parsed if 300 <= log['status'] < 400]
        erros_cliente = [log for log in self.logs_parsed if 400 <= log['status'] < 500]
        erros_servidor = [log for log in self.logs_parsed if 500 <= log['status'] < 600]
        
        # Dict comprehension - URLs com erro
        urls_com_erro = {
            log['url']: log['status'] 
            for log in self.logs_parsed 
            if log['status'] >= 400
        }
        
        return {
            'distribuicao_status': status_count,
            'sucessos': len(sucessos),
            'redirecionamentos': len(redirecionamentos),
            'erros_cliente': len(erros_cliente),
            'erros_servidor': len(erros_servidor),
            'urls_com_erro': urls_com_erro,
            'taxa_sucesso': len(sucessos) / len(self.logs_parsed) * 100
        }
    
    def analisar_requisicoes(self):
        """Análise de requisições usando comprehensions"""
        if not self.logs_parsed:
            return {}
        
        # Dict comprehension - contador de métodos HTTP
        metodos = {
            method: len([log for log in self.logs_parsed if log['method'] == method])
            for method in {log['method'] for log in self.logs_parsed}
        }
        
        # Dict comprehension - URLs mais acessadas
        urls_populares = {
            url: len([log for log in self.logs_parsed if log['url'] == url])
            for url in {log['url'] for log in self.logs_parsed}
        }
        
        # List comprehension - requisições grandes (>2KB)
        requisicoes_grandes = [
            {'url': log['url'], 'size': log['size'], 'ip': log['ip']}
            for log in self.logs_parsed if log['size'] > 2048
        ]
        
        # Dict comprehension - análise de APIs vs páginas
        tipo_endpoint = {
            'apis': len([log for log in self.logs_parsed if '/api/' in log['url']]),
            'paginas': len([log for log in self.logs_parsed if '/api/' not in log['url']])
        }
        
        return {
            'metodos_http': metodos,
            'urls_populares': sorted(urls_populares.items(), key=lambda x: x[1], reverse=True),
            'requisicoes_grandes': requisicoes_grandes,
            'tipo_endpoint': tipo_endpoint,
            'total_transferido': sum(log['size'] for log in self.logs_parsed)
        }
    
    def detectar_anomalias(self):
        """Detecção de anomalias usando comprehensions"""
        if not self.logs_parsed:
            return {}
        
        # List comprehension - múltiplos erros do mesmo IP
        ips_com_erros = [
            log['ip'] for log in self.logs_parsed if log['status'] >= 400
        ]
        ips_problematicos = [
            ip for ip in set(ips_com_erros) 
            if ips_com_erros.count(ip) >= 2
        ]
        
        # List comprehension - tentativas de acesso a URLs sensíveis
        urls_suspeitas = ['/admin', '/login', '/api/users', '/config']
        acessos_suspeitos = [
            {'ip': log['ip'], 'url': log['url'], 'status': log['status']}
            for log in self.logs_parsed
            if any(suspeita in log['url'] for suspeita in urls_suspeitas)
        ]
        
        # Dict comprehension - padrões de User-Agent (simulado)
        user_agents_suspeitos = {
            log['ip']: 'Bot suspeito'
            for log in self.logs_parsed
            if log['method'] in ['DELETE', 'PUT'] and log['status'] in [403, 404]
        }
        
        return {
            'ips_problematicos': ips_problematicos,
            'acessos_suspeitos': acessos_suspeitos,
            'user_agents_suspeitos': user_agents_suspeitos,
            'total_anomalias': len(ips_problematicos) + len(acessos_suspeitos)
        }
    
    def gerar_relatorio_completo(self):
        """Gera relatório completo usando todas as análises"""
        print(f"\\n{'='*60}")
        print("📊 RELATÓRIO COMPLETO DE ANÁLISE DE LOGS")
        print(f"{'='*60}")
        
        # Análises usando comprehensions
        analise_ips = self.analisar_ips()
        analise_status = self.analisar_status_codes()
        analise_req = self.analisar_requisicoes()
        anomalias = self.detectar_anomalias()
        
        print(f"\\n🌐 ANÁLISE DE IPs:")
        print(f"  📊 Total de IPs únicos: {analise_ips['total_ips_unicos']}")
        print(f"  🚨 IPs suspeitos (>3 req): {len(analise_ips['ips_suspeitos'])}")
        print(f"  🏆 Top 3 IPs mais ativos:")
        for ip, count in analise_ips['ips_mais_ativos']:
            print(f"    • {ip}: {count} requests")
        
        print(f"\\n📈 ANÁLISE DE STATUS:")
        print(f"  ✅ Taxa de sucesso: {analise_status['taxa_sucesso']:.1f}%")
        print(f"  📊 Distribuição:")
        for status, count in sorted(analise_status['distribuicao_status'].items()):
            print(f"    • {status}: {count} requests")
        
        print(f"\\n🔗 ANÁLISE DE REQUISIÇÕES:")
        print(f"  📊 Métodos HTTP:")
        for method, count in analise_req['metodos_http'].items():
            print(f"    • {method}: {count}")
        print(f"  💾 Total transferido: {analise_req['total_transferido']:,} bytes")
        print(f"  🚀 Requisições grandes (>2KB): {len(analise_req['requisicoes_grandes'])}")
        
        print(f"\\n🚨 DETECÇÃO DE ANOMALIAS:")
        print(f"  ⚠️ Total de anomalias: {anomalias['total_anomalias']}")
        print(f"  🔴 IPs problemáticos: {len(anomalias['ips_problematicos'])}")
        print(f"  🕵️ Acessos suspeitos: {len(anomalias['acessos_suspeitos'])}")
        
        return {
            'ips': analise_ips,
            'status': analise_status,
            'requisicoes': analise_req,
            'anomalias': anomalias
        }

# DEMONSTRAÇÃO DO ANALISADOR
print("=== ANALISADOR DE LOGS INTELIGENTE ===\\n")

# Criar instância e carregar dados
analisador = AnalisadorLogs()
analisador.carregar_logs_simulados()

print("\\n📝 EXEMPLO DE LOGS RAW:")
for i, log in enumerate(analisador.logs_raw[:3], 1):
    print(f"  {i}. {log}")
print("  ... (mais logs)")

print("\\n🔧 PARSING DOS LOGS:")
logs_parsed = analisador.parse_logs_apache()

print("\\n📋 EXEMPLO DE LOG PARSED:")
if logs_parsed:
    exemplo = logs_parsed[0]
    print("  {")
    for key, value in exemplo.items():
        print(f"    '{key}': {repr(value)},")
    print("  }")

# Gerar relatório completo
relatorio = analisador.gerar_relatorio_completo()

print("\\n🎉 Análise de logs concluída com sucesso!")
print("💡 Conceitos aplicados:")
print("  • List comprehensions para parsing e filtragem")
print("  • Dict comprehensions para contagens e agrupamentos")
print("  • Set comprehensions para valores únicos")
print("  • Expressões condicionais em comprehensions")
print("  • Walrus operator (Python 3.8+)")
print("  • Análise de padrões e detecção de anomalias")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Analisador de logs inteligente criado!")
        print("🎯 Aplicação real: monitoramento de servidores, análise de segurança, DevOps")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_14", "Analisador de Logs Inteligente", 75)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_15(self) -> None:
        """Mini Projeto - Módulo 15: Sistema de Backup Inteligente"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE BACKUP INTELIGENTE")
        print("💾 Sistema completo de backup com compressão e versionamento!")
        print("🛠️ Usando: Manipulação de Arquivos, JSON, CSV, ZIP, Diretórios")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 💾 SISTEMA DE BACKUP INTELIGENTE
# Projeto completo de backup com versionamento e compressão

import os
import json
import csv
import zipfile
import shutil
from datetime import datetime, timedelta
import hashlib
from pathlib import Path

class SistemaBackupInteligente:
    def __init__(self, diretorio_backup="backups"):
        self.diretorio_backup = Path(diretorio_backup)
        self.config_file = self.diretorio_backup / "backup_config.json"
        self.log_file = self.diretorio_backup / "backup_log.csv"
        self.metadata_file = self.diretorio_backup / "metadata.json"
        
        # Criar diretório se não existir
        self.diretorio_backup.mkdir(exist_ok=True)
        
        # Configurações padrão
        self.config = {
            "max_versoes": 5,
            "compressao_ativa": True,
            "backup_automatico": False,
            "tipos_arquivo_incluir": [".py", ".txt", ".json", ".csv", ".md"],
            "pastas_ignorar": ["__pycache__", ".git", "node_modules", ".vscode"],
            "tamanho_max_arquivo_mb": 10
        }
        
        self.carregar_configuracao()
        self.inicializar_log()
    
    def carregar_configuracao(self):
        """Carrega configuração do arquivo JSON"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config_carregada = json.load(f)
                    self.config.update(config_carregada)
                print("✅ Configuração carregada")
            except Exception as e:
                print(f"⚠️ Erro ao carregar config: {e}")
        else:
            self.salvar_configuracao()
    
    def salvar_configuracao(self):
        """Salva configuração atual em JSON"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            print("✅ Configuração salva")
        except Exception as e:
            print(f"❌ Erro ao salvar config: {e}")
    
    def inicializar_log(self):
        """Inicializa arquivo de log CSV"""
        if not self.log_file.exists():
            with open(self.log_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'operacao', 'origem', 'destino', 
                    'arquivos_processados', 'tamanho_total', 'status', 'observacoes'
                ])
    
    def registrar_log(self, operacao, origem, destino, arquivos, tamanho, status, obs=""):
        """Registra operação no log CSV"""
        try:
            with open(self.log_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().isoformat(),
                    operacao,
                    str(origem),
                    str(destino),
                    arquivos,
                    tamanho,
                    status,
                    obs
                ])
        except Exception as e:
            print(f"⚠️ Erro ao registrar log: {e}")
    
    def calcular_hash_arquivo(self, caminho_arquivo):
        """Calcula hash MD5 de um arquivo"""
        hash_md5 = hashlib.md5()
        try:
            with open(caminho_arquivo, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception:
            return None
    
    def deve_incluir_arquivo(self, caminho_arquivo):
        """Verifica se arquivo deve ser incluído no backup"""
        arquivo_path = Path(caminho_arquivo)
        
        # Verifica extensão
        if self.config["tipos_arquivo_incluir"]:
            if arquivo_path.suffix not in self.config["tipos_arquivo_incluir"]:
                return False
        
        # Verifica tamanho
        try:
            tamanho_mb = arquivo_path.stat().st_size / (1024 * 1024)
            if tamanho_mb > self.config["tamanho_max_arquivo_mb"]:
                return False
        except:
            return False
        
        # Verifica se está em pasta ignorada
        for pasta_ignorar in self.config["pastas_ignorar"]:
            if pasta_ignorar in str(arquivo_path):
                return False
        
        return True
    
    def escanear_diretorio(self, caminho_origem):
        """Escaneia diretório e retorna lista de arquivos válidos"""
        origem_path = Path(caminho_origem)
        
        if not origem_path.exists():
            print(f"❌ Diretório não existe: {caminho_origem}")
            return []
        
        arquivos_validos = []
        total_arquivos = 0
        
        print(f"🔍 Escaneando: {caminho_origem}")
        
        for arquivo in origem_path.rglob("*"):
            if arquivo.is_file():
                total_arquivos += 1
                
                if self.deve_incluir_arquivo(arquivo):
                    arquivos_validos.append(arquivo)
        
        print(f"📊 Encontrados: {len(arquivos_validos)}/{total_arquivos} arquivos válidos")
        return arquivos_validos
    
    def criar_backup(self, caminho_origem, nome_backup=None):
        """Cria backup de um diretório"""
        if nome_backup is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_backup = f"backup_{timestamp}"
        
        print(f"\\n🚀 Iniciando backup: {nome_backup}")
        
        # Escanear arquivos
        arquivos = self.escanear_diretorio(caminho_origem)
        if not arquivos:
            print("❌ Nenhum arquivo para backup")
            return False
        
        # Criar diretório de versão
        versao_dir = self.diretorio_backup / nome_backup
        versao_dir.mkdir(exist_ok=True)
        
        arquivos_copiados = 0
        tamanho_total = 0
        arquivos_com_erro = []
        
        # Copiar arquivos
        print("📁 Copiando arquivos...")
        for arquivo_origem in arquivos:
            try:
                # Manter estrutura de diretórios
                rel_path = arquivo_origem.relative_to(Path(caminho_origem))
                arquivo_destino = versao_dir / rel_path
                
                # Criar diretório pai se necessário
                arquivo_destino.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar arquivo
                shutil.copy2(arquivo_origem, arquivo_destino)
                
                arquivos_copiados += 1
                tamanho_total += arquivo_origem.stat().st_size
                
                if arquivos_copiados % 10 == 0:
                    print(f"  📁 Copiados: {arquivos_copiados}/{len(arquivos)}")
                
            except Exception as e:
                arquivos_com_erro.append(f"{arquivo_origem}: {e}")
        
        # Criar metadata
        metadata = {
            "nome_backup": nome_backup,
            "timestamp": datetime.now().isoformat(),
            "origem": str(caminho_origem),
            "arquivos_total": len(arquivos),
            "arquivos_copiados": arquivos_copiados,
            "tamanho_bytes": tamanho_total,
            "arquivos_com_erro": arquivos_com_erro,
            "hash_backup": self.calcular_hash_diretorio(versao_dir)
        }
        
        # Salvar metadata
        metadata_path = versao_dir / "backup_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        # Compressão se ativada
        if self.config["compressao_ativa"]:
            print("🗜️ Comprimindo backup...")
            zip_path = versao_dir.with_suffix('.zip')
            self.comprimir_diretorio(versao_dir, zip_path)
            
            # Remove diretório original após compressão
            shutil.rmtree(versao_dir)
            
            # Atualiza tamanho comprimido
            metadata["tamanho_comprimido"] = zip_path.stat().st_size
            metadata["comprimido"] = True
        
        # Registrar no log
        status = "SUCESSO" if not arquivos_com_erro else "SUCESSO_COM_ERROS"
        obs = f"{len(arquivos_com_erro)} erros" if arquivos_com_erro else ""
        
        self.registrar_log(
            "BACKUP",
            caminho_origem,
            nome_backup,
            arquivos_copiados,
            tamanho_total,
            status,
            obs
        )
        
        print(f"\\n✅ Backup concluído!")
        print(f"📊 Arquivos: {arquivos_copiados}/{len(arquivos)}")
        print(f"💾 Tamanho: {tamanho_total / 1024:.1f} KB")
        if arquivos_com_erro:
            print(f"⚠️ Erros: {len(arquivos_com_erro)}")
        
        # Limpeza de versões antigas
        self.limpar_versoes_antigas()
        
        return True
    
    def calcular_hash_diretorio(self, diretorio):
        """Calcula hash MD5 combinado de todos os arquivos"""
        hash_combinado = hashlib.md5()
        
        for arquivo in sorted(Path(diretorio).rglob("*")):
            if arquivo.is_file() and arquivo.name != "backup_metadata.json":
                hash_arquivo = self.calcular_hash_arquivo(arquivo)
                if hash_arquivo:
                    hash_combinado.update(hash_arquivo.encode())
        
        return hash_combinado.hexdigest()
    
    def comprimir_diretorio(self, diretorio, arquivo_zip):
        """Comprime diretório em arquivo ZIP"""
        with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for arquivo in Path(diretorio).rglob("*"):
                if arquivo.is_file():
                    arcname = arquivo.relative_to(diretorio)
                    zip_file.write(arquivo, arcname)
    
    def listar_backups(self):
        """Lista todos os backups disponíveis"""
        backups = []
        
        for item in self.diretorio_backup.iterdir():
            if item.name.startswith('backup_') and (item.is_dir() or item.suffix == '.zip'):
                # Tentar carregar metadata
                if item.is_dir():
                    metadata_path = item / "backup_metadata.json"
                else:  # ZIP
                    try:
                        with zipfile.ZipFile(item, 'r') as zip_file:
                            metadata_content = zip_file.read("backup_metadata.json")
                            metadata = json.loads(metadata_content.decode('utf-8'))
                            backups.append(metadata)
                            continue
                    except:
                        pass
                
                if item.is_dir() and metadata_path.exists():
                    try:
                        with open(metadata_path, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                            backups.append(metadata)
                    except:
                        pass
        
        return sorted(backups, key=lambda x: x.get('timestamp', ''), reverse=True)
    
    def limpar_versoes_antigas(self):
        """Remove versões antigas de backup"""
        backups = self.listar_backups()
        
        if len(backups) > self.config["max_versoes"]:
            # Manter apenas as versões mais recentes
            backups_para_remover = backups[self.config["max_versoes"]:]
            
            for backup in backups_para_remover:
                nome = backup["nome_backup"]
                
                # Remover diretório ou ZIP
                path_dir = self.diretorio_backup / nome
                path_zip = self.diretorio_backup / f"{nome}.zip"
                
                if path_dir.exists():
                    shutil.rmtree(path_dir)
                    print(f"🗑️ Removido backup antigo: {nome}")
                elif path_zip.exists():
                    path_zip.unlink()
                    print(f"🗑️ Removido backup antigo: {nome}.zip")
    
    def relatorio_backups(self):
        """Gera relatório completo dos backups"""
        print(f"\\n{'='*60}")
        print("📊 RELATÓRIO DE BACKUPS")
        print(f"{'='*60}")
        
        backups = self.listar_backups()
        
        if not backups:
            print("📭 Nenhum backup encontrado")
            return
        
        print(f"\\n📈 RESUMO:")
        print(f"  💾 Total de backups: {len(backups)}")
        
        tamanho_total = sum(b.get('tamanho_bytes', 0) for b in backups)
        print(f"  📊 Espaço usado: {tamanho_total / (1024*1024):.1f} MB")
        
        print(f"\\n📋 LISTA DE BACKUPS:")
        for i, backup in enumerate(backups, 1):
            timestamp = backup.get('timestamp', 'N/A')[:16]
            nome = backup.get('nome_backup', 'N/A')
            arquivos = backup.get('arquivos_copiados', 0)
            tamanho_mb = backup.get('tamanho_bytes', 0) / (1024*1024)
            
            print(f"  {i}. {nome}")
            print(f"     📅 {timestamp} | 📁 {arquivos} arquivos | 💾 {tamanho_mb:.1f} MB")
        
        # Ler últimas entradas do log
        print(f"\\n📝 ÚLTIMAS OPERAÇÕES:")
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                logs = list(reader)
                
                for log_entry in logs[-3:]:  # Últimas 3
                    timestamp, operacao, origem, destino, arquivos, tamanho, status, obs = log_entry
                    print(f"  📅 {timestamp[:16]} - {operacao}: {arquivos} arquivos ({status})")
        except:
            print("  ⚠️ Log não disponível")

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE BACKUP INTELIGENTE ===\\n")

# Criar instância
backup_system = SistemaBackupInteligente("demo_backups")

# Criar estrutura de exemplo para backup
print("📁 Criando estrutura de exemplo...")
exemplo_dir = Path("exemplo_projeto")
exemplo_dir.mkdir(exist_ok=True)

# Criar arquivos de exemplo
arquivos_exemplo = [
    ("main.py", "# Arquivo principal\\nprint('Hello World')"),
    ("config.json", '{"debug": true, "version": "1.0"}'),
    ("dados.csv", "nome,idade\\nJoão,30\\nMaria,25"),
    ("README.md", "# Projeto Exemplo\\nDescrição do projeto"),
    ("src/utils.py", "def helper():\\n    return 'helper'"),
    ("src/models.py", "class Model:\\n    pass"),
    ("docs/manual.txt", "Manual do usuário\\nInstruções...")
]

for caminho, conteudo in arquivos_exemplo:
    arquivo_path = exemplo_dir / caminho
    arquivo_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(arquivo_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)

print(f"✅ Criados {len(arquivos_exemplo)} arquivos de exemplo")

# Configurar sistema
print("\\n⚙️ Configurando sistema...")
backup_system.config["max_versoes"] = 3
backup_system.config["compressao_ativa"] = True
backup_system.salvar_configuracao()

# Criar backup
print("\\n💾 Criando primeiro backup...")
backup_system.criar_backup("exemplo_projeto", "backup_demo_v1")

# Modificar alguns arquivos
print("\\n📝 Modificando arquivos...")
with open(exemplo_dir / "main.py", 'a', encoding='utf-8') as f:
    f.write("\\n# Versão 2.0\\nprint('Updated!')")

# Criar segundo backup
print("\\n💾 Criando segundo backup...")
backup_system.criar_backup("exemplo_projeto", "backup_demo_v2")

# Gerar relatório
backup_system.relatorio_backups()

# Limpeza
print(f"\\n🧹 Limpando arquivos de exemplo...")
shutil.rmtree("exemplo_projeto")
shutil.rmtree("demo_backups")

print("\\n🎉 Sistema de Backup funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Manipulação avançada de arquivos e diretórios")
print("  • Serialização JSON para configuração e metadata")
print("  • Logs estruturados em CSV")
print("  • Compressão ZIP")
print("  • Hashing para integridade")
print("  • Versionamento inteligente")
print("  • Configuração flexível")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de backup inteligente criado!")
        print("🎯 Aplicação real: backup de projetos, versionamento, arquivamento")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_15", "Sistema de Backup Inteligente", 75)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_16(self) -> None:
        """Mini Projeto - Módulo 16: Sistema de Monitoramento Robusto"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE MONITORAMENTO ROBUSTO")
        print("🔍 Sistema completo de monitoramento com tratamento de erros avançado!")
        print("🛠️ Usando: Try/Except, Finally, Custom Exceptions, Context Managers")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🔍 SISTEMA DE MONITORAMENTO ROBUSTO
# Projeto com tratamento avançado de exceções e monitoramento

import time
import json
import traceback
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Callable, Any
from contextlib import contextmanager
import threading
import queue

# Exceções customizadas
class MonitoramentoError(Exception):
    """Exceção base para erros de monitoramento"""
    pass

class SensorOfflineError(MonitoramentoError):
    """Sensor está offline ou inacessível"""
    pass

class ValorForaLimiteError(MonitoramentoError):
    """Valor fora dos limites aceitáveis"""
    def __init__(self, valor, limite_min, limite_max):
        self.valor = valor
        self.limite_min = limite_min
        self.limite_max = limite_max
        super().__init__(f"Valor {valor} fora dos limites [{limite_min}, {limite_max}]")

class ConfiguracaoInvalidaError(MonitoramentoError):
    """Configuração do sistema inválida"""
    pass

class AlertaCriticoError(MonitoramentoError):
    """Alerta crítico que requer ação imediata"""
    pass

class NivelAlerta(Enum):
    """Níveis de alerta do sistema"""
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class SistemaMonitoramento:
    def __init__(self):
        self.sensores = {}
        self.alertas = []
        self.configuracao = {}
        self.logs_erro = []
        self.status_sistema = "INICIANDO"
        self.metricas_performance = {
            "total_leituras": 0,
            "erros_consecutivos": 0,
            "ultima_leitura_sucesso": None,
            "tempo_ativo": datetime.now()
        }
    
    @contextmanager
    def contexto_monitoramento(self, nome_operacao):
        """Context manager para operações de monitoramento"""
        inicio = time.time()
        
        print(f"🔄 Iniciando: {nome_operacao}")
        
        try:
            yield
            duracao = time.time() - inicio
            print(f"✅ {nome_operacao} concluída em {duracao:.2f}s")
            
        except SensorOfflineError as e:
            self.registrar_erro("SENSOR_OFFLINE", str(e), nome_operacao)
            raise
            
        except ValorForaLimiteError as e:
            self.registrar_erro("VALOR_LIMITE", str(e), nome_operacao)
            self.gerar_alerta(NivelAlerta.WARNING, f"Limite excedido: {e}")
            raise
            
        except AlertaCriticoError as e:
            self.registrar_erro("ALERTA_CRITICO", str(e), nome_operacao)
            self.gerar_alerta(NivelAlerta.CRITICAL, str(e))
            raise
            
        except Exception as e:
            duracao = time.time() - inicio
            self.registrar_erro("ERRO_GENERICO", str(e), nome_operacao)
            print(f"❌ {nome_operacao} falhou após {duracao:.2f}s: {e}")
            raise
            
        finally:
            # Sempre executado, mesmo com exceções
            self.metricas_performance["total_leituras"] += 1
    
    def registrar_erro(self, tipo_erro, mensagem, contexto=""):
        """Registra erro com detalhes completos"""
        erro_info = {
            "timestamp": datetime.now().isoformat(),
            "tipo": tipo_erro,
            "mensagem": mensagem,
            "contexto": contexto,
            "traceback": traceback.format_exc(),
            "metricas_momento": self.metricas_performance.copy()
        }
        
        self.logs_erro.append(erro_info)
        
        # Manter apenas últimos 100 erros
        if len(self.logs_erro) > 100:
            self.logs_erro = self.logs_erro[-100:]
        
        # Atualizar contadores
        self.metricas_performance["erros_consecutivos"] += 1
    
    def gerar_alerta(self, nivel: NivelAlerta, mensagem: str):
        """Gera alerta com nível específico"""
        alerta = {
            "timestamp": datetime.now().isoformat(),
            "nivel": nivel.name,
            "mensagem": mensagem,
            "id": len(self.alertas) + 1
        }
        
        self.alertas.append(alerta)
        
        # Notificação baseada no nível
        if nivel == NivelAlerta.CRITICAL:
            print(f"🚨 CRÍTICO: {mensagem}")
        elif nivel == NivelAlerta.ERROR:
            print(f"❌ ERRO: {mensagem}")
        elif nivel == NivelAlerta.WARNING:
            print(f"⚠️ AVISO: {mensagem}")
        else:
            print(f"ℹ️ INFO: {mensagem}")
    
    def configurar_sensor(self, nome: str, config: Dict):
        """Configura sensor com validação robusta"""
        try:
            # Validação de configuração
            campos_obrigatorios = ["tipo", "limite_min", "limite_max", "intervalo"]
            
            for campo in campos_obrigatorios:
                if campo not in config:
                    raise ConfiguracaoInvalidaError(f"Campo obrigatório '{campo}' não encontrado")
            
            # Validação de tipos
            if not isinstance(config["limite_min"], (int, float)):
                raise ConfiguracaoInvalidaError("limite_min deve ser numérico")
            
            if not isinstance(config["limite_max"], (int, float)):
                raise ConfiguracaoInvalidaError("limite_max deve ser numérico")
            
            if config["limite_min"] >= config["limite_max"]:
                raise ConfiguracaoInvalidaError("limite_min deve ser menor que limite_max")
            
            # Configuração válida
            self.sensores[nome] = {
                **config,
                "status": "CONFIGURADO",
                "ultima_leitura": None,
                "historico_erros": []
            }
            
            print(f"✅ Sensor '{nome}' configurado com sucesso")
            return True
            
        except ConfiguracaoInvalidaError as e:
            self.registrar_erro("CONFIG_INVALIDA", str(e), f"sensor_{nome}")
            print(f"❌ Erro na configuração do sensor '{nome}': {e}")
            return False
        
        except Exception as e:
            self.registrar_erro("ERRO_CONFIG", str(e), f"sensor_{nome}")
            print(f"❌ Erro inesperado ao configurar sensor '{nome}': {e}")
            return False
    
    def simular_leitura_sensor(self, nome: str) -> float:
        """Simula leitura de sensor com possíveis falhas"""
        import random
        
        if nome not in self.sensores:
            raise SensorOfflineError(f"Sensor '{nome}' não encontrado")
        
        sensor = self.sensores[nome]
        
        # Simular diferentes tipos de erro
        rand = random.random()
        
        if rand < 0.1:  # 10% chance de sensor offline
            raise SensorOfflineError(f"Sensor '{nome}' não responde")
        
        elif rand < 0.2:  # 10% chance de valor fora do limite
            if random.choice([True, False]):
                valor = sensor["limite_max"] + random.uniform(1, 50)
            else:
                valor = sensor["limite_min"] - random.uniform(1, 50)
            
            raise ValorForaLimiteError(valor, sensor["limite_min"], sensor["limite_max"])
        
        elif rand < 0.25:  # 5% chance de alerta crítico
            raise AlertaCriticoError(f"Falha crítica detectada no sensor '{nome}'")
        
        else:
            # Leitura normal
            faixa = sensor["limite_max"] - sensor["limite_min"]
            valor = sensor["limite_min"] + (faixa * random.uniform(0.2, 0.8))
            return round(valor, 2)
    
    def ler_sensor_com_retry(self, nome: str, max_tentativas: int = 3) -> Optional[float]:
        """Lê sensor com retry automático e tratamento robusto"""
        
        for tentativa in range(1, max_tentativas + 1):
            try:
                with self.contexto_monitoramento(f"Leitura sensor {nome} (tentativa {tentativa})"):
                    valor = self.simular_leitura_sensor(nome)
                    
                    # Sucesso - resetar contador de erros
                    self.metricas_performance["erros_consecutivos"] = 0
                    self.metricas_performance["ultima_leitura_sucesso"] = datetime.now()
                    
                    # Atualizar sensor
                    self.sensores[nome]["ultima_leitura"] = {
                        "valor": valor,
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    return valor
                    
            except SensorOfflineError as e:
                if tentativa < max_tentativas:
                    print(f"🔄 Tentativa {tentativa} falhou, aguardando antes da próxima...")
                    time.sleep(0.5)  # Aguardar antes de retry
                else:
                    print(f"❌ Sensor '{nome}' offline após {max_tentativas} tentativas")
                    return None
                    
            except ValorForaLimiteError as e:
                # Para valores fora do limite, não retry - é um valor válido mas problemático
                print(f"⚠️ Valor fora do limite detectado: {e}")
                return e.valor
                
            except AlertaCriticoError as e:
                # Alerta crítico não deve ter retry
                print(f"🚨 Alerta crítico - parando tentativas: {e}")
                return None
                
            except Exception as e:
                if tentativa < max_tentativas:
                    print(f"❌ Erro na tentativa {tentativa}: {e}")
                    time.sleep(0.5)
                else:
                    print(f"❌ Falha definitiva após {max_tentativas} tentativas")
                    return None
        
        return None
    
    def monitoramento_continuo(self, duracao_segundos: int = 10):
        """Executa monitoramento contínuo com tratamento robusto"""
        print(f"\\n🔄 Iniciando monitoramento contínuo por {duracao_segundos}s...")
        
        inicio = time.time()
        self.status_sistema = "MONITORANDO"
        
        try:
            while (time.time() - inicio) < duracao_segundos:
                for nome_sensor in self.sensores.keys():
                    try:
                        valor = self.ler_sensor_com_retry(nome_sensor, max_tentativas=2)
                        
                        if valor is not None:
                            print(f"📊 {nome_sensor}: {valor}")
                        else:
                            print(f"❌ {nome_sensor}: Falha na leitura")
                    
                    except Exception as e:
                        print(f"❌ Erro crítico no sensor {nome_sensor}: {e}")
                
                time.sleep(1)  # Aguardar entre ciclos
                
        except KeyboardInterrupt:
            print("\\n⏹️ Monitoramento interrompido pelo usuário")
            
        except Exception as e:
            print(f"\\n❌ Erro crítico no sistema de monitoramento: {e}")
            self.status_sistema = "ERRO_CRITICO"
            
        finally:
            self.status_sistema = "PARADO"
            print("\\n🛑 Monitoramento finalizado")
    
    def relatorio_status(self):
        """Gera relatório completo do sistema"""
        print(f"\\n{'='*60}")
        print("📊 RELATÓRIO DE STATUS DO SISTEMA")
        print(f"{'='*60}")
        
        # Status geral
        print(f"\\n🔍 STATUS GERAL:")
        print(f"  🟢 Sistema: {self.status_sistema}")
        print(f"  ⏱️ Tempo ativo: {datetime.now() - self.metricas_performance['tempo_ativo']}")
        print(f"  📊 Total de leituras: {self.metricas_performance['total_leituras']}")
        print(f"  ❌ Erros consecutivos: {self.metricas_performance['erros_consecutivos']}")
        
        # Status dos sensores
        print(f"\\n📡 SENSORES ({len(self.sensores)}):")
        for nome, sensor in self.sensores.items():
            status = "🟢 ONLINE" if sensor.get("ultima_leitura") else "🔴 OFFLINE"
            ultima = sensor.get("ultima_leitura", {}).get("timestamp", "Nunca")
            print(f"  {status} {nome}: última leitura {ultima[:19] if ultima != 'Nunca' else ultima}")
        
        # Alertas
        print(f"\\n🚨 ALERTAS ({len(self.alertas)}):")
        if self.alertas:
            for alerta in self.alertas[-5:]:  # Últimos 5
                nivel_icon = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌", "CRITICAL": "🚨"}
                icon = nivel_icon.get(alerta["nivel"], "❓")
                print(f"  {icon} [{alerta['nivel']}] {alerta['mensagem']}")
        else:
            print("  ✅ Nenhum alerta ativo")
        
        # Erros recentes
        print(f"\\n📝 ERROS RECENTES ({len(self.logs_erro)}):")
        if self.logs_erro:
            for erro in self.logs_erro[-3:]:  # Últimos 3
                timestamp = erro["timestamp"][:19]
                tipo = erro["tipo"]
                mensagem = erro["mensagem"][:50]
                print(f"  ❌ {timestamp} [{tipo}] {mensagem}...")
        else:
            print("  ✅ Nenhum erro registrado")

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE MONITORAMENTO ROBUSTO ===\\n")

# Criar instância
monitor = SistemaMonitoramento()

# Configurar sensores
print("⚙️ CONFIGURANDO SENSORES:")

# Sensor de temperatura
config_temp = {
    "tipo": "temperatura",
    "limite_min": 18.0,
    "limite_max": 25.0,
    "intervalo": 1,
    "unidade": "°C"
}

# Sensor de umidade
config_umidade = {
    "tipo": "umidade", 
    "limite_min": 40.0,
    "limite_max": 70.0,
    "intervalo": 1,
    "unidade": "%"
}

# Configuração inválida para demonstrar tratamento de erro
config_invalida = {
    "tipo": "pressao",
    "limite_min": 100,
    # limite_max ausente - erro!
    "intervalo": 1
}

monitor.configurar_sensor("temperatura", config_temp)
monitor.configurar_sensor("umidade", config_umidade)
monitor.configurar_sensor("pressao", config_invalida)  # Vai falhar

print("\\n🔍 TESTANDO LEITURAS INDIVIDUAIS:")

# Testar leituras com diferentes cenários
for i in range(5):
    print(f"\\n--- Ciclo {i+1} ---")
    
    for sensor in ["temperatura", "umidade"]:
        if sensor in monitor.sensores:
            valor = monitor.ler_sensor_com_retry(sensor)
            print(f"🌡️ {sensor}: {valor}")

print("\\n📊 EXECUTANDO MONITORAMENTO CONTÍNUO:")
# Executar monitoramento por alguns segundos
monitor.monitoramento_continuo(duracao_segundos=3)

# Gerar relatório final
monitor.relatorio_status()

print("\\n🎉 Sistema de Monitoramento funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Exceções customizadas hierárquicas")
print("  • Context managers para controle de recursos")
print("  • Try/except/finally com diferentes tipos de exceção")
print("  • Retry automático com backoff")
print("  • Logging estruturado de erros")
print("  • Sistema de alertas por nível")
print("  • Métricas de performance e saúde")
print("  • Tratamento robusto de falhas")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de monitoramento robusto criado!")
        print("🎯 Aplicação real: IoT, servidores, sistemas críticos, DevOps")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_16", "Sistema de Monitoramento Robusto", 80)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_17(self) -> None:
        """Mini Projeto - Módulo 17: Framework de Plugins Modular"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: FRAMEWORK DE PLUGINS MODULAR")
        print("🔌 Sistema extensível de plugins com carregamento dinâmico!")
        print("🛠️ Usando: Imports Dinâmicos, Módulos, Packages, Introspection")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🔌 FRAMEWORK DE PLUGINS MODULAR
# Sistema completo de plugins com carregamento dinâmico

import os
import sys
import importlib
import inspect
from abc import ABC, abstractmethod
from typing import Dict, List, Type, Any, Optional
from pathlib import Path
import json
from datetime import datetime

# Interface base para plugins
class PluginBase(ABC):
    """Interface base que todos os plugins devem implementar"""
    
    @property
    @abstractmethod
    def nome(self) -> str:
        """Nome do plugin"""
        pass
    
    @property
    @abstractmethod  
    def versao(self) -> str:
        """Versão do plugin"""
        pass
    
    @property
    @abstractmethod
    def descricao(self) -> str:
        """Descrição do plugin"""
        pass
    
    @abstractmethod
    def inicializar(self) -> bool:
        """Inicializa o plugin"""
        pass
    
    @abstractmethod
    def executar(self, **kwargs) -> Any:
        """Executa funcionalidade principal do plugin"""
        pass
    
    @abstractmethod
    def finalizar(self) -> None:
        """Finaliza e limpa recursos do plugin"""
        pass
    
    def dependencias(self) -> List[str]:
        """Lista de dependências opcionais"""
        return []
    
    def configuracao_padrao(self) -> Dict[str, Any]:
        """Configuração padrão do plugin"""
        return {}

# Decorador para registro automático de plugins
def plugin(nome: str, versao: str = "1.0", descricao: str = ""):
    """Decorador para registrar plugins automaticamente"""
    def decorador(cls):
        cls._plugin_nome = nome
        cls._plugin_versao = versao 
        cls._plugin_descricao = descricao
        return cls
    return decorador

class GerenciadorPlugins:
    """Gerenciador central de plugins"""
    
    def __init__(self, diretorio_plugins: str = "plugins"):
        self.diretorio_plugins = Path(diretorio_plugins)
        self.plugins_carregados: Dict[str, PluginBase] = {}
        self.plugins_disponiveis: Dict[str, Dict] = {}
        self.configuracoes: Dict[str, Dict] = {}
        self.hooks: Dict[str, List] = {}
        
        # Criar diretório se não existir
        self.diretorio_plugins.mkdir(exist_ok=True)
        
        # Criar __init__.py no diretório de plugins
        init_file = self.diretorio_plugins / "__init__.py"
        if not init_file.exists():
            init_file.write_text("# Diretório de plugins\\n")
    
    def descobrir_plugins(self) -> Dict[str, Dict]:
        """Descobre todos os plugins disponíveis no diretório"""
        plugins_encontrados = {}
        
        print("🔍 Descobrindo plugins...")
        
        # Adicionar diretório de plugins ao path
        if str(self.diretorio_plugins.parent) not in sys.path:
            sys.path.insert(0, str(self.diretorio_plugins.parent))
        
        # Procurar arquivos .py no diretório de plugins
        for arquivo_py in self.diretorio_plugins.glob("*.py"):
            if arquivo_py.name.startswith("__"):
                continue
                
            nome_modulo = f"{self.diretorio_plugins.name}.{arquivo_py.stem}"
            
            try:
                # Importar módulo dinamicamente
                modulo = importlib.import_module(nome_modulo)
                
                # Procurar classes que herdam de PluginBase
                for nome, obj in inspect.getmembers(modulo, inspect.isclass):
                    if (issubclass(obj, PluginBase) and 
                        obj != PluginBase and 
                        not inspect.isabstract(obj)):
                        
                        # Criar instância temporária para obter informações
                        try:
                            instancia_temp = obj()
                            
                            plugin_info = {
                                "nome": instancia_temp.nome,
                                "versao": instancia_temp.versao,
                                "descricao": instancia_temp.descricao,
                                "classe": obj,
                                "modulo": nome_modulo,
                                "arquivo": str(arquivo_py),
                                "dependencias": instancia_temp.dependencias()
                            }
                            
                            plugins_encontrados[instancia_temp.nome] = plugin_info
                            print(f"  ✅ Encontrado: {instancia_temp.nome} v{instancia_temp.versao}")
                            
                        except Exception as e:
                            print(f"  ❌ Erro ao instanciar {nome}: {e}")
                            
            except Exception as e:
                print(f"  ❌ Erro ao importar {arquivo_py.name}: {e}")
        
        self.plugins_disponiveis = plugins_encontrados
        return plugins_encontrados
    
    def carregar_plugin(self, nome_plugin: str) -> bool:
        """Carrega um plugin específico"""
        if nome_plugin in self.plugins_carregados:
            print(f"⚠️ Plugin '{nome_plugin}' já está carregado")
            return True
        
        if nome_plugin not in self.plugins_disponiveis:
            print(f"❌ Plugin '{nome_plugin}' não encontrado")
            return False
        
        plugin_info = self.plugins_disponiveis[nome_plugin]
        
        try:
            print(f"🔄 Carregando plugin: {nome_plugin}")
            
            # Verificar dependências
            for dep in plugin_info["dependencias"]:
                if dep not in self.plugins_carregados:
                    print(f"📦 Carregando dependência: {dep}")
                    if not self.carregar_plugin(dep):
                        print(f"❌ Falha ao carregar dependência: {dep}")
                        return False
            
            # Instanciar plugin
            classe_plugin = plugin_info["classe"]
            instancia = classe_plugin()
            
            # Carregar configuração se existir
            config = self.configuracoes.get(nome_plugin, instancia.configuracao_padrao())
            
            # Inicializar plugin
            if instancia.inicializar():
                self.plugins_carregados[nome_plugin] = instancia
                print(f"✅ Plugin '{nome_plugin}' carregado com sucesso")
                
                # Disparar hooks de carregamento
                self._disparar_hook("plugin_carregado", nome_plugin, instancia)
                
                return True
            else:
                print(f"❌ Falha na inicialização do plugin '{nome_plugin}'")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao carregar plugin '{nome_plugin}': {e}")
            return False
    
    def descarregar_plugin(self, nome_plugin: str) -> bool:
        """Descarrega um plugin"""
        if nome_plugin not in self.plugins_carregados:
            print(f"⚠️ Plugin '{nome_plugin}' não está carregado")
            return False
        
        try:
            plugin = self.plugins_carregados[nome_plugin]
            plugin.finalizar()
            
            del self.plugins_carregados[nome_plugin]
            print(f"✅ Plugin '{nome_plugin}' descarregado")
            
            # Disparar hooks de descarregamento
            self._disparar_hook("plugin_descarregado", nome_plugin)
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao descarregar plugin '{nome_plugin}': {e}")
            return False
    
    def executar_plugin(self, nome_plugin: str, **kwargs) -> Any:
        """Executa um plugin carregado"""
        if nome_plugin not in self.plugins_carregados:
            raise ValueError(f"Plugin '{nome_plugin}' não está carregado")
        
        plugin = self.plugins_carregados[nome_plugin]
        
        try:
            print(f"▶️ Executando plugin: {nome_plugin}")
            resultado = plugin.executar(**kwargs)
            print(f"✅ Plugin '{nome_plugin}' executado com sucesso")
            return resultado
            
        except Exception as e:
            print(f"❌ Erro na execução do plugin '{nome_plugin}': {e}")
            raise
    
    def registrar_hook(self, evento: str, callback):
        """Registra callback para evento do sistema"""
        if evento not in self.hooks:
            self.hooks[evento] = []
        self.hooks[evento].append(callback)
    
    def _disparar_hook(self, evento: str, *args, **kwargs):
        """Dispara hooks registrados para um evento"""
        if evento in self.hooks:
            for callback in self.hooks[evento]:
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    print(f"⚠️ Erro em hook {evento}: {e}")
    
    def listar_plugins(self):
        """Lista todos os plugins disponíveis e carregados"""
        print(f"\\n{'='*60}")
        print("📋 PLUGINS DISPONÍVEIS")
        print(f"{'='*60}")
        
        if not self.plugins_disponiveis:
            print("📭 Nenhum plugin encontrado")
            return
        
        for nome, info in self.plugins_disponiveis.items():
            status = "🟢 CARREGADO" if nome in self.plugins_carregados else "⚪ DISPONÍVEL"
            
            print(f"\\n{status} {nome} v{info['versao']}")
            print(f"  📝 {info['descricao']}")
            print(f"  📁 {info['arquivo']}")
            
            if info['dependencias']:
                deps = ", ".join(info['dependencias'])
                print(f"  📦 Dependências: {deps}")
    
    def salvar_configuracoes(self, arquivo: str = "plugin_config.json"):
        """Salva configurações dos plugins"""
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(self.configuracoes, f, indent=2, ensure_ascii=False)
            print(f"✅ Configurações salvas em {arquivo}")
        except Exception as e:
            print(f"❌ Erro ao salvar configurações: {e}")
    
    def carregar_configuracoes(self, arquivo: str = "plugin_config.json"):
        """Carrega configurações dos plugins"""
        try:
            if os.path.exists(arquivo):
                with open(arquivo, 'r', encoding='utf-8') as f:
                    self.configuracoes = json.load(f)
                print(f"✅ Configurações carregadas de {arquivo}")
        except Exception as e:
            print(f"❌ Erro ao carregar configurações: {e}")

# ===============================================
# PLUGINS DE EXEMPLO
# ===============================================

# Vamos criar alguns plugins de exemplo diretamente aqui
# (normalmente estariam em arquivos separados)

@plugin("calculadora", "1.0", "Plugin de calculadora básica")
class CalculadoraPlugin(PluginBase):
    @property
    def nome(self) -> str:
        return "calculadora"
    
    @property
    def versao(self) -> str:
        return "1.0"
    
    @property
    def descricao(self) -> str:
        return "Plugin de calculadora básica"
    
    def inicializar(self) -> bool:
        print("🧮 Calculadora inicializada")
        return True
    
    def executar(self, **kwargs) -> Any:
        operacao = kwargs.get('operacao', 'soma')
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        
        if operacao == 'soma':
            resultado = a + b
        elif operacao == 'subtracao':
            resultado = a - b
        elif operacao == 'multiplicacao':
            resultado = a * b
        elif operacao == 'divisao':
            resultado = a / b if b != 0 else None
        else:
            resultado = None
        
        print(f"🧮 {a} {operacao} {b} = {resultado}")
        return resultado
    
    def finalizar(self) -> None:
        print("🧮 Calculadora finalizada")

@plugin("gerador_texto", "1.2", "Gerador de texto lorem ipsum")
class GeradorTextoPlugin(PluginBase):
    @property
    def nome(self) -> str:
        return "gerador_texto"
    
    @property
    def versao(self) -> str:
        return "1.2"
    
    @property
    def descricao(self) -> str:
        return "Gerador de texto lorem ipsum"
    
    def inicializar(self) -> bool:
        self.palavras = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
            "adipiscing", "elit", "sed", "do", "eiusmod", "tempor",
            "incididunt", "ut", "labore", "et", "dolore", "magna"
        ]
        print("📝 Gerador de texto inicializado")
        return True
    
    def executar(self, **kwargs) -> Any:
        num_palavras = kwargs.get('palavras', 10)
        
        import random
        texto = " ".join(random.choices(self.palavras, k=num_palavras))
        
        print(f"📝 Texto gerado ({num_palavras} palavras): {texto}")
        return texto
    
    def finalizar(self) -> None:
        print("📝 Gerador de texto finalizado")

@plugin("formatador", "2.0", "Plugin de formatação de dados")
class FormatadorPlugin(PluginBase):
    @property
    def nome(self) -> str:
        return "formatador"
    
    @property
    def versao(self) -> str:
        return "2.0"
    
    @property
    def descricao(self) -> str:
        return "Plugin de formatação de dados"
    
    def dependencias(self) -> List[str]:
        return ["gerador_texto"]  # Depende do gerador de texto
    
    def inicializar(self) -> bool:
        print("🎨 Formatador inicializado")
        return True
    
    def executar(self, **kwargs) -> Any:
        texto = kwargs.get('texto', '')
        formato = kwargs.get('formato', 'maiusculo')
        
        if formato == 'maiusculo':
            resultado = texto.upper()
        elif formato == 'minusculo':
            resultado = texto.lower()
        elif formato == 'titulo':
            resultado = texto.title()
        elif formato == 'capitalizado':
            resultado = texto.capitalize()
        else:
            resultado = texto
        
        print(f"🎨 Texto formatado ({formato}): {resultado}")
        return resultado
    
    def finalizar(self) -> None:
        print("🎨 Formatador finalizado")

# DEMONSTRAÇÃO DO FRAMEWORK
print("=== FRAMEWORK DE PLUGINS MODULAR ===\\n")

# Criar gerenciador
gerenciador = GerenciadorPlugins()

# Registrar plugins manualmente (simulando descoberta de arquivos)
gerenciador.plugins_disponiveis = {
    "calculadora": {
        "nome": "calculadora",
        "versao": "1.0",
        "descricao": "Plugin de calculadora básica",
        "classe": CalculadoraPlugin,
        "modulo": "calculadora",
        "arquivo": "calculadora.py",
        "dependencias": []
    },
    "gerador_texto": {
        "nome": "gerador_texto", 
        "versao": "1.2",
        "descricao": "Gerador de texto lorem ipsum",
        "classe": GeradorTextoPlugin,
        "modulo": "gerador_texto",
        "arquivo": "gerador_texto.py", 
        "dependencias": []
    },
    "formatador": {
        "nome": "formatador",
        "versao": "2.0", 
        "descricao": "Plugin de formatação de dados",
        "classe": FormatadorPlugin,
        "modulo": "formatador",
        "arquivo": "formatador.py",
        "dependencias": ["gerador_texto"]
    }
}

print("📋 PLUGINS DESCOBERTOS:")
gerenciador.listar_plugins()

print("\\n🔌 CARREGANDO PLUGINS:")
gerenciador.carregar_plugin("calculadora")
gerenciador.carregar_plugin("formatador")  # Vai carregar gerador_texto automaticamente

print("\\n▶️ TESTANDO PLUGINS:")

# Testar calculadora
print("\\n--- Testando Calculadora ---")
gerenciador.executar_plugin("calculadora", operacao="soma", a=10, b=5)
gerenciador.executar_plugin("calculadora", operacao="multiplicacao", a=7, b=8)

# Testar gerador de texto
print("\\n--- Testando Gerador de Texto ---")
texto = gerenciador.executar_plugin("gerador_texto", palavras=8)

# Testar formatador (que usa o texto gerado)
print("\\n--- Testando Formatador ---")
gerenciador.executar_plugin("formatador", texto=texto, formato="maiusculo")
gerenciador.executar_plugin("formatador", texto=texto, formato="titulo")

print("\\n📊 STATUS FINAL:")
gerenciador.listar_plugins()

print(f"\\n🔌 Plugins carregados: {len(gerenciador.plugins_carregados)}")
for nome in gerenciador.plugins_carregados.keys():
    print(f"  ✅ {nome}")

print("\\n🎉 Framework de Plugins funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Importação dinâmica de módulos")
print("  • Abstract Base Classes (ABC)")
print("  • Introspecção de classes e objetos")
print("  • Sistema de hooks e eventos")
print("  • Gerenciamento de dependências")
print("  • Configuração flexível via JSON")
print("  • Decoradores para registro automático")
print("  • Arquitetura extensível e modular")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Framework de plugins modular criado!")
        print("🎯 Aplicação real: sistemas extensíveis, editores, IDEs, frameworks")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_17", "Framework de Plugins Modular", 80)
        
        self.utils.pausar()

    def _mini_projeto_modulo_18(self) -> None:
        """Mini Projeto - Módulo 18: Sistema de Gestão de Funcionários (OOP)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE GESTÃO DE FUNCIONÁRIOS")
        print("👥 Sistema completo usando Programação Orientada a Objetos!")
        print("🛠️ Usando: Classes, Objetos, Métodos, Atributos, Encapsulamento")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 👥 SISTEMA DE GESTÃO DE FUNCIONÁRIOS
# Sistema completo de RH usando OOP

from datetime import datetime, date
from typing import List, Optional, Dict
import json

class Pessoa:
    """Classe base para representar uma pessoa"""
    
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email: str):
        self.__nome = nome  # Atributo privado
        self.__cpf = cpf
        self.__data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self.__email = email
    
    # Getters (métodos de acesso)
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento
    
    @property
    def email(self) -> str:
        return self.__email
    
    # Setters (métodos de modificação)
    @email.setter
    def email(self, novo_email: str):
        if "@" in novo_email and "." in novo_email:
            self.__email = novo_email
        else:
            raise ValueError("Email inválido")
    
    def calcular_idade(self) -> int:
        """Calcula idade da pessoa"""
        hoje = date.today()
        return hoje.year - self.__data_nascimento.year - (
            (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day)
        )
    
    def __str__(self) -> str:
        return f"{self.__nome} ({self.calcular_idade()} anos)"

class Funcionario(Pessoa):
    """Classe que representa um funcionário da empresa"""
    
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email: str,
                 cargo: str, salario: float, departamento: str):
        super().__init__(nome, cpf, data_nascimento, email)
        self.__cargo = cargo
        self.__salario = salario
        self.__departamento = departamento
        self.__data_admissao = date.today()
        self.__ativo = True
        self.__historico_salarios: List[Dict] = []
        
        # Registra salário inicial
        self.__historico_salarios.append({
            "data": self.__data_admissao.isoformat(),
            "salario": salario,
            "motivo": "Admissão"
        })
    
    @property
    def cargo(self) -> str:
        return self.__cargo
    
    @property
    def salario(self) -> float:
        return self.__salario
    
    @property
    def departamento(self) -> str:
        return self.__departamento
    
    @property
    def data_admissao(self) -> date:
        return self.__data_admissao
    
    @property
    def ativo(self) -> bool:
        return self.__ativo
    
    def promover(self, novo_cargo: str, novo_salario: float):
        """Promove funcionário para novo cargo"""
        self.__historico_salarios.append({
            "data": date.today().isoformat(),
            "salario": novo_salario,
            "motivo": f"Promoção para {novo_cargo}"
        })
        
        print(f"🎉 {self.nome} promovido de {self.__cargo} para {novo_cargo}")
        print(f"💰 Novo salário: R$ {novo_salario:,.2f}")
        
        self.__cargo = novo_cargo
        self.__salario = novo_salario
    
    def ajustar_salario(self, novo_salario: float, motivo: str = "Ajuste"):
        """Ajusta salário do funcionário"""
        diferenca = novo_salario - self.__salario
        percentual = (diferenca / self.__salario) * 100
        
        self.__historico_salarios.append({
            "data": date.today().isoformat(),
            "salario": novo_salario,
            "motivo": motivo
        })
        
        print(f"💰 Salário de {self.nome} ajustado:")
        print(f"   De: R$ {self.__salario:,.2f}")
        print(f"   Para: R$ {novo_salario:,.2f}")
        print(f"   Variação: {percentual:+.1f}%")
        
        self.__salario = novo_salario
    
    def demitir(self, motivo: str = "Demissão"):
        """Demite funcionário"""
        self.__ativo = False
        print(f"❌ {self.nome} foi demitido. Motivo: {motivo}")
    
    def calcular_tempo_empresa(self) -> int:
        """Calcula tempo de empresa em dias"""
        return (date.today() - self.__data_admissao).days
    
    def get_historico_salarios(self) -> List[Dict]:
        """Retorna histórico de salários"""
        return self.__historico_salarios.copy()
    
    def to_dict(self) -> Dict:
        """Converte funcionário para dicionário"""
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento.isoformat(),
            "email": self.email,
            "cargo": self.__cargo,
            "salario": self.__salario,
            "departamento": self.__departamento,
            "data_admissao": self.__data_admissao.isoformat(),
            "ativo": self.__ativo,
            "historico_salarios": self.__historico_salarios
        }
    
    def __str__(self) -> str:
        status = "Ativo" if self.__ativo else "Inativo"
        return f"{super().__str__()} - {self.__cargo} ({self.__departamento}) - {status}"

class GestorRH:
    """Classe para gerenciar funcionários"""
    
    def __init__(self):
        self.__funcionarios: Dict[str, Funcionario] = {}
        self.__contador_id = 1
    
    def contratar_funcionario(self, nome: str, cpf: str, data_nascimento: str,
                            email: str, cargo: str, salario: float, 
                            departamento: str) -> str:
        """Contrata novo funcionário"""
        
        # Verifica se CPF já existe
        for func in self.__funcionarios.values():
            if func.cpf == cpf:
                raise ValueError(f"CPF {cpf} já cadastrado!")
        
        # Cria funcionário
        funcionario = Funcionario(nome, cpf, data_nascimento, email, 
                                cargo, salario, departamento)
        
        # Gera ID único
        func_id = f"FUNC{self.__contador_id:04d}"
        self.__contador_id += 1
        
        # Adiciona ao sistema
        self.__funcionarios[func_id] = funcionario
        
        print(f"✅ Funcionário {nome} contratado com ID: {func_id}")
        return func_id
    
    def buscar_funcionario(self, identificador: str) -> Optional[Funcionario]:
        """Busca funcionário por ID ou nome"""
        # Busca por ID
        if identificador in self.__funcionarios:
            return self.__funcionarios[identificador]
        
        # Busca por nome
        for funcionario in self.__funcionarios.values():
            if funcionario.nome.lower() == identificador.lower():
                return funcionario
        
        return None
    
    def listar_funcionarios(self, apenas_ativos: bool = True) -> List[Funcionario]:
        """Lista funcionários"""
        funcionarios = list(self.__funcionarios.values())
        
        if apenas_ativos:
            funcionarios = [f for f in funcionarios if f.ativo]
        
        return funcionarios
    
    def funcionarios_por_departamento(self, departamento: str) -> List[Funcionario]:
        """Lista funcionários de um departamento"""
        return [f for f in self.__funcionarios.values() 
                if f.departamento.lower() == departamento.lower() and f.ativo]
    
    def relatorio_folha_pagamento(self) -> Dict:
        """Gera relatório da folha de pagamento"""
        funcionarios_ativos = self.listar_funcionarios(True)
        
        total_salarios = sum(f.salario for f in funcionarios_ativos)
        
        por_departamento = {}
        for func in funcionarios_ativos:
            dept = func.departamento
            if dept not in por_departamento:
                por_departamento[dept] = {"funcionarios": 0, "total": 0}
            
            por_departamento[dept]["funcionarios"] += 1
            por_departamento[dept]["total"] += func.salario
        
        return {
            "total_funcionarios": len(funcionarios_ativos),
            "total_folha": total_salarios,
            "media_salarial": total_salarios / len(funcionarios_ativos) if funcionarios_ativos else 0,
            "por_departamento": por_departamento
        }
    
    def salvar_dados(self, arquivo: str = "funcionarios.json"):
        """Salva dados dos funcionários"""
        dados = {
            "funcionarios": {
                func_id: func.to_dict() 
                for func_id, func in self.__funcionarios.items()
            },
            "contador_id": self.__contador_id
        }
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Dados salvos em {arquivo}")

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE GESTÃO DE FUNCIONÁRIOS ===")
print()

# Criando gestor RH
rh = GestorRH()

# Contratando funcionários
print("👥 CONTRATANDO FUNCIONÁRIOS:")
rh.contratar_funcionario(
    "Ana Silva", "123.456.789-01", "15/03/1990", 
    "ana@empresa.com", "Desenvolvedora", 8000.0, "TI"
)

rh.contratar_funcionario(
    "João Santos", "987.654.321-00", "22/07/1985",
    "joao@empresa.com", "Gerente", 12000.0, "TI"
)

rh.contratar_funcionario(
    "Maria Costa", "456.789.123-45", "10/11/1992",
    "maria@empresa.com", "Analista", 6000.0, "Financeiro"
)

print()

# Listando funcionários
print("📋 FUNCIONÁRIOS ATIVOS:")
for func in rh.listar_funcionarios():
    print(f"  • {func}")

print()

# Promovendo funcionário
print("🎉 PROMOÇÕES:")
ana = rh.buscar_funcionario("Ana Silva")
if ana:
    ana.promover("Desenvolvedora Sênior", 10000.0)

print()

# Relatório da folha
print("💰 RELATÓRIO DA FOLHA:")
relatorio = rh.relatorio_folha_pagamento()
print(f"Total de funcionários: {relatorio['total_funcionarios']}")
print(f"Total da folha: R$ {relatorio['total_folha']:,.2f}")
print(f"Média salarial: R$ {relatorio['media_salarial']:,.2f}")

print()
print("📊 POR DEPARTAMENTO:")
for dept, dados in relatorio['por_departamento'].items():
    print(f"  {dept}: {dados['funcionarios']} funcionários - R$ {dados['total']:,.2f}")

# Salvando dados
rh.salvar_dados()

print()
print("✅ Sistema de Gestão de Funcionários implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Classes e objetos")
print("  • Encapsulamento (atributos privados)")
print("  • Properties (getters/setters)")
print("  • Métodos de instância")
print("  • Composição de classes")
print("  • Persistência de dados")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Gestão de Funcionários criado!")
        print("🎯 Aplicação real: RH, sistemas corporativos, gestão empresarial")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_18", "Sistema de Gestão de Funcionários", 75)
        
        self.utils.pausar()

    def _mini_projeto_modulo_19(self) -> None:
        """Mini Projeto - Módulo 19: Sistema de Jogos RPG (Herança e Polimorfismo)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE JOGOS RPG")
        print("⚔️ Sistema de RPG usando Herança e Polimorfismo!")
        print("🛠️ Usando: Herança, Polimorfismo, Classes Abstratas, Super()")
        
        self.utils.pausar()
        
        codigo_projeto = '''# ⚔️ SISTEMA DE JOGOS RPG
# Sistema completo usando Herança e Polimorfismo

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from enum import Enum
import random

class TipoElemento(Enum):
    FOGO = "fogo"
    AGUA = "agua"
    TERRA = "terra"
    AR = "ar"
    NEUTRO = "neutro"

class Personagem(ABC):
    """Classe abstrata base para todos os personagens"""
    
    def __init__(self, nome: str, vida: int, mana: int, forca: int, defesa: int):
        self._nome = nome
        self._vida_maxima = vida
        self._vida_atual = vida
        self._mana_maxima = mana
        self._mana_atual = mana
        self._forca = forca
        self._defesa = defesa
        self._nivel = 1
        self._experiencia = 0
        self._vivo = True
    
    # Properties
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def vida_atual(self) -> int:
        return self._vida_atual
    
    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima
    
    @property
    def vivo(self) -> bool:
        return self._vivo and self._vida_atual > 0
    
    @property
    def nivel(self) -> int:
        return self._nivel
    
    # Métodos abstratos - devem ser implementados pelas subclasses
    @abstractmethod
    def atacar(self, alvo: 'Personagem') -> int:
        """Método abstrato para atacar"""
        pass
    
    @abstractmethod
    def habilidade_especial(self, alvo: 'Personagem') -> str:
        """Método abstrato para habilidade especial"""
        pass
    
    @abstractmethod
    def get_tipo(self) -> str:
        """Retorna o tipo do personagem"""
        pass
    
    # Métodos concretos
    def receber_dano(self, dano: int) -> int:
        """Recebe dano considerando defesa"""
        dano_real = max(1, dano - self._defesa)
        self._vida_atual = max(0, self._vida_atual - dano_real)
        
        if self._vida_atual <= 0:
            self._vivo = False
            print(f"💀 {self._nome} foi derrotado!")
        
        return dano_real
    
    def curar(self, quantidade: int):
        """Cura o personagem"""
        cura_real = min(quantidade, self._vida_maxima - self._vida_atual)
        self._vida_atual += cura_real
        print(f"💚 {self._nome} recuperou {cura_real} pontos de vida!")
        return cura_real
    
    def ganhar_experiencia(self, xp: int):
        """Ganha experiência e pode subir de nível"""
        self._experiencia += xp
        print(f"⭐ {self._nome} ganhou {xp} XP!")
        
        # Verifica se subiu de nível
        xp_necessario = self._nivel * 100
        if self._experiencia >= xp_necessario:
            self._subir_nivel()
    
    def _subir_nivel(self):
        """Sobe de nível"""
        self._nivel += 1
        self._experiencia = 0
        
        # Aumenta atributos
        self._vida_maxima += 20
        self._vida_atual = self._vida_maxima  # Cura completa
        self._mana_maxima += 10
        self._mana_atual = self._mana_maxima
        self._forca += 5
        self._defesa += 3
        
        print(f"🎉 {self._nome} subiu para o nível {self._nivel}!")
        print(f"   Vida: {self._vida_maxima}, Força: {self._forca}, Defesa: {self._defesa}")
    
    def __str__(self) -> str:
        status = "Vivo" if self.vivo else "Morto"
        return f"{self._nome} (Nv.{self._nivel}) - {self._vida_atual}/{self._vida_maxima} HP - {status}"

class Guerreiro(Personagem):
    """Classe Guerreiro - especialista em combate corpo a corpo"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=120, mana=30, forca=25, defesa=20)
        self._ira = 0  # Atributo especial
    
    def atacar(self, alvo: Personagem) -> int:
        """Ataque básico do guerreiro"""
        dano_base = self._forca + random.randint(5, 15)
        
        # Bônus de ira
        if self._ira > 0:
            dano_base += self._ira * 2
            print(f"🔥 {self._nome} ataca com fúria! (+{self._ira * 2} dano)")
            self._ira = max(0, self._ira - 1)
        
        print(f"⚔️ {self._nome} ataca {alvo.nome} causando {dano_base} de dano!")
        return alvo.receber_dano(dano_base)
    
    def habilidade_especial(self, alvo: Personagem) -> str:
        """Golpe Devastador - ataque poderoso"""
        if self._mana_atual < 15:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 15
        dano = self._forca * 2 + random.randint(10, 20)
        self._ira += 2  # Ganha ira
        
        print(f"💥 {self._nome} usa GOLPE DEVASTADOR!")
        alvo.receber_dano(dano)
        return f"Dano causado: {dano}"
    
    def get_tipo(self) -> str:
        return "Guerreiro"

class Mago(Personagem):
    """Classe Mago - especialista em magia"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=80, mana=100, forca=15, defesa=10)
        self._elemento = random.choice(list(TipoElemento))
    
    def atacar(self, alvo: Personagem) -> int:
        """Míssil mágico"""
        if self._mana_atual < 5:
            # Ataque físico fraco se não tem mana
            dano = self._forca + random.randint(1, 5)
            print(f"🔮 {self._nome} ataca com cajado causando {dano} de dano!")
        else:
            self._mana_atual -= 5
            dano = self._forca + 10 + random.randint(5, 15)
            print(f"✨ {self._nome} lança míssil mágico de {self._elemento.value} causando {dano} de dano!")
        
        return alvo.receber_dano(dano)
    
    def habilidade_especial(self, alvo: Personagem) -> str:
        """Explosão Elemental"""
        if self._mana_atual < 25:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 25
        dano = 30 + random.randint(15, 25)
        
        print(f"🌟 {self._nome} conjura EXPLOSÃO DE {self._elemento.value.upper()}!")
        alvo.receber_dano(dano)
        
        # Chance de efeito adicional
        if random.random() < 0.3:
            if self._elemento == TipoElemento.FOGO:
                dano_extra = 10
                print(f"🔥 {alvo.nome} está queimando! (+{dano_extra} dano)")
                alvo.receber_dano(dano_extra)
            elif self._elemento == TipoElemento.AGUA:
                print(f"💧 {self._nome} recupera 15 pontos de mana!")
                self._mana_atual = min(self._mana_maxima, self._mana_atual + 15)
        
        return f"Dano causado: {dano}"
    
    def get_tipo(self) -> str:
        return f"Mago ({self._elemento.value})"

class Ladino(Personagem):
    """Classe Ladino - especialista em velocidade e furtividade"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=90, mana=50, forca=20, defesa=15)
        self._furtivo = False
    
    def atacar(self, alvo: Personagem) -> int:
        """Ataque rápido"""
        dano_base = self._forca + random.randint(8, 12)
        
        # Bônus se estiver furtivo
        if self._furtivo:
            dano_base *= 2
            self._furtivo = False
            print(f"🗡️ {self._nome} ataca pelas costas! DANO CRÍTICO!")
        else:
            print(f"🗡️ {self._nome} ataca rapidamente {alvo.nome}!")
        
        print(f"   Dano causado: {dano_base}")
        return alvo.receber_dano(dano_base)
    
    def habilidade_especial(self, alvo: Personagem) -> str:
        """Fica invisível para próximo ataque"""
        if self._mana_atual < 20:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 20
        self._furtivo = True
        
        print(f"👻 {self._nome} entra em modo FURTIVO!")
        print("   Próximo ataque causará dano crítico!")
        return "Modo furtivo ativado"
    
    def get_tipo(self) -> str:
        return "Ladino"

class Curandeiro(Personagem):
    """Classe Curandeiro - especialista em cura e suporte"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=100, mana=80, forca=12, defesa=18)
    
    def atacar(self, alvo: Personagem) -> int:
        """Ataque com luz sagrada"""
        if self._mana_atual >= 8:
            self._mana_atual -= 8
            dano = self._forca + 8 + random.randint(3, 10)
            print(f"✨ {self._nome} ataca com luz sagrada causando {dano} de dano!")
        else:
            dano = self._forca + random.randint(1, 6)
            print(f"🔨 {self._nome} ataca com cajado causando {dano} de dano!")
        
        return alvo.receber_dano(dano)
    
    def habilidade_especial(self, alvo: Personagem) -> str:
        """Cura Divina"""
        if self._mana_atual < 20:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 20
        cura = 40 + random.randint(10, 20)
        
        print(f"✨ {self._nome} conjura CURA DIVINA!")
        if alvo == self:
            self.curar(cura)
            return f"Auto-cura: {cura} HP"
        else:
            alvo.curar(cura)
            return f"Curou {alvo.nome}: {cura} HP"
    
    def get_tipo(self) -> str:
        return "Curandeiro"

class SistemaCombate:
    """Sistema de combate do jogo"""
    
    @staticmethod
    def combate_turno(atacante: Personagem, defensor: Personagem):
        """Executa um turno de combate"""
        if not atacante.vivo:
            return
        
        print(f"\n--- Turno de {atacante.nome} ---")
        print(f"Status: {atacante}")
        print(f"Alvo: {defensor}")
        
        # Decide ação (70% ataque normal, 30% habilidade especial)
        if random.random() < 0.7 or atacante._mana_atual < 15:
            atacante.atacar(defensor)
        else:
            result = atacante.habilidade_especial(defensor)
            print(f"Resultado: {result}")
        
        # Pequena pausa para leitura
        import time
        time.sleep(0.5)
    
    @staticmethod
    def batalha_completa(personagem1: Personagem, personagem2: Personagem) -> Personagem:
        """Executa uma batalha completa"""
        print(f"\n⚔️ BATALHA: {personagem1.nome} vs {personagem2.nome}")
        print("=" * 50)
        
        turno = 0
        while personagem1.vivo and personagem2.vivo and turno < 20:
            turno += 1
            print(f"\n🎲 TURNO {turno}")
            
            # Turno do personagem 1
            if personagem1.vivo:
                SistemaCombate.combate_turno(personagem1, personagem2)
            
            # Turno do personagem 2
            if personagem2.vivo:
                SistemaCombate.combate_turno(personagem2, personagem1)
        
        # Determina vencedor
        if personagem1.vivo and not personagem2.vivo:
            vencedor = personagem1
            print(f"\n🏆 {vencedor.nome} venceu a batalha!")
            vencedor.ganhar_experiencia(50)
        elif personagem2.vivo and not personagem1.vivo:
            vencedor = personagem2
            print(f"\n🏆 {vencedor.nome} venceu a batalha!")
            vencedor.ganhar_experiencia(50)
        else:
            print("\n🤝 Batalha terminou em empate!")
            return None
        
        return vencedor

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE JOGOS RPG ===")
print()

# Criando personagens de diferentes classes
print("👥 CRIANDO HERÓIS:")
herois = [
    Guerreiro("Conan"),
    Mago("Gandalf"),
    Ladino("Robin"),
    Curandeiro("Zelda")
]

for heroi in herois:
    print(f"  ✅ {heroi.get_tipo()}: {heroi}")

print()

# Demonstração de polimorfismo
print("🎭 DEMONSTRAÇÃO DE POLIMORFISMO:")
print("(Cada classe implementa atacar() de forma diferente)")
print()

for heroi in herois:
    print(f"--- {heroi.nome} ({heroi.get_tipo()}) ---")
    # Todos têm o método atacar, mas comportamentos diferentes
    dummy_target = Guerreiro("Dummy")
    dummy_target._vida_atual = 1000  # Para não morrer
    heroi.atacar(dummy_target)
    print()

# Batalha épica
print("⚔️ BATALHA ÉPICA:")
guerreiro = herois[0]  # Conan
mago = herois[1]       # Gandalf

vencedor = SistemaCombate.batalha_completa(guerreiro, mago)

print()
print("✅ Sistema de RPG implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Herança (Personagem -> Guerreiro, Mago, etc.)")
print("  • Polimorfismo (mesmo método, comportamentos diferentes)")
print("  • Classes abstratas (ABC)")
print("  • Métodos abstratos (@abstractmethod)")
print("  • Super() para chamar métodos da classe pai")
print("  • Enums para constantes")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de RPG criado!")
        print("🎯 Aplicação real: jogos, simulações, sistemas com hierarquias")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_19", "Sistema de Jogos RPG", 90)
        
        self.utils.pausar()

    def _mini_projeto_modulo_20(self) -> None:
        """Mini Projeto - Módulo 20: Sistema de Cache Inteligente (Decorators)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE CACHE INTELIGENTE")
        print("⚡ Sistema de cache com decorators e context managers!")
        print("🛠️ Usando: Decorators, Context Managers, Functools, Time")
        
        self.utils.pausar()
        
        codigo_projeto = '''# ⚡ SISTEMA DE CACHE INTELIGENTE
# Sistema completo de cache usando decorators e context managers

import time
import functools
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Any, Callable, Optional
from contextlib import contextmanager
import threading

class CacheStats:
    """Estatísticas do cache"""
    
    def __init__(self):
        self.hits = 0          # Acertos
        self.misses = 0        # Perdas
        self.evictions = 0     # Remoções
        self.total_requests = 0
        self._lock = threading.Lock()
    
    def hit(self):
        with self._lock:
            self.hits += 1
            self.total_requests += 1
    
    def miss(self):
        with self._lock:
            self.misses += 1
            self.total_requests += 1
    
    def evict(self):
        with self._lock:
            self.evictions += 1
    
    @property
    def hit_ratio(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return self.hits / self.total_requests
    
    def __str__(self):
        return f"Cache Stats: {self.hits} hits, {self.misses} misses, {self.hit_ratio:.2%} ratio"

class TimedCache:
    """Cache com expiração por tempo"""
    
    def __init__(self, default_ttl: int = 300, max_size: int = 100):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl  # Time to live em segundos
        self.max_size = max_size
        self.stats = CacheStats()
        self._lock = threading.Lock()
    
    def _is_expired(self, entry: Dict[str, Any]) -> bool:
        """Verifica se entrada expirou"""
        return datetime.now() > entry['expires_at']
    
    def _evict_expired(self):
        """Remove entradas expiradas"""
        expired_keys = []
        for key, entry in self.cache.items():
            if self._is_expired(entry):
                expired_keys.append(key)
        
        for key in expired_keys:
            del self.cache[key]
            self.stats.evict()
    
    def _evict_lru(self):
        """Remove entrada menos recentemente usada"""
        if not self.cache:
            return
        
        # Encontra entrada mais antiga
        oldest_key = min(self.cache.keys(), 
                        key=lambda k: self.cache[k]['last_accessed'])
        
        del self.cache[oldest_key]
        self.stats.evict()
    
    def get(self, key: str) -> Optional[Any]:
        """Obtém valor do cache"""
        with self._lock:
            if key not in self.cache:
                self.stats.miss()
                return None
            
            entry = self.cache[key]
            
            # Verifica se expirou
            if self._is_expired(entry):
                del self.cache[key]
                self.stats.miss()
                self.stats.evict()
                return None
            
            # Atualiza último acesso
            entry['last_accessed'] = datetime.now()
            entry['access_count'] += 1
            self.stats.hit()
            
            return entry['value']
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Define valor no cache"""
        with self._lock:
            # Limpa expirados primeiro
            self._evict_expired()
            
            # Se chegou no limite, remove LRU
            if len(self.cache) >= self.max_size and key not in self.cache:
                self._evict_lru()
            
            # Calcula expiração
            ttl = ttl or self.default_ttl
            expires_at = datetime.now() + timedelta(seconds=ttl)
            
            # Armazena entrada
            self.cache[key] = {
                'value': value,
                'created_at': datetime.now(),
                'last_accessed': datetime.now(),
                'expires_at': expires_at,
                'access_count': 0,
                'ttl': ttl
            }
    
    def delete(self, key: str) -> bool:
        """Remove entrada do cache"""
        with self._lock:
            if key in self.cache:
                del self.cache[key]
                return True
            return False
    
    def clear(self):
        """Limpa todo o cache"""
        with self._lock:
            self.cache.clear()
    
    def info(self) -> Dict[str, Any]:
        """Informações do cache"""
        with self._lock:
            self._evict_expired()
            
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'stats': self.stats,
                'entries': [
                    {
                        'key': key,
                        'created_at': entry['created_at'].isoformat(),
                        'expires_at': entry['expires_at'].isoformat(),
                        'access_count': entry['access_count'],
                        'ttl': entry['ttl']
                    }
                    for key, entry in self.cache.items()
                ]
            }

# Cache global
_global_cache = TimedCache()

def cached(ttl: int = 300, key_func: Optional[Callable] = None):
    """
    Decorator para cache automático de funções
    
    Args:
        ttl: Tempo de vida em segundos
        key_func: Função personalizada para gerar chave
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Gera chave do cache
            if key_func:
                cache_key = key_func(*args, **kwargs)
            else:
                # Chave padrão: nome_função + argumentos
                args_str = str(args) + str(sorted(kwargs.items()))
                cache_key = f"{func.__name__}_{hash(args_str)}"
            
            # Tenta buscar no cache
            cached_result = _global_cache.get(cache_key)
            if cached_result is not None:
                print(f"📦 Cache HIT para {func.__name__}")
                return cached_result
            
            # Cache miss - executa função
            print(f"⚡ Cache MISS para {func.__name__} - executando...")
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            print(f"⏱️ Função executada em {execution_time:.3f}s")
            
            # Armazena no cache
            _global_cache.set(cache_key, result, ttl)
            
            return result
        
        # Adiciona métodos úteis ao wrapper
        wrapper.cache_clear = lambda: _global_cache.clear()
        wrapper.cache_info = lambda: _global_cache.info()
        wrapper.cache_stats = lambda: _global_cache.stats
        
        return wrapper
    return decorator

def timed_execution(func: Callable) -> Callable:
    """Decorator para medir tempo de execução"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        
        print(f"⏱️ {func.__name__} executado em {execution_time:.3f}s")
        return result
    return wrapper

def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator para retry automático"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"❌ Tentativa {attempt + 1} falhou: {e}")
                        print(f"🔄 Tentando novamente em {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"💥 Todas as {max_attempts} tentativas falharam!")
            
            raise last_exception
        return wrapper
    return decorator

@contextmanager
def cache_context(cache_name: str = "temp"):
    """Context manager para cache temporário"""
    temp_cache = TimedCache(default_ttl=60, max_size=50)
    
    print(f"🚀 Iniciando cache temporário '{cache_name}'")
    try:
        yield temp_cache
    finally:
        info = temp_cache.info()
        print(f"📊 Cache '{cache_name}' finalizado:")
        print(f"   Entradas criadas: {len(info['entries'])}")
        print(f"   {info['stats']}")
        temp_cache.clear()

# DEMONSTRAÇÃO DO SISTEMA

# Funções de exemplo para teste
@cached(ttl=10)  # Cache por 10 segundos
@timed_execution
def operacao_lenta(n: int) -> int:
    """Simula operação que demora para executar"""
    print(f"💻 Processando operação pesada com n={n}...")
    time.sleep(2)  # Simula processamento
    return n ** 2 + n * 10

@cached(ttl=5, key_func=lambda x, y: f"soma_{x}_{y}")
def soma_complexa(x: int, y: int) -> int:
    """Soma com processamento 'complexo'"""
    print(f"🧮 Calculando soma complexa de {x} + {y}...")
    time.sleep(1)
    return x + y + (x * y) // 2

@retry(max_attempts=3, delay=0.5)
@cached(ttl=15)
def operacao_instavel(success_rate: float = 0.3) -> str:
    """Operação que pode falhar"""
    import random
    if random.random() > success_rate:
        raise Exception("Operação falhou!")
    
    time.sleep(0.5)
    return f"Sucesso! Rate: {success_rate}"

print("=== SISTEMA DE CACHE INTELIGENTE ===")
print()

# Teste de cache básico
print("🧪 TESTE 1: Cache básico")
print("Primeira chamada (cache miss):")
resultado1 = operacao_lenta(5)
print(f"Resultado: {resultado1}")

print("\\nSegunda chamada (cache hit):")
resultado2 = operacao_lenta(5)
print(f"Resultado: {resultado2}")

print(f"\\nVerificação: {resultado1 == resultado2}")

print()

# Teste com diferentes parâmetros
print("🧪 TESTE 2: Cache com parâmetros diferentes")
resultado3 = soma_complexa(3, 7)
resultado4 = soma_complexa(5, 2)
resultado5 = soma_complexa(3, 7)  # Deve usar cache

print()

# Teste de retry
print("🧪 TESTE 3: Sistema de retry")
try:
    resultado_instavel = operacao_instavel(0.7)  # 70% chance de sucesso
    print(f"Resultado: {resultado_instavel}")
except Exception as e:
    print(f"Falha final: {e}")

print()

# Context manager de cache
print("🧪 TESTE 4: Context manager")
with cache_context("teste_temporario") as temp_cache:
    temp_cache.set("chave1", "valor1", 30)
    temp_cache.set("chave2", "valor2", 60)
    
    print(f"Valor 1: {temp_cache.get('chave1')}")
    print(f"Valor 2: {temp_cache.get('chave2')}")

print()

# Estatísticas do cache
print("📊 ESTATÍSTICAS DO CACHE:")
stats = operacao_lenta.cache_stats()
print(f"  {stats}")

info = operacao_lenta.cache_info()
print(f"  Entradas no cache: {info['size']}/{info['max_size']}")

print()

# Teste de expiração
print("🧪 TESTE 5: Expiração de cache")
print("Aguardando expiração do cache (10s)...")
# Em um caso real, aguardaríamos, mas aqui vamos simular
_global_cache.clear()  # Simula expiração
print("Cache expirado. Nova chamada:")
resultado_apos_expiracao = operacao_lenta(5)

print()
print("✅ Sistema de Cache Inteligente implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Decorators personalizados")
print("  • Context managers")
print("  • Functools.wraps")
print("  • Threading locks")
print("  • Estratégias de cache (LRU, TTL)")
print("  • Retry patterns")
print("  • Medição de performance")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Cache Inteligente criado!")
        print("🎯 Aplicação real: otimização de performance, sistemas web, APIs")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_20", "Sistema de Cache Inteligente", 90)
        
        self.utils.pausar()

    def _mini_projeto_modulo_21(self) -> None:
        """Mini Projeto - Módulo 21: Pipeline de Processamento de Dados (Generators)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS")
        print("🔄 Pipeline eficiente usando Generators e Iterators!")
        print("🛠️ Usando: Generators, Yield, Iterator Protocol, Memory Efficiency")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🔄 PIPELINE DE PROCESSAMENTO DE DADOS
# Sistema completo usando generators para eficiência de memória

import csv
import json
import time
import os
from typing import Iterator, Generator, Dict, Any, List, Optional, Callable
from datetime import datetime
from itertools import islice, chain, groupby
import random

class DataGenerator:
    """Gerador de dados sintéticos para demonstração"""
    
    @staticmethod
    def generate_sales_data(num_records: int = 1000) -> Generator[Dict[str, Any], None, None]:
        """Gera dados de vendas sintéticos"""
        print(f"📊 Gerando {num_records} registros de vendas...")
        
        produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam", "Fone"]
        vendedores = ["Ana", "João", "Maria", "Carlos", "Paula"]
        regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
        
        for i in range(num_records):
            # Simula processamento gradual
            if i % 100 == 0:
                print(f"   Gerado {i}/{num_records} registros...")
            
            yield {
                "id": f"V{i+1:06d}",
                "produto": random.choice(produtos),
                "vendedor": random.choice(vendedores),
                "regiao": random.choice(regioes),
                "quantidade": random.randint(1, 10),
                "preco_unitario": round(random.uniform(50.0, 1000.0), 2),
                "data": datetime.now().strftime("%Y-%m-%d"),
                "timestamp": int(time.time()) + i
            }
    
    @staticmethod
    def read_csv_lazy(filename: str) -> Generator[Dict[str, str], None, None]:
        """Lê CSV de forma lazy (linha por linha)"""
        print(f"📖 Lendo arquivo {filename} de forma lazy...")
        
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row_num, row in enumerate(reader, 1):
                if row_num % 1000 == 0:
                    print(f"   Processado linha {row_num}")
                yield row

class DataTransformer:
    """Transformadores de dados usando generators"""
    
    @staticmethod
    def filter_data(data_stream: Iterator[Dict], condition: Callable[[Dict], bool]) -> Generator[Dict, None, None]:
        """Filtra dados baseado em condição"""
        for record in data_stream:
            if condition(record):
                yield record
    
    @staticmethod
    def transform_data(data_stream: Iterator[Dict], transformer: Callable[[Dict], Dict]) -> Generator[Dict, None, None]:
        """Transforma cada registro"""
        for record in data_stream:
            yield transformer(record)
    
    @staticmethod
    def add_calculated_fields(data_stream: Iterator[Dict]) -> Generator[Dict, None, None]:
        """Adiciona campos calculados"""
        for record in data_stream:
            # Calcula total da venda
            if 'quantidade' in record and 'preco_unitario' in record:
                quantidade = float(record['quantidade'])
                preco = float(record['preco_unitario'])
                record['total'] = round(quantidade * preco, 2)
                
                # Categoria de venda
                if record['total'] > 500:
                    record['categoria'] = "Alto Valor"
                elif record['total'] > 200:
                    record['categoria'] = "Médio Valor"
                else:
                    record['categoria'] = "Baixo Valor"
            
            yield record
    
    @staticmethod
    def aggregate_by_key(data_stream: Iterator[Dict], key: str) -> Generator[Dict, None, None]:
        """Agrega dados por chave"""
        # Agrupa dados por chave
        grouped_data = {}
        
        for record in data_stream:
            group_key = record.get(key, "Sem categoria")
            
            if group_key not in grouped_data:
                grouped_data[group_key] = {
                    'grupo': group_key,
                    'quantidade': 0,
                    'total_vendas': 0.0,
                    'contagem': 0
                }
            
            group = grouped_data[group_key]
            group['contagem'] += 1
            
            if 'quantidade' in record:
                group['quantidade'] += int(record['quantidade'])
            if 'total' in record:
                group['total_vendas'] += float(record['total'])
        
        # Retorna agregados
        for group_data in grouped_data.values():
            if group_data['contagem'] > 0:
                group_data['media_venda'] = round(
                    group_data['total_vendas'] / group_data['contagem'], 2
                )
            yield group_data

class DataPipeline:
    """Pipeline de processamento de dados"""
    
    def __init__(self):
        self.steps: List[Callable] = []
        self.metrics = {
            'records_processed': 0,
            'records_filtered': 0,
            'processing_time': 0,
            'memory_efficiency': True
        }
    
    def add_step(self, step_func: Callable, description: str = ""):
        """Adiciona etapa ao pipeline"""
        self.steps.append((step_func, description))
        return self
    
    def process(self, data_source: Iterator[Dict]) -> Generator[Dict, None, None]:
        """Executa pipeline completo"""
        print("🔄 Iniciando pipeline de processamento...")
        start_time = time.time()
        
        current_stream = data_source
        
        # Aplica cada etapa do pipeline
        for i, (step_func, description) in enumerate(self.steps, 1):
            print(f"   Etapa {i}: {description or step_func.__name__}")
            current_stream = step_func(current_stream)
        
        # Processa e conta registros
        for record in current_stream:
            self.metrics['records_processed'] += 1
            
            # Log de progresso
            if self.metrics['records_processed'] % 100 == 0:
                print(f"   Processados {self.metrics['records_processed']} registros...")
            
            yield record
        
        # Finaliza métricas
        self.metrics['processing_time'] = time.time() - start_time
        print(f"✅ Pipeline finalizado: {self.metrics['records_processed']} registros em {self.metrics['processing_time']:.2f}s")

class DataSink:
    """Destinos para dados processados"""
    
    @staticmethod
    def to_json_file(data_stream: Iterator[Dict], filename: str) -> int:
        """Salva dados em arquivo JSON"""
        print(f"💾 Salvando dados em {filename}...")
        
        records = []
        count = 0
        
        for record in data_stream:
            records.append(record)
            count += 1
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
        
        print(f"✅ {count} registros salvos em {filename}")
        return count
    
    @staticmethod
    def to_csv_file(data_stream: Iterator[Dict], filename: str) -> int:
        """Salva dados em arquivo CSV"""
        print(f"📄 Salvando dados em {filename}...")
        
        count = 0
        fieldnames = None
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = None
            
            for record in data_stream:
                # Inicializa writer com fieldnames do primeiro registro
                if writer is None:
                    fieldnames = list(record.keys())
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                
                writer.writerow(record)
                count += 1
        
        print(f"✅ {count} registros salvos em {filename}")
        return count
    
    @staticmethod
    def to_memory_summary(data_stream: Iterator[Dict]) -> Dict[str, Any]:
        """Gera resumo dos dados na memória"""
        print("📊 Gerando resumo dos dados...")
        
        summary = {
            'total_records': 0,
            'unique_values': {},
            'numeric_stats': {},
            'sample_records': []
        }
        
        # Processa stream uma única vez
        for record in data_stream:
            summary['total_records'] += 1
            
            # Amostra dos primeiros 5 registros
            if len(summary['sample_records']) < 5:
                summary['sample_records'].append(record)
            
            # Contadores de valores únicos
            for key, value in record.items():
                if key not in summary['unique_values']:
                    summary['unique_values'][key] = set()
                summary['unique_values'][key].add(str(value))
        
        # Converte sets para contagens
        for key, value_set in summary['unique_values'].items():
            summary['unique_values'][key] = len(value_set)
        
        return summary

# DEMONSTRAÇÃO PRÁTICA

print("=== PIPELINE DE PROCESSAMENTO DE DADOS ===")
print()

# 1. Geração de dados sintéticos
print("🎯 ETAPA 1: Geração de dados")
dados_vendas = DataGenerator.generate_sales_data(500)

# 2. Criação do pipeline
print("\\n🔧 ETAPA 2: Construção do pipeline")
pipeline = DataPipeline()

# Adiciona etapas ao pipeline
pipeline.add_step(
    lambda stream: DataTransformer.filter_data(
        stream, 
        lambda record: float(record['preco_unitario']) > 100
    ),
    "Filtrar produtos com preço > R$ 100"
).add_step(
    DataTransformer.add_calculated_fields,
    "Adicionar campos calculados (total, categoria)"
).add_step(
    lambda stream: DataTransformer.filter_data(
        stream,
        lambda record: record['categoria'] in ['Alto Valor', 'Médio Valor']
    ),
    "Filtrar apenas vendas de valor médio/alto"
)

# 3. Processamento do pipeline
print("\\n⚡ ETAPA 3: Processamento")
dados_processados = pipeline.process(dados_vendas)

# 4. Agregação
print("\\n📊 ETAPA 4: Agregação por vendedor")
dados_agregados = DataTransformer.aggregate_by_key(dados_processados, 'vendedor')

# 5. Salvamento
print("\\n💾 ETAPA 5: Salvamento")
summary = DataSink.to_memory_summary(dados_agregados)

print("\\n📋 RESUMO DOS DADOS PROCESSADOS:")
print(f"Total de registros: {summary['total_records']}")
print(f"Campos únicos: {list(summary['unique_values'].keys())}")

print("\\n🔍 AMOSTRA DE DADOS:")
for i, record in enumerate(summary['sample_records'], 1):
    print(f"  Registro {i}: {record}")

# Exemplo de generator mais avançado
def fibonacci_generator(max_value: int) -> Generator[int, None, None]:
    """Gerador de números Fibonacci"""
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

print("\\n🧮 BONUS: Gerador Fibonacci")
fib_numbers = list(islice(fibonacci_generator(100), 10))
print(f"Primeiros 10 números Fibonacci até 100: {fib_numbers}")

# Pipeline de processamento de texto
def word_frequency_pipeline(text: str) -> Generator[tuple, None, None]:
    """Pipeline para análise de frequência de palavras"""
    # Tokenização
    words = (word.lower().strip('.,!?;:"()[]') for word in text.split())
    
    # Filtragem
    valid_words = (word for word in words if len(word) > 2 and word.isalpha())
    
    # Contagem (usando sorted + groupby)
    sorted_words = sorted(valid_words)
    for word, group in groupby(sorted_words):
        count = len(list(group))
        yield (word, count)

print("\\n📝 BONUS: Análise de texto")
texto_exemplo = "Python é uma linguagem de programação. Python é fácil de aprender. Programação em Python é divertida."
palavra_freq = list(word_frequency_pipeline(texto_exemplo))
print("Frequência de palavras:")
for palavra, freq in sorted(palavra_freq, key=lambda x: x[1], reverse=True)[:5]:
    print(f"  '{palavra}': {freq}")

print()
print("✅ Pipeline de Processamento de Dados implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Generators para eficiência de memória")
print("  • Yield statements")
print("  • Iterator protocol")
print("  • Pipeline pattern")
print("  • Lazy evaluation")
print("  • Stream processing")
print("  • Memory-efficient data processing")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Pipeline de Processamento criado!")
        print("🎯 Aplicação real: big data, ETL, processamento de streams")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_21", "Pipeline de Processamento de Dados", 95)
        
        self.utils.pausar()

    def _mini_projeto_modulo_22(self) -> None:
        """Mini Projeto - Módulo 22: Analisador de Logs (Regex)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: ANALISADOR DE LOGS AVANÇADO")
        print("🔍 Sistema completo de análise de logs usando Regex!")
        print("🛠️ Usando: Regex Patterns, Groups, Lookahead, Compilação")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🔍 ANALISADOR DE LOGS AVANÇADO
# Sistema completo de análise usando expressões regulares

import re
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Iterator
from collections import defaultdict, Counter
import time

class LogPattern:
    """Padrões de regex para diferentes tipos de logs"""
    
    # Padrões comuns
    IP_ADDRESS = r'\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b'
    TIMESTAMP_APACHE = r'\\[([^\\]]+)\\]'
    TIMESTAMP_SYSLOG = r'(\\w{3}\\s+\\d{1,2}\\s+\\d{2}:\\d{2}:\\d{2})'
    EMAIL = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    URL = r'https?://[^\\s<>"\\[\\]{}|\\\\^`]+'
    
    # Log específicos
    APACHE_ACCESS = re.compile(
        r'(?P<ip>' + IP_ADDRESS + r')\\s+'
        r'(?P<user>\\S+)\\s+'
        r'(?P<userid>\\S+)\\s+'
        r'\\[(?P<timestamp>[^\\]]+)\\]\\s+'
        r'"(?P<method>\\w+)\\s+(?P<path>\\S+)\\s+(?P<protocol>[^"]+)"\\s+'
        r'(?P<status>\\d{3})\\s+'
        r'(?P<size>\\d+|-)\\s+'
        r'"(?P<referer>[^"]*)"\\s+'
        r'"(?P<user_agent>[^"]*)"'
    )
    
    NGINX_ERROR = re.compile(
        r'(?P<timestamp>\\d{4}/\\d{2}/\\d{2}\\s+\\d{2}:\\d{2}:\\d{2})\\s+'
        r'\\[(?P<level>\\w+)\\]\\s+'
        r'(?P<pid>\\d+)#(?P<tid>\\d+):\\s+'
        r'(?P<message>.*)'
    )
    
    SYSLOG = re.compile(
        r'(?P<timestamp>\\w{3}\\s+\\d{1,2}\\s+\\d{2}:\\d{2}:\\d{2})\\s+'
        r'(?P<hostname>\\S+)\\s+'
        r'(?P<process>\\w+)(?:\\[(?P<pid>\\d+)\\])?:\\s+'
        r'(?P<message>.*)'
    )
    
    # Padrões de segurança
    SQL_INJECTION = re.compile(
        r'(?i)(union|select|insert|update|delete|drop|create|alter)\\s.*(?:;|--|#|\\/\\*)',
        re.IGNORECASE
    )
    
    XSS_ATTEMPT = re.compile(
        r'(?i)<script[^>]*>.*?</script>|javascript:|on\\w+\\s*=',
        re.IGNORECASE
    )
    
    BRUTE_FORCE = re.compile(
        r'(?i)(failed|invalid|incorrect).*(?:login|password|authentication)',
        re.IGNORECASE
    )

class LogEntry:
    """Representa uma entrada de log processada"""
    
    def __init__(self, raw_line: str, parsed_data: Dict, log_type: str):
        self.raw_line = raw_line
        self.parsed_data = parsed_data
        self.log_type = log_type
        self.timestamp = self._parse_timestamp()
        self.security_flags = self._check_security()
    
    def _parse_timestamp(self) -> Optional[datetime]:
        """Tenta parsear timestamp da entrada"""
        timestamp_str = self.parsed_data.get('timestamp', '')
        
        # Formatos comuns de timestamp
        formats = [
            '%d/%b/%Y:%H:%M:%S %z',      # Apache
            '%Y/%m/%d %H:%M:%S',         # Nginx
            '%b %d %H:%M:%S',            # Syslog
            '%Y-%m-%d %H:%M:%S',         # ISO
        ]
        
        for fmt in formats:
            try:
                if fmt == '%b %d %H:%M:%S':
                    # Syslog não tem ano, assume ano atual
                    dt = datetime.strptime(timestamp_str, fmt)
                    dt = dt.replace(year=datetime.now().year)
                    return dt
                else:
                    return datetime.strptime(timestamp_str.split()[0], fmt)
            except ValueError:
                continue
        
        return None
    
    def _check_security(self) -> List[str]:
        """Verifica indicadores de segurança"""
        flags = []
        text = self.raw_line.lower()
        
        if LogPattern.SQL_INJECTION.search(self.raw_line):
            flags.append('SQL_INJECTION')
        
        if LogPattern.XSS_ATTEMPT.search(self.raw_line):
            flags.append('XSS_ATTEMPT')
        
        if LogPattern.BRUTE_FORCE.search(self.raw_line):
            flags.append('BRUTE_FORCE')
        
        # Verifica status HTTP suspeitos
        status = self.parsed_data.get('status', '')
        if status in ['404', '403', '500', '502', '503']:
            flags.append(f'HTTP_{status}')
        
        # Verifica IPs suspeitos (múltiplos requests)
        ip = self.parsed_data.get('ip', '')
        if ip and self._is_suspicious_ip(ip):
            flags.append('SUSPICIOUS_IP')
        
        return flags
    
    def _is_suspicious_ip(self, ip: str) -> bool:
        """Verifica se IP é suspeito (simplificado)"""
        # Lista simples de IPs suspeitos para demo
        suspicious_ips = ['192.168.1.100', '10.0.0.1']
        return ip in suspicious_ips
    
    def to_dict(self) -> Dict:
        """Converte para dicionário"""
        return {
            'raw_line': self.raw_line,
            'parsed_data': self.parsed_data,
            'log_type': self.log_type,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'security_flags': self.security_flags
        }

class LogAnalyzer:
    """Analisador principal de logs"""
    
    def __init__(self):
        self.entries: List[LogEntry] = []
        self.stats = {
            'total_lines': 0,
            'parsed_lines': 0,
            'error_lines': 0,
            'security_incidents': 0
        }
    
    def parse_line(self, line: str) -> Optional[LogEntry]:
        """Analisa uma linha de log"""
        line = line.strip()
        if not line:
            return None
        
        self.stats['total_lines'] += 1
        
        # Tenta diferentes padrões
        patterns = [
            ('apache_access', LogPattern.APACHE_ACCESS),
            ('nginx_error', LogPattern.NGINX_ERROR),
            ('syslog', LogPattern.SYSLOG)
        ]
        
        for log_type, pattern in patterns:
            match = pattern.match(line)
            if match:
                self.stats['parsed_lines'] += 1
                entry = LogEntry(line, match.groupdict(), log_type)
                
                if entry.security_flags:
                    self.stats['security_incidents'] += 1
                
                return entry
        
        # Linha não reconhecida
        self.stats['error_lines'] += 1
        return LogEntry(line, {'message': line}, 'unknown')
    
    def analyze_file(self, filename: str):
        """Analisa arquivo de log completo"""
        print(f"📖 Analisando arquivo: {filename}")
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    entry = self.parse_line(line)
                    if entry:
                        self.entries.append(entry)
                    
                    if line_num % 1000 == 0:
                        print(f"   Processadas {line_num} linhas...")
        
        except FileNotFoundError:
            print(f"❌ Arquivo {filename} não encontrado")
        except Exception as e:
            print(f"❌ Erro ao processar arquivo: {e}")
    
    def analyze_text(self, log_text: str):
        """Analisa texto de log"""
        print("📝 Analisando texto de log...")
        
        lines = log_text.strip().split('\\n')
        for line in lines:
            entry = self.parse_line(line)
            if entry:
                self.entries.append(entry)
    
    def get_statistics(self) -> Dict:
        """Gera estatísticas do log"""
        if not self.entries:
            return {}
        
        # Contadores básicos
        log_types = Counter(entry.log_type for entry in self.entries)
        status_codes = Counter(
            entry.parsed_data.get('status', 'N/A') 
            for entry in self.entries
        )
        
        # IPs mais frequentes
        ips = Counter(
            entry.parsed_data.get('ip', 'N/A')
            for entry in self.entries
            if entry.parsed_data.get('ip')
        )
        
        # Incidentes de segurança
        security_incidents = defaultdict(int)
        for entry in self.entries:
            for flag in entry.security_flags:
                security_incidents[flag] += 1
        
        # Análise temporal
        timestamps = [entry.timestamp for entry in self.entries if entry.timestamp]
        time_range = None
        if timestamps:
            time_range = {
                'start': min(timestamps).isoformat(),
                'end': max(timestamps).isoformat(),
                'duration_hours': (max(timestamps) - min(timestamps)).total_seconds() / 3600
            }
        
        return {
            'summary': dict(self.stats),
            'log_types': dict(log_types),
            'status_codes': dict(status_codes.most_common(10)),
            'top_ips': dict(ips.most_common(10)),
            'security_incidents': dict(security_incidents),
            'time_range': time_range,
            'total_entries': len(self.entries)
        }
    
    def find_patterns(self, pattern: str, flags: int = 0) -> List[Dict]:
        """Busca padrão customizado nos logs"""
        print(f"🔍 Buscando padrão: {pattern}")
        
        compiled_pattern = re.compile(pattern, flags)
        matches = []
        
        for entry in self.entries:
            match = compiled_pattern.search(entry.raw_line)
            if match:
                matches.append({
                    'line': entry.raw_line,
                    'match': match.group(),
                    'groups': match.groups() if match.groups() else [],
                    'timestamp': entry.timestamp.isoformat() if entry.timestamp else None
                })
        
        print(f"   Encontrados {len(matches)} resultados")
        return matches
    
    def detect_anomalies(self) -> Dict[str, List]:
        """Detecta anomalias nos logs"""
        anomalies = {
            'high_error_rate': [],
            'suspicious_ips': [],
            'unusual_patterns': [],
            'time_anomalies': []
        }
        
        # IPs com muitos requests
        ip_counts = Counter(
            entry.parsed_data.get('ip', '')
            for entry in self.entries
            if entry.parsed_data.get('ip')
        )
        
        avg_requests = sum(ip_counts.values()) / len(ip_counts) if ip_counts else 0
        threshold = avg_requests * 3  # 3x a média
        
        for ip, count in ip_counts.items():
            if count > threshold:
                anomalies['suspicious_ips'].append({
                    'ip': ip,
                    'requests': count,
                    'threshold': threshold
                })
        
        # Status codes com alta frequência de erro
        status_counts = Counter(
            entry.parsed_data.get('status', '')
            for entry in self.entries
        )
        
        error_statuses = ['400', '401', '403', '404', '500', '502', '503']
        total_requests = sum(status_counts.values())
        
        for status in error_statuses:
            count = status_counts.get(status, 0)
            if count > 0:
                error_rate = (count / total_requests) * 100
                if error_rate > 10:  # Mais de 10% de erro
                    anomalies['high_error_rate'].append({
                        'status': status,
                        'count': count,
                        'rate': f"{error_rate:.1f}%"
                    })
        
        return anomalies
    
    def generate_report(self) -> str:
        """Gera relatório completo"""
        stats = self.get_statistics()
        anomalies = self.detect_anomalies()
        
        report = f"""
📊 RELATÓRIO DE ANÁLISE DE LOGS
{'='*50}

📈 RESUMO GERAL:
  • Total de linhas: {stats['summary']['total_lines']}
  • Linhas parseadas: {stats['summary']['parsed_lines']}
  • Linhas com erro: {stats['summary']['error_lines']}
  • Incidentes de segurança: {stats['summary']['security_incidents']}

📋 TIPOS DE LOG:
"""
        
        for log_type, count in stats['log_types'].items():
            report += f"  • {log_type}: {count}\\n"
        
        if stats['status_codes']:
            report += "\\n🌐 TOP STATUS CODES:\\n"
            for status, count in stats['status_codes']:
                report += f"  • {status}: {count}\\n"
        
        if stats['top_ips']:
            report += "\\n🌍 TOP IPs:\\n"
            for ip, count in stats['top_ips']:
                report += f"  • {ip}: {count} requests\\n"
        
        if stats['security_incidents']:
            report += "\\n🚨 INCIDENTES DE SEGURANÇA:\\n"
            for incident, count in stats['security_incidents'].items():
                report += f"  • {incident}: {count}\\n"
        
        if anomalies['suspicious_ips']:
            report += "\\n⚠️ IPs SUSPEITOS:\\n"
            for anomaly in anomalies['suspicious_ips']:
                report += f"  • {anomaly['ip']}: {anomaly['requests']} requests\\n"
        
        return report

# DEMONSTRAÇÃO DO SISTEMA

print("=== ANALISADOR DE LOGS AVANÇADO ===")
print()

# Dados de exemplo para demonstração
log_exemplo = """192.168.1.1 - - [1/Jan/2024:10:00:1 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
192.168.1.100 - - [1/Jan/2024:10:00:2 +0000] "POST /login.php HTTP/1.1" 401 512 "-" "BadBot/1.0"  
192.168.1.2 - - [1/Jan/2024:10:00:3 +0000] "GET /admin/config.php HTTP/1.1" 403 256 "-" "Mozilla/5.0"
192.168.1.100 - - [1/Jan/2024:10:00:4 +0000] "GET /index.php?id=1' OR 1=1-- HTTP/1.1" 500 128 "-" "BadBot/1.0"
192.168.1.3 - - [1/Jan/2024:10:00:5 +0000] "GET /search?q=<script>alert('xss')</script> HTTP/1.1" 400 64 "-" "Mozilla/5.0"
192.168.1.100 - - [1/Jan/2024:10:00:6 +0000] "POST /login.php HTTP/1.1" 401 512 "-" "BadBot/1.0"
192.168.1.4 - - [1/Jan/2024:10:00:7 +0000] "GET /products/laptops HTTP/1.1" 200 2048 "-" "Mozilla/5.0"
192.168.1.100 - - [1/Jan/2024:10:00:8 +0000] "POST /login.php HTTP/1.1" 401 512 "-" "BadBot/1.0" """

# Criando analisador
analyzer = LogAnalyzer()

# Analisando logs
print("🔍 Analisando logs de exemplo...")
analyzer.analyze_text(log_exemplo)

print(f"✅ Processadas {len(analyzer.entries)} entradas")

# Estatísticas
print("\\n📊 ESTATÍSTICAS:")
stats = analyzer.get_statistics()

print(f"• Total de entradas: {stats['total_entries']}")
print(f"• Tipos de log: {stats['log_types']}")
print(f"• Incidentes de segurança: {stats['security_incidents']}")

# Busca por padrões específicos
print("\\n🔍 BUSCA POR PADRÕES:")

# Busca por tentativas de SQL Injection
sql_attempts = analyzer.find_patterns(r"SELECT|UNION|OR\\s+\\d+=\\d+", re.IGNORECASE)
print(f"• Tentativas de SQL Injection: {len(sql_attempts)}")

# Busca por IPs específicos
ip_pattern = r'192\\.168\\.1\\.100'
suspicious_ip_logs = analyzer.find_patterns(ip_pattern)
print(f"• Atividade do IP suspeito: {len(suspicious_ip_logs)}")

# Detecta anomalias
print("\\n⚠️ DETECÇÃO DE ANOMALIAS:")
anomalies = analyzer.detect_anomalies()

if anomalies['suspicious_ips']:
    print("IPs suspeitos encontrados:")
    for anomaly in anomalies['suspicious_ips']:
        print(f"  • {anomaly['ip']}: {anomaly['requests']} requests")

if anomalies['high_error_rate']:
    print("Alta taxa de erro:")
    for error in anomalies['high_error_rate']:
        print(f"  • Status {error['status']}: {error['rate']}")

# Demonstração de regex customizado
print("\\n🧪 REGEX CUSTOMIZADO:")

# Extrai URLs de requests
url_pattern = r'"[A-Z]+ ([^"\\s]+) HTTP'
urls = analyzer.find_patterns(url_pattern)
print(f"URLs extraídas: {len(urls)}")
for match in urls[:3]:  # Mostra apenas as 3 primeiras
    print(f"  • {match['groups'][0] if match['groups'] else match['match']}")

# Validação de email (exemplo)
email_pattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
emails = analyzer.find_patterns(email_pattern, re.IGNORECASE)
print(f"\\nEmails encontrados: {len(emails)}")

# Relatório final
print("\\n📋 RELATÓRIO FINAL:")
print(analyzer.generate_report())

print("✅ Analisador de Logs implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Expressões regulares avançadas")
print("  • Grupos e capturas")
print("  • Flags de regex")
print("  • Padrões compilados")
print("  • Lookahead/lookbehind")
print("  • Análise de segurança")
print("  • Detecção de anomalias")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Analisador de Logs criado!")
        print("🎯 Aplicação real: monitoramento, segurança, DevOps, auditoria")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_22", "Analisador de Logs Avançado", 95)
        
        self.utils.pausar()

    def _mini_projeto_modulo_23(self) -> None:
        """Mini Projeto - Módulo 23: Profiler de Performance (Debugging)"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: PROFILER DE PERFORMANCE")
        print("🚀 Sistema completo de profiling e debugging!")
        print("🛠️ Usando: Profiling, Tracing, Memory Analysis, Timing")
        
        self.utils.pausar()
        
        codigo_projeto = '''# 🚀 PROFILER DE PERFORMANCE
# Sistema completo de análise de performance e debugging

import cProfile
import pstats
import tracemalloc
import time
import sys
import functools
import gc
from typing import Dict, List, Any, Callable, Optional
from datetime import datetime
from contextlib import contextmanager
import threading
import psutil
import os

class PerformanceProfiler:
    """Profiler principal de performance"""
    
    def __init__(self):
        self.profilers = {}
        self.memory_snapshots = []
        self.timing_data = {}
        self.call_counts = {}
        self._active_timers = {}
    
    @contextmanager
    def profile_block(self, name: str):
        """Context manager para profilear bloco de código"""
        print(f"🚀 Iniciando profiling: {name}")
        
        # Inicia profiler
        profiler = cProfile.Profile()
        start_time = time.time()
        
        # Snapshot de memória inicial
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        snapshot_start = tracemalloc.take_snapshot()
        
        profiler.enable()
        
        try:
            yield
        finally:
            # Finaliza profiler
            profiler.disable()
            end_time = time.time()
            
            # Snapshot de memória final
            snapshot_end = tracemalloc.take_snapshot()
            
            # Armazena dados
            self.profilers[name] = {
                'profiler': profiler,
                'execution_time': end_time - start_time,
                'memory_start': snapshot_start,
                'memory_end': snapshot_end,
                'timestamp': datetime.now()
            }
            
            print(f"✅ Profiling '{name}' concluído: {end_time - start_time:.3f}s")
    
    def profile_function(self, func: Callable) -> Callable:
        """Decorator para profilear função"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = f"{func.__module__}.{func.__name__}"
            
            with self.profile_block(func_name):
                result = func(*args, **kwargs)
            
            # Conta chamadas
            self.call_counts[func_name] = self.call_counts.get(func_name, 0) + 1
            
            return result
        
        return wrapper
    
    def time_function(self, iterations: int = 1):
        """Decorator para medir tempo de execução"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                times = []
                result = None
                
                for i in range(iterations):
                    start = time.perf_counter()
                    result = func(*args, **kwargs)
                    end = time.perf_counter()
                    times.append(end - start)
                
                func_name = f"{func.__module__}.{func.__name__}"
                self.timing_data[func_name] = {
                    'times': times,
                    'avg_time': sum(times) / len(times),
                    'min_time': min(times),
                    'max_time': max(times),
                    'iterations': iterations
                }
                
                print(f"⏱️ {func_name}: {self.timing_data[func_name]['avg_time']:.6f}s (avg)")
                
                return result
            
            return wrapper
        return decorator
    
    def memory_usage(self, func: Callable) -> Callable:
        """Decorator para monitorar uso de memória"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Força garbage collection antes da medição
            gc.collect()
            
            # Medição inicial
            process = psutil.Process()
            memory_before = process.memory_info().rss / 1024 / 1024  # MB
            
            # Executa função
            result = func(*args, **kwargs)
            
            # Medição final
            gc.collect()
            memory_after = process.memory_info().rss / 1024 / 1024  # MB
            
            func_name = f"{func.__module__}.{func.__name__}"
            memory_diff = memory_after - memory_before
            
            print(f"🧠 {func_name}: {memory_diff:+.2f} MB")
            
            return result
        
        return wrapper
    
    def get_memory_analysis(self, profile_name: str) -> Dict[str, Any]:
        """Analisa uso de memória de um profile"""
        if profile_name not in self.profilers:
            return {}
        
        data = self.profilers[profile_name]
        snapshot_start = data['memory_start']
        snapshot_end = data['memory_end']
        
        # Compara snapshots
        top_stats = snapshot_end.compare_to(snapshot_start, 'lineno')
        
        analysis = {
            'total_memory_diff': sum(stat.size_diff for stat in top_stats),
            'top_memory_users': []
        }
        
        # Top 10 maiores incrementos de memória
        for stat in top_stats[:10]:
            if stat.size_diff > 0:
                analysis['top_memory_users'].append({
                    'file': stat.traceback.format()[0],
                    'size_diff': stat.size_diff,
                    'count_diff': stat.count_diff
                })
        
        return analysis
    
    def get_function_stats(self, profile_name: str, top_n: int = 10) -> List[Dict]:
        """Obtém estatísticas das funções mais custosas"""
        if profile_name not in self.profilers:
            return []
        
        profiler = self.profilers[profile_name]['profiler']
        
        # Cria StringIO para capturar output
        import io
        stream = io.StringIO()
        
        # Gera estatísticas
        stats = pstats.Stats(profiler, stream=stream)
        stats.sort_stats('cumulative')
        
        # Extrai dados das funções
        function_stats = []
        
        for func_name, (cc, nc, tt, ct, callers) in stats.stats.items():
            function_stats.append({
                'function': f"{func_name[0]}:{func_name[1]}({func_name[2]})",
                'calls': nc,
                'total_time': tt,
                'cumulative_time': ct,
                'time_per_call': tt / nc if nc > 0 else 0
            })
        
        # Ordena por tempo cumulativo
        function_stats.sort(key=lambda x: x['cumulative_time'], reverse=True)
        
        return function_stats[:top_n]
    
    def generate_report(self) -> str:
        """Gera relatório completo de performance"""
        report = f"""
🚀 RELATÓRIO DE PERFORMANCE
{'='*50}
Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 RESUMO GERAL:
  • Profiles executados: {len(self.profilers)}
  • Funções cronometradas: {len(self.timing_data)}
  • Total de chamadas: {sum(self.call_counts.values())}

"""
        
        # Relatório por profile
        for name, data in self.profilers.items():
            report += f"\\n🔍 PROFILE: {name}\\n"
            report += f"  • Tempo de execução: {data['execution_time']:.3f}s\\n"
            
            # Top funções
            stats = self.get_function_stats(name, 5)
            if stats:
                report += "  • Top 5 funções mais custosas:\\n"
                for i, stat in enumerate(stats, 1):
                    report += f"    {i}. {stat['function']}: {stat['cumulative_time']:.3f}s\\n"
            
            # Análise de memória
            memory_analysis = self.get_memory_analysis(name)
            if memory_analysis:
                report += f"  • Diferença de memória: {memory_analysis['total_memory_diff']:+} bytes\\n"
        
        # Timing data
        if self.timing_data:
            report += "\\n⏱️ TEMPOS DE EXECUÇÃO:\\n"
            for func_name, timing in self.timing_data.items():
                report += f"  • {func_name}: {timing['avg_time']:.6f}s (média de {timing['iterations']} execuções)\\n"
        
        # Call counts
        if self.call_counts:
            report += "\\n📞 CONTAGEM DE CHAMADAS:\\n"
            sorted_calls = sorted(self.call_counts.items(), key=lambda x: x[1], reverse=True)
            for func_name, count in sorted_calls[:10]:
                report += f"  • {func_name}: {count} chamadas\\n"
        
        return report

class CodeOptimizer:
    """Analisador e otimizador de código"""
    
    @staticmethod
    def compare_implementations(*funcs, iterations: int = 1000, **kwargs):
        """Compara performance de diferentes implementações"""
        print(f"🏁 Comparando {len(funcs)} implementações ({iterations} iterações)")
        
        results = {}
        
        for func in funcs:
            func_name = func.__name__
            times = []
            
            for _ in range(iterations):
                start = time.perf_counter()
                func(**kwargs)
                end = time.perf_counter()
                times.append(end - start)
            
            results[func_name] = {
                'avg_time': sum(times) / len(times),
                'min_time': min(times),
                'max_time': max(times),
                'total_time': sum(times)
            }
        
        # Ordena por tempo médio
        sorted_results = sorted(results.items(), key=lambda x: x[1]['avg_time'])
        
        print("\\n📊 RESULTADOS:")
        for i, (name, stats) in enumerate(sorted_results, 1):
            print(f"{i}. {name}: {stats['avg_time']:.6f}s (média)")
        
        # Calcula speedup
        if len(sorted_results) > 1:
            fastest = sorted_results[0][1]['avg_time']
            print("\\n🚀 SPEEDUP:")
            for name, stats in sorted_results[1:]:
                speedup = stats['avg_time'] / fastest
                print(f"  • {name}: {speedup:.2f}x mais lento")
        
        return results

# FUNÇÕES DE EXEMPLO PARA PROFILING

def bubble_sort(arr):
    """Implementação ineficiente de ordenação"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """Implementação eficiente de ordenação"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def memory_intensive_function():
    """Função que consome muita memória"""
    # Cria listas grandes
    data = []
    for i in range(10000):
        data.append([j for j in range(100)])
    
    # Processa dados
    result = []
    for sublist in data:
        result.append(sum(sublist))
    
    return result

def cpu_intensive_function(n=1000000):
    """Função que consome muito CPU"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# DEMONSTRAÇÃO DO SISTEMA

print("=== PROFILER DE PERFORMANCE ===")
print()

# Criando profiler
profiler = PerformanceProfiler()

# Teste 1: Profiling de bloco
print("🧪 TESTE 1: Profiling de bloco de código")
with profiler.profile_block("ordenacao_bubble"):
    import random
    dados = [random.randint(1, 1000) for _ in range(1000)]
    bubble_sort(dados.copy())

with profiler.profile_block("ordenacao_quick"):
    quick_sort(dados.copy())

print()

# Teste 2: Decorators de profiling
print("🧪 TESTE 2: Decorators de profiling")

@profiler.profile_function
@profiler.memory_usage
def teste_memoria():
    return memory_intensive_function()

@profiler.time_function(iterations=5)
def teste_cpu():
    return cpu_intensive_function(100000)

# Executa testes
teste_memoria()
teste_cpu()

print()

# Teste 3: Comparação de implementações
print("🧪 TESTE 3: Comparação de implementações")

def sort_builtin(data):
    return sorted(data)

def sort_bubble(data):
    return bubble_sort(data.copy())

def sort_quick(data):
    return quick_sort(data.copy())

# Dados para teste
test_data = [random.randint(1, 100) for _ in range(100)]

# Compara implementações
CodeOptimizer.compare_implementations(
    sort_builtin, sort_bubble, sort_quick,
    iterations=100,
    data=test_data
)

print()

# Teste 4: Análise detalhada
print("🧪 TESTE 4: Análise detalhada de performance")

# Função stats do bubble sort
bubble_stats = profiler.get_function_stats("ordenacao_bubble")
if bubble_stats:
    print("Top 3 funções mais custosas (bubble sort):")
    for i, stat in enumerate(bubble_stats[:3], 1):
        print(f"  {i}. {stat['function']}: {stat['cumulative_time']:.3f}s")

print()

# Análise de memória
memory_analysis = profiler.get_memory_analysis("ordenacao_bubble")
if memory_analysis:
    print(f"Diferença de memória (bubble sort): {memory_analysis['total_memory_diff']:+} bytes")

print()

# Relatório final
print("📋 RELATÓRIO FINAL:")
print(profiler.generate_report())

# Dicas de otimização
print("💡 DICAS DE OTIMIZAÇÃO:")
print("  • Use algoritmos eficientes (O(n log n) vs O(n²))")
print("  • Evite loops desnecessários")
print("  • Reutilize objetos quando possível")
print("  • Use generators para grandes datasets")
print("  • Profile regularmente seu código")
print("  • Otimize gargalos identificados")

print()
print("✅ Profiler de Performance implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • cProfile e pstats")
print("  • tracemalloc para análise de memória")
print("  • Decorators de profiling")
print("  • Context managers")
print("  • Análise de performance")
print("  • Comparação de algoritmos")
print("  • Métricas de otimização")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Profiler de Performance criado!")
        print("🎯 Aplicação real: otimização de código, debugging, análise de performance")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_23", "Profiler de Performance", 100)
        
        self.utils.pausar()