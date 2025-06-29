#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 21: Generators e Iterators
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda generators e iterators de forma interativa
"""

from ..shared.base_module import BaseModule
import sys
import time
import random
from typing import Iterator, Generator, Dict, Any, List, Optional, Callable
from datetime import datetime
from itertools import islice, chain, groupby


class Modulo21Geradores(BaseModule):
    """Módulo 21: Generators e Iterators - Eficiência Máxima"""
    
    def __init__(self):
        super().__init__("modulo_21", "Generators e Iterators")
        self.has_mini_project = True
        self.mini_project_points = 110
    
    def execute(self) -> None:
        """Executa o módulo Generators e Iterators"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._geradores()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _geradores(self) -> None:
        """Conteúdo principal do módulo Generators e Iterators"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ MÓDULO 21: GENERATORS E ITERATORS")
        else:
            print("\n" + "="*60)
            print("⚡ MÓDULO 21: GENERATORS E ITERATORS")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo dos Generators e Iterators!")
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
            self._mini_projeto_pipeline_dados()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (7 SEÇÕES) ===
        secoes = [
            {
                'id': 'secao_conceito_generators',
                'titulo': '🎯 O que são Generators?',
                'descricao': 'Entenda o conceito que revoluciona o processamento de dados',
                'funcao': self._secao_conceito_generators
            },
            {
                'id': 'secao_yield_funcionamento',
                'titulo': '⚙️ Como yield funciona?',
                'descricao': 'Veja a mágica por trás da palavra-chave yield',
                'funcao': self._secao_yield_funcionamento
            },
            {
                'id': 'secao_iterators_customizados',
                'titulo': '🔄 Iterators Customizados',
                'descricao': 'Aprenda a criar seus próprios iterators do zero',
                'funcao': self._secao_iterators_customizados
            },
            {
                'id': 'secao_generator_expressions',
                'titulo': '💡 Generator Expressions',
                'descricao': 'Sintaxe concisa para generators poderosos',
                'funcao': self._secao_generator_expressions
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas em projetos profissionais',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_memoria_performance',
                'titulo': '⚡ Memória e Performance',
                'descricao': 'Por que generators são tão eficientes?',
                'funcao': self._secao_memoria_performance
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre Generators',
                'descricao': 'Fatos interessantes e funcionalidades avançadas',
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

    def _secao_conceito_generators(self) -> None:
        """Seção: O que são Generators?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO GENERATORS?", "🎯")

        # === DEFINIÇÃO DO CONCEITO (SEMPRE PRIMEIRO) ===
        self.print_concept(
            "Generator",
            "Uma função especial que produz uma sequência de valores sob demanda, pausando e retomando sua execução"
        )

        # === DICA RELACIONADA ===
        self.print_tip("Generators são como 'fábricas preguiçosas' - só produzem quando você pede!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como uma torneira de água:", "text")
        self.print_colored("• Lista comum: enche um balde inteiro (usa muita memória)", "text")
        self.print_colored("• Generator: abre torneira quando precisa (economiza água/memória)", "text")
        self.print_colored("• Você controla quando quer mais água (valores)", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Função usa 'yield' ao invés de 'return'",
            "2. Quando yield é encontrado, função 'pausa' e retorna valor",
            "3. Estado da função fica 'congelado' na memória",
            "4. Próxima chamada continua de onde parou",
            "5. Quando função termina, levanta StopIteration"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO SIMPLES:", "success")
        codigo_exemplo = '''# Comparando função normal vs generator
def numeros_lista(n):
    """Função normal - cria lista completa"""
    resultado = []
    for i in range(1, n + 1):
        resultado.append(i)
    return resultado

def numeros_generator(n):
    """Generator - produz um valor por vez"""
    for i in range(1, n + 1):
        yield i  # Pausa aqui e retorna valor

# Testando a diferença
print("=== FUNÇÃO NORMAL ===")
lista = numeros_lista(5)
print(f"Lista completa: {lista}")
print(f"Tipo: {type(lista)}")

print("\\n=== GENERATOR ===")
gen = numeros_generator(5)
print(f"Generator object: {gen}")
print(f"Tipo: {type(gen)}")

print("\\nUsando generator:")
for numero in gen:
    print(f"Recebi: {numero}")'''

        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix - Streaming de conteúdo (carrega conforme assiste)",
            "Google - Processamento de big data (resultados sob demanda)",
            "Instagram - Feed infinito (carrega mais posts quando scrolla)",
            "Spotify - Recomendações musicais (gera sugestões dinamicamente)",
            "Bancos - Processamento de transações (batch processing eficiente)"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_yield_funcionamento(self) -> None:
        """Seção: Como yield funciona?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO YIELD FUNCIONA?", "⚙️", "success")

        self.print_concept(
            "yield",
            "A palavra-chave mágica que transforma uma função em generator, pausando a execução e retornando valores"
        )

        self.print_colored("\n🔍 VAMOS DISSECAR O YIELD:", "info")

        codigo_detalhado = '''# Demonstração passo a passo do yield
def contador_com_debug():
    """Generator que mostra cada passo da execução"""
    print("🚀 Generator iniciado!")
    
    print("📝 Antes do primeiro yield")
    yield 1
    print("📝 Depois do primeiro yield, antes do segundo")
    
    yield 2
    print("📝 Depois do segundo yield, antes do terceiro")
    
    yield 3
    print("📝 Depois do terceiro yield - prestes a terminar")
    
    print("🏁 Generator terminando!")

print("=== RASTREANDO EXECUÇÃO DO GENERATOR ===")

# Criando o generator
gen = contador_com_debug()
print(f"Generator criado: {gen}")

print("\\n1. Primeira chamada de next():")
primeiro = next(gen)
print(f"   Valor retornado: {primeiro}")

print("\\n2. Segunda chamada de next():")
segundo = next(gen)  
print(f"   Valor retornado: {segundo}")

print("\\n3. Terceira chamada de next():")
terceiro = next(gen)
print(f"   Valor retornado: {terceiro}")

print("\\n4. Tentando chamar next() novamente:")
try:
    quarto = next(gen)
except StopIteration:
    print("   StopIteration levantada - generator esgotado!")

# Yield com valor de retorno
def generator_com_calculo():
    """Generator que faz cálculos sob demanda"""
    print("💭 Calculando quadrados...")
    for i in range(1, 6):
        quadrado = i ** 2
        print(f"   Calculei {i}² = {quadrado}")
        yield quadrado

print("\\n=== GENERATOR COM CÁLCULOS ===")
quadrados = generator_com_calculo()

print("Consumindo valores um a um:")
for valor in quadrados:
    print(f"Recebi: {valor}")
    input("   Pressione ENTER para continuar...")'''

        self.exemplo(codigo_detalhado)
        print("\n🚀 Executando demonstração interativa:")
        self.executar_codigo(codigo_detalhado)

        self.print_tip("yield 'congela' o estado da função - variáveis locais ficam preservadas!")

        self.pausar()

    def _secao_iterators_customizados(self) -> None:
        """Seção: Iterators Customizados"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ITERATORS CUSTOMIZADOS", "🔄", "warning")

        self.print_concept(
            "Iterator Protocol",
            "Um padrão que define como criar objetos que podem ser percorridos com for loops"
        )

        self.print_colored("\n🏗️ PROTOCOLO DO ITERATOR:", "info")
        protocolo = [
            "__iter__(): retorna o próprio iterator",
            "__next__(): retorna próximo item ou StopIteration"
        ]
        for item in protocolo:
            self.print_colored(f"• {item}", "text")

        exemplo_iterators = '''# Criando iterators customizados do zero
class ContadorIterator:
    """Iterator que conta de start até end"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        raise StopIteration

class FibonacciIterator:
    """Iterator que gera sequência de Fibonacci"""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            if self.count == 1:
                return self.a
            elif self.count == 2:
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                return self.b
        raise StopIteration

# Comparando com generators equivalentes
def contador_generator(start, end):
    """Generator equivalente ao ContadorIterator"""
    for i in range(start, end):
        yield i

def fibonacci_generator(max_count):
    """Generator equivalente ao FibonacciIterator"""
    a, b = 0, 1
    for _ in range(max_count):
        yield a
        a, b = b, a + b

print("=== ITERATOR CLASSES VS GENERATORS ===")

print("\\n1. Contador Iterator:")
contador_iter = ContadorIterator(1, 6)
print("  Iterator:", list(contador_iter))

contador_gen = contador_generator(1, 6)
print("  Generator:", list(contador_gen))

print("\\n2. Fibonacci Iterator:")
fib_iter = FibonacciIterator(8)
print("  Iterator:", list(fib_iter))

fib_gen = fibonacci_generator(8)
print("  Generator:", list(fib_gen))

# Medindo linhas de código
import inspect

contador_iter_lines = len(inspect.getsource(ContadorIterator).split('\\n'))
contador_gen_lines = len(inspect.getsource(contador_generator).split('\\n'))

print(f"\\n📊 COMPARAÇÃO DE CÓDIGO:")
print(f"Contador Iterator: {contador_iter_lines} linhas")
print(f"Contador Generator: {contador_gen_lines} linhas")
print(f"Generator é {contador_iter_lines/contador_gen_lines:.1f}x mais conciso!")'''

        self.exemplo(exemplo_iterators)
        print("\n🚀 Comparando iterators e generators:")
        self.executar_codigo(exemplo_iterators)

        self.pausar()

    def _secao_generator_expressions(self) -> None:
        """Seção: Generator Expressions"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("GENERATOR EXPRESSIONS", "💡", "info")

        self.print_concept(
            "Generator Expression",
            "Sintaxe concisa para criar generators usando parênteses ao invés de colchetes"
        )

        self.print_colored("\n🆚 SINTAXE COMPARADA:", "warning")
        self.print_colored("Lista: [x**2 for x in range(5)]", "text")
        self.print_colored("Generator: (x**2 for x in range(5))", "text")

        exemplo_expressions = '''# Generator Expressions - sintaxe concisa
import sys

# Comparando List Comprehension vs Generator Expression
print("=== COMPARAÇÃO: LISTA VS GENERATOR EXPRESSION ===")

# Lista - todos os valores na memória
lista_quadrados = [x**2 for x in range(1000)]
print(f"Lista com 1000 quadrados: {sys.getsizeof(lista_quadrados)} bytes")

# Generator - valores sob demanda
gen_quadrados = (x**2 for x in range(1000))
print(f"Generator equivalente: {sys.getsizeof(gen_quadrados)} bytes")

diferenca = sys.getsizeof(lista_quadrados) / sys.getsizeof(gen_quadrados)
print(f"Generator usa {diferenca:.0f}x menos memória!")

# Exemplos práticos de generator expressions
print("\\n=== EXEMPLOS PRÁTICOS ===")

# 1. Processando números
pares = (x for x in range(20) if x % 2 == 0)
print("Números pares:", list(pares))

# 2. Transformando strings
nomes = ["João", "maria", "PEDRO", "ana"]
nomes_formatados = (nome.title() for nome in nomes)
print("Nomes formatados:", list(nomes_formatados))

# 3. Calculando valores
vendas = [100, 250, 300, 150, 400]
vendas_com_desconto = (venda * 0.9 for venda in vendas if venda > 200)
print("Vendas > 200 com 10% desconto:", list(vendas_com_desconto))

# 4. Aninhando generator expressions
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elementos_pares = (num for linha in matriz for num in linha if num % 2 == 0)
print("Elementos pares da matriz:", list(elementos_pares))

# 5. Pipeline de transformações
texto = "Python é uma linguagem incrível"
palavras_grandes = (palavra.upper() for palavra in texto.split() if len(palavra) > 4)
print("Palavras grandes em maiúscula:", list(palavras_grandes))

# Usando generator expression com sum, max, any, all
numeros = (x for x in range(1, 101))
soma = sum(numeros)
print(f"\\nSoma de 1 a 100: {soma}")

# Reutilizando generator (cuidado - eles se esgotam!)
numeros2 = (x for x in range(1, 11))
print(f"Primeiro uso - lista: {list(numeros2)}")
print(f"Segundo uso - lista: {list(numeros2)}")  # Vazio!

# Generator infinito
def contador_infinito():
    i = 0
    while True:
        yield i
        i += 1

print("\\n=== GENERATOR INFINITO ===")
infinito = contador_infinito()
primeiros_10 = [next(infinito) for _ in range(10)]
print(f"Primeiros 10 números: {primeiros_10}")'''

        self.exemplo(exemplo_expressions)
        print("\n🚀 Testando generator expressions:")
        self.executar_codigo(exemplo_expressions)

        self.pausar()

    def _secao_casos_uso_reais(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CASOS DE USO NO MUNDO REAL", "🌍", "accent")

        casos_uso = {
            "📊 Processamento de Big Data": [
                "Apache Spark: Processamento distribuído de datasets",
                "Pandas: Leitura de arquivos CSV gigantes chunk por chunk",
                "ETL Pipelines: Transformação de dados em streaming"
            ],
            "🌐 Desenvolvimento Web": [
                "Django: Paginação eficiente de resultados",
                "FastAPI: Streaming de responses HTTP",
                "Web scraping: Processamento de páginas uma por vez"
            ],
            "🎮 Jogos e Simulações": [
                "Procedural generation: Geração infinita de terrenos",
                "AI pathfinding: Exploração de caminhos sob demanda",
                "Event systems: Processamento de eventos em tempo real"
            ],
            "💾 Sistemas de Arquivo": [
                "Log processing: Análise de logs linha por linha",
                "Backup systems: Compressão incremental",
                "File monitoring: Observação de mudanças em tempo real"
            ],
            "🔄 APIs e Microserviços": [
                "Pagination: Resultados paginados de APIs",
                "Stream processing: Kafka, RabbitMQ consumers",
                "Rate limiting: Controle de throughput"
            ]
        }

        for categoria, exemplos in casos_uso.items():
            self.print_colored(f"\n{categoria}:", "warning")
            for exemplo in exemplos:
                self.print_colored(f"  • {exemplo}", "text")

        self.print_colored("\n💼 EMPRESAS QUE USAM INTENSIVAMENTE:", "info")
        empresas = [
            "Google: MapReduce e BigQuery para processamento distribuído",
            "Netflix: Streaming de vídeo e recomendações em tempo real",
            "Instagram: Feed infinito com lazy loading",
            "Airbnb: Busca e filtros de propriedades com paginação",
            "Uber: Processamento de localizações e rotas dinâmicas"
        ]
        for empresa in empresas:
            self.print_colored(f"• {empresa}", "accent")

        # Exemplo prático
        self.print_colored("\n💻 EXEMPLO PRÁTICO - PROCESSAMENTO DE LOGS:", "success")
        exemplo_pratico = '''# Simulando processamento de logs de um servidor web
import random
from datetime import datetime, timedelta

def gerar_log_entries(num_entries=100):
    """Generator que simula entradas de log de servidor"""
    ips = ["192.168.1.10", "10.0.0.15", "172.16.0.5", "203.0.113.1"]
    pages = ["/", "/login", "/dashboard", "/api/users", "/api/orders"]
    statuses = [200, 200, 200, 404, 500, 301]  # 200 mais comum
    
    base_time = datetime.now() - timedelta(hours=24)
    
    for i in range(num_entries):
        timestamp = base_time + timedelta(minutes=i)
        ip = random.choice(ips)
        page = random.choice(pages)
        status = random.choice(statuses)
        size = random.randint(100, 5000)
        
        # Formato típico de log de servidor
        yield f'{ip} - - [{timestamp.strftime("%d/%b/%Y:%H:%M:%S")}] "GET {page} HTTP/1.1" {status} {size}'

def processar_logs_memoria_eficiente(log_generator):
    """Processa logs sem carregar tudo na memória"""
    stats = {
        'total_requests': 0,
        'errors_4xx': 0,
        'errors_5xx': 0,
        'unique_ips': set(),
        'popular_pages': {},
        'total_bytes': 0
    }
    
    for log_line in log_generator:
        stats['total_requests'] += 1
        
        # Parsing simples da linha de log
        parts = log_line.split()
        ip = parts[0]
        status = int(parts[-2])
        size = int(parts[-1])
        
        # Extrai página da requisição
        page = parts[6] if len(parts) > 6 else "unknown"
        
        # Atualiza estatísticas
        stats['unique_ips'].add(ip)
        stats['total_bytes'] += size
        
        if 400 <= status < 500:
            stats['errors_4xx'] += 1
        elif status >= 500:
            stats['errors_5xx'] += 1
        
        if page in stats['popular_pages']:
            stats['popular_pages'][page] += 1
        else:
            stats['popular_pages'][page] = 1
    
    return stats

# Processando logs com generator
print("🔍 Processando logs do servidor...")
logs = gerar_log_entries(50)
estatisticas = processar_logs_memoria_eficiente(logs)

print(f"\\n📊 ESTATÍSTICAS:")
print(f"Total de requisições: {estatisticas['total_requests']}")
print(f"IPs únicos: {len(estatisticas['unique_ips'])}")
print(f"Erros 4xx: {estatisticas['errors_4xx']}")
print(f"Erros 5xx: {estatisticas['errors_5xx']}")
print(f"Total de bytes: {estatisticas['total_bytes']:,}")

print(f"\\n📈 PÁGINAS MAIS ACESSADAS:")
pages_sorted = sorted(estatisticas['popular_pages'].items(), key=lambda x: x[1], reverse=True)
for page, count in pages_sorted[:3]:
    print(f"  {page}: {count} acessos")'''

        self.exemplo(exemplo_pratico)
        print("\n🚀 Exemplo real de processamento:")
        self.executar_codigo(exemplo_pratico)

        self.pausar()

    def _secao_memoria_performance(self) -> None:
        """Seção: Memória e Performance"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("MEMÓRIA E PERFORMANCE", "⚡", "success")

        self.print_concept(
            "Lazy Evaluation",
            "Generators só calculam valores quando necessário, economizando memória e melhorando performance"
        )

        exemplo_performance = '''# Demonstração de eficiência de memória e performance
import sys
import time
import tracemalloc

def medir_memoria_e_tempo(func, *args, **kwargs):
    """Utilitário para medir uso de memória e tempo"""
    tracemalloc.start()
    start_time = time.time()
    
    resultado = func(*args, **kwargs)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'resultado': resultado,
        'tempo': end_time - start_time,
        'memoria_atual': current,
        'memoria_pico': peak
    }

# Função que usa lista (carrega tudo na memória)
def processar_com_lista(n):
    """Processa números usando lista"""
    numeros = [x**2 for x in range(n)]  # Todos na memória
    soma = sum(numeros)
    return soma

# Função que usa generator (lazy evaluation)
def processar_com_generator(n):
    """Processa números usando generator"""
    numeros = (x**2 for x in range(n))  # Sob demanda
    soma = sum(numeros)
    return soma

print("=== COMPARAÇÃO DE PERFORMANCE ===")
n = 100000  # 100 mil números

print(f"\\nProcessando {n:,} números...")

# Teste com lista
print("\\n1. Usando LISTA:")
stats_lista = medir_memoria_e_tempo(processar_com_lista, n)
print(f"   Tempo: {stats_lista['tempo']:.4f} segundos")
print(f"   Memória pico: {stats_lista['memoria_pico'] / 1024 / 1024:.2f} MB")
print(f"   Resultado: {stats_lista['resultado']:,}")

# Teste com generator
print("\\n2. Usando GENERATOR:")
stats_gen = medir_memoria_e_tempo(processar_com_generator, n)
print(f"   Tempo: {stats_gen['tempo']:.4f} segundos")
print(f"   Memória pico: {stats_gen['memoria_pico'] / 1024 / 1024:.2f} MB")
print(f"   Resultado: {stats_gen['resultado']:,}")

# Comparação
reducao_memoria = (1 - stats_gen['memoria_pico'] / stats_lista['memoria_pico']) * 100
print(f"\\n📊 REDUÇÃO DE MEMÓRIA: {reducao_memoria:.1f}%")

# Demonstrando lazy evaluation
print("\\n=== LAZY EVALUATION EM AÇÃO ===")

def generator_com_prints(n):
    """Generator que mostra quando cada valor é calculado"""
    for i in range(n):
        print(f"   Calculando {i}...")
        yield i**2

print("\\nCriando generator (não calcula nada ainda):")
gen = generator_com_prints(5)
print("Generator criado!")

print("\\nConsumindo valores um por vez:")
for i, valor in enumerate(gen):
    print(f"Recebi valor {valor}")
    if i >= 2:  # Para após 3 valores
        break
print("Parou no meio - valores restantes não foram calculados!")

# Generator infinito - impossível com listas
def fibonacci_infinito():
    """Generator que produz Fibonacci infinitamente"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\\n=== GENERATOR INFINITO ===")
fib = fibonacci_infinito()
primeiros_15 = []
for _ in range(15):
    primeiros_15.append(next(fib))

print(f"Primeiros 15 Fibonacci: {primeiros_15}")
print("Generator ainda tem infinitos números disponíveis!")

# Pipeline eficiente
def numeros_grandes(start, end):
    """Produz números em range"""
    for i in range(start, end):
        yield i

def apenas_pares(numeros_gen):
    """Filtra apenas pares"""
    for num in numeros_gen:
        if num % 2 == 0:
            yield num

def elevar_ao_cubo(numeros_gen):
    """Eleva números ao cubo"""
    for num in numeros_gen:
        yield num ** 3

print("\\n=== PIPELINE EFICIENTE ===")
print("Processando 1 milhão de números através de pipeline...")

pipeline = elevar_ao_cubo(apenas_pares(numeros_grandes(1, 1000000)))

# Pega apenas os primeiros 10 resultados
resultado = []
for i, valor in enumerate(pipeline):
    resultado.append(valor)
    if i >= 9:  # Apenas 10 valores
        break

print(f"Primeiros 10 resultados: {resultado}")
print("Pipeline processou apenas os valores necessários!")'''

        self.exemplo(exemplo_performance)
        print("\n🚀 Medindo performance:")
        self.executar_codigo(exemplo_performance)

        self.pausar()

    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre Generators"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CURIOSIDADES SOBRE GENERATORS", "💫", "info")

        curiosidades = [
            {
                "titulo": "🎭 Origem dos Generators",
                "texto": "Generators foram inspirados nos 'iterators' do C++ e 'yield' do CLU (1975), mas Python os popularizou!"
            },
            {
                "titulo": "🧠 PEP 255",
                "texto": "Generators foram oficialmente introduzidos no Python 2.2 através da PEP 255 por Tim Peters e Neil Schemenauer!"
            },
            {
                "titulo": "⚡ Performance Extrema",
                "texto": "Um generator pode ser até 90% mais eficiente em memória que listas equivalentes em datasets grandes!"
            },
            {
                "titulo": "🔄 yield from",
                "texto": "Python 3.3 introduziu 'yield from' para delegar geração a outros generators de forma elegante!"
            },
            {
                "titulo": "🎪 Generator Tricks",
                "texto": "Você pode enviar valores DE VOLTA para generators usando .send() e até lançar exceções com .throw()!"
            },
            {
                "titulo": "🌟 Async Generators",
                "texto": "Python 3.6+ tem 'async generators' com 'async def' + 'yield' para programação assíncrona!"
            }
        ]

        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n{curiosidade['titulo']}", "accent")
            self.print_colored(curiosidade['texto'], "text")
            if i < len(curiosidades):
                input("\n🔸 Pressione ENTER para a próxima curiosidade...")

        # === CÓDIGO CURIOSO ===
        self.print_colored("\n🎪 CÓDIGO CURIOSO - GENERATOR COM COMUNICAÇÃO BIDIRECIONAL:", "warning")
        
        codigo_curioso = '''# Generator avançado com send() e throw()
def calculator_generator():
    """Generator que funciona como uma calculadora interativa"""
    print("🧮 Calculadora Generator iniciada!")
    result = 0
    
    while True:
        try:
            # Recebe operação do usuário
            operation = yield result
            
            if operation is None:
                continue
                
            if operation[0] == 'add':
                result += operation[1]
                print(f"➕ Adicionei {operation[1]}. Resultado: {result}")
                
            elif operation[0] == 'multiply':
                result *= operation[1]
                print(f"✖️ Multipliquei por {operation[1]}. Resultado: {result}")
                
            elif operation[0] == 'reset':
                result = 0
                print("🔄 Reset realizado. Resultado: 0")
                
            elif operation[0] == 'sqrt':
                if result >= 0:
                    result = result ** 0.5
                    print(f"√ Raiz quadrada calculada. Resultado: {result:.2f}")
                else:
                    raise ValueError("Não é possível calcular raiz de número negativo")
                    
        except Exception as e:
            print(f"❌ Erro na calculadora: {e}")
            result = 0  # Reset em caso de erro

# Demonstração da calculadora
print("=== CALCULADORA GENERATOR ===")
calc = calculator_generator()

# Inicia o generator
current = next(calc)
print(f"Valor inicial: {current}")

# Enviando operações
current = calc.send(('add', 10))
print(f"Após adicionar 10: {current}")

current = calc.send(('multiply', 3))
print(f"Após multiplicar por 3: {current}")

current = calc.send(('sqrt', None))
print(f"Após raiz quadrada: {current}")

# Teste de erro com throw()
print("\\nTestando tratamento de erro:")
try:
    calc.throw(ValueError, "Erro simulado!")
except ValueError:
    print("Erro capturado e tratado pelo generator")

current = next(calc)
print(f"Valor após erro: {current}")

# Generator com yield from
def sub_generator(n):
    """Sub-generator que produz números"""
    for i in range(n):
        yield f"Sub: {i}"

def main_generator():
    """Generator principal que delega para sub-generators"""
    yield "Início"
    yield from sub_generator(3)  # Delega para sub-generator
    yield "Meio"
    yield from sub_generator(2)
    yield "Fim"

print("\\n=== YIELD FROM ===")
main_gen = main_generator()
for value in main_gen:
    print(f"  {value}")

# Generator coroutine (conceito avançado)
def echo_coroutine():
    """Coroutine que ecoa mensagens"""
    print("🔊 Echo coroutine iniciada")
    while True:
        message = yield
        if message is not None:
            print(f"Echo: {message.upper()}")

print("\\n=== COROUTINE ===")
echo = echo_coroutine()
next(echo)  # Priming the coroutine

echo.send("hello world")
echo.send("python é incrível")
echo.send("generators são poderosos")'''

        self.exemplo(codigo_curioso)
        print("\n🚀 Recursos avançados de generators:")
        self.executar_codigo(codigo_curioso)

        self.print_success("\n🎉 Agora você conhece os segredos dos Generators!")
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
                'title': 'Quiz: Conhecimentos sobre Generators e Iterators',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual palavra-chave transforma uma função em generator?',
                        'answer': ['yield'],
                        'hint': 'É a palavra que "pausa" a função e retorna um valor'
                    },
                    {
                        'question': 'Quais métodos uma classe deve implementar para ser um iterator?',
                        'answer': ['__iter__ e __next__', '__iter__ __next__', 'iter e next'],
                        'hint': 'São dois métodos especiais que começam e terminam com __'
                    },
                    {
                        'question': 'Qual a principal vantagem dos generators sobre listas?',
                        'answer': ['economia de memória', 'memoria', 'lazy evaluation'],
                        'hint': 'Pense em como generators processam dados sob demanda'
                    },
                    {
                        'question': 'Como você cria uma generator expression?',
                        'answer': ['parênteses', '()', 'com parênteses'],
                        'hint': 'É como list comprehension, mas com outro tipo de bracket'
                    },
                    {
                        'question': 'O que acontece quando um generator se esgota?',
                        'answer': ['stopiteration', 'levanta stopiteration', 'stopiteration exception'],
                        'hint': 'Uma exceção específica é levantada automaticamente'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete este generator que produz números pares',
                        'starter': '''def numeros_pares(max_num):
    for i in range(2, max_num + 1, 2):
        # Complete aqui
''',
                        'solution': 'yield i',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a generator expression para quadrados ímpares',
                        'starter': '''numeros = range(1, 11)
quadrados_impares = # Complete aqui
print(list(quadrados_impares))''',
                        'solution': '(x**2 for x in numeros if x % 2 == 1)',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o método __next__ do iterator',
                        'starter': '''class ContadorRegressivo:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > 0:
            # Complete aqui
            self.start -= 1
            return self.start + 1
        raise StopIteration''',
                        'solution': 'result = self.start',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Monitor de Sistema em Tempo Real',
                'type': 'creative',
                'instruction': 'Crie um generator que simula monitoramento de sistema (CPU, memória, disco) gerando valores aleatórios a cada segundo, com alertas quando valores ficam críticos'
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

    def _run_quiz(self, quiz_data: Dict[str, Any]) -> None:
        """Executa quiz de conhecimentos"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("QUIZ: GENERATORS E ITERATORS", "📝", "info")
        
        pontos = 0
        total_questoes = len(quiz_data['questions'])
        
        for i, question in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\n🎯 PERGUNTA {i}/{total_questoes}:", "warning")
            self.print_colored(question['question'], "text")
            
            resposta = input("\n👉 Sua resposta: ").strip().lower()
            
            correto = any(resposta == ans.lower() for ans in question['answer'])
            
            if correto:
                pontos += 1
                self.print_success("✅ Correto! Muito bem!")
            else:
                self.print_warning(f"❌ Incorreto. {question['hint']}")
                self.print_colored(f"💡 Resposta esperada: {question['answer'][0]}", "info")
            
            if i < total_questoes:
                input("\n🔸 Pressione ENTER para a próxima pergunta...")
        
        # Resultado final
        percentual = (pontos / total_questoes) * 100
        self.print_colored(f"\n📊 RESULTADO: {pontos}/{total_questoes} ({percentual:.1f}%)", "accent")
        
        if percentual >= 80:
            self.print_success("🏆 Excelente! Você domina generators!")
        elif percentual >= 60:
            self.print_colored("👍 Bom trabalho! Continue praticando!", "warning")
        else:
            self.print_colored("📚 Revise o conteúdo e tente novamente!", "info")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _run_code_completion(self, code_data: Dict[str, Any]) -> None:
        """Executa exercícios de completar código"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMPLETE O CÓDIGO", "💻", "success")
        
        for i, exercise in enumerate(code_data['exercises'], 1):
            self.print_colored(f"\n🎯 EXERCÍCIO {i}: {exercise['instruction']}", "warning")
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercise['starter'])
            
            resposta = input("\n👉 Complete a linha: ").strip()
            
            if resposta.lower() == exercise['solution'].lower():
                self.print_success("✅ Perfeito! Código completado corretamente!")
            else:
                self.print_warning(f"❌ Não está certo. A resposta era: {exercise['solution']}")
            
            if i < len(code_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _run_creative_exercise(self, creative_data: Dict[str, Any]) -> None:
        """Executa exercício criativo"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("EXERCÍCIO CRIATIVO", "🎨", "accent")
        self.print_colored(creative_data['instruction'], "text")
        
        self.print_colored("\n💡 EXEMPLO DE SOLUÇÃO:", "info")
        exemplo_criativo = '''# Monitor de Sistema em Tempo Real
import random
import time

def system_monitor():
    """Generator que monitora sistema em tempo real"""
    while True:
        # Simula métricas do sistema
        cpu = random.uniform(0, 100)
        memory = random.uniform(20, 95)
        disk = random.uniform(10, 90)
        
        # Cria relatório
        timestamp = time.strftime("%H:%M:%S")
        status = "🟢 NORMAL"
        
        # Verifica alertas
        if cpu > 80 or memory > 90 or disk > 85:
            status = "🔴 CRÍTICO"
        elif cpu > 60 or memory > 70 or disk > 70:
            status = "🟡 ALERTA"
        
        yield {
            'timestamp': timestamp,
            'cpu': round(cpu, 1),
            'memory': round(memory, 1),
            'disk': round(disk, 1),
            'status': status
        }
        
        time.sleep(1)  # Atualiza a cada segundo

# Demonstração do monitor
print("=== MONITOR DE SISTEMA ===")
monitor = system_monitor()

print("Monitorando por 5 segundos...")
for i, metrics in enumerate(monitor):
    print(f"{metrics['timestamp']} | CPU: {metrics['cpu']}% | "
          f"MEM: {metrics['memory']}% | DISK: {metrics['disk']}% | {metrics['status']}")
    
    if i >= 4:  # Para após 5 leituras
        break

print("\\nMonitoramento finalizado!")'''
        
        self.exemplo(exemplo_criativo)
        self.executar_codigo(exemplo_criativo)
        
        self.print_colored("\n🎨 AGORA É SUA VEZ!", "warning")
        self.print_colored("Crie sua própria versão ou modifique este exemplo!", "text")
        self.print_tip("Você pode adicionar outras métricas, salvar logs, enviar notificações, etc.")
        
        input("\n🔸 Pressione ENTER quando terminar de pensar na sua solução...")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste conhecimentos sobre generators e iterators",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Monitor de sistema em tempo real",
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

    def _mini_projeto_pipeline_dados(self) -> None:
        """Mini Projeto - Módulo 21: Pipeline de Processamento de Dados com Generators"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS")
        else:
            print("\n" + "="*60)
            print("🎯 MINI PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS")
            print("="*60)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um pipeline de processamento de dados eficiente usando generators!")

        self.print_concept(
            "Pipeline de Processamento",
            "Um sistema que processa grandes volumes de dados de forma eficiente, usando generators para economizar memória"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado em:", "text")
        usos_praticos = [
            "🏦 Bancos - Processamento de milhões de transações diárias",
            "📊 Google Analytics - Análise de big data em tempo real",
            "🛒 Amazon - Processamento de logs de vendas e comportamento",
            "📱 Instagram - Análise de engajamento e feeds personalizados",
            "🎵 Spotify - Processamento de dados de escuta para recomendações"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        input("\n🔸 Pressione ENTER para começar o projeto...")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Geração de dados
        self.print_section("PASSO 1: Gerador de Dados Sintéticos", "📝", "info")
        self.print_tip("Vamos criar um generator que produz dados de vendas sintéticos")

        codigo_passo1 = '''# PASSO 1: Gerador de dados sintéticos
import random
import time
from datetime import datetime, timedelta
from typing import Generator, Dict, Any

class DataGenerator:
    """Gerador de dados sintéticos para demonstração"""
    
    @staticmethod
    def generate_sales_data(num_records: int = 100) -> Generator[Dict[str, Any], None, None]:
        """Gera dados de vendas sintéticos usando generator"""
        print(f"📊 Iniciando geração de {num_records} registros...")
        
        produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam", "Fone", "SSD", "RAM"]
        vendedores = ["Ana Silva", "João Santos", "Maria Lima", "Carlos Oliveira", "Paula Costa"]
        regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
        
        base_date = datetime.now() - timedelta(days=30)
        
        for i in range(num_records):
            # Progresso visual
            if i % 20 == 0 and i > 0:
                print(f"   Gerados {i}/{num_records} registros...")
            
            # Simula delay de processamento real
            if i % 50 == 0:
                time.sleep(0.1)
            
            # Gera registro individual
            venda = {
                "id": f"V{i+1:06d}",
                "produto": random.choice(produtos),
                "vendedor": random.choice(vendedores),
                "regiao": random.choice(regioes),
                "quantidade": random.randint(1, 10),
                "preco_unitario": round(random.uniform(50.0, 2000.0), 2),
                "data": (base_date + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
                "desconto": round(random.uniform(0, 0.3), 2),  # 0 a 30%
                "cliente_tipo": random.choice(["Bronze", "Prata", "Ouro", "Platina"])
            }
            
            yield venda

# Demonstração do gerador
print("=== GERADOR DE DADOS SINTÉTICOS ===")

# Criando o generator (não executa ainda!)
vendas_gen = DataGenerator.generate_sales_data(50)
print(f"Generator criado: {vendas_gen}")
print(f"Tipo: {type(vendas_gen)}")

# Consumindo alguns registros para demonstrar
print("\\nPrimeiros 5 registros gerados:")
for i, venda in enumerate(vendas_gen):
    print(f"  {i+1}. {venda['id']}: {venda['produto']} - R$ {venda['preco_unitario']}")
    if i >= 4:  # Para após 5 registros
        break

print("\\n✅ PASSO 1 CONCLUÍDO: Gerador de dados funcionando!")'''

        self.exemplo(codigo_passo1)
        self.executar_codigo(codigo_passo1)

        # PASSO 2: Transformadores de dados
        self.print_section("PASSO 2: Transformadores de Dados", "⚙️", "success")
        self.print_colored("Agora vamos criar generators que transformam os dados:", "text")

        codigo_passo2 = '''# PASSO 2: Transformadores de dados usando generators
from typing import Iterator, Callable

class DataTransformer:
    """Transformadores de dados usando generators para eficiência"""
    
    @staticmethod
    def filter_data(data_stream: Iterator[Dict], condition: Callable[[Dict], bool]) -> Generator[Dict, None, None]:
        """Filtra dados baseado em uma condição"""
        for record in data_stream:
            if condition(record):
                yield record
    
    @staticmethod
    def transform_record(data_stream: Iterator[Dict], transformer: Callable[[Dict], Dict]) -> Generator[Dict, None, None]:
        """Transforma cada registro individualmente"""
        for record in data_stream:
            yield transformer(record)
    
    @staticmethod
    def add_calculated_fields(data_stream: Iterator[Dict]) -> Generator[Dict, None, None]:
        """Adiciona campos calculados aos registros"""
        for record in data_stream:
            # Calcula total bruto
            quantidade = int(record.get('quantidade', 0))
            preco = float(record.get('preco_unitario', 0))
            desconto = float(record.get('desconto', 0))
            
            total_bruto = quantidade * preco
            valor_desconto = total_bruto * desconto
            total_liquido = total_bruto - valor_desconto
            
            # Adiciona campos calculados
            record['total_bruto'] = round(total_bruto, 2)
            record['valor_desconto'] = round(valor_desconto, 2)
            record['total_liquido'] = round(total_liquido, 2)
            
            # Classifica venda por valor
            if total_liquido >= 1000:
                record['categoria_venda'] = "Premium"
            elif total_liquido >= 500:
                record['categoria_venda'] = "Médio"
            else:
                record['categoria_venda'] = "Básico"
            
            # Calcula comissão do vendedor (5% do total líquido)
            record['comissao_vendedor'] = round(total_liquido * 0.05, 2)
            
            yield record
    
    @staticmethod
    def enrich_with_metadata(data_stream: Iterator[Dict]) -> Generator[Dict, None, None]:
        """Enriquece registros com metadados"""
        for i, record in enumerate(data_stream):
            # Adiciona metadados de processamento
            record['_processed_at'] = datetime.now().isoformat()
            record['_record_number'] = i + 1
            record['_pipeline_step'] = "enriched"
            
            yield record

# Testando transformadores
print("=== TRANSFORMADORES DE DADOS ===")

# Gera dados novamente
print("\\n1. Gerando dados base:")
dados_base = DataGenerator.generate_sales_data(30)

# Aplica filtro (vendas acima de R$ 500)
print("\\n2. Filtrando vendas com preço > R$ 500:")
dados_filtrados = DataTransformer.filter_data(
    dados_base,
    lambda record: float(record['preco_unitario']) > 500
)

# Adiciona campos calculados
print("\\n3. Adicionando campos calculados:")
dados_calculados = DataTransformer.add_calculated_fields(dados_filtrados)

# Enriquece com metadados
print("\\n4. Enriquecendo com metadados:")
dados_enriquecidos = DataTransformer.enrich_with_metadata(dados_calculados)

# Processa pipeline e mostra resultados
print("\\n5. Processando pipeline completo:")
resultados = []
for record in dados_enriquecidos:
    resultados.append(record)

print(f"\\nTotal de registros processados: {len(resultados)}")

if resultados:
    print("\\nAmostra do primeiro registro processado:")
    primeiro = resultados[0]
    for key, value in primeiro.items():
        print(f"  {key}: {value}")

print("\\n✅ PASSO 2 CONCLUÍDO: Pipeline de transformação funcionando!")'''

        self.exemplo(codigo_passo2)
        self.executar_codigo(codigo_passo2)

        # PASSO 3: Agregação e análise
        self.print_section("PASSO 3: Agregação e Análise Final", "🎬", "warning")
        self.print_colored("Finalmente, vamos agregar e analisar os dados processados:", "text")

        codigo_passo3 = '''# PASSO 3: Agregação e análise final
from collections import defaultdict
import statistics

class DataAggregator:
    """Agregadores de dados usando generators"""
    
    @staticmethod
    def aggregate_by_field(data_stream: Iterator[Dict], group_field: str) -> Generator[Dict, None, None]:
        """Agrega dados por um campo específico"""
        groups = defaultdict(list)
        
        # Agrupa todos os registros
        for record in data_stream:
            group_key = record.get(group_field, "Não informado")
            groups[group_key].append(record)
        
        # Calcula estatísticas para cada grupo
        for group_name, records in groups.items():
            if not records:
                continue
            
            # Calcula métricas do grupo
            total_vendas = len(records)
            total_receita = sum(float(r.get('total_liquido', 0)) for r in records)
            media_receita = total_receita / total_vendas if total_vendas > 0 else 0
            
            # Estatísticas de quantidade
            quantidades = [int(r.get('quantidade', 0)) for r in records]
            total_unidades = sum(quantidades)
            media_unidades = statistics.mean(quantidades) if quantidades else 0
            
            # Calcula comissões
            total_comissoes = sum(float(r.get('comissao_vendedor', 0)) for r in records)
            
            yield {
                'grupo': group_name,
                'grupo_campo': group_field,
                'total_vendas': total_vendas,
                'total_receita': round(total_receita, 2),
                'media_receita_por_venda': round(media_receita, 2),
                'total_unidades_vendidas': total_unidades,
                'media_unidades_por_venda': round(media_unidades, 2),
                'total_comissoes': round(total_comissoes, 2),
                'participacao_percentual': 0  # Será calculado depois
            }

class ReportGenerator:
    """Gerador de relatórios finais"""
    
    @staticmethod
    def generate_summary_report(aggregated_data: Iterator[Dict]) -> Dict[str, Any]:
        """Gera relatório resumo dos dados agregados"""
        print("📊 Gerando relatório final...")
        
        groups = list(aggregated_data)
        
        if not groups:
            return {"error": "Nenhum dado para análise"}
        
        # Calcula totais globais
        total_global_vendas = sum(g['total_vendas'] for g in groups)
        total_global_receita = sum(g['total_receita'] for g in groups)
        
        # Atualiza participação percentual
        for group in groups:
            if total_global_receita > 0:
                group['participacao_percentual'] = round(
                    (group['total_receita'] / total_global_receita) * 100, 2
                )
        
        # Ordena por receita (maior primeiro)
        groups_sorted = sorted(groups, key=lambda x: x['total_receita'], reverse=True)
        
        # Identifica top performers
        top_group = groups_sorted[0] if groups_sorted else None
        bottom_group = groups_sorted[-1] if groups_sorted else None
        
        report = {
            'resumo_geral': {
                'total_grupos': len(groups),
                'total_vendas': total_global_vendas,
                'total_receita': round(total_global_receita, 2),
                'receita_media_por_grupo': round(total_global_receita / len(groups), 2)
            },
            'top_performer': top_group,
            'bottom_performer': bottom_group,
            'grupos_detalhados': groups_sorted,
            'insights': ReportGenerator._generate_insights(groups_sorted)
        }
        
        return report
    
    @staticmethod
    def _generate_insights(groups: List[Dict]) -> List[str]:
        """Gera insights automáticos dos dados"""
        insights = []
        
        if len(groups) >= 2:
            top = groups[0]
            bottom = groups[-1]
            
            diferenca = top['total_receita'] - bottom['total_receita']
            insights.append(f"📈 Maior diferença de receita: R$ {diferenca:.2f} entre {top['grupo']} e {bottom['grupo']}")
        
        # Identifica grupos com alta performance por venda
        high_performers = [g for g in groups if g['media_receita_por_venda'] > 1000]
        if high_performers:
            insights.append(f"⭐ {len(high_performers)} grupos têm receita média > R$ 1.000 por venda")
        
        # Analisa concentração de receita
        top3_receita = sum(g['total_receita'] for g in groups[:3])
        total_receita = sum(g['total_receita'] for g in groups)
        concentracao = (top3_receita / total_receita) * 100 if total_receita > 0 else 0
        
        if concentracao > 60:
            insights.append(f"🎯 Top 3 grupos concentram {concentracao:.1f}% da receita total")
        
        return insights

# DEMONSTRAÇÃO COMPLETA DO PIPELINE
print("=== PIPELINE COMPLETO DE PROCESSAMENTO ===")
print()

# Pipeline completo: Geração → Filtragem → Transformação → Agregação → Relatório
print("🔄 Executando pipeline completo...")

# 1. Geração de dados
print("\\n   📊 Passo 1: Gerando dados...")
dados = DataGenerator.generate_sales_data(100)

# 2. Filtragem (vendas acima de R$ 200)
print("   🔍 Passo 2: Filtrando dados...")
dados_filtrados = DataTransformer.filter_data(
    dados,
    lambda r: float(r['preco_unitario']) > 200
)

# 3. Cálculos
print("   🧮 Passo 3: Adicionando cálculos...")
dados_calculados = DataTransformer.add_calculated_fields(dados_filtrados)

# 4. Agregação por vendedor
print("   📋 Passo 4: Agregando por vendedor...")
dados_agregados = DataAggregator.aggregate_by_field(dados_calculados, 'vendedor')

# 5. Relatório final
print("   📈 Passo 5: Gerando relatório...")
relatorio = ReportGenerator.generate_summary_report(dados_agregados)

# Exibe resultados
print("\\n" + "="*60)
print("📊 RELATÓRIO FINAL DO PIPELINE")
print("="*60)

resumo = relatorio['resumo_geral']
print(f"\\n📈 RESUMO GERAL:")
print(f"   Vendedores analisados: {resumo['total_grupos']}")
print(f"   Total de vendas: {resumo['total_vendas']}")
print(f"   Receita total: R$ {resumo['total_receita']:,.2f}")
print(f"   Receita média por vendedor: R$ {resumo['receita_media_por_grupo']:,.2f}")

if relatorio['top_performer']:
    top = relatorio['top_performer']
    print(f"\\n🏆 TOP PERFORMER: {top['grupo']}")
    print(f"   Vendas: {top['total_vendas']}")
    print(f"   Receita: R$ {top['total_receita']:,.2f}")
    print(f"   Participação: {top['participacao_percentual']}%")

print(f"\\n💡 INSIGHTS:")
for insight in relatorio['insights']:
    print(f"   {insight}")

print(f"\\n🔍 TOP 3 VENDEDORES:")
for i, vendedor in enumerate(relatorio['grupos_detalhados'][:3], 1):
    print(f"   {i}. {vendedor['grupo']}: R$ {vendedor['total_receita']:,.2f} ({vendedor['participacao_percentual']}%)")

print("\\n✅ PIPELINE CONCLUÍDO COM SUCESSO!")
print("\\n🎯 CONCEITOS APLICADOS:")
conceitos = [
    "✓ Generators para processamento eficiente de memória",
    "✓ Pipeline pattern com yield statements",
    "✓ Lazy evaluation para grandes datasets",
    "✓ Iterator protocol customizado",
    "✓ Generator expressions para transformações",
    "✓ Stream processing em tempo real",
    "✓ Agregação de dados com generators"
]

for conceito in conceitos:
    print(f"  {conceito}")'''

        self.exemplo(codigo_passo3)
        self.executar_codigo(codigo_passo3)

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("\nAqui está a estrutura completa que você criou:", "text")

        codigo_final = '''# 🐍 PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS
# Módulo 21: Generators e Iterators

import random
import time
from datetime import datetime, timedelta
from typing import Iterator, Generator, Dict, Any, List, Callable
from collections import defaultdict
import statistics

class DataGenerator:
    @staticmethod
    def generate_sales_data(num_records: int) -> Generator[Dict[str, Any], None, None]:
        """Gera dados de vendas usando generator para eficiência de memória"""
        # Implementação com yield para produção sob demanda
        pass

class DataTransformer:
    @staticmethod
    def filter_data(data_stream: Iterator[Dict], condition: Callable) -> Generator[Dict, None, None]:
        """Filtra dados em stream usando generator"""
        # Pipeline de filtros eficiente
        pass
    
    @staticmethod
    def add_calculated_fields(data_stream: Iterator[Dict]) -> Generator[Dict, None, None]:
        """Adiciona campos calculados em tempo real"""
        # Transformações sob demanda
        pass

class DataAggregator:
    @staticmethod
    def aggregate_by_field(data_stream: Iterator[Dict], group_field: str) -> Generator[Dict, None, None]:
        """Agrega dados por campo usando generators"""
        # Agregação eficiente de memória
        pass

# Pipeline completo com generators para máxima eficiência'''

        self.exemplo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um pipeline de processamento de dados profissional!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔄 Implementar processamento paralelo com multiprocessing",
            "💾 Adicionar persistência em banco de dados",
            "📊 Criar dashboards em tempo real",
            "🌐 Integrar com APIs externas para dados reais",
            "⚡ Otimizar para processamento de terabytes",
            "🎯 Implementar machine learning no pipeline"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Generators!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Pipeline de Processamento de Dados")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo21Geradores()
    print("Teste do módulo 21 - versão refatorada")
    module._geradores()