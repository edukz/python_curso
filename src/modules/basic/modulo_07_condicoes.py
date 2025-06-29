#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 7: Estruturas Condicionais (if/else)
Aprenda a tomar decisões nos seus programas
"""

from ..shared.base_module import BaseModule


class Modulo07Condicoes(BaseModule):
    """Módulo 7: Tomando Decisões com if/else"""
    
    def __init__(self):
        super().__init__("modulo_7", "Estruturas Condicionais")
        self.has_mini_project = True
        self.mini_project_points = 60
    
    def execute(self) -> None:
        """Executa o módulo Estruturas Condicionais"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._condicoes_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _condicoes_interativo(self) -> None:
        """Conteúdo principal do módulo Estruturas Condicionais"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🤔 MÓDULO 7: TOMANDO DECISÕES COM IF/ELSE")
        else:
            print("\n" + "="*50)
            print("🤔 MÓDULO 7: TOMANDO DECISÕES COM IF/ELSE")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Chegou a hora de ensinar programas a tomar decisões inteligentes!")
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
            self._mini_projeto_avaliador_inteligente()
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
                'id': 'secao_conceito_decisoes',
                'titulo': '🎯 O que são decisões na programação?',
                'descricao': 'Entenda como programas tomam decisões',
                'funcao': self._secao_conceito_decisoes
            },
            {
                'id': 'secao_if_else_basico',
                'titulo': '⚙️ Como if/else funciona?',
                'descricao': 'Veja o processo passo a passo das condições',
                'funcao': self._secao_if_else_basico
            },
            {
                'id': 'secao_operadores_comparacao',
                'titulo': '🔍 Operadores de comparação',
                'descricao': 'Veja condições em ação com código real',
                'funcao': self._secao_operadores_comparacao
            },
            {
                'id': 'secao_operadores_logicos',
                'titulo': '🧠 Operadores lógicos (and, or, not)',
                'descricao': 'Combine múltiplas condições inteligentemente',
                'funcao': self._secao_operadores_logicos
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas de condições',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Aprenda com os erros mais frequentes',
                'funcao': self._secao_erros_comuns
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
    
    def _secao_conceito_decisoes(self) -> None:
        """Seção: O que são decisões na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO DECISÕES NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Estruturas Condicionais",
            "São comandos que fazem o programa escolher diferentes caminhos baseado em condições específicas"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Assim como você decide se vai levar guarda-chuva baseado na previsão do tempo!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine um semáforo inteligente:", "text")
        self.print_colored("• Se tem carros esperando → Fica verde", "text")
        self.print_colored("• Se não tem carros → Continua vermelho", "text")
        self.print_colored("• Se é de madrugada → Fica amarelo piscando", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. O programa verifica uma condição (ex: idade >= 18)",
            "2. Se a condição for verdadeira, executa um bloco de código",
            "3. Se for falsa, pode executar outro bloco (else) ou pular"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Programa que decide se pode votar
idade = 17

if idade >= 16:
    print("✅ Você pode votar!")
else:
    print("❌ Ainda não pode votar")
    print(f"Faltam {16 - idade} anos")'''
        
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix - Decide quais filmes recomendar baseado no seu histórico",
            "Bancos - Aprovam ou negam empréstimos baseado em critérios",
            "GPS - Escolhe a melhor rota baseado no trânsito",
            "Games - Muda a dificuldade baseado na performance do jogador"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_if_else_basico(self) -> None:
        """Seção: Como if/else funciona?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO IF/ELSE FUNCIONA?", "⚙️")
        
        # === ESTRUTURA BÁSICA ===
        self.print_colored("🏗️ ESTRUTURA BÁSICA DO IF/ELSE:", "warning")
        estrutura = '''if condição:
    # Código executado se condição for True
    print("Condição verdadeira!")
else:
    # Código executado se condição for False
    print("Condição falsa!")'''
        
        self.exemplo(estrutura)
        
        # === PONTOS IMPORTANTES ===
        self.print_colored("\n📌 PONTOS IMPORTANTES:", "info")
        pontos = [
            "• Os dois pontos (:) são obrigatórios",
            "• A indentação (espaços) define o que está dentro do if",
            "• O else é opcional - pode ter só if",
            "• Pode ter elif (else if) para múltiplas condições"
        ]
        
        for ponto in pontos:
            self.print_colored(ponto, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO ELIF ===
        self.print_colored("\n🔀 EXEMPLO COM ELIF (MÚLTIPLAS CONDIÇÕES):", "success")
        codigo_elif = '''nota = 8.5

if nota >= 9:
    print("🌟 Conceito A - Excelente!")
elif nota >= 7:
    print("📚 Conceito B - Muito bom!")
elif nota >= 6:
    print("📖 Conceito C - Bom")
else:
    print("📝 Conceito D - Precisa estudar mais")

print(f"Sua nota: {nota}")'''
        
        self.exemplo(codigo_elif)
        
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_elif)
        
        self.pausar()
    
    def _secao_operadores_comparacao(self) -> None:
        """Seção: Operadores de comparação"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("OPERADORES DE COMPARAÇÃO", "🔍")
        
        # === LISTA DE OPERADORES ===
        self.print_colored("🔧 FERRAMENTAS PARA COMPARAR VALORES:", "warning")
        operadores = [
            ("==", "Igual", "5 == 5 → True"),
            ("!=", "Diferente", "5 != 3 → True"),
            (">", "Maior que", "8 > 5 → True"),
            ("<", "Menor que", "3 < 7 → True"),
            (">=", "Maior ou igual", "5 >= 5 → True"),
            ("<=", "Menor ou igual", "4 <= 6 → True")
        ]
        
        for simbolo, nome, exemplo in operadores:
            self.print_colored(f"• {simbolo:2} ({nome:12}) - Exemplo: {exemplo}", "text")
            input("   ⏳ Pressione ENTER para o próximo...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💡 EXEMPLO PRÁTICO - SISTEMA DE ACESSO:", "success")
        codigo_acesso = '''# Sistema de controle de acesso
idade = 25
tem_documento = True

print("🏢 SISTEMA DE CONTROLE DE ACESSO")
print("-" * 40)

if idade >= 18:
    print("✅ Idade: Maior de idade")
else:
    print("❌ Idade: Menor de idade")

if tem_documento == True:
    print("✅ Documento: Apresentado")
else:
    print("❌ Documento: Não apresentado")

if idade >= 18 and tem_documento:
    print("\\n🎉 ACESSO LIBERADO!")
else:
    print("\\n🚫 ACESSO NEGADO!")'''
        
        self.exemplo(codigo_acesso)
        
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_acesso)
        
        self.print_tip("Cuidado: Use == para comparar, não = (que é para atribuir valores)")
        
        self.pausar()
    
    def _secao_operadores_logicos(self) -> None:
        """Seção: Operadores lógicos (and, or, not)"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("OPERADORES LÓGICOS", "🧠")
        
        # === EXPLICAÇÃO DOS OPERADORES ===
        self.print_colored("🤝 COMBINANDO MÚLTIPLAS CONDIÇÕES:", "warning")
        
        # Operador AND
        self.print_colored("\n🔗 AND - TODAS as condições devem ser verdadeiras:", "info")
        self.print_colored("• Como uma porta com duas chaves - precisa das duas!", "text")
        
        codigo_and = '''# Exemplo AND - Precisa de TODAS as condições
idade = 20
tem_carteira = True
tem_carro = True

if idade >= 18 and tem_carteira and tem_carro:
    print("🚗 Pode dirigir seu próprio carro!")
else:
    print("🚫 Não pode dirigir")'''
        
        self.exemplo(codigo_and)
        self.executar_codigo(codigo_and)
        input("\n🔸 Pressione ENTER para o próximo operador...")
        
        # Operador OR
        self.print_colored("\n🎯 OR - PELO MENOS UMA condição deve ser verdadeira:", "info")
        self.print_colored("• Como ter múltiplas chaves - qualquer uma abre!", "text")
        
        codigo_or = '''# Exemplo OR - Basta UMA condição ser verdadeira
tem_dinheiro = False
tem_cartao = True
tem_pix = False

if tem_dinheiro or tem_cartao or tem_pix:
    print("💳 Pode pagar a compra!")
else:
    print("💸 Não pode pagar")
    
print("Formas de pagamento disponíveis:")
if tem_dinheiro:
    print("  💵 Dinheiro")
if tem_cartao:
    print("  💳 Cartão")
if tem_pix:
    print("  📱 PIX")'''
        
        self.exemplo(codigo_or)
        self.executar_codigo(codigo_or)
        input("\n🔸 Pressione ENTER para o próximo operador...")
        
        # Operador NOT
        self.print_colored("\n🔄 NOT - INVERTE o resultado (verdadeiro vira falso):", "info")
        self.print_colored("• Como um interruptor - liga vira desliga!", "text")
        
        codigo_not = '''# Exemplo NOT - Inverte o resultado
chovendo = False
tem_guarda_chuva = True

print(f"Está chovendo? {chovendo}")
print(f"Tem guarda-chuva? {tem_guarda_chuva}")

if not chovendo:
    print("☀️ Não está chovendo - pode sair sem guarda-chuva!")
else:
    print("🌧️ Está chovendo - melhor levar guarda-chuva!")
    
# Exemplo mais complexo
if not chovendo and tem_guarda_chuva:
    print("✅ Condições perfeitas para um passeio!")'''
        
        self.exemplo(codigo_not)
        self.executar_codigo(codigo_not)
        
        # === TABELA DA VERDADE ===
        self.print_colored("\n📊 TABELA DA VERDADE:", "warning")
        tabela = [
            "True  and True  = True",
            "True  and False = False",
            "False and True  = False", 
            "False and False = False",
            "",
            "True  or True   = True",
            "True  or False  = True",
            "False or True   = True",
            "False or False  = False",
            "",
            "not True  = False",
            "not False = True"
        ]
        
        for linha in tabela:
            if linha:
                self.print_colored(f"  {linha}", "text")
            else:
                print()
        
        self.pausar()
    
    def _secao_casos_uso(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR NA VIDA REAL?", "🌍")
        
        casos_uso = [
            {
                'titulo': '🏦 SISTEMA BANCÁRIO',
                'descricao': 'Aprovação de empréstimos e cartões de crédito',
                'exemplo': '''# Sistema de aprovação de empréstimo
renda = 5000
score = 750
tempo_emprego = 24  # meses

if renda >= 3000 and score >= 600 and tempo_emprego >= 12:
    print("✅ Empréstimo APROVADO!")
    if score >= 800:
        print("🌟 Taxa preferencial: 1.5% ao mês")
    else:
        print("📊 Taxa padrão: 2.1% ao mês")
else:
    print("❌ Empréstimo NEGADO")'''
            },
            {
                'titulo': '🎮 DESENVOLVIMENTO DE GAMES',
                'descricao': 'Lógica de gameplay e progressão',
                'exemplo': '''# Sistema de level up em game
experiencia = 1250
level_atual = 5

if experiencia >= 1000 and level_atual < 10:
    print("🎉 LEVEL UP!")
    print(f"Subiu para level {level_atual + 1}")
    
    if level_atual == 4:
        print("🔓 Nova habilidade desbloqueada: Fireball!")
    elif level_atual == 9:
        print("🏆 Conquistou o título: Mestre Aventureiro!")
else:
    falta_exp = 1000 - (experiencia % 1000)
    print(f"Faltam {falta_exp} pontos para o próximo level")'''
            },
            {
                'titulo': '🛒 E-COMMERCE',
                'descricao': 'Cálculo de frete e promoções',
                'exemplo': '''# Sistema de desconto e frete
valor_compra = 150.00
eh_cliente_vip = True
cep_regiao = "SP"

desconto = 0
frete = 15.00

# Calcula desconto
if valor_compra >= 100:
    desconto = 10  # 10% de desconto
elif valor_compra >= 50:
    desconto = 5   # 5% de desconto

# Desconto VIP adicional
if eh_cliente_vip:
    desconto += 5

# Calcula frete
if valor_compra >= 200 or eh_cliente_vip:
    frete = 0  # Frete grátis

valor_final = valor_compra * (1 - desconto/100) + frete

print(f"💰 Valor da compra: R$ {valor_compra:.2f}")
print(f"🎁 Desconto total: {desconto}%")
print(f"🚚 Frete: R$ {frete:.2f}")
print(f"💸 Total a pagar: R$ {valor_final:.2f}")'''
            }
        ]
        
        for i, caso in enumerate(casos_uso):
            self.print_colored(f"\n{caso['titulo']}", "warning")
            self.print_colored(f"📝 {caso['descricao']}", "text")
            
            self.print_code_section("EXEMPLO", caso['exemplo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(caso['exemplo'])
            
            if i < len(casos_uso) - 1:
                input("\n🔸 Pressione ENTER para o próximo caso...")
        
        self.print_success("\n🌟 Condições estão em TODO LUGAR na programação!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS", "⭐")
        
        praticas = [
            {
                'titulo': '📝 Use nomes descritivos para variáveis',
                'ruim': '''if x > 18:
    print("OK")''',
                'bom': '''if idade > 18:
    print("Maior de idade")'''
            },
            {
                'titulo': '🔍 Prefira comparações explícitas',
                'ruim': '''if nome:  # Pode confundir
    print("OK")''',
                'bom': '''if nome != "":  # Mais claro
    print("Nome informado")'''
            },
            {
                'titulo': '🎯 Evite condições muito complexas',
                'ruim': '''if (idade >= 18 and tem_documento and not suspenso and credito_ok and not bloqueado):
    print("Aprovado")''',
                'bom': '''# Quebrar em variáveis intermediárias
pode_dirigir = idade >= 18 and tem_documento and not suspenso
tem_credito_ok = credito_ok and not bloqueado

if pode_dirigir and tem_credito_ok:
    print("Aprovado")'''
            },
            {
                'titulo': '💡 Use comentários para lógicas complexas',
                'ruim': '''if score >= 600 and renda * 12 > valor * 0.3:
    print("Aprovado")''',
                'bom': '''# Regra do banco: score mínimo 600 e 
# renda anual deve ser pelo menos 30% do valor
if score >= 600 and renda * 12 > valor * 0.3:
    print("Empréstimo aprovado")'''
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{i}. {pratica['titulo']}", "warning")
            
            self.print_colored("\n❌ EVITE:", "error")
            self.exemplo(pratica['ruim'])
            
            self.print_colored("✅ PREFIRA:", "success")
            self.exemplo(pratica['bom'])
            
            if i < len(praticas):
                input("\n🔸 Pressione ENTER para a próxima prática...")
        
        self.print_tip("Código limpo e legível é mais importante que código 'inteligente'!")
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ERROS COMUNS E COMO EVITAR", "⚠️")
        
        erros = [
            {
                'titulo': '🔸 Esquecer os dois pontos (:)',
                'erro': '''if idade >= 18  # ❌ ERRO: Faltou :
    print("Maior de idade")''',
                'correto': '''if idade >= 18:  # ✅ CORRETO
    print("Maior de idade")''',
                'dica': 'Python sempre exige : após if, elif, else'
            },
            {
                'titulo': '🔸 Confundir = com ==',
                'erro': '''if nome = "João":  # ❌ ERRO: = é atribuição
    print("Olá João")''',
                'correto': '''if nome == "João":  # ✅ CORRETO: == é comparação
    print("Olá João")''',
                'dica': '= atribui valor, == compara valores'
            },
            {
                'titulo': '🔸 Indentação incorreta',
                'erro': '''if idade >= 18:
print("Maior de idade")  # ❌ ERRO: Sem indentação''',
                'correto': '''if idade >= 18:
    print("Maior de idade")  # ✅ CORRETO: Com indentação''',
                'dica': 'Use 4 espaços para indentar (padrão Python)'
            },
            {
                'titulo': '🔸 Usar and/or incorretamente',
                'erro': '''# ❌ ERRO: Esta condição nunca será True
if idade >= 18 and idade <= 10:
    print("Impossível")''',
                'correto': '''# ✅ CORRETO: Usar OR para faixas excludentes
if idade <= 10 or idade >= 65:
    print("Desconto especial")''',
                'dica': 'AND exige que ambas sejam verdadeiras simultaneamente'
            }
        ]
        
        for i, erro in enumerate(erros, 1):
            self.print_colored(f"\n{i}. {erro['titulo']}", "warning")
            
            self.print_colored("\n❌ CÓDIGO COM ERRO:", "error")
            self.exemplo(erro['erro'])
            
            self.print_colored("✅ CÓDIGO CORRETO:", "success")
            self.exemplo(erro['correto'])
            
            self.print_tip(erro['dica'])
            
            if i < len(erros):
                input("\n🔸 Pressione ENTER para o próximo erro...")
        
        self.print_success("\n🎯 Conhecendo os erros comuns, você os evitará!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre condições!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Condições',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual operador usamos para verificar se dois valores são iguais?',
                        'answer': ['==', 'igual', 'duplo igual'],
                        'hint': 'Não confunda com = que é para atribuir valores!'
                    },
                    {
                        'question': 'Se queremos que TODAS as condições sejam verdadeiras, qual operador lógico usamos?',
                        'answer': ['and', 'e'],
                        'hint': 'Pense em "isso E aquilo" - ambos precisam ser verdade'
                    },
                    {
                        'question': 'O que é obrigatório no final de um if em Python?',
                        'answer': [':', 'dois pontos', 'doispontos'],
                        'hint': 'É um sinal de pontuação que vem depois da condição'
                    },
                    {
                        'question': 'Qual comando usamos para múltiplas condições alternativas?',
                        'answer': ['elif', 'else if'],
                        'hint': 'É uma junção de "else" + "if" em Python'
                    },
                    {
                        'question': 'Quantos espaços são recomendados para indentação em Python?',
                        'answer': ['4', 'quatro', '4 espaços'],
                        'hint': 'É o padrão oficial do Python (PEP 8)'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a condição para verificar se a pessoa pode votar (16+ anos)',
                        'starter': '''idade = 17
if idade ___ 16:
    print("✅ Pode votar!")
else:
    print("❌ Não pode votar ainda")''',
                        'solution': '>=',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete usando operador lógico para dirigir (18+ anos E ter carteira)',
                        'starter': '''idade = 20
tem_carteira = True

if idade >= 18 ___ tem_carteira:
    print("🚗 Pode dirigir!")
else:
    print("🚫 Não pode dirigir")''',
                        'solution': 'and',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o sistema de desconto com múltiplas condições',
                        'starter': '''valor = 120
eh_vip = True
desconto = 0

if valor >= 100:
    desconto = 10
____ valor >= 50:
    desconto = 5

if eh_vip:
    desconto ___ 5

print(f"Desconto total: {desconto}%")''',
                        'solution': 'elif\n+=',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Classificação Pessoal',
                'type': 'creative',
                'instruction': 'Crie um sistema que classifica algo do seu interesse (filmes, músicas, livros, etc.) baseado em critérios que você escolher!'
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
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre condições if/else",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie seu próprio sistema de classificação",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto de Avaliador Inteligente",
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
        
        if percentage >= 80:
            self.print_success("🌟 Excelente! Você domina as condições!")
        elif percentage >= 60:
            self.print_success("👏 Muito bom! Continue praticando!")
        else:
            self.print_tip("💪 Continue estudando! Revise as seções teóricas.")
        
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código para Completar", ex['starter'])
            
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print(f"\n✍️ Complete a condição:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Perfeito! Resposta correta!")
                    # Mostrar código completo funcionando
                    codigo_completo = ex['starter'].replace('___', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'intermediate':
                print(f"\n✍️ Complete o operador lógico:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Correto! Operador lógico perfeito!")
                    codigo_completo = ex['starter'].replace('___', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'advanced':
                print(f"\n✍️ Complete as duas partes (uma por linha):")
                print("Linha 1:")
                input1 = input(">>> ").strip()
                print("Linha 2:")
                input2 = input(">>> ").strip()
                
                solutions = ex['solution'].split('\n')
                correct = (input1.lower() == solutions[0].lower() and 
                          input2.lower() == solutions[1].lower())
                
                if correct:
                    self.print_success("✅ Excelente! Código avançado completo!")
                    codigo_completo = ex['starter'].replace('____', input1).replace('___', input2)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. As respostas eram: {solutions[0]} e {solutions[1]}")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de código!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        
        print("\n💡 Exemplo de sistema de classificação:")
        print("Sistema de Avaliação de Filmes:")
        print("• Se duração > 180 minutos → 'Filme longo'")
        print("• Se nota_imdb >= 8.0 → 'Obra-prima'") 
        print("• Se ano >= 2020 → 'Lançamento recente'")
        
        print("\n🎯 Agora é sua vez! Pense em algo que gosta e crie critérios para classificar:")
        
        categoria = input("\n📝 O que você quer classificar? (ex: livros, músicas, jogos): ").strip()
        
        if categoria:
            print(f"\n🌟 Ótima escolha! Vamos criar um sistema para classificar {categoria}!")
            
            criterio1 = input(f"🔸 Critério 1 - Complete: Se _____ então... : ").strip()
            resultado1 = input(f"🔸 Resultado 1 - O que acontece?: ").strip()
            
            criterio2 = input(f"🔸 Critério 2 - Complete: Se _____ então... : ").strip()
            resultado2 = input(f"🔸 Resultado 2 - O que acontece?: ").strip()
            
            # Criar código baseado nas respostas
            codigo_criativo = f'''# 🎨 SISTEMA DE CLASSIFICAÇÃO DE {categoria.upper()}
# Criado por você!

def classificar_{categoria.lower().replace(' ', '_')}():
    print("🎯 SISTEMA DE CLASSIFICAÇÃO DE {categoria.upper()}")
    print("=" * 50)
    
    # Critério 1
    if {criterio1}:
        print("✅ {resultado1}")
    else:
        print("⚠️ Não atende ao critério 1")
    
    # Critério 2  
    if {criterio2}:
        print("✅ {resultado2}")
    else:
        print("⚠️ Não atende ao critério 2")
    
    print("\\n🎉 Sistema funcionando!")

# Testando o sistema
classificar_{categoria.lower().replace(' ', '_')}()'''
            
            print("\n🚀 Aqui está seu sistema de classificação personalizado:")
            self.exemplo(codigo_criativo)
            
            print(f"\n🎉 Incrível! Você criou um sistema inteligente para {categoria}!")
            self.print_success("🏆 Parabéns pela criatividade!")
        else:
            print("\n🎨 Sem problema! A criatividade vem com a prática!")
        
        self.pausar()
    
    def _mini_projeto_avaliador_inteligente(self) -> None:
        """Mini Projeto - Módulo 7: Avaliador Inteligente de Perfis"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: AVALIADOR INTELIGENTE DE PERFIS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: AVALIADOR INTELIGENTE DE PERFIS")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu sistema de avaliação inteligente usando condições!")
        
        self.print_concept(
            "Avaliador Inteligente",
            "Um sistema que analisa perfis e toma decisões automáticas baseado em múltiplos critérios"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Recursos Humanos - Triagem automática de candidatos",
            "Bancos - Análise de risco para empréstimos",
            "Plataformas de dating - Compatibilidade entre usuários",
            "E-commerce - Sistema de recomendação personalizada"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Coleta de informações
        self.print_section("PASSO 1: Coletando informações do perfil", "📝", "info")
        self.print_tip("Vamos simular dados de um candidato para nossa análise")
        
        try:
            print("\n🧪 Dados do candidato para análise:")
            nome = "Ana Silva"
            idade = 28
            experiencia = 5  # anos
            formacao = "Superior"
            nota_teste = 8.5
            tem_certificacoes = True
            disponibilidade = "Integral"
            
            print(f"👤 Nome: {nome}")
            print(f"🎂 Idade: {idade} anos")
            print(f"💼 Experiência: {experiencia} anos")
            print(f"🎓 Formação: {formacao}")
            print(f"📊 Nota do teste: {nota_teste}")
            print(f"🏆 Certificações: {'Sim' if tem_certificacoes else 'Não'}")
            print(f"⏰ Disponibilidade: {disponibilidade}")
            
            input("\n🔸 Pressione ENTER para começar a análise...")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Processamento e análise
        self.print_section("PASSO 2: Analisando o perfil com inteligência", "⚙️", "success")
        self.print_colored("Agora vamos aplicar nossa lógica de avaliação:", "text")
        
        # PASSO 3: Gerando resultado
        self.print_section("PASSO 3: Resultado da avaliação inteligente", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo do seu Avaliador Inteligente:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: AVALIADOR INTELIGENTE DE PERFIS
# Módulo 7: Estruturas Condicionais

def avaliar_candidato(nome, idade, experiencia, formacao, nota_teste, tem_certificacoes, disponibilidade):
    """Sistema inteligente de avaliação de candidatos"""
    
    print(f"\\n🔍 ANALISANDO PERFIL DE: {{nome.upper()}}")
    print("=" * 50)
    
    # Inicializar pontuação e critérios
    pontuacao = 0
    criterios_positivos = []
    criterios_negativos = []
    bonus = 0
    
    # === CRITÉRIO 1: IDADE ===
    if 22 <= idade <= 50:
        pontuacao += 25
        criterios_positivos.append("✅ Faixa etária ideal para a vaga")
    elif 18 <= idade <= 60:
        pontuacao += 15
        criterios_positivos.append("⚠️ Faixa etária aceitável")
    else:
        criterios_negativos.append("❌ Faixa etária fora do perfil")
    
    # === CRITÉRIO 2: EXPERIÊNCIA ===
    if experiencia >= 5:
        pontuacao += 30
        criterios_positivos.append("✅ Experiência sólida e comprovada")
        if experiencia >= 10:
            bonus += 10
            criterios_positivos.append("🌟 BÔNUS: Experiência excepcional!")
    elif experiencia >= 2:
        pontuacao += 20
        criterios_positivos.append("⚠️ Experiência adequada")
    elif experiencia >= 1:
        pontuacao += 10
        criterios_positivos.append("⚠️ Experiência limitada mas válida")
    else:
        criterios_negativos.append("❌ Falta de experiência na área")
    
    # === CRITÉRIO 3: FORMAÇÃO ===
    formacao_lower = formacao.lower()
    if "superior" in formacao_lower or "universitario" in formacao_lower:
        pontuacao += 25
        criterios_positivos.append("✅ Formação superior completa")
    elif "tecnico" in formacao_lower or "técnico" in formacao_lower:
        pontuacao += 15
        criterios_positivos.append("⚠️ Formação técnica adequada")
    elif "medio" in formacao_lower or "médio" in formacao_lower:
        pontuacao += 10
        criterios_positivos.append("⚠️ Ensino médio completo")
    else:
        criterios_negativos.append("❌ Formação não atende aos requisitos")
    
    # === CRITÉRIO 4: PERFORMANCE NO TESTE ===
    if nota_teste >= 9.0:
        pontuacao += 20
        criterios_positivos.append("✅ Performance excepcional no teste")
        bonus += 5
    elif nota_teste >= 7.0:
        pontuacao += 15
        criterios_positivos.append("✅ Boa performance no teste")
    elif nota_teste >= 5.0:
        pontuacao += 10
        criterios_positivos.append("⚠️ Performance aceitável no teste")
    else:
        criterios_negativos.append("❌ Performance insuficiente no teste")
    
    # === CRITÉRIOS BÔNUS ===
    if tem_certificacoes:
        bonus += 10
        criterios_positivos.append("🏆 BÔNUS: Possui certificações relevantes")
    
    if disponibilidade.lower() == "integral":
        bonus += 5
        criterios_positivos.append("⏰ BÔNUS: Disponibilidade integral")
    elif disponibilidade.lower() == "parcial":
        criterios_positivos.append("⚠️ Disponibilidade parcial")
    
    # === CÁLCULO FINAL ===
    pontuacao_final = pontuacao + bonus
    
    # === EXIBIR ANÁLISE DETALHADA ===
    print("\\n📊 ANÁLISE DETALHADA:")
    print("-" * 30)
    
    if criterios_positivos:
        print("\\n🟢 PONTOS POSITIVOS:")
        for criterio in criterios_positivos:
            print(f"  {criterio}")
    
    if criterios_negativos:
        print("\\n🔴 PONTOS DE ATENÇÃO:")
        for criterio in criterios_negativos:
            print(f"  {criterio}")
    
    print(f"\\n📈 PONTUAÇÃO BASE: {{pontuacao}}/100")
    if bonus > 0:
        print(f"🎁 BÔNUS ADICIONAIS: +{{bonus}} pontos")
    print(f"🏆 PONTUAÇÃO FINAL: {{pontuacao_final}}/110")
    
    # === DECISÃO INTELIGENTE ===
    print("\\n" + "="*50)
    if pontuacao_final >= 90:
        decisao = "APROVADO IMEDIATAMENTE"
        emoji = "🌟"
        recomendacao = "Candidato excepcional - Agendar entrevista URGENTE!"
    elif pontuacao_final >= 70:
        decisao = "APROVADO PARA PRÓXIMA FASE"
        emoji = "✅"
        recomendacao = "Bom candidato - Prosseguir com entrevista técnica"
    elif pontuacao_final >= 50:
        decisao = "EM ANÁLISE"
        emoji = "⚠️"
        recomendacao = "Candidato médio - Avaliar junto com outros perfis"
    elif pontuacao_final >= 30:
        decisao = "REPROVADO COM RESSALVAS"
        emoji = "❌"
        recomendacao = "Não atende agora - Reavaliar em 6 meses"
    else:
        decisao = "REPROVADO"
        emoji = "🚫"
        recomendacao = "Perfil não compatível com a vaga"
    
    print(f"{{emoji}} DECISÃO: {{decisao}}")
    print(f"💡 RECOMENDAÇÃO: {{recomendacao}}")
    
    return pontuacao_final, decisao

# === TESTANDO O SISTEMA ===
print("🏢 SISTEMA DE AVALIAÇÃO INTELIGENTE DE CANDIDATOS")
print("="*60)

# Candidato real do exemplo
resultado = avaliar_candidato(
    nome="{nome}",
    idade={idade},
    experiencia={experiencia},
    formacao="{formacao}",
    nota_teste={nota_teste},
    tem_certificacoes={tem_certificacoes},
    disponibilidade="{disponibilidade}"
)

print("\\n🎯 SISTEMA FUNCIONANDO PERFEITAMENTE!")
print("✨ Capaz de avaliar centenas de candidatos automaticamente!")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        print("🚀 Executando seu Avaliador Inteligente:")
        self.executar_codigo(codigo_final)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema de avaliação inteligente!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais critérios de avaliação (idiomas, localização, etc.)",
            "Implementar pesos diferentes para cada critério",
            "Criar relatórios comparativos entre candidatos",
            "Integrar com banco de dados para processar milhares de perfis",
            "Adicionar machine learning para aprender com contratações de sucesso"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre das Condições!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Avaliador Inteligente de Perfis")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo07Condicoes()
    print("Teste do módulo 7 - versão refatorada")
    module._condicoes_interativo()