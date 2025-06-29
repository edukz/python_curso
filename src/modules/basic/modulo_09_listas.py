#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 9: Listas
Aprenda sobre listas, coleções de dados organizadas
"""

from ..shared.base_module import BaseModule


class Modulo09Listas(BaseModule):
    """Módulo 9: Dominando Listas e Coleções"""
    
    def __init__(self):
        super().__init__("modulo_9", "Listas e Coleções")
        self.has_mini_project = True
        self.mini_project_points = 65
    
    def execute(self) -> None:
        """Executa o módulo Listas e Coleções"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._listas_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _listas_interativo(self) -> None:
        """Conteúdo principal do módulo Listas e Coleções"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📋 MÓDULO 9: DOMINANDO LISTAS E COLEÇÕES")
        else:
            print("\n" + "="*50)
            print("📋 MÓDULO 9: DOMINANDO LISTAS E COLEÇÕES")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos descobrir o poder das listas para organizar dados como um profissional!")
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
            self._mini_projeto_organizador_musical()
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
                'id': 'secao_conceito_listas',
                'titulo': '🎯 O que são listas na programação?',
                'descricao': 'Entenda como organizar múltiplos dados',
                'funcao': self._secao_conceito_listas
            },
            {
                'id': 'secao_criacao_acesso',
                'titulo': '⚙️ Como criar e acessar listas?',
                'descricao': 'Domine a criação e manipulação básica',
                'funcao': self._secao_criacao_acesso
            },
            {
                'id': 'secao_metodos_essenciais',
                'titulo': '🔧 Métodos essenciais das listas',
                'descricao': 'Append, remove, insert e muito mais',
                'funcao': self._secao_metodos_essenciais
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Listas em ação - Exemplos práticos',
                'descricao': 'Veja listas resolvendo problemas reais',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 Onde usar listas na vida real?',
                'descricao': 'Aplicações práticas em sistemas',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas com listas',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Evite índices inválidos e outros problemas',
                'funcao': self._secao_erros_comuns
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
    
    def _secao_conceito_listas(self) -> None:
        """Seção: O que são listas na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO LISTAS NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Listas",
            "São coleções ordenadas que armazenam múltiplos itens em uma única variável, permitindo organização eficiente"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Imagine sua lista de compras - você pode adicionar, remover e verificar itens!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma prateleira de livros:", "text")
        self.print_colored("• Cada posição (índice) tem um livro específico", "text")
        self.print_colored("• Você pode adicionar novos livros no final", "text")
        self.print_colored("• Pode remover ou trocar livros de posição", "text")
        self.print_colored("• Cada livro tem uma posição numerada (0, 1, 2...)", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Criamos uma lista usando colchetes [] com itens separados por vírgula",
            "2. Cada item tem um índice (posição) que começa em 0",
            "3. Podemos acessar, modificar, adicionar e remover itens facilmente"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Comparação: sem lista vs com lista
print("❌ SEM LISTA (repetitivo):")
fruta1 = "maçã"
fruta2 = "banana" 
fruta3 = "laranja"
print(f"Tenho: {fruta1}, {fruta2}, {fruta3}")

print("\\n✅ COM LISTA (organizado):")
frutas = ["maçã", "banana", "laranja"]
print(f"Minha lista: {frutas}")
print(f"Primeira fruta: {frutas[0]}")
print(f"Total de frutas: {len(frutas)}")

# Fácil de adicionar mais!
frutas.append("uva")
print(f"Após adicionar: {frutas}")'''
        
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver a diferença:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "YouTube - Lista de vídeos da playlist",
            "Amazon - Carrinho de compras com produtos",
            "Spotify - Lista de músicas favoritas",
            "WhatsApp - Lista de contatos e mensagens"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_criacao_acesso(self) -> None:
        """Seção: Como criar e acessar listas?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO CRIAR E ACESSAR LISTAS?", "⚙️")
        
        # === CRIAÇÃO DE LISTAS ===
        self.print_concept(
            "Criação de Listas",
            "Use colchetes [] para criar listas com diferentes tipos de dados"
        )
        
        self.print_colored("\n🏗️ FORMAS DE CRIAR LISTAS:", "warning")
        tipos_criacao = [
            "• lista_vazia = [] → Lista vazia para adicionar depois",
            "• numeros = [1, 2, 3, 4, 5] → Lista de números",
            "• nomes = ['Ana', 'João', 'Maria'] → Lista de strings",
            "• mista = ['Python', 2024, True, 3.14] → Tipos diferentes"
        ]
        
        for tipo in tipos_criacao:
            self.print_colored(tipo, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO CRIAÇÃO ===
        self.print_colored("\n💻 EXEMPLO DE CRIAÇÃO:", "success")
        codigo_criacao = '''# Diferentes formas de criar listas
print("🔧 CRIANDO LISTAS:")

# Lista vazia
carrinho = []
print(f"Carrinho vazio: {carrinho}")

# Lista de números
idades = [25, 30, 22, 28, 35]
print(f"Idades: {idades}")

# Lista de strings
cores = ["azul", "verde", "vermelho", "amarelo"]
print(f"Cores: {cores}")

# Lista mista (diferentes tipos)
perfil = ["João", 28, True, 1.80, "São Paulo"]
print(f"Perfil: {perfil}")

# Usando range para criar lista
numeros = list(range(1, 6))
print(f"Números de 1 a 5: {numeros}")'''
        
        self.exemplo(codigo_criacao)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_criacao)
        
        input("\n🔸 Pressione ENTER para aprender sobre acesso...")
        
        # === ACESSO A ELEMENTOS ===
        self.print_colored("\n🎯 ACESSANDO ELEMENTOS:", "info")
        self.print_colored("Cada elemento tem um índice (posição) que começa em 0:", "text")
        
        codigo_acesso = '''# Acessando elementos da lista
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print(f"Lista completa: {frutas}")
print()

# Índices positivos (do início)
print("📍 ÍNDICES POSITIVOS:")
print(f"Posição 0 (primeira): {frutas[0]}")
print(f"Posição 1 (segunda): {frutas[1]}")
print(f"Posição 2 (terceira): {frutas[2]}")

# Índices negativos (do final)
print("\\n📍 ÍNDICES NEGATIVOS:")
print(f"Posição -1 (última): {frutas[-1]}")
print(f"Posição -2 (penúltima): {frutas[-2]}")

# Fatias (slicing)
print("\\n✂️ FATIAS (SLICING):")
print(f"Primeiras 3: {frutas[:3]}")
print(f"Últimas 2: {frutas[-2:]}")
print(f"Do meio: {frutas[1:4]}")'''
        
        self.exemplo(codigo_acesso)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_acesso)
        
        self.print_tip("Índices negativos contam do final: -1 é o último, -2 é o penúltimo!")
        
        self.pausar()
    
    def _secao_metodos_essenciais(self) -> None:
        """Seção: Métodos essenciais das listas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MÉTODOS ESSENCIAIS DAS LISTAS", "🔧")
        
        # === MÉTODOS DE ADIÇÃO ===
        self.print_colored("\n➕ MÉTODOS PARA ADICIONAR:", "warning")
        
        codigo_adicao = '''# Métodos para adicionar elementos
carrinho = ["notebook", "mouse"]
print(f"Carrinho inicial: {carrinho}")

# append() - adiciona no final
carrinho.append("teclado")
print(f"Após append: {carrinho}")

# insert() - adiciona em posição específica
carrinho.insert(1, "monitor")  # posição 1
print(f"Após insert: {carrinho}")

# extend() - adiciona múltiplos itens
novos_itens = ["cabo USB", "mousepad"]
carrinho.extend(novos_itens)
print(f"Após extend: {carrinho}")'''
        
        self.exemplo(codigo_adicao)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_adicao)
        
        input("\n🔸 Pressione ENTER para métodos de remoção...")
        
        # === MÉTODOS DE REMOÇÃO ===
        self.print_colored("\n➖ MÉTODOS PARA REMOVER:", "warning")
        
        codigo_remocao = '''# Métodos para remover elementos
lista = ["a", "b", "c", "d", "e"]
print(f"Lista inicial: {lista}")

# remove() - remove por valor (primeira ocorrência)
lista.remove("c")
print(f"Após remove('c'): {lista}")

# pop() - remove e retorna por índice
item_removido = lista.pop(1)  # remove posição 1
print(f"Item removido: {item_removido}")
print(f"Após pop(1): {lista}")

# pop() sem índice remove o último
ultimo = lista.pop()
print(f"Último removido: {ultimo}")
print(f"Lista final: {lista}")

# clear() - remove todos os elementos
lista.clear()
print(f"Após clear(): {lista}")'''
        
        self.exemplo(codigo_remocao)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_remocao)
        
        input("\n🔸 Pressione ENTER para outros métodos úteis...")
        
        # === OUTROS MÉTODOS ÚTEIS ===
        self.print_colored("\n🛠️ OUTROS MÉTODOS ÚTEIS:", "warning")
        
        codigo_outros = '''# Outros métodos importantes
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original: {numeros}")

# len() - tamanho da lista
tamanho = len(numeros)
print(f"Tamanho: {tamanho}")

# count() - conta ocorrências
contador = numeros.count(1)
print(f"Número 1 aparece {contador} vezes")

# index() - encontra posição do valor
posicao = numeros.index(4)
print(f"Número 4 está na posição: {posicao}")

# sort() - ordena a lista
numeros.sort()
print(f"Ordenado crescente: {numeros}")

# reverse() - inverte a ordem
numeros.reverse()
print(f"Invertido: {numeros}")

# in - verifica se item existe
existe = 5 in numeros
print(f"5 está na lista? {existe}")'''
        
        self.exemplo(codigo_outros)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_outros)
        
        # === RESUMO VISUAL ===
        self.print_colored("\n📋 RESUMO DOS MÉTODOS:", "info")
        metodos = [
            "append(item) → Adiciona no final",
            "insert(pos, item) → Adiciona em posição específica", 
            "remove(item) → Remove primeira ocorrência",
            "pop(index) → Remove e retorna item",
            "clear() → Remove todos os elementos",
            "sort() → Ordena a lista",
            "reverse() → Inverte a ordem",
            "count(item) → Conta ocorrências",
            "index(item) → Encontra posição"
        ]
        
        for metodo in metodos:
            self.print_colored(f"• {metodo}", "text")
        
        self.pausar()
    
    def _secao_exemplos_praticos(self) -> None:
        """Seção: Listas em ação - Exemplos práticos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("LISTAS EM AÇÃO - EXEMPLOS PRÁTICOS", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Sistema de Notas Escolares',
                'descricao': 'Lista para gerenciar notas e calcular estatísticas',
                'codigo': '''# Sistema de notas escolares
print("📚 SISTEMA DE NOTAS")
print("=" * 30)

# Lista de notas
notas = [8.5, 7.2, 9.0, 6.8, 8.9, 7.5, 9.2, 8.1]
print(f"Notas: {notas}")

# Estatísticas básicas
total_notas = len(notas)
soma_notas = sum(notas)
media = soma_notas / total_notas
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"\\n📊 ESTATÍSTICAS:")
print(f"Total de notas: {total_notas}")
print(f"Média: {media:.2f}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")

# Análise de aprovação
aprovados = [nota for nota in notas if nota >= 7.0]
reprovados = [nota for nota in notas if nota < 7.0]

print(f"\\n✅ Aprovados: {len(aprovados)} ({len(aprovados)/total_notas*100:.1f}%)")
print(f"❌ Reprovados: {len(reprovados)} ({len(reprovados)/total_notas*100:.1f}%)")''',
                'explicacao': 'Demonstra uso de listas para cálculos estatísticos e análises'
            },
            {
                'titulo': 'EXEMPLO 2: Gerenciador de Tarefas',
                'descricao': 'Lista dinâmica para organizar e gerenciar tarefas',
                'codigo': '''# Gerenciador de tarefas
print("✅ GERENCIADOR DE TAREFAS")
print("=" * 35)

# Lista de tarefas
tarefas = [
    {"titulo": "Estudar Python", "concluida": False, "prioridade": "alta"},
    {"titulo": "Fazer exercícios", "concluida": True, "prioridade": "média"},
    {"titulo": "Projeto final", "concluida": False, "prioridade": "alta"},
    {"titulo": "Revisar código", "concluida": False, "prioridade": "baixa"}
]

def exibir_tarefas(lista_tarefas):
    """Exibe todas as tarefas formatadas"""
    for i, tarefa in enumerate(lista_tarefas, 1):
        status = "✅" if tarefa["concluida"] else "⏳"
        prioridade = tarefa["prioridade"].upper()
        print(f"{i}. {status} {tarefa['titulo']} [{prioridade}]")

def marcar_concluida(lista_tarefas, indice):
    """Marca uma tarefa como concluída"""
    if 0 <= indice < len(lista_tarefas):
        lista_tarefas[indice]["concluida"] = True
        print(f"✅ Tarefa '{lista_tarefas[indice]['titulo']}' concluída!")

# Demonstração
print("📋 LISTA ATUAL:")
exibir_tarefas(tarefas)

print("\\n🔄 Marcando tarefa 1 como concluída...")
marcar_concluida(tarefas, 0)

print("\\n📋 LISTA ATUALIZADA:")
exibir_tarefas(tarefas)

# Estatísticas
total = len(tarefas)
concluidas = sum(1 for t in tarefas if t["concluida"])
pendentes = total - concluidas

print(f"\\n📊 PROGRESSO:")
print(f"Total: {total} | Concluídas: {concluidas} | Pendentes: {pendentes}")
print(f"Porcentagem: {concluidas/total*100:.1f}% completo")''',
                'explicacao': 'Mostra listas com dicionários para estruturas de dados complexas'
            },
            {
                'titulo': 'EXEMPLO 3: Filtro e Ordenação de Dados',
                'descricao': 'Técnicas avançadas de manipulação de listas',
                'codigo': '''# Filtro e ordenação de dados
print("🔍 FILTRO E ORDENAÇÃO")
print("=" * 30)

# Lista de produtos
produtos = [
    {"nome": "Notebook", "preco": 2500.00, "categoria": "eletrônicos"},
    {"nome": "Livro Python", "preco": 89.90, "categoria": "livros"},
    {"nome": "Mouse", "preco": 45.00, "categoria": "eletrônicos"},
    {"nome": "Cadeira", "preco": 350.00, "categoria": "móveis"},
    {"nome": "Monitor", "preco": 800.00, "categoria": "eletrônicos"}
]

print("📦 PRODUTOS ORIGINAIS:")
for produto in produtos:
    print(f"• {produto['nome']}: R$ {produto['preco']:.2f}")

# Filtrar eletrônicos
eletronicos = [p for p in produtos if p["categoria"] == "eletrônicos"]
print(f"\\n💻 ELETRÔNICOS ({len(eletronicos)} itens):")
for produto in eletronicos:
    print(f"• {produto['nome']}: R$ {produto['preco']:.2f}")

# Filtrar por preço
baratos = [p for p in produtos if p["preco"] < 100]
print(f"\\n💰 PRODUTOS BARATOS ({len(baratos)} itens):")
for produto in baratos:
    print(f"• {produto['nome']}: R$ {produto['preco']:.2f}")

# Ordenar por preço
produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
print(f"\\n📈 ORDENADOS POR PREÇO:")
for produto in produtos_ordenados:
    print(f"• {produto['nome']}: R$ {produto['preco']:.2f}")

# Preço médio
preco_medio = sum(p["preco"] for p in produtos) / len(produtos)
print(f"\\n📊 PREÇO MÉDIO: R$ {preco_medio:.2f}")''',
                'explicacao': 'Demonstra list comprehensions, filtros e ordenação avançada'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            if exemplo['explicacao']:
                self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você viu listas resolvendo problemas reais!")
        self.pausar()
    
    def _secao_casos_uso(self) -> None:
        """Seção: Onde usar listas na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR LISTAS NA VIDA REAL?", "🌍")
        
        casos_uso = [
            {
                'titulo': '🛒 E-COMMERCE E VENDAS',
                'descricao': 'Carrinho de compras e gestão de produtos',
                'exemplo': '''# Sistema de carrinho de compras
print("🛒 SISTEMA DE E-COMMERCE")
print("=" * 30)

class CarrinhoCompras:
    def __init__(self):
        self.itens = []
        self.total = 0.0
    
    def adicionar_item(self, produto, preco, quantidade=1):
        item = {
            'produto': produto,
            'preco': preco,
            'quantidade': quantidade,
            'subtotal': preco * quantidade
        }
        self.itens.append(item)
        self.total += item['subtotal']
        print(f"✅ {produto} adicionado ao carrinho")
    
    def remover_item(self, produto):
        for item in self.itens:
            if item['produto'] == produto:
                self.total -= item['subtotal']
                self.itens.remove(item)
                print(f"❌ {produto} removido do carrinho")
                return
        print(f"⚠️ {produto} não encontrado no carrinho")
    
    def exibir_carrinho(self):
        if not self.itens:
            print("🛒 Carrinho vazio")
            return
        
        print("\\n🛒 ITENS NO CARRINHO:")
        print("-" * 50)
        for item in self.itens:
            print(f"{item['produto']:20} "
                  f"R$ {item['preco']:6.2f} x{item['quantidade']} = "
                  f"R$ {item['subtotal']:7.2f}")
        print("-" * 50)
        print(f"{'TOTAL:':32} R$ {self.total:7.2f}")

# Demonstração
carrinho = CarrinhoCompras()

# Adicionando produtos
carrinho.adicionar_item("Smartphone", 899.90, 1)
carrinho.adicionar_item("Capinha", 29.90, 2)
carrinho.adicionar_item("Carregador", 45.00, 1)

carrinho.exibir_carrinho()

# Aplicando desconto
if carrinho.total > 500:
    desconto = carrinho.total * 0.1
    print(f"\\n🎁 DESCONTO (10%): -R$ {desconto:.2f}")
    print(f"💰 TOTAL FINAL: R$ {carrinho.total - desconto:.2f}")'''
            },
            {
                'titulo': '📊 ANÁLISE DE DADOS',
                'descricao': 'Processamento e análise de grandes conjuntos de dados',
                'exemplo': '''# Análise de dados de vendas
import random

print("📊 ANÁLISE DE DADOS DE VENDAS")
print("=" * 35)

# Simulando dados de vendas de 30 dias
vendas_diarias = [random.randint(800, 2500) for _ in range(30)]

print(f"📈 VENDAS DOS ÚLTIMOS 30 DIAS:")
print(f"Dados: {vendas_diarias[:10]}... (primeiros 10 dias)")

# Análises estatísticas
total_vendas = sum(vendas_diarias)
media_diaria = total_vendas / len(vendas_diarias)
melhor_dia = max(vendas_diarias)
pior_dia = min(vendas_diarias)

print(f"\\n📊 ESTATÍSTICAS:")
print(f"Total do mês: R$ {total_vendas:,}")
print(f"Média diária: R$ {media_diaria:.2f}")
print(f"Melhor dia: R$ {melhor_dia:,}")
print(f"Pior dia: R$ {pior_dia:,}")

# Tendências
dias_acima_media = [v for v in vendas_diarias if v > media_diaria]
print(f"\\n📈 PERFORMANCE:")
print(f"Dias acima da média: {len(dias_acima_media)}/{len(vendas_diarias)}")
print(f"Taxa de sucesso: {len(dias_acima_media)/len(vendas_diarias)*100:.1f}%")

# Metas
meta_diaria = 1500
dias_meta = [v for v in vendas_diarias if v >= meta_diaria]
print(f"\\n🎯 METAS:")
print(f"Meta diária: R$ {meta_diaria:,}")
print(f"Dias que bateram meta: {len(dias_meta)}")
print(f"Percentual de meta: {len(dias_meta)/len(vendas_diarias)*100:.1f}%")'''
            },
            {
                'titulo': '🎵 STREAMING E MÍDIA',
                'descricao': 'Playlists e recomendações de conteúdo',
                'exemplo': '''# Sistema de playlist musical
print("🎵 SISTEMA DE PLAYLIST")
print("=" * 25)

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
        self.posicao_atual = 0
    
    def adicionar_musica(self, titulo, artista, duracao):
        musica = {
            'titulo': titulo,
            'artista': artista,
            'duracao': duracao,
            'tocada': False
        }
        self.musicas.append(musica)
        print(f"🎵 '{titulo}' por {artista} adicionada")
    
    def tocar_proxima(self):
        if self.posicao_atual < len(self.musicas):
            musica = self.musicas[self.posicao_atual]
            musica['tocada'] = True
            print(f"▶️ Tocando: {musica['titulo']} - {musica['artista']}")
            self.posicao_atual += 1
        else:
            print("🔚 Fim da playlist")
    
    def shuffle(self):
        import random
        random.shuffle(self.musicas)
        self.posicao_atual = 0
        print("🔀 Playlist embaralhada!")
    
    def estatisticas(self):
        total = len(self.musicas)
        tocadas = sum(1 for m in self.musicas if m['tocada'])
        duracao_total = sum(m['duracao'] for m in self.musicas)
        
        print(f"\\n📊 ESTATÍSTICAS DA PLAYLIST:")
        print(f"Nome: {self.nome}")
        print(f"Total de músicas: {total}")
        print(f"Já tocadas: {tocadas}")
        print(f"Duração total: {duracao_total} minutos")

# Criando playlist
rock_classico = Playlist("Rock Clássico")

# Adicionando músicas
rock_classico.adicionar_musica("Bohemian Rhapsody", "Queen", 6)
rock_classico.adicionar_musica("Stairway to Heaven", "Led Zeppelin", 8)
rock_classico.adicionar_musica("Hotel California", "Eagles", 6)
rock_classico.adicionar_musica("Sweet Child O' Mine", "Guns N' Roses", 5)

# Tocando algumas músicas
print("\\n🎶 REPRODUZINDO:")
rock_classico.tocar_proxima()
rock_classico.tocar_proxima()

# Estatísticas
rock_classico.estatisticas()

# Shuffle
rock_classico.shuffle()'''
            }
        ]
        
        for i, caso in enumerate(casos_uso):
            self.print_colored(f"\n{caso['titulo']}", "warning")
            self.print_colored(f"📝 {caso['descricao']}", "text")
            
            self.print_code_section("EXEMPLO", caso['exemplo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(caso['exemplo'])
            
            if i < len(casos_uso) - 1:
                input("\n🔸 Pressione ENTER para o próximo caso...")
        
        self.print_success("\n🌟 Listas são fundamentais em praticamente todos os sistemas!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas com listas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS COM LISTAS", "⭐")
        
        praticas = [
            {
                'titulo': '🎯 Use nomes descritivos para listas',
                'ruim': '''# ❌ EVITE: Nomes genéricos
lista = ["João", "Maria", "Pedro"]
l = [1, 2, 3, 4, 5]
dados = ["produto1", 10, 29.90]''',
                'bom': '''# ✅ PREFIRA: Nomes que explicam o conteúdo
nomes_alunos = ["João", "Maria", "Pedro"]
idades = [1, 2, 3, 4, 5]  
info_produto = ["produto1", 10, 29.90]'''
            },
            {
                'titulo': '⚡ Prefira list comprehensions quando apropriado',
                'ruim': '''# ❌ EVITE: Loop desnecessário para operações simples
numeros = [1, 2, 3, 4, 5]
quadrados = []
for num in numeros:
    quadrados.append(num ** 2)''',
                'bom': '''# ✅ PREFIRA: List comprehension mais elegante
numeros = [1, 2, 3, 4, 5]
quadrados = [num ** 2 for num in numeros]
# Mais conciso e pythônico'''
            },
            {
                'titulo': '🔍 Verifique limites antes de acessar índices',
                'ruim': '''# ❌ PERIGO: Acesso sem verificação
lista = [1, 2, 3]
print(lista[5])  # IndexError!''',
                'bom': '''# ✅ SEGURO: Sempre verifique os limites
lista = [1, 2, 3]
indice = 5

if 0 <= indice < len(lista):
    print(lista[indice])
else:
    print("Índice fora do alcance")'''
            },
            {
                'titulo': '🚀 Use métodos apropriados para cada operação',
                'ruim': '''# ❌ EVITE: Métodos incorretos
lista = [1, 2, 3]
# Forma lenta de verificar existência
existe = False
for item in lista:
    if item == 2:
        existe = True
        break''',
                'bom': '''# ✅ PREFIRA: Operadores e métodos built-in
lista = [1, 2, 3]
# Forma rápida e clara
existe = 2 in lista
posicao = lista.index(2) if 2 in lista else -1'''
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{i}. {pratica['titulo']}", "warning")
            
            self.print_colored("\n❌ EVITE:", "error")
            self.exemplo(pratica['ruim'])
            
            self.print_colored("✅ PREFIRA:", "success")
            self.exemplo(pratica['bom'])
            
            if i < len(praticas):
                input("\n🔸 Pressione ENTER para a próxima prática...")
        
        self.print_tip("Listas bem utilizadas tornam seu código mais legível e eficiente!")
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ERROS COMUNS COM LISTAS", "⚠️")
        
        erros = [
            {
                'titulo': '📍 Erro de índice - IndexError',
                'erro': '''# ❌ ERRO: Acessar índice que não existe
frutas = ["maçã", "banana", "laranja"]
print(frutas[5])  # IndexError! Lista só tem 3 itens (0,1,2)''',
                'correto': '''# ✅ CORRETO: Verificar tamanho antes de acessar
frutas = ["maçã", "banana", "laranja"]

# Opção 1: Verificação manual
if len(frutas) > 5:
    print(frutas[5])
else:
    print("Índice fora do alcance")

# Opção 2: Try/except
try:
    print(frutas[5])
except IndexError:
    print("Índice não existe na lista")''',
                'dica': 'Sempre verifique se o índice está dentro dos limites da lista'
            },
            {
                'titulo': '🔄 Modificar lista durante iteração',
                'erro': '''# ❌ ERRO: Modificar lista enquanto itera
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Problema: modifica durante loop!''',
                'correto': '''# ✅ CORRETO: Criar nova lista ou iterar em cópia
numeros = [1, 2, 3, 4, 5]

# Opção 1: List comprehension
impares = [num for num in numeros if num % 2 != 0]

# Opção 2: Iterar em cópia
numeros_copia = numeros.copy()
for num in numeros_copia:
    if num % 2 == 0:
        numeros.remove(num)''',
                'dica': 'Nunca modifique uma lista enquanto está iterando sobre ela'
            },
            {
                'titulo': '🔍 Usar remove() sem verificar existência',
                'erro': '''# ❌ ERRO: Tentar remover item que não existe
lista = ["a", "b", "c"]
lista.remove("d")  # ValueError! "d" não existe''',
                'correto': '''# ✅ CORRETO: Verificar antes de remover
lista = ["a", "b", "c"]

# Opção 1: Verificação com 'in'
if "d" in lista:
    lista.remove("d")
else:
    print("Item não encontrado")

# Opção 2: Try/except
try:
    lista.remove("d")
except ValueError:
    print("Item não existe na lista")''',
                'dica': 'Sempre verifique se o item existe antes de tentar removê-lo'
            },
            {
                'titulo': '📝 Confundir append() com extend()',
                'erro': '''# ❌ ERRO: Usar append() para múltiplos itens
lista = [1, 2, 3]
lista.append([4, 5, 6])  # Adiciona UMA lista, não os itens
print(lista)  # [1, 2, 3, [4, 5, 6]] - lista aninhada!''',
                'correto': '''# ✅ CORRETO: Use extend() para múltiplos itens
lista = [1, 2, 3]

# Para adicionar múltiplos itens individuais
lista.extend([4, 5, 6])
print(lista)  # [1, 2, 3, 4, 5, 6]

# append() é para adicionar UM item (pode ser uma lista)
outra_lista = [1, 2, 3]
outra_lista.append(4)  # Adiciona o número 4
print(outra_lista)  # [1, 2, 3, 4]''',
                'dica': 'append() adiciona UM item, extend() adiciona MÚLTIPLOS itens'
            }
        ]
        
        for i, erro in enumerate(erros, 1):
            self.print_colored(f"\n{i}. {erro['titulo']}", "warning")
            
            self.print_colored("\n❌ CÓDIGO COM ERRO:", "error")
            self.exemplo(erro['erro'])
            
            self.print_colored("✅ CÓDIGO CORRETO:", "success")
            self.exemplo(erro['correto'])
            
            self.print_tip(erro['dica'])
            
            if i < len(erros):
                input("\n🔸 Pressione ENTER para o próximo erro...")
        
        self.print_success("\n🎯 Conhecendo os erros comuns, você os evitará!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre listas!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Listas',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Como você acessa o primeiro elemento de uma lista?',
                        'answer': ['lista[0]', '[0]', 'índice 0'],
                        'hint': 'Listas começam no índice 0!'
                    },
                    {
                        'question': 'Qual método adiciona um item no final da lista?',
                        'answer': ['append', 'append()'],
                        'hint': 'É o método mais comum para adicionar itens'
                    },
                    {
                        'question': 'Como você acessa o último elemento usando índice negativo?',
                        'answer': ['lista[-1]', '[-1]', '-1'],
                        'hint': 'Índices negativos contam do final'
                    },
                    {
                        'question': 'Qual função retorna o tamanho de uma lista?',
                        'answer': ['len', 'len()'],
                        'hint': 'É uma função built-in muito usada'
                    },
                    {
                        'question': 'Qual método remove um item por valor?',
                        'answer': ['remove', 'remove()'],
                        'hint': 'Remove a primeira ocorrência do valor'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete para adicionar "maçã" no final da lista',
                        'starter': '''frutas = ["banana", "laranja"]
frutas.___("maçã")
print(frutas)''',
                        'solution': 'append',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete para acessar o último elemento',
                        'starter': '''numeros = [10, 20, 30, 40, 50]
ultimo = numeros[___]
print(f"Último número: {ultimo}")''',
                        'solution': '-1',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete para remover item e obter o tamanho',
                        'starter': '''cores = ["azul", "verde", "vermelho", "amarelo"]
cores.___("verde")
tamanho = ___(cores)
print(f"Cores restantes: {cores}")
print(f"Total: {tamanho}")''',
                        'solution': 'remove\nlen',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Minha Lista Personalizada',
                'type': 'creative',
                'instruction': 'Crie uma lista com algo que você gosta (filmes, livros, jogos, etc.) e mostre operações interessantes!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre listas e seus métodos",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie sua própria lista temática",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto Organizador Musical",
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
        
        if percentage >= 80:
            self.print_success("🌟 Excelente! Você domina as listas!")
        elif percentage >= 60:
            self.print_success("👏 Muito bom! Continue praticando!")
        else:
            self.print_tip("💪 Continue estudando! Revise as seções teóricas.")
        
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código para Completar", ex['starter'])
            
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print(f"\n✍️ Complete com o método:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Perfeito! Resposta correta!")
                    # Mostrar código completo funcionando
                    codigo_completo = ex['starter'].replace('___', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'intermediate':
                print(f"\n✍️ Complete com o índice:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Correto! Índice perfeito!")
                    codigo_completo = ex['starter'].replace('___', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'advanced':
                print(f"\n✍️ Complete as duas partes (uma por linha):")
                print("Parte 1:")
                input1 = input(">>> ").strip()
                print("Parte 2:")
                input2 = input(">>> ").strip()
                
                solutions = ex['solution'].split('\n')
                correct = (input1.lower() == solutions[0].lower() and 
                          input2.lower() == solutions[1].lower())
                
                if correct:
                    self.print_success("✅ Excelente! Código avançado completo!")
                    codigo_completo = ex['starter'].replace('___', input1, 1).replace('___', input2, 1)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. As respostas eram: {solutions[0]} e {solutions[1]}")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de listas!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        
        print("\n💡 Exemplos de listas temáticas:")
        print("🎬 Lista de filmes favoritos")
        print("📚 Lista de livros para ler") 
        print("🎵 Lista de músicas favoritas")
        print("🍕 Lista de comidas preferidas")
        print("🏖️ Lista de lugares para visitar")
        
        print("\n🎯 Vamos criar sua lista personalizada:")
        
        tema = input("\n📝 Qual o tema da sua lista? (ex: filmes, livros, músicas): ").strip()
        
        if tema:
            print(f"\n🌟 Ótima escolha! Vamos criar uma lista de {tema}!")
            
            # Coletar itens
            itens = []
            print(f"\n📋 Digite itens para sua lista de {tema} (digite 'fim' para terminar):")
            
            while len(itens) < 5:  # Limite para não ser muito longo
                item = input(f"Item {len(itens) + 1}: ").strip()
                if item.lower() == 'fim':
                    break
                if item:
                    itens.append(item)
                    print(f"✅ '{item}' adicionado!")
            
            if itens:
                # Gerar código baseado na lista criada
                itens_str = str(itens)
                codigo_criativo = f'''# 🎨 MINHA LISTA PERSONALIZADA DE {tema.upper()}
print("📋 MINHA LISTA DE {tema.upper()}")
print("=" * 40)

# Lista criada por você
minha_lista = {itens_str}

print(f"📊 Total de itens: {{len(minha_lista)}}")
print()

# Exibindo todos os itens
print("📝 ITENS DA LISTA:")
for i, item in enumerate(minha_lista, 1):
    print(f"{{i}}. {{item}}")

# Operações interessantes
print(f"\\n⭐ Primeiro item: {{minha_lista[0]}}")
print(f"🏆 Último item: {{minha_lista[-1]}}")

# Adicionando um novo item
novo_item = "item especial"
minha_lista.append(novo_item)
print(f"\\n➕ Adicionado: {{novo_item}}")
print(f"📊 Nova lista: {{minha_lista}}")

# Verificando se existe um item
item_procurado = minha_lista[0]  # Primeiro item
if item_procurado in minha_lista:
    posicao = minha_lista.index(item_procurado)
    print(f"\\n🔍 '{{item_procurado}}' está na posição {{posicao}}")

print("\\n✨ Lista criada com sucesso!")'''
                
                print(f"\n🚀 Aqui está seu código personalizado para {tema}:")
                self.exemplo(codigo_criativo)
                
                print("\n🎬 Executando sua lista:")
                self.executar_codigo(codigo_criativo)
                
                print(f"\n🎉 Incrível! Você criou uma lista personalizada de {tema}!")
                self.print_success("🏆 Parabéns pela criatividade com listas!")
            else:
                print("\n🎨 Sem problemas! Listas podem começar vazias também!")
        else:
            print("\n💡 Próxima vez você pode criar sua lista temática!")
        
        self.pausar()
    
    def _mini_projeto_organizador_musical(self) -> None:
        """Mini Projeto - Módulo 9: Organizador Musical Inteligente"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: ORGANIZADOR MUSICAL INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: ORGANIZADOR MUSICAL INTELIGENTE")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema completo de organização musical usando listas!")
        
        self.print_concept(
            "Organizador Musical Inteligente",
            "Um sistema que gerencia playlists, artistas e estatísticas musicais usando o poder das listas"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Spotify - Organização de playlists e recomendações",
            "Apple Music - Biblioteca musical e estatísticas",
            "YouTube Music - Gerenciamento de favoritos",
            "Rádios Online - Programação e rotação musical"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Coleta de dados musicais
        self.print_section("PASSO 1: Configurando biblioteca musical", "📝", "info")
        self.print_tip("Vamos criar um sistema com múltiplas listas para diferentes aspectos musicais")
        
        try:
            print("\n🎵 Preparando biblioteca musical:")
            generos_disponiveis = ["Rock", "Pop", "Jazz", "Blues", "Eletrônica", "Clássica"]
            
            for genero in generos_disponiveis:
                print(f"  🎼 {genero}")
            
            input("\n🔸 Pressione ENTER para ver o sistema...")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Implementação do sistema
        self.print_section("PASSO 2: Construindo o organizador", "⚙️", "success")
        self.print_colored("Agora vamos criar um sistema completo de organização:", "text")
        
        # PASSO 3: Sistema funcionando
        self.print_section("PASSO 3: Sistema musical em funcionamento", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo do seu Organizador Musical:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: ORGANIZADOR MUSICAL INTELIGENTE
# Módulo 9: Listas e Coleções

import random

class OrganizadorMusical:
    def __init__(self):
        """Inicializa o organizador musical"""
        # Listas principais do sistema
        self.biblioteca = []
        self.playlists = []
        self.artistas_favoritos = []
        self.historico_reproducao = []
        
        # Dados de exemplo
        self._carregar_dados_exemplo()
    
    def _carregar_dados_exemplo(self):
        """Carrega dados de exemplo para demonstração"""
        # Biblioteca principal de músicas
        self.biblioteca = [
            {{"titulo": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock", "duracao": 6, "plays": 150}},
            {{"titulo": "Billie Jean", "artista": "Michael Jackson", "genero": "Pop", "duracao": 4, "plays": 200}},
            {{"titulo": "Take Five", "artista": "Dave Brubeck", "genero": "Jazz", "duracao": 5, "plays": 80}},
            {{"titulo": "Hotel California", "artista": "Eagles", "genero": "Rock", "duracao": 6, "plays": 175}},
            {{"titulo": "Thriller", "artista": "Michael Jackson", "genero": "Pop", "duracao": 6, "plays": 190}},
            {{"titulo": "Blue in Green", "artista": "Miles Davis", "genero": "Jazz", "duracao": 5, "plays": 65}},
            {{"titulo": "Sweet Child O' Mine", "artista": "Guns N' Roses", "genero": "Rock", "duracao": 5, "plays": 140}},
            {{"titulo": "Shape of You", "artista": "Ed Sheeran", "genero": "Pop", "duracao": 4, "plays": 300}}
        ]
        
        # Playlists temáticas
        self.playlists = [
            {{"nome": "Rock Clássico", "musicas": ["Bohemian Rhapsody", "Hotel California", "Sweet Child O' Mine"]}},
            {{"nome": "Hits do Pop", "musicas": ["Billie Jean", "Thriller", "Shape of You"]}},
            {{"nome": "Jazz Suave", "musicas": ["Take Five", "Blue in Green"]}}
        ]
        
        # Artistas favoritos (lista simples)
        self.artistas_favoritos = ["Queen", "Michael Jackson", "Miles Davis"]
    
    def exibir_biblioteca(self):
        """Exibe toda a biblioteca musical"""
        print("\\n🎵 BIBLIOTECA MUSICAL")
        print("=" * 70)
        print(f"{{'TÍTULO':<20}} {{'ARTISTA':<15}} {{'GÊNERO':<10}} {{'DURAÇÃO':<8}} {{'PLAYS':<6}}")
        print("=" * 70)
        
        for musica in self.biblioteca:
            print(f"{{musica['titulo']:<20}} {{musica['artista']:<15}} "
                  f"{{musica['genero']:<10}} {{musica['duracao']:<8}}min {{musica['plays']:<6}}")
        
        print(f"\\n📊 Total: {{len(self.biblioteca)}} músicas")
    
    def buscar_por_artista(self, nome_artista):
        """Busca todas as músicas de um artista"""
        musicas_artista = [m for m in self.biblioteca if m['artista'].lower() == nome_artista.lower()]
        
        if musicas_artista:
            print(f"\\n🎤 MÚSICAS DE {{nome_artista.upper()}}:")
            print("-" * 40)
            for musica in musicas_artista:
                print(f"• {{musica['titulo']}} ({{musica['genero']}}) - {{musica['plays']}} plays")
            return musicas_artista
        else:
            print(f"❌ Nenhuma música encontrada para {{nome_artista}}")
            return []
    
    def buscar_por_genero(self, genero):
        """Busca todas as músicas de um gênero"""
        musicas_genero = [m for m in self.biblioteca if m['genero'].lower() == genero.lower()]
        
        if musicas_genero:
            print(f"\\n🎼 MÚSICAS DE {{genero.upper()}}:")
            print("-" * 40)
            for musica in musicas_genero:
                print(f"• {{musica['titulo']}} - {{musica['artista']}} ({{musica['plays']}} plays)")
            return musicas_genero
        else:
            print(f"❌ Nenhuma música encontrada no gênero {{genero}}")
            return []
    
    def top_musicas(self, limite=5):
        """Exibe o top de músicas mais tocadas"""
        musicas_ordenadas = sorted(self.biblioteca, key=lambda x: x['plays'], reverse=True)
        top_lista = musicas_ordenadas[:limite]
        
        print(f"\\n🏆 TOP {{limite}} MAIS TOCADAS:")
        print("-" * 50)
        for i, musica in enumerate(top_lista, 1):
            print(f"{{i}}. {{musica['titulo']}} - {{musica['artista']}} ({{musica['plays']}} plays)")
        
        return top_lista
    
    def criar_playlist_automatica(self, genero, tamanho=5):
        """Cria playlist automática baseada em gênero"""
        musicas_genero = [m for m in self.biblioteca if m['genero'].lower() == genero.lower()]
        
        if len(musicas_genero) >= tamanho:
            # Seleciona músicas aleatórias do gênero
            playlist_musicas = random.sample(musicas_genero, tamanho)
            nome_playlist = f"Mix {{genero}} Automático"
            
            nova_playlist = {{
                "nome": nome_playlist,
                "musicas": [m['titulo'] for m in playlist_musicas]
            }}
            
            self.playlists.append(nova_playlist)
            
            print(f"\\n🎧 PLAYLIST CRIADA: {{nome_playlist}}")
            print("-" * 40)
            for i, musica in enumerate(playlist_musicas, 1):
                print(f"{{i}}. {{musica['titulo']}} - {{musica['artista']}}")
            
            return nova_playlist
        else:
            print(f"❌ Não há músicas suficientes do gênero {{genero}}")
            return None
    
    def exibir_playlists(self):
        """Exibe todas as playlists"""
        print("\\n📋 PLAYLISTS DISPONÍVEIS:")
        print("=" * 40)
        
        for i, playlist in enumerate(self.playlists, 1):
            print(f"\\n{{i}}. {{playlist['nome']}} ({{len(playlist['musicas'])}} músicas)")
            for j, musica in enumerate(playlist['musicas'], 1):
                print(f"   {{j}}. {{musica}}")
    
    def estatisticas_gerais(self):
        """Exibe estatísticas gerais da biblioteca"""
        total_musicas = len(self.biblioteca)
        total_artistas = len(set(m['artista'] for m in self.biblioteca))
        total_generos = len(set(m['genero'] for m in self.biblioteca))
        total_plays = sum(m['plays'] for m in self.biblioteca)
        duracao_total = sum(m['duracao'] for m in self.biblioteca)
        
        print("\\n📊 ESTATÍSTICAS GERAIS:")
        print("=" * 30)
        print(f"🎵 Total de músicas: {{total_musicas}}")
        print(f"🎤 Total de artistas: {{total_artistas}}")
        print(f"🎼 Total de gêneros: {{total_generos}}")
        print(f"▶️ Total de reproduções: {{total_plays:,}}")
        print(f"⏰ Duração total: {{duracao_total}} minutos ({{duracao_total/60:.1f}} horas)")
        print(f"📈 Média de plays por música: {{total_plays/total_musicas:.1f}}")
        
        # Gênero mais popular
        generos_count = {{}}
        for musica in self.biblioteca:
            genero = musica['genero']
            generos_count[genero] = generos_count.get(genero, 0) + musica['plays']
        
        genero_popular = max(generos_count, key=generos_count.get)
        print(f"🏆 Gênero mais tocado: {{genero_popular}}")

# === DEMONSTRAÇÃO DO SISTEMA ===
print("🎵 ORGANIZADOR MUSICAL INTELIGENTE V1.0")
print("=" * 50)

# Criando instância do organizador
organizador = OrganizadorMusical()

# Demonstração 1: Exibir biblioteca
organizador.exibir_biblioteca()

# Demonstração 2: Buscar por artista
organizador.buscar_por_artista("Michael Jackson")

# Demonstração 3: Top músicas
organizador.top_musicas(3)

# Demonstração 4: Buscar por gênero
organizador.buscar_por_genero("Rock")

# Demonstração 5: Criar playlist automática
organizador.criar_playlist_automatica("Jazz", 2)

# Demonstração 6: Exibir todas as playlists
organizador.exibir_playlists()

# Demonstração 7: Estatísticas gerais
organizador.estatisticas_gerais()

print("\\n✨ ORGANIZADOR FUNCIONANDO PERFEITAMENTE!")
print("🎧 Suas músicas nunca estiveram tão bem organizadas!")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        print("🚀 Executando seu Organizador Musical Inteligente:")
        self.executar_codigo(codigo_final)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um organizador musical completo!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar sistema de avaliação e comentários",
            "Implementar algoritmos de recomendação musical",
            "Integrar com APIs de streaming (Spotify, Apple Music)",
            "Criar interface gráfica para o organizador",
            "Adicionar análise de letras e sentimentos musicais"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Maestro das Listas!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Organizador Musical Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo09Listas()
    print("Teste do módulo 9 - versão refatorada")
    module._listas_interativo()