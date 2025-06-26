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
            self._operacoes_matematicas()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _operacoes_matematicas(self) -> None:
        """Conteúdo principal sobre operações matemáticas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧮 MÓDULO 6: OPERAÇÕES MATEMÁTICAS")
        else:
            print("\n" + "="*50)
            print("🧮 MÓDULO 6: OPERAÇÕES MATEMÁTICAS")
            print("="*50)
        
        print("Python é uma calculadora poderosa!")
        
        codigo = '''# Operações básicas
a = 10
b = 3

print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b:.2f}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto: {a} % {b} = {a % b}")
print(f"Potência: {a} ** 2 = {a ** 2}")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.pausar()
        
        self.exercicio(
            "Qual operador usamos para calcular o resto de uma divisão?",
            "%",
            "É um símbolo de porcentagem"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_calculadora_financeira()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_calculadora_financeira(self) -> None:
        """Mini Projeto - Módulo 6: Calculadora Financeira Inteligente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CALCULADORA FINANCEIRA INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CALCULADORA FINANCEIRA INTELIGENTE")
            print("="*50)
        
        print("💰 Vamos criar uma calculadora para planejamento financeiro!")
        print("Sistema usado em:")
        print("• Apps bancários (Nubank, Itaú)")
        print("• Consultorias financeiras")
        print("• Sistemas de investimento")
        print("• Planilhas empresariais")
        
        self.pausar()
        
        print("\n💻 Calculadora completa com análises automáticas:")
        
        codigo_financeiro = '''# 💰 CALCULADORA FINANCEIRA INTELIGENTE
print("💰" * 30)
print("     CALCULADORA FINANCEIRA V2.0")
print("💰" * 30)

# Dados financeiros de entrada
salario_bruto = 5000.00
desconto_inss = salario_bruto * 0.11        # 11% INSS
desconto_ir = salario_bruto * 0.075         # 7.5% IR
salario_liquido = salario_bruto - desconto_inss - desconto_ir

print(f"\\n📊 ANÁLISE SALARIAL:")
print(f"💵 Salário Bruto: R$ {salario_bruto:.2f}")
print(f"📉 INSS (11%): R$ {desconto_inss:.2f}")
print(f"📉 IR (7.5%): R$ {desconto_ir:.2f}")
print(f"💚 Salário Líquido: R$ {salario_liquido:.2f}")

# Planejamento de gastos (regra 50-30-20)
gastos_essenciais = salario_liquido * 0.50   # 50% necessidades
gastos_desejos = salario_liquido * 0.30       # 30% desejos
poupanca = salario_liquido * 0.20             # 20% poupança

print(f"\\n🎯 PLANEJAMENTO INTELIGENTE (50-30-20):")
print(f"🏠 Gastos Essenciais (50%): R$ {gastos_essenciais:.2f}")
print(f"🎮 Gastos com Desejos (30%): R$ {gastos_desejos:.2f}")
print(f"💎 Poupança (20%): R$ {poupanca:.2f}")

# Projeções de investimento
taxa_rendimento_anual = 0.10  # 10% ao ano
meses = 12
rendimento_mensal = taxa_rendimento_anual / 12
valor_futuro_1_ano = poupanca * meses * (1 + rendimento_mensal)

print(f"\\n📈 PROJEÇÃO DE INVESTIMENTOS:")
print(f"💰 Poupança mensal: R$ {poupanca:.2f}")
print(f"📅 Em 12 meses: R$ {valor_futuro_1_ano:.2f}")
print(f"🚀 Rendimento estimado: R$ {valor_futuro_1_ano - (poupanca * meses):.2f}")

# Metas financeiras
meta_emergencia = salario_liquido * 6        # 6 meses de reserva
meses_para_meta = meta_emergencia / poupanca

print(f"\\n🎯 METAS FINANCEIRAS:")
print(f"🛡️  Reserva de Emergência (6 meses): R$ {meta_emergencia:.2f}")
print(f"⏰ Tempo para atingir: {meses_para_meta:.1f} meses")

# Análise de comprometimento
percentual_comprometido = ((gastos_essenciais + gastos_desejos) / salario_liquido) * 100

print(f"\\n📊 ANÁLISE DE COMPROMETIMENTO:")
print(f"📈 Renda comprometida: {percentual_comprometido:.1f}%")

if percentual_comprometido <= 80:
    situacao = "🟢 EXCELENTE - Finanças controladas!"
elif percentual_comprometido <= 90:
    situacao = "🟡 ATENÇÃO - Cuidado com os gastos"
else:
    situacao = "🔴 CRÍTICO - Reorganize suas finanças"

print(f"🎯 Situação: {situacao}")

print("\\n💰" * 30)
print("     ANÁLISE CONCLUÍDA!")
print("💰" * 30)'''
        
        self.exemplo(codigo_financeiro)
        self.executar_codigo(codigo_financeiro)
        
        print("\n🎉 CALCULADORA FINANCEIRA CRIADA!")
        print("\n🌍 ONDE ESSA TECNOLOGIA É USADA:")
        print("• 🏦 Bancos: Análise de crédito e planejamento")
        print("• 💳 Fintechs: Apps de controle financeiro")
        print("• 🏢 Empresas: Orçamentos e projeções")
        print("• 📊 Consultorias: Relatórios para clientes")
        print("• 🎓 Educação: Simuladores financeiros")
        
        print("\n💡 MATEMÁTICA FINANCEIRA APLICADA:")
        print("• Cálculo de percentuais automatizado")
        print("• Projeções de crescimento")
        print("• Regra 50-30-20 (planejamento inteligente)")
        print("• Análise de risco financeiro")
        print("• Metas SMART (específicas e mensuráveis)")
        
        print("\n🏆 CONQUISTA: Analista Financeiro!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Calculadora Financeira Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo06Operacoes()
    print("Teste do módulo 6 - versão standalone")
    module._operacoes_matematicas()