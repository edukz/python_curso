#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulos do Curso Interativo de Python
Contém todos os módulos de ensino do curso
"""

try:
    from ..utils import PythonCourseUtils
except ImportError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils import PythonCourseUtils


class CourseModules:
    """Classe que contém todos os módulos do curso"""
    
    def __init__(self):
        self.utils = PythonCourseUtils()

    def modulo_1_introducao(self) -> None:
        """Módulo 1: Introdução ao Python"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 1: INTRODUÇÃO AO PYTHON")
        
        print("🐍 Bem-vindo ao fascinante mundo da programação Python! 🎉")
        print("\n═══════════════════════════════════════════════")
        print("            O QUE É PYTHON?")
        print("═══════════════════════════════════════════════")
        
        print("\nPython é uma linguagem de programação criada por Guido van Rossum")
        print("em 1991. O nome vem do grupo de comédia britânico 'Monty Python'!")
        
        print("\n🌟 Por que Python é especial?")
        print("• 📚 FÁCIL DE APRENDER - Sintaxe simples e intuitiva")
        print("• 🚀 PODEROSA E VERSÁTIL - Resolve problemas complexos")
        print("• 🌍 MUITO POPULAR - Uma das linguagens mais usadas no mundo")
        print("• 🤝 COMUNIDADE ATIVA - Milhões de programadores ajudam uns aos outros")
        
        self.utils.pausar()
        
        print("\n🔧 Onde Python é usado no mundo real?")
        print("• 🤖 INTELIGÊNCIA ARTIFICIAL - Netflix, Tesla, Google")
        print("• 🌐 DESENVOLVIMENTO WEB - Instagram, Spotify, Pinterest")
        print("• 📊 ANÁLISE DE DADOS - NASA, Banco Central, universidades")
        print("• 🎮 JOGOS - Civilization IV, EVE Online")
        print("• 🏢 AUTOMAÇÃO - Dropbox, Reddit, BitTorrent")
        print("• 🧬 CIÊNCIA - Descobertas médicas, pesquisa espacial")
        
        self.utils.pausar()
        
        print("\n🔹 O que é PROGRAMAÇÃO?")
        print("Programar é como dar instruções para um computador, mas de forma")
        print("muito específica e organizada. É como escrever uma receita de bolo:")
        print("")
        print("📝 RECEITA DE BOLO:")
        print("1. Pegue 3 ovos")
        print("2. Misture com farinha")
        print("3. Asse por 30 minutos")
        print("")
        print("💻 PROGRAMA EM PYTHON:")
        print("1. Peça o nome do usuário")
        print("2. Calcule a idade")
        print("3. Mostre uma mensagem personalizada")
        
        self.utils.pausar()
        
        print("\n🧠 Como o computador 'entende' Python?")
        print("O computador só entende 0s e 1s (código binário).")
        print("Python é traduzido para essa linguagem por um 'interpretador'.")
        print("")
        print("VOCÊ ESCREVE: print('Olá!')")
        print("PYTHON TRADUZ: 01001000 01100101 01101100...")
        print("COMPUTADOR EXECUTA: Olá!")
        
        self.utils.pausar()
        
        print("\n🎯 O que você vai aprender neste curso?")
        print("1. 📝 Como 'falar' com o computador")
        print("2. 🗃️  Como guardar e organizar informações")
        print("3. 🤔 Como fazer o programa tomar decisões")
        print("4. 🔄 Como repetir tarefas automaticamente")
        print("5. 📋 Como trabalhar com listas de dados")
        print("6. ⚙️  Como criar suas próprias 'ferramentas'")
        print("7. 🧮 Como construir uma calculadora completa!")
        
        self.utils.pausar()
        
        print("\n💡 CURIOSIDADES SOBRE PYTHON:")
        print("• Python executa aproximadamente 100.000 linhas por segundo!")
        print("• O Instagram processa 95 milhões de fotos por dia usando Python")
        print("• Python ajudou a descobrir ondas gravitacionais no espaço")
        print("• Netflix usa Python para recomendar filmes para você")
        print("• Python pode controlar robôs, drones e até mesmo carros!")
        
        self.utils.exercicio(
            "Em que ano Python foi criado?",
            ["1991", "mil novecentos e noventa e um"],
            "Foi criado no início dos anos 90"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_1()

    def modulo_2_primeiro_programa(self) -> None:
        """Módulo 2: Seu primeiro programa"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 2: SEU PRIMEIRO PROGRAMA")
        
        print("🎉 Chegou a hora de escrever seu PRIMEIRO programa em Python!")
        print("\n═══════════════════════════════════════════════")
        print("        O TRADICIONAL 'OLÁ, MUNDO!'")
        print("═══════════════════════════════════════════════")
        
        print("\n🌍 Por que todo programador começa com 'Olá, Mundo!'?")
        print("Esta é uma tradição que começou em 1978 com o livro")
        print("'The C Programming Language'. É o primeiro programa")
        print("que todo programador escreve em uma nova linguagem!")
        
        self.utils.pausar()
        
        print("\n💻 Vamos ao nosso primeiro código:")
        
        codigo = 'print("Olá, Mundo!")'
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        print("\n🎯 PARABÉNS! Você acabou de executar seu primeiro programa!")
        
        self.utils.pausar()
        
        print("\n🔍 Vamos DISSECAR este código:")
        print("• 'print' - É o NOME da função")
        print("• '('  - Abre os parênteses (início dos parâmetros)")
        print("• '\"'  - Abre as aspas (início do texto)")
        print("• 'Olá, Mundo!' - O TEXTO que queremos exibir")
        print("• '\"'  - Fecha as aspas (fim do texto)")
        print("• ')'  - Fecha os parênteses (fim dos parâmetros)")
        
        self.utils.pausar()
        
        print("\n📚 O que é a função print()?")
        print("• É uma FUNÇÃO BUILT-IN (já vem com Python)")
        print("• Sua única missão: EXIBIR coisas na tela")
        print("• Você pode imprimir textos, números, resultados...")
        print("• É uma das funções mais usadas em Python!")
        
        self.utils.pausar()
        
        print("\n✏️ Vamos experimentar variações:")
        
        # Exemplo 2
        codigo2 = "print('Olá, Mundo!')"
        print("\n🔸 Com aspas simples:")
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        # Exemplo 3
        codigo3 = '''print("Python é incrível!")
print("Estou aprendendo a programar!")'''
        print("\n🔸 Múltiplas linhas:")
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        # Exemplo 4
        codigo4 = 'print("🐍 Python 🐍")'
        print("\n🔸 Com emojis:")
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n❓ ASPAS SIMPLES vs ASPAS DUPLAS")
        print("Em Python, tanto faz usar ' ou \" para textos.")
        print("A regra é: seja CONSISTENTE!")
        print("")
        print("✅ CORRETO:")
        print('   print("Olá!")')
        print("   print('Oi!')")
        print("")
        print("❌ ERRO COMUM:")
        print("   print('Olá\")")  # Misturou aspas!
        
        self.utils.pausar()
        
        print("\n🚨 ERROS COMUNS que iniciantes cometem:")
        print("1. print(Olá)      ❌ - Esqueceu as aspas")
        print("2. Print('Olá')    ❌ - 'P' maiúsculo")
        print("3. print 'Olá'     ❌ - Esqueceu os parênteses")
        print("4. print('Olá'     ❌ - Esqueceu de fechar")
        print("5. print(\"Olá')    ❌ - Misturou tipos de aspas")
        
        self.utils.pausar()
        
        print("\n🔧 DICA PROFISSIONAL:")
        print("Use o print() para 'debugar' seus programas!")
        print("Quando algo não funciona, adicione prints para")
        print("ver o que está acontecendo. É como acender uma")
        print("lanterna no código!")
        
        # Exercícios práticos
        self.utils.exercicio(
            "Qual comando usamos para exibir texto na tela?",
            ["print", "print()", "função print"],
            "É uma função que começa com 'p'"
        )
        
        self.utils.exercicio(
            "O que está ERRADO neste código: Print('Oi')",
            ["P maiúsculo", "maiúsculo", "print deve ser minúsculo"],
            "Python diferencia maiúsculas de minúsculas"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_2()
        
        self.utils.exercicio(
            "Complete o código: _____(\"Olá!\")",
            ["print"],
            "Função para exibir na tela"
        )

    def modulo_3_variaveis(self) -> None:
        """Módulo 3: Variáveis"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 3: VARIÁVEIS - A MEMÓRIA DO SEU PROGRAMA")
        
        print("🗃️ Imagine que variáveis são como CAIXAS ETIQUETADAS")
        print("onde você guarda suas coisas favoritas!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO VARIÁVEIS?")
        print("═══════════════════════════════════════════════")
        
        print("\n🏠 Na vida real:")
        print("📦 CAIXA 'Roupas de Inverno' → Contém casacos e blusas")
        print("📦 CAIXA 'Documentos' → Contém RG, CPF, diplomas")
        print("📦 CAIXA 'Fotos' → Contém suas memórias")
        
        print("\n💻 Em Python:")
        print("📦 VARIÁVEL 'nome' → Contém 'João Silva'")
        print("📦 VARIÁVEL 'idade' → Contém 25")
        print("📦 VARIÁVEL 'salario' → Contém 3500.00")
        
        self.utils.pausar()
        
        print("\n🎯 Vamos criar nossas primeiras variáveis:")
        
        codigo = '''nome = "Python"
idade = 30
print("Linguagem:", nome)
print("Idade:", idade)'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        print("\n🔍 O que aconteceu aqui?")
        print("1. Criamos uma caixa chamada 'nome' e guardamos 'Python'")
        print("2. Criamos uma caixa chamada 'idade' e guardamos 30")
        print("3. Pedimos para mostrar o conteúdo das caixas")
        
        self.utils.pausar()
        
        print("\n⚡ ATRIBUIÇÃO - O sinal '=' é especial!")
        print("• Em matemática: 2 + 2 = 4 (igualdade)")
        print("• Em Python: nome = 'João' (ATRIBUIÇÃO)")
        print("")
        print("🎯 Leia sempre da DIREITA para ESQUERDA:")
        print("   nome = 'João'")
        print("   ↑       ↑")
        print("   |       └─ Valor que vai ser guardado")
        print("   └─ Nome da caixa onde vai ser guardado")
        
        self.utils.pausar()
        
        print("\n📝 Vamos ver mais exemplos práticos:")
        
        # Exemplo mais rico
        codigo2 = '''# Informações de uma pessoa
nome_completo = "Ana Silva Santos"
idade = 28
altura = 1.65
tem_carteira = True

print("=== PERFIL DA PESSOA ===")
print("Nome:", nome_completo)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Tem carteira de motorista:", tem_carteira)'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🔄 Variáveis podem MUDAR de valor:")
        
        codigo3 = '''pontos = 0
print("Pontos iniciais:", pontos)

pontos = 10
print("Depois de ganhar:", pontos)

pontos = 25
print("Depois de ganhar mais:", pontos)'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        print("\n💡 Por isso se chama VARIÁVEL - o valor pode VARIAR!")
        
        self.utils.pausar()
        
        print("\n📋 REGRAS IMPORTANTES para nomes de variáveis:")
        print("") 
        print("✅ PODE usar:")
        print("• Letras (a-z, A-Z)")
        print("• Números (0-9) - mas NÃO no início")
        print("• Underscore (_)")
        print("")
        print("❌ NÃO PODE usar:")
        print("• Espaços em branco")
        print("• Caracteres especiais (@, #, !, etc)")
        print("• Palavras reservadas do Python")
        print("• Começar com números")
        
        self.utils.pausar()
        
        print("\n💯 EXEMPLOS de nomes VÁLIDOS:")
        print("✅ nome")
        print("✅ idade")
        print("✅ nome_completo")
        print("✅ salario2023")
        print("✅ _temperatura")
        print("✅ PI")
        print("")
        print("💥 EXEMPLOS de nomes INVÁLIDOS:")
        print("❌ 2nome (começa com número)")
        print("❌ nome completo (tem espaço)")
        print("❌ salário (tem acento)")
        print("❌ for (palavra reservada)")
        print("❌ nome@ (caractere especial)")
        
        self.utils.pausar()
        
        print("\n🎨 CONVENÇÕES de nomenclatura:")
        print("• snake_case: nome_da_variavel (recomendado em Python)")
        print("• camelCase: nomeDaVariavel (mais usado em outras linguagens)")
        print("• PascalCase: NomeDaVariavel (para classes)")
        print("• CONSTANTES: VALOR_FIXO (para valores que não mudam)")
        
        self.utils.pausar()
        
        print("\n⚠️ PYTHON É CASE-SENSITIVE (diferencia maiúsculas/minúsculas):")
        
        codigo4 = '''nome = "João"
Nome = "Maria"
NOME = "Pedro"

print("nome:", nome)
print("Nome:", Nome)
print("NOME:", NOME)'''
        
        print("São 3 variáveis DIFERENTES!")
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n🧮 Operações com variáveis:")
        
        codigo5 = '''a = 10
b = 5
soma = a + b
produto = a * b

print("a =", a)
print("b =", b)
print("a + b =", soma)
print("a * b =", produto)

# Podemos usar uma variável para criar outra!
dobro_de_a = a * 2
print("Dobro de a:", dobro_de_a)'''
        
        self.utils.exemplo(codigo5)
        self.utils.executar_codigo(codigo5)
        
        self.utils.pausar()
        
        print("\n🎯 DICA PROFISSIONAL - Nomes descritivos:")
        print("")
        print("😰 RUIM:")
        print("   x = 1000")
        print("   y = 0.08")
        print("   z = x * y")
        print("")
        print("😍 BOM:")
        print("   preco_produto = 1000")
        print("   taxa_desconto = 0.08")
        print("   desconto = preco_produto * taxa_desconto")
        print("")
        print("🔍 Qual código é mais fácil de entender?")
        
        # Exercícios práticos
        self.utils.exercicio(
            "Se eu escrever: x = 10, o que é 'x'?",
            ["variável", "variavel", "uma variável", "uma variavel"],
            "É onde guardamos o valor 10"
        )
        
        self.utils.exercicio(
            "Qual nome de variável está CORRETO?",
            ["nome_usuario", "nome usuario", "2nome", "nome@"],
            "Não pode ter espaços nem caracteres especiais"
        )
        
        self.utils.exercicio(
            "Em Python, 'nome' e 'Nome' são a mesma variável?",
            ["não", "nao", "false", "diferentes"],
            "Python diferencia maiúsculas de minúsculas"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_3()

    def modulo_4_tipos_dados(self) -> None:
        """Módulo 4: Tipos de Dados"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 4: TIPOS DE DADOS - O DNA DAS INFORMAÇÕES")
        
        print("🧬 Cada informação em Python tem um 'DNA' especial!")
        print("Esse DNA define o que podemos fazer com ela.")
        
        print("\n═══════════════════════════════════════════════")
        print("        OS 4 TIPOS FUNDAMENTAIS")
        print("═══════════════════════════════════════════════")
        
        print("\n🔢 1. NÚMEROS INTEIROS (int)")
        print("   São números SEM vírgula: 1, 100, -5, 0")
        print("   Usamos para: idades, quantidade, posições...")
        
        print("\n🔢 2. NÚMEROS DECIMAIS (float)")  
        print("   São números COM vírgula: 3.14, 1.75, -2.5")
        print("   Usamos para: preços, medidas, percentuais...")
        
        print("\n📝 3. TEXTOS (string)")
        print("   São palavras entre aspas: 'João', \"Python\"")
        print("   Usamos para: nomes, mensagens, descrições...")
        
        print("\n✅ 4. VERDADEIRO/FALSO (boolean)")
        print("   Apenas dois valores: True ou False")
        print("   Usamos para: decisões, estados, flags...")
        
        self.utils.pausar()
        
        print("\n🎯 Vamos ver cada tipo em ação:")
        
        codigo = '''# Números inteiros (int)
idade = 25
quantidade = 100
temperatura = -10

print("=== INTEIROS ===")
print("Idade:", idade)
print("Quantidade:", quantidade) 
print("Temperatura:", temperatura)

# Números decimais (float)
altura = 1.75
preco = 29.99
pi = 3.14159

print("\\n=== DECIMAIS ===")
print("Altura:", altura)
print("Preço: R$", preco)
print("Pi:", pi)

# Textos (string)
nome = "Ana Silva"
cidade = "São Paulo"
hobby = 'programação'

print("\\n=== TEXTOS ===")
print("Nome:", nome)
print("Cidade:", cidade)
print("Hobby:", hobby)

# Verdadeiro/Falso (boolean)
tem_carteira = True
e_maior_idade = True
gosta_python = True
tem_medo_python = False

print("\\n=== VERDADEIRO/FALSO ===")
print("Tem carteira:", tem_carteira)
print("É maior de idade:", e_maior_idade)
print("Gosta de Python:", gosta_python)
print("Tem medo de Python:", tem_medo_python)'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        self.utils.pausar()
        
        print("\n🔍 Como descobrir o tipo de uma variável?")
        print("Use a função type()!")
        
        codigo2 = '''# Testando tipos
nome = "João"
idade = 30
altura = 1.80
tem_pets = True

print("Tipo de 'nome':", type(nome))
print("Tipo de 'idade':", type(idade))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'tem_pets':", type(tem_pets))'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🔄 CONVERSÃO ENTRE TIPOS (Type Casting):")
        
        codigo3 = '''# Convertendo entre tipos
numero_texto = "123"
numero_int = int(numero_texto)
numero_float = float(numero_texto)

print("Original (string):", numero_texto, "- Tipo:", type(numero_texto))
print("Como int:", numero_int, "- Tipo:", type(numero_int))
print("Como float:", numero_float, "- Tipo:", type(numero_float))

# Convertendo números para texto
idade = 25
idade_texto = str(idade)
print("\\nIdade como número:", idade, "- Tipo:", type(idade))
print("Idade como texto:", idade_texto, "- Tipo:", type(idade_texto))

# Convertendo para boolean
print("\\n=== CONVERSÕES PARA BOOLEAN ===")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n⚠️ CUIDADOS com conversões:")
        
        codigo4 = '''# Conversões que podem dar erro
try:
    numero = int("abc")  # Isso vai dar erro!
except ValueError as e:
    print("ERRO:", e)
    print("Não posso converter 'abc' para número!")

try:
    numero = int("3.14")  # Isso também dá erro!
except ValueError as e:
    print("ERRO:", e)
    print("Para converter '3.14', use float() primeiro!")
    
# Jeito correto:
numero_correto = int(float("3.14"))
print("Conversão correta:", numero_correto)'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n🧮 OPERAÇÕES por tipo:")
        
        print("\n📊 COM NÚMEROS (int/float):")
        print("• Soma: 5 + 3 = 8")
        print("• Subtração: 10 - 4 = 6") 
        print("• Multiplicação: 3 * 7 = 21")
        print("• Divisão: 15 / 3 = 5.0")
        print("• Potência: 2 ** 3 = 8")
        
        codigo5 = '''a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")'''
        
        self.utils.exemplo(codigo5)
        self.utils.executar_codigo(codigo5)
        
        print("\n📝 COM TEXTOS (string):")
        print("• Concatenação: 'Olá' + ' ' + 'Mundo' = 'Olá Mundo'")
        print("• Repetição: 'Python! ' * 3 = 'Python! Python! Python! '")
        
        codigo6 = '''nome = "Ana"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

grito = "Python! " * 3
print("Grito:", grito)

# Tamanho do texto
print("Tamanho do nome:", len(nome_completo))'''
        
        self.utils.exemplo(codigo6)
        self.utils.executar_codigo(codigo6)
        
        self.utils.pausar()
        
        print("\n💡 CURIOSIDADES sobre tipos:")
        print("• Python descobre o tipo automaticamente!")
        print("• Uma variável pode mudar de tipo durante o programa")
        print("• Strings podem usar aspas simples ' ou duplas \"")
        print("• Números muito grandes são automaticamente int")
        print("• True e False SEMPRE começam com maiúscula")
        
        codigo7 = '''# Variável mudando de tipo
variavel = 42          # int
print("Como int:", variavel, type(variavel))

variavel = 3.14        # float  
print("Como float:", variavel, type(variavel))

variavel = "Python"    # string
print("Como string:", variavel, type(variavel))

variavel = True        # boolean
print("Como boolean:", variavel, type(variavel))'''
        
        self.utils.exemplo(codigo7)
        self.utils.executar_codigo(codigo7)
        
        self.utils.pausar()
        
        print("\n🎯 DICAS PROFISSIONAIS:")
        print("• Use int para contadores, idades, quantidades")
        print("• Use float para medidas, preços, cálculos precisos")
        print("• Use string para nomes, mensagens, textos")
        print("• Use boolean para flags, estados, condições")
        print("• Sempre valide entradas do usuário!")
        print("• Nomes de variáveis devem indicar o tipo esperado")
        
        # Exercícios práticos
        self.utils.exercicio(
            "Qual tipo de dado é o valor 3.14?",
            ["float", "ponto flutuante", "número decimal"],
            "É um número com decimais"
        )
        
        self.utils.exercicio(
            "Como converter o texto '100' para número inteiro?",
            ["int('100')", "int(\"100\")", "int('100')"],
            "Use a função int()"
        )
        
        self.utils.exercicio(
            "True e False são de que tipo?",
            ["boolean", "bool", "verdadeiro/falso"],
            "São valores lógicos"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_4()

    # ============================================================================
    # MÓDULOS INTERMEDIÁRIOS (12-17)
    # ============================================================================

    def modulo_12_dicionarios(self) -> None:
        """Módulo 12: Dicionários e Sets"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 12: DICIONÁRIOS E SETS - ESTRUTURAS AVANÇADAS")
        
        print("🗂️ Dicionários são como 'cadastros' onde cada informação tem uma CHAVE!")
        print("📚 Sets são coleções de itens ÚNICOS, sem repetição!")
        
        print("\n═══════════════════════════════════════════════")
        print("        DICIONÁRIOS - DADOS ORGANIZADOS")
        print("═══════════════════════════════════════════════")
        
        print("\n🔑 Como funciona:")
        print("• CHAVE: o 'nome' da informação")
        print("• VALOR: a informação em si")
        print("• Como uma agenda: NOME → TELEFONE")
        
        self.utils.pausar()
        
        # Exemplo básico de dicionário
        codigo1 = '''# Criando um dicionário
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Programadora"
}

print("=== DADOS DA PESSOA ===")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")
print(f"Profissão: {pessoa['profissao']}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔧 Operações com dicionários:")
        
        codigo2 = '''# Manipulando dicionários
estoque = {"maçãs": 50, "bananas": 30, "laranjas": 25}

print("Estoque inicial:", estoque)

# Adicionar item
estoque["uvas"] = 40
print("Após adicionar uvas:", estoque)

# Modificar item
estoque["maçãs"] = 60
print("Após aumentar maçãs:", estoque)

# Remover item
del estoque["bananas"]
print("Após remover bananas:", estoque)

# Verificar se existe
if "laranjas" in estoque:
    print(f"Temos {estoque['laranjas']} laranjas!")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🔍 Métodos úteis de dicionários:")
        
        codigo3 = '''# Métodos de dicionário
notas = {"João": 8.5, "Maria": 9.2, "Pedro": 7.8, "Ana": 9.5}

print("Todas as chaves:", list(notas.keys()))
print("Todos os valores:", list(notas.values()))
print("Pares chave-valor:", list(notas.items()))

print("\\n=== RELATÓRIO DE NOTAS ===")
for nome, nota in notas.items():
    status = "Aprovado" if nota >= 7.0 else "Reprovado"
    print(f"{nome}: {nota} - {status}")

# Nota mais alta
melhor_nota = max(notas.values())
melhor_aluno = max(notas, key=notas.get)
print(f"\\nMelhor aluno: {melhor_aluno} com nota {melhor_nota}")'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n📚 SETS - Coleções Únicas:")
        
        codigo4 = '''# Trabalhando com sets
frutas = {"maçã", "banana", "laranja", "maçã", "uva", "banana"}
print("Set de frutas:", frutas)  # Sem repetições!

numeros_pares = {2, 4, 6, 8, 10}
numeros_primos = {2, 3, 5, 7, 11}

print("\\nNúmeros pares:", numeros_pares)
print("Números primos:", numeros_primos)

# Operações de conjuntos
print("\\n=== OPERAÇÕES DE CONJUNTOS ===")
print("União:", numeros_pares | numeros_primos)
print("Interseção:", numeros_pares & numeros_primos)
print("Diferença:", numeros_pares - numeros_primos)

# Adicionar e remover
frutas.add("kiwi")
frutas.discard("banana")
print("\\nFrutas após modificações:", frutas)'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n💼 Exemplo prático - Sistema de Usuários:")
        
        codigo5 = '''# Sistema de usuários
usuarios = {}

def cadastrar_usuario(nome, email, idade):
    usuarios[email] = {
        "nome": nome,
        "idade": idade,
        "ativo": True
    }
    print(f"✅ Usuário {nome} cadastrado!")

def listar_usuarios():
    print("\\n=== USUÁRIOS CADASTRADOS ===")
    for email, dados in usuarios.items():
        status = "🟢 Ativo" if dados["ativo"] else "🔴 Inativo"
        print(f"{dados['nome']} ({email}) - {dados['idade']} anos - {status}")

# Testando o sistema
cadastrar_usuario("João Silva", "joao@email.com", 30)
cadastrar_usuario("Maria Santos", "maria@email.com", 25)
cadastrar_usuario("Pedro Costa", "pedro@email.com", 35)

listar_usuarios()

print(f"\\nTotal de usuários: {len(usuarios)}")'''
        
        self.utils.exemplo(codigo5)
        self.utils.executar_codigo(codigo5)
        
        # Exercícios
        self.utils.exercicio(
            "Como acessar o valor 'Ana' no dicionário {'nome': 'Ana', 'idade': 20}?",
            ["dict['nome']", "dict[\"nome\"]", "dicionario['nome']"],
            "Use a chave entre colchetes"
        )
        
        self.utils.exercicio(
            "O que acontece se eu criar um set com elementos repetidos?",
            ["remove repetições", "elementos únicos", "sem duplicatas"],
            "Sets não permitem duplicatas"
        )

    def modulo_13_funcoes_avancadas(self) -> None:
        """Módulo 13: Funções Avançadas e Lambda"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 13: FUNÇÕES AVANÇADAS & LAMBDA - PODER REAL DO PYTHON")
        
        print("🚀 Agora vamos desbloquear o VERDADEIRO poder das funções!")
        print("🎯 Lambda, *args, **kwargs, closures, decorators básicos...")
        
        print("\n═══════════════════════════════════════════════")
        print("        FUNÇÕES LAMBDA - FUNÇÕES ANÔNIMAS")
        print("═══════════════════════════════════════════════")
        
        print("\n⚡ Lambda = função de UMA LINHA APENAS!")
        print("📝 Sintaxe: lambda parâmetros: expressão")
        print("💡 Usa quando a função é simples e usada poucas vezes")
        
        self.utils.pausar()
        
        # Lambda básico
        codigo1 = '''# Funções normais vs Lambda
def quadrado_normal(x):
    return x ** 2

quadrado_lambda = lambda x: x ** 2

print("Função normal:", quadrado_normal(5))
print("Lambda:", quadrado_lambda(5))

# Mais exemplos de lambda
dobrar = lambda x: x * 2
somar = lambda a, b: a + b
eh_par = lambda n: n % 2 == 0

print("\\nExemplos de lambda:")
print(f"Dobrar 8: {dobrar(8)}")
print(f"Somar 3 + 7: {somar(3, 7)}")
print(f"15 é par? {eh_par(15)}")
print(f"20 é par? {eh_par(20)}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n🔥 Lambda com map(), filter() e sorted():")
        
        codigo2 = '''# Lambda com funções built-in
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# MAP - aplica função a todos elementos
quadrados = list(map(lambda x: x**2, numeros))
print("Quadrados:", quadrados)

# FILTER - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# SORTED - ordena com critério personalizado
pessoas = ["Ana", "João", "Pedro", "Maria"]
por_tamanho = sorted(pessoas, key=lambda nome: len(nome))
print("Ordenado por tamanho:", por_tamanho)

# Exemplo mais complexo
produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 200}
]

# Ordenar por preço
por_preco = sorted(produtos, key=lambda p: p["preco"])
print("\\nProdutos por preço:")
for produto in por_preco:
    print(f"  {produto['nome']}: R$ {produto['preco']}")'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        self.utils.pausar()
        
        print("\n🎯 *args e **kwargs - Argumentos Flexíveis:")
        
        codigo3 = '''# *args - argumentos posicionais variáveis
def somar_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print("Soma de 2 números:", somar_todos(5, 3))
print("Soma de 5 números:", somar_todos(1, 2, 3, 4, 5))
print("Soma de 1 número:", somar_todos(10))

# **kwargs - argumentos nomeados variáveis
def criar_perfil(nome, **kwargs):
    print(f"\\n=== PERFIL DE {nome.upper()} ===")
    for chave, valor in kwargs.items():
        print(f"{chave.title()}: {valor}")

criar_perfil("João", idade=30, cidade="São Paulo", profissao="Programador")
criar_perfil("Maria", idade=25, hobby="Fotografia", tem_pets=True)

# Combinando tudo
def funcao_completa(obrigatorio, *args, **kwargs):
    print(f"Parâmetro obrigatório: {obrigatorio}")
    print(f"Args extras: {args}")
    print(f"Kwargs extras: {kwargs}")

funcao_completa("teste", 1, 2, 3, nome="Python", versao=3.9)'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        self.utils.pausar()
        
        print("\n🔒 Closures - Funções que 'lembram':")
        
        codigo4 = '''# Closures - função interna acessa variável externa
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator  # 'lembra' do fator!
    return multiplicar

# Criando multiplicadores personalizados
vezes_2 = criar_multiplicador(2)
vezes_10 = criar_multiplicador(10)
vezes_100 = criar_multiplicador(100)

print("5 x 2 =", vezes_2(5))
print("5 x 10 =", vezes_10(5))
print("5 x 100 =", vezes_100(5))

# Contador com closure
def criar_contador():
    count = 0
    def incrementar():
        nonlocal count  # Modifica variável do escopo externo
        count += 1
        return count
    return incrementar

contador1 = criar_contador()
contador2 = criar_contador()

print("\\nContador 1:", contador1(), contador1(), contador1())
print("Contador 2:", contador2(), contador2())'''
        
        self.utils.exemplo(codigo4)
        self.utils.executar_codigo(codigo4)
        
        self.utils.pausar()
        
        print("\n🎨 Decorator Simples:")
        
        codigo5 = '''# Decorator básico - adiciona funcionalidade
def medir_tempo(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱️ {func.__name__} executou em {fim - inicio:.4f}s")
        return resultado
    return wrapper

# Usando o decorator
@medir_tempo
def calcular_soma(n):
    return sum(range(n))

@medir_tempo  
def calcular_fibonacci(n):
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# Testando
resultado = calcular_soma(1000000)
print(f"Soma até 1 milhão: {resultado}")

fib_10 = calcular_fibonacci(10)
print(f"Fibonacci(10): {fib_10}")'''
        
        self.utils.exemplo(codigo5)
        self.utils.executar_codigo(codigo5)
        
        # Exercícios
        self.utils.exercicio(
            "Como criar uma lambda que retorna o dobro de um número?",
            ["lambda x: x * 2", "lambda x: 2 * x", "lambda n: n * 2"],
            "lambda parâmetro: expressão"
        )
        
        self.utils.exercicio(
            "O que significa *args numa função?",
            ["argumentos variáveis", "argumentos posicionais", "vários argumentos"],
            "Permite número variável de argumentos"
        )

    def modulo_5_entrada_dados(self) -> None:
        """Módulo 5: Entrada de Dados"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 5: ENTRADA DE DADOS")
        
        print("Podemos pedir informações ao usuário com input()")
        
        codigo = '''nome = input("Qual é seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao Python!")'''
        
        self.utils.exemplo(codigo)
        
        print("\n🔸 Vamos testar!")
        nome = input("Qual é seu nome? ")
        print(f"Olá, {nome}! Bem-vindo ao Python!")
        
        print("\n⚠️  Importante: input() sempre retorna texto (string)")
        print("Para números, precisamos converter:")
        
        codigo2 = '''idade = int(input("Sua idade: "))
print(f"Ano que vem você terá {idade + 1} anos")'''
        
        self.utils.exemplo(codigo2)
        
        self.utils.pausar()
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_5()

    def modulo_6_operacoes(self) -> None:
        """Módulo 6: Operações Matemáticas"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 6: OPERAÇÕES MATEMÁTICAS")
        
        print("Python é uma calculadora poderosa!")
        
        codigo = '''# Operações básicas
a = 10
b = 3

print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b:.2f}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto: {a} % {b} = {a % b}")
print(f"Potência: {a} ** 2 = {a ** 2}")'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        self.utils.pausar()
        
        self.utils.exercicio(
            "Qual operador usamos para calcular o resto de uma divisão?",
            "%",
            "É um símbolo de porcentagem"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_modulo_6()

    def modulo_7_condicoes(self) -> None:
        """Módulo 7: Condições (if/else)"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 7: TOMANDO DECISÕES (IF/ELSE)")
        
        print("Programas precisam tomar decisões!")
        
        codigo = '''idade = 18

if idade >= 18:
    print("Você é maior de idade! 🎉")
    print("Pode tirar carteira de motorista")
else:
    print("Você é menor de idade")
    print(f"Faltam {18 - idade} anos para a maioridade")'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        print("\n📌 Operadores de comparação:")
        print("• == (igual)")
        print("• != (diferente)")
        print("• > (maior)")
        print("• < (menor)")
        print("• >= (maior ou igual)")
        print("• <= (menor ou igual)")
        
        # Mini Projeto do Módulo 7
        self._mini_projeto_modulo_7()
        
        self.utils.pausar()

    def modulo_8_loops(self) -> None:
        """Módulo 8: Repetições (Loops)"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 8: REPETIÇÕES (LOOPS)")
        
        print("Loops permitem repetir código várias vezes!")
        
        print("\n1️⃣ Loop FOR - quando sabemos quantas vezes repetir:")
        codigo1 = '''for i in range(5):
    print(f"Contando: {i}")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        self.utils.pausar()
        
        print("\n2️⃣ Loop WHILE - repete enquanto condição for verdadeira:")
        codigo2 = '''contador = 0
while contador < 3:
    print(f"Contador vale: {contador}")
    contador += 1'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        
        # Mini Projeto do Módulo 8
        self._mini_projeto_modulo_8()
        
        self.utils.pausar()

    def modulo_9_listas(self) -> None:
        """Módulo 9: Listas"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 9: LISTAS")
        
        print("Listas armazenam múltiplos valores!")
        
        codigo = '''# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Adicionando elementos
frutas.append("uva")
print(f"Lista atualizada: {frutas}")

# Percorrendo a lista
print("\\nTodas as frutas:")
for fruta in frutas:
    print(f"- {fruta}")'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        # Mini Projeto do Módulo 9
        self._mini_projeto_modulo_9()
        
        self.utils.pausar()

    def modulo_10_funcoes(self) -> None:
        """Módulo 10: Funções"""
        self.utils.limpar_tela()
        self.utils.titulo("MÓDULO 10: FUNÇÕES")
        
        print("Funções são blocos de código reutilizáveis!")
        
        codigo = '''def saudar(nome):
    """Função que saúda uma pessoa"""
    return f"Olá, {nome}! Como vai?"

def calcular_media(n1, n2, n3):
    """Calcula a média de 3 números"""
    media = (n1 + n2 + n3) / 3
    return media

# Usando as funções
mensagem = saudar("Maria")
print(mensagem)

resultado = calcular_media(8, 7, 9)
print(f"Média: {resultado:.1f}")'''
        
        self.utils.exemplo(codigo)
        self.utils.executar_codigo(codigo)
        
        # Mini Projeto do Módulo 10
        self._mini_projeto_modulo_10()
        
        self.utils.pausar()

    def projeto_final(self) -> None:
        """Projeto Final: Calculadora"""
        self.utils.limpar_tela()
        self.utils.titulo("PROJETO FINAL: CALCULADORA")
        
        print("Vamos criar uma calculadora simples!")
        print("Este projeto usa tudo que aprendemos:")
        print("✓ Variáveis")
        print("✓ Input/Output")
        print("✓ Operações")
        print("✓ Condições")
        print("✓ Loops")
        print("✓ Funções")
        
        self.utils.pausar()
        
        codigo = '''def calculadora():
    while True:
        print("\\n--- CALCULADORA ---")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        
        opcao = input("\\nEscolha uma opção: ")
        
        if opcao == "5":
            print("Até logo!")
            break
        
        if opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            
            if opcao == "1":
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero!")
        else:
            print("Opção inválida!")

# Executar a calculadora
calculadora()'''
        
        self.utils.exemplo(codigo)
        print("\n🎯 Execute este código para testar a calculadora!")
        
        # Mini Projeto do Módulo 11 (Projeto Final)
        self._mini_projeto_modulo_11()
        
        self.utils.pausar()

    # Métodos dos módulos avançados
    def modulo_12_dicionarios(self):
        """Módulo 12: Dicionários e Sets"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_12_dicionarios()
    
    def modulo_13_funcoes_avancadas(self):
        """Módulo 13: Funções Avançadas & Lambda"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_13_funcoes_avancadas()
    
    def modulo_14_comprehensions(self):
        """Módulo 14: List/Dict Comprehensions"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_14_comprehensions()
    
    def modulo_15_arquivos(self):
        """Módulo 15: Manipulação de Arquivos"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_15_arquivos()
    
    def modulo_16_excecoes(self):
        """Módulo 16: Tratamento de Erros"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_16_excecoes()
    
    def modulo_17_modulos(self):
        """Módulo 17: Módulos e Bibliotecas"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_17_modulos()
    
    def modulo_18_oop_basico(self):
        """Módulo 18: Programação Orientada a Objetos"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_18_oop_basico()
    
    def modulo_19_oop_avancado(self):
        """Módulo 19: OOP Avançado - Herança e Polimorfismo"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_19_oop_avancado()
    
    def modulo_20_decorators(self):
        """Módulo 20: Decorators e Context Managers"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_20_decorators()
    
    def modulo_21_geradores(self):
        """Módulo 21: Generators e Iterators"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_21_geradores()
    
    def modulo_22_regex(self):
        """Módulo 22: Expressões Regulares"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_22_regex()
    
    def modulo_23_debugging(self):
        """Módulo 23: Debugging e Profiling"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.modulo_23_debugging()
    
    def projeto_intermediario(self):
        """Módulo 24: PROJETO - Sistema de Biblioteca"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.projeto_intermediario()
    
    def projeto_avancado(self):
        """Módulo 25: PROJETO - Web Scraper"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.projeto_avancado()
    
    def projeto_final_avancado(self):
        """Módulo 26: PROJETO FINAL - API REST"""
        from .advanced_modules import AdvancedModules
        adv = AdvancedModules()
        return adv.projeto_final_avancado()
    
    # ======================================
    #        MINI PROJETOS PRÁTICOS
    # ======================================
    
    def _mini_projeto_modulo_1(self) -> None:
        """Mini Projeto - Módulo 1: Cartão de Apresentação Python"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: CARTÃO DE APRESENTAÇÃO PYTHON")
        
        print("🎉 Vamos criar seu primeiro projeto prático!")
        print("Você vai fazer um programa que cria um cartão de apresentação.")
        print("Este tipo de programa é útil para:")
        print("• Páginas pessoais")
        print("• Assinaturas de email")
        print("• Perfis profissionais")
        print("• Cartões de visita digitais")
        
        self.utils.pausar()
        
        print("\n📝 PASSO 1: Vamos coletar suas informações")
        print("Digite suas informações (pode ser real ou fictício):")
        
        try:
            nome = input("👤 Seu nome: ").strip()
            if not nome:
                nome = "Estudante Python"
            
            profissao = input("💼 Sua profissão/área de interesse: ").strip()
            if not profissao:
                profissao = "Futuro Programador Python"
            
            hobby = input("🎮 Um hobby ou interesse: ").strip()
            if not hobby:
                hobby = "Aprender programação"
                
            print(f"\n✅ Informações coletadas para {nome}!")
            
        except KeyboardInterrupt:
            print("\n⚠️ Projeto cancelado pelo usuário")
            return
            
        self.utils.pausar()
        
        print("\n💻 PASSO 2: Agora vamos PROGRAMAR o cartão!")
        print("Aqui está o código que você criou:")
        
        codigo_gerado = f'''# 🐍 MEU PRIMEIRO PROJETO PYTHON
# Cartão de Apresentação Digital

print("=" * 50)
print("     🎯 CARTÃO DE APRESENTAÇÃO DIGITAL")
print("=" * 50)
print()
print("👤 Nome: {nome}")
print("💼 Profissão: {profissao}")
print("🎮 Hobby: {hobby}")
print("🐍 Status: Aprendendo Python!")
print()
print("=" * 50)
print("🚀 Feito com Python - A linguagem do futuro!")
print("=" * 50)'''
        
        self.utils.exemplo(codigo_gerado)
        self.utils.pausar()
        
        print("\n🎬 RESULTADO FINAL:")
        self.utils.executar_codigo(codigo_gerado)
        
        print("\n🎉 PARABÉNS! Você criou seu primeiro projeto!")
        print("\n💡 APLICAÇÕES NA VIDA REAL:")
        print("• Sites pessoais usam códigos similares")
        print("• Apps de rede social fazem perfis assim")
        print("• Sistemas de RH organizam dados de funcionários")
        print("• Jogos criam fichas de personagens")
        
        print("\n🏆 CONQUISTA DESBLOQUEADA: Primeiro Projeto!")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_1", "Cartão de Apresentação Python", 50)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_2(self) -> None:
        """Mini Projeto - Módulo 2: Gerador de Mensagens Motivacionais"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: GERADOR DE MENSAGENS MOTIVACIONAIS")
        
        print("🌟 Vamos criar um programa que gera mensagens motivacionais!")
        print("Tipo de programa usado em:")
        print("• Apps de bem-estar mental")
        print("• Sistemas de coaching")
        print("• Jogos com sistema de conquistas")
        print("• Chatbots motivacionais")
        
        self.utils.pausar()
        
        print("\n📱 CONTEXTO REAL:")
        print("Apps como Headspace, Calm e Duolingo usam")
        print("sistemas similares para motivar usuários!")
        
        self.utils.pausar()
        
        print("\n💻 Vamos construir o programa passo a passo:")
        
        # Passo 1 - Mensagem básica
        print("\n🔸 PASSO 1: Mensagem de bom dia")
        codigo1 = '''print("🌅 Bom dia!")
print("Hoje é um novo dia cheio de possibilidades!")'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        self.utils.pausar()
        
        # Passo 2 - Adicionar personalização
        print("\n🔸 PASSO 2: Vamos personalizar com emojis")
        codigo2 = '''print("=" * 40)
print("     🌟 MENSAGEM DO DIA 🌟")
print("=" * 40)
print()
print("🌅 Bom dia, campeão!")
print("💪 Você é capaz de grandes coisas!")
print("🚀 Cada linha de código te torna mais forte!")
print("🎯 Hoje você vai arrasar!")
print()
print("=" * 40)'''
        
        self.utils.exemplo(codigo2)
        self.utils.executar_codigo(codigo2)
        self.utils.pausar()
        
        # Passo 3 - Sistema completo
        print("\n🔸 PASSO 3: Sistema completo como apps reais")
        codigo3 = '''# 🌟 GERADOR DE MOTIVAÇÃO DIÁRIA
print("🎊" * 20)
print("        MOTIVAÇÃO PYTHON")  
print("🎊" * 20)
print()
print("📱 Carregando sua dose diária de motivação...")
print()
print("✨ Mensagem especial para você:")
print("👑 Você escolheu aprender Python!")
print("🧠 Isso mostra que você é inteligente!")
print("🔥 Cada exercício te deixa mais expert!")
print("🏆 Você já está no caminho do sucesso!")
print()
print("💡 DICA PROFISSIONAL:")
print("Programadores ganham em média R$ 5.000-15.000")
print("Python é a linguagem mais procurada!")
print()
print("🎯 Continue assim e você chegará lá!")
print("🎊" * 20)'''
        
        self.utils.exemplo(codigo3)
        self.utils.executar_codigo(codigo3)
        
        print("\n🎉 PROJETO CONCLUÍDO!")
        print("\n🌍 COMO ISSO É USADO NO MUNDO REAL:")
        print("• 📱 WhatsApp: Mensagens de status")
        print("• 🎮 Games: Sistemas de conquistas")
        print("• 📚 Duolingo: Motivação para estudar")
        print("• 💼 LinkedIn: Posts motivacionais")
        print("• 🏃 Apps fitness: Encorajamento diário")
        
        print("\n🚀 PRÓXIMO NÍVEL:")
        print("Com o que você vai aprender, poderá criar:")
        print("• Apps que lembram de beber água")
        print("• Sistemas de metas pessoais")
        print("• Chatbots para empresas")
        print("• Jogos educativos")
        
        print("\n🏆 CONQUISTA: Criador de Experiências!")
        self.utils.pausar()
    
    def _mini_projeto_modulo_3(self) -> None:
        """Mini Projeto - Módulo 3: Sistema de Perfil de Jogador"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE PERFIL DE JOGADOR")
        
        print("🎮 Vamos criar um sistema de perfil para um jogo RPG!")
        print("Tipo de sistema usado em:")
        print("• Jogos online (World of Warcraft, League of Legends)")
        print("• Apps de fitness (Nike Training, Strava)")
        print("• Redes sociais (Instagram, LinkedIn)")
        print("• Sistemas de e-learning")
        
        self.utils.pausar()
        
        print("\n📝 Vamos criar variáveis para armazenar dados do jogador:")
        
        # Demonstração passo a passo
        codigo1 = '''# 🎮 SISTEMA DE PERFIL DE JOGADOR
# Criando variáveis para dados do perfil

# Informações básicas
nome_jogador = "DragonSlayer2024"
nivel = 15
experiencia = 2350
vida_maxima = 100
vida_atual = 85

# Status de habilidades
forca = 18
agilidade = 12
inteligencia = 20
sorte = 8

# Informações de progresso
missoes_completas = 7
inimigos_derrotados = 143
moedas = 1250
item_favorito = "Espada Flamejante"

print("=" * 50)
print("     🎮 PERFIL DO JOGADOR")
print("=" * 50)
print()
print(f"👤 Jogador: {nome_jogador}")
print(f"⭐ Nível: {nivel}")
print(f"💫 XP: {experiencia}")
print(f"❤️  Vida: {vida_atual}/{vida_maxima}")
print()
print("🎯 ATRIBUTOS:")
print(f"💪 Força: {forca}")
print(f"🏃 Agilidade: {agilidade}")
print(f"🧠 Inteligência: {inteligencia}")
print(f"🍀 Sorte: {sorte}")
print()
print("📊 ESTATÍSTICAS:")
print(f"✅ Missões: {missoes_completas}")
print(f"⚔️  Vitórias: {inimigos_derrotados}")
print(f"💰 Moedas: {moedas}")
print(f"🗡️  Item Favorito: {item_favorito}")
print("=" * 50)'''
        
        self.utils.exemplo(codigo1)
        self.utils.executar_codigo(codigo1)
        
        print("\n🎉 PROJETO CONCLUÍDO!")
        print("\n🌍 APLICAÇÕES NO MUNDO REAL:")
        print("• 🎮 Steam: Perfis de jogadores")
        print("• 💼 LinkedIn: Perfis profissionais")
        print("• 🏥 Hospitais: Fichas de pacientes")
        print("• 🏪 E-commerce: Dados de clientes")
        print("• 🎓 Escolas: Sistemas acadêmicos")
        
        print("\n💡 CONCEITOS APRENDIDOS:")
        print("• Organização de dados com variáveis")
        print("• Diferentes tipos de informação")
        print("• Nomenclatura descritiva de variáveis")
        print("• Formatação profissional de saídas")
        
        print("\n🏆 CONQUISTA: Organizador de Dados!")
        self.utils.pausar()
    
    def _mini_projeto_modulo_4(self) -> None:
        """Mini Projeto - Módulo 4: Calculadora de Estatísticas Pessoais"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: CALCULADORA DE ESTATÍSTICAS PESSOAIS")
        
        print("📊 Vamos criar uma calculadora que processa diferentes tipos de dados!")
        print("Sistema similar aos usados em:")
        print("• Apps de saúde (Apple Health, Google Fit)")
        print("• Sistemas bancários (controle financeiro)")
        print("• E-commerce (análise de compras)")
        print("• Redes sociais (estatísticas de perfil)")
        
        self.utils.pausar()
        
        print("\n💻 Programa completo usando todos os tipos de dados:")
        
        codigo_completo = '''# 📊 CALCULADORA DE ESTATÍSTICAS PESSOAIS
print("🔢" * 20)
print("   ANÁLISE DE DADOS PESSOAIS")
print("🔢" * 20)

# Dados pessoais (diferentes tipos)
nome = "Maria Silva"                    # string
idade = 28                             # int
altura = 1.68                          # float
peso = 65.5                           # float
tem_plano_saude = True                # boolean
pratica_exercicios = True             # boolean
salario = 4500.00                     # float
dependentes = 2                       # int

print(f"\\n👤 DADOS PESSOAIS:")
print(f"Nome: {nome} (tipo: {type(nome).__name__})")
print(f"Idade: {idade} anos (tipo: {type(idade).__name__})")
print(f"Altura: {altura}m (tipo: {type(altura).__name__})")

print(f"\\n💪 SAÚDE:")
print(f"Peso: {peso}kg (tipo: {type(peso).__name__})")
print(f"Plano de Saúde: {tem_plano_saude} (tipo: {type(tem_plano_saude).__name__})")
print(f"Pratica Exercícios: {pratica_exercicios} (tipo: {type(pratica_exercicios).__name__})")

# Cálculos automáticos (conversões e operações)
imc = peso / (altura ** 2)             # float result
idade_meses = idade * 12               # int calculation
salario_anual = salario * 12           # float calculation
renda_per_capita = salario / (dependentes + 1)  # float division

print(f"\\n📈 CÁLCULOS AUTOMÁTICOS:")
print(f"IMC: {imc:.2f} (tipo: {type(imc).__name__})")
print(f"Idade em meses: {idade_meses} (tipo: {type(idade_meses).__name__})")
print(f"Salário anual: R$ {salario_anual:.2f} (tipo: {type(salario_anual).__name__})")
print(f"Renda per capita: R$ {renda_per_capita:.2f} (tipo: {type(renda_per_capita).__name__})")

# Análises com boolean
print(f"\\n🎯 ANÁLISES:")
if imc < 18.5:
    situacao_peso = "Abaixo do peso"
elif imc < 25:
    situacao_peso = "Peso normal"
else:
    situacao_peso = "Acima do peso"
    
perfil_saudavel = tem_plano_saude and pratica_exercicios
print(f"Situação do peso: {situacao_peso}")
print(f"Perfil saudável: {perfil_saudavel} (tipo: {type(perfil_saudavel).__name__})")

print("\\n🔢" * 20)
print("   ANÁLISE CONCLUÍDA!")
print("🔢" * 20)'''
        
        self.utils.exemplo(codigo_completo)
        self.utils.executar_codigo(codigo_completo)
        
        print("\n🎉 CALCULADORA CRIADA COM SUCESSO!")
        print("\n🌍 ONDE ISSO É USADO:")
        print("• 🏥 Sistemas hospitalares: Cálculo de IMC e estatísticas")
        print("• 💰 Bancos: Análise de renda e perfil financeiro")
        print("• 📱 Apps fitness: Monitoramento de saúde")
        print("• 🛒 E-commerce: Análise de comportamento de compra")
        print("• 📊 Business Intelligence: Relatórios executivos")
        
        print("\n💡 TÉCNICAS PROFISSIONAIS USADAS:")
        print("• Conversão automática entre tipos")
        print("• Formatação de números com decimais (.2f)")
        print("• Operações lógicas com boolean")
        print("• Cálculos matemáticos com diferentes tipos")
        print("• Análise de dados em tempo real")
        
        print("\n🏆 CONQUISTA: Analista de Dados!")
        self.utils.pausar()
    
    def _mini_projeto_modulo_5(self) -> None:
        """Mini Projeto - Módulo 5: Assistente Virtual de Cadastro"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: ASSISTENTE VIRTUAL DE CADASTRO")
        
        print("🤖 Vamos criar um assistente que coleta dados do usuário!")
        print("Sistema como os usados em:")
        print("• Cadastros de apps (Netflix, Spotify)")
        print("• Formulários de e-commerce")
        print("• Chatbots de atendimento")
        print("• Sistemas de check-in")
        
        self.utils.pausar()
        
        print("\n👨‍💻 Vamos construir um assistente interativo:")
        
        codigo_assistente = '''# 🤖 ASSISTENTE VIRTUAL DE CADASTRO
print("🤖" * 25)
print("     ASSISTENTE VIRTUAL V1.0")
print("🤖" * 25)
print()
print("Olá! Sou seu assistente virtual!")
print("Vou ajudar você a fazer seu cadastro.")
print()

# Coleta de dados interativa
print("📝 DADOS PESSOAIS:")
nome = input("👤 Como você se chama? ")
idade = input("🎂 Qual sua idade? ")
cidade = input("🏙️  Em que cidade você mora? ")
profissao = input("💼 Qual sua profissão? ")

print("\\n📧 CONTATO:")
email = input("📧 Seu melhor email: ")
telefone = input("📱 Seu telefone (com DDD): ")

print("\\n🎯 PREFERÊNCIAS:")
cor_favorita = input("🎨 Sua cor favorita: ")
comida_favorita = input("🍕 Sua comida favorita: ")
hobby = input("🎮 Seu hobby principal: ")

# Processamento e validação
print("\\n⏳ Processando informações...")
print("✅ Dados coletados com sucesso!")
print()

# Conversão de tipos quando necessário
try:
    idade_num = int(idade)
    ano_nascimento = 2024 - idade_num
except ValueError:
    idade_num = 0
    ano_nascimento = "Não calculado"

print("📋" * 25)
print("     RESUMO DO CADASTRO")
print("📋" * 25)
print()
print(f"👤 Nome: {nome}")
print(f"🎂 Idade: {idade} anos")
print(f"🏙️  Cidade: {cidade}")
print(f"💼 Profissão: {profissao}")
print()
print(f"📧 Email: {email}")
print(f"📱 Telefone: {telefone}")
print()
print(f"🎨 Cor favorita: {cor_favorita}")
print(f"🍕 Comida favorita: {comida_favorita}")
print(f"🎮 Hobby: {hobby}")
print()
if ano_nascimento != "Não calculado":
    print(f"📅 Ano aproximado de nascimento: {ano_nascimento}")
print()
print("✅ Cadastro realizado com sucesso!")
print("🎉 Bem-vindo(a) ao sistema!")
print("📋" * 25)'''
        
        self.utils.exemplo(codigo_assistente)
        
        print("\n🎬 Vamos executar nosso assistente:")
        print("(Digite informações reais ou fictícias)")
        self.utils.pausar()
        
        # Execução interativa simplificada para demonstração
        demo_code = '''# DEMO - Assistente Virtual
print("🤖 ASSISTENTE VIRTUAL DEMO")
print("(Simulação com dados de exemplo)")
print()

# Simulação de entrada
nome = "Alex Santos"
idade = "25"
cidade = "São Paulo"
email = "alex@email.com"

print("📋 RESUMO DO CADASTRO DEMO:")
print(f"👤 Nome: {nome}")
print(f"🎂 Idade: {idade} anos")
print(f"🏙️ Cidade: {cidade}")
print(f"📧 Email: {email}")
print("✅ Sistema funcionando perfeitamente!")'''
        
        self.utils.executar_codigo(demo_code)
        
        print("\n🎉 ASSISTENTE CRIADO!")
        print("\n🌍 APLICAÇÕES REAIS:")
        print("• 📱 Apps de delivery: Cadastro de usuários")
        print("• 🏪 E-commerce: Checkout de compras")
        print("• 🏥 Hospitais: Cadastro de pacientes")
        print("• 🎓 Escolas: Matrícula de alunos")
        print("• 🏢 Empresas: Cadastro de funcionários")
        
        print("\n💡 CONCEITOS PROFISSIONAIS:")
        print("• Validação de entrada de dados")
        print("• Conversão segura de tipos (try/except)")
        print("• Interface amigável ao usuário")
        print("• Coleta estruturada de informações")
        print("• Processamento em tempo real")
        
        print("\n🏆 CONQUISTA: Desenvolvedor de Interfaces!")
        self.utils.pausar()
    
    def _mini_projeto_modulo_6(self) -> None:
        """Mini Projeto - Módulo 6: Calculadora Financeira Inteligente"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: CALCULADORA FINANCEIRA INTELIGENTE")
        
        print("💰 Vamos criar uma calculadora para planejamento financeiro!")
        print("Sistema usado em:")
        print("• Apps bancários (Nubank, Itaú)")
        print("• Consultorias financeiras")
        print("• Sistemas de investimento")
        print("• Planilhas empresariais")
        
        self.utils.pausar()
        
        print("\n💻 Calculadora completa com análises automáticas:")
        
        codigo_financeiro = '''# 💰 CALCULADORA FINANCEIRA INTELIGENTE
print("💰" * 30)
print("     CALCULADORA FINANCEIRA V2.0")
print("💰" * 30)

# Dados financeiros de entrada
salario_bruto = 5000.00
desconto_inss = salario_bruto * 0.11        # 11% INSS
desconto_ir = salario_bruto * 0.075         # 7.5% IR
salario_liquido = salario_bruto - desconto_inss - desconto_ir

print(f"\\n📊 ANÁLISE SALARIAL:")
print(f"💵 Salário Bruto: R$ {salario_bruto:.2f}")
print(f"📉 INSS (11%): R$ {desconto_inss:.2f}")
print(f"📉 IR (7.5%): R$ {desconto_ir:.2f}")
print(f"💚 Salário Líquido: R$ {salario_liquido:.2f}")

# Planejamento de gastos (regra 50-30-20)
gastos_essenciais = salario_liquido * 0.50   # 50% necessidades
gastos_desejos = salario_liquido * 0.30       # 30% desejos
poupanca = salario_liquido * 0.20             # 20% poupança

print(f"\\n🎯 PLANEJAMENTO INTELIGENTE (50-30-20):")
print(f"🏠 Gastos Essenciais (50%): R$ {gastos_essenciais:.2f}")
print(f"🎮 Gastos com Desejos (30%): R$ {gastos_desejos:.2f}")
print(f"💎 Poupança (20%): R$ {poupanca:.2f}")

# Projeções de investimento
taxa_rendimento_anual = 0.10  # 10% ao ano
meses = 12
rendimento_mensal = taxa_rendimento_anual / 12
valor_futuro_1_ano = poupanca * meses * (1 + rendimento_mensal)

print(f"\\n📈 PROJEÇÃO DE INVESTIMENTOS:")
print(f"💰 Poupança mensal: R$ {poupanca:.2f}")
print(f"📅 Em 12 meses: R$ {valor_futuro_1_ano:.2f}")
print(f"🚀 Rendimento estimado: R$ {valor_futuro_1_ano - (poupanca * meses):.2f}")

# Metas financeiras
meta_emergencia = salario_liquido * 6        # 6 meses de reserva
meses_para_meta = meta_emergencia / poupanca

print(f"\\n🎯 METAS FINANCEIRAS:")
print(f"🛡️  Reserva de Emergência (6 meses): R$ {meta_emergencia:.2f}")
print(f"⏰ Tempo para atingir: {meses_para_meta:.1f} meses")

# Análise de comprometimento
percentual_comprometido = ((gastos_essenciais + gastos_desejos) / salario_liquido) * 100

print(f"\\n📊 ANÁLISE DE COMPROMETIMENTO:")
print(f"📈 Renda comprometida: {percentual_comprometido:.1f}%")

if percentual_comprometido <= 80:
    situacao = "🟢 EXCELENTE - Finançasn controladas!"
elif percentual_comprometido <= 90:
    situacao = "🟡 ATENÇÃO - Cuidado com os gastos"
else:
    situacao = "🔴 CRÍTICO - Reorganize suas finanças"

print(f"🎯 Situação: {situacao}")

print("\\n💰" * 30)
print("     ANÁLISE CONCLUÍDA!")
print("💰" * 30)'''
        
        self.utils.exemplo(codigo_financeiro)
        self.utils.executar_codigo(codigo_financeiro)
        
        print("\n🎉 CALCULADORA FINANCEIRA CRIADA!")
        print("\n🌍 ONDE ESSA TECNOLOGIA É USADA:")
        print("• 🏦 Bancos: Análise de crédito e planejamento")
        print("• 💳 Fintechs: Apps de controle financeiro")
        print("• 🏢 Empresas: Orçamentos e projeções")
        print("• 📊 Consultorias: Relatórios para clientes")
        print("• 🎓 Educação: Simuladores financeiros")
        
        print("\n💡 MATEMÁTICA FINANCEIRA APLICADA:")
        print("• Cálculo de percentuais automatizado")
        print("• Projeções de crescimento")
        print("• Regra 50-30-20 (planejamento inteligente)")
        print("• Análise de risco financeiro")
        print("• Metas SMART (específicas e mensuráveis)")
        
        print("\n🏆 CONQUISTA: Analista Financeiro!")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_6", "Calculadora Científica Avançada", 65)
        
        self.utils.pausar()
    
    # ======================================
    #    NOVOS MINI PROJETOS (MÓDULOS 7-11)
    # ======================================
    
    def _mini_projeto_modulo_7(self) -> None:
        """Mini Projeto - Módulo 7: Sistema de Classificação Inteligente"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE CLASSIFICAÇÃO INTELIGENTE")
        
        print("🧠 Vamos criar um sistema que toma decisões baseadas em condições!")
        print("💼 Tipo de sistema usado em:")
        print("• Sistema de aprovação de crédito")
        print("• Classificação de produtos")
        print("• Sistemas de recomendação")
        print("• Diagnósticos automatizados")
        
        self.utils.pausar()
        
        print("\n📝 PROJETO: Sistema de Avaliação de Candidatos")
        
        codigo_projeto = '''# 🎯 SISTEMA DE CLASSIFICAÇÃO INTELIGENTE
# Sistema de Avaliação de Candidatos para Vaga

print("🏢 SISTEMA DE AVALIAÇÃO DE CANDIDATOS")
print("=" * 50)

def avaliar_candidato(nome, idade, experiencia, formacao, nota_teste):
    """Avalia candidato baseado em critérios definidos"""
    print(f"\\n👤 Avaliando: {nome}")
    print("-" * 30)
    
    pontuacao = 0
    criterios_atendidos = []
    
    # Critério 1: Idade
    if 18 <= idade <= 65:
        pontuacao += 20
        criterios_atendidos.append("✅ Idade adequada")
    else:
        criterios_atendidos.append("❌ Idade fora do range")
    
    # Critério 2: Experiência
    if experiencia >= 3:
        pontuacao += 30
        criterios_atendidos.append("✅ Experiência suficiente")
    elif experiencia >= 1:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Experiência limitada")
    else:
        criterios_atendidos.append("❌ Sem experiência")
    
    # Critério 3: Formação
    if formacao.lower() in ["superior", "universitario", "faculdade"]:
        pontuacao += 25
        criterios_atendidos.append("✅ Formação superior")
    elif formacao.lower() in ["tecnico", "técnico"]:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Formação técnica")
    else:
        pontuacao += 5
        criterios_atendidos.append("⚠️ Formação básica")
    
    # Critério 4: Nota do teste
    if nota_teste >= 8:
        pontuacao += 25
        criterios_atendidos.append("✅ Excelente no teste")
    elif nota_teste >= 6:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Bom no teste")
    else:
        criterios_atendidos.append("❌ Nota baixa no teste")
    
    # Exibe avaliação detalhada
    print("📊 CRITÉRIOS AVALIADOS:")
    for criterio in criterios_atendidos:
        print(f"  {criterio}")
    
    print(f"\\n🏆 PONTUAÇÃO TOTAL: {pontuacao}/100")
    
    # Decisão final
    if pontuacao >= 80:
        status = "APROVADO - EXCELENTE CANDIDATO"
        emoji = "🌟"
    elif pontuacao >= 60:
        status = "APROVADO - BOM CANDIDATO"
        emoji = "✅"
    elif pontuacao >= 40:
        status = "EM ANÁLISE - CANDIDATO RAZOÁVEL"
        emoji = "⚠️"
    else:
        status = "REPROVADO - NÃO ATENDE CRITÉRIOS"
        emoji = "❌"
    
    print(f"\\n{emoji} RESULTADO: {status}")
    return pontuacao, status

# Testando o sistema com candidatos
print("\\n🧪 TESTANDO O SISTEMA:")

# Candidato 1: Perfil Excelente
print("\\n" + "="*50)
pontos1, resultado1 = avaliar_candidato(
    "Ana Silva", 28, 5, "Superior", 9.2
)

# Candidato 2: Perfil Médio
print("\\n" + "="*50)
pontos2, resultado2 = avaliar_candidato(
    "Carlos Santos", 22, 1, "Técnico", 7.0
)

# Candidato 3: Perfil Baixo
print("\\n" + "="*50)
pontos3, resultado3 = avaliar_candidato(
    "João Oliveira", 45, 0, "Ensino Médio", 5.5
)

# Relatório final
print("\\n" + "="*60)
print("📊 RELATÓRIO FINAL DE AVALIAÇÕES")
print("="*60)
print(f"Ana Silva: {pontos1} pontos - {resultado1.split(' - ')[0]}")
print(f"Carlos Santos: {pontos2} pontos - {resultado2.split(' - ')[0]}")
print(f"João Oliveira: {pontos3} pontos - {resultado3.split(' - ')[0]}")

print("\\n🎯 SISTEMA FUNCIONANDO PERFEITAMENTE!")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Classificação Inteligente criado!")
        print("🎯 Aplicação real: RH, sistemas de aprovação, classificadores automáticos")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_7", "Sistema de Classificação Inteligente", 60)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_8(self) -> None:
        """Mini Projeto - Módulo 8: Gerador de Padrões e Sequências"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: GERADOR DE PADRÕES E SEQUÊNCIAS")
        
        print("🔄 Vamos criar um sistema que gera padrões usando loops!")
        print("🎨 Tipo de aplicação usada em:")
        print("• Arte generativa e design")
        print("• Análise de dados e gráficos")
        print("• Jogos e animações")
        print("• Simulações científicas")
        
        self.utils.pausar()
        
        print("\n📝 PROJETO: Gerador de Padrões Visuais ASCII")
        
        codigo_projeto = '''# 🎨 GERADOR DE PADRÕES E SEQUÊNCIAS
# Sistema de Criação de Arte ASCII e Padrões Matemáticos

import time

print("🎨 GERADOR DE PADRÕES VISUAIS")
print("=" * 50)

def desenhar_triangulo(altura, caractere="*"):
    """Desenha um triângulo usando loops"""
    print(f"\\n📐 TRIÂNGULO (altura {altura}):")
    for i in range(1, altura + 1):
        espacos = " " * (altura - i)
        estrelas = caractere * (2 * i - 1)
        print(espacos + estrelas)

def desenhar_retangulo(largura, altura, caractere="#"):
    """Desenha um retângulo preenchido"""
    print(f"\\n⬜ RETÂNGULO ({largura}x{altura}):")
    for i in range(altura):
        print(caractere * largura)

def desenhar_diamante(tamanho):
    """Desenha um diamante usando loops aninhados"""
    print(f"\\n💎 DIAMANTE (tamanho {tamanho}):")
    
    # Parte superior do diamante
    for i in range(tamanho):
        espacos = " " * (tamanho - i - 1)
        estrelas = "*" * (2 * i + 1)
        print(espacos + estrelas)
    
    # Parte inferior do diamante
    for i in range(tamanho - 2, -1, -1):
        espacos = " " * (tamanho - i - 1)
        estrelas = "*" * (2 * i + 1)
        print(espacos + estrelas)

def sequencia_fibonacci(n):
    """Gera sequência de Fibonacci usando loops"""
    print(f"\\n🔢 SEQUÊNCIA FIBONACCI ({n} termos):")
    a, b = 0, 1
    print(f"Termo 1: {a}")
    if n > 1:
        print(f"Termo 2: {b}")
    
    for i in range(3, n + 1):
        proximo = a + b
        print(f"Termo {i}: {proximo}")
        a, b = b, proximo

def tabuada_visual(numero):
    """Cria tabuada visual com padrões"""
    print(f"\\n✖️ TABUADA VISUAL DO {numero}:")
    print("-" * 30)
    
    for i in range(1, 11):
        resultado = numero * i
        # Cria padrão visual baseado no resultado
        barras = "█" * (resultado // 5)  # 1 barra para cada 5 unidades
        print(f"{numero} × {i:2d} = {resultado:2d} {barras}")

def animacao_carregamento():
    """Cria animação de carregamento usando loops"""
    print("\\n⏳ ANIMAÇÃO DE CARREGAMENTO:")
    
    # Simulação de carregamento
    for progresso in range(0, 101, 10):
        barra = "█" * (progresso // 5)
        espacos = "░" * (20 - len(barra))
        print(f"\\rCarregando: [{barra}{espacos}] {progresso}%", end="")
        time.sleep(0.3)  # Pausa para efeito visual
    print("\\n✅ Carregamento completo!")

def padrao_xadrez(tamanho):
    """Cria padrão de tabuleiro de xadrez"""
    print(f"\\n♟️ PADRÃO XADREZ ({tamanho}x{tamanho}):")
    for linha in range(tamanho):
        linha_str = ""
        for coluna in range(tamanho):
            if (linha + coluna) % 2 == 0:
                linha_str += "⬜"
            else:
                linha_str += "⬛"
        print(linha_str)

# Demonstração dos padrões
print("\\n🎨 GALERIA DE PADRÕES:")

# 1. Formas geométricas
desenhar_triangulo(5, "⭐")
desenhar_retangulo(8, 4, "🟦")
desenhar_diamante(4)

# 2. Sequências matemáticas
sequencia_fibonacci(8)
tabuada_visual(7)

# 3. Padrões visuais
padrao_xadrez(6)

# 4. Animação (simplificada para demo)
print("\\n🎬 DEMO DE ANIMAÇÃO:")
print("Simulando carregamento...")
for i in range(5):
    print(f"{'█' * (i+1)}{'░' * (4-i)} {(i+1)*20}%")

print("\\n🎉 TODOS OS PADRÕES GERADOS COM SUCESSO!")
print("\\n💡 CONCEITOS APLICADOS:")
print("• Loops for e while para repetição")
print("• Loops aninhados para padrões 2D")
print("• Lógica matemática para sequências")
print("• Manipulação de strings para arte ASCII")
print("• Condicionais dentro de loops")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Gerador de Padrões e Sequências criado!")
        print("🎯 Aplicação real: arte generativa, visualização de dados, games")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_8", "Gerador de Padrões e Sequências", 65)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_9(self) -> None:
        """Mini Projeto - Módulo 9: Sistema de Inventário Inteligente"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE INVENTÁRIO INTELIGENTE")
        
        print("📦 Vamos criar um sistema de gerenciamento de inventário!")
        print("🏪 Tipo de sistema usado em:")
        print("• E-commerce e lojas online")
        print("• Supermercados e varejo")
        print("• Almoxarifados e depósitos")
        print("• Controle de estoque empresarial")
        
        self.utils.pausar()
        
        print("\n📝 PROJETO: Sistema de Controle de Estoque")
        
        codigo_projeto = '''# 📦 SISTEMA DE INVENTÁRIO INTELIGENTE
# Sistema Completo de Controle de Estoque

print("🏪 SISTEMA DE INVENTÁRIO INTELIGENTE")
print("=" * 50)

# Base de dados do inventário (usando listas)
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
quantidades = [15, 45, 30, 8, 22]
precos = [2500.00, 85.50, 120.00, 800.00, 150.00]
categorias = ["Eletrônicos", "Periféricos", "Periféricos", "Eletrônicos", "Periféricos"]

# Histórico de movimentações
historico_vendas = []
historico_compras = []

def exibir_estoque():
    """Exibe todo o estoque atual"""
    print("\\n📊 ESTOQUE ATUAL:")
    print("-" * 70)
    print(f"{'ID':<3} {'PRODUTO':<12} {'QTD':<5} {'PREÇO':<10} {'CATEGORIA':<12} {'VALOR TOTAL'}")
    print("-" * 70)
    
    valor_total_estoque = 0
    for i in range(len(produtos)):
        valor_item = quantidades[i] * precos[i]
        valor_total_estoque += valor_item
        
        # Status do estoque
        if quantidades[i] <= 5:
            status = "🔴 BAIXO"
        elif quantidades[i] <= 15:
            status = "🟡 MÉDIO"
        else:
            status = "🟢 ALTO"
        
        print(f"{i+1:<3} {produtos[i]:<12} {quantidades[i]:<5} R${precos[i]:<9.2f} {categorias[i]:<12} R${valor_item:.2f} {status}")
    
    print("-" * 70)
    print(f"💰 VALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")

def adicionar_estoque(produto_id, quantidade_add):
    """Adiciona produtos ao estoque"""
    if 0 <= produto_id < len(produtos):
        produto_nome = produtos[produto_id]
        quantidades[produto_id] += quantidade_add
        
        # Registra no histórico
        historico_compras.append({
            "produto": produto_nome,
            "quantidade": quantidade_add,
            "operacao": "COMPRA"
        })
        
        print(f"✅ Adicionado: {quantidade_add} unidades de {produto_nome}")
        print(f"📊 Novo estoque: {quantidades[produto_id]} unidades")
    else:
        print("❌ Produto não encontrado!")

def vender_produto(produto_id, quantidade_venda):
    """Registra venda e atualiza estoque"""
    if 0 <= produto_id < len(produtos):
        produto_nome = produtos[produto_id]
        
        if quantidades[produto_id] >= quantidade_venda:
            quantidades[produto_id] -= quantidade_venda
            valor_venda = quantidade_venda * precos[produto_id]
            
            # Registra no histórico
            historico_vendas.append({
                "produto": produto_nome,
                "quantidade": quantidade_venda,
                "valor": valor_venda,
                "operacao": "VENDA"
            })
            
            print(f"🛒 Venda realizada: {quantidade_venda} unidades de {produto_nome}")
            print(f"💰 Valor da venda: R$ {valor_venda:.2f}")
            print(f"📊 Estoque restante: {quantidades[produto_id]} unidades")
            
            # Alerta de estoque baixo
            if quantidades[produto_id] <= 5:
                print(f"⚠️ ALERTA: Estoque baixo de {produto_nome}!")
        else:
            print(f"❌ Estoque insuficiente! Disponível: {quantidades[produto_id]} unidades")
    else:
        print("❌ Produto não encontrado!")

def produtos_mais_vendidos():
    """Analisa produtos mais vendidos"""
    print("\\n📈 ANÁLISE DE VENDAS:")
    vendas_por_produto = {}
    
    # Conta vendas por produto
    for venda in historico_vendas:
        produto = venda["produto"]
        if produto in vendas_por_produto:
            vendas_por_produto[produto] += venda["quantidade"]
        else:
            vendas_por_produto[produto] = venda["quantidade"]
    
    if vendas_por_produto:
        print("🏆 RANKING DE VENDAS:")
        # Ordena por quantidade vendida (simulação de ordenação)
        produtos_ordenados = []
        for produto, qtd in vendas_por_produto.items():
            produtos_ordenados.append((produto, qtd))
        
        # Ordena manualmente (bubble sort simplificado)
        for i in range(len(produtos_ordenados)):
            for j in range(len(produtos_ordenados) - 1):
                if produtos_ordenados[j][1] < produtos_ordenados[j + 1][1]:
                    produtos_ordenados[j], produtos_ordenados[j + 1] = produtos_ordenados[j + 1], produtos_ordenados[j]
        
        for i, (produto, qtd) in enumerate(produtos_ordenados):
            medal = ["🥇", "🥈", "🥉"][i] if i < 3 else "🏅"
            print(f"{medal} {produto}: {qtd} unidades vendidas")
    else:
        print("📊 Nenhuma venda registrada ainda.")

def alertas_estoque():
    """Gera alertas de estoque baixo"""
    print("\\n⚠️ ALERTAS DE ESTOQUE:")
    alertas_encontrados = False
    
    for i in range(len(produtos)):
        if quantidades[i] <= 5:
            print(f"🔴 CRÍTICO: {produtos[i]} - Apenas {quantidades[i]} unidades!")
            alertas_encontrados = True
        elif quantidades[i] <= 10:
            print(f"🟡 ATENÇÃO: {produtos[i]} - {quantidades[i]} unidades restantes")
            alertas_encontrados = True
    
    if not alertas_encontrados:
        print("✅ Todos os produtos com estoque adequado!")

# DEMONSTRAÇÃO DO SISTEMA
print("\\n🧪 TESTANDO O SISTEMA:")

# 1. Exibir estoque inicial
exibir_estoque()

# 2. Realizar algumas vendas
print("\\n" + "="*50)
print("🛒 SIMULANDO VENDAS:")
vender_produto(0, 3)  # Vender 3 Notebooks
vender_produto(1, 10) # Vender 10 Mouses
vender_produto(3, 2)  # Vender 2 Monitores

# 3. Adicionar estoque
print("\\n" + "="*50)
print("📦 REABASTECENDO ESTOQUE:")
adicionar_estoque(3, 5)  # Adicionar 5 Monitores
adicionar_estoque(4, 8)  # Adicionar 8 Webcams

# 4. Verificar estoque atualizado
exibir_estoque()

# 5. Análises e relatórios
produtos_mais_vendidos()
alertas_estoque()

print("\\n💰 RESUMO FINANCEIRO:")
total_vendas = sum(venda["valor"] for venda in historico_vendas)
print(f"💵 Total de vendas: R$ {total_vendas:.2f}")

print("\\n🎯 SISTEMA DE INVENTÁRIO FUNCIONANDO PERFEITAMENTE!")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Inventário Inteligente criado!")
        print("🎯 Aplicação real: e-commerce, retail, supply chain, ERP")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_9", "Sistema de Inventário Inteligente", 70)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_10(self) -> None:
        """Mini Projeto - Módulo 10: Sistema de Automação Residencial"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE AUTOMAÇÃO RESIDENCIAL")
        
        print("🏠 Vamos criar um sistema de casa inteligente usando funções!")
        print("🤖 Tipo de sistema usado em:")
        print("• Smart homes e IoT")
        print("• Automação predial")
        print("• Sistemas de segurança")
        print("• Controle de energia inteligente")
        
        self.utils.pausar()
        
        print("\n📝 PROJETO: Central de Automação Doméstica")
        
        codigo_projeto = '''# 🏠 SISTEMA DE AUTOMAÇÃO RESIDENCIAL
# Central de Controle de Casa Inteligente

import time
from datetime import datetime

print("🏠 SISTEMA DE AUTOMAÇÃO RESIDENCIAL")
print("=" * 50)

# Estados dos dispositivos
luzes_estado = {
    "sala": False,
    "quarto": False,
    "cozinha": False,
    "banheiro": False
}

temperatura_ambiente = 24.0
ar_condicionado_ligado = False
temperatura_desejada = 22.0

seguranca_ativa = False
sensores_movimento = {
    "entrada": False,
    "sala": False,
    "quintal": False
}

def controlar_luz(comodo, estado):
    """Controla iluminação de um cômodo"""
    if comodo in luzes_estado:
        luzes_estado[comodo] = estado
        status = "LIGADA" if estado else "DESLIGADA"
        emoji = "💡" if estado else "⚫"
        print(f"{emoji} Luz da {comodo}: {status}")
        
        # Simulação de economia de energia
        if not estado:
            print(f"💚 Economia de energia ativa na {comodo}")
    else:
        print(f"❌ Cômodo '{comodo}' não encontrado!")

def ligar_todas_luzes():
    """Liga todas as luzes da casa"""
    print("\\n🌟 LIGANDO TODAS AS LUZES:")
    for comodo in luzes_estado.keys():
        controlar_luz(comodo, True)

def desligar_todas_luzes():
    """Desliga todas as luzes da casa"""
    print("\\n🌙 DESLIGANDO TODAS AS LUZES:")
    for comodo in luzes_estado.keys():
        controlar_luz(comodo, False)

def controlar_temperatura(nova_temperatura):
    """Controla o sistema de climatização"""
    global temperatura_desejada, ar_condicionado_ligado
    
    temperatura_desejada = nova_temperatura
    
    print(f"\\n🌡️ CONTROLE DE TEMPERATURA:")
    print(f"Temperatura atual: {temperatura_ambiente}°C")
    print(f"Temperatura desejada: {temperatura_desejada}°C")
    
    # Lógica do ar condicionado
    if temperatura_ambiente > temperatura_desejada + 1:
        ar_condicionado_ligado = True
        modo = "RESFRIAMENTO"
        emoji = "❄️"
    elif temperatura_ambiente < temperatura_desejada - 1:
        ar_condicionado_ligado = True
        modo = "AQUECIMENTO"
        emoji = "🔥"
    else:
        ar_condicionado_ligado = False
        modo = "DESLIGADO"
        emoji = "⚫"
    
    print(f"{emoji} Ar condicionado: {modo}")
    return modo

def ativar_modo_seguranca():
    """Ativa sistema de segurança"""
    global seguranca_ativa
    seguranca_ativa = True
    
    print("\\n🛡️ MODO SEGURANÇA ATIVADO:")
    print("• Sensores de movimento ativos")
    print("• Câmeras de vigilância ligadas")
    print("• Alarme armado")
    print("• Notificações de segurança ativas")

def desativar_modo_seguranca():
    """Desativa sistema de segurança"""
    global seguranca_ativa
    seguranca_ativa = False
    
    print("\\n🔓 MODO SEGURANÇA DESATIVADO:")
    print("• Sistema de alarme desarmado")
    print("• Modo normal de operação")

def simular_sensor_movimento(local, detectado):
    """Simula detecção de movimento"""
    sensores_movimento[local] = detectado
    
    if detectado and seguranca_ativa:
        print(f"\\n🚨 ALERTA DE SEGURANÇA!")
        print(f"📍 Movimento detectado: {local}")
        print(f"🕐 Horário: {datetime.now().strftime('%H:%M:%S')}")
        
        # Ações automáticas de segurança
        if local == "entrada":
            print("💡 Ligando luz da entrada automaticamente")
            controlar_luz("sala", True)
        
        print("📱 Notificação enviada para o celular")

def modo_economia_energia():
    """Ativa modo de economia de energia"""
    print("\\n🌱 MODO ECONOMIA DE ENERGIA ATIVADO:")
    
    # Desliga luzes desnecessárias
    luzes_ligadas = [comodo for comodo, estado in luzes_estado.items() if estado]
    if luzes_ligadas:
        print("💡 Desligando luzes desnecessárias:")
        for comodo in luzes_ligadas:
            controlar_luz(comodo, False)
    
    # Ajusta temperatura para economia
    print("🌡️ Ajustando temperatura para economia")
    controlar_temperatura(25.0)  # Temperatura mais econômica
    
    print("📊 Economia estimada: 30% na conta de luz")

def modo_cinema():
    """Configura ambiente para assistir filme"""
    print("\\n🎬 MODO CINEMA ATIVADO:")
    
    # Configurações de iluminação
    desligar_todas_luzes()
    controlar_luz("sala", True)  # Luz baixa na sala
    print("💡 Iluminação ajustada para cinema")
    
    # Temperatura confortável
    controlar_temperatura(21.0)
    print("🌡️ Temperatura ajustada para conforto")
    
    # Configurações de som (simulação)
    print("🔊 Sistema de som configurado")
    print("📺 TV preparada para modo cinema")

def relatorio_status():
    """Gera relatório completo do sistema"""
    print("\\n📊 RELATÓRIO DE STATUS DA CASA:")
    print("=" * 40)
    
    # Status das luzes
    print("💡 ILUMINAÇÃO:")
    for comodo, estado in luzes_estado.items():
        status = "🟢 Ligada" if estado else "🔴 Desligada"
        print(f"  {comodo.capitalize()}: {status}")
    
    # Status do clima
    print("\\n🌡️ CLIMATIZAÇÃO:")
    print(f"  Temperatura atual: {temperatura_ambiente}°C")
    print(f"  Temperatura desejada: {temperatura_desejada}°C")
    ar_status = "🟢 Ligado" if ar_condicionado_ligado else "🔴 Desligado"
    print(f"  Ar condicionado: {ar_status}")
    
    # Status da segurança
    print("\\n🛡️ SEGURANÇA:")
    seg_status = "🟢 Ativa" if seguranca_ativa else "🔴 Inativa"
    print(f"  Sistema: {seg_status}")
    
    # Cálculo de consumo (simulação)
    luzes_ligadas = sum(1 for estado in luzes_estado.values() if estado)
    consumo_estimado = luzes_ligadas * 10  # 10W por luz
    if ar_condicionado_ligado:
        consumo_estimado += 1500  # 1500W para o ar
    
    print(f"\\n⚡ CONSUMO ESTIMADO: {consumo_estimado}W")

# DEMONSTRAÇÃO DO SISTEMA
print("\\n🧪 TESTANDO O SISTEMA DE AUTOMAÇÃO:")

# 1. Status inicial
relatorio_status()

# 2. Teste de iluminação
print("\\n" + "="*50)
print("💡 TESTANDO CONTROLE DE ILUMINAÇÃO:")
controlar_luz("sala", True)
controlar_luz("cozinha", True)

# 3. Teste de temperatura
print("\\n" + "="*50)
print("🌡️ TESTANDO CONTROLE DE TEMPERATURA:")
controlar_temperatura(20.0)

# 4. Teste de segurança
print("\\n" + "="*50)
print("🛡️ TESTANDO SISTEMA DE SEGURANÇA:")
ativar_modo_seguranca()
simular_sensor_movimento("entrada", True)

# 5. Modos especiais
print("\\n" + "="*50)
print("🎭 TESTANDO MODOS ESPECIAIS:")
modo_cinema()

time.sleep(1)  # Pausa para demonstração

modo_economia_energia()

# 6. Relatório final
print("\\n" + "="*50)
relatorio_status()

print("\\n🎉 SISTEMA DE AUTOMAÇÃO RESIDENCIAL FUNCIONANDO!")
print("\\n💡 FUNCIONALIDADES IMPLEMENTADAS:")
print("• Controle inteligente de iluminação")
print("• Sistema de climatização automático")
print("• Segurança com sensores de movimento")
print("• Modos predefinidos (cinema, economia)")
print("• Relatórios de status e consumo")
print("• Automação baseada em eventos")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Automação Residencial criado!")
        print("🎯 Aplicação real: IoT, smart homes, automação predial")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_10", "Sistema de Automação Residencial", 75)
        
        self.utils.pausar()
    
    def _mini_projeto_modulo_11(self) -> None:
        """Mini Projeto - Módulo 11: Sistema de Análise Financeira Completo"""
        self.utils.limpar_tela()
        self.utils.titulo("🎯 MINI PROJETO: SISTEMA DE ANÁLISE FINANCEIRA COMPLETO")
        
        print("💰 Vamos criar um sistema financeiro profissional integrando tudo!")
        print("🏦 Tipo de sistema usado em:")
        print("• Bancos e fintechs")
        print("• Consultorias financeiras")
        print("• Sistemas de planejamento")
        print("• Apps de controle financeiro")
        
        self.utils.pausar()
        
        print("\n📝 PROJETO FINAL: Analisador Financeiro Pessoal")
        
        codigo_projeto = '''# 💰 SISTEMA DE ANÁLISE FINANCEIRA COMPLETO
# Projeto Final Integrando Todos os Conceitos Python

print("💰 SISTEMA DE ANÁLISE FINANCEIRA COMPLETO")
print("=" * 60)

# Dados financeiros do usuário
receitas_mensais = []
despesas_mensais = []
investimentos = []
metas_financeiras = []

def adicionar_receita(descricao, valor, categoria="Salário"):
    """Adiciona receita ao sistema"""
    receita = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": "2024-01"  # Simplificado para demo
    }
    receitas_mensais.append(receita)
    print(f"✅ Receita adicionada: {descricao} - R$ {valor:.2f}")

def adicionar_despesa(descricao, valor, categoria="Outros"):
    """Adiciona despesa ao sistema"""
    despesa = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": "2024-01"
    }
    despesas_mensais.append(despesa)
    print(f"📝 Despesa adicionada: {descricao} - R$ {valor:.2f}")

def calcular_totais():
    """Calcula totais de receitas e despesas"""
    total_receitas = 0
    for receita in receitas_mensais:
        total_receitas += receita["valor"]
    
    total_despesas = 0
    for despesa in despesas_mensais:
        total_despesas += despesa["valor"]
    
    saldo = total_receitas - total_despesas
    
    return total_receitas, total_despesas, saldo

def analise_categorias():
    """Analisa gastos por categoria"""
    print("\\n📊 ANÁLISE POR CATEGORIAS:")
    print("-" * 40)
    
    # Agrupa despesas por categoria
    categorias_despesas = {}
    for despesa in despesas_mensais:
        categoria = despesa["categoria"]
        if categoria in categorias_despesas:
            categorias_despesas[categoria] += despesa["valor"]
        else:
            categorias_despesas[categoria] = despesa["valor"]
    
    # Calcula percentuais
    total_despesas = sum(categorias_despesas.values())
    
    if total_despesas > 0:
        for categoria, valor in categorias_despesas.items():
            percentual = (valor / total_despesas) * 100
            # Cria barra visual simples
            barras = "█" * int(percentual // 5)
            print(f"{categoria:<15}: R$ {valor:>8.2f} ({percentual:5.1f}%) {barras}")
    else:
        print("Nenhuma despesa registrada.")

def regra_50_30_20(receita_total):
    """Aplica a regra 50-30-20 para planejamento"""
    print("\\n📏 REGRA 50-30-20 - PLANEJAMENTO IDEAL:")
    print("-" * 50)
    
    necessidades = receita_total * 0.50    # 50% necessidades
    desejos = receita_total * 0.30          # 30% desejos
    investimentos = receita_total * 0.20    # 20% investimentos
    
    print(f"💡 Baseado na sua receita de R$ {receita_total:.2f}:")
    print(f"🏠 Necessidades (50%): R$ {necessidades:.2f}")
    print(f"🎯 Desejos (30%):      R$ {desejos:.2f}")
    print(f"💎 Investimentos (20%): R$ {investimentos:.2f}")
    
    return necessidades, desejos, investimentos

def projecao_futuro(saldo_mensal, meses):
    """Projeta economia futura"""
    print(f"\\n🔮 PROJEÇÃO PARA {meses} MESES:")
    print("-" * 30)
    
    if saldo_mensal > 0:
        economia_total = saldo_mensal * meses
        # Simulação de juros compostos (5% ao ano)
        taxa_mensal = 0.05 / 12
        valor_investido = 0
        
        print("Mês | Economia | Investido | Total Acumulado")
        print("-" * 45)
        
        for mes in range(1, meses + 1):
            valor_investido = (valor_investido + saldo_mensal) * (1 + taxa_mensal)
            print(f"{mes:3d} | R$ {saldo_mensal:7.2f} | R$ {valor_investido:8.2f} | R$ {mes * saldo_mensal + (valor_investido - economia_total):11.2f}")
            
            if mes <= 5:  # Mostra apenas os primeiros 5 meses para demo
                continue
    else:
        print("⚠️ Saldo negativo - foque em reduzir despesas!")

def criar_meta_financeira(descricao, valor_meta, prazo_meses):
    """Cria uma meta financeira"""
    meta = {
        "descricao": descricao,
        "valor_meta": valor_meta,
        "prazo_meses": prazo_meses,
        "valor_mensal_necessario": valor_meta / prazo_meses
    }
    metas_financeiras.append(meta)
    
    print(f"\\n🎯 META CRIADA: {descricao}")
    print(f"💰 Valor da meta: R$ {valor_meta:.2f}")
    print(f"📅 Prazo: {prazo_meses} meses")
    print(f"💵 Necessário por mês: R$ {meta['valor_mensal_necessario']:.2f}")

def relatorio_completo():
    """Gera relatório financeiro completo"""
    print("\\n" + "="*60)
    print("📋 RELATÓRIO FINANCEIRO COMPLETO")
    print("="*60)
    
    # Totais gerais
    total_receitas, total_despesas, saldo = calcular_totais()
    
    print(f"\\n💰 RESUMO FINANCEIRO:")
    print(f"Receitas totais:  R$ {total_receitas:>10.2f}")
    print(f"Despesas totais:  R$ {total_despesas:>10.2f}")
    print(f"{'='*35}")
    
    if saldo > 0:
        print(f"Saldo positivo:   R$ {saldo:>10.2f} ✅")
        print("💡 Excelente! Você está economizando!")
    else:
        print(f"Saldo negativo:   R$ {saldo:>10.2f} ⚠️")
        print("💡 Atenção! Revise seus gastos.")
    
    # Análise de categorias
    analise_categorias()
    
    # Aplicação da regra 50-30-20
    if total_receitas > 0:
        regra_50_30_20(total_receitas)
    
    # Metas financeiras
    if metas_financeiras:
        print("\\n🎯 SUAS METAS FINANCEIRAS:")
        for i, meta in enumerate(metas_financeiras, 1):
            print(f"{i}. {meta['descricao']}: R$ {meta['valor_meta']:.2f} em {meta['prazo_meses']} meses")
    
    # Projeção futura
    if saldo > 0:
        projecao_futuro(saldo, 12)
    
    # Dicas personalizadas
    print("\\n💡 DICAS PERSONALIZADAS:")
    if saldo > total_receitas * 0.20:
        print("🌟 Você está poupando muito bem! Continue assim!")
    elif saldo > 0:
        print("👍 Bom trabalho poupando! Tente aumentar um pouco mais.")
    else:
        print("📢 Foque em reduzir despesas desnecessárias.")
        
        # Identifica categoria com maior gasto
        if despesas_mensais:
            maior_categoria = ""
            maior_valor = 0
            categorias = {}
            
            for despesa in despesas_mensais:
                cat = despesa["categoria"]
                if cat in categorias:
                    categorias[cat] += despesa["valor"]
                else:
                    categorias[cat] = despesa["valor"]
            
            for cat, valor in categorias.items():
                if valor > maior_valor:
                    maior_valor = valor
                    maior_categoria = cat
            
            print(f"🎯 Maior gasto: {maior_categoria} (R$ {maior_valor:.2f})")

# DEMONSTRAÇÃO COMPLETA DO SISTEMA
print("\\n🧪 SIMULANDO PERFIL FINANCEIRO REAL:")

# Adicionando receitas
print("\\n1️⃣ ADICIONANDO RECEITAS:")
adicionar_receita("Salário Principal", 4500.00, "Salário")
adicionar_receita("Freelance", 800.00, "Renda Extra")
adicionar_receita("Investimentos", 200.00, "Rendimentos")

# Adicionando despesas
print("\\n2️⃣ ADICIONANDO DESPESAS:")
adicionar_despesa("Aluguel", 1200.00, "Moradia")
adicionar_despesa("Supermercado", 600.00, "Alimentação")
adicionar_despesa("Transporte", 300.00, "Transporte")
adicionar_despesa("Plano de Saúde", 250.00, "Saúde")
adicionar_despesa("Academia", 80.00, "Saúde")
adicionar_despesa("Netflix", 25.00, "Entretenimento")
adicionar_despesa("Restaurantes", 400.00, "Alimentação")
adicionar_despesa("Roupas", 200.00, "Vestuário")

# Criando metas
print("\\n3️⃣ DEFININDO METAS:")
criar_meta_financeira("Emergência (6 meses)", 15000.00, 18)
criar_meta_financeira("Viagem Europa", 8000.00, 12)

# Relatório completo
relatorio_completo()

print("\\n" + "="*60)
print("🎉 SISTEMA FINANCEIRO COMPLETO FUNCIONANDO!")
print("\\n🏆 CONCEITOS PYTHON APLICADOS:")
print("• ✅ Variáveis e tipos de dados")
print("• ✅ Listas e dicionários para armazenar dados")
print("• ✅ Funções para modularizar código")
print("• ✅ Loops para processamento de dados")
print("• ✅ Condicionais para lógica de negócio")
print("• ✅ Operações matemáticas para cálculos")
print("• ✅ Formatação de strings para relatórios")
print("\\n💼 PRONTO PARA O MERCADO DE TRABALHO!")'''
        
        self.utils.exemplo(codigo_projeto)
        self.utils.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Análise Financeira Completo criado!")
        print("🎯 Aplicação real: fintech, planejamento financeiro, consultoria")
        print("\n🎓 VOCÊ COMPLETOU TODOS OS CONCEITOS BÁSICOS DE PYTHON!")
        
        # Registra conclusão do mini projeto
        self.utils.mini_projeto_completo("modulo_11", "Sistema de Análise Financeira Completo", 100)
        
        self.utils.pausar()