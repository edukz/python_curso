#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 23: Debugging e Profiling
Aprenda técnicas avançadas para encontrar e corrigir problemas no código
"""

import cProfile
import pstats
import time
import sys
import functools
from ..shared.base_module import BaseModule


class Modulo23Debugging(BaseModule):
    """Módulo 23: Debugging e Profiling - Encontrando e Corrigindo Problemas"""
    
    def __init__(self):
        super().__init__("modulo_23", "Debugging e Profiling")
        self.has_mini_project = True
        self.mini_project_points = 90
    
    def execute(self) -> None:
        """Executa o módulo sobre debugging e profiling"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._debugging_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _debugging_module(self) -> None:
        """Conteúdo principal sobre debugging e profiling"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐛 MÓDULO 23: DEBUGGING E PROFILING")
        else:
            print("\n" + "="*60)
            print("🐛 MÓDULO 23: DEBUGGING E PROFILING")
            print("="*60)
        
        print("🔍 Aprenda a encontrar e corrigir problemas no código!")
        print("🎯 Técnicas abordadas:")
        print("• Debugging com print e logging")
        print("• Uso do debugger interativo (pdb)")
        print("• Profiling de performance")
        print("• Medição de tempo e memória")
        print("• Análise de algoritmos")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._tecnicas_debugging()
        self._debugger_pdb()
        self._profiling_performance()
        self._medicao_tempo_memoria()
        self._decorators_profiling()
        self._mini_projeto_profiler()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _tecnicas_debugging(self):
        """Técnicas básicas de debugging"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔧 TÉCNICAS DE DEBUGGING")
        
        print("🐛 Métodos básicos para encontrar problemas:")
        print("• Print debugging - simples mas eficaz")
        print("• Logging - mais profissional")
        print("• Assert statements - verificações automáticas")
        print("• Try/except - captura de erros")
        
        codigo = '''import logging
import sys
from datetime import datetime

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def calcular_media(numeros):
    """Função com debugging integrado"""
    logging.info(f"Calculando média de {len(numeros)} números")
    
    # Debug: mostrar valores recebidos
    logging.debug(f"Números recebidos: {numeros}")
    
    # Validação com assert
    assert len(numeros) > 0, "Lista não pode estar vazia"
    assert all(isinstance(n, (int, float)) for n in numeros), "Todos os valores devem ser números"
    
    try:
        total = sum(numeros)
        media = total / len(numeros)
        
        logging.info(f"Média calculada: {media}")
        return media
        
    except Exception as e:
        logging.error(f"Erro ao calcular média: {e}")
        raise

def dividir_numeros(a, b):
    """Função com tratamento de erro"""
    print(f"🔢 Dividindo {a} por {b}")
    
    if b == 0:
        print("⚠️ Tentativa de divisão por zero!")
        logging.warning(f"Divisão por zero evitada: {a} / {b}")
        return None
    
    resultado = a / b
    print(f"✅ Resultado: {resultado}")
    return resultado

# Testes
try:
    print("=== TESTE 1: Média normal ===")
    media1 = calcular_media([1, 2, 3, 4, 5])
    print(f"Média: {media1}")
    
    print("\\n=== TESTE 2: Lista vazia ===")
    try:
        media2 = calcular_media([])
    except AssertionError as e:
        print(f"❌ Erro capturado: {e}")
    
    print("\\n=== TESTE 3: Divisões ===")
    dividir_numeros(10, 2)
    dividir_numeros(10, 0)  # Vai gerar warning
    
except Exception as e:
    logging.error(f"Erro geral: {e}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Técnicas de debugging")
        else:
            print("\n" + "="*50)
            print("TÉCNICAS DE DEBUGGING:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _debugger_pdb(self):
        """Uso do debugger interativo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐞 DEBUGGER INTERATIVO (PDB)")
        
        print("🔍 O debugger PDB permite:")
        print("• Pausar execução em pontos específicos")
        print("• Examinar variáveis em tempo real")
        print("• Executar código passo a passo")
        print("• Navegar pela stack de chamadas")
        
        print("\n📋 Comandos principais do PDB:")
        print("• n (next) - próxima linha")
        print("• s (step) - entrar em função")
        print("• c (continue) - continuar execução")
        print("• l (list) - mostrar código")
        print("• p <var> - mostrar variável")
        print("• pp <var> - pretty print")
        print("• q (quit) - sair do debugger")
        
        codigo = '''import pdb

def fibonacci(n):
    """Calcula fibonacci com debugging"""
    print(f"Calculando fibonacci({n})")
    
    # Breakpoint automático
    # pdb.set_trace()  # Descomentaria para debugar
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        print(f"  Iteração {i}: a={a}, b={b}")
    
    return b

def debug_example():
    """Exemplo de função com debugging"""
    valores = [1, 2, 3, 4, 5]
    resultados = []
    
    print("Processando valores...")
    for i, valor in enumerate(valores):
        # Simular breakpoint condicional
        if valor == 3:
            print(f"🔍 Valor especial encontrado: {valor}")
            # pdb.set_trace()  # Pausaria aqui
        
        resultado = valor ** 2
        resultados.append(resultado)
        print(f"  {i}: {valor}² = {resultado}")
    
    return resultados

# Exemplo sem pausar (para demonstração)
print("=== EXEMPLO FIBONACCI ===")
fib_5 = fibonacci(5)
print(f"Fibonacci(5) = {fib_5}")

print("\\n=== EXEMPLO DEBUG ===")
quadrados = debug_example()
print(f"Quadrados: {quadrados}")

print("\\n💡 Para usar o debugger:")
print("1. Descomente as linhas pdb.set_trace()")
print("2. Execute o código")
print("3. Use os comandos do PDB para navegar")
print("4. Digite 'c' para continuar ou 'q' para sair")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Debugger PDB")
        else:
            print("\n" + "="*50)
            print("DEBUGGER PDB:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _profiling_performance(self):
        """Profiling de performance com cProfile"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ PROFILING DE PERFORMANCE")
        
        print("📊 cProfile mostra onde seu código gasta tempo:")
        print("• Tempo total de execução")
        print("• Número de chamadas de função")
        print("• Tempo por chamada")
        print("• Funções mais custosas")
        
        codigo = '''import cProfile
import pstats
import time
import random
from io import StringIO

def algoritmo_lento(n):
    """Algoritmo ineficiente para demonstração"""
    resultado = 0
    for i in range(n):
        for j in range(100):  # Loop desnecessário
            resultado += i * j
    return resultado

def algoritmo_rapido(n):
    """Versão otimizada"""
    return sum(i * sum(range(100)) for i in range(n))

def busca_linear(lista, item):
    """Busca linear - O(n)"""
    for i, elemento in enumerate(lista):
        if elemento == item:
            return i
    return -1

def busca_binaria(lista_ordenada, item):
    """Busca binária - O(log n)"""
    esquerda, direita = 0, len(lista_ordenada) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_ordenada[meio] == item:
            return meio
        elif lista_ordenada[meio] < item:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1

def testar_performance():
    """Testa performance de diferentes algoritmos"""
    
    # Preparar dados
    lista_grande = list(range(10000))
    item_busca = random.choice(lista_grande)
    
    print("=== COMPARAÇÃO DE ALGORITMOS ===")
    
    # Algoritmo lento vs rápido
    print("\\n1. Algoritmo de soma:")
    start = time.time()
    resultado_lento = algoritmo_lento(1000)
    tempo_lento = time.time() - start
    
    start = time.time()
    resultado_rapido = algoritmo_rapido(1000)
    tempo_rapido = time.time() - start
    
    print(f"   Lento: {tempo_lento:.4f}s")
    print(f"   Rápido: {tempo_rapido:.4f}s")
    print(f"   Speedup: {tempo_lento/tempo_rapido:.2f}x")
    
    # Busca linear vs binária
    print("\\n2. Algoritmos de busca:")
    start = time.time()
    pos_linear = busca_linear(lista_grande, item_busca)
    tempo_linear = time.time() - start
    
    start = time.time()
    pos_binaria = busca_binaria(lista_grande, item_busca)
    tempo_binaria = time.time() - start
    
    print(f"   Linear: {tempo_linear:.6f}s")
    print(f"   Binária: {tempo_binaria:.6f}s")
    if tempo_linear > 0:
        print(f"   Speedup: {tempo_linear/tempo_binaria:.2f}x")

# Executar profiling
print("=== PROFILING COM cProfile ===")

# Capturar saída do profiler
profiler = cProfile.Profile()
profiler.enable()

# Código a ser analisado
testar_performance()

profiler.disable()

# Analisar resultados
stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 funções

print("\\n📊 RELATÓRIO DE PROFILING:")
print("="*50)
print(stream.getvalue())'''
        
        if self.ui:
            self.ui.code_block(codigo, "Profiling de performance")
        else:
            print("\n" + "="*50)
            print("PROFILING DE PERFORMANCE:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _medicao_tempo_memoria(self):
        """Medição de tempo e memória"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⏱️ MEDIÇÃO DE TEMPO E MEMÓRIA")
        
        print("📏 Ferramentas para medir performance:")
        print("• time.time() - tempo simples")
        print("• time.perf_counter() - alta precisão")
        print("• timeit - múltiplas execuções")
        print("• sys.getsizeof() - tamanho de objetos")
        
        codigo = '''import time
import timeit
import sys
import gc
from functools import wraps

def cronometro(func):
    """Decorator para medir tempo de execução"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        tempo = fim - inicio
        print(f"⏱️ {func.__name__} executou em {tempo:.6f} segundos")
        return resultado
    return wrapper

def medidor_memoria(func):
    """Decorator para medir uso de memória"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        gc.collect()  # Limpar garbage collector
        mem_antes = sys.getsizeof(locals())
        
        resultado = func(*args, **kwargs)
        
        mem_depois = sys.getsizeof(locals())
        print(f"💾 {func.__name__} - Memória: {mem_depois - mem_antes} bytes")
        return resultado
    return wrapper

@cronometro
@medidor_memoria
def criar_lista_comprehension(n):
    """Cria lista usando list comprehension"""
    return [i**2 for i in range(n)]

@cronometro
@medidor_memoria
def criar_lista_loop(n):
    """Cria lista usando loop tradicional"""
    resultado = []
    for i in range(n):
        resultado.append(i**2)
    return resultado

@cronometro
def ordenar_lista(lista):
    """Ordena lista usando sorted()"""
    return sorted(lista)

@cronometro
def ordenar_lista_inplace(lista):
    """Ordena lista in-place"""
    lista.sort()
    return lista

# Testes de performance
print("=== MEDIÇÃO DE TEMPO E MEMÓRIA ===")

n = 10000
print(f"\\nCriando listas com {n} elementos:")
lista1 = criar_lista_comprehension(n)
lista2 = criar_lista_loop(n)

print(f"\\nTamanhos das listas:")
print(f"Lista 1: {sys.getsizeof(lista1):,} bytes")
print(f"Lista 2: {sys.getsizeof(lista2):,} bytes")

# Comparar métodos de ordenação
import random
lista_teste = list(range(5000))
random.shuffle(lista_teste)

print(f"\\nOrdenando lista com {len(lista_teste)} elementos:")
lista_sorted = ordenar_lista(lista_teste.copy())
lista_inplace = ordenar_lista_inplace(lista_teste.copy())

# Usando timeit para medições precisas
print("\\n=== MEDIÇÕES COM TIMEIT ===")

tempo_comprehension = timeit.timeit(
    lambda: [i**2 for i in range(1000)],
    number=100
)

tempo_loop = timeit.timeit(
    lambda: [i**2 for i in range(1000) for _ in [None] if not _.append(i**2)][:1000],
    number=100
)

print(f"List comprehension (100x): {tempo_comprehension:.6f}s")
print(f"Média por execução: {tempo_comprehension/100:.8f}s")

# Análise de diferentes estruturas de dados
estruturas = {
    'lista': [1, 2, 3, 4, 5] * 1000,
    'tupla': tuple([1, 2, 3, 4, 5] * 1000),
    'set': set([1, 2, 3, 4, 5] * 200),  # Sets removem duplicatas
    'dict': {i: i**2 for i in range(1000)}
}

print("\\n=== TAMANHOS DAS ESTRUTURAS ===")
for nome, estrutura in estruturas.items():
    tamanho = sys.getsizeof(estrutura)
    print(f"{nome:10}: {tamanho:,} bytes ({len(estrutura)} elementos)")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Medição de tempo e memória")
        else:
            print("\n" + "="*50)
            print("MEDIÇÃO DE TEMPO E MEMÓRIA:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _decorators_profiling(self):
        """Decorators para profiling"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 DECORATORS PARA PROFILING")
        
        print("🧰 Decorators úteis para análise:")
        print("• @cronometro - medir tempo")
        print("• @cache - otimizar com cache")
        print("• @debug - log de entrada/saída")
        print("• @retry - tentar novamente em caso de erro")
        
        codigo = '''import time
import functools
from typing import Any, Callable
import random

def cronometro_avancado(unidade='s'):
    """Decorator configurável para cronometragem"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.perf_counter()
            resultado = func(*args, **kwargs)
            fim = time.perf_counter()
            
            tempo = fim - inicio
            if unidade == 'ms':
                tempo *= 1000
                simbolo = 'ms'
            elif unidade == 'us':
                tempo *= 1000000
                simbolo = 'μs'
            else:
                simbolo = 's'
            
            print(f"⏱️ {func.__name__}: {tempo:.3f} {simbolo}")
            return resultado
        return wrapper
    return decorator

def debug_calls(func):
    """Decorator para debug de chamadas de função"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        params = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"🔍 Chamando {func.__name__}({params})")
        
        try:
            resultado = func(*args, **kwargs)
            print(f"✅ {func.__name__} retornou: {resultado}")
            return resultado
        except Exception as e:
            print(f"❌ {func.__name__} gerou erro: {e}")
            raise
    return wrapper

def retry(max_tentativas=3, delay=1):
    """Decorator para tentar novamente em caso de erro"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentativa == max_tentativas - 1:
                        print(f"❌ Falhou após {max_tentativas} tentativas: {e}")
                        raise
                    print(f"⚠️ Tentativa {tentativa + 1} falhou: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def cache_simples(func):
    """Cache simples para funções"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Criar chave do cache
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"🎯 Cache hit para {func.__name__}")
            return cache[key]
        
        print(f"💭 Cache miss para {func.__name__}")
        resultado = func(*args, **kwargs)
        cache[key] = resultado
        return resultado
    
    return wrapper

# Exemplos de uso dos decorators

@cronometro_avancado('ms')
@debug_calls
def fibonacci_recursivo(n):
    """Fibonacci recursivo (ineficiente)"""
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

@cronometro_avancado('ms')
@cache_simples
@debug_calls
def fibonacci_com_cache(n):
    """Fibonacci com cache (eficiente)"""
    if n <= 1:
        return n
    return fibonacci_com_cache(n-1) + fibonacci_com_cache(n-2)

@retry(max_tentativas=3, delay=0.5)
@debug_calls
def operacao_instavel():
    """Simula operação que pode falhar"""
    if random.random() < 0.7:  # 70% chance de falhar
        raise Exception("Operação falhou!")
    return "Sucesso!"

# Testes
print("=== DECORATORS EM AÇÃO ===")

print("\\n1. Fibonacci sem cache (lento):")
try:
    fib_sem_cache = fibonacci_recursivo(10)
except RecursionError:
    print("❌ Recursão muito profunda!")

print("\\n2. Fibonacci com cache (rápido):")
fib_com_cache = fibonacci_com_cache(10)

print("\\n3. Operação instável com retry:")
try:
    resultado = operacao_instavel()
    print(f"🎉 {resultado}")
except Exception as e:
    print(f"💥 Falhou definitivamente: {e}")

print("\\n4. Comparação de cache:")
print("Primeira chamada:")
fibonacci_com_cache(15)
print("Segunda chamada (deve usar cache):")
fibonacci_com_cache(15)'''
        
        if self.ui:
            self.ui.code_block(codigo, "Decorators para profiling")
        else:
            print("\n" + "="*50)
            print("DECORATORS PARA PROFILING:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_profiler(self):
        """Mini projeto: Sistema de profiling completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: SISTEMA DE PROFILING COMPLETO")
        
        print("📊 Vamos criar um sistema completo de profiling!")
        print("🎯 Funcionalidades:")
        print("• Monitoramento de tempo de execução")
        print("• Análise de uso de memória")
        print("• Detecção de gargalos")
        print("• Relatórios detalhados")
        print("• Dashboard de performance")
        
        input("\n🔸 Pressione ENTER para começar o projeto...")
        
        codigo = '''import time
import sys
import functools
import threading
from collections import defaultdict, deque
from datetime import datetime
import json

class PerformanceProfiler:
    """Sistema completo de profiling de performance"""
    
    def __init__(self):
        self.stats = defaultdict(list)
        self.memory_stats = defaultdict(list)
        self.call_counts = defaultdict(int)
        self.error_counts = defaultdict(int)
        self.start_time = time.time()
        self.lock = threading.Lock()
    
    def profile_function(self, include_memory=True):
        """Decorator principal para profiling"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_name = f"{func.__module__}.{func.__name__}"
                
                # Coleta inicial
                start_time = time.perf_counter()
                start_memory = sys.getsizeof(locals()) if include_memory else 0
                
                with self.lock:
                    self.call_counts[func_name] += 1
                
                try:
                    resultado = func(*args, **kwargs)
                    
                    # Coleta final
                    end_time = time.perf_counter()
                    end_memory = sys.getsizeof(locals()) if include_memory else 0
                    
                    execution_time = end_time - start_time
                    memory_delta = end_memory - start_memory
                    
                    # Armazenar estatísticas
                    with self.lock:
                        self.stats[func_name].append({
                            'timestamp': datetime.now().isoformat(),
                            'execution_time': execution_time,
                            'args_count': len(args),
                            'kwargs_count': len(kwargs),
                            'success': True
                        })
                        
                        if include_memory:
                            self.memory_stats[func_name].append(memory_delta)
                    
                    return resultado
                    
                except Exception as e:
                    with self.lock:
                        self.error_counts[func_name] += 1
                        self.stats[func_name].append({
                            'timestamp': datetime.now().isoformat(),
                            'execution_time': time.perf_counter() - start_time,
                            'args_count': len(args),
                            'kwargs_count': len(kwargs),
                            'success': False,
                            'error': str(e)
                        })
                    raise
            
            return wrapper
        return decorator
    
    def get_function_stats(self, func_name):
        """Obter estatísticas de uma função específica"""
        if func_name not in self.stats:
            return None
        
        calls = self.stats[func_name]
        successful_calls = [c for c in calls if c['success']]
        
        if not successful_calls:
            return {
                'function': func_name,
                'total_calls': len(calls),
                'successful_calls': 0,
                'error_rate': 100.0
            }
        
        times = [c['execution_time'] for c in successful_calls]
        
        return {
            'function': func_name,
            'total_calls': len(calls),
            'successful_calls': len(successful_calls),
            'error_count': self.error_counts[func_name],
            'error_rate': (self.error_counts[func_name] / len(calls)) * 100,
            'avg_time': sum(times) / len(times),
            'min_time': min(times),
            'max_time': max(times),
            'total_time': sum(times),
            'avg_memory_delta': sum(self.memory_stats[func_name]) / len(self.memory_stats[func_name]) if self.memory_stats[func_name] else 0
        }
    
    def generate_report(self):
        """Gerar relatório completo"""
        report = {
            'profiler_uptime': time.time() - self.start_time,
            'total_functions': len(self.stats),
            'functions': {}
        }
        
        for func_name in self.stats:
            report['functions'][func_name] = self.get_function_stats(func_name)
        
        return report
    
    def print_dashboard(self):
        """Exibir dashboard no console"""
        print("\\n" + "="*80)
        print("                    DASHBOARD DE PERFORMANCE")
        print("="*80)
        
        report = self.generate_report()
        
        print(f"⏱️ Tempo de monitoramento: {report['profiler_uptime']:.2f}s")
        print(f"🔧 Funções monitoradas: {report['total_functions']}")
        
        # Top funções mais chamadas
        func_stats = [(name, stats['total_calls']) for name, stats in report['functions'].items()]
        func_stats.sort(key=lambda x: x[1], reverse=True)
        
        print("\\n🔝 TOP FUNÇÕES MAIS CHAMADAS:")
        for i, (func_name, calls) in enumerate(func_stats[:5], 1):
            stats = report['functions'][func_name]
            print(f"  {i}. {func_name.split('.')[-1]}: {calls} calls, {stats['avg_time']*1000:.2f}ms avg")
        
        # Funções mais lentas
        slow_funcs = [(name, stats['avg_time']) for name, stats in report['functions'].items() if stats['successful_calls'] > 0]
        slow_funcs.sort(key=lambda x: x[1], reverse=True)
        
        print("\\n🐌 FUNÇÕES MAIS LENTAS:")
        for i, (func_name, avg_time) in enumerate(slow_funcs[:5], 1):
            stats = report['functions'][func_name]
            print(f"  {i}. {func_name.split('.')[-1]}: {avg_time*1000:.2f}ms avg, {stats['total_calls']} calls")
        
        # Funções com erros
        error_funcs = [(name, stats['error_count']) for name, stats in report['functions'].items() if stats['error_count'] > 0]
        if error_funcs:
            error_funcs.sort(key=lambda x: x[1], reverse=True)
            print("\\n❌ FUNÇÕES COM ERROS:")
            for func_name, error_count in error_funcs:
                stats = report['functions'][func_name]
                print(f"  • {func_name.split('.')[-1]}: {error_count} erros ({stats['error_rate']:.1f}%)")
        else:
            print("\\n✅ Nenhum erro detectado!")
    
    def save_report(self, filename='performance_report.json'):
        """Salvar relatório em arquivo JSON"""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"💾 Relatório salvo em {filename}")

# Instância global do profiler
profiler = PerformanceProfiler()

# Exemplo de uso - decorar funções para monitoramento
@profiler.profile_function()
def algoritmo_ordenacao(lista):
    """Algoritmo de ordenação bubble sort"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

@profiler.profile_function()
def busca_sequencial(lista, item):
    """Busca sequencial em lista"""
    for i, elemento in enumerate(lista):
        if elemento == item:
            return i
    return -1

@profiler.profile_function()
def calcular_fibonacci(n):
    """Fibonacci iterativo"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@profiler.profile_function()
def processar_dados(dados):
    """Processamento complexo de dados"""
    resultado = []
    for item in dados:
        # Simular processamento complexo
        processado = item ** 2 + item ** 0.5
        resultado.append(processado)
    time.sleep(0.001)  # Simular I/O
    return resultado

@profiler.profile_function()
def funcao_com_erro():
    """Função que às vezes falha"""
    import random
    if random.random() < 0.3:  # 30% chance de erro
        raise ValueError("Erro simulado!")
    return "Sucesso"

# Executar testes para gerar dados
print("=== EXECUTANDO TESTES PARA PROFILING ===")

# Teste 1: Ordenação
print("\\n1. Testando algoritmos de ordenação...")
for i in range(5):
    lista_teste = list(range(100, 0, -1))  # Lista reversa
    algoritmo_ordenacao(lista_teste)

# Teste 2: Buscas
print("2. Testando buscas...")
lista_grande = list(range(1000))
for i in range(10):
    busca_sequencial(lista_grande, i * 100)

# Teste 3: Fibonacci
print("3. Testando Fibonacci...")
for i in range(10, 20):
    calcular_fibonacci(i)

# Teste 4: Processamento de dados
print("4. Testando processamento...")
for tamanho in [10, 50, 100]:
    dados = list(range(tamanho))
    processar_dados(dados)

# Teste 5: Função com erros
print("5. Testando função instável...")
for _ in range(20):
    try:
        funcao_com_erro()
    except ValueError:
        pass  # Ignorar erros esperados

# Exibir dashboard
profiler.print_dashboard()

# Salvar relatório
profiler.save_report()

print("\\n🎉 Sistema de profiling completo!")
print("💡 Este sistema pode ser expandido para:")
print("   • Monitoramento em tempo real")
print("   • Alertas de performance")
print("   • Integração com bancos de dados")
print("   • Dashboard web interativo")
print("   • Análise de tendências temporais")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Sistema de Profiling Completo")
        else:
            print("\n" + "="*50)
            print("MINI PROJETO - SISTEMA DE PROFILING:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        # Pontos do mini projeto
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            print(f"\n🎁 +{self.mini_project_points} pontos pelo mini projeto!")
        
        input("\n🔸 Pressione ENTER para finalizar o módulo...")