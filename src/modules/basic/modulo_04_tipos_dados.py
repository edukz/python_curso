#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 4: Tipos de Dados
Aprenda sobre os tipos fundamentais de dados em Python
"""

from ..shared.base_module import BaseModule


class Modulo04TiposDados(BaseModule):
    """Módulo 4: Tipos de Dados - O DNA das Informações"""
    
    def __init__(self):
        super().__init__("modulo_4", "Tipos de Dados")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo sobre tipos de dados"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._tipos_dados_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _tipos_dados_interativo(self) -> None:
        """Conteúdo principal do módulo Tipos de Dados"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧬 MÓDULO 4: TIPOS DE DADOS - O DNA DAS INFORMAÇÕES")
        else:
            print("\n" + "="*50)
            print("🧬 MÓDULO 4: TIPOS DE DADOS - O DNA DAS INFORMAÇÕES")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Chegou a hora de descobrir os tipos de dados - o DNA da programação!")
        self.print_tip("Este módulo está dividido em seções interativas. Você controla o ritmo!")

        # === FLUXO PRINCIPAL COM TRATAMENTO DE CTRL+C ===

        # 1. Sistema de navegação por seções
        try:
            self._navegacao_secoes_interativas()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Navegação interrompida pelo usuário. Voltando ao menu principal...")
            return

        # 2. Seção de Prática Interativa
        try:
            self._secao_pratica_interativa()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Módulo interrompido pelo usuário. Voltando ao menu principal...")
            return

        # 3. Mini Projeto Prático
        try:
            self._mini_projeto_conversor_universal()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()

    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (7 SEÇÕES RECOMENDADAS) ===
        secoes = [
            {
                'id': 'secao_o_que_sao_tipos',
                'titulo': '🧬 O que são tipos de dados?',
                'descricao': 'Entenda o conceito fundamental dos tipos',
                'funcao': self._secao_o_que_sao_tipos
            },
            {
                'id': 'secao_numeros_inteiros',
                'titulo': '🔢 Números inteiros (int)',
                'descricao': 'Aprenda sobre números sem decimais',
                'funcao': self._secao_numeros_inteiros
            },
            {
                'id': 'secao_numeros_decimais',
                'titulo': '📊 Números decimais (float)',
                'descricao': 'Explore números com vírgula',
                'funcao': self._secao_numeros_decimais
            },
            {
                'id': 'secao_textos_strings',
                'titulo': '📝 Textos e strings',
                'descricao': 'Domine a manipulação de texto',
                'funcao': self._secao_textos_strings
            },
            {
                'id': 'secao_booleanos',
                'titulo': '✅ Verdadeiro/Falso (boolean)',
                'descricao': 'Compreenda os valores lógicos',
                'funcao': self._secao_booleanos
            },
            {
                'id': 'secao_conversoes',
                'titulo': '🔄 Conversões entre tipos',
                'descricao': 'Aprenda a transformar tipos de dados',
                'funcao': self._secao_conversoes
            },
            {
                'id': 'secao_operacoes_tipos',
                'titulo': '🧮 Operações com diferentes tipos',
                'descricao': 'Veja como operar com cada tipo',
                'funcao': self._secao_operacoes_tipos
            }
        ]

        secoes_visitadas = set()

        # === LOOP PRINCIPAL DE NAVEGAÇÃO ===
        while True:
            # Limpa tela e mostra cabeçalho
            self.ui.clear_screen() if self.ui else print("\n" + "="*50)
            self.print_section("NAVEGAÇÃO DO MÓDULO", "📚", "accent")
            self.print_colored("Escolha uma seção para estudar:", "text")

            # Lista todas as seções com status
            print()
            for i, secao in enumerate(secoes, 1):
                status = "✅" if secao['id'] in secoes_visitadas else "📖"
                print(f"{status} {i}. {secao['titulo']}")
                self.print_colored(f"    {secao['descricao']}", "text")
                print()

            print("0. 🎯 Continuar para os Exercícios Práticos")

            # Mostra progresso visual
            progresso = len(secoes_visitadas)
            total = len(secoes)
            self.print_colored(f"\n📊 Progresso: {progresso}/{total} seções visitadas", "info")

            if progresso == total:
                self.print_success("🌟 Você completou todas as seções! Está pronto para praticar!")

            # Processa escolha do usuário
            try:
                escolha = input(f"\n👉 Escolha uma seção (1-{len(secoes)}) ou 0 para continuar: ").strip()

                if escolha == "0":
                    # Verifica se visitou seções suficientes
                    if progresso >= 3:  # Pelo menos 3 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 3 seções antes de continuar!")
                        continuar = input("Quer continuar mesmo assim? (s/n): ").lower()
                        if continuar in ['s', 'sim', 'yes']:
                            break
                elif escolha.isdigit() and 1 <= int(escolha) <= len(secoes):
                    # Executa seção escolhida
                    idx = int(escolha) - 1
                    secoes[idx]['funcao']()
                    secoes_visitadas.add(secoes[idx]['id'])
                else:
                    self.print_warning(f"❌ Opção inválida! Digite um número de 1 a {len(secoes)} ou 0.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Pulando para exercícios práticos...")
                break
            except Exception as e:
                self.print_warning(f"❌ Erro: {str(e)}. Tente novamente.")
    
    def _secao_o_que_sao_tipos(self) -> None:
        """Seção: O que são tipos de dados?"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧬 O QUE SÃO TIPOS DE DADOS?")

        self.print_concept("🧬 Imagine que você tem uma caixa de ferramentas...")
        self.print_colored("Cada ferramenta serve para uma tarefa específica:", "cyan")
        self.print_colored("• Martelo para pregar", "yellow")
        self.print_colored("• Chave de fenda para parafusos", "yellow")
        self.print_colored("• Alicate para segurar", "yellow")
        
        self.print_concept("\n💻 Em programação, os TIPOS DE DADOS são como essas ferramentas!")
        self.print_colored("Cada tipo serve para armazenar e trabalhar com informações diferentes.", "green")
        
        self.print_section("\n🎯 OS 4 TIPOS PRINCIPAIS:")
        self.print_colored("🔢 Inteiros (int): 1, 100, -5 - Para contar coisas", "yellow")
        self.print_colored("📊 Decimais (float): 3.14, 1.75 - Para medir com precisão", "yellow") 
        self.print_colored("📝 Textos (string): 'Ana', \"Python\" - Para palavras", "yellow")
        self.print_colored("✅ Booleanos (bool): True, False - Para decisões", "yellow")
        
        self.print_tip("\n💡 Python escolhe o tipo automaticamente baseado no valor que você atribui!")
        
        codigo = '''# Python detecta os tipos automaticamente
nome = "Maria"        # Automaticamente vira string
idade = 25           # Automaticamente vira int  
altura = 1.65        # Automaticamente vira float
tem_pets = True      # Automaticamente vira bool

print("Nome:", nome, "- Tipo:", type(nome))
print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))
print("Tem pets:", tem_pets, "- Tipo:", type(tem_pets))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_concept("\n🎆 ONDE ISSO É USADO NA VIDA REAL:")
        self.print_colored("🏦 Bancos: CPF (string), saldo (float), idade (int)", "green")
        self.print_colored("🚗 Uber: nome (string), preço (float), disponível (bool)", "green")
        self.print_colored("🎮 Games: nome do jogador (string), pontos (int), vivo (bool)", "green")
        
        self.pausar()

    def _secao_numeros_inteiros(self) -> None:
        """Seção: Números inteiros (int)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔢 NÚMEROS INTEIROS (INT)")

        self.print_concept("🔢 Números inteiros são como peças de LEGO...")
        self.print_colored("Você sempre conta peças inteiras: 1, 2, 3, nunca 2.5 peças!", "cyan")
        
        self.print_section("\n🎯 CARACTERÍSTICAS DOS INTEIROS:")
        self.print_colored("• Números SEM vírgula", "yellow")
        self.print_colored("• Podem ser positivos, negativos ou zero", "yellow")
        self.print_colored("• Perfeitos para contar, indexar, iterar", "yellow")
        
        codigo = '''# Exemplos de números inteiros
idade = 25
temperatura = -10
pontos = 0
quantidade_produtos = 100
andar_predio = 15

print("👤 Idade:", idade)
print("🌡️ Temperatura:", temperatura)
print("🎮 Pontos:", pontos)
print("📦 Produtos:", quantidade_produtos)
print("🏢 Andar:", andar_predio)

# Verificando o tipo
print("\nTodos são do tipo:", type(idade))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n🧮 OPERAÇÕES COM INTEIROS:")
        
        codigo2 = '''a = 10
b = 3

print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto da divisão: {a} % {b} = {a % b}")
print(f"Potência: {a} ** {b} = {a ** b}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_tip("\n💡 DICA PRO: Use // para divisão inteira e % para resto!")
        
        self.print_concept("\n🎆 USOS PROFISSIONAIS:")
        self.print_colored("📈 Índices de listas e arrays", "green")
        self.print_colored("🔁 Contadores em loops", "green")
        self.print_colored("📅 Anos, meses, dias", "green")
        self.print_colored("📊 IDs de bancos de dados", "green")
        
        self.pausar()

    def _secao_numeros_decimais(self) -> None:
        """Seção: Números decimais (float)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 NÚMEROS DECIMAIS (FLOAT)")

        self.print_concept("📊 Números decimais são como réguas de precisão...")
        self.print_colored("Você pode medir 1.75m, 3.14159, valores mais exatos!", "cyan")
        
        self.print_section("\n🎯 CARACTERÍSTICAS DOS DECIMAIS:")
        self.print_colored("• Números COM ponto decimal (não vírgula!)", "yellow")
        self.print_colored("• Permitem precisão em medidas", "yellow")
        self.print_colored("• Essenciais para cálculos financeiros", "yellow")
        
        codigo = '''# Exemplos de números decimais
preco = 29.99
altura = 1.75
pi = 3.14159
temperatura = 36.5
percentual = 0.15  # 15%

print("💰 Preço: R$", preco)
print("📏 Altura:", altura, "metros")
print("🔢 Pi:", pi)
print("🌡️ Temperatura:", temperatura, "°C")
print("📊 Percentual:", percentual * 100, "%")

# Verificando o tipo
print("\nTodos são do tipo:", type(preco))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n🧮 CÁLCULOS COM DECIMAIS:")
        
        codigo2 = '''# Cálculos financeiros precisos
preco_produto = 25.90
quantidade = 3
taxa_imposto = 0.10  # 10%

subtotal = preco_produto * quantidade
imposto = subtotal * taxa_imposto
total = subtotal + imposto

print(f"Preço unitário: R$ {preco_produto:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Imposto (10%): R$ {imposto:.2f}")
print(f"Total: R$ {total:.2f}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_tip("\n💡 DICA PRO: Use :.2f para mostrar apenas 2 casas decimais!")
        
        self.print_concept("\n🎆 USOS PROFISSIONAIS:")
        self.print_colored("💰 Preços e valores monetários", "green")
        self.print_colored("📉 Percentuais e taxas", "green")
        self.print_colored("🗺 Coordenadas GPS", "green")
        self.print_colored("🧮 Cálculos científicos", "green")
        
        self.pausar()

    def _secao_textos_strings(self) -> None:
        """Seção: Textos e strings"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📝 TEXTOS E STRINGS")

        self.print_concept("📝 Strings são como colares de pérolas...")
        self.print_colored("Cada letra é uma pérola, juntas formam palavras e frases!", "cyan")
        
        self.print_section("\n🎯 CARACTERÍSTICAS DAS STRINGS:")
        self.print_colored("• Sempre entre aspas: 'simples' ou \"duplas\"", "yellow")
        self.print_colored("• Podem conter letras, números, símbolos", "yellow")
        self.print_colored("• São imutáveis (não mudam, criam novas)", "yellow")
        
        codigo = '''# Diferentes formas de criar strings
nome = "Maria Silva"
cidade = 'São Paulo'
email = "maria@email.com"
telefone = "(11) 99999-9999"  # Número como texto!
mensagem = """Esta é uma string
multi-linhas!"""

print("👤 Nome:", nome)
print("🏢 Cidade:", cidade)
print("✉️ Email:", email)
print("📱 Telefone:", telefone)
print("💬 Mensagem:", mensagem)

# Verificando o tipo
print("\nTodos são do tipo:", type(nome))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n🔧 OPERAÇÕES COM STRINGS:")
        
        codigo2 = '''nome = "Ana"
sobrenome = "Silva"

# Concatenação (juntar)
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

# Repetição
grito = "Python! " * 3
print("Grito:", grito)

# Tamanho
print("Tamanho do nome:", len(nome_completo))

# Maiúscula/minúscula
print("Maiúsculo:", nome_completo.upper())
print("Minúsculo:", nome_completo.lower())
print("Primeira maiúscula:", nome_completo.title())'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_tip("\n💡 DICA PRO: Use f-strings para formatar texto: f'Olá, {nome}!'")
        
        codigo3 = '''# F-strings - a forma moderna!
nome = "Carlos"
idade = 30
salario = 5000.50

# Forma antiga (não recomendada)
mensagem_antiga = "Olá, " + nome + ", você tem " + str(idade) + " anos"

# Forma moderna com f-string
mensagem_nova = f"Olá, {nome}, você tem {idade} anos e ganha R$ {salario:.2f}"

print("Forma antiga:", mensagem_antiga)
print("Forma moderna:", mensagem_nova)'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_concept("\n🎆 USOS PROFISSIONAIS:")
        self.print_colored("📄 Nomes, endereços, descrições", "green")
        self.print_colored("🔐 Senhas e tokens (como texto)", "green")
        self.print_colored("📧 Mensagens e notificações", "green")
        self.print_colored("📈 Logs e relatórios", "green")
        
        self.pausar()

    def _secao_booleanos(self) -> None:
        """Seção: Verdadeiro/Falso (boolean)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ VERDADEIRO/FALSO (BOOLEAN)")

        self.print_concept("✅ Booleanos são como interruptores de luz...")
        self.print_colored("Ou está ligado (True) ou desligado (False). Simples assim!", "cyan")
        
        self.print_section("\n🎯 CARACTERÍSTICAS DOS BOOLEANOS:")
        self.print_colored("• Apenas DOIS valores: True ou False", "yellow")
        self.print_colored("• SEMPRE com primeira letra maiúscula", "yellow")
        self.print_colored("• Base de toda lógica de programação", "yellow")
        
        codigo = '''# Exemplos de valores booleanos
esta_logado = True
tem_desconto = False
e_maior_idade = True
aceita_termos = False
tem_estoque = True

print("🔑 Está logado?", esta_logado)
print("🏷️ Tem desconto?", tem_desconto)
print("👤 É maior de idade?", e_maior_idade)
print("📜 Aceita termos?", aceita_termos)
print("📦 Tem estoque?", tem_estoque)

# Verificando o tipo
print("\nTodos são do tipo:", type(esta_logado))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n🧮 OPERAÇÕES LÓGICAS:")
        
        codigo2 = '''# Operações lógicas com booleanos
tem_carteira = True
e_maior_idade = True
tem_dinheiro = False

# AND - todas as condições devem ser verdadeiras
pode_dirigir = tem_carteira and e_maior_idade
print("Pode dirigir?", pode_dirigir)

# OR - pelo menos uma condição deve ser verdadeira
pode_comprar = tem_carteira or tem_dinheiro
print("Pode comprar?", pode_comprar)

# NOT - inverte o valor
nao_tem_dinheiro = not tem_dinheiro
print("Não tem dinheiro?", nao_tem_dinheiro)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("\n🔍 CONVERSÕES PARA BOOLEAN:")
        
        codigo3 = '''# Diferentes valores convertidos para boolean
print("=== VALORES QUE VIRAM True ===")
print("bool(1):", bool(1))
print("bool(-1):", bool(-1))
print("bool('Python'):", bool("Python"))
print("bool([1, 2, 3]):", bool([1, 2, 3]))

print("\n=== VALORES QUE VIRAM False ===")
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool(None):", bool(None))'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_tip("\n💡 DICA PRO: 0, string vazia, lista vazia = False. Todo resto = True!")
        
        self.print_concept("\n🎆 USOS PROFISSIONAIS:")
        self.print_colored("🔑 Controle de acesso (logado/não logado)", "green")
        self.print_colored("🟢 Status de sistemas (ativo/inativo)", "green")
        self.print_colored("🛍️ E-commerce (tem estoque/sem estoque)", "green")
        self.print_colored("⚙️ Configurações (ligado/desligado)", "green")
        
        self.pausar()

    def _secao_conversoes(self) -> None:
        """Seção: Conversões entre tipos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔄 CONVERSÕES ENTRE TIPOS")

        self.print_concept("🔄 Conversões são como tradutores...")
        self.print_colored("Eles transformam informações de um 'idioma' para outro!", "cyan")
        
        self.print_section("\n🎯 FUNÇÕES DE CONVERSÃO:")
        self.print_colored("• int() - converte para inteiro", "yellow")
        self.print_colored("• float() - converte para decimal", "yellow")
        self.print_colored("• str() - converte para texto", "yellow")
        self.print_colored("• bool() - converte para boolean", "yellow")
        
        codigo = '''# Convertendo string para números
numero_texto = "123"
print("Original:", numero_texto, "- Tipo:", type(numero_texto))

numero_int = int(numero_texto)
print("Como int:", numero_int, "- Tipo:", type(numero_int))

numero_float = float(numero_texto)
print("Como float:", numero_float, "- Tipo:", type(numero_float))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n📊 CONVERSÕES COM DECIMAIS:")
        
        codigo2 = '''# Convertendo números para texto
idade = 25
preco = 49.90

idade_texto = str(idade)
preco_texto = str(preco)

print("Idade como número:", idade, "- Tipo:", type(idade))
print("Idade como texto:", idade_texto, "- Tipo:", type(idade_texto))

print("Preço como número:", preco, "- Tipo:", type(preco))
print("Preço como texto:", preco_texto, "- Tipo:", type(preco_texto))

# Agora posso usar em f-strings facilmente
mensagem = f"Você tem {idade} anos e o produto custa R$ {preco}"
print("\nMensagem:", mensagem)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_warning("\n⚠️ CUIDADOS COM CONVERSÕES:")
        
        codigo3 = '''# Conversões que podem dar erro
print("=== CONVERSÕES PROBLEMÁTICAS ===")

try:
    numero = int("abc")  # Não dá!
except ValueError:
    print("❌ Não posso converter 'abc' para número")

try:
    numero = int("3.14")  # Também não dá direto!
except ValueError:
    print("❌ Não posso converter '3.14' direto para int")
    
print("\n=== SOLUÇÕES CORRETAS ===")
# Para string com decimal, primeiro float, depois int
numero_correto = int(float("3.14"))
print("✅ '3.14' -> float -> int:", numero_correto)

# Sempre validar entrada do usuário
entrada = "100"
if entrada.isdigit():
    numero = int(entrada)
    print(f"✅ Conversão segura: {numero}")
else:
    print("❌ Entrada inválida para número")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_tip("\n💡 DICA PRO: Sempre valide antes de converter. Use try/except para segurança!")
        
        self.print_concept("\n🎆 USOS PROFISSIONAIS:")
        self.print_colored("💱 Entrada de usuário (sempre string → número)", "green")
        self.print_colored("📄 Leitura de arquivos CSV/Excel", "green")
        self.print_colored("🌐 APIs (JSON sempre vem como string)", "green")
        self.print_colored("📊 Análise de dados (limpeza de tipos)", "green")
        
        self.pausar()

    def _secao_operacoes_tipos(self) -> None:
        """Seção: Operações com diferentes tipos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧮 OPERAÇÕES COM DIFERENTES TIPOS")

        self.print_concept("🧮 Cada tipo tem suas próprias 'superpowers'!")
        self.print_colored("Vamos ver o que cada um pode fazer...", "cyan")
        
        self.print_section("\n🔢 OPERAÇÕES COM INTEIROS:")
        
        codigo = '''# Aritmética com inteiros
a = 15
b = 4

print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto: {a} % {b} = {a % b}")
print(f"Potência: {a} ** {b} = {a ** b}")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_section("\n📊 OPERAÇÕES COM DECIMAIS:")
        
        codigo2 = '''# Cálculos financeiros precisos
preco_base = 100.0
desconto = 0.15  # 15%
taxa = 0.05      # 5%

valor_desconto = preco_base * desconto
preco_com_desconto = preco_base - valor_desconto
taxa_aplicada = preco_com_desconto * taxa
preco_final = preco_com_desconto + taxa_aplicada

print(f"Preço base: R$ {preco_base:.2f}")
print(f"Desconto (15%): R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
print(f"Taxa (5%): R$ {taxa_aplicada:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("\n📝 OPERAÇÕES COM STRINGS:")
        
        codigo3 = '''# Manipulação avançada de strings
nome = "  Ana Maria da Silva  "
email = "ANA.SILVA@EMAIL.COM"

# Limpeza e formatação
nome_limpo = nome.strip()  # Remove espaços
nome_titulo = nome_limpo.title()  # Primeira letra maiúscula
email_limpo = email.lower()  # Tudo minúsculo

print(f"Nome original: '{nome}'")
print(f"Nome limpo: '{nome_limpo}'")
print(f"Nome formatado: '{nome_titulo}'")
print(f"Email original: '{email}'")
print(f"Email formatado: '{email_limpo}'")

# Divisão de strings
partes_nome = nome_titulo.split()
print(f"\nPartes do nome: {partes_nome}")
print(f"Primeiro nome: {partes_nome[0]}")
print(f"Sobrenome: {partes_nome[-1]}")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_section("\n✅ OPERAÇÕES COM BOOLEANOS:")
        
        codigo4 = '''# Lógica complexa com booleanos
idade = 20
tem_carteira = True
tem_carro = False
tem_dinheiro = True

# Condições compostas
e_maior_idade = idade >= 18
pode_dirigir = e_maior_idade and tem_carteira
pode_viajar = pode_dirigir and (tem_carro or tem_dinheiro)

print(f"Idade: {idade}")
print(f"É maior de idade: {e_maior_idade}")
print(f"Tem carteira: {tem_carteira}")
print(f"Pode dirigir: {pode_dirigir}")
print(f"Tem carro: {tem_carro}")
print(f"Tem dinheiro: {tem_dinheiro}")
print(f"Pode viajar: {pode_viajar}")'''
        
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        self.print_tip("\n💡 DICA PRO: Combine diferentes tipos para criar lógica poderosa!")
        
        self.print_concept("\n🎆 EXEMPLO REAL - VALIDAÇÃO DE USUÁRIO:")
        
        codigo5 = '''# Sistema real de validação
nome_usuario = "  Maria123  "
idade_str = "25"
email = "maria@teste.com"
aceita_termos = True

# Validações
nome_valido = len(nome_usuario.strip()) >= 3
idade_valida = idade_str.isdigit() and int(idade_str) >= 18
email_valido = "@" in email and "." in email
termos_aceitos = aceita_termos == True

# Resultado final
usuario_aprovado = nome_valido and idade_valida and email_valido and termos_aceitos

print(f"Nome '{nome_usuario.strip()}' é válido: {nome_valido}")
print(f"Idade '{idade_str}' é válida: {idade_valida}")
print(f"Email '{email}' é válido: {email_valido}")
print(f"Termos aceitos: {termos_aceitos}")
print(f"\n🎆 USUÁRIO APROVADO: {usuario_aprovado}")'''
        
        self.exemplo(codigo5)
        self.executar_codigo(codigo5)
        
        self.print_concept("\n🎆 ONDE ISSO É USADO:")
        self.print_colored("🔑 Sistemas de login e cadastro", "green")
        self.print_colored("💳 Validação de cartão de crédito", "green")
        self.print_colored("🎮 Games (sistema de pontuação)", "green")
        self.print_colored("📈 Dashboards financeiros", "green")
        
        self.pausar()

    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        if self.ui:
            self.ui.clear_screen()
            
        # Flag para indicar que estamos em seção de prática (evita interferência)
        if hasattr(self.progress, 'set_in_practice_section'):
            self.progress.set_in_practice_section(True)
            
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")

        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")

        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("0. Continuar para o Mini Projeto")

            try:
                escolha = input("\n👉 Sua escolha: ").strip().lower()

                if escolha in ["0", "continuar", "sair", "proximo"]:
                    break
                elif escolha in ["1", "quiz", "conhecimentos"]:
                    try:
                        self._exercicio_quiz_tipos_dados()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._exercicio_completar_codigo()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo"]:
                    try:
                        self._exercicio_criativo_tipos()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício criativo. Continuando...")
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
        
        # Limpa flag de seção de prática
        if hasattr(self.progress, 'set_in_practice_section'):
            self.progress.set_in_practice_section(False)

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre tipos de dados",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie seu perfil pessoal usando todos os tipos",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto final",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para aprender melhor!"
        ]

        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()

        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _exercicio_quiz_tipos_dados(self) -> None:
        """Quiz sobre tipos de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧠 QUIZ RÁPIDO - TIPOS DE DADOS")

        self.print_colored("🧠 Vamos testar seus conhecimentos com 5 perguntas!", "info")
        
        perguntas = [
            {
                'pergunta': 'Qual é o tipo de dados do valor 42?',
                'opcoes': ['A) string', 'B) float', 'C) int', 'D) boolean'],
                'resposta_correta': 'C',
                'explicacao': '42 é um número inteiro, sem decimais, portanto é do tipo int.'
            },
            {
                'pergunta': 'Como converter a string "123" para inteiro?',
                'opcoes': ['A) str("123")', 'B) int("123")', 'C) float("123")', 'D) bool("123")'],
                'resposta_correta': 'B',
                'explicacao': 'A função int() converte strings numéricas para inteiros.'
            },
            {
                'pergunta': 'Qual valor booleano representa "falso"?',
                'opcoes': ['A) false', 'B) FALSE', 'C) False', 'D) 0'],
                'resposta_correta': 'C',
                'explicacao': 'Em Python, False deve ser escrito com F maiúsculo.'
            },
            {
                'pergunta': 'Qual é o resultado de bool("") (string vazia)?',
                'opcoes': ['A) True', 'B) False', 'C) Erro', 'D) 0'],
                'resposta_correta': 'B',
                'explicacao': 'String vazia ("") é considerada "falsa" em Python, retorna False.'
            },
            {
                'pergunta': 'Qual operação é válida com strings?',
                'opcoes': ['A) "Ana" - "Silva"', 'B) "Ana" + "Silva"', 'C) "Ana" / "Silva"', 'D) "Ana" % "Silva"'],
                'resposta_correta': 'B',
                'explicacao': 'Strings podem ser concatenadas com o operador +.'
            }
        ]
        
        acertos = 0
        for i, pergunta in enumerate(perguntas, 1):
            self.print_section(f"📝 PERGUNTA {i}/5", "📝")
            self.print_colored(f"\n{pergunta['pergunta']}", "warning")
            print()
            for opcao in pergunta['opcoes']:
                self.print_colored(f"  {opcao}", "yellow")
            
            while True:
                resposta = input("\n🎯 Sua resposta (A, B, C ou D): ").upper().strip()
                if resposta in ['A', 'B', 'C', 'D']:
                    break
                self.print_warning("⚠️ Digite apenas A, B, C ou D")
            
            if resposta == pergunta['resposta_correta']:
                self.print_success(f"✅ CORRETO! {pergunta['explicacao']}")
                acertos += 1
            else:
                self.print_colored(f"❌ Incorreto. {pergunta['explicacao']}", "error")
            
            self.pausar()
        
        # Resultado final
        percentual = (acertos / len(perguntas)) * 100
        if percentual >= 80:
            self.print_success(f"\n🎆 EXCELENTE! Você acertou {acertos}/5 ({percentual:.0f}%)")
        elif percentual >= 60:
            self.print_colored(f"\n💪 BOM! Você acertou {acertos}/5 ({percentual:.0f}%)", "yellow")
        else:
            self.print_colored(f"\n📚 Continue estudando! Você acertou {acertos}/5 ({percentual:.0f}%)", "cyan")

    def _exercicio_completar_codigo(self) -> None:
        """Exercícios de completar código"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔧 COMPLETAR CÓDIGO - TIPOS DE DADOS")

        self.print_colored("🔧 Agora vamos completar trechos de código!", "info")
        self.print_tip("Vou mostrar código incompleto e você me diz o que está faltando.")
        
        exercicios = [
            {
                'titulo': 'Conversão de tipos',
                'codigo_incompleto': '''idade_texto = "25"
# Converter para número inteiro
idade = ______(idade_texto)
print("Idade:", idade)''',
                'resposta_correta': 'int',
                'codigo_completo': '''idade_texto = "25"
# Converter para número inteiro
idade = int(idade_texto)
print("Idade:", idade)''',
                'explicacao': 'Use int() para converter string para inteiro.'
            },
            {
                'titulo': 'Operações com strings',
                'codigo_incompleto': '''nome = "Ana"
sobrenome = "Silva"
# Juntar nome e sobrenome
nome_completo = nome ____ " " ____ sobrenome
print(nome_completo)''',
                'resposta_correta': '+',
                'codigo_completo': '''nome = "Ana"
sobrenome = "Silva"
# Juntar nome e sobrenome
nome_completo = nome + " " + sobrenome
print(nome_completo)''',
                'explicacao': 'Use + para concatenar (juntar) strings.'
            },
            {
                'titulo': 'Descobrir tipo de dados',
                'codigo_incompleto': '''valor = 3.14
# Descobrir o tipo
tipo_valor = ______(valor)
print("Tipo:", tipo_valor)''',
                'resposta_correta': 'type',
                'codigo_completo': '''valor = 3.14
# Descobrir o tipo
tipo_valor = type(valor)
print("Tipo:", tipo_valor)''',
                'explicacao': 'Use type() para descobrir o tipo de uma variável.'
            }
        ]
        
        for i, exercicio in enumerate(exercicios, 1):
            self.print_section(f"📝 EXERCÍCIO {i}/3: {exercicio['titulo']}", "📝")
            self.print_colored("\nCódigo incompleto:", "warning")
            self.exemplo(exercicio['codigo_incompleto'])
            
            resposta = input("\n🎯 O que deve substituir os ______ ? ").strip()
            
            if resposta.lower() == exercicio['resposta_correta'].lower():
                self.print_success(f"✅ CORRETO! {exercicio['explicacao']}")
                self.print_colored("\nCódigo completo:", "success")
                self.exemplo(exercicio['codigo_completo'])
                self.executar_codigo(exercicio['codigo_completo'])
            else:
                self.print_colored(f"❌ Não foi dessa vez. A resposta era: {exercicio['resposta_correta']}", "error")
                self.print_colored(exercicio['explicacao'], "yellow")
                self.print_colored("\nCódigo correto:", "info")
                self.exemplo(exercicio['codigo_completo'])
            
            self.pausar()

    def _exercicio_criativo_tipos(self) -> None:
        """Exercício criativo com tipos de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎨 EXERCÍCIO CRIATIVO - PERFIL PESSOAL")

        self.print_colored("🎨 Vamos criar um programa que usa TODOS os tipos de dados!", "info")
        self.print_tip("Você vai criar um 'Perfil Pessoal' usando int, float, string e bool.")
        
        self.print_section("🎯 DESAFIO", "🎯")
        self.print_colored("Crie variáveis para:", "cyan")
        self.print_colored("• Seu nome (string)", "yellow")
        self.print_colored("• Sua idade (int)", "yellow")
        self.print_colored("• Sua altura em metros (float)", "yellow")
        self.print_colored("• Se você gosta de programação (bool)", "yellow")
        
        print("\n" + "-"*50)
        print("📝 Digite suas informações:")
        
        try:
            # Coletar dados do usuário
            nome = input("👤 Seu nome: ").strip()
            idade_str = input("🎂 Sua idade: ").strip()
            altura_str = input("📏 Sua altura (ex: 1.75): ").strip()
            gosta_programacao_str = input("💻 Gosta de programação? (sim/nao): ").strip().lower()
            
            # Validar e converter
            if not nome:
                nome = "Programador(a) Python"
            
            try:
                idade = int(idade_str) if idade_str.isdigit() else 25
            except:
                idade = 25
                
            try:
                altura = float(altura_str.replace(',', '.')) if altura_str else 1.70
            except:
                altura = 1.70
                
            gosta_programacao = gosta_programacao_str in ['sim', 's', 'yes', 'y', 'true']
            
            # Gerar perfil personalizado
            if self.ui:
                self.ui.clear_screen()
                self.ui.header("🎆 SEU PERFIL PESSOAL")
            
            codigo_gerado = f'''# 🎆 PERFIL PESSOAL GERADO
# Usando todos os tipos de dados!

# Dados pessoais (diferentes tipos)
nome = "{nome}"                    # string
idade = {idade}                          # int
altura = {altura}                      # float
gosta_programacao = {gosta_programacao}     # boolean

# Cálculos automáticos
idade_meses = idade * 12                 # int operation
anos_restantes_100 = 100 - idade         # int operation
imc_aproximado = 70 / (altura ** 2)      # float operation (peso estimado)

# Análises
e_adulto = idade >= 18                   # boolean comparison
alta_estatura = altura > 1.75             # boolean comparison
perfil_tech = gosta_programacao and e_adulto  # boolean logic

# Exibir perfil completo
print("🎆" * 15)
print("   PERFIL PESSOAL")
print("🎆" * 15)

print(f"\n👤 Nome: {{nome}} (tipo: {{type(nome).__name__}})")
print(f"🎂 Idade: {{idade}} anos (tipo: {{type(idade).__name__}})")
print(f"📏 Altura: {{altura}}m (tipo: {{type(altura).__name__}})")
print(f"💻 Gosta de Python: {{gosta_programacao}} (tipo: {{type(gosta_programacao).__name__}})")

print(f"\n📈 CÁLCULOS:")
print(f"Idade em meses: {{idade_meses}}")
print(f"Anos para chegar aos 100: {{anos_restantes_100}}")
print(f"IMC aproximado: {{imc_aproximado:.1f}}")

print(f"\n🎯 ANÁLISES:")
print(f"É adulto: {{e_adulto}}")
print(f"Tem altura alta: {{alta_estatura}}")
print(f"Perfil tech: {{perfil_tech}}")

print("\n🎆" * 15)
print("  PERFIL COMPLETO!")
print("🎆" * 15)'''
            
            self.print_colored("\n💻 Seu código gerado:", "success")
            self.exemplo(codigo_gerado)
            
            print("\n" + "="*50)
            print("🎬 EXECUTANDO SEU PERFIL:")
            print("="*50)
            
            # Executar o código personalizado
            exec(codigo_gerado.split('# Exibir perfil completo')[1])
            
            self.print_success("\n🎉 INCRÍVEL! Você usou todos os tipos de dados!")
            self.print_colored("\n💡 OBSERVE:", "info")
            self.print_colored(f"• String: '{nome}' para armazenar texto", "green")
            self.print_colored(f"• Int: {idade} para números inteiros", "green")
            self.print_colored(f"• Float: {altura} para números decimais", "green")
            self.print_colored(f"• Bool: {gosta_programacao} para valores lógicos", "green")
            
        except KeyboardInterrupt:
            raise
        except Exception as e:
            self.print_colored(f"❌ Erro no exercício: {e}", "error")
            self.print_tip("Tudo bem! O importante é praticar.")
        
        self.pausar()

    def _mini_projeto_conversor_universal(self) -> None:
        """Mini Projeto - Módulo 4: Conversor Universal de Dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CONVERSOR UNIVERSAL DE DADOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CONVERSOR UNIVERSAL DE DADOS")
            print("="*50)
        
        self.print_success("🔄 Vamos criar um conversor que trabalha com todos os tipos de dados!")
        self.print_colored("Sistema similar aos usados em:", "cyan")
        self.print_colored("• Planilhas (Excel, Google Sheets)", "green")
        self.print_colored("• Bancos de dados (limpeza de dados)", "green")
        self.print_colored("• APIs (conversão de formatos)", "green")
        self.print_colored("• Sistemas de importação de dados", "green")
        
        self.print_section("💻 Programa completo usando todos os tipos de dados", "💻")
        
        codigo_completo = '''# 🔄 CONVERSOR UNIVERSAL DE DADOS
print("🔄" * 20)
print("   CONVERSOR UNIVERSAL")
print("🔄" * 20)

# === DADOS DE ENTRADA (simulando entrada de usuário) ===
entradas = [
    "123",           # string que parece inteiro
    "45.67",         # string que parece float
    "true",          # string que parece boolean
    "Python",        # string comum
    "0",             # string zero
    "",              # string vazia
    "false",         # string false
    "99.99",         # string preço
    "2024",          # string ano
    "sim"            # string boolean em português
]

print(f"\\n📊 DADOS PARA CONVERTER ({len(entradas)} itens):")
for i, entrada in enumerate(entradas, 1):
    print(f"{i:2d}. '{entrada}' (tipo: {type(entrada).__name__})")

# === SISTEMA DE CONVERSÃO INTELIGENTE ===
resultados = {
    'inteiros': [],
    'decimais': [],
    'booleanos': [],
    'textos': [],
    'erros': []
}

print(f"\\n🧮 PROCESSANDO CONVERSÕES...")
print("-" * 50)

for entrada in entradas:
    print(f"\\n🔍 Analisando: '{entrada}'")
    
    # Tentar converter para inteiro
    try:
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            valor_int = int(entrada)
            resultados['inteiros'].append((entrada, valor_int))
            print(f"  ✅ Inteiro: {valor_int}")
            continue
    except ValueError:
        pass
    
    # Tentar converter para decimal
    try:
        if '.' in entrada and entrada.replace('.', '').replace('-', '').isdigit():
            valor_float = float(entrada)
            resultados['decimais'].append((entrada, valor_float))
            print(f"  ✅ Decimal: {valor_float}")
            continue
    except ValueError:
        pass
    
    # Tentar converter para boolean
    if entrada.lower() in ['true', 'false', 'sim', 'nao', '1', '0']:
        valor_bool = entrada.lower() in ['true', 'sim', '1']
        resultados['booleanos'].append((entrada, valor_bool))
        print(f"  ✅ Boolean: {valor_bool}")
        continue
    
    # Se não conseguiu converter, manter como string
    if entrada:  # String não vazia
        resultados['textos'].append((entrada, entrada))
        print(f"  ✅ Texto: '{entrada}'")
    else:  # String vazia
        resultados['textos'].append((entrada, "[vazio]"))
        print(f"  ✅ Texto vazio: '[vazio]'")

# === RELATÓRIO FINAL ===
print(f"\\n📈 RELATÓRIO DE CONVERSÃO:")
print("=" * 50)

print(f"\\n🔢 INTEIROS CONVERTIDOS ({len(resultados['inteiros'])}):")
for original, convertido in resultados['inteiros']:
    print(f"  '{original}' → {convertido} (tipo: {type(convertido).__name__})")

print(f"\\n📊 DECIMAIS CONVERTIDOS ({len(resultados['decimais'])}):")
for original, convertido in resultados['decimais']:
    print(f"  '{original}' → {convertido} (tipo: {type(convertido).__name__})")

print(f"\\n✅ BOOLEANOS CONVERTIDOS ({len(resultados['booleanos'])}):")
for original, convertido in resultados['booleanos']:
    print(f"  '{original}' → {convertido} (tipo: {type(convertido).__name__})")

print(f"\\n📝 TEXTOS MANTIDOS ({len(resultados['textos'])}):")
for original, convertido in resultados['textos']:
    print(f"  '{original}' → '{convertido}' (tipo: {type(convertido).__name__})")

# === ESTATÍSTICAS FINAIS ===
total_processados = len(entradas)
total_convertidos = len(resultados['inteiros']) + len(resultados['decimais']) + len(resultados['booleanos'])
total_textos = len(resultados['textos'])

print(f"\\n📈 ESTATÍSTICAS:")
print(f"Total processado: {total_processados} itens")
print(f"Convertidos: {total_convertidos} itens ({total_convertidos/total_processados*100:.1f}%)")
print(f"Mantidos como texto: {total_textos} itens ({total_textos/total_processados*100:.1f}%)")

print("\\n🔄" * 20)
print("   CONVERSÃO CONCLUÍDA!")
print("🔄" * 20)'''
        
        self.exemplo(codigo_completo)
        self.executar_codigo(codigo_completo)
        
        self.print_success("\n🎉 CONVERSOR UNIVERSAL CRIADO COM SUCESSO!")
        self.print_colored("\n🌍 ONDE ISSO É USADO:", "info")
        self.print_colored("• 📊 Excel/Google Sheets: Detecção automática de tipos", "green")
        self.print_colored("• 📊 Bancos de dados: Limpeza e normalização", "green")
        self.print_colored("• 🌐 APIs: Conversão JSON/XML para tipos nativos", "green")
        self.print_colored("• 🤖 Machine Learning: Pré-processamento de dados", "green")
        self.print_colored("• 📄 Sistemas ETL: Extração e transformação", "green")
        
        self.print_colored("\n💡 TÉCNICAS PROFISSIONAIS USADAS:", "info")
        self.print_colored("• Validação de entrada com isdigit()", "yellow")
        self.print_colored("• Tratamento de exceções com try/except", "yellow")
        self.print_colored("• Lógica condicional para detecção de tipos", "yellow")
        self.print_colored("• Estruturas de dados para organizar resultados", "yellow")
        self.print_colored("• Cálculo de estatísticas e percentuais", "yellow")
        
        self.print_success("\n🏆 CONQUISTA: Especialista em Tipos de Dados!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Conversor Universal de Dados")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo04TiposDados()
    print("Teste do módulo 4 - versão standalone")
    module._tipos_dados_interativo()