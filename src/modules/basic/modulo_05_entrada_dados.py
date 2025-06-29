#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 5: Entrada de Dados
Como receber informações do usuário de forma interativa
"""

from ..shared.base_module import BaseModule


class Modulo05EntradaDados(BaseModule):
    """Módulo 5: Entrada de Dados - Interação com o usuário"""
    
    def __init__(self):
        super().__init__("modulo_5", "Entrada de Dados")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo sobre entrada de dados"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._entrada_dados_interativa()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _entrada_dados_interativa(self) -> None:
        """Conteúdo principal do módulo entrada de dados"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📝 MÓDULO 5: ENTRADA DE DADOS")
        else:
            print("\n" + "="*50)
            print("📝 MÓDULO 5: ENTRADA DE DADOS")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Agora seus programas vão conversar com o usuário!")
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
            self._mini_projeto_questionario_personalizado()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return
        
        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""
        
        # === DEFINIÇÃO DAS SEÇÕES ===
        secoes = [
            {
                'id': 'secao_conceito_input',
                'titulo': '🎯 O que é entrada de dados?',
                'descricao': 'Entenda como programas recebem informações',
                'funcao': self._secao_conceito_input
            },
            {
                'id': 'secao_funcao_input',
                'titulo': '⚙️ Como a função input() funciona?',
                'descricao': 'Veja o processo passo a passo',
                'funcao': self._secao_funcao_input
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Exemplos práticos',
                'descricao': 'Veja entrada de dados em ação',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_tipos_conversao',
                'titulo': '🔄 Conversão de tipos',
                'descricao': 'Transforme texto em números',
                'funcao': self._secao_tipos_conversao
            },
            {
                'id': 'secao_formatacao_saida',
                'titulo': '🎨 Formatação de saída',
                'descricao': 'Deixe suas mensagens mais bonitas',
                'funcao': self._secao_formatacao_saida
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Aprenda com os erros mais frequentes',
                'funcao': self._secao_erros_comuns
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre interação',
                'descricao': 'Fatos interessantes sobre interfaces',
                'funcao': self._secao_curiosidades
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
    
    def _secao_conceito_input(self) -> None:
        """Seção: O que é entrada de dados?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É ENTRADA DE DADOS?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Entrada de Dados",
            "É quando um programa 'pergunta' algo para o usuário e\nespera uma resposta para continuar funcionando."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("É como uma conversa: o programa fala, você responde!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine um caixa do supermercado perguntando: 'Vai ser dinheiro ou cartão?'", "text")
        self.print_colored("Ele precisa da sua resposta para continuar o processo!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. O programa mostra uma pergunta na tela",
            "2. O cursor fica piscando esperando você digitar",
            "3. Você digita a resposta e pressiona ENTER",
            "4. O programa guarda sua resposta numa variável"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Perguntando o nome do usuário
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Prazer em conhecê-lo!")'''
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Caixas eletrônicos pedem sua senha",
            "Apps de delivery perguntam seu endereço",
            "Jogos pedem seu nome de usuário",
            "Sites de compra pedem dados do cartão"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_funcao_input(self) -> None:
        """Seção: Como a função input() funciona?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO A FUNÇÃO INPUT() FUNCIONA?", "⚙️", "info")
        
        self.print_concept(
            "input()",
            "Uma função que 'pausa' o programa e espera o usuário\ndigitar algo e pressionar ENTER."
        )
        
        # === ANATOMIA DA FUNÇÃO ===
        self.print_colored("\n🔍 ANATOMIA DA FUNÇÃO INPUT:", "warning")
        self.print_colored("input('mensagem aqui')", "text")
        input("\n🔸 Pressione ENTER para ver cada parte...")
        
        partes = [
            ("input", "Nome da função que captura texto"),
            ("( )", "Parênteses obrigatórios para chamar a função"),
            ("'mensagem'", "Texto que aparece para o usuário (opcional)"),
            ("=", "Operador que guarda o resultado numa variável")
        ]
        
        for parte, explicacao in partes:
            self.print_colored(f"🔹 {parte}: {explicacao}", "text")
            input("   ⏳ Pressione ENTER para a próxima parte...")
        
        # === EXEMPLOS PROGRESSIVOS ===
        self.print_colored("\n💡 EXEMPLOS PROGRESSIVOS:", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Input simples',
                'codigo': 'resposta = input()\nprint(f"Você digitou: {resposta}")',
                'explicacao': 'Input sem mensagem - só espera você digitar'
            },
            {
                'titulo': 'EXEMPLO 2: Input com mensagem',
                'codigo': 'nome = input("Digite seu nome: ")\nprint(f"Oi, {nome}!")',
                'explicacao': 'Input com mensagem - mais amigável'
            },
            {
                'titulo': 'EXEMPLO 3: Input formatado',
                'codigo': 'cor = input("🎨 Qual sua cor favorita? ")\nprint(f"🌈 {cor} é uma cor linda!")',
                'explicacao': 'Input com emojis e formatação bonita'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"💡 {exemplo['explicacao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você entende como input() funciona!")
        self.pausar()
    
    def _secao_exemplos_praticos(self) -> None:
        """Seção: Exemplos práticos de entrada de dados"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("EXEMPLOS PRÁTICOS", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Calculadora Pessoal',
                'descricao': 'Programa que pede dois números e faz uma soma',
                'codigo': '''# Calculadora simples
print("🧮 CALCULADORA PESSOAL")
print("-" * 25)

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

# Convertendo para números
num1 = int(numero1)
num2 = int(numero2)

resultado = num1 + num2
print(f"✨ {num1} + {num2} = {resultado}")''',
                'explicacao': 'Coleta dois números e faz uma operação matemática'
            },
            {
                'titulo': 'EXEMPLO 2: Ficha Pessoal',
                'descricao': 'Programa que cria uma ficha com dados do usuário',
                'codigo': '''# Ficha pessoal
print("📋 CRIANDO SUA FICHA")
print("-" * 20)

nome = input("👤 Nome: ")
idade = input("🎂 Idade: ")
cidade = input("🏘️ Cidade: ")

print("\\n✅ FICHA CRIADA!")
print("=" * 30)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
print("=" * 30)''',
                'explicacao': 'Coleta várias informações e organiza num formato bonito'
            },
            {
                'titulo': 'EXEMPLO 3: Quiz Interativo',
                'descricao': 'Programa que faz perguntas e dá feedback',
                'codigo': '''# Quiz simples
print("🎯 QUIZ: VOCÊ CONHECE PYTHON?")
print("-" * 30)

resposta = input("Python foi criado em que ano? ")

if resposta == "1991":
    print("🎉 CORRETO! Python foi criado em 1991!")
else:
    print(f"❌ Você disse {resposta}, mas foi em 1991")
    
print("\\n🏆 Obrigado por jogar!")''',
                'explicacao': 'Faz pergunta, verifica resposta e dá feedback'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Você viu entrada de dados em ação!")
        self.pausar()
    
    def _secao_tipos_conversao(self) -> None:
        """Seção: Conversão de tipos de dados"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CONVERSÃO DE TIPOS", "🔄", "warning")
        
        self.print_concept(
            "Conversão de Tipos",
            "input() sempre retorna texto (string). Para fazer matemática,\nprecisamos converter para números."
        )
        
        # === PROBLEMA COMUM ===
        self.print_colored("\n❌ PROBLEMA COMUM:", "warning")
        codigo_problema = '''idade1 = input("Primeira idade: ")  # usuário digita: 20
idade2 = input("Segunda idade: ")   # usuário digita: 15
soma = idade1 + idade2  # Resultado: "2015" (texto grudado!)
print(soma)  # Mostra: 2015 (errado!)'''
        
        self.print_code_section("CÓDIGO PROBLEMÁTICO", codigo_problema)
        
        self.print_colored("🤔 Por que acontece isso?", "text")
        self.print_colored("Porque input() sempre retorna TEXTO, não número!", "text")
        
        input("\n🔸 Pressione ENTER para ver a solução...")
        
        # === SOLUÇÃO ===
        self.print_colored("\n✅ SOLUÇÃO: CONVERSÃO DE TIPOS", "success")
        
        conversores = [
            ("int()", "Converte texto para número inteiro", "int('20') → 20"),
            ("float()", "Converte texto para número decimal", "float('20.5') → 20.5"),
            ("str()", "Converte número para texto", "str(20) → '20'")
        ]
        
        for funcao, descricao, exemplo in conversores:
            self.print_colored(f"🔧 {funcao}: {descricao}", "info")
            self.print_colored(f"   Exemplo: {exemplo}", "text")
            input("   ⏳ Pressione ENTER para o próximo...")
        
        # === EXEMPLO CORRETO ===
        self.print_colored("\n💡 EXEMPLO CORRETO:", "success")
        codigo_correto = '''print("🧮 SOMADOR DE IDADES")
idade1 = input("Primeira idade: ")
idade2 = input("Segunda idade: ")

# Convertendo para números
num1 = int(idade1)  # "20" vira 20
num2 = int(idade2)  # "15" vira 15

soma = num1 + num2  # 20 + 15 = 35
print(f"Total: {soma} anos")'''
        
        self.print_code_section("CÓDIGO CORRETO", codigo_correto)
        
        print("\n🚀 Executando versão correta:")
        self.executar_codigo(codigo_correto)
        
        # === DICAS IMPORTANTES ===
        self.print_colored("\n💡 DICAS IMPORTANTES:", "info")
        dicas = [
            "Sempre converta ANTES de fazer matemática",
            "int() só funciona com números inteiros",
            "float() aceita números com vírgula (use ponto: 3.14)",
            "Se o usuário digitar letra, vai dar erro!"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "text")
        
        self.pausar()
    
    def _secao_formatacao_saida(self) -> None:
        """Seção: Formatação de saída"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FORMATAÇÃO DE SAÍDA", "🎨", "accent")
        
        self.print_concept(
            "Formatação",
            "Formas de deixar suas mensagens mais bonitas e organizadas\nusando f-strings, emojis e símbolos especiais."
        )
        
        # === F-STRINGS ===
        self.print_colored("\n🔤 F-STRINGS: A FORMA MODERNA", "warning")
        self.print_colored("F-strings começam com 'f' e usam {} para inserir variáveis", "text")
        
        exemplos_fstring = [
            {
                'nome': 'F-string básica',
                'codigo': '''nome = input("Seu nome: ")
idade = input("Sua idade: ")
print(f"Oi {nome}, você tem {idade} anos!")''',
                'dica': 'Use f"texto {variavel}" para inserir variáveis'
            },
            {
                'nome': 'F-string com cálculos',
                'codigo': '''ano_nascimento = input("Ano de nascimento: ")
ano_atual = 2024
idade = ano_atual - int(ano_nascimento)
print(f"Você nasceu em {ano_nascimento} e tem {idade} anos")''',
                'dica': 'Pode fazer cálculos dentro das chaves {}'
            },
            {
                'nome': 'F-string decorada',
                'codigo': '''produto = input("Nome do produto: ")
preco = input("Preço: ")
print(f"🛍️ {produto.upper()} custa R$ {preco}")
print(f"💰 Oferta especial: {produto}!")''',
                'dica': 'Combine com emojis e métodos como .upper()'
            }
        ]
        
        for i, exemplo in enumerate(exemplos_fstring, 1):
            self.print_colored(f"\n{i}. {exemplo['nome'].upper()}", "success")
            self.print_colored(f"💡 {exemplo['dica']}", "info")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando:")
            self.executar_codigo(exemplo['codigo'])
            
            if i < len(exemplos_fstring):
                input("\n🔸 Pressione ENTER para o próximo...")
        
        # === DECORAÇÃO VISUAL ===
        self.print_colored("\n✨ TÉCNICAS DE DECORAÇÃO:", "warning")
        
        decoracoes = [
            ('Linhas separadoras', 'print("=" * 30)', "Cria uma linha de 30 sinais ="),
            ('Emojis temáticos', 'print("🎉 Parabéns! 🎊")', "Deixa mensagens mais divertidas"),
            ('Espaçamento', 'print("\\n" + "Texto" + "\\n")', "\\n cria linhas em branco"),
            ('Centralização', 'print("TÍTULO".center(20))', "Centraliza texto em 20 caracteres")
        ]
        
        for nome, codigo, explicacao in decoracoes:
            self.print_colored(f"🎨 {nome}: {explicacao}", "text")
            self.print_colored(f"   Código: {codigo}", "info")
            input("   ⏳ Pressione ENTER para o próximo...")
        
        # === EXEMPLO FINAL COMPLETO ===
        self.print_colored("\n🌟 EXEMPLO FINAL: MENSAGEM SUPER FORMATADA", "success")
        codigo_final = '''nome = input("Nome: ")
comida = input("Comida favorita: ")

print("\\n" + "=" * 40)
print("🍽️  PERFIL GASTRONÔMICO  🍽️".center(40))
print("=" * 40)
print(f"👤 Chef: {nome.title()}")
print(f"🍴 Especialidade: {comida.capitalize()}")
print(f"⭐ Status: Aprovado pela comunidade!")
print("=" * 40)
print("🎉 Perfil criado com sucesso!")'''
        
        self.print_code_section("CÓDIGO FINAL", codigo_final)
        
        print("\n🚀 Executando exemplo completo:")
        self.executar_codigo(codigo_final)
        
        self.print_success("\n🎨 Agora suas mensagens ficam profissionais!")
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ERROS COMUNS E COMO EVITAR", "⚠️", "warning")
        
        erros_comuns = [
            {
                'titulo': 'ERRO 1: Tentar fazer matemática com texto',
                'codigo_errado': '''idade = input("Sua idade: ")  # "25"
proxima_idade = idade + 1  # ERRO! "25" + 1''',
                'codigo_correto': '''idade = input("Sua idade: ")
idade_numero = int(idade)  # Converte para número
proxima_idade = idade_numero + 1  # Agora funciona!''',
                'explicacao': 'input() sempre retorna texto. Converta para número antes de calcular.'
            },
            {
                'titulo': 'ERRO 2: Esquecer os parênteses no input',
                'codigo_errado': '''nome = input "Seu nome: "  # ERRO! Faltam ()''',
                'codigo_correto': '''nome = input("Seu nome: ")  # Correto!''',
                'explicacao': 'input é uma função e precisa de parênteses (), mesmo que vazio.'
            },
            {
                'titulo': 'ERRO 3: Misturar aspas',
                'codigo_errado': '''nome = input("Seu nome: ')  # ERRO! Aspas diferentes''',
                'codigo_correto': '''nome = input("Seu nome: ")  # Todas aspas duplas
# OU
nome = input('Seu nome: ')  # Todas aspas simples''',
                'explicacao': 'Use o mesmo tipo de aspas para abrir e fechar strings.'
            },
            {
                'titulo': 'ERRO 4: Não guardar o resultado do input',
                'codigo_errado': '''input("Seu nome: ")  # ERRO! Resposta perdida
print(f"Oi, {nome}")  # nome não existe!''',
                'codigo_correto': '''nome = input("Seu nome: ")  # Guarda na variável
print(f"Oi, {nome}")  # Agora funciona!''',
                'explicacao': 'Sempre guarde o resultado do input() numa variável.'
            },
            {
                'titulo': 'ERRO 5: Converter letra para número',
                'codigo_errado': '''resposta = input("Digite um número: ")  # usuário digita "abc"
numero = int(resposta)  # ERRO! Não pode converter "abc"''',
                'codigo_correto': '''resposta = input("Digite um número: ")
try:
    numero = int(resposta)
    print(f"Número: {numero}")
except:
    print("❌ Digite apenas números!")''',
                'explicacao': 'Valide se a entrada é realmente um número antes de converter.'
            }
        ]
        
        for i, erro in enumerate(erros_comuns, 1):
            self.print_colored(f"\n{erro['titulo']}", "warning")
            
            # Código errado
            self.print_colored("❌ CÓDIGO PROBLEMÁTICO:", "error" if hasattr(self.ui, 'get_color') else "warning")
            self.print_code_section("ERRADO", erro['codigo_errado'])
            
            # Código correto
            self.print_colored("✅ CÓDIGO CORRETO:", "success")
            self.print_code_section("CORRETO", erro['codigo_correto'])
            
            # Explicação
            self.print_colored(f"💡 EXPLICAÇÃO: {erro['explicacao']}", "info")
            
            if i < len(erros_comuns):
                input("\n🔸 Pressione ENTER para o próximo erro...")
        
        # === DICAS FINAIS ===
        self.print_colored("\n🛡️ DICAS PARA EVITAR ERROS:", "success")
        dicas_prevencao = [
            "Sempre teste seu código com diferentes entradas",
            "Leia as mensagens de erro - elas ajudam!",
            "Use nomes de variáveis claros (nome, idade, não x, y)",
            "Valide entradas importantes antes de usar",
            "Pratique! Quanto mais você programa, menos erra"
        ]
        
        for dica in dicas_prevencao:
            self.print_colored(f"• {dica}", "text")
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre interação"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES SOBRE INTERAÇÃO", "💫", "accent")
        
        curiosidades = [
            {
                'titulo': 'A primeira interface de usuário',
                'fato': 'O primeiro computador interativo foi criado em 1945 e ocupava uma sala inteira! Hoje você tem mais poder no seu celular.',
                'emoji': '🖥️'
            },
            {
                'titulo': 'O teclado QWERTY',
                'fato': 'O layout do teclado foi criado em 1873 para máquinas de escrever. Foi feito propositalmente LENTO para as teclas não travarem!',
                'emoji': '⌨️'
            },
            {
                'titulo': 'O primeiro "Hello, World!"',
                'fato': 'O programa que imprime "Hello, World!" foi criado em 1972. Desde então, é tradição todo programador começar com ele!',
                'emoji': '👋'
            },
            {
                'titulo': 'Interfaces de voz',
                'fato': 'Assistentes como Siri e Alexa processam milhões de comandos por minuto usando entrada de dados por voz!',
                'emoji': '🗣️'
            },
            {
                'titulo': 'Games e input()',
                'fato': 'Jogos como Minecraft processam centenas de inputs por segundo - teclado, mouse, controle - tudo ao mesmo tempo!',
                'emoji': '🎮'
            },
            {
                'titulo': 'Input() do futuro',
                'fato': 'Cientistas já desenvolvem interfaces cérebro-computador. Um dia, talvez possamos programar só com o pensamento!',
                'emoji': '🧠'
            }
        ]
        
        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n{curiosidade['emoji']} CURIOSIDADE {i}: {curiosidade['titulo'].upper()}", "warning")
            self.print_colored(f"   {curiosidade['fato']}", "text")
            
            if i < len(curiosidades):
                input("\n🔸 Pressione ENTER para a próxima curiosidade...")
        
        self.print_success("\n🌟 A entrada de dados conecta humanos e computadores!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")
        
        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")
        
        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Conhecimentos sobre Entrada de Dados',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Que função usamos para pedir dados ao usuário?',
                        'answer': ['input', 'input()'],
                        'hint': 'Começa com "in" e termina com "put"'
                    },
                    {
                        'question': 'input() sempre retorna que tipo de dado?',
                        'answer': ['texto', 'string', 'str'],
                        'hint': 'Sempre texto, mesmo se você digitar números'
                    },
                    {
                        'question': 'Como convertemos texto para número inteiro?',
                        'answer': ['int()', 'int', 'usando int()'],
                        'hint': 'Função de 3 letras que transforma em integer'
                    },
                    {
                        'question': 'F-strings começam com que letra?',
                        'answer': ['f', 'F'],
                        'hint': 'É a primeira letra de "format"'
                    },
                    {
                        'question': 'O que acontece se não guardarmos input() numa variável?',
                        'answer': ['perdemos', 'se perde', 'perdemos a resposta', 'perde'],
                        'hint': 'A resposta do usuário vai para onde?'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o input que pede o nome',
                        'starter': 'print("Programa de Boas-vindas")\n# Complete aqui\nprint(f"Bem-vindo, {nome}!")',
                        'solution': 'nome = input("Digite seu nome: ")',
                        'type': 'input_simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o código que soma dois números',
                        'starter': 'print("Calculadora")\nnum1 = input("Primeiro número: ")\nnum2 = input("Segundo número: ")\n# Complete aqui\nprint(f"Resultado: {resultado}")',
                        'solution': 'resultado = int(num1) + int(num2)',
                        'type': 'conversion'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete com f-string formatada',
                        'starter': 'produto = input("Nome do produto: ")\npreco = input("Preço: ")\n# Complete aqui\nprint("Cadastro finalizado!")',
                        'solution': 'print(f"🛍️ {produto.title()} por R$ {preco}")',
                        'type': 'fstring'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Criador de Fichas',
                'type': 'creative',
                'instruction': 'Crie um programa que pede 3 informações pessoais e cria uma ficha bonita!'
            }
        ]
        
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
                        self._run_quiz(exercicios[0])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo"]:
                    try:
                        self._run_creative_exercise(exercicios[2])
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
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre entrada de dados",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um programa de fichas",
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
    
    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo"""
        self.print_section(quiz_data['title'], "📝")
        score = 0
        total_questions = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            print(f"\n📝 Pergunta {i} de {total_questions}:")
            correto = self.exercicio(
                q['question'],
                q['answer'],
                q['hint']
            )
            if correto:
                score += 1
        
        # Feedback detalhado baseado na pontuação
        percentage = (score / total_questions) * 100
        
        self.print_success(f"\n🏆 RESULTADO: {score} de {total_questions} perguntas corretas ({percentage:.0f}%)")
        
        if percentage == 100:
            self.print_success("🌟 PERFEITO! Você dominou entrada de dados!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você entende bem o assunto!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo.", "info")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código Inicial", ex['starter'])
            
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'input_simple':
                print("\n✍️ Complete com um input() que pede o nome:")
                print("💡 Formato: variavel = input('mensagem')")
                user_input = input(">>> ").strip()
                if 'input(' in user_input and 'nome' in user_input:
                    user_code = user_input
                else:
                    user_code = 'nome = input("Digite seu nome: ")'
                    self.print_tip("Usando solução padrão - lembre de usar input()")
                    
            elif exercise_type == 'conversion':
                print("\n✍️ Complete convertendo strings para números e somando:")
                print("💡 Use int() para converter e + para somar")
                user_input = input(">>> ").strip()
                if 'int(' in user_input and '+' in user_input:
                    user_code = user_input
                else:
                    user_code = 'resultado = int(num1) + int(num2)'
                    self.print_tip("Usando solução padrão - lembre de usar int()")
                    
            elif exercise_type == 'fstring':
                print("\n✍️ Complete com uma f-string bonita:")
                print("💡 Use f'' e {} para variáveis, pode adicionar emojis!")
                user_input = input(">>> ").strip()
                if user_input:
                    if user_input.startswith('print(f'):
                        user_code = user_input
                    elif user_input.startswith('f"') or user_input.startswith("f'"):
                        user_code = f'print({user_input})'
                    else:
                        user_code = f'print(f"{user_input}")'
                else:
                    user_code = 'print(f"🛍️ {produto} por R$ {preco}")'
                    self.print_tip("Usando solução padrão.")
            else:
                print("\n✍️ Digite a linha que falta:")
                user_input = input(">>> ").strip()
                user_code = user_input if user_input else ex['solution']
            
            # Substitui no código
            lines = ex['starter'].split('\n')
            for j, line in enumerate(lines):
                if '# Complete aqui' in line:
                    lines[j] = user_code
                    break
            complete_code = '\n'.join(lines)
            
            print("\n🚀 Executando seu código completo:")
            self.executar_codigo(complete_code)
            
            print(f"\n💡 Solução sugerida: {ex['solution']}")
            self.print_success("✅ Muito bem! Você completou o código!")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        print("💡 Exemplo: Nome, idade e hobby")
        print("🎯 Use input(), f-strings e deixe bonito com emojis!")
        
        print("\n📝 Vamos criar juntos:")
        
        try:
            campo1 = input("Que informação quer pedir? (ex: nome): ").strip()
            if not campo1:
                campo1 = "nome"
            
            campo2 = input("Segunda informação? (ex: idade): ").strip()
            if not campo2:
                campo2 = "idade"
                
            campo3 = input("Terceira informação? (ex: hobby): ").strip()
            if not campo3:
                campo3 = "hobby"
            
            print(f"\n🌟 Criando ficha com: {campo1}, {campo2}, {campo3}")
            
            # Gera código personalizado
            codigo_personalizado = f'''print("📋 CRIADOR DE FICHAS")
print("-" * 30)

{campo1} = input("📝 {campo1.capitalize()}: ")
{campo2} = input("📝 {campo2.capitalize()}: ")
{campo3} = input("📝 {campo3.capitalize()}: ")

print("\\n✅ FICHA CRIADA!")
print("=" * 40)
print(f"🔸 {campo1.capitalize()}: {{{campo1}}}")
print(f"🔸 {campo2.capitalize()}: {{{campo2}}}")
print(f"🔸 {campo3.capitalize()}: {{{campo3}}}")
print("=" * 40)
print("🎉 Ficha salva com sucesso!")'''
            
            print("\n💻 Seu código personalizado:")
            self.print_code_section("SEU PROGRAMA", codigo_personalizado)
            
            print("\n🚀 Executando seu programa:")
            self.executar_codigo(codigo_personalizado)
            
            self.print_success("\n🎉 Parabéns! Você criou um programa único!")
            
        except KeyboardInterrupt:
            self.print_warning("\nExercício cancelado")
        
        self.pausar()
    
    def _mini_projeto_questionario_personalizado(self) -> None:
        """Mini Projeto - Módulo 5: Questionário Personalizado"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: QUESTIONÁRIO PERSONALIZADO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: QUESTIONÁRIO PERSONALIZADO")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um questionário interativo completo!")
        
        self.print_concept(
            "Questionário Personalizado",
            "Um programa que faz perguntas, processa as respostas e\ngera um relatório personalizado com as informações."
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é usado em:", "text")
        usos_praticos = [
            "Pesquisas de satisfação em empresas",
            "Formulários de cadastro em sites",
            "Quiz de personalidade em redes sociais",
            "Coleta de dados para pesquisas acadêmicas",
            "Sistemas de CRM (relacionamento com cliente)"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Escolha do tema
        self.print_section("PASSO 1: Escolha do Tema", "📝", "info")
        self.print_tip("Vamos criar um questionário sobre um tema de sua escolha!")
        
        temas_sugeridos = [
            "🎬 Cinema e Filmes",
            "🍕 Alimentação e Culinária", 
            "🎮 Games e Tecnologia",
            "🌍 Viagens e Aventuras",
            "📚 Livros e Leitura",
            "🎵 Música e Shows",
            "⚽ Esportes e Atividades"
        ]
        
        print("\n🎯 Temas sugeridos:")
        for tema in temas_sugeridos:
            print(f"  {tema}")
        
        try:
            tema_escolhido = input("\n✍️ Escolha um tema (ou crie o seu): ").strip()
            if not tema_escolhido:
                tema_escolhido = "Interesses Pessoais"
            
            self.print_success(f"🎯 Tema escolhido: {tema_escolhido}!")
            
            # PASSO 2: Criação das perguntas
            self.print_section("PASSO 2: Definindo as Perguntas", "❓", "success")
            self.print_colored("Vamos criar 4 perguntas sobre seu tema:", "text")
            
            perguntas = []
            for i in range(1, 5):
                pergunta = input(f"📝 Pergunta {i}: ").strip()
                if not pergunta:
                    pergunta = f"Qual é seu/sua {tema_escolhido.lower()} favorito(a)?"
                perguntas.append(pergunta)
            
            # PASSO 3: Geração do código
            self.print_section("PASSO 3: Gerando o Programa", "⚙️", "warning")
            self.print_colored("Criando seu questionário personalizado...", "text")
            
            # Criação do código personalizado
            codigo_questionario = f'''#!/usr/bin/env python3
# 🎯 QUESTIONÁRIO: {tema_escolhido.upper()}
# Criado com Python

print("=" * 50)
print("📋 QUESTIONÁRIO: {tema_escolhido.upper()}")
print("=" * 50)
print("🎯 Responda as perguntas abaixo:")
print()

# Coletando respostas
respostas = []

print("📝 Pergunta 1:")
resp1 = input("{perguntas[0]} ")
respostas.append(resp1)

print("\\n📝 Pergunta 2:")
resp2 = input("{perguntas[1]} ")
respostas.append(resp2)

print("\\n📝 Pergunta 3:")
resp3 = input("{perguntas[2]} ")
respostas.append(resp3)

print("\\n📝 Pergunta 4:")
resp4 = input("{perguntas[3]} ")
respostas.append(resp4)

# Processando dados
print("\\n⏳ Processando suas respostas...")
print("." * 20)

# Relatório final
print("\\n" + "=" * 60)
print("📊 SEU RELATÓRIO PERSONALIZADO")
print("=" * 60)
print(f"🎯 Tema: {tema_escolhido}")
print(f"📅 Data: 2024")
print("\\n📝 SUAS RESPOSTAS:")
print("-" * 30)

for i, (pergunta, resposta) in enumerate(zip(["{perguntas[0]}", "{perguntas[1]}", "{perguntas[2]}", "{perguntas[3]}"], respostas), 1):
    print(f"❓ {i}. {{pergunta}}")
    print(f"✅ Sua resposta: {{resposta}}")
    print()

print("=" * 60)
print("🎉 Obrigado por participar!")
print("📊 Dados coletados com sucesso!")
print("=" * 60)

# Estatísticas básicas
total_caracteres = sum(len(resp) for resp in respostas)
resposta_mais_longa = max(respostas, key=len)

print("\\n📈 ESTATÍSTICAS:")
print(f"📝 Total de respostas: 4")
print(f"🔤 Caracteres digitados: {{total_caracteres}}")
print(f"📏 Resposta mais elaborada: {{resposta_mais_longa[:30]}}...")
print("\\n✨ Questionário criado com Python!")'''

        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")
        self.exemplo(codigo_questionario)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.print_colored("🚀 Executando seu questionário personalizado:", "text")
        self.executar_codigo(codigo_questionario)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema completo de questionário!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar validação de respostas (verificar se não está vazio)",
            "Salvar respostas em arquivo de texto",
            "Criar análise automática das respostas",
            "Adicionar múltipla escolha nas perguntas",
            "Conectar com banco de dados para pesquisas grandes"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre em Entrada de Dados!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Questionário Personalizado")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo05EntradaDados()
    print("Teste do módulo 5 - versão refatorada")
    module._entrada_dados_interativa()