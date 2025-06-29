#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 23: Debugging e Profiling
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda técnicas avançadas de debugging de forma interativa e prática
"""

from ..shared.base_module import BaseModule
import cProfile
import pstats
import time
import sys
import functools
import traceback
import logging
import pdb
import os
import threading
import psutil
import random
from typing import Dict, List, Optional, Any, Callable, Generator
from collections import defaultdict, deque
from datetime import datetime
from io import StringIO
import json


class Modulo23Debugging(BaseModule):
    """Módulo 23: Debugging e Profiling - Encontrando e Corrigindo Problemas"""
    
    def __init__(self):
        super().__init__("modulo_23", "Debugging e Profiling")
        self.has_mini_project = True
        self.mini_project_points = 140
    
    def execute(self) -> None:
        """Executa o módulo Debugging e Profiling"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._debugging()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _debugging(self) -> None:
        """Conteúdo principal do módulo Debugging e Profiling"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐛 MÓDULO 23: DEBUGGING E PROFILING")
        else:
            print("\n" + "="*60)
            print("🐛 MÓDULO 23: DEBUGGING E PROFILING")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo do Debugging e Profiling!")
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
            self._mini_projeto_sistema_debugging_avancado()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (6 SEÇÕES) ===
        secoes = [
            {
                'id': 'secao_conceito_debugging',
                'titulo': '🎯 O que é Debugging?',
                'descricao': 'Entenda a arte de encontrar e corrigir bugs',
                'funcao': self._secao_conceito_debugging
            },
            {
                'id': 'secao_tecnicas_basicas',
                'titulo': '🔧 Técnicas Básicas de Debugging',
                'descricao': 'Métodos fundamentais para identificar problemas',
                'funcao': self._secao_tecnicas_basicas
            },
            {
                'id': 'secao_debugger_pdb',
                'titulo': '🐞 Debugger Interativo (PDB)',
                'descricao': 'Domine o debugger nativo do Python',
                'funcao': self._secao_debugger_pdb
            },
            {
                'id': 'secao_profiling_performance',
                'titulo': '⚡ Profiling de Performance',
                'descricao': 'Meça e otimize a performance do seu código',
                'funcao': self._secao_profiling_performance
            },
            {
                'id': 'secao_monitoramento_recursos',
                'titulo': '📊 Monitoramento de Recursos',
                'descricao': 'Monitore memória, CPU e outros recursos',
                'funcao': self._secao_monitoramento_recursos
            },
            {
                'id': 'secao_debugging_avancado',
                'titulo': '🚀 Debugging Avançado',
                'descricao': 'Técnicas profissionais e ferramentas avançadas',
                'funcao': self._secao_debugging_avancado
            }
        ]

        # === INTRODUÇÃO GERAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📚 GUIA DE NAVEGAÇÃO")
        else:
            print("\n" + "="*50)
            print("📚 GUIA DE NAVEGAÇÃO")
            print("="*50)

        self.print_concept("🗺️ Este módulo contém 6 seções principais sobre debugging:")
        print()
        
        for i, secao in enumerate(secoes, 1):
            self.print_colored(f"{i}. {secao['titulo']}", "cyan")
            self.print_tip(f"   {secao['descricao']}")
            print()

        self.print_warning("💡 DICA: Você pode interromper qualquer seção com Ctrl+C e voltar ao menu")
        self.print_success("🎮 Vamos começar! Pressione ENTER em cada seção para avançar no seu ritmo")
        
        try:
            input("\n🚀 Pressione ENTER para começar a jornada...")
        except KeyboardInterrupt:
            raise

        # === EXECUÇÃO DAS SEÇÕES ===
        secoes_completadas = 0
        
        for i, secao in enumerate(secoes, 1):
            try:
                # Cabeçalho da seção
                if self.ui:
                    self.ui.clear_screen()
                    self.ui.header(f"SEÇÃO {i}/6: {secao['titulo']}")
                else:
                    print(f"\n{'='*60}")
                    print(f"SEÇÃO {i}/6: {secao['titulo']}")
                    print('='*60)
                
                self.print_concept(f"📖 {secao['descricao']}")
                
                # Progresso visual
                progresso = "🟢" * secoes_completadas + "⚪" * (len(secoes) - secoes_completadas)
                self.print_tip(f"Progresso: {progresso} ({secoes_completadas}/{len(secoes)} concluídas)")
                
                try:
                    input(f"\n▶️ Pressione ENTER para começar: {secao['titulo']}")
                except KeyboardInterrupt:
                    raise
                
                # Executar seção
                secao['funcao']()
                secoes_completadas += 1
                
                # Feedback de conclusão
                if secoes_completadas < len(secoes):
                    self.print_success(f"✅ Seção {i} concluída! Preparando próxima seção...")
                    try:
                        input("\n⏭️ Pressione ENTER para continuar para a próxima seção...")
                    except KeyboardInterrupt:
                        raise
                        
            except KeyboardInterrupt:
                self.print_warning(f"\n\n⚠️ Seção '{secao['titulo']}' interrompida pelo usuário")
                raise

        # === CONCLUSÃO DAS SEÇÕES ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎊 SEÇÕES CONCLUÍDAS!")
        else:
            print("\n" + "="*50)
            print("🎊 SEÇÕES CONCLUÍDAS!")
            print("="*50)

        self.print_success("🎉 Parabéns! Você concluiu todas as 6 seções sobre debugging!")
        self.print_concept("🧠 Agora você conhece:")
        self.print_tip("✅ Conceitos fundamentais de debugging")
        self.print_tip("✅ Técnicas básicas e avançadas")
        self.print_tip("✅ Uso do debugger PDB")
        self.print_tip("✅ Profiling de performance")
        self.print_tip("✅ Monitoramento de recursos")
        self.print_tip("✅ Debugging avançado")
        
        try:
            input("\n🎯 Pressione ENTER para continuar para a seção de prática...")
        except KeyboardInterrupt:
            raise

    def _show_help(self) -> None:
        """Mostra ajuda sobre navegação e controles"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("❓ SISTEMA DE AJUDA")
        else:
            print("\n" + "="*40)
            print("❓ SISTEMA DE AJUDA")
            print("="*40)

        self.print_concept("🗺️ NAVEGAÇÃO:")
        self.print_tip("• Use ENTER para avançar entre seções")
        self.print_tip("• Pressione Ctrl+C para voltar ao menu principal")
        self.print_tip("• Cada seção tem exemplos interativos")

        self.print_concept("\n🎯 ESTRUTURA DO MÓDULO:")
        self.print_tip("• 6 seções conceituais")
        self.print_tip("• Seção de prática com exercícios")
        self.print_tip("• Mini projeto final")

        self.print_concept("\n💡 DICAS:")
        self.print_tip("• Pratique os exemplos de código")
        self.print_tip("• Teste os comandos do debugger")
        self.print_tip("• Experimente as ferramentas de profiling")

        try:
            input("\n📚 Pressione ENTER para voltar...")
        except KeyboardInterrupt:
            pass

    def _secao_conceito_debugging(self) -> None:
        """Seção 1: O que é Debugging?"""
        
        self.print_concept("🎯 DEBUGGING é a arte de encontrar e corrigir bugs no código")
        self.print_tip("🐛 Bug = comportamento inesperado ou incorreto do programa")
        
        self.print_colored("\n💡 Tipos de bugs mais comuns:", "cyan")
        self.print_tip("🔹 Erros de sintaxe (SyntaxError)")
        self.print_tip("🔹 Erros de lógica (comportamento incorreto)")
        self.print_tip("🔹 Erros de runtime (exceções durante execução)")
        self.print_tip("🔹 Erros de performance (código lento)")
        self.print_tip("🔹 Vazamentos de memória")
        
        try:
            input("\n▶️ Pressione ENTER para ver exemplos práticos...")
        except KeyboardInterrupt:
            raise

        codigo_exemplo = '''# 🐛 EXEMPLOS DE BUGS COMUNS

print("=== EXEMPLO 1: Bug de Lógica ===")

def calcular_media_bugada(numeros):
    """Função com bug de lógica"""
    total = 0
    for numero in numeros:
        total += numero
    # BUG: Divisão por zero não tratada!
    return total / len(numeros)

# Teste que funciona
print("Média de [1,2,3,4,5]:", calcular_media_bugada([1,2,3,4,5]))

# Teste que quebra
try:
    print("Média de lista vazia:", calcular_media_bugada([]))
except ZeroDivisionError as e:
    print(f"❌ Bug encontrado: {e}")

print("\\n=== EXEMPLO 2: Bug de Índice ===")

def buscar_elemento_bugado(lista, indice):
    """Função com bug de índice"""
    # BUG: Não verifica se índice é válido!
    return lista[indice]

dados = [10, 20, 30]
print("Elemento no índice 1:", buscar_elemento_bugado(dados, 1))

try:
    print("Elemento no índice 10:", buscar_elemento_bugado(dados, 10))
except IndexError as e:
    print(f"❌ Bug encontrado: {e}")

print("\\n=== EXEMPLO 3: Bug de Performance ===")

def fibonacci_lento(n):
    """Versão ineficiente do Fibonacci"""
    if n <= 1:
        return n
    # BUG: Algoritmo exponencial muito lento!
    return fibonacci_lento(n-1) + fibonacci_lento(n-2)

import time

print("Calculando Fibonacci(30) - versão lenta...")
inicio = time.time()
resultado = fibonacci_lento(30)
fim = time.time()
print(f"Resultado: {resultado}")
print(f"⏱️ Tempo: {fim - inicio:.4f} segundos (muito lento!)")

print("\\n=== VERSÃO CORRIGIDA ===")

def fibonacci_rapido(n, memo={}):
    """Versão otimizada com memoização"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_rapido(n-1, memo) + fibonacci_rapido(n-2, memo)
    return memo[n]

print("Calculando Fibonacci(30) - versão rápida...")
inicio = time.time()
resultado = fibonacci_rapido(30)
fim = time.time()
print(f"Resultado: {resultado}")
print(f"⏱️ Tempo: {fim - inicio:.6f} segundos (super rápido!)")'''

        self.exemplo_interativo(codigo_exemplo, "Exemplos de Bugs Comuns")
        
        self.print_success("\n🎯 PROCESSO DE DEBUGGING:")
        self.print_tip("1️⃣ Identificar que existe um problema")
        self.print_tip("2️⃣ Reproduzir o problema consistentemente")
        self.print_tip("3️⃣ Isolar a causa do problema")
        self.print_tip("4️⃣ Formular hipótese sobre a causa")
        self.print_tip("5️⃣ Testar a hipótese")
        self.print_tip("6️⃣ Corrigir o problema")
        self.print_tip("7️⃣ Verificar que a correção funciona")
        
        try:
            input("\n✅ Seção 1 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_tecnicas_basicas(self) -> None:
        """Seção 2: Técnicas Básicas de Debugging"""
        
        self.print_concept("🔧 TÉCNICAS FUNDAMENTAIS para encontrar bugs")
        
        self.print_colored("\n🔍 1. PRINT DEBUGGING", "yellow")
        self.print_tip("Técnica mais simples: adicionar prints para ver valores")
        
        codigo_print = '''# 🖨️ PRINT DEBUGGING - Técnica básica mas eficaz

def calcular_desconto(preco, percentual):
    """Calcula desconto com debugging"""
    print(f"🔍 DEBUG: preco={preco}, percentual={percentual}")
    
    desconto = preco * percentual / 100
    print(f"🔍 DEBUG: desconto calculado={desconto}")
    
    preco_final = preco - desconto
    print(f"🔍 DEBUG: preco_final={preco_final}")
    
    return preco_final

# Teste
produto_preco = 100
produto_desconto = 15
resultado = calcular_desconto(produto_preco, produto_desconto)
print(f"\\n✅ Preço com desconto: R$ {resultado:.2f}")

print("\\n" + "="*50)
print("🔧 DEBUGGING COM LOGGING - Mais profissional")

import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def processar_pedido(itens):
    """Processa pedido com logging"""
    logging.info(f"Iniciando processamento de {len(itens)} itens")
    
    total = 0
    for i, item in enumerate(itens):
        logging.debug(f"Processando item {i+1}: {item}")
        
        preco = item.get('preco', 0)
        quantidade = item.get('quantidade', 1)
        
        logging.debug(f"  Preço: {preco}, Quantidade: {quantidade}")
        
        subtotal = preco * quantidade
        total += subtotal
        
        logging.debug(f"  Subtotal: {subtotal}, Total acumulado: {total}")
    
    logging.info(f"Processamento concluído. Total: R$ {total:.2f}")
    return total

# Teste com logging
pedido = [
    {'nome': 'Produto A', 'preco': 25.50, 'quantidade': 2},
    {'nome': 'Produto B', 'preco': 15.00, 'quantidade': 1},
    {'nome': 'Produto C', 'preco': 45.99, 'quantidade': 3}
]

total_pedido = processar_pedido(pedido)
print(f"\\n🛒 Total do pedido: R$ {total_pedido:.2f}")'''

        self.exemplo_interativo(codigo_print, "Print Debugging e Logging")
        
        try:
            input("\n▶️ Pressione ENTER para ver mais técnicas...")
        except KeyboardInterrupt:
            raise

        self.print_colored("\n🧪 2. ASSERT STATEMENTS", "yellow")
        self.print_tip("Verificações automáticas para validar suposições")
        
        codigo_assert = '''# ✅ ASSERT DEBUGGING - Verificações automáticas

def dividir_numeros(a, b):
    """Divisão com verificações assert"""
    # Verificar tipos
    assert isinstance(a, (int, float)), f"'a' deve ser número, recebido {type(a)}"
    assert isinstance(b, (int, float)), f"'b' deve ser número, recebido {type(b)}"
    
    # Verificar divisão por zero
    assert b != 0, "Divisão por zero não é permitida"
    
    resultado = a / b
    
    # Verificar se resultado é válido
    assert not (resultado != resultado), "Resultado é NaN"  # Verifica NaN
    
    return resultado

print("=== TESTES COM ASSERT ===")

# Teste válido
try:
    resultado = dividir_numeros(10, 2)
    print(f"✅ 10 / 2 = {resultado}")
except AssertionError as e:
    print(f"❌ Erro: {e}")

# Teste com divisão por zero
try:
    resultado = dividir_numeros(10, 0)
    print(f"✅ 10 / 0 = {resultado}")
except AssertionError as e:
    print(f"❌ Erro capturado: {e}")

# Teste com tipo inválido
try:
    resultado = dividir_numeros("10", 2)
    print(f"✅ '10' / 2 = {resultado}")
except AssertionError as e:
    print(f"❌ Erro capturado: {e}")

print("\\n🔧 ASSERT em estruturas de dados:")

def processar_lista_numeros(numeros):
    """Processa lista com validações"""
    assert isinstance(numeros, list), "Entrada deve ser uma lista"
    assert len(numeros) > 0, "Lista não pode estar vazia"
    assert all(isinstance(n, (int, float)) for n in numeros), "Todos elementos devem ser números"
    
    # Processamento
    media = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return {
        'media': media,
        'maximo': maximo,
        'minimo': minimo,
        'total': len(numeros)
    }

# Testes
listas_teste = [
    [1, 2, 3, 4, 5],           # Válida
    [],                         # Vazia (erro)
    "não é lista",             # Tipo errado (erro)
    [1, 2, "três", 4]          # Elemento inválido (erro)
]

for i, lista in enumerate(listas_teste):
    try:
        resultado = processar_lista_numeros(lista)
        print(f"✅ Lista {i+1}: {resultado}")
    except AssertionError as e:
        print(f"❌ Lista {i+1} falhou: {e}")'''

        self.exemplo_interativo(codigo_assert, "Assert Statements")
        
        self.print_colored("\n🎯 3. DIVIDE E CONQUISTE", "yellow")
        self.print_tip("Isole partes do código para encontrar onde está o problema")
        
        codigo_divide = '''# 🔍 DIVIDE E CONQUISTE - Isolando problemas

def sistema_complexo_bugado():
    """Sistema com múltiplas operações - onde está o bug?"""
    
    # Etapa 1: Carregar dados
    print("📊 Carregando dados...")
    dados = carregar_dados()
    print(f"   Dados carregados: {len(dados)} registros")
    
    # Etapa 2: Processar dados
    print("⚙️ Processando dados...")
    dados_processados = processar_dados(dados)
    print(f"   Dados processados: {len(dados_processados)} registros")
    
    # Etapa 3: Calcular resultados
    print("🧮 Calculando resultados...")
    resultados = calcular_resultados(dados_processados)
    print(f"   Resultados: {resultados}")
    
    # Etapa 4: Gerar relatório
    print("📋 Gerando relatório...")
    relatorio = gerar_relatorio(resultados)
    print(f"   Relatório gerado: {len(relatorio)} linhas")
    
    return relatorio

def carregar_dados():
    """Simula carregamento de dados"""
    return [
        {'id': 1, 'valor': 100, 'tipo': 'A'},
        {'id': 2, 'valor': 200, 'tipo': 'B'},
        {'id': 3, 'valor': 150, 'tipo': 'A'},
        {'id': 4, 'valor': 300, 'tipo': 'C'},
        {'id': 5, 'valor': None, 'tipo': 'B'}  # 🐛 Dado problemático!
    ]

def processar_dados(dados):
    """Processa dados - BUG AQUI!"""
    processados = []
    for item in dados:
        # 🐛 BUG: Não verifica se valor é None
        item_processado = {
            'id': item['id'],
            'valor_dobrado': item['valor'] * 2,  # Falha se valor é None!
            'tipo': item['tipo']
        }
        processados.append(item_processado)
    return processados

def calcular_resultados(dados_processados):
    """Calcula resultados"""
    total = sum(item['valor_dobrado'] for item in dados_processados)
    media = total / len(dados_processados)
    return {'total': total, 'media': media}

def gerar_relatorio(resultados):
    """Gera relatório"""
    linhas = [
        f"Total: {resultados['total']:.2f}",
        f"Média: {resultados['media']:.2f}"
    ]
    return linhas

print("=== EXECUTANDO SISTEMA COMPLEXO ===")
try:
    relatorio = sistema_complexo_bugado()
    print("✅ Sistema executado com sucesso!")
    for linha in relatorio:
        print(f"  {linha}")
except Exception as e:
    print(f"❌ Erro no sistema: {e}")
    print(f"   Tipo do erro: {type(e).__name__}")

print("\\n=== VERSÃO CORRIGIDA ===")

def processar_dados_corrigido(dados):
    """Versão corrigida com validação"""
    processados = []
    for item in dados:
        # ✅ CORREÇÃO: Verificar se valor é válido
        if item['valor'] is None:
            print(f"⚠️ Aviso: Item {item['id']} tem valor None, usando 0")
            valor = 0
        else:
            valor = item['valor']
        
        item_processado = {
            'id': item['id'],
            'valor_dobrado': valor * 2,
            'tipo': item['tipo']
        }
        processados.append(item_processado)
    return processados

def sistema_complexo_corrigido():
    """Versão corrigida do sistema"""
    dados = carregar_dados()
    dados_processados = processar_dados_corrigido(dados)  # Usando versão corrigida
    resultados = calcular_resultados(dados_processados)
    relatorio = gerar_relatorio(resultados)
    return relatorio

print("Executando versão corrigida...")
try:
    relatorio = sistema_complexo_corrigido()
    print("✅ Sistema corrigido executado com sucesso!")
    for linha in relatorio:
        print(f"  {linha}")
except Exception as e:
    print(f"❌ Erro: {e}")'''

        self.exemplo_interativo(codigo_divide, "Divide e Conquiste")
        
        try:
            input("\n✅ Seção 2 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_debugger_pdb(self) -> None:
        """Seção 3: Debugger Interativo (PDB)"""
        
        self.print_concept("🐞 PDB é o debugger interativo nativo do Python")
        self.print_tip("🎯 Permite pausar a execução e inspecionar variáveis em tempo real")
        
        self.print_colored("\n📋 COMANDOS PRINCIPAIS DO PDB:", "cyan")
        self.print_tip("• n (next) - executa próxima linha")
        self.print_tip("• s (step) - entra dentro de funções")
        self.print_tip("• c (continue) - continua execução")
        self.print_tip("• l (list) - mostra código atual")
        self.print_tip("• p <variável> - mostra valor de variável")
        self.print_tip("• pp <variável> - pretty print de variável")
        self.print_tip("• w (where) - mostra stack trace")
        self.print_tip("• q (quit) - sair do debugger")
        
        try:
            input("\n▶️ Pressione ENTER para ver exemplos do PDB...")
        except KeyboardInterrupt:
            raise

        codigo_pdb = '''# 🐞 DEBUGGER PDB - Debugging interativo

import pdb

def fibonacci_com_debug(n):
    """Fibonacci com pontos de debug"""
    print(f"🔍 Calculando fibonacci({n})")
    
    # Breakpoint condicional
    if n > 10:
        print("🛑 Número grande detectado - ativando debugger")
        # pdb.set_trace()  # Descomentaria para debugar
    
    if n <= 1:
        resultado = n
    else:
        print(f"  Calculando fibonacci({n-1}) + fibonacci({n-2})")
        resultado = fibonacci_com_debug(n-1) + fibonacci_com_debug(n-2)
    
    print(f"  fibonacci({n}) = {resultado}")
    return resultado

def debug_lista_operacoes():
    """Demonstra debugging de operações em lista"""
    numeros = [1, 5, 3, 8, 2, 7, 4, 6]
    print(f"Lista original: {numeros}")
    
    # Ponto de debug antes do processamento
    # pdb.set_trace()  # Pausaria aqui para inspecionar
    
    # Operações que podem ter bugs
    pares = []
    impares = []
    
    for i, numero in enumerate(numeros):
        print(f"  Processando índice {i}: {numero}")
        
        # Breakpoint condicional
        if numero > 5:
            print(f"    🔍 Número alto encontrado: {numero}")
            # pdb.set_trace()  # Pausaria para números > 5
        
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    
    return pares, impares

print("=== EXEMPLO DE DEBUGGING COM PDB ===")
print()

# Exemplo sem pausar (para demonstração)
print("1. Fibonacci pequeno:")
resultado = fibonacci_com_debug(5)
print(f"Resultado: {resultado}")

print("\\n2. Operações em lista:")
pares, impares = debug_lista_operacoes()

print("\\n💡 COMO USAR O PDB:")
print("1. Descomente as linhas 'pdb.set_trace()'")
print("2. Execute o código")
print("3. Quando pausar, use os comandos:")
print("   - 'l' para ver código")
print("   - 'p variável' para ver valores")
print("   - 'n' para próxima linha")
print("   - 'c' para continuar")
print("   - 'q' para sair")

print("\\n🔧 DEBUGGING AVANÇADO COM BREAKPOINTS:")

def funcao_com_bug_complexo(dados):
    """Função com lógica complexa para debugar"""
    resultado = {}
    
    for categoria, items in dados.items():
        print(f"Processando categoria: {categoria}")
        
        # Breakpoint para categoria específica
        if categoria == "problematica":
            print("🚨 Categoria problemática detectada!")
            # pdb.set_trace()  # Pausaria aqui
        
        total = 0
        count = 0
        
        for item in items:
            # Verificar se item é válido
            if isinstance(item, dict) and 'valor' in item:
                valor = item['valor']
                if isinstance(valor, (int, float)) and valor > 0:
                    total += valor
                    count += 1
                else:
                    print(f"  ⚠️ Valor inválido ignorado: {valor}")
            else:
                print(f"  ⚠️ Item inválido ignorado: {item}")
        
        if count > 0:
            media = total / count
            resultado[categoria] = {
                'total': total,
                'count': count,
                'media': media
            }
        else:
            print(f"  ❌ Nenhum item válido em {categoria}")
            resultado[categoria] = None
    
    return resultado

# Dados de teste com problemas
dados_teste = {
    'valida': [
        {'valor': 100},
        {'valor': 200},
        {'valor': 150}
    ],
    'problematica': [
        {'valor': 50},
        {'valor': -10},    # Valor negativo
        {'valor': None},   # Valor None
        {'nome': 'sem valor'},  # Sem campo valor
        300                # Não é dict
    ],
    'vazia': []
}

print("\\n3. Debugging de função complexa:")
resultado = funcao_com_bug_complexo(dados_teste)

print("\\nResultado final:")
for categoria, stats in resultado.items():
    if stats:
        print(f"  {categoria}: Total={stats['total']}, Média={stats['media']:.2f}")
    else:
        print(f"  {categoria}: Sem dados válidos")'''

        self.exemplo_interativo(codigo_pdb, "Debugger PDB")
        
        self.print_colored("\n🎯 DICAS AVANÇADAS DO PDB:", "yellow")
        self.print_tip("💡 Use breakpoints condicionais para problemas específicos")
        self.print_tip("💡 Combine 'l' + 'p' para ver código e valores")
        self.print_tip("💡 Use 'w' para entender a stack de chamadas")
        self.print_tip("💡 Experimente 'pp' para objetos complexos")
        
        try:
            input("\n✅ Seção 3 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_profiling_performance(self) -> None:
        """Seção 4: Profiling de Performance"""
        
        self.print_concept("⚡ PROFILING é a medição detalhada de performance do código")
        self.print_tip("📊 Identifica gargalos e otimiza o código onde realmente importa")
        
        self.print_colored("\n🔧 Ferramentas de Profiling:", "cyan")
        self.print_tip("🔹 cProfile - profiler nativo do Python")
        self.print_tip("🔹 timeit - medição precisa de pequenos trechos")
        self.print_tip("🔹 line_profiler - profiling linha por linha")
        self.print_tip("🔹 memory_profiler - monitoramento de memória")
        
        try:
            input("\n▶️ Pressione ENTER para ver profiling em ação...")
        except KeyboardInterrupt:
            raise

        codigo_profiling = '''# ⚡ PROFILING DE PERFORMANCE

import cProfile
import pstats
import time
import timeit
from io import StringIO

def algoritmo_lento(n):
    """Algoritmo ineficiente para demonstração"""
    resultado = 0
    for i in range(n):
        for j in range(1000):  # Loop desnecessário
            resultado += i * j
    return resultado

def algoritmo_rapido(n):
    """Versão otimizada"""
    return sum(i * sum(range(1000)) for i in range(n))

def ordenacao_bubble(lista):
    """Bubble sort - O(n²)"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenacao_rapida(lista):
    """Usando sorted() built-in"""
    return sorted(lista)

print("=== PROFILING COM cProfile ===")

# Executar profiling
profiler = cProfile.Profile()
profiler.enable()

# Código a ser analisado
lista_teste = list(range(1000, 0, -1))  # Lista reversa
resultado_lento = algoritmo_lento(500)
lista_ordenada = ordenacao_bubble(lista_teste.copy())

profiler.disable()

# Analisar resultados
stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(10)

print("📊 RELATÓRIO DE PROFILING:")
print("="*50)
output = stream.getvalue()
print(output[:1000] + "..." if len(output) > 1000 else output)

print("\\n=== COMPARAÇÃO DE PERFORMANCE ===")

# Medição com timeit
tempo_lento = timeit.timeit(
    lambda: algoritmo_lento(100), 
    number=5
)

tempo_rapido = timeit.timeit(
    lambda: algoritmo_rapido(100), 
    number=5
)

print(f"Algoritmo lento (5x): {tempo_lento:.4f}s")
print(f"Algoritmo rápido (5x): {tempo_rapido:.4f}s")
print(f"Speedup: {tempo_lento/tempo_rapido:.2f}x mais rápido")

# Comparação de ordenação
import random
lista_grande = list(range(5000))
random.shuffle(lista_grande)

print(f"\\nTestando ordenação de {len(lista_grande)} elementos:")

tempo_bubble = timeit.timeit(
    lambda: ordenacao_bubble(lista_grande.copy()), 
    number=1
)

tempo_builtin = timeit.timeit(
    lambda: ordenacao_rapida(lista_grande.copy()), 
    number=100
) / 100  # Média de 100 execuções

print(f"Bubble sort: {tempo_bubble:.4f}s")
print(f"Sorted built-in: {tempo_builtin:.6f}s")
print(f"Speedup: {tempo_bubble/tempo_builtin:.0f}x mais rápido")

print("\\n🎯 DICAS DE PROFILING:")
print("• Use cProfile para visão geral")
print("• Use timeit para comparações precisas")
print("• Foque nas funções que consomem mais tempo")
print("• Otimize apenas depois de medir!")'''

        self.exemplo_interativo(codigo_profiling, "Profiling de Performance")
        
        try:
            input("\n✅ Seção 4 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_monitoramento_recursos(self) -> None:
        """Seção 5: Monitoramento de Recursos"""
        
        self.print_concept("📊 MONITORAMENTO permite acompanhar uso de CPU, memória e I/O")
        self.print_tip("⚠️ Essencial para identificar vazamentos e gargalos de recursos")
        
        try:
            input("\n▶️ Pressione ENTER para ver monitoramento em ação...")
        except KeyboardInterrupt:
            raise

        codigo_monitoramento = '''# 📊 MONITORAMENTO DE RECURSOS

import sys
import time
import threading
from collections import deque
import gc

# Simular psutil se não disponível
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("⚠️ psutil não disponível - usando alternativas básicas")

def medir_memoria_basico():
    """Medição básica de memória usando sys"""
    return sys.getsizeof

def monitorar_memoria_funcao(func):
    """Decorator para monitorar uso de memória"""
    def wrapper(*args, **kwargs):
        # Forçar garbage collection
        gc.collect()
        
        # Medição inicial básica
        mem_antes = sum(sys.getsizeof(obj) for obj in gc.get_objects())
        
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        
        # Medição final
        gc.collect()
        mem_depois = sum(sys.getsizeof(obj) for obj in gc.get_objects())
        
        delta_mem = mem_depois - mem_antes
        tempo_exec = end_time - start_time
        
        print(f"📊 {func.__name__}:")
        print(f"   ⏱️ Tempo: {tempo_exec:.4f}s")
        print(f"   💾 Δ Memória: {delta_mem:,} bytes")
        
        return resultado
    return wrapper

class MonitorRecursos:
    """Monitor simples de recursos"""
    
    def __init__(self):
        self.historico_memoria = deque(maxlen=100)
        self.historico_tempo = deque(maxlen=100)
        self.monitorando = False
        self.thread_monitor = None
    
    def iniciar_monitoramento(self, intervalo=1.0):
        """Inicia monitoramento contínuo"""
        if self.monitorando:
            return
        
        self.monitorando = True
        self.thread_monitor = threading.Thread(
            target=self._loop_monitoramento, 
            args=(intervalo,)
        )
        self.thread_monitor.daemon = True
        self.thread_monitor.start()
        print(f"📈 Monitoramento iniciado (intervalo: {intervalo}s)")
    
    def parar_monitoramento(self):
        """Para monitoramento"""
        self.monitorando = False
        if self.thread_monitor:
            self.thread_monitor.join(timeout=2)
        print("📉 Monitoramento parado")
    
    def _loop_monitoramento(self, intervalo):
        """Loop de monitoramento"""
        while self.monitorando:
            timestamp = time.time()
            
            # Memória básica
            num_objetos = len(gc.get_objects())
            memoria_aprox = sum(sys.getsizeof(obj) for obj in gc.get_objects()[:1000])
            
            self.historico_tempo.append(timestamp)
            self.historico_memoria.append(memoria_aprox)
            
            time.sleep(intervalo)
    
    def relatorio(self):
        """Gera relatório de recursos"""
        if not self.historico_memoria:
            print("❌ Nenhum dado de monitoramento disponível")
            return
        
        mem_min = min(self.historico_memoria)
        mem_max = max(self.historico_memoria)
        mem_media = sum(self.historico_memoria) / len(self.historico_memoria)
        
        print("📊 RELATÓRIO DE RECURSOS:")
        print(f"   📝 Amostras coletadas: {len(self.historico_memoria)}")
        print(f"   💾 Memória mín: {mem_min:,} bytes")
        print(f"   💾 Memória máx: {mem_max:,} bytes")
        print(f"   💾 Memória média: {mem_media:,.0f} bytes")
        print(f"   📈 Variação: {mem_max - mem_min:,} bytes")

# Funções de teste para monitoramento
@monitorar_memoria_funcao
def criar_lista_grande():
    """Cria lista que consome memória"""
    lista = []
    for i in range(100000):
        lista.append(f"item_{i}")
    return lista

@monitorar_memoria_funcao
def processar_dados_memoria():
    """Processamento que usa memória temporária"""
    dados = {}
    for i in range(10000):
        dados[f"chave_{i}"] = {
            'valor': i * 2,
            'texto': f"texto_longo_para_item_{i}" * 10,
            'lista': list(range(i % 100))
        }
    
    # Processamento
    resultado = []
    for chave, valor in dados.items():
        resultado.append(valor['valor'] * 2)
    
    return sum(resultado)

def vazamento_memoria_simulado():
    """Simula vazamento de memória"""
    vazamento = []
    for i in range(50000):
        vazamento.append([0] * 1000)  # Listas que "vazam"
    return len(vazamento)

print("=== MONITORAMENTO DE RECURSOS ===")

# Teste 1: Monitoramento de função
print("\\n1. Testando funções com monitoramento:")
lista = criar_lista_grande()
print(f"   Lista criada com {len(lista)} elementos")

resultado = processar_dados_memoria()
print(f"   Resultado do processamento: {resultado}")

# Teste 2: Monitor contínuo
print("\\n2. Monitor contínuo de recursos:")
monitor = MonitorRecursos()

try:
    monitor.iniciar_monitoramento(0.5)
    
    print("   Executando operações monitoradas...")
    time.sleep(1)
    
    # Operação que consome memória
    print("   Criando dados temporários...")
    temp_data = vazamento_memoria_simulado()
    print(f"   Vazamento simulado: {temp_data} listas criadas")
    
    time.sleep(1)
    
    # Limpar memória
    del temp_data
    gc.collect()
    print("   Memória limpa")
    
    time.sleep(1)
    
finally:
    monitor.parar_monitoramento()

monitor.relatorio()

print("\\n💡 DICAS DE MONITORAMENTO:")
print("• Use psutil para monitoramento completo do sistema")
print("• Monitore continuamente em produção")
print("• Observe padrões de crescimento de memória")
print("• Configure alertas para limites de recursos")

if PSUTIL_AVAILABLE:
    print("\\n🔧 Informações do sistema (psutil):")
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        print(f"   🖥️ CPU: {cpu_percent}%")
        print(f"   💾 Memória: {memoria.percent}% ({memoria.used/1024/1024/1024:.1f}GB/{memoria.total/1024/1024/1024:.1f}GB)")
    except:
        print("   ❌ Erro ao obter informações do sistema")'''

        self.exemplo_interativo(codigo_monitoramento, "Monitoramento de Recursos")
        
        try:
            input("\n✅ Seção 5 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_debugging_avancado(self) -> None:
        """Seção 6: Debugging Avançado"""
        
        self.print_concept("🚀 DEBUGGING AVANÇADO combina múltiplas técnicas para problemas complexos")
        self.print_tip("🎯 Estratégias profissionais para bugs difíceis de reproduzir")
        
        try:
            input("\n▶️ Pressione ENTER para ver técnicas avançadas...")
        except KeyboardInterrupt:
            raise

        codigo_avancado = '''# 🚀 DEBUGGING AVANÇADO - Técnicas profissionais

import functools
import traceback
import logging
import time
import threading
from datetime import datetime
from collections import defaultdict, deque
import json

# Configurar logging avançado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class DebugProfiler:
    """Profiler avançado para debugging"""
    
    def __init__(self):
        self.call_stack = []
        self.performance_data = defaultdict(list)
        self.error_log = []
        self.call_count = defaultdict(int)
    
    def debug_function(self, include_args=True, track_performance=True):
        """Decorator avançado para debugging"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_name = f"{func.__module__}.{func.__name__}"
                
                # Incrementar contador
                self.call_count[func_name] += 1
                call_id = self.call_count[func_name]
                
                # Preparar informações de entrada
                entrada_info = {
                    'function': func_name,
                    'call_id': call_id,
                    'timestamp': datetime.now().isoformat(),
                    'thread_id': threading.get_ident()
                }
                
                if include_args:
                    entrada_info['args'] = str(args)[:200]  # Limitar tamanho
                    entrada_info['kwargs'] = str(kwargs)[:200]
                
                # Adicionar à pilha de chamadas
                self.call_stack.append(entrada_info)
                
                start_time = time.time()
                
                try:
                    logging.debug(f"🔍 ENTRADA {func_name} (#{call_id})")
                    resultado = func(*args, **kwargs)
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    
                    # Registrar performance
                    if track_performance:
                        self.performance_data[func_name].append(execution_time)
                    
                    logging.debug(f"✅ SAÍDA {func_name} (#{call_id}) - {execution_time:.4f}s")
                    
                    return resultado
                    
                except Exception as e:
                    end_time = time.time()
                    execution_time = end_time - start_time
                    
                    # Registrar erro
                    error_info = {
                        'function': func_name,
                        'call_id': call_id,
                        'error': str(e),
                        'error_type': type(e).__name__,
                        'execution_time': execution_time,
                        'timestamp': datetime.now().isoformat(),
                        'traceback': traceback.format_exc()
                    }
                    
                    self.error_log.append(error_info)
                    
                    logging.error(f"❌ ERRO {func_name} (#{call_id}): {e}")
                    raise
                    
                finally:
                    # Remover da pilha
                    if self.call_stack:
                        self.call_stack.pop()
            
            return wrapper
        return decorator
    
    def get_call_stack(self):
        """Retorna pilha atual de chamadas"""
        return self.call_stack.copy()
    
    def get_performance_summary(self):
        """Resumo de performance"""
        summary = {}
        for func_name, times in self.performance_data.items():
            if times:
                summary[func_name] = {
                    'calls': len(times),
                    'total_time': sum(times),
                    'avg_time': sum(times) / len(times),
                    'min_time': min(times),
                    'max_time': max(times)
                }
        return summary
    
    def get_error_summary(self):
        """Resumo de erros"""
        error_counts = defaultdict(int)
        for error in self.error_log:
            error_counts[error['error_type']] += 1
        
        return {
            'total_errors': len(self.error_log),
            'error_types': dict(error_counts),
            'recent_errors': self.error_log[-5:] if self.error_log else []
        }
    
    def export_debug_data(self, filename='debug_report.json'):
        """Exporta dados de debugging"""
        data = {
            'performance': self.get_performance_summary(),
            'errors': self.get_error_summary(),
            'call_counts': dict(self.call_count),
            'export_time': datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Relatório de debug exportado para {filename}")

# Instância global do profiler
debug_profiler = DebugProfiler()

# Funções de exemplo com debugging avançado
@debug_profiler.debug_function(include_args=True, track_performance=True)
def operacao_complexa(dados, opcoes=None):
    """Operação complexa que pode falhar"""
    if opcoes is None:
        opcoes = {}
    
    # Simular processamento complexo
    if not isinstance(dados, list):
        raise TypeError("Dados devem ser uma lista")
    
    if len(dados) == 0:
        raise ValueError("Lista não pode estar vazia")
    
    resultado = []
    for i, item in enumerate(dados):
        if opcoes.get('slow_mode'):
            time.sleep(0.01)  # Simular operação lenta
        
        if isinstance(item, (int, float)):
            processado = item ** 2
        elif isinstance(item, str):
            processado = len(item)
        else:
            raise TypeError(f"Tipo não suportado no índice {i}: {type(item)}")
        
        resultado.append(processado)
    
    return resultado

@debug_profiler.debug_function()
def funcao_recursiva(n, depth=0):
    """Função recursiva para testar pilha de chamadas"""
    if depth > 10:
        raise RecursionError("Profundidade máxima atingida")
    
    if n <= 1:
        return 1
    
    return n * funcao_recursiva(n-1, depth+1)

@debug_profiler.debug_function()
def funcao_com_bug_intermitente():
    """Função que falha aleatoriamente"""
    import random
    
    if random.random() < 0.3:  # 30% chance de erro
        raise RuntimeError("Erro intermitente!")
    
    return "Sucesso!"

print("=== DEBUGGING AVANÇADO ===")

# Teste 1: Operações bem-sucedidas
print("\\n1. Testando operações normais:")
try:
    resultado1 = operacao_complexa([1, 2, 3, "hello", 5.5])
    print(f"   ✅ Resultado: {resultado1}")
    
    resultado2 = operacao_complexa([10, 20], {'slow_mode': False})
    print(f"   ✅ Resultado: {resultado2}")
    
except Exception as e:
    print(f"   ❌ Erro: {e}")

# Teste 2: Operações com erros
print("\\n2. Testando cenários de erro:")
cenarios_erro = [
    ("lista vazia", []),
    ("tipo inválido", "não é lista"),
    ("item inválido", [1, 2, {}]),
]

for desc, dados in cenarios_erro:
    try:
        resultado = operacao_complexa(dados)
        print(f"   ✅ {desc}: {resultado}")
    except Exception as e:
        print(f"   ❌ {desc}: {type(e).__name__}: {e}")

# Teste 3: Função recursiva
print("\\n3. Testando recursão:")
try:
    resultado = funcao_recursiva(5)
    print(f"   ✅ Fatorial de 5: {resultado}")
    
    # Teste com erro
    resultado = funcao_recursiva(20)  # Vai dar erro
except Exception as e:
    print(f"   ❌ Erro na recursão: {e}")

# Teste 4: Bug intermitente
print("\\n4. Testando bug intermitente (10 tentativas):")
sucessos = 0
for i in range(10):
    try:
        resultado = funcao_com_bug_intermitente()
        sucessos += 1
        print(f"   ✅ Tentativa {i+1}: {resultado}")
    except Exception as e:
        print(f"   ❌ Tentativa {i+1}: {e}")

print(f"   📊 Taxa de sucesso: {sucessos}/10 ({sucessos*10}%)")

# Teste 5: Relatórios de debugging
print("\\n5. Relatórios de debugging:")

print("\\n📊 Pilha atual de chamadas:")
pilha = debug_profiler.get_call_stack()
if pilha:
    for nivel, chamada in enumerate(pilha):
        print(f"   {nivel}: {chamada['function']} (#{chamada['call_id']})")
else:
    print("   (vazia)")

print("\\n⚡ Resumo de performance:")
perf_summary = debug_profiler.get_performance_summary()
for func, stats in perf_summary.items():
    print(f"   {func.split('.')[-1]}:")
    print(f"     Chamadas: {stats['calls']}")
    print(f"     Tempo total: {stats['total_time']:.4f}s")
    print(f"     Tempo médio: {stats['avg_time']:.4f}s")

print("\\n❌ Resumo de erros:")
error_summary = debug_profiler.get_error_summary()
print(f"   Total de erros: {error_summary['total_errors']}")
print(f"   Tipos de erro: {error_summary['error_types']}")

# Exportar relatório
debug_profiler.export_debug_data()

print("\\n🎯 TÉCNICAS AVANÇADAS DEMONSTRADAS:")
print("• Profiler customizado com decorators")
print("• Rastreamento de pilha de chamadas")
print("• Análise de performance automática")
print("• Log estruturado de erros")
print("• Exportação de dados para análise")
print("• Debugging de bugs intermitentes")'''

        self.exemplo_interativo(codigo_avancado, "Debugging Avançado")
        
        try:
            input("\n✅ Seção 6 concluída! Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise

    def _secao_pratica_interativa(self) -> None:
        """Seção de Prática Interativa com exercícios"""
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 SEÇÃO DE PRÁTICA - DEBUGGING E PROFILING")
        else:
            print("\n" + "="*60)
            print("🎯 SEÇÃO DE PRÁTICA - DEBUGGING E PROFILING")
            print("="*60)

        self.print_success("🎉 Hora de praticar seus conhecimentos!")
        self.print_concept("📚 Esta seção contém: Quiz, Exercícios de Código e Desafio Criativo")
        
        try:
            input("\n🚀 Pressione ENTER para começar a prática...")
        except KeyboardInterrupt:
            raise

        # === QUIZ INTERATIVO ===
        self._quiz_debugging()
        
        # === EXERCÍCIOS DE CÓDIGO ===
        self._exercicios_codigo_debugging()
        
        # === DESAFIO CRIATIVO ===
        self._desafio_criativo_debugging()

    def _quiz_debugging(self) -> None:
        """Quiz sobre debugging e profiling"""
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📝 QUIZ: DEBUGGING E PROFILING")
        else:
            print("\n" + "="*50)
            print("📝 QUIZ: DEBUGGING E PROFILING")
            print("="*50)

        perguntas = [
            {
                'pergunta': 'Qual comando do PDB executa a próxima linha sem entrar em funções?',
                'opcoes': ['a) s (step)', 'b) n (next)', 'c) c (continue)', 'd) l (list)'],
                'resposta': 'b',
                'explicacao': 'O comando "n" (next) executa a próxima linha sem entrar em funções chamadas.'
            },
            {
                'pergunta': 'Qual ferramenta é melhor para identificar funções que consomem mais tempo?',
                'opcoes': ['a) print debugging', 'b) assert statements', 'c) cProfile', 'd) logging'],
                'resposta': 'c',
                'explicacao': 'cProfile é o profiler nativo do Python, ideal para análise de performance.'
            },
            {
                'pergunta': 'O que significa um "vazamento de memória" em Python?',
                'opcoes': ['a) Erro de sintaxe', 'b) Memória não liberada pelo GC', 'c) Código muito lento', 'd) Exceção não tratada'],
                'resposta': 'b',
                'explicacao': 'Vazamento de memória ocorre quando objetos não são liberados pelo Garbage Collector.'
            },
            {
                'pergunta': 'Qual é a primeira etapa do processo de debugging?',
                'opcoes': ['a) Corrigir o problema', 'b) Usar o debugger', 'c) Identificar que existe problema', 'd) Escrever testes'],
                'resposta': 'c',
                'explicacao': 'Primeiro precisamos identificar e reconhecer que existe um problema no código.'
            },
            {
                'pergunta': 'Para que serve o comando "pp" no PDB?',
                'opcoes': ['a) Pausar programa', 'b) Pretty print de variáveis', 'c) Sair do debugger', 'd) Mostrar código'],
                'resposta': 'b',
                'explicacao': 'O comando "pp" faz pretty print, formatando a saída de forma mais legível.'
            }
        ]

        acertos = 0
        total = len(perguntas)

        for i, pergunta in enumerate(perguntas, 1):
            try:
                self.print_colored(f"\n❓ PERGUNTA {i}/{total}:", "cyan")
                self.print_concept(pergunta['pergunta'])
                print()
                for opcao in pergunta['opcoes']:
                    self.print_tip(opcao)
                
                while True:
                    try:
                        resposta = input("\n🤔 Sua resposta (a/b/c/d): ").lower().strip()
                        if resposta in ['a', 'b', 'c', 'd']:
                            break
                        self.print_warning("Digite apenas a, b, c ou d")
                    except KeyboardInterrupt:
                        raise
                
                if resposta == pergunta['resposta']:
                    self.print_success("✅ Correto!")
                    acertos += 1
                else:
                    self.print_warning(f"❌ Incorreto. A resposta certa é: {pergunta['resposta']}")
                
                self.print_tip(f"💡 {pergunta['explicacao']}")
                
                if i < total:
                    try:
                        input("\n⏭️ Pressione ENTER para próxima pergunta...")
                    except KeyboardInterrupt:
                        raise
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Quiz interrompido!")
                raise

        # Resultado final
        porcentagem = (acertos / total) * 100
        self.print_colored(f"\n🎯 RESULTADO FINAL: {acertos}/{total} ({porcentagem:.0f}%)", "cyan")
        
        if porcentagem >= 80:
            self.print_success("🏆 Excelente! Você domina debugging!")
        elif porcentagem >= 60:
            self.print_success("👍 Bom trabalho! Continue praticando!")
        else:
            self.print_warning("📚 Revise os conceitos e tente novamente!")

        if self.progress:
            self.progress.add_points(acertos * 5)
            self.print_tip(f"🎁 +{acertos * 5} pontos pelo quiz!")

    def _exercicios_codigo_debugging(self) -> None:
        """Exercícios práticos de debugging"""
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("💻 EXERCÍCIOS DE CÓDIGO")
        else:
            print("\n" + "="*50)
            print("💻 EXERCÍCIOS DE CÓDIGO")
            print("="*50)

        self.print_concept("🛠️ Vamos praticar debugging com código real!")
        
        exercicios = [
            {
                'titulo': 'Corrigir Bug de Divisão',
                'codigo_bugado': '''def calcular_media(numeros):
    total = sum(numeros)
    return total / len(numeros)

# Teste
print(calcular_media([1, 2, 3, 4, 5]))
print(calcular_media([]))  # BUG: Divisão por zero!''',
                'solucao': '''def calcular_media(numeros):
    if not numeros:  # Verificar lista vazia
        return 0
    total = sum(numeros)
    return total / len(numeros)'''
            },
            {
                'titulo': 'Otimizar Performance',
                'codigo_bugado': '''def buscar_duplicatas_lento(lista):
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicatas:
                duplicatas.append(lista[i])
    return duplicatas

# Muito lento para listas grandes!''',
                'solucao': '''def buscar_duplicatas_rapido(lista):
    vistos = set()
    duplicatas = set()
    for item in lista:
        if item in vistos:
            duplicatas.add(item)
        else:
            vistos.add(item)
    return list(duplicatas)'''
            },
            {
                'titulo': 'Adicionar Logging',
                'codigo_bugado': '''def processar_arquivo(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    processed = []
    for line in lines:
        if line.strip():
            processed.append(line.upper())
    
    return processed

# Sem informações de debug!''',
                'solucao': '''import logging

def processar_arquivo(filename):
    logging.info(f"Iniciando processamento de {filename}")
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    logging.debug(f"Lidas {len(lines)} linhas")
    
    processed = []
    for i, line in enumerate(lines):
        if line.strip():
            processed.append(line.upper())
            logging.debug(f"Linha {i+1} processada")
    
    logging.info(f"Processamento concluído: {len(processed)} linhas válidas")
    return processed'''
            }
        ]

        for i, exercicio in enumerate(exercicios, 1):
            try:
                self.print_colored(f"\n🔧 EXERCÍCIO {i}: {exercicio['titulo']}", "yellow")
                
                self.print_tip("Código com problema:")
                self.exemplo_interativo(exercicio['codigo_bugado'], f"Exercício {i} - Problema")
                
                try:
                    input(f"\n🤔 Analise o código e pressione ENTER para ver a solução...")
                except KeyboardInterrupt:
                    raise
                
                self.print_success("✅ Solução:")
                self.exemplo_interativo(exercicio['solucao'], f"Exercício {i} - Solução")
                
                if i < len(exercicios):
                    try:
                        input("\n⏭️ Pressione ENTER para próximo exercício...")
                    except KeyboardInterrupt:
                        raise
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Exercícios interrompidos!")
                raise

        if self.progress:
            self.progress.add_points(30)
            self.print_success("🎁 +30 pontos pelos exercícios!")

    def _desafio_criativo_debugging(self) -> None:
        """Desafio criativo de debugging"""
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎨 DESAFIO CRIATIVO")
        else:
            print("\n" + "="*50)
            print("🎨 DESAFIO CRIATIVO")
            print("="*50)

        self.print_concept("🚀 DESAFIO: Crie um sistema de debugging personalizado!")
        
        desafio_codigo = '''# 🎨 DESAFIO CRIATIVO: Sistema de Debugging Personalizado
# 
# Sua missão: Criar um decorator que combine:
# 1. Medição de tempo de execução
# 2. Captura de erros com stack trace
# 3. Log de entrada e saída de funções
# 4. Contagem de chamadas
# 5. Análise de argumentos
#
# Exemplo de uso desejado:
#
# @meu_debug_decorator
# def funcao_exemplo(x, y):
#     return x + y
#
# Saída esperada:
# [DEBUG] Entrada: funcao_exemplo(x=1, y=2) - Chamada #1
# [DEBUG] Saída: funcao_exemplo -> 3 (0.0001s) - Sucesso
#
# Implemente seu decorator aqui:

import functools
import time
from collections import defaultdict

# Sua implementação aqui:
def meu_debug_decorator(func):
    # TODO: Implementar decorator completo
    pass

# Teste suas funções:
@meu_debug_decorator
def somar(a, b):
    return a + b

@meu_debug_decorator  
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

# Testes
print("=== TESTANDO SISTEMA DE DEBUG ===")
resultado1 = somar(5, 3)
resultado2 = dividir(10, 2)

try:
    resultado3 = dividir(10, 0)  # Deve capturar erro
except ValueError as e:
    print(f"Erro capturado: {e}")

print("\\n🎯 REQUISITOS DO DESAFIO:")
print("✅ Medição de tempo")
print("✅ Log de entrada/saída")  
print("✅ Captura de erros")
print("✅ Contagem de chamadas")
print("✅ Análise de argumentos")'''

        self.exemplo_interativo(desafio_codigo, "Desafio Criativo")
        
        self.print_colored("\n🏆 IMPLEMENTAÇÃO SUGERIDA:", "green")
        
        solucao_desafio = '''# ✅ SOLUÇÃO DO DESAFIO

import functools
import time
import traceback
from collections import defaultdict

# Contador global de chamadas
call_counter = defaultdict(int)

def meu_debug_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        
        # Incrementar contador
        call_counter[func_name] += 1
        call_num = call_counter[func_name]
        
        # Preparar argumentos para log
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        # Log de entrada
        print(f"[DEBUG] Entrada: {func_name}({all_args}) - Chamada #{call_num}")
        
        start_time = time.time()
        
        try:
            # Executar função
            resultado = func(*args, **kwargs)
            
            # Calcular tempo
            end_time = time.time()
            exec_time = end_time - start_time
            
            # Log de saída (sucesso)
            print(f"[DEBUG] Saída: {func_name} -> {resultado} ({exec_time:.4f}s) - Sucesso")
            
            return resultado
            
        except Exception as e:
            # Calcular tempo mesmo com erro
            end_time = time.time()
            exec_time = end_time - start_time
            
            # Log de erro
            print(f"[DEBUG] Erro: {func_name} -> {type(e).__name__}: {e} ({exec_time:.4f}s)")
            print(f"[DEBUG] Stack: {traceback.format_exc().strip()}")
            
            # Re-lançar exceção
            raise
    
    return wrapper

# Exemplo completo de uso:
@meu_debug_decorator
def somar(a, b):
    """Soma dois números"""
    time.sleep(0.01)  # Simular processamento
    return a + b

@meu_debug_decorator  
def dividir(a, b):
    """Divide dois números"""
    if b == 0:
        raise ValueError("Divisão por zero não permitida!")
    return a / b

@meu_debug_decorator
def fibonacci(n):
    """Calcula Fibonacci recursivo"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Demonstração
print("=== SISTEMA DE DEBUG EM AÇÃO ===")

# Testes bem-sucedidos
print("\\n1. Operações normais:")
resultado1 = somar(5, 3)
resultado2 = dividir(10, 2)
resultado3 = somar(1.5, 2.5)

# Teste com erro
print("\\n2. Teste de erro:")
try:
    resultado_erro = dividir(10, 0)
except ValueError:
    print("   (Erro tratado pelo código principal)")

# Teste recursivo
print("\\n3. Teste recursivo:")
fib_resultado = fibonacci(5)

# Estatísticas
print("\\n📊 ESTATÍSTICAS:")
for func_name, count in call_counter.items():
    print(f"   {func_name}: {count} chamadas")

print("\\n🎉 Sistema de debugging personalizado funcionando!")'''

        self.exemplo_interativo(solucao_desafio, "Solução do Desafio")
        
        self.print_success("\n🏆 PARABÉNS! Você completou o desafio criativo!")
        self.print_tip("💡 Este tipo de decorator é muito útil em projetos reais")
        
        if self.progress:
            self.progress.add_points(50)
            self.print_success("🎁 +50 pontos pelo desafio criativo!")

        try:
            input("\n🎯 Pressione ENTER para continuar para o mini projeto...")
        except KeyboardInterrupt:
            raise

    def _mini_projeto_sistema_debugging_avancado(self) -> None:
        """Mini Projeto: Sistema de Debugging Avançado"""
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: SISTEMA DE DEBUGGING AVANÇADO")
        else:
            print("\n" + "="*60)
            print("🚀 MINI PROJETO: SISTEMA DE DEBUGGING AVANÇADO")
            print("="*60)

        self.print_success("🎉 Projeto Final: Sistema Completo de Debugging e Profiling!")
        self.print_concept("🛠️ Vamos criar um sistema profissional que combina todas as técnicas aprendidas")
        
        self.print_colored("\n🎯 FUNCIONALIDADES DO SISTEMA:", "cyan")
        self.print_tip("✅ Profiling automático de funções")
        self.print_tip("✅ Detecção de vazamentos de memória")
        self.print_tip("✅ Análise de performance em tempo real")
        self.print_tip("✅ Sistema de alertas para problemas")
        self.print_tip("✅ Dashboard de monitoramento")
        self.print_tip("✅ Exportação de relatórios")
        
        try:
            input("\n🚀 Pressione ENTER para começar o desenvolvimento...")
        except KeyboardInterrupt:
            raise

        projeto_codigo = '''# 🚀 MINI PROJETO: SISTEMA DE DEBUGGING AVANÇADO
# Sistema completo para debugging e profiling em produção

import time
import functools
import threading
import traceback
import json
import gc
import sys
from datetime import datetime, timedelta
from collections import defaultdict, deque
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict

@dataclass
class PerformanceMetrics:
    """Métricas de performance de uma função"""
    function_name: str
    total_calls: int = 0
    total_time: float = 0.0
    avg_time: float = 0.0
    min_time: float = float('inf')
    max_time: float = 0.0
    error_count: int = 0
    last_called: Optional[str] = None
    memory_usage: List[int] = None
    
    def __post_init__(self):
        if self.memory_usage is None:
            self.memory_usage = []
    
    def update_timing(self, execution_time: float):
        """Atualiza métricas de tempo"""
        self.total_calls += 1
        self.total_time += execution_time
        self.avg_time = self.total_time / self.total_calls
        self.min_time = min(self.min_time, execution_time)
        self.max_time = max(self.max_time, execution_time)
        self.last_called = datetime.now().isoformat()
    
    def add_error(self):
        """Registra um erro"""
        self.error_count += 1
    
    def add_memory_usage(self, memory_bytes: int):
        """Adiciona medição de memória"""
        self.memory_usage.append(memory_bytes)
        # Manter apenas últimas 100 medições
        if len(self.memory_usage) > 100:
            self.memory_usage.pop(0)

class AdvancedDebugSystem:
    """Sistema avançado de debugging e profiling"""
    
    def __init__(self):
        self.metrics: Dict[str, PerformanceMetrics] = {}
        self.active_calls: Dict[int, Dict] = {}  # Thread ID -> call info
        self.alerts: List[Dict] = []
        self.monitoring_active = False
        self.monitor_thread = None
        self.performance_thresholds = {
            'slow_function_time': 1.0,  # segundos
            'high_error_rate': 0.1,     # 10%
            'memory_growth_rate': 1024*1024*10  # 10MB
        }
        self.lock = threading.RLock()
    
    def profile_function(self, 
                        monitor_memory: bool = True,
                        alert_on_slow: bool = True,
                        alert_on_errors: bool = True):
        """Decorator principal para profiling automático"""
        def decorator(func: Callable) -> Callable:
            func_name = f"{func.__module__}.{func.__name__}"
            
            # Inicializar métricas se necessário
            if func_name not in self.metrics:
                self.metrics[func_name] = PerformanceMetrics(func_name)
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                thread_id = threading.get_ident()
                
                # Preparar informações da chamada
                call_info = {
                    'function': func_name,
                    'start_time': time.time(),
                    'thread_id': thread_id,
                    'args_count': len(args),
                    'kwargs_count': len(kwargs)
                }
                
                # Medição de memória inicial
                if monitor_memory:
                    gc.collect()
                    call_info['start_memory'] = sum(sys.getsizeof(obj) for obj in gc.get_objects()[:1000])
                
                # Registrar chamada ativa
                with self.lock:
                    self.active_calls[thread_id] = call_info
                
                try:
                    # Executar função
                    resultado = func(*args, **kwargs)
                    
                    # Calcular métricas
                    end_time = time.time()
                    execution_time = end_time - call_info['start_time']
                    
                    # Atualizar estatísticas
                    with self.lock:
                        metrics = self.metrics[func_name]
                        metrics.update_timing(execution_time)
                        
                        # Medição de memória final
                        if monitor_memory:
                            gc.collect()
                            end_memory = sum(sys.getsizeof(obj) for obj in gc.get_objects()[:1000])
                            memory_delta = end_memory - call_info['start_memory']
                            metrics.add_memory_usage(memory_delta)
                        
                        # Verificar alertas
                        if alert_on_slow and execution_time > self.performance_thresholds['slow_function_time']:
                            self._add_alert('slow_function', {
                                'function': func_name,
                                'execution_time': execution_time,
                                'threshold': self.performance_thresholds['slow_function_time']
                            })
                    
                    return resultado
                    
                except Exception as e:
                    # Registrar erro
                    with self.lock:
                        self.metrics[func_name].add_error()
                        
                        if alert_on_errors:
                            error_rate = (self.metrics[func_name].error_count / 
                                        max(1, self.metrics[func_name].total_calls))
                            
                            if error_rate > self.performance_thresholds['high_error_rate']:
                                self._add_alert('high_error_rate', {
                                    'function': func_name,
                                    'error_rate': error_rate,
                                    'threshold': self.performance_thresholds['high_error_rate'],
                                    'error': str(e)
                                })
                    
                    raise
                    
                finally:
                    # Remover chamada ativa
                    with self.lock:
                        if thread_id in self.active_calls:
                            del self.active_calls[thread_id]
            
            return wrapper
        return decorator
    
    def _add_alert(self, alert_type: str, details: Dict):
        """Adiciona alerta ao sistema"""
        alert = {
            'type': alert_type,
            'timestamp': datetime.now().isoformat(),
            'details': details
        }
        
        self.alerts.append(alert)
        
        # Manter apenas últimos 1000 alertas
        if len(self.alerts) > 1000:
            self.alerts.pop(0)
        
        # Log do alerta
        print(f"🚨 ALERTA [{alert_type}]: {details}")
    
    def start_monitoring(self, interval: float = 5.0):
        """Inicia monitoramento contínuo"""
        if self.monitoring_active:
            return
        
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval,)
        )
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        print(f"📈 Monitoramento iniciado (intervalo: {interval}s)")
    
    def stop_monitoring(self):
        """Para monitoramento"""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        print("📉 Monitoramento parado")
    
    def _monitoring_loop(self, interval: float):
        """Loop de monitoramento contínuo"""
        while self.monitoring_active:
            try:
                self._check_system_health()
                time.sleep(interval)
            except Exception as e:
                print(f"❌ Erro no monitoramento: {e}")
    
    def _check_system_health(self):
        """Verifica saúde geral do sistema"""
        with self.lock:
            # Verificar funções ativas há muito tempo
            current_time = time.time()
            for thread_id, call_info in self.active_calls.items():
                duration = current_time - call_info['start_time']
                if duration > 30:  # 30 segundos
                    self._add_alert('long_running_function', {
                        'function': call_info['function'],
                        'duration': duration,
                        'thread_id': thread_id
                    })
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Retorna dados para dashboard"""
        with self.lock:
            # Estatísticas gerais
            total_functions = len(self.metrics)
            total_calls = sum(m.total_calls for m in self.metrics.values())
            total_errors = sum(m.error_count for m in self.metrics.values())
            
            # Top 5 funções mais chamadas
            top_called = sorted(
                self.metrics.values(),
                key=lambda m: m.total_calls,
                reverse=True
            )[:5]
            
            # Top 5 funções mais lentas
            top_slow = sorted(
                self.metrics.values(),
                key=lambda m: m.avg_time,
                reverse=True
            )[:5]
            
            # Funções com mais erros
            top_errors = sorted(
                [m for m in self.metrics.values() if m.error_count > 0],
                key=lambda m: m.error_count,
                reverse=True
            )[:5]
            
            return {
                'summary': {
                    'total_functions': total_functions,
                    'total_calls': total_calls,
                    'total_errors': total_errors,
                    'active_calls': len(self.active_calls),
                    'recent_alerts': len([a for a in self.alerts 
                                        if datetime.fromisoformat(a['timestamp']) > 
                                        datetime.now() - timedelta(minutes=5)])
                },
                'top_called': [asdict(m) for m in top_called],
                'top_slow': [asdict(m) for m in top_slow],
                'top_errors': [asdict(m) for m in top_errors],
                'recent_alerts': self.alerts[-10:],
                'active_calls': list(self.active_calls.values())
            }
    
    def print_dashboard(self):
        """Exibe dashboard no console"""
        data = self.get_dashboard_data()
        
        print("\\n" + "="*80)
        print("                    DASHBOARD DE DEBUGGING AVANÇADO")
        print("="*80)
        
        # Resumo
        summary = data['summary']
        print(f"📊 RESUMO GERAL:")
        print(f"   Funções monitoradas: {summary['total_functions']}")
        print(f"   Total de chamadas: {summary['total_calls']:,}")
        print(f"   Total de erros: {summary['total_errors']:,}")
        print(f"   Chamadas ativas: {summary['active_calls']}")
        print(f"   Alertas recentes (5min): {summary['recent_alerts']}")
        
        # Top funções
        if data['top_called']:
            print(f"\\n🔝 TOP FUNÇÕES MAIS CHAMADAS:")
            for i, metrics in enumerate(data['top_called'], 1):
                print(f"   {i}. {metrics['function_name'].split('.')[-1]}: "
                      f"{metrics['total_calls']:,} calls, "
                      f"{metrics['avg_time']*1000:.2f}ms avg")
        
        if data['top_slow']:
            print(f"\\n🐌 TOP FUNÇÕES MAIS LENTAS:")
            for i, metrics in enumerate(data['top_slow'], 1):
                print(f"   {i}. {metrics['function_name'].split('.')[-1]}: "
                      f"{metrics['avg_time']*1000:.2f}ms avg, "
                      f"{metrics['total_calls']} calls")
        
        if data['top_errors']:
            print(f"\\n❌ FUNÇÕES COM MAIS ERROS:")
            for i, metrics in enumerate(data['top_errors'], 1):
                error_rate = metrics['error_count'] / max(1, metrics['total_calls']) * 100
                print(f"   {i}. {metrics['function_name'].split('.')[-1]}: "
                      f"{metrics['error_count']} erros ({error_rate:.1f}%)")
        
        # Alertas recentes
        if data['recent_alerts']:
            print(f"\\n🚨 ALERTAS RECENTES:")
            for alert in data['recent_alerts'][-5:]:
                timestamp = datetime.fromisoformat(alert['timestamp']).strftime('%H:%M:%S')
                print(f"   [{timestamp}] {alert['type']}: {alert['details']}")
    
    def export_report(self, filename: str = None):
        """Exporta relatório completo"""
        if filename is None:
            filename = f"debug_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = self.get_dashboard_data()
        data['export_timestamp'] = datetime.now().isoformat()
        data['metrics'] = {name: asdict(metrics) for name, metrics in self.metrics.items()}
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Relatório exportado para {filename}")
        return filename

# Instância global do sistema
debug_system = AdvancedDebugSystem()

# DEMONSTRAÇÃO COMPLETA DO SISTEMA

# Funções de exemplo para teste
@debug_system.profile_function(monitor_memory=True, alert_on_slow=True)
def operacao_rapida(n):
    """Operação rápida para teste"""
    return sum(range(n))

@debug_system.profile_function(monitor_memory=True, alert_on_slow=True)
def operacao_lenta(n):
    """Operação lenta que vai gerar alerta"""
    time.sleep(1.5)  # Mais que o threshold de 1.0s
    return n ** 2

@debug_system.profile_function(alert_on_errors=True)
def operacao_instavel():
    """Operação que falha frequentemente"""
    import random
    if random.random() < 0.4:  # 40% chance de erro
        raise RuntimeError("Erro simulado!")
    return "Sucesso"

@debug_system.profile_function()
def processamento_memoria(tamanho):
    """Operação que consome memória"""
    dados = []
    for i in range(tamanho):
        dados.append([0] * 1000)
    return len(dados)

def demonstrar_sistema():
    """Demonstração completa do sistema"""
    print("=== SISTEMA DE DEBUGGING AVANÇADO ===")
    
    # Iniciar monitoramento
    debug_system.start_monitoring(interval=2.0)
    
    try:
        print("\\n🧪 EXECUTANDO TESTES...")
        
        # Teste 1: Operações normais
        print("\\n1. Operações rápidas:")
        for i in range(10):
            resultado = operacao_rapida(1000 + i * 100)
            print(f"   Operação {i+1}: {resultado}")
        
        # Teste 2: Operação lenta (vai gerar alerta)
        print("\\n2. Operação lenta (gerará alerta):")
        resultado_lento = operacao_lenta(5)
        print(f"   Resultado: {resultado_lento}")
        
        # Teste 3: Operações instáveis
        print("\\n3. Operações instáveis:")
        sucessos = 0
        for i in range(15):
            try:
                resultado = operacao_instavel()
                sucessos += 1
                print(f"   ✅ Tentativa {i+1}: {resultado}")
            except RuntimeError:
                print(f"   ❌ Tentativa {i+1}: Falhou")
        print(f"   Taxa de sucesso: {sucessos}/15 ({sucessos/15*100:.1f}%)")
        
        # Teste 4: Operação com memória
        print("\\n4. Operações que consomem memória:")
        for tamanho in [1000, 5000, 10000]:
            resultado = processamento_memoria(tamanho)
            print(f"   Processado {tamanho} -> {resultado} itens")
        
        # Aguardar um pouco para o monitoramento coletar dados
        time.sleep(3)
        
        # Exibir dashboard
        debug_system.print_dashboard()
        
        # Exportar relatório
        arquivo = debug_system.export_report()
        
    finally:
        # Parar monitoramento
        debug_system.stop_monitoring()
    
    print("\\n🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("\\n🎯 FUNCIONALIDADES DEMONSTRADAS:")
    print("• ✅ Profiling automático de performance")
    print("• ✅ Monitoramento de memória")
    print("• ✅ Sistema de alertas inteligente")
    print("• ✅ Dashboard em tempo real")
    print("• ✅ Detecção de funções lentas")
    print("• ✅ Análise de taxa de erro")
    print("• ✅ Exportação de relatórios")
    print("• ✅ Monitoramento de threads")
    
    return arquivo

# Executar demonstração
if __name__ == "__main__":
    arquivo_relatorio = demonstrar_sistema()
    print(f"\\n📊 Relatório completo salvo em: {arquivo_relatorio}")'''

        self.exemplo_interativo(projeto_codigo, "Sistema de Debugging Avançado")
        
        self.print_success("\n🏆 PARABÉNS! Você criou um sistema completo de debugging!")
        
        self.print_colored("\n🎯 CARACTERÍSTICAS DO SEU SISTEMA:", "green")
        self.print_tip("🔧 Profiling automático com decorators")
        self.print_tip("📊 Monitoramento de performance em tempo real")
        self.print_tip("🚨 Sistema inteligente de alertas")
        self.print_tip("📈 Dashboard interativo")
        self.print_tip("💾 Exportação de relatórios detalhados")
        self.print_tip("🧵 Suporte a multi-threading")
        self.print_tip("🔍 Detecção de vazamentos de memória")
        
        self.print_colored("\n💡 APLICAÇÕES REAIS:", "yellow")
        self.print_tip("🌐 Monitoramento de APIs em produção")
        self.print_tip("📱 Debugging de aplicações móveis")
        self.print_tip("🎮 Otimização de jogos")
        self.print_tip("🏭 Sistemas industriais críticos")
        self.print_tip("🤖 Debugging de sistemas de IA")
        
        # Registrar conclusão do mini projeto
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            self.print_success(f"🎁 +{self.mini_project_points} pontos pelo mini projeto!")
            
        self.complete_mini_project("Sistema de Debugging Avançado")
        
        try:
            input("\n🏁 Pressione ENTER para finalizar o módulo...")
        except KeyboardInterrupt:
            pass

    def exemplo_interativo(self, codigo: str, titulo: str) -> None:
        """Executa exemplo de código de forma interativa"""
        if self.ui:
            self.ui.code_block(codigo, titulo)
        else:
            print(f"\n{'='*50}")
            print(f"CÓDIGO: {titulo}")
            print('='*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            self.print_warning(f"Erro na execução do exemplo: {e}", "❌")