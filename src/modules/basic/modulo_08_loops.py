#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 8: Loops (Repetições)
Aprenda sobre estruturas de repetição (for e while)
"""

from ..shared.base_module import BaseModule


class Modulo08Loops(BaseModule):
    """Módulo 8: Dominando Loops e Repetições"""
    
    def __init__(self):
        super().__init__("modulo_8", "Loops e Repetições")
        self.has_mini_project = True
        self.mini_project_points = 60
    
    def execute(self) -> None:
        """Executa o módulo Loops e Repetições"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._loops_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _loops_interativo(self) -> None:
        """Conteúdo principal do módulo Loops e Repetições"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔄 MÓDULO 8: DOMINANDO LOOPS E REPETIÇÕES")
        else:
            print("\n" + "="*50)
            print("🔄 MÓDULO 8: DOMINANDO LOOPS E REPETIÇÕES")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos aprender a automatizar tarefas repetitivas como um profissional!")
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
            self._mini_projeto_gerador_interativo()
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
                'id': 'secao_conceito_loops',
                'titulo': '🎯 O que são loops na programação?',
                'descricao': 'Entenda como automatizar tarefas repetitivas',
                'funcao': self._secao_conceito_loops
            },
            {
                'id': 'secao_for_basico',
                'titulo': '⚙️ Como o loop FOR funciona?',
                'descricao': 'Domine repetições controladas e previsíveis',
                'funcao': self._secao_for_basico
            },
            {
                'id': 'secao_while_basico',
                'titulo': '🔄 Como o loop WHILE funciona?',
                'descricao': 'Aprenda repetições baseadas em condições',
                'funcao': self._secao_while_basico
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Loops em ação - Exemplos práticos',
                'descricao': 'Veja loops resolvendo problemas reais',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 Onde usar loops na vida real?',
                'descricao': 'Aplicações práticas de loops',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas com loops',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Evite loops infinitos e outros problemas',
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
    
    def _secao_conceito_loops(self) -> None:
        """Seção: O que são loops na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO LOOPS NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Loops (Repetições)",
            "São estruturas que permitem executar o mesmo código várias vezes de forma automática e eficiente"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Imagine ter que escrever 1000 prints diferentes - loops fazem isso em 3 linhas!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma máquina de lavar roupa:", "text")
        self.print_colored("• Ela repete o ciclo: molhar → esfregar → enxaguar", "text")
        self.print_colored("• Faz isso automaticamente várias vezes", "text")
        self.print_colored("• Para quando a roupa está limpa (condição)", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Definimos o que queremos repetir (código dentro do loop)",
            "2. Estabelecemos quando parar (condição ou contador)",
            "3. O computador executa automaticamente até o fim"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Sem loop (chato e repetitivo)
print("Olá 1")
print("Olá 2")
print("Olá 3")
print("Olá 4")
print("Olá 5")

print("\\n--- COM LOOP (elegante!) ---")

# Com loop (inteligente e eficiente)
for i in range(1, 6):
    print(f"Olá {i}")'''
        
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver a diferença:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Instagram - Carrega fotos uma por uma na timeline",
            "Netflix - Processa milhões de filmes para recomendações",
            "WhatsApp - Envia mensagens para todos os contatos do grupo",
            "Jogos - Move personagens, atualiza física, desenha frames"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_for_basico(self) -> None:
        """Seção: Como o loop FOR funciona?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO O LOOP FOR FUNCIONA?", "⚙️")
        
        # === CONCEITO ESPECÍFICO ===
        self.print_concept(
            "Loop FOR",
            "Usado quando você SABE quantas vezes quer repetir algo ou tem uma lista para percorrer"
        )
        
        # === ESTRUTURA BÁSICA ===
        self.print_colored("\n🏗️ ESTRUTURA BÁSICA DO FOR:", "warning")
        estrutura = '''for variavel in sequencia:
    # Código que se repete
    print(f"Repetição número: {variavel}")'''
        
        self.exemplo(estrutura)
        
        # === TIPOS DE FOR ===
        self.print_colored("\n📌 PRINCIPAIS TIPOS DE FOR:", "info")
        tipos = [
            "• for i in range(5) → Repete 5 vezes (0,1,2,3,4)",
            "• for item in lista → Percorre cada item da lista",
            "• for i in range(1,6) → Conta de 1 até 5",
            "• for letra in 'Python' → Percorre cada letra"
        ]
        
        for tipo in tipos:
            self.print_colored(tipo, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO RANGE ===
        self.print_colored("\n🔢 EXEMPLO COM RANGE:", "success")
        codigo_range = '''# Range básico
print("Contando de 0 a 4:")
for i in range(5):
    print(f"  {i}")

# Range com início e fim
print("\\nContando de 1 a 5:")
for i in range(1, 6):
    print(f"  {i}")

# Range com passo
print("\\nContando de 2 em 2:")
for i in range(0, 11, 2):
    print(f"  {i}")'''
        
        self.exemplo(codigo_range)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_range)
        
        input("\n🔸 Pressione ENTER para ver mais exemplos...")
        
        # === EXEMPLO COM LISTAS ===
        self.print_colored("\n📝 EXEMPLO COM LISTAS:", "success")
        codigo_lista = '''# Percorrendo uma lista
frutas = ["🍎", "🍌", "🍊", "🍇", "🥝"]

print("Frutas da feira:")
for fruta in frutas:
    print(f"  Comprando {fruta}")

print("\\nContador automático:")
for i, fruta in enumerate(frutas, 1):
    print(f"  {i}. {fruta}")'''
        
        self.exemplo(codigo_lista)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_lista)
        
        self.print_tip("O enumerate() adiciona um contador automático!")
        
        self.pausar()
    
    def _secao_while_basico(self) -> None:
        """Seção: Como o loop WHILE funciona?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO O LOOP WHILE FUNCIONA?", "🔄")
        
        # === CONCEITO ESPECÍFICO ===
        self.print_concept(
            "Loop WHILE",
            "Usado quando você NÃO SABE quantas vezes vai repetir - continua enquanto uma condição for verdadeira"
        )
        
        # === ANALOGIA ESPECÍFICA ===
        self.print_colored("\n🏠 ANALOGIA DO WHILE:", "warning")
        self.print_colored("Como um porteiro de festa:", "text")
        self.print_colored("• ENQUANTO tiver espaço na festa...", "text")
        self.print_colored("• Continua deixando pessoas entrar", "text")
        self.print_colored("• Para quando a festa lota (condição muda)", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === ESTRUTURA BÁSICA ===
        self.print_colored("\n🏗️ ESTRUTURA BÁSICA DO WHILE:", "info")
        estrutura = '''# Configuração inicial
contador = 0

while condicao:
    # Código que se repete
    print("Repetindo...")
    
    # IMPORTANTE: Modificar a condição!
    contador += 1'''
        
        self.exemplo(estrutura)
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_while = '''# Contagem regressiva
print("🚀 CONTAGEM REGRESSIVA:")
contador = 5

while contador > 0:
    print(f"  {contador}...")
    contador -= 1  # CRÍTICO: sempre modificar!

print("  🎉 DECOLAGEM!")

print("\\n🎮 JOGO SIMPLES:")
pontos = 0
nivel = 1

while pontos < 50:
    print(f"Nível {nivel}: +{nivel*5} pontos")
    pontos += nivel * 5
    nivel += 1

print(f"🏆 Parabéns! {pontos} pontos totais!")'''
        
        self.exemplo(codigo_while)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_while)
        
        # === CUIDADO COM LOOPS INFINITOS ===
        self.print_colored("\n⚠️ CUIDADO - LOOP INFINITO:", "error")
        loop_ruim = '''# ❌ NUNCA FAÇA ISSO!
contador = 5
while contador > 0:
    print("Infinito!")
    # Esqueceu de modificar contador!
    # Loop nunca termina!'''
        
        self.exemplo(loop_ruim)
        self.print_warning("Sempre certifique-se de que a condição vai mudar!")
        
        self.pausar()
    
    def _secao_exemplos_praticos(self) -> None:
        """Seção: Loops em ação - Exemplos práticos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("LOOPS EM AÇÃO - EXEMPLOS PRÁTICOS", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Calculadora de Tabuada',
                'descricao': 'For loop para gerar tabuada de qualquer número',
                'codigo': '''# Gerador de tabuada
numero = 7
print(f"📊 TABUADA DO {numero}:")
print("=" * 20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado:2d}")''',
                'explicacao': 'Usa range(1,11) para multiplicar de 1 a 10, com formatação alinhada'
            },
            {
                'titulo': 'EXEMPLO 2: Validador de Senha',
                'descricao': 'While loop para pedir senha até acertar',
                'codigo': '''# Simulação de validação de senha
senha_correta = "python123"
tentativas = 0
max_tentativas = 3

print("🔐 SISTEMA DE LOGIN")
while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    tentativas += 1
    
    if senha == senha_correta:
        print("✅ Login realizado com sucesso!")
        break
    else:
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"❌ Senha incorreta! {restantes} tentativas restantes")
        else:
            print("🚫 Acesso bloqueado!")''',
                'explicacao': 'Combina while com if para controlar tentativas e dar feedback'
            },
            {
                'titulo': 'EXEMPLO 3: Processador de Lista',
                'descricao': 'For loop para processar dados de uma lista',
                'codigo': '''# Processamento de notas de alunos
notas = [8.5, 7.2, 9.0, 6.8, 8.9, 7.5, 9.2]
total = 0
aprovados = 0

print("📚 PROCESSAMENTO DE NOTAS:")
print("-" * 30)

for i, nota in enumerate(notas, 1):
    total += nota
    status = "✅ APROVADO" if nota >= 7.0 else "❌ REPROVADO"
    
    if nota >= 7.0:
        aprovados += 1
    
    print(f"Aluno {i}: {nota:4.1f} - {status}")

media = total / len(notas)
taxa_aprovacao = (aprovados / len(notas)) * 100

print(f"\\n📊 ESTATÍSTICAS:")
print(f"Média da turma: {media:.2f}")
print(f"Taxa de aprovação: {taxa_aprovacao:.1f}%")''',
                'explicacao': 'Demonstra acumuladores, contadores e cálculos dentro de loops'
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
        
        self.print_success("\n🎉 Agora você viu loops resolvendo problemas reais!")
        self.pausar()
    
    def _secao_casos_uso(self) -> None:
        """Seção: Onde usar loops na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR LOOPS NA VIDA REAL?", "🌍")
        
        casos_uso = [
            {
                'titulo': '🎮 DESENVOLVIMENTO DE GAMES',
                'descricao': 'Game loop - o coração de qualquer jogo',
                'exemplo': '''# Game loop simplificado
import time
import random

print("🎮 MINI GAME - COLETE AS MOEDAS!")
pontos = 0
tempo_restante = 10

# Loop principal do jogo
while tempo_restante > 0:
    print(f"⏰ Tempo: {tempo_restante}s | 💰 Pontos: {pontos}")
    
    # Simula evento aleatório
    if random.random() > 0.5:
        moedas = random.randint(1, 5)
        pontos += moedas
        print(f"  ✨ Você coletou {moedas} moedas!")
    else:
        print("  💨 Nada desta vez...")
    
    time.sleep(1)
    tempo_restante -= 1

print(f"\\n🏆 GAME OVER! Pontuação final: {pontos}")'''
            },
            {
                'titulo': '📊 ANÁLISE DE DADOS',
                'descricao': 'Processamento de grandes volumes de informação',
                'exemplo': '''# Análise de vendas mensais
vendas_mensais = [
    15000, 18500, 22000, 17800, 19200,
    21500, 23800, 25100, 20900, 22400,
    24600, 28000
]

meses = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

print("📊 RELATÓRIO ANUAL DE VENDAS")
print("=" * 40)

total_anual = 0
melhor_mes = 0
melhor_valor = 0

# Processa dados mês a mês
for i, vendas in enumerate(vendas_mensais):
    total_anual += vendas
    
    if vendas > melhor_valor:
        melhor_valor = vendas
        melhor_mes = i
    
    print(f"{meses[i]}: R$ {vendas:,}")

media_mensal = total_anual / len(vendas_mensais)

print(f"\\n💰 RESUMO:")
print(f"Total anual: R$ {total_anual:,}")
print(f"Média mensal: R$ {media_mensal:,.0f}")
print(f"Melhor mês: {meses[melhor_mes]} (R$ {melhor_valor:,})")'''
            },
            {
                'titulo': '🤖 AUTOMAÇÃO E IA',
                'descricao': 'Machine Learning e processamento automático',
                'exemplo': '''# Simulação de treinamento de IA
import random

print("🤖 TREINAMENTO DE IA SIMPLES")
print("Aprendendo a reconhecer padrões...")

# Parâmetros do modelo
precisao = 0.5  # Começa com 50%
epoch = 0
target_precisao = 0.95

# Loop de treinamento
while precisao < target_precisao:
    epoch += 1
    
    # Simula melhoria gradual
    melhoria = random.uniform(0.01, 0.05)
    precisao += melhoria
    
    # Previne overfitting
    if precisao > 1.0:
        precisao = 0.98 + random.uniform(-0.02, 0.02)
    
    print(f"Época {epoch:3d}: Precisão = {precisao:.1%}")
    
    # Evita loop infinito
    if epoch >= 100:
        break

if precisao >= target_precisao:
    print(f"\\n✅ IA treinada com sucesso!")
    print(f"🎯 Precisão final: {precisao:.1%}")
else:
    print(f"\\n⚠️ Treinamento incompleto após {epoch} épocas")'''
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
        
        self.print_success("\n🌟 Loops estão em TODO LUGAR na programação!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas com loops"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS COM LOOPS", "⭐")
        
        praticas = [
            {
                'titulo': '🎯 Use o loop certo para cada situação',
                'ruim': '''# ❌ EVITE: FOR quando deveria ser WHILE
for i in range(1000000):
    if condicao_complexa():
        break
    # código...''',
                'bom': '''# ✅ PREFIRA: WHILE para condições dinâmicas
while condicao_complexa():
    # código...
    # condição pode mudar naturalmente'''
            },
            {
                'titulo': '⚡ Evite loops desnecessários',
                'ruim': '''# ❌ EVITE: Loop para buscar em lista
encontrado = None
for item in lista:
    if item.id == procurado:
        encontrado = item
        break''',
                'bom': '''# ✅ PREFIRA: Função built-in quando possível
encontrado = next((item for item in lista 
                   if item.id == procurado), None)
# ou usar filter(), map(), etc.'''
            },
            {
                'titulo': '🔒 Sempre previna loops infinitos',
                'ruim': '''# ❌ PERIGO: Sem modificação da condição
tentativas = 0
while tentativas < 5:
    fazer_algo()
    # Esqueceu: tentativas += 1''',
                'bom': '''# ✅ SEGURO: Sempre modifica a condição
tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    fazer_algo()
    tentativas += 1  # Sempre incremente!'''
            },
            {
                'titulo': '📝 Use nomes descritivos para variáveis',
                'ruim': '''# ❌ CONFUSO: Nomes genéricos
for i in dados:
    for j in i:
        print(j)''',
                'bom': '''# ✅ CLARO: Nomes que fazem sentido
for aluno in turma:
    for nota in aluno.notas:
        print(f"Nota: {nota}")'''
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
        
        self.print_tip("Loops eficientes fazem seus programas mais rápidos e legíveis!")
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ERROS COMUNS COM LOOPS", "⚠️")
        
        erros = [
            {
                'titulo': '🌀 Loop infinito - O pesadelo dos programadores',
                'erro': '''# ❌ ERRO: Loop nunca termina
contador = 0
while contador < 10:
    print(f"Contando: {contador}")
    # ERRO: Esqueceu de incrementar!''',
                'correto': '''# ✅ CORRETO: Sempre modifica a condição
contador = 0
while contador < 10:
    print(f"Contando: {contador}")
    contador += 1  # Incrementa para sair do loop''',
                'dica': 'Sempre verifique se a condição do while será modificada!'
            },
            {
                'titulo': '🔢 Erro de índice em listas',
                'erro': '''# ❌ ERRO: Acessa índice que não existe
lista = [1, 2, 3]
for i in range(5):  # range maior que a lista!
    print(lista[i])  # IndexError quando i >= 3''',
                'correto': '''# ✅ CORRETO: Use len() ou iterate diretamente
lista = [1, 2, 3]
for i in range(len(lista)):  # Tamanho correto
    print(lista[i])

# Ainda melhor:
for item in lista:  # Sem índices
    print(item)''',
                'dica': 'Prefira iterar diretamente nos itens em vez de usar índices'
            },
            {
                'titulo': '🔄 Modificar lista durante iteração',
                'erro': '''# ❌ ERRO: Modifica lista enquanto itera
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Modifica durante loop!''',
                'correto': '''# ✅ CORRETO: Cria nova lista ou usa compreensão
numeros = [1, 2, 3, 4, 5]

# Opção 1: Lista nova
impares = []
for num in numeros:
    if num % 2 != 0:
        impares.append(num)

# Opção 2: List comprehension (melhor)
impares = [num for num in numeros if num % 2 != 0]''',
                'dica': 'Nunca modifique uma lista enquanto está iterando sobre ela'
            },
            {
                'titulo': '🎯 Range com valores incorretos',
                'erro': '''# ❌ ERRO: Range vazio ou incorreto
for i in range(5, 1):  # Range vazio!
    print(i)  # Nunca executa

for i in range(1, 10, -1):  # Step negativo com ordem errada
    print(i)  # Nunca executa''',
                'correto': '''# ✅ CORRETO: Range com valores lógicos
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

# Verificar se range não está vazio
inicio, fim = 5, 1
if inicio < fim:
    for i in range(inicio, fim):
        print(i)''',
                'dica': 'Sempre verifique se os parâmetros do range fazem sentido'
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
        self.print_colored("Vamos testar o que você aprendeu sobre loops!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Loops',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual loop você usa quando SABE quantas vezes vai repetir?',
                        'answer': ['for', 'loop for'],
                        'hint': 'É ideal para listas e contadores fixos'
                    },
                    {
                        'question': 'Qual comando gera números de 0 a 4?',
                        'answer': ['range(5)', 'range(0,5)'],
                        'hint': 'Lembre-se: range para antes do último número'
                    },
                    {
                        'question': 'Como você evita um loop infinito em WHILE?',
                        'answer': ['modificando a condição', 'incrementando variável', 'alterando condição'],
                        'hint': 'A condição precisa mudar para se tornar False'
                    },
                    {
                        'question': 'Qual palavra-chave para interromper um loop?',
                        'answer': ['break'],
                        'hint': 'É usada para sair do loop antes do fim natural'
                    },
                    {
                        'question': 'Qual palavra-chave para pular para próxima iteração?',
                        'answer': ['continue'],
                        'hint': 'Pula o resto do código e vai para próxima repetição'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o for para contar de 1 a 5',
                        'starter': '''for i in _____(1, 6):
    print(f"Contando: {i}")''',
                        'solution': 'range',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o while para countdown',
                        'starter': '''contador = 5
_____ contador > 0:
    print(contador)
    contador -= 1
print("Fim!")''',
                        'solution': 'while',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o loop com break quando achar o item',
                        'starter': '''lista = ["a", "b", "c", "d"]
procurado = "c"

for item in lista:
    if item == procurado:
        print(f"Achei: {item}")
        _____
    print(f"Verificando: {item}")''',
                        'solution': 'break',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Gerador de Padrões',
                'type': 'creative',
                'instruction': 'Crie um padrão visual usando loops! Pode ser estrelas, números, emojis - use sua criatividade!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre loops FOR e WHILE",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie padrões visuais com loops",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto Gerador Interativo",
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
            self.print_success("🌟 Excelente! Você domina os loops!")
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
                print(f"\n✍️ Complete com a palavra-chave:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Perfeito! Resposta correta!")
                    # Mostrar código completo funcionando
                    codigo_completo = ex['starter'].replace('_____', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'intermediate':
                print(f"\n✍️ Complete com a palavra-chave:")
                user_input = input(">>> ").strip()
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Correto! Loop perfeito!")
                    codigo_completo = ex['starter'].replace('_____', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
                    
            elif exercise_type == 'advanced':
                print(f"\n✍️ Complete com a palavra-chave:")
                user_input = input(">>> ").strip()
                
                if user_input.lower() == ex['solution'].lower():
                    self.print_success("✅ Excelente! Controle de loop avançado!")
                    codigo_completo = ex['starter'].replace('_____', user_input)
                    print("\n🚀 Código completo:")
                    self.executar_codigo(codigo_completo)
                else:
                    self.print_warning(f"❌ Resposta incorreta. A resposta era: {ex['solution']}")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de loops!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        
        print("\n💡 Exemplos de padrões que você pode criar:")
        print("⭐ Pirâmide de estrelas")
        print("🔢 Sequência de números") 
        print("🎨 Arte ASCII com emojis")
        print("📊 Gráfico simples de barras")
        
        print("\n🎯 Vamos criar seu padrão personalizado:")
        
        tipo = input("\n📝 Que tipo de padrão? (estrelas/números/emojis/outro): ").strip().lower()
        tamanho = input("📏 Quantas linhas? (ex: 5): ").strip()
        
        try:
            tamanho = int(tamanho) if tamanho.isdigit() else 5
        except:
            tamanho = 5
        
        if tipo in ['estrelas', 'estrela', 'star']:
            simbolo = "⭐"
            nome_padrao = "Pirâmide de Estrelas"
        elif tipo in ['números', 'numeros', 'number']:
            simbolo = None
            nome_padrao = "Padrão Numérico"
        elif tipo in ['emojis', 'emoji']:
            emoji_escolhido = input("Qual emoji? (ex: 🌟): ").strip()
            simbolo = emoji_escolhido if emoji_escolhido else "🎨"
            nome_padrao = f"Arte de {simbolo}"
        else:
            simbolo = "█"
            nome_padrao = "Padrão Personalizado"
        
        # Gerar código baseado nas escolhas
        if simbolo:
            codigo_criativo = f'''# 🎨 {nome_padrao.upper()}
print("🎨 {nome_padrao}")
print("=" * 30)

for i in range(1, {tamanho + 1}):
    espacos = " " * ({tamanho} - i)
    simbolos = "{simbolo}" * i
    print(f"{{espacos}}{{simbolos}}")

print("\\n✨ Padrão criado com sucesso!")'''
        else:
            codigo_criativo = f'''# 🔢 {nome_padrao.upper()}
print("🔢 {nome_padrao}")
print("=" * 30)

for i in range(1, {tamanho + 1}):
    numeros = ""
    for j in range(i):
        numeros += str(i) + " "
    print(numeros.strip())

print("\\n✨ Padrão criado com sucesso!")'''
        
        print(f"\n🚀 Aqui está seu {nome_padrao} personalizado:")
        self.exemplo(codigo_criativo)
        
        print("\n🎬 Executando seu padrão:")
        self.executar_codigo(codigo_criativo)
        
        print(f"\n🎉 Incrível! Você criou um {nome_padrao} único!")
        self.print_success("🏆 Parabéns pela criatividade com loops!")
        
        self.pausar()
    
    def _mini_projeto_gerador_interativo(self) -> None:
        """Mini Projeto - Módulo 8: Gerador Interativo de Padrões e Sequências"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: GERADOR INTERATIVO DE PADRÕES")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: GERADOR INTERATIVO DE PADRÕES")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um gerador completo usando o poder dos loops!")
        
        self.print_concept(
            "Gerador Interativo de Padrões",
            "Um programa que usa loops FOR e WHILE para criar múltiplos padrões visuais e sequências matemáticas"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Game Development - Geração procedural de mapas e texturas",
            "Arte Digital - Criação de padrões fractais e designs",
            "Data Visualization - Gráficos e representações visuais",
            "Interface Design - Elementos visuais e animações"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Coleta de preferências
        self.print_section("PASSO 1: Configurando o gerador", "📝", "info")
        self.print_tip("Vamos criar um menu interativo para o usuário escolher padrões")
        
        try:
            print("\n🎨 Preparando opções de padrões:")
            padroes_disponiveis = [
                "Pirâmide de Estrelas",
                "Árvore de Natal",
                "Tabela de Multiplicação",
                "Sequência Fibonacci",
                "Arte ASCII",
                "Gráfico de Barras"
            ]
            
            for i, padrao in enumerate(padroes_disponiveis, 1):
                print(f"  {i}. {padrao}")
            
            input("\n🔸 Pressione ENTER para ver o código...")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Implementação dos padrões
        self.print_section("PASSO 2: Implementando os geradores", "⚙️", "success")
        self.print_colored("Agora vamos criar cada gerador usando loops:", "text")
        
        # PASSO 3: Sistema completo
        self.print_section("PASSO 3: Sistema completo funcionando", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo do seu Gerador Interativo:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: GERADOR INTERATIVO DE PADRÕES E SEQUÊNCIAS
# Módulo 8: Loops e Repetições

import random
import time

def gerar_piramide_estrelas(altura):
    """Gera pirâmide de estrelas usando loops FOR"""
    print(f"\\n⭐ PIRÂMIDE DE ESTRELAS (Altura: {{altura}})")
    print("-" * 30)
    
    for i in range(1, altura + 1):
        espacos = " " * (altura - i)
        estrelas = "⭐" * i
        print(f"{{espacos}}{{estrelas}}")

def gerar_arvore_natal(altura):
    """Gera árvore de Natal com loops FOR aninhados"""
    print(f"\\n🎄 ÁRVORE DE NATAL (Altura: {{altura}})")
    print("-" * 30)
    
    # Copa da árvore
    for i in range(1, altura + 1):
        espacos = " " * (altura - i)
        folhas = "🌲" * i
        print(f"{{espacos}}{{folhas}}")
    
    # Tronco
    espacos_tronco = " " * (altura - 1)
    print(f"{{espacos_tronco}}🟫")
    print(f"{{espacos_tronco}}🟫")

def gerar_tabuada(numero, limite=10):
    """Gera tabuada usando loop FOR"""
    print(f"\\n🔢 TABUADA DO {{numero}}")
    print("-" * 25)
    
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{{numero}} x {{i:2d}} = {{resultado:3d}}")

def gerar_fibonacci(quantidade):
    """Gera sequência Fibonacci usando loop WHILE"""
    print(f"\\n🌀 SEQUÊNCIA FIBONACCI ({{quantidade}} números)")
    print("-" * 35)
    
    if quantidade <= 0:
        return
    
    # Casos base
    if quantidade >= 1:
        a = 0
        print(f"1º: {{a}}")
    
    if quantidade >= 2:
        b = 1
        print(f"2º: {{b}}")
    
    # Gerando resto da sequência
    contador = 3
    while contador <= quantidade:
        proximo = a + b
        print(f"{{contador}}º: {{proximo}}")
        a, b = b, proximo
        contador += 1

def gerar_arte_ascii(largura, altura):
    """Gera arte ASCII usando loops aninhados"""
    print(f"\\n🎭 ARTE ASCII ({{largura}}x{{altura}})")
    print("-" * 25)
    
    for linha in range(altura):
        arte = ""
        for coluna in range(largura):
            # Padrão: bordas azuis, interior branco
            if linha == 0 or linha == altura-1 or coluna == 0 or coluna == largura-1:
                arte += "🟦"
            else:
                arte += "⬜"
        print(arte)

def gerar_grafico_barras(dados, titulo="Gráfico"):
    """Gera gráfico de barras simples"""
    print(f"\\n📊 {{titulo.upper()}}")
    print("-" * 30)
    
    for i, valor in enumerate(dados, 1):
        barra = "█" * valor
        print(f"Item {{i}}: {{barra}} ({{valor}})")

def menu_principal():
    """Menu principal do gerador"""
    print("🎨 GERADOR INTERATIVO DE PADRÕES E SEQUÊNCIAS")
    print("=" * 55)
    print("\\nEscolha um padrão para gerar:")
    print("1. ⭐ Pirâmide de Estrelas")
    print("2. 🎄 Árvore de Natal")
    print("3. 🔢 Tabela de Multiplicação")
    print("4. 🌀 Sequência Fibonacci")
    print("5. 🎭 Arte ASCII")
    print("6. 📊 Gráfico de Barras")
    print("7. 🎲 Surpresa Aleatória!")
    print("0. 🚪 Sair")

def executar_gerador():
    """Função principal que executa o gerador"""
    continuar = True
    
    while continuar:
        menu_principal()
        
        try:
            opcao = input("\\n👉 Sua escolha: ").strip()
            
            if opcao == "1":
                altura = int(input("Altura da pirâmide (1-10): ") or "5")
                altura = max(1, min(altura, 10))
                gerar_piramide_estrelas(altura)
                
            elif opcao == "2":
                altura = int(input("Altura da árvore (1-8): ") or "5")
                altura = max(1, min(altura, 8))
                gerar_arvore_natal(altura)
                
            elif opcao == "3":
                numero = int(input("Número da tabuada (1-20): ") or "7")
                numero = max(1, min(numero, 20))
                gerar_tabuada(numero)
                
            elif opcao == "4":
                quantidade = int(input("Quantos números Fibonacci (1-20): ") or "10")
                quantidade = max(1, min(quantidade, 20))
                gerar_fibonacci(quantidade)
                
            elif opcao == "5":
                largura = int(input("Largura (3-15): ") or "8")
                altura = int(input("Altura (3-10): ") or "5")
                largura = max(3, min(largura, 15))
                altura = max(3, min(altura, 10))
                gerar_arte_ascii(largura, altura)
                
            elif opcao == "6":
                print("\\nGerando dados aleatórios para demonstração...")
                dados = [random.randint(1, 15) for _ in range(5)]
                gerar_grafico_barras(dados, "Vendas por Região")
                
            elif opcao == "7":
                print("\\n🎲 SURPRESA! Gerando padrão aleatório...")
                time.sleep(1)
                opcoes = ["1", "2", "3", "4", "5", "6"]
                opcao_aleatoria = random.choice(opcoes)
                print(f"Sorteado: Opção {{opcao_aleatoria}}!")
                
                # Re-executa com opção sorteada
                if opcao_aleatoria == "1":
                    gerar_piramide_estrelas(random.randint(3, 7))
                elif opcao_aleatoria == "2":
                    gerar_arvore_natal(random.randint(3, 6))
                elif opcao_aleatoria == "3":
                    gerar_tabuada(random.randint(2, 12))
                elif opcao_aleatoria == "4":
                    gerar_fibonacci(random.randint(8, 15))
                elif opcao_aleatoria == "5":
                    gerar_arte_ascii(random.randint(5, 12), random.randint(4, 8))
                elif opcao_aleatoria == "6":
                    dados = [random.randint(1, 20) for _ in range(6)]
                    gerar_grafico_barras(dados, "Dados Aleatórios")
                
            elif opcao == "0":
                print("\\n👋 Obrigado por usar o Gerador de Padrões!")
                continuar = False
                
            else:
                print("\\n❌ Opção inválida! Escolha de 0 a 7.")
            
            if continuar and opcao != "0":
                input("\\n🔸 Pressione ENTER para continuar...")
                
        except ValueError:
            print("\\n❌ Digite apenas números!")
        except Exception as e:
            print(f"\\n❌ Erro inesperado: {{e}}")

# === EXECUTANDO O GERADOR ===
print("🚀 INICIANDO GERADOR INTERATIVO...")
executar_gerador()
print("\\n✨ GERADOR FINALIZADO! Loops são poderosos! 🔄")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        print("🚀 Executando uma demonstração do seu Gerador Interativo:")
        
        # Demonstração simplificada para não ser interativa
        codigo_demo = '''# 🎨 DEMONSTRAÇÃO DO GERADOR
print("🚀 DEMONSTRAÇÃO - GERADOR DE PADRÕES")
print("=" * 45)

# Demo 1: Pirâmide
print("\\n⭐ PIRÂMIDE DE ESTRELAS:")
for i in range(1, 6):
    espacos = " " * (5 - i)
    estrelas = "⭐" * i
    print(f"{espacos}{estrelas}")

# Demo 2: Tabuada
print("\\n🔢 TABUADA DO 3:")
for i in range(1, 6):
    print(f"3 x {i} = {3*i}")

# Demo 3: Fibonacci
print("\\n🌀 FIBONACCI (8 números):")
a, b = 0, 1
fib = [a, b]
for _ in range(6):
    proximo = a + b
    fib.append(proximo)
    a, b = b, proximo
print("Sequência:", fib)

print("\\n✨ TODOS OS PADRÕES FUNCIONANDO PERFEITAMENTE!")'''
        
        self.executar_codigo(codigo_demo)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um gerador completo de padrões!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais tipos de padrões (fractais, espirais)",
            "Implementar animações usando loops temporais",
            "Criar padrões coloridos usando bibliotecas gráficas",
            "Salvar padrões em arquivos de imagem",
            "Integrar com sistemas de visualização de dados"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Loops!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Gerador Interativo de Padrões e Sequências")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo08Loops()
    print("Teste do módulo 8 - versão refatorada")
    module._loops_interativo()