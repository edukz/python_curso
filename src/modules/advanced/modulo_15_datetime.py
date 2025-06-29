#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 15: Trabalhando com Datas e Horas
Aprenda a manipular datas, horários, fusos e cálculos temporais
"""

from ..shared.base_module import BaseModule


class Modulo15Datetime(BaseModule):
    """Módulo 15: Dominando Datas e Horas"""
    
    def __init__(self):
        super().__init__("modulo_15", "Trabalhando com Datas e Horas")
        self.has_mini_project = True
        self.mini_project_points = 85
    
    def execute(self) -> None:
        """Executa o módulo Trabalhando com Datas e Horas"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._datetime_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _datetime_interativo(self) -> None:
        """Conteúdo principal do módulo Trabalhando com Datas e Horas"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⏰ MÓDULO 15: DOMINANDO DATAS E HORAS")
        else:
            print("\n" + "="*50)
            print("⏰ MÓDULO 15: DOMINANDO DATAS E HORAS")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos dominar o tempo em Python como verdadeiros crononautas!")
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
            self._mini_projeto_agenda_temporal()
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
                'id': 'secao_conceito_tempo',
                'titulo': '🎯 O que são datas e horas na programação?',
                'descricao': 'Entenda como o computador lida com tempo',
                'funcao': self._secao_conceito_tempo
            },
            {
                'id': 'secao_datetime_basico',
                'titulo': '⚙️ Módulo datetime: criando e manipulando',
                'descricao': 'Domine date, time, datetime e timedelta',
                'funcao': self._secao_datetime_basico
            },
            {
                'id': 'secao_formatacao',
                'titulo': '🎨 Formatação e parsing de datas',
                'descricao': 'strftime, strptime e formatação personalizada',
                'funcao': self._secao_formatacao
            },
            {
                'id': 'secao_calculos_temporais',
                'titulo': '🧮 Cálculos e operações temporais',
                'descricao': 'Diferenças, adições e subtrações de tempo',
                'funcao': self._secao_calculos_temporais
            },
            {
                'id': 'secao_fusos_horarios',
                'titulo': '🌍 Fusos horários e timezone',
                'descricao': 'UTC, timezone awareness e conversões',
                'funcao': self._secao_fusos_horarios
            },
            {
                'id': 'secao_casos_praticos',
                'titulo': '💼 Casos práticos do mundo real',
                'descricao': 'Aplicações profissionais com datas',
                'funcao': self._secao_casos_praticos
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre tempo e calendários',
                'descricao': 'Fatos fascinantes sobre medição de tempo',
                'funcao': self._secao_curiosidades
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
    
    def _secao_conceito_tempo(self) -> None:
        """Seção: O que são datas e horas na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO DATAS E HORAS NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Tempo em Programação",
            "A representação digital de momentos, durações e intervalos que permite ao computador entender e calcular com tempo"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Computadores medem tempo em números! Tudo é matemática por baixo dos panos.")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você tem um relógio digital muito preciso que não só mostra as horas, mas também consegue fazer contas: 'Se são 14:30 e eu somar 2 horas e 45 minutos, que horas serão?' O módulo datetime é esse relógio superinteligente!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO O COMPUTADOR ENTENDE TEMPO:", "info")
        passos_tecnicos = [
            "1. O computador conta segundos desde 1º de janeiro de 1970 (Unix Timestamp)",
            "2. Python converte esses números em objetos datetime que são fáceis de usar",
            "3. Você pode fazer operações matemáticas: somar dias, calcular diferenças",
            "4. Formatação transforma números em texto legível: '2024-01-15 14:30:00'"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''from datetime import datetime
import time

# Como o computador vê o tempo agora
timestamp_agora = time.time()
print(f"⏰ Timestamp Unix: {timestamp_agora}")

# Como nós vemos o mesmo momento
datetime_agora = datetime.now()
print(f"📅 Para humanos: {datetime_agora}")

# Demonstração de cálculo simples
print(f"\\n🧮 CÁLCULO TEMPORAL:")
print(f"Agora: {datetime_agora.strftime('%H:%M:%S')}")
print(f"Em 1 hora será: {(datetime_agora.replace(hour=datetime_agora.hour+1) if datetime_agora.hour < 23 else datetime_agora.replace(hour=0, day=datetime_agora.day+1)).strftime('%H:%M:%S')}")'''
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "📱 WhatsApp mostra 'há 5 minutos' nas mensagens",
            "✈️ Sistemas de voo calculam durações e conexões",
            "🏦 Bancos registram timestamps para todas as transações",
            "📺 Netflix agenda lançamentos por fuso horário",
            "🚀 NASA sincroniza missões espaciais com precisão de milissegundos"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_datetime_basico(self) -> None:
        """Seção: Módulo datetime: criando e manipulando"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MÓDULO DATETIME: CRIANDO E MANIPULANDO", "⚙️", "success")
        
        exemplos = [
            {
                'titulo': 'DATETIME: Momento completo (data + hora)',
                'descricao': 'Representa um momento específico no tempo',
                'codigo': '''from datetime import datetime

# Obter momento atual
agora = datetime.now()
print(f"🕒 Agora: {agora}")
print(f"📅 Só a data: {agora.date()}")
print(f"⏰ Só a hora: {agora.time()}")

# Criar momento específico
natal_2024 = datetime(2024, 12, 25, 18, 0, 0)
print(f"🎄 Natal 2024: {natal_2024}")

# Extrair componentes
print(f"\\n🔍 COMPONENTES DO DATETIME:")
print(f"Ano: {agora.year}")
print(f"Mês: {agora.month}")
print(f"Dia: {agora.day}")
print(f"Hora: {agora.hour}")
print(f"Minuto: {agora.minute}")
print(f"Segundo: {agora.second}")
print(f"Dia da semana: {agora.weekday()} (0=segunda)")''',
                'explicacao': 'datetime é perfeito para timestamps e eventos específicos'
            },
            {
                'titulo': 'DATE: Apenas datas (sem hora)',
                'descricao': 'Quando você só precisa do dia, mês e ano',
                'codigo': '''from datetime import date

# Data de hoje
hoje = date.today()
print(f"📅 Hoje: {hoje}")

# Criar data específica
independencia = date(1822, 9, 7)
print(f"🇧🇷 Independência: {independencia}")

# Operações com datas
print(f"\\n📊 INFORMAÇÕES DA DATA:")
print(f"Hoje é: {hoje.strftime('%A, %d de %B de %Y')}")
print(f"Dias desde a independência: {(hoje - independencia).days}")

# Primeiro e último dia do mês
primeiro_dia = hoje.replace(day=1)
if hoje.month == 12:
    ultimo_dia = date(hoje.year + 1, 1, 1) - date.timedelta(days=1)
else:
    ultimo_dia = date(hoje.year, hoje.month + 1, 1) - date.timedelta(days=1)

print(f"\\n📆 DESTE MÊS:")
print(f"Primeiro dia: {primeiro_dia}")
print(f"Último dia: {ultimo_dia}")''',
                'explicacao': 'Use date quando não importa a hora exata'
            },
            {
                'titulo': 'TIMEDELTA: Durações e diferenças',
                'descricao': 'Representa períodos de tempo e permite cálculos',
                'codigo': '''from datetime import datetime, timedelta

agora = datetime.now()

# Criar durações
uma_semana = timedelta(weeks=1)
tres_dias = timedelta(days=3)
duas_horas = timedelta(hours=2)
trinta_minutos = timedelta(minutes=30)

print("⏱️ CALCULANDO COM TEMPO:")
print(f"Agora: {agora.strftime('%d/%m/%Y %H:%M')}")
print(f"Daqui a 1 semana: {(agora + uma_semana).strftime('%d/%m/%Y %H:%M')}")
print(f"Há 3 dias: {(agora - tres_dias).strftime('%d/%m/%Y %H:%M')}")
print(f"Em 2h30min: {(agora + duas_horas + trinta_minutos).strftime('%d/%m/%Y %H:%M')}")

# Diferença entre momentos
inicio_ano = datetime(agora.year, 1, 1)
diferenca = agora - inicio_ano

print(f"\\n📈 DESDE O INÍCIO DO ANO:")
print(f"Dias passados: {diferenca.days}")
print(f"Horas totais: {diferenca.total_seconds() / 3600:.1f}")

# Cálculos úteis
fim_semana = agora + timedelta(days=(5 - agora.weekday()))
print(f"\\n🎉 Próxima sexta: {fim_semana.strftime('%d/%m/%Y')}")''',
                'explicacao': 'timedelta é essencial para cálculos temporais'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.exemplo(exemplo['codigo'])
            print(f"\n🚀 Executando exemplo {i}:")
            self.executar_codigo(exemplo['codigo'])
            
            if exemplo['explicacao']:
                self.print_colored(f"\n💡 QUANDO USAR: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você domina os tipos básicos de datetime!")
        self.pausar()
    
    def _secao_formatacao(self) -> None:
        """Seção: Formatação e parsing de datas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FORMATAÇÃO E PARSING DE DATAS", "🎨", "info")
        
        self.print_colored("Transformar datas em texto bonito e texto em datas!", "text")
        
        codigo_formatacao = '''from datetime import datetime

agora = datetime.now()

print("🎨 FORMATAÇÃO COM STRFTIME (datetime → string)")
print("=" * 50)

# Formatos básicos
print(f"Padrão ISO: {agora.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Brasileiro: {agora.strftime('%d/%m/%Y %H:%M')}")
print(f"Americano: {agora.strftime('%m/%d/%Y %I:%M %p')}")
print(f"Só data: {agora.strftime('%d de %B de %Y')}")
print(f"Só hora: {agora.strftime('%H:%M:%S')}")

# Formatos criativos
print(f"\\n✨ FORMATOS CRIATIVOS:")
print(f"Completo: {agora.strftime('%A, %d de %B de %Y às %H:%M')}")
print(f"Compacto: {agora.strftime('%d%m%y_%H%M')}")
print(f"Timestamp: {agora.strftime('%Y%m%d_%H%M%S')}")
print(f"Por extenso: {agora.strftime('Hoje é %A, dia %d de %B')}")

print(f"\\n📝 CÓDIGOS MAIS USADOS:")
codigos = {
    "%Y": "Ano com 4 dígitos (2024)",
    "%m": "Mês numérico (01-12)",
    "%d": "Dia do mês (01-31)",
    "%H": "Hora 24h (00-23)",
    "%M": "Minuto (00-59)",
    "%S": "Segundo (00-59)",
    "%A": "Nome completo do dia",
    "%B": "Nome completo do mês",
    "%a": "Nome abreviado do dia",
    "%b": "Nome abreviado do mês"
}

for codigo, desc in codigos.items():
    valor = agora.strftime(codigo)
    print(f"  {codigo} → {desc} → '{valor}'")'''
        
        self.exemplo(codigo_formatacao)
        print("\n🚀 Executando formatação:")
        self.executar_codigo(codigo_formatacao)
        
        # === PARSING (TEXTO PARA DATETIME) ===
        input("\n🔸 Pressione ENTER para ver parsing...")
        
        codigo_parsing = '''# STRPTIME: Converter texto em datetime
from datetime import datetime

print("\\n🔄 PARSING COM STRPTIME (string → datetime)")
print("=" * 50)

# Exemplos de conversão
textos_data = [
    ("2024-01-15 14:30:00", "%Y-%m-%d %H:%M:%S"),
    ("15/01/2024 14:30", "%d/%m/%Y %H:%M"),
    ("01/15/2024 2:30 PM", "%m/%d/%Y %I:%M %p"),
    ("15 de Janeiro de 2024", "%d de %B de %Y"),
    ("2024-01-15", "%Y-%m-%d")
]

print("✅ CONVERSÕES BEM-SUCEDIDAS:")
for texto, formato in textos_data:
    try:
        dt = datetime.strptime(texto, formato)
        print(f"'{texto}' → {dt}")
    except ValueError as e:
        print(f"❌ Erro: '{texto}' - {e}")

print(f"\\n🔧 PROCESSAMENTO DE DADOS REAIS:")
# Simulação de parsing de logs
logs_exemplo = [
    "2024-01-15 09:15:30 - Sistema iniciado",
    "2024-01-15 09:16:45 - Usuário logado",
    "2024-01-15 09:45:12 - Backup executado"
]

for log in logs_exemplo:
    # Extrair timestamp do início da linha
    timestamp_str = log.split(" - ")[0]
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    evento = log.split(" - ")[1]
    
    # Reformatar para algo mais legível
    horario_br = timestamp.strftime("%d/%m às %H:%M")
    print(f"📝 {horario_br}: {evento}")

print(f"\\n💡 DICA: Use try/except para dados externos não confiáveis!")'''
        
        self.exemplo(codigo_parsing)
        print("\n🚀 Executando parsing:")
        self.executar_codigo(codigo_parsing)
        
        self.pausar()
    
    def _secao_calculos_temporais(self) -> None:
        """Seção: Cálculos e operações temporais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CÁLCULOS E OPERAÇÕES TEMPORAIS", "🧮", "warning")
        
        self.print_colored("Matemática com tempo: somar, subtrair, comparar!", "text")
        
        codigo_calculos = '''from datetime import datetime, timedelta, date

print("🧮 OPERAÇÕES MATEMÁTICAS COM TEMPO")
print("=" * 50)

agora = datetime.now()
print(f"Momento de referência: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# Adições e subtrações
print(f"\\n➕ ADIÇÕES:")
print(f"+ 7 dias: {(agora + timedelta(days=7)).strftime('%d/%m/%Y')}")
print(f"+ 3 horas: {(agora + timedelta(hours=3)).strftime('%H:%M:%S')}")
print(f"+ 45 minutos: {(agora + timedelta(minutes=45)).strftime('%H:%M:%S')}")
print(f"+ 1 ano aprox: {(agora + timedelta(days=365)).strftime('%d/%m/%Y')}")

print(f"\\n➖ SUBTRAÇÕES:")
print(f"- 30 dias: {(agora - timedelta(days=30)).strftime('%d/%m/%Y')}")
print(f"- 2 horas: {(agora - timedelta(hours=2)).strftime('%H:%M:%S')}")
print(f"- 1 semana: {(agora - timedelta(weeks=1)).strftime('%d/%m/%Y')}")

# Cálculos de diferenças
inicio_ano = datetime(agora.year, 1, 1)
diferenca = agora - inicio_ano

print(f"\\n📊 DIFERENÇAS:")
print(f"Desde início do ano:")
print(f"  📅 {diferenca.days} dias")
print(f"  ⏰ {diferenca.total_seconds() / 3600:.1f} horas")
print(f"  🕐 {diferenca.total_seconds() / 60:.0f} minutos")

# Comparações
natal = datetime(agora.year, 12, 25)
if natal < agora:
    natal = datetime(agora.year + 1, 12, 25)

dias_para_natal = (natal - agora).days
print(f"\\n🎄 Para o Natal faltam: {dias_para_natal} dias")

# Cálculos úteis do dia a dia
print(f"\\n💼 CÁLCULOS ÚTEIS:")

# Próxima segunda-feira
dias_para_segunda = (7 - agora.weekday()) % 7
if dias_para_segunda == 0:
    dias_para_segunda = 7
proxima_segunda = agora + timedelta(days=dias_para_segunda)
print(f"Próxima segunda: {proxima_segunda.strftime('%d/%m/%Y')}")

# Idade em dias (exemplo com data fixa)
nascimento = date(1990, 5, 15)
hoje = date.today()
idade_dias = (hoje - nascimento).days
idade_anos = idade_dias // 365
print(f"Pessoa nascida em {nascimento}: {idade_anos} anos ({idade_dias} dias)")

# Fim do mês
if agora.month == 12:
    fim_mes = datetime(agora.year + 1, 1, 1) - timedelta(days=1)
else:
    fim_mes = datetime(agora.year, agora.month + 1, 1) - timedelta(days=1)
print(f"Fim do mês: {fim_mes.strftime('%d/%m/%Y')}")'''
        
        self.exemplo(codigo_calculos)
        print("\n🚀 Executando cálculos:")
        self.executar_codigo(codigo_calculos)
        
        # === EXEMPLOS AVANÇADOS ===
        input("\n🔸 Pressione ENTER para ver exemplos avançados...")
        
        codigo_avancado = '''# CÁLCULOS AVANÇADOS E ÚTEIS
from datetime import datetime, timedelta

print("\\n🚀 CÁLCULOS AVANÇADOS")
print("=" * 50)

def calcular_idade_precisa(data_nascimento):
    """Calcula idade precisa considerando ano bissexto"""
    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    
    # Verifica se já fez aniversário este ano
    if hoje.month < data_nascimento.month or \\
       (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    
    return idade

def proximo_dia_util(data_ref=None):
    """Encontra o próximo dia útil (segunda a sexta)"""
    if data_ref is None:
        data_ref = date.today()
    
    # 0=segunda, 1=terça, ..., 6=domingo
    if data_ref.weekday() == 4:  # sexta
        return data_ref + timedelta(days=3)  # pula para segunda
    elif data_ref.weekday() == 5:  # sábado
        return data_ref + timedelta(days=2)  # pula para segunda
    elif data_ref.weekday() == 6:  # domingo
        return data_ref + timedelta(days=1)  # pula para segunda
    else:
        return data_ref + timedelta(days=1)  # próximo dia

def tempo_trabalhado_hoje():
    """Simula cálculo de tempo trabalhado"""
    inicio_trabalho = datetime.now().replace(hour=9, minute=0, second=0)
    agora = datetime.now()
    
    if agora < inicio_trabalho:
        return timedelta(0)
    
    # Simula que trabalha até 18h
    fim_trabalho = datetime.now().replace(hour=18, minute=0, second=0)
    if agora > fim_trabalho:
        agora = fim_trabalho
    
    return agora - inicio_trabalho

# Demonstrações
print("🎂 Cálculo de idade precisa:")
nascimentos = [date(1990, 3, 15), date(1985, 12, 25), date(2000, 6, 10)]
for nasc in nascimentos:
    idade = calcular_idade_precisa(nasc)
    print(f"  Nascido em {nasc.strftime('%d/%m/%Y')}: {idade} anos")

print(f"\\n💼 Próximo dia útil: {proximo_dia_util().strftime('%d/%m/%Y')}")

tempo_trab = tempo_trabalhado_hoje()
horas = tempo_trab.total_seconds() // 3600
minutos = (tempo_trab.total_seconds() % 3600) // 60
print(f"⏰ Tempo trabalhado hoje: {int(horas)}h {int(minutos)}min")

# Cálculo de prazo
print(f"\\n📋 CÁLCULO DE PRAZOS:")
data_pedido = datetime.now()
prazo_entrega = 5  # 5 dias úteis

data_entrega = data_pedido
dias_adicionados = 0
while dias_adicionados < prazo_entrega:
    data_entrega += timedelta(days=1)
    # Pula fins de semana
    if data_entrega.weekday() < 5:  # segunda a sexta
        dias_adicionados += 1

print(f"Pedido feito: {data_pedido.strftime('%d/%m/%Y')}")
print(f"Entrega em: {data_entrega.strftime('%d/%m/%Y')} ({prazo_entrega} dias úteis)")'''
        
        self.exemplo(codigo_avancado)
        print("\n🚀 Executando exemplos avançados:")
        self.executar_codigo(codigo_avancado)
        
        self.pausar()
    
    def _secao_fusos_horarios(self) -> None:
        """Seção: Fusos horários e timezone"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FUSOS HORÁRIOS E TIMEZONE", "🌍", "accent")
        
        self.print_colored("Dominando o tempo global: UTC, timezone awareness e conversões!", "text")
        
        codigo_timezone = '''from datetime import datetime, timezone, timedelta
import time

print("🌍 TRABALHANDO COM FUSOS HORÁRIOS")
print("=" * 50)

# Datetime naive vs aware
agora_naive = datetime.now()
agora_utc = datetime.now(timezone.utc)

print("🕐 DATETIME NAIVE vs AWARE:")
print(f"Naive (sem timezone): {agora_naive}")
print(f"Aware (com UTC): {agora_utc}")
print(f"Diferença: Naive não sabe onde está no mundo!")

# UTC - O padrão mundial
print(f"\\n🌐 UTC - TEMPO UNIVERSAL:")
utc_agora = datetime.utcnow()
print(f"UTC agora: {utc_agora}")
print(f"Timestamp Unix: {time.time():.0f}")

# Criando timezones personalizados
brasilia_tz = timezone(timedelta(hours=-3))  # Brasil (UTC-3)
tokyo_tz = timezone(timedelta(hours=9))      # Japão (UTC+9)
london_tz = timezone(timedelta(hours=0))     # Londres (UTC+0)

print(f"\\n⏰ MESMO MOMENTO EM DIFERENTES FUSOS:")
momento_utc = datetime.now(timezone.utc)
print(f"UTC:      {momento_utc.strftime('%H:%M:%S')}")
print(f"Brasília: {momento_utc.astimezone(brasilia_tz).strftime('%H:%M:%S')}")
print(f"Tóquio:   {momento_utc.astimezone(tokyo_tz).strftime('%H:%M:%S')}")
print(f"Londres:  {momento_utc.astimezone(london_tz).strftime('%H:%M:%S')}")

# Convertendo entre fusos
print(f"\\n🔄 CONVERSÕES ENTRE FUSOS:")
reuniao_brasilia = datetime(2024, 6, 15, 14, 30, 0, tzinfo=brasilia_tz)
print(f"Reunião em Brasília: {reuniao_brasilia.strftime('%d/%m/%Y %H:%M %Z')}")

# Converter para outros fusos
reuniao_tokyo = reuniao_brasilia.astimezone(tokyo_tz)
reuniao_london = reuniao_brasilia.astimezone(london_tz)

print(f"Mesmo horário em Tóquio: {reuniao_tokyo.strftime('%d/%m/%Y %H:%M')}")
print(f"Mesmo horário em Londres: {reuniao_london.strftime('%d/%m/%Y %H:%M')}")

# Exemplo prático: Sistema global
print(f"\\n💼 SISTEMA GLOBAL - LOG DE EVENTOS:")
eventos = [
    ("Usuário login", datetime(2024, 1, 15, 9, 30, 0, tzinfo=brasilia_tz)),
    ("Compra realizada", datetime(2024, 1, 15, 22, 45, 0, tzinfo=tokyo_tz)),
    ("Backup executado", datetime(2024, 1, 15, 2, 15, 0, tzinfo=london_tz))
]

print("Todos os eventos convertidos para UTC:")
for evento, dt_local in eventos:
    dt_utc = dt_local.astimezone(timezone.utc)
    print(f"  {dt_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}: {evento}")
    print(f"    (Local: {dt_local.strftime('%H:%M %Z')})")'''
        
        self.exemplo(codigo_timezone)
        print("\n🚀 Executando exemplos de timezone:")
        self.executar_codigo(codigo_timezone)
        
        # === DICAS IMPORTANTES ===
        input("\n🔸 Pressione ENTER para ver dicas importantes...")
        
        self.print_colored("\n💡 DICAS IMPORTANTES SOBRE TIMEZONE:", "warning")
        dicas = [
            "🌐 Sempre use UTC para armazenar datas no banco de dados",
            "📱 Converta para timezone local apenas na interface do usuário",
            "⚠️ Cuidado com horário de verão - use bibliotecas como pytz",
            "🔄 APIs REST devem aceitar e retornar datas em ISO 8601 com timezone",
            "📊 Para logs de sistema, sempre use UTC com timezone explícito"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "text")
        
        self.pausar()
    
    def _secao_casos_praticos(self) -> None:
        """Seção: Casos práticos do mundo real"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CASOS PRÁTICOS DO MUNDO REAL", "💼", "info")
        
        self.print_colored("Aplicações reais de datetime em sistemas profissionais!", "text")
        
        codigo_casos = '''from datetime import datetime, timedelta, timezone
import calendar

print("💼 CASOS PRÁTICOS DO MUNDO REAL")
print("=" * 50)

# 1. SISTEMA DE AGENDAMENTO
def sistema_agendamento():
    print("📅 1. SISTEMA DE AGENDAMENTO")
    print("-" * 30)
    
    # Horários disponíveis (9h às 17h, de hora em hora)
    data_consulta = datetime(2024, 6, 15, 9, 0)
    horarios_disponiveis = []
    
    for i in range(9):  # 9h às 17h
        horario = data_consulta.replace(hour=9+i)
        horarios_disponiveis.append(horario)
    
    print("Horários disponíveis para 15/06/2024:")
    for i, horario in enumerate(horarios_disponiveis, 1):
        print(f"  {i}. {horario.strftime('%H:%M')}")
    
    # Agendar consulta
    consulta_marcada = horarios_disponiveis[2]  # 11h
    print(f"\\n✅ Consulta agendada: {consulta_marcada.strftime('%d/%m/%Y às %H:%M')}")
    
    # Lembrete automático
    lembrete = consulta_marcada - timedelta(hours=24)
    print(f"📱 Lembrete será enviado: {lembrete.strftime('%d/%m às %H:%M')}")

# 2. CONTROLE DE PONTO ELETRÔNICO
def controle_ponto():
    print("\\n⏰ 2. CONTROLE DE PONTO ELETRÔNICO")
    print("-" * 30)
    
    # Simulação de batidas de ponto
    batidas = [
        datetime(2024, 1, 15, 8, 30),   # Entrada
        datetime(2024, 1, 15, 12, 0),   # Saída almoço
        datetime(2024, 1, 15, 13, 30),  # Volta almoço
        datetime(2024, 1, 15, 18, 15)   # Saída
    ]
    
    print("Registros de ponto:")
    tipos = ["🟢 Entrada", "🔴 Saída (Almoço)", "🟢 Retorno", "🔴 Saída"]
    for batida, tipo in zip(batidas, tipos):
        print(f"  {batida.strftime('%H:%M')} - {tipo}")
    
    # Cálculo de horas trabalhadas
    manha = batidas[1] - batidas[0]  # Saída almoço - Entrada
    tarde = batidas[3] - batidas[2]  # Saída - Retorno almoço
    total = manha + tarde
    
    horas = int(total.total_seconds() // 3600)
    minutos = int((total.total_seconds() % 3600) // 60)
    
    print(f"\\n📊 Horas trabalhadas: {horas}h {minutos}min")
    
    # Verificar se cumpriu jornada
    jornada_minima = timedelta(hours=8)
    if total >= jornada_minima:
        print("✅ Jornada cumprida")
    else:
        faltam = jornada_minima - total
        print(f"⚠️ Faltam {int(faltam.total_seconds()//60)} minutos")

# 3. SISTEMA DE BACKUP AUTOMÁTICO
def sistema_backup():
    print("\\n💾 3. SISTEMA DE BACKUP AUTOMÁTICO")
    print("-" * 30)
    
    ultimo_backup = datetime(2024, 1, 10, 3, 0)
    agora = datetime(2024, 1, 15, 14, 30)
    
    print(f"Último backup: {ultimo_backup.strftime('%d/%m/%Y às %H:%M')}")
    print(f"Agora: {agora.strftime('%d/%m/%Y às %H:%M')}")
    
    # Verificar se precisa fazer backup (a cada 3 dias)
    tempo_desde_backup = agora - ultimo_backup
    intervalo_backup = timedelta(days=3)
    
    if tempo_desde_backup >= intervalo_backup:
        print("🚨 BACKUP NECESSÁRIO!")
        proximo_backup = agora.replace(hour=3, minute=0, second=0)
        if proximo_backup <= agora:
            proximo_backup += timedelta(days=1)
        print(f"📅 Próximo backup: {proximo_backup.strftime('%d/%m às %H:%M')}")
    else:
        falta = intervalo_backup - tempo_desde_backup
        print(f"✅ Backup em dia (próximo em {falta.days} dias)")

# 4. RELATÓRIO DE VENDAS POR PERÍODO
def relatorio_vendas():
    print("\\n📊 4. RELATÓRIO DE VENDAS")
    print("-" * 30)
    
    # Vendas do mês (simulação)
    hoje = datetime(2024, 1, 15)
    primeiro_dia = hoje.replace(day=1)
    
    # Último dia do mês
    if hoje.month == 12:
        ultimo_dia = datetime(hoje.year + 1, 1, 1) - timedelta(days=1)
    else:
        ultimo_dia = datetime(hoje.year, hoje.month + 1, 1) - timedelta(days=1)
    
    dias_no_mes = ultimo_dia.day
    dias_passados = hoje.day
    
    print(f"Período: {primeiro_dia.strftime('%d/%m')} a {ultimo_dia.strftime('%d/%m/%Y')}")
    print(f"Progresso: {dias_passados}/{dias_no_mes} dias ({dias_passados/dias_no_mes*100:.1f}%)")
    
    # Simulação de vendas
    vendas_ate_agora = 45_000
    meta_mensal = 80_000
    
    print(f"\\n💰 Vendas até agora: R$ {vendas_ate_agora:,.2f}")
    print(f"🎯 Meta mensal: R$ {meta_mensal:,.2f}")
    
    # Projeção
    media_diaria = vendas_ate_agora / dias_passados
    projecao = media_diaria * dias_no_mes
    
    print(f"📈 Média diária: R$ {media_diaria:,.2f}")
    print(f"📊 Projeção do mês: R$ {projecao:,.2f}")
    
    if projecao >= meta_mensal:
        print("🎉 Meta será atingida!")
    else:
        falta = meta_mensal - projecao
        print(f"⚠️ Faltarão R$ {falta:,.2f} para a meta")

# Executar todos os casos
sistema_agendamento()
controle_ponto()
sistema_backup()
relatorio_vendas()

print("\\n💡 Estes são exemplos reais de como datetime é usado em sistemas profissionais!")'''
        
        self.exemplo(codigo_casos)
        print("\n🚀 Executando casos práticos:")
        self.executar_codigo(codigo_casos)
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre tempo e calendários"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES SOBRE TEMPO E CALENDÁRIOS", "💫", "accent")
        
        self.print_colored("Fatos fascinantes sobre como medimos e percebemos o tempo!", "text")
        
        codigo_curiosidades = '''from datetime import datetime, date, timedelta
import calendar

print("💫 CURIOSIDADES FASCINANTES SOBRE TEMPO")
print("=" * 50)

print("🌍 1. FATOS SOBRE CALENDÁRIOS:")
print("-" * 30)
print("• O ano tem 365.25 dias (por isso anos bissextos a cada 4 anos)")
print("• Mas na verdade são 365.2425 dias (por isso 2100 NÃO será bissexto)")
print("• O calendário gregoriano 'perdeu' 11 dias em 1582")
print("• Setembro tem esse nome por ser o 7º mês (septem) no calendário romano")
print("• Outubro = 8º, Novembro = 9º, Dezembro = 10º")

print("\\n⏰ 2. FATOS SOBRE TEMPO:")
print("-" * 30)
print("• Um dia não tem exatamente 24 horas (varia alguns microssegundos)")
print("• A Terra está desacelerando: dias ficam 1.7ms mais longos por século")
print("• O segundo foi definido pela frequência de vibração do átomo de césio")
print("• Existem 'segundos bissextos' para sincronizar relógios atômicos")

# Demonstrações práticas
print("\\n🧮 3. CÁLCULOS CURIOSOS:")
print("-" * 30)

# Calculando a idade em diferentes unidades
nascimento = date(1990, 5, 15)
hoje = date.today()
idade_timedelta = hoje - nascimento

print(f"Se você nasceu em {nascimento.strftime('%d/%m/%Y')}:")
print(f"  📅 Idade em dias: {idade_timedelta.days:,}")
print(f"  ⏰ Idade em horas: {idade_timedelta.days * 24:,}")
print(f"  💓 Idade em batimentos cardíacos (aprox): {idade_timedelta.days * 24 * 60 * 70:,}")

# Anos bissextos
print(f"\\n🦘 ANOS BISSEXTOS:")
anos_bissextos = [ano for ano in range(2020, 2101) if calendar.isleap(ano)]
print(f"Entre 2020-2100: {len(anos_bissextos)} anos bissextos")
print(f"Próximos 5: {anos_bissextos[:5]}")

# Problema do milênio Y2K
print(f"\\n💻 CURIOSIDADES DE PROGRAMAÇÃO:")
print("• Y2K (2000): Medo de sistemas com anos de 2 dígitos")
print("• Y2038: Unix timestamp vai 'quebrar' em 19/01/2038 às 03:14:07 UTC")
print("• Isso porque usa int32 para contar segundos desde 1970")

# Demonstração Y2038
y2038 = datetime(2038, 1, 19, 3, 14, 7)
print(f"• Data crítica Y2038: {y2038}")
segundos_1970_y2038 = int(y2038.timestamp())
print(f"• Timestamp Y2038: {segundos_1970_y2038:,}")
print(f"• Limite int32: {2**31-1:,}")

print(f"\\n🌙 4. CURIOSIDADES ASTRONÔMICAS:")
print("-" * 30)
print("• Um 'dia sideral' (rotação completa da Terra) = 23h 56min 4s")
print("• A Lua se afasta da Terra 3.8cm por ano")
print("• Marte tem dias de 24h 37min (quase igual à Terra!)")
print("• Em Vênus, um dia dura 243 dias terrestres")

# Cálculo de idade em outros planetas
print(f"\\n🪐 SUA IDADE EM OUTROS PLANETAS:")
if idade_timedelta.days > 0:
    idade_anos = idade_timedelta.days / 365.25
    
    planetas = {
        "Mercúrio": 0.24,
        "Vênus": 0.62,
        "Marte": 1.88,
        "Júpiter": 11.86,
        "Saturno": 29.46
    }
    
    for planeta, periodo in planetas.items():
        idade_planeta = idade_anos / periodo
        print(f"  {planeta}: {idade_planeta:.1f} anos")

print(f"\\n⚡ 5. VELOCIDADE DA LUZ E TEMPO:")
print("-" * 30)
print("• A luz demora 8min 20s para vir do Sol até a Terra")
print("• Quando você vê a lua, está vendo ela como era 1.3s atrás")
print("• GPS precisa compensar relatividade (relógios em satélites)")

# Demonstração de precisão temporal
agora = datetime.now()
print(f"\\n🔬 PRECISÃO TEMPORAL:")
print(f"Agora com microssegundos: {agora}")
print(f"Só microssegundos: {agora.microsecond:,}")
print(f"Em nanosegundos seria: {agora.microsecond * 1000:,} ns")

print(f"\\n🎭 6. CURIOSIDADES CULTURAIS:")
print("-" * 30)
print("• Algumas culturas não têm conceito de 'tempo linear'")
print("• O Japão tem eras baseadas no imperador (ex: Era Reiwa)")
print("• Etiópia usa calendário com 13 meses")
print("• China usa zodíaco de 12 anos + 5 elementos = ciclo de 60 anos")

print(f"\\n💡 MORAL DA HISTÓRIA:")
print("O tempo é mais complexo e fascinante do que parece!")
print("Python datetime nos ajuda a navegar essa complexidade! 🐍⏰")'''
        
        self.exemplo(codigo_curiosidades)
        print("\n🚀 Executando curiosidades:")
        self.executar_codigo(codigo_curiosidades)
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre datas e horas!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Datas e Horas',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual objeto datetime representa apenas a data (sem hora)?',
                        'answer': ['date', 'datetime.date'],
                        'hint': 'É um dos tipos básicos do módulo datetime'
                    },
                    {
                        'question': 'Como você soma 7 dias a uma data?',
                        'answer': ['timedelta(days=7)', '+ timedelta(days=7)'],
                        'hint': 'Use timedelta para representar períodos de tempo'
                    },
                    {
                        'question': 'Qual método converte datetime para string formatada?',
                        'answer': ['strftime', 'strftime()'],
                        'hint': 'str + f + time = string format time'
                    },
                    {
                        'question': 'O que significa UTC?',
                        'answer': ['tempo universal coordenado', 'coordinated universal time', 'utc'],
                        'hint': 'É o padrão mundial de tempo'
                    },
                    {
                        'question': 'Como calcular diferença entre duas datas?',
                        'answer': ['subtracao', 'data1 - data2', 'subtração'],
                        'hint': 'Use operador matemático básico'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete para obter a data de hoje',
                        'starter': 'from datetime import date\nhoje = date.______\nprint(hoje)',
                        'solution': 'today()',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete para formatar data brasileira',
                        'starter': 'from datetime import datetime\nagora = datetime.now()\ndata_br = agora.strftime("______")\nprint(data_br)',
                        'solution': '%d/%m/%Y',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete para adicionar 1 semana',
                        'starter': 'from datetime import datetime, timedelta\nagora = datetime.now()\nproxima_semana = agora + ______\nprint(proxima_semana)',
                        'solution': 'timedelta(weeks=1)',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Calculadora de Tempo Pessoal',
                'type': 'creative',
                'instruction': 'Crie um programa que calcule informações interessantes sobre sua idade: quantos dias você viveu, quantas vezes seu coração bateu, quando você completará 10.000 dias de vida, etc.'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            # Limpa tela antes do menu
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
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre datetime",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios sobre manipulação de datas",
            "🎨 OPÇÃO 3 - Exercício Criativo: Calculadora de tempo pessoal",
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
    
    def _mini_projeto_agenda_temporal(self) -> None:
        """Mini Projeto - Módulo 15: Agenda Temporal Inteligente"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: AGENDA TEMPORAL INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: AGENDA TEMPORAL INTELIGENTE")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar uma agenda que entende tempo como um especialista!")
        
        self.print_concept(
            "Agenda Temporal Inteligente",
            "Um sistema completo de gerenciamento de tempo que trabalha com eventos, lembretes, fusos horários e análises temporais avançadas"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "🏢 Empresas multinacionais com reuniões globais",
            "👨‍⚕️ Clínicas e hospitais com agendamentos complexos",
            "🎓 Universidades com cronogramas acadêmicos",
            "✈️ Companhias aéreas com voos e conexões"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Análise do sistema temporal
        self.print_section("PASSO 1: Criando Sistema Temporal", "📝", "info")
        self.print_tip("Vamos construir um sistema que entende tempo globalmente")
        
        try:
            # === CÓDIGO PRINCIPAL DO PROJETO ===
            codigo_projeto = '''# ⏰ AGENDA TEMPORAL INTELIGENTE
# Sistema avançado de gerenciamento de tempo e eventos

from datetime import datetime, timedelta, timezone, date
import calendar
from typing import List, Dict, Optional
import json

class EventoTemporal:
    """Representa um evento com informações temporais completas"""
    
    def __init__(self, titulo: str, inicio: datetime, fim: datetime = None, 
                 timezone_local: timezone = None, categoria: str = "geral",
                 lembretes: List[int] = None, descricao: str = ""):
        self.titulo = titulo
        self.inicio = inicio
        self.fim = fim or (inicio + timedelta(hours=1))
        self.timezone_local = timezone_local or timezone.utc
        self.categoria = categoria
        self.lembretes = lembretes or [15, 60]  # minutos antes
        self.descricao = descricao
        self.criado_em = datetime.now(timezone.utc)
        self.id = hash(f"{titulo}{inicio}")
    
    def duracao(self) -> timedelta:
        """Retorna duração do evento"""
        return self.fim - self.inicio
    
    def para_timezone(self, tz: timezone) -> 'EventoTemporal':
        """Converte evento para outro timezone"""
        novo_inicio = self.inicio.astimezone(tz)
        novo_fim = self.fim.astimezone(tz)
        
        evento_convertido = EventoTemporal(
            self.titulo, novo_inicio, novo_fim, tz, 
            self.categoria, self.lembretes, self.descricao
        )
        evento_convertido.id = self.id
        return evento_convertido
    
    def conflita_com(self, outro: 'EventoTemporal') -> bool:
        """Verifica se há conflito de horário com outro evento"""
        return not (self.fim <= outro.inicio or self.inicio >= outro.fim)
    
    def tempo_ate_inicio(self) -> timedelta:
        """Calcula tempo até o início do evento"""
        agora = datetime.now(self.timezone_local)
        return self.inicio - agora
    
    def ja_passou(self) -> bool:
        """Verifica se o evento já passou"""
        agora = datetime.now(self.timezone_local)
        return self.fim < agora
    
    def esta_acontecendo(self) -> bool:
        """Verifica se o evento está acontecendo agora"""
        agora = datetime.now(self.timezone_local)
        return self.inicio <= agora <= self.fim
    
    def __str__(self):
        return f"{self.titulo} ({self.inicio.strftime('%d/%m %H:%M')} - {self.duracao()})"

class AgendaTemporalInteligente:
    """Sistema completo de agenda com recursos temporais avançados"""
    
    def __init__(self):
        self.eventos: List[EventoTemporal] = []
        self.timezone_padrao = timezone(timedelta(hours=-3))  # Brasília
        self.configuracoes = {
            "formato_data": "%d/%m/%Y",
            "formato_hora": "%H:%M",
            "dias_antecedencia_relatorio": 7,
            "lembrete_padrao_minutos": [15, 60],
            "horario_trabalho_inicio": 9,
            "horario_trabalho_fim": 18
        }
    
    def adicionar_evento(self, evento: EventoTemporal) -> bool:
        """Adiciona evento verificando conflitos"""
        conflitos = self.verificar_conflitos(evento)
        
        if conflitos:
            print(f"⚠️ CONFLITO DETECTADO!")
            print(f"Evento '{evento.titulo}' conflita com:")
            for conflito in conflitos:
                print(f"  • {conflito.titulo} ({conflito.inicio.strftime('%H:%M')} - {conflito.fim.strftime('%H:%M')})")
            
            resposta = input("Deseja adicionar mesmo assim? (s/n): ").lower()
            if resposta not in ['s', 'sim']:
                return False
        
        self.eventos.append(evento)
        print(f"✅ Evento '{evento.titulo}' adicionado com sucesso!")
        return True
    
    def verificar_conflitos(self, novo_evento: EventoTemporal) -> List[EventoTemporal]:
        """Retorna lista de eventos que conflitam com o novo"""
        conflitos = []
        for evento in self.eventos:
            if evento.conflita_com(novo_evento) and not evento.ja_passou():
                conflitos.append(evento)
        return conflitos
    
    def eventos_do_dia(self, data: date = None) -> List[EventoTemporal]:
        """Retorna eventos de um dia específico"""
        if data is None:
            data = date.today()
        
        eventos_dia = []
        for evento in self.eventos:
            if evento.inicio.date() == data:
                eventos_dia.append(evento)
        
        return sorted(eventos_dia, key=lambda e: e.inicio)
    
    def proximos_eventos(self, dias: int = 7) -> List[EventoTemporal]:
        """Retorna próximos eventos em N dias"""
        agora = datetime.now(self.timezone_padrao)
        limite = agora + timedelta(days=dias)
        
        proximos = []
        for evento in self.eventos:
            if agora <= evento.inicio <= limite:
                proximos.append(evento)
        
        return sorted(proximos, key=lambda e: e.inicio)
    
    def eventos_por_categoria(self) -> Dict[str, List[EventoTemporal]]:
        """Agrupa eventos por categoria"""
        por_categoria = {}
        for evento in self.eventos:
            if evento.categoria not in por_categoria:
                por_categoria[evento.categoria] = []
            por_categoria[evento.categoria].append(evento)
        
        return por_categoria
    
    def relatorio_tempo_livre(self, data: date = None) -> List[Dict]:
        """Calcula períodos livres no dia"""
        if data is None:
            data = date.today()
        
        eventos_dia = self.eventos_do_dia(data)
        if not eventos_dia:
            return [{
                "inicio": "09:00",
                "fim": "18:00", 
                "duracao": "9h",
                "descricao": "Dia totalmente livre"
            }]
        
        # Calcular períodos livres entre eventos
        periodos_livres = []
        
        # Antes do primeiro evento
        primeiro_evento = eventos_dia[0]
        inicio_trabalho = datetime.combine(data, datetime.min.time().replace(hour=9))
        
        if primeiro_evento.inicio > inicio_trabalho:
            duracao = primeiro_evento.inicio - inicio_trabalho
            periodos_livres.append({
                "inicio": "09:00",
                "fim": primeiro_evento.inicio.strftime("%H:%M"),
                "duracao": f"{int(duracao.total_seconds()//3600)}h{int((duracao.total_seconds()%3600)//60):02d}min",
                "descricao": "Período livre manhã"
            })
        
        # Entre eventos
        for i in range(len(eventos_dia) - 1):
            evento_atual = eventos_dia[i]
            proximo_evento = eventos_dia[i + 1]
            
            if evento_atual.fim < proximo_evento.inicio:
                duracao = proximo_evento.inicio - evento_atual.fim
                if duracao.total_seconds() > 900:  # Mais de 15 minutos
                    periodos_livres.append({
                        "inicio": evento_atual.fim.strftime("%H:%M"),
                        "fim": proximo_evento.inicio.strftime("%H:%M"),
                        "duracao": f"{int(duracao.total_seconds()//3600)}h{int((duracao.total_seconds()%3600)//60):02d}min",
                        "descricao": "Intervalo entre eventos"
                    })
        
        return periodos_livres
    
    def calcular_estatisticas_temporais(self) -> Dict:
        """Calcula estatísticas sobre uso do tempo"""
        if not self.eventos:
            return {"erro": "Nenhum evento cadastrado"}
        
        agora = datetime.now(self.timezone_padrao)
        eventos_passados = [e for e in self.eventos if e.ja_passou()]
        eventos_futuros = [e for e in self.eventos if not e.ja_passou()]
        
        # Tempo total gasto em eventos
        tempo_total = sum([e.duracao() for e in eventos_passados], timedelta())
        
        # Por categoria
        tempo_por_categoria = {}
        for categoria, eventos_cat in self.eventos_por_categoria().items():
            tempo_categoria = sum([e.duracao() for e in eventos_cat if e.ja_passou()], timedelta())
            if tempo_categoria.total_seconds() > 0:
                tempo_por_categoria[categoria] = {
                    "horas": tempo_categoria.total_seconds() / 3600,
                    "eventos": len([e for e in eventos_cat if e.ja_passou()])
                }
        
        return {
            "eventos_total": len(self.eventos),
            "eventos_passados": len(eventos_passados),
            "eventos_futuros": len(eventos_futuros),
            "tempo_total_horas": tempo_total.total_seconds() / 3600,
            "tempo_por_categoria": tempo_por_categoria,
            "evento_mais_longo": max(eventos_passados, key=lambda e: e.duracao()).titulo if eventos_passados else "N/A",
            "categoria_mais_usada": max(tempo_por_categoria.keys(), key=lambda k: tempo_por_categoria[k]["horas"]) if tempo_por_categoria else "N/A"
        }
    
    def gerar_relatorio_detalhado(self) -> str:
        """Gera relatório completo da agenda"""
        agora = datetime.now(self.timezone_padrao)
        relatorio = []
        
        relatorio.append("📊 RELATÓRIO TEMPORAL DETALHADO")
        relatorio.append("=" * 50)
        relatorio.append(f"📅 Gerado em: {agora.strftime('%d/%m/%Y às %H:%M')}")
        
        # Eventos de hoje
        hoje = date.today()
        eventos_hoje = self.eventos_do_dia(hoje)
        
        relatorio.append(f"\\n🗓️ EVENTOS DE HOJE ({hoje.strftime('%d/%m/%Y')}):")
        if eventos_hoje:
            for evento in eventos_hoje:
                status = "🔴 Passou" if evento.ja_passou() else "🟡 Agora" if evento.esta_acontecendo() else "🟢 Futuro"
                relatorio.append(f"  {status} {evento.inicio.strftime('%H:%M')} - {evento.titulo} ({evento.categoria})")
        else:
            relatorio.append("  📅 Nenhum evento agendado para hoje")
        
        # Próximos eventos
        proximos = self.proximos_eventos(7)
        relatorio.append(f"\\n📅 PRÓXIMOS 7 DIAS:")
        for evento in proximos[:5]:  # Limitar a 5
            dias_ate = (evento.inicio.date() - hoje).days
            if dias_ate == 0:
                continue
            elif dias_ate == 1:
                quando = "amanhã"
            else:
                quando = f"em {dias_ate} dias"
            relatorio.append(f"  📅 {evento.inicio.strftime('%d/%m')} ({quando}): {evento.titulo}")
        
        # Tempo livre hoje
        tempo_livre = self.relatorio_tempo_livre(hoje)
        relatorio.append(f"\\n⏰ TEMPO LIVRE HOJE:")
        if tempo_livre:
            for periodo in tempo_livre:
                relatorio.append(f"  🕐 {periodo['inicio']} às {periodo['fim']} ({periodo['duracao']})")
        else:
            relatorio.append("  📅 Dia completamente ocupado")
        
        # Estatísticas
        stats = self.calcular_estatisticas_temporais()
        if "erro" not in stats:
            relatorio.append(f"\\n📈 ESTATÍSTICAS:")
            relatorio.append(f"  📊 Total de eventos: {stats['eventos_total']}")
            relatorio.append(f"  ⏰ Tempo total gasto: {stats['tempo_total_horas']:.1f} horas")
            if stats['categoria_mais_usada'] != "N/A":
                relatorio.append(f"  🏆 Categoria mais usada: {stats['categoria_mais_usada']}")
        
        return "\\n".join(relatorio)

# DEMONSTRAÇÃO COMPLETA DO SISTEMA
print("⏰ AGENDA TEMPORAL INTELIGENTE")
print("=" * 60)

# Criar instância da agenda
agenda = AgendaTemporalInteligente()

# Timezones para demonstração
brasilia_tz = timezone(timedelta(hours=-3))
utc_tz = timezone.utc
tokyo_tz = timezone(timedelta(hours=9))

print("\\n📅 CRIANDO EVENTOS DE DEMONSTRAÇÃO...")

# Criar eventos variados
eventos_demo = [
    EventoTemporal(
        "Reunião de Equipe",
        datetime(2024, 6, 15, 9, 0, tzinfo=brasilia_tz),
        datetime(2024, 6, 15, 10, 30, tzinfo=brasilia_tz),
        brasilia_tz,
        "trabalho",
        [15, 60],
        "Reunião semanal da equipe de desenvolvimento"
    ),
    EventoTemporal(
        "Consulta Médica",
        datetime(2024, 6, 15, 14, 30, tzinfo=brasilia_tz),
        datetime(2024, 6, 15, 15, 30, tzinfo=brasilia_tz),
        brasilia_tz,
        "pessoal",
        [60, 1440],  # 1h e 1 dia antes
        "Consulta de rotina"
    ),
    EventoTemporal(
        "Call Internacional",
        datetime(2024, 6, 16, 8, 0, tzinfo=brasilia_tz),
        datetime(2024, 6, 16, 9, 0, tzinfo=brasilia_tz),
        brasilia_tz,
        "trabalho",
        [30],
        "Reunião com time do Japão"
    ),
    EventoTemporal(
        "Academia",
        datetime(2024, 6, 17, 18, 0, tzinfo=brasilia_tz),
        datetime(2024, 6, 17, 19, 30, tzinfo=brasilia_tz),
        brasilia_tz,
        "saude",
        [30],
        "Treino funcional"
    )
]

# Adicionar eventos
for evento in eventos_demo:
    agenda.adicionar_evento(evento)

print(f"\\n✅ {len(eventos_demo)} eventos adicionados com sucesso!")

# Demonstrar conversão de timezone
print("\\n🌍 CONVERSÃO DE TIMEZONE:")
evento_internacional = eventos_demo[2]  # Call Internacional
print(f"🇧🇷 Brasília: {evento_internacional.inicio.strftime('%d/%m %H:%M')}")

evento_tokyo = evento_internacional.para_timezone(tokyo_tz)
evento_utc = evento_internacional.para_timezone(utc_tz)

print(f"🇯🇵 Tóquio:   {evento_tokyo.inicio.strftime('%d/%m %H:%M')}")
print(f"🌍 UTC:      {evento_utc.inicio.strftime('%d/%m %H:%M')}")

# Verificação de conflitos
print("\\n⚠️ TESTE DE CONFLITO:")
evento_conflitante = EventoTemporal(
    "Reunião Conflitante",
    datetime(2024, 6, 15, 9, 30, tzinfo=brasilia_tz),
    datetime(2024, 6, 15, 10, 0, tzinfo=brasilia_tz),
    brasilia_tz,
    "trabalho"
)

conflitos = agenda.verificar_conflitos(evento_conflitante)
if conflitos:
    print(f"🚨 Conflito detectado com: {conflitos[0].titulo}")
else:
    print("✅ Nenhum conflito encontrado")

# Relatórios
print("\\n📊 EVENTOS POR CATEGORIA:")
por_categoria = agenda.eventos_por_categoria()
for categoria, eventos in por_categoria.items():
    print(f"  📂 {categoria.title()}: {len(eventos)} eventos")

print("\\n⏰ ANÁLISE DE TEMPO LIVRE:")
data_teste = date(2024, 6, 15)
tempo_livre = agenda.relatorio_tempo_livre(data_teste)
for periodo in tempo_livre:
    print(f"  🕐 {periodo['inicio']} às {periodo['fim']}: {periodo['descricao']} ({periodo['duracao']})")

# Estatísticas
print("\\n📈 ESTATÍSTICAS TEMPORAIS:")
stats = agenda.calcular_estatisticas_temporais()
if "erro" not in stats:
    print(f"  📊 Total de eventos: {stats['eventos_total']}")
    print(f"  📅 Eventos futuros: {stats['eventos_futuros']}")
    print(f"  ⏰ Tempo total: {stats['tempo_total_horas']:.1f} horas")
    
    if stats['tempo_por_categoria']:
        print("  📂 Por categoria:")
        for cat, info in stats['tempo_por_categoria'].items():
            print(f"    • {cat}: {info['horas']:.1f}h ({info['eventos']} eventos)")

# Relatório completo
print("\\n" + "="*60)
print(agenda.gerar_relatorio_detalhado())

print("\\n🎉 AGENDA TEMPORAL FUNCIONANDO PERFEITAMENTE!")
print("💡 Conceitos aplicados:")
print("  • Criação e manipulação de objetos datetime")
print("  • Cálculos temporais avançados")
print("  • Conversões entre timezones")
print("  • Detecção de conflitos temporais")
print("  • Análise estatística de uso do tempo")
print("  • Formatação e apresentação de dados temporais")
print("  • Programação orientada a objetos com datetime")'''
            
            # === CÓDIGO FINAL GERADO ===
            self.print_colored("Aqui está o código completo que você criou:", "text")
            
            self.exemplo(codigo_projeto)
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.executar_codigo(codigo_projeto)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou uma agenda temporal inteligente!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Integrar com APIs de calendário (Google Calendar, Outlook)",
            "Adicionar notificações push para lembretes",
            "Implementar sincronização entre dispositivos",
            "Criar interface web com Flask/Django",
            "Adicionar machine learning para sugestões de horários",
            "Integrar com sistemas de videoconferência (Zoom, Teams)"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre do Tempo Python!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Agenda Temporal Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo15Datetime()
    print("Teste do módulo 15 - versão standalone")
    module._datetime_interativo()