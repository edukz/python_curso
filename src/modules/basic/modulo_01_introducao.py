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
        
        self.print_success("🐍 Bem-vindo ao fascinante mundo da programação Python! 🎉")
        
        self.print_section("O QUE É PYTHON?", "🐍")
        
        self.print_concept(
            "Python",
            "Uma linguagem de programação criada por Guido van Rossum em 1991.\n" +
            "O nome vem do grupo de comédia britânico 'Monty Python'!"
        )
        
        self.print_section("Por que Python é especial?", "🌟", "warning")
        
        características = [
            ("📚 FÁCIL DE APRENDER", "Sintaxe simples e intuitiva"),
            ("🚀 PODEROSA E VERSÁTIL", "Resolve problemas complexos"),
            ("🌍 MUITO POPULAR", "Uma das linguagens mais usadas no mundo"),
            ("🤝 COMUNIDADE ATIVA", "Milhões de programadores ajudam uns aos outros")
        ]
        
        for titulo, desc in características:
            self.print_colored(f"• {titulo}", "accent")
            self.print_colored(f"  {desc}", "text")
        
        self.print_section("Onde Python é usado no mundo real?", "🔧", "info")
        
        aplicacoes = [
            ("🤖 INTELIGÊNCIA ARTIFICIAL", "Netflix, Tesla, Google", "warning"),
            ("🌐 DESENVOLVIMENTO WEB", "Instagram, Spotify, Pinterest", "success"),
            ("📊 ANÁLISE DE DADOS", "NASA, Banco Central, universidades", "info"),
            ("🎮 JOGOS", "Civilization IV, EVE Online", "accent"),
            ("🏢 AUTOMAÇÃO", "Dropbox, Reddit, BitTorrent", "primary"),
            ("🧬 CIÊNCIA", "Descobertas médicas, pesquisa espacial", "warning")
        ]
        
        for titulo, exemplos, cor in aplicacoes:
            self.print_colored(f"• {titulo}", cor)
            self.print_colored(f"  {exemplos}", "text")
        
        self.print_section("O que é PROGRAMAÇÃO?", "🔹")
        
        self.print_concept(
            "Programação",
            "É como dar instruções para um computador, mas de forma\n" +
            "muito específica e organizada. É como escrever uma receita de bolo:"
        )
        
        self.print_colored("\n📝 RECEITA DE BOLO:", "warning")
        self.print_colored("1. Pegue 3 ovos", "text")
        self.print_colored("2. Misture com farinha", "text")
        self.print_colored("3. Asse por 30 minutos", "text")
        
        self.print_colored("\n💻 PROGRAMA EM PYTHON:", "success")
        self.print_colored("1. Peça o nome do usuário", "text")
        self.print_colored("2. Calcule a idade", "text")
        self.print_colored("3. Mostre uma mensagem personalizada", "text")
        
        self.print_section("Como o computador 'entende' Python?", "🧠", "accent")
        
        self.print_colored(
            "O computador só entende 0s e 1s (código binário).\n" +
            "Python é traduzido para essa linguagem por um 'interpretador'.",
            "text"
        )
        
        self.print_colored("\nPROCESSO DE TRADUÇÃO:", "warning")
        self.print_colored("VOCÊ ESCREVE: print('Olá!')", "success")
        self.print_colored("PYTHON TRADUZ: 01001000 01100101 01101100...", "info")
        self.print_colored("COMPUTADOR EXECUTA: Olá!", "accent")
        
        self.print_section("O que você vai aprender neste curso?", "🎯", "success")
        
        topicos = [
            ("1. 📝", "Como 'falar' com o computador"),
            ("2. 🗃️", "Como guardar e organizar informações"),
            ("3. 🤔", "Como fazer o programa tomar decisões"),
            ("4. 🔄", "Como repetir tarefas automaticamente"),
            ("5. 📋", "Como trabalhar com listas de dados"),
            ("6. ⚙️", "Como criar suas próprias 'ferramentas'")
        ]
        
        for num, desc in topicos:
            self.print_colored(f"{num} {desc}", "primary")
        self.print_colored("7. 🧮 Como construir uma calculadora completa!", "primary")
        
        self.print_section("CURIOSIDADES SOBRE PYTHON", "💡", "warning")
        
        curiosidades = [
            "Python executa aproximadamente 100.000 linhas por segundo!",
            "O Instagram processa 95 milhões de fotos por dia usando Python",
            "Python ajudou a descobrir ondas gravitacionais no espaço",
            "Netflix usa Python para recomendar filmes para você",
            "Python pode controlar robôs, drones e até mesmo carros!"
        ]
        
        for curiosidade in curiosidades:
            self.print_colored(f"• {curiosidade}", "info")
        
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
        
        self.print_success("🎉 Vamos criar seu primeiro projeto prático!")
        
        self.print_concept(
            "Cartão de Apresentação Digital",
            "Um programa que cria um cartão de apresentação personalizado"
        )
        
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos = [
            "Páginas pessoais",
            "Assinaturas de email",
            "Perfis profissionais",
            "Cartões de visita digitais"
        ]
        for uso in usos:
            self.print_colored(f"• {uso}", "accent")
        
        self.print_section("PASSO 1: Vamos coletar suas informações", "📝", "info")
        self.print_tip("Digite suas informações (pode ser real ou fictício)")
        
        try:
            if self.ui:
                input_color = self.ui.get_color("warning")
                reset = self.ui.get_color("reset")
                
                nome = input(f"{input_color}👤 Seu nome: {reset}").strip()
                if not nome:
                    nome = "Estudante Python"
                
                profissao = input(f"{input_color}💼 Sua profissão/área de interesse: {reset}").strip()
                if not profissao:
                    profissao = "Futuro Programador Python"
                
                hobby = input(f"{input_color}🎮 Um hobby ou interesse: {reset}").strip()
                if not hobby:
                    hobby = "Aprender programação"
            else:
                nome = input("👤 Seu nome: ").strip()
                if not nome:
                    nome = "Estudante Python"
                
                profissao = input("💼 Sua profissão/área de interesse: ").strip()
                if not profissao:
                    profissao = "Futuro Programador Python"
                
                hobby = input("🎮 Um hobby ou interesse: ").strip()
                if not hobby:
                    hobby = "Aprender programação"
                
            self.print_success(f"Informações coletadas para {nome}!")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
            
        self.print_section("PASSO 2: Agora vamos PROGRAMAR o cartão!", "💻", "success")
        self.print_colored("Aqui está o código que você criou:", "text")
        
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
        
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_gerado)
        
        self.print_success("🎉 PARABÉNS! Você criou seu primeiro projeto!")
        
        self.print_section("APLICAÇÕES NA VIDA REAL", "💡", "info")
        aplicacoes = [
            "Sites pessoais usam códigos similares",
            "Apps de rede social fazem perfis assim",
            "Sistemas de RH organizam dados de funcionários",
            "Jogos criam fichas de personagens"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Primeiro Projeto!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Cartão de Apresentação Python")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo01Introducao()
    print("Teste do módulo 1 - versão standalone")
    module._introducao_python()