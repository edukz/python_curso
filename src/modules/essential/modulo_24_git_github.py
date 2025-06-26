#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 24: Git e GitHub Essencial
Aprenda controle de versão com Git e GitHub
"""

import subprocess
import os
from ..shared.base_module import BaseModule


class Modulo24GitGithub(BaseModule):
    """Módulo 24: Git e GitHub Essencial"""
    
    def __init__(self):
        super().__init__("modulo_24", "Git e GitHub Essencial")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre Git e GitHub"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._git_github_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _git_github_module(self) -> None:
        """Conteúdo principal sobre Git e GitHub"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐙 MÓDULO 24: GIT E GITHUB ESSENCIAL")
        else:
            print("\n" + "="*60)
            print("🐙 MÓDULO 24: GIT E GITHUB ESSENCIAL")
            print("="*60)
        
        print("📝 Aprenda controle de versão com Git e GitHub!")
        print("🎯 Tópicos abordados:")
        print("• Fundamentos do controle de versão")
        print("• Comandos essenciais do Git")
        print("• Trabalhando com repositórios remotos")
        print("• GitHub: colaboração e workflow")
        print("• Branching e merging")
        print("• Resolução de conflitos")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._introducao_git()
        self._comandos_essenciais()
        self._trabalhando_com_repositorios()
        self._github_colaboracao()
        self._branching_merging()
        self._mini_projeto_git()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _introducao_git(self):
        """Introdução ao controle de versão"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📚 INTRODUÇÃO AO CONTROLE DE VERSÃO")
        
        print("🤔 O que é controle de versão?")
        print("• Sistema que registra mudanças em arquivos ao longo do tempo")
        print("• Permite voltar a versões anteriores")
        print("• Facilita colaboração entre desenvolvedores")
        print("• Rastreia quem fez que mudanças e quando")
        
        print("\n🌟 Por que usar Git?")
        print("• ⚡ Distribuído - cada clone é um backup completo")
        print("• 🚀 Rápido - operações locais são instantâneas") 
        print("• 🌳 Branching poderoso - crie linhas de desenvolvimento")
        print("• 🔒 Integridade - checksums garantem dados íntegros")
        print("• 🌍 Padrão da indústria - usado por milhões de projetos")
        
        print("\n📖 Conceitos fundamentais:")
        print("• Repository (repo) - pasta com histórico Git")
        print("• Working Directory - arquivos atuais do projeto")
        print("• Staging Area - arquivos preparados para commit")
        print("• Commit - snapshot do projeto em um momento")
        print("• Branch - linha independente de desenvolvimento")
        print("• Remote - versão do repo em outro local")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _comandos_essenciais(self):
        """Comandos essenciais do Git"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ COMANDOS ESSENCIAIS DO GIT")
        
        print("🛠️ Comandos básicos para começar:")
        
        comandos = [
            ("git init", "Inicializa repositório Git", "git init meu-projeto"),
            ("git clone", "Clona repositório existente", "git clone https://github.com/user/repo.git"),
            ("git status", "Mostra status dos arquivos", "git status"),
            ("git add", "Adiciona arquivos ao staging", "git add arquivo.py\ngit add .  # adiciona todos"),
            ("git commit", "Cria commit com mudanças", "git commit -m 'Adiciona nova feature'"),
            ("git push", "Envia commits para remoto", "git push origin main"),
            ("git pull", "Busca e merge do remoto", "git pull origin main"),
            ("git log", "Mostra histórico de commits", "git log --oneline")
        ]
        
        for comando, descricao, exemplo in comandos:
            print(f"\n📌 {comando}")
            print(f"   {descricao}")
            print(f"   💡 Exemplo: {exemplo}")
        
        print("\n🔄 Fluxo básico do Git:")
        print("1. Modificar arquivos (Working Directory)")
        print("2. git add - Preparar mudanças (Staging Area)")
        print("3. git commit - Salvar snapshot (Repository)")
        print("4. git push - Enviar para remoto")
        
        print("\n🆘 Comandos úteis para correções:")
        print("• git diff - Ver mudanças não commitadas")
        print("• git reset - Desfazer staging")
        print("• git checkout -- arquivo - Descartar mudanças")
        print("• git revert - Desfazer commit sem perder histórico")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _trabalhando_com_repositorios(self):
        """Trabalhando com repositórios remotos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌐 TRABALHANDO COM REPOSITÓRIOS REMOTOS")
        
        print("☁️ Repositórios remotos:")
        print("• GitHub - plataforma mais popular")
        print("• GitLab - alternativa open source")
        print("• Bitbucket - integração com Atlassian")
        print("• Azure DevOps - solução Microsoft")
        
        print("\n🔗 Configurando remoto:")
        codigo_remoto = '''# Adicionar repositório remoto
git remote add origin https://github.com/usuario/repo.git

# Ver remotos configurados
git remote -v

# Renomear remoto
git remote rename origin upstream

# Remover remoto
git remote remove origin'''
        
        print(codigo_remoto)
        
        print("\n📤 Enviando mudanças:")
        codigo_push = '''# Primeira vez - definir upstream
git push -u origin main

# Próximas vezes
git push

# Força push (cuidado!)
git push --force-with-lease'''
        
        print(codigo_push)
        
        print("\n📥 Recebendo mudanças:")
        codigo_pull = '''# Buscar e fazer merge
git pull origin main

# Apenas buscar (sem merge)
git fetch origin

# Ver diferenças antes do merge
git diff HEAD origin/main'''
        
        print(codigo_pull)
        
        print("\n🔑 Autenticação:")
        print("• SSH Keys - mais seguro, sem senha")
        print("• Personal Access Token - para HTTPS")
        print("• GitHub CLI - ferramenta oficial")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _github_colaboracao(self):
        """GitHub e colaboração"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🤝 GITHUB E COLABORAÇÃO")
        
        print("🌟 GitHub - além do Git:")
        print("• Issues - rastreamento de bugs e features")
        print("• Pull Requests - revisão de código")
        print("• Actions - CI/CD automatizado")
        print("• Projects - gerenciamento de tarefas")
        print("• Wiki - documentação do projeto")
        print("• Releases - versões do software")
        
        print("\n🔄 Workflow de colaboração:")
        print("1. 🍴 Fork do repositório")
        print("2. 📥 Clone do seu fork")
        print("3. 🌿 Criar branch para feature")
        print("4. 💻 Desenvolver e committar")
        print("5. 📤 Push da branch")
        print("6. 🔀 Criar Pull Request")
        print("7. 👀 Code Review")
        print("8. ✅ Merge após aprovação")
        
        print("\n📝 Boas práticas para commits:")
        print("• Use mensagens descritivas")
        print("• Primeira linha: resumo (até 50 chars)")
        print("• Linha em branco, depois detalhes")
        print("• Use verbos no imperativo")
        print("• Exemplos:")
        print("  ✅ 'Add user authentication'")
        print("  ✅ 'Fix login bug on mobile devices'")
        print("  ❌ 'Changed stuff'")
        print("  ❌ 'Fixed it'")
        
        print("\n🏷️ Conventional Commits:")
        print("• feat: nova funcionalidade")
        print("• fix: correção de bug")
        print("• docs: documentação")
        print("• style: formatação de código")
        print("• refactor: refatoração")
        print("• test: testes")
        print("• chore: tarefas de manutenção")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _branching_merging(self):
        """Branching e merging"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌳 BRANCHING E MERGING")
        
        print("🌿 Branches - linhas de desenvolvimento:")
        print("• main/master - branch principal")
        print("• develop - desenvolvimento ativo")
        print("• feature/* - novas funcionalidades")
        print("• hotfix/* - correções urgentes")
        print("• release/* - preparação de versões")
        
        print("\n⚡ Comandos de branch:")
        codigo_branch = '''# Listar branches
git branch
git branch -r  # remotas
git branch -a  # todas

# Criar e trocar para nova branch
git checkout -b feature/nova-funcionalidade
# ou no Git moderno:
git switch -c feature/nova-funcionalidade

# Trocar entre branches
git checkout main
git switch main

# Deletar branch
git branch -d feature/antiga
git branch -D feature/forcar-delete  # força'''
        
        print(codigo_branch)
        
        print("\n🔀 Merge - unindo branches:")
        codigo_merge = '''# Merge simples
git checkout main
git merge feature/minha-feature

# Merge com commit específico
git merge --no-ff feature/minha-feature

# Abortar merge em conflito
git merge --abort'''
        
        print(codigo_merge)
        
        print("\n⚔️ Resolvendo conflitos:")
        print("1. Git marca conflitos nos arquivos")
        print("2. Edite os arquivos manualmente")
        print("3. Remove marcadores de conflito")
        print("4. git add arquivo-resolvido")
        print("5. git commit (finaliza merge)")
        
        conflito_exemplo = '''<<<<<<< HEAD
print("Versão atual")
=======
print("Versão da branch")
>>>>>>> feature/nova-feature

# Resolva escolhendo uma ou combinando:
print("Versão final")'''
        
        print(f"\n💡 Exemplo de conflito:\n{conflito_exemplo}")
        
        print("\n🎯 Estratégias de merge:")
        print("• Fast-forward - move ponteiro da branch")
        print("• Three-way merge - cria commit de merge")
        print("• Rebase - reaplica commits em nova base")
        print("• Squash - combina todos commits em um")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_git(self):
        """Mini projeto: Sistema de controle de versão"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: MEU PRIMEIRO REPOSITÓRIO")
        
        print("📊 Vamos criar um projeto completo com Git!")
        print("🎯 Objetivos:")
        print("• Criar repositório local")
        print("• Fazer commits organizados")
        print("• Trabalhar com branches")
        print("• Simular colaboração")
        print("• Resolver conflitos")
        
        input("\n🔸 Pressione ENTER para começar o projeto...")
        
        # Projeto prático passo a passo
        print("\n" + "="*60)
        print("                TUTORIAL PRÁTICO")
        print("="*60)
        
        print("\n📁 PASSO 1: Criando o projeto")
        print("Execute os seguintes comandos:")
        comandos_1 = '''mkdir meu-primeiro-git
cd meu-primeiro-git
git init
echo "# Meu Primeiro Projeto Git" > README.md
git add README.md
git commit -m "feat: adiciona README inicial"'''
        print(comandos_1)
        
        print("\n📝 PASSO 2: Adicionando código")
        comandos_2 = '''# Criar arquivo Python
echo 'print("Olá, Git!")' > hello.py
git add hello.py
git commit -m "feat: adiciona script hello.py"

# Ver histórico
git log --oneline'''
        print(comandos_2)
        
        print("\n🌿 PASSO 3: Trabalhando com branches")
        comandos_3 = '''# Criar branch para nova feature
git checkout -b feature/calculadora

# Adicionar calculadora
echo 'def somar(a, b): return a + b' > calc.py
git add calc.py
git commit -m "feat: adiciona função de soma"

# Voltar para main e fazer merge
git checkout main
git merge feature/calculadora'''
        print(comandos_3)
        
        print("\n☁️ PASSO 4: Conectando ao GitHub")
        comandos_4 = '''# No GitHub, crie um repositório vazio
# Depois execute:
git remote add origin https://github.com/SEU_USUARIO/meu-primeiro-git.git
git branch -M main
git push -u origin main'''
        print(comandos_4)
        
        print("\n⚔️ PASSO 5: Simulando conflito")
        comandos_5 = '''# Criar duas branches conflitantes
git checkout -b feature/melhorar-hello
echo 'print("Olá, Mundo Git!")' > hello.py
git commit -am "feat: melhora mensagem de hello"

git checkout main
git checkout -b feature/novo-hello  
echo 'print("Bem-vindo ao Git!")' > hello.py
git commit -am "feat: nova mensagem de boas-vindas"

# Merge que causará conflito
git checkout main
git merge feature/melhorar-hello
git merge feature/novo-hello  # CONFLITO!'''
        print(comandos_5)
        
        print("\n🛠️ PASSO 6: Resolvendo conflito")
        print("1. Abra hello.py em um editor")
        print("2. Resolva o conflito manualmente")
        print("3. git add hello.py")
        print("4. git commit -m 'resolve: conflito em hello.py'")
        
        print("\n📊 PASSO 7: Comandos úteis")
        comandos_uteis = '''# Ver status
git status

# Ver diferenças
git diff

# Histórico visual
git log --graph --oneline --all

# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Ver arquivos em commit específico
git show HEAD:hello.py'''
        print(comandos_uteis)
        
        print("\n🎉 Parabéns! Você completou o projeto Git!")
        print("💡 Próximos passos:")
        print("• Explore GitHub Actions para CI/CD")
        print("• Aprenda sobre Git Flow ou GitHub Flow")
        print("• Pratique com projetos Open Source")
        print("• Configure SSH keys para segurança")
        print("• Use ferramentas visuais como GitKraken ou SourceTree")
        
        # Pontos do mini projeto
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            print(f"\n🎁 +{self.mini_project_points} pontos pelo projeto Git!")
        
        input("\n🔸 Pressione ENTER para finalizar o módulo...")