#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 24: Git e GitHub Essencial
Sistema completo de ensino de controle de versão
"""

import os
import time
import subprocess
from typing import Dict, List, Any, Optional
from ..ui_components import UIComponents
from ..progress_manager import ProgressManager


class GitGitHubModule:
    """Módulo completo de Git e GitHub"""
    
    def __init__(self, ui: UIComponents, progress: ProgressManager):
        self.ui = ui
        self.progress = progress
        self.module_id = "modulo_24"
        self.git_simulator = GitSimulator(ui)
        
    def executar(self) -> bool:
        """Executa o módulo completo"""
        try:
            self.ui.clear_screen()
            self.ui.header("🐙 MÓDULO 24: GIT E GITHUB ESSENCIAL", 
                          "Controle de Versão para Desenvolvedores")
            
            # Menu principal do módulo
            while True:
                self._mostrar_menu_principal()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._teoria_controle_versao()
                elif escolha == "2":
                    self._comandos_git_essenciais()
                elif escolha == "3":
                    self._workflow_github()
                elif escolha == "4":
                    self._exercicios_praticos()
                elif escolha == "5":
                    self._simulador_git()
                elif escolha == "6":
                    self._projeto_colaborativo()
                elif escolha == "7":
                    self._boas_praticas()
                elif escolha == "8":
                    self._troubleshooting()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            # Marca módulo como completo
            self.progress.complete_module(self.module_id)
            self.ui.success("🎉 Módulo Git e GitHub concluído!")
            return True
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")
            return False
    
    def _mostrar_menu_principal(self):
        """Exibe menu principal do módulo"""
        self.ui.clear_screen()
        self.ui.header("🐙 GIT E GITHUB ESSENCIAL", "Controle de Versão Profissional")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Teoria: Controle de Versão")
        print("2. 💻 Comandos Git Essenciais") 
        print("3. 🌐 Workflow GitHub")
        print("4. 🧪 Exercícios Práticos")
        print("5. 🎮 Simulador Git Interativo")
        print("6. 👥 Projeto Colaborativo")
        print("7. ⭐ Boas Práticas")
        print("8. 🔧 Troubleshooting")
        print("0. 🔙 Voltar ao Menu Principal")
    
    def _teoria_controle_versao(self):
        """Seção teórica sobre controle de versão"""
        self.ui.clear_screen()
        self.ui.header("📖 TEORIA: CONTROLE DE VERSÃO", "Fundamentos Essenciais")
        
        sections = [
            {
                "title": "🤔 O QUE É CONTROLE DE VERSÃO?",
                "content": [
                    "Sistema que registra mudanças em arquivos ao longo do tempo",
                    "Permite recuperar versões específicas quando necessário",
                    "Essencial para desenvolvimento individual e em equipe",
                    "Rastreia WHO, WHAT, WHEN, WHY das mudanças"
                ]
            },
            {
                "title": "📈 BENEFÍCIOS DO CONTROLE DE VERSÃO",
                "content": [
                    "✅ Histórico completo de mudanças",
                    "✅ Backup automático de código",
                    "✅ Colaboração eficiente em equipe",
                    "✅ Branches para features isoladas",
                    "✅ Merge inteligente de código",
                    "✅ Identificação de quem fez cada mudança"
                ]
            },
            {
                "title": "🐙 POR QUE GIT?",
                "content": [
                    "🚀 Sistema distribuído (cada clone é um backup completo)",
                    "⚡ Performance superior a outros VCS",
                    "🌟 Padrão da indústria (usado por 87% dos desenvolvedores)",
                    "🔀 Sistema de branches poderoso e flexível",
                    "🌐 Integração perfeita com GitHub, GitLab, etc.",
                    "📱 Suporte a projetos de qualquer tamanho"
                ]
            },
            {
                "title": "🏗️ CONCEITOS FUNDAMENTAIS",
                "content": [
                    "📁 Repository (repo): Pasta com histórico Git",
                    "💾 Commit: Snapshot do projeto em um momento",
                    "🌿 Branch: Linha paralela de desenvolvimento", 
                    "🔀 Merge: Integração de mudanças entre branches",
                    "📤 Push: Enviar commits para repositório remoto",
                    "📥 Pull: Buscar mudanças do repositório remoto",
                    "👥 Clone: Cópia local de repositório remoto",
                    "🔄 Fork: Cópia pessoal de repositório de terceiros"
                ]
            }
        ]
        
        for i, section in enumerate(sections, 1):
            print(f"\n{section['title']}")
            print("=" * 50)
            for item in section['content']:
                print(f"  {item}")
            
            if i < len(sections):
                input(f"\n🔸 Pressione ENTER para continuar para a seção {i+1}...")
                self.ui.clear_screen()
                self.ui.header("📖 TEORIA: CONTROLE DE VERSÃO", f"Seção {i+1}/{len(sections)}")
        
        self._mostrar_fluxo_git()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _mostrar_fluxo_git(self):
        """Mostra o fluxo básico do Git"""
        print("\n🔄 FLUXO BÁSICO DO GIT:")
        print("=" * 50)
        
        fluxo = [
            "1. 📝 Working Directory (você edita arquivos)",
            "2. ➕ git add (arquivos vão para Staging Area)", 
            "3. 💾 git commit (snapshot salvo no Repository)",
            "4. 📤 git push (enviar para repositório remoto)",
            "",
            "📥 git pull (buscar mudanças remotas)",
            "🔄 git merge (integrar mudanças)",
            "🌿 git branch (criar/mudar branches)"
        ]
        
        for step in fluxo:
            if step:
                print(f"  {step}")
            else:
                print()
    
    def _comandos_git_essenciais(self):
        """Ensina comandos Git essenciais"""
        self.ui.clear_screen()
        self.ui.header("💻 COMANDOS GIT ESSENCIAIS", "Toolkit do Desenvolvedor")
        
        categorias = {
            "🏁 CONFIGURAÇÃO INICIAL": [
                ("git config --global user.name \"Seu Nome\"", "Define seu nome"),
                ("git config --global user.email \"email@exemplo.com\"", "Define seu email"),
                ("git config --list", "Lista todas as configurações"),
                ("git init", "Inicia repositório Git na pasta atual")
            ],
            "📁 OPERAÇÕES BÁSICAS": [
                ("git status", "Mostra status dos arquivos"),
                ("git add arquivo.py", "Adiciona arquivo específico"),
                ("git add .", "Adiciona todos os arquivos modificados"),
                ("git commit -m \"mensagem\"", "Cria commit com mensagem"),
                ("git log", "Mostra histórico de commits"),
                ("git log --oneline", "Histórico resumido em uma linha")
            ],
            "🌐 REPOSITÓRIOS REMOTOS": [
                ("git remote add origin URL", "Conecta repositório remoto"),
                ("git push -u origin main", "Envia commits (primeira vez)"),
                ("git push", "Envia commits (após configurado)"),
                ("git pull", "Busca e integra mudanças remotas"),
                ("git clone URL", "Clona repositório existente"),
                ("git remote -v", "Lista repositórios remotos")
            ],
            "🌿 BRANCHES": [
                ("git branch", "Lista branches locais"),
                ("git branch nome-branch", "Cria nova branch"),
                ("git checkout nome-branch", "Muda para branch"),
                ("git checkout -b nova-branch", "Cria e muda para branch"),
                ("git merge branch-origem", "Integra branch na atual"),
                ("git branch -d nome-branch", "Deleta branch local")
            ],
            "🔄 NAVEGAÇÃO E HISTÓRICO": [
                ("git diff", "Mostra mudanças não commitadas"),
                ("git diff --staged", "Mostra mudanças no staging"),
                ("git show commit-hash", "Detalhes de commit específico"),
                ("git checkout commit-hash", "Vai para commit específico"),
                ("git reset --soft HEAD~1", "Desfaz último commit (mantém mudanças)"),
                ("git reset --hard HEAD~1", "Desfaz último commit (remove mudanças)")
            ]
        }
        
        for categoria, comandos in categorias.items():
            print(f"\n{categoria}")
            print("=" * 50)
            for comando, descricao in comandos:
                print(f"  📝 {comando:<35} | {descricao}")
            
            input("\n🔸 Pressione ENTER para próxima categoria...")
            if categoria != list(categorias.keys())[-1]:
                self.ui.clear_screen()
                self.ui.header("💻 COMANDOS GIT ESSENCIAIS", "Próxima Categoria")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _workflow_github(self):
        """Ensina workflow do GitHub"""
        self.ui.clear_screen()
        self.ui.header("🌐 WORKFLOW GITHUB", "Colaboração Profissional")
        
        workflows = [
            {
                "title": "🚀 CRIANDO SEU PRIMEIRO REPOSITÓRIO",
                "steps": [
                    "1. 🌐 Acesse github.com e faça login",
                    "2. ➕ Clique em 'New repository'",
                    "3. 📝 Escolha nome descritivo (ex: meu-primeiro-projeto)",
                    "4. ✅ Marque 'Add a README file'",
                    "5. 🎯 Escolha licença (MIT é uma boa opção)",
                    "6. 🟢 Clique 'Create repository'",
                    "",
                    "💡 DICA: Use nomes com hífens, não espaços!"
                ]
            },
            {
                "title": "📥 CLONANDO E CONFIGURANDO LOCALMENTE",
                "steps": [
                    "1. 📋 Copie a URL do repositório (botão verde 'Code')",
                    "2. 💻 Abra terminal na pasta desejada",
                    "3. 📥 git clone URL-do-repositorio",
                    "4. 📁 cd nome-do-repositorio",
                    "5. ✏️ Edite arquivos com seu editor favorito",
                    "6. 📝 git add .",
                    "7. 💾 git commit -m \"Primeira modificação\"",
                    "8. 📤 git push"
                ]
            },
            {
                "title": "🔄 WORKFLOW DIÁRIO DE DESENVOLVIMENTO",
                "steps": [
                    "🌅 INÍCIO DO DIA:",
                    "  📥 git pull (buscar atualizações)",
                    "",
                    "🛠️ DURANTE DESENVOLVIMENTO:",
                    "  📝 Editar código",
                    "  🧪 Testar mudanças",
                    "  ➕ git add arquivos-modificados",
                    "  💾 git commit -m \"Descrição clara\"",
                    "",
                    "🌆 FIM DO DIA:",
                    "  📤 git push (enviar para GitHub)",
                    "",
                    "💡 COMMITS FREQUENTES = SEGURANÇA!"
                ]
            },
            {
                "title": "🌿 TRABALHANDO COM BRANCHES",
                "steps": [
                    "1. 🌿 git checkout -b feature/nova-funcionalidade",
                    "2. 💻 Desenvolver a funcionalidade",
                    "3. 🧪 Testar completamente",
                    "4. 💾 git commit -m \"Implementa nova funcionalidade\"",
                    "5. 📤 git push -u origin feature/nova-funcionalidade",
                    "6. 🌐 Criar Pull Request no GitHub",
                    "7. 👥 Revisar código com equipe",
                    "8. 🔀 Merge na branch main",
                    "9. 🧹 Deletar branch feature"
                ]
            },
            {
                "title": "🤝 COLABORANDO EM PROJETOS OPEN SOURCE",
                "steps": [
                    "1. 🍴 Fork do repositório original",
                    "2. 📥 Clone do SEU fork",
                    "3. 🌿 Criar branch para sua contribuição",
                    "4. 💻 Implementar mudanças",
                    "5. 📤 Push para SEU fork",
                    "6. 📬 Criar Pull Request para repositório original",
                    "7. 💬 Responder feedback dos mantenedores",
                    "8. 🎉 Celebrar sua contribuição aceita!"
                ]
            }
        ]
        
        for i, workflow in enumerate(workflows, 1):
            print(f"\n{workflow['title']}")
            print("=" * 60)
            for step in workflow['steps']:
                print(f"  {step}")
            
            if i < len(workflows):
                input(f"\n🔸 Pressione ENTER para próximo workflow ({i+1}/{len(workflows)})...")
                self.ui.clear_screen()
                self.ui.header("🌐 WORKFLOW GITHUB", f"Workflow {i+1}/{len(workflows)}")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _exercicios_praticos(self):
        """Exercícios práticos de Git"""
        self.ui.clear_screen()
        self.ui.header("🧪 EXERCÍCIOS PRÁTICOS", "Aprenda Fazendo")
        
        exercicios = [
            {
                "titulo": "🏁 Exercício 1: Primeiro Repositório",
                "objetivo": "Criar e configurar seu primeiro repositório Git",
                "passos": [
                    "1. Crie uma pasta chamada 'meu-primeiro-git'",
                    "2. Inicialize um repositório Git",
                    "3. Configure seu nome e email",
                    "4. Crie um arquivo README.md",
                    "5. Faça seu primeiro commit",
                    "6. Verifique o histórico"
                ],
                "comandos": [
                    "mkdir meu-primeiro-git",
                    "cd meu-primeiro-git",
                    "git init",
                    "git config user.name \"Seu Nome\"",
                    "git config user.email \"seu@email.com\"",
                    "echo '# Meu Primeiro Projeto Git' > README.md",
                    "git add README.md",
                    "git commit -m \"Primeiro commit: adiciona README\"",
                    "git log --oneline"
                ]
            },
            {
                "titulo": "🌿 Exercício 2: Trabalhando com Branches",
                "objetivo": "Praticar criação e merge de branches",
                "passos": [
                    "1. Crie uma branch 'desenvolvimento'",
                    "2. Mude para essa branch",
                    "3. Crie um arquivo Python simples",
                    "4. Faça commit na branch desenvolvimento",
                    "5. Volte para main",
                    "6. Faça merge da branch desenvolvimento"
                ],
                "comandos": [
                    "git branch desenvolvimento",
                    "git checkout desenvolvimento",
                    "echo 'print(\"Hello from branch!\")' > hello.py",
                    "git add hello.py",
                    "git commit -m \"Adiciona hello.py\"",
                    "git checkout main",
                    "git merge desenvolvimento"
                ]
            },
            {
                "titulo": "🔄 Exercício 3: Simulação de Conflito",
                "objetivo": "Aprender a resolver conflitos de merge",
                "passos": [
                    "1. Crie duas branches: feature-a e feature-b",
                    "2. Em cada branch, modifique a mesma linha do mesmo arquivo",
                    "3. Faça merge de uma branch em main",
                    "4. Tente fazer merge da segunda (causará conflito)",
                    "5. Resolva o conflito manualmente",
                    "6. Complete o merge"
                ],
                "dica": "💡 Conflitos são normais! Eles mostram onde o Git precisa de sua ajuda para decidir qual código manter."
            }
        ]
        
        for i, exercicio in enumerate(exercicios, 1):
            print(f"\n{exercicio['titulo']}")
            print("=" * 60)
            print(f"🎯 OBJETIVO: {exercicio['objetivo']}")
            print("\n📋 PASSOS:")
            for passo in exercicio['passos']:
                print(f"  {passo}")
            
            if 'comandos' in exercicio:
                print("\n💻 COMANDOS:")
                for comando in exercicio['comandos']:
                    print(f"  $ {comando}")
            
            if 'dica' in exercicio:
                print(f"\n{exercicio['dica']}")
            
            if i < len(exercicios):
                input(f"\n🔸 Pressione ENTER para próximo exercício ({i+1}/{len(exercicios)})...")
                self.ui.clear_screen()
                self.ui.header("🧪 EXERCÍCIOS PRÁTICOS", f"Exercício {i+1}/{len(exercicios)}")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _simulador_git(self):
        """Simulador interativo de Git"""
        self.git_simulator.executar()
    
    def _projeto_colaborativo(self):
        """Projeto colaborativo simulado"""
        self.ui.clear_screen()
        self.ui.header("👥 PROJETO COLABORATIVO", "Simulação de Equipe")
        
        print("🎯 CENÁRIO: Você faz parte de uma equipe desenvolvendo um sistema de biblioteca")
        print("=" * 70)
        
        cenarios = [
            {
                "dia": "Segunda-feira",
                "tarefa": "Setup inicial do projeto",
                "acao": [
                    "🏗️ O líder da equipe criou o repositório 'sistema-biblioteca'",
                    "📥 Você recebeu acesso e deve clonar o projeto",
                    "📋 Configurar ambiente de desenvolvimento local",
                    "🌿 Criar branch 'setup-ambiente' para suas configurações"
                ]
            },
            {
                "dia": "Terça-feira", 
                "tarefa": "Implementar cadastro de livros",
                "acao": [
                    "🌿 Criar branch 'feature/cadastro-livros'",
                    "📝 Implementar classe Livro",
                    "🧪 Escrever testes unitários",
                    "💾 Fazer commits atômicos com mensagens claras",
                    "📤 Push da branch e criar Pull Request"
                ]
            },
            {
                "dia": "Quarta-feira",
                "tarefa": "Code Review e ajustes",
                "acao": [
                    "👀 Revisar Pull Request de colega (sistema de usuários)",
                    "💬 Deixar comentários construtivos no código",
                    "🔧 Aplicar sugestões do code review no seu PR",
                    "🔄 Fazer novo push com correções",
                    "✅ Aguardar aprovação final"
                ]
            },
            {
                "dia": "Quinta-feira",
                "tarefa": "Merge e integração",
                "acao": [
                    "🎉 Seu PR foi aprovado e merged!",
                    "📥 Fazer pull da main para pegar mudanças",
                    "🌿 Criar nova branch 'feature/busca-livros'",
                    "🔗 Integrar com código dos colegas",
                    "🧪 Testar compatibilidade"
                ]
            },
            {
                "dia": "Sexta-feira",
                "tarefa": "Release e deploy",
                "acao": [
                    "🏷️ Participar da criação da tag v1.0.0",
                    "📦 Preparar release notes",
                    "🚀 Deploy em ambiente de staging",
                    "📊 Revisar métricas do projeto",
                    "🍕 Celebrar release com a equipe!"
                ]
            }
        ]
        
        for i, cenario in enumerate(cenarios, 1):
            print(f"\n📅 {cenario['dia'].upper()} - {cenario['tarefa']}")
            print("-" * 50)
            for acao in cenario['acao']:
                print(f"  {acao}")
            
            if i < len(cenarios):
                input(f"\n🔸 Pressione ENTER para o próximo dia ({i+1}/5)...")
                self.ui.clear_screen()
                self.ui.header("👥 PROJETO COLABORATIVO", f"Dia {i+1}/5")
        
        print("\n🎓 LIÇÕES APRENDIDAS:")
        print("=" * 40)
        licoes = [
            "🔄 Sempre fazer pull antes de começar nova feature",
            "🌿 Uma branch por feature = organização",
            "💬 Code review melhora qualidade e conhecimento",
            "📝 Commits claros facilitam o trabalho em equipe",
            "🧪 Testes evitam quebrar código dos colegas",
            "🏷️ Tags marcam versões importantes",
            "📊 Métricas ajudam a acompanhar progresso"
        ]
        
        for licao in licoes:
            print(f"  {licao}")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _boas_praticas(self):
        """Boas práticas de Git e GitHub"""
        self.ui.clear_screen()
        self.ui.header("⭐ BOAS PRÁTICAS", "Git e GitHub Profissional")
        
        categorias = {
            "💬 MENSAGENS DE COMMIT": {
                "boas": [
                    "✅ feat: adiciona sistema de login",
                    "✅ fix: corrige bug na validação de email",
                    "✅ docs: atualiza README com instruções",
                    "✅ refactor: melhora performance da busca",
                    "✅ test: adiciona testes para módulo auth"
                ],
                "ruins": [
                    "❌ mudanças",
                    "❌ fix",
                    "❌ coisas",
                    "❌ update",
                    "❌ ."
                ],
                "formato": "tipo: descrição clara do que foi feito"
            },
            "🌿 ESTRATÉGIA DE BRANCHES": {
                "modelo": [
                    "🌟 main/master: código em produção",
                    "🚀 develop: integração de features",
                    "🌿 feature/nome: nova funcionalidade",
                    "🐛 bugfix/nome: correção de bug",
                    "🔥 hotfix/nome: correção urgente"
                ],
                "regras": [
                    "🚫 Nunca committar direto na main",
                    "🔄 Sempre usar Pull Requests",
                    "🧪 Testar antes de fazer merge",
                    "🧹 Deletar branches após merge"
                ]
            },
            "📁 ORGANIZAÇÃO DE ARQUIVOS": {
                "include": [
                    "✅ Código fonte",
                    "✅ README.md detalhado",
                    "✅ requirements.txt / package.json",
                    "✅ .gitignore apropriado",
                    "✅ Licença do projeto",
                    "✅ Documentação"
                ],
                "ignore": [
                    "❌ Arquivos compilados (.pyc, .class)",
                    "❌ Dependências (node_modules/, venv/)",
                    "❌ Arquivos temporários (.tmp, .log)",
                    "❌ Configurações locais (.env)",
                    "❌ Arquivos do IDE (.vscode/, .idea/)"
                ]
            },
            "🔒 SEGURANÇA": {
                "nunca": [
                    "🚨 Senhas ou tokens",
                    "🚨 Chaves de API",
                    "🚨 Arquivos de configuração sensíveis",
                    "🚨 Dados pessoais de usuários",
                    "🚨 Credenciais de banco de dados"
                ],
                "sempre": [
                    "✅ Use .env para variáveis sensíveis",
                    "✅ Configure .gitignore corretamente",
                    "✅ Use GitHub Secrets para CI/CD",
                    "✅ Revise commits antes de push"
                ]
            }
        }
        
        for categoria, detalhes in categorias.items():
            print(f"\n{categoria}")
            print("=" * 50)
            
            for secao, items in detalhes.items():
                print(f"\n📋 {secao.upper()}:")
                for item in items:
                    print(f"  {item}")
            
            input("\n🔸 Pressione ENTER para próxima categoria...")
            if categoria != list(categorias.keys())[-1]:
                self.ui.clear_screen()
                self.ui.header("⭐ BOAS PRÁTICAS", "Próxima Categoria")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _troubleshooting(self):
        """Solução de problemas comuns"""
        self.ui.clear_screen()
        self.ui.header("🔧 TROUBLESHOOTING", "Soluções para Problemas Comuns")
        
        problemas = [
            {
                "problema": "😱 'git: command not found'",
                "causa": "Git não está instalado",
                "solucao": [
                    "🪟 Windows: Baixar de git-scm.com",
                    "🍎 Mac: brew install git",
                    "🐧 Linux: sudo apt install git",
                    "✅ Verificar: git --version"
                ]
            },
            {
                "problema": "🚫 'Permission denied (publickey)'",
                "causa": "Problema com chaves SSH",
                "solucao": [
                    "🔑 Gerar chave SSH: ssh-keygen -t ed25519 -C \"email\"",
                    "📋 Copiar chave: cat ~/.ssh/id_ed25519.pub",
                    "⚙️ Adicionar no GitHub (Settings > SSH Keys)",
                    "🧪 Testar: ssh -T git@github.com"
                ]
            },
            {
                "problema": "💥 Conflito de merge",
                "causa": "Duas pessoas modificaram a mesma linha",
                "solucao": [
                    "👀 Abrir arquivo com conflito",
                    "🔍 Procurar por <<<<<<< e >>>>>>>",
                    "✏️ Editar mantendo o código correto",
                    "🗑️ Remover marcadores de conflito",
                    "➕ git add arquivo-resolvido",
                    "💾 git commit (sem -m para usar editor)"
                ]
            },
            {
                "problema": "😵 'detached HEAD state'",
                "causa": "Checkout para commit específico",
                "solucao": [
                    "🏠 Voltar para branch: git checkout main",
                    "🌿 Ou criar branch: git checkout -b nova-branch",
                    "💡 HEAD detached = você não está em branch"
                ]
            },
            {
                "problema": "📝 Commit com mensagem errada",
                "causa": "Typo ou mensagem inadequada",
                "solucao": [
                    "📝 Último commit: git commit --amend -m \"Nova mensagem\"",
                    "⚠️ Só se ainda não fez push!",
                    "🚨 Se já fez push, deixe como está"
                ]
            },
            {
                "problema": "🗑️ Deletei arquivo por engano",
                "causa": "rm arquivo importante",
                "solucao": [
                    "🔍 Se ainda não commitou: git checkout arquivo",
                    "📚 Se já commitou: git log --oneline",
                    "⏮️ Voltar versão: git checkout hash-commit -- arquivo",
                    "💾 Fazer novo commit com arquivo restaurado"
                ]
            },
            {
                "problema": "📦 Repository muito grande",
                "causa": "Arquivos grandes no histórico",
                "solucao": [
                    "🎯 Usar Git LFS para arquivos grandes",
                    "🧹 BFG Repo-Cleaner para limpar histórico",
                    "📝 Configurar .gitignore para prevenir",
                    "⚠️ Operações avançadas - fazer backup!"
                ]
            }
        ]
        
        for i, item in enumerate(problemas, 1):
            print(f"\n🔴 PROBLEMA {i}: {item['problema']}")
            print(f"🔍 CAUSA: {item['causa']}")
            print("🔧 SOLUÇÃO:")
            for step in item['solucao']:
                print(f"  {step}")
            
            if i < len(problemas):
                input(f"\n🔸 Pressione ENTER para próximo problema ({i+1}/{len(problemas)})...")
                self.ui.clear_screen()
                self.ui.header("🔧 TROUBLESHOOTING", f"Problema {i+1}/{len(problemas)}")
        
        print("\n💡 DICAS IMPORTANTES:")
        print("=" * 30)
        dicas = [
            "📚 Sempre leia a mensagem de erro completa",
            "🔍 Google é seu amigo para erros específicos",
            "💾 Faça backup antes de comandos 'perigosos'",
            "👥 Peça ajuda - comunidade Git é muito receptiva",
            "📖 Documentação oficial é excelente: git-scm.com"
        ]
        
        for dica in dicas:
            print(f"  {dica}")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")


class GitSimulator:
    """Simulador interativo de comandos Git"""
    
    def __init__(self, ui: UIComponents):
        self.ui = ui
        self.estado = {
            "branch_atual": "main",
            "staged_files": [],
            "modified_files": [],
            "commits": [
                {"hash": "a1b2c3d", "message": "Initial commit", "author": "System"}
            ],
            "branches": ["main"]
        }
    
    def executar(self):
        """Executa simulador Git"""
        self.ui.clear_screen()
        self.ui.header("🎮 SIMULADOR GIT INTERATIVO", "Pratique sem Medo!")
        
        print("🎯 INSTRUÇÕES:")
        print("  • Digite comandos Git como se fosse um terminal real")
        print("  • O simulador mostrará o resultado de cada comando")
        print("  • Digite 'help' para ver comandos disponíveis")
        print("  • Digite 'exit' para sair do simulador")
        print("  • Digite 'reset' para voltar ao estado inicial")
        
        while True:
            self._mostrar_status()
            comando = input(f"\n({self.estado['branch_atual']}) $ git ").strip().lower()
            
            if comando == "exit":
                break
            elif comando == "help":
                self._mostrar_ajuda()
            elif comando == "reset":
                self._reset_simulador()
            else:
                self._processar_comando(comando)
    
    def _mostrar_status(self):
        """Mostra status atual do repositório simulado"""
        print(f"\n📁 REPOSITÓRIO SIMULADO (Branch: {self.estado['branch_atual']})")
        print("=" * 50)
        
        if self.estado['staged_files']:
            print("🟢 Arquivos em staging:")
            for arquivo in self.estado['staged_files']:
                print(f"  ➕ {arquivo}")
        
        if self.estado['modified_files']:
            print("🟡 Arquivos modificados:")
            for arquivo in self.estado['modified_files']:
                print(f"  📝 {arquivo}")
        
        if not self.estado['staged_files'] and not self.estado['modified_files']:
            print("✅ Working directory clean")
    
    def _processar_comando(self, comando):
        """Processa comando Git digitado"""
        if comando == "status":
            print("📊 git status executado!")
            
        elif comando.startswith("add"):
            if "." in comando:
                self.estado['staged_files'].extend(self.estado['modified_files'])
                self.estado['modified_files'] = []
                print("✅ Todos os arquivos adicionados ao staging!")
            else:
                arquivo = comando.replace("add", "").strip()
                if arquivo in self.estado['modified_files']:
                    self.estado['modified_files'].remove(arquivo)
                    self.estado['staged_files'].append(arquivo)
                    print(f"✅ {arquivo} adicionado ao staging!")
                else:
                    print("❌ Arquivo não encontrado ou já em staging")
                    
        elif comando.startswith("commit"):
            if self.estado['staged_files']:
                message = "Commit simulado"
                if "-m" in comando:
                    parts = comando.split('"')
                    if len(parts) >= 2:
                        message = parts[1]
                
                new_commit = {
                    "hash": f"x{len(self.estado['commits'])}y{len(self.estado['commits'])}z",
                    "message": message,
                    "author": "Você"
                }
                self.estado['commits'].append(new_commit)
                self.estado['staged_files'] = []
                print(f"✅ Commit criado: {new_commit['hash']} - {message}")
            else:
                print("❌ Nada para committar! Use 'git add' primeiro")
                
        elif comando == "log":
            print("📚 Histórico de commits:")
            for commit in reversed(self.estado['commits'][-5:]):
                print(f"  💾 {commit['hash']} - {commit['message']} ({commit['author']})")
                
        elif comando.startswith("branch"):
            if len(comando.split()) == 1:
                print("🌿 Branches disponíveis:")
                for branch in self.estado['branches']:
                    marker = "* " if branch == self.estado['branch_atual'] else "  "
                    print(f"  {marker}{branch}")
            else:
                nova_branch = comando.split()[1]
                self.estado['branches'].append(nova_branch)
                print(f"✅ Branch '{nova_branch}' criada!")
                
        elif comando.startswith("checkout"):
            if len(comando.split()) >= 2:
                target = comando.split()[1]
                if target in self.estado['branches']:
                    self.estado['branch_atual'] = target
                    print(f"✅ Mudou para branch '{target}'")
                else:
                    print(f"❌ Branch '{target}' não existe")
            else:
                print("❌ Especifique uma branch para checkout")
                
        elif comando == "push":
            print("📤 Simulando push para origin...")
            print("✅ Push realizado com sucesso!")
            
        elif comando == "pull":
            print("📥 Simulando pull do origin...")
            # Simula mudança externa
            self.estado['modified_files'].append("arquivo_remoto.py")
            print("✅ Pull realizado! Novos arquivos baixados")
            
        else:
            print(f"❓ Comando '{comando}' não reconhecido. Digite 'help' para ajuda")
        
        # Simula mudanças aleatórias ocasionalmente
        import random
        if random.random() < 0.2:  # 20% chance
            arquivos_exemplo = ["main.py", "utils.py", "config.py", "README.md"]
            arquivo = random.choice(arquivos_exemplo)
            if arquivo not in self.estado['modified_files'] and arquivo not in self.estado['staged_files']:
                self.estado['modified_files'].append(arquivo)
    
    def _mostrar_ajuda(self):
        """Mostra comandos disponíveis no simulador"""
        print("\n📖 COMANDOS DISPONÍVEIS:")
        print("=" * 30)
        comandos = [
            "status - Mostra status dos arquivos",
            "add . - Adiciona todos os arquivos",
            "add arquivo - Adiciona arquivo específico",
            "commit -m \"mensagem\" - Cria commit",
            "log - Mostra histórico",
            "branch - Lista branches",
            "branch nome - Cria nova branch",
            "checkout nome - Muda para branch",
            "push - Envia para repositório remoto",
            "pull - Busca do repositório remoto"
        ]
        
        for comando in comandos:
            print(f"  📝 {comando}")
    
    def _reset_simulador(self):
        """Reseta simulador para estado inicial"""
        self.estado = {
            "branch_atual": "main",
            "staged_files": [],
            "modified_files": ["exemplo.py"],  # Começa com um arquivo modificado
            "commits": [
                {"hash": "a1b2c3d", "message": "Initial commit", "author": "System"}
            ],
            "branches": ["main"]
        }
        print("🔄 Simulador resetado para estado inicial!")