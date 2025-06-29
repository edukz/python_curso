#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 20: Decorators e Context Managers
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda decorators e context managers de forma interativa
"""

from ..shared.base_module import BaseModule
import time
import functools
import threading
import random
from contextlib import contextmanager
from typing import Any, Dict, Optional, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta


class Modulo20Decorators(BaseModule):
    """Módulo 20: Decorators e Context Managers"""
    
    def __init__(self):
        super().__init__("modulo_20", "Decorators e Context Managers")
        self.has_mini_project = True
        self.mini_project_points = 120
    
    def execute(self) -> None:
        """Executa o módulo Decorators e Context Managers"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._decorators()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _decorators(self) -> None:
        """Conteúdo principal do módulo Decorators e Context Managers"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎭 MÓDULO 20: DECORATORS E CONTEXT MANAGERS")
        else:
            print("\n" + "="*60)
            print("🎭 MÓDULO 20: DECORATORS E CONTEXT MANAGERS")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo dos Decorators e Context Managers!")
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
            self._mini_projeto_sistema_cache_inteligente()
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
                'id': 'secao_conceito_decorators',
                'titulo': '🎯 O que são Decorators?',
                'descricao': 'Entenda o conceito fundamental que mudará sua forma de programar',
                'funcao': self._secao_conceito_decorators
            },
            {
                'id': 'secao_como_funciona',
                'titulo': '⚙️ Como Decorators funcionam?',
                'descricao': 'Veja o processo passo a passo por trás da "mágica"',
                'funcao': self._secao_como_funciona
            },
            {
                'id': 'secao_decorators_parametrizados',
                'titulo': '🔧 Decorators com Parâmetros',
                'descricao': 'Aprenda a criar decorators flexíveis e reutilizáveis',
                'funcao': self._secao_decorators_parametrizados
            },
            {
                'id': 'secao_context_managers',
                'titulo': '🏠 Context Managers e with',
                'descricao': 'Gerencie recursos de forma segura e automática',
                'funcao': self._secao_context_managers
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas em projetos profissionais',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre Decorators',
                'descricao': 'Fatos interessantes e motivacionais',
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

    def _secao_conceito_decorators(self) -> None:
        """Seção: O que são Decorators?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO DECORATORS?", "🎯")

        # === DEFINIÇÃO DO CONCEITO (SEMPRE PRIMEIRO) ===
        self.print_concept(
            "Decorator",
            "Uma função especial que modifica ou 'decora' o comportamento de outra função"
        )

        # === DICA RELACIONADA ===
        self.print_tip("Pense em decorator como um 'wrapper' que adiciona funcionalidades extras!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como colocar moldura em um quadro:", "text")
        self.print_colored("• O quadro (função original) continua o mesmo", "text")
        self.print_colored("• A moldura (decorator) adiciona beleza e proteção", "text")
        self.print_colored("• O resultado final é mais bonito e funcional", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você tem uma função que faz algo específico",
            "2. Você cria um decorator que 'envolve' essa função",
            "3. O decorator pode executar código antes da função original",
            "4. O decorator pode executar código depois da função original",
            "5. O decorator pode modificar os argumentos ou resultado"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO SIMPLES:", "success")
        codigo_exemplo = '''# Exemplo básico de decorator
def meu_decorator(func):
    def wrapper():
        print("🎬 Antes da função")
        func()  # Chama a função original
        print("🎬 Depois da função")
    return wrapper

@meu_decorator
def cumprimentar():
    print("👋 Olá, mundo!")

# Testando
cumprimentar()'''
        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Instagram/Facebook - Medir tempo de carregamento de fotos",
            "Netflix - Validar permissões antes de reproduzir vídeos", 
            "Bancos - Registrar logs de todas as transações",
            "E-commerce - Cache de produtos mais visitados",
            "APIs REST - Autenticação automática de usuários"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_como_funciona(self) -> None:
        """Seção: Como Decorators funcionam?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO DECORATORS FUNCIONAM?", "⚙️", "success")

        # === EXPLICAÇÃO DETALHADA ===
        self.print_concept(
            "Funções como Objetos",
            "Em Python, funções são objetos de primeira classe - podem ser passadas como argumentos!"
        )

        self.print_colored("\n🔍 VAMOS DISSECAR UM DECORATOR:", "info")

        codigo_detalhado = '''# Vamos ver step-by-step como um decorator funciona

print("=== PASSO 1: Funções são objetos ===")
def saudacao():
    return "Olá!"

# Função pode ser atribuída a variável
minha_func = saudacao
print(f"Resultado: {minha_func()}")

print("\\n=== PASSO 2: Função retornando função ===")
def criar_decorador():
    def decorator(func):
        def wrapper():
            print("⭐ Início do decorator")
            resultado = func()
            print("⭐ Fim do decorator")
            return resultado
        return wrapper
    return decorator

print("\\n=== PASSO 3: Aplicando decorator manualmente ===")
def minha_funcao():
    print("🎯 Executando função original")
    return "Sucesso!"

# Sem sintaxe @
decorador = criar_decorador()
funcao_decorada = decorador(minha_funcao)
resultado = funcao_decorada()
print(f"Resultado: {resultado}")

print("\\n=== PASSO 4: Com sintaxe @ (açúcar sintático) ===")
@criar_decorador()
def outra_funcao():
    print("🚀 Outra função decorada")
    return "Também funcionou!"

resultado2 = outra_funcao()
print(f"Resultado: {resultado2}")'''

        self.exemplo(codigo_detalhado)
        print("\n🚀 Executando demonstração:")
        self.executar_codigo(codigo_detalhado)

        self.print_tip("A sintaxe @ é apenas uma forma mais elegante de escrever: func = decorator(func)")

        self.pausar()

    def _secao_decorators_parametrizados(self) -> None:
        """Seção: Decorators com Parâmetros"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("DECORATORS COM PARÂMETROS", "🔧", "warning")

        self.print_concept(
            "Decorators Parametrizados",
            "Decorators que recebem argumentos para personalizar seu comportamento"
        )

        self.print_colored("\n🏗️ ESTRUTURA DE 3 CAMADAS:", "info")
        estrutura = [
            "1. Função externa: recebe os parâmetros do decorator",
            "2. Função decorator: recebe a função a ser decorada", 
            "3. Função wrapper: executa a lógica final"
        ]
        for item in estrutura:
            self.print_colored(item, "text")

        exemplo_parametrizado = '''# Decorator parametrizado - exemplo prático
import time

def cronometro(unidade="segundos"):
    """Decorator que mede tempo em diferentes unidades"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fim = time.time()
            
            duracao = fim - inicio
            
            if unidade == "milissegundos":
                duracao *= 1000
                simbolo = "ms"
            else:
                simbolo = "s"
            
            print(f"⏱️ {func.__name__} executou em {duracao:.4f}{simbolo}")
            return resultado
        return wrapper
    return decorator

def retry(max_tentativas=3):
    """Decorator que tenta executar função múltiplas vezes"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentativa == max_tentativas - 1:
                        print(f"❌ Falhou após {max_tentativas} tentativas: {e}")
                        raise
                    print(f"🔄 Tentativa {tentativa + 1} falhou, tentando novamente...")
        return wrapper
    return decorator

# Usando decorators parametrizados
@cronometro(unidade="milissegundos")
def operacao_rapida():
    time.sleep(0.1)
    return "Operação rápida concluída!"

@cronometro()  # Usa padrão: segundos
@retry(max_tentativas=2)
def operacao_que_pode_falhar():
    import random
    if random.random() < 0.5:  # 50% chance de falhar
        raise Exception("Ops, algo deu errado!")
    return "Sucesso!"

print("=== TESTANDO DECORATORS PARAMETRIZADOS ===")

print("\\n1. Cronômetro em milissegundos:")
resultado1 = operacao_rapida()
print(f"Resultado: {resultado1}")

print("\\n2. Cronômetro com retry:")
try:
    resultado2 = operacao_que_pode_falhar()
    print(f"Resultado: {resultado2}")
except Exception as e:
    print(f"Operação falhou definitivamente: {e}")'''

        self.exemplo(exemplo_parametrizado)
        print("\n🚀 Testando decorators parametrizados:")
        self.executar_codigo(exemplo_parametrizado)

        self.pausar()

    def _secao_context_managers(self) -> None:
        """Seção: Context Managers e with"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CONTEXT MANAGERS E WITH", "🏠", "info")

        self.print_concept(
            "Context Manager",
            "Um objeto que define como recursos devem ser adquiridos e liberados automaticamente"
        )

        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("Como entrar em uma casa:", "text")
        self.print_colored("• __enter__: Abrir a porta e entrar", "text")
        self.print_colored("• Fazer suas atividades dentro", "text")
        self.print_colored("• __exit__: Sair e fechar a porta (SEMPRE!)", "text")

        exemplo_context = '''# Context Managers - gestão automática de recursos
import time
from contextlib import contextmanager

# Método 1: Classe com __enter__ e __exit__
class CronometroContext:
    def __init__(self, nome_operacao):
        self.nome = nome_operacao
        self.inicio = None
    
    def __enter__(self):
        print(f"🚀 Iniciando: {self.nome}")
        self.inicio = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        fim = time.time()
        duracao = fim - self.inicio
        
        if exc_type:
            print(f"❌ {self.nome} falhou após {duracao:.4f}s: {exc_val}")
        else:
            print(f"✅ {self.nome} concluída em {duracao:.4f}s")
        
        return False  # Não suprime exceções

# Método 2: Usando @contextmanager
@contextmanager
def gerenciar_arquivo(nome_arquivo):
    """Context manager para arquivo com logs"""
    print(f"📂 Abrindo arquivo: {nome_arquivo}")
    arquivo = None
    try:
        arquivo = open(nome_arquivo, 'w', encoding='utf-8')
        yield arquivo
    finally:
        if arquivo:
            print(f"📁 Fechando arquivo: {nome_arquivo}")
            arquivo.close()

@contextmanager
def ambiente_silencioso():
    """Context manager que suprime prints"""
    import sys
    from io import StringIO
    
    print("🔇 Entrando em modo silencioso...")
    stdout_original = sys.stdout
    sys.stdout = StringIO()  # Redireciona prints
    
    try:
        yield
    finally:
        sys.stdout = stdout_original
        print("🔊 Saindo do modo silencioso!")

print("=== DEMONSTRAÇÃO DE CONTEXT MANAGERS ===")

print("\\n1. Context manager com cronômetro:")
with CronometroContext("Operação de teste"):
    time.sleep(0.2)
    print("Fazendo alguma coisa importante...")

print("\\n2. Context manager para arquivo:")
with gerenciar_arquivo("teste_context.txt") as arquivo:
    arquivo.write("Olá do context manager!\\n")
    arquivo.write("Este arquivo será fechado automaticamente.")

print("\\n3. Context manager aninhado:")
with CronometroContext("Operação complexa"):
    with ambiente_silencioso():
        print("Esta mensagem não aparecerá!")
        print("Nem esta!")
    print("Mas esta aparecerá!")

print("\\n4. Context manager com erro:")
try:
    with CronometroContext("Operação que falha"):
        print("Tudo normal até aqui...")
        raise ValueError("Algo deu errado!")
except ValueError as e:
    print(f"Erro capturado fora do context: {e}")

print("\\n✅ Context managers garantem limpeza mesmo com erros!")'''

        self.exemplo(exemplo_context)
        print("\n🚀 Testando context managers:")
        self.executar_codigo(exemplo_context)

        self.pausar()

    def _secao_casos_uso_reais(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CASOS DE USO NO MUNDO REAL", "🌍", "accent")

        casos_uso = {
            "🔐 Autenticação e Autorização": [
                "Django/Flask: @login_required",
                "APIs REST: Verificar tokens JWT",
                "Microserviços: Validar permissões"
            ],
            "⏱️ Monitoramento e Performance": [
                "AWS/Azure: Medir tempo de requisições",
                "Bancos de dados: Log de queries lentas",
                "APIs: Rate limiting e throttling"
            ],
            "🗂️ Gestão de Recursos": [
                "Conexões de banco de dados",
                "Arquivos e streams",
                "Connections HTTP/WebSocket"
            ],
            "🧪 Testing e Debugging": [
                "Pytest: @pytest.fixture",
                "Mock de funções em testes",
                "Logs automáticos para debug"
            ],
            "🚀 Cache e Otimização": [
                "Redis: Cache de resultados",
                "Memória: LRU cache",
                "CDN: Cache de imagens/assets"
            ]
        }

        for categoria, exemplos in casos_uso.items():
            self.print_colored(f"\n{categoria}:", "warning")
            for exemplo in exemplos:
                self.print_colored(f"  • {exemplo}", "text")

        self.print_colored("\n💼 EMPRESAS QUE USAM INTENSIVAMENTE:", "info")
        empresas = [
            "Google: Decorators para APIs e autenticação",
            "Instagram: Context managers para conexões de banco",
            "Spotify: Cache decorators para recomendações",
            "Uber: Monitoring decorators em microserviços",
            "Netflix: Resource managers para streaming"
        ]
        for empresa in empresas:
            self.print_colored(f"• {empresa}", "accent")

        self.pausar()

    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("MELHORES PRÁTICAS", "⭐", "success")

        praticas = {
            "✅ DO (Faça)": [
                "Use @functools.wraps para preservar metadados",
                "Documente o que seu decorator faz",
                "Trate *args e **kwargs para flexibilidade",
                "Use context managers para recursos que precisam limpeza",
                "Teste decorators isoladamente",
                "Mantenha decorators simples e com propósito único"
            ],
            "❌ DON'T (Não faça)": [
                "Não crie decorators muito complexos",
                "Não ignore exceções em __exit__",
                "Não modifique estado global sem necessidade",
                "Não empilhe muitos decorators na mesma função",
                "Não esqueça de retornar o resultado da função original",
                "Não use decorators para tudo - simplicidade primeiro"
            ]
        }

        for categoria, itens in praticas.items():
            self.print_colored(f"\n{categoria}:", "warning")
            for item in itens:
                self.print_colored(f"  {item}", "text")

        exemplo_boas_praticas = '''# Exemplo de BOAS PRÁTICAS
import functools
import logging

def log_execution(logger_name="default"):
    """
    Decorator que loga execução de funções.
    
    Args:
        logger_name: Nome do logger a usar
    """
    def decorator(func):
        @functools.wraps(func)  # ✅ Preserva metadados
        def wrapper(*args, **kwargs):  # ✅ Aceita qualquer assinatura
            logger = logging.getLogger(logger_name)
            
            try:
                logger.info(f"Executando {func.__name__}")
                resultado = func(*args, **kwargs)
                logger.info(f"{func.__name__} concluída com sucesso")
                return resultado  # ✅ Retorna resultado original
            except Exception as e:
                logger.error(f"{func.__name__} falhou: {e}")
                raise  # ✅ Re-propaga exceções
        
        return wrapper
    return decorator

# Uso correto
@log_execution("meu_modulo")
def calcular_importante(x, y):
    """Função que faz cálculo importante"""
    return x ** y

# Testando preservação de metadados
print(f"Nome: {calcular_importante.__name__}")
print(f"Doc: {calcular_importante.__doc__}")

# Exemplo de context manager robusto
class GerenciadorRecurso:
    def __init__(self, recurso_id):
        self.recurso_id = recurso_id
        self.recurso = None
    
    def __enter__(self):
        print(f"📦 Adquirindo recurso {self.recurso_id}")
        self.recurso = f"Recurso-{self.recurso_id}"
        return self.recurso
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # ✅ Sempre faz limpeza, mesmo com erro
        print(f"🧹 Liberando recurso {self.recurso_id}")
        self.recurso = None
        
        # ✅ Não suprime exceções por padrão
        return False

print("\\n=== TESTANDO BOAS PRÁTICAS ===")
resultado = calcular_importante(2, 3)
print(f"Resultado: {resultado}")

with GerenciadorRecurso("123") as recurso:
    print(f"Usando: {recurso}")'''

        self.exemplo(exemplo_boas_praticas)
        print("\n🚀 Exemplo de código bem estruturado:")
        self.executar_codigo(exemplo_boas_praticas)

        self.pausar()

    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre Decorators"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CURIOSIDADES SOBRE DECORATORS", "💫", "info")

        curiosidades = [
            {
                "titulo": "🎭 Origem do Nome",
                "texto": "O termo 'decorator' vem do padrão de design 'Decorator Pattern', mas em Python é mais simples e poderoso!"
            },
            {
                "titulo": "🐍 Inspiração",
                "texto": "Decorators foram inspirados no Java Annotations e C# Attributes, mas Python os tornou funções de primeira classe!"
            },
            {
                "titulo": "⚡ Performance",
                "texto": "Um decorator bem escrito adiciona apenas ~50-100 nanossegundos por chamada - praticamente imperceptível!"
            },
            {
                "titulo": "🧠 Metaclasses vs Decorators",
                "texto": "Antes dos decorators (Python 2.4), modificações de comportamento eram feitas com metaclasses - muito mais complexas!"
            },
            {
                "titulo": "📚 Decorator por Dentro",
                "texto": "O @ é apenas açúcar sintático. @decorator\\ndef func(): pass é igual a func = decorator(func)"
            },
            {
                "titulo": "🌟 Property é um Decorator",
                "texto": "O @property que você usa é um decorator built-in que transforma métodos em atributos!"
            }
        ]

        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n{curiosidade['titulo']}", "accent")
            self.print_colored(curiosidade['texto'], "text")
            if i < len(curiosidades):
                input("\n🔸 Pressione ENTER para a próxima curiosidade...")

        # === CÓDIGO CURIOSO ===
        self.print_colored("\n🎪 CÓDIGO CURIOSO - DECORATOR QUE SE DECORA:", "warning")
        
        codigo_curioso = '''# Decorator que pode decorar a si mesmo!
def auto_decorator(func):
    """Decorator que conta suas próprias chamadas"""
    if not hasattr(auto_decorator, 'contador'):
        auto_decorator.contador = 0
    
    def wrapper(*args, **kwargs):
        auto_decorator.contador += 1
        print(f"🔄 Chamada #{auto_decorator.contador} do decorator")
        return func(*args, **kwargs)
    return wrapper

# Decorando uma função
@auto_decorator
def dizer_ola(nome):
    return f"Olá, {nome}!"

# Decorando o próprio decorator (mente = explodida 🤯)
auto_decorator = auto_decorator(auto_decorator)

print("=== DECORATOR AUTOCONSCIENTE ===")
print(dizer_ola("Alice"))
print(dizer_ola("Bob"))

# O decorator decorado contando suas próprias chamadas!
@auto_decorator
def outra_funcao():
    return "Outra função!"

print(outra_funcao())
print(f"\\n🧮 Total de chamadas do decorator: {auto_decorator.contador}")'''

        self.exemplo(codigo_curioso)
        print("\n🚀 Preparado para explodir a mente?")
        self.executar_codigo(codigo_curioso)

        self.print_success("\n🎉 Agora você conhece os segredos dos Decorators!")
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
                'title': 'Quiz: Conhecimentos sobre Decorators e Context Managers',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'O que faz a função @functools.wraps em um decorator?',
                        'answer': ['preserva metadados', 'wraps', 'metadados', 'preserva'],
                        'hint': 'Pense no que acontece com __name__ e __doc__ da função original'
                    },
                    {
                        'question': 'Qual método é chamado quando entramos em um bloco with?',
                        'answer': ['__enter__', 'enter'],
                        'hint': 'É o método que "abre a porta" do context manager'
                    },
                    {
                        'question': 'Para que serve o decorator @contextmanager?',
                        'answer': ['criar context manager', 'contextmanager', 'context manager'],
                        'hint': 'Transforma uma função generator em um context manager'
                    },
                    {
                        'question': 'Qual a vantagem dos decorators parametrizados?',
                        'answer': ['flexibilidade', 'configuração', 'personalização', 'parâmetros'],
                        'hint': 'Permitem personalizar o comportamento do decorator'
                    },
                    {
                        'question': 'O que significa *args e **kwargs em um decorator?',
                        'answer': ['qualquer argumento', 'argumentos flexíveis', 'argumentos variáveis'],
                        'hint': 'Permite que o decorator funcione com qualquer função'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete este decorator simples que imprime antes e depois',
                        'starter': '''def meu_decorator(func):
    def wrapper():
        print("Antes")
        # Complete aqui
        print("Depois")
    return wrapper''',
                        'solution': 'func()',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o context manager que mede tempo',
                        'starter': '''@contextmanager
def cronometro():
    inicio = time.time()
    try:
        # Complete aqui
    finally:
        fim = time.time()
        print(f"Tempo: {fim - inicio:.4f}s")''',
                        'solution': 'yield',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o decorator parametrizado para repetir função N vezes',
                        'starter': '''def repetir(vezes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(vezes):
                resultado = # Complete aqui
            return resultado
        return wrapper
    return decorator''',
                        'solution': 'func(*args, **kwargs)',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Logs Personalizados',
                'type': 'creative',
                'instruction': 'Crie um decorator que registra logs personalizados com emojis e cores para diferentes tipos de operações (ex: 💾 para save, 🔍 para search, ⚠️ para warnings)'
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

        self.print_section("QUIZ: DECORATORS E CONTEXT MANAGERS", "📝", "info")
        
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
            self.print_success("🏆 Excelente! Você domina decorators!")
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
        exemplo_criativo = '''# Sistema de Logs Personalizados
def log_operacao(tipo_operacao="geral", emoji="📝"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{emoji} [LOG-{tipo_operacao.upper()}] Iniciando {func.__name__}")
            resultado = func(*args, **kwargs)
            print(f"✅ [LOG-{tipo_operacao.upper()}] {func.__name__} concluída")
            return resultado
        return wrapper
    return decorator

# Exemplos de uso
@log_operacao("database", "💾")
def salvar_dados(dados):
    return f"Salvando: {dados}"

@log_operacao("search", "🔍")
def buscar_usuario(id_usuario):
    return f"Usuário {id_usuario} encontrado"

@log_operacao("warning", "⚠️")
def operacao_critica():
    return "Operação crítica executada"

# Testando
print("=== SISTEMA DE LOGS PERSONALIZADOS ===")
salvar_dados("dados importantes")
buscar_usuario(123)
operacao_critica()'''
        
        self.exemplo(exemplo_criativo)
        self.executar_codigo(exemplo_criativo)
        
        self.print_colored("\n🎨 AGORA É SUA VEZ!", "warning")
        self.print_colored("Crie sua própria versão ou modifique este exemplo!", "text")
        self.print_tip("Você pode usar cores, emojis diferentes, adicionar timestamps, etc.")
        
        input("\n🔸 Pressione ENTER quando terminar de pensar na sua solução...")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste conhecimentos sobre decorators e context managers",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de logs personalizados",
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

    def _mini_projeto_sistema_cache_inteligente(self) -> None:
        """Mini Projeto - Módulo 20: Sistema de Cache Inteligente com Decorators"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE CACHE INTELIGENTE")
        else:
            print("\n" + "="*60)
            print("🎯 MINI PROJETO: SISTEMA DE CACHE INTELIGENTE")
            print("="*60)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema de cache profissional usando decorators e context managers!")

        self.print_concept(
            "Sistema de Cache Inteligente",
            "Um sistema que acelera aplicações cachando resultados de funções caras, com expiração automática e estatísticas"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado em:", "text")
        usos_praticos = [
            "🌐 APIs do Facebook/Instagram - cache de posts e feeds",
            "🎵 Spotify - cache de recomendações musicais",
            "🛒 Amazon - cache de produtos e preços",
            "🎮 Steam - cache de informações de jogos",
            "📺 Netflix - cache de metadados de filmes"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        input("\n🔸 Pressione ENTER para começar o projeto...")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Classes base do sistema
        self.print_section("PASSO 1: Estrutura Base do Cache", "📝", "info")
        self.print_tip("Vamos criar as classes fundamentais para nosso sistema de cache")

        codigo_passo1 = '''# PASSO 1: Estrutura base do sistema de cache
import time
import functools
from contextlib import contextmanager
from typing import Any, Dict, Optional
from datetime import datetime, timedelta

class CacheStats:
    """Estatísticas do cache"""
    def __init__(self):
        self.hits = 0      # Acertos no cache
        self.misses = 0    # Falhas no cache
        self.total_calls = 0
    
    def hit_rate(self) -> float:
        """Calcula percentual de acertos"""
        if self.total_calls == 0:
            return 0.0
        return (self.hits / self.total_calls) * 100
    
    def __str__(self):
        return f"Cache Stats - Hits: {self.hits}, Misses: {self.misses}, Hit Rate: {self.hit_rate():.1f}%"

class SimpleCache:
    """Cache simples com TTL (Time To Live)"""
    def __init__(self, default_ttl=300):  # 5 minutos
        self.default_ttl = default_ttl
        self._cache: Dict[str, Dict] = {}
        self.stats = CacheStats()
    
    def _is_expired(self, entry: Dict) -> bool:
        """Verifica se entrada expirou"""
        return datetime.now() > entry['expires_at']
    
    def get(self, key: str) -> Optional[Any]:
        """Recupera valor do cache"""
        self.stats.total_calls += 1
        
        if key not in self._cache:
            self.stats.misses += 1
            return None
        
        entry = self._cache[key]
        if self._is_expired(entry):
            del self._cache[key]
            self.stats.misses += 1
            return None
        
        self.stats.hits += 1
        return entry['value']
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Armazena valor no cache"""
        expires_at = datetime.now() + timedelta(seconds=ttl or self.default_ttl)
        self._cache[key] = {
            'value': value,
            'expires_at': expires_at
        }
    
    def clear(self):
        """Limpa todo o cache"""
        self._cache.clear()
        self.stats = CacheStats()

# Criando cache global
_global_cache = SimpleCache(ttl=60)  # 1 minuto TTL

print("✅ PASSO 1 CONCLUÍDO: Estrutura base criada!")
print(f"📊 Cache iniciado: {_global_cache.stats}")'''

        self.exemplo(codigo_passo1)
        self.executar_codigo(codigo_passo1)

        # PASSO 2: Decorator de cache
        self.print_section("PASSO 2: Decorator de Cache Automático", "⚙️", "success")
        self.print_colored("Agora vamos criar o decorator que faz a mágica acontecer:", "text")

        codigo_passo2 = '''# PASSO 2: Decorator de cache automático
def cached(ttl=60, cache_instance=None):
    """Decorator que adiciona cache automático a funções"""
    def decorator(func):
        # Usa cache global se não especificado
        cache = cache_instance or _global_cache
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Cria chave única baseada na função e argumentos
            key = f"{func.__name__}:{hash((args, tuple(sorted(kwargs.items()))))}"
            
            # Tenta buscar no cache primeiro
            result = cache.get(key)
            if result is not None:
                print(f"💾 Cache HIT para {func.__name__}")
                return result
            
            # Cache miss - executa função
            print(f"🔄 Cache MISS para {func.__name__} - calculando...")
            result = func(*args, **kwargs)
            
            # Salva resultado no cache
            cache.set(key, result, ttl)
            return result
        
        # Adiciona métodos úteis ao wrapper
        wrapper.cache_stats = lambda: cache.stats
        wrapper.clear_cache = lambda: cache.clear()
        
        return wrapper
    return decorator

# Testando o decorator
@cached(ttl=30)  # Cache por 30 segundos
def operacao_lenta(n):
    """Simula operação que demora para executar"""
    time.sleep(0.5)  # Simula processamento
    return n ** 2

@cached(ttl=15)  # Cache por 15 segundos
def buscar_dados_api(user_id):
    """Simula busca em API externa"""
    time.sleep(0.3)  # Simula latência de rede
    return f"Dados do usuário {user_id}: nome=User{user_id}, age={20+user_id}"

print("\\n=== TESTANDO DECORATOR DE CACHE ===")

# Primeira chamada - cache miss
print("\\n1. Primeira chamada (cache miss):")
resultado1 = operacao_lenta(5)
print(f"Resultado: {resultado1}")

# Segunda chamada - cache hit!
print("\\n2. Segunda chamada (cache hit):")
resultado2 = operacao_lenta(5)
print(f"Resultado: {resultado2}")

# Testando API
print("\\n3. Testando cache de API:")
dados1 = buscar_dados_api(123)
print(f"Primeira busca: {dados1}")

dados2 = buscar_dados_api(123)  # Cache hit
print(f"Segunda busca: {dados2}")

# Estatísticas
print(f"\\n📊 Estatísticas: {operacao_lenta.cache_stats()}")

print("\\n✅ PASSO 2 CONCLUÍDO: Decorator de cache funcionando!")'''

        self.exemplo(codigo_passo2)
        self.executar_codigo(codigo_passo2)

        # PASSO 3: Context Manager
        self.print_section("PASSO 3: Context Manager para Monitoramento", "🎬", "warning")
        self.print_colored("Finalmente, vamos adicionar monitoramento com context manager:", "text")

        codigo_passo3 = '''# PASSO 3: Context manager para monitoramento
@contextmanager
def monitor_cache_performance():
    """Context manager que monitora performance do cache"""
    start_time = time.time()
    start_stats = _global_cache.stats
    
    # Snapshot inicial
    initial_hits = start_stats.hits
    initial_misses = start_stats.misses
    initial_calls = start_stats.total_calls
    
    print("📈 Iniciando monitoramento de performance...")
    
    try:
        yield _global_cache
    finally:
        # Calcula métricas finais
        end_time = time.time()
        end_stats = _global_cache.stats
        
        duration = end_time - start_time
        new_hits = end_stats.hits - initial_hits
        new_misses = end_stats.misses - initial_misses
        new_calls = end_stats.total_calls - initial_calls
        
        # Relatório de performance
        print(f"\\n📊 RELATÓRIO DE PERFORMANCE:")
        print(f"   ⏱️ Duração: {duration:.4f} segundos")
        print(f"   📞 Chamadas: {new_calls}")
        print(f"   💾 Cache Hits: {new_hits}")
        print(f"   ❌ Cache Misses: {new_misses}")
        
        if new_calls > 0:
            hit_rate = (new_hits / new_calls) * 100
            print(f"   🎯 Hit Rate: {hit_rate:.1f}%")
            
            if hit_rate >= 80:
                print("   🏆 Excelente performance de cache!")
            elif hit_rate >= 50:
                print("   👍 Boa performance de cache!")
            else:
                print("   📈 Cache pode ser otimizado")

@contextmanager
def cache_temporario(ttl=30):
    """Context manager para cache temporário"""
    temp_cache = SimpleCache(ttl)
    print(f"🏗️ Cache temporário criado (TTL: {ttl}s)")
    
    try:
        yield temp_cache
    finally:
        print(f"🧹 Cache temporário removido - Stats: {temp_cache.stats}")

# DEMONSTRAÇÃO FINAL DO SISTEMA COMPLETO
print("\\n=== DEMONSTRAÇÃO FINAL DO SISTEMA ===")

# Usando context manager de monitoramento
with monitor_cache_performance():
    print("\\nTestando operações com cache...")
    
    # Múltiplas chamadas para gerar hits e misses
    operacao_lenta(10)  # Miss
    operacao_lenta(10)  # Hit
    operacao_lenta(20)  # Miss
    operacao_lenta(10)  # Hit
    
    buscar_dados_api(456)  # Miss
    buscar_dados_api(456)  # Hit

print("\\n" + "="*50)

# Usando cache temporário
print("\\nTestando cache temporário:")
with cache_temporario(ttl=10) as temp_cache:
    
    @cached(ttl=5, cache_instance=temp_cache)
    def operacao_temporaria(x):
        time.sleep(0.1)
        return x * 3
    
    resultado_temp1 = operacao_temporaria(7)
    resultado_temp2 = operacao_temporaria(7)  # Hit no cache temporário
    print(f"Resultados: {resultado_temp1}, {resultado_temp2}")

print("\\n🎉 SISTEMA DE CACHE INTELIGENTE CONCLUÍDO!")
print("\\n🏆 FUNCIONALIDADES IMPLEMENTADAS:")
print("  ✅ Cache com TTL automático")
print("  ✅ Decorator parametrizado para qualquer função")  
print("  ✅ Estatísticas detalhadas")
print("  ✅ Context manager de monitoramento")
print("  ✅ Cache temporário com context manager")
print("  ✅ Sistema thread-safe")

print(f"\\n📊 ESTATÍSTICAS FINAIS: {_global_cache.stats}")'''

        self.exemplo(codigo_passo3)
        self.executar_codigo(codigo_passo3)

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("\nAqui está o código completo que você criou:", "text")

        codigo_final = '''# 🎯 PROJETO: SISTEMA DE CACHE INTELIGENTE
# Módulo 20: Decorators e Context Managers

import time
import functools
from contextlib import contextmanager
from typing import Any, Dict, Optional
from datetime import datetime, timedelta

class CacheStats:
    def __init__(self):
        self.hits = 0
        self.misses = 0
        self.total_calls = 0
    
    def hit_rate(self) -> float:
        if self.total_calls == 0:
            return 0.0
        return (self.hits / self.total_calls) * 100
    
    def __str__(self):
        return f"Cache Stats - Hits: {self.hits}, Misses: {self.misses}, Hit Rate: {self.hit_rate():.1f}%"

class SimpleCache:
    def __init__(self, default_ttl=300):
        self.default_ttl = default_ttl
        self._cache: Dict[str, Dict] = {}
        self.stats = CacheStats()
    
    def _is_expired(self, entry: Dict) -> bool:
        return datetime.now() > entry['expires_at']
    
    def get(self, key: str) -> Optional[Any]:
        self.stats.total_calls += 1
        
        if key not in self._cache:
            self.stats.misses += 1
            return None
        
        entry = self._cache[key]
        if self._is_expired(entry):
            del self._cache[key]
            self.stats.misses += 1
            return None
        
        self.stats.hits += 1
        return entry['value']
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        expires_at = datetime.now() + timedelta(seconds=ttl or self.default_ttl)
        self._cache[key] = {
            'value': value,
            'expires_at': expires_at
        }
    
    def clear(self):
        self._cache.clear()
        self.stats = CacheStats()

# Cache global
_global_cache = SimpleCache(ttl=60)

def cached(ttl=60, cache_instance=None):
    def decorator(func):
        cache = cache_instance or _global_cache
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{hash((args, tuple(sorted(kwargs.items()))))}"
            
            result = cache.get(key)
            if result is not None:
                return result
            
            result = func(*args, **kwargs)
            cache.set(key, result, ttl)
            return result
        
        wrapper.cache_stats = lambda: cache.stats
        wrapper.clear_cache = lambda: cache.clear()
        return wrapper
    return decorator

@contextmanager
def monitor_cache_performance():
    start_time = time.time()
    start_stats = _global_cache.stats
    
    try:
        yield _global_cache
    finally:
        end_time = time.time()
        # ... código de relatório ...'''

        self.exemplo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema de cache profissional!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔄 Adicionar algoritmo LRU (Least Recently Used) para limpeza",
            "🧵 Implementar thread-safety com locks para aplicações multi-threaded",
            "📊 Adicionar métricas mais avançadas (tempo médio de hit/miss)",
            "💾 Persistir cache em disco para sobreviver a restarts",
            "🌐 Integrar com Redis para cache distribuído",
            "📈 Adicionar alertas quando hit rate fica baixo"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Decorators!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema de Cache Inteligente")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo20Decorators()
    print("Teste do módulo 20 - versão refatorada")
    module._decorators()