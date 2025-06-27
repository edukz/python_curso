#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 13: Funções Avançadas
Aprenda sobre *args, **kwargs, lambda e programação funcional
"""

from ..shared.base_module import BaseModule


class Modulo13FuncoesAvancadas(BaseModule):
    """Módulo 13: Funções Avançadas & Lambda"""
    
    def __init__(self):
        super().__init__("modulo_13", "Funções Avançadas & Lambda")
        self.has_mini_project = True
        self.mini_project_points = 70
    
    def execute(self) -> None:
        """Executa o módulo sobre funções avançadas"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._funcoes_avancadas()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _funcoes_avancadas(self) -> None:
        """Conteúdo principal sobre funções avançadas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ MÓDULO 13: FUNÇÕES AVANÇADAS & LAMBDA")
        else:
            print("\n" + "="*50)
            print("⚡ MÓDULO 13: FUNÇÕES AVANÇADAS & LAMBDA")
            print("="*50)
        
        self.print_concept("⚡ Vamos dominar funcionalidades AVANÇADAS de funções!")
        self.print_concept("🚀 Lambda, *args, **kwargs e muito mais!")
        
        self.print_section("PARÂMETROS FLEXÍVEIS")
        
        self.print_concept("🎯 *args = argumentos posicionais variáveis")
        self.print_concept("🎯 **kwargs = argumentos nomeados variáveis")
        self.print_tip("✨ Tornam funções muito mais flexíveis!")
        
        codigo1 = '''# *args - argumentos posicionais variáveis
def somar_todos(*numeros):
    """Soma qualquer quantidade de números"""
    print(f"Recebido: {numeros}")  # É uma tupla
    total = 0
    for num in numeros:
        total += num
    return total

# Testando *args
print("=== TESTANDO *ARGS ===")
print("Soma de 1, 2, 3:", somar_todos(1, 2, 3))
print("Soma de 10, 20:", somar_todos(10, 20))
print("Soma de 1, 2, 3, 4, 5, 6:", somar_todos(1, 2, 3, 4, 5, 6))

# **kwargs - argumentos nomeados variáveis
def criar_perfil(nome, **informacoes):
    """Cria perfil com informações flexíveis"""
    print(f"\\n=== PERFIL DE {nome.upper()} ===")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

# Testando **kwargs
print("\\n=== TESTANDO **KWARGS ===")
criar_perfil("João", idade=25, cidade="São Paulo", profissao="Programador")
criar_perfil("Maria", idade=30, empresa="TechCorp", salario=8000, hobbies="Natação")

# Combinando tudo
def funcao_completa(obrigatorio, padrao="valor padrão", *args, **kwargs):
    """Função com todos os tipos de parâmetros"""
    print(f"\\nObrigatório: {obrigatorio}")
    print(f"Padrão: {padrao}")
    print(f"Args extras: {args}")
    print(f"Kwargs extras: {kwargs}")

print("\\n=== FUNÇÃO COMPLETA ===")
funcao_completa("necessário", "customizado", 1, 2, 3, nome="Python", ano=2023)'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.print_section("⚡ LAMBDA - Funções Anônimas")
        
        codigo2 = '''# Lambda - funções anônimas
print("=== FUNÇÕES LAMBDA ===")

# Função normal vs Lambda
def quadrado_normal(x):
    return x ** 2

quadrado_lambda = lambda x: x ** 2

print(f"Quadrado normal de 5: {quadrado_normal(5)}")
print(f"Quadrado lambda de 5: {quadrado_lambda(5)}")

# Lambdas com múltiplos parâmetros
somar = lambda a, b: a + b
maior = lambda a, b: a if a > b else b

print(f"\\nSoma 10 + 20 = {somar(10, 20)}")
print(f"Maior entre 15 e 8 = {maior(15, 8)}")

# Lambdas em listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - aplica função a todos elementos
quadrados = list(map(lambda x: x**2, numeros))
print(f"\\nQuadrados: {quadrados}")

# filter() - filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Exemplo prático - lista de dicionários
pessoas = [
    {"nome": "Ana", "idade": 25, "salario": 5000},
    {"nome": "Bruno", "idade": 30, "salario": 6000},
    {"nome": "Carlos", "idade": 35, "salario": 7000}
]

# Ordenar por idade
por_idade = sorted(pessoas, key=lambda p: p["idade"])
print(f"\\nPor idade: {[p['nome'] for p in por_idade]}")

# Ordenar por salário (decrescente)
por_salario = sorted(pessoas, key=lambda p: p["salario"], reverse=True)
print(f"Por salário: {[p['nome'] for p in por_salario]}")

# Filtrar salário > 5500
bem_pagos = list(filter(lambda p: p["salario"] > 5500, pessoas))
print(f"Bem pagos: {[p['nome'] for p in bem_pagos]}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.exercicio(
            "Como criar uma função lambda que multiplica dois números?",
            ["lambda a, b: a * b", "lambda x, y: x * y"],
            "lambda a, b: a * b"
        )
        
        # Mini Projeto do Módulo 13
        self._mini_projeto_processador_dados()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_processador_dados(self) -> None:
        """Mini Projeto - Módulo 13: Sistema de Processamento de Dados com Lambda"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: PROCESSADOR DE DADOS AVANÇADO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: PROCESSADOR DE DADOS AVANÇADO")
            print("="*50)
        
        self.print_concept("🧮 Sistema de análise de dados usando funções lambda e avançadas!")
        self.print_tip("🛠️ Usando: Lambda, map(), filter(), reduce(), *args, **kwargs")
        
        self.pausar()
        
        codigo_projeto = '''# 🧮 SISTEMA DE PROCESSAMENTO DE DADOS AVANÇADO
# Projeto usando lambdas, map, filter, reduce e funções avançadas

from functools import reduce
import statistics
from datetime import datetime

class ProcessadorDados:
    def __init__(self):
        self.transformacoes = {}  # Armazena funções de transformação
        self.historico_operacoes = []
    
    def registrar_transformacao(self, nome, funcao):
        """Registra uma função de transformação personalizada"""
        self.transformacoes[nome] = funcao
        print(f"✅ Transformação '{nome}' registrada")
    
    def processar_vendas(self, *vendas, **configuracoes):
        """Processa dados de vendas com configurações flexíveis"""
        # Configurações padrão
        config = {
            "aplicar_desconto": False,
            "desconto_percentual": 0,
            "filtrar_minimo": 0,
            "moeda": "R$",
            "debug": False
        }
        config.update(configuracoes)  # Atualiza com parâmetros passados
        
        if config["debug"]:
            print(f"📊 Processando {len(vendas)} vendas com config: {config}")
        
        # Converter para lista se necessário
        dados_vendas = list(vendas)
        
        # Aplicar filtro de valor mínimo (usando filter + lambda)
        if config["filtrar_minimo"] > 0:
            dados_vendas = list(filter(
                lambda x: x >= config["filtrar_minimo"], 
                dados_vendas
            ))
        
        # Aplicar desconto (usando map + lambda)
        if config["aplicar_desconto"]:
            desconto = config["desconto_percentual"] / 100
            dados_vendas = list(map(
                lambda x: x * (1 - desconto), 
                dados_vendas
            ))
        
        # Registrar operação
        operacao = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "vendas_processadas": len(dados_vendas),
            "configuracao": config.copy()
        }
        self.historico_operacoes.append(operacao)
        
        return dados_vendas
    
    def analisar_dados(self, dados, *operacoes_customizadas):
        """Análise avançada de dados usando lambdas"""
        if not dados:
            return {"erro": "Dados vazios"}
        
        # Análises básicas com lambdas
        analises = {
            "total": reduce(lambda x, y: x + y, dados),
            "quantidade": len(dados),
            "maior_valor": reduce(lambda x, y: x if x > y else y, dados),
            "menor_valor": reduce(lambda x, y: x if x < y else y, dados),
            "media": sum(dados) / len(dados),
        }
        
        # Análises estatísticas
        if len(dados) > 1:
            analises.update({
                "mediana": statistics.median(dados),
                "desvio_padrao": statistics.stdev(dados)
            })
        
        # Categorização usando lambdas
        categorizar_venda = lambda x: ("Alta" if x > 1000 else 
                                     "Média" if x > 500 else "Baixa")
        
        analises["categorias"] = {
            "alta": len(list(filter(lambda x: x > 1000, dados))),
            "media": len(list(filter(lambda x: 500 <= x <= 1000, dados))),
            "baixa": len(list(filter(lambda x: x < 500, dados)))
        }
        
        # Aplicar operações customizadas se fornecidas
        for i, operacao in enumerate(operacoes_customizadas):
            if callable(operacao):
                try:
                    resultado = operacao(dados)
                    analises[f"custom_{i+1}"] = resultado
                except Exception as e:
                    analises[f"custom_{i+1}_erro"] = str(e)
        
        return analises
    
    def pipeline_transformacao(self, dados, *nomes_transformacoes):
        """Aplica pipeline de transformações registradas"""
        resultado = dados.copy()
        
        for nome in nomes_transformacoes:
            if nome in self.transformacoes:
                try:
                    # Aplica transformação
                    if isinstance(resultado, list):
                        resultado = list(map(self.transformacoes[nome], resultado))
                    else:
                        resultado = self.transformacoes[nome](resultado)
                    print(f"✅ Aplicada transformação: {nome}")
                except Exception as e:
                    print(f"❌ Erro na transformação {nome}: {e}")
                    break
            else:
                print(f"⚠️ Transformação '{nome}' não encontrada")
        
        return resultado
    
    def relatorio_detalhado(self, dados, titulo="Relatório de Dados"):
        """Gera relatório detalhado formatado"""
        print(f"\\n{'='*50}")
        print(f"📊 {titulo.upper()}")
        print(f"{'='*50}")
        
        analise = self.analisar_dados(dados)
        
        print(f"📈 Total: R$ {analise['total']:,.2f}")
        print(f"📊 Quantidade: {analise['quantidade']} itens")
        print(f"💰 Maior venda: R$ {analise['maior_valor']:,.2f}")
        print(f"💵 Menor venda: R$ {analise['menor_valor']:,.2f}")
        print(f"📊 Média: R$ {analise['media']:,.2f}")
        
        if 'mediana' in analise:
            print(f"📊 Mediana: R$ {analise['mediana']:,.2f}")
            print(f"📊 Desvio Padrão: R$ {analise['desvio_padrao']:,.2f}")
        
        print(f"\\n🎯 CATEGORIZAÇÃO:")
        cats = analise['categorias']
        print(f"  🔥 Vendas Altas (>R$1000): {cats['alta']}")
        print(f"  📊 Vendas Médias (R$500-1000): {cats['media']}")
        print(f"  📉 Vendas Baixas (<R$500): {cats['baixa']}")
        
        return analise

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE PROCESSAMENTO DE DADOS ===\\n")

# Criar instância
processor = ProcessadorDados()

# Dados de exemplo - vendas do mês
vendas_janeiro = [1200, 800, 450, 1500, 300, 950, 1800, 600, 750, 1100, 400, 2000]

print("📊 DADOS ORIGINAIS:")
print(f"Vendas Janeiro: {vendas_janeiro}")

# 1. PROCESSAMENTO BÁSICO
print("\\n🔧 PROCESSAMENTO COM CONFIGURAÇÕES:")

# Processar com desconto
vendas_com_desconto = processor.processar_vendas(
    *vendas_janeiro,
    aplicar_desconto=True,
    desconto_percentual=10,
    filtrar_minimo=500,
    debug=True
)

print(f"Vendas após desconto 10% e filtro >R$500: {[f'{v:.0f}' for v in vendas_com_desconto]}")

# 2. REGISTRAR TRANSFORMAÇÕES CUSTOMIZADAS
print("\\n⚙️ REGISTRANDO TRANSFORMAÇÕES:")

# Lambda para converter para dólar (cotação fictícia R$ 5,20)
processor.registrar_transformacao("para_dolar", lambda x: x / 5.2)

# Lambda para aplicar taxa de comissão
processor.registrar_transformacao("comissao_5", lambda x: x * 0.05)

# Lambda para arredondar
processor.registrar_transformacao("arredondar", lambda x: round(x, 2))

# 3. APLICAR PIPELINE DE TRANSFORMAÇÕES
print("\\n🔄 PIPELINE DE TRANSFORMAÇÕES:")
vendas_em_dolar = processor.pipeline_transformacao(
    vendas_com_desconto,
    "para_dolar",
    "arredondar"
)

print(f"Vendas em dólares: {vendas_em_dolar}")

# 4. ANÁLISES AVANÇADAS COM OPERAÇÕES CUSTOMIZADAS
print("\\n🧮 ANÁLISES CUSTOMIZADAS:")

# Operações customizadas usando lambdas
operacao_bonus = lambda dados: sum(v for v in dados if v > 1000) * 0.02
operacao_meta = lambda dados: len([v for v in dados if v > 800]) / len(dados) * 100

analise = processor.analisar_dados(
    vendas_janeiro,
    operacao_bonus,  # Bônus de 2% para vendas >1000
    operacao_meta    # Percentual que atingiu meta de 800
)

print(f"💰 Bônus total (2% vendas >R$1000): R$ {analise.get('custom_1', 0):.2f}")
print(f"🎯 Percentual que atingiu meta: {analise.get('custom_2', 0):.1f}%")

# 5. RELATÓRIO FINAL
processor.relatorio_detalhado(vendas_janeiro, "Vendas Janeiro 2024")

# 6. HISTÓRICO DE OPERAÇÕES
print(f"\\n📝 HISTÓRICO DE OPERAÇÕES ({len(processor.historico_operacoes)}):")
for i, op in enumerate(processor.historico_operacoes, 1):
    print(f"  {i}. {op['timestamp']} - {op['vendas_processadas']} vendas processadas")

print("\\n🎉 Sistema de Processamento funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Funções lambda para transformações rápidas")
print("  • map(), filter(), reduce() para processamento")
print("  • *args e **kwargs para flexibilidade")
print("  • Pipeline de transformações")
print("  • Análises estatísticas avançadas")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        self.print_success("🏆 PARABÉNS! Sistema de processamento de dados criado!")
        self.print_tip("🎯 Aplicação real: análise de vendas, business intelligence, ETL")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Processador de Dados Avançado")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo13FuncoesAvancadas()
    print("Teste do módulo 13 - versão standalone")
    module._funcoes_avancadas()