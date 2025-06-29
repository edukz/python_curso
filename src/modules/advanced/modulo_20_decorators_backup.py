#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 20: Decorators e Context Managers
Aprenda decorators, context managers e programação avançada
"""

from ..shared.base_module import BaseModule


class Modulo20Decorators(BaseModule):
    """Módulo 20: Decorators e Context Managers"""
    
    def __init__(self):
        super().__init__("modulo_20", "Decorators e Context Managers")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre decorators"""
        if not self.ui or not self.progress:
            self.print_warning("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._decorators()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _decorators(self) -> None:
        """Conteúdo principal sobre decorators"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎭 MÓDULO 20: DECORATORS E CONTEXT MANAGERS")
        else:
            self.print_section("🎭 MÓDULO 20: DECORATORS E CONTEXT MANAGERS")
        
        self.print_concept("🎭 Decorators são uma das funcionalidades mais PODEROSAS do Python!")
        self.print_concept("🔧 Context managers garantem limpeza automática de recursos!")
        
        self.print_section("DECORATORS - MODIFICANDO FUNÇÕES")
        
        self.print_concept("🎯 Decorator = função que modifica outra função")
        self.print_tip("✨ Usado para:")
        self.print_colored("• ⏱️  Medir tempo de execução", 'green')
        self.print_colored("• 🔐 Autenticação e autorização", 'green')
        self.print_colored("• 📝 Logs automáticos", 'green')
        self.print_colored("• 🧪 Validação de entrada", 'green')
        
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
    time.sleep(0.5)  # Reduzido para demo
    return "Operação concluída!"

print("=== TESTANDO DECORATORS ===")
print("Fibonacci de 6:")  # Reduzido para demo
resultado = calcular_fibonacci(6)
print(f"Resultado: {resultado}\\n")

print("Operação lenta:")
resultado2 = operacao_lenta()
print(f"Resultado: {resultado2}")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.print_section("🔧 Decorators com Parâmetros")
        
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
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("🏠 Context Managers")
        
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
    time.sleep(0.3)  # Reduzido para demo
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
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Para que serve a função @functools.wraps em decorators?",
            ["preserva metadados", "wraps", "metadados"],
            "Preserva nome, docstring e outros metadados da função original"
        )
        
        # Mini Projeto do Módulo 20
        self._mini_projeto_cache_inteligente()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_cache_inteligente(self) -> None:
        """Mini Projeto - Módulo 20: Sistema de Cache Inteligente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE CACHE INTELIGENTE")
        else:
            self.print_section("🎯 MINI PROJETO: SISTEMA DE CACHE INTELIGENTE")
        
        self.print_concept("💾 Sistema avançado de cache com decorators e context managers!")
        self.print_tip("🛠️ Usando: Decorators avançados, Context managers, Threading")
        
        self.pausar()
        
        codigo_projeto = '''# 💾 SISTEMA DE CACHE INTELIGENTE
# Sistema completo usando decorators e context managers

import time
import functools
import threading
from contextlib import contextmanager
from typing import Any, Dict, Optional, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class CacheStats:
    """Estatísticas do cache"""
    hits: int = 0
    misses: int = 0
    evictions: int = 0
    total_calls: int = 0
    
    def hit_rate(self) -> float:
        """Calcula taxa de acerto do cache"""
        if self.total_calls == 0:
            return 0.0
        return (self.hits / self.total_calls) * 100
    
    def __str__(self) -> str:
        return f"Cache Stats - Hits: {self.hits}, Misses: {self.misses}, Hit Rate: {self.hit_rate():.1f}%"

class TimedCache:
    """Cache com expiração por tempo (TTL)"""
    
    def __init__(self, default_ttl: int = 300, max_size: int = 1000):
        self.default_ttl = default_ttl
        self.max_size = max_size
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._stats = CacheStats()
        self._lock = threading.RLock()  # Thread-safe
    
    def _is_expired(self, entry: Dict[str, Any]) -> bool:
        """Verifica se entrada expirou"""
        return datetime.now() > entry['expires_at']
    
    def _evict_expired(self):
        """Remove entradas expiradas"""
        current_time = datetime.now()
        expired_keys = [
            key for key, entry in self._cache.items()
            if current_time > entry['expires_at']
        ]
        
        for key in expired_keys:
            del self._cache[key]
            self._stats.evictions += 1
    
    def _evict_lru(self):
        """Remove entrada menos recentemente usada"""
        if not self._cache:
            return
        
        # Encontra a entrada mais antiga
        oldest_key = min(
            self._cache.keys(),
            key=lambda k: self._cache[k]['last_accessed']
        )
        
        del self._cache[oldest_key]
        self._stats.evictions += 1
    
    def get(self, key: str) -> Optional[Any]:
        """Recupera valor do cache"""
        with self._lock:
            self._stats.total_calls += 1
            
            if key not in self._cache:
                self._stats.misses += 1
                return None
            
            entry = self._cache[key]
            
            # Verifica se expirou
            if self._is_expired(entry):
                del self._cache[key]
                self._stats.misses += 1
                self._stats.evictions += 1
                return None
            
            # Atualiza último acesso
            entry['last_accessed'] = datetime.now()
            self._stats.hits += 1
            return entry['value']
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Armazena valor no cache"""
        with self._lock:
            # Remove expirados periodicamente
            if len(self._cache) % 10 == 0:
                self._evict_expired()
            
            # Remove LRU se necessário
            while len(self._cache) >= self.max_size:
                self._evict_lru()
            
            expires_at = datetime.now() + timedelta(seconds=ttl or self.default_ttl)
            
            self._cache[key] = {
                'value': value,
                'expires_at': expires_at,
                'last_accessed': datetime.now(),
                'created_at': datetime.now()
            }
    
    def clear(self):
        """Limpa todo o cache"""
        with self._lock:
            self._cache.clear()
            self._stats = CacheStats()
    
    def stats(self) -> CacheStats:
        """Retorna estatísticas"""
        return self._stats
    
    def size(self) -> int:
        """Retorna tamanho atual do cache"""
        with self._lock:
            return len(self._cache)

# Cache global
_global_cache = TimedCache()

def cached(ttl: int = 300, cache_instance: Optional[TimedCache] = None):
    """Decorator para cache automático de funções"""
    def decorator(func: Callable) -> Callable:
        cache = cache_instance or _global_cache
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Cria chave única
            key = f"{func.__module__}.{func.__name__}:{hash((args, tuple(sorted(kwargs.items()))))}"
            
            # Tenta recuperar do cache
            result = cache.get(key)
            if result is not None:
                print(f"💾 Cache hit: {func.__name__}")
                return result
            
            # Executa função e armazena resultado
            print(f"🔄 Cache miss: {func.__name__}")
            result = func(*args, **kwargs)
            cache.set(key, result, ttl)
            
            return result
        
        # Adiciona método para limpar cache da função
        wrapper.clear_cache = lambda: cache.clear()
        wrapper.cache_stats = lambda: cache.stats()
        
        return wrapper
    return decorator

def timed_execution(func: Callable) -> Callable:
    """Decorator que mede tempo de execução"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            print(f"⏱️ {func.__name__} executou em {end_time - start_time:.4f}s")
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
                        print(f"🔄 Tentativa {attempt + 1} falhou: {e}. Tentando novamente em {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"❌ Todas as {max_attempts} tentativas falharam")
            
            raise last_exception
        return wrapper
    return decorator

@contextmanager
def cache_context(cache_instance: Optional[TimedCache] = None):
    """Context manager para cache temporário"""
    cache = cache_instance or TimedCache(ttl=60, max_size=100)
    
    print(f"🏗️ Iniciando contexto de cache (TTL: {cache.default_ttl}s)")
    try:
        yield cache
    finally:
        stats = cache.stats()
        print(f"📊 Contexto finalizado - {stats}")
        cache.clear()

@contextmanager
def performance_monitor():
    """Context manager para monitoramento de performance"""
    start_time = time.time()
    start_stats = _global_cache.stats()
    
    print("📈 Iniciando monitoramento de performance...")
    try:
        yield
    finally:
        end_time = time.time()
        end_stats = _global_cache.stats()
        
        duration = end_time - start_time
        new_calls = end_stats.total_calls - start_stats.total_calls
        new_hits = end_stats.hits - start_stats.hits
        
        print(f"📊 Performance Report:")
        print(f"   ⏱️ Duração: {duration:.4f}s")
        print(f"   📞 Chamadas: {new_calls}")
        print(f"   💾 Cache hits: {new_hits}")
        if new_calls > 0:
            hit_rate = (new_hits / new_calls) * 100
            print(f"   🎯 Hit rate: {hit_rate:.1f}%")

# FUNÇÕES DE TESTE

@cached(ttl=30)
@timed_execution
def calcular_fibonacci_cache(n: int) -> int:
    """Fibonacci com cache"""
    if n <= 1:
        return n
    return calcular_fibonacci_cache(n-1) + calcular_fibonacci_cache(n-2)

@cached(ttl=60)
@retry(max_attempts=3, delay=0.5)
@timed_execution
def operacao_instavel(falha_rate: float = 0.3) -> str:
    """Simula operação que pode falhar"""
    import random
    
    if random.random() < falha_rate:
        raise Exception("Operação falhou!")
    
    time.sleep(0.2)  # Simula processamento
    return f"Operação bem-sucedida! (falha_rate: {falha_rate})"

@cached(ttl=120)
def buscar_dados_externos(id_usuario: int) -> Dict[str, Any]:
    """Simula busca de dados externos"""
    time.sleep(0.5)  # Simula latência de rede
    return {
        "id": id_usuario,
        "nome": f"Usuário {id_usuario}",
        "dados": f"Dados complexos para {id_usuario}",
        "timestamp": datetime.now().isoformat()
    }

# DEMONSTRAÇÃO DO SISTEMA

print("=== SISTEMA DE CACHE INTELIGENTE ===")
print()

# 1. Teste básico de cache
print("🧪 TESTE 1: Cache básico")
with performance_monitor():
    print("Primeira chamada (cache miss):")
    result1 = calcular_fibonacci_cache(10)
    print(f"Fibonacci(10) = {result1}")
    
    print("\\nSegunda chamada (cache hit):")
    result2 = calcular_fibonacci_cache(10)
    print(f"Fibonacci(10) = {result2}")

print(f"\\n📊 Estatísticas globais: {_global_cache.stats()}")

# 2. Teste com context manager de cache
print("\\n🧪 TESTE 2: Context manager de cache")
with cache_context() as temp_cache:
    
    # Função temporária com cache específico
    @cached(ttl=30, cache_instance=temp_cache)
    def operacao_temporaria(x: int) -> int:
        time.sleep(0.1)
        return x ** 2
    
    print("Executando operações temporárias:")
    for i in range(3):
        result = operacao_temporaria(5)
        print(f"  {i+1}ª chamada: {result}")

# 3. Teste de retry
print("\\n🧪 TESTE 3: Sistema de retry")
try:
    resultado = operacao_instavel(falha_rate=0.7)  # Alta chance de falha
    print(f"✅ {resultado}")
except Exception as e:
    print(f"❌ Operação falhou após todas as tentativas: {e}")

# 4. Teste de dados externos
print("\\n🧪 TESTE 4: Cache de dados externos")
with performance_monitor():
    print("Buscando dados de usuários...")
    for user_id in [1, 2, 1, 3, 2]:  # IDs 1 e 2 repetidos
        dados = buscar_dados_externos(user_id)
        print(f"  Usuário {user_id}: {dados['nome']}")

# 5. Estatísticas finais
print("\\n📊 ESTATÍSTICAS FINAIS:")
print(f"Cache size: {_global_cache.size()} entradas")
print(f"Stats: {_global_cache.stats()}")

print("\\n✅ Sistema de Cache Inteligente funcionando!")
print("🎯 Funcionalidades implementadas:")
print("  • Cache com TTL (Time To Live)")
print("  • Eviction automática (LRU + expiração)")
print("  • Thread-safe com locks")
print("  • Decorators parametrizados")
print("  • Context managers customizados")
print("  • Sistema de retry")
print("  • Monitoramento de performance")
print("  • Estatísticas detalhadas")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        self.print_success("\n🏆 PARABÉNS! Sistema de cache inteligente criado!")
        self.print_tip("🎯 Aplicação real: APIs, web apps, sistemas de alta performance")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Cache Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo20Decorators()
    print("Teste do módulo 20 - versão standalone")
    module._decorators()