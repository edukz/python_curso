#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 6: Operações Matemáticas
Aprenda sobre operadores aritméticos e cálculos em Python
"""

from ..shared.base_module import BaseModule


class Modulo06Operacoes(BaseModule):
    """Módulo 6: Operações Matemáticas"""
    
    def __init__(self):
        super().__init__("modulo_6", "Operações Matemáticas")
        self.has_mini_project = True
        self.mini_project_points = 65
    
    def execute(self) -> None:
        """Executa o módulo sobre operações matemáticas"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._operacoes_matematicas_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _operacoes_matematicas_interativo(self) -> None:
        """Conteúdo principal do módulo Operações Matemáticas"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧮 MÓDULO 6: OPERAÇÕES MATEMÁTICAS - A CALCULADORA PYTHON")
        else:
            print("\n" + "="*50)
            print("🧮 MÓDULO 6: OPERAÇÕES MATEMÁTICAS - A CALCULADORA PYTHON")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Chegou a hora de dominar a matemática com Python!")
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
            self._mini_projeto_calculadora_cientifica()
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
                'id': 'secao_o_que_sao_operacoes',
                'titulo': '🧮 O que são operações matemáticas?',
                'descricao': 'Entenda como o Python é uma super calculadora',
                'funcao': self._secao_o_que_sao_operacoes
            },
            {
                'id': 'secao_operadores_basicos',
                'titulo': '➕ Operadores básicos (+, -, *, /)',
                'descricao': 'Domine as operações fundamentais',
                'funcao': self._secao_operadores_basicos
            },
            {
                'id': 'secao_operadores_avancados',
                'titulo': '🚀 Operadores avançados (**, //, %)',
                'descricao': 'Descubra ferramentas poderosas para cálculos',
                'funcao': self._secao_operadores_avancados
            },
            {
                'id': 'secao_precedencia',
                'titulo': '🎯 Ordem de precedencia (PEMDAS)',
                'descricao': 'Aprenda qual conta é feita primeiro',
                'funcao': self._secao_precedencia
            },
            {
                'id': 'secao_calculos_praticos',
                'titulo': '📊 Cálculos práticos do dia a dia',
                'descricao': 'Resolva problemas reais com Python',
                'funcao': self._secao_calculos_praticos
            },
            {
                'id': 'secao_funcoes_matematicas',
                'titulo': '🧪 Funções matemáticas especiais',
                'descricao': 'Explore round(), abs(), min(), max()',
                'funcao': self._secao_funcoes_matematicas
            },
            {
                'id': 'secao_aplicacoes_reais',
                'titulo': '🌍 Aplicações no mundo real',
                'descricao': 'Veja onde a matemática é usada profissionalmente',
                'funcao': self._secao_aplicacoes_reais
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
    
    def _secao_o_que_sao_operacoes(self) -> None:
        """Seção: O que são operações matemáticas?"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧮 O QUE SÃO OPERAÇÕES MATEMÁTICAS?")

        self.print_colored("🧮 Imagine que você tem uma super calculadora na mão...", "info")
        self.print_colored("Mas esta calculadora é tão poderosa que pode fazer qualquer cálculo!", "cyan")
        
        self.print_section("\n🎯 O QUE SÃO OPERAÇÕES:")
        self.print_colored("Operações são comandos que dizem ao Python:", "yellow")
        self.print_colored("• 'Some estes números'", "yellow")
        self.print_colored("• 'Divida este valor'", "yellow")
        self.print_colored("• 'Calcule a potência'", "yellow")
        
        self.print_colored("\n💻 Em Python, você escreve matemática quase como no papel!", "info")
        self.print_colored("A diferença é que o Python executa na hora e mostra o resultado.", "green")
        
        self.print_section("\n🎯 COMPARANDO COM O MUNDO REAL:")
        
        codigo = '''# Matemática tradicional vs Python
print("📝 Na escola você escreve: 2 + 3 = ?")
print("💻 No Python você escreve: 2 + 3")
print(f"E o resultado é: {2 + 3}")

print("\n🧮 Vamos ver mais exemplos:")
print(f"10 - 4 = {10 - 4}")
print(f"5 * 6 = {5 * 6}")
print(f"15 / 3 = {15 / 3}")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_tip("\n💡 VANTAGEM: Python calcula tudo automaticamente!")
        
        self.print_colored("\n🎆 ONDE ISSO É USADO NA VIDA REAL:", "info")
        self.print_colored("🏦 Bancos: Calcular juros e parcelamentos", "green")
        self.print_colored("🛍️ E-commerce: Preços com desconto", "green")
        self.print_colored("🎮 Games: Sistema de pontuação", "green")
        self.print_colored("📈 Empresas: Relatórios financeiros", "green")
        
        self.pausar()

    def _secao_operadores_basicos(self) -> None:
        """Seção: Operadores básicos (+, -, *, /)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("➕ OPERADORES BÁSICOS")

        self.print_colored("➕ Os operadores básicos são como ferramentas universais...", "info")
        self.print_colored("Você vai usar eles o tempo todo, em qualquer programa!", "cyan")
        
        self.print_section("\n🎯 OS 4 OPERADORES ESSENCIAIS:")
        
        operadores = [
            ("+", "SOMA", "Junta valores", "2 + 3 = 5"),
            ("-", "SUBTRAÇÃO", "Retira valores", "10 - 4 = 6"),
            ("*", "MULTIPLICAÇÃO", "Repete valores", "3 * 4 = 12"),
            ("/", "DIVISÃO", "Divide valores", "15 / 3 = 5.0")
        ]
        
        for simbolo, nome, descricao, exemplo in operadores:
            self.print_colored(f"{simbolo} {nome}: {descricao}", "yellow")
            self.print_colored(f"   Exemplo: {exemplo}", "cyan")
            print()
        
        self.print_section("\n💻 EXEMPLOS PRÁTICOS:")
        
        codigo = '''# Operadores básicos em ação
# Vamos simular uma compra no mercado

preco_pao = 5.50
preco_leite = 4.20
preco_ovos = 8.90

print("=== COMPRAS NO MERCADO ===")
print(f"🍞 Pão: R$ {preco_pao}")
print(f"🥛 Leite: R$ {preco_leite}")
print(f"🥚 Ovos: R$ {preco_ovos}")

# Soma: total da compra
total = preco_pao + preco_leite + preco_ovos
print(f"\n➕ Total da compra: R$ {total:.2f}")

# Subtração: troco
dinheiro = 25.00
troco = dinheiro - total
print(f"➖ Troco: R$ {troco:.2f}")

# Multiplicação: comprar várias unidades
quantidade_paes = 3
total_paes = preco_pao * quantidade_paes
print(f"\n✖️ {quantidade_paes} pães: R$ {total_paes:.2f}")

# Divisão: dividir conta entre amigos
amigos = 2
valor_por_pessoa = total / amigos
print(f"➗ Dividindo entre {amigos} pessoas: R$ {valor_por_pessoa:.2f} cada")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_tip("\n💡 OBSERVE: Python respeita os tipos! 15 / 3 = 5.0 (float, não int)")
        
        self.print_colored("\n🎆 USOS PROFISSIONAIS:", "info")
        self.print_colored("💰 Sistemas de pagamento (soma, desconto)", "green")
        self.print_colored("📈 Planilhas inteligentes (cálculos automáticos)", "green")
        self.print_colored("🎮 Jogos (pontos, vida, dano)", "green")
        self.print_colored("📊 Análise de dados (médias, somatórios)", "green")
        
        self.pausar()

    def _secao_operadores_avancados(self) -> None:
        """Seção: Operadores avançados (**, //, %)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 OPERADORES AVANÇADOS")

        self.print_colored("🚀 Os operadores avançados são como ferramentas especiais...", "info")
        self.print_colored("Eles resolvem problemas que os básicos não conseguem!", "cyan")
        
        self.print_section("\n🎯 OS 3 OPERADORES ESPECIAIS:")
        
        operadores_avancados = [
            ("**", "POTÊNCIA", "Eleva à potência", "2 ** 3 = 8 (2 ao cubo)"),
            ("//", "DIVISÃO INTEIRA", "Divisão sem decimais", "10 // 3 = 3 (só a parte inteira)"),
            ("%", "RESTO (MÓDULO)", "Sobra da divisão", "10 % 3 = 1 (resto da divisão)")
        ]
        
        for simbolo, nome, descricao, exemplo in operadores_avancados:
            self.print_colored(f"{simbolo} {nome}: {descricao}", "yellow")
            self.print_colored(f"   Exemplo: {exemplo}", "cyan")
            print()
        
        self.print_section("\n🧪 POTÊNCIA (**) - O MAIS PODEROSO:")
        
        codigo_potencia = '''# Potência em ação
print("=== CALCULADORA DE POTÊNCIAS ===")

# Casos simples
print(f"2 ao quadrado: 2 ** 2 = {2 ** 2}")
print(f"3 ao cubo: 3 ** 3 = {3 ** 3}")
print(f"10 ao quadrado: 10 ** 2 = {10 ** 2}")

# Casos práticos
print("\n=== APLICAÇÕES PRÁTICAS ===")

# Juros compostos
capital = 1000
taxa = 1.05  # 5% ao mês
meses = 12
valor_final = capital * (taxa ** meses)
print(f"Investimento: R$ {capital} por {meses} meses a 5%")
print(f"Valor final: R$ {valor_final:.2f}")

# Área de um quadrado
lado = 5
area = lado ** 2
print(f"\nÁrea de quadrado {lado}x{lado}: {area} m²")'''
        
        self.exemplo(codigo_potencia)
        self.executar_codigo(codigo_potencia)
        
        self.print_section("\n🔢 DIVISÃO INTEIRA (//) - PARA QUANTIDADES:")
        
        codigo_divisao = '''# Divisão inteira - só números inteiros
print("=== DIVISÃO INTEIRA ===")

# Exemplo: Organizar pessoas em grupos
pessoas = 23
grupos_de = 5

# Quantos grupos completos?
grupos_completos = pessoas // grupos_de
print(f"{pessoas} pessoas em grupos de {grupos_de}")
print(f"Grupos completos: {grupos_completos}")

# Exemplo: Pacotes
chocolates = 47
chocolates_por_pacote = 6
pacotes = chocolates // chocolates_por_pacote
print(f"\n{chocolates} chocolates, {chocolates_por_pacote} por pacote")
print(f"Pacotes cheios: {pacotes}")

# Comparando com divisão normal
print(f"\nDivisão normal: {chocolates} / {chocolates_por_pacote} = {chocolates / chocolates_por_pacote}")
print(f"Divisão inteira: {chocolates} // {chocolates_por_pacote} = {chocolates // chocolates_por_pacote}")'''
        
        self.exemplo(codigo_divisao)
        self.executar_codigo(codigo_divisao)
        
        self.print_section("\n🔄 RESTO (%) - O DETETIVE DOS NÚMEROS:")
        
        codigo_resto = '''# Operador resto - encontra sobras
print("=== OPERADOR RESTO ===")

# Descobrir sobras
chocolates = 47
chocolates_por_pacote = 6
pacotes = chocolates // chocolates_por_pacote
sobra = chocolates % chocolates_por_pacote

print(f"{chocolates} chocolates em pacotes de {chocolates_por_pacote}")
print(f"Pacotes: {pacotes}")
print(f"Sobram: {sobra} chocolates")

# Verificar se é par ou ímpar
print("\n=== DETECTOR DE PARES E ÍMPARES ===")
numeros = [10, 15, 22, 7, 100]

for numero in numeros:
    resto = numero % 2
    if resto == 0:
        tipo = "PAR"
    else:
        tipo = "ÍMPAR"
    print(f"{numero} é {tipo} (resto por 2: {resto})")

# Dias da semana
print("\n=== CALENDÁRIO INTELIGENTE ===")
dia_hoje = 3  # 0=Dom, 1=Seg, 2=Ter, 3=Qua, 4=Qui, 5=Sex, 6=Sab
dias_nomes = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

print(f"Hoje é {dias_nomes[dia_hoje]}")
print(f"Em 10 dias será: {dias_nomes[(dia_hoje + 10) % 7]}")
print(f"Em 50 dias será: {dias_nomes[(dia_hoje + 50) % 7]}")'''
        
        self.exemplo(codigo_resto)
        self.executar_codigo(codigo_resto)
        
        self.print_tip("\n💡 DICA PRO: O operador % é usado para criar sistemas cíclicos!")
        
        self.print_colored("\n🎆 USOS PROFISSIONAIS:", "info")
        self.print_colored("📈 ** - Cálculos financeiros e científicos", "green")
        self.print_colored("📦 // - Distribuição de produtos e recursos", "green")
        self.print_colored("🔄 % - Sistemas de turno, paginação, criptografia", "green")
        
        self.pausar()

    def _secao_precedencia(self) -> None:
        """Seção: Ordem de precedência (PEMDAS)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 ORDEM DE PRECEDÊNCIA (PEMDAS)")

        self.print_colored("🎯 Quando há várias operações juntas, quem vai primeiro?", "info")
        self.print_colored("Python segue a mesma regra da matemática: PEMDAS!", "cyan")
        
        self.print_section("\n🏅 A REGRA PEMDAS:")
        self.print_colored("P - Parênteses () - SEMPRE primeiro", "yellow")
        self.print_colored("E - Expoentes ** - Potências", "yellow")
        self.print_colored("M - Multiplicação * - Da esquerda para direita", "yellow")
        self.print_colored("D - Divisão / - Da esquerda para direita", "yellow")
        self.print_colored("A - Adição + - Da esquerda para direita", "yellow")
        self.print_colored("S - Subtração - - Da esquerda para direita", "yellow")
        
        self.print_section("\n💻 EXEMPLOS PASSO A PASSO:")
        
        codigo_precedencia = '''# Demonstrando ordem de operações
print("=== ORDEM DE PRECEDÊNCIA ===")

# Exemplo 1: Sem parênteses
resultado1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado1}")
print("Passo a passo:")
print("1. Primeiro: 3 * 4 = 12")
print("2. Depois: 2 + 12 = 14")

# Exemplo 2: Com parênteses
resultado2 = (2 + 3) * 4
print(f"\n(2 + 3) * 4 = {resultado2}")
print("Passo a passo:")
print("1. Primeiro: (2 + 3) = 5")
print("2. Depois: 5 * 4 = 20")

# Exemplo 3: Complexo
resultado3 = 2 ** 3 + 4 * 5 - 6 / 2
print(f"\n2 ** 3 + 4 * 5 - 6 / 2 = {resultado3}")
print("Passo a passo:")
print("1. Potência: 2 ** 3 = 8")
print("2. Multiplicação: 4 * 5 = 20")
print("3. Divisão: 6 / 2 = 3.0")
print("4. Soma/Subtração: 8 + 20 - 3.0 = 25.0")'''
        
        self.exemplo(codigo_precedencia)
        self.executar_codigo(codigo_precedencia)
        
        self.print_section("\n🛍️ EXEMPLO PRÁTICO - CALCULADORA DE DESCONTO:")
        
        codigo_desconto = '''# Calculadora de desconto com precedência
print("=== CALCULADORA DE DESCONTO ===")

preco_original = 100
desconto_percentual = 20
taxa_entrega = 15

# JEITO ERRADO (sem parênteses)
calculo_errado = preco_original - desconto_percentual / 100 * preco_original + taxa_entrega
print(f"Cálculo ERRADO: {calculo_errado}")
print("Problema: Python fez 20/100 primeiro, depois multiplicou...")

# JEITO CERTO (com parênteses)
desconto_real = (desconto_percentual / 100) * preco_original
preco_com_desconto = preco_original - desconto_real
preco_final = preco_com_desconto + taxa_entrega

print(f"\nCálculo CORRETO:")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({desconto_percentual}%): R$ {desconto_real:.2f}")
print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
print(f"+ Taxa entrega: R$ {taxa_entrega:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# JEITO MAIS DIRETO (com parênteses)
preco_direto = preco_original * (1 - desconto_percentual/100) + taxa_entrega
print(f"\nCálculo direto: R$ {preco_direto:.2f}")'''
        
        self.exemplo(codigo_desconto)
        self.executar_codigo(codigo_desconto)
        
        self.print_tip("\n💡 DICA DE OURO: Na dúvida, use parênteses! Eles deixam seu código mais claro.")
        
        self.print_colored("\n🎆 POR QUE ISSO IMPORTA:", "info")
        self.print_colored("💰 Sistemas financeiros: Um erro de precedencia pode custar milhões", "green")
        self.print_colored("🎮 Games: HP, dano, bônus precisam ser calculados na ordem certa", "green")
        self.print_colored("📊 Relatórios: Médias, percentuais e totais devem estar corretos", "green")
        
        self.pausar()

    def _secao_calculos_praticos(self) -> None:
        """Seção: Cálculos práticos do dia a dia"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 CÁLCULOS PRÁTICOS DO DIA A DIA")

        self.print_colored("📊 Vamos resolver problemas reais que você encontra no dia a dia!", "info")
        self.print_colored("Estes exemplos mostram o poder da programação na vida prática.", "cyan")
        
        self.print_section("\n💰 PROBLEMA 1: DIVIDIR CONTA NO RESTAURANTE")
        
        codigo_restaurante = '''# Dividir conta no restaurante
print("=== CALCULADORA DE RESTAURANTE ===")

# Dados da conta
valor_conta = 120.50
gorjeta_percentual = 10
numero_pessoas = 4

# Cálculos
valor_gorjeta = valor_conta * (gorjeta_percentual / 100)
total_com_gorjeta = valor_conta + valor_gorjeta
valor_por_pessoa = total_com_gorjeta / numero_pessoas

print(f"Conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({gorjeta_percentual}%): R$ {valor_gorjeta:.2f}")
print(f"Total: R$ {total_com_gorjeta:.2f}")
print(f"Valor por pessoa ({numero_pessoas} pessoas): R$ {valor_por_pessoa:.2f}")

# Versão com diferentes gorjetas
print("\n=== SIMULAÇÃO DE GORJETAS ===")
for gorjeta in [5, 10, 15, 20]:
    total = valor_conta * (1 + gorjeta/100)
    por_pessoa = total / numero_pessoas
    print(f"Gorjeta {gorjeta}%: R$ {por_pessoa:.2f} por pessoa")'''
        
        self.exemplo(codigo_restaurante)
        self.executar_codigo(codigo_restaurante)
        
        self.print_section("\n🏠 PROBLEMA 2: CALCULADORA DE FINANCIAMENTO")
        
        codigo_financiamento = '''# Calculadora de financiamento
print("=== FINANCIAMENTO DE CASA ===")

valor_casa = 350000  # R$ 350 mil
entrada_percentual = 20  # 20% de entrada
parcelas = 360  # 30 anos (360 meses)
juros_anual = 8.5  # 8.5% ao ano

# Cálculos
valor_entrada = valor_casa * (entrada_percentual / 100)
valor_financiado = valor_casa - valor_entrada
juros_mensal = juros_anual / 12 / 100  # Converter para mensal e decimal

# Fórmula da prestação (simplificada)
# PMT = PV * (i * (1+i)^n) / ((1+i)^n - 1)
fator = (1 + juros_mensal) ** parcelas
prestacao = valor_financiado * (juros_mensal * fator) / (fator - 1)

total_pago = prestacao * parcelas
total_juros = total_pago - valor_financiado

print(f"Valor da casa: R$ {valor_casa:,.2f}")
print(f"Entrada ({entrada_percentual}%): R$ {valor_entrada:,.2f}")
print(f"Valor financiado: R$ {valor_financiado:,.2f}")
print(f"Prestação mensal: R$ {prestacao:,.2f}")
print(f"Total de juros: R$ {total_juros:,.2f}")
print(f"Total pago: R$ {(valor_entrada + total_pago):,.2f}")

print(f"\nCada prestação representará {(prestacao/8000)*100:.1f}% de um salário de R$ 8.000")'''
        
        self.exemplo(codigo_financiamento)
        self.executar_codigo(codigo_financiamento)
        
        self.print_section("\n⛽ PROBLEMA 3: CALCULADORA DE VIAGEM")
        
        codigo_viagem = '''# Calculadora de viagem
print("=== PLANEJADOR DE VIAGEM ===")

# Dados da viagem
distancia_km = 500  # São Paulo - Rio
consumo_carro = 12  # km por litro
preco_litro = 5.50
pedegio_total = 45.80
diarias_hotel = 3
preco_diaria = 180.00

# Cálculos de combustível
litros_necessarios = distancia_km / consummo_carro
custo_combustivel = litros_necessarios * preco_litro

# Cálculos totais
custo_hotel = diarias_hotel * preco_diaria
custo_total_viagem = custo_combustivel + custo_hotel + pedagio_total

print(f"Distância: {distancia_km} km")
print(f"Consumo: {consummo_carro} km/L")
print(f"Litros necessários: {litros_necessarios:.1f}L")
print(f"Custo combustível: R$ {custo_combustivel:.2f}")
print(f"Pedágio: R$ {pedagio_total:.2f}")
print(f"Hotel ({diarias_hotel} diárias): R$ {custo_hotel:.2f}")
print(f"\nTOTAL DA VIAGEM: R$ {custo_total_viagem:.2f}")

# Custo por pessoa
pessoas = 4
custo_por_pessoa = custo_total_viagem / pessoas
print(f"Custo por pessoa ({pessoas} pessoas): R$ {custo_por_pessoa:.2f}")'''
        
        # Fix the typo in the code before execution
        codigo_viagem_corrigido = codigo_viagem.replace('consummo_carro', 'consumo_carro').replace('pedagio_total', 'pedegio_total')
        
        self.exemplo(codigo_viagem)
        self.executar_codigo(codigo_viagem_corrigido)
        
        self.print_tip("\n💡 OBSERVOU? Programar é resolver problemas reais de forma automática!")
        
        self.print_colored("\n🎆 ONDE ESSAS HABILIDADES SÃO USADAS:", "info")
        self.print_colored("🏦 Bancos: Simulações de crédito e financiamento", "green")
        self.print_colored("📱 Apps: Calculadoras de corrida, delivery, viagem", "green")
        self.print_colored("🏢 Empresas: Planejamento orçamentário e de custos", "green")
        self.print_colored("🎯 Consultorias: Assessoria financeira personalizada", "green")
        
        self.pausar()

    def _secao_funcoes_matematicas(self) -> None:
        """Seção: Funções matemáticas especiais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧪 FUNÇÕES MATEMÁTICAS ESPECIAIS")

        self.print_colored("🧪 Python tem funções prontas para cálculos especiais!", "info")
        self.print_colored("São como ferramentas mágicas para problemas comuns.", "cyan")
        
        self.print_section("\n🎯 AS 5 FUNÇÕES MAIS ÚTEIS:")
        
        funcoes = [
            ("round()", "ARREDONDAR", "round(3.7) = 4"),
            ("abs()", "VALOR ABSOLUTO", "abs(-5) = 5"),
            ("min()", "MENOR VALOR", "min(1, 5, 3) = 1"),
            ("max()", "MAIOR VALOR", "max(1, 5, 3) = 5"),
            ("sum()", "SOMAR LISTA", "sum([1, 2, 3]) = 6")
        ]
        
        for funcao, nome, exemplo in funcoes:
            self.print_colored(f"{funcao} - {nome}: {exemplo}", "yellow")
        
        self.print_section("\n💻 EXEMPLOS PRÁTICOS:")
        
        codigo_funcoes = '''# Funções matemáticas em ação
print("=== FUNÇÕES MATEMÁTICAS ===")

# round() - Arredondar números
preco_bruto = 29.876
preco_bonito = round(preco_bruto, 2)  # 2 casas decimais
print(f"Preço bruto: R$ {preco_bruto}")
print(f"Preço arredondado: R$ {preco_bonito}")

# abs() - Valor absoluto (sempre positivo)
temperatura_ontem = -5
temperatura_hoje = 8
diferenca = abs(temperatura_hoje - temperatura_ontem)
print(f"\nTemperatura ontem: {temperatura_ontem}°C")
print(f"Temperatura hoje: {temperatura_hoje}°C")
print(f"Diferença: {diferenca}°C")

# min() e max() - Menor e maior
notas = [8.5, 7.2, 9.1, 6.8, 8.9]
menor_nota = min(notas)
maior_nota = max(notas)
media = sum(notas) / len(notas)

print(f"\nNotas: {notas}")
print(f"Menor nota: {menor_nota}")
print(f"Maior nota: {maior_nota}")
print(f"Média: {round(media, 2)}")

# sum() - Somar todos os valores
vendas_semana = [1200, 850, 1500, 900, 1800, 2100, 950]
total_vendas = sum(vendas_semana)
media_diaria = total_vendas / len(vendas_semana)

print(f"\nVendas da semana: {vendas_semana}")
print(f"Total: R$ {total_vendas:.2f}")
print(f"Média diária: R$ {round(media_diaria, 2)}")

# Encontrando extremos
melhor_dia = vendas_semana.index(max(vendas_semana)) + 1
pior_dia = vendas_semana.index(min(vendas_semana)) + 1
print(f"Melhor dia: {melhor_dia}º (R$ {max(vendas_semana)})")
print(f"Pior dia: {pior_dia}º (R$ {min(vendas_semana)})")'''
        
        self.exemplo(codigo_funcoes)
        self.executar_codigo(codigo_funcoes)
        
        self.print_section("\n📈 EXEMPLO AVANÇADO - ANÁLISE DE DADOS:")
        
        codigo_analise = '''# Análise estatística simples
print("=== ANÁLISE ESTATÍSTICA ===")

# Dados de vendas de 3 meses
vendas_janeiro = [15000, 18000, 12000, 16000]
vendas_fevereiro = [14000, 17000, 19000, 15000]
vendas_marco = [20000, 22000, 18000, 21000]

# Todas as vendas juntas
todas_vendas = vendas_janeiro + vendas_fevereiro + vendas_marco

# Estatísticas gerais
total_vendas = sum(todas_vendas)
media_geral = total_vendas / len(todas_vendas)
maior_venda = max(todas_vendas)
menor_venda = min(todas_vendas)
amplitude = maior_venda - menor_venda

print(f"Total de vendas: R$ {total_vendas:,.2f}")
print(f"Média geral: R$ {round(media_geral, 2):,.2f}")
print(f"Maior venda: R$ {maior_venda:,.2f}")
print(f"Menor venda: R$ {menor_venda:,.2f}")
print(f"Amplitude: R$ {amplitude:,.2f}")

# Análise por mês
print("\n=== ANÁLISE MENSAL ===")
meses = [
    ("Janeiro", vendas_janeiro),
    ("Fevereiro", vendas_fevereiro),
    ("Março", vendas_marco)
]

for nome_mes, vendas_mes in meses:
    total_mes = sum(vendas_mes)
    media_mes = total_mes / len(vendas_mes)
    crescimento = ((media_mes - media_geral) / media_geral) * 100
    
    print(f"{nome_mes}:")
    print(f"  Total: R$ {total_mes:,.2f}")
    print(f"  Média: R$ {round(media_mes, 2):,.2f}")
    print(f"  vs Média geral: {round(crescimento, 1)}%")
    print()'''
        
        self.exemplo(codigo_analise)
        self.executar_codigo(codigo_analise)
        
        self.print_tip("\n💡 DICA: Essas funções são os blocos básicos da análise de dados!")
        
        self.print_colored("\n🎆 APLICAÇÕES PROFISSIONAIS:", "info")
        self.print_colored("📈 Data Science: Base para análises estatísticas", "green")
        self.print_colored("💰 Finanças: Cálculos de risco e retorno", "green")
        self.print_colored("🎮 Games: Sistemas de pontos e ranking", "green")
        self.print_colored("🏢 Vendas: Relatórios e metas automáticas", "green")
        
        self.pausar()

    def _secao_aplicacoes_reais(self) -> None:
        """Seção: Aplicações no mundo real"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌍 APLICAÇÕES NO MUNDO REAL")

        self.print_colored("🌍 Vamos descobrir onde a matemática Python é usada no mundo!", "info")
        self.print_colored("Prepare-se para se surpreender com o que dá para fazer!", "cyan")
        
        self.print_section("\n🏦 1. SISTEMA BANCÁRIO - NUBANK")
        self.print_colored("Como o Nubank calcula tudo automaticamente:", "yellow")
        
        codigo_banco = '''# Sistema bancário simplificado
print("=== SISTEMA BANCÁRIO ===")

# Perfil do cliente
saldo = 2500.0
limite_cartao = 1500.0
renda_mensal = 4000.0
score = 750

# Cálculo automático de crédito
# Fórmula simplificada: (renda * score / 1000) + saldo
credito_disponivel = (renda_mensal * score / 1000) + saldo * 0.5
credito_aprovado = min(credito_disponivel, 10000)  # Limite máximo

# Análise de risco
percentual_renda = (credito_aprovado / renda_mensal) * 100
if percentual_renda <= 300:
    classificacao = "BAIXO RISCO"
elif percentual_renda <= 500:
    classificacao = "MÉDIO RISCO"
else:
    classificacao = "ALTO RISCO"

print(f"Cliente:")
print(f"  Saldo: R$ {saldo:,.2f}")
print(f"  Renda: R$ {renda_mensal:,.2f}")
print(f"  Score: {score}")
print(f"\nAnálise automática:")
print(f"  Crédito calculado: R$ {credito_disponivel:,.2f}")
print(f"  Crédito aprovado: R$ {credito_aprovado:,.2f}")
print(f"  Classificação: {classificacao}")

# Simulação de parcelamento
compra = 1200.0
print(f"\n=== SIMULAÇÃO DE PARCELAMENTO ===")
print(f"Compra: R$ {compra:.2f}")
for parcelas in [1, 3, 6, 12]:
    if parcelas == 1:
        juros = 0
        valor_parcela = compra
    else:
        juros = 2.5 * (parcelas - 1)  # 2.5% por mês adicional
        valor_total = compra * (1 + juros/100)
        valor_parcela = valor_total / parcelas
    
    print(f"{parcelas:2d}x: R$ {valor_parcela:6.2f} (total: R$ {valor_parcela * parcelas:,.2f})")'''
        
        self.exemplo(codigo_banco)
        self.executar_codigo(codigo_banco)
        
        self.print_section("\n🛍️ 2. E-COMMERCE - AMAZON/MERCADO LIVRE")
        self.print_colored("Como plataformas calculam preços, frete e recomendações:", "yellow")
        
        codigo_ecommerce = '''# Sistema de e-commerce
print("=== PLATAFORMA E-COMMERCE ===")

# Dados do produto
preco_base = 89.90
desconto_categoria = 15  # 15% off eletrônicos
frete_base = 12.50
distancia_km = 150
avaliacao_vendedor = 4.8

# Cálculo de preço dinâmico
preco_com_desconto = preco_base * (1 - desconto_categoria/100)

# Cálculo de frete dinâmico
frete_por_km = 0.08
frete_calculado = frete_base + (distancia_km * frete_por_km)

# Frete grátis para compras acima de R$ 80
if preco_com_desconto >= 80:
    frete_final = 0
    economia_frete = frete_calculado
else:
    frete_final = frete_calculado
    economia_frete = 0

# Pontuação do produto (algoritmo simplificado)
pontuacao_preco = max(0, 10 - (preco_com_desconto / 10))  # Quanto menor, melhor
pontuacao_frete = 10 if frete_final == 0 else max(0, 10 - frete_final)
pontuacao_vendedor = avaliacao_vendedor * 2
pontuacao_total = round((pontuacao_preco + pontuacao_frete + pontuacao_vendedor) / 3, 1)

print(f"Produto: Smartphone XYZ")
print(f"Preço base: R$ {preco_base:.2f}")
print(f"Desconto: {desconto_categoria}%")
print(f"Preço final: R$ {preco_com_desconto:.2f}")
print(f"\nFrete:")
print(f"  Distância: {distancia_km} km")
print(f"  Calculado: R$ {frete_calculado:.2f}")
print(f"  Final: R$ {frete_final:.2f}")
if economia_frete > 0:
    print(f"  🎉 Frete GRÁTIS! (economia: R$ {economia_frete:.2f})")

print(f"\nAnálise do algoritmo:")
print(f"  Vendedor: {avaliacao_vendedor}/5.0 estrelas")
print(f"  Pontuação total: {pontuacao_total}/10")
print(f"  Total da compra: R$ {preco_com_desconto + frete_final:.2f}")'''
        
        self.exemplo(codigo_ecommerce)
        self.executar_codigo(codigo_ecommerce)
        
        self.print_section("\n🎮 3. GAME DEVELOPMENT - SISTEMA DE PONTOS")
        self.print_colored("Como jogos calculam XP, nível e recompensas:", "yellow")
        
        codigo_game = '''# Sistema de jogo
print("=== RPG SISTEMA DE NÍVEL ===")

# Status do jogador
xp_atual = 8750
nivel_atual = 12
kills = 45
mortes = 8
tempo_jogo_horas = 25

# Cálculo de nível (XP necessário cresce exponencialmente)
xp_para_proximo = (nivel_atual + 1) ** 2 * 50
xp_faltando = xp_para_proximo - xp_atual
percentual_nivel = (xp_atual / xp_para_proximo) * 100

# Cálculo de KDA (Kill/Death/Assist ratio)
kda = kills / max(mortes, 1)  # Evitar divisão por zero

# Sistema de ranking
if kda >= 3.0:
    rank = "LENDA"
    multiplicador_xp = 1.5
elif kda >= 2.0:
    rank = "VETERANO"
    multiplicador_xp = 1.3
elif kda >= 1.5:
    rank = "EXPERIENTE"
    multiplicador_xp = 1.1
else:
    rank = "NOVATO"
    multiplicador_xp = 1.0

# Recompensa por tempo de jogo
bonus_tempo = min(tempo_jogo_horas * 10, 500)  # Máx 500 XP

# XP total da próxima partida (simulada)
xp_base_partida = 150
xp_partida = round(xp_base_partida * multiplicador_xp) + bonus_tempo

print(f"Jogador: DragonSlayer2024")
print(f"Nível: {nivel_atual}")
print(f"XP: {xp_atual:,} / {xp_para_proximo:,} ({percentual_nivel:.1f}%)")
print(f"XP faltando: {xp_faltando:,}")
print(f"\nEstatísticas:")
print(f"  Kills: {kills}")
print(f"  Mortes: {mortes}")
print(f"  KDA: {kda:.2f}")
print(f"  Rank: {rank}")
print(f"  Tempo: {tempo_jogo_horas}h")
print(f"\nPróxima partida:")
print(f"  XP base: {xp_base_partida}")
print(f"  Multiplicador: {multiplicador_xp}x")
print(f"  Bônus tempo: +{bonus_tempo}")
print(f"  Total XP: {xp_partida}")

# Simular se vai subir de nível
if xp_atual + xp_partida >= xp_para_proximo:
    print(f"  🎉 VAI SUBIR DE NÍVEL!")'''
        
        self.exemplo(codigo_game)
        self.executar_codigo(codigo_game)
        
        self.print_colored("\n🎆 O QUE VOCÊ ACABOU DE VER:", "info")
        self.print_colored("🧮 Fórmulas matemáticas controlam nossas vidas digitais!", "green")
        self.print_colored("💰 Cada compra, cada crédito, cada jogo usa esses cálculos", "green")
        self.print_colored("🚀 E agora VOCÊ sabe fazer isso também!", "green")
        
        self.print_tip("\n💡 INSPIRE-SE: Estes exemplos mostram como programadores criam produtos que milhões usam!")
        
        self.pausar()

    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")

        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")

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
                        self._exercicio_quiz_operacoes()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._exercicio_completar_codigo()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo"]:
                    try:
                        self._exercicio_criativo_calculadora()
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre operações matemáticas",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie sua calculadora personalizada",
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

    def _exercicio_quiz_operacoes(self) -> None:
        """Quiz sobre operações matemáticas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧠 QUIZ RÁPIDO - OPERAÇÕES")

        self.print_colored("🧠 Vamos testar seus conhecimentos com 5 perguntas!", "info")
        
        perguntas = [
            {
                'pergunta': 'Qual é o resultado de 2 ** 3?',
                'opcoes': ['A) 6', 'B) 8', 'C) 9', 'D) 5'],
                'resposta_correta': 'B',
                'explicacao': '2 ** 3 = 2 × 2 × 2 = 8. O operador ** calcula potências.'
            },
            {
                'pergunta': 'O que faz o operador % (módulo)?',
                'opcoes': ['A) Multiplicação', 'B) Percentual', 'C) Resto da divisão', 'D) Potência'],
                'resposta_correta': 'C',
                'explicacao': 'O operador % retorna o resto da divisão. Ex: 10 % 3 = 1.'
            },
            {
                'pergunta': 'Qual é o resultado de 10 // 3?',
                'opcoes': ['A) 3.33', 'B) 3', 'C) 4', 'D) 1'],
                'resposta_correta': 'B',
                'explicacao': 'O operador // faz divisão inteira, retornando apenas a parte inteira.'
            },
            {
                'pergunta': 'Na expressão 2 + 3 * 4, qual operação é feita primeiro?',
                'opcoes': ['A) 2 + 3', 'B) 3 * 4', 'C) Ambas simultaneamente', 'D) Depende'],
                'resposta_correta': 'B',
                'explicacao': 'Multiplicação tem precedência sobre adição (regra PEMDAS).'
            },
            {
                'pergunta': 'O que retorna abs(-15)?',
                'opcoes': ['A) -15', 'B) 15', 'C) 0', 'D) Erro'],
                'resposta_correta': 'B',
                'explicacao': 'abs() retorna o valor absoluto, sempre positivo. abs(-15) = 15.'
            }
        ]
        
        acertos = 0
        for i, pergunta in enumerate(perguntas, 1):
            self.print_section(f"📝 PERGUNTA {i}/5", "📝")
            self.print_colored(f"\n{pergunta['pergunta']}", "warning")
            print()
            for opcao in pergunta['opcoes']:
                self.print_colored(f"  {opcao}", "yellow")
            
            while True:
                resposta = input("\n🎯 Sua resposta (A, B, C ou D): ").upper().strip()
                if resposta in ['A', 'B', 'C', 'D']:
                    break
                self.print_warning("⚠️ Digite apenas A, B, C ou D")
            
            if resposta == pergunta['resposta_correta']:
                self.print_success(f"✅ CORRETO! {pergunta['explicacao']}")
                acertos += 1
            else:
                self.print_colored(f"❌ Incorreto. {pergunta['explicacao']}", "error")
            
            self.pausar()
        
        # Resultado final
        percentual = (acertos / len(perguntas)) * 100
        if percentual >= 80:
            self.print_success(f"\n🎆 EXCELENTE! Você acertou {acertos}/5 ({percentual:.0f}%)")
        elif percentual >= 60:
            self.print_colored(f"\n💪 BOM! Você acertou {acertos}/5 ({percentual:.0f}%)", "yellow")
        else:
            self.print_colored(f"\n📚 Continue estudando! Você acertou {acertos}/5 ({percentual:.0f}%)", "cyan")

    def _exercicio_completar_codigo(self) -> None:
        """Exercícios de completar código"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔧 COMPLETAR CÓDIGO - OPERAÇÕES")

        self.print_colored("🔧 Agora vamos completar trechos de código!", "info")
        self.print_tip("Vou mostrar código incompleto e você me diz o que está faltando.")
        
        exercicios = [
            {
                'titulo': 'Potência',
                'codigo_incompleto': '''base = 3
expoente = 4
resultado = base ______ expoente
print(f"{base} elevado a {expoente} = {resultado}")''',
                'resposta_correta': '**',
                'codigo_completo': '''base = 3
expoente = 4
resultado = base ** expoente
print(f"{base} elevado a {expoente} = {resultado}")''',
                'explicacao': 'Use ** para calcular potências em Python.'
            },
            {
                'titulo': 'Resto da divisão',
                'codigo_incompleto': '''numero = 17
divisor = 5
resto = numero ______ divisor
print(f"O resto de {numero} dividido por {divisor} é {resto}")''',
                'resposta_correta': '%',
                'codigo_completo': '''numero = 17
divisor = 5
resto = numero % divisor
print(f"O resto de {numero} dividido por {divisor} é {resto}")''',
                'explicacao': 'Use % para calcular o resto da divisão (módulo).'
            },
            {
                'titulo': 'Arredondamento',
                'codigo_incompleto': '''preco = 29.876
preco_arredondado = ______(preco, 2)
print(f"Preço: R$ {preco_arredondado}")''',
                'resposta_correta': 'round',
                'codigo_completo': '''preco = 29.876
preco_arredondado = round(preco, 2)
print(f"Preço: R$ {preco_arredondado}")''',
                'explicacao': 'Use round() para arredondar números.'
            }
        ]
        
        for i, exercicio in enumerate(exercicios, 1):
            self.print_section(f"📝 EXERCÍCIO {i}/3: {exercicio['titulo']}", "📝")
            self.print_colored("\nCódigo incompleto:", "warning")
            self.exemplo(exercicio['codigo_incompleto'])
            
            resposta = input("\n🎯 O que deve substituir os ______ ? ").strip()
            
            if resposta.lower() == exercicio['resposta_correta'].lower():
                self.print_success(f"✅ CORRETO! {exercicio['explicacao']}")
                self.print_colored("\nCódigo completo:", "success")
                self.exemplo(exercicio['codigo_completo'])
                self.executar_codigo(exercicio['codigo_completo'])
            else:
                self.print_colored(f"❌ Não foi dessa vez. A resposta era: {exercicio['resposta_correta']}", "error")
                self.print_colored(exercicio['explicacao'], "yellow")
                self.print_colored("\nCódigo correto:", "info")
                self.exemplo(exercicio['codigo_completo'])
            
            self.pausar()

    def _exercicio_criativo_calculadora(self) -> None:
        """Exercício criativo com operações"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎨 EXERCÍCIO CRIATIVO - CALCULADORA PESSOAL")

        self.print_colored("🎨 Vamos criar uma calculadora personalizada para VOCÊ!", "info")
        self.print_tip("Você vai criar cálculos úteis para seu dia a dia.")
        
        self.print_section("\n🎯 DESAFIO:")
        self.print_colored("Crie uma calculadora que resolva UM problema do seu dia:", "cyan")
        self.print_colored("• Dividir conta no restaurante", "yellow")
        self.print_colored("• Calcular desconto em compras", "yellow")
        self.print_colored("• Descobrir quantas horas faltam para algo", "yellow")
        self.print_colored("• Ou qualquer cálculo que você sempre faz!", "yellow")
        
        print("\n" + "-"*50)
        print("📝 Vamos criar juntos:")
        
        try:
            # Escolher tipo de calculadora
            print("\nEscolha o tipo de calculadora:")
            print("1. 🍽️ Divisor de conta")
            print("2. 💰 Calculadora de desconto")
            print("3. ⏰ Contador de tempo")
            print("4. 🎨 Criar minha própria")
            
            escolha = input("\n🎯 Sua escolha (1-4): ").strip()
            
            if escolha == "1":
                self._criar_divisor_conta()
            elif escolha == "2":
                self._criar_calculadora_desconto()
            elif escolha == "3":
                self._criar_contador_tempo()
            elif escolha == "4":
                self._criar_calculadora_personalizada()
            else:
                self.print_warning("Opção inválida! Vou criar uma calculadora básica para você.")
                self._criar_calculadora_basica()
                
        except KeyboardInterrupt:
            raise
        except Exception as e:
            self.print_error(f"❌ Erro no exercício: {e}")
            self.print_tip("Tudo bem! O importante é praticar.")
        
        self.pausar()

    def _criar_divisor_conta(self) -> None:
        """Criar divisor de conta personalizado"""
        self.print_colored("\n🍽️ Vamos criar seu divisor de conta personalizado!", "info")
        
        # Coletar dados
        try:
            valor_str = input("💰 Valor total da conta: R$ ").replace(',', '.')
            valor = float(valor_str) if valor_str else 100.0
            
            pessoas_str = input("👥 Número de pessoas: ").strip()
            pessoas = int(pessoas_str) if pessoas_str.isdigit() else 4
            
            gorjeta_str = input("🎆 Gorjeta (% ou deixe vazio para 10%): ").strip()
            gorjeta = float(gorjeta_str) if gorjeta_str else 10.0
            
        except:
            valor, pessoas, gorjeta = 100.0, 4, 10.0
        
        # Gerar código personalizado
        codigo_gerado = f'''# 🍽️ DIVISOR DE CONTA PERSONALIZADO
print("🍽️" * 20)
print("   SEU DIVISOR DE CONTA")
print("🍽️" * 20)

# Seus dados
valor_conta = {valor}
num_pessoas = {pessoas}
gorjeta_percent = {gorjeta}

# Cálculos automáticos
valor_gorjeta = valor_conta * (gorjeta_percent / 100)
total_com_gorjeta = valor_conta + valor_gorjeta
valor_por_pessoa = total_com_gorjeta / num_pessoas

# Resultado
print(f"Conta: R$ {{valor_conta:.2f}}")
print(f"Gorjeta ({{gorjeta_percent}}%): R$ {{valor_gorjeta:.2f}}")
print(f"Total: R$ {{total_com_gorjeta:.2f}}")
print(f"Por pessoa ({{num_pessoas}} pessoas): R$ {{valor_por_pessoa:.2f}}")

# Bônus: simular diferentes gorjetas
print("\n📈 SIMULAÇÃO DE GORJETAS:")
for g in [5, 10, 15, 20]:
    total = valor_conta * (1 + g/100) / num_pessoas
    print(f"{{g:2d}}%: R$ {{total:.2f}} por pessoa")

print("\n🍽️" * 20)'''
        
        self.print_colored("\n💻 Sua calculadora personalizada:", "info")
        self.exemplo(codigo_gerado)
        
        print("\n" + "="*50)
        print("🉺 EXECUTANDO SUA CALCULADORA:")
        print("="*50)
        
        exec(codigo_gerado.split('print("🍽️" * 20)')[1])
        
        self.print_success("\n🎉 Sua calculadora está pronta! Salve esse código para usar sempre!")

    def _criar_calculadora_desconto(self) -> None:
        """Criar calculadora de desconto"""
        self.print_colored("\n💰 Vamos criar sua calculadora de desconto!", "info")
        
        # Código exemplo
        codigo_desconto = '''# 💰 CALCULADORA DE DESCONTO INTELIGENTE
print("💰" * 25)
print("   CALCULADORA DE DESCONTO")
print("💰" * 25)

# Simulação com produto real
preco_original = 199.90
desconto_percentual = 30

# Cálculos
valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto
economia = valor_desconto

print(f"Produto: Smartphone XYZ")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Você economiza: R$ {economia:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# Comparador de descontos
print(f"\n📈 COMPARADOR DE DESCONTOS:")
for desc in [10, 20, 30, 40, 50]:
    preco_com_desc = preco_original * (1 - desc/100)
    economia_desc = preco_original - preco_com_desc
    print(f"{desc:2d}%: R$ {preco_com_desc:6.2f} (economia: R$ {economia_desc:.2f})")

print("\n💰" * 25)'''
        
        self.print_colored("\n💻 Calculadora de desconto inteligente:", "info")
        self.exemplo(codigo_desconto)
        self.executar_codigo(codigo_desconto)
        
        self.print_success("\n🎉 Perfeita para comparar ofertas em lojas!")

    def _criar_contador_tempo(self) -> None:
        """Criar contador de tempo"""
        self.print_colored("\n⏰ Vamos criar seu contador de tempo!", "info")
        
        codigo_tempo = '''# ⏰ CONTADOR DE TEMPO INTELIGENTE
print("⏰" * 25)
print("   CONTADOR DE TEMPO")
print("⏰" * 25)

# Exemplo: quanto tempo para o fim de semana?
hora_atual = 14  # 14h (2pm)
dia_atual = 2    # Terça-feira (0=Seg, 1=Ter, 2=Qua...)

# Cálculos
horas_restantes_hoje = 24 - hora_atual
dias_para_sexta = (4 - dia_atual) % 7  # Sexta é dia 4
horas_totais_para_sexta = dias_para_sexta * 24 + (18 - hora_atual)  # Até 18h da sexta

print(f"Agora são {hora_atual}h de uma Terça-feira")
print(f"Horas restantes hoje: {horas_restantes_hoje}h")
print(f"Dias para sexta: {dias_para_sexta}")
print(f"Horas até o fim do expediente (sexta 18h): {horas_totais_para_sexta}h")

# Converter para dias e horas
dias_completos = horas_totais_para_sexta // 24
horas_restantes = horas_totais_para_sexta % 24

print(f"\n🏁 Faltam {dias_completos} dias e {horas_restantes} horas!")

# Bônus: contador para eventos
eventos = [
    ("Fim de semana", 2 * 24),  # 2 dias
    ("Próximo feriado", 15 * 24),  # 15 dias
    ("Férias", 60 * 24)  # 60 dias
]

print(f"\n📅 EVENTOS IMPORTANTES:")
for evento, horas in eventos:
    dias = horas // 24
    print(f"{evento}: {dias} dias ({horas} horas)")

print("\n⏰" * 25)'''
        
        self.print_colored("\n💻 Contador de tempo inteligente:", "info")
        self.exemplo(codigo_tempo)
        self.executar_codigo(codigo_tempo)
        
        self.print_success("\n🎉 Ótimo para planejar eventos e metas!")

    def _criar_calculadora_personalizada(self) -> None:
        """Criar calculadora personalizada"""
        self.print_colored("\n🎨 Vamos criar algo único para você!", "info")
        
        # Exemplo genérico mas útil
        codigo_personalizado = '''# 🎨 SUA CALCULADORA PERSONALIZADA
print("🎨" * 25)
print("   CALCULADORA UNIVERSAL")
print("🎨" * 25)

# Exemplos de cálculos úteis
print("📈 CÁLCULOS ÚTEIS DO DIA A DIA:")

# 1. Velocidade média
distancia = 120  # km
tempo = 1.5      # horas
velocidade = distancia / tempo
print(f"\n1. Velocidade média: {velocidade:.1f} km/h")

# 2. Consumo de combustível
km_rodados = 400
litros_gastos = 35
consumo = km_rodados / litros_gastos
print(f"2. Consumo do carro: {consumo:.2f} km/L")

# 3. Índice de Massa Corporal (IMC)
peso = 70  # kg
altura = 1.75  # metros
imc = peso / (altura ** 2)
print(f"3. IMC: {imc:.1f}")

# 4. Juros simples
capital = 1000
taxa = 5  # % ao mês
meses = 12
juros = capital * (taxa / 100) * meses
total = capital + juros
print(f"4. Investimento: R$ {total:.2f} em {meses} meses")

# 5. Regra de 3 simples
# Se 3 pessoas comem 2 pizzas, quantas pizzas para 8 pessoas?
pessoas_base = 3
pizzas_base = 2
pessoas_nova = 8
pizzas_necessarias = (pessoas_nova * pizzas_base) / pessoas_base
print(f"5. Pizzas para {pessoas_nova} pessoas: {pizzas_necessarias:.1f}")

print(f"\n🏆 Você domina a matemática do dia a dia!")
print("🎨" * 25)'''
        
        self.print_colored("\n💻 Calculadora universal:", "info")
        self.exemplo(codigo_personalizado)
        self.executar_codigo(codigo_personalizado)
        
        self.print_success("\n🎉 Agora você tem uma caixa de ferramentas matemática!")

    def _criar_calculadora_basica(self) -> None:
        """Criar calculadora básica"""
        codigo_basico = '''# 🧮 CALCULADORA BÁSICA
print("🧮 OPERAÇÕES BÁSICAS")
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")'''
        
        self.executar_codigo(codigo_basico)

    def _mini_projeto_calculadora_cientifica(self) -> None:
        """Mini Projeto - Módulo 6: Calculadora Científica Multi-funcional"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CALCULADORA CIENTÍFICA PESSOAL")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CALCULADORA CIENTÍFICA PESSOAL")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar sua calculadora científica aplicando todas as operações que você aprendeu!")

        self.print_colored(
            "Calculadora Científica Multi-funcional",
            "info"
        )
        self.print_colored(
            "Um sistema completo que resolve problemas matemáticos do mundo real, desde cálculos básicos até análises financeiras e estatísticas",
            "text"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Engenheiros calculando estruturas e cargas",
            "Analistas financeiros avaliando investimentos",
            "Estudantes resolvendo problemas matemáticos",
            "Empresários analisando custos e lucros"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Definir funcionalidades
        self.print_section("PASSO 1: Definindo as Funcionalidades", "📝", "info")
        self.print_tip("Vamos criar uma calculadora com 5 módulos especializados")

        try:
            funcionalidades = [
                "🧮 Operações Básicas (+-*/)",
                "🚀 Operações Avançadas (**,//,%)",
                "📊 Análise Estatística (média, min, max)",
                "💰 Calculadora Financeira (juros, parcelas)",
                "🔢 Conversor de Unidades (temperatura, medidas)"
            ]
            
            print("\nFuncionalidades da sua calculadora:")
            for i, func in enumerate(funcionalidades, 1):
                self.print_colored(f"{i}. {func}", "yellow")
                
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Construir o sistema
        self.print_section("PASSO 2: Construindo o Sistema", "⚙️", "success")
        self.print_colored("Agora vamos programar cada módulo:", "text")

        # PASSO 3: Código final
        self.print_section("PASSO 3: Sua Calculadora Completa", "🎬", "warning")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")

        codigo_final = '''# 🧮 PROJETO: CALCULADORA CIENTÍFICA PESSOAL
# Módulo 6: Operações Matemáticas

def calculadora_cientifica():
    """Calculadora científica multi-funcional"""
    print("🧮" * 30)
    print("   CALCULADORA CIENTÍFICA PESSOAL")
    print("🧮" * 30)
    
    while True:
        # Menu principal
        print("\\n📋 ESCOLHA UMA OPERAÇÃO:")
        print("1. 🧮 Operações Básicas")
        print("2. 🚀 Operações Avançadas")
        print("3. 📊 Análise Estatística")
        print("4. 💰 Calculadora Financeira")
        print("5. 🔢 Conversor de Unidades")
        print("0. 🚪 Sair")
        
        try:
            opcao = input("\\n👉 Sua escolha: ")
            
            if opcao == "0":
                print("\\n👋 Obrigado por usar a Calculadora Científica!")
                break
            elif opcao == "1":
                operacoes_basicas()
            elif opcao == "2":
                operacoes_avancadas()
            elif opcao == "3":
                analise_estatistica()
            elif opcao == "4":
                calculadora_financeira()
            elif opcao == "5":
                conversor_unidades()
            else:
                print("❌ Opção inválida!")
                
        except KeyboardInterrupt:
            print("\\n\\n👋 Calculadora encerrada pelo usuário!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

def operacoes_basicas():
    """Módulo de operações básicas"""
    print("\\n🧮 OPERAÇÕES BÁSICAS")
    try:
        a = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        b = float(input("Digite o segundo número: "))
        
        if operador == "+":
            resultado = a + b
        elif operador == "-":
            resultado = a - b
        elif operador == "*":
            resultado = a * b
        elif operador == "/":
            if b != 0:
                resultado = a / b
            else:
                print("❌ Erro: Divisão por zero!")
                return
        else:
            print("❌ Operador inválido!")
            return
            
        print(f"\\n✅ Resultado: {a} {operador} {b} = {resultado}")
        
    except ValueError:
        print("❌ Erro: Digite apenas números!")

def operacoes_avancadas():
    """Módulo de operações avançadas"""
    print("\\n🚀 OPERAÇÕES AVANÇADAS")
    try:
        a = float(input("Digite a base: "))
        print("Operações disponíveis:")
        print("** - Potência")
        print("// - Divisão inteira")
        print("% - Resto da divisão")
        
        operador = input("Digite a operação: ")
        b = float(input("Digite o segundo número: "))
        
        if operador == "**":
            resultado = a ** b
        elif operador == "//":
            if b != 0:
                resultado = a // b
            else:
                print("❌ Erro: Divisão por zero!")
                return
        elif operador == "%":
            if b != 0:
                resultado = a % b
            else:
                print("❌ Erro: Divisão por zero!")
                return
        else:
            print("❌ Operador inválido!")
            return
            
        print(f"\\n✅ Resultado: {a} {operador} {b} = {resultado}")
        
    except ValueError:
        print("❌ Erro: Digite apenas números!")

def analise_estatistica():
    """Módulo de análise estatística"""
    print("\\n📊 ANÁLISE ESTATÍSTICA")
    try:
        numeros_str = input("Digite os números separados por espaço: ")
        numeros = [float(x) for x in numeros_str.split()]
        
        if not numeros:
            print("❌ Nenhum número fornecido!")
            return
            
        # Cálculos estatísticos
        soma = sum(numeros)
        media = soma / len(numeros)
        minimo = min(numeros)
        maximo = max(numeros)
        amplitude = maximo - minimo
        
        print(f"\\n📊 RESULTADOS:")
        print(f"Números analisados: {numeros}")
        print(f"Quantidade: {len(numeros)}")
        print(f"Soma: {soma}")
        print(f"Média: {media:.2f}")
        print(f"Menor: {minimo}")
        print(f"Maior: {maximo}")
        print(f"Amplitude: {amplitude}")
        
    except ValueError:
        print("❌ Erro: Digite apenas números válidos!")

def calculadora_financeira():
    """Módulo financeiro"""
    print("\\n💰 CALCULADORA FINANCEIRA")
    try:
        capital = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (% ao mês): "))
        periodo = int(input("Período (meses): "))
        
        # Juros simples
        juros_simples = capital * (taxa / 100) * periodo
        montante_simples = capital + juros_simples
        
        # Juros compostos
        montante_composto = capital * ((1 + taxa/100) ** periodo)
        juros_compostos = montante_composto - capital
        
        print(f"\\n💰 SIMULAÇÃO FINANCEIRA:")
        print(f"Capital inicial: R$ {capital:.2f}")
        print(f"Taxa: {taxa}% ao mês")
        print(f"Período: {periodo} meses")
        print(f"\\n📈 JUROS SIMPLES:")
        print(f"Juros: R$ {juros_simples:.2f}")
        print(f"Montante: R$ {montante_simples:.2f}")
        print(f"\\n📈 JUROS COMPOSTOS:")
        print(f"Juros: R$ {juros_compostos:.2f}")
        print(f"Montante: R$ {montante_composto:.2f}")
        print(f"\\n💡 Diferença: R$ {(montante_composto - montante_simples):.2f}")
        
    except ValueError:
        print("❌ Erro: Digite valores válidos!")

def conversor_unidades():
    """Módulo conversor"""
    print("\\n🔢 CONVERSOR DE UNIDADES")
    print("1. Celsius ↔ Fahrenheit")
    print("2. Metros ↔ Pés")
    print("3. Quilos ↔ Libras")
    
    try:
        opcao = input("Escolha a conversão: ")
        valor = float(input("Digite o valor: "))
        
        if opcao == "1":
            print("C - Celsius para Fahrenheit")
            print("F - Fahrenheit para Celsius")
            tipo = input("Tipo de conversão: ").upper()
            
            if tipo == "C":
                resultado = (valor * 9/5) + 32
                print(f"\\n🌡️ {valor}°C = {resultado:.1f}°F")
            elif tipo == "F":
                resultado = (valor - 32) * 5/9
                print(f"\\n🌡️ {valor}°F = {resultado:.1f}°C")
                
        elif opcao == "2":
            print("M - Metros para Pés")
            print("P - Pés para Metros")
            tipo = input("Tipo de conversão: ").upper()
            
            if tipo == "M":
                resultado = valor * 3.28084
                print(f"\\n📏 {valor}m = {resultado:.2f} pés")
            elif tipo == "P":
                resultado = valor / 3.28084
                print(f"\\n📏 {valor} pés = {resultado:.2f}m")
                
        elif opcao == "3":
            print("K - Quilos para Libras")
            print("L - Libras para Quilos")
            tipo = input("Tipo de conversão: ").upper()
            
            if tipo == "K":
                resultado = valor * 2.20462
                print(f"\\n⚖️ {valor}kg = {resultado:.2f} libras")
            elif tipo == "L":
                resultado = valor / 2.20462
                print(f"\\n⚖️ {valor} libras = {resultado:.2f}kg")
                
    except ValueError:
        print("❌ Erro: Digite valores válidos!")

# Executar a calculadora
calculadora_cientifica()'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        
        print("\n🚀 Vamos testar sua calculadora com alguns exemplos:")
        
        # Demonstração das funcionalidades
        exemplos_codigo = '''
# Demonstração da Calculadora Científica
print("🧮" * 30)
print("   CALCULADORA CIENTÍFICA - DEMONSTRAÇÃO")
print("🧮" * 30)

# Teste de operações básicas
print("\\n🧮 OPERAÇÕES BÁSICAS:")
print(f"10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"10 * 5 = {10 * 5}")
print(f"10 / 5 = {10 / 5}")

# Teste de operações avançadas
print("\\n🚀 OPERAÇÕES AVANÇADAS:")
print(f"2 ** 8 = {2 ** 8} (2 elevado à 8ª potência)")
print(f"17 // 5 = {17 // 5} (divisão inteira)")
print(f"17 % 5 = {17 % 5} (resto da divisão)")

# Teste de análise estatística
print("\\n📊 ANÁLISE ESTATÍSTICA:")
numeros = [85, 92, 78, 96, 88, 91, 79, 94]
print(f"Notas: {numeros}")
print(f"Média: {sum(numeros)/len(numeros):.1f}")
print(f"Maior nota: {max(numeros)}")
print(f"Menor nota: {min(numeros)}")

# Teste financeiro
print("\\n💰 SIMULAÇÃO FINANCEIRA:")
capital = 1000
taxa = 2  # 2% ao mês
meses = 12
juros_compostos = capital * ((1 + taxa/100) ** meses) - capital
print(f"Investindo R$ {capital} a {taxa}% por {meses} meses")
print(f"Juros ganhos: R$ {juros_compostos:.2f}")
print(f"Montante final: R$ {capital + juros_compostos:.2f}")

# Teste de conversão
print("\\n🔢 CONVERSÕES ÚTEIS:")
print(f"25°C = {(25 * 9/5) + 32}°F")
print(f"100 metros = {100 * 3.28084:.1f} pés")
print(f"70 kg = {70 * 2.20462:.1f} libras")

print("\\n🎉 Sua calculadora está funcionando perfeitamente!")
print("🧮" * 30)
'''
        
        self.executar_codigo(exemplos_codigo)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou sua Calculadora Científica Pessoal!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais funções matemáticas (trigonometria, logaritmos)",
            "Criar interface gráfica com botões clicáveis",
            "Salvar histórico de cálculos em arquivo",
            "Integrar com planilhas Excel para análise de dados"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre das Operações Matemáticas!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Calculadora Científica Multi-funcional")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo06Operacoes()
    print("Teste do módulo 6 - versão standalone")
    module._operacoes_matematicas_interativo()