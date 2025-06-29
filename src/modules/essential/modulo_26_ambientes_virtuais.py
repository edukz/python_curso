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
        """Executa o módulo Ambientes Virtuais e Dependências"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._ambientes_virtuais_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _ambientes_virtuais_module(self) -> None:
        """Conteúdo principal do módulo Ambientes Virtuais"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MÓDULO 26: AMBIENTES VIRTUAIS E DEPENDÊNCIAS")
        else:
            print("\n" + "="*50)
            print("🎯 MÓDULO 26: AMBIENTES VIRTUAIS E DEPENDÊNCIAS")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo profissional do Python!")
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
            self._mini_projeto_setup_profissional()
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
                'id': 'secao_por_que_ambientes',
                'titulo': '🎯 Por que usar Ambientes Virtuais?',
                'descricao': 'Entenda os problemas que eles resolvem',
                'funcao': self._secao_por_que_ambientes
            },
            {
                'id': 'secao_como_funciona',
                'titulo': '⚙️ Como funcionam os ambientes virtuais?',
                'descricao': 'Veja a mágica por trás do isolamento',
                'funcao': self._secao_como_funciona
            },
            {
                'id': 'secao_venv_pratica',
                'titulo': '💡 venv na prática',
                'descricao': 'Aprenda a criar e usar ambientes virtuais',
                'funcao': self._secao_venv_pratica
            },
            {
                'id': 'secao_pip_maestro',
                'titulo': '📦 pip - O maestro dos pacotes',
                'descricao': 'Domine o gerenciador de pacotes do Python',
                'funcao': self._secao_pip_maestro
            },
            {
                'id': 'secao_requirements',
                'titulo': '📋 requirements.txt - A receita do projeto',
                'descricao': 'Garanta que todos usem as mesmas versões',
                'funcao': self._secao_requirements
            },
            {
                'id': 'secao_ferramentas_modernas',
                'titulo': '🚀 Ferramentas modernas',
                'descricao': 'Poetry, Pipenv e outras maravilhas',
                'funcao': self._secao_ferramentas_modernas
            },
            {
                'id': 'secao_dicas_pro',
                'titulo': '⭐ Dicas profissionais',
                'descricao': 'Segredos dos desenvolvedores experientes',
                'funcao': self._secao_dicas_pro
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
    
    def _secao_por_que_ambientes(self) -> None:
        """Seção: Por que usar Ambientes Virtuais?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("POR QUE USAR AMBIENTES VIRTUAIS?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Ambiente Virtual",
            "Um espaço isolado onde cada projeto Python tem suas próprias dependências, sem conflitos com outros projetos"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Pense em ambientes virtuais como apartamentos: cada projeto tem seu próprio espaço!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você mora em uma república com amigos:", "text")
        self.print_colored("• SEM ambientes virtuais = Todos compartilham a mesma geladeira", "text")
        self.print_colored("  - João gosta de leite integral, Maria de desnatado", "text")
        self.print_colored("  - Conflitos inevitáveis! Quem compra qual?", "text")
        self.print_colored("• COM ambientes virtuais = Cada um tem sua mini-geladeira", "text")
        self.print_colored("  - João tem seu leite integral, Maria seu desnatado", "text")
        self.print_colored("  - Paz e harmonia no lar! 🎉", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PROBLEMAS REAIS ===
        self.print_colored("\n💥 PROBLEMAS SEM AMBIENTES VIRTUAIS:", "error")
        problemas = [
            "1. Projeto A precisa Django 3.0, Projeto B precisa Django 4.0",
            "2. Instalar pacotes globalmente pode quebrar ferramentas do sistema",
            "3. 'Funciona na minha máquina' vira pesadelo da equipe",
            "4. Difícil saber quais pacotes cada projeto usa"
        ]
        
        for i, problema in enumerate(problemas, 1):
            self.print_colored(problema, "text")
            if i < len(problemas):
                input("   ⏳ Pressione ENTER para o próximo problema...")
        
        # === SOLUÇÕES COM AMBIENTES ===
        self.print_colored("\n✅ SOLUÇÕES COM AMBIENTES VIRTUAIS:", "success")
        solucoes = [
            "• Cada projeto tem suas versões específicas",
            "• Sistema operacional fica protegido e limpo",
            "• Mesmas versões em desenvolvimento e produção",
            "• Fácil deletar e recriar se algo der errado"
        ]
        
        for solucao in solucoes:
            self.print_colored(solucao, "primary")
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix - Diferentes microsserviços com versões específicas",
            "Instagram - Times trabalhando em features com dependências diferentes",
            "Spotify - Experimentos com bibliotecas de machine learning",
            "Startups - Múltiplos MVPs com tecnologias variadas"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_como_funciona(self) -> None:
        """Seção: Como funcionam os ambientes virtuais?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO FUNCIONAM OS AMBIENTES VIRTUAIS?", "⚙️", "info")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 A MÁGICA POR TRÁS:", "warning")
        passos = [
            "1. 📁 Cria uma pasta especial para o projeto",
            "2. 🐍 Copia o Python para dentro dessa pasta",
            "3. 📦 Instala pacotes APENAS nessa pasta",
            "4. 🔀 Redireciona comandos para usar essa pasta"
        ]
        
        for i, passo in enumerate(passos, 1):
            self.print_colored(passo, "text")
            if i < len(passos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === ESTRUTURA VISUAL ===
        self.print_colored("\n📁 ESTRUTURA DE UM AMBIENTE VIRTUAL:", "success")
        estrutura = '''meu_projeto/
├── venv/                    # Pasta do ambiente virtual
│   ├── bin/                # Executáveis (Linux/Mac)
│   │   ├── python         # Python isolado
│   │   ├── pip           # pip isolado
│   │   └── activate      # Script de ativação
│   ├── Scripts/           # Executáveis (Windows)
│   │   ├── python.exe    # Python isolado
│   │   ├── pip.exe      # pip isolado
│   │   └── activate.bat # Script de ativação
│   └── lib/              # Bibliotecas instaladas
│       └── site-packages/ # Seus pacotes aqui!
└── seu_codigo.py         # Seu projeto'''
        
        self.print_colored(estrutura, "text")
        
        # === DEMONSTRAÇÃO PRÁTICA ===
        self.print_colored("\n💻 VEJA FUNCIONANDO:", "accent")
        
        # Detectar sistema operacional
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        
        if sistema == "Windows":
            comandos = '''# Windows
# Antes de ativar:
where python  # C:\\Python39\\python.exe

# Depois de ativar:
venv\\Scripts\\activate
where python  # C:\\projeto\\venv\\Scripts\\python.exe'''
        else:
            comandos = '''# Unix/Linux/macOS
# Antes de ativar:
which python  # /usr/bin/python3

# Depois de ativar:
source venv/bin/activate
which python  # /home/user/projeto/venv/bin/python'''
        
        self.exemplo(comandos)
        
        self.print_success("\n🎉 Agora você entende a mágica! É simples e poderoso!")
        self.pausar()
    
    def _secao_venv_pratica(self) -> None:
        """Seção: venv na prática"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("VENV NA PRÁTICA", "💡", "success")
        
        self.print_concept(
            "venv",
            "Ferramenta oficial do Python para criar ambientes virtuais. Incluída desde Python 3.3!"
        )
        
        # === COMANDOS ESSENCIAIS ===
        self.print_colored("\n⚡ COMANDOS MÁGICOS:", "warning")
        
        # Detectar sistema
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        self.print_colored(f"📋 Sistema detectado: {sistema}", "info")
        
        # === PASSO A PASSO INTERATIVO ===
        self.print_colored("\n🚀 VAMOS CRIAR SEU PRIMEIRO AMBIENTE:", "accent")
        
        passos = [
            {
                'titulo': 'PASSO 1: Criar o ambiente',
                'comando_win': 'python -m venv meu_ambiente',
                'comando_unix': 'python3 -m venv meu_ambiente',
                'explicacao': 'Cria uma pasta "meu_ambiente" com Python isolado'
            },
            {
                'titulo': 'PASSO 2: Ativar o ambiente',
                'comando_win': 'meu_ambiente\\Scripts\\activate',
                'comando_unix': 'source meu_ambiente/bin/activate',
                'explicacao': 'Agora você está "dentro" do ambiente!'
            },
            {
                'titulo': 'PASSO 3: Instalar pacotes',
                'comando_win': 'pip install requests pandas',
                'comando_unix': 'pip install requests pandas',
                'explicacao': 'Pacotes instalados APENAS neste ambiente'
            },
            {
                'titulo': 'PASSO 4: Ver o que foi instalado',
                'comando_win': 'pip list',
                'comando_unix': 'pip list',
                'explicacao': 'Lista todos os pacotes do ambiente'
            },
            {
                'titulo': 'PASSO 5: Desativar quando terminar',
                'comando_win': 'deactivate',
                'comando_unix': 'deactivate',
                'explicacao': 'Volta ao Python do sistema'
            }
        ]
        
        for i, passo in enumerate(passos, 1):
            self.print_colored(f"\n{passo['titulo']}", "primary")
            
            if sistema == "Windows":
                comando = passo['comando_win']
            else:
                comando = passo['comando_unix']
            
            self.print_code_section("COMANDO", comando)
            self.print_colored(f"💡 {passo['explicacao']}", "info")
            
            if i < len(passos):
                input("\n🔸 Pressione ENTER para o próximo passo...")
        
        # === DICAS PROFISSIONAIS ===
        self.print_colored("\n⭐ DICAS DE OURO:", "warning")
        dicas = [
            "Use sempre 'venv' ou '.venv' como nome (padrão da comunidade)",
            "Adicione venv/ ao .gitignore (NUNCA commite o ambiente!)",
            "Crie um ambiente por projeto (não compartilhe!)",
            "Documente no README como criar o ambiente"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "accent")
        
        self.pausar()
    
    def _secao_pip_maestro(self) -> None:
        """Seção: pip - O maestro dos pacotes"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PIP - O MAESTRO DOS PACOTES", "📦", "info")
        
        self.print_concept(
            "pip",
            "Python Package Installer - sua porta de entrada para 400.000+ pacotes gratuitos!"
        )
        
        # === COMANDOS ESSENCIAIS ===
        self.print_colored("\n🎯 COMANDOS QUE TODO DEV USA:", "warning")
        
        comandos_essenciais = [
            {
                'titulo': 'Instalar pacote',
                'comando': 'pip install requests',
                'descricao': 'Baixa e instala o pacote requests'
            },
            {
                'titulo': 'Instalar versão específica',
                'comando': 'pip install django==3.2.0',
                'descricao': 'Instala exatamente a versão 3.2.0'
            },
            {
                'titulo': 'Atualizar pacote',
                'comando': 'pip install --upgrade requests',
                'descricao': 'Atualiza para a versão mais recente'
            },
            {
                'titulo': 'Remover pacote',
                'comando': 'pip uninstall requests',
                'descricao': 'Remove o pacote (pergunta confirmação)'
            },
            {
                'titulo': 'Listar pacotes instalados',
                'comando': 'pip list',
                'descricao': 'Mostra todos os pacotes do ambiente'
            },
            {
                'titulo': 'Ver detalhes de um pacote',
                'comando': 'pip show requests',
                'descricao': 'Informações completas sobre o pacote'
            }
        ]
        
        for cmd in comandos_essenciais:
            self.print_colored(f"\n💻 {cmd['titulo']}:", "primary")
            self.print_code_section("", cmd['comando'])
            self.print_colored(f"→ {cmd['descricao']}", "text")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n🚀 VAMOS VER NA PRÁTICA:", "success")
        exemplo_pratico = '''# Criar um projeto de web scraping
pip install requests beautifulsoup4

# Ver o que foi instalado
pip list

# Ops! Preciso de uma versão específica
pip install requests==2.28.0

# Verificar informações
pip show requests'''
        
        self.exemplo(exemplo_pratico)
        
        # === DICA IMPORTANTE ===
        self.print_tip("Sempre use pip DENTRO do ambiente virtual ativado!")
        
        self.pausar()
    
    def _secao_requirements(self) -> None:
        """Seção: requirements.txt - A receita do projeto"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("REQUIREMENTS.TXT - A RECEITA DO PROJETO", "📋", "warning")
        
        self.print_concept(
            "requirements.txt",
            "Arquivo que lista todas as dependências do projeto, como uma receita de bolo!"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🍰 ANALOGIA DA RECEITA:", "accent")
        self.print_colored("Imagine compartilhar uma receita de bolo:", "text")
        self.print_colored("• SEM requirements.txt = 'Use farinha, ovos, açúcar...'", "text")
        self.print_colored("  - Quanto de cada? Que tipo? Vai dar errado!", "text")
        self.print_colored("• COM requirements.txt = '2 xícaras farinha, 3 ovos grandes...'", "text")
        self.print_colored("  - Receita exata! Todo mundo faz igual! 🎉", "text")
        
        # === COMO CRIAR ===
        self.print_colored("\n📝 CRIANDO SEU REQUIREMENTS.TXT:", "success")
        
        self.print_colored("\n1️⃣ Método automático (recomendado):", "primary")
        comando_freeze = '''# Depois de instalar todos os pacotes:
pip freeze > requirements.txt

# Isso cria um arquivo com TODAS as versões exatas:
requests==2.28.1
beautifulsoup4==4.11.1
certifi==2022.9.24
...'''
        self.exemplo(comando_freeze)
        
        self.print_colored("\n2️⃣ Método manual (mais controle):", "primary")
        manual_exemplo = '''# requirements.txt
requests>=2.25.0         # Versão 2.25.0 ou maior
django~=3.2.0           # Versão 3.2.x (não 3.3!)
pandas==1.3.5           # Exatamente esta versão
beautifulsoup4          # Qualquer versão (cuidado!)'''
        self.exemplo(manual_exemplo)
        
        # === USANDO REQUIREMENTS ===
        self.print_colored("\n🚀 INSTALANDO DE REQUIREMENTS.TXT:", "info")
        uso_requirements = '''# Clone um projeto e:
cd projeto
python -m venv venv
source venv/bin/activate  # ou venv\\Scripts\\activate no Windows
pip install -r requirements.txt

# Pronto! Ambiente idêntico ao do desenvolvedor!'''
        self.exemplo(uso_requirements)
        
        # === ESTRUTURA PROFISSIONAL ===
        self.print_colored("\n🏗️ ESTRUTURA PROFISSIONAL:", "warning")
        estrutura_pro = '''projeto/
├── requirements.txt          # Dependências principais
├── requirements-dev.txt      # Ferramentas de desenvolvimento
├── requirements-test.txt     # Bibliotecas de teste
└── requirements-prod.txt     # Versões exatas para produção'''
        
        self.print_colored(estrutura_pro, "text")
        
        self.print_success("\n🎉 Agora você sabe compartilhar projetos como um profissional!")
        self.pausar()
    
    def _secao_ferramentas_modernas(self) -> None:
        """Seção: Ferramentas modernas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FERRAMENTAS MODERNAS", "🚀", "accent")
        
        self.print_colored("✨ O futuro do gerenciamento de dependências Python!", "text")
        
        # === POETRY ===
        self.print_colored("\n🎭 POETRY - A estrela em ascensão:", "warning")
        self.print_colored("• Combina pip + venv + build + publish", "text")
        self.print_colored("• Um comando para tudo: poetry add requests", "text")
        self.print_colored("• Lock file automático (como npm)", "text")
        self.print_colored("• Resolver conflitos inteligentemente", "text")
        
        poetry_exemplo = '''# Iniciar projeto
poetry new meu-projeto

# Adicionar dependência
poetry add requests

# Instalar tudo
poetry install

# Rodar código
poetry run python app.py'''
        self.exemplo(poetry_exemplo)
        
        # === PIPENV ===
        self.print_colored("\n🐍 PIPENV - Simplicidade primeiro:", "info")
        self.print_colored("• pip + venv em um só comando", "text")
        self.print_colored("• Pipfile mais legível que requirements.txt", "text")
        self.print_colored("• Separa dependências de dev e produção", "text")
        
        pipenv_exemplo = '''# Criar ambiente e Pipfile
pipenv install requests

# Dependência de desenvolvimento
pipenv install --dev pytest

# Ativar shell
pipenv shell'''
        self.exemplo(pipenv_exemplo)
        
        # === CONDA ===
        self.print_colored("\n🔬 CONDA - Para cientistas de dados:", "success")
        self.print_colored("• Gerencia Python E outras linguagens", "text")
        self.print_colored("• Ótimo para bibliotecas científicas", "text")
        self.print_colored("• Resolve dependências complexas", "text")
        
        # === RECOMENDAÇÕES ===
        self.print_colored("\n🎯 QUAL USAR?", "warning")
        recomendacoes = [
            "📚 Aprendendo? → pip + venv (básico e essencial)",
            "🎨 Projeto novo? → Poetry (moderno e completo)",
            "🔬 Data Science? → conda (ecossistema científico)",
            "🏢 Empresa? → Siga o padrão da equipe!"
        ]
        
        for rec in recomendacoes:
            self.print_colored(f"• {rec}", "primary")
        
        self.pausar()
    
    def _secao_dicas_pro(self) -> None:
        """Seção: Dicas profissionais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DICAS PROFISSIONAIS", "⭐", "success")
        
        self.print_colored("🏆 Segredos dos desenvolvedores experientes!", "text")
        
        # === DICAS DE OURO ===
        dicas = [
            {
                'titulo': '🎯 SEMPRE use ambientes virtuais',
                'explicacao': 'Mesmo para projetos pequenos. É um hábito que salva vidas!',
                'exemplo': 'python -m venv venv && source venv/bin/activate'
            },
            {
                'titulo': '📝 .gitignore é seu amigo',
                'explicacao': 'NUNCA commite a pasta do ambiente virtual',
                'exemplo': '''# .gitignore
venv/
.venv/
env/
__pycache__/
*.pyc
.env'''
            },
            {
                'titulo': '🔄 Mantenha requirements.txt atualizado',
                'explicacao': 'Sempre que adicionar/remover pacotes',
                'exemplo': 'pip freeze > requirements.txt'
            },
            {
                'titulo': '📦 Use versões específicas em produção',
                'explicacao': 'Evita surpresas desagradáveis',
                'exemplo': 'django==3.2.15  # não use django>=3.2'
            },
            {
                'titulo': '🚀 Automatize com scripts',
                'explicacao': 'Crie scripts para setup rápido',
                'exemplo': '''#!/bin/bash
# setup.sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Ambiente pronto!"'''
            }
        ]
        
        for i, dica in enumerate(dicas, 1):
            self.print_colored(f"\n{dica['titulo']}", "warning")
            self.print_colored(f"💡 {dica['explicacao']}", "text")
            if dica['exemplo']:
                self.print_code_section("EXEMPLO", dica['exemplo'])
            
            if i < len(dicas):
                input("\n🔸 Pressione ENTER para a próxima dica...")
        
        # === TROUBLESHOOTING ===
        self.print_colored("\n🔧 PROBLEMAS COMUNS E SOLUÇÕES:", "error")
        problemas = [
            "❌ 'pip: command not found' → Ative o ambiente primeiro!",
            "❌ 'Permission denied' → Use ambiente virtual, não sudo",
            "❌ Versões conflitantes → Delete venv/ e recrie",
            "❌ Import error → Pacote não instalado no ambiente atual"
        ]
        
        for problema in problemas:
            self.print_colored(f"• {problema}", "text")
        
        self.print_success("\n🎉 Agora você tem o conhecimento dos profissionais!")
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
                'title': 'Quiz: Conhecimentos sobre Ambientes Virtuais',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual comando cria um ambiente virtual chamado "env"?',
                        'answer': ['python -m venv env', 'python3 -m venv env'],
                        'hint': 'Use o módulo venv do Python'
                    },
                    {
                        'question': 'Como ativar um ambiente virtual no Linux/Mac?',
                        'answer': ['source venv/bin/activate', 'source env/bin/activate', '. venv/bin/activate'],
                        'hint': 'Use o comando source'
                    },
                    {
                        'question': 'Qual comando gera o arquivo requirements.txt?',
                        'answer': ['pip freeze > requirements.txt', 'pip freeze>requirements.txt'],
                        'hint': 'Use pip freeze e redirecione a saída'
                    },
                    {
                        'question': 'Por que nunca devemos commitar a pasta venv?',
                        'answer': ['muito grande', 'específica do sistema', 'pode ser recriada', 'todas'],
                        'hint': 'Pense no tamanho e portabilidade'
                    },
                    {
                        'question': 'Qual ferramenta moderna combina pip + venv + build?',
                        'answer': ['poetry', 'Poetry'],
                        'hint': 'É uma ferramenta com nome artístico'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o comando para criar um ambiente virtual',
                        'starter': 'python -m ____ meu_projeto',
                        'solution': 'venv',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o comando para instalar do requirements.txt',
                        'starter': 'pip install ____ requirements.txt',
                        'solution': '-r',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o .gitignore para ignorar ambientes virtuais',
                        'starter': '# .gitignore\n____/\n.____/\nenv/\n__pycache__/',
                        'solution': 'venv\nvenv',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Crie seu Setup Script',
                'type': 'creative',
                'instruction': 'Crie um script (setup.sh ou setup.bat) que automatize a criação do ambiente virtual e instalação de dependências!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre ambientes virtuais",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um script de automação",
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
    
    def _run_quiz(self, quiz_data):
        """Executa o quiz interativo"""
        self.print_section(quiz_data['title'], "📝", "info")
        
        score = 0
        total = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\nPergunta {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            while True:
                try:
                    resposta = input("\n📝 Sua resposta: ").strip().lower()
                    
                    if resposta in ["help", "ajuda", "dica"]:
                        self.print_tip(q['hint'])
                        continue
                    
                    # Verifica se a resposta está correta
                    respostas_corretas = [ans.lower() for ans in q['answer']]
                    if resposta in respostas_corretas or any(resposta in ans for ans in respostas_corretas):
                        self.print_success("✅ Correto!")
                        score += 1
                        break
                    else:
                        self.print_warning("❌ Não está certo...")
                        tentar = input("Tentar novamente? (s/n): ").lower()
                        if tentar not in ['s', 'sim', 'yes']:
                            self.print_colored(f"💡 Resposta: {q['answer'][0]}", "info")
                            break
                
                except KeyboardInterrupt:
                    raise
        
        # Resultado final
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        percentual = (score / total) * 100
        self.print_colored(f"Você acertou {score} de {total} questões ({percentual:.0f}%)", "text")
        
        if percentual >= 80:
            self.print_success("🌟 Excelente! Você domina o conteúdo!")
        elif percentual >= 60:
            self.print_colored("💪 Muito bom! Continue praticando!", "warning")
        else:
            self.print_colored("📚 Revise o conteúdo e tente novamente!", "info")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _run_code_completion(self, exercise_data):
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "success")
        
        for i, exercise in enumerate(exercise_data['exercises'], 1):
            nivel = exercise['type'].upper()
            cor = {'SIMPLE': 'info', 'INTERMEDIATE': 'warning', 'ADVANCED': 'error'}.get(exercise['type'], 'text')
            
            self.print_colored(f"\n[{nivel}] {exercise['instruction']}", cor)
            self.print_code_section("CÓDIGO INICIAL", exercise['starter'])
            
            while True:
                try:
                    resposta = input("\n💻 Complete o código: ").strip()
                    
                    if resposta.lower() in ["help", "ajuda"]:
                        self.print_tip("Pense no que está faltando para o comando funcionar...")
                        continue
                    
                    if resposta.lower() == exercise['solution'].lower():
                        self.print_success("✅ Perfeito!")
                        # Mostra o código completo
                        codigo_completo = exercise['starter'].replace('____', exercise['solution'])
                        self.print_code_section("CÓDIGO COMPLETO", codigo_completo)
                        break
                    else:
                        self.print_warning("❌ Não está certo...")
                        mostrar = input("Ver a resposta? (s/n): ").lower()
                        if mostrar in ['s', 'sim', 'yes']:
                            self.print_colored(f"💡 Resposta: {exercise['solution']}", "info")
                            break
                
                except KeyboardInterrupt:
                    raise
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Exercícios de código completados!")
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _run_creative_exercise(self, exercise_data):
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "accent")
        
        self.print_colored(f"\n{exercise_data['instruction']}", "text")
        
        self.print_colored("\n💡 IDEIAS PARA SEU SCRIPT:", "warning")
        ideias = [
            "• Criar ambiente virtual automaticamente",
            "• Detectar sistema operacional (Windows/Linux/Mac)",
            "• Instalar requirements.txt se existir",
            "• Criar estrutura de pastas do projeto",
            "• Mostrar mensagens coloridas de progresso",
            "• Verificar se Python está instalado"
        ]
        
        for ideia in ideias:
            self.print_colored(ideia, "text")
        
        self.print_colored("\n📝 EXEMPLO DE INÍCIO:", "info")
        exemplo_script = '''#!/bin/bash
echo "🚀 Configurando projeto Python..."

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    exit 1
fi

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Continue daqui...'''
        
        self.print_code_section("SCRIPT INICIAL", exemplo_script)
        
        input("\n🎨 Use sua criatividade! Pressione ENTER quando terminar...")
        
        self.print_success("🎉 Ótimo trabalho! Scripts de automação economizam muito tempo!")
        
        # Mostra um exemplo completo
        mostrar = input("\nQuer ver um exemplo completo? (s/n): ").lower()
        if mostrar in ['s', 'sim', 'yes']:
            self._mostrar_script_completo()
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mostrar_script_completo(self):
        """Mostra exemplo de script completo"""
        script_completo = '''#!/bin/bash
# setup.sh - Script de setup automático

set -e  # Para se houver erro

echo "🚀 Configurando projeto Python..."

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 não encontrado!${NC}"
    exit 1
fi

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente
echo "🔑 Ativando ambiente..."
source venv/bin/activate

# Atualizar pip
echo "⬆️ Atualizando pip..."
pip install --upgrade pip

# Instalar dependências se existir requirements.txt
if [ -f requirements.txt ]; then
    echo "📚 Instalando dependências..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt não encontrado"
fi

# Criar estrutura de pastas
echo "📁 Criando estrutura do projeto..."
mkdir -p src tests docs

# Criar .gitignore se não existir
if [ ! -f .gitignore ]; then
    echo "📝 Criando .gitignore..."
    cat > .gitignore << EOF
venv/
.venv/
__pycache__/
*.pyc
.env
.DS_Store
.idea/
.vscode/
EOF
fi

echo -e "${GREEN}✅ Setup completo!${NC}"
echo "🎯 Para ativar o ambiente: source venv/bin/activate"'''
        
        self.print_code_section("SCRIPT COMPLETO", script_completo)
    
    def _mini_projeto_setup_profissional(self) -> None:
        """Mini Projeto - Setup Profissional de Projeto Python"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SETUP PROFISSIONAL DE PROJETO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SETUP PROFISSIONAL DE PROJETO")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um setup completo e profissional para seus projetos Python!")
        
        self.print_concept(
            "Setup Profissional",
            "Uma estrutura organizada com ambientes virtuais, dependências gerenciadas e automação completa"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de setup é usado por:", "text")
        usos_praticos = [
            "Netflix - Para padronizar todos os microsserviços",
            "Spotify - Garantir que todos os devs tenham o mesmo ambiente",
            "Instagram - Facilitar onboarding de novos desenvolvedores",
            "Startups - Economizar tempo e evitar problemas de configuração"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Estrutura do projeto
        self.print_section("PASSO 1: ESTRUTURA DO PROJETO", "📁", "info")
        self.print_tip("Uma boa estrutura é a base de todo projeto profissional!")
        
        try:
            nome_projeto = input("\n📝 Nome do seu projeto (ex: meu_app): ").strip() or "meu_projeto"
            
            estrutura = f'''{nome_projeto}/
├── .gitignore              # Arquivos para ignorar no git
├── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto
├── requirements-dev.txt    # Dependências de desenvolvimento
├── setup.py               # Configuração do pacote
├── src/                   # Código fonte
│   ├── __init__.py
│   └── main.py
├── tests/                 # Testes
│   ├── __init__.py
│   └── test_main.py
├── docs/                  # Documentação
│   └── README.md
└── scripts/               # Scripts úteis
    └── setup.sh          # Script de setup'''
            
            self.print_colored("\n📁 Estrutura criada:", "success")
            self.print_colored(estrutura, "text")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Arquivos essenciais
        self.print_section("PASSO 2: ARQUIVOS ESSENCIAIS", "📝", "success")
        self.print_colored("Vamos criar os arquivos fundamentais:", "text")
        
        # .gitignore
        self.print_colored("\n1️⃣ .gitignore - Para não commitar o que não deve:", "primary")
        gitignore_content = '''# Ambientes virtuais
venv/
.venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Env files
.env
.env.local

# Testing
.pytest_cache/
.coverage
htmlcov/

# Distribution
dist/
build/
*.egg-info/'''
        
        self.exemplo(gitignore_content)
        
        # README.md
        self.print_colored("\n2️⃣ README.md - Documentação principal:", "primary")
        readme_content = f'''# {nome_projeto.title()}

Descrição breve do que o projeto faz.

## 🚀 Quick Start

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/{nome_projeto}.git
cd {nome_projeto}

# Execute o setup automático
chmod +x scripts/setup.sh
./scripts/setup.sh

# Ou setup manual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
```

## 📋 Requisitos

- Python 3.8+
- pip

## 🛠️ Desenvolvimento

```bash
# Instalar dependências de dev
pip install -r requirements-dev.txt

# Executar testes
pytest

# Executar linter
flake8 src/

# Executar formatador
black src/
```

## 📦 Estrutura

```
{nome_projeto}/
├── src/        # Código fonte
├── tests/      # Testes
├── docs/       # Documentação
└── scripts/    # Scripts úteis
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.'''
        
        self.print_code_section("README.md", readme_content[:500] + "\n...")
        
        # PASSO 3: Script de automação
        self.print_section("PASSO 3: SCRIPT DE AUTOMAÇÃO", "🔧", "warning")
        
        self.print_colored("Criando script de setup automático:", "text")
        
        setup_script = '''#!/bin/bash
# scripts/setup.sh - Setup automático do projeto

set -e  # Para se houver erro

echo "🚀 Configurando projeto..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    exit 1
fi

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente
echo "🔑 Ativando ambiente..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Unix/Linux/macOS
    source venv/bin/activate
fi

# Atualizar pip
echo "⬆️ Atualizando pip..."
python -m pip install --upgrade pip

# Instalar dependências
if [ -f requirements.txt ]; then
    echo "📚 Instalando dependências..."
    pip install -r requirements.txt
fi

if [ -f requirements-dev.txt ]; then
    echo "🛠️ Instalando dependências de desenvolvimento..."
    pip install -r requirements-dev.txt
fi

# Criar estrutura se não existir
echo "📁 Verificando estrutura..."
mkdir -p src tests docs

echo "✅ Setup completo!"
echo "🎯 Para ativar o ambiente:"
echo "   Linux/Mac: source venv/bin/activate"
echo "   Windows: venv\\Scripts\\activate"'''
        
        self.exemplo(setup_script)
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("\nAqui está o código completo do arquivo principal:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: {nome_projeto.upper()}
# src/main.py

"""
{nome_projeto.title()} - Aplicação Python profissional
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent
VERSION = "0.1.0"


def main():
    """Função principal da aplicação"""
    print(f"🚀 {nome_projeto.title()} v{VERSION}")
    print(f"📁 Rodando de: {PROJECT_ROOT}")
    
    # Verificar ambiente
    if os.getenv("DEBUG", "False").lower() == "true":
        print("🔍 Modo DEBUG ativado")
    
    # Sua lógica aqui
    print("✨ Aplicação iniciada com sucesso!")
    

if __name__ == "__main__":
    main()'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        
        # Simular execução
        print(f"🚀 {nome_projeto.title()} v0.1.0")
        print(f"📁 Rodando de: /caminho/para/{nome_projeto}")
        print("✨ Aplicação iniciada com sucesso!")
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success(f"\n🎉 PARABÉNS! Você criou um setup profissional para {nome_projeto}!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar testes automatizados com pytest",
            "Configurar CI/CD com GitHub Actions",
            "Adicionar pre-commit hooks para qualidade",
            "Configurar Docker para deploy",
            "Implementar logging profissional",
            "Adicionar type hints e mypy"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de Projetos Python!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Setup Profissional de Projeto")
        
        self.pausar()