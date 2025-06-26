#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 8: Loops (Repetições)
Aprenda sobre estruturas de repetição (for e while)
"""

from ..shared.base_module import BaseModule


class Modulo08Loops(BaseModule):
    """Módulo 8: Repetições (Loops)"""
    
    def __init__(self):
        super().__init__("modulo_8", "Loops e Repetições")
        self.has_mini_project = True
        self.mini_project_points = 60
    
    def execute(self) -> None:
        """Executa o módulo sobre loops"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._loops()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _loops(self) -> None:
        """Conteúdo principal sobre loops"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔄 MÓDULO 8: REPETIÇÕES (LOOPS)")
        else:
            print("\n" + "="*50)
            print("🔄 MÓDULO 8: REPETIÇÕES (LOOPS)")
            print("="*50)
        
        print("Quando precisamos repetir tarefas, usamos loops!")
        
        print("\n🔄 LOOP FOR - Para repetições com número definido:")
        codigo_for = '''# Contando de 1 a 5
for i in range(1, 6):
    print(f"Contagem: {i}")

print("\\nListando frutas:")
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"🍎 {fruta}")'''
        
        self.exemplo(codigo_for)
        self.executar_codigo(codigo_for)
        
        self.pausar()
        
        print("\n⏰ LOOP WHILE - Para repetições com condição:")
        codigo_while = '''# Contagem regressiva
contador = 5
while contador > 0:
    print(f"⏰ {contador}")
    contador -= 1
print("🚀 DECOLAGEM!")'''
        
        self.exemplo(codigo_while)
        self.executar_codigo(codigo_while)
        
        # Mini Projeto
        self._mini_projeto_gerador_padroes()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_gerador_padroes(self) -> None:
        """Mini Projeto - Gerador de Padrões e Sequências"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: GERADOR DE PADRÕES")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: GERADOR DE PADRÕES")
            print("="*50)
        
        print("🎨 Vamos criar um gerador de padrões visuais!")
        print("Usado em: arte digital, designs, jogos, visualizações")
        
        self.pausar()
        
        codigo_projeto = '''# 🎨 GERADOR DE PADRÕES E SEQUÊNCIAS
print("🎨 GERADOR DE PADRÕES VISUAIS")
print("=" * 40)

# Padrão 1: Pirâmide de estrelas
print("\\n⭐ PIRÂMIDE DE ESTRELAS:")
for i in range(1, 6):
    espacos = " " * (5 - i)
    estrelas = "⭐" * i
    print(f"{espacos}{estrelas}")

# Padrão 2: Tabela de multiplicação
print("\\n🔢 TABELA DE MULTIPLICAÇÃO (5):")
for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i:2d} = {resultado:2d}")

# Padrão 3: Sequência Fibonacci
print("\\n🌀 SEQUÊNCIA FIBONACCI:")
a, b = 0, 1
fibonacci = [a, b]
for i in range(8):
    proximo = a + b
    fibonacci.append(proximo)
    a, b = b, proximo

print("Fibonacci:", fibonacci)

# Padrão 4: Arte ASCII
print("\\n🎭 ARTE ASCII:")
for linha in range(5):
    if linha == 0 or linha == 4:
        print("🟦" * 10)
    else:
        print("🟦" + "⬜" * 8 + "🟦")

print("\\n✨ PADRÕES GERADOS COM SUCESSO!")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 CONQUISTA: Artista Digital!")
        self.complete_mini_project("Gerador de Padrões e Sequências")
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo08Loops()
    print("Teste do módulo 8 - versão standalone")
    module._loops()