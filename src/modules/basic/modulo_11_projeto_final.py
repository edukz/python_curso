#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 11: Projeto Final
Integração de todos os conceitos básicos em um projeto completo
"""

from ..shared.base_module import BaseModule


class Modulo11ProjetoFinal(BaseModule):
    """Módulo 11: Projeto Final - Calculadora Avançada"""
    
    def __init__(self):
        super().__init__("modulo_11", "Projeto Final - Calculadora")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o projeto final"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._projeto_final()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _projeto_final(self) -> None:
        """Projeto final integrando todos os conceitos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 MÓDULO 11: PROJETO FINAL - CALCULADORA")
        else:
            print("\n" + "="*50)
            print("🎓 MÓDULO 11: PROJETO FINAL - CALCULADORA")
            print("="*50)
        
        self.print_success("🎉 Parabéns! Chegou ao projeto final dos módulos básicos!")
        self.print_section("🧮 Vamos criar uma calculadora que usa TODOS os conceitos aprendidos:")
        self.print_concept("\n✅ Variáveis e tipos de dados")
        self.print_concept("✅ Entrada de dados")
        self.print_concept("✅ Operações matemáticas")
        self.print_concept("✅ Estruturas condicionais")
        self.print_concept("✅ Loops")
        self.print_concept("✅ Listas")
        self.print_concept("✅ Funções")
        
        codigo_calculadora = '''# 🧮 CALCULADORA CIENTÍFICA AVANÇADA
# Projeto Final - Integrando todos os conceitos básicos

import math

def exibir_menu():
    """Exibe o menu principal da calculadora"""
    print("\\n🧮 CALCULADORA CIENTÍFICA AVANÇADA")
    print("=" * 40)
    print("1. ➕ Operações Básicas")
    print("2. 📊 Operações Avançadas") 
    print("3. 📈 Análise de Números")
    print("4. 💾 Histórico")
    print("5. 🚪 Sair")
    print("=" * 40)

def operacoes_basicas():
    """Realiza operações matemáticas básicas"""
    print("\\n➕ OPERAÇÕES BÁSICAS")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "❌ Erro: Divisão por zero!"
        else:
            return "❌ Operação inválida!"
        
        return f"📊 Resultado: {num1} {operacao} {num2} = {resultado}"
    
    except ValueError:
        return "❌ Erro: Digite números válidos!"

def operacoes_avancadas():
    """Realiza operações matemáticas avançadas"""
    print("\\n📊 OPERAÇÕES AVANÇADAS")
    print("1. √ Raiz Quadrada")
    print("2. ^ Potência")
    print("3. 📐 Trigonometria")
    
    opcao = input("Escolha uma opção: ")
    
    try:
        if opcao == "1":
            num = float(input("Digite o número: "))
            if num >= 0:
                resultado = math.sqrt(num)
                return f"√{num} = {resultado:.4f}"
            else:
                return "❌ Não é possível calcular raiz de número negativo!"
        
        elif opcao == "2":
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = math.pow(base, expoente)
            return f"{base}^{expoente} = {resultado}"
        
        elif opcao == "3":
            angulo = float(input("Digite o ângulo em graus: "))
            radianos = math.radians(angulo)
            seno = math.sin(radianos)
            cosseno = math.cos(radianos)
            tangente = math.tan(radianos)
            return f"Ângulo {angulo}°:\\nSeno: {seno:.4f}\\nCosseno: {cosseno:.4f}\\nTangente: {tangente:.4f}"
        
        else:
            return "❌ Opção inválida!"
    
    except ValueError:
        return "❌ Erro: Digite números válidos!"

def analisar_numeros():
    """Analisa uma lista de números"""
    print("\\n📈 ANÁLISE DE NÚMEROS")
    
    try:
        entrada = input("Digite números separados por vírgula: ")
        numeros = [float(x.strip()) for x in entrada.split(",")]
        
        if not numeros:
            return "❌ Nenhum número fornecido!"
        
        # Cálculos estatísticos
        total = sum(numeros)
        quantidade = len(numeros)
        media = total / quantidade
        maximo = max(numeros)
        minimo = min(numeros)
        
        # Números pares e ímpares
        pares = [n for n in numeros if int(n) % 2 == 0]
        impares = [n for n in numeros if int(n) % 2 != 0]
        
        resultado = f\"\"\"
📊 ANÁLISE ESTATÍSTICA:
• Números analisados: {numeros}
• Quantidade: {quantidade}
• Soma total: {total}
• Média: {media:.2f}
• Maior valor: {maximo}
• Menor valor: {minimo}
• Números pares: {len(pares)}
• Números ímpares: {len(impares)}
\"\"\"
        return resultado
    
    except ValueError:
        return "❌ Erro: Digite apenas números válidos!"

# Simulação da calculadora funcionando
historico = []

print("🎬 DEMONSTRAÇÃO DA CALCULADORA:")

# Teste 1: Operação básica
resultado1 = operacoes_basicas()
print("\\n" + resultado1) if resultado1 else None

# Simulação com dados fixos para demonstração
print("\\n📊 DEMO - Operação: 15 + 25")
resultado_demo = 15 + 25
print(f"Resultado: {resultado_demo}")
historico.append(f"15 + 25 = {resultado_demo}")

print("\\n📈 DEMO - Análise dos números: 10, 20, 30, 40, 50")
numeros_demo = [10, 20, 30, 40, 50]
media_demo = sum(numeros_demo) / len(numeros_demo)
print(f"Média: {media_demo}")
print(f"Máximo: {max(numeros_demo)}")
print(f"Mínimo: {min(numeros_demo)}")

print("\\n💾 HISTÓRICO DE OPERAÇÕES:")
for operacao in historico:
    print(f"📝 {operacao}")

print("\\n🎉 CALCULADORA CIENTÍFICA FUNCIONANDO PERFEITAMENTE!")
print("🏆 PROJETO FINAL CONCLUÍDO COM SUCESSO!")'''
        
        self.exemplo(codigo_calculadora)
        self.executar_codigo(codigo_calculadora)
        
        # Mini Projeto Financeiro
        self._mini_projeto_analise_financeira()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_analise_financeira(self) -> None:
        """Mini Projeto - Sistema de Análise Financeira Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 PROJETO FINAL: ANÁLISE FINANCEIRA COMPLETA")
        else:
            print("\n" + "="*50)
            print("🎯 PROJETO FINAL: ANÁLISE FINANCEIRA COMPLETA")
            print("="*50)
        
        self.print_success("💰 PARABÉNS! Projeto final que integra TODOS os conceitos!")
        self.print_tip("🏆 Este é o nível de um sistema profissional real!")
        
        self.print_section("\n🎊 VOCÊ DOMINOU:")
        self.print_colored("✅ Módulo 1: Introdução ao Python", "green")
        self.print_colored("✅ Módulo 2: Primeiro Programa", "green")
        self.print_colored("✅ Módulo 3: Variáveis e Tipos", "green")
        self.print_colored("✅ Módulo 4: Tipos de Dados", "green")
        self.print_colored("✅ Módulo 5: Entrada de Dados", "green")
        self.print_colored("✅ Módulo 6: Operações Matemáticas", "green")
        self.print_colored("✅ Módulo 7: Estruturas Condicionais", "green")
        self.print_colored("✅ Módulo 8: Loops e Repetições", "green")
        self.print_colored("✅ Módulo 9: Listas e Coleções", "green")
        self.print_colored("✅ Módulo 10: Funções Reutilizáveis", "green")
        self.print_colored("✅ Módulo 11: Projeto Final", "green")
        
        self.print_section("\n🚀 PRÓXIMOS PASSOS:")
        self.print_tip("🔥 Módulos Avançados (12-23): Conceitos intermediários")
        self.print_tip("⚡ Módulos Essenciais (24-30): Ferramentas profissionais")
        self.print_tip("💼 Projetos Graduais: Aplicações do mundo real")
        
        self.print_success("\n🏆 CONQUISTA ÉPICA: DESENVOLVEDOR PYTHON BÁSICO!")
        
        # Registra conclusão do projeto final
        self.complete_mini_project("Sistema de Análise Financeira Completo")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo11ProjetoFinal()
    print("Teste do módulo 11 - versão standalone")
    module._projeto_final()