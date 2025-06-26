#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 9: Listas
Aprenda sobre listas, coleções de dados organizadas
"""

from ..shared.base_module import BaseModule


class Modulo09Listas(BaseModule):
    """Módulo 9: Listas"""
    
    def __init__(self):
        super().__init__("modulo_9", "Listas e Coleções")
        self.has_mini_project = True
        self.mini_project_points = 65
    
    def execute(self) -> None:
        """Executa o módulo sobre listas"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._listas()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _listas(self) -> None:
        """Conteúdo principal sobre listas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📋 MÓDULO 9: LISTAS E COLEÇÕES")
        else:
            print("\n" + "="*50)
            print("📋 MÓDULO 9: LISTAS E COLEÇÕES")
            print("="*50)
        
        print("Listas armazenam múltiplos valores organizados!")
        
        codigo = '''# Criando e usando listas
frutas = ["maçã", "banana", "laranja", "uva"]
numeros = [1, 2, 3, 4, 5]
mista = ["Python", 2024, True, 3.14]

print("Frutas:", frutas)
print("Primeiro item:", frutas[0])
print("Último item:", frutas[-1])

# Adicionando itens
frutas.append("manga")
print("Após adicionar:", frutas)

# Removendo itens
frutas.remove("banana")
print("Após remover:", frutas)

# Percorrendo a lista
print("\\nTodas as frutas:")
for fruta in frutas:
    print(f"🍎 {fruta}")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        self.pausar()
        
        # Mini Projeto
        self._mini_projeto_inventario()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_inventario(self) -> None:
        """Mini Projeto - Sistema de Inventário Inteligente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE INVENTÁRIO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE INVENTÁRIO")
            print("="*50)
        
        print("📦 Vamos criar um sistema de inventário!")
        print("Usado em: e-commerce, lojas, almoxarifados, empresas")
        
        self.pausar()
        
        codigo_projeto = '''# 📦 SISTEMA DE INVENTÁRIO INTELIGENTE
print("📦 SISTEMA DE INVENTÁRIO V1.0")
print("=" * 40)

# Inventário inicial
inventario = [
    {"nome": "Notebook", "quantidade": 5, "preco": 2500.00},
    {"nome": "Mouse", "quantidade": 20, "preco": 50.00},
    {"nome": "Teclado", "quantidade": 15, "preco": 120.00},
    {"nome": "Monitor", "quantidade": 8, "preco": 800.00}
]

def exibir_inventario(inventario):
    """Exibe o inventário atual"""
    print("\\n📊 INVENTÁRIO ATUAL:")
    print("-" * 60)
    print(f"{'PRODUTO':<15} {'QTD':<5} {'PREÇO':<10} {'TOTAL':<15}")
    print("-" * 60)
    
    valor_total = 0
    for item in inventario:
        total_item = item['quantidade'] * item['preco']
        valor_total += total_item
        print(f"{item['nome']:<15} {item['quantidade']:<5} R${item['preco']:<9.2f} R${total_item:<14.2f}")
    
    print("-" * 60)
    print(f"{'VALOR TOTAL DO ESTOQUE:':<35} R${valor_total:.2f}")
    return valor_total

def buscar_produto(inventario, nome_produto):
    """Busca um produto no inventário"""
    for item in inventario:
        if item['nome'].lower() == nome_produto.lower():
            return item
    return None

def adicionar_estoque(inventario, nome_produto, quantidade):
    """Adiciona quantidade ao estoque"""
    produto = buscar_produto(inventario, nome_produto)
    if produto:
        produto['quantidade'] += quantidade
        print(f"✅ Adicionado {quantidade} unidades de {nome_produto}")
    else:
        print(f"❌ Produto {nome_produto} não encontrado")

# Demonstração do sistema
valor_inicial = exibir_inventario(inventario)

print("\\n🔄 MOVIMENTAÇÕES DE ESTOQUE:")
print("1. Entrada: +10 Notebooks")
adicionar_estoque(inventario, "Notebook", 10)

print("2. Saída: -5 Mouses")
adicionar_estoque(inventario, "Mouse", -5)

print("\\n📊 INVENTÁRIO ATUALIZADO:")
valor_final = exibir_inventario(inventario)

# Análise
diferenca = valor_final - valor_inicial
print(f"\\n📈 ANÁLISE:")
print(f"Valor inicial: R$ {valor_inicial:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print(f"Diferença: R$ {diferenca:.2f}")

# Produtos em baixo estoque
print("\\n⚠️ ALERTA - BAIXO ESTOQUE:")
for item in inventario:
    if item['quantidade'] < 10:
        print(f"🔴 {item['nome']}: apenas {item['quantidade']} unidades")

print("\\n✅ SISTEMA FUNCIONANDO PERFEITAMENTE!")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 CONQUISTA: Gerente de Inventário!")
        self.complete_mini_project("Sistema de Inventário Inteligente")
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo09Listas()
    print("Teste do módulo 9 - versão standalone")
    module._listas()