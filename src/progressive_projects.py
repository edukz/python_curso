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
    
    def __init__(self, ui_components=None, progress_manager=None):
        self.ui = ui_components
        self.progress = progress_manager
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
            return
            
        project_id, step = project_info
        progress = self.user_progress[project_id]
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header(f"🚀 PROJETO: {step.title}", f"Módulo {module_number}")
        
        self._display_project_intro(project_id, step, module_number)
        self._display_step_content(step)
        self._handle_step_interaction(project_id, step)
    
    def _display_project_intro(self, project_id: str, step: ProjectStep, module_number: int):
        """Exibe introdução do projeto"""
        project_names = {
            "biblioteca_pessoal": "📚 Sistema de Biblioteca Pessoal",
            "ecommerce_simples": "🛒 E-commerce Simples", 
            "api_dashboard": "📊 API e Dashboard Analytics"
        }
        
        print(f"\n🎯 {project_names[project_id]}")
        print("=" * 60)
        print(f"📍 Passo {module_number}/10 do projeto")
        print(f"⏱️ Tempo estimado: {step.estimated_time} minutos")
        print(f"📈 Dificuldade: {step.difficulty.title()}")
        print()
        print("🧠 Conceitos que você vai aprender:")
        for concept in step.concepts_learned:
            print(f"  • {concept}")
        print()
        
    def _display_step_content(self, step: ProjectStep):
        """Exibe conteúdo do passo"""
        print("📋 DESCRIÇÃO:")
        print("=" * 40)
        print(step.description)
        print()
        
        print("🔧 INSTRUÇÕES:")
        print("=" * 40)
        for i, instruction in enumerate(step.instructions, 1):
            print(f"{i:2d}. {instruction}")
        print()
        
        if step.code_template:
            print("💻 TEMPLATE DE CÓDIGO:")
            print("=" * 40)
            print(step.code_template)
            print()
        
        print("✅ CRITÉRIOS DE VALIDAÇÃO:")
        print("=" * 40)
        for criteria in step.validation_criteria:
            print(f"  ✓ {criteria}")
        print()
        
        if step.expected_output:
            print("📤 SAÍDA ESPERADA:")
            print("=" * 40)
            print(step.expected_output)
            print()
    
    def _handle_step_interaction(self, project_id: str, step: ProjectStep):
        """Gerencia interação do usuário com o passo"""
        print("🎮 OPÇÕES:")
        print("1. Continuar com o módulo")
        print("2. Ver código de exemplo")
        print("3. Marcar passo como concluído")
        print("4. Ver progresso do projeto")
        print("0. Pular projeto por enquanto")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            return
        elif choice == "2":
            self._show_example_code(step)
        elif choice == "3":
            self._mark_step_completed(project_id, step)
        elif choice == "4":
            self._show_project_progress(project_id)
        elif choice == "0":
            print("Você pode retomar o projeto a qualquer momento!")
            input("Pressione ENTER para continuar...")
    
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
            
            print(f"✅ Passo '{step.title}' marcado como concluído!")
            print(f"🎉 Você completou {len(progress.completed_steps)} passos do projeto!")
            
            # Verificar se projeto foi completado
            total_steps = len(self.projects[project_id])
            if len(progress.completed_steps) >= total_steps:
                progress.is_completed = True
                print(f"🏆 PARABÉNS! Você completou todo o projeto '{project_id}'!")
                
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
                description="Criar um sistema simples para armazenar informações de livros usando variáveis e print.",
                instructions=[
                    "Crie variáveis para título, autor, ano e gênero de um livro",
                    "Use input() para permitir que o usuário digite as informações",
                    "Exiba as informações formatadas na tela",
                    "Teste com pelo menos 2 livros diferentes"
                ],
                code_template="""
# Template: Sistema de Biblioteca - Passo 1
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor: ")
ano = input("Digite o ano de publicação: ")
genero = input("Digite o gênero: ")

print("\\n=== LIVRO CADASTRADO ===")
print(f"Título: {titulo}")
print(f"Autor: {autor}")
print(f"Ano: {ano}")
print(f"Gênero: {genero}")
                """,
                expected_output="Exibição formatada das informações do livro",
                validation_criteria=[
                    "Usa variáveis para armazenar dados",
                    "Usa input() para capturar dados do usuário", 
                    "Usa f-strings ou format() para exibir dados",
                    "Código está organizado e legível"
                ],
                concepts_learned=[
                    "Variáveis e tipos de dados",
                    "Função input() e output",
                    "F-strings e formatação",
                    "Estrutura básica de programa"
                ],
                difficulty="beginner",
                estimated_time=15
            ),
            ProjectStep(
                step_id="bib_002",
                module_id="modulo_2", 
                title="Validação e Controle de Fluxo",
                description="Adicionar validação de dados e controle de fluxo ao sistema de biblioteca.",
                instructions=[
                    "Adicione validação para ano (deve ser número entre 1000-2024)",
                    "Use if/else para verificar se livro é clássico (mais de 50 anos)",
                    "Implemente while loop para permitir cadastro de vários livros",
                    "Use break para sair do loop quando usuário digitar 'sair'"
                ],
                code_template="""
# Sistema de Biblioteca - Passo 2: Validação e Controle
while True:
    print("\\n=== CADASTRO DE LIVROS ===")
    titulo = input("Título (ou 'sair' para terminar): ")
    
    if titulo.lower() == 'sair':
        break
    
    autor = input("Autor: ")
    
    # Validação do ano
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if 1000 <= ano <= 2024:
                break
            else:
                print("Ano deve estar entre 1000 e 2024")
        except ValueError:
            print("Digite um número válido")
    
    genero = input("Gênero: ")
    
    # Verificar se é clássico
    ano_atual = 2024
    if (ano_atual - ano) >= 50:
        classificacao = "Clássico"
    else:
        classificacao = "Contemporâneo"
    
    print(f"\\n✅ Livro '{titulo}' cadastrado como {classificacao}!")
                """,
                expected_output="Sistema com validação e classificação automática",
                validation_criteria=[
                    "Valida entrada de ano corretamente",
                    "Usa if/else para classificar livros",
                    "Implementa loop while funcional",
                    "Trata exceções adequadamente"
                ],
                concepts_learned=[
                    "Estruturas condicionais (if/else)",
                    "Loops (while)",
                    "Tratamento de exceções (try/except)",
                    "Validação de entrada de dados"
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