#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 21: Generators e Iterators
Aprenda sobre generators, iterators e processamento eficiente de dados
"""

from ..shared.base_module import BaseModule


class Modulo21Geradores(BaseModule):
    """Módulo 21: Generators e Iterators - Eficiência Máxima"""
    
    def __init__(self):
        super().__init__("modulo_21", "Generators e Iterators")
        self.has_mini_project = True
        self.mini_project_points = 95
    
    def execute(self) -> None:
        """Executa o módulo sobre generators"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._geradores()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _geradores(self) -> None:
        """Conteúdo principal sobre generators"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ MÓDULO 21: GENERATORS E ITERATORS")
        else:
            print("\n" + "="*50)
            print("⚡ MÓDULO 21: GENERATORS E ITERATORS")
            print("="*50)
        
        print("⚡ Generators são uma das funcionalidades mais EFICIENTES do Python!")
        print("🔄 Iterators permitem percorrer sequências de forma elegante!")
        
        print("\n═══════════════════════════════════════════════")
        print("        ITERATORS - PERCORRENDO SEQUÊNCIAS")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Iterator = objeto que implementa __iter__ e __next__")
        print("🔄 Protocolo de iteração:")
        print("• __iter__(): retorna o próprio iterator")
        print("• __next__(): retorna próximo item ou StopIteration")
        
        self.pausar()
        
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
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
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
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
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
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Qual palavra-chave transforma uma função em generator?",
            ["yield"],
            "A palavra-chave 'yield' torna uma função um generator"
        )
        
        # Mini Projeto do Módulo 21
        self._mini_projeto_pipeline_dados()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_pipeline_dados(self) -> None:
        """Mini Projeto - Módulo 21: Pipeline de Processamento de Dados (Generators)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: PIPELINE DE PROCESSAMENTO DE DADOS")
            print("="*50)
        
        print("🔄 Pipeline eficiente usando Generators e Iterators!")
        print("🛠️ Usando: Generators, Yield, Iterator Protocol, Memory Efficiency")
        
        self.pausar()
        
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
    def generate_sales_data(num_records: int = 100) -> Generator[Dict[str, Any], None, None]:
        """Gera dados de vendas sintéticos"""
        print(f"📊 Gerando {num_records} registros de vendas...")
        
        produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam", "Fone"]
        vendedores = ["Ana", "João", "Maria", "Carlos", "Paula"]
        regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
        
        for i in range(num_records):
            # Simula processamento gradual
            if i % 20 == 0 and i > 0:
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
            if self.metrics['records_processed'] % 20 == 0:
                print(f"   Processados {self.metrics['records_processed']} registros...")
            
            yield record
        
        # Finaliza métricas
        self.metrics['processing_time'] = time.time() - start_time
        print(f"✅ Pipeline finalizado: {self.metrics['records_processed']} registros em {self.metrics['processing_time']:.2f}s")

class DataSink:
    """Destinos para dados processados"""
    
    @staticmethod
    def to_memory_summary(data_stream: Iterator[Dict]) -> Dict[str, Any]:
        """Gera resumo dos dados na memória"""
        print("📊 Gerando resumo dos dados...")
        
        summary = {
            'total_records': 0,
            'unique_values': {},
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
dados_vendas = DataGenerator.generate_sales_data(50)

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
print("\\n💾 ETAPA 5: Análise final")
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
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Pipeline de Processamento criado!")
        print("🎯 Aplicação real: big data, ETL, processamento de streams")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Pipeline de Processamento de Dados")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo21Geradores()
    print("Teste do módulo 21 - versão standalone")
    module._geradores()