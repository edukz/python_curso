#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 10: Funções
Aprenda a criar e usar funções reutilizáveis em Python
"""

from ..shared.base_module import BaseModule


class Modulo10Funcoes(BaseModule):
    """Módulo 10: Dominando Funções e Reutilização de Código"""
    
    def __init__(self):
        super().__init__("modulo_10", "Funções e Reutilização")
        self.has_mini_project = True
        self.mini_project_points = 70
    
    def execute(self) -> None:
        """Executa o módulo Funções e Reutilização"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._funcoes_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _funcoes_interativo(self) -> None:
        """Conteúdo principal do módulo Funções e Reutilização"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚙️ MÓDULO 10: DOMINANDO FUNÇÕES E REUTILIZAÇÃO DE CÓDIGO")
        else:
            print("\n" + "="*50)
            print("⚙️ MÓDULO 10: DOMINANDO FUNÇÕES E REUTILIZAÇÃO DE CÓDIGO")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos aprender a criar código reutilizável como profissionais!")
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
            self._mini_projeto_conversor_universal()
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
                'id': 'secao_conceito_funcoes',
                'titulo': '🎯 O que são funções na programação?',
                'descricao': 'Entenda o poder de reutilizar código inteligentemente',
                'funcao': self._secao_conceito_funcoes
            },
            {
                'id': 'secao_criando_funcoes',
                'titulo': '⚙️ Como criar suas próprias funções?',
                'descricao': 'Domine a sintaxe def e aprenda a definir funções',
                'funcao': self._secao_criando_funcoes
            },
            {
                'id': 'secao_parametros_argumentos',
                'titulo': '🔧 Parâmetros e argumentos',
                'descricao': 'Envie dados para suas funções e receba resultados',
                'funcao': self._secao_parametros_argumentos
            },
            {
                'id': 'secao_valores_retorno',
                'titulo': '🔄 Return: devolvendo valores',
                'descricao': 'Aprenda como funções retornam resultados',
                'funcao': self._secao_valores_retorno
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Funções em ação - Exemplos práticos',
                'descricao': 'Veja funções resolvendo problemas reais',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 Onde usar funções na vida real?',
                'descricao': 'Aplicações práticas de funções em projetos',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas com funções',
                'descricao': 'Dicas de profissionais para código limpo',
                'funcao': self._secao_melhores_praticas
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
    
    def _secao_conceito_funcoes(self) -> None:
        """Seção: O que são funções na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO FUNÇÕES NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Função",
            "Um bloco de código reutilizável que executa uma tarefa específica quando chamado"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Funções evitam repetição de código - escreva uma vez, use mil vezes!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma máquina de lavar roupa: você coloca roupas sujas (entrada), "
                          "ela executa o processo de lavagem (função), e retorna roupas limpas (saída). "
                          "Toda vez que você precisar lavar roupas, usa a mesma máquina!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 📝 Você define a função uma vez com 'def nome_funcao():'",
            "2. 💻 Escreve o código que deve ser executado dentro da função",
            "3. 📞 Chama a função quantas vezes precisar: nome_funcao()",
            "4. 🔄 A função executa e pode retornar um resultado"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Exemplo simples de função
def saudar():
    print("Olá! Bem-vindo ao mundo das funções!")

# Chamando a função
saudar()  # Executa a função
saudar()  # Executa novamente
saudar()  # E mais uma vez!'''
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Facebook - funções para enviar mensagens, curtir posts",
            "Netflix - funções para buscar filmes, reproduzir vídeos",
            "WhatsApp - funções para enviar, receber, criptografar mensagens",
            "Games - funções para movimento, ataque, pontuação"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_criando_funcoes(self) -> None:
        """Seção: Como criar suas próprias funções?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO CRIAR SUAS PRÓPRIAS FUNÇÕES?", "⚙️", "success")
        
        # === SINTAXE BÁSICA ===
        self.print_concept(
            "Sintaxe def",
            "A palavra 'def' (definir) é usada para criar funções em Python"
        )
        
        self.print_colored("\n📋 ESTRUTURA BÁSICA:", "info")
        estrutura = '''def nome_da_funcao():
    """Documentação da função (opcional)"""
    # Código que a função vai executar
    print("Fazendo algo útil!")'''
        self.exemplo(estrutura)
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💡 VAMOS CRIAR NOSSA PRIMEIRA FUNÇÃO:", "warning")
        exemplo_criacao = '''# Criando uma função para calcular idade
def calcular_idade_em_dias():
    """Calcula quantos dias uma pessoa de 25 anos viveu"""
    idade_anos = 25
    dias_por_ano = 365
    total_dias = idade_anos * dias_por_ano
    print(f"Uma pessoa de {idade_anos} anos viveu aproximadamente {total_dias} dias!")
    
# Chamando nossa função
print("Executando nossa função personalizada:")
calcular_idade_em_dias()'''
        
        self.exemplo(exemplo_criacao)
        print("\n🚀 Executando:")
        self.executar_codigo(exemplo_criacao)
        
        # === MÚLTIPLAS FUNÇÕES ===
        self.print_colored("\n🎯 CRIANDO MÚLTIPLAS FUNÇÕES:", "accent")
        multiplas_funcoes = '''# Várias funções trabalhando juntas
def mostrar_separador():
    print("=" * 40)
    
def cumprimentar():
    print("Olá! Como você está hoje?")
    
def despedir():
    print("Tchau! Até a próxima!")

# Usando todas as funções
mostrar_separador()
cumprimentar()
mostrar_separador()
despedir()
mostrar_separador()'''
        
        self.exemplo(multiplas_funcoes)
        print("\n🚀 Executando todas as funções:")
        self.executar_codigo(multiplas_funcoes)
        
        self.print_success("\n🎉 Agora você sabe criar suas próprias funções!")
        self.pausar()
    
    def _secao_parametros_argumentos(self) -> None:
        """Seção: Parâmetros e argumentos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PARÂMETROS E ARGUMENTOS", "🔧", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Parâmetros",
            "Variáveis que permitem enviar informações para dentro da função"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA SIMPLES:", "warning")
        self.print_colored("É como uma receita de bolo: os ingredientes (parâmetros) podem variar, "
                          "mas o processo (função) continua o mesmo. Chocolate ou morango, ainda é bolo!", "text")
        input("\n🔸 Pressione ENTER para ver exemplos...")
        
        # === FUNÇÃO COM PARÂMETROS ===
        self.print_colored("\n💻 FUNÇÃO SEM PARÂMETROS (limitada):", "error")
        sem_parametros = '''def saudar_joao():
    print("Olá, João! Como vai?")
    
saudar_joao()  # Só funciona para João'''
        self.exemplo(sem_parametros)
        self.executar_codigo(sem_parametros)
        
        self.print_colored("\n💻 FUNÇÃO COM PARÂMETROS (flexível):", "success")
        com_parametros = '''def saudar_pessoa(nome):
    print(f"Olá, {nome}! Como vai?")
    
# Agora funciona para qualquer pessoa!
saudar_pessoa("João")
saudar_pessoa("Maria")
saudar_pessoa("Pedro")'''
        self.exemplo(com_parametros)
        self.executar_codigo(com_parametros)
        
        # === MÚLTIPLOS PARÂMETROS ===
        self.print_colored("\n🎯 MÚLTIPLOS PARÂMETROS:", "accent")
        multiplos_parametros = '''def apresentar_pessoa(nome, idade, cidade):
    print(f"Esta é {nome}, tem {idade} anos e mora em {cidade}")
    
# Chamando com diferentes argumentos
apresentar_pessoa("Ana", 28, "São Paulo")
apresentar_pessoa("Carlos", 35, "Rio de Janeiro")
apresentar_pessoa("Lucia", 42, "Belo Horizonte")'''
        self.exemplo(multiplos_parametros)
        self.executar_codigo(multiplos_parametros)
        
        # === PARÂMETROS PADRÃO ===
        self.print_colored("\n⭐ PARÂMETROS COM VALORES PADRÃO:", "warning")
        parametros_padrao = '''def criar_perfil(nome, idade=25, profissao="Estudante"):
    print(f"Perfil: {nome}, {idade} anos, {profissao}")
    
# Usando valores padrão
criar_perfil("João")  # idade=25, profissao="Estudante"

# Personalizando alguns valores
criar_perfil("Maria", 30)  # profissao="Estudante"

# Personalizando todos
criar_perfil("Pedro", 35, "Engenheiro")'''
        self.exemplo(parametros_padrao)
        self.executar_codigo(parametros_padrao)
        
        self.print_tip("Parâmetros padrão tornam suas funções mais flexíveis e fáceis de usar!")
        self.pausar()
    
    def _secao_valores_retorno(self) -> None:
        """Seção: Return - devolvendo valores"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("RETURN: DEVOLVENDO VALORES", "🔄", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Return",
            "Comando que faz a função devolver um resultado que pode ser usado em outros lugares"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO CAIXA ELETRÔNICO:", "warning")
        self.print_colored("Você insere o cartão e digita a senha (parâmetros), o caixa processa "
                          "(função executa) e retorna o dinheiro (return). Você pode usar esse "
                          "dinheiro para comprar coisas!", "text")
        input("\n🔸 Pressione ENTER para ver a diferença...")
        
        # === SEM RETURN ===
        self.print_colored("\n❌ FUNÇÃO SEM RETURN (só mostra):", "error")
        sem_return = '''def calcular_quadrado_sem_return(numero):
    resultado = numero * numero
    print(f"O quadrado de {numero} é {resultado}")
    # Não retorna nada - não pode reutilizar o resultado
    
calcular_quadrado_sem_return(5)
# O resultado 25 se perdeu! Não posso usar em cálculos'''
        self.exemplo(sem_return)
        self.executar_codigo(sem_return)
        
        # === COM RETURN ===
        self.print_colored("\n✅ FUNÇÃO COM RETURN (devolver para usar):", "success")
        com_return = '''def calcular_quadrado_com_return(numero):
    resultado = numero * numero
    return resultado  # Retorna o valor para ser usado
    
# Agora posso usar o resultado!
quadrado_5 = calcular_quadrado_com_return(5)
print(f"Guardei o resultado: {quadrado_5}")

# Posso usar em outros cálculos
dobro_do_quadrado = quadrado_5 * 2
print(f"Dobro do quadrado: {dobro_do_quadrado}")'''
        self.exemplo(com_return)
        self.executar_codigo(com_return)
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n🎯 EXEMPLO PRÁTICO - CALCULADORA:", "accent")
        calculadora = '''def somar(a, b):
    return a + b
    
def multiplicar(a, b):
    return a * b
    
def calcular_area_retangulo(largura, altura):
    area = multiplicar(largura, altura)
    return area

# Usando as funções juntas
comprimento = 8
largura = 5

area = calcular_area_retangulo(comprimento, largura)
perimetro = somar(comprimento + largura, comprimento + largura)

print(f"Retângulo {comprimento}x{largura}:")
print(f"Área: {area} m²")
print(f"Perímetro: {perimetro} m")'''
        self.exemplo(calculadora)
        self.executar_codigo(calculadora)
        
        self.print_success("\n🎉 Com return você pode encadear funções e criar programas poderosos!")
        self.pausar()
    
    def _secao_exemplos_praticos(self) -> None:
        """Seção: Funções em ação - Exemplos práticos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FUNÇÕES EM AÇÃO - EXEMPLOS PRÁTICOS", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Validador de Email',
                'descricao': 'Função que verifica se um email é válido',
                'codigo': '''def validar_email(email):
    """Verifica se um email tem formato básico válido"""
    if "@" in email and "." in email:
        return True
    else:
        return False

# Testando a validação
emails = ["user@example.com", "email_invalido", "test@gmail.com"]

for email in emails:
    if validar_email(email):
        print(f"✅ {email} é válido")
    else:
        print(f"❌ {email} é inválido")''',
                'explicacao': 'Esta função verifica se há @ e . no email, retornando True ou False'
            },
            {
                'titulo': 'EXEMPLO 2: Calculadora de Desconto',
                'descricao': 'Função para calcular preços com desconto',
                'codigo': '''def calcular_desconto(preco_original, percentual_desconto):
    """Calcula o preço final após aplicar desconto"""
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final

# Simulando compras com desconto
produtos = [
    ("Notebook", 2500, 15),  # produto, preço, desconto%
    ("Mouse", 80, 10),
    ("Teclado", 150, 20)
]

print("🛒 CALCULADORA DE DESCONTOS:")
for produto, preco, desconto in produtos:
    preco_final = calcular_desconto(preco, desconto)
    print(f"{produto}: R${preco} → R${preco_final:.2f} ({desconto}% off)")''',
                'explicacao': 'Calcula desconto em porcentagem e retorna o preço final'
            },
            {
                'titulo': 'EXEMPLO 3: Gerador de Senhas',
                'descricao': 'Função que cria senhas aleatórias seguras',
                'codigo': '''import random
import string

def gerar_senha(tamanho=8):
    """Gera uma senha aleatória com letras e números"""
    caracteres = string.ascii_letters + string.digits
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

# Gerando diferentes senhas
print("🔐 GERADOR DE SENHAS:")
print(f"Senha curta (6 chars): {gerar_senha(6)}")
print(f"Senha média (8 chars): {gerar_senha()}")
print(f"Senha longa (12 chars): {gerar_senha(12)}")''',
                'explicacao': 'Combina letras e números aleatoriamente para criar senhas seguras'
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
        
        self.print_success("\n🎉 Agora você viu funções resolvendo problemas reais!")
        self.pausar()
    
    def _secao_casos_uso(self) -> None:
        """Seção: Onde usar funções na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR FUNÇÕES NA VIDA REAL?", "🌍", "accent")
        
        # === APLICAÇÕES POR ÁREA ===
        areas = [
            {
                'area': '🎮 JOGOS',
                'funcoes': [
                    'movimentar_personagem() - move jogador na tela',
                    'verificar_colisao() - detecta se objetos se tocaram',
                    'calcular_pontuacao() - atualiza score do jogador',
                    'gerar_inimigo() - cria novos inimigos no jogo'
                ]
            },
            {
                'area': '🛒 E-COMMERCE',
                'funcoes': [
                    'calcular_frete() - determina custo de entrega',
                    'aplicar_cupom() - aplica desconto no carrinho',
                    'verificar_estoque() - checa disponibilidade',
                    'processar_pagamento() - realiza transação'
                ]
            },
            {
                'area': '📱 REDES SOCIAIS',
                'funcoes': [
                    'publicar_post() - compartilha conteúdo',
                    'curtir_post() - adiciona like',
                    'enviar_notificacao() - alerta usuários',
                    'filtrar_feed() - personaliza timeline'
                ]
            },
            {
                'area': '🏦 SISTEMA BANCÁRIO',
                'funcoes': [
                    'verificar_saldo() - consulta conta',
                    'transferir_dinheiro() - move valores',
                    'calcular_juros() - determina rendimentos',
                    'validar_senha() - autentica usuário'
                ]
            }
        ]
        
        for area_info in areas:
            self.print_colored(f"\n{area_info['area']}", "warning")
            for funcao in area_info['funcoes']:
                self.print_colored(f"  • {funcao}", "text")
            input("\n🔸 Pressione ENTER para próxima área...")
        
        # === VANTAGENS DAS FUNÇÕES ===
        self.print_colored("\n⭐ POR QUE USAR FUNÇÕES?", "success")
        vantagens = [
            "🔄 Reutilização: Escreva uma vez, use mil vezes",
            "🧹 Organização: Código mais limpo e estruturado",
            "🐛 Depuração: Mais fácil encontrar e corrigir erros",
            "👥 Colaboração: Equipes podem trabalhar em funções separadas",
            "⚡ Eficiência: Desenvolvimento mais rápido"
        ]
        
        for vantagem in vantagens:
            self.print_colored(f"  {vantagem}", "primary")
        
        self.print_tip("Grandes empresas como Google, Facebook e Netflix usam milhões de funções!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas com funções"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS COM FUNÇÕES", "⭐", "warning")
        
        # === NOMES DESCRITIVOS ===
        self.print_colored("\n📝 1. USE NOMES DESCRITIVOS:", "success")
        nomes_exemplo = '''# ❌ Ruim - nomes confusos
def calc(x, y):
    return x * y

def proc(data):
    return data.upper()

# ✅ Bom - nomes claros
def calcular_area_retangulo(largura, altura):
    return largura * altura

def converter_para_maiuscula(texto):
    return texto.upper()'''
        self.exemplo(nomes_exemplo)
        
        # === FUNÇÕES PEQUENAS ===
        self.print_colored("\n🎯 2. MANTENHA FUNÇÕES PEQUENAS:", "info")
        funcoes_pequenas = '''# ✅ Função focada em uma tarefa
def validar_cpf(cpf):
    """Valida formato básico de CPF"""
    return len(cpf) == 11 and cpf.isdigit()

# ✅ Outra função para tarefa específica  
def formatar_cpf(cpf):
    """Formata CPF com pontos e traço"""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"'''
        self.exemplo(funcoes_pequenas)
        
        # === DOCUMENTAÇÃO ===
        self.print_colored("\n📚 3. DOCUMENTE SUAS FUNÇÕES:", "accent")
        documentacao_exemplo = '''def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    
    Args:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
    
    Returns:
        float: Valor do IMC calculado
    """
    return peso / (altura ** 2)'''
        self.exemplo(documentacao_exemplo)
        
        # === VALORES PADRÃO ===
        self.print_colored("\n⚙️ 4. USE VALORES PADRÃO INTELIGENTES:", "warning")
        valores_padrao = '''# ✅ Valores padrão úteis
def enviar_email(destinatario, assunto, corpo, copia_oculta=False):
    """Envia email com opções flexíveis"""
    print(f"Enviando para: {destinatario}")
    print(f"Assunto: {assunto}")
    if copia_oculta:
        print("Com cópia oculta ativada")

# Uso simples
enviar_email("user@example.com", "Teste", "Mensagem")

# Uso avançado
enviar_email("user@example.com", "Confidencial", "Dados", True)'''
        self.exemplo(valores_padrao)
        self.executar_codigo(valores_padrao)
        
        # === DICAS FINAIS ===
        self.print_colored("\n💡 DICAS DE OURO:", "success")
        dicas = [
            "🎯 Uma função = uma responsabilidade",
            "📏 Máximo 20 linhas por função (idealmente menos)",
            "🔤 Use verbos nos nomes: calcular, enviar, verificar",
            "⚡ Teste suas funções com dados diferentes",
            "🧹 Evite variáveis globais dentro de funções"
        ]
        
        for dica in dicas:
            self.print_colored(f"  {dica}", "primary")
        
        self.print_success("\n🏆 Seguindo essas práticas, você escreverá código profissional!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre funções com exercícios práticos!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Funções',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual palavra-chave é usada para criar funções em Python?',
                        'answer': ['def', 'define'],
                        'hint': 'É uma palavra de 3 letras que significa "definir"'
                    },
                    {
                        'question': 'O que a palavra "return" faz em uma função?',
                        'answer': ['retorna um valor', 'devolve resultado', 'retorna'],
                        'hint': 'Pense em "devolver" ou "entregar" um resultado'
                    },
                    {
                        'question': 'Como você chama uma função chamada "saudar"?',
                        'answer': ['saudar()', 'saudar ( )', 'saudar( )'],
                        'hint': 'Nome da função seguido de parênteses'
                    },
                    {
                        'question': 'Qual a principal vantagem de usar funções?',
                        'answer': ['reutilização', 'reutilizar código', 'evitar repetição'],
                        'hint': 'Escrever uma vez e usar várias vezes'
                    },
                    {
                        'question': 'O que são os valores dentro dos parênteses da função?',
                        'answer': ['parâmetros', 'argumentos', 'parametros'],
                        'hint': 'São as "entradas" que você fornece para a função'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a função que saúda uma pessoa',
                        'starter': '''def saudar(nome):
    # Complete aqui
    return ___

print(saudar("Ana"))''',
                        'solution': 'return f"Olá, {nome}!"',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a função que calcula área do círculo',
                        'starter': '''def calcular_area_circulo(raio):
    pi = 3.14159
    # Complete aqui (área = pi * raio²)
    return ___

print(f"Área: {calcular_area_circulo(5)}")''',
                        'solution': 'return pi * raio * raio',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a função que verifica se número é par ou ímpar',
                        'starter': '''def verificar_par_impar(numero):
    # Complete aqui
    if ___:
        return "par"
    else:
        return "ímpar"

print(f"8 é {verificar_par_impar(8)}")
print(f"7 é {verificar_par_impar(7)}")''',
                        'solution': 'numero % 2 == 0',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sua Própria Calculadora',
                'type': 'creative',
                'instruction': 'Crie uma função que faça um cálculo interessante de sua escolha! '
                             'Pode ser conversão de temperatura, cálculo de gorjeta, idade em dias, '
                             'ou qualquer coisa que você queira calcular. Use sua criatividade!'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            # Limpa tela antes do menu para garantir visibilidade
            if self.ui:
                self.ui.clear_screen()
            
            self.print_section("MENU DE EXERCÍCIOS", "📚", "accent")
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("\n" + "─" * 40)
            print("0. 🎯 Continuar para o Mini Projeto")
            print("─" * 40)
            
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre funções",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie sua própria calculadora",
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
        """Executa o quiz sobre funções"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("QUIZ: CONHECIMENTOS SOBRE FUNÇÕES", "📝", "warning")
        self.print_colored("Vamos testar o que você aprendeu!", "text")
        
        acertos = 0
        total_perguntas = len(quiz_data['questions'])
        
        for i, pergunta in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\n📝 PERGUNTA {i}/{total_perguntas}:", "accent")
            if self.exercicio(pergunta['question'], pergunta['answer'], pergunta['hint']):
                acertos += 1
            
            input("\n🔸 Pressione ENTER para continuar...")
        
        # Resultado final
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        percentual = (acertos / total_perguntas) * 100
        
        if percentual >= 80:
            self.print_success(f"🎉 EXCELENTE! Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)")
            self.print_colored("Você domina os conceitos de funções!", "success")
        elif percentual >= 60:
            self.print_colored(f"👍 BOM! Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)", "warning")
            self.print_colored("Continue praticando para aperfeiçoar!", "text")
        else:
            self.print_colored(f"💪 Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)", "error")
            self.print_colored("Revise o conteúdo e tente novamente!", "text")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_code_completion(self, code_data) -> None:
        """Executa exercícios de completar código"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DESAFIO: COMPLETE O CÓDIGO", "💻", "accent")
        self.print_colored("Complete os códigos sobre funções!", "text")
        
        for i, exercicio in enumerate(code_data['exercises'], 1):
            self.print_colored(f"\n💻 EXERCÍCIO {i}/{len(code_data['exercises'])}: {exercicio['instruction']}", "warning")
            
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercicio['starter'])
            
            self.print_colored("\n✍️ Sua tarefa: Substitua '___' pelo código correto", "info")
            resposta = input("👉 Sua resposta: ").strip()
            
            if resposta.lower() == exercicio['solution'].lower():
                self.print_success("✅ CORRETO! Muito bem!")
                
                # Mostrar código funcionando
                codigo_completo = exercicio['starter'].replace('___', exercicio['solution'])
                self.print_colored("\n🚀 Veja funcionando:", "success")
                self.executar_codigo(codigo_completo)
            else:
                self.print_warning(f"❌ Não foi dessa vez. A resposta era: {exercicio['solution']}")
                
                # Mostrar código correto
                codigo_completo = exercicio['starter'].replace('___', exercicio['solution'])
                self.print_colored("\n💡 Veja como fica correto:", "info")
                self.executar_codigo(codigo_completo)
            
            if i < len(code_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Parabéns por completar todos os exercícios!")
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_creative_exercise(self, creative_data) -> None:
        """Executa exercício criativo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("EXERCÍCIO CRIATIVO: SUA PRÓPRIA CALCULADORA", "🎨", "success")
        self.print_colored(creative_data['instruction'], "text")
        
        self.print_colored("\n💡 EXEMPLOS DE IDEIAS:", "info")
        ideias = [
            "🌡️ Converter Celsius para Fahrenheit",
            "💰 Calcular gorjeta em restaurante",
            "📅 Calcular idade em dias",
            "⏰ Converter horas em segundos",
            "🏃 Calcular velocidade média",
            "💸 Calcular desconto de produtos"
        ]
        
        for ideia in ideias:
            self.print_colored(f"  • {ideia}", "primary")
        
        self.print_colored("\n✍️ COMO FAZER:", "warning")
        self.print_colored("1. Escolha o que sua função vai calcular", "text")
        self.print_colored("2. Defina que parâmetros ela precisa", "text")
        self.print_colored("3. Escreva o código da função", "text")
        self.print_colored("4. Teste com alguns valores", "text")
        
        self.print_colored("\n🖥️ DIGITE SEU CÓDIGO:", "accent")
        self.print_colored("(Digite 'fim' em uma linha vazia para terminar)", "text")
        
        codigo_usuario = []
        while True:
            linha = input()
            if linha.lower() == 'fim':
                break
            codigo_usuario.append(linha)
        
        codigo_completo = '\n'.join(codigo_usuario)
        
        if codigo_completo.strip():
            self.print_colored("\n🚀 EXECUTANDO SUA CRIAÇÃO:", "success")
            try:
                exec(codigo_completo)
                self.print_success("\n🎉 FANTÁSTICO! Sua função funcionou perfeitamente!")
                self.print_colored("Você acabou de criar código reutilizável!", "success")
            except Exception as e:
                self.print_warning(f"\n❌ Oops! Houve um erro: {e}")
                self.print_colored("Não desanime! Programar é um processo de tentativa e erro.", "info")
        else:
            self.print_colored("\nNenhum código foi digitado. Tudo bem, você pode tentar depois!", "text")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _mini_projeto_conversor_universal(self) -> None:
        """Mini Projeto - Módulo 10: Conversor Universal de Unidades"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CONVERSOR UNIVERSAL DE UNIDADES")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CONVERSOR UNIVERSAL DE UNIDADES")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu conversor universal aplicando todas as técnicas de funções!")
        
        self.print_concept(
            "Conversor Universal",
            "Um sistema que converte diferentes unidades usando funções especializadas e reutilizáveis"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Engenheiros convertendo medidas em projetos",
            "Cozinheiros adaptando receitas internacionais",
            "Viajantes calculando moedas e temperaturas",
            "Estudantes resolvendo exercícios de física"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Funções básicas de conversão
        self.print_section("PASSO 1: Criando Funções de Conversão", "📝", "info")
        self.print_tip("Vamos criar funções para diferentes tipos de conversão")
        
        try:
            # PASSO 2: Sistema de menu
            self.print_section("PASSO 2: Sistema de Menu Interativo", "⚙️", "success")
            self.print_colored("Agora vamos criar um menu para o usuário escolher conversões:", "text")
            
            # PASSO 3: Resultado final
            self.print_section("PASSO 3: Conversor Funcionando", "🎬", "warning")
            
            # === CÓDIGO FINAL GERADO ===
            self.print_colored("Aqui está o código completo do seu Conversor Universal:", "text")
            
            codigo_final = f'''# 🐍 PROJETO: CONVERSOR UNIVERSAL DE UNIDADES
# Módulo 10: Funções e Reutilização

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def metros_para_pes(metros):
    """Converte metros para pés"""
    return metros * 3.28084

def pes_para_metros(pes):
    """Converte pés para metros"""
    return pes / 3.28084

def quilogramas_para_libras(kg):
    """Converte quilogramas para libras"""
    return kg * 2.20462

def libras_para_quilogramas(libras):
    """Converte libras para quilogramas"""
    return libras / 2.20462

def quilometros_para_milhas(km):
    """Converte quilômetros para milhas"""
    return km * 0.621371

def milhas_para_quilometros(milhas):
    """Converte milhas para quilômetros"""
    return milhas / 0.621371

def mostrar_menu():
    """Exibe o menu de opções"""
    print("\\n🔄 CONVERSOR UNIVERSAL DE UNIDADES")
    print("=" * 40)
    print("1. 🌡️  Temperatura (°C ↔ °F)")
    print("2. 📏 Comprimento (metros ↔ pés)")
    print("3. ⚖️  Peso (kg ↔ libras)")
    print("4. 🛣️  Distância (km ↔ milhas)")
    print("0. ❌ Sair")
    print("=" * 40)

def conversor_temperatura():
    """Menu de conversão de temperatura"""
    print("\\n🌡️ CONVERSÃO DE TEMPERATURA")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    
    opcao = input("\\nEscolha (1 ou 2): ")
    
    if opcao == "1":
        celsius = float(input("Digite a temperatura em °C: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"🌡️ {celsius}°C = {fahrenheit:.1f}°F")
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em °F: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"🌡️ {fahrenheit}°F = {celsius:.1f}°C")

def conversor_comprimento():
    """Menu de conversão de comprimento"""
    print("\\n📏 CONVERSÃO DE COMPRIMENTO")
    print("1. Metros → Pés")
    print("2. Pés → Metros")
    
    opcao = input("\\nEscolha (1 ou 2): ")
    
    if opcao == "1":
        metros = float(input("Digite o comprimento em metros: "))
        pes = metros_para_pes(metros)
        print(f"📏 {metros}m = {pes:.2f} pés")
    elif opcao == "2":
        pes = float(input("Digite o comprimento em pés: "))
        metros = pes_para_metros(pes)
        print(f"📏 {pes} pés = {metros:.2f}m")

def conversor_peso():
    """Menu de conversão de peso"""
    print("\\n⚖️ CONVERSÃO DE PESO")
    print("1. Quilogramas → Libras")
    print("2. Libras → Quilogramas")
    
    opcao = input("\\nEscolha (1 ou 2): ")
    
    if opcao == "1":
        kg = float(input("Digite o peso em kg: "))
        libras = quilogramas_para_libras(kg)
        print(f"⚖️ {kg}kg = {libras:.2f} libras")
    elif opcao == "2":
        libras = float(input("Digite o peso em libras: "))
        kg = libras_para_quilogramas(libras)
        print(f"⚖️ {libras} libras = {kg:.2f}kg")

def conversor_distancia():
    """Menu de conversão de distância"""
    print("\\n🛣️ CONVERSÃO DE DISTÂNCIA")
    print("1. Quilômetros → Milhas")
    print("2. Milhas → Quilômetros")
    
    opcao = input("\\nEscolha (1 ou 2): ")
    
    if opcao == "1":
        km = float(input("Digite a distância em km: "))
        milhas = quilometros_para_milhas(km)
        print(f"🛣️ {km}km = {milhas:.2f} milhas")
    elif opcao == "2":
        milhas = float(input("Digite a distância em milhas: "))
        km = milhas_para_quilometros(milhas)
        print(f"🛣️ {milhas} milhas = {km:.2f}km")

# PROGRAMA PRINCIPAL
print("🎉 BEM-VINDO AO CONVERSOR UNIVERSAL!")
print("Criado com funções reutilizáveis em Python")

# Simulando algumas conversões
print("\\n🧪 DEMONSTRAÇÃO DO CONVERSOR:")
print("\\n🌡️ TEMPERATURA:")
print(f"25°C = {celsius_para_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_para_celsius(77):.1f}°C")

print("\\n📏 COMPRIMENTO:")
print(f"10 metros = {metros_para_pes(10):.2f} pés")
print(f"100 pés = {pes_para_metros(100):.2f} metros")

print("\\n⚖️ PESO:")
print(f"70 kg = {quilogramas_para_libras(70):.2f} libras")
print(f"150 libras = {libras_para_quilogramas(150):.2f} kg")

print("\\n🛣️ DISTÂNCIA:")
print(f"100 km = {quilometros_para_milhas(100):.2f} milhas")
print(f"50 milhas = {milhas_para_quilometros(50):.2f} km")

print("\\n🎉 CONVERSOR FUNCIONANDO PERFEITAMENTE!")
print("✅ 8 funções de conversão criadas")
print("✅ Sistema modular e reutilizável")
print("✅ Código organizado e profissional")'''
            
            self.exemplo(codigo_final)
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.executar_codigo(codigo_final)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou seu Conversor Universal com Funções!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais tipos de conversão (área, volume, energia)",
            "Criar interface gráfica para o conversor",
            "Integrar com APIs de cotação de moedas",
            "Salvar histórico de conversões em arquivo"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre das Funções!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Conversor Universal de Unidades")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo10Funcoes()
    print("Teste do módulo 10 - versão standalone")
    module._funcoes_interativo()