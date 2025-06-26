#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 28: Estrutura de Projetos - Versão Simplificada
Aprenda a organizar projetos Python profissionalmente
"""

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
            self._estrutura_projetos_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _estrutura_projetos_module(self) -> None:
        """Conteúdo principal sobre estrutura de projetos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 28: ESTRUTURA DE PROJETOS PYTHON")
        else:
            print("\n" + "="*60)
            print("🏗️ MÓDULO 28: ESTRUTURA DE PROJETOS PYTHON")
            print("="*60)
        
        print("📁 Aprenda a organizar projetos Python como um profissional!")
        print("🎯 Tópicos abordados:")
        print("• Estrutura básica de projetos")
        print("• Gerenciamento de dependências")
        print("• Arquivos de configuração")
        print("• Documentação e README")
        print("• Templates de projeto")
        print("• Boas práticas de organização")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._estrutura_basica()
        self._gerenciamento_dependencias()
        self._documentacao()
        self._mini_projeto_gerador()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _estrutura_basica(self):
        """Estrutura básica de projetos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📁 ESTRUTURA BÁSICA DE PROJETOS")
        
        print("🏗️ Estrutura recomendada para projetos Python:")
        
        exemplo_estrutura = """
meu_projeto/
│
├── README.md                 # Documentação principal
├── LICENSE                   # Licença do projeto
├── .gitignore               # Arquivos a ignorar no Git
├── requirements.txt         # Dependências
├── setup.py                 # Configuração de instalação
├── pyproject.toml          # Configuração moderna
│
├── src/                     # Código fonte
│   └── meu_projeto/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
│
├── tests/                   # Testes
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── docs/                    # Documentação
│   ├── index.md
│   └── api.md
│
└── scripts/                 # Scripts auxiliares
    ├── deploy.sh
    └── setup_dev.py
"""
        
        print(exemplo_estrutura)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _gerenciamento_dependencias(self):
        """Gerenciamento de dependências"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📦 GERENCIAMENTO DE DEPENDÊNCIAS")
        
        print("🔧 Como gerenciar dependências adequadamente:")
        
        print("\n1️⃣ requirements.txt:")
        print("• Lista todas as dependências")
        print("• Especifica versões")
        print("• Facilita reprodução do ambiente")
        
        print("\n2️⃣ setup.py:")
        print("• Define metadados do projeto")
        print("• Especifica dependências de instalação")
        print("• Permite distribuição via pip")
        
        print("\n3️⃣ Ambientes virtuais:")
        print("• Isolam dependências do projeto")
        print("• Evitam conflitos entre projetos")
        print("• Comandos: python -m venv venv")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _documentacao(self):
        """Documentação e README"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📚 DOCUMENTAÇÃO E README")
        
        print("📝 Como criar documentação eficaz:")
        
        print("\n🎯 README.md essencial:")
        print("• Título e descrição do projeto")
        print("• Instruções de instalação")
        print("• Como usar/executar")
        print("• Exemplos práticos")
        print("• Licença e contribuições")
        
        print("\n📖 Documentação adicional:")
        print("• docs/ - Documentação detalhada")
        print("• Changelog - Histórico de mudanças")
        print("• Contributing.md - Guia de contribuição")
        print("• API docs - Documentação da API")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_gerador(self):
        """Mini projeto: Gerador de estruturas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: GERADOR DE ESTRUTURAS")
        
        print("📊 Vamos criar um gerador de estruturas de projeto!")
        print("🎯 Funcionalidades:")
        print("• Criar estrutura básica automaticamente")
        print("• Gerar arquivos de configuração")
        print("• Templates personalizáveis")
        print("• README automático")
        
        input("\n🔸 Pressione ENTER para começar...")
        
        codigo_gerador = '''
def criar_projeto(nome):
    """Cria estrutura básica de projeto Python"""
    import os
    
    # Criar diretório principal
    os.makedirs(nome, exist_ok=True)
    
    # Estrutura de diretórios
    diretorios = [
        f"{nome}/src/{nome}",
        f"{nome}/tests",
        f"{nome}/docs",
        f"{nome}/scripts"
    ]
    
    for dir_path in diretorios:
        os.makedirs(dir_path, exist_ok=True)
    
    # Arquivos básicos
    arquivos = {
        f"{nome}/README.md": f"# {nome.title()}\\n\\nDescrição do projeto",
        f"{nome}/.gitignore": "__pycache__/\\n*.pyc\\n.env\\n",
        f"{nome}/requirements.txt": "# Dependências\\n",
        f"{nome}/src/{nome}/__init__.py": "",
        f"{nome}/src/{nome}/main.py": "def main():\\n    print('Hello World!')\\n",
        f"{nome}/tests/__init__.py": "",
        f"{nome}/tests/test_main.py": "def test_main():\\n    assert True\\n"
    }
    
    for arquivo, conteudo in arquivos.items():
        with open(arquivo, 'w') as f:
            f.write(conteudo)
    
    print(f"✅ Projeto '{nome}' criado com sucesso!")
    return nome

# Demonstração
projeto = criar_projeto("meu_projeto_exemplo")
print(f"📁 Estrutura criada em: {projeto}/")
'''
        
        print("💻 Código do gerador:")
        print(codigo_gerador)
        
        print("\n🏆 PARABÉNS! Você criou um gerador de projetos!")
        print("🎯 Aplicação real: automatizar criação de novos projetos")
        
        # Registra conclusão do mini projeto
        if hasattr(self, 'complete_mini_project'):
            self.complete_mini_project("Gerador de Estruturas de Projeto")
        
        input("\n🔸 Pressione ENTER para finalizar...")


# Para teste standalone
if __name__ == "__main__":
    module = Modulo28EstruturaProjetos()
    print("Teste do módulo 28 - versão standalone")
    module._estrutura_projetos_module()