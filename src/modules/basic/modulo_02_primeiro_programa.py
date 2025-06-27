#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 2: Seu Primeiro Programa
Aprenda a escrever seu primeiro programa em Python com a função print()
"""

from ..shared.base_module import BaseModule


class Modulo02PrimeiroPrograma(BaseModule):
    """Módulo 2: Seu Primeiro Programa em Python"""
    
    def __init__(self):
        super().__init__("modulo_2", "Seu Primeiro Programa")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo do primeiro programa"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._primeiro_programa()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _primeiro_programa(self) -> None:
        """Conteúdo principal sobre o primeiro programa"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎉 MÓDULO 2: SEU PRIMEIRO PROGRAMA")
        else:
            print("\n" + "="*50)
            print("🎉 MÓDULO 2: SEU PRIMEIRO PROGRAMA")
            print("="*50)
        
        self.print_success("🎉 Chegou a hora de escrever seu PRIMEIRO programa em Python!")
        self.print_section("O TRADICIONAL 'OLÁ, MUNDO!'")
        
        self.print_concept("\n🌍 Por que todo programador começa com 'Olá, Mundo!'?")
        self.print_colored("Esta é uma tradição que começou em 1978 com o livro", "cyan")
        self.print_colored("'The C Programming Language'. É o primeiro programa", "cyan")
        self.print_colored("que todo programador escreve em uma nova linguagem!", "cyan")
        
        self.print_section("\n💻 Vamos ao nosso primeiro código:")
        
        codigo = 'print("Olá, Mundo!")'
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_success("\n🎯 PARABÉNS! Você acabou de executar seu primeiro programa!")
        
        self.print_section("\n🔍 Vamos DISSECAR este código:")
        self.print_colored("• 'print' - É o NOME da função", "yellow")
        self.print_colored("• '('  - Abre os parênteses (início dos parâmetros)", "yellow")
        self.print_colored("• '\"'  - Abre as aspas (início do texto)", "yellow")
        self.print_colored("• 'Olá, Mundo!' - O TEXTO que queremos exibir", "yellow")
        self.print_colored("• '\"'  - Fecha as aspas (fim do texto)", "yellow")
        self.print_colored("• ')'  - Fecha os parênteses (fim dos parâmetros)", "yellow")
        
        self.print_concept("\n📚 O que é a função print()?")
        self.print_colored("• É uma FUNÇÃO BUILT-IN (já vem com Python)", "green")
        self.print_colored("• Sua única missão: EXIBIR coisas na tela", "green")
        self.print_colored("• Você pode imprimir textos, números, resultados...", "green")
        self.print_colored("• É uma das funções mais usadas em Python!", "green")
        
        self.print_section("\n✏️ Vamos experimentar variações:")
        
        # Exemplo 2
        codigo2 = "print('Olá, Mundo!')"
        self.print_colored("\n🔸 Com aspas simples:", "blue")
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        # Exemplo 3
        codigo3 = '''print("Python é incrível!")
print("Estou aprendendo a programar!")'''
        self.print_colored("\n🔸 Múltiplas linhas:", "blue")
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exemplo 4
        codigo4 = 'print("🐍 Python 🐍")'
        self.print_colored("\n🔸 Com emojis:", "blue")
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        self.print_concept("\n❓ ASPAS SIMPLES vs ASPAS DUPLAS")
        self.print_colored("Em Python, tanto faz usar ' ou \" para textos.", "cyan")
        self.print_tip("A regra é: seja CONSISTENTE!")
        print("")
        self.print_success("✅ CORRETO:")
        self.print_colored('   print("Olá!")', "green")
        self.print_colored("   print('Oi!')", "green")
        print("")
        self.print_warning("❌ ERRO COMUM:")
        self.print_colored("   print('Olá\")", "red")  # Misturou aspas!
        
        self.print_warning("\n🚨 ERROS COMUNS que iniciantes cometem:")
        self.print_colored("1. print(Olá)      ❌ - Esqueceu as aspas", "red")
        self.print_colored("2. Print('Olá')    ❌ - 'P' maiúsculo", "red")
        self.print_colored("3. print 'Olá'     ❌ - Esqueceu os parênteses", "red")
        self.print_colored("4. print('Olá'     ❌ - Esqueceu de fechar", "red")
        self.print_colored("5. print(\"Olá')    ❌ - Misturou tipos de aspas", "red")
        
        self.print_tip("\n🔧 DICA PROFISSIONAL:")
        self.print_colored("Use o print() para 'debugar' seus programas!", "yellow")
        self.print_colored("Quando algo não funciona, adicione prints para", "yellow")
        self.print_colored("ver o que está acontecendo. É como acender uma", "yellow")
        self.print_colored("lanterna no código!", "yellow")
        
        # Exercícios práticos
        self.exercicio(
            "Qual comando usamos para exibir texto na tela?",
            ["print", "print()", "função print"],
            "É uma função que começa com 'p'"
        )
        
        self.exercicio(
            "O que está ERRADO neste código: Print('Oi')",
            ["P maiúsculo", "maiúsculo", "print deve ser minúsculo"],
            "Python diferencia maiúsculas de minúsculas"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_mensagens_motivacionais()
        
        # Marcar módulo como completo
        self.complete_module()
        
        self.exercicio(
            "Complete o código: _____(\"Olá!\")",
            ["print"],
            "Função para exibir na tela"
        )
    
    def _mini_projeto_mensagens_motivacionais(self) -> None:
        """Mini Projeto - Módulo 2: Gerador de Mensagens Motivacionais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: GERADOR DE MENSAGENS MOTIVACIONAIS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: GERADOR DE MENSAGENS MOTIVACIONAIS")
            print("="*50)
        
        self.print_success("🌟 Vamos criar um programa que gera mensagens motivacionais!")
        self.print_colored("Tipo de programa usado em:", "cyan")
        self.print_colored("• Apps de bem-estar mental", "green")
        self.print_colored("• Sistemas de coaching", "green")
        self.print_colored("• Jogos com sistema de conquistas", "green")
        self.print_colored("• Chatbots motivacionais", "green")
        
        self.print_concept("\n📱 CONTEXTO REAL:")
        self.print_colored("Apps como Headspace, Calm e Duolingo usam", "yellow")
        self.print_colored("sistemas similares para motivar usuários!", "yellow")
        
        self.print_section("\n💻 Vamos construir o programa passo a passo:")
        
        # Passo 1 - Mensagem básica
        self.print_colored("\n🔸 PASSO 1: Mensagem de bom dia", "blue")
        codigo1 = '''print("🌅 Bom dia!")
print("Hoje é um novo dia cheio de possibilidades!")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        # Passo 2 - Adicionar personalização
        self.print_colored("\n🔸 PASSO 2: Vamos personalizar com emojis", "blue")
        codigo2 = '''print("=" * 40)
print("     🌟 MENSAGEM DO DIA 🌟")
print("=" * 40)
print()
print("🌅 Bom dia, campeão!")
print("💪 Você é capaz de grandes coisas!")
print("🚀 Cada linha de código te torna mais forte!")
print("🎯 Hoje você vai arrasar!")
print()
print("=" * 40)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        # Passo 3 - Sistema completo
        self.print_colored("\n🔸 PASSO 3: Sistema completo como apps reais", "blue")
        codigo3 = '''# 🌟 GERADOR DE MOTIVAÇÃO DIÁRIA
print("🎊" * 20)
print("        MOTIVAÇÃO PYTHON")  
print("🎊" * 20)
print()
print("📱 Carregando sua dose diária de motivação...")
print()
print("✨ Mensagem especial para você:")
print("👑 Você escolheu aprender Python!")
print("🧠 Isso mostra que você é inteligente!")
print("🔥 Cada exercício te deixa mais expert!")
print("🏆 Você já está no caminho do sucesso!")
print()
print("💡 DICA PROFISSIONAL:")
print("Programadores ganham em média R$ 5.000-15.000")
print("Python é a linguagem mais procurada!")
print()
print("🎯 Continue assim e você chegará lá!")
print("🎊" * 20)'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_success("\n🎉 PROJETO CONCLUÍDO!")
        self.print_concept("\n🌍 COMO ISSO É USADO NO MUNDO REAL:")
        self.print_colored("• 📱 WhatsApp: Mensagens de status", "green")
        self.print_colored("• 🎮 Games: Sistemas de conquistas", "green")
        self.print_colored("• 📚 Duolingo: Motivação para estudar", "green")
        self.print_colored("• 💼 LinkedIn: Posts motivacionais", "green")
        self.print_colored("• 🏃 Apps fitness: Encorajamento diário", "green")
        
        self.print_section("\n🚀 PRÓXIMO NÍVEL:")
        self.print_colored("Com o que você vai aprender, poderá criar:", "cyan")
        self.print_colored("• Apps que lembram de beber água", "yellow")
        self.print_colored("• Sistemas de metas pessoais", "yellow")
        self.print_colored("• Chatbots para empresas", "yellow")
        self.print_colored("• Jogos educativos", "yellow")
        
        self.print_success("\n🏆 CONQUISTA: Criador de Experiências!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Gerador de Mensagens Motivacionais")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo02PrimeiroPrograma()
    print("Teste do módulo 2 - versão standalone")
    module._primeiro_programa()