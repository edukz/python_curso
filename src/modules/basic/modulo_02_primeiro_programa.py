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
        """Executa o módulo Primeiro Programa"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._primeiro_programa_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _primeiro_programa_interativo(self) -> None:
        """Conteúdo principal do módulo Primeiro Programa"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MÓDULO 2: SEU PRIMEIRO PROGRAMA")
        else:
            print("\n" + "="*50)
            print("🎯 MÓDULO 2: SEU PRIMEIRO PROGRAMA")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Chegou a hora de escrever seu PRIMEIRO programa em Python!")
        self.print_tip("Este módulo está dividido em seções interativas. Você controla o ritmo!")

        # === FLUXO PRINCIPAL COM TRATAMENTO DE CTRL+C ===

        # 1. Sistema de navegação por seções
        try:
            self._navegacao_secoes_interativas()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Navegação interrompida pelo usuário. Voltando ao menu principal...")
            return

        # 2. Seção de Prática Interativa
        try:
            self._secao_pratica_interativa()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Módulo interrompido pelo usuário. Voltando ao menu principal...")
            return

        # 3. Mini Projeto Prático
        try:
            self._mini_projeto_cartoes_digitais()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES ===
        secoes = [
            {
                'id': 'secao_o_que_e_programa',
                'titulo': '🎯 O que é um programa?',
                'descricao': 'Entenda o conceito fundamental de programação',
                'funcao': self._secao_o_que_e_programa
            },
            {
                'id': 'secao_funcao_print',
                'titulo': '💻 A função print() - sua primeira ferramenta',
                'descricao': 'Domine a função mais usada em Python',
                'funcao': self._secao_funcao_print
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Exemplos práticos do print()',
                'descricao': 'Veja print() em ação com código real',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_aspas_formatacao',
                'titulo': '🔤 Aspas e formatação de texto',
                'descricao': 'Aprenda a trabalhar com strings corretamente',
                'funcao': self._secao_aspas_formatacao
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Aprenda com os erros mais frequentes de iniciantes',
                'funcao': self._secao_erros_comuns
            },
            {
                'id': 'secao_dicas_profissionais',
                'titulo': '⭐ Dicas de profissionais experientes',
                'descricao': 'Segredos que todo programador deveria saber',
                'funcao': self._secao_dicas_profissionais
            },
            {
                'id': 'secao_mundo_real',
                'titulo': '🌍 Como programs são usados no mundo real',
                'descricao': 'Aplicações práticas e exemplos inspiradores',
                'funcao': self._secao_mundo_real
            }
        ]

        secoes_visitadas = set()

        # === LOOP PRINCIPAL DE NAVEGAÇÃO ===
        while True:
            # Limpa tela e mostra cabeçalho
            self.ui.clear_screen() if self.ui else print("\n" + "="*50)
            self.print_section("NAVEGAÇÃO DO MÓDULO", "📚", "accent")
            self.print_colored("Escolha uma seção para estudar:", "text")

            # Lista todas as seções com status
            print()
            for i, secao in enumerate(secoes, 1):
                status = "✅" if secao['id'] in secoes_visitadas else "📖"
                print(f"{status} {i}. {secao['titulo']}")
                self.print_colored(f"    {secao['descricao']}", "text")
                print()

            print("0. 🎯 Continuar para os Exercícios Práticos")

            # Mostra progresso visual
            progresso = len(secoes_visitadas)
            total = len(secoes)
            self.print_colored(f"\n📊 Progresso: {progresso}/{total} seções visitadas", "info")

            if progresso == total:
                self.print_success("🌟 Você completou todas as seções! Está pronto para praticar!")

            # Processa escolha do usuário
            try:
                escolha = input(f"\n👉 Escolha uma seção (1-{len(secoes)}) ou 0 para continuar: ").strip()

                if escolha == "0":
                    # Verifica se visitou seções suficientes
                    if progresso >= 3:  # Pelo menos 3 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 3 seções antes de continuar!")
                        continuar = input("Quer continuar mesmo assim? (s/n): ").lower()
                        if continuar in ['s', 'sim', 'yes']:
                            break
                elif escolha.isdigit() and 1 <= int(escolha) <= len(secoes):
                    # Executa seção escolhida
                    idx = int(escolha) - 1
                    secoes[idx]['funcao']()
                    secoes_visitadas.add(secoes[idx]['id'])
                else:
                    self.print_warning(f"❌ Opção inválida! Digite um número de 1 a {len(secoes)} ou 0.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Pulando para exercícios práticos...")
                break
            except Exception as e:
                self.print_warning(f"❌ Erro: {str(e)}. Tente novamente.")

    def _secao_o_que_e_programa(self) -> None:
        """Seção: O que é um programa?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É UM PROGRAMA?", "🎯")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Programa de Computador",
            "Uma sequência de instruções que o computador segue para realizar uma tarefa específica"
        )

        # === DICA RELACIONADA ===
        self.print_tip("Pense em um programa como uma receita de bolo - passo a passo até o resultado final!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Um programa é como dar instruções para um amigo fazer um sanduíche:", "text")
        self.print_colored("1. Pegue o pão", "text")
        self.print_colored("2. Passe a maionese", "text")
        self.print_colored("3. Coloque o presunto", "text")
        self.print_colored("4. Feche o sanduíche", "text")
        self.print_colored("\nO computador segue suas instruções exatamente assim!", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você escreve o código (as instruções) em Python",
            "2. O Python traduz seu código para linguagem de máquina",
            "3. O computador executa as instruções uma por uma",
            "4. Você vê o resultado na tela!"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''print("Olá! Eu sou um programa!")'''
        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE PROGRAMAS SÃO USADOS NO MUNDO REAL:", "accent")
        aplicacoes = [
            "WhatsApp - programa que envia mensagens",
            "Instagram - programa que organiza fotos",
            "Netflix - programa que mostra filmes",
            "Google Maps - programa que calcula rotas",
            "Spotify - programa que toca músicas"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_funcao_print(self) -> None:
        """Seção: A função print() - sua primeira ferramenta"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("A FUNÇÃO PRINT() - SUA PRIMEIRA FERRAMENTA", "💻")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Função print()",
            "Uma ferramenta que exibe (imprime) informações na tela do computador"
        )

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("A função print() é como um megafone:", "text")
        self.print_colored("• Você fala algo no megafone (escreve no print)", "text")
        self.print_colored("• O megafone amplifica sua voz (print mostra na tela)", "text")
        self.print_colored("• Todos conseguem ouvir (ver na tela) sua mensagem", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 ANATOMIA DO PRINT():", "info")
        passos_anatomia = [
            "1. 'print' - É o nome da função (sempre minúsculo!)",
            "2. '(' - Abre parênteses para começar os parâmetros",
            "3. \"texto\" - A mensagem que você quer mostrar (entre aspas)",
            "4. ')' - Fecha parênteses para terminar"
        ]

        for i, passo in enumerate(passos_anatomia, 1):
            self.print_colored(passo, "text")
            if i < len(passos_anatomia):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 PRIMEIRO EXEMPLO:", "success")
        codigo_exemplo = '''print("Olá, Mundo!")'''
        self.exemplo(codigo_exemplo)
        print("\n🚀 Resultado:")
        self.executar_codigo(codigo_exemplo)

        # === CARACTERÍSTICAS IMPORTANTES ===
        self.print_colored("\n⭐ CARACTERÍSTICAS DA FUNÇÃO PRINT():", "accent")
        caracteristicas = [
            "É uma função built-in (já vem instalada com Python)",
            "Sempre usa letra minúscula - print, nunca Print",
            "Precisa de parênteses - print() não print",
            "Texto sempre entre aspas - simples ' ou duplas \" ",
            "É a função mais usada por programadores iniciantes"
        ]
        for caract in caracteristicas:
            self.print_colored(f"• {caract}", "primary")

        self.pausar()

    def _secao_exemplos_praticos(self) -> None:
        """Seção: Exemplos práticos do print()"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("EXEMPLOS PRÁTICOS DO PRINT()", "💡", "success")

        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Mensagem simples',
                'descricao': 'O clássico primeiro programa de todo programador',
                'codigo': '''print("Olá, Mundo!")''',
                'explicacao': 'Este é o programa mais famoso da história da programação!'
            },
            {
                'titulo': 'EXEMPLO 2: Múltiplas mensagens',
                'descricao': 'Como exibir várias linhas de texto',
                'codigo': '''print("Bem-vindo ao Python!")
print("Você está aprendendo programação")
print("Isso é incrível!")''',
                'explicacao': 'Cada print() cria uma nova linha na tela'
            },
            {
                'titulo': 'EXEMPLO 3: Usando emojis',
                'descricao': 'Deixando seus programas mais divertidos e visuais',
                'codigo': '''print("🐍 Python é incrível! 🐍")
print("🚀 Vamos programar juntos! 🚀")
print("🎉 Você está arrasando! 🎉")''',
                'explicacao': 'Python funciona perfeitamente com emojis e caracteres especiais'
            }
        ]

        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")

            self.print_code_section("CÓDIGO", exemplo['codigo'])

            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])

            if exemplo['explicacao']:
                self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")

            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")

        self.print_success("\n🎉 Agora você viu print() em ação! Vamos praticar!")
        self.pausar()

    def _secao_aspas_formatacao(self) -> None:
        """Seção: Aspas e formatação de texto"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ASPAS E FORMATAÇÃO DE TEXTO", "🔤")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Strings (Texto)",
            "Qualquer sequência de caracteres (letras, números, símbolos) que representam texto"
        )

        # === TIPOS DE ASPAS ===
        self.print_colored("\n🔧 TIPOS DE ASPAS EM PYTHON:", "info")
        self.print_colored("1. Aspas duplas: \"texto\" ", "text")
        self.print_colored("2. Aspas simples: 'texto' ", "text")
        self.print_colored("\n✅ Ambas funcionam exatamente igual!", "success")

        # === EXEMPLOS PRÁTICOS ===
        self.print_colored("\n💻 COMPARAÇÃO PRÁTICA:", "warning")
        
        print("\n🔸 Com aspas duplas:")
        codigo1 = '''print("Python é fantástico!")'''
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        print("\n🔸 Com aspas simples:")
        codigo2 = '''print('Python é fantástico!')'''
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        # === QUANDO USAR CADA UMA ===
        self.print_colored("\n🎯 QUANDO USAR CADA TIPO:", "accent")
        self.print_colored("• Use aspas duplas quando o texto tem aspas simples dentro", "primary")
        exemplo_duplas = '''print("Ele disse: 'Python é incrível!'")'''
        self.exemplo(exemplo_duplas)
        self.executar_codigo(exemplo_duplas)
        
        print()
        self.print_colored("• Use aspas simples quando o texto tem aspas duplas dentro", "primary")
        exemplo_simples = '''print('O livro se chama "Aprendendo Python"')'''
        self.exemplo(exemplo_simples)
        self.executar_codigo(exemplo_simples)

        # === DICA PROFISSIONAL ===
        self.print_tip("\nDICA PROFISSIONAL: Escolha um tipo e seja consistente em todo o projeto!")

        self.pausar()

    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ERROS COMUNS E COMO EVITAR", "⚠️")

        self.print_colored("🎯 Todo programador comete erros - faz parte do aprendizado!", "info")
        self.print_colored("Vamos ver os erros mais comuns para você evitá-los:", "text")

        erros_comuns = [
            {
                'titulo': 'ERRO 1: Esquecer as aspas',
                'errado': 'print(Olá mundo)',
                'correto': 'print("Olá mundo")',
                'explicacao': 'Python não sabe o que é "Olá mundo" sem as aspas. Ele pensa que é uma variável!'
            },
            {
                'titulo': 'ERRO 2: Letra maiúscula no print',
                'errado': 'Print("Olá")',
                'correto': 'print("Olá")',
                'explicacao': 'Python diferencia maiúsculas de minúsculas. A função se chama print, não Print!'
            },
            {
                'titulo': 'ERRO 3: Esquecer os parênteses',
                'errado': 'print "Olá mundo"',
                'correto': 'print("Olá mundo")',
                'explicacao': 'Em Python 3, print() é uma função e precisa de parênteses!'
            },
            {
                'titulo': 'ERRO 4: Não fechar aspas ou parênteses',
                'errado': 'print("Olá mundo"',
                'correto': 'print("Olá mundo")',
                'explicacao': 'Tudo que abre deve fechar! Aspas e parênteses sempre em pares.'
            },
            {
                'titulo': 'ERRO 5: Misturar tipos de aspas',
                'errado': 'print("Olá mundo\')',
                'correto': 'print("Olá mundo")',
                'explicacao': 'Se começou com aspas duplas, termine com aspas duplas!'
            }
        ]

        for i, erro in enumerate(erros_comuns, 1):
            self.print_colored(f"\n{erro['titulo']}", "warning")
            
            self.print_colored("❌ ERRADO:", "red")
            self.print_code_section("Código com erro", erro['errado'])
            
            self.print_colored("✅ CORRETO:", "green")
            self.print_code_section("Código correto", erro['correto'])
            print("\n🚀 Funcionando:")
            self.executar_codigo(erro['correto'])
            
            self.print_colored(f"💡 EXPLICAÇÃO: {erro['explicacao']}", "info")
            
            if i < len(erros_comuns):
                input("\n🔸 Pressione ENTER para o próximo erro...")

        self.print_success("\n🎉 Agora você conhece os erros mais comuns e sabe como evitá-los!")
        self.pausar()

    def _secao_dicas_profissionais(self) -> None:
        """Seção: Dicas de profissionais experientes"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("DICAS DE PROFISSIONAIS EXPERIENTES", "⭐")

        dicas = [
            {
                'titulo': '🔧 DICA 1: Use print() para debug',
                'explicacao': 'Quando algo não funciona, adicione prints para ver o que está acontecendo',
                'exemplo': '''nome = "João"
print(f"Debug: nome = {nome}")
print("Processando...")
resultado = nome.upper()
print(f"Debug: resultado = {resultado}")'''
            },
            {
                'titulo': '🎨 DICA 2: Deixe seus prints bonitos',
                'explicacao': 'Programas com saída visual atrativa impressionam mais',
                'exemplo': '''print("=" * 40)
print("    🎉 BEM-VINDO AO MEU PROGRAMA 🎉")
print("=" * 40)
print("Status: ✅ Funcionando perfeitamente!")'''
            },
            {
                'titulo': '📝 DICA 3: Comente seu código',
                'explicacao': 'Use # para deixar lembretes para você mesmo',
                'exemplo': '''# Este programa cumprimenta o usuário
print("Olá!")  # Mensagem de boas-vindas
print("Bem-vindo!")  # Mensagem adicional'''
            },
            {
                'titulo': '🚀 DICA 4: Pratique todos os dias',
                'explicação': 'Mesmo 15 minutos por dia fazem diferença enorme',
                'exemplo': '''# Desafio diário: criar algo novo com print()
print("📅 Dia 1: Aprendi print()")
print("📅 Dia 2: Criei arte ASCII")
print("📅 Dia 3: Fiz um menu bonito")'''
            }
        ]

        for i, dica in enumerate(dicas, 1):
            self.print_colored(f"\n{dica['titulo']}", "warning")
            self.print_colored(f"💡 {dica['explicacao']}", "text")
            
            self.print_code_section("EXEMPLO PRÁTICO", dica['exemplo'])
            print("\n🚀 Resultado:")
            self.executar_codigo(dica['exemplo'])
            
            if i < len(dicas):
                input("\n🔸 Pressione ENTER para a próxima dica...")

        self.print_success("\n🌟 Agora você tem dicas valiosas de programadores experientes!")
        self.pausar()

    def _secao_mundo_real(self) -> None:
        """Seção: Como programas são usados no mundo real"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO PROGRAMAS SÃO USADOS NO MUNDO REAL", "🌍")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Programas no Mundo Real",
            "Aplicações práticas que resolvem problemas reais e facilitam a vida das pessoas"
        )

        # === CATEGORIAS DE APLICAÇÕES ===
        categorias = [
            {
                'titulo': '📱 APLICATIVOS MÓVEIS',
                'exemplos': [
                    'WhatsApp - usar print() para logs de mensagens',
                    'Instagram - usar print() para debug de upload de fotos', 
                    'Uber - usar print() para rastrear localização do motorista',
                    'iFood - usar print() para confirmar pedidos'
                ]
            },
            {
                'titulo': '🌐 SITES E SISTEMAS WEB',
                'exemplos': [
                    'Google - usar print() para logs de busca',
                    'Netflix - usar print() para debug de streaming',
                    'Amazon - usar print() para confirmar compras',
                    'YouTube - usar print() para estatísticas de vídeos'
                ]
            },
            {
                'titulo': '🤖 AUTOMAÇÃO E IA',
                'exemplos': [
                    'ChatGPT - usar print() para debug de respostas',
                    'Robôs industriais - usar print() para status',
                    'Carros autônomos - usar print() para sensores',
                    'Smart homes - usar print() para controle'
                ]
            },
            {
                'titulo': '💼 SISTEMAS EMPRESARIAIS',
                'exemplos': [
                    'Bancos - usar print() para logs de transações',
                    'Hospitais - usar print() para sistemas de prontuário',
                    'Escolas - usar print() para controle de notas',
                    'Lojas - usar print() para relatórios de vendas'
                ]
            }
        ]

        for categoria in categorias:
            self.print_colored(f"\n{categoria['titulo']}", "warning")
            for exemplo in categoria['exemplos']:
                self.print_colored(f"• {exemplo}", "primary")
            input("\n🔸 Pressione ENTER para a próxima categoria...")

        # === EXEMPLO PRÁTICO INSPIRADOR ===
        self.print_colored("\n🚀 EXEMPLO INSPIRADOR:", "success")
        self.print_colored("Um programador júnior criou um sistema simples para uma padaria:", "text")
        
        codigo_padaria = '''print("=" * 30)
print("  🥖 PADARIA DO JOÃO 🥖")
print("=" * 30)
print("Pães vendidos hoje: 150")
print("Faturamento: R$ 450,00")
print("Status: ✅ Meta atingida!")
print("=" * 30)'''
        
        self.exemplo(codigo_padaria)
        print("\n🚀 Resultado:")
        self.executar_codigo(codigo_padaria)
        
        self.print_colored("\n💰 RESULTADO: O dono ficou tão impressionado que contratou o programador!", "success")
        self.print_colored("Moral da história: Até um simples print() pode abrir portas!", "info")

        self.pausar()

    def _mini_projeto_cartoes_digitais(self) -> None:
        """Mini Projeto - Módulo 2: Gerador de Cartões Digitais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: GERADOR DE CARTÕES DIGITAIS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: GERADOR DE CARTÕES DIGITAIS")
            print("="*50)
        
        self.print_success("🎉 Vamos criar seu projeto prático aplicando tudo sobre print()!")

        self.print_concept(
            "Gerador de Cartões Digitais",
            "Um programa que cria diferentes tipos de cartões personalizados usando apenas print()"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Sites de e-cards como Hallmark e Blue Mountain",
            "Apps de mensagens que criam cards personalizados",
            "Sistemas de RH para parabenizar funcionários",
            "Redes sociais que geram posts automáticos"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Escolha do tipo de cartão
        self.print_section("PASSO 1: Escolhendo o tipo de cartão", "📝", "info")
        self.print_tip("Primeiro vamos decidir que tipo de cartão criar")

        try:
            print("\n🎨 Que tipo de cartão você quer criar?")
            print("1. 🎂 Cartão de Aniversário")
            print("2. 🎉 Cartão de Parabéns")
            print("3. ❤️ Cartão de Amor/Amizade")
            print("4. 🌟 Cartão Motivacional")
            
            escolha = input("\n👉 Escolha (1-4): ").strip()
            
            tipos_cartao = {
                '1': {'nome': 'Aniversário', 'emoji': '🎂', 'cor': 'success'},
                '2': {'nome': 'Parabéns', 'emoji': '🎉', 'cor': 'warning'}, 
                '3': {'nome': 'Amor/Amizade', 'emoji': '❤️', 'cor': 'accent'},
                '4': {'nome': 'Motivacional', 'emoji': '🌟', 'cor': 'info'}
            }
            
            if escolha in tipos_cartao:
                tipo_escolhido = tipos_cartao[escolha]
                self.print_colored(f"\n✅ Você escolheu: {tipo_escolhido['emoji']} Cartão de {tipo_escolhido['nome']}!", "success")
            else:
                tipo_escolhido = tipos_cartao['1']  # Default
                self.print_colored("\n🎂 Vamos fazer um cartão de aniversário!", "success")

        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Coleta de informações
        self.print_section("PASSO 2: Personalizando seu cartão", "⚙️", "success")
        self.print_colored("Agora vamos personalizar com suas informações:", "text")

        try:
            nome_destinatario = input("\n👤 Para quem é o cartão? ").strip() or "Amigo"
            nome_remetente = input("👤 Qual é o seu nome? ").strip() or "Programador Python"
            mensagem_extra = input("💌 Mensagem especial (opcional): ").strip() or "Feito com Python!"
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 3: Geração do cartão
        self.print_section("PASSO 3: Gerando seu cartão digital", "🎬", "warning")

        # Gera o código baseado na escolha
        if escolha == '1':  # Aniversário
            codigo_final = f'''# 🎂 CARTÃO DE ANIVERSÁRIO DIGITAL
# Feito com Python por {nome_remetente}

print("🎊" * 25)
print("")
print("    🎂 FELIZ ANIVERSÁRIO! 🎂")
print("")
print("🎊" * 25)
print("")
print(f"    Parabéns, {nome_destinatario}!")
print("")
print("🎈 Que este novo ano seja repleto de:")
print("   ✨ Alegrias")
print("   🌟 Conquistas")
print("   💖 Amor")
print("   🚀 Aventuras")
print("")
print(f"💌 {mensagem_extra}")
print("")
print(f"    Com carinho, {nome_remetente} 💕")
print("")
print("🎊" * 25)'''
        elif escolha == '2':  # Parabéns
            codigo_final = f'''# 🎉 CARTÃO DE PARABÉNS DIGITAL
# Feito com Python por {nome_remetente}

print("🏆" * 25)
print("")
print("    🎉 PARABÉNS! 🎉")
print("")
print("🏆" * 25)
print("")
print(f"    {nome_destinatario}, você conseguiu!")
print("")
print("✨ Sua conquista é motivo de orgulho!")
print("🌟 Você merece todo o sucesso!")
print("🚀 Continue brilhando assim!")
print("")
print(f"💌 {mensagem_extra}")
print("")
print(f"    Orgulhoso de você, {nome_remetente} 🌟")
print("")
print("🏆" * 25)'''
        elif escolha == '3':  # Amor/Amizade
            codigo_final = f'''# ❤️ CARTÃO DE AMOR/AMIZADE DIGITAL
# Feito com Python por {nome_remetente}

print("💖" * 25)
print("")
print("    ❤️ COM AMOR ❤️")
print("")
print("💖" * 25)
print("")
print(f"    Para {nome_destinatario},")
print("")
print("🌹 Você é especial na minha vida")
print("✨ Obrigado por existir")
print("🤗 Nossa amizade/amor é um presente")
print("💫 Que sorte a minha te conhecer!")
print("")
print(f"💌 {mensagem_extra}")
print("")
print(f"    Para sempre, {nome_remetente} 💕")
print("")
print("💖" * 25)'''
        else:  # Motivacional
            codigo_final = f'''# 🌟 CARTÃO MOTIVACIONAL DIGITAL
# Feito com Python por {nome_remetente}

print("⭐" * 25)
print("")
print("    🌟 VOCÊ É INCRÍVEL! 🌟")
print("")
print("⭐" * 25)
print("")
print(f"    {nome_destinatario},")
print("")
print("💪 Você é mais forte do que imagina")
print("🚀 Seus sonhos são possíveis")
print("✨ Cada dia é uma nova oportunidade")
print("🏆 Continue acreditando em si!")
print("")
print(f"💌 {mensagem_extra}")
print("")
print(f"    Torcendo por você, {nome_remetente} 🌟")
print("")
print("⭐" * 25)'''
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")
        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou seu projeto de cartões digitais!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais tipos de cartões (formatura, natal, etc.)",
            "Criar bordas mais elaboradas com caracteres ASCII",
            "Integrar com sistema de envio de email",
            "Salvar cartões em arquivos de texto"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Criador de Cartões Digitais!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Gerador de Cartões Digitais")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")

        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")

        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Conhecimentos sobre print()',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é o nome da função que exibe texto na tela em Python?',
                        'answer': ['print', 'print()', 'função print'],
                        'hint': 'É uma função que começa com "p" e tem 5 letras'
                    },
                    {
                        'question': 'Python diferencia maiúsculas de minúsculas? (sim/não)',
                        'answer': ['sim', 's', 'yes'],
                        'hint': 'print é diferente de Print'
                    },
                    {
                        'question': 'Posso usar tanto aspas simples \'\' quanto duplas ""? (sim/não)',
                        'answer': ['sim', 's', 'yes'],
                        'hint': 'Ambas funcionam igualmente bem em Python'
                    },
                    {
                        'question': 'Complete: print(___"Olá"___) - que símbolos vão no lugar dos ___?',
                        'answer': ['()','parênteses', '( )'],
                        'hint': 'print é uma função, precisa de...'
                    },
                    {
                        'question': 'O que está errado: Print("teste") ?',
                        'answer': ['P maiúsculo', 'maiúsculo', 'letra maiúscula', 'Print'],
                        'hint': 'Olhe a primeira letra da palavra print'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o código para exibir "Olá Python!"',
                        'starter': '_____("Olá Python!")',
                        'solution': 'print("Olá Python!")',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Crie dois prints que formem uma mensagem de boas-vindas',
                        'starter': '# Linha 1: "Bem-vindo ao Python!"\n# Linha 2: "Vamos programar juntos!"\n_____\n_____',
                        'solution': 'print("Bem-vindo ao Python!")\nprint("Vamos programar juntos!")',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Crie um cartão simples usando múltiplos prints e símbolos',
                        'starter': '# Crie um cartão com bordas usando * ou =\n# Inclua uma mensagem no meio\n# Use pelo menos 3 prints',
                        'solution': 'print("*" * 20)\nprint("* Olá, Mundo! *")\nprint("*" * 20)',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Arte ASCII Simples',
                'type': 'creative',
                'instruction': 'Use apenas print() para criar uma arte ASCII simples (emoji, casa, estrela, etc.)'
            }
        ]

        # === MENU PRINCIPAL DE EXERCÍCIOS ===
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
                elif escolha in ["3", "criativo"]:
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
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre print()",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie arte ASCII simples",
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

    def _run_quiz(self, quiz_data) -> None:
        """Executa o quiz de conhecimentos"""
        self.print_section(quiz_data['title'], "📝", "info")
        score = 0
        total = len(quiz_data['questions'])

        self.print_colored(f"Vamos testar seus conhecimentos com {total} perguntas!", "text")
        print()

        for i, q in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\n📌 PERGUNTA {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            tentativas = 0
            max_tentativas = 2
            
            while tentativas < max_tentativas:
                try:
                    resposta = input("\n👉 Sua resposta: ").strip().lower()
                    
                    if any(ans.lower() in resposta for ans in q['answer']):
                        self.print_success("✅ Correto! Muito bem!")
                        score += 1
                        break
                    else:
                        tentativas += 1
                        if tentativas < max_tentativas:
                            self.print_warning(f"❌ Não é isso. Dica: {q['hint']}")
                            self.print_colored("Tente novamente:", "text")
                        else:
                            self.print_warning(f"❌ A resposta era: {q['answer'][0]}")
                            
                except KeyboardInterrupt:
                    self.print_warning("\n⚠️ Quiz cancelado.")
                    return

        # Resultado final
        percentual = (score / total) * 100
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        self.print_colored(f"Você acertou {score} de {total} perguntas ({percentual:.0f}%)", "text")
        
        if score == total:
            self.print_success("🌟 PERFEITO! Você dominou completamente o print()!")
        elif score >= total * 0.8:
            self.print_success("🎉 EXCELENTE! Você entende muito bem o print()!")
        elif score >= total * 0.6:
            self.print_colored("👍 BOM! Você está no caminho certo!", "info")
        else:
            self.print_colored("📚 Continue estudando! Revisite as seções se necessário.", "warning")
            
        self.pausar()

    def _run_code_completion(self, exercise_data) -> None:
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "success")
        
        for i, exercise in enumerate(exercise_data['exercises'], 1):
            self.print_colored(f"\n🎯 EXERCÍCIO {i}: {exercise['type'].upper()}", "warning")
            self.print_colored(exercise['instruction'], "text")
            
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercise['starter'])
            
            print("\n✍️ Digite sua solução (ou 'skip' para pular):")
            try:
                resposta = input(">>> ").strip()
                
                if resposta.lower() == 'skip':
                    self.print_colored("⏭️ Exercício pulado.", "warning")
                    continue
                    
                if resposta:
                    print("\n🚀 Testando sua solução:")
                    try:
                        self.executar_codigo(resposta)
                        self.print_success("✅ Sua solução funcionou!")
                        
                        ver_solucao = input("\n💡 Quer ver a solução sugerida? (s/n): ").lower()
                        if ver_solucao == 's':
                            self.print_colored("\n🔍 SOLUÇÃO SUGERIDA:", "info")
                            self.exemplo(exercise['solution'])
                            
                    except Exception as e:
                        self.print_warning(f"❌ Erro ao executar: {str(e)}")
                        self.print_colored("\n💡 SOLUÇÃO CORRETA:", "info")
                        self.exemplo(exercise['solution'])
                        self.executar_codigo(exercise['solution'])
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Exercício cancelado.")
                return
                
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de código!")
        self.pausar()

    def _run_creative_exercise(self, exercise_data) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "accent")
        self.print_colored(exercise_data['instruction'], "text")
        
        print("\n💡 EXEMPLOS DE ARTE ASCII SIMPLES:")
        exemplos = [
            "Estrela:\n  *\n ***\n*****",
            "Casa:\n   /\\\n  /  \\\n |__|",
            "Coração:\n ♥ ♥\n♥♥♥♥\n ♥♥♥"
        ]
        
        for exemplo in exemplos:
            self.print_colored(f"• {exemplo}", "primary")
            
        print("\n✍️ Agora é sua vez! Digite seus prints (digite 'fim' para terminar):")
        
        linhas_codigo = []
        try:
            while True:
                linha = input(">>> ")
                if linha.lower() == 'fim':
                    break
                if linha.strip():
                    linhas_codigo.append(linha)
                    
        except KeyboardInterrupt:
            self.print_warning("\n⚠️ Exercício cancelado.")
            return
            
        if linhas_codigo:
            codigo_completo = '\n'.join(linhas_codigo)
            print("\n🚀 Sua criação:")
            try:
                self.executar_codigo(codigo_completo)
                self.print_success("\n🎨 Fantástico! Você criou arte com código!")
            except Exception as e:
                self.print_warning(f"❌ Erro na execução: {str(e)}")
        else:
            self.print_colored("👋 Tudo bem, talvez na próxima vez!", "info")
            
        self.pausar()
    


# Para teste standalone
if __name__ == "__main__":
    module = Modulo02PrimeiroPrograma()
    print("Teste do módulo 2 - versão standalone")
    module._primeiro_programa_interativo()