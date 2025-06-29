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
        self.print_tip("Este módulo está dividido em seções interativas. Você controla o ritmo!")
        
        # Sistema de navegação por seções
        try:
            self._navegacao_secoes_interativas()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Navegação interrompida pelo usuário. Voltando ao menu principal...")
            return
        
        # Seção de Prática Interativa
        try:
            self._secao_pratica_interativa()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Módulo interrompido pelo usuário. Voltando ao menu principal...")
            return
        
        # Mini Projeto Prático
        try:
            self._mini_projeto_cartao_apresentacao()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""
        secoes = [
            {
                'id': 'python_intro',
                'titulo': '🐍 O que é Python?',
                'descricao': 'Descobra a origem e características do Python',
                'funcao': self._secao_o_que_e_python
            },
            {
                'id': 'python_especial',
                'titulo': '🌟 Por que Python é especial?',
                'descricao': 'Entenda os pontos fortes da linguagem',
                'funcao': self._secao_por_que_especial
            },
            {
                'id': 'python_usos',
                'titulo': '🔧 Onde Python é usado?',
                'descricao': 'Exemplos reais de empresas que usam Python',
                'funcao': self._secao_onde_usado
            },
            {
                'id': 'programacao_conceito',
                'titulo': '🔹 O que é programação?',
                'descricao': 'Entenda o conceito de programação de forma simples',
                'funcao': self._secao_conceito_programacao
            },
            {
                'id': 'python_funcionamento',
                'titulo': '🧠 Como o computador entende Python?',
                'descricao': 'O processo de tradução do código',
                'funcao': self._secao_como_funciona
            },
            {
                'id': 'curso_conteudo',
                'titulo': '🎯 O que você vai aprender?',
                'descricao': 'Visão geral do curso completo',
                'funcao': self._secao_conteudo_curso
            },
            {
                'id': 'curiosidades',
                'titulo': '💡 Curiosidades sobre Python',
                'descricao': 'Fatos interessantes e motivacionais',
                'funcao': self._secao_curiosidades
            }
        ]
        
        secoes_visitadas = set()
        
        while True:
            self.ui.clear_screen() if self.ui else print("\n" + "="*50)
            self.print_section("NAVEGAÇÃO DO MÓDULO", "📚", "accent")
            self.print_colored("Escolha uma seção para estudar:", "text")
            
            print()
            for i, secao in enumerate(secoes, 1):
                status = "✅" if secao['id'] in secoes_visitadas else "📖"
                print(f"{status} {i}. {secao['titulo']}")
                self.print_colored(f"    {secao['descricao']}", "text")
                print()
            
            print("0. 🎯 Continuar para os Exercícios Práticos")
            
            # Mostrar progresso
            progresso = len(secoes_visitadas)
            total = len(secoes)
            self.print_colored(f"\n📊 Progresso: {progresso}/{total} seções visitadas", "info")
            
            if progresso == total:
                self.print_success("🌟 Você completou todas as seções! Está pronto para praticar!")
            
            try:
                escolha = input("\n👉 Escolha uma seção (1-7) ou 0 para continuar: ").strip()
                
                if escolha == "0":
                    if progresso >= 3:  # Pelo menos 3 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 3 seções antes de continuar!")
                        continuar = input("Quer continuar mesmo assim? (s/n): ").lower()
                        if continuar in ['s', 'sim', 'yes']:
                            break
                elif escolha.isdigit() and 1 <= int(escolha) <= len(secoes):
                    idx = int(escolha) - 1
                    secoes[idx]['funcao']()
                    secoes_visitadas.add(secoes[idx]['id'])
                else:
                    self.print_warning("❌ Opção inválida! Digite um número de 1 a 7 ou 0.")
                    
            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Pulando para exercícios práticos...")
                break
            except Exception as e:
                self.print_warning(f"❌ Erro: {str(e)}. Tente novamente.")
    
    def _secao_o_que_e_python(self) -> None:
        """Seção: O que é Python?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("O QUE É PYTHON?", "🐍")
        
        self.print_concept(
            "Python",
            "Uma linguagem de programação criada por Guido van Rossum em 1991."
        )
        
        self.print_tip("O nome vem do grupo de comédia britânico 'Monty Python'! 🎭")
        
        self.print_colored("\n🎭 CURIOSIDADE:", "warning")
        self.print_colored("Guido van Rossum era fã do programa 'Monty Python's Flying Circus'", "text")
        self.print_colored("e queria um nome curto, único e levemente misterioso!", "text")
        
        self.pausar()
    
    def _secao_por_que_especial(self) -> None:
        """Seção: Por que Python é especial?"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("Por que Python é especial?", "🌟", "warning")
        
        características = [
            ("📚 FÁCIL DE APRENDER", "Sintaxe simples e intuitiva"),
            ("🚀 PODEROSA E VERSÁTIL", "Resolve problemas complexos"),
            ("🌍 MUITO POPULAR", "Uma das linguagens mais usadas no mundo"),
            ("🤝 COMUNIDADE ATIVA", "Milhões de programadores ajudam uns aos outros")
        ]
        
        for i, (titulo, desc) in enumerate(características, 1):
            self.print_colored(f"\n{i}. {titulo}", "accent")
            self.print_colored(f"   {desc}", "text")
            
            if i < len(características):
                input("   🔸 Pressione ENTER para ver a próxima característica...")
        
        self.print_success("\n🎉 Essas são as principais razões pelas quais Python é amado!")
        self.pausar()
    
    def _secao_onde_usado(self) -> None:
        """Seção: Onde Python é usado no mundo real?"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("Onde Python é usado no mundo real?", "🔧", "info")
        
        aplicacoes = [
            ("🤖 INTELIGÊNCIA ARTIFICIAL", "Netflix, Tesla, Google", "warning"),
            ("🌐 DESENVOLVIMENTO WEB", "Instagram, Spotify, Pinterest", "success"),
            ("📊 ANÁLISE DE DADOS", "NASA, Banco Central, universidades", "info"),
            ("🎮 JOGOS", "Civilization IV, EVE Online", "accent"),
            ("🏢 AUTOMAÇÃO", "Dropbox, Reddit, BitTorrent", "primary"),
            ("🧬 CIÊNCIA", "Descobertas médicas, pesquisa espacial", "warning")
        ]
        
        for i, (titulo, exemplos, cor) in enumerate(aplicacoes, 1):
            self.print_colored(f"\n{i}. {titulo}", cor)
            self.print_colored(f"   Exemplos: {exemplos}", "text")
            
            if i < len(aplicacoes):
                input("   🔸 Pressione ENTER para ver a próxima área...")
        
        self.print_success("\n🌟 Python está em todos os lugares!")
        self.pausar()
    
    def _secao_conceito_programacao(self) -> None:
        """Seção: O que é programação?"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("O que é PROGRAMAÇÃO?", "🔹")
        
        self.print_concept(
            "Programação",
            "É como dar instruções para um computador, mas de forma\nmuito específica e organizada."
        )
        
        self.print_tip("Vamos usar uma analogia que todos entendem: fazer um bolo! 🍰")
        
        input("\n🔸 Pressione ENTER para ver a analogia...")
        
        self.print_colored("\n📝 RECEITA DE BOLO:", "warning")
        receita = ["1. Pegue 3 ovos", "2. Misture com farinha", "3. Asse por 30 minutos"]
        for passo in receita:
            self.print_colored(passo, "text")
            input("   ⏳ Pressione ENTER para o próximo passo...")
        
        input("\n🔸 Agora vamos ver como é em programação...")
        
        self.print_colored("\n💻 PROGRAMA EM PYTHON:", "success")
        programa = ["1. Peça o nome do usuário", "2. Calcule a idade", "3. Mostre uma mensagem personalizada"]
        for passo in programa:
            self.print_colored(passo, "text")
            input("   ⏳ Pressione ENTER para o próximo passo...")
        
        self.print_success("\n🎯 Viu como é similar? Programação é dar instruções passo a passo!")
        self.pausar()
    
    def _secao_como_funciona(self) -> None:
        """Seção: Como o computador entende Python?"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("Como o computador 'entende' Python?", "🧠", "accent")
        
        self.print_colored(
            "O computador só entende 0s e 1s (código binário).\nPython é traduzido para essa linguagem por um 'interpretador'.",
            "text"
        )
        
        input("\n🔸 Vamos ver o processo passo a passo...")
        
        self.print_colored("\n🔄 PROCESSO DE TRADUÇÃO:", "warning")
        
        passos = [
            ("VOCÊ ESCREVE:", "print('Olá!')", "success"),
            ("PYTHON TRADUZ:", "01001000 01100101 01101100...", "info"),
            ("COMPUTADOR EXECUTA:", "Olá!", "accent")
        ]
        
        for i, (etapa, exemplo, cor) in enumerate(passos, 1):
            print(f"\n{i}. {etapa}")
            self.print_colored(f"   {exemplo}", cor)
            if i < len(passos):
                input("   ⏳ Pressione ENTER para ver a próxima etapa...")
        
        self.print_success("\n🎉 É assim que o Python 'fala' com o computador!")
        self.pausar()
    
    def _secao_conteudo_curso(self) -> None:
        """Seção: O que você vai aprender neste curso?"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("O que você vai aprender neste curso?", "🎯", "success")
        
        topicos = [
            ("1. 📝", "Como 'falar' com o computador"),
            ("2. 🗃️", "Como guardar e organizar informações"),
            ("3. 🤔", "Como fazer o programa tomar decisões"),
            ("4. 🔄", "Como repetir tarefas automaticamente"),
            ("5. 📋", "Como trabalhar com listas de dados"),
            ("6. ⚙️", "Como criar suas próprias 'ferramentas'"),
            ("7. 🧮", "Como construir uma calculadora completa!")
        ]
        
        for num, desc in topicos:
            self.print_colored(f"{num} {desc}", "primary")
            input("   🔸 Pressione ENTER para ver o próximo tópico...")
        
        self.print_success("\n🚀 Ao final, você será capaz de criar seus próprios programas!")
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre Python"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("CURIOSIDADES SOBRE PYTHON", "💡", "warning")
        
        curiosidades = [
            "Python executa aproximadamente 100.000 linhas por segundo!",
            "O Instagram processa 95 milhões de fotos por dia usando Python",
            "Python ajudou a descobrir ondas gravitacionais no espaço",
            "Netflix usa Python para recomendar filmes para você",
            "Python pode controlar robôs, drones e até mesmo carros!"
        ]
        
        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n💫 CURIOSIDADE {i}:", "accent")
            self.print_colored(f"   {curiosidade}", "info")
            
            if i < len(curiosidades):
                input("   🔸 Pressione ENTER para a próxima curiosidade...")
        
        self.print_success("\n🌟 Python é realmente incrível!")
        self.pausar()
    
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
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")
        
        # Instruções para iniciantes
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")
        
        exercicios = [
            {
                'title': 'Quiz: Conhecimentos sobre Python',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Em que ano Python foi criado?',
                        'answer': ['1991', 'mil novecentos e noventa e um'],
                        'hint': 'Foi criado no início dos anos 90'
                    },
                    {
                        'question': 'Quem criou Python?',
                        'answer': ['Guido van Rossum', 'Guido', 'Van Rossum'],
                        'hint': 'O primeiro nome começa com G'
                    },
                    {
                        'question': 'Python é usado no Instagram? (sim/não)',
                        'answer': ['sim', 's', 'yes'],
                        'hint': 'Lembre-se das empresas mencionadas'
                    },
                    {
                        'question': 'O nome Python vem de que grupo de comédia?',
                        'answer': ['Monty Python', 'monty python'],
                        'hint': 'É um grupo britânico famoso'
                    },
                    {
                        'question': 'Python é uma linguagem fácil de aprender? (sim/não)',
                        'answer': ['sim', 's', 'yes'],
                        'hint': 'Uma das principais características mencionadas'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete com uma mensagem simples',
                        'starter': 'print("🎉 Parabéns!")\n# Complete aqui\nprint("🎉 Fim!")',
                        'solution': 'print("Estou aprendendo Python!")',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'DESAFIO: Complete com uma operação matemática',
                        'starter': 'print("Calculadora Python:")\n# Complete aqui\nprint("Resultado calculado!")',
                        'solution': 'print(2 + 3)',
                        'type': 'math'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete com texto formatado',
                        'starter': 'nome = "Python"\nversao = 3.12\n# Complete aqui\nprint("Fim do programa")',
                        'solution': 'print(f"Linguagem: {nome}, Versão: {versao}")',
                        'type': 'format'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Seu Slogan Python',
                'type': 'creative',
                'instruction': 'Crie seu próprio slogan sobre aprender Python!'
            }
        ]
        
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("0. Continuar para o Mini Projeto")
            
            try:
                escolha = input("\n👉 Sua escolha: ").strip().lower()
                
                if escolha in ["0", "continuar", "sair", "proximo"]:
                    break
                elif escolha in ["1", "quiz", "conhecimentos"]:
                    try:
                        self._run_quiz(exercicios[0])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo", "slogan"]:
                    try:
                        self._run_creative_exercise(exercicios[2])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício criativo. Continuando...")
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")
                    
            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return  # Sai da função em vez de continuar para o mini projeto
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre Python",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie seu slogan Python",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto final",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para aprender melhor!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo"""
        self.print_section(quiz_data['title'], "📝")
        score = 0
        total_questions = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            print(f"\n📝 Pergunta {i} de {total_questions}:")
            correto = self.exercicio(
                q['question'],
                q['answer'],
                q['hint']
            )
            if correto:
                score += 1
        
        # Feedback detalhado baseado na pontuação
        percentage = (score / total_questions) * 100
        
        self.print_success(f"\n🏆 RESULTADO: {score} de {total_questions} perguntas corretas ({percentage:.0f}%)")
        
        if percentage == 100:
            self.print_success("🌟 PERFEITO! Você dominou os conceitos básicos!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você tem um bom entendimento!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos e tente novamente.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo e tente mais tarde.", "info")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código Inicial", ex['starter'])
            
            # Diferentes tipos de exercícios
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print("\n✍️ Digite uma mensagem entre aspas:")
                print("💡 Exemplo: 'Olá, mundo!' ou 'Python é incrível!'")
                user_input = input(">>> ").strip()
                if user_input:
                    if user_input.startswith('"') and user_input.endswith('"'):
                        user_code = f'print({user_input})'
                    elif user_input.startswith("'") and user_input.endswith("'"):
                        user_code = f'print({user_input})'
                    else:
                        user_code = f'print("{user_input}")'
                else:
                    user_code = 'print("Olá!")'
                    
            elif exercise_type == 'math':
                print("\n✍️ Digite uma operação matemática:")
                print("💡 Exemplos: 2 + 3, 10 - 4, 5 * 2, 15 / 3")
                user_input = input(">>> ").strip()
                
                # Validação básica de operação matemática
                if user_input and any(op in user_input for op in ['+', '-', '*', '/']):
                    # Verifica se não há caracteres perigosos
                    if all(c.isdigit() or c in '+-*/.() ' for c in user_input):
                        try:
                            # Testa se a operação é válida
                            eval(user_input)
                            user_code = f'print({user_input})'
                        except:
                            self.print_warning("❌ Operação inválida. Usando exemplo padrão.")
                            user_code = 'print(2 + 2)'
                    else:
                        self.print_warning("❌ Use apenas números e operadores (+, -, *, /)")
                        user_code = 'print(2 + 2)'
                else:
                    self.print_warning("💡 Nenhuma operação detectada. Usando exemplo padrão.")
                    user_code = 'print(2 + 2)'
                    
            elif exercise_type == 'format':
                print("\n✍️ Digite um f-string usando as variáveis 'nome' e 'versao':")
                print("💡 F-strings são textos que começam com 'f' e usam {} para variáveis")
                print("📝 Exemplo: f'A linguagem {nome} versão {versao} é ótima!'")
                print("🎯 Dica: Use {nome} e {versao} no seu texto!")
                
                user_input = input(">>> ").strip()
                if user_input:
                    if user_input.startswith('f"') or user_input.startswith("f'"):
                        user_code = f'print({user_input})'
                    elif '{nome}' in user_input and '{versao}' in user_input:
                        user_code = f'print(f"{user_input}")'
                    elif '{nome}' in user_input or '{versao}' in user_input:
                        user_code = f'print(f"{user_input}")'
                        self.print_tip("Boa! Você usou pelo menos uma variável!")
                    else:
                        user_code = f'print("{user_input}")'
                        self.print_tip("Não foi um f-string, mas funciona! Texto normal também é válido.")
                else:
                    user_code = 'print(f"Linguagem: {nome}")'
                    self.print_tip("Usando exemplo padrão com f-string.")
            else:
                # Tipo padrão
                print("\n✍️ Digite a linha que falta:")
                user_input = input(">>> ").strip()
                user_code = f'print("{user_input}")' if user_input else 'print("")'
            
            # Substitui a linha inteira que contém o comentário
            lines = ex['starter'].split('\n')
            for j, line in enumerate(lines):
                if '# Complete aqui' in line:
                    lines[j] = user_code
                    break
            complete_code = '\n'.join(lines)
            
            print("\n🚀 Executando seu código completo:")
            self.executar_codigo(complete_code)
            
            print(f"\n💡 Solução sugerida: {ex['solution']}")
            self.print_success("✅ Muito bem! Você completou o código!")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        print("💡 Exemplo: 'Python: A linguagem que transforma ideias em realidade!'")
        print("🎯 Seja criativo! Pode ser divertido, motivacional ou técnico.")
        
        slogan = input("\n✍️ Seu slogan Python: ").strip()
        
        if slogan:
            print("\n🌟 Seu slogan ficou incrível!")
            
            # Vamos criar um código mais elaborado
            codigo_slogan = f'''print("=" * 50)
print("🐍✨ SEU SLOGAN PYTHON ✨🐍")
print("=" * 50)
print()
print("🎯 {slogan}")
print()
print("=" * 50)
print("🚀 Criado com Python!")
print("=" * 50)'''
            
            print("\n🚀 Executando seu slogan em grande estilo:")
            self.executar_codigo(codigo_slogan)
            
            self.print_success("\n🎉 Parabéns pela criatividade!")
            
            # Bonus: perguntar se quer criar outro
            outro = input("\n🎨 Quer criar outro slogan? (s/n): ").lower()
            if outro == 's':
                slogan2 = input("\n✍️ Segundo slogan: ").strip()
                if slogan2:
                    codigo_duplo = f'''print("🔥 SEUS SLOGANS PYTHON 🔥")
print("1️⃣ {slogan}")
print("2️⃣ {slogan2}")
print("🏆 Você é um criador de slogans!")'''
                    self.executar_codigo(codigo_duplo)
        else:
            self.print_warning("❌ Você precisa criar um slogan para continuar!")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo01Introducao()
    print("Teste do módulo 1 - versão standalone")
    module._introducao_python()