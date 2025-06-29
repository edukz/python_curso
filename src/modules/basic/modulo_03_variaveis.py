#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 3: Variáveis e Tipos de Dados
Aprenda sobre variáveis, a memória do seu programa
"""

from ..shared.base_module import BaseModule


class Modulo03Variaveis(BaseModule):
    """Módulo 3: Variáveis - A Memória do Seu Programa"""
    
    def __init__(self):
        super().__init__("modulo_3", "Variáveis e Tipos de Dados")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo Variáveis"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._variaveis_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _variaveis_interativo(self) -> None:
        """Conteúdo principal do módulo Variáveis"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MÓDULO 3: VARIÁVEIS - A MEMÓRIA DO SEU PROGRAMA")
        else:
            print("\n" + "="*50)
            print("🎯 MÓDULO 3: VARIÁVEIS - A MEMÓRIA DO SEU PROGRAMA")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Chegou a hora de aprender sobre variáveis - a base de todo programa!")
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
            self._mini_projeto_cartao_apresentacao()
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
                'id': 'secao_o_que_sao_variaveis',
                'titulo': '🎯 O que são variáveis?',
                'descricao': 'Entenda o conceito fundamental de variáveis',
                'funcao': self._secao_o_que_sao_variaveis
            },
            {
                'id': 'secao_como_criar_variaveis',
                'titulo': '🛠️ Como criar e usar variáveis',
                'descricao': 'Aprenda a sintaxe e atribuição de valores',
                'funcao': self._secao_como_criar_variaveis
            },
            {
                'id': 'secao_tipos_dados',
                'titulo': '📊 Tipos de dados em Python',
                'descricao': 'Explore strings, números e booleanos',
                'funcao': self._secao_tipos_dados
            },
            {
                'id': 'secao_nomes_variaveis',
                'titulo': '🏷️ Regras para nomes de variáveis',
                'descricao': 'Aprenda as convenções e restrições',
                'funcao': self._secao_nomes_variaveis
            },
            {
                'id': 'secao_operacoes_variaveis',
                'titulo': '⚙️ Operações com variáveis',
                'descricao': 'Descubra como manipular e combinar variáveis',
                'funcao': self._secao_operacoes_variaveis
            },
            {
                'id': 'secao_boas_praticas',
                'titulo': '⭐ Boas práticas e dicas profissionais',
                'descricao': 'Segredos para escrever código limpo e legível',
                'funcao': self._secao_boas_praticas
            },
            {
                'id': 'secao_mundo_real',
                'titulo': '🌍 Variáveis no mundo real',
                'descricao': 'Veja como variáveis são usadas em aplicações reais',
                'funcao': self._secao_mundo_real
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

    def _secao_o_que_sao_variaveis(self) -> None:
        """Seção: O que são variáveis?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO VARIÁVEIS?", "🎯")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Variável",
            "Um espaço na memória do computador onde guardamos informações que podem mudar"
        )

        # === DICA RELACIONADA ===
        self.print_tip("Pense nas variáveis como gavetas etiquetadas onde você guarda seus pertences!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine seu guarda-roupa com gavetas etiquetadas:", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você cria uma 'gaveta' com nome (ex: nome = 'João')",
            "2. O Python reserva espaço na memória para guardar 'João'",
            "3. Sempre que usar 'nome', Python busca o valor guardado",
            "4. Você pode trocar o conteúdo quando quiser (nome = 'Maria')"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''nome = "Python"
idade = 30
print("Linguagem:", nome)
print("Idade:", idade)'''
        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE VARIÁVEIS SÃO USADAS NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Instagram - guardar seu nome de usuário e número de seguidores",
            "Netflix - armazenar seu histórico de filmes assistidos",
            "WhatsApp - salvar suas mensagens e contatos",
            "Bancos - manter saldo da conta e histórico de transações",
            "Jogos - armazenar pontuação, nível e itens do jogador"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_como_criar_variaveis(self) -> None:
        """Seção: Como criar e usar variáveis"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO CRIAR E USAR VARIÁVEIS", "🛠️")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Atribuição",
            "O processo de dar um valor para uma variável usando o sinal ="
        )

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como colar uma etiqueta numa caixa e colocar algo dentro:", "text")
        self.print_colored("• Caixa = nome da variável", "text")
        self.print_colored("• Etiqueta = nome que você escolhe", "text")
        self.print_colored("• Conteúdo = valor que você guarda", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === SINTAXE ===
        self.print_colored("\n🔧 SINTAXE BÁSICA:", "info")
        self.print_colored("nome_da_variavel = valor", "success")
        
        print("\n🎯 Leia sempre da DIREITA para ESQUERDA:")
        print("   nome = 'João'")
        print("   ↑       ↑")
        print("   |       └─ Valor que vai ser guardado")
        print("   └─ Nome da caixa onde vai ser guardado")

        # === EXEMPLOS PRÁTICOS ===
        self.print_colored("\n💻 EXEMPLOS PRÁTICOS:", "warning")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Criando variáveis simples',
                'codigo': '''nome = "Ana"
idade = 25
cidade = "São Paulo"
print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")'''
            },
            {
                'titulo': 'EXEMPLO 2: Variáveis podem mudar',
                'codigo': '''pontos = 0
print(f"Pontos iniciais: {pontos}")

pontos = 50
print(f"Depois de ganhar: {pontos}")

pontos = pontos + 25
print(f"Depois de ganhar mais: {pontos}")'''
            }
        ]

        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")

        self.print_success("\n🎉 Agora você sabe criar e modificar variáveis!")
        self.pausar()

    def _secao_tipos_dados(self) -> None:
        """Seção: Tipos de dados em Python"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("TIPOS DE DADOS EM PYTHON", "📊")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Tipos de Dados",
            "Diferentes categorias de informações que podemos guardar em variáveis"
        )

        # === TIPOS PRINCIPAIS ===
        tipos = [
            {
                'nome': 'STRING (texto)',
                'simbolo': '🔤',
                'descricao': 'Qualquer texto entre aspas',
                'exemplos': ['"Olá"', "'Python'", '"123 texto"'],
                'codigo': '''nome = "Python"
mensagem = 'Olá, mundo!'
codigo = "ABC123"
print(f"Nome: {nome}")
print(f"Mensagem: {mensagem}")
print(f"Código: {codigo}")'''
            },
            {
                'nome': 'INTEGER (número inteiro)',
                'simbolo': '🔢',
                'descricao': 'Números sem vírgula',
                'exemplos': ['42', '-10', '0'],
                'codigo': '''idade = 25
pontos = 1500
temperatura = -5
print(f"Idade: {idade}")
print(f"Pontos: {pontos}")
print(f"Temperatura: {temperatura}°C")'''
            },
            {
                'nome': 'FLOAT (número decimal)',
                'simbolo': '📊',
                'descricao': 'Números com vírgula (usa ponto)',
                'exemplos': ['3.14', '1.75', '-2.5'],
                'codigo': '''altura = 1.75
preco = 29.90
pi = 3.14159
print(f"Altura: {altura}m")
print(f"Preço: R$ {preco}")
print(f"Pi: {pi}")'''
            },
            {
                'nome': 'BOOLEAN (verdadeiro/falso)',
                'simbolo': '✅',
                'descricao': 'Apenas True ou False',
                'exemplos': ['True', 'False'],
                'codigo': '''ativo = True
chuva = False
maior_idade = True
print(f"Usuário ativo: {ativo}")
print(f"Está chovendo: {chuva}")
print(f"Maior de idade: {maior_idade}")'''
            }
        ]

        for i, tipo in enumerate(tipos, 1):
            self.print_colored(f"\n{tipo['simbolo']} {tipo['nome']}", "warning")
            self.print_colored(f"📝 {tipo['descricao']}", "text")
            
            self.print_colored("\n✨ Exemplos:", "info")
            for exemplo in tipo['exemplos']:
                self.print_colored(f"  • {exemplo}", "primary")
                
            self.print_code_section("CÓDIGO PRÁTICO", tipo['codigo'])
            print("\n🚀 Resultado:")
            self.executar_codigo(tipo['codigo'])
            
            if i < len(tipos):
                input("\n🔸 Pressione ENTER para o próximo tipo...")

        self.print_success("\n🎉 Agora você conhece os tipos básicos de dados em Python!")
        self.pausar()

    def _secao_nomes_variaveis(self) -> None:
        """Seção: Regras para nomes de variáveis"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("REGRAS PARA NOMES DE VARIÁVEIS", "🏷️")

        # === REGRAS BÁSICAS ===
        self.print_colored("📝 REGRAS OBRIGATÓRIAS:", "warning")
        regras = [
            "✅ Pode usar letras (a-z, A-Z)",
            "✅ Pode usar números (0-9) - mas NÃO no início",
            "✅ Pode usar underscore (_)",
            "❌ Não pode ter espaços",
            "❌ Não pode ter acentos ou caracteres especiais",
            "❌ Não pode começar com números",
            "❌ Não pode usar palavras reservadas do Python"
        ]
        
        for regra in regras:
            self.print_colored(f"  {regra}", "text")

        # === EXEMPLOS VÁLIDOS E INVÁLIDOS ===
        self.print_colored("\n✅ NOMES VÁLIDOS:", "success")
        validos = ["nome", "idade", "nome_completo", "salario2023", "_temperatura", "PI"]
        for nome in validos:
            self.print_colored(f"  • {nome}", "text")
            
        self.print_colored("\n❌ NOMES INVÁLIDOS:", "red")
        invalidos = [
            ("2nome", "começa com número"),
            ("nome completo", "tem espaço"),
            ("salário", "tem acento"),
            ("for", "palavra reservada"),
            ("nome@", "caractere especial")
        ]
        for nome, motivo in invalidos:
            self.print_colored(f"  • {nome} - {motivo}", "text")

        # === CONVENÇÕES ===
        self.print_colored("\n🎨 CONVENÇÕES DE NOMENCLATURA:", "info")
        convencoes = [
            ("snake_case", "nome_da_variavel", "Recomendado em Python"),
            ("camelCase", "nomeDaVariavel", "Comum em outras linguagens"),
            ("PascalCase", "NomeDaVariavel", "Para classes"),
            ("CONSTANTS", "VALOR_FIXO", "Para constantes")
        ]
        
        for estilo, exemplo, uso in convencoes:
            self.print_colored(f"  • {estilo}: {exemplo} - {uso}", "primary")

        # === CASE SENSITIVE ===
        self.print_colored("\n⚠️ PYTHON É CASE-SENSITIVE:", "warning")
        codigo_case = '''nome = "João"
Nome = "Maria"
NOME = "Pedro"

print(f"nome: {nome}")
print(f"Nome: {Nome}")
print(f"NOME: {NOME}")
print("São 3 variáveis DIFERENTES!")'''
        
        self.exemplo(codigo_case)
        self.executar_codigo(codigo_case)

        self.pausar()

    def _secao_operacoes_variaveis(self) -> None:
        """Seção: Operações com variáveis"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("OPERAÇÕES COM VARIÁVEIS", "⚙️")

        # === OPERAÇÕES MATEMÁTICAS ===
        self.print_colored("🧮 OPERAÇÕES MATEMÁTICAS:", "warning")
        codigo_math = '''a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"a = {a}, b = {b}")
print(f"Soma: {a} + {b} = {soma}")
print(f"Subtração: {a} - {b} = {subtracao}")
print(f"Multiplicação: {a} * {b} = {multiplicacao}")
print(f"Divisão: {a} / {b} = {divisao:.2f}")'''
        
        self.exemplo(codigo_math)
        self.executar_codigo(codigo_math)

        # === OPERAÇÕES COM STRINGS ===
        self.print_colored("\n🔤 OPERAÇÕES COM TEXTO:", "info")
        codigo_string = '''nome = "Python"
versao = "3.12"

# Concatenação (juntar textos)
linguagem_completa = nome + " " + versao

# Repetição
separador = "-" * 20

print(separador)
print(f"Linguagem: {linguagem_completa}")
print(f"Nome repetido: {nome * 3}")
print(separador)'''
        
        self.exemplo(codigo_string)
        self.executar_codigo(codigo_string)

        # === OPERAÇÕES DE ATRIBUIÇÃO ===
        self.print_colored("\n🔄 ATUALIZAÇÃO DE VARIÁVEIS:", "success")
        codigo_update = '''pontos = 100
print(f"Pontos iniciais: {pontos}")

# Formas de atualizar
pontos = pontos + 50  # Forma longa
print(f"Após ganhar 50: {pontos}")

pontos += 30  # Forma curta (equivale a: pontos = pontos + 30)
print(f"Após ganhar mais 30: {pontos}")

pontos -= 20  # Subtrair
print(f"Após perder 20: {pontos}")

pontos *= 2  # Multiplicar
print(f"Após dobrar: {pontos}")'''
        
        self.exemplo(codigo_update)
        self.executar_codigo(codigo_update)

        self.pausar()

    def _secao_boas_praticas(self) -> None:
        """Seção: Boas práticas e dicas profissionais"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("BOAS PRÁTICAS E DICAS PROFISSIONAIS", "⭐")

        dicas = [
            {
                'titulo': '📝 DICA 1: Use nomes descritivos',
                'ruim': '''x = 1000
y = 0.08
z = x * y''',
                'bom': '''preco_produto = 1000
taxa_desconto = 0.08
desconto = preco_produto * taxa_desconto'''
            },
            {
                'titulo': '📊 DICA 2: Seja consistente com o estilo',
                'ruim': '''nomeUsuario = "João"
idade_usuario = 25
UserActive = True''',
                'bom': '''nome_usuario = "João"
idade_usuario = 25
usuario_ativo = True'''
            },
            {
                'titulo': '📋 DICA 3: Agrupe variáveis relacionadas',
                'ruim': '''x = "João"
y = 25
z = "joao@email.com"
a = True''',
                'bom': '''# Dados do usuário
nome_usuario = "João"
idade_usuario = 25
email_usuario = "joao@email.com"
usuario_ativo = True'''
            }
        ]

        for i, dica in enumerate(dicas, 1):
            self.print_colored(f"\n{dica['titulo']}", "warning")
            
            self.print_colored("❌ RUIM:", "red")
            self.print_code_section("Evite", dica['ruim'])
            
            self.print_colored("✅ BOM:", "green")
            self.print_code_section("Prefira", dica['bom'])
            
            if i < len(dicas):
                input("\n🔸 Pressione ENTER para a próxima dica...")

        self.print_success("\n🌟 Agora você tem dicas valiosas para escrever código profissional!")
        self.pausar()

    def _secao_mundo_real(self) -> None:
        """Seção: Variáveis no mundo real"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("VARIÁVEIS NO MUNDO REAL", "🌍")

        # === EXEMPLOS DE APLICAÇÕES ===
        aplicacoes = [
            {
                'nome': '📱 REDES SOCIAIS',
                'exemplo': '''# Instagram
nome_usuario = "python_dev"
seguidores = 15420
posts = 247
verificado = True
bio = "Desenvolvedor Python 🐍"'''
            },
            {
                'nome': '🎮 JOGOS',
                'exemplo': '''# RPG Online
nome_personagem = "DragonSlayer"
nivel = 45
vida = 850
mana = 320
classe = "Mago"
exp_atual = 15750'''
            },
            {
                'nome': '💳 SISTEMA BANCÁRIO',
                'exemplo': '''# Conta corrente
numero_conta = "12345-6"
titular = "Maria Silva"
saldo = 2500.75
limite = 1000.00
conta_ativa = True
agencia = "0001"'''
            },
            {
                'nome': '📚 E-LEARNING',
                'exemplo': '''# Curso online
aluno = "João Santos"
curso_atual = "Python para Iniciantes"
progresso = 75  # percentual
modulos_completos = 8
modulos_total = 12
certificado_disponivel = False'''
            }
        ]

        for aplicacao in aplicacoes:
            self.print_colored(f"\n{aplicacao['nome']}", "warning")
            self.exemplo(aplicacao['exemplo'])
            self.executar_codigo(aplicacao['exemplo'])
            input("\n🔸 Pressione ENTER para o próximo exemplo...")

        self.print_success("\n🎉 Você viu como variáveis estão em tudo que usamos!")
        self.pausar()
    
    def _mini_projeto_cartao_apresentacao(self) -> None:
        """Mini Projeto - Módulo 3: Cartão de Apresentação Personalizado"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CARTÃO DE APRESENTAÇÃO PERSONALIZADO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CARTÃO DE APRESENTAÇÃO PERSONALIZADO")
            print("="*50)
        
        self.print_success("🎉 Vamos criar seu projeto prático aplicando tudo sobre variáveis!")

        self.print_concept(
            "Cartão de Apresentação Personalizado",
            "Um programa que cria um cartão profissional usando variáveis para armazenar informações pessoais"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "LinkedIn - criar perfis profissionais automáticos",
            "Eventos corporativos - gerar crachás personalizados",
            "Freelancers - criar propostas com dados pessoais",
            "Redes sociais - bio dinâmica baseada em variáveis"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Coleta de informações
        self.print_section("PASSO 1: Coletando suas informações", "📝", "info")
        self.print_tip("Vamos criar variáveis para armazenar seus dados pessoais")

        try:
            print("\n👤 Vamos personalizar seu cartão de apresentação!")
            nome_completo = input("👤 Qual é o seu nome completo? ").strip() or "Ana Silva"
            profissao = input("💼 Qual é a sua profissão? ").strip() or "Desenvolvedora Python"
            empresa = input("🏢 Onde você trabalha/estuda? ").strip() or "TechCorp"
            cidade = input("🌆 Em que cidade você mora? ").strip() or "São Paulo"
            anos_experiencia = input("📅 Quantos anos de experiência? ").strip() or "3"
            linguagem_favorita = input("🐍 Qual sua linguagem de programação favorita? ").strip() or "Python"
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Processamento dos dados
        self.print_section("PASSO 2: Organizando os dados em variáveis", "⚙️", "success")
        self.print_colored("Agora vamos criar variáveis para organizar suas informações:", "text")

        # PASSO 3: Geração do cartão
        self.print_section("PASSO 3: Gerando seu cartão de apresentação", "🎬", "warning")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")

        codigo_final = f'''# 🐍 PROJETO: CARTÃO DE APRESENTAÇÃO PERSONALIZADO
# Módulo 3: Variáveis

# === INFORMAÇÕES PESSOAIS (usando variáveis) ===
nome_completo = "{nome_completo}"
profissao = "{profissao}"
empresa = "{empresa}"
cidade = "{cidade}"
anos_experiencia = {anos_experiencia}
linguagem_favorita = "{linguagem_favorita}"

# === DADOS CALCULADOS ===
nivel_experiencia = "Iniciante" if anos_experiencia < 2 else "Intermediário" if anos_experiencia < 5 else "Avançado"
email_profissional = nome_completo.lower().replace(" ", ".") + "@" + empresa.lower() + ".com"

# === GERAÇÃO DO CARTÃO ===
print("═" * 60)
print("               🎆 CARTÃO DE APRESENTAÇÃO 🎆")
print("═" * 60)
print()
print(f"      👤 {nome_completo}")
print(f"      💼 {profissao}")
print()
print("─" * 60)
print()
print(f"  🏢 Empresa: {empresa}")
print(f"  🌆 Localização: {cidade}")
print(f"  📅 Experiência: {anos_experiencia} anos ({nivel_experiencia})")
print(f"  🐍 Especialidade: {linguagem_favorita}")
print(f"  📧 Email: {email_profissional}")
print()
print("─" * 60)
print("           ✨ Conecte-se comigo! ✨")
print("═" * 60)'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou seu projeto de cartão de apresentação!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar foto do perfil usando ASCII art",
            "Criar diferentes modelos de cartão (formal, criativo, etc.)",
            "Integrar com redes sociais para buscar informações automaticamente",
            "Salvar cartões em arquivos para reutilizar"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Criador de Cartões Profissionais!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Cartão de Apresentação Personalizado")
        
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
                'title': 'Quiz: Conhecimentos sobre Variáveis',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'O que é uma variável em programação?',
                        'answer': ['espaço na memória', 'caixa', 'container', 'recipiente'],
                        'hint': 'Pense numa caixa etiquetada onde guardamos coisas'
                    },
                    {
                        'question': 'Qual o símbolo usado para atribuir valor a uma variável?',
                        'answer': ['=', 'igual'],
                        'hint': 'Usado em nome = "João"'
                    },
                    {
                        'question': 'Em Python, "nome" e "Nome" são a mesma variável? (sim/não)',
                        'answer': ['não', 'nao', 'diferentes'],
                        'hint': 'Python diferencia maiúsculas de minúsculas'
                    },
                    {
                        'question': 'Qual nome de variável é VÁLIDO: "2nome" ou "nome2"?',
                        'answer': ['nome2'],
                        'hint': 'Variáveis não podem começar com números'
                    },
                    {
                        'question': 'Que tipo de dado é True ou False?',
                        'answer': ['boolean', 'bool', 'booleano'],
                        'hint': 'É um tipo que representa verdadeiro ou falso'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Crie uma variável "nome" com seu nome e exiba',
                        'starter': '# Crie uma variável nome\n_____ = "_____"\nprint("Meu nome é:", _____)',
                        'solution': 'nome = "Ana"\nprint("Meu nome é:", nome)',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Crie variáveis para idade e cidade, depois exiba tudo junto',
                        'starter': '# Complete o código\nnome = "João"\n_____ = 25\n_____ = "São Paulo"\nprint(f"Olá, {_____}! Você tem {_____} anos e mora em {_____}")',
                        'solution': 'nome = "João"\nidade = 25\ncidade = "São Paulo"\nprint(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}")',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Crie um sistema de pontos que aumenta e diminui',
                        'starter': '# Sistema de pontos\npontos = 0\n# Ganhou 50 pontos\npontos = _____\n# Ganhou mais 30\npontos _____ 30\n# Perdeu 20\npontos _____ 20\nprint(f"Pontos finais: {pontos}")',
                        'solution': 'pontos = 0\npontos = pontos + 50\npontos += 30\npontos -= 20\nprint(f"Pontos finais: {pontos}")',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Perfil Personalizado',
                'type': 'creative',
                'instruction': 'Crie variáveis para um perfil pessoal e exiba de forma criativa (nome, hobby, comida favorita, etc.)'
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
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre variáveis",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um perfil personalizado",
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

    def _run_quiz(self, quiz_data) -> None:
        """Executa o quiz de conhecimentos"""
        self.print_section(quiz_data['title'], "📝", "info")
        score = 0
        total = len(quiz_data['questions'])

        self.print_colored(f"Vamos testar seus conhecimentos com {total} perguntas!", "text")
        print()

        for i, q in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\n📌 PERGUNTA {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            tentativas = 0
            max_tentativas = 2
            
            while tentativas < max_tentativas:
                try:
                    resposta = input("\n👉 Sua resposta: ").strip().lower()
                    
                    if any(ans.lower() in resposta for ans in q['answer']):
                        self.print_success("✅ Correto! Muito bem!")
                        score += 1
                        break
                    else:
                        tentativas += 1
                        if tentativas < max_tentativas:
                            self.print_warning(f"❌ Não é isso. Dica: {q['hint']}")
                            self.print_colored("Tente novamente:", "text")
                        else:
                            self.print_warning(f"❌ A resposta era: {q['answer'][0]}")
                            
                except KeyboardInterrupt:
                    self.print_warning("\n⚠️ Quiz cancelado.")
                    return

        # Resultado final
        percentual = (score / total) * 100
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        self.print_colored(f"Você acertou {score} de {total} perguntas ({percentual:.0f}%)", "text")
        
        if score == total:
            self.print_success("🌟 PERFEITO! Você dominou completamente as variáveis!")
        elif score >= total * 0.8:
            self.print_success("🎉 EXCELENTE! Você entende muito bem variáveis!")
        elif score >= total * 0.6:
            self.print_colored("👍 BOM! Você está no caminho certo!", "info")
        else:
            self.print_colored("📚 Continue estudando! Revisite as seções se necessário.", "warning")
            
        self.pausar()

    def _run_code_completion(self, exercise_data) -> None:
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "success")
        
        for i, exercise in enumerate(exercise_data['exercises'], 1):
            self.print_colored(f"\n🎯 EXERCÍCIO {i}: {exercise['type'].upper()}", "warning")
            self.print_colored(exercise['instruction'], "text")
            
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercise['starter'])
            
            print("\n✍️ Digite sua solução (ou 'skip' para pular):")
            try:
                resposta = input(">>> ").strip()
                
                if resposta.lower() == 'skip':
                    self.print_colored("⏭️ Exercício pulado.", "warning")
                    continue
                    
                if resposta:
                    print("\n🚀 Testando sua solução:")
                    try:
                        self.executar_codigo(resposta)
                        self.print_success("✅ Sua solução funcionou!")
                        
                        ver_solucao = input("\n💡 Quer ver a solução sugerida? (s/n): ").lower()
                        if ver_solucao == 's':
                            self.print_colored("\n🔍 SOLUÇÃO SUGERIDA:", "info")
                            self.exemplo(exercise['solution'])
                            
                    except Exception as e:
                        self.print_warning(f"❌ Erro ao executar: {str(e)}")
                        self.print_colored("\n💡 SOLUÇÃO CORRETA:", "info")
                        self.exemplo(exercise['solution'])
                        self.executar_codigo(exercise['solution'])
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Exercício cancelado.")
                return
                
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de código!")
        self.pausar()

    def _run_creative_exercise(self, exercise_data) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "accent")
        self.print_colored(exercise_data['instruction'], "text")
        
        print("\n💡 EXEMPLO:")
        exemplo_codigo = '''nome = "Ana"
hobby = "fotografia"
comida_favorita = "pizza"
filme_favorito = "Matrix"

print("=" * 30)
print(f"   👤 {nome.upper()}")
print("=" * 30)
print(f"🎨 Hobby: {hobby}")
print(f"🍕 Comida: {comida_favorita}")
print(f"🎥 Filme: {filme_favorito}")
print("=" * 30)'''
        
        self.exemplo(exemplo_codigo)
        self.executar_codigo(exemplo_codigo)
            
        print("\n✍️ Agora é sua vez! Digite suas variáveis e código (digite 'fim' para terminar):")
        
        linhas_codigo = []
        try:
            while True:
                linha = input(">>> ")
                if linha.lower() == 'fim':
                    break
                if linha.strip():
                    linhas_codigo.append(linha)
                    
        except KeyboardInterrupt:
            self.print_warning("\n⚠️ Exercício cancelado.")
            return
            
        if linhas_codigo:
            codigo_completo = '\n'.join(linhas_codigo)
            print("\n🚀 Sua criação:")
            try:
                self.executar_codigo(codigo_completo)
                self.print_success("\n🎨 Fantástico! Você criou um perfil usando variáveis!")
            except Exception as e:
                self.print_warning(f"❌ Erro na execução: {str(e)}")
        else:
            self.print_colored("👋 Tudo bem, talvez na próxima vez!", "info")
            
        self.pausar()
    


# Para teste standalone
if __name__ == "__main__":
    module = Modulo03Variaveis()
    print("Teste do módulo 3 - versão standalone")
    module._variaveis_interativo()