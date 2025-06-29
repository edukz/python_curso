#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 28: Estrutura de Projetos
Aprenda a organizar projetos Python profissionalmente
"""

import os
import time
from ..shared.base_module import BaseModule


class Modulo28EstruturaProjetos(BaseModule):
    """Módulo 28: Estrutura de Projetos - Organização Profissional"""
    
    def __init__(self):
        super().__init__("modulo_28", "Estrutura de Projetos")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre Estrutura de Projetos"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._estrutura_projetos_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _estrutura_projetos_principal(self) -> None:
        """Conteúdo principal do módulo estrutura de projetos"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 28: ESTRUTURA DE PROJETOS PYTHON")
        else:
            print("\n" + "="*60)
            print("🏗️ MÓDULO 28: ESTRUTURA DE PROJETOS PYTHON")
            print("="*60)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🏗️ Bem-vindo ao mundo da organização profissional de projetos! 🎉")
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
            self._mini_projeto_gerador_estruturas()
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
                'id': 'secao_conceito_estrutura',
                'titulo': '🎯 O que é estrutura de projeto?',
                'descricao': 'Entenda por que organização é fundamental',
                'funcao': self._secao_conceito_estrutura
            },
            {
                'id': 'secao_anatomia_projeto',
                'titulo': '🏗️ Anatomia de um projeto Python',
                'descricao': 'Veja a estrutura padrão passo a passo',
                'funcao': self._secao_anatomia_projeto
            },
            {
                'id': 'secao_gerenciamento_dependencias',
                'titulo': '📦 Gerenciamento de dependências',
                'descricao': 'requirements.txt, setup.py e ambientes virtuais',
                'funcao': self._secao_gerenciamento_dependencias
            },
            {
                'id': 'secao_documentacao_essencial',
                'titulo': '📚 Documentação essencial',
                'descricao': 'README, licenças e arquivos de configuração',
                'funcao': self._secao_documentacao_essencial
            },
            {
                'id': 'secao_organizacao_codigo',
                'titulo': '📁 Organização de código fonte',
                'descricao': 'Como estruturar módulos e pacotes',
                'funcao': self._secao_organizacao_codigo
            },
            {
                'id': 'secao_testes_scripts',
                'titulo': '🧪 Testes e scripts auxiliares',
                'descricao': 'Onde colocar testes e utilitários',
                'funcao': self._secao_testes_scripts
            },
            {
                'id': 'secao_boas_praticas',
                'titulo': '⭐ Boas práticas profissionais',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_boas_praticas
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
    
    def _secao_conceito_estrutura(self) -> None:
        """Seção: O que é estrutura de projeto?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É ESTRUTURA DE PROJETO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Estrutura de Projeto",
            "Uma organização padronizada de arquivos e pastas que torna o código fácil de entender, manter e compartilhar."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Uma boa estrutura economiza horas de trabalho e evita confusões!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine sua casa: você tem quartos específicos para cada coisa", "text")
        self.print_colored("- cozinha para comer, quarto para dormir, banheiro para higiene.", "text")
        self.print_colored("Um projeto Python funciona igual: cada pasta tem sua função!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 📁 Código fonte fica em src/ (como roupas no guarda-roupa)",
            "2. 🧪 Testes ficam em tests/ (como remédios no armário de medicina)",
            "3. 📚 Documentação fica em docs/ (como manuais na estante)",
            "4. ⚙️ Configurações ficam na raiz (como controles na mesa de centro)"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Google - Organiza projetos com milhões de linhas de código",
            "Microsoft - Mantém consistência entre milhares de desenvolvedores",
            "Netflix - Facilita manutenção de sistemas complexos",
            "Spotify - Permite colaboração eficiente entre equipes globais"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_anatomia_projeto(self) -> None:
        """Seção: Anatomia de um projeto Python"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ANATOMIA DE UM PROJETO PYTHON", "🏗️", "success")
        
        self.print_colored("🔍 Vamos dissecar um projeto profissional passo a passo:", "text")
        
        estrutura = """
🗂️  meu_projeto/
├── 📄 README.md              ← Cartão de visitas do projeto
├── 📝 LICENSE                ← Como outros podem usar seu código
├── 🚫 .gitignore            ← Arquivos que o Git deve ignorar
├── 📦 requirements.txt       ← Lista de dependências
├── ⚙️  setup.py             ← Configuração de instalação
├── 🔧 pyproject.toml        ← Configuração moderna Python
│
├── 📁 src/                   ← Todo o código fonte fica aqui
│   └── meu_projeto/
│       ├── 🐍 __init__.py   ← Marca como pacote Python
│       ├── 🚀 main.py       ← Ponto de entrada principal
│       ├── ⚙️  config.py    ← Configurações do sistema
│       └── 🛠️  utils/       ← Funções auxiliares
│           ├── 🐍 __init__.py
│           └── 🔧 helpers.py
│
├── 🧪 tests/                 ← Todos os testes ficam aqui
│   ├── 🐍 __init__.py
│   ├── ✅ test_main.py
│   └── ✅ test_utils.py
│
├── 📚 docs/                  ← Documentação detalhada
│   ├── 📖 index.md
│   └── 📋 api.md
│
└── 🎬 scripts/               ← Scripts de automação
    ├── 🚀 deploy.sh
    └── 🔧 setup_dev.py
"""
        
        self.print_colored(estrutura, "text")
        
        self.print_colored("\n💡 EXPLICAÇÃO DOS SÍMBOLOS:", "info")
        simbolos = [
            "📄 Documentação - Explica como usar",
            "📁 Pastas - Organizam por categoria",
            "🐍 Python - Arquivos de código",
            "🧪 Testes - Verificam se funciona",
            "⚙️ Configuração - Define comportamento"
        ]
        
        for simbolo in simbolos:
            self.print_colored(f"  {simbolo}", "text")
        
        self.pausar()
    
    def _secao_gerenciamento_dependencias(self) -> None:
        """Seção: Gerenciamento de dependências"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("GERENCIAMENTO DE DEPENDÊNCIAS", "📦", "warning")
        
        self.print_colored("🎯 Dependências são como ingredientes de uma receita:", "text")
        self.print_colored("Você precisa saber exatamente quais e em que versão!", "text")
        
        # === REQUIREMENTS.TXT ===
        self.print_colored("\n1️⃣ REQUIREMENTS.TXT - A Lista de Compras", "accent")
        
        exemplo_requirements = """# Exemplo de requirements.txt
requests==2.31.0          # Para fazer requisições web
pandas>=1.5.0             # Para análise de dados
flask==2.3.2              # Framework web
pytest>=7.0.0             # Para testes
black                     # Formatador de código (última versão)"""
        
        self.print_code_section("EXEMPLO", exemplo_requirements)
        
        self.print_tip("Use == para versão exata, >= para versão mínima!")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === AMBIENTE VIRTUAL ===
        self.print_colored("\n2️⃣ AMBIENTES VIRTUAIS - Sua Cozinha Pessoal", "accent")
        self.print_colored("🏠 Como ter uma cozinha separada para cada receita:", "text")
        
        comandos_venv = """# Criar ambiente virtual
python -m venv meu_projeto_env

# Ativar no Windows
meu_projeto_env\\Scripts\\activate

# Ativar no Linux/Mac
source meu_projeto_env/bin/activate

# Instalar dependências
pip install -r requirements.txt"""
        
        self.print_code_section("COMANDOS", comandos_venv)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === SETUP.PY ===
        self.print_colored("\n3️⃣ SETUP.PY - Certidão de Nascimento", "accent")
        
        exemplo_setup = """from setuptools import setup, find_packages

setup(
    name="meu_projeto",
    version="1.0.0",
    author="Seu Nome",
    description="Descrição curta do projeto",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "pandas>=1.5.0",
    ],
    python_requires=">=3.8",
)"""
        
        self.print_code_section("EXEMPLO", exemplo_setup)
        
        self.print_success("\n🎯 Com setup.py, qualquer pessoa pode instalar seu projeto com: pip install .")
        
        self.pausar()
    
    def _secao_documentacao_essencial(self) -> None:
        """Seção: Documentação essencial"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DOCUMENTAÇÃO ESSENCIAL", "📚", "info")
        
        self.print_colored("📖 Documentação é como um manual de instruções:", "text")
        self.print_colored("Explica COMO usar e POR QUE existe!", "text")
        
        # === README.MD ===
        self.print_colored("\n📄 README.MD - O Cartão de Visitas", "accent")
        
        template_readme = """# 🚀 Meu Projeto Incrível

Descrição clara do que o projeto faz em uma frase.

## 🎯 O que faz?
- Funcionalidade 1
- Funcionalidade 2
- Funcionalidade 3

## 🔧 Como instalar?
```bash
pip install -r requirements.txt
```

## 🚀 Como usar?
```python
from meu_projeto import funcao_principal
resultado = funcao_principal("exemplo")
```

## 📝 Licença
MIT License"""
        
        self.print_code_section("TEMPLATE README", template_readme)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === GITIGNORE ===
        self.print_colored("\n🚫 .GITIGNORE - O Filtro Inteligente", "accent")
        self.print_colored("Lista arquivos que NÃO devem ir para o repositório:", "text")
        
        exemplo_gitignore = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Ambientes virtuais
venv/
env/
ENV/

# Arquivos sensíveis
.env
config.ini
secrets.json

# IDEs
.vscode/
.idea/
*.swp

# Sistema operacional
.DS_Store
Thumbs.db"""
        
        self.print_code_section("EXEMPLO .GITIGNORE", exemplo_gitignore)
        
        self.print_warning("⚠️ NUNCA commite senhas, tokens ou informações sensíveis!")
        
        self.pausar()
    
    def _secao_organizacao_codigo(self) -> None:
        """Seção: Organização de código fonte"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ORGANIZAÇÃO DE CÓDIGO FONTE", "📁", "success")
        
        self.print_colored("🎯 Código bem organizado é como uma biblioteca bem catalogada:", "text")
        self.print_colored("Cada livro (módulo) tem seu lugar certo!", "text")
        
        # === ESTRUTURA SRC ===
        self.print_colored("\n📦 PASTA SRC/ - O Coração do Projeto", "accent")
        
        organizacao_src = """
📁 src/
└── 📁 meu_projeto/
    ├── 🐍 __init__.py          ← Torna pasta um pacote Python
    ├── 🚀 main.py              ← Ponto de entrada principal
    ├── ⚙️  config.py           ← Configurações globais
    ├── 🗃️  models.py           ← Classes e estruturas de dados
    ├── 🔧 utils.py             ← Funções auxiliares
    ├── 📁 controllers/         ← Lógica de controle
    │   ├── 🐍 __init__.py
    │   └── 🎮 game_controller.py
    ├── 📁 services/            ← Serviços externos
    │   ├── 🐍 __init__.py
    │   └── 🌐 api_service.py
    └── 📁 views/               ← Interface com usuário
        ├── 🐍 __init__.py
        └── 🖥️  terminal_view.py
"""
        
        self.print_colored(organizacao_src, "text")
        
        # === EXEMPLO DE __INIT__.PY ===
        self.print_colored("\n🐍 ARQUIVO __INIT__.PY - A Porta de Entrada", "accent")
        
        exemplo_init = '''"""
Meu Projeto Incrível
Descrição do que o pacote faz
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"

# Importações principais para facilitar uso
from .main import funcao_principal
from .utils import helper_function

# Lista o que pode ser importado
__all__ = ["funcao_principal", "helper_function"]'''
        
        self.print_code_section("EXEMPLO __INIT__.PY", exemplo_init)
        
        self.print_tip("Com __init__.py bem configurado, usar seu código fica mais fácil!")
        
        self.pausar()
    
    def _secao_testes_scripts(self) -> None:
        """Seção: Testes e scripts auxiliares"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("TESTES E SCRIPTS AUXILIARES", "🧪", "warning")
        
        # === PASTA TESTS ===
        self.print_colored("🧪 PASTA TESTS/ - Seu Laboratório de Qualidade", "accent")
        self.print_colored("Testes garantem que seu código funciona corretamente!", "text")
        
        estrutura_tests = """
📁 tests/
├── 🐍 __init__.py
├── ✅ test_main.py           ← Testa funções principais
├── ✅ test_utils.py          ← Testa funções auxiliares
├── ✅ test_models.py         ← Testa classes e estruturas
├── 📁 fixtures/              ← Dados para testes
│   └── 📄 sample_data.json
└── 📁 integration/           ← Testes de integração
    └── ✅ test_api.py
"""
        
        self.print_colored(estrutura_tests, "text")
        
        exemplo_teste = """import pytest
from src.meu_projeto.utils import somar

def test_somar_numeros_positivos():
    \"\"\"Testa soma de números positivos\"\"\"
    resultado = somar(2, 3)
    assert resultado == 5

def test_somar_numeros_negativos():
    \"\"\"Testa soma de números negativos\"\"\"
    resultado = somar(-2, -3)
    assert resultado == -5

def test_somar_zero():
    \"\"\"Testa soma com zero\"\"\"
    resultado = somar(5, 0)
    assert resultado == 5"""
        
        self.print_code_section("EXEMPLO DE TESTE", exemplo_teste)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PASTA SCRIPTS ===
        self.print_colored("\n🎬 PASTA SCRIPTS/ - Seus Assistentes Automatizados", "accent")
        
        estrutura_scripts = """
📁 scripts/
├── 🚀 deploy.sh              ← Automatiza publicação
├── 🔧 setup_dev.py           ← Configura ambiente de desenvolvimento
├── 📊 generate_report.py     ← Gera relatórios
├── 🗑️  cleanup.py            ← Limpa arquivos temporários
└── 📦 build.py               ← Constrói pacote para distribuição
"""
        
        self.print_colored(estrutura_scripts, "text")
        
        exemplo_script = """#!/usr/bin/env python3
\"\"\"
Script para configurar ambiente de desenvolvimento
\"\"\"

import os
import subprocess

def setup_development():
    \"\"\"Configura ambiente completo\"\"\"
    print("🔧 Configurando ambiente de desenvolvimento...")
    
    # Criar ambiente virtual
    subprocess.run(["python", "-m", "venv", "venv"])
    
    # Instalar dependências
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Instalar ferramentas de desenvolvimento
    subprocess.run(["pip", "install", "pytest", "black", "flake8"])
    
    print("✅ Ambiente configurado com sucesso!")

if __name__ == "__main__":
    setup_development()"""
        
        self.print_code_section("EXEMPLO SCRIPT", exemplo_script)
        
        self.pausar()
    
    def _secao_boas_praticas(self) -> None:
        """Seção: Boas práticas profissionais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("BOAS PRÁTICAS PROFISSIONAIS", "⭐", "accent")
        
        self.print_colored("🎯 Dicas dos profissionais mais experientes do mundo:", "text")
        
        praticas = [
            {
                'emoji': '📝',
                'titulo': 'NOMES DESCRITIVOS',
                'dica': 'Use nomes que explicam o propósito',
                'exemplo': 'calculadora_imc.py em vez de calc.py'
            },
            {
                'emoji': '🎯',
                'titulo': 'UMA RESPONSABILIDADE POR ARQUIVO',
                'dica': 'Cada arquivo deve ter um propósito claro',
                'exemplo': 'database.py para banco, api.py para API'
            },
            {
                'emoji': '📚',
                'titulo': 'DOCUMENTATION STRINGS',
                'dica': 'Documente funções e classes importantes',
                'exemplo': '"""Esta função calcula o IMC do usuário"""'
            },
            {
                'emoji': '🔒',
                'titulo': 'NUNCA HARDCODE SECRETS',
                'dica': 'Use arquivos .env para dados sensíveis',
                'exemplo': 'API_KEY=os.getenv("API_KEY") em vez de API_KEY="123"'
            },
            {
                'emoji': '🧪',
                'titulo': 'TESTES SEMPRE',
                'dica': 'Cada função importante deve ter teste',
                'exemplo': 'test_calcular_imc() para calcular_imc()'
            },
            {
                'emoji': '📦',
                'titulo': 'CONTROLE DE VERSÃO',
                'dica': 'Use versionamento semântico',
                'exemplo': '1.0.0 → 1.0.1 (bugfix) → 1.1.0 (feature)'
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{i}. {pratica['emoji']} {pratica['titulo']}", "warning")
            self.print_colored(f"   💡 {pratica['dica']}", "text")
            self.print_colored(f"   📝 Exemplo: {pratica['exemplo']}", "info")
            
            if i < len(praticas):
                input("   ⏳ Pressione ENTER para a próxima dica...")
        
        # === CHECKLIST FINAL ===
        self.print_colored("\n✅ CHECKLIST DE PROJETO PROFISSIONAL:", "success")
        checklist = [
            "README.md bem escrito",
            "requirements.txt atualizado",
            ".gitignore configurado",
            "Testes funcionando",
            "Código documentado",
            "Estrutura organizada",
            "Secrets protegidos"
        ]
        
        for item in checklist:
            self.print_colored(f"□ {item}", "text")
        
        self.print_success("\n🏆 Seguindo essas práticas, você programará como um profissional!")
        
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
                'title': 'Quiz: Conhecimentos sobre Estrutura de Projetos',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Em qual pasta devemos colocar o código fonte principal do projeto?',
                        'answer': ['src', 'src/', 'pasta src', 'source'],
                        'hint': 'É uma pasta de 3 letras que significa "source" (fonte)'
                    },
                    {
                        'question': 'Qual arquivo lista as dependências do projeto?',
                        'answer': ['requirements.txt', 'requirements', 'requeriments.txt'],
                        'hint': 'É um arquivo .txt que lista os "requisitos" do projeto'
                    },
                    {
                        'question': 'Qual arquivo torna uma pasta um pacote Python?',
                        'answer': ['__init__.py', '__init__', 'init.py'],
                        'hint': 'É um arquivo especial com underscores duplos antes e depois de "init"'
                    },
                    {
                        'question': 'Em qual pasta devemos colocar os testes do projeto?',
                        'answer': ['tests', 'tests/', 'test', 'pasta tests'],
                        'hint': 'É uma pasta com nome no plural relacionado a "testar"'
                    },
                    {
                        'question': 'Qual comando cria um ambiente virtual Python?',
                        'answer': ['python -m venv', 'python -m venv nome', 'python -m venv venv'],
                        'hint': 'Use "python -m" seguido do nome do módulo que começa com "v"'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete a Estrutura',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o arquivo requirements.txt básico',
                        'starter': '# requirements.txt\n# Complete com 3 dependências populares:\n\n# Complete aqui\n',
                        'solution': 'requests==2.31.0\npandas>=1.5.0\nflask==2.3.2',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o __init__.py do projeto',
                        'starter': '"""\nMeu Projeto Python\n"""\n\n__version__ = "1.0.0"\n\n# Importe a função principal de main.py\n# Complete aqui\n\n__all__ = ["funcao_principal"]',
                        'solution': 'from .main import funcao_principal',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o setup.py básico',
                        'starter': 'from setuptools import setup, find_packages\n\nsetup(\n    name="meu_projeto",\n    version="1.0.0",\n    # Complete as configurações principais\n    # Complete aqui\n)',
                        'solution': 'packages=find_packages(where="src"),\n    package_dir={"": "src"},\n    install_requires=["requests", "pandas"]',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Planeje Seu Projeto',
                'type': 'creative',
                'instruction': 'Descreva um projeto Python que você gostaria de criar e como organizaria sua estrutura de pastas!'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete a Estrutura")
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
                elif escolha in ["2", "codigo", "completar", "estrutura"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo", "projeto"]:
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre estrutura de projetos",
            "💻 OPÇÃO 2 - Complete a Estrutura: 3 exercícios progressivos de configuração",
            "🎨 OPÇÃO 3 - Exercício Criativo: Planeje a estrutura do seu próprio projeto",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: Gerador automático de estruturas",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'estrutura', 'criativo'",
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
        """Executa um quiz interativo sobre estrutura de projetos"""
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
        
        if percentage == 100:
            self.print_success("🌟 PERFEITO! Você dominou a estrutura de projetos!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você entende bem como organizar projetos!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos e tente novamente.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo sobre estrutura de projetos.", "info")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código de estrutura"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código Inicial", ex['starter'])
            
            # Diferentes tipos de exercícios
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print("\n✍️ Complete o arquivo requirements.txt:")
                print("💡 Digite 3 dependências no formato: nome==versao ou nome>=versao")
                print("📝 Exemplo: requests==2.31.0")
                
                deps = []
                for j in range(3):
                    dep = input(f"Dependência {j+1}: ").strip()
                    if dep:
                        deps.append(dep)
                    else:
                        deps.append(f"biblioteca{j+1}>=1.0.0")
                
                user_code = '\n'.join(deps)
                    
            elif exercise_type == 'intermediate':
                print("\n✍️ Complete a importação no __init__.py:")
                print("💡 Digite: from .main import funcao_principal")
                print("🎯 Lembre-se do ponto antes de 'main' (importação relativa)")
                
                user_input = input(">>> ").strip()
                if 'from' in user_input and 'import' in user_input and 'main' in user_input:
                    user_code = user_input
                else:
                    user_code = "from .main import funcao_principal"
                    self.print_tip("Usando exemplo padrão. Lembre-se da sintaxe: from .modulo import funcao")
                    
            elif exercise_type == 'advanced':
                print("\n✍️ Complete as configurações do setup.py:")
                print("💡 Digite 3 linhas de configuração (packages, package_dir, install_requires)")
                print("📝 Exemplo primeira linha: packages=find_packages(where=\"src\")")
                
                configs = []
                prompts = [
                    "Configuração packages: ",
                    "Configuração package_dir: ", 
                    "Configuração install_requires: "
                ]
                
                for prompt in prompts:
                    config = input(prompt).strip()
                    if config:
                        if not config.endswith(','):
                            config += ','
                        configs.append(config)
                
                if configs:
                    user_code = '\n    '.join(configs)
                else:
                    user_code = ex['solution']
            else:
                # Tipo padrão
                print("\n✍️ Digite a linha que falta:")
                user_input = input(">>> ").strip()
                user_code = user_input if user_input else ex['solution']
            
            # Substitui a linha que contém o comentário
            lines = ex['starter'].split('\n')
            for j, line in enumerate(lines):
                if '# Complete aqui' in line:
                    if exercise_type == 'simple':
                        # Para requirements.txt, substitui apenas a linha do comentário
                        lines[j] = user_code
                    else:
                        lines[j] = user_code
                    break
            complete_code = '\n'.join(lines)
            
            print("\n🚀 Resultado do seu código:")
            self.print_code_section("COMPLETO", complete_code)
            
            print(f"\n💡 Solução sugerida: {ex['solution']}")
            self.print_success("✅ Muito bem! Você completou a estrutura!")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo de planejamento de projeto"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        print("💡 Exemplo: 'Um app para rastrear hábitos diários com gráficos motivacionais'")
        print("🎯 Pense em algo que você gostaria de usar no seu dia a dia!")
        
        nome_projeto = input("\n✍️ Nome do projeto: ").strip()
        if not nome_projeto:
            nome_projeto = "meu_projeto_incrivel"
            
        descricao = input("📝 Descrição (o que faz?): ").strip()
        if not descricao:
            descricao = "Um projeto Python útil e interessante"
            
        print("\n🏗️ Como você organizaria as pastas? (escolha algumas)")
        print("📁 Opções: src/, tests/, docs/, scripts/, data/, static/, templates/")
        pastas = input("📂 Suas pastas (separadas por vírgula): ").strip()
        
        if nome_projeto and descricao:
            print("\n🌟 Sua ideia ficou incrível!")
            print(f"\n🎯 PROJETO: {nome_projeto.title()}")
            print(f"📝 DESCRIÇÃO: {descricao}")
            
            # Estrutura sugerida
            pastas_escolhidas = [p.strip() for p in pastas.split(',')] if pastas else ['src/', 'tests/', 'docs/']
            
            print(f"\n📁 ESTRUTURA SUGERIDA:")
            print(f"{nome_projeto.lower().replace(' ', '_')}/")
            print("├── README.md")
            print("├── requirements.txt")
            for pasta in pastas_escolhidas:
                if pasta:
                    pasta_limpa = pasta.strip().rstrip('/')
                    print(f"├── {pasta_limpa}/")
            print("└── .gitignore")
            
            # Código exemplo do projeto
            codigo_projeto = f'''# 🐍 PROJETO: {nome_projeto.upper()}
# {descricao}

def main():
    \"\"\"Função principal do projeto {nome_projeto}\"\"\"
    print("🚀 Iniciando {nome_projeto}...")
    print("📝 {descricao}")
    print("✅ Projeto executando com sucesso!")
    return "Funcionando!"

if __name__ == "__main__":
    resultado = main()
    print(f"🎉 Status: {{resultado}}")'''
            
            print("\n💻 CÓDIGO EXEMPLO GERADO:")
            self.exemplo(codigo_projeto)
            
            print("\n🚀 Executando seu projeto conceitual:")
            self.executar_codigo(codigo_projeto)
            
            self.print_success("🎉 Parabéns! Você planejou um projeto completo!")
            
            # Dicas personalizadas baseadas na descrição
            if any(palavra in descricao.lower() for palavra in ['web', 'site', 'flask', 'django']):
                self.print_tip("💡 Para projetos web, considere adicionar: templates/, static/, requirements.txt com Flask/Django")
            elif any(palavra in descricao.lower() for palavra in ['dados', 'data', 'análise', 'gráfico']):
                self.print_tip("💡 Para análise de dados, considere: notebooks/, data/, requirements.txt com pandas/matplotlib")
            elif any(palavra in descricao.lower() for palavra in ['bot', 'telegram', 'discord', 'whatsapp']):
                self.print_tip("💡 Para bots, considere: config/, logs/, requirements.txt com bibliotecas específicas")
            else:
                self.print_tip("💡 Lembre-se: README.md bem escrito é o cartão de visitas do seu projeto!")
        else:
            self.print_warning("❌ Você precisa pelo menos dar um nome e descrição ao projeto!")
        
        self.pausar()
    
    def _mini_projeto_gerador_estruturas(self) -> None:
        """Mini Projeto - Módulo 28: Gerador Automático de Estruturas de Projeto"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: GERADOR DE ESTRUTURAS")
        else:
            print("\n" + "="*60)
            print("🎯 MINI PROJETO: GERADOR DE ESTRUTURAS")
            print("="*60)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu gerador automático de projetos Python!")
        
        self.print_concept(
            "Gerador de Estruturas",
            "Um programa que cria automaticamente toda a estrutura profissional de um projeto Python, incluindo pastas, arquivos de configuração e documentação básica."
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Empresas que criam muitos projetos novos (acelera desenvolvimento)",
            "Desenvolvedores freelancers (padroniza todos os projetos)",
            "Equipes de desenvolvimento (garante consistência)",
            "Estudantes (aprende estrutura correta desde o início)"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Coleta de informações do projeto
        self.print_section("PASSO 1: Informações do Projeto", "📝", "info")
        self.print_tip("Vamos coletar as informações básicas do seu projeto!")
        
        try:
            nome_projeto = input("\n🏷️ Nome do projeto (ex: minha_calculadora): ").strip()
            if not nome_projeto:
                nome_projeto = "meu_projeto_python"
            
            descricao = input("📝 Descrição breve (ex: Calculadora simples): ").strip()
            if not descricao:
                descricao = "Um projeto Python incrível"
            
            autor = input("👤 Seu nome (ex: João Silva): ").strip()
            if not autor:
                autor = "Desenvolvedor Python"
            
            versao = input("🔢 Versão inicial (pressione ENTER para 1.0.0): ").strip()
            if not versao:
                versao = "1.0.0"
                
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Processamento e criação da estrutura
        self.print_section("PASSO 2: Gerando Estrutura", "⚙️", "success")
        self.print_colored("Agora vamos processar os dados e criar a estrutura:", "text")
        
        # === SIMULAÇÃO DA CRIAÇÃO ===
        estruturas = [
            f"📁 Criando diretório principal: {nome_projeto}/",
            f"📁 Criando src/{nome_projeto}/",
            "📁 Criando tests/",
            "📁 Criando docs/",
            "📁 Criando scripts/",
            "📄 Gerando README.md",
            "📦 Gerando requirements.txt",
            "🐍 Gerando __init__.py",
            "🚀 Gerando main.py",
            "⚙️ Gerando setup.py",
            "🚫 Gerando .gitignore"
        ]
        
        for estrutura in estruturas:
            self.print_colored(f"  {estrutura}", "text")
            time.sleep(0.3)  # Simulação de processamento
        
        # PASSO 3: Resultado final
        self.print_section("PASSO 3: Resultado Final", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: GERADOR DE ESTRUTURAS DE PROJETO
# Módulo 28: Estrutura de Projetos

import os

def criar_estrutura_projeto(nome, descricao, autor, versao):
    """Cria estrutura completa de projeto Python"""
    
    print(f"🏗️ Criando projeto: {{nome}}")
    
    # === CRIAR DIRETÓRIOS ===
    diretorios = [
        f"{{nome}}",
        f"{{nome}}/src/{{nome}}",
        f"{{nome}}/tests",
        f"{{nome}}/docs", 
        f"{{nome}}/scripts"
    ]
    
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)
        print(f"📁 Criado: {{diretorio}}")
    
    # === ARQUIVOS DE CONFIGURAÇÃO ===
    arquivos = {{
        f"{{nome}}/README.md": f"""# {{descricao}}

## 🎯 Descrição
{{descricao}}

## 🔧 Instalação
```bash
pip install -r requirements.txt
```

## 🚀 Como usar
```python
from {{nome}} import main
main.executar()
```

## 👤 Autor
{{autor}}
""",
        
        f"{{nome}}/requirements.txt": """# Dependências do projeto
requests>=2.31.0
pytest>=7.0.0
""",
        
        f"{{nome}}/src/{{nome}}/__init__.py": f"""\\"""
{{descricao}}
\\"""

__version__ = "{{versao}}"
__author__ = "{{autor}}"

from .main import executar

__all__ = ["executar"]
""",
        
        f"{{nome}}/src/{{nome}}/main.py": """def executar():
    \\"""Função principal do projeto\\"""
    print('🎉 Projeto funcionando!')
    return 'Sucesso!'

if __name__ == '__main__':
    executar()
""",
        
        f"{{nome}}/.gitignore": """__pycache__/
*.pyc
*.pyo
.env
venv/
.vscode/
.idea/
""",
        
        f"{{nome}}/tests/test_main.py": """import pytest
from src.{nome}.main import executar

def test_executar():
    resultado = executar()
    assert resultado == "Sucesso!"
""",
        
        f"{{nome}}/setup.py": f"""from setuptools import setup, find_packages

setup(
    name="{{nome}}",
    version="{{versao}}",
    author="{{autor}}",
    description="{{descricao}}",
    packages=find_packages(where="src"),
    package_dir={{"": "src"}},
    install_requires=[
        "requests>=2.31.0",
    ],
    python_requires=">=3.8",
)
"""
    }}
    
    # === CRIAR ARQUIVOS ===
    for arquivo, conteudo in arquivos.items():
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"📄 Criado: {{arquivo}}")
    
    print(f"✅ Projeto '{{nome}}' criado com sucesso!")
    print(f"📁 Acesse: cd {{nome}}")
    return nome

# === EXECUÇÃO DO GERADOR ===
projeto_criado = criar_estrutura_projeto(
    nome="{nome_projeto}",
    descricao="{descricao}",
    autor="{autor}",
    versao="{versao}"
)

print(f"\\n🏆 SEU PROJETO ESTÁ PRONTO!")
print(f"📊 Estatísticas:")
print(f"• Nome: {{projeto_criado}}")
print(f"• Arquivos criados: 8")
print(f"• Pastas criadas: 5") 
print(f"• Configuração completa: ✅")'''

        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.print_colored("🚀 Vamos ver seu gerador funcionando:", "text")
        
        # Simulação da execução
        print(f"\n🏗️ Criando projeto: {nome_projeto}")
        diretorios_criados = [
            f"{nome_projeto}/",
            f"{nome_projeto}/src/{nome_projeto}/",
            f"{nome_projeto}/tests/",
            f"{nome_projeto}/docs/", 
            f"{nome_projeto}/scripts/"
        ]
        
        for diretorio in diretorios_criados:
            print(f"📁 Criado: {diretorio}")
            time.sleep(0.2)
        
        arquivos_criados = [
            "README.md", "requirements.txt", "__init__.py", 
            "main.py", ".gitignore", "test_main.py", "setup.py"
        ]
        
        for arquivo in arquivos_criados:
            print(f"📄 Criado: {arquivo}")
            time.sleep(0.2)
        
        print(f"\n✅ Projeto '{nome_projeto}' criado com sucesso!")
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou seu gerador de estruturas de projeto!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar templates diferentes (web, data science, CLI)",
            "Integrar com Git para inicializar repositório automaticamente",
            "Criar interface gráfica para facilitar uso",
            "Adicionar geração de documentação automática",
            "Integrar com ferramentas de CI/CD (GitHub Actions)"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de Projetos!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Gerador de Estruturas de Projeto")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo28EstruturaProjetos()
    print("Teste do módulo 28 - versão standalone")
    module._estrutura_projetos_principal()