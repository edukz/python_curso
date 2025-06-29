#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Projetos Graduais
Projetos reais que evoluem através dos módulos do curso
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

@dataclass
class ProjectStep:
    """Representa um passo de um projeto"""
    step_id: str
    module_id: str
    title: str
    description: str
    instructions: List[str]
    code_template: str
    expected_output: str
    validation_criteria: List[str]
    concepts_learned: List[str]
    difficulty: str  # "beginner", "intermediate", "advanced"
    estimated_time: int  # em minutos
    
@dataclass
class ProjectProgress:
    """Progresso do usuário em um projeto"""
    project_id: str
    current_step: int
    completed_steps: List[str]
    code_submissions: Dict[str, str]
    last_updated: str
    total_time_spent: int
    is_completed: bool

class ProgressiveProjectsSystem:
    """Sistema principal de projetos graduais"""
    
    def __init__(self, ui_components=None, progress_manager=None, course_controller=None):
        self.ui = ui_components
        self.progress = progress_manager
        self.course_controller = course_controller
        self.projects = self._load_projects()
        self.user_progress = self._load_user_progress()
        
    def _load_projects(self) -> Dict[str, List[ProjectStep]]:
        """Carrega definições dos projetos"""
        return {
            "biblioteca_pessoal": self._get_biblioteca_project(),
            "ecommerce_simples": self._get_ecommerce_project(), 
            "api_dashboard": self._get_api_dashboard_project()
        }
    
    def _load_user_progress(self) -> Dict[str, ProjectProgress]:
        """Carrega progresso do usuário"""
        progress_file = "data/projects_progress.json"
        if os.path.exists(progress_file):
            try:
                with open(progress_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return {
                        k: ProjectProgress(**v) for k, v in data.items()
                    }
            except:
                pass
        
        # Inicializar progresso vazio
        return {
            "biblioteca_pessoal": ProjectProgress(
                project_id="biblioteca_pessoal",
                current_step=0,
                completed_steps=[],
                code_submissions={},
                last_updated=datetime.now().isoformat(),
                total_time_spent=0,
                is_completed=False
            ),
            "ecommerce_simples": ProjectProgress(
                project_id="ecommerce_simples", 
                current_step=0,
                completed_steps=[],
                code_submissions={},
                last_updated=datetime.now().isoformat(),
                total_time_spent=0,
                is_completed=False
            ),
            "api_dashboard": ProjectProgress(
                project_id="api_dashboard",
                current_step=0, 
                completed_steps=[],
                code_submissions={},
                last_updated=datetime.now().isoformat(),
                total_time_spent=0,
                is_completed=False
            )
        }
    
    def save_progress(self):
        """Salva progresso dos projetos"""
        os.makedirs("data", exist_ok=True)
        progress_data = {
            k: asdict(v) for k, v in self.user_progress.items()
        }
        
        with open("data/projects_progress.json", 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, indent=2, ensure_ascii=False)
    
    def reload_progress(self):
        """Recarrega progresso dos projetos do arquivo"""
        self.user_progress = self._load_user_progress()
    
    def get_project_for_module(self, module_number: int) -> Optional[tuple]:
        """Retorna projeto e passo correspondente ao módulo"""
        if 1 <= module_number <= 10:
            project_id = "biblioteca_pessoal"
            step_index = module_number - 1
        elif 11 <= module_number <= 20:
            project_id = "ecommerce_simples"
            step_index = module_number - 11
        elif 21 <= module_number <= 30:
            project_id = "api_dashboard"
            step_index = module_number - 21
        else:
            return None
            
        if project_id in self.projects:
            steps = self.projects[project_id]
            if step_index < len(steps):
                return (project_id, steps[step_index])
        
        return None
    
    def show_project_step(self, module_number: int):
        """Exibe o passo do projeto para o módulo atual"""
        project_info = self.get_project_for_module(module_number)
        if not project_info:
            return None
            
        project_id, step = project_info
        progress = self.user_progress[project_id]
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header(f"🚀 PROJETO: {step.title}", f"Módulo {module_number}")
        
        self._display_project_intro(project_id, step, module_number)
        self._display_step_content(step)
        return self._handle_step_interaction(project_id, step, module_number)
    
    def _display_project_intro(self, project_id: str, step: ProjectStep, module_number: int):
        """Exibe introdução do projeto"""
        project_names = {
            "biblioteca_pessoal": "📚 Sistema de Biblioteca Pessoal",
            "ecommerce_simples": "🛒 E-commerce Simples", 
            "api_dashboard": "📊 API e Dashboard Analytics"
        }
        
        if self.ui:
            # Use o sistema de cores melhorado
            info_color = self.ui.get_color("info")
            accent_color = self.ui.get_color("accent")
            text_color = self.ui.get_color("text")
            reset = self.ui.get_color("reset")
            
            print(f"\n{accent_color}🎯 {project_names[project_id]}{reset}")
            print(f"{info_color}{'─' * 50}{reset}")
            print(f"{info_color}📍 Passo {module_number}/10{reset} • {text_color}⏱️ {step.estimated_time}min{reset} • {accent_color}📈 {step.difficulty.title()}{reset}")
            print()
            print(f"{accent_color}🧠 Conceitos principais:{reset}")
            for concept in step.concepts_learned:
                print(f"  {info_color}•{reset} {text_color}{concept}{reset}")
        else:
            # Fallback sem cores
            print(f"\n🎯 {project_names[project_id]}")
            print("─" * 50)
            print(f"📍 Passo {module_number}/10 • ⏱️ {step.estimated_time}min • 📈 {step.difficulty.title()}")
            print()
            print("🧠 Conceitos principais:")
            for concept in step.concepts_learned:
                print(f"  • {concept}")
        print()
        
    def _display_step_content(self, step: ProjectStep):
        """Exibe conteúdo detalhado do passo"""
        if self.ui:
            # Seções organizadas com cores
            section_color = self.ui.get_color("warning")
            content_color = self.ui.get_color("text")
            code_color = self.ui.get_color("primary")
            success_color = self.ui.get_color("success")
            reset = self.ui.get_color("reset")
            
            # Descrição
            print(f"{section_color}📋 DESCRIÇÃO{reset}")
            print(f"{content_color}{step.description}{reset}")
            print()
            
            # Instruções
            print(f"{section_color}🔧 PASSO A PASSO{reset}")
            for i, instruction in enumerate(step.instructions, 1):
                print(f" {section_color}{i}.{reset} {content_color}{instruction}{reset}")
            print()
            
            # Template de código
            if step.code_template:
                print(f"{section_color}💻 TEMPLATE INICIAL{reset}")
                print(f"{code_color}{step.code_template}{reset}")
                print()
            
            # Critérios
            print(f"{section_color}✅ VALIDAÇÃO{reset}")
            for criteria in step.validation_criteria:
                print(f"  {success_color}✓{reset} {content_color}{criteria}{reset}")
            print()
        else:
            # Fallback sem cores
            print("📋 DESCRIÇÃO")
            print(step.description)
            print()
            
            print("🔧 PASSO A PASSO")
            for i, instruction in enumerate(step.instructions, 1):
                print(f" {i}. {instruction}")
            print()
            
            if step.code_template:
                print("💻 TEMPLATE INICIAL")
                print(step.code_template)
                print()
            
            print("✅ VALIDAÇÃO")
            for criteria in step.validation_criteria:
                print(f"  ✓ {criteria}")
            print()
        
        if step.expected_output:
            if self.ui:
                section_color = self.ui.get_color("warning")
                content_color = self.ui.get_color("text")
                reset = self.ui.get_color("reset")
                print(f"{section_color}📤 RESULTADO ESPERADO{reset}")
                print(f"{content_color}{step.expected_output}{reset}")
            else:
                print("📤 RESULTADO ESPERADO")
                print(step.expected_output)
            print()
    
    def _handle_step_interaction(self, project_id: str, step: ProjectStep, module_number: int):
        """Gerencia interação do usuário com o passo"""
        if self.ui:
            # Menu redesenhado com cores
            menu_color = self.ui.get_color("accent")
            option_color = self.ui.get_color("primary")
            input_color = self.ui.get_color("warning")
            reset = self.ui.get_color("reset")
            
            print(f"\n{menu_color}{'═' * 50}{reset}")
            print(f"{menu_color}🎯 O QUE FAZER AGORA?{reset}")
            print(f"{menu_color}{'═' * 50}{reset}")
            print(f"{option_color}1.{reset} 🚀 Continuar com o módulo")
            print(f"{option_color}2.{reset} 💡 Ver código de exemplo")
            print(f"{option_color}3.{reset} ✅ Marcar passo como concluído")
            print(f"{option_color}4.{reset} 📈 Ver progresso do projeto")
            print(f"{option_color}0.{reset} 🚪 Pular projeto por enquanto")
            print(f"{menu_color}{'═' * 50}{reset}")
            
            choice = input(f"\n{input_color}👉 Sua escolha: {reset}").strip()
        else:
            # Fallback sem cores
            print("\n" + "═" * 50)
            print("🎯 O QUE FAZER AGORA?")
            print("═" * 50)
            print("1. 🚀 Continuar com o módulo")
            print("2. 💡 Ver código de exemplo")
            print("3. ✅ Marcar passo como concluído")
            print("4. 📈 Ver progresso do projeto")
            print("0. 🚪 Pular projeto por enquanto")
            print("═" * 50)
            
            choice = input("\n👉 Sua escolha: ").strip()
        
        if choice == "1":
            # Retorna o número do módulo para execução
            return f"execute_module_{module_number}"
        elif choice == "2":
            self._show_example_code(step)
            # Recursively call to show menu again
            return self._handle_step_interaction(project_id, step, module_number)
        elif choice == "3":
            self._mark_step_completed(project_id, step)
            # Após marcar como concluído, retorna None para voltar ao menu
            return None
        elif choice == "4":
            self._show_project_progress(project_id)
            # Recursively call to show menu again
            return self._handle_step_interaction(project_id, step, module_number)
        elif choice == "0":
            if self.ui:
                success_color = self.ui.get_color("success")
                reset = self.ui.get_color("reset")
                print(f"\n{success_color}✅ Você pode retomar o projeto a qualquer momento!{reset}")
            else:
                print("\n✅ Você pode retomar o projeto a qualquer momento!")
            input("Pressione ENTER para continuar...")
            return None
        else:
            if self.ui:
                error_color = self.ui.get_color("error")
                reset = self.ui.get_color("reset")
                print(f"\n{error_color}❌ Opção inválida! Tente novamente.{reset}")
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            # Recursively call to show menu again
            return self._handle_step_interaction(project_id, step, module_number)
    
    def _show_example_code(self, step: ProjectStep):
        """Mostra código de exemplo para o passo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("💡 CÓDIGO DE EXEMPLO", step.title)
        
        print("📝 Este é um exemplo de como resolver este passo:")
        print("=" * 50)
        print(step.code_template)
        print()
        print("💡 Dicas importantes:")
        for criteria in step.validation_criteria:
            print(f"  • {criteria}")
        
        input("\nPressione ENTER para voltar...")
    
    def _mark_step_completed(self, project_id: str, step: ProjectStep):
        """Marca passo como concluído"""
        progress = self.user_progress[project_id]
        
        if step.step_id not in progress.completed_steps:
            progress.completed_steps.append(step.step_id)
            progress.current_step += 1
            progress.last_updated = datetime.now().isoformat()
            
            # Salvar progresso
            self.save_progress()
            
            if self.ui:
                success_color = self.ui.get_color("success")
                info_color = self.ui.get_color("info")
                reset = self.ui.get_color("reset")
                
                print(f"\n{success_color}{'✅' * 25}{reset}")
                print(f"{success_color}✅ Passo '{step.title}' marcado como concluído!{reset}")
                print(f"{info_color}🎉 Você completou {len(progress.completed_steps)} passos do projeto!{reset}")
                print(f"{success_color}{'✅' * 25}{reset}")
            else:
                print(f"✅ Passo '{step.title}' marcado como concluído!")
                print(f"🎉 Você completou {len(progress.completed_steps)} passos do projeto!")
            
            # Verificar se projeto foi completado
            total_steps = len(self.projects[project_id])
            if len(progress.completed_steps) >= total_steps:
                progress.is_completed = True
                if self.ui:
                    celebration_color = self.ui.get_color("warning")
                    print(f"\n{celebration_color}🏆 PARABÉNS! Você completou todo o projeto '{project_id}'!{reset}")
                else:
                    print(f"🏆 PARABÉNS! Você completou todo o projeto '{project_id}'!")
                
        else:
            if self.ui:
                info_color = self.ui.get_color("info")
                reset = self.ui.get_color("reset")
                print(f"{info_color}ℹ️ Este passo já foi marcado como concluído.{reset}")
            else:
                print("ℹ️ Este passo já foi marcado como concluído.")
            
        input("Pressione ENTER para continuar...")
    
    def _show_project_progress(self, project_id: str):
        """Mostra progresso geral do projeto"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 PROGRESSO DO PROJETO", project_id.title())
        
        progress = self.user_progress[project_id]
        total_steps = len(self.projects[project_id])
        completed = len(progress.completed_steps)
        completion_percentage = (completed / total_steps) * 100
        
        print(f"📈 Progresso: {completed}/{total_steps} passos ({completion_percentage:.1f}%)")
        print(f"⏱️ Tempo gasto: {progress.total_time_spent} minutos")
        print(f"📅 Última atualização: {progress.last_updated[:10]}")
        print()
        
        print("📋 PASSOS COMPLETADOS:")
        print("=" * 40)
        for step_id in progress.completed_steps:
            # Encontrar título do passo
            for step in self.projects[project_id]:
                if step.step_id == step_id:
                    print(f"  ✅ {step.title}")
                    break
        
        print("\n📋 PRÓXIMOS PASSOS:")
        print("=" * 40)
        for step in self.projects[project_id]:
            if step.step_id not in progress.completed_steps:
                print(f"  ⏳ {step.title}")
                break
        
        input("\nPressione ENTER para continuar...")
    
    # ========= DEFINIÇÕES DOS PROJETOS =========
    
    def _get_biblioteca_project(self) -> List[ProjectStep]:
        """Define projeto Sistema de Biblioteca Pessoal (Módulos 1-10)"""
        return [
            ProjectStep(
                step_id="bib_001",
                module_id="modulo_1",
                title="Cadastro de Livros Básico",
                description="""🎯 OBJETIVO DO PROJETO:
Vamos criar seu primeiro programa Python! Imagine que você tem uma coleção de livros em casa e quer organizá-los no computador. Este projeto vai ensinar você a:

📚 O QUE VAMOS FAZER:
• Perguntar para o usuário informações sobre um livro (como título, autor, etc.)
• Guardar essas informações na "memória" do computador (usando variáveis)
• Mostrar as informações organizadas na tela

🌟 POR QUE ISSO É ÚTIL:
• É a base de qualquer sistema de cadastro (lojas, escolas, hospitais)
• Você aprende os conceitos fundamentais de programação
• É algo que você pode mostrar para família e amigos!

💡 CONCEITOS QUE VOCÊ VAI DOMINAR:
• Variáveis: Como o computador "lembra" das informações
• Input: Como fazer perguntas para o usuário
• Print: Como mostrar informações na tela
• F-strings: Como deixar o texto bonito e organizado""",
                instructions=[
                    "📝 PASSO 1: Entenda o que são variáveis\n   → Variáveis são como 'caixas' onde guardamos informações\n   → Exemplo: titulo = 'Harry Potter' (guardamos o nome do livro na caixa 'titulo')",
                    
                    "🗣️ PASSO 2: Aprenda a fazer perguntas para o usuário\n   → Use input() para perguntar algo\n   → Exemplo: nome = input('Qual seu nome?')\n   → O que o usuário digitar será guardado na variável 'nome'",
                    
                    "📋 PASSO 3: Colete as informações do livro\n   → Pergunte o título, autor, ano e gênero\n   → Guarde cada resposta em uma variável diferente\n   → Dica: Use nomes claros como 'titulo', 'autor', 'ano', 'genero'",
                    
                    "✨ PASSO 4: Exiba as informações de forma organizada\n   → Use print() para mostrar as informações\n   → Use f-strings para deixar bonito: f'Título: {titulo}'\n   → Crie uma 'ficha' visual do livro",
                    
                    "🔄 PASSO 5: Teste com livros diferentes\n   → Execute o programa pelo menos 2 vezes\n   → Use livros que você conhece\n   → Veja como cada execução guarda informações diferentes"
                ],
                code_template="""# 🐍 MEU PRIMEIRO PROGRAMA PYTHON! 🐍
# Sistema de Biblioteca - Cadastro de Livros

# 📝 PARTE 1: COLETANDO INFORMAÇÕES
# As linhas abaixo fazem perguntas para o usuário
# O que for digitado será guardado nas "caixas" (variáveis)

titulo = input("📚 Digite o título do livro: ")
# ↑ Esta linha pergunta o título e guarda na variável 'titulo'

autor = input("✍️ Digite o autor: ")
# ↑ Esta linha pergunta o autor e guarda na variável 'autor'

ano = input("📅 Digite o ano de publicação: ")
# ↑ Esta linha pergunta o ano e guarda na variável 'ano'

genero = input("📖 Digite o gênero (ficção, romance, etc.): ")
# ↑ Esta linha pergunta o gênero e guarda na variável 'genero'

# 📋 PARTE 2: EXIBINDO AS INFORMAÇÕES
# Agora vamos mostrar tudo organizado na tela

print("\\n" + "="*40)  # Cria uma linha decorativa
print("📚✨ LIVRO CADASTRADO COM SUCESSO! ✨📚")
print("="*40)
print(f"📖 Título: {titulo}")
print(f"✍️ Autor: {autor}")
print(f"📅 Ano: {ano}")
print(f"📚 Gênero: {genero}")
print("="*40)
print("🎉 Parabéns! Seu livro foi adicionado à biblioteca!")

# 💡 EXPLICAÇÃO DO CÓDIGO:
# - input() = pergunta algo para o usuário
# - = (igual) = guarda a resposta numa variável
# - print() = mostra algo na tela
# - f"{variavel}" = coloca o conteúdo da variável no texto""",
                expected_output="""EXEMPLO DO QUE VOCÊ VERÁ:

Quando executar o programa, aparecerá:
📚 Digite o título do livro: [usuário digita: O Pequeno Príncipe]
✍️ Digite o autor: [usuário digita: Antoine de Saint-Exupéry]
📅 Digite o ano de publicação: [usuário digita: 1943]
📖 Digite o gênero: [usuário digita: Fábula]

========================================
📚✨ LIVRO CADASTRADO COM SUCESSO! ✨📚
========================================
📖 Título: O Pequeno Príncipe
✍️ Autor: Antoine de Saint-Exupéry
📅 Ano: 1943
📚 Gênero: Fábula
========================================
🎉 Parabéns! Seu livro foi adicionado à biblioteca!""",
                validation_criteria=[
                    "✅ O programa faz 4 perguntas (título, autor, ano, gênero)",
                    "✅ As respostas são guardadas em variáveis com nomes claros",
                    "✅ As informações são exibidas de forma organizada e bonita",
                    "✅ O código tem comentários explicando cada parte",
                    "✅ Usa f-strings para inserir as variáveis no texto",
                    "✅ Funciona quando você digita diferentes livros"
                ],
                concepts_learned=[
                    "🗃️ VARIÁVEIS: Como criar 'caixas' para guardar informações (titulo = 'Harry Potter')",
                    "🗣️ FUNÇÃO INPUT(): Como fazer perguntas para o usuário e receber respostas",
                    "📺 FUNÇÃO PRINT(): Como mostrar informações na tela de forma organizada",
                    "✨ F-STRINGS: Como inserir variáveis dentro de textos (f'Título: {titulo}')",
                    "📝 COMENTÁRIOS: Como explicar seu código usando # (muito importante!)",
                    "🏗️ ESTRUTURA DE PROGRAMA: Como organizar código em seções lógicas"
                ],
                difficulty="beginner",
                estimated_time=15
            ),
            ProjectStep(
                step_id="bib_002",
                module_id="modulo_2", 
                title="Sistema Inteligente - Validação e Decisões",
                description="""🎯 EVOLUINDO SEU PROGRAMA:
Agora vamos tornar seu programa mais inteligente! No projeto anterior, você aprendeu o básico. Agora vamos ensinar o computador a:

🧠 O QUE VAMOS ADICIONAR:
• Verificar se as informações estão corretas (validação)
• Tomar decisões automáticas (if/else)
• Permitir cadastrar vários livros de uma vez (loops)
• Classificar livros automaticamente (ex: clássico ou moderno)

🌟 POR QUE ISSO É REVOLUCIONÁRIO:
• Seu programa agora "pensa" e toma decisões
• Não aceita mais informações inválidas
• Funciona como um sistema profissional
• Você está aprendendo lógica de programação!

💡 NOVOS CONCEITOS SUPER IMPORTANTES:
• Condições (if/else): Como o programa toma decisões
• Loops (while): Como repetir ações automaticamente
• Validação: Como verificar se dados estão corretos
• Break: Como parar um loop quando necessário""",
                instructions=[
                    "🛡️ PASSO 1: Aprenda sobre validação de dados\n   → Validação = verificar se a informação está certa\n   → Exemplo: ano deve ser um número, não uma palavra\n   → Se estiver errado, peça para digitar novamente",
                    
                    "🤔 PASSO 2: Ensine o programa a tomar decisões\n   → Use if/else para fazer verificações\n   → Exemplo: if ano < 1974: print('Livro clássico!')\n   → O programa vai classificar automaticamente",
                    
                    "🔄 PASSO 3: Implemente loops para cadastros múltiplos\n   → Use while True: para repetir o cadastro\n   → Permita cadastrar vários livros seguidos\n   → O usuário escolhe quando parar",
                    
                    "🚪 PASSO 4: Adicione uma 'porta de saída'\n   → Use break para sair do loop\n   → Quando usuário digitar 'sair', o programa para\n   → Sempre deixe uma forma de sair!",
                    
                    "✨ PASSO 5: Teste o sistema completo\n   → Tente cadastrar livros válidos e inválidos\n   → Veja como o programa se comporta\n   → Teste a classificação automática de livros"
                ],
                code_template="""# 🧠 SISTEMA INTELIGENTE DE BIBLIOTECA 🧠
# Agora com validação e decisões automáticas!

print("🏛️ Bem-vindo ao Sistema Inteligente de Biblioteca!")
print("📚 Agora podemos cadastrar vários livros e classificá-los automaticamente!")

# 🔄 LOOP PRINCIPAL - Permite cadastrar vários livros
while True:
    print("\\n" + "="*50)
    print("📚 NOVO CADASTRO DE LIVRO")
    print("="*50)
    
    # 🚪 PORTA DE SAÍDA - sempre tenha uma!
    titulo = input("📖 Título do livro (ou digite 'sair' para terminar): ")
    
    # 🤔 PRIMEIRA DECISÃO: O usuário quer sair?
    if titulo.lower() == 'sair':
        print("👋 Obrigado por usar o sistema! Até logo!")
        break  # ← Isso para o loop
    
    # 📝 Coletando outras informações
    autor = input("✍️ Autor: ")
    genero = input("📚 Gênero: ")
    
    # 🛡️ VALIDAÇÃO INTELIGENTE DO ANO
    print("\\n📅 Agora vamos validar o ano...")
    while True:  # ← Loop para validação
        try:
            ano = int(input("Ano de publicação (1000-2024): "))
            
            # 🤔 SEGUNDA DECISÃO: O ano está válido?
            if 1000 <= ano <= 2024:
                print(f"✅ Ano {ano} é válido!")
                break  # ← Sai do loop de validação
            else:
                print("❌ Erro: Ano deve estar entre 1000 e 2024")
                print("💡 Tente novamente...")
                
        except ValueError:
            print("❌ Erro: Digite apenas números!")
            print("💡 Exemplo: 1997, 2020, etc.")
    
    # 🧠 CLASSIFICAÇÃO AUTOMÁTICA (Inteligência Artificial básica!)
    ano_atual = 2024
    idade_livro = ano_atual - ano
    
    # 🤔 TERCEIRA DECISÃO: É clássico ou contemporâneo?
    if idade_livro >= 50:
        classificacao = "📜 CLÁSSICO"
        emoji_classe = "📜"
    else:
        classificacao = "🆕 CONTEMPORÂNEO"
        emoji_classe = "🆕"
    
    # 📋 EXIBINDO RESULTADO COMPLETO
    print("\\n" + "🎉"*20)
    print("✅ LIVRO CADASTRADO COM SUCESSO!")
    print("🎉"*20)
    print(f"📖 Título: {titulo}")
    print(f"✍️ Autor: {autor}")
    print(f"📅 Ano: {ano}")
    print(f"📚 Gênero: {genero}")
    print(f"{emoji_classe} Classificação: {classificacao}")
    print(f"🕐 Idade do livro: {idade_livro} anos")
    print("="*50)

print("\\n🎓 PARABÉNS! Você criou um sistema inteligente!")
print("💡 Seu programa agora:")
print("   ✅ Valida dados automaticamente")
print("   ✅ Toma decisões sozinho")
print("   ✅ Processa múltiplos livros")
print("   ✅ Classifica livros automaticamente")

# 💡 CONCEITOS APRENDIDOS:
# - while True = loop infinito (até encontrar break)
# - if/else = tomada de decisões
# - try/except = tratamento de erros
# - break = para sair de loops
# - Validação = verificar se dados estão corretos""",
                expected_output="""EXEMPLO DO SISTEMA EM FUNCIONAMENTO:

🏛️ Bem-vindo ao Sistema Inteligente de Biblioteca!
📚 Agora podemos cadastrar vários livros e classificá-los automaticamente!

==================================================
📚 NOVO CADASTRO DE LIVRO
==================================================
📖 Título do livro: O Senhor dos Anéis
✍️ Autor: J.R.R. Tolkien
📚 Gênero: Fantasia

📅 Agora vamos validar o ano...
Ano de publicação (1000-2024): 1954
✅ Ano 1954 é válido!

🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
✅ LIVRO CADASTRADO COM SUCESSO!
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
📖 Título: O Senhor dos Anéis
✍️ Autor: J.R.R. Tolkien
📅 Ano: 1954
📚 Gênero: Fantasia
📜 Classificação: 📜 CLÁSSICO
🕐 Idade do livro: 70 anos
==================================================""",
                validation_criteria=[
                    "✅ O programa aceita múltiplos cadastros (loop while funciona)",
                    "✅ Valida anos corretamente (só aceita números entre 1000-2024)",
                    "✅ Trata erros quando usuário digita texto em vez de número",
                    "✅ Classifica livros automaticamente (clássico vs contemporâneo)",
                    "✅ Permite sair digitando 'sair' (break funciona)",
                    "✅ Código bem comentado explicando cada parte"
                ],
                concepts_learned=[
                    "🔄 LOOPS (while): Como repetir ações até uma condição ser atendida",
                    "🤔 CONDIÇÕES (if/else): Como o programa toma decisões automáticas",
                    "🛡️ VALIDAÇÃO: Como verificar se dados estão corretos antes de usar",
                    "🚨 TRATAMENTO DE ERROS (try/except): Como lidar com entradas inválidas",
                    "🚪 CONTROLE DE FLUXO (break): Como sair de loops quando necessário",
                    "📊 CÁLCULOS: Como fazer operações matemáticas simples (idade do livro)"
                ],
                difficulty="beginner",
                estimated_time=20
            ),
            ProjectStep(
                step_id="bib_003",
                module_id="modulo_3",
                title="Lista de Livros e Busca",
                description="Implementar armazenamento em lista e função de busca básica.",
                instructions=[
                    "Crie lista para armazenar todos os livros",
                    "Modifique cadastro para adicionar livros à lista",
                    "Implemente função para listar todos os livros",
                    "Crie função de busca por título",
                    "Adicione menu de opções (cadastrar, listar, buscar)"
                ],
                code_template="""
# Sistema de Biblioteca - Passo 3: Lista e Busca
biblioteca = []

def cadastrar_livro():
    # ... código de cadastro ...
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'genero': genero,
        'classificacao': classificacao
    }
    biblioteca.append(livro)
    print(f"📚 Livro adicionado! Total: {len(biblioteca)} livros")

def listar_livros():
    if not biblioteca:
        print("📭 Nenhum livro cadastrado ainda.")
        return
    
    print(f"\\n📚 BIBLIOTECA ({len(biblioteca)} livros):")
    print("-" * 50)
    for i, livro in enumerate(biblioteca, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def buscar_livro():
    if not biblioteca:
        print("📭 Biblioteca vazia!")
        return
    
    termo = input("Digite o título a buscar: ").lower()
    encontrados = []
    
    for livro in biblioteca:
        if termo in livro['titulo'].lower():
            encontrados.append(livro)
    
    if encontrados:
        print(f"\\n🔍 Encontrados {len(encontrados)} livro(s):")
        for livro in encontrados:
            print(f"• {livro['titulo']} - {livro['autor']}")
    else:
        print("❌ Nenhum livro encontrado.")

# Menu principal
while True:
    print("\\n=== BIBLIOTECA PESSOAL ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    # ... implementar menu ...
                """,
                expected_output="Sistema com menu e funcionalidades de busca",
                validation_criteria=[
                    "Lista armazena livros corretamente",
                    "Menu de opções funcional",
                    "Busca encontra livros por título",
                    "Funções bem organizadas"
                ],
                concepts_learned=[
                    "Listas e métodos de lista",
                    "Dicionários para estruturar dados",
                    "Funções (def)",
                    "Menu de opções com loop"
                ],
                difficulty="beginner",
                estimated_time=25
            ),
            # Continuando com os demais módulos 4-10...
            ProjectStep(
                step_id="bib_004",
                module_id="modulo_4",
                title="Persistência em Arquivo",
                description="Salvar e carregar biblioteca em arquivo JSON.",
                instructions=[
                    "Implemente função para salvar biblioteca em arquivo JSON",
                    "Crie função para carregar dados do arquivo",
                    "Adicione tratamento para arquivo não existir",
                    "Chame carregar_dados() no início do programa",
                    "Chame salvar_dados() sempre que cadastrar livro"
                ],
                code_template="""
import json
import os

ARQUIVO_BIBLIOTECA = "biblioteca.json"

def salvar_dados():
    try:
        with open(ARQUIVO_BIBLIOTECA, 'w', encoding='utf-8') as arquivo:
            json.dump(biblioteca, arquivo, indent=2, ensure_ascii=False)
        print("💾 Dados salvos automaticamente!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

def carregar_dados():
    global biblioteca
    if os.path.exists(ARQUIVO_BIBLIOTECA):
        try:
            with open(ARQUIVO_BIBLIOTECA, 'r', encoding='utf-8') as arquivo:
                biblioteca = json.load(arquivo)
            print(f"📂 Carregados {len(biblioteca)} livros do arquivo!")
        except Exception as e:
            print(f"❌ Erro ao carregar: {e}")
            biblioteca = []
    else:
        biblioteca = []
        print("📝 Criando nova biblioteca...")

# Inicializar dados
carregar_dados()
                """,
                expected_output="Sistema que persiste dados entre execuções",
                validation_criteria=[
                    "Salva dados em JSON corretamente",
                    "Carrega dados na inicialização",
                    "Trata erros de arquivo adequadamente",
                    "Encoding UTF-8 preserva acentos"
                ],
                concepts_learned=[
                    "Manipulação de arquivos",
                    "JSON para persistência",
                    "Tratamento de exceções",
                    "Encoding de caracteres"
                ],
                difficulty="intermediate",
                estimated_time=30
            )
        ]
    
    def _get_ecommerce_project(self) -> List[ProjectStep]:
        """Define projeto E-commerce Simples (Módulos 11-20)"""
        return [
            ProjectStep(
                step_id="ecom_001", 
                module_id="modulo_11",
                title="Catálogo de Produtos",
                description="Criar um sistema de catálogo usando classes e objetos.",
                instructions=[
                    "Criar classe Produto com atributos nome, preço, categoria",
                    "Implementar método __str__ para exibição",
                    "Criar lista de produtos", 
                    "Implementar função para listar produtos"
                ],
                code_template="""
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} ({self.categoria})"

# Criar catálogo
catalogo = []
# Adicionar produtos...
                """,
                expected_output="Lista de produtos formatada",
                validation_criteria=[
                    "Classe Produto bem definida",
                    "Método __str__ implementado",
                    "Lista de produtos funcional"
                ],
                concepts_learned=[
                    "Classes e objetos",
                    "Métodos especiais",
                    "Listas de objetos"
                ],
                difficulty="intermediate", 
                estimated_time=25
            ),
            # Mais passos do e-commerce...
        ]
    
    def _get_api_dashboard_project(self) -> List[ProjectStep]:
        """Define projeto API e Dashboard (Módulos 21-30)"""
        return [
            ProjectStep(
                step_id="api_001",
                module_id="modulo_21", 
                title="API de Dados Básica",
                description="Criar uma API simples usando Flask para servir dados.",
                instructions=[
                    "Instalar Flask",
                    "Criar endpoint básico /api/data",
                    "Retornar dados JSON",
                    "Testar com curl ou browser"
                ],
                code_template="""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    dados = {
        'usuarios': 150,
        'vendas': 2500,
        'produtos': 45
    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
                """,
                expected_output="API funcionando em localhost:5000",
                validation_criteria=[
                    "Flask instalado e funcionando",
                    "Endpoint retorna JSON válido",
                    "Dados estruturados corretamente"
                ],
                concepts_learned=[
                    "APIs REST básicas",
                    "Flask framework", 
                    "JSON e serialização"
                ],
                difficulty="advanced",
                estimated_time=35
            ),
            # Mais passos da API...
        ]