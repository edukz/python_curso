#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 3: Variáveis e Tipos de Dados
Aprenda sobre variáveis, a memória do seu programa
"""

from ..shared.base_module import BaseModule


class Modulo03Variaveis(BaseModule):
    """Módulo 3: Variáveis - A Memória do Seu Programa"""
    
    def __init__(self):
        super().__init__("modulo_3", "Variáveis e Tipos de Dados")
        self.has_mini_project = True
        self.mini_project_points = 50
    
    def execute(self) -> None:
        """Executa o módulo sobre variáveis"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._variaveis_tipos()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _variaveis_tipos(self) -> None:
        """Conteúdo principal sobre variáveis"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🗃️ MÓDULO 3: VARIÁVEIS - A MEMÓRIA DO SEU PROGRAMA")
        else:
            print("\n" + "="*50)
            print("🗃️ MÓDULO 3: VARIÁVEIS - A MEMÓRIA DO SEU PROGRAMA")
            print("="*50)
        
        print("🗃️ Imagine que variáveis são como CAIXAS ETIQUETADAS")
        print("onde você guarda suas coisas favoritas!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO VARIÁVEIS?")
        print("═══════════════════════════════════════════════")
        
        print("\n🏠 Na vida real:")
        print("📦 CAIXA 'Roupas de Inverno' → Contém casacos e blusas")
        print("📦 CAIXA 'Documentos' → Contém RG, CPF, diplomas")
        print("📦 CAIXA 'Fotos' → Contém suas memórias")
        
        print("\n💻 Em Python:")
        print("📦 VARIÁVEL 'nome' → Contém 'João Silva'")
        print("📦 VARIÁVEL 'idade' → Contém 25")
        print("📦 VARIÁVEL 'salario' → Contém 3500.00")
        
        self.pausar()
        
        print("\n🎯 Vamos criar nossas primeiras variáveis:")
        
        codigo = '''nome = "Python"
idade = 30
print("Linguagem:", nome)
print("Idade:", idade)'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        print("\n🔍 O que aconteceu aqui?")
        print("1. Criamos uma caixa chamada 'nome' e guardamos 'Python'")
        print("2. Criamos uma caixa chamada 'idade' e guardamos 30")
        print("3. Pedimos para mostrar o conteúdo das caixas")
        
        self.pausar()
        
        print("\n⚡ ATRIBUIÇÃO - O sinal '=' é especial!")
        print("• Em matemática: 2 + 2 = 4 (igualdade)")
        print("• Em Python: nome = 'João' (ATRIBUIÇÃO)")
        print("")
        print("🎯 Leia sempre da DIREITA para ESQUERDA:")
        print("   nome = 'João'")
        print("   ↑       ↑")
        print("   |       └─ Valor que vai ser guardado")
        print("   └─ Nome da caixa onde vai ser guardado")
        
        self.pausar()
        
        print("\n📝 Vamos ver mais exemplos práticos:")
        
        # Exemplo mais rico
        codigo2 = '''# Informações de uma pessoa
nome_completo = "Ana Silva Santos"
idade = 28
altura = 1.65
tem_carteira = True

print("=== PERFIL DA PESSOA ===")
print("Nome:", nome_completo)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Tem carteira de motorista:", tem_carteira)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🔄 Variáveis podem MUDAR de valor:")
        
        codigo3 = '''pontos = 0
print("Pontos iniciais:", pontos)

pontos = 10
print("Depois de ganhar:", pontos)

pontos = 25
print("Depois de ganhar mais:", pontos)'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        print("\n💡 Por isso se chama VARIÁVEL - o valor pode VARIAR!")
        
        self.pausar()
        
        print("\n📋 REGRAS IMPORTANTES para nomes de variáveis:")
        print("") 
        print("✅ PODE usar:")
        print("• Letras (a-z, A-Z)")
        print("• Números (0-9) - mas NÃO no início")
        print("• Underscore (_)")
        print("")
        print("❌ NÃO PODE usar:")
        print("• Espaços em branco")
        print("• Caracteres especiais (@, #, !, etc)")
        print("• Palavras reservadas do Python")
        print("• Começar com números")
        
        self.pausar()
        
        print("\n💯 EXEMPLOS de nomes VÁLIDOS:")
        print("✅ nome")
        print("✅ idade")
        print("✅ nome_completo")
        print("✅ salario2023")
        print("✅ _temperatura")
        print("✅ PI")
        print("")
        print("💥 EXEMPLOS de nomes INVÁLIDOS:")
        print("❌ 2nome (começa com número)")
        print("❌ nome completo (tem espaço)")
        print("❌ salário (tem acento)")
        print("❌ for (palavra reservada)")
        print("❌ nome@ (caractere especial)")
        
        self.pausar()
        
        print("\n🎨 CONVENÇÕES de nomenclatura:")
        print("• snake_case: nome_da_variavel (recomendado em Python)")
        print("• camelCase: nomeDaVariavel (mais usado em outras linguagens)")
        print("• PascalCase: NomeDaVariavel (para classes)")
        print("• CONSTANTES: VALOR_FIXO (para valores que não mudam)")
        
        self.pausar()
        
        print("\n⚠️ PYTHON É CASE-SENSITIVE (diferencia maiúsculas/minúsculas):")
        
        codigo4 = '''nome = "João"
Nome = "Maria"
NOME = "Pedro"

print("nome:", nome)
print("Nome:", Nome)
print("NOME:", NOME)'''
        
        print("São 3 variáveis DIFERENTES!")
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        self.pausar()
        
        print("\n🧮 Operações com variáveis:")
        
        codigo5 = '''a = 10
b = 5
soma = a + b
produto = a * b

print("a =", a)
print("b =", b)
print("a + b =", soma)
print("a * b =", produto)

# Podemos usar uma variável para criar outra!
dobro_de_a = a * 2
print("Dobro de a:", dobro_de_a)'''
        
        self.exemplo(codigo5)
        self.executar_codigo(codigo5)
        
        self.pausar()
        
        print("\n🎯 DICA PROFISSIONAL - Nomes descritivos:")
        print("")
        print("😰 RUIM:")
        print("   x = 1000")
        print("   y = 0.08")
        print("   z = x * y")
        print("")
        print("😍 BOM:")
        print("   preco_produto = 1000")
        print("   taxa_desconto = 0.08")
        print("   desconto = preco_produto * taxa_desconto")
        print("")
        print("🔍 Qual código é mais fácil de entender?")
        
        # Exercícios práticos
        self.exercicio(
            "Se eu escrever: x = 10, o que é 'x'?",
            ["variável", "variavel", "uma variável", "uma variavel"],
            "É onde guardamos o valor 10"
        )
        
        self.exercicio(
            "Qual nome de variável está CORRETO?",
            ["nome_usuario", "nome usuario", "2nome", "nome@"],
            "Não pode ter espaços nem caracteres especiais"
        )
        
        self.exercicio(
            "Em Python, 'nome' e 'Nome' são a mesma variável?",
            ["não", "nao", "false", "diferentes"],
            "Python diferencia maiúsculas de minúsculas"
        )
        
        # Mini Projeto Prático
        self._mini_projeto_perfil_jogador()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_perfil_jogador(self) -> None:
        """Mini Projeto - Módulo 3: Sistema de Perfil de Jogador"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE PERFIL DE JOGADOR")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE PERFIL DE JOGADOR")
            print("="*50)
        
        print("🎮 Vamos criar um sistema de perfil para um jogo RPG!")
        print("Tipo de sistema usado em:")
        print("• Jogos online (World of Warcraft, League of Legends)")
        print("• Apps de fitness (Nike Training, Strava)")
        print("• Redes sociais (Instagram, LinkedIn)")
        print("• Sistemas de e-learning")
        
        self.pausar()
        
        print("\n📝 Vamos criar variáveis para armazenar dados do jogador:")
        
        # Demonstração passo a passo
        codigo1 = '''# 🎮 SISTEMA DE PERFIL DE JOGADOR
# Criando variáveis para dados do perfil

# Informações básicas
nome_jogador = "DragonSlayer2024"
nivel = 15
experiencia = 2350
vida_maxima = 100
vida_atual = 85

# Status de habilidades
forca = 18
agilidade = 12
inteligencia = 20
sorte = 8

# Informações de progresso
missoes_completas = 7
inimigos_derrotados = 143
moedas = 1250
item_favorito = "Espada Flamejante"

print("=" * 50)
print("     🎮 PERFIL DO JOGADOR")
print("=" * 50)
print()
print(f"👤 Jogador: {nome_jogador}")
print(f"⭐ Nível: {nivel}")
print(f"💫 XP: {experiencia}")
print(f"❤️  Vida: {vida_atual}/{vida_maxima}")
print()
print("🎯 ATRIBUTOS:")
print(f"💪 Força: {forca}")
print(f"🏃 Agilidade: {agilidade}")
print(f"🧠 Inteligência: {inteligencia}")
print(f"🍀 Sorte: {sorte}")
print()
print("📊 ESTATÍSTICAS:")
print(f"✅ Missões: {missoes_completas}")
print(f"⚔️  Vitórias: {inimigos_derrotados}")
print(f"💰 Moedas: {moedas}")
print(f"🗡️  Item Favorito: {item_favorito}")
print("=" * 50)'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        print("\n🎉 PROJETO CONCLUÍDO!")
        print("\n🌍 APLICAÇÕES NO MUNDO REAL:")
        print("• 🎮 Steam: Perfis de jogadores")
        print("• 💼 LinkedIn: Perfis profissionais")
        print("• 🏥 Hospitais: Fichas de pacientes")
        print("• 🏪 E-commerce: Dados de clientes")
        print("• 🎓 Escolas: Sistemas acadêmicos")
        
        print("\n💡 CONCEITOS APRENDIDOS:")
        print("• Organização de dados com variáveis")
        print("• Diferentes tipos de informação")
        print("• Nomenclatura descritiva de variáveis")
        print("• Formatação profissional de saídas")
        
        print("\n🏆 CONQUISTA: Organizador de Dados!")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Perfil de Jogador")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo03Variaveis()
    print("Teste do módulo 3 - versão standalone")
    module._variaveis_tipos()