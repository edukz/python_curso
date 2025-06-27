#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 4: Tipos de Dados
Aprenda sobre os tipos fundamentais de dados em Python
"""

from ..shared.base_module import BaseModule


class Modulo04TiposDados(BaseModule):
    """Módulo 4: Tipos de Dados - O DNA das Informações"""
    
    def __init__(self):
        super().__init__("modulo_4", "Tipos de Dados")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo sobre tipos de dados"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._tipos_dados()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _tipos_dados(self) -> None:
        """Conteúdo principal sobre tipos de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧬 MÓDULO 4: TIPOS DE DADOS - O DNA DAS INFORMAÇÕES")
        else:
            print("\n" + "="*50)
            print("🧬 MÓDULO 4: TIPOS DE DADOS - O DNA DAS INFORMAÇÕES")
            print("="*50)
        
        self.print_concept("🧬 Cada informação em Python tem um 'DNA' especial!")
        self.print_colored("Esse DNA define o que podemos fazer com ela.", "cyan")
        
        self.print_section("OS 4 TIPOS FUNDAMENTAIS")
        
        self.print_concept("\n🔢 1. NÚMEROS INTEIROS (int)")
        self.print_colored("   São números SEM vírgula: 1, 100, -5, 0", "yellow")
        self.print_colored("   Usamos para: idades, quantidade, posições...", "green")
        
        self.print_concept("\n🔢 2. NÚMEROS DECIMAIS (float)")  
        self.print_colored("   São números COM vírgula: 3.14, 1.75, -2.5", "yellow")
        self.print_colored("   Usamos para: preços, medidas, percentuais...", "green")
        
        self.print_concept("\n📝 3. TEXTOS (string)")
        self.print_colored("   São palavras entre aspas: 'João', \"Python\"", "yellow")
        self.print_colored("   Usamos para: nomes, mensagens, descrições...", "green")
        
        self.print_concept("\n✅ 4. VERDADEIRO/FALSO (boolean)")
        self.print_colored("   Apenas dois valores: True ou False", "yellow")
        self.print_colored("   Usamos para: decisões, estados, flags...", "green")
        
        self.print_section("\n🎯 Vamos ver cada tipo em ação:")
        
        codigo = '''# Números inteiros (int)
idade = 25
quantidade = 100
temperatura = -10

print("=== INTEIROS ===")
print("Idade:", idade)
print("Quantidade:", quantidade) 
print("Temperatura:", temperatura)

# Números decimais (float)
altura = 1.75
preco = 29.99
pi = 3.14159

print("\\n=== DECIMAIS ===")
print("Altura:", altura)
print("Preço: R$", preco)
print("Pi:", pi)

# Textos (string)
nome = "Ana Silva"
cidade = "São Paulo"
hobby = 'programação'

print("\\n=== TEXTOS ===")
print("Nome:", nome)
print("Cidade:", cidade)
print("Hobby:", hobby)

# Verdadeiro/Falso (boolean)
tem_carteira = True
e_maior_idade = True
gosta_python = True
tem_medo_python = False

print("\\n=== VERDADEIRO/FALSO ===")
print("Tem carteira:", tem_carteira)
print("É maior de idade:", e_maior_idade)
print("Gosta de Python:", gosta_python)
print("Tem medo de Python:", tem_medo_python)'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.print_concept("\n🔍 Como descobrir o tipo de uma variável?")
        self.print_tip("Use a função type()!")
        
        codigo2 = '''# Testando tipos
nome = "João"
idade = 30
altura = 1.80
tem_pets = True

print("Tipo de 'nome':", type(nome))
print("Tipo de 'idade':", type(idade))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'tem_pets':", type(tem_pets))'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("\n🔄 CONVERSÃO ENTRE TIPOS (Type Casting):")
        
        codigo3 = '''# Convertendo entre tipos
numero_texto = "123"
numero_int = int(numero_texto)
numero_float = float(numero_texto)

print("Original (string):", numero_texto, "- Tipo:", type(numero_texto))
print("Como int:", numero_int, "- Tipo:", type(numero_int))
print("Como float:", numero_float, "- Tipo:", type(numero_float))

# Convertendo números para texto
idade = 25
idade_texto = str(idade)
print("\\nIdade como número:", idade, "- Tipo:", type(idade))
print("Idade como texto:", idade_texto, "- Tipo:", type(idade_texto))

# Convertendo para boolean
print("\\n=== CONVERSÕES PARA BOOLEAN ===")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.print_warning("\n⚠️ CUIDADOS com conversões:")
        
        codigo4 = '''# Conversões que podem dar erro
try:
    numero = int("abc")  # Isso vai dar erro!
except ValueError as e:
    print("ERRO:", e)
    print("Não posso converter 'abc' para número!")

try:
    numero = int("3.14")  # Isso também dá erro!
except ValueError as e:
    print("ERRO:", e)
    print("Para converter '3.14', use float() primeiro!")
    
# Jeito correto:
numero_correto = int(float("3.14"))
print("Conversão correta:", numero_correto)'''
        
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        self.print_section("\n🧮 OPERAÇÕES por tipo:")
        
        self.print_concept("\n📊 COM NÚMEROS (int/float):")
        self.print_colored("• Soma: 5 + 3 = 8", "yellow")
        self.print_colored("• Subtração: 10 - 4 = 6", "yellow") 
        self.print_colored("• Multiplicação: 3 * 7 = 21", "yellow")
        self.print_colored("• Divisão: 15 / 3 = 5.0", "yellow")
        self.print_colored("• Potência: 2 ** 3 = 8", "yellow")
        
        codigo5 = '''a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")'''
        
        self.exemplo(codigo5)
        self.executar_codigo(codigo5)
        
        self.print_concept("\n📝 COM TEXTOS (string):")
        self.print_colored("• Concatenação: 'Olá' + ' ' + 'Mundo' = 'Olá Mundo'", "yellow")
        self.print_colored("• Repetição: 'Python! ' * 3 = 'Python! Python! Python! '", "yellow")
        
        codigo6 = '''nome = "Ana"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

grito = "Python! " * 3
print("Grito:", grito)

# Tamanho do texto
print("Tamanho do nome:", len(nome_completo))'''
        
        self.exemplo(codigo6)
        self.executar_codigo(codigo6)
        
        self.print_concept("\n💡 CURIOSIDADES sobre tipos:")
        self.print_colored("• Python descobre o tipo automaticamente!", "cyan")
        self.print_colored("• Uma variável pode mudar de tipo durante o programa", "cyan")
        self.print_colored("• Strings podem usar aspas simples ' ou duplas \"", "cyan")
        self.print_colored("• Números muito grandes são automaticamente int", "cyan")
        self.print_colored("• True e False SEMPRE começam com maiúscula", "cyan")
        
        codigo7 = '''# Variável mudando de tipo
variavel = 42          # int
print("Como int:", variavel, type(variavel))

variavel = 3.14        # float  
print("Como float:", variavel, type(variavel))

variavel = "Python"    # string
print("Como string:", variavel, type(variavel))

variavel = True        # boolean
print("Como boolean:", variavel, type(variavel))'''
        
        self.exemplo(codigo7)
        self.executar_codigo(codigo7)
        
        self.pausar()
        
        self.print_tip("\n🎯 DICAS PROFISSIONAIS:")
        self.print_colored("• Use int para contadores, idades, quantidades", "green")
        self.print_colored("• Use float para medidas, preços, cálculos precisos", "green")
        self.print_colored("• Use string para nomes, mensagens, textos", "green")
        self.print_colored("• Use boolean para flags, estados, condições", "green")
        self.print_colored("• Sempre valide entradas do usuário!", "yellow")
        self.print_colored("• Nomes de variáveis devem indicar o tipo esperado", "yellow")
        
        # Exercícios práticos
        self.exercicio(
            "Qual tipo de dado é o valor 3.14?",
            ["float", "ponto flutuante", "número decimal"],
            "É um número com decimais"
        )
        
        self.exercicio(
            "Como converter o texto '100' para número inteiro?",
            ["int('100')", "int(\"100\")", "int('100')"],
            "Use a função int()"
        )
        
        self.exercicio(
            "True e False são de que tipo?",
            ["boolean", "bool", "verdadeiro/falso"],
            "São valores lógicos"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_calculadora_estatisticas()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_calculadora_estatisticas(self) -> None:
        """Mini Projeto - Módulo 4: Calculadora de Estatísticas Pessoais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CALCULADORA DE ESTATÍSTICAS PESSOAIS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CALCULADORA DE ESTATÍSTICAS PESSOAIS")
            print("="*50)
        
        self.print_success("📊 Vamos criar uma calculadora que processa diferentes tipos de dados!")
        self.print_colored("Sistema similar aos usados em:", "cyan")
        self.print_colored("• Apps de saúde (Apple Health, Google Fit)", "green")
        self.print_colored("• Sistemas bancários (controle financeiro)", "green")
        self.print_colored("• E-commerce (análise de compras)", "green")
        self.print_colored("• Redes sociais (estatísticas de perfil)", "green")
        
        self.print_section("\n💻 Programa completo usando todos os tipos de dados:")
        
        codigo_completo = '''# 📊 CALCULADORA DE ESTATÍSTICAS PESSOAIS
print("🔢" * 20)
print("   ANÁLISE DE DADOS PESSOAIS")
print("🔢" * 20)

# Dados pessoais (diferentes tipos)
nome = "Maria Silva"                    # string
idade = 28                             # int
altura = 1.68                          # float
peso = 65.5                           # float
tem_plano_saude = True                # boolean
pratica_exercicios = True             # boolean
salario = 4500.00                     # float
dependentes = 2                       # int

print(f"\\n👤 DADOS PESSOAIS:")
print(f"Nome: {nome} (tipo: {type(nome).__name__})")
print(f"Idade: {idade} anos (tipo: {type(idade).__name__})")
print(f"Altura: {altura}m (tipo: {type(altura).__name__})")

print(f"\\n💪 SAÚDE:")
print(f"Peso: {peso}kg (tipo: {type(peso).__name__})")
print(f"Plano de Saúde: {tem_plano_saude} (tipo: {type(tem_plano_saude).__name__})")
print(f"Pratica Exercícios: {pratica_exercicios} (tipo: {type(pratica_exercicios).__name__})")

# Cálculos automáticos (conversões e operações)
imc = peso / (altura ** 2)             # float result
idade_meses = idade * 12               # int calculation
salario_anual = salario * 12           # float calculation
renda_per_capita = salario / (dependentes + 1)  # float division

print(f"\\n📈 CÁLCULOS AUTOMÁTICOS:")
print(f"IMC: {imc:.2f} (tipo: {type(imc).__name__})")
print(f"Idade em meses: {idade_meses} (tipo: {type(idade_meses).__name__})")
print(f"Salário anual: R$ {salario_anual:.2f} (tipo: {type(salario_anual).__name__})")
print(f"Renda per capita: R$ {renda_per_capita:.2f} (tipo: {type(renda_per_capita).__name__})")

# Análises com boolean
print(f"\\n🎯 ANÁLISES:")
if imc < 18.5:
    situacao_peso = "Abaixo do peso"
elif imc < 25:
    situacao_peso = "Peso normal"
else:
    situacao_peso = "Acima do peso"
    
perfil_saudavel = tem_plano_saude and pratica_exercicios
print(f"Situação do peso: {situacao_peso}")
print(f"Perfil saudável: {perfil_saudavel} (tipo: {type(perfil_saudavel).__name__})")

print("\\n🔢" * 20)
print("   ANÁLISE CONCLUÍDA!")
print("🔢" * 20)'''
        
        self.exemplo(codigo_completo)
        self.executar_codigo(codigo_completo)
        
        self.print_success("\n🎉 CALCULADORA CRIADA COM SUCESSO!")
        self.print_concept("\n🌍 ONDE ISSO É USADO:")
        self.print_colored("• 🏥 Sistemas hospitalares: Cálculo de IMC e estatísticas", "green")
        self.print_colored("• 💰 Bancos: Análise de renda e perfil financeiro", "green")
        self.print_colored("• 📱 Apps fitness: Monitoramento de saúde", "green")
        self.print_colored("• 🛒 E-commerce: Análise de comportamento de compra", "green")
        self.print_colored("• 📊 Business Intelligence: Relatórios executivos", "green")
        
        self.print_concept("\n💡 TÉCNICAS PROFISSIONAIS USADAS:")
        self.print_colored("• Conversão automática entre tipos", "yellow")
        self.print_colored("• Formatação de números com decimais (.2f)", "yellow")
        self.print_colored("• Operações lógicas com boolean", "yellow")
        self.print_colored("• Cálculos matemáticos com diferentes tipos", "yellow")
        self.print_colored("• Análise de dados em tempo real", "yellow")
        
        self.print_success("\n🏆 CONQUISTA: Analista de Dados!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Calculadora de Estatísticas Pessoais")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo04TiposDados()
    print("Teste do módulo 4 - versão standalone")
    module._tipos_dados()