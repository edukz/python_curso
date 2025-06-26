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
        
        print("🎉 Chegou a hora de escrever seu PRIMEIRO programa em Python!")
        print("\n═══════════════════════════════════════════════")
        print("        O TRADICIONAL 'OLÁ, MUNDO!'")
        print("═══════════════════════════════════════════════")
        
        print("\n🌍 Por que todo programador começa com 'Olá, Mundo!'?")
        print("Esta é uma tradição que começou em 1978 com o livro")
        print("'The C Programming Language'. É o primeiro programa")
        print("que todo programador escreve em uma nova linguagem!")
        
        self.pausar()
        
        print("\n💻 Vamos ao nosso primeiro código:")
        
        codigo = 'print("Olá, Mundo!")'
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        print("\n🎯 PARABÉNS! Você acabou de executar seu primeiro programa!")
        
        self.pausar()
        
        print("\n🔍 Vamos DISSECAR este código:")
        print("• 'print' - É o NOME da função")
        print("• '('  - Abre os parênteses (início dos parâmetros)")
        print("• '\"'  - Abre as aspas (início do texto)")
        print("• 'Olá, Mundo!' - O TEXTO que queremos exibir")
        print("• '\"'  - Fecha as aspas (fim do texto)")
        print("• ')'  - Fecha os parênteses (fim dos parâmetros)")
        
        self.pausar()
        
        print("\n📚 O que é a função print()?")
        print("• É uma FUNÇÃO BUILT-IN (já vem com Python)")
        print("• Sua única missão: EXIBIR coisas na tela")
        print("• Você pode imprimir textos, números, resultados...")
        print("• É uma das funções mais usadas em Python!")
        
        self.pausar()
        
        print("\n✏️ Vamos experimentar variações:")
        
        # Exemplo 2
        codigo2 = "print('Olá, Mundo!')"
        print("\n🔸 Com aspas simples:")
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        # Exemplo 3
        codigo3 = '''print("Python é incrível!")
print("Estou aprendendo a programar!")'''
        print("\n🔸 Múltiplas linhas:")
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exemplo 4
        codigo4 = 'print("🐍 Python 🐍")'
        print("\n🔸 Com emojis:")
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        self.pausar()
        
        print("\n❓ ASPAS SIMPLES vs ASPAS DUPLAS")
        print("Em Python, tanto faz usar ' ou \" para textos.")
        print("A regra é: seja CONSISTENTE!")
        print("")
        print("✅ CORRETO:")
        print('   print("Olá!")')
        print("   print('Oi!')")
        print("")
        print("❌ ERRO COMUM:")
        print("   print('Olá\")")  # Misturou aspas!
        
        self.pausar()
        
        print("\n🚨 ERROS COMUNS que iniciantes cometem:")
        print("1. print(Olá)      ❌ - Esqueceu as aspas")
        print("2. Print('Olá')    ❌ - 'P' maiúsculo")
        print("3. print 'Olá'     ❌ - Esqueceu os parênteses")
        print("4. print('Olá'     ❌ - Esqueceu de fechar")
        print("5. print(\"Olá')    ❌ - Misturou tipos de aspas")
        
        self.pausar()
        
        print("\n🔧 DICA PROFISSIONAL:")
        print("Use o print() para 'debugar' seus programas!")
        print("Quando algo não funciona, adicione prints para")
        print("ver o que está acontecendo. É como acender uma")
        print("lanterna no código!")
        
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
        
        print("🌟 Vamos criar um programa que gera mensagens motivacionais!")
        print("Tipo de programa usado em:")
        print("• Apps de bem-estar mental")
        print("• Sistemas de coaching")
        print("• Jogos com sistema de conquistas")
        print("• Chatbots motivacionais")
        
        self.pausar()
        
        print("\n📱 CONTEXTO REAL:")
        print("Apps como Headspace, Calm e Duolingo usam")
        print("sistemas similares para motivar usuários!")
        
        self.pausar()
        
        print("\n💻 Vamos construir o programa passo a passo:")
        
        # Passo 1 - Mensagem básica
        print("\n🔸 PASSO 1: Mensagem de bom dia")
        codigo1 = '''print("🌅 Bom dia!")
print("Hoje é um novo dia cheio de possibilidades!")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        self.pausar()
        
        # Passo 2 - Adicionar personalização
        print("\n🔸 PASSO 2: Vamos personalizar com emojis")
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
        self.pausar()
        
        # Passo 3 - Sistema completo
        print("\n🔸 PASSO 3: Sistema completo como apps reais")
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
        
        print("\n🎉 PROJETO CONCLUÍDO!")
        print("\n🌍 COMO ISSO É USADO NO MUNDO REAL:")
        print("• 📱 WhatsApp: Mensagens de status")
        print("• 🎮 Games: Sistemas de conquistas")
        print("• 📚 Duolingo: Motivação para estudar")
        print("• 💼 LinkedIn: Posts motivacionais")
        print("• 🏃 Apps fitness: Encorajamento diário")
        
        print("\n🚀 PRÓXIMO NÍVEL:")
        print("Com o que você vai aprender, poderá criar:")
        print("• Apps que lembram de beber água")
        print("• Sistemas de metas pessoais")
        print("• Chatbots para empresas")
        print("• Jogos educativos")
        
        print("\n🏆 CONQUISTA: Criador de Experiências!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Gerador de Mensagens Motivacionais")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo02PrimeiroPrograma()
    print("Teste do módulo 2 - versão standalone")
    module._primeiro_programa()