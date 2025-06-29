#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 13: Funções Avançadas
Aprenda sobre *args, **kwargs, lambda e programação funcional
"""

from ..shared.base_module import BaseModule


class Modulo13FuncoesAvancadas(BaseModule):
    """Módulo 13: Dominando Funções Avançadas"""
    
    def __init__(self):
        super().__init__("modulo_13", "Funções Avançadas & Lambda")
        self.has_mini_project = True
        self.mini_project_points = 80
    
    def execute(self) -> None:
        """Executa o módulo Funções Avançadas"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._funcoes_avancadas_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _funcoes_avancadas_interativo(self) -> None:
        """Conteúdo principal do módulo Funções Avançadas"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ MÓDULO 13: DOMINANDO FUNÇÕES AVANÇADAS")
        else:
            print("\n" + "="*50)
            print("⚡ MÓDULO 13: DOMINANDO FUNÇÕES AVANÇADAS")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos desbloquear o poder secreto das funções Python!")
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
            self._mini_projeto_analisador_inteligente()
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
                'id': 'secao_args_kwargs',
                'titulo': '🎯 *args e **kwargs: argumentos flexíveis',
                'descricao': 'Aprenda a criar funções super flexíveis',
                'funcao': self._secao_args_kwargs
            },
            {
                'id': 'secao_lambda',
                'titulo': '⚡ Lambda: funções de uma linha',
                'descricao': 'Domine as funções anônimas poderosas',
                'funcao': self._secao_lambda
            },
            {
                'id': 'secao_funcoes_ordem_superior',
                'titulo': '🔧 Funções de ordem superior',
                'descricao': 'map(), filter(), reduce() e programação funcional',
                'funcao': self._secao_funcoes_ordem_superior
            },
            {
                'id': 'secao_closures_decoradores',
                'titulo': '🎭 Closures e conceitos avançados',
                'descricao': 'Entenda como funções podem "lembrar" coisas',
                'funcao': self._secao_closures_decoradores
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas em projetos reais',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas e performance',
                'descricao': 'Técnicas avançadas de profissionais',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades e truques ninja',
                'descricao': 'Segredos que poucos programadores conhecem',
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
                    if progresso >= 4:  # Pelo menos 4 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 4 seções antes de continuar!")
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
    
    def _secao_args_kwargs(self) -> None:
        """Seção: *args e **kwargs - argumentos flexíveis"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("*ARGS E **KWARGS: ARGUMENTOS FLEXÍVEIS", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "*args e **kwargs",
            "Superpoderes que tornam funções capazes de receber qualquer quantidade de argumentos, como uma função que se adapta sozinha"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("*args = argumentos posicionais ilimitados | **kwargs = argumentos nomeados ilimitados!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine um restaurante onde o garçom pode anotar:", "text")
        self.print_colored("• *args = Qualquer quantidade de pratos (pizza, macarrão, salada...)", "text")
        self.print_colored("• **kwargs = Informações específicas (sem_sal=True, bem_passado=False)", "text")
        self.print_colored("• O garçom se adapta a qualquer pedido, não importa o tamanho!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 📦 *args coleta argumentos extras em uma TUPLA",
            "2. 🏷️ **kwargs coleta argumentos nomeados em um DICIONÁRIO",
            "3. 🔄 Python empacota automaticamente os argumentos",
            "4. ✨ Sua função fica infinitamente flexível!"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLOS PRÁTICOS ===
        self.print_colored("\n💻 VAMOS VER EM AÇÃO:", "success")
        
        exemplos_args = [
            {
                'titulo': 'EXEMPLO 1: *args em ação',
                'descricao': 'Função que soma qualquer quantidade de números',
                'codigo': '''# Função que aceita qualquer quantidade de números
def somar_todos(*numeros):
    print(f"Recebi os números: {numeros}")  # É uma tupla!
    total = sum(numeros)
    return total

# Testando com diferentes quantidades
print("Soma de 1, 2, 3:", somar_todos(1, 2, 3))
print("Soma de 10, 20, 30, 40:", somar_todos(10, 20, 30, 40))
print("Soma de apenas 42:", somar_todos(42))

# Função mais avançada
def criar_lista_compras(*itens):
    print("🛒 LISTA DE COMPRAS:")
    for i, item in enumerate(itens, 1):
        print(f"  {i}. {item}")
    print(f"Total de itens: {len(itens)}")

criar_lista_compras("Pão", "Leite", "Ovos", "Banana", "Café")''',
                'explicacao': '*args transforma múltiplos argumentos em uma tupla dentro da função'
            },
            {
                'titulo': 'EXEMPLO 2: **kwargs em ação',
                'descricao': 'Função que cria perfis personalizados',
                'codigo': '''# Função que aceita informações nomeadas ilimitadas
def criar_perfil(nome, **detalhes):
    print(f"\\n👤 PERFIL DE {nome.upper()}")
    print("="*30)
    
    for chave, valor in detalhes.items():
        emoji = "📧" if "email" in chave else "📍" if "cidade" in chave else "💼"
        print(f"{emoji} {chave.title()}: {valor}")

# Testando com diferentes informações
criar_perfil("Ana", idade=28, cidade="São Paulo", profissao="Desenvolvedora")
criar_perfil("Bruno", idade=35, email="bruno@email.com", hobby="Fotografia", salario=8000)

# Função de configuração flexível
def configurar_sistema(**config):
    configuracoes_padrao = {
        "tema": "claro",
        "idioma": "português",
        "notificacoes": True
    }
    
    # Atualiza configurações padrão com as fornecidas
    configuracoes_padrao.update(config)
    
    print("\\n⚙️ CONFIGURAÇÕES DO SISTEMA:")
    for setting, value in configuracoes_padrao.items():
        print(f"  • {setting}: {value}")

configurar_sistema(tema="escuro", idioma="inglês")''',
                'explicacao': '**kwargs transforma argumentos nomeados em um dicionário'
            },
            {
                'titulo': 'EXEMPLO 3: Combinando tudo',
                'descricao': 'Função super flexível com todos os tipos',
                'codigo': '''# Função que usa TODOS os tipos de argumentos
def funcao_suprema(obrigatorio, padrao="valor padrão", *args, **kwargs):
    print(f"\\n🚀 FUNÇÃO SUPREMA EXECUTANDO:")
    print(f"📌 Obrigatório: {obrigatorio}")
    print(f"🔧 Padrão: {padrao}")
    print(f"📦 Args extras: {args}")
    print(f"🏷️ Kwargs extras: {kwargs}")
    
    # Exemplo de uso prático
    if args:
        print(f"📊 Soma dos args: {sum(args)}")
    
    if "debug" in kwargs and kwargs["debug"]:
        print("🐛 Modo debug ativado!")

# Testando a função suprema
funcao_suprema("Obrigatório")
funcao_suprema("Item", "Customizado", 1, 2, 3, debug=True, versao="2.0")

# Exemplo real: sistema de log flexível
def log_evento(nivel, mensagem, *detalhes, **metadata):
    timestamp = "2024-01-15 10:30:00"
    
    print(f"\\n📝 [{timestamp}] {nivel.upper()}: {mensagem}")
    
    if detalhes:
        print("   Detalhes:", " | ".join(map(str, detalhes)))
    
    if metadata:
        print("   Metadata:", metadata)

log_evento("info", "Sistema iniciado")
log_evento("error", "Falha na conexão", "timeout", "retry_failed", usuario="admin", ip="192.168.1.1")''',
                'explicacao': 'Combinando tudo, você cria funções infinitamente flexíveis'
            }
        ]
        
        for i, exemplo in enumerate(exemplos_args, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos_args):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🌐 APIs web - endpoints que aceitam parâmetros flexíveis",
            "🔧 Frameworks - Django, Flask usam *args/**kwargs extensivamente",
            "📊 Análise de dados - funções que processam datasets variáveis",
            "🎮 Jogos - sistemas de configuração e customização",
            "🤖 Machine Learning - hiperparâmetros dinâmicos"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_lambda(self) -> None:
        """Seção: Lambda - funções de uma linha"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("LAMBDA: FUNÇÕES DE UMA LINHA", "⚡", "success")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Lambda",
            "Funções anônimas super compactas que fazem uma tarefa específica em uma única linha. São como 'funções descartáveis' para usar e jogar fora"
        )
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Lambda é como um guardanapo:", "text")
        self.print_colored("• 🍽️ Função normal = prato de porcelana (formal, reutilizável)", "text")
        self.print_colored("• 🧻 Lambda = guardanapo (rápido, prático, descartável)", "text")
        self.print_colored("• 💡 Você usa quando precisa de algo simples e rápido!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXEMPLOS PRÁTICOS ===
        exemplos_lambda = [
            {
                'titulo': 'LAMBDA BÁSICO: Operações simples',
                'descricao': 'Substitua funções pequenas por lambdas',
                'codigo': '''# Comparação: função normal vs lambda
def quadrado_normal(x):
    return x ** 2

# Mesma coisa com lambda - uma linha só!
quadrado_lambda = lambda x: x ** 2

print("🔢 TESTE DE QUADRADO:")
print(f"Normal: {quadrado_normal(5)}")
print(f"Lambda: {quadrado_lambda(5)}")

# Mais exemplos de lambdas simples
dobrar = lambda x: x * 2
eh_par = lambda x: x % 2 == 0
maior = lambda a, b: a if a > b else b
saudacao = lambda nome: f"Olá, {nome}!"

print("\\n⚡ LAMBDAS EM AÇÃO:")
print(f"Dobro de 7: {dobrar(7)}")
print(f"10 é par? {eh_par(10)}")
print(f"Maior entre 15 e 8: {maior(15, 8)}")
print(f"Saudação: {saudacao('Python')}")

# Lambda com múltiplos parâmetros
calculadora = lambda a, b, op: a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a / b

print("\\n🧮 CALCULADORA LAMBDA:")
print(f"10 + 5 = {calculadora(10, 5, '+')}")
print(f"10 * 3 = {calculadora(10, 3, '*')}")''',
                'explicacao': 'Lambda é perfeito para operações simples que cabem em uma linha'
            },
            {
                'titulo': 'LAMBDA COM LISTAS: map(), filter(), sorted()',
                'descricao': 'O verdadeiro poder das lambdas aparece com listas',
                'codigo': '''# Lista de números para testar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("📋 LISTA ORIGINAL:", numeros)

# map() - aplica função a todos elementos
quadrados = list(map(lambda x: x**2, numeros))
print("🔢 Quadrados:", quadrados)

# filter() - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda x: x % 2 != 0, numeros))
print("📊 Pares:", pares)
print("📊 Ímpares:", impares)

# Exemplo com strings
nomes = ["ana", "BRUNO", "carla", "DIEGO", "eva"]
print("\\n👤 NOMES ORIGINAIS:", nomes)

# Transformar tudo para título
nomes_titulo = list(map(lambda nome: nome.title(), nomes))
print("✨ Em título:", nomes_titulo)

# Filtrar nomes com mais de 3 letras
nomes_longos = list(filter(lambda nome: len(nome) > 3, nomes))
print("📏 Nomes longos:", nomes_longos)

# sorted() com lambda - ordenação customizada
idades = [("Ana", 25), ("Bruno", 30), ("Carla", 22), ("Diego", 35)]
print("\\n👥 PESSOAS E IDADES:", idades)

# Ordenar por idade
por_idade = sorted(idades, key=lambda pessoa: pessoa[1])
print("📈 Por idade:", por_idade)

# Ordenar por nome
por_nome = sorted(idades, key=lambda pessoa: pessoa[0])
print("🔤 Por nome:", por_nome)''',
                'explicacao': 'Lambda + map/filter/sorted = combinação poderosa para processar dados'
            },
            {
                'titulo': 'LAMBDA AVANÇADO: Casos reais',
                'descricao': 'Lambdas em situações do mundo real',
                'codigo': '''# Lista de produtos de e-commerce
produtos = [
    {"nome": "Notebook", "preco": 2500, "categoria": "Eletrônicos", "estoque": 10},
    {"nome": "Mouse", "preco": 45, "categoria": "Eletrônicos", "estoque": 50},
    {"nome": "Livro Python", "preco": 80, "categoria": "Livros", "estoque": 25},
    {"nome": "Mesa", "preco": 300, "categoria": "Móveis", "estoque": 5},
    {"nome": "Cadeira", "preco": 200, "categoria": "Móveis", "estoque": 0}
]

print("🛒 LOJA VIRTUAL - ANÁLISE DE PRODUTOS\\n")

# 1. Produtos em estoque
em_estoque = list(filter(lambda p: p["estoque"] > 0, produtos))
print(f"📦 Produtos em estoque: {len(em_estoque)}")
for p in em_estoque:
    print(f"  • {p['nome']} - R$ {p['preco']}")

# 2. Produtos caros (>R$ 100)
caros = list(filter(lambda p: p["preco"] > 100, produtos))
print(f"\\n💰 Produtos caros (>{100}): {len(caros)}")

# 3. Ordenar por preço (maior para menor)
por_preco = sorted(produtos, key=lambda p: p["preco"], reverse=True)
print("\\n📊 PRODUTOS POR PREÇO (MAIOR→MENOR):")
for p in por_preco:
    print(f"  R$ {p['preco']:>6} - {p['nome']}")

# 4. Aplicar desconto de 10% em eletrônicos
eletronicos = list(filter(lambda p: p["categoria"] == "Eletrônicos", produtos))
eletronicos_desconto = list(map(lambda p: {**p, "preco": p["preco"] * 0.9}, eletronicos))

print("\\n⚡ ELETRÔNICOS COM 10% DESCONTO:")
for p in eletronicos_desconto:
    print(f"  • {p['nome']}: R$ {p['preco']:.2f}")

# 5. Criar relatório de estoque baixo
estoque_baixo = list(filter(lambda p: p["estoque"] < 10, produtos))
print(f"\\n⚠️ ALERTA: {len(estoque_baixo)} produtos com estoque baixo")

# 6. Valor total do estoque
valor_total = sum(map(lambda p: p["preco"] * p["estoque"], produtos))
print(f"\\n💵 VALOR TOTAL DO ESTOQUE: R$ {valor_total:,.2f}")''',
                'explicacao': 'Lambdas são essenciais para análise de dados e operações em listas complexas'
            }
        ]
        
        for i, exemplo in enumerate(exemplos_lambda, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.exemplo(exemplo['codigo'])
            print(f"\n🚀 Executando exemplo {i}:")
            self.executar_codigo(exemplo['codigo'])
            
            self.print_colored(f"\n💡 {exemplo['explicacao']}", "info")
            
            if i < len(exemplos_lambda):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você domina o poder das funções lambda!")
        self.pausar()
    
    def _secao_funcoes_ordem_superior(self) -> None:
        """Seção: Funções de ordem superior"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FUNÇÕES DE ORDEM SUPERIOR", "🔧", "success")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Funções de Ordem Superior",
            "Funções especiais que trabalham COM outras funções - como supervisores que comandam uma equipe de funções trabalhadores"
        )
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma fábrica de processamento:", "text")
        self.print_colored("• 🏭 map() = esteira que TRANSFORMA cada item", "text")
        self.print_colored("• 🔍 filter() = inspetor que SELECIONA apenas alguns", "text")
        self.print_colored("• 📊 reduce() = máquina que COMBINA tudo em um resultado", "text")
        self.print_colored("• ⚙️ As funções são os OPERÁRIOS que fazem o trabalho!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXEMPLOS DETALHADOS ===
        exemplos_ordem_superior = [
            {
                'titulo': 'MAP(): O Transformador Universal',
                'descricao': 'Aplica uma função a todos os elementos',
                'codigo': '''# MAP: aplica função a cada elemento da lista
print("🔄 MAP(): TRANSFORMADOR UNIVERSAL\\n")

# Exemplo 1: Converter temperaturas
celsius = [0, 10, 20, 30, 40, 100]
print(f"🌡️ Celsius: {celsius}")

# Converter para Fahrenheit: F = C * 9/5 + 32
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(f"🌡️ Fahrenheit: {fahrenheit}")

# Exemplo 2: Processar nomes
funcionarios = ["joão silva", "maria santos", "pedro costa"]
print(f"\\n👤 Nomes originais: {funcionarios}")

# Transformar em formato profissional
nomes_profissionais = list(map(lambda nome: nome.title(), funcionarios))
print(f"✨ Nomes profissionais: {nomes_profissionais}")

# Criar emails corporativos
emails = list(map(lambda nome: f"{nome.lower().replace(' ', '.')}@empresa.com", funcionarios))
print(f"📧 Emails corporativos: {emails}")

# Exemplo 3: Aplicar desconto em produtos
precos = [100, 250, 80, 300, 150]
desconto_10 = list(map(lambda p: p * 0.9, precos))
desconto_15 = list(map(lambda p: p * 0.85, precos))

print(f"\\n💰 Preços originais: {precos}")
print(f"💰 Com 10% desconto: {[f'{p:.2f}' for p in desconto_10]}")
print(f"💰 Com 15% desconto: {[f'{p:.2f}' for p in desconto_15]}")

# Exemplo 4: Map com múltiplas listas
numeros1 = [1, 2, 3, 4, 5]
numeros2 = [10, 20, 30, 40, 50]

# Somar elementos correspondentes
somas = list(map(lambda x, y: x + y, numeros1, numeros2))
print(f"\\n🔢 Lista 1: {numeros1}")
print(f"🔢 Lista 2: {numeros2}")
print(f"➕ Somas: {somas}")''',
                'explicacao': 'map() transforma TODOS os elementos aplicando a mesma função'
            },
            {
                'titulo': 'FILTER(): O Seletor Inteligente',
                'descricao': 'Filtra elementos que atendem uma condição',
                'codigo': '''# FILTER: seleciona apenas elementos que passam no teste
print("🔍 FILTER(): SELETOR INTELIGENTE\\n")

# Exemplo 1: Filtrar números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"🔢 Números: {numeros}")

pares = list(filter(lambda x: x % 2 == 0, numeros))
maiores_que_5 = list(filter(lambda x: x > 5, numeros))
multiplos_de_3 = list(filter(lambda x: x % 3 == 0, numeros))

print(f"📊 Pares: {pares}")
print(f"📊 Maiores que 5: {maiores_que_5}")
print(f"📊 Múltiplos de 3: {multiplos_de_3}")

# Exemplo 2: Filtrar produtos
produtos = [
    {"nome": "Notebook", "preco": 2500, "categoria": "tech"},
    {"nome": "Mouse", "preco": 45, "categoria": "tech"},
    {"nome": "Livro", "preco": 80, "categoria": "educacao"},
    {"nome": "Mesa", "preco": 300, "categoria": "moveis"},
    {"nome": "Smartphone", "preco": 1200, "categoria": "tech"}
]

print("\\n🛒 FILTRAGEM DE PRODUTOS:")

# Produtos de tecnologia
tech_products = list(filter(lambda p: p["categoria"] == "tech", produtos))
print(f"📱 Produtos tech: {[p['nome'] for p in tech_products]}")

# Produtos caros (>R$ 500)
caros = list(filter(lambda p: p["preco"] > 500, produtos))
print(f"💰 Produtos caros: {[p['nome'] for p in caros]}")

# Produtos tech E caros
tech_caros = list(filter(lambda p: p["categoria"] == "tech" and p["preco"] > 1000, produtos))
print(f"🚀 Tech caros: {[p['nome'] for p in tech_caros]}")

# Exemplo 3: Filtrar strings
palavras = ["python", "java", "javascript", "go", "rust", "typescript"]
print(f"\\n📝 Palavras: {palavras}")

# Palavras com mais de 4 letras
longas = list(filter(lambda w: len(w) > 4, palavras))
print(f"📏 Palavras longas: {longas}")

# Palavras que contêm "script"
com_script = list(filter(lambda w: "script" in w, palavras))
print(f"📜 Com 'script': {com_script}")

# Exemplo 4: Filtrar por múltiplas condições
vendas = [1200, 800, 450, 1500, 300, 950, 1800, 600, 750, 1100]
print(f"\\n📈 Vendas: {vendas}")

# Vendas médias (entre 500 e 1000)
vendas_medias = list(filter(lambda v: 500 <= v <= 1000, vendas))
print(f"📊 Vendas médias (500-1000): {vendas_medias}")''',
                'explicacao': 'filter() seleciona apenas elementos que passam no teste da função'
            },
            {
                'titulo': 'REDUCE(): O Combinador Supremo',
                'descricao': 'Combina todos os elementos em um único resultado',
                'codigo': '''# REDUCE: combina todos elementos em um só resultado
from functools import reduce

print("📊 REDUCE(): COMBINADOR SUPREMO\\n")

# Exemplo 1: Operações matemáticas
numeros = [1, 2, 3, 4, 5]
print(f"🔢 Números: {numeros}")

# Somar todos
soma = reduce(lambda x, y: x + y, numeros)
print(f"➕ Soma: {soma}")

# Multiplicar todos (fatorial-like)
produto = reduce(lambda x, y: x * y, numeros)
print(f"✖️ Produto: {produto}")

# Encontrar o maior
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(f"📈 Maior: {maior}")

# Exemplo 2: Combinar strings
palavras = ["Python", "é", "incrível", "para", "programar"]
print(f"\\n📝 Palavras: {palavras}")

# Juntar com espaços
frase = reduce(lambda x, y: f"{x} {y}", palavras)
print(f"💬 Frase: {frase}")

# Exemplo 3: Análise de vendas
vendas_diarias = [1200, 800, 1500, 950, 1100, 1300, 750]
print(f"\\n📈 Vendas diárias: {vendas_diarias}")

# Total de vendas
total = reduce(lambda x, y: x + y, vendas_diarias)
print(f"💰 Total da semana: R$ {total}")

# Exemplo 4: Aninhamento de listas
listas = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(f"\\n📋 Listas aninhadas: {listas}")

# Achatar (flatten) - juntar todas em uma
achatar = reduce(lambda x, y: x + y, listas)
print(f"🔄 Achatada: {achatar}")

# Exemplo 5: Processamento complexo - carrinho de compras
carrinho = [
    {"produto": "Notebook", "preco": 2500, "quantidade": 1},
    {"produto": "Mouse", "preco": 45, "quantidade": 2},
    {"produto": "Teclado", "preco": 120, "quantidade": 1}
]

print("\\n🛒 CARRINHO DE COMPRAS:")
for item in carrinho:
    subtotal = item["preco"] * item["quantidade"]
    print(f"  {item['produto']}: R$ {item['preco']} x {item['quantidade']} = R$ {subtotal}")

# Calcular total do carrinho
total_carrinho = reduce(
    lambda total, item: total + (item["preco"] * item["quantidade"]),
    carrinho,
    0  # valor inicial
)
print(f"\\n💳 TOTAL DO CARRINHO: R$ {total_carrinho}")''',
                'explicacao': 'reduce() combina todos os elementos aplicando a função de forma acumulativa'
            }
        ]
        
        for i, exemplo in enumerate(exemplos_ordem_superior, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.exemplo(exemplo['codigo'])
            print(f"\n🚀 Executando exemplo {i}:")
            self.executar_codigo(exemplo['codigo'])
            
            self.print_colored(f"\n💡 {exemplo['explicacao']}", "info")
            
            if i < len(exemplos_ordem_superior):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você domina as funções de ordem superior!")
        self.pausar()
    
    def _secao_closures_decoradores(self) -> None:
        """Seção: Closures e conceitos avançados"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CLOSURES E CONCEITOS AVANÇADOS", "🎭")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Closure",
            "Uma função que 'lembra' de variáveis do ambiente onde foi criada, mesmo depois que sai de lá. É como uma função com memória!"
        )
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Closure é como um funcionário que leva trabalho para casa:", "text")
        self.print_colored("• 🏢 Função interna = funcionário", "text")
        self.print_colored("• 💼 Variáveis externas = documentos importantes do escritório", "text")
        self.print_colored("• 🏠 Quando vai para casa, leva cópias dos documentos", "text")
        self.print_colored("• 📋 Pode trabalhar em casa usando esses documentos!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXEMPLOS PRÁTICOS ===
        self.print_colored("\n💻 CLOSURES EM AÇÃO:", "success")
        
        exemplo_closure = '''# CLOSURES: funções que "lembram" do ambiente
print("🧠 CLOSURES: FUNÇÕES COM MEMÓRIA\\n")

# Exemplo 1: Contador com memória
def criar_contador():
    # Variável no escopo externo
    count = 0
    
    def incrementar():
        nonlocal count  # Permite modificar variável externa
        count += 1
        return count
    
    return incrementar  # Retorna a função interna

# Criando contadores independentes
contador1 = criar_contador()
contador2 = criar_contador()

print("🔢 CONTADORES INDEPENDENTES:")
print(f"Contador 1: {contador1()}")  # 1
print(f"Contador 1: {contador1()}")  # 2
print(f"Contador 2: {contador2()}")  # 1 (independente!)
print(f"Contador 1: {contador1()}")  # 3
print(f"Contador 2: {contador2()}")  # 2

# Exemplo 2: Multiplicador personalizado
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator  # 'fator' lembrado do escopo externo
    return multiplicar

dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
multiplicar_por_10 = criar_multiplicador(10)

print("\\n✖️ MULTIPLICADORES PERSONALIZADOS:")
print(f"Dobrar 5: {dobrar(5)}")
print(f"Triplicar 4: {triplicar(4)}")
print(f"10x de 7: {multiplicar_por_10(7)}")

# Exemplo 3: Sistema de configuração
def criar_configurador(prefixo, sufixo):
    def formatar(texto):
        return f"{prefixo}{texto}{sufixo}"
    return formatar

html_bold = criar_configurador("<b>", "</b>")
markdown_code = criar_configurador("`", "`")
brackets = criar_configurador("[", "]")

print("\\n🎨 FORMATADORES PERSONALIZADOS:")
print(f"HTML Bold: {html_bold('Python')}")
print(f"Markdown Code: {markdown_code('lambda')}")
print(f"Brackets: {brackets('closure')}")'''
        
        self.exemplo(exemplo_closure)
        print("🚀 Vamos ver closures funcionando:")
        self.executar_codigo(exemplo_closure)
        
        input("\n🔸 Pressione ENTER para ver decoradores básicos...")
        
        # === INTRODUÇÃO A DECORADORES ===
        self.print_colored("\n🎭 INTRODUÇÃO A DECORADORES:", "info")
        
        exemplo_decorador = '''# DECORADORES: funções que modificam outras funções
print("🎭 DECORADORES BÁSICOS\\n")

# Exemplo 1: Decorador simples de tempo
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo = fim - inicio
        print(f"⏱️ {func.__name__} executou em {tempo:.4f} segundos")
        return resultado
    return wrapper

# Usando o decorador manualmente
def calcular_soma():
    total = sum(range(1000000))
    return total

# Aplicando decorador
soma_com_tempo = medir_tempo(calcular_soma)
resultado = soma_com_tempo()
print(f"Resultado: {resultado}")

# Exemplo 2: Decorador de log
def log_chamadas(func):
    def wrapper(*args, **kwargs):
        print(f"📝 Chamando função: {func.__name__}")
        if args:
            print(f"   Args: {args}")
        if kwargs:
            print(f"   Kwargs: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"✅ {func.__name__} concluída")
        return resultado
    return wrapper

# Função simples para testar
def saudacao(nome, entusiasmo=1):
    return f"Olá, {nome}!" + "!" * entusiasmo

# Aplicando decorador
saudacao_com_log = log_chamadas(saudacao)
resultado = saudacao_com_log("Python", entusiasmo=3)
print(f"Resultado: {resultado}")

# Exemplo 3: Decorador de cache simples
def cache_simples(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"🎯 Cache hit para {args}")
            return cache[args]
        
        print(f"💾 Calculando para {args}")
        resultado = func(*args)
        cache[args] = resultado
        return resultado
    
    return wrapper

# Função pesada para demonstrar cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Aplicando cache
fib_com_cache = cache_simples(fibonacci)

print("\\n🔢 FIBONACCI COM CACHE:")
print(f"fib(10) primeira vez: {fib_com_cache(10)}")
print(f"fib(10) segunda vez: {fib_com_cache(10)}")  # Vem do cache!'''
        
        self.exemplo(exemplo_decorador)
        print("🚀 Vamos ver decoradores em ação:")
        self.executar_codigo(exemplo_decorador)
        
        # === APLICAÇÕES PRÁTICAS ===
        self.print_colored("\n🌍 ONDE SÃO USADOS:", "accent")
        aplicacoes_avancadas = [
            "🌐 Web frameworks - autenticação, cache, logging",
            "🔒 Segurança - validação de permissões",
            "📊 Performance - medição de tempo, profiling",
            "🎮 Games - sistemas de eventos e callbacks",
            "🤖 APIs - rate limiting, validação de dados"
        ]
        for app in aplicacoes_avancadas:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_casos_uso_reais(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR NA VIDA REAL?", "🌍", "accent")
        
        # === CASOS DE USO PRÁTICOS ===
        self.print_colored("🚀 PROJETOS REAIS QUE USAM FUNÇÕES AVANÇADAS:", "warning")
        
        casos_reais = [
            {
                'setor': '🌐 DESENVOLVIMENTO WEB',
                'aplicacao': 'API REST com Flask',
                'exemplo': '''# Sistema de API REST usando funções avançadas
from functools import wraps

# Decorador de autenticação
def requer_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not validar_token(token):
            return {'error': 'Token inválido'}, 401
        return f(*args, **kwargs)
    return wrapper

# Endpoint com validação flexível
@app.route('/usuarios', methods=['POST'])
@requer_auth
def criar_usuario(**dados_usuario):
    # Validação usando filter + lambda
    campos_obrigatorios = ['nome', 'email']
    faltando = list(filter(lambda c: c not in dados_usuario, campos_obrigatorios))
    
    if faltando:
        return {'error': f'Campos obrigatórios: {faltando}'}, 400
    
    # Processamento usando map
    dados_limpos = {
        k: v.strip().lower() if isinstance(v, str) else v 
        for k, v in dados_usuario.items()
    }
    
    return criar_usuario_db(dados_limpos)'''
            },
            {
                'setor': '📊 CIÊNCIA DE DADOS',
                'aplicacao': 'Pipeline de Processamento',
                'exemplo': '''# Pipeline de análise de dados
def criar_pipeline(*operacoes):
    def processar(dados):
        # reduce aplicando todas as operações em sequência
        return reduce(lambda d, op: op(d), operacoes, dados)
    return processar

# Operações usando lambdas
limpar_dados = lambda df: df.dropna()
normalizar = lambda df: (df - df.mean()) / df.std()
filtrar_outliers = lambda df: df[abs(df) < 3]

# Criar pipeline personalizado
pipeline_completo = criar_pipeline(
    limpar_dados,
    normalizar,
    filtrar_outliers
)

# Aplicar em dataset
dados_processados = pipeline_completo(dados_brutos)'''
            },
            {
                'setor': '🎮 DESENVOLVIMENTO DE JOGOS',
                'aplicacao': 'Sistema de Eventos',
                'exemplo': '''# Sistema de eventos em jogos
class GameEventSystem:
    def __init__(self):
        self.listeners = {}
    
    def on(self, evento, callback):
        """Registra callback para evento"""
        if evento not in self.listeners:
            self.listeners[evento] = []
        self.listeners[evento].append(callback)
    
    def emit(self, evento, **dados):
        """Dispara evento para todos os listeners"""
        if evento in self.listeners:
            # Cada callback recebe os dados usando **kwargs
            for callback in self.listeners[evento]:
                callback(**dados)

# Uso no jogo
game_events = GameEventSystem()

# Registrar eventos usando lambda
game_events.on('player_level_up', lambda level, player: print(f"{player} subiu para level {level}!"))
game_events.on('item_collected', lambda item, player: add_to_inventory(player, item))

# Disparar eventos
game_events.emit('player_level_up', level=5, player='João')'''
            }
        ]
        
        for caso in casos_reais:
            self.print_colored(f"\n{caso['setor']}: {caso['aplicacao']}", "info")
            self.exemplo(caso['exemplo'])
            input("🔸 Pressione ENTER para o próximo caso...")
        
        # === CASOS PRÁTICOS DIRETOS ===
        self.print_colored("\n💼 SITUAÇÕES DO DIA A DIA:", "success")
        
        codigo_pratico = '''# Casos práticos que você encontrará no trabalho
print("💼 SITUAÇÕES REAIS DE TRABALHO\\n")

# 1. PROCESSAMENTO DE LOGS
logs = [
    "2024-01-15 10:30:00 ERROR: Database connection failed",
    "2024-01-15 10:30:01 INFO: Retrying connection",
    "2024-01-15 10:30:02 INFO: Connection successful",
    "2024-01-15 10:31:00 WARNING: High memory usage",
    "2024-01-15 10:32:00 ERROR: API timeout"
]

print("📋 LOGS ORIGINAIS:")
for log in logs[:3]:
    print(f"  {log}")
print("  ...")

# Filtrar apenas erros
erros = list(filter(lambda log: "ERROR" in log, logs))
print(f"\\n❌ ERROS ENCONTRADOS: {len(erros)}")
for erro in erros:
    print(f"  {erro}")

# Extrair apenas horários
horarios = list(map(lambda log: log.split()[1], logs))
print(f"\\n🕐 HORÁRIOS: {horarios}")

# 2. VALIDAÇÃO DE FORMULÁRIO
formulario = {
    "nome": "  João Silva  ",
    "email": "JOAO@EMAIL.COM",
    "idade": "25",
    "telefone": "(11) 99999-9999"
}

print("\\n📝 VALIDAÇÃO DE FORMULÁRIO:")
print("Original:", formulario)

# Pipeline de limpeza usando map
limpar_campo = lambda valor: valor.strip() if isinstance(valor, str) else valor
normalizar_email = lambda email: email.lower() if "@" in email else email
converter_idade = lambda idade: int(idade) if idade.isdigit() else 0

# Aplicar limpezas
formulario_limpo = {k: limpar_campo(v) for k, v in formulario.items()}
formulario_limpo["email"] = normalizar_email(formulario_limpo["email"])
formulario_limpo["idade"] = converter_idade(formulario_limpo["idade"])

print("Limpo:", formulario_limpo)

# 3. ANÁLISE DE VENDAS POR DEPARTAMENTO
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 2500, "vendedor": "Ana"},
    {"produto": "Livro", "categoria": "Educação", "valor": 45, "vendedor": "Bruno"},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 80, "vendedor": "Ana"},
    {"produto": "Curso", "categoria": "Educação", "valor": 200, "vendedor": "Carla"},
    {"produto": "Tablet", "categoria": "Eletrônicos", "valor": 800, "vendedor": "Bruno"}
]

print("\\n📊 ANÁLISE DE VENDAS:")

# Vendas por categoria
from itertools import groupby

vendas_ordenadas = sorted(vendas, key=lambda v: v["categoria"])
por_categoria = {}
for categoria, grupo in groupby(vendas_ordenadas, key=lambda v: v["categoria"]):
    valores = [v["valor"] for v in grupo]
    por_categoria[categoria] = {
        "total": sum(valores),
        "quantidade": len(valores),
        "media": sum(valores) / len(valores)
    }

for cat, dados in por_categoria.items():
    print(f"  {cat}: R$ {dados['total']} (média: R$ {dados['media']:.2f})")

# Top vendedores
vendas_por_vendedor = {}
for venda in vendas:
    vendedor = venda["vendedor"]
    if vendedor not in vendas_por_vendedor:
        vendas_por_vendedor[vendedor] = 0
    vendas_por_vendedor[vendedor] += venda["valor"]

top_vendedores = sorted(vendas_por_vendedor.items(), key=lambda x: x[1], reverse=True)
print(f"\\n🏆 TOP VENDEDORES:")
for vendedor, total in top_vendedores:
    print(f"  {vendedor}: R$ {total}")'''
        
        self.exemplo(codigo_pratico)
        print("🚀 Vamos ver casos práticos:")
        self.executar_codigo(codigo_pratico)
        
        self.print_success("\n🎉 Agora você vê como usar funções avançadas no trabalho real!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas e performance"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS E PERFORMANCE", "⭐")
        
        # === DICAS PROFISSIONAIS ===
        self.print_colored("💎 DICAS DE PROFISSIONAIS EXPERIENTES:", "warning")
        
        dicas_profissionais = [
            {
                'titulo': '1. Quando usar Lambda vs Função Normal',
                'bom': '''# ✅ Use lambda para operações SIMPLES de uma linha
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
ordenados = sorted(pessoas, key=lambda p: p["idade"])''',
                'ruim': '''# ❌ Evite lambdas complexas - use função normal
# Ruim: lambda complexo
processar = lambda x: x.strip().lower().replace(" ", "_") if isinstance(x, str) and len(x) > 0 else "default"

# Melhor: função normal
def processar_texto(texto):
    """Processa texto removendo espaços e convertendo para lowercase"""
    if not isinstance(texto, str) or len(texto) == 0:
        return "default"
    return texto.strip().lower().replace(" ", "_")''',
                'explicacao': 'Lambda para operações simples, funções normais para lógica complexa'
            },
            {
                'titulo': '2. Performance: Generator vs List',
                'bom': '''# ✅ Use generators para economia de memória
def processar_arquivo_grande():
    with open("arquivo_gigante.txt", "r") as file:
        # Generator - processa um por vez
        for linha in file:
            yield linha.strip().upper()

# Usa pouca memória mesmo com arquivos gigantes
for linha_processada in processar_arquivo_grande():
    print(linha_processada)''',
                'ruim': '''# ❌ Carregar tudo na memória pode explodir o sistema
def processar_arquivo_ruim():
    with open("arquivo_gigante.txt", "r") as file:
        # Lista - carrega TUDO na memória
        return [linha.strip().upper() for linha in file]

# Pode usar 10GB+ de RAM!
todas_linhas = processar_arquivo_ruim()''',
                'explicacao': 'Generators economizam memória processando um item por vez'
            },
            {
                'titulo': '3. *args e **kwargs: Use com Moderação',
                'bom': '''# ✅ Use quando realmente precisar de flexibilidade
def log_evento(nivel, mensagem, *detalhes, **metadata):
    """Log com argumentos flexíveis mas bem documentados"""
    timestamp = datetime.now()
    print(f"[{timestamp}] {nivel}: {mensagem}")
    
    if detalhes:
        print(f"Detalhes: {detalhes}")
    
    if metadata:
        for key, value in metadata.items():
            print(f"  {key}: {value}")

# Uso claro e intuitivo
log_evento("ERROR", "Falha na conexão", "timeout", "retry_failed", 
           usuario="admin", ip="192.168.1.1")''',
                'ruim': '''# ❌ Não abuse - seja específico quando possível
def funcao_confusa(*args, **kwargs):
    """Função que aceita qualquer coisa - difícil de usar!"""
    # Usuário não sabe o que passar
    # Documentação impossível
    # Debugging complicado
    pass

# Como usar isso? Ninguém sabe!
funcao_confusa("algo", 123, flag=True)  # ???''',
                'explicacao': 'Use *args/**kwargs quando a flexibilidade for realmente necessária'
            }
        ]
        
        for dica in dicas_profissionais:
            self.print_colored(f"\n{dica['titulo']}", "info")
            self.print_colored("✅ RECOMENDADO:", "success")
            self.exemplo(dica['bom'])
            if 'ruim' in dica:
                self.print_colored("\n❌ EVITE:", "warning")
                self.exemplo(dica['ruim'])
            self.print_colored(f"\n💡 {dica['explicacao']}", "accent")
            input("\n🔸 Pressione ENTER para a próxima dica...")
        
        # === PERFORMANCE E OTIMIZAÇÃO ===
        self.print_colored("\n⚡ DICAS DE PERFORMANCE:", "success")
        
        codigo_performance = '''# Comparando performance de diferentes abordagens
import time

# Dados para teste
numeros = list(range(1000000))

print("⚡ TESTE DE PERFORMANCE\\n")

# 1. List Comprehension vs map()
print("🔄 LIST COMPREHENSION vs MAP:")

# List comprehension
start = time.time()
quadrados_lc = [x**2 for x in numeros]
tempo_lc = time.time() - start

# Map com lambda
start = time.time()
quadrados_map = list(map(lambda x: x**2, numeros))
tempo_map = time.time() - start

print(f"List comprehension: {tempo_lc:.4f}s")
print(f"Map + lambda: {tempo_map:.4f}s")
print(f"Vencedor: {'List comprehension' if tempo_lc < tempo_map else 'Map'}")

# 2. Filter vs List Comprehension
print("\\n🔍 FILTER vs LIST COMPREHENSION:")

# Filter
start = time.time()
pares_filter = list(filter(lambda x: x % 2 == 0, numeros))
tempo_filter = time.time() - start

# List comprehension com if
start = time.time()
pares_lc = [x for x in numeros if x % 2 == 0]
tempo_lc = time.time() - start

print(f"Filter: {tempo_filter:.4f}s")
print(f"List comprehension: {tempo_lc:.4f}s")
print(f"Vencedor: {'Filter' if tempo_filter < tempo_lc else 'List comprehension'}")

# 3. Generator vs List
print("\\n🔄 GENERATOR vs LIST (memória):")

# Generator
def quadrados_generator(nums):
    for num in nums:
        yield num ** 2

# Lista
def quadrados_lista(nums):
    return [num ** 2 for num in nums]

# Teste de memória (simulado)
print("Generator: Usa ~100MB independente do tamanho")
print("Lista: Usa memória proporcional ao tamanho dos dados")
print("Para 1M números: Generator ~100MB, Lista ~400MB+")

print("\\n💡 DICAS FINAIS:")
print("• List comprehension geralmente é mais rápida")
print("• Use generators para economizar memória")
print("• map/filter são úteis com funções já existentes")
print("• Meça sempre - performance pode variar!")'''
        
        self.exemplo(codigo_performance)
        print("🚀 Testando performance:")
        self.executar_codigo(codigo_performance)
        
        # === RESUMO DAS MELHORES PRÁTICAS ===
        self.print_colored("\n📋 RESUMO DAS MELHORES PRÁTICAS:", "accent")
        praticas_resumo = [
            "⚡ Lambda: só para operações simples de uma linha",
            "📝 Documentação: sempre documente *args/**kwargs",
            "🧠 Legibilidade: prefira código claro a código 'clever'",
            "🔄 Generators: use para economizar memória",
            "📊 Performance: list comprehension geralmente vence",
            "🎯 Simplicidade: complexo demais? Use função normal"
        ]
        
        for pratica in praticas_resumo:
            self.print_colored(f"• {pratica}", "primary")
        
        self.print_success("\n🎉 Agora você programa como os profissionais!")
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades e truques ninja"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES E TRUQUES NINJA", "💫")
        
        # === TRUQUES AVANÇADOS ===
        self.print_colored("🥷 TRUQUES QUE POUCOS CONHECEM:", "warning")
        
        truques_ninja = [
            {
                'titulo': '🎭 Lambdas Recursivas (Mente = Explodida)',
                'codigo': '''# Lambdas podem ser recursivas! 🤯
print("🎭 LAMBDAS RECURSIVAS - TRUQUE NINJA\\n")

# Fatorial com lambda recursiva
fatorial = (lambda f, n: 1 if n <= 1 else n * f(f, n-1))
print(f"Fatorial de 5: {fatorial(fatorial, 5)}")

# Fibonacci com lambda recursiva
fib = (lambda f, n: n if n <= 1 else f(f, n-1) + f(f, n-2))
print(f"Fibonacci de 10: {fib(fib, 10)}")

# Versão mais elegante usando Y combinator (ultra ninja!)
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
fatorial_y = Y(lambda f: lambda n: 1 if n <= 1 else n * f(n-1))
print(f"Fatorial Y de 6: {fatorial_y(6)}")

print("🤯 Sim, lambdas podem ser recursivas!")''',
                'explicacao': 'Lambdas recursivas são possíveis mas raramente usadas na prática'
            },
            {
                'titulo': '🔥 Operador Walrus + Lambda',
                'codigo': '''# Operador := (walrus) com lambdas
print("🔥 OPERADOR WALRUS + LAMBDA\\n")

# Processamento com armazenamento inline
numeros = [1, 4, 9, 16, 25, 36, 49]

# Normal: calcular e armazenar
resultados = []
for n in numeros:
    raiz = n ** 0.5
    if raiz > 3:
        resultados.append(raiz)

print(f"Método normal: {resultados}")

# Ninja: walrus + lambda
resultados_ninja = [raiz for n in numeros if (raiz := n ** 0.5) > 3]
print(f"Método ninja: {resultados_ninja}")

# Ainda mais ninja: com lambda
processar = lambda nums: [r for n in nums if (r := n ** 0.5) > 3]
print(f"Ultra ninja: {processar(numeros)}")

# Walrus em filter (mente explodindo)
dados = ["python", "java", "javascript", "go", "typescript"]
longos = list(filter(lambda s: (tam := len(s)) > 4 and print(f"{s}: {tam} chars"), dados))
print(f"\\nPalavras longas: {[s for s in dados if len(s) > 4]}")''',
                'explicacao': 'Operador walrus (:=) permite assignment dentro de expressões'
            },
            {
                'titulo': '🎪 Partial Functions: Funções Parciais',
                'codigo': '''# functools.partial: criando funções pré-configuradas
from functools import partial

print("🎪 FUNÇÕES PARCIAIS - TRUQUE MÁGICO\\n")

# Função base
def potencia(base, expoente):
    return base ** expoente

# Criando funções especializadas
quadrado = partial(potencia, expoente=2)
cubo = partial(potencia, expoente=3)
potencia_de_2 = partial(potencia, 2)  # base fixada

print(f"Quadrado de 5: {quadrado(5)}")
print(f"Cubo de 3: {cubo(3)}")
print(f"2^8: {potencia_de_2(8)}")

# Exemplo prático: configuração de logger
def log_message(level, module, message):
    print(f"[{level}] {module}: {message}")

# Loggers especializados
log_error = partial(log_message, "ERROR")
log_db = partial(log_message, "INFO", "DATABASE")
log_api_error = partial(log_message, "ERROR", "API")

log_error("CORE", "Sistema falhou")
log_db("Conexão estabelecida")
log_api_error("Timeout na requisição")

# Partial com map - ninja supremo!
numeros = [1, 2, 3, 4, 5]
multiplicar = lambda x, fator: x * fator
multiplicar_por_3 = partial(multiplicar, fator=3)

resultado = list(map(multiplicar_por_3, numeros))
print(f"\\nMultiplicados por 3: {resultado}")''',
                'explicacao': 'Partial permite criar versões especializadas de funções'
            },
            {
                'titulo': '🧙‍♂️ Metaclasses e Funções Dinâmicas',
                'codigo': '''# Criando funções dinamicamente - magia pura!
print("🧙‍♂️ CRIAÇÃO DINÂMICA DE FUNÇÕES\\n")

# 1. Criando funções com exec (cuidado!)
operacoes = ['somar', 'multiplicar', 'dividir']
for op in operacoes:
    if op == 'somar':
        codigo = f"lambda a, b: a + b"
    elif op == 'multiplicar':
        codigo = f"lambda a, b: a * b"
    elif op == 'dividir':
        codigo = f"lambda a, b: a / b if b != 0 else 'Erro'"
    
    # Criar função dinamicamente
    globals()[op] = eval(codigo)

print(f"Soma dinâmica: {somar(10, 5)}")
print(f"Multiplicação dinâmica: {multiplicar(4, 3)}")
print(f"Divisão dinâmica: {dividir(10, 2)}")

# 2. Factory de funções
def criar_validador(tipo):
    validadores = {
        'email': lambda x: '@' in x and '.' in x,
        'telefone': lambda x: len(x) >= 10 and x.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').isdigit(),
        'cpf': lambda x: len(x.replace('.', '').replace('-', '')) == 11,
        'idade': lambda x: 0 <= int(x) <= 120 if x.isdigit() else False
    }
    return validadores.get(tipo, lambda x: True)

# Criando validadores dinamicamente
validar_email = criar_validador('email')
validar_telefone = criar_validador('telefone')

print(f"\\nEmail válido? {validar_email('user@email.com')}")
print(f"Telefone válido? {validar_telefone('(11) 99999-9999')}")

# 3. Gerador de funções matemáticas
def criar_operacao_matematica(simbolo):
    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else float('inf'),
        '**': lambda a, b: a ** b,
        '%': lambda a, b: a % b if b != 0 else 0
    }
    return operacoes.get(simbolo, lambda a, b: 0)

# Calculadora dinâmica
calc_soma = criar_operacao_matematica('+')
calc_potencia = criar_operacao_matematica('**')

print(f"\\nCalculadora dinâmica:")
print(f"15 + 25 = {calc_soma(15, 25)}")
print(f"2 ** 10 = {calc_potencia(2, 10)}")''',
                'explicacao': 'Python permite criar funções dinamicamente durante a execução'
            }
        ]
        
        for i, truque in enumerate(truques_ninja, 1):
            self.print_colored(f"\n{truque['titulo']}", "warning")
            self.exemplo(truque['codigo'])
            print(f"\n🥷 Executando truque ninja {i}:")
            self.executar_codigo(truque['codigo'])
            self.print_colored(f"\n💡 {truque['explicacao']}", "info")
            
            if i < len(truques_ninja):
                input("\n🔸 Pressione ENTER para o próximo truque...")
        
        # === CURIOSIDADES FINAIS ===
        self.print_colored("\n🎊 CURIOSIDADES FINAIS:", "success")
        curiosidades_finais = [
            "🐍 Python tem mais de 60 funções built-in que funcionam como ordem superior",
            "⚡ Lambda foi inspirada no cálculo lambda de Alonzo Church (1930s)",
            "🧠 Closures existem desde as primeiras linguagens funcionais como LISP",
            "🚀 Google MapReduce foi baseado nos conceitos de map() e reduce()",
            "🎯 JavaScript copiou muitos conceitos de Python para funções",
            "💎 Ruby tem blocos que são como lambdas super poderosos"
        ]
        
        for curiosidade in curiosidades_finais:
            self.print_colored(f"• {curiosidade}", "primary")
        
        self.print_success("\n🎉 Agora você conhece os segredos dos ninjas Python!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        if self.ui:
            self.ui.clear_screen()
        
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
                'title': 'Quiz: Conhecimentos sobre Funções Avançadas',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'O que significa *args em uma função?',
                        'answer': ['argumentos posicionais variáveis', 'argumentos variáveis', '*args'],
                        'hint': 'Permite que a função receba qualquer quantidade de argumentos posicionais'
                    },
                    {
                        'question': 'Como criar uma função lambda que soma dois números?',
                        'answer': ['lambda a, b: a + b', 'lambda x, y: x + y'],
                        'hint': 'Lambda seguido pelos parâmetros, dois pontos e a expressão'
                    },
                    {
                        'question': 'Qual função aplica uma operação a todos os elementos de uma lista?',
                        'answer': ['map', 'map()'],
                        'hint': 'Esta função "mapeia" uma operação para cada elemento'
                    },
                    {
                        'question': 'Qual função filtra elementos de uma lista baseado em uma condição?',
                        'answer': ['filter', 'filter()'],
                        'hint': 'Esta função cria um "filtro" que deixa passar apenas alguns elementos'
                    },
                    {
                        'question': 'O que **kwargs representa em uma função?',
                        'answer': ['argumentos nomeados variáveis', 'keyword arguments', '**kwargs'],
                        'hint': 'Permite receber argumentos com nome (chave=valor) de forma flexível'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a função para usar *args para somar qualquer quantidade de números',
                        'starter': '''def somar_todos(*____):
    return sum(____)

print(somar_todos(1, 2, 3, 4, 5))''',
                        'solution': 'numeros',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o lambda para filtrar números pares',
                        'starter': '''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 __ 0, numeros))
print(pares)''',
                        'solution': '==',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a função que aceita **kwargs para criar um perfil flexível',
                        'starter': '''def criar_perfil(nome, **____):
    print(f"Nome: {nome}")
    for chave, valor in ____.items():
        print(f"{chave}: {valor}")

criar_perfil("Ana", idade=25, cidade="SP")''',
                        'solution': 'info',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Processamento de Dados',
                'type': 'creative',
                'instruction': '''🎨 PROJETO CRIATIVO: Crie um sistema de processamento de dados personalizado!

Usando funções avançadas, crie um sistema que processe uma lista de vendas:

Dados de exemplo:
vendas = [
    {"produto": "Notebook", "preco": 2500, "categoria": "tech"},
    {"produto": "Livro", "preco": 45, "categoria": "educacao"},
    {"produto": "Mouse", "preco": 80, "categoria": "tech"}
]

Crie funções que usem:
1. 🔧 **lambda** para transformar dados
2. 📊 **map()** para aplicar operações
3. 🔍 **filter()** para filtrar resultados
4. ⚙️ ***args/** **kwargs** para flexibilidade

Ideias criativas:
• Sistema de desconto por categoria
• Calculadora de impostos personalizável
• Relatório de vendas formatado
• Filtros combinados por múltiplos critérios
• Qualquer coisa que sua imaginação criar!

Seja criativo e use pelo menos 3 conceitos que aprendeu!'''
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            # Limpa tela antes do menu
            if self.ui:
                self.ui.clear_screen()
            
            self.print_section("MENU DE EXERCÍCIOS", "📚", "accent")
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("\n" + "─" * 40)
            print("0. 🎯 Continuar para o Mini Projeto")
            print("─" * 40)
            
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre funções avançadas",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um sistema de processamento de dados",
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
    
    def _mini_projeto_analisador_inteligente(self) -> None:
        """Mini Projeto - Módulo 13: Analisador Inteligente de Dados"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: ANALISADOR INTELIGENTE DE DADOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: ANALISADOR INTELIGENTE DE DADOS")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um analisador de dados super inteligente usando todas as funções avançadas!")
        
        self.print_concept(
            "Analisador Inteligente",
            "Um sistema completo que usa *args, **kwargs, lambda, map, filter e reduce para analisar qualquer tipo de dados de forma flexível"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "📊 Business Intelligence - análise de vendas e métricas",
            "🎯 Marketing - segmentação de clientes e campanhas",
            "💰 Finanças - análise de investimentos e riscos",
            "🏥 Saúde - processamento de dados médicos",
            "🎮 Gaming - análise de comportamento de jogadores"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Configuração inicial
        self.print_section("PASSO 1: Configurando o Sistema", "📝", "info")
        self.print_tip("Vamos criar um analisador que se adapta a qualquer tipo de dados")
        
        try:
            tipo_analise = input("🔍 Que tipo de dados vamos analisar? (vendas/usuarios/produtos): ").strip().lower()
            if not tipo_analise:
                tipo_analise = "vendas"
            
            print(f"\n🎉 Perfeito! Vamos criar um analisador de {tipo_analise}!")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Implementação
        self.print_section("PASSO 2: Implementando o Sistema", "⚙️", "success")
        self.print_colored("Agora vamos criar o analisador inteligente:", "text")
        
        # PASSO 3: Demonstração
        self.print_section("PASSO 3: Sistema em Funcionamento", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está seu Analisador Inteligente completo:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: ANALISADOR INTELIGENTE DE DADOS
# Módulo 13: Funções Avançadas
# Especializado em: {tipo_analise}

from functools import reduce
from collections import defaultdict
import statistics
from datetime import datetime

class AnalisadorInteligente:
    def __init__(self, tipo_dados="{tipo_analise}"):
        self.tipo_dados = tipo_dados
        self.transformacoes = {{}}  # Funções de transformação personalizadas
        self.filtros = {{}}         # Filtros personalizados
        self.historico = []         # Histórico de análises
        
        # Configurações padrão por tipo
        self.configs_padrao = {{
            "vendas": {{"moeda": "R$", "formato_data": "%d/%m/%Y"}},
            "usuarios": {{"formato_nome": "title", "anonimizar": False}},
            "produtos": {{"mostrar_estoque": True, "categoria_padrao": "Geral"}}
        }}
    
    def registrar_transformacao(self, nome, funcao_lambda):
        """Registra uma transformação usando lambda"""
        self.transformacoes[nome] = funcao_lambda
        print(f"✅ Transformação '{nome}' registrada")
    
    def registrar_filtro(self, nome, funcao_lambda):
        """Registra um filtro usando lambda"""
        self.filtros[nome] = funcao_lambda
        print(f"✅ Filtro '{nome}' registrado")
    
    def processar_dados(self, dados, *operacoes, **configuracoes):
        """Processa dados usando *args para operações e **kwargs para config"""
        
        # Mescla configurações padrão com as fornecidas
        config = self.configs_padrao.get(self.tipo_dados, {{}})
        config.update(configuracoes)
        
        if config.get("debug", False):
            print(f"🔧 Processando {{len(dados)}} itens com config: {{config}}")
        
        resultado = dados.copy()
        
        # Aplica operações em sequência usando *args
        for operacao in operacoes:
            if operacao in self.transformacoes:
                # Aplica transformação usando map
                resultado = list(map(self.transformacoes[operacao], resultado))
                print(f"✅ Aplicada transformação: {{operacao}}")
            elif operacao in self.filtros:
                # Aplica filtro usando filter
                resultado = list(filter(self.filtros[operacao], resultado))
                print(f"✅ Aplicado filtro: {{operacao}}")
            else:
                print(f"⚠️ Operação '{{operacao}}' não encontrada")
        
        # Registra no histórico
        self.historico.append({{
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "operacoes": operacoes,
            "config": config,
            "itens_processados": len(resultado)
        }})
        
        return resultado
    
    def analisar_vendas(self, vendas, **opcoes):
        """Análise específica para vendas usando lambdas e funções avançadas"""
        
        print("\\n📊 ANÁLISE AVANÇADA DE VENDAS")
        print("="*40)
        
        # Estatísticas básicas usando reduce e lambda
        total_vendas = reduce(lambda acc, venda: acc + venda["valor"], vendas, 0)
        maior_venda = reduce(lambda max_v, venda: max_v if max_v["valor"] > venda["valor"] else venda, vendas)
        menor_venda = reduce(lambda min_v, venda: min_v if min_v["valor"] < venda["valor"] else venda, vendas)
        
        # Análise por categoria usando filter e map
        categorias = set(map(lambda v: v["categoria"], vendas))
        analise_categoria = {{}}
        
        for categoria in categorias:
            vendas_categoria = list(filter(lambda v: v["categoria"] == categoria, vendas))
            total_categoria = sum(map(lambda v: v["valor"], vendas_categoria))
            analise_categoria[categoria] = {{
                "quantidade": len(vendas_categoria),
                "total": total_categoria,
                "media": total_categoria / len(vendas_categoria) if vendas_categoria else 0
            }}
        
        # Aplicar filtros personalizados se especificados
        if opcoes.get("filtrar_grandes", False):
            limite = opcoes.get("limite_grande", 1000)
            vendas_grandes = list(filter(lambda v: v["valor"] > limite, vendas))
            print(f"\\n🔥 VENDAS GRANDES (>R$ {{limite}}): {{len(vendas_grandes)}}")
        
        # Top vendedores usando sorted + lambda
        vendas_por_vendedor = defaultdict(float)
        for venda in vendas:
            vendas_por_vendedor[venda["vendedor"]] += venda["valor"]
        
        top_vendedores = sorted(vendas_por_vendedor.items(), 
                               key=lambda x: x[1], reverse=True)[:3]
        
        # Imprimir resultados
        print(f"💰 Total de vendas: R$ {{total_vendas:,.2f}}")
        print(f"📊 Quantidade de vendas: {{len(vendas)}}")
        print(f"📈 Maior venda: {{maior_venda['produto']}} - R$ {{maior_venda['valor']:,.2f}}")
        print(f"📉 Menor venda: {{menor_venda['produto']}} - R$ {{menor_venda['valor']:,.2f}}")
        
        print(f"\\n🎯 ANÁLISE POR CATEGORIA:")
        for cat, dados in analise_categoria.items():
            print(f"  {{cat}}: {{dados['quantidade']}} vendas, R$ {{dados['total']:,.2f}} (média: R$ {{dados['media']:,.2f}})")
        
        print(f"\\n🏆 TOP 3 VENDEDORES:")
        for i, (vendedor, total) in enumerate(top_vendedores, 1):
            print(f"  {{i}}. {{vendedor}}: R$ {{total:,.2f}}")
        
        return {{
            "total": total_vendas,
            "quantidade": len(vendas),
            "categorias": analise_categoria,
            "top_vendedores": top_vendedores
        }}
    
    def pipeline_analise(self, dados, *steps, **config):
        """Pipeline flexível de análise usando *args e **kwargs"""
        
        resultado = dados
        
        print(f"\\n🔄 EXECUTANDO PIPELINE DE ANÁLISE")
        print(f"📋 Steps: {{', '.join(steps)}}")
        print(f"⚙️ Config: {{config}}")
        
        for step in steps:
            if step == "limpar":
                # Remove itens inválidos usando filter
                antes = len(resultado)
                resultado = list(filter(lambda item: all(v is not None for v in item.values()), resultado))
                print(f"  🧹 Limpeza: {{antes}} → {{len(resultado)}} itens")
                
            elif step == "normalizar":
                # Normaliza valores usando map
                if "campo_normalizar" in config:
                    campo = config["campo_normalizar"]
                    valores = [item[campo] for item in resultado if campo in item]
                    if valores:
                        max_val = max(valores)
                        resultado = list(map(
                            lambda item: {{**item, f"{{campo}}_norm": item.get(campo, 0) / max_val}}
                            if campo in item else item,
                            resultado
                        ))
                        print(f"  📊 Normalização aplicada ao campo '{{campo}}'")
                
            elif step == "agrupar":
                # Agrupa por campo usando reduce
                if "campo_grupo" in config:
                    campo = config["campo_grupo"]
                    grupos = defaultdict(list)
                    for item in resultado:
                        grupos[item.get(campo, "Outros")].append(item)
                    resultado = dict(grupos)
                    print(f"  📁 Agrupamento por '{{campo}}': {{len(resultado)}} grupos")
                    
            elif step == "ordenar":
                # Ordena usando sorted + lambda
                if "campo_ordem" in config:
                    campo = config["campo_ordem"]
                    reverso = config.get("decrescente", False)
                    resultado = sorted(resultado, 
                                     key=lambda item: item.get(campo, 0), 
                                     reverse=reverso)
                    print(f"  🔄 Ordenação por '{{campo}}' ({'decrescente' if reverso else 'crescente'})")
        
        return resultado
    
    def relatorio_inteligente(self, dados, **opcoes):
        """Gera relatório inteligente adaptável"""
        
        print(f"\\n📋 RELATÓRIO INTELIGENTE - {{self.tipo_dados.upper()}}")
        print("="*50)
        
        # Estatísticas automáticas baseadas no tipo de dados
        if self.tipo_dados == "vendas":
            self.analisar_vendas(dados, **opcoes)
        
        # Insights automáticos usando lambdas
        print(f"\\n💡 INSIGHTS AUTOMÁTICOS:")
        
        # Padrões temporais se houver datas
        if dados and "data" in dados[0]:
            datas = list(map(lambda item: item["data"], dados))
            print(f"  📅 Período analisado: {{min(datas)}} até {{max(datas)}}")
        
        # Distribuição de valores se houver valores numéricos
        if dados and "valor" in dados[0]:
            valores = list(map(lambda item: item["valor"], dados))
            if len(valores) > 1:
                media = statistics.mean(valores)
                mediana = statistics.median(valores)
                desvio = statistics.stdev(valores)
                
                print(f"  📊 Média: R$ {{media:,.2f}}")
                print(f"  📊 Mediana: R$ {{mediana:,.2f}}")
                print(f"  📊 Desvio Padrão: R$ {{desvio:,.2f}}")
                
                # Análise de outliers usando lambda
                limite_superior = media + 2 * desvio
                outliers = list(filter(lambda item: item["valor"] > limite_superior, dados))
                if outliers:
                    print(f"  🎯 Outliers detectados: {{len(outliers)}} vendas acima de R$ {{limite_superior:,.2f}}")

# DEMONSTRAÇÃO COMPLETA
print("🧠 DEMONSTRAÇÃO: ANALISADOR INTELIGENTE")
print("="*50)

# Criar analisador
analisador = AnalisadorInteligente("{tipo_analise}")

# Dados de exemplo para {tipo_analise}
if "{tipo_analise}" == "vendas":
    dados_exemplo = [
        {{"produto": "Notebook", "valor": 2500, "categoria": "Eletrônicos", "vendedor": "Ana", "data": "15/01/2024"}},
        {{"produto": "Mouse", "valor": 45, "categoria": "Eletrônicos", "vendedor": "Bruno", "data": "15/01/2024"}},
        {{"produto": "Livro Python", "valor": 80, "categoria": "Educação", "vendedor": "Ana", "data": "16/01/2024"}},
        {{"produto": "Mesa", "valor": 300, "categoria": "Móveis", "vendedor": "Carla", "data": "16/01/2024"}},
        {{"produto": "Smartphone", "valor": 1200, "categoria": "Eletrônicos", "vendedor": "Bruno", "data": "17/01/2024"}},
        {{"produto": "Cadeira", "valor": 200, "categoria": "Móveis", "vendedor": "Ana", "data": "17/01/2024"}}
    ]
else:
    dados_exemplo = [
        {{"nome": "João", "idade": 25, "categoria": "Premium", "valor": 1000}},
        {{"nome": "Maria", "idade": 30, "categoria": "Basic", "valor": 500}},
        {{"nome": "Pedro", "idade": 35, "categoria": "Premium", "valor": 1500}}
    ]

print(f"\\n📊 DADOS DE EXEMPLO ({{len(dados_exemplo)}} itens):")
for item in dados_exemplo[:3]:
    print(f"  {{item}}")
if len(dados_exemplo) > 3:
    print("  ...")

# 1. REGISTRAR TRANSFORMAÇÕES E FILTROS
print("\\n⚙️ REGISTRANDO OPERAÇÕES PERSONALIZADAS:")

# Transformações usando lambda
analisador.registrar_transformacao("aplicar_desconto_10", 
    lambda item: {{**item, "valor": item["valor"] * 0.9}})

analisador.registrar_transformacao("formatar_nome", 
    lambda item: {{**item, "produto": item.get("produto", item.get("nome", "")).title()}})

# Filtros usando lambda
analisador.registrar_filtro("apenas_caros", 
    lambda item: item["valor"] > 500)

analisador.registrar_filtro("categoria_eletrônicos", 
    lambda item: item.get("categoria", "").lower() == "eletrônicos")

# 2. PROCESSAMENTO COM OPERAÇÕES
print("\\n🔄 PROCESSAMENTO COM OPERAÇÕES:")
dados_processados = analisador.processar_dados(
    dados_exemplo,
    "formatar_nome",
    "apenas_caros",
    debug=True,
    log_operacoes=True
)

print(f"Itens após processamento: {{len(dados_processados)}}")

# 3. ANÁLISE PRINCIPAL
analisador.relatorio_inteligente(dados_exemplo, 
                                filtrar_grandes=True, 
                                limite_grande=800)

# 4. PIPELINE AVANÇADO
print("\\n🔧 PIPELINE AVANÇADO:")
resultado_pipeline = analisador.pipeline_analise(
    dados_exemplo,
    "limpar", "normalizar", "ordenar",
    campo_normalizar="valor",
    campo_ordem="valor",
    decrescente=True
)

# 5. HISTÓRICO DE OPERAÇÕES
print(f"\\n📝 HISTÓRICO DE ANÁLISES ({{len(analisador.historico)}}):")
for i, operacao in enumerate(analisador.historico, 1):
    print(f"  {{i}}. {{operacao['timestamp']}} - {{operacao['itens_processados']}} itens processados")

print("\\n🎉 Analisador Inteligente funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • *args e **kwargs para máxima flexibilidade")
print("  • Lambda functions para transformações rápidas")
print("  • map(), filter(), reduce() para processamento eficiente")
print("  • Closures para manter estado de configurações")
print("  • Programação funcional para código elegante")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success(f"🎉 PARABÉNS! Você criou um analisador inteligente de {tipo_analise}!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🧠 Machine Learning - usar para preprocessamento de dados",
            "📊 Business Intelligence - dashboards e relatórios automáticos", 
            "🌐 APIs REST - endpoints de análise flexíveis",
            "⚡ Real-time Analytics - processamento de streams de dados",
            "🤖 AutoML - pipelines de dados para modelos automáticos",
            "📱 Mobile Analytics - análise de comportamento de usuários"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre das Funções Avançadas!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Analisador Inteligente de Dados")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo13FuncoesAvancadas()
    print("Teste do módulo 13 - versão refatorada")
    module.execute()