#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 14: Módulos e Pacotes
Aprenda a organizar e reutilizar código como um profissional
"""

from ..shared.base_module import BaseModule


class Modulo14ModulosPacotes(BaseModule):
    """Módulo 14: Dominando Módulos e Pacotes"""
    
    def __init__(self):
        super().__init__("modulo_14", "Módulos e Pacotes")
        self.has_mini_project = True
        self.mini_project_points = 85
    
    def execute(self) -> None:
        """Executa o módulo Módulos e Pacotes"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._modulos_pacotes_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _modulos_pacotes_interativo(self) -> None:
        """Conteúdo principal do módulo Módulos e Pacotes"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📦 MÓDULO 14: DOMINANDO MÓDULOS E PACOTES")
        else:
            print("\n" + "="*50)
            print("📦 MÓDULO 14: DOMINANDO MÓDULOS E PACOTES")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos aprender a organizar código como os profissionais do Vale do Silício!")
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
            self._mini_projeto_sistema_bibliotecas()
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
                'id': 'secao_conceito_modulos',
                'titulo': '🎯 O que são módulos e por que usar?',
                'descricao': 'Entenda o poder da modularização',
                'funcao': self._secao_conceito_modulos
            },
            {
                'id': 'secao_importacao_basica',
                'titulo': '⚙️ Como importar e usar módulos?',
                'descricao': 'Domine diferentes formas de importação',
                'funcao': self._secao_importacao_basica
            },
            {
                'id': 'secao_criando_modulos',
                'titulo': '🔧 Criando seus próprios módulos',
                'descricao': 'Organize seu código profissionalmente',
                'funcao': self._secao_criando_modulos
            },
            {
                'id': 'secao_bibliotecas_populares',
                'titulo': '📚 Bibliotecas essenciais do Python',
                'descricao': 'Conheça as ferramentas mais usadas',
                'funcao': self._secao_bibliotecas_populares
            },
            {
                'id': 'secao_pip_instalacao',
                'titulo': '🛠️ Instalando e gerenciando pacotes',
                'descricao': 'Pip, ambientes virtuais e boas práticas',
                'funcao': self._secao_pip_instalacao
            },
            {
                'id': 'secao_estrutura_projetos',
                'titulo': '📁 Estrutura profissional de projetos',
                'descricao': 'Como organizar projetos grandes',
                'funcao': self._secao_estrutura_projetos
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre o ecossistema Python',
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
    
    def _secao_conceito_modulos(self) -> None:
        """Seção: O que são módulos e por que usar?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO MÓDULOS E POR QUE USAR?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Módulo",
            "Um arquivo .py que contém funções, classes e variáveis que podem ser reutilizadas em outros programas"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Módulos são como 'caixas de ferramentas' - você pega só o que precisa!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você está montando um móvel. Em vez de fazer cada parafuso do zero, você usa uma caixa de ferramentas pronta. Módulos são como essa caixa - código pronto para usar!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você escreve funções úteis em um arquivo .py (ex: calculadora.py)",
            "2. Em outro programa, você 'importa' essas funções",
            "3. Agora pode usar as funções sem reescrever o código",
            "4. Se precisar corrigir algo, muda só no arquivo original"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Módulos mais usados no Python
import math     # Funções matemáticas
import random   # Números aleatórios
import datetime # Data e hora

print("=== DEMONSTRANDO MÓDULOS ===")
print(f"📐 Raiz quadrada de 16: {math.sqrt(16)}")
print(f"🎲 Número aleatório 1-10: {random.randint(1, 10)}")
print(f"📅 Data atual: {datetime.date.today()}")

# Cada módulo tem dezenas de funções prontas!'''
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏢 Netflix usa módulos para separar login, streaming, recomendações",
            "🚗 Tesla organiza código em módulos: bateria, motor, navegação",
            "📱 Instagram separa stories, feed, mensagens em módulos diferentes",
            "🎮 Jogos dividem: gráficos, áudio, física em módulos separados"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_importacao_basica(self) -> None:
        """Seção: Como importar e usar módulos?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO IMPORTAR E USAR MÓDULOS?", "⚙️", "success")
        
        exemplos = [
            {
                'titulo': 'IMPORTAÇÃO COMPLETA: import módulo',
                'descricao': 'Importa o módulo inteiro - precisa usar módulo.função()',
                'codigo': '''import math
import random
import datetime

print("=== IMPORTAÇÃO COMPLETA ===")
print(f"📐 Pi: {math.pi}")
print(f"📐 Raiz de 25: {math.sqrt(25)}")
print(f"🎲 Número aleatório: {random.randint(1, 100)}")
print(f"📅 Agora: {datetime.datetime.now().strftime('%H:%M:%S')}")

# Vantagem: Fica claro de onde vem cada função
# Desvantagem: Nome fica longo''',
                'explicacao': 'Use quando quiser deixar claro a origem de cada função'
            },
            {
                'titulo': 'IMPORTAÇÃO ESPECÍFICA: from módulo import função',
                'descricao': 'Importa só o que você precisa - usa direto a função',
                'codigo': '''from math import pi, sqrt, sin, cos
from random import randint, choice, shuffle
from datetime import datetime, date

print("=== IMPORTAÇÃO ESPECÍFICA ===")
print(f"📐 Pi sem 'math.': {pi}")
print(f"📐 Raiz sem 'math.': {sqrt(36)}")
print(f"🎲 Número sem 'random.': {randint(1, 50)}")
print(f"📅 Data sem 'datetime.': {date.today()}")

# Vantagem: Código mais limpo
# Cuidado: Pode confundir de onde vem a função''',
                'explicacao': 'Use quando você conhece bem o módulo e quer código mais limpo'
            },
            {
                'titulo': 'APELIDOS: import módulo as apelido',
                'descricao': 'Dá um nome mais curto para módulos com nomes longos',
                'codigo': '''import datetime as dt
import random as rand

print("=== USANDO APELIDOS ===")
print(f"📅 Com apelido: {dt.date.today()}")
print(f"🎲 Com apelido: {rand.randint(1, 10)}")

# Apelidos famosos da comunidade Python:
print("\\n🌟 APELIDOS FAMOSOS:")
print("• matplotlib.pyplot as plt (gráficos)")
print("• pandas as pd (análise de dados)")
print("• numpy as np (computação científica)")
print("• tensorflow as tf (machine learning)")''',
                'explicacao': 'Padrão da comunidade - todos usam os mesmos apelidos'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.exemplo(exemplo['codigo'])
            print(f"\n🚀 Executando exemplo {i}:")
            self.executar_codigo(exemplo['codigo'])
            
            if exemplo['explicacao']:
                self.print_colored(f"\n💡 QUANDO USAR: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você domina as 3 formas principais de importar!")
        self.pausar()
    
    def _secao_criando_modulos(self) -> None:
        """Seção: Criando seus próprios módulos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CRIANDO SEUS PRÓPRIOS MÓDULOS", "🔧", "info")
        
        self.print_colored("Vamos criar um módulo de utilidades que você pode usar em seus projetos!", "text")
        
        codigo_modulo = '''# Este seria o conteúdo do arquivo 'meu_modulo_util.py'

# === FUNÇÕES MATEMÁTICAS ===
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    imc = peso / (altura ** 2)
    
    # Determina categoria
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal" 
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return round(imc, 1), categoria

def converter_temperatura(valor, origem, destino):
    """Converte temperaturas entre C, F e K"""
    # Converte tudo para Celsius primeiro
    if origem == "F":
        celsius = (valor - 32) * 5/9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        celsius = valor
    
    # Converte para o destino
    if destino == "F":
        return round(celsius * 9/5 + 32, 1)
    elif destino == "K":
        return round(celsius + 273.15, 1)
    else:
        return round(celsius, 1)

# === FUNÇÕES DE TEXTO ===
def gerar_senha(tamanho=8, incluir_simbolos=True):
    """Gera uma senha aleatória segura"""
    import random
    import string
    
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%&*"
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def formatar_cpf(cpf):
    """Formata um CPF no padrão XXX.XXX.XXX-XX"""
    # Remove tudo que não é número
    numeros = ''.join(filter(str.isdigit, cpf))
    
    if len(numeros) != 11:
        return "CPF inválido"
    
    return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"

# === CONSTANTES DO MÓDULO ===
VERSAO = "1.0.0"
AUTOR = "Seu Nome"
DATA_CRIACAO = "2024"

# === DEMONSTRAÇÃO DAS FUNÇÕES ===
print("=== TESTANDO NOSSO MÓDULO PERSONALIZADO ===")

# Teste IMC
imc, categoria = calcular_imc(70, 1.75)
print(f"💪 IMC: {imc} - {categoria}")

# Teste conversão de temperatura
temp_f = converter_temperatura(25, "C", "F")
print(f"🌡️ 25°C = {temp_f}°F")

# Teste geração de senha
senha = gerar_senha(12)
print(f"🔐 Senha gerada: {senha}")

# Teste formatação de CPF
cpf_formatado = formatar_cpf("12345678901")
print(f"📄 CPF formatado: {cpf_formatado}")

print(f"\\n📋 Módulo {AUTOR} v{VERSAO} ({DATA_CRIACAO})")
print("✅ Todas as funções testadas com sucesso!")'''
        
        self.exemplo(codigo_modulo)
        print("\n🚀 Vamos ver nosso módulo funcionando:")
        self.executar_codigo(codigo_modulo)
        
        # === COMO USAR EM OUTROS ARQUIVOS ===
        self.print_colored("\n📁 COMO USAR EM OUTROS ARQUIVOS:", "warning")
        codigo_uso = '''# Em outro arquivo .py, você usaria assim:

# Importação completa
import meu_modulo_util
resultado = meu_modulo_util.calcular_imc(80, 1.80)

# Importação específica  
from meu_modulo_util import gerar_senha, formatar_cpf
senha = gerar_senha(16)
cpf = formatar_cpf("11122233344")

# Com apelido
import meu_modulo_util as util
temp = util.converter_temperatura(30, "C", "F")

print("🎯 Seu código fica organizado e reutilizável!")'''
        
        self.exemplo(codigo_uso)
        
        self.print_colored("\n💡 VANTAGENS DOS MÓDULOS PRÓPRIOS:", "success")
        vantagens = [
            "♻️ Reutilização: Escreve uma vez, usa em vários projetos",
            "🗂️ Organização: Cada tipo de função no seu arquivo",
            "🐛 Manutenção: Corrige em um lugar, funciona em todos",
            "👥 Colaboração: Facilita trabalho em equipe",
            "🚀 Velocidade: Desenvolve projetos mais rápido"
        ]
        for vantagem in vantagens:
            self.print_colored(f"• {vantagem}", "primary")
        
        self.pausar()
    
    def _secao_bibliotecas_populares(self) -> None:
        """Seção: Bibliotecas essenciais do Python"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("BIBLIOTECAS ESSENCIAIS DO PYTHON", "📚", "accent")
        
        self.print_colored("O Python é poderoso por sua comunidade! Conheça as bibliotecas mais usadas:", "text")
        
        codigo_bibliotecas = '''# === MAPA DAS BIBLIOTECAS PYTHON ===

bibliotecas = {
    "🏗️ Já vem com Python (Biblioteca Padrão)": {
        "os": "Interagir com sistema operacional (arquivos, pastas)",
        "sys": "Configurações do sistema Python",
        "json": "Trabalhar com dados JSON (APIs, configs)",
        "re": "Expressões regulares (busca avançada em texto)",
        "datetime": "Trabalhar com datas e horários",
        "random": "Números aleatórios e escolhas",
        "math": "Funções matemáticas avançadas",
        "urllib": "Fazer requisições web básicas",
        "sqlite3": "Banco de dados SQLite integrado",
        "tkinter": "Interface gráfica básica"
    },
    
    "📊 Ciência de Dados & IA": {
        "pandas": "Manipular planilhas e dados (Excel do Python)",
        "numpy": "Computação numérica e arrays",
        "matplotlib": "Criar gráficos e visualizações",
        "seaborn": "Gráficos estatísticos bonitos",
        "scikit-learn": "Machine Learning (IA simples)",
        "tensorflow": "Deep Learning (IA avançada)",
        "jupyter": "Notebooks interativos para análise"
    },
    
    "🌐 Desenvolvimento Web": {
        "requests": "Fazer requisições HTTP facilmente",
        "flask": "Framework web simples e rápido",
        "django": "Framework web completo (Instagram usa!)",
        "fastapi": "APIs modernas super rápidas",
        "beautifulsoup4": "Extrair dados de sites (web scraping)",
        "selenium": "Automatizar navegadores web"
    },
    
    "🖥️ Interface Gráfica & Desktop": {
        "tkinter": "Interface básica (já vem com Python)",
        "PyQt5/PySide2": "Interfaces profissionais (Spotify usa!)",
        "kivy": "Apps para celular Android/iOS",
        "pygame": "Criar jogos 2D"
    },
    
    "🔧 Ferramentas & Utilidades": {
        "pillow": "Editar e manipular imagens",
        "openpyxl": "Trabalhar com arquivos Excel",
        "cryptography": "Criptografia e segurança",
        "schedule": "Agendar tarefas automáticas",
        "click": "Criar programas de linha de comando"
    }
}

print("🐍 ECOSSISTEMA PYTHON - SUAS FERRAMENTAS PODEROSAS\\n")

for categoria, libs in bibliotecas.items():
    print(f"\\n{categoria}:")
    print("="*50)
    
    for nome, descricao in libs.items():
        print(f"📦 {nome:15} - {descricao}")

print("\\n💡 DICAS IMPORTANTES:")
print("🔸 Bibliotecas padrão: Já instaladas, use import diretamente")
print("🔸 Bibliotecas externas: Use 'pip install nome_biblioteca'")
print("🔸 Procure sempre na documentação oficial primeiro")
print("🔸 GitHub é ótimo para ver exemplos de uso")

print("\\n🚀 PRÓXIMOS PASSOS:")
print("1. Escolha uma área que te interessa")
print("2. Instale 2-3 bibliotecas dessa área")
print("3. Faça pequenos projetos para praticar")
print("4. Explore a documentação e exemplos")

print("\\n🌟 O Python tem mais de 300.000 bibliotecas disponíveis!")'''
        
        self.exemplo(codigo_bibliotecas)
        print("\n🚀 Executando mapa de bibliotecas:")
        self.executar_codigo(codigo_bibliotecas)
        
        self.pausar()
    
    def _secao_pip_instalacao(self) -> None:
        """Seção: Instalando e gerenciando pacotes"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("INSTALANDO E GERENCIANDO PACOTES", "🛠️", "warning")
        
        self.print_colored("O pip é o 'gerente de bibliotecas' do Python. Vamos dominar!", "text")
        
        codigo_pip = '''# === GUIA COMPLETO DO PIP ===

print("🛠️ PIP: O GERENCIADOR DE PACOTES DO PYTHON\\n")

# Comandos principais do pip (executados no terminal)
comandos_pip = {
    "Instalação": [
        "pip install requests                 # Instala uma biblioteca",
        "pip install pandas numpy matplotlib  # Instala várias de uma vez",
        "pip install django==3.2             # Versão específica",
        "pip install 'requests>=2.0,<3.0'    # Range de versões"
    ],
    
    "Informações": [
        "pip list                            # Lista tudo instalado",
        "pip show requests                   # Detalhes de uma biblioteca",
        "pip search machine learning         # Busca por termo",
        "pip freeze                          # Lista com versões exatas"
    ],
    
    "Atualização": [
        "pip install --upgrade requests      # Atualiza uma biblioteca",
        "pip install --upgrade pip           # Atualiza o próprio pip",
        "pip list --outdated                 # Mostra o que pode atualizar"
    ],
    
    "Desinstalação": [
        "pip uninstall requests              # Remove uma biblioteca",
        "pip uninstall -y requests           # Remove sem confirmar"
    ],
    
    "Ambientes Virtuais (IMPORTANTE!)": [
        "python -m venv meu_projeto          # Cria ambiente virtual",
        "meu_projeto\\\\Scripts\\\\activate         # Ativa (Windows)",
        "source meu_projeto/bin/activate     # Ativa (Linux/Mac)",
        "pip install flask                   # Instala só neste projeto",
        "deactivate                          # Desativa ambiente"
    ]
}

for categoria, comandos in comandos_pip.items():
    print(f"\\n🔹 {categoria}:")
    print("-" * 50)
    for comando in comandos:
        print(f"  {comando}")

# Demonstração prática
print("\\n💻 DEMONSTRAÇÃO PRÁTICA:\\n")

# Simulando verificação de bibliotecas instaladas
import sys
bibliotecas_teste = ['os', 'sys', 'json', 'math', 'random', 'datetime']

print("✅ BIBLIOTECAS PADRÃO DISPONÍVEIS:")
for lib in bibliotecas_teste:
    try:
        __import__(lib)
        print(f"📦 {lib:10} - Instalada ✅")
    except ImportError:
        print(f"📦 {lib:10} - Não encontrada ❌")

# Dicas importantes sobre versões
print(f"\\n🐍 VERSÃO DO PYTHON: {sys.version.split()[0]}")
print(f"📍 LOCAL DE INSTALAÇÃO: {sys.executable}")

print("\\n⚠️ DICAS IMPORTANTES:")
dicas = [
    "Sempre use ambientes virtuais para projetos diferentes",
    "Mantenha um arquivo requirements.txt com suas dependências",
    "Atualize regularmente, mas teste antes em produção",
    "Use pip freeze > requirements.txt para exportar",
    "pip install -r requirements.txt para instalar de arquivo"
]

for i, dica in enumerate(dicas, 1):
    print(f"{i}. {dica}")

print("\\n🎯 FLUXO PROFISSIONAL:")
fluxo = [
    "1. Criar ambiente virtual para o projeto",
    "2. Ativar o ambiente", 
    "3. Instalar bibliotecas necessárias",
    "4. Desenvolver o projeto",
    "5. Exportar dependências (requirements.txt)",
    "6. Compartilhar projeto com requirements.txt"
]

for passo in fluxo:
    print(f"   {passo}")

print("\\n🌟 Com isso você gerencia bibliotecas como um profissional!")'''
        
        self.exemplo(codigo_pip)
        print("\n🚀 Executando guia do pip:")
        self.executar_codigo(codigo_pip)
        
        self.pausar()
    
    def _secao_estrutura_projetos(self) -> None:
        """Seção: Estrutura profissional de projetos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ESTRUTURA PROFISSIONAL DE PROJETOS", "📁", "info")
        
        self.print_colored("Como organizar seus projetos Python como as grandes empresas!", "text")
        
        codigo_estrutura = '''# === ESTRUTURA PROFISSIONAL DE PROJETOS PYTHON ===

print("📁 COMO ORGANIZAR PROJETOS PYTHON PROFISSIONALMENTE\\n")

# Estrutura recomendada para projetos
estrutura_projeto = """
meu_projeto/
│
├── 📁 src/                    # Código fonte principal
│   ├── 📄 __init__.py         # Torna pasta um pacote Python
│   ├── 📄 main.py            # Arquivo principal de execução
│   ├── 📁 models/            # Classes e modelos de dados
│   │   ├── 📄 __init__.py
│   │   ├── 📄 user.py
│   │   └── 📄 product.py
│   ├── 📁 services/          # Lógica de negócio
│   │   ├── 📄 __init__.py
│   │   ├── 📄 auth_service.py
│   │   └── 📄 data_service.py
│   ├── 📁 utils/             # Funções auxiliares
│   │   ├── 📄 __init__.py
│   │   ├── 📄 helpers.py
│   │   └── 📄 validators.py
│   └── 📁 config/            # Configurações
│       ├── 📄 __init__.py
│       └── 📄 settings.py
│
├── 📁 tests/                 # Testes automatizados
│   ├── 📄 __init__.py
│   ├── 📄 test_models.py
│   ├── 📄 test_services.py
│   └── 📄 test_utils.py
│
├── 📁 docs/                  # Documentação
│   ├── 📄 README.md
│   ├── 📄 INSTALL.md
│   └── 📄 API.md
│
├── 📁 data/                  # Arquivos de dados
│   ├── 📄 sample.csv
│   └── 📄 config.json
│
├── 📁 scripts/               # Scripts utilitários
│   ├── 📄 setup.py
│   └── 📄 deploy.py
│
├── 📄 requirements.txt       # Dependências do projeto
├── 📄 .gitignore            # Arquivos ignorados pelo Git
├── 📄 .env                  # Variáveis de ambiente
├── 📄 LICENSE               # Licença do projeto
└── 📄 README.md             # Documentação principal
"""

print("🏗️ ESTRUTURA RECOMENDADA:")
print(estrutura_projeto)

# Exemplos de diferentes tipos de projeto
tipos_projeto = {
    "🌐 Aplicação Web (Flask/Django)": {
        "pastas_extras": ["templates/", "static/", "migrations/"],
        "arquivos_extras": ["app.py", "wsgi.py", "gunicorn.conf.py"],
        "exemplo": "Site de e-commerce, blog, API REST"
    },
    
    "📊 Projeto de Ciência de Dados": {
        "pastas_extras": ["notebooks/", "data/raw/", "data/processed/", "models/"],
        "arquivos_extras": ["analysis.ipynb", "train.py", "predict.py"],
        "exemplo": "Análise de vendas, ML para previsões"
    },
    
    "🖥️ Aplicação Desktop": {
        "pastas_extras": ["ui/", "resources/", "assets/"],
        "arquivos_extras": ["main_window.py", "setup.py", "build.py"],
        "exemplo": "Editor de texto, calculadora, sistema"
    },
    
    "📦 Biblioteca/Pacote": {
        "pastas_extras": ["examples/", "tutorials/"],
        "arquivos_extras": ["setup.py", "MANIFEST.in", "pyproject.toml"],
        "exemplo": "Requests, Pandas, suas próprias libs"
    }
}

print("\\n🎯 ESTRUTURAS POR TIPO DE PROJETO:\\n")

for tipo, detalhes in tipos_projeto.items():
    print(f"{tipo}:")
    print(f"  📁 Pastas extras: {', '.join(detalhes['pastas_extras'])}")
    print(f"  📄 Arquivos extras: {', '.join(detalhes['arquivos_extras'])}")
    print(f"  💡 Exemplo: {detalhes['exemplo']}")
    print()

# Boas práticas
print("✅ BOAS PRÁTICAS PROFISSIONAIS:\\n")
boas_praticas = [
    "📝 README.md claro explicando o projeto",
    "📋 requirements.txt com todas as dependências",
    "🔒 .env para dados sensíveis (senhas, chaves API)",
    "🚫 .gitignore para não versionar arquivos desnecessários",
    "🧪 Pasta tests/ com testes automatizados",
    "📚 Documentação na pasta docs/",
    "🔄 Controle de versão com Git",
    "🏷️ Versionamento semântico (v1.0.0, v1.1.0, etc)",
    "📦 __init__.py em todas as pastas de código",
    "🔧 Configurações centralizadas em config/"
]

for pratica in boas_praticas:
    print(f"  {pratica}")

print("\\n🌟 BENEFÍCIOS DA BOA ORGANIZAÇÃO:")
beneficios = [
    "🤝 Facilita trabalho em equipe",
    "🔍 Código fácil de encontrar e entender", 
    "🐛 Bugs mais fáceis de identificar",
    "📈 Projeto escala melhor",
    "♻️ Componentes reutilizáveis",
    "🚀 Deploy e manutenção mais simples",
    "💼 Parece profissional para empregadores"
]

for beneficio in beneficios:
    print(f"  {beneficio}")

print("\\n💡 DICA FINAL: Comece simples e evolua a estrutura conforme o projeto cresce!")'''
        
        self.exemplo(codigo_estrutura)
        print("\n🚀 Executando guia de estrutura:")
        self.executar_codigo(codigo_estrutura)
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre o ecossistema Python"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES SOBRE O ECOSSISTEMA PYTHON", "💫", "accent")
        
        self.print_colored("Fatos interessantes que vão te motivar ainda mais!", "text")
        
        codigo_curiosidades = '''# === CURIOSIDADES INCRÍVEIS SOBRE PYTHON ===

print("💫 FATOS INTERESSANTES SOBRE O ECOSSISTEMA PYTHON\\n")

curiosidades = {
    "🎭 Origem do Nome": [
        "Python não tem nada a ver com cobra!",
        "O nome vem do grupo de comédia 'Monty Python'",
        "Guido van Rossum (criador) era fã do grupo",
        "Por isso muitos exemplos usam 'spam' e 'eggs'"
    ],
    
    "📈 Números Impressionantes": [
        "🏆 Linguagem #1 mais popular do mundo (2024)",
        "📦 Mais de 500.000 bibliotecas no PyPI",
        "💰 Salário médio: R$ 8.000-15.000 (Brasil)",
        "🌐 Usada por 8.2 milhões de desenvolvedores",
        "📊 48% dos cientistas de dados usam Python"
    ],
    
    "🏢 Empresas Famosas que Usam": [
        "🎬 Netflix - Sistema de recomendações",
        "🔍 Google - Buscador, YouTube, Gmail",
        "📷 Instagram - Backend completo",
        "🎵 Spotify - Análise de dados e recomendações",
        "🚗 Tesla - Software dos carros",
        "🛸 NASA - Análise de dados espaciais",
        "💰 Bank of America - Análise financeira",
        "🎮 Eve Online - Servidor do jogo"
    ],
    
    "🌟 Conquistas Históricas": [
        "🕳️ Primeira foto de buraco negro (Event Horizon)",
        "🚀 Software da SpaceX usa Python",
        "🦠 Análise genética do COVID-19",
        "🔬 Descoberta do Bóson de Higgs (CERN)",
        "🌌 Controle do telescópio Hubble",
        "🎯 Algoritmos do YouTube"
    ],
    
    "📚 Bibliotecas com Histórias Incríveis": [
        "📊 NumPy: Criada por um estudante de doutorado",
        "🐼 Pandas: Nome significa 'Panel Data'", 
        "🎨 Matplotlib: Inspirada no MATLAB",
        "⚡ Django: Nomeada em homenagem ao guitarrista Django Reinhardt",
        "🌶️ Flask: Nome vem de 'micro-framework'",
        "🚀 Requests: 'HTTP para humanos'"
    ],
    
    "💡 Filosofia Python (The Zen of Python)": [
        "'Simples é melhor que complexo'",
        "'Legibilidade conta'",
        "'Deve haver uma forma óbvia de fazer'",
        "'Agora é melhor que nunca'",
        "'Se a implementação é difícil de explicar, é má'"
    ]
}

for categoria, fatos in curiosidades.items():
    print(f"\\n{categoria}:")
    print("=" * 50)
    for fato in fatos:
        print(f"  • {fato}")
    print()

# Timeline interessante
print("📅 LINHA DO TEMPO PYTHON:\\n")
timeline = {
    "1989": "🎯 Guido van Rossum começa a criar Python",
    "1991": "🐍 Python 0.9.0 - Primeira versão pública",
    "2000": "🚀 Python 2.0 - List comprehensions",
    "2008": "⚡ Python 3.0 - Quebra compatibilidade, mas melhora tudo",
    "2010": "📊 NumPy e SciPy se tornam populares",
    "2011": "🌐 Django alimenta Instagram (2010) e Spotify",
    "2015": "🤖 TensorFlow lançado pelo Google",
    "2020": "📈 Python vira linguagem #1 do mundo",
    "2024": "🎉 Você está aprendendo a linguagem do futuro!"
}

for ano, evento in timeline.items():
    print(f"  {ano}: {evento}")

print("\\n🎯 POR QUE PYTHON É TÃO POPULAR?")
razoes = [
    "📖 Sintaxe simples - parece inglês",
    "🔧 'Baterias incluídas' - muita coisa já vem pronta",
    "🌐 Comunidade incrível e acolhedora",
    "📚 Documentação excelente",
    "🚀 Rápido para prototipar e testar ideias",
    "🔬 Perfeito para ciência e IA",
    "💼 Alta demanda no mercado de trabalho",
    "🎓 Fácil de aprender, difícil de dominar"
]

for razao in razoes:
    print(f"  {razao}")

print("\\n💪 VOCÊ ESTÁ NO CAMINHO CERTO!")
print("Python não é apenas uma linguagem, é uma comunidade global")
print("que está moldando o futuro da tecnologia. Bem-vindo(a) ao clube! 🎉")

print("\\n🌟 PRÓXIMOS PASSOS NA SUA JORNADA:")
proximo_passos = [
    "1. 🎯 Domine os fundamentos (você já está fazendo!)",
    "2. 🛠️ Escolha uma área: Web, IA, Data Science, Automação",
    "3. 🚀 Faça projetos práticos no GitHub",
    "4. 🤝 Participe da comunidade Python Brasil",
    "5. 💼 Candidate-se a vagas Python (sim, você consegue!)"
]

for passo in proximo_passos:
    print(f"  {passo}")

print("\\n🐍 Lembre-se: Toda jornada de mil milhas começa com um único passo!")'''
        
        self.exemplo(codigo_curiosidades)
        print("\n🚀 Executando curiosidades:")
        self.executar_codigo(codigo_curiosidades)
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre módulos e pacotes!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Módulos e Pacotes',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual comando é usado para instalar uma biblioteca externa no Python?',
                        'answer': ['pip install', 'pip install biblioteca', 'pip'],
                        'hint': 'É o gerenciador de pacotes do Python'
                    },
                    {
                        'question': 'Como você importa apenas a função sqrt do módulo math?',
                        'answer': ['from math import sqrt'],
                        'hint': 'Use from ... import ...'
                    },
                    {
                        'question': 'O que significa o arquivo __init__.py em uma pasta?',
                        'answer': ['torna a pasta um pacote', 'pacote python', 'pacote'],
                        'hint': 'Relacionado a organização de código em pacotes'
                    },
                    {
                        'question': 'Qual biblioteca é mais usada para manipular dados como Excel?',
                        'answer': ['pandas', 'pd'],
                        'hint': 'Tem nome de animal preto e branco'
                    },
                    {
                        'question': 'Como criar um ambiente virtual chamado "projeto"?',
                        'answer': ['python -m venv projeto', 'venv projeto'],
                        'hint': 'Use python -m venv seguido do nome'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a importação do módulo datetime',
                        'starter': '# Complete a importação\n# ______ datetime\nprint(datetime.date.today())',
                        'solution': 'import',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a importação específica',
                        'starter': '# Complete para importar apenas randint\n# from random ______ randint\nprint(randint(1, 10))',
                        'solution': 'import',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a instalação de biblioteca',
                        'starter': '# Como instalar a biblioteca requests?\n# ______ install requests',
                        'solution': 'pip',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Criando seu Módulo Utilitário',
                'type': 'creative',
                'instruction': 'Crie um módulo com 3 funções úteis para seu dia a dia (ex: calculadora, formatador de texto, gerador de senha)'
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
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre módulos e pacotes",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios sobre importação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie seu próprio módulo utilitário",
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
    
    def _mini_projeto_sistema_bibliotecas(self) -> None:
        """Mini Projeto - Módulo 14: Sistema Inteligente de Bibliotecas"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA INTELIGENTE DE BIBLIOTECAS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA INTELIGENTE DE BIBLIOTECAS")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema que gerencia bibliotecas Python como um profissional!")
        
        self.print_concept(
            "Sistema Inteligente de Bibliotecas",
            "Um programa que analisa, instala, atualiza e organiza bibliotecas Python automaticamente"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "🏢 Empresas que gerenciam múltiplos projetos Python",
            "🎓 Escolas que precisam manter ambientes atualizados",
            "👥 Equipes de desenvolvimento que compartilham dependências",
            "🚀 DevOps que automatizam deployments"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Análise do ambiente atual
        self.print_section("PASSO 1: Analisando o Ambiente Python", "📝", "info")
        self.print_tip("Primeiro vamos mapear tudo que está instalado")
        
        try:
            # === CÓDIGO PRINCIPAL DO PROJETO ===
            codigo_projeto = '''# 📚 SISTEMA INTELIGENTE DE BIBLIOTECAS
# Gerenciador avançado de dependências Python

import sys
import pkg_resources
import subprocess
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# === 1. ANALISADOR DE AMBIENTE ===
class PythonEnvironmentAnalyzer:
    """Analisa o ambiente Python atual"""
    
    def __init__(self):
        self.installed_packages = {}
        self.python_info = {}
        self.environment_health = {}
    
    def analyze_environment(self) -> Dict:
        """Análise completa do ambiente Python"""
        print("🔍 ANALISANDO AMBIENTE PYTHON...\\n")
        
        # Informações do Python
        self.python_info = {
            "version": sys.version.split()[0],
            "executable": sys.executable,
            "platform": sys.platform,
            "path": sys.path[:3]  # Primeiros 3 caminhos
        }
        
        print(f"🐍 Python: {self.python_info['version']}")
        print(f"📍 Localização: {self.python_info['executable']}")
        print(f"💻 Plataforma: {self.python_info['platform']}")
        
        # Pacotes instalados
        self._scan_installed_packages()
        
        # Análise de saúde
        self._analyze_health()
        
        return {
            "python_info": self.python_info,
            "packages": self.installed_packages,
            "health": self.environment_health
        }
    
    def _scan_installed_packages(self) -> None:
        """Escaneia todos os pacotes instalados"""
        print("\\n📦 ESCANEANDO PACOTES INSTALADOS...")
        
        # Simula pacotes instalados (em ambiente real usaria pkg_resources)
        mock_packages = {
            "pip": "23.0.1",
            "setuptools": "65.5.0", 
            "wheel": "0.38.4",
            "requests": "2.28.1",
            "numpy": "1.24.1",
            "pandas": "1.5.3",
            "matplotlib": "3.6.2",
            "flask": "2.2.2",
            "django": "4.1.5"
        }
        
        self.installed_packages = mock_packages
        
        print(f"✅ Encontrados {len(self.installed_packages)} pacotes")
        
        # Categorizar por tipo
        categories = self._categorize_packages()
        
        for category, packages in categories.items():
            if packages:
                print(f"\\n📂 {category}:")
                for pkg, version in packages.items():
                    print(f"  • {pkg:15} v{version}")
    
    def _categorize_packages(self) -> Dict[str, Dict[str, str]]:
        """Categoriza pacotes por função"""
        categories = {
            "🔧 Ferramentas Base": {},
            "📊 Ciência de Dados": {},
            "🌐 Web Development": {},
            "🎨 Visualização": {},
            "🔨 Utilitários": {}
        }
        
        # Mapeamento simples (em projeto real seria mais sofisticado)
        category_map = {
            "pip": "🔧 Ferramentas Base",
            "setuptools": "🔧 Ferramentas Base",
            "wheel": "🔧 Ferramentas Base",
            "numpy": "📊 Ciência de Dados",
            "pandas": "📊 Ciência de Dados",
            "matplotlib": "🎨 Visualização",
            "flask": "🌐 Web Development",
            "django": "🌐 Web Development",
            "requests": "🔨 Utilitários"
        }
        
        for package, version in self.installed_packages.items():
            category = category_map.get(package, "🔨 Utilitários")
            categories[category][package] = version
        
        return categories
    
    def _analyze_health(self) -> None:
        """Analisa a saúde do ambiente"""
        print("\\n🏥 ANÁLISE DE SAÚDE DO AMBIENTE...")
        
        health_score = 85  # Simulado
        outdated_count = 2  # Simulado
        security_issues = 0  # Simulado
        
        self.environment_health = {
            "score": health_score,
            "outdated_packages": outdated_count,
            "security_issues": security_issues,
            "recommendations": [
                "Atualize 2 pacotes desatualizados",
                "Considere usar ambiente virtual",
                "Documente dependências em requirements.txt"
            ]
        }
        
        print(f"📊 Pontuação de Saúde: {health_score}/100")
        
        if health_score >= 80:
            print("✅ Ambiente em boa condição!")
        elif health_score >= 60:
            print("⚠️ Ambiente precisa de alguns ajustes")
        else:
            print("❌ Ambiente precisa de atenção urgente")
        
        if outdated_count > 0:
            print(f"📈 {outdated_count} pacotes podem ser atualizados")
        
        if security_issues > 0:
            print(f"🔒 {security_issues} problemas de segurança encontrados")

# === 2. GERENCIADOR DE DEPENDÊNCIAS ===
class DependencyManager:
    """Gerencia instalação e atualização de dependências"""
    
    def __init__(self):
        self.package_database = self._load_package_database()
    
    def _load_package_database(self) -> Dict:
        """Carrega base de dados de pacotes populares"""
        return {
            "data_science": {
                "numpy": "Computação numérica fundamental",
                "pandas": "Manipulação e análise de dados",
                "matplotlib": "Visualização de dados básica",
                "seaborn": "Visualização estatística",
                "scikit-learn": "Machine Learning",
                "jupyter": "Notebooks interativos"
            },
            "web_development": {
                "flask": "Framework web minimalista",
                "django": "Framework web completo",
                "fastapi": "API moderna e rápida",
                "requests": "Cliente HTTP simples",
                "beautifulsoup4": "Web scraping"
            },
            "automation": {
                "selenium": "Automação de navegador",
                "schedule": "Agendamento de tarefas",
                "click": "Interface linha de comando",
                "python-dotenv": "Gerenciamento de variáveis de ambiente"
            },
            "utilities": {
                "pillow": "Processamento de imagens",
                "openpyxl": "Manipulação de Excel",
                "python-dateutil": "Manipulação avançada de datas",
                "tqdm": "Barras de progresso"
            }
        }
    
    def suggest_packages_for_project(self, project_type: str) -> List[str]:
        """Sugere pacotes para tipo de projeto"""
        suggestions = {
            "data_science": ["numpy", "pandas", "matplotlib", "jupyter"],
            "web_app": ["flask", "requests", "python-dotenv"],
            "automation": ["selenium", "schedule", "click"],
            "general": ["requests", "python-dateutil", "tqdm"]
        }
        
        return suggestions.get(project_type, suggestions["general"])
    
    def create_requirements_file(self, packages: List[str], filename: str = "requirements.txt") -> str:
        """Cria arquivo requirements.txt"""
        content = "# Dependências do projeto\\n"
        content += f"# Gerado em {datetime.now().strftime('%Y-%m-%d %H:%M')}\\n\\n"
        
        for package in packages:
            # Em projeto real, pegaria versões específicas
            content += f"{package}>=1.0.0\\n"
        
        return content
    
    def simulate_installation(self, packages: List[str]) -> Dict[str, bool]:
        """Simula instalação de pacotes"""
        results = {}
        
        print("\\n📦 SIMULANDO INSTALAÇÃO...")
        
        for package in packages:
            # Simula sucesso na maioria dos casos
            success = True  # Em projeto real: subprocess.run(["pip", "install", package])
            results[package] = success
            
            if success:
                print(f"✅ {package} instalado com sucesso")
            else:
                print(f"❌ Falha ao instalar {package}")
        
        return results

# === 3. ORGANIZADOR DE PROJETOS ===
class ProjectOrganizer:
    """Organiza estrutura de projetos Python"""
    
    def __init__(self):
        self.project_templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Carrega templates de estrutura de projeto"""
        return {
            "basic": [
                "src/",
                "src/__init__.py",
                "src/main.py",
                "tests/",
                "README.md",
                "requirements.txt",
                ".gitignore"
            ],
            "web_app": [
                "app/",
                "app/__init__.py",
                "app/routes.py",
                "app/models.py",
                "templates/",
                "static/",
                "config.py",
                "run.py",
                "requirements.txt"
            ],
            "data_science": [
                "data/raw/",
                "data/processed/",
                "notebooks/",
                "src/",
                "src/data_processing.py",
                "src/analysis.py",
                "models/",
                "requirements.txt",
                "README.md"
            ]
        }
    
    def generate_project_structure(self, project_name: str, template: str) -> str:
        """Gera estrutura de projeto"""
        if template not in self.project_templates:
            template = "basic"
        
        structure = f"{project_name}/\\n"
        
        for item in self.project_templates[template]:
            if item.endswith("/"):
                structure += f"├── 📁 {item}\\n"
            else:
                structure += f"├── 📄 {item}\\n"
        
        return structure
    
    def create_readme_template(self, project_name: str, description: str) -> str:
        """Cria template de README.md"""
        return f"""
# {project_name}

{description}

## Instalação

```bash
pip install -r requirements.txt
```

## Como usar

```python
python src/main.py
```

## Estrutura do projeto

- `src/` - Código fonte
- `tests/` - Testes automatizados  
- `requirements.txt` - Dependências

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

MIT License

"""

# === 4. DEMONSTRAÇÃO COMPLETA ===
print("📚 SISTEMA INTELIGENTE DE BIBLIOTECAS\\n")
print("Gerenciando dependências Python como um profissional!\\n")

# Inicializar componentes
analyzer = PythonEnvironmentAnalyzer()
dep_manager = DependencyManager()
project_organizer = ProjectOrganizer()

# PASSO 1: Análise do ambiente
print("=" * 60)
print("📊 PASSO 1: ANÁLISE DO AMBIENTE")
print("=" * 60)

environment_data = analyzer.analyze_environment()

# PASSO 2: Sugestões personalizadas
print("\\n" + "=" * 60)
print("💡 PASSO 2: SUGESTÕES INTELIGENTES")
print("=" * 60)

project_types = ["data_science", "web_app", "automation"]

for proj_type in project_types:
    suggestions = dep_manager.suggest_packages_for_project(proj_type)
    print(f"\\n🎯 Para projeto {proj_type.replace('_', ' ').title()}:")
    for package in suggestions:
        description = ""
        for category in dep_manager.package_database.values():
            if package in category:
                description = category[package]
                break
        print(f"  • {package:15} - {description}")

# PASSO 3: Criação de estrutura
print("\\n" + "=" * 60)
print("🏗️ PASSO 3: ORGANIZAÇÃO DE PROJETO")
print("=" * 60)

project_name = "meu_projeto_data_science"
structure = project_organizer.generate_project_structure(project_name, "data_science")
print(f"\\n📁 ESTRUTURA SUGERIDA PARA '{project_name}':")
print(structure)

# PASSO 4: Arquivo de dependências
print("\\n" + "=" * 60)
print("📝 PASSO 4: GERANDO REQUIREMENTS.TXT")
print("=" * 60)

packages_to_install = ["numpy", "pandas", "matplotlib", "jupyter"]
requirements_content = dep_manager.create_requirements_file(packages_to_install)
print("\\n📄 CONTEÚDO DO REQUIREMENTS.TXT:")
print(requirements_content)

# PASSO 5: Simulação de instalação
print("\\n" + "=" * 60)
print("⚙️ PASSO 5: INSTALAÇÃO AUTOMÁTICA")
print("=" * 60)

installation_results = dep_manager.simulate_installation(packages_to_install)
success_count = sum(installation_results.values())
print(f"\\n📊 RESULTADO: {success_count}/{len(packages_to_install)} pacotes instalados")

# PASSO 6: Relatório final
print("\\n" + "=" * 60)
print("📋 RELATÓRIO FINAL")
print("=" * 60)

print(f"\\n✅ AMBIENTE ANALISADO:")
print(f"  • Python {environment_data['python_info']['version']}")
print(f"  • {len(environment_data['packages'])} pacotes instalados")
print(f"  • Saúde: {environment_data['health']['score']}/100")

print(f"\\n🎯 PROJETO CONFIGURADO:")
print(f"  • Estrutura: {len(project_organizer.project_templates['data_science'])} arquivos/pastas")
print(f"  • Dependências: {len(packages_to_install)} pacotes")
print(f"  • Tipo: Ciência de Dados")

print(f"\\n🚀 PRÓXIMOS PASSOS:")
print("  1. Criar ambiente virtual: python -m venv meu_projeto")
print("  2. Ativar ambiente: meu_projeto\\\\Scripts\\\\activate")
print("  3. Instalar dependências: pip install -r requirements.txt")
print("  4. Começar a desenvolver!")

print("\\n🎉 SISTEMA FUNCIONANDO PERFEITAMENTE!")
print("💡 Conceitos aplicados:")
print("  • Análise de ambiente Python")
print("  • Gerenciamento de dependências")
print("  • Organização profissional de projetos")
print("  • Automação de tarefas repetitivas")
print("  • Boas práticas de desenvolvimento")
print("  • Sistema modular e extensível")

print("\\n🌟 Parabéns! Você criou um sistema profissional de gestão de bibliotecas!")'''
            
            # === CÓDIGO FINAL GERADO ===
            self.print_colored("Aqui está o código completo que você criou:", "text")
            
            self.exemplo(codigo_projeto)
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.executar_codigo(codigo_projeto)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema inteligente de bibliotecas!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Integrar com pip real para instalações automáticas",
            "Adicionar interface gráfica com tkinter ou PyQt",
            "Criar sistema de cache para análises rápidas",
            "Implementar detecção de vulnerabilidades",
            "Desenvolver API REST para uso em CI/CD",
            "Criar dashboard web com Flask/Django"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de Sistemas Python!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema Inteligente de Bibliotecas")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo14ModulosPacotes()
    print("Teste do módulo 14 - versão standalone")
    module._modulos_pacotes_interativo()