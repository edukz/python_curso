#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 26: Ambientes Virtuais e Dependências
Aprenda a gerenciar projetos Python de forma profissional
"""

import subprocess
import os
import sys
import shutil
from pathlib import Path
from ..shared.base_module import BaseModule


class Modulo26AmbientesVirtuais(BaseModule):
    """Módulo 26: Ambientes Virtuais e Dependências"""
    
    def __init__(self):
        super().__init__("modulo_26", "Ambientes Virtuais e Dependências")
        self.has_mini_project = True
        self.mini_project_points = 85
    
    def execute(self) -> None:
        """Executa o módulo sobre Ambientes Virtuais"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._ambientes_virtuais_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _ambientes_virtuais_module(self) -> None:
        """Conteúdo principal sobre ambientes virtuais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📦 MÓDULO 26: AMBIENTES VIRTUAIS E DEPENDÊNCIAS")
        else:
            print("\n" + "="*60)
            print("📦 MÓDULO 26: AMBIENTES VIRTUAIS E DEPENDÊNCIAS")
            print("="*60)
        
        print("🔒 Isole seus projetos e gerencie dependências como um profissional!")
        print("🎯 Tópicos abordados:")
        print("• Por que usar ambientes virtuais")
        print("• venv, virtualenv e conda")
        print("• pip e gerenciamento de pacotes")
        print("• requirements.txt e lock files")
        print("• Poetry e ferramentas modernas")
        print("• Docker para isolamento completo")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._por_que_ambientes_virtuais()
        self._venv_basico()
        self._pip_gerenciamento_pacotes()
        self._requirements_reproducibilidade()
        self._ferramentas_modernas()
        self._mini_projeto_ambiente()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _por_que_ambientes_virtuais(self):
        """Por que usar ambientes virtuais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🤔 POR QUE USAR AMBIENTES VIRTUAIS?")
        
        print("🎯 Problemas que ambientes virtuais resolvem:")
        
        print("\n❌ Sem ambientes virtuais:")
        problemas = '''🔴 PROBLEMAS COMUNS:

1. 💥 Conflito de Dependências
   • Projeto A precisa Django 3.0
   • Projeto B precisa Django 4.0
   • Impossível ter ambos no mesmo sistema!

2. 🗑️ Poluição do Sistema
   • Pacotes instalados globalmente
   • Difícil de rastrear o que cada projeto usa
   • Sistema fica bagunçado com o tempo

3. 🚫 Problemas de Reprodução
   • "Funciona na minha máquina"
   • Diferentes versões em dev/prod
   • Dificuldade para onboarding de equipe

4. 🔒 Permissões e Segurança
   • Precisa de sudo/admin para instalar pacotes
   • Risco de quebrar ferramentas do sistema
   • Packages não confiáveis afetam todo sistema'''
        print(problemas)
        
        print("\n✅ Com ambientes virtuais:")
        solucoes = '''🟢 SOLUÇÕES:

1. 🔐 Isolamento Completo
   • Cada projeto tem suas próprias dependências
   • Versões específicas para cada projeto
   • Zero conflitos entre projetos

2. 🧹 Sistema Limpo
   • Pacotes ficam isolados por projeto
   • Fácil remoção - só deletar a pasta
   • Sistema base permanece intocado

3. 📋 Reprodutibilidade
   • requirements.txt documenta dependências
   • Mesmo ambiente em dev/teste/produção
   • Onboarding rápido da equipe

4. 🛡️ Segurança
   • Sem necessidade de sudo/admin
   • Pacotes duvidosos ficam isolados
   • Rollback fácil se algo der errado'''
        print(solucoes)
        
        print("\n🏗️ Casos de uso profissionais:")
        casos = '''📊 CENÁRIOS REAIS:

• 🚀 Startup: Múltiplos MVPs com tech stacks diferentes
• 🏢 Empresa: Times trabalhando em versões diferentes do mesmo framework
• 🧪 Pesquisa: Experimentos com bibliotecas experimentais
• 📚 Aprendizado: Estudar diferentes versões sem quebrar nada
• 🔧 Manutenção: Suporte a sistemas legados e modernos
• 🌍 Open Source: Contribuir para projetos com dependências específicas'''
        print(casos)
        
        print("\n💡 Analogia: Apartamentos vs Casa Compartilhada")
        print("🏠 Sistema global = Casa compartilhada")
        print("   • Todos dividem os mesmos recursos")
        print("   • Conflitos inevitáveis")
        print("   • Difícil manter organizado")
        print("")
        print("🏢 Ambiente virtual = Apartamento próprio")
        print("   • Cada projeto tem seu espaço")
        print("   • Independência total")
        print("   • Fácil organização e limpeza")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _venv_basico(self):
        """venv - ferramenta padrão do Python"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐍 VENV - FERRAMENTA PADRÃO DO PYTHON")
        
        print("📦 venv - incluído no Python 3.3+:")
        print("• Ferramenta oficial e padrão")
        print("• Sem instalação adicional necessária")
        print("• Leve e rápido")
        print("• Suporte em todas as plataformas")
        
        print("\n🛠️ Comandos essenciais:")
        
        # Detectar sistema operacional
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        
        if sistema == "Windows":
            comandos_criar = '''# Windows
# Criar ambiente virtual
python -m venv meu_projeto
python -m venv C:\\caminho\\para\\projeto

# Ativar ambiente
meu_projeto\\Scripts\\activate

# Desativar
deactivate'''
        else:
            comandos_criar = '''# Unix/Linux/macOS
# Criar ambiente virtual
python3 -m venv meu_projeto
python3 -m venv /caminho/para/projeto

# Ativar ambiente
source meu_projeto/bin/activate

# Desativar
deactivate'''
        
        print(f"\n📋 Sistema detectado: {sistema}")
        print(comandos_criar)
        
        print("\n🔍 Verificando o ambiente:")
        verificacao = '''# Depois de ativar, verificar:
which python     # Unix/Linux/macOS
where python     # Windows

# Deve mostrar o caminho do ambiente virtual
# Ex: /home/user/meu_projeto/bin/python

# Ver pacotes instalados
pip list

# Ver localização do pip
which pip        # Unix/Linux/macOS
where pip        # Windows'''
        print(verificacao)
        
        print("\n📁 Estrutura do ambiente virtual:")
        estrutura = '''meu_projeto/
├── bin/                    # Unix/Linux/macOS
│   ├── activate           # Script de ativação
│   ├── python             # Executável Python
│   └── pip                # Pip do ambiente
├── Scripts/               # Windows
│   ├── activate.bat       # Script de ativação
│   ├── python.exe         # Executável Python
│   └── pip.exe            # Pip do ambiente
├── lib/                   # Bibliotecas instaladas
│   └── python3.x/
│       └── site-packages/ # Pacotes Python
├── include/               # Headers C/C++
└── pyvenv.cfg            # Configuração do ambiente'''
        print(estrutura)
        
        print("\n⚡ Workflow típico:")
        workflow = '''1. 📂 Criar diretório do projeto
   mkdir meu_projeto
   cd meu_projeto

2. 🔨 Criar ambiente virtual
   python -m venv venv

3. 🔑 Ativar ambiente
   source venv/bin/activate  # Unix/Linux/macOS
   venv\\Scripts\\activate     # Windows

4. 📦 Instalar dependências
   pip install requests pandas flask

5. 💻 Desenvolver o projeto
   # Seu código aqui

6. 📋 Salvar dependências
   pip freeze > requirements.txt

7. 🔒 Desativar quando terminar
   deactivate'''
        print(workflow)
        
        print("\n🎯 Boas práticas:")
        praticas = '''✅ FAÇA:
• Use nomes consistentes (venv, .venv, env)
• Adicione venv/ ao .gitignore
• Ative o ambiente antes de instalar pacotes
• Documente como configurar o ambiente no README
• Use requirements.txt para dependências

❌ NÃO FAÇA:
• Commitar a pasta do ambiente virtual
• Instalar pacotes sem ativar o ambiente
• Usar o mesmo ambiente para projetos diferentes
• Esquecer de ativar o ambiente'''
        print(praticas)
        
        print("\n🔧 Opções avançadas do venv:")
        avancado = '''# Especificar versão do Python
python3.9 -m venv myproject
python3.10 -m venv myproject

# Copiar pacotes do sistema (não recomendado)
python -m venv --system-site-packages myproject

# Sem pip (instalar manualmente depois)
python -m venv --without-pip myproject

# Limpar e recriar
rm -rf venv
python -m venv venv'''
        print(avancado)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _pip_gerenciamento_pacotes(self):
        """pip e gerenciamento de pacotes"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📦 PIP E GERENCIAMENTO DE PACOTES")
        
        print("🛠️ pip - Python Package Installer:")
        print("• Gerenciador de pacotes padrão do Python")
        print("• Acesso ao PyPI (Python Package Index)")
        print("• 400,000+ pacotes disponíveis")
        print("• Resolução automática de dependências")
        
        print("\n⚡ Comandos essenciais:")
        
        comandos_pip = '''# Instalação básica
pip install requests                    # Última versão
pip install requests==2.28.1           # Versão específica
pip install "requests>=2.25.0"         # Versão mínima
pip install "requests>=2.25,<3.0"      # Range de versões

# Múltiplos pacotes
pip install requests pandas numpy flask

# Instalar de diferentes fontes
pip install git+https://github.com/user/repo.git
pip install https://github.com/user/repo/archive/main.zip
pip install ./local_package/
pip install -e ./editable_package/     # Modo desenvolvimento

# Upgrade e downgrade
pip install --upgrade requests         # Atualizar
pip install --upgrade-strategy eager requests  # Atualizar dependências também
pip install requests==2.25.0 --force-reinstall  # Forçar reinstalação'''
        print(comandos_pip)
        
        print("\n🔍 Investigação e listagem:")
        listagem = '''# Listar pacotes instalados
pip list                               # Todos os pacotes
pip list --outdated                    # Pacotes desatualizados
pip list --uptodate                    # Pacotes atualizados
pip list --user                       # Pacotes do usuário

# Informações detalhadas
pip show requests                      # Info do pacote
pip show -f requests                   # Incluir arquivos

# Buscar pacotes
pip search machine learning           # Buscar no PyPI (pode estar desabilitado)

# Verificar dependências
pip check                             # Verificar compatibilidade'''
        print(listagem)
        
        print("\n🗑️ Remoção e limpeza:")
        remocao = '''# Remover pacotes
pip uninstall requests                 # Remover um pacote
pip uninstall -y requests              # Sem confirmação
pip uninstall -r requirements.txt     # Remover de lista

# Limpeza
pip cache purge                       # Limpar cache
pip cache dir                         # Ver diretório do cache
pip cache info                        # Info do cache'''
        print(remocao)
        
        print("\n📋 Trabalhando com requirements:")
        requirements = '''# Gerar requirements.txt
pip freeze > requirements.txt         # Todas as dependências
pip freeze | grep -v "pkg-resources" > requirements.txt  # Linux bugfix

# Instalar de requirements
pip install -r requirements.txt       # Instalar tudo
pip install -r requirements.txt --upgrade  # Com upgrade

# Requirements mais específicos
echo "requests>=2.25.0" >> requirements.txt
echo "pandas~=1.3.0" >> requirements.txt    # Compatible release
echo "numpy==1.21.*" >> requirements.txt    # Wildcard'''
        print(requirements)
        
        print("\n🔧 Configuração avançada:")
        config_avancado = '''# Arquivo pip.conf / pip.ini
# ~/.pip/pip.conf (Unix) ou %APPDATA%\\pip\\pip.ini (Windows)

[global]
timeout = 60
index-url = https://pypi.org/simple/
extra-index-url = https://test.pypi.org/simple/
trusted-host = localhost

[install]
user = true

# Usar mirror local/corporativo
pip install -i https://pypi.company.com/simple/ requests

# Instalar sem dependências
pip install --no-deps requests

# Apenas baixar (não instalar)
pip download requests

# Verificar antes de instalar
pip install --dry-run requests'''
        print(config_avancado)
        
        print("\n🚨 Troubleshooting comum:")
        troubleshooting = '''❌ PROBLEMAS COMUNS:

1. Permission Denied
   Solução: Usar ambiente virtual ou --user
   pip install --user requests

2. SSL Certificate Error
   Solução: Atualizar certificados ou usar --trusted-host
   pip install --trusted-host pypi.org requests

3. Dependency Hell
   Solução: Usar pip-tools ou Poetry
   pip install pip-tools
   pip-compile requirements.in

4. Slow Installation
   Solução: Usar wheels pré-compilados
   pip install --only-binary=all requests

5. Package Not Found
   Solução: Verificar nome exato no PyPI
   pip search similar-name'''
        print(troubleshooting)
        
        print("\n💡 Dicas profissionais:")
        dicas = '''🏆 DICAS AVANÇADAS:

• Use pip-tools para lock files determinísticos
• Configure mirrors corporativos para velocidade
• Use --user para instalações globais sem sudo
• Mantenha pip atualizado: python -m pip install --upgrade pip
• Use virtual environments SEMPRE
• Documente versões exatas em produção
• Use .pip-constraints.txt para limites globais'''
        print(dicas)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _requirements_reproducibilidade(self):
        """requirements.txt e reprodutibilidade"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📋 REQUIREMENTS.TXT E REPRODUTIBILIDADE")
        
        print("🎯 Garantindo ambientes consistentes:")
        print("• Documentar dependências exatas")
        print("• Reproduzir ambiente em qualquer máquina")
        print("• Versionamento de dependências")
        print("• Deploy consistente")
        
        print("\n📝 Tipos de requirements:")
        
        tipos_req = '''# requirements.txt - dependências principais
requests>=2.25.0
pandas~=1.3.0
flask==2.0.1

# requirements-dev.txt - dependências de desenvolvimento
pytest>=6.0.0
black
flake8
mypy

# requirements-prod.txt - produção (versões exatas)
requests==2.28.1
pandas==1.3.5
flask==2.0.1

# requirements-test.txt - apenas para testes
pytest==7.1.2
pytest-cov==3.0.0
factory-boy==3.2.1'''
        print(tipos_req)
        
        print("\n🔒 Lock files vs Requirements:")
        lock_vs_req = '''📋 REQUIREMENTS.TXT (Flexível):
requests>=2.25.0        # Aceita 2.25.0, 2.26.0, 2.27.0...
pandas~=1.3.0          # Aceita 1.3.0, 1.3.1, mas não 1.4.0
flask                  # Qualquer versão (perigoso!)

🔐 LOCK FILE (Exato):
requests==2.28.1        # Exatamente esta versão
urllib3==1.26.12       # Dependência transitiva específica
certifi==2022.9.24     # Todas as dependências fixadas

# Gerar lock file
pip freeze > requirements-lock.txt'''
        print(lock_vs_req)
        
        print("\n🏗️ Estrutura de projeto profissional:")
        estrutura_pro = '''meu_projeto/
├── requirements/
│   ├── base.txt           # Dependências principais
│   ├── development.txt    # Para desenvolvimento
│   ├── production.txt     # Para produção
│   └── testing.txt        # Para testes
├── requirements.txt       # Link para base.txt
├── setup.py              # Se for um pacote
├── pyproject.toml         # Configuração moderna
├── .python-version        # Versão do Python (pyenv)
└── runtime.txt           # Para Heroku/plataformas

# base.txt
django>=3.2,<4.0
psycopg2-binary>=2.8
celery>=5.0

# development.txt
-r base.txt
django-debug-toolbar
pytest
black
flake8

# production.txt
-r base.txt
gunicorn
sentry-sdk'''
        print(estrutura_pro)
        
        print("\n⚙️ Workflow com múltiplos ambientes:")
        workflow_multi = '''# 1. Desenvolvimento local
python -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt

# 2. Teste automatizado
pip install -r requirements/testing.txt
pytest

# 3. Staging/Produção
pip install -r requirements/production.txt

# 4. Atualizar dependências
pip install --upgrade -r requirements/development.txt
pip freeze > requirements/lock.txt'''
        print(workflow_multi)
        
        print("\n🔧 Ferramentas avançadas:")
        ferramentas = '''# pip-tools - Gerenciamento avançado
pip install pip-tools

# requirements.in (high-level)
django
requests
pandas

# Gerar requirements.txt (detailed)
pip-compile requirements.in

# Sincronizar ambiente
pip-sync requirements.txt

# Atualizar dependências
pip-compile --upgrade requirements.in

# pipdeptree - Visualizar árvore de dependências
pip install pipdeptree
pipdeptree --packages pandas
pipdeptree --graph-output png > deps.png

# pip-audit - Verificar vulnerabilidades
pip install pip-audit
pip-audit

# pip-autoremove - Remover dependências órfãs
pip install pip-autoremove
pip-autoremove'''
        print(ferramentas)
        
        print("\n🐳 Docker para isolamento total:")
        dockerfile = '''# Dockerfile para Python
FROM python:3.9-slim

WORKDIR /app

# Copiar requirements primeiro (cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Comando padrão
CMD ["python", "app.py"]

# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development'''
        print(dockerfile)
        
        print("\n✅ Checklist de reprodutibilidade:")
        checklist = '''📋 ANTES DE COMMITAR:

□ requirements.txt atualizado
□ Versões específicas para dependências críticas
□ .gitignore inclui venv/ e __pycache__/
□ README com instruções de setup
□ Versão do Python documentada (.python-version)
□ Testes passando em ambiente limpo
□ Lock file gerado para produção

📋 DEPLOY/PRODUÇÃO:

□ Ambiente virtual dedicado
□ Requirements de produção (sem dev deps)
□ Versões exatas fixadas
□ Backup do ambiente funcionando
□ Monitoramento de dependências desatualizadas
□ Processo de atualização documentado'''
        print(checklist)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _ferramentas_modernas(self):
        """Poetry e ferramentas modernas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 POETRY E FERRAMENTAS MODERNAS")
        
        print("✨ Ferramentas de nova geração para Python:")
        print("• Poetry - gerenciamento completo de projetos")
        print("• Pipenv - pip + venv combinados")
        print("• conda - científico e multiplataforma")
        print("• pyenv - múltiplas versões do Python")
        
        print("\n🎭 Poetry - Gerenciamento Completo:")
        
        poetry_intro = '''🌟 POETRY - O FUTURO DO PYTHON:

✅ O que Poetry faz:
• Gerenciamento de dependências
• Ambientes virtuais automáticos
• Build e publicação de pacotes
• Lock files determinísticos
• Resolução inteligente de conflitos

💡 Instalação:
curl -sSL https://install.python-poetry.org | python3 -
# ou
pip install poetry'''
        print(poetry_intro)
        
        poetry_comandos = '''# Inicializar projeto
poetry new meu-projeto          # Criar projeto do zero
poetry init                     # Inicializar em pasta existente

# Gerenciar dependências
poetry add requests             # Adicionar dependência
poetry add pytest --group dev  # Dependência de desenvolvimento
poetry add "django>=3.0,<4.0"  # Com constraints
poetry remove requests          # Remover

# Ambiente virtual
poetry shell                    # Ativar shell do ambiente
poetry run python script.py    # Executar comando no ambiente
poetry env info                 # Info do ambiente

# Instalação
poetry install                  # Instalar dependências
poetry install --no-dev        # Sem dependências de dev
poetry update                   # Atualizar dependências

# Build e publicação
poetry build                    # Criar wheel/tarball
poetry publish                  # Publicar no PyPI'''
        print(poetry_comandos)
        
        print("\n📋 pyproject.toml - Configuração moderna:")
        pyproject = '''[tool.poetry]
name = "meu-projeto"
version = "0.1.0"
description = "Descrição do projeto"
authors = ["Seu Nome <email@exemplo.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.0"
pandas = "~1.3.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
black = "^22.0.0"
flake8 = "^4.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]'''
        print(pyproject)
        
        print("\n🐍 Pipenv - Pip + Venv Simplificado:")
        pipenv_exemplo = '''# Instalação
pip install pipenv

# Criar ambiente e Pipfile
pipenv --python 3.9

# Instalar dependências
pipenv install requests         # Produção
pipenv install pytest --dev    # Desenvolvimento

# Ativar ambiente
pipenv shell

# Executar comandos
pipenv run python script.py
pipenv run pytest

# Pipfile
[packages]
requests = "*"
django = ">=3.0"

[dev-packages]
pytest = "*"
black = "*"

[requires]
python_version = "3.9"'''
        print(pipenv_exemplo)
        
        print("\n🐍 pyenv - Múltiplas Versões do Python:")
        pyenv_exemplo = '''# Instalação (Unix/Linux/macOS)
curl https://pyenv.run | bash

# Listar versões disponíveis
pyenv install --list

# Instalar versão específica
pyenv install 3.9.16
pyenv install 3.10.8

# Definir versão global
pyenv global 3.9.16

# Definir versão para projeto
pyenv local 3.10.8           # Cria .python-version

# Listar versões instaladas
pyenv versions

# Verificar versão atual
pyenv version'''
        print(pyenv_exemplo)
        
        print("\n🔬 conda - Para Ciência de Dados:")
        conda_exemplo = '''# Instalação: Anaconda ou Miniconda
# https://docs.conda.io/en/latest/miniconda.html

# Criar ambiente
conda create -n myproject python=3.9
conda create -n data-science python=3.9 pandas numpy matplotlib

# Ativar/desativar
conda activate myproject
conda deactivate

# Instalar pacotes
conda install pandas numpy     # Do repositório conda
conda install -c conda-forge scikit-learn  # Canal específico
pip install requests           # Usar pip quando necessário

# Listar ambientes
conda env list

# Exportar ambiente
conda env export > environment.yml

# Criar de environment.yml
conda env create -f environment.yml

# environment.yml
name: data-science
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - pandas
  - numpy
  - matplotlib
  - pip
  - pip:
    - requests
    - custom-package'''
        print(conda_exemplo)
        
        print("\n🔄 Comparação de ferramentas:")
        comparacao = '''🛠️ QUANDO USAR CADA UMA:

📦 pip + venv:
✅ Projetos simples
✅ Compatibilidade máxima
✅ Controle total
❌ Mais manual

🎭 Poetry:
✅ Projetos novos
✅ Publicar pacotes
✅ Gerenciamento completo
❌ Curva de aprendizado

🐍 Pipenv:
✅ Projetos web/aplicações
✅ Fácil de usar
✅ Pipfile intuitivo
❌ Performance

🔬 conda:
✅ Ciência de dados
✅ Pacotes não-Python
✅ Ambientes complexos
❌ Overhead

🐍 pyenv:
✅ Múltiplas versões Python
✅ Compatibilidade
✅ Testes em diferentes versões
❌ Só gerencia Python'''
        print(comparacao)
        
        print("\n🏆 Recomendações por cenário:")
        recomendacoes = '''🎯 ESCOLHA POR CASO DE USO:

🚀 Iniciante:
   pip + venv (aprender os fundamentos)

📦 Projeto Pessoal:
   Poetry (experiência moderna)

🏢 Empresa/Equipe:
   Docker + requirements.txt (consistência)

🔬 Data Science:
   conda + Jupyter (ecossistema científico)

🌐 Web Development:
   Poetry ou Pipenv (facilidade)

📱 Múltiplos Projetos:
   pyenv + Poetry (flexibilidade)

☁️ Deploy/Produção:
   Docker (isolamento total)'''
        print(recomendacoes)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_ambiente(self):
        """Mini projeto: Setup completo de projeto"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: SETUP PROFISSIONAL DE PROJETO")
        
        print("📊 Vamos criar um setup completo e profissional!")
        print("🎯 Objetivos:")
        print("• Configurar ambiente isolado")
        print("• Estrutura de projeto moderna")
        print("• Gerenciamento de dependências")
        print("• Automação com scripts")
        print("• Documentação completa")
        
        input("\n🔸 Pressione ENTER para começar o projeto...")
        
        print("\n📁 1. ESTRUTURA DO PROJETO:")
        estrutura = '''projeto-profissional/
├── .env                       # Variáveis de ambiente
├── .gitignore                 # Arquivos para ignorar
├── .python-version            # Versão do Python
├── README.md                  # Documentação
├── pyproject.toml             # Configuração moderna
├── requirements/              # Dependências organizadas
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
│   └── testing.txt
├── scripts/                   # Scripts de automação
│   ├── setup.sh               # Setup inicial
│   ├── test.sh                # Executar testes
│   └── deploy.sh              # Deploy
├── src/                       # Código fonte
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── utils.py
├── tests/                     # Testes
│   ├── __init__.py
│   ├── test_main.py
│   └── conftest.py
├── docs/                      # Documentação
│   ├── installation.md
│   └── usage.md
└── docker/                    # Configuração Docker
    ├── Dockerfile
    └── docker-compose.yml'''
        print(estrutura)
        
        print("\n📋 2. REQUIREMENTS ORGANIZADOS:")
        
        req_base = '''# requirements/base.txt
requests>=2.25.0
python-dotenv>=0.19.0
click>=8.0.0'''
        
        req_dev = '''# requirements/development.txt
-r base.txt

# Qualidade de código
black>=22.0.0
flake8>=4.0.0
isort>=5.10.0
mypy>=0.950

# Testing
pytest>=7.0.0
pytest-cov>=3.0.0
pytest-mock>=3.7.0

# Desenvolvimento
ipython>=8.0.0
jupyter>=1.0.0'''
        
        req_prod = '''# requirements/production.txt
-r base.txt

# Servidor
gunicorn>=20.1.0

# Monitoramento
sentry-sdk>=1.5.0

# Versões fixadas para produção
requests==2.28.1
python-dotenv==0.20.0
click==8.1.3'''
        
        print("📦 base.txt:")
        print(req_base)
        print("\n🛠️ development.txt:")
        print(req_dev)
        print("\n🚀 production.txt:")
        print(req_prod)
        
        print("\n🔧 3. SCRIPTS DE AUTOMAÇÃO:")
        
        script_setup = '''#!/bin/bash
# scripts/setup.sh - Setup inicial do projeto

set -e

echo "🚀 Configurando projeto..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado"
    exit 1
fi

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente
echo "🔑 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "⬆️ Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements/development.txt

# Criar .env se não existir
if [ ! -f .env ]; then
    echo "⚙️ Criando arquivo .env..."
    cp .env.example .env 2>/dev/null || echo "DEBUG=True" > .env
fi

echo "✅ Setup concluído!"
echo "🔑 Para ativar o ambiente: source venv/bin/activate"'''
        
        script_test = '''#!/bin/bash
# scripts/test.sh - Executar testes

set -e

echo "🧪 Executando testes..."

# Ativar ambiente
source venv/bin/activate

# Linting
echo "🔍 Verificando código com flake8..."
flake8 src/ tests/

echo "📏 Verificando formatação com black..."
black --check src/ tests/

echo "🔤 Verificando imports com isort..."
isort --check-only src/ tests/

echo "🏷️ Verificando tipos com mypy..."
mypy src/

# Testes
echo "🧪 Executando testes com pytest..."
pytest tests/ --cov=src/ --cov-report=html --cov-report=term

echo "✅ Todos os testes passaram!"'''
        
        print("🛠️ setup.sh:")
        print(script_setup)
        print("\n🧪 test.sh:")
        print(script_test)
        
        print("\n📝 4. CONFIGURAÇÃO MODERNA (pyproject.toml):")
        
        pyproject_completo = '''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "projeto-profissional"
version = "0.1.0"
description = "Projeto Python profissional"
authors = [
    {name = "Seu Nome", email = "email@exemplo.com"},
]
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
dependencies = [
    "requests>=2.25.0",
    "python-dotenv>=0.19.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "black>=22.0.0",
    "flake8>=4.0.0",
    "isort>=5.10.0",
    "mypy>=0.950",
    "pytest>=7.0.0",
    "pytest-cov>=3.0.0",
]

[project.scripts]
meu-cli = "src.main:cli"

[tool.black]
line-length = 88
target-version = ["py38"]
include = "\\.pyi?$"
extend-exclude = """
/(
    \\.eggs
  | \\.git
  | \\.venv
  | build
  | dist
)/
"""

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --tb=short --strict-markers"
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]

[tool.coverage.run]
source = ["src"]
omit = ["tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
]'''
        print(pyproject_completo)
        
        print("\n📚 5. README.md COMPLETO:")
        
        readme = '''# Projeto Profissional

Uma demonstração de setup profissional para projetos Python.

## 🚀 Quick Start

```bash
# Clonar repositório
git clone https://github.com/usuario/projeto-profissional.git
cd projeto-profissional

# Setup automático
chmod +x scripts/setup.sh
./scripts/setup.sh

# Ativar ambiente
source venv/bin/activate

# Executar aplicação
python src/main.py
```

## 📋 Requisitos

- Python 3.8+
- pip

## 🛠️ Desenvolvimento

### Configuração Manual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate     # Windows

# Instalar dependências
pip install -r requirements/development.txt
```

### Executar Testes

```bash
# Testes completos
./scripts/test.sh

# Apenas pytest
pytest

# Com coverage
pytest --cov=src/
```

### Qualidade de Código

```bash
# Formatação
black src/ tests/

# Linting
flake8 src/ tests/

# Imports
isort src/ tests/

# Tipos
mypy src/
```

## 🚀 Deploy

### Produção

```bash
# Instalar dependências de produção
pip install -r requirements/production.txt

# Executar com gunicorn
gunicorn src.main:app
```

### Docker

```bash
# Build
docker build -t projeto-profissional .

# Run
docker run -p 8000:8000 projeto-profissional
```

## 📁 Estrutura

- `src/` - Código fonte
- `tests/` - Testes
- `requirements/` - Dependências organizadas
- `scripts/` - Scripts de automação
- `docs/` - Documentação

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.'''
        print(readme)
        
        print("\n✅ 6. CHECKLIST FINAL:")
        checklist_final = '''📋 VERIFICAÇÃO FINAL:

□ Ambiente virtual criado e ativado
□ Dependências instaladas corretamente
□ Testes passando
□ Linting sem erros
□ Formatação consistente
□ Tipos verificados
□ README documentado
□ .gitignore configurado
□ Scripts executáveis
□ Estrutura organizada

🎉 PROJETO PROFISSIONAL PRONTO!'''
        print(checklist_final)
        
        # Pontos do mini projeto
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            print(f"\n🎁 +{self.mini_project_points} pontos pelo projeto completo!")
        
        print("\n🚀 Próximos passos:")
        print("• Configurar CI/CD (GitHub Actions, GitLab CI)")
        print("• Adicionar pre-commit hooks")
        print("• Configurar dependabot para atualizações")
        print("• Implementar releases automáticos")
        print("• Adicionar badges no README")
        print("• Configurar monitoramento (Sentry)")
        
        input("\n🔸 Pressione ENTER para finalizar o módulo...")