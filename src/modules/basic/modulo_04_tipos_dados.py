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
        
        print("🧬 Cada informação em Python tem um 'DNA' especial!")
        print("Esse DNA define o que podemos fazer com ela.")
        
        print("\n═══════════════════════════════════════════════")
        print("        OS 4 TIPOS FUNDAMENTAIS")
        print("═══════════════════════════════════════════════")
        
        print("\n🔢 1. NÚMEROS INTEIROS (int)")
        print("   São números SEM vírgula: 1, 100, -5, 0")
        print("   Usamos para: idades, quantidade, posições...")
        
        print("\n🔢 2. NÚMEROS DECIMAIS (float)")  
        print("   São números COM vírgula: 3.14, 1.75, -2.5")
        print("   Usamos para: preços, medidas, percentuais...")
        
        print("\n📝 3. TEXTOS (string)")
        print("   São palavras entre aspas: 'João', \"Python\"")
        print("   Usamos para: nomes, mensagens, descrições...")
        
        print("\n✅ 4. VERDADEIRO/FALSO (boolean)")
        print("   Apenas dois valores: True ou False")
        print("   Usamos para: decisões, estados, flags...")
        
        self.pausar()
        
        print("\n🎯 Vamos ver cada tipo em ação:")
        
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
        
        self.pausar()
        
        print("\n🔍 Como descobrir o tipo de uma variável?")
        print("Use a função type()!")
        
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
        
        self.pausar()
        
        print("\n🔄 CONVERSÃO ENTRE TIPOS (Type Casting):")
        
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
        
        self.pausar()
        
        print("\n⚠️ CUIDADOS com conversões:")
        
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
        
        self.pausar()
        
        print("\n🧮 OPERAÇÕES por tipo:")
        
        print("\n📊 COM NÚMEROS (int/float):")
        print("• Soma: 5 + 3 = 8")
        print("• Subtração: 10 - 4 = 6") 
        print("• Multiplicação: 3 * 7 = 21")
        print("• Divisão: 15 / 3 = 5.0")
        print("• Potência: 2 ** 3 = 8")
        
        codigo5 = '''a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")'''
        
        self.exemplo(codigo5)
        self.executar_codigo(codigo5)
        
        print("\n📝 COM TEXTOS (string):")
        print("• Concatenação: 'Olá' + ' ' + 'Mundo' = 'Olá Mundo'")
        print("• Repetição: 'Python! ' * 3 = 'Python! Python! Python! '")
        
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
        
        self.pausar()
        
        print("\n💡 CURIOSIDADES sobre tipos:")
        print("• Python descobre o tipo automaticamente!")
        print("• Uma variável pode mudar de tipo durante o programa")
        print("• Strings podem usar aspas simples ' ou duplas \"")
        print("• Números muito grandes são automaticamente int")
        print("• True e False SEMPRE começam com maiúscula")
        
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
        
        print("\n🎯 DICAS PROFISSIONAIS:")
        print("• Use int para contadores, idades, quantidades")
        print("• Use float para medidas, preços, cálculos precisos")
        print("• Use string para nomes, mensagens, textos")
        print("• Use boolean para flags, estados, condições")
        print("• Sempre valide entradas do usuário!")
        print("• Nomes de variáveis devem indicar o tipo esperado")
        
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
        
        print("📊 Vamos criar uma calculadora que processa diferentes tipos de dados!")
        print("Sistema similar aos usados em:")
        print("• Apps de saúde (Apple Health, Google Fit)")
        print("• Sistemas bancários (controle financeiro)")
        print("• E-commerce (análise de compras)")
        print("• Redes sociais (estatísticas de perfil)")
        
        self.pausar()
        
        print("\n💻 Programa completo usando todos os tipos de dados:")
        
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
        
        print("\n🎉 CALCULADORA CRIADA COM SUCESSO!")
        print("\n🌍 ONDE ISSO É USADO:")
        print("• 🏥 Sistemas hospitalares: Cálculo de IMC e estatísticas")
        print("• 💰 Bancos: Análise de renda e perfil financeiro")
        print("• 📱 Apps fitness: Monitoramento de saúde")
        print("• 🛒 E-commerce: Análise de comportamento de compra")
        print("• 📊 Business Intelligence: Relatórios executivos")
        
        print("\n💡 TÉCNICAS PROFISSIONAIS USADAS:")
        print("• Conversão automática entre tipos")
        print("• Formatação de números com decimais (.2f)")
        print("• Operações lógicas com boolean")
        print("• Cálculos matemáticos com diferentes tipos")
        print("• Análise de dados em tempo real")
        
        print("\n🏆 CONQUISTA: Analista de Dados!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Calculadora de Estatísticas Pessoais")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo04TiposDados()
    print("Teste do módulo 4 - versão standalone")
    module._tipos_dados()