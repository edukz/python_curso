#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 1: Introdução ao Python
Primeiro módulo do curso - Apresenta a linguagem Python
"""

from ..shared.base_module import BaseModule


class Modulo01Introducao(BaseModule):
    """Módulo 1: Introdução ao Python"""
    
    def __init__(self):
        super().__init__("modulo_1", "Introdução ao Python")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo de introdução ao Python"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._introducao_python()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _introducao_python(self) -> None:
        """Conteúdo principal do módulo de introdução"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐍 MÓDULO 1: INTRODUÇÃO AO PYTHON")
        else:
            print("\n" + "="*50)
            print("🐍 MÓDULO 1: INTRODUÇÃO AO PYTHON")
            print("="*50)
        
        print("🐍 Bem-vindo ao fascinante mundo da programação Python! 🎉")
        print("\n═══════════════════════════════════════════════")
        print("            O QUE É PYTHON?")
        print("═══════════════════════════════════════════════")
        
        print("\nPython é uma linguagem de programação criada por Guido van Rossum")
        print("em 1991. O nome vem do grupo de comédia britânico 'Monty Python'!")
        
        print("\n🌟 Por que Python é especial?")
        print("• 📚 FÁCIL DE APRENDER - Sintaxe simples e intuitiva")
        print("• 🚀 PODEROSA E VERSÁTIL - Resolve problemas complexos")
        print("• 🌍 MUITO POPULAR - Uma das linguagens mais usadas no mundo")
        print("• 🤝 COMUNIDADE ATIVA - Milhões de programadores ajudam uns aos outros")
        
        self.pausar()
        
        print("\n🔧 Onde Python é usado no mundo real?")
        print("• 🤖 INTELIGÊNCIA ARTIFICIAL - Netflix, Tesla, Google")
        print("• 🌐 DESENVOLVIMENTO WEB - Instagram, Spotify, Pinterest")
        print("• 📊 ANÁLISE DE DADOS - NASA, Banco Central, universidades")
        print("• 🎮 JOGOS - Civilization IV, EVE Online")
        print("• 🏢 AUTOMAÇÃO - Dropbox, Reddit, BitTorrent")
        print("• 🧬 CIÊNCIA - Descobertas médicas, pesquisa espacial")
        
        self.pausar()
        
        print("\n🔹 O que é PROGRAMAÇÃO?")
        print("Programar é como dar instruções para um computador, mas de forma")
        print("muito específica e organizada. É como escrever uma receita de bolo:")
        print("")
        print("📝 RECEITA DE BOLO:")
        print("1. Pegue 3 ovos")
        print("2. Misture com farinha")
        print("3. Asse por 30 minutos")
        print("")
        print("💻 PROGRAMA EM PYTHON:")
        print("1. Peça o nome do usuário")
        print("2. Calcule a idade")
        print("3. Mostre uma mensagem personalizada")
        
        self.pausar()
        
        print("\n🧠 Como o computador 'entende' Python?")
        print("O computador só entende 0s e 1s (código binário).")
        print("Python é traduzido para essa linguagem por um 'interpretador'.")
        print("")
        print("VOCÊ ESCREVE: print('Olá!')")
        print("PYTHON TRADUZ: 01001000 01100101 01101100...")
        print("COMPUTADOR EXECUTA: Olá!")
        
        self.pausar()
        
        print("\n🎯 O que você vai aprender neste curso?")
        print("1. 📝 Como 'falar' com o computador")
        print("2. 🗃️  Como guardar e organizar informações")
        print("3. 🤔 Como fazer o programa tomar decisões")
        print("4. 🔄 Como repetir tarefas automaticamente")
        print("5. 📋 Como trabalhar com listas de dados")
        print("6. ⚙️  Como criar suas próprias 'ferramentas'")
        print("7. 🧮 Como construir uma calculadora completa!")
        
        self.pausar()
        
        print("\n💡 CURIOSIDADES SOBRE PYTHON:")
        print("• Python executa aproximadamente 100.000 linhas por segundo!")
        print("• O Instagram processa 95 milhões de fotos por dia usando Python")
        print("• Python ajudou a descobrir ondas gravitacionais no espaço")
        print("• Netflix usa Python para recomendar filmes para você")
        print("• Python pode controlar robôs, drones e até mesmo carros!")
        
        # Exercício interativo
        correto = self.exercicio(
            "Em que ano Python foi criado?",
            ["1991", "mil novecentos e noventa e um"],
            "Foi criado no início dos anos 90"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_cartao_apresentacao()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_cartao_apresentacao(self) -> None:
        """Mini Projeto - Módulo 1: Cartão de Apresentação Python"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CARTÃO DE APRESENTAÇÃO PYTHON")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CARTÃO DE APRESENTAÇÃO PYTHON")
            print("="*50)
        
        print("🎉 Vamos criar seu primeiro projeto prático!")
        print("Você vai fazer um programa que cria um cartão de apresentação.")
        print("Este tipo de programa é útil para:")
        print("• Páginas pessoais")
        print("• Assinaturas de email")
        print("• Perfis profissionais")
        print("• Cartões de visita digitais")
        
        self.pausar()
        
        print("\n📝 PASSO 1: Vamos coletar suas informações")
        print("Digite suas informações (pode ser real ou fictício):")
        
        try:
            nome = input("👤 Seu nome: ").strip()
            if not nome:
                nome = "Estudante Python"
            
            profissao = input("💼 Sua profissão/área de interesse: ").strip()
            if not profissao:
                profissao = "Futuro Programador Python"
            
            hobby = input("🎮 Um hobby ou interesse: ").strip()
            if not hobby:
                hobby = "Aprender programação"
                
            print(f"\n✅ Informações coletadas para {nome}!")
            
        except KeyboardInterrupt:
            print("\n⚠️ Projeto cancelado pelo usuário")
            return
            
        self.pausar()
        
        print("\n💻 PASSO 2: Agora vamos PROGRAMAR o cartão!")
        print("Aqui está o código que você criou:")
        
        codigo_gerado = f'''# 🐍 MEU PRIMEIRO PROJETO PYTHON
# Cartão de Apresentação Digital

print("=" * 50)
print("     🎯 CARTÃO DE APRESENTAÇÃO DIGITAL")
print("=" * 50)
print()
print("👤 Nome: {nome}")
print("💼 Profissão: {profissao}")
print("🎮 Hobby: {hobby}")
print("🐍 Status: Aprendendo Python!")
print()
print("=" * 50)
print("🚀 Feito com Python - A linguagem do futuro!")
print("=" * 50)'''
        
        self.exemplo(codigo_gerado)
        self.pausar()
        
        print("\n🎬 RESULTADO FINAL:")
        self.executar_codigo(codigo_gerado)
        
        print("\n🎉 PARABÉNS! Você criou seu primeiro projeto!")
        print("\n💡 APLICAÇÕES NA VIDA REAL:")
        print("• Sites pessoais usam códigos similares")
        print("• Apps de rede social fazem perfis assim")
        print("• Sistemas de RH organizam dados de funcionários")
        print("• Jogos criam fichas de personagens")
        
        print("\n🏆 CONQUISTA DESBLOQUEADA: Primeiro Projeto!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Cartão de Apresentação Python")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo01Introducao()
    print("Teste do módulo 1 - versão standalone")
    module._introducao_python()