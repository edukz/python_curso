#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulos Essenciais do Curso de Python
Ferramentas fundamentais que todo desenvolvedor Python deve dominar
"""

import os
import time
import subprocess
import sys
from typing import Dict, List, Any, Optional
from ..ui_components import UIComponents
from ..progress_manager import ProgressManager
from .modulo_24_git_github import GitGitHubModule


class EssentialModules:
    """Classe que contém os módulos essenciais do curso"""
    
    def __init__(self):
        self.ui = None
        self.progress = None
        
    def set_dependencies(self, ui: UIComponents, progress: ProgressManager):
        """Define dependências necessárias"""
        self.ui = ui
        self.progress = progress

    def modulo_24_git_github(self) -> None:
        """Módulo 24: Git e GitHub Essencial"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
            
        git_module = GitGitHubModule(self.ui, self.progress)
        git_module.executar()

    def modulo_25_terminal_cli(self) -> None:
        """Módulo 25: Terminal e Command Line Interface"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("🐧 MÓDULO 25: TERMINAL E COMMAND LINE", 
                          "Domine a Interface de Linha de Comando")
            
            while True:
                self._mostrar_menu_terminal()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._teoria_terminal()
                elif escolha == "2":
                    self._comandos_basicos()
                elif escolha == "3":
                    self._navegacao_arquivos()
                elif escolha == "4":
                    self._manipulacao_arquivos()
                elif escolha == "5":
                    self._pipes_redirecionamento()
                elif escolha == "6":
                    self._bash_scripting_basico()
                elif escolha == "7":
                    self._exercicios_terminal()
                elif escolha == "8":
                    self._simulador_terminal()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_25")
            self.ui.success("🎉 Módulo Terminal concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    def modulo_26_ambientes_virtuais(self) -> None:
        """Módulo 26: Ambientes Virtuais e Gerenciamento de Dependências"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("📦 MÓDULO 26: AMBIENTES VIRTUAIS", 
                          "Isolamento e Gerenciamento de Dependências")
            
            while True:
                self._mostrar_menu_venv()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._teoria_ambientes_virtuais()
                elif escolha == "2":
                    self._criando_venv()
                elif escolha == "3":
                    self._gerenciamento_pip()
                elif escolha == "4":
                    self._requirements_txt()
                elif escolha == "5":
                    self._boas_praticas_dependencias()
                elif escolha == "6":
                    self._exercicios_venv()
                elif escolha == "7":
                    self._projeto_pratico_venv()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_26")
            self.ui.success("🎉 Módulo Ambientes Virtuais concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    def modulo_27_testes_tdd(self) -> None:
        """Módulo 27: Testes e Test-Driven Development"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("🧪 MÓDULO 27: TESTES E TDD", 
                          "Test-Driven Development e Qualidade de Código")
            
            while True:
                self._mostrar_menu_testes()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._teoria_testes()
                elif escolha == "2":
                    self._unittest_basico()
                elif escolha == "3":
                    self._pytest_introducao()
                elif escolha == "4":
                    self._tdd_na_pratica()
                elif escolha == "5":
                    self._mocks_fixtures()
                elif escolha == "6":
                    self._coverage_testes()
                elif escolha == "7":
                    self._exercicios_tdd()
                elif escolha == "8":
                    self._projeto_com_testes()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_27")
            self.ui.success("🎉 Módulo Testes e TDD concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    def modulo_28_estrutura_projetos(self) -> None:
        """Módulo 28: Estrutura de Projetos Python"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 28: ESTRUTURA DE PROJETOS", 
                          "Organização Profissional de Código Python")
            
            while True:
                self._mostrar_menu_estrutura()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._organizacao_pastas()
                elif escolha == "2":
                    self._packages_modules()
                elif escolha == "3":
                    self._setup_pyproject()
                elif escolha == "4":
                    self._documentacao_projetos()
                elif escolha == "5":
                    self._configuracoes_projeto()
                elif escolha == "6":
                    self._templates_projeto()
                elif escolha == "7":
                    self._exercicios_estrutura()
                elif escolha == "8":
                    self._projeto_completo()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_28")
            self.ui.success("🎉 Módulo Estrutura de Projetos concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    def modulo_29_apis_web_requests(self) -> None:
        """Módulo 29: APIs e Web Requests"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("🌐 MÓDULO 29: APIs E WEB REQUESTS", 
                          "Conectando Python com o Mundo Web")
            
            while True:
                self._mostrar_menu_apis()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._teoria_apis()
                elif escolha == "2":
                    self._biblioteca_requests()
                elif escolha == "3":
                    self._metodos_http()
                elif escolha == "4":
                    self._json_handling()
                elif escolha == "5":
                    self._autenticacao_apis()
                elif escolha == "6":
                    self._tratamento_erros_apis()
                elif escolha == "7":
                    self._exercicios_apis()
                elif escolha == "8":
                    self._projeto_consumo_api()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_29")
            self.ui.success("🎉 Módulo APIs e Web Requests concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    def modulo_30_seguranca_basica(self) -> None:
        """Módulo 30: Segurança Básica em Python"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self.ui.clear_screen()
            self.ui.header("🛡️ MÓDULO 30: SEGURANÇA BÁSICA", 
                          "Desenvolvendo com Responsabilidade e Segurança")
            
            while True:
                self._mostrar_menu_seguranca()
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._principios_seguranca()
                elif escolha == "2":
                    self._validacao_input()
                elif escolha == "3":
                    self._prevencao_injection()
                elif escolha == "4":
                    self._gerenciamento_secrets()
                elif escolha == "5":
                    self._criptografia_basica()
                elif escolha == "6":
                    self._logging_seguro()
                elif escolha == "7":
                    self._exercicios_seguranca()
                elif escolha == "8":
                    self._auditoria_codigo()
                else:
                    self.ui.warning("❌ Opção inválida! Tente novamente.")
                    time.sleep(1)
            
            self.progress.complete_module("modulo_30")
            self.ui.success("🎉 Módulo Segurança Básica concluído!")
            
        except Exception as e:
            self.ui.error(f"Erro no módulo: {str(e)}")

    # ============ MÉTODOS DE MENU ============
    
    def _mostrar_menu_terminal(self):
        """Menu do módulo Terminal"""
        self.ui.clear_screen()
        self.ui.header("🐧 TERMINAL E COMMAND LINE", "Interface de Linha de Comando")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Teoria: Por que usar Terminal?")
        print("2. 💻 Comandos Básicos (ls, cd, pwd, etc.)")
        print("3. 📁 Navegação e Exploração de Arquivos")
        print("4. 🔧 Manipulação de Arquivos e Diretórios")
        print("5. 🔀 Pipes e Redirecionamento")
        print("6. 📜 Bash Scripting Básico")
        print("7. 🧪 Exercícios Práticos")
        print("8. 🎮 Simulador de Terminal")
        print("0. 🔙 Voltar ao Menu Principal")

    def _mostrar_menu_venv(self):
        """Menu do módulo Ambientes Virtuais"""
        self.ui.clear_screen()
        self.ui.header("📦 AMBIENTES VIRTUAIS", "Isolamento de Dependências")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Teoria: Por que Ambientes Virtuais?")
        print("2. 🏗️ Criando e Ativando venv")
        print("3. 📦 Gerenciamento com pip")
        print("4. 📋 requirements.txt e Reprodução")
        print("5. ⭐ Boas Práticas de Dependências")
        print("6. 🧪 Exercícios Práticos")
        print("7. 🚀 Projeto: Setup Completo")
        print("0. 🔙 Voltar ao Menu Principal")

    def _mostrar_menu_testes(self):
        """Menu do módulo Testes"""
        self.ui.clear_screen()
        self.ui.header("🧪 TESTES E TDD", "Test-Driven Development")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Teoria: Por que Testar?")
        print("2. 🔬 unittest - Testes Básicos")
        print("3. 🚀 pytest - Framework Moderno")
        print("4. 🎯 TDD na Prática")
        print("5. 🎭 Mocks e Fixtures")
        print("6. 📊 Coverage de Testes")
        print("7. 🧪 Exercícios TDD")
        print("8. 🏗️ Projeto com Testes Completos")
        print("0. 🔙 Voltar ao Menu Principal")

    def _mostrar_menu_estrutura(self):
        """Menu do módulo Estrutura de Projetos"""
        self.ui.clear_screen()
        self.ui.header("🏗️ ESTRUTURA DE PROJETOS", "Organização Profissional")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📁 Organização de Pastas")
        print("2. 📦 Packages e Modules")
        print("3. ⚙️ setup.py e pyproject.toml")
        print("4. 📚 Documentação de Projetos")
        print("5. 🔧 Configurações e Variáveis")
        print("6. 📋 Templates de Projeto")
        print("7. 🧪 Exercícios de Estruturação")
        print("8. 🚀 Projeto Completo Organizado")
        print("0. 🔙 Voltar ao Menu Principal")

    def _mostrar_menu_apis(self):
        """Menu do módulo APIs"""
        self.ui.clear_screen()
        self.ui.header("🌐 APIs E WEB REQUESTS", "Conectividade Web")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Teoria: REST APIs e HTTP")
        print("2. 📡 Biblioteca requests")
        print("3. 🔄 Métodos HTTP (GET, POST, etc.)")
        print("4. 📋 Manipulação de JSON")
        print("5. 🔐 Autenticação em APIs")
        print("6. ⚠️ Tratamento de Erros")
        print("7. 🧪 Exercícios com APIs Reais")
        print("8. 🚀 Projeto: Cliente de API")
        print("0. 🔙 Voltar ao Menu Principal")

    def _mostrar_menu_seguranca(self):
        """Menu do módulo Segurança"""
        self.ui.clear_screen()
        self.ui.header("🛡️ SEGURANÇA BÁSICA", "Desenvolvimento Seguro")
        
        print("📚 CONTEÚDO DO MÓDULO:")
        print("=" * 60)
        print("1. 📖 Princípios de Segurança")
        print("2. ✅ Validação de Input")
        print("3. 🛡️ Prevenção de Injection")
        print("4. 🔐 Gerenciamento de Secrets")
        print("5. 🔒 Criptografia Básica")
        print("6. 📝 Logging Seguro")
        print("7. 🧪 Exercícios de Segurança")
        print("8. 🔍 Auditoria de Código")
        print("0. 🔙 Voltar ao Menu Principal")

    # ============ IMPLEMENTAÇÕES DOS MÉTODOS ============
    
    def _teoria_terminal(self):
        """Teoria sobre terminal"""
        self.ui.clear_screen()
        self.ui.header("📖 TEORIA: POR QUE USAR TERMINAL?", "Fundamentos da CLI")
        
        print("🎯 O TERMINAL É FUNDAMENTAL PORQUE:")
        print("=" * 50)
        print("✅ Mais rápido que interfaces gráficas")
        print("✅ Permite automação com scripts")
        print("✅ Controle total sobre o sistema")
        print("✅ Funciona em servidores remotos")
        print("✅ Padrão em desenvolvimento profissional")
        print("✅ Integração com Git, Docker, etc.")
        
        print("\n🏗️ CONCEITOS BÁSICOS:")
        print("=" * 30)
        print("🖥️ Shell: Interpretador de comandos")
        print("📁 Diretório: Pasta no sistema")
        print("📄 Path: Caminho para arquivo/pasta")
        print("🔗 Comando: Instrução para o sistema")
        print("⚙️ Flag/Opção: Modificador de comando")
        print("📤 Output: Resultado do comando")
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _comandos_basicos(self):
        """Comandos básicos do terminal"""
        self.ui.clear_screen()
        self.ui.header("💻 COMANDOS BÁSICOS", "Toolkit Essencial")
        
        comandos = {
            "🧭 NAVEGAÇÃO": [
                ("pwd", "Mostra diretório atual"),
                ("ls", "Lista arquivos e pastas"),
                ("ls -la", "Lista detalhada (incluindo ocultos)"),
                ("cd pasta", "Entra na pasta"),
                ("cd ..", "Volta um nível"),
                ("cd ~", "Vai para home do usuário"),
                ("cd /", "Vai para raiz do sistema")
            ],
            "📁 ARQUIVOS E PASTAS": [
                ("mkdir pasta", "Cria pasta"),
                ("touch arquivo.txt", "Cria arquivo vazio"),
                ("cp origem destino", "Copia arquivo"),
                ("mv origem destino", "Move/renomeia arquivo"),
                ("rm arquivo", "Remove arquivo"),
                ("rm -rf pasta", "Remove pasta e conteúdo"),
                ("rmdir pasta", "Remove pasta vazia")
            ],
            "👀 VISUALIZAÇÃO": [
                ("cat arquivo.txt", "Mostra conteúdo do arquivo"),
                ("less arquivo.txt", "Mostra arquivo paginado"),
                ("head arquivo.txt", "Mostra primeiras linhas"),
                ("tail arquivo.txt", "Mostra últimas linhas"),
                ("wc arquivo.txt", "Conta linhas, palavras, caracteres"),
                ("file arquivo", "Mostra tipo do arquivo")
            ],
            "🔍 BUSCA": [
                ("find . -name '*.py'", "Busca arquivos Python"),
                ("grep 'texto' arquivo", "Busca texto em arquivo"),
                ("which python", "Mostra caminho do comando"),
                ("locate arquivo", "Busca arquivo no sistema")
            ]
        }
        
        for categoria, cmds in comandos.items():
            print(f"\n{categoria}")
            print("=" * 40)
            for cmd, desc in cmds:
                print(f"  📝 {cmd:<25} | {desc}")
            
            input("\n🔸 Pressione ENTER para próxima categoria...")
            if categoria != list(comandos.keys())[-1]:
                self.ui.clear_screen()
                self.ui.header("💻 COMANDOS BÁSICOS", "Próxima Categoria")

    def _navegacao_arquivos(self):
        """Navegação e exploração"""
        self.ui.clear_screen()
        self.ui.header("📁 NAVEGAÇÃO E EXPLORAÇÃO", "Dominando o Sistema de Arquivos")
        
        print("🗺️ ESTRUTURA DO SISTEMA DE ARQUIVOS:")
        print("=" * 50)
        print("📁 / (raiz)")
        print("├── 📁 home/")
        print("│   └── 📁 usuario/")
        print("│       ├── 📁 Documents/")
        print("│       ├── 📁 Downloads/")
        print("│       └── 📁 Desktop/")
        print("├── 📁 usr/")
        print("│   ├── 📁 bin/ (programas)")
        print("│   └── 📁 local/")
        print("└── 📁 var/ (logs, dados)")
        
        print("\n🧭 NAVEGAÇÃO EFICIENTE:")
        print("=" * 30)
        print("📍 . = diretório atual")
        print("📍 .. = diretório pai")
        print("📍 ~ = home do usuário")
        print("📍 / = raiz do sistema")
        print("📍 - = diretório anterior")
        
        print("\n💡 DICAS DE NAVEGAÇÃO:")
        print("=" * 25)
        print("⚡ Use TAB para autocompletar")
        print("⚡ Ctrl+R para buscar histórico")
        print("⚡ Ctrl+L para limpar tela")
        print("⚡ Setas ↑↓ para histórico")
        print("⚡ Ctrl+C para cancelar comando")
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _manipulacao_arquivos(self):
        """Manipulação de arquivos"""
        self.ui.clear_screen()
        self.ui.header("🔧 MANIPULAÇÃO DE ARQUIVOS", "Criando, Editando, Organizando")
        
        print("🎯 OPERAÇÕES COMUNS:")
        print("=" * 30)
        
        exemplos = [
            ("📝 CRIAR", [
                "mkdir meu_projeto",
                "touch README.md",
                "echo 'Hello World' > hello.txt"
            ]),
            ("📋 COPIAR", [
                "cp arquivo.txt backup.txt",
                "cp -r pasta/ pasta_backup/",
                "cp *.py /dest/"
            ]),
            ("🚚 MOVER/RENOMEAR", [
                "mv arquivo.txt novo_nome.txt",
                "mv arquivo.txt /nova/pasta/",
                "mv *.log logs/"
            ]),
            ("🗑️ REMOVER", [
                "rm arquivo.txt",
                "rm -rf pasta_temporaria/",
                "rm *.tmp"
            ])
        ]
        
        for operacao, cmds in exemplos:
            print(f"\n{operacao}")
            print("-" * 20)
            for cmd in cmds:
                print(f"  $ {cmd}")
            
            input("\n🔸 Pressione ENTER para próxima operação...")
            if operacao != exemplos[-1][0]:
                self.ui.clear_screen()
                self.ui.header("🔧 MANIPULAÇÃO DE ARQUIVOS", "Próxima Operação")

    def _pipes_redirecionamento(self):
        """Pipes e redirecionamento"""
        self.ui.clear_screen()
        self.ui.header("🔀 PIPES E REDIRECIONAMENTO", "Conectando Comandos")
        
        print("🚰 REDIRECIONAMENTO:")
        print("=" * 30)
        print("📤 > arquivo.txt    | Sobrescreve arquivo")
        print("📤 >> arquivo.txt   | Adiciona ao arquivo")
        print("📥 < arquivo.txt    | Usa arquivo como input")
        print("⚠️ 2> erro.log     | Redireciona erros")
        print("🔄 &> tudo.log     | Redireciona tudo")
        
        print("\n🔗 PIPES (|):")
        print("=" * 15)
        print("📊 ls | wc -l              | Conta arquivos")
        print("🔍 cat arquivo.txt | grep 'palavra' | Busca palavra")
        print("📈 ps aux | grep python    | Processos Python")
        print("📋 history | tail -10      | Últimos 10 comandos")
        
        print("\n🎯 EXEMPLOS PRÁTICOS:")
        print("=" * 25)
        
        exemplos = [
            "# Criar lista de arquivos Python",
            "find . -name '*.py' > lista_python.txt",
            "",
            "# Backup de logs com data",
            "cat app.log | grep ERROR > errors_$(date +%Y%m%d).log",
            "",
            "# Contar linhas de código",
            "find . -name '*.py' | xargs wc -l | tail -1",
            "",
            "# Buscar e organizar",
            "grep -r 'TODO' . | sort | uniq > todos.txt"
        ]
        
        for exemplo in exemplos:
            print(exemplo)
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _bash_scripting_basico(self):
        """Bash scripting básico"""
        self.ui.clear_screen()
        self.ui.header("📜 BASH SCRIPTING BÁSICO", "Automação com Scripts")
        
        print("🚀 MEU PRIMEIRO SCRIPT:")
        print("=" * 30)
        
        script_exemplo = '''#!/bin/bash
# backup.sh - Script de backup simples

echo "🔄 Iniciando backup..."
DATA=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backup_$DATA"

mkdir $BACKUP_DIR
cp -r src/ $BACKUP_DIR/
cp *.py $BACKUP_DIR/

echo "✅ Backup criado em: $BACKUP_DIR"
echo "📊 Arquivos copiados: $(find $BACKUP_DIR -type f | wc -l)"'''
        
        print(script_exemplo)
        
        print("\n💡 CONCEITOS IMPORTANTES:")
        print("=" * 30)
        print("📋 #!/bin/bash = shebang (interprete)")
        print("💬 # = comentário")
        print("📦 $VARIAVEL = usar variável")
        print("⚙️ $(comando) = executar comando")
        print("🔧 chmod +x script.sh = tornar executável")
        print("▶️ ./script.sh = executar script")
        
        print("\n🎯 ESTRUTURAS BÁSICAS:")
        print("=" * 25)
        
        estruturas = '''# Condicionais
if [ -f "arquivo.txt" ]; then
    echo "Arquivo existe"
fi

# Loops
for arquivo in *.py; do
    echo "Processando: $arquivo"
done

# Funções
fazer_backup() {
    cp "$1" "backup_$1"
    echo "Backup de $1 criado"
}'''
        
        print(estruturas)
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _exercicios_terminal(self):
        """Exercícios práticos de terminal"""
        self.ui.clear_screen()
        self.ui.header("🧪 EXERCÍCIOS PRÁTICOS", "Praticando no Terminal")
        
        exercicios = [
            {
                "titulo": "🏁 Exercício 1: Exploração Básica",
                "objetivo": "Familiarizar-se com navegação",
                "tarefas": [
                    "1. Descubra em que diretório você está",
                    "2. Liste todos os arquivos (incluindo ocultos)",
                    "3. Navegue até sua pasta home",
                    "4. Crie uma pasta chamada 'python_pratica'",
                    "5. Entre na pasta criada"
                ],
                "comandos": [
                    "pwd",
                    "ls -la",
                    "cd ~",
                    "mkdir python_pratica",
                    "cd python_pratica"
                ]
            },
            {
                "titulo": "📁 Exercício 2: Organização de Arquivos",
                "objetivo": "Praticar manipulação de arquivos",
                "tarefas": [
                    "1. Crie 3 arquivos Python vazios",
                    "2. Crie uma pasta 'src'",
                    "3. Mova os arquivos para a pasta src",
                    "4. Faça backup da pasta src",
                    "5. Liste o conteúdo recursivamente"
                ],
                "comandos": [
                    "touch main.py utils.py config.py",
                    "mkdir src",
                    "mv *.py src/",
                    "cp -r src/ src_backup/",
                    "ls -R"
                ]
            },
            {
                "titulo": "🔍 Exercício 3: Busca e Filtros",
                "objetivo": "Dominar busca e pipes",
                "tarefas": [
                    "1. Encontre todos arquivos .py no sistema",
                    "2. Conte quantos arquivos Python existem",
                    "3. Busque a palavra 'import' em arquivos Python",
                    "4. Crie um relatório dos resultados",
                    "5. Visualize as últimas 5 linhas"
                ],
                "comandos": [
                    "find /usr -name '*.py' 2>/dev/null",
                    "find . -name '*.py' | wc -l",
                    "grep -r 'import' *.py",
                    "find . -name '*.py' | wc -l > relatorio.txt",
                    "tail -5 relatorio.txt"
                ]
            }
        ]
        
        for i, ex in enumerate(exercicios, 1):
            print(f"\n{ex['titulo']}")
            print("=" * 50)
            print(f"🎯 OBJETIVO: {ex['objetivo']}")
            print("\n📋 TAREFAS:")
            for tarefa in ex['tarefas']:
                print(f"  {tarefa}")
            
            print("\n💻 COMANDOS SUGERIDOS:")
            for cmd in ex['comandos']:
                print(f"  $ {cmd}")
            
            if i < len(exercicios):
                input(f"\n🔸 Pressione ENTER para próximo exercício ({i+1}/{len(exercicios)})...")
                self.ui.clear_screen()
                self.ui.header("🧪 EXERCÍCIOS PRÁTICOS", f"Exercício {i+1}/{len(exercicios)}")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _simulador_terminal(self):
        """Simulador de terminal"""
        self.ui.clear_screen()
        self.ui.header("🎮 SIMULADOR DE TERMINAL", "Pratique Comandos Sem Riscos")
        
        print("🎯 INSTRUÇÕES:")
        print("  • Digite comandos como se fosse um terminal real")
        print("  • O simulador mostrará o resultado esperado")
        print("  • Digite 'help' para ver comandos disponíveis")
        print("  • Digite 'exit' para sair do simulador")
        
        # Simulador básico
        current_dir = "/home/usuario"
        files = ["documento.txt", "foto.jpg", "script.py"]
        dirs = ["projetos", "downloads", "documentos"]
        
        while True:
            comando = input(f"\n{current_dir} $ ").strip().lower()
            
            if comando == "exit":
                break
            elif comando == "help":
                print("📋 Comandos disponíveis:")
                print("  ls, pwd, cd, mkdir, touch, cat, help, exit")
            elif comando == "pwd":
                print(current_dir)
            elif comando == "ls":
                print("  ".join(dirs + files))
            elif comando == "ls -la":
                print("drwxr-xr-x  usuario usuario  projetos")
                print("drwxr-xr-x  usuario usuario  downloads") 
                print("drwxr-xr-x  usuario usuario  documentos")
                print("-rw-r--r--  usuario usuario  documento.txt")
                print("-rw-r--r--  usuario usuario  foto.jpg")
                print("-rwxr-xr-x  usuario usuario  script.py")
            elif comando.startswith("cd "):
                dir_name = comando.split()[1]
                if dir_name in dirs or dir_name == "..":
                    print(f"✅ Navegou para {dir_name}")
                else:
                    print(f"❌ Diretório '{dir_name}' não encontrado")
            elif comando.startswith("mkdir "):
                dir_name = comando.split()[1]
                dirs.append(dir_name)
                print(f"✅ Diretório '{dir_name}' criado")
            elif comando.startswith("touch "):
                file_name = comando.split()[1]
                files.append(file_name)
                print(f"✅ Arquivo '{file_name}' criado")
            elif comando.startswith("cat "):
                file_name = comando.split()[1]
                if file_name in files:
                    print(f"📄 Conteúdo de {file_name}:")
                    print("Hello World!")
                else:
                    print(f"❌ Arquivo '{file_name}' não encontrado")
            else:
                print(f"❓ Comando '{comando}' não reconhecido. Digite 'help' para ajuda")

    # ============ MÉTODOS PARA OUTROS MÓDULOS (IMPLEMENTAÇÃO BÁSICA) ============
    
    def _teoria_ambientes_virtuais(self):
        """Teoria sobre ambientes virtuais"""
        self.ui.clear_screen()
        self.ui.header("📖 TEORIA: AMBIENTES VIRTUAIS", "Isolamento é Fundamental")
        
        print("🎯 POR QUE USAR AMBIENTES VIRTUAIS?")
        print("=" * 50)
        print("🔒 Isolamento de dependências entre projetos")
        print("📦 Evita conflitos de versões de bibliotecas")
        print("🧹 Mantém sistema limpo e organizado")
        print("📋 Facilita reprodução do ambiente")
        print("🚀 Deploy mais previsível")
        print("👥 Colaboração em equipe sem problemas")
        
        print("\n💡 EXEMPLO DE PROBLEMA SEM VENV:")
        print("=" * 40)
        print("🚨 Projeto A precisa Django 3.2")
        print("🚨 Projeto B precisa Django 4.1")
        print("🚨 Impossível ter ambas versões globalmente!")
        print("✅ Solução: Um venv para cada projeto")
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _criando_venv(self):
        """Como criar ambientes virtuais"""
        self.ui.clear_screen()
        self.ui.header("🏗️ CRIANDO E ATIVANDO VENV", "Passo a Passo")
        
        print("📋 PASSO A PASSO:")
        print("=" * 25)
        
        passos = [
            ("1️⃣ CRIAR VENV", "python -m venv meu_projeto_env"),
            ("2️⃣ ATIVAR (Linux/Mac)", "source meu_projeto_env/bin/activate"),
            ("2️⃣ ATIVAR (Windows)", "meu_projeto_env\\Scripts\\activate"),
            ("3️⃣ VERIFICAR", "which python && python --version"),
            ("4️⃣ INSTALAR PACOTES", "pip install requests"),
            ("5️⃣ DESATIVAR", "deactivate")
        ]
        
        for passo, comando in passos:
            print(f"\n{passo}:")
            print(f"  $ {comando}")
            
        print("\n🎯 SINAIS DE QUE ESTÁ ATIVO:")
        print("=" * 30)
        print("📍 (nome_env) aparece no prompt")
        print("📍 which python aponta para venv")
        print("📍 pip list mostra apenas pacotes do venv")
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _gerenciamento_pip(self):
        """Gerenciamento com pip"""
        self.ui.clear_screen()
        self.ui.header("📦 GERENCIAMENTO COM PIP", "Instalando e Organizando Pacotes")
        
        comandos_pip = {
            "📥 INSTALAÇÃO": [
                ("pip install requests", "Instala pacote"),
                ("pip install requests==2.28.0", "Versão específica"),
                ("pip install -r requirements.txt", "Instala dependências"),
                ("pip install -e .", "Instala projeto em modo desenvolvimento")
            ],
            "📋 INFORMAÇÕES": [
                ("pip list", "Lista pacotes instalados"),
                ("pip show requests", "Detalhes do pacote"),
                ("pip freeze", "Lista com versões exatas"),
                ("pip check", "Verifica dependências")
            ],
            "🔄 ATUALIZAÇÃO": [
                ("pip install --upgrade pip", "Atualiza o próprio pip"),
                ("pip install --upgrade requests", "Atualiza pacote"),
                ("pip list --outdated", "Mostra pacotes desatualizados")
            ],
            "🗑️ REMOÇÃO": [
                ("pip uninstall requests", "Remove pacote"),
                ("pip uninstall -r requirements.txt", "Remove lista de pacotes")
            ]
        }
        
        for categoria, cmds in comandos_pip.items():
            print(f"\n{categoria}")
            print("=" * 30)
            for cmd, desc in cmds:
                print(f"  📝 {cmd:<35} | {desc}")
            
            input("\n🔸 Pressione ENTER para próxima categoria...")
            if categoria != list(comandos_pip.keys())[-1]:
                self.ui.clear_screen()
                self.ui.header("📦 GERENCIAMENTO COM PIP", "Próxima Categoria")

    def _requirements_txt(self):
        """Requirements.txt e reprodução"""
        self.ui.clear_screen()
        self.ui.header("📋 REQUIREMENTS.TXT", "Reproduzindo Ambientes")
        
        print("🎯 O QUE É REQUIREMENTS.TXT?")
        print("=" * 40)
        print("📋 Lista de todas as dependências do projeto")
        print("🔒 Garante que todos usem as mesmas versões")
        print("🚀 Facilita deploy e configuração")
        print("👥 Essencial para trabalho em equipe")
        
        print("\n📝 EXEMPLO DE REQUIREMENTS.TXT:")
        print("=" * 40)
        exemplo_req = """requests==2.28.1
flask==2.2.2
pandas>=1.4.0,<2.0.0
pytest==7.1.2
black==22.6.0
# Dependências de desenvolvimento
pytest-cov==3.0.0"""
        print(exemplo_req)
        
        print("\n⚙️ COMANDOS IMPORTANTES:")
        print("=" * 30)
        comandos = [
            ("pip freeze > requirements.txt", "Gera requirements.txt"),
            ("pip install -r requirements.txt", "Instala dependências"),
            ("pip-tools compile requirements.in", "Gera versões exatas"),
            ("pip-tools sync", "Sincroniza ambiente")
        ]
        
        for cmd, desc in comandos:
            print(f"  📝 {cmd:<35} | {desc}")
        
        input("\n🔸 Pressione ENTER para continuar...")

    def _boas_praticas_dependencias(self):
        """Boas práticas de dependências"""
        self.ui.clear_screen()
        self.ui.header("⭐ BOAS PRÁTICAS", "Gerenciamento Profissional")
        
        praticas = {
            "📁 ORGANIZAÇÃO": [
                "✅ Um venv por projeto",
                "✅ Nome descritivo para venv",
                "✅ .gitignore inclui venv/",
                "✅ requirements.txt na raiz do projeto"
            ],
            "🔒 VERSIONAMENTO": [
                "✅ Use versões exatas para produção",
                "✅ Ranges flexíveis para desenvolvimento", 
                "✅ Pin versões críticas",
                "✅ Teste upgrades regularmente"
            ],
            "🚀 DEPLOY": [
                "✅ requirements.txt separado para produção",
                "✅ requirements-dev.txt para desenvolvimento",
                "✅ Use pip-tools para manage dependencies",
                "✅ Docker para ambientes complexos"
            ],
            "🔧 FERRAMENTAS": [
                "✅ pip-tools para dependency management",
                "✅ pipenv como alternativa moderna",
                "✅ conda para ciência de dados",
                "✅ poetry para projetos complexos"
            ]
        }
        
        for categoria, items in praticas.items():
            print(f"\n{categoria}")
            print("=" * 25)
            for item in items:
                print(f"  {item}")
            
            input("\n🔸 Pressione ENTER para próxima categoria...")
            if categoria != list(praticas.keys())[-1]:
                self.ui.clear_screen()
                self.ui.header("⭐ BOAS PRÁTICAS", "Próxima Categoria")

    # Implementações básicas para outros módulos...
    def _exercicios_venv(self): 
        print("🧪 Exercícios de venv em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _projeto_pratico_venv(self): 
        print("🚀 Projeto prático em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _teoria_testes(self): 
        print("📖 Teoria de testes em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _unittest_basico(self): 
        print("🔬 unittest básico em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _pytest_introducao(self): 
        print("🚀 pytest em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _tdd_na_pratica(self): 
        print("🎯 TDD prático em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _mocks_fixtures(self): 
        print("🎭 Mocks e fixtures em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _coverage_testes(self): 
        print("📊 Coverage em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _exercicios_tdd(self): 
        print("🧪 Exercícios TDD em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _projeto_com_testes(self): 
        print("🏗️ Projeto com testes em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    # Continuando com implementações básicas...
    def _organizacao_pastas(self): 
        print("📁 Organização de pastas em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _packages_modules(self): 
        print("📦 Packages e modules em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _setup_pyproject(self): 
        print("⚙️ setup.py/pyproject.toml em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _documentacao_projetos(self): 
        print("📚 Documentação em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _configuracoes_projeto(self): 
        print("🔧 Configurações em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _templates_projeto(self): 
        print("📋 Templates em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _exercicios_estrutura(self): 
        print("🧪 Exercícios estrutura em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _projeto_completo(self): 
        print("🚀 Projeto completo em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    # APIs
    def _teoria_apis(self): 
        print("📖 Teoria APIs em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _biblioteca_requests(self): 
        print("📡 Biblioteca requests em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _metodos_http(self): 
        print("🔄 Métodos HTTP em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _json_handling(self): 
        print("📋 JSON handling em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _autenticacao_apis(self): 
        print("🔐 Autenticação em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _tratamento_erros_apis(self): 
        print("⚠️ Tratamento de erros em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _exercicios_apis(self): 
        print("🧪 Exercícios APIs em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _projeto_consumo_api(self): 
        print("🚀 Projeto API em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    # Segurança
    def _principios_seguranca(self): 
        print("📖 Princípios segurança em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _validacao_input(self): 
        print("✅ Validação de input em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _prevencao_injection(self): 
        print("🛡️ Prevenção injection em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _gerenciamento_secrets(self): 
        print("🔐 Gerenciamento secrets em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _criptografia_basica(self): 
        print("🔒 Criptografia em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _logging_seguro(self): 
        print("📝 Logging seguro em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _exercicios_seguranca(self): 
        print("🧪 Exercícios segurança em desenvolvimento...")
        input("Pressione ENTER para continuar...")
    
    def _auditoria_codigo(self): 
        print("🔍 Auditoria de código em desenvolvimento...")
        input("Pressione ENTER para continuar...")