#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Demos Interativas
Animações ASCII no terminal para demonstrar conceitos Python de forma visual
"""

import time
import os
import random
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime


class ASCIIAnimator:
    """Classe para criar animações ASCII no terminal"""
    
    def __init__(self):
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m',
            'bold': '\033[1m',
            'underline': '\033[4m'
        }
        self.animation_speed = 1.0
    
    def clear_screen(self) -> None:
        """Limpa a tela"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_colored(self, text: str, color: str = 'white') -> None:
        """Imprime texto colorido"""
        print(f"{self.colors.get(color, '')}{text}{self.colors['reset']}")
    
    def animate_text(self, text: str, delay: float = 0.05) -> None:
        """Anima texto caractere por caractere"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay * self.animation_speed)
        print()
    
    def draw_box(self, content: List[str], title: str = "", color: str = 'white') -> None:
        """Desenha uma caixa com conteúdo"""
        if not content:
            return
        
        max_width = max(len(line) for line in content)
        if title:
            max_width = max(max_width, len(title) + 4)
        
        # Cabeçalho
        if title:
            print(f"{self.colors[color]}╔{'═' * (max_width + 2)}╗{self.colors['reset']}")
            title_padding = (max_width - len(title)) // 2
            print(f"{self.colors[color]}║{' ' * title_padding}{title}{' ' * (max_width - len(title) - title_padding + 2)}║{self.colors['reset']}")
            print(f"{self.colors[color]}╠{'═' * (max_width + 2)}╣{self.colors['reset']}")
        else:
            print(f"{self.colors[color]}╔{'═' * (max_width + 2)}╗{self.colors['reset']}")
        
        # Conteúdo
        for line in content:
            padding = max_width - len(line)
            print(f"{self.colors[color]}║ {line}{' ' * padding} ║{self.colors['reset']}")
        
        # Rodapé
        print(f"{self.colors[color]}╚{'═' * (max_width + 2)}╝{self.colors['reset']}")
    
    def draw_memory_block(self, var_name: str, value: Any, address: str = None) -> List[str]:
        """Desenha um bloco de memória para uma variável"""
        if address is None:
            address = f"0x{random.randint(1000, 9999):04x}"
        
        value_str = str(value)
        if isinstance(value, str):
            value_str = f"'{value}'"
        
        return [
            f"┌─────────────────┐",
            f"│ {var_name:<15} │",
            f"├─────────────────┤",
            f"│ {value_str:<15} │",
            f"├─────────────────┤",
            f"│ {address:<15} │",
            f"└─────────────────┘"
        ]
    
    def animate_assignment(self, var_name: str, old_value: Any, new_value: Any) -> None:
        """Anima atribuição de variável"""
        self.clear_screen()
        self.print_colored(f"📝 DEMONSTRAÇÃO: {var_name} = {new_value}", 'yellow')
        print()
        
        # Estado inicial
        if old_value is not None:
            print("Estado Anterior:")
            lines = self.draw_memory_block(var_name, old_value)
            for line in lines:
                print(f"  {line}")
            time.sleep(1.5 * self.animation_speed)
        
        print("\n" + "="*50)
        self.animate_text("🔄 Executando atribuição...", 0.03)
        time.sleep(1 * self.animation_speed)
        
        # Estado final
        print("\nNovo Estado:")
        lines = self.draw_memory_block(var_name, new_value)
        for line in lines:
            print(f"  {line}")
        
        time.sleep(2 * self.animation_speed)


class VariableDemo:
    """Demonstrações sobre variáveis e memória"""
    
    def __init__(self, animator: ASCIIAnimator):
        self.animator = animator
    
    def basic_assignment_demo(self) -> None:
        """Demo básica de atribuição"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: ATRIBUIÇÃO DE VARIÁVEIS", 'cyan')
        print()
        
        demos = [
            ("nome", None, "Python"),
            ("idade", None, 30),
            ("ativo", None, True),
            ("idade", 30, 31),
            ("nome", "Python", "Java")
        ]
        
        for var, old, new in demos:
            self.animator.animate_assignment(var, old, new)
            input("\n⏯️ Pressione ENTER para continuar...")
    
    def string_memory_demo(self) -> None:
        """Demonstra como strings são armazenadas"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: STRINGS NA MEMÓRIA", 'cyan')
        print()
        
        text = "Python"
        self.animator.print_colored("Código: texto = 'Python'", 'yellow')
        print()
        
        # Mostra cada caractere
        print("String 'Python' na memória:")
        print()
        
        for i, char in enumerate(text):
            address = f"0x100{i}"
            print(f"Índice {i}: '{char}' → {address}")
            time.sleep(0.5 * self.animator.animation_speed)
        
        print("\n" + "="*40)
        print("📊 Acesso por índice:")
        
        examples = [(0, 'P'), (2, 't'), (-1, 'n')]
        for idx, char in examples:
            self.animator.animate_text(f"texto[{idx}] = '{char}'", 0.03)
            time.sleep(1 * self.animator.animation_speed)
        
        input("\n⏯️ Pressione ENTER para continuar...")
    
    def list_memory_demo(self) -> None:
        """Demonstra como listas são armazenadas"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: LISTAS NA MEMÓRIA", 'cyan')
        print()
        
        lista = [10, 20, 30]
        self.animator.print_colored("Código: numeros = [10, 20, 30]", 'yellow')
        print()
        
        # Desenha a lista
        print("Lista na memória:")
        print()
        print("numeros →  ┌────┬────┬────┐")
        print("           │ 10 │ 20 │ 30 │")
        print("           └────┴────┴────┘")
        print("Índices:     0    1    2")
        
        time.sleep(2 * self.animator.animation_speed)
        
        # Demonstra operações
        print("\n" + "="*40)
        print("📝 Operações:")
        
        operations = [
            ("numeros.append(40)", [10, 20, 30, 40]),
            ("numeros[1] = 25", [10, 25, 30, 40]),
            ("numeros.pop()", [10, 25, 30])
        ]
        
        for op, result in operations:
            print(f"\n🔄 {op}")
            time.sleep(1 * self.animator.animation_speed)
            
            print("Nova lista:")
            items_str = " │ ".join(f"{x:2d}" for x in result)
            sep_str = "─" * (len(items_str) + 2)
            print(f"           ┌{sep_str}┐")
            print(f"           │ {items_str} │")
            print(f"           └{sep_str}┘")
            
            time.sleep(1.5 * self.animator.animation_speed)
        
        input("\n⏯️ Pressione ENTER para continuar...")


class LoopDemo:
    """Demonstrações de loops"""
    
    def __init__(self, animator: ASCIIAnimator):
        self.animator = animator
    
    def for_loop_demo(self) -> None:
        """Demonstra loop for visualmente"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: LOOP FOR", 'cyan')
        print()
        
        code = "for i in range(5):\n    print(f'i = {i}')"
        self.animator.print_colored(f"Código:\n{code}", 'yellow')
        print()
        
        # Animação do loop
        for i in range(5):
            self.animator.clear_screen()
            self.animator.print_colored("🔄 EXECUTANDO LOOP FOR", 'cyan')
            print()
            
            # Mostra estado da variável
            self.animator.draw_box([
                f"Iteração: {i + 1}/5",
                f"Variável i = {i}",
                f"range(5) = [0, 1, 2, 3, 4]"
            ], "Estado Atual", 'green')
            
            # Visualiza range
            print("\nVisualizando range(5):")
            range_visual = ""
            for j in range(5):
                if j == i:
                    range_visual += f"[{self.animator.colors['red']}{j}{self.animator.colors['reset']}] "
                else:
                    range_visual += f" {j}  "
            print(f"  {range_visual}")
            print("   ↑" + " " * (i * 4) + "  (i atual)")
            
            print(f"\n📤 Saída: i = {i}")
            
            time.sleep(2 * self.animator.animation_speed)
        
        print("\n✅ Loop concluído!")
        input("\n⏯️ Pressione ENTER para continuar...")
    
    def while_loop_demo(self) -> None:
        """Demonstra loop while"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: LOOP WHILE", 'cyan')
        print()
        
        code = "contador = 0\nwhile contador < 4:\n    print(contador)\n    contador += 1"
        self.animator.print_colored(f"Código:\n{code}", 'yellow')
        print()
        
        contador = 0
        iteration = 1
        
        while contador < 4:
            self.animator.clear_screen()
            self.animator.print_colored("🔄 EXECUTANDO LOOP WHILE", 'cyan')
            print()
            
            # Estado atual
            self.animator.draw_box([
                f"Iteração: {iteration}",
                f"contador = {contador}",
                f"Condição: {contador} < 4 → {contador < 4}"
            ], "Estado Atual", 'green')
            
            # Visualiza condição
            print("\nVerificando condição:")
            condition_color = 'green' if contador < 4 else 'red'
            self.animator.print_colored(f"  {contador} < 4 = {contador < 4}", condition_color)
            
            if contador < 4:
                print(f"\n📤 Saída: {contador}")
                print("🔄 Executando: contador += 1")
                time.sleep(1.5 * self.animator.animation_speed)
                
                contador += 1
                print(f"📝 Novo valor: contador = {contador}")
            
            iteration += 1
            time.sleep(2 * self.animator.animation_speed)
        
        print("\n❌ Condição falsa - loop termina!")
        input("\n⏯️ Pressione ENTER para continuar...")
    
    def nested_loop_demo(self) -> None:
        """Demonstra loops aninhados"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: LOOPS ANINHADOS", 'cyan')
        print()
        
        code = "for i in range(3):\n    for j in range(2):\n        print(f'({i},{j})')"
        self.animator.print_colored(f"Código:\n{code}", 'yellow')
        print()
        
        # Grid para visualizar
        for i in range(3):
            for j in range(2):
                self.animator.clear_screen()
                self.animator.print_colored("🔄 LOOPS ANINHADOS", 'cyan')
                print()
                
                # Estado das variáveis
                self.animator.draw_box([
                    f"Loop externo: i = {i}",
                    f"Loop interno: j = {j}",
                    f"Combinação: ({i},{j})"
                ], "Estado Atual", 'green')
                
                # Grid visual
                print("\nGrid de iterações:")
                print("    j=0  j=1")
                for row in range(3):
                    line = f"i={row} "
                    for col in range(2):
                        if row == i and col == j:
                            line += f"[{self.animator.colors['red']}●{self.animator.colors['reset']}]  "
                        elif row < i or (row == i and col < j):
                            line += f"[{self.animator.colors['green']}✓{self.animator.colors['reset']}]  "
                        else:
                            line += "[ ]  "
                    print(f"  {line}")
                
                print(f"\n📤 Saída: ({i},{j})")
                time.sleep(1.5 * self.animator.animation_speed)
        
        print("\n✅ Todos os loops concluídos!")
        input("\n⏯️ Pressione ENTER para continuar...")


class ConditionalDemo:
    """Demonstrações de condicionais"""
    
    def __init__(self, animator: ASCIIAnimator):
        self.animator = animator
    
    def if_else_demo(self) -> None:
        """Demonstra if/else com fluxo visual"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: IF/ELSE", 'cyan')
        print()
        
        examples = [
            (18, "idade >= 18"),
            (15, "idade >= 18"),
            (21, "idade >= 18")
        ]
        
        for idade, condition in examples:
            self.animator.clear_screen()
            self.animator.print_colored("🔀 DEMONSTRAÇÃO IF/ELSE", 'cyan')
            print()
            
            code = f"idade = {idade}\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')"
            self.animator.print_colored(f"Código:\n{code}", 'yellow')
            print()
            
            # Fluxo visual
            print("Fluxo de Decisão:")
            print()
            print("    ┌─────────────┐")
            print("    │   INÍCIO    │")
            print("    └──────┬──────┘")
            print("           │")
            print(f"    ┌──────▼──────┐")
            print(f"    │ idade = {idade:2d}  │")
            print("    └──────┬──────┘")
            print("           │")
            
            # Condição
            condition_result = idade >= 18
            condition_color = 'green' if condition_result else 'red'
            
            print("    ┌──────▼──────┐")
            print(f"    │ idade >= 18?│")
            print("    └──────┬──────┘")
            print("           │")
            
            # Resultado
            if condition_result:
                print("    ┌──────▼──────┐")
                print(f"    │{self.animator.colors['green']}   SIM (True) {self.animator.colors['reset']}│")
                print("    └──────┬──────┘")
                print("           │")
                print("    ┌──────▼──────┐")
                print("    │'Maior de    │")
                print("    │ idade'      │")
                print("    └─────────────┘")
                resultado = "Maior de idade"
            else:
                print("    ┌──────▼──────┐")
                print(f"    │{self.animator.colors['red']}  NÃO (False) {self.animator.colors['reset']}│")
                print("    └──────┬──────┘")
                print("           │")
                print("    ┌──────▼──────┐")
                print("    │'Menor de    │")
                print("    │ idade'      │")
                print("    └─────────────┘")
                resultado = "Menor de idade"
            
            time.sleep(2 * self.animator.animation_speed)
            print(f"\n📤 Resultado: {resultado}")
            
            input("\n⏯️ Pressione ENTER para próximo exemplo...")
    
    def elif_demo(self) -> None:
        """Demonstra elif com múltiplas condições"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: IF/ELIF/ELSE", 'cyan')
        print()
        
        examples = [85, 75, 65, 45]
        
        for nota in examples:
            self.animator.clear_screen()
            self.animator.print_colored("🔀 DEMONSTRAÇÃO ELIF", 'cyan')
            print()
            
            code = f"nota = {nota}\nif nota >= 90:\n    conceito = 'A'\nelif nota >= 80:\n    conceito = 'B'\nelif nota >= 70:\n    conceito = 'C'\nelif nota >= 60:\n    conceito = 'D'\nelse:\n    conceito = 'F'"
            self.animator.print_colored(f"Código:\n{code}", 'yellow')
            print()
            
            # Teste cada condição
            print("Testando condições em sequência:")
            print()
            
            conditions = [
                (f"nota >= 90", nota >= 90, "A"),
                (f"nota >= 80", nota >= 80, "B"),
                (f"nota >= 70", nota >= 70, "C"),
                (f"nota >= 60", nota >= 60, "D"),
                ("else", True, "F")
            ]
            
            for i, (cond_text, result, conceito) in enumerate(conditions):
                if i == 0:
                    prefix = "if"
                elif i < len(conditions) - 1:
                    prefix = "elif"
                else:
                    prefix = "else"
                
                if i < len(conditions) - 1:
                    test_result = f"{nota} >= {90 - i*10}"
                    color = 'green' if result else 'red'
                    status = "✓ VERDADEIRO" if result else "✗ FALSO"
                    print(f"  {prefix} {test_result}: {self.animator.colors[color]}{status}{self.animator.colors['reset']}")
                else:
                    if not any(nota >= (90 - j*10) for j in range(4)):
                        print(f"  {prefix}: {self.animator.colors['green']}✓ EXECUTADO{self.animator.colors['reset']}")
                        final_conceito = conceito
                        break
                
                if result:
                    print(f"      → conceito = '{conceito}'")
                    final_conceito = conceito
                    break
                
                time.sleep(1 * self.animator.animation_speed)
            
            print(f"\n📤 Resultado final: conceito = '{final_conceito}'")
            input("\n⏯️ Pressione ENTER para próximo exemplo...")


class DataStructureDemo:
    """Demonstrações de estruturas de dados"""
    
    def __init__(self, animator: ASCIIAnimator):
        self.animator = animator
    
    def list_operations_demo(self) -> None:
        """Demonstra operações em listas"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: OPERAÇÕES EM LISTAS", 'cyan')
        print()
        
        lista = []
        
        operations = [
            ("lista = []", lambda: []),
            ("lista.append(10)", lambda: lista + [10]),
            ("lista.append(20)", lambda: [10, 20]),
            ("lista.append(30)", lambda: [10, 20, 30]),
            ("lista.insert(1, 15)", lambda: [10, 15, 20, 30]),
            ("lista.remove(20)", lambda: [10, 15, 30]),
            ("lista.pop()", lambda: [10, 15])
        ]
        
        for operation, result_func in operations:
            self.animator.clear_screen()
            self.animator.print_colored("📝 OPERAÇÕES EM LISTAS", 'cyan')
            print()
            
            self.animator.print_colored(f"Operação: {operation}", 'yellow')
            print()
            
            # Estado anterior
            if lista:
                print("Estado anterior:")
                self._draw_list(lista)
                print()
            
            # Executa operação
            lista = result_func()
            
            print("🔄 Executando operação...")
            time.sleep(1 * self.animator.animation_speed)
            
            # Novo estado
            print("\nNovo estado:")
            self._draw_list(lista)
            
            print(f"\nTamanho da lista: {len(lista)}")
            
            time.sleep(2 * self.animator.animation_speed)
            input("\n⏯️ Pressione ENTER para continuar...")
    
    def _draw_list(self, lista: List[Any]) -> None:
        """Desenha representação visual de uma lista"""
        if not lista:
            print("  lista = [] (vazia)")
            return
        
        # Cabeçalho
        print("  lista = [", end="")
        
        # Elementos
        for i, item in enumerate(lista):
            color = 'green' if i == len(lista) - 1 else 'white'
            if i > 0:
                print(", ", end="")
            print(f"{self.animator.colors[color]}{item}{self.animator.colors['reset']}", end="")
        print("]")
        
        # Índices
        print("          ", end="")
        for i in range(len(lista)):
            if i > 0:
                print("   ", end="")
            print(f"↑", end="")
        print()
        
        print("          ", end="")
        for i in range(len(lista)):
            if i > 0:
                print("   ", end="")
            print(f"{i}", end="")
        print()
    
    def dictionary_demo(self) -> None:
        """Demonstra operações em dicionários"""
        self.animator.clear_screen()
        self.animator.print_colored("🎯 DEMO: DICIONÁRIOS", 'cyan')
        print()
        
        dic = {}
        
        operations = [
            ("pessoa = {}", {}),
            ("pessoa['nome'] = 'Ana'", {"nome": "Ana"}),
            ("pessoa['idade'] = 25", {"nome": "Ana", "idade": 25}),
            ("pessoa['cidade'] = 'SP'", {"nome": "Ana", "idade": 25, "cidade": "SP"}),
            ("del pessoa['idade']", {"nome": "Ana", "cidade": "SP"})
        ]
        
        for operation, new_dict in operations:
            self.animator.clear_screen()
            self.animator.print_colored("📖 OPERAÇÕES EM DICIONÁRIOS", 'cyan')
            print()
            
            self.animator.print_colored(f"Operação: {operation}", 'yellow')
            print()
            
            # Estado anterior
            if dic:
                print("Estado anterior:")
                self._draw_dict(dic)
                print()
            
            # Novo estado
            dic = new_dict.copy()
            
            print("🔄 Executando operação...")
            time.sleep(1 * self.animator.animation_speed)
            
            print("\nNovo estado:")
            self._draw_dict(dic)
            
            time.sleep(2 * self.animator.animation_speed)
            input("\n⏯️ Pressione ENTER para continuar...")
    
    def _draw_dict(self, dic: Dict[str, Any]) -> None:
        """Desenha representação visual de um dicionário"""
        if not dic:
            print("  pessoa = {} (vazio)")
            return
        
        print("  pessoa = {")
        for i, (key, value) in enumerate(dic.items()):
            is_last = i == len(dic) - 1
            value_str = f"'{value}'" if isinstance(value, str) else str(value)
            comma = "" if is_last else ","
            print(f"    '{key}': {value_str}{comma}")
        print("  }")


class InteractiveDemoSession:
    """Sessão principal de demos interativas"""
    
    def __init__(self, ui_components):
        self.ui = ui_components
        self.animator = ASCIIAnimator()
        self.variable_demo = VariableDemo(self.animator)
        self.loop_demo = LoopDemo(self.animator)
        self.conditional_demo = ConditionalDemo(self.animator)
        self.data_demo = DataStructureDemo(self.animator)
    
    def start_demo_session(self) -> None:
        """Inicia sessão de demos interativas"""
        self.ui.header("DEMOS INTERATIVAS", "Visualizações Python", "🎥")
        
        # Introdução explicativa
        print("\n" + "="*60)
        print("🎓 BEM-VINDO ÀS DEMOS INTERATIVAS!")
        print("="*60)
        print("🎯 OBJETIVO: Visualizar como Python funciona internamente")
        print("🧠 APRENDA: Como o código é executado passo a passo")
        print("👁️ VEJA: Variáveis, loops e estruturas em ação!")
        print("\n💡 DICA: Use estas demos para entender conceitos difíceis")
        print("⚡ INTERATIVO: Pressione ENTER para avançar em cada etapa")
        
        while True:
            print("\n" + "="*60)
            print("🎯 ESCOLHA UMA CATEGORIA DE DEMO:")
            print("="*60)
            
            print("\n📊 1. VARIÁVEIS E MEMÓRIA")
            print("   🔍 Veja como Python armazena dados na memória")
            print("   📝 Entenda atribuições e referências")
            
            print("\n🔄 2. LOOPS E REPETIÇÕES") 
            print("   🎲 Visualize for e while em execução")
            print("   👀 Acompanhe cada iteração detalhadamente")
            
            print("\n🔀 3. CONDICIONAIS (IF/ELSE)")
            print("   🧭 Veja o fluxo de decisão do programa")
            print("   ⚖️ Entenda como Python escolhe caminhos")
            
            print("\n📦 4. ESTRUTURAS DE DADOS")
            print("   📋 Visualize listas e dicionários em ação")
            print("   🔧 Veja operações sendo executadas")
            
            print("\n🎮 5. DEMOS AVANÇADAS")
            print("   🚀 Recursão, algoritmos e conceitos avançados")
            print("   🧩 Quebra-cabeças visuais de programação")
            
            print("\n⚙️ 6. CONFIGURAÇÕES")
            print("   🐌 Ajuste velocidade das animações")
            print("   🎨 Personalize visualizações")
            
            print("\n🔙 0. VOLTAR AO MENU PRINCIPAL")
            
            choice = input("\n👉 Sua escolha (0-6): ").strip()
            
            if choice == "1":
                self._variable_demos_menu()
            elif choice == "2":
                self._loop_demos_menu()
            elif choice == "3":
                self._conditional_demos_menu()
            elif choice == "4":
                self._data_structure_demos_menu()
            elif choice == "5":
                self._advanced_demos_menu()
            elif choice == "6":
                self._animation_settings()
            elif choice == "0":
                break
            else:
                print("❌ Opção inválida! Escolha um número de 0 a 6.")
    
    def _variable_demos_menu(self) -> None:
        """Menu de demos de variáveis"""
        self.ui.section("DEMOS: VARIÁVEIS E MEMÓRIA", "📊")
        
        print("\n🎓 APRENDA COMO PYTHON GERENCIA VARIÁVEIS:")
        print("=" * 50)
        print("🧠 Veja como Python armazena dados na memória")
        print("🔗 Entenda referências e atribuições")
        print("📍 Visualize endereços de memória")
        
        print("\n🎯 ESCOLHA UMA DEMONSTRAÇÃO:")
        print("\n1. 📝 ATRIBUIÇÃO BÁSICA")
        print("   💡 Como criar e modificar variáveis")
        print("   👀 Veja: nome = 'Python', idade = 25")
        print("   🎯 Aprenda: Atribuição, reatribuição, tipos")
        
        print("\n2. 🔤 STRINGS NA MEMÓRIA")
        print("   💡 Como Python armazena texto")
        print("   👀 Veja: Cada caractere tem seu endereço")
        print("   🎯 Aprenda: Indexação, imutabilidade")
        
        print("\n3. 📋 LISTAS NA MEMÓRIA")
        print("   💡 Como Python gerencia coleções")
        print("   👀 Veja: Operações append, insert, remove")
        print("   🎯 Aprenda: Mutabilidade, índices dinâmicos")
        
        print("\n4. 🔄 REFERÊNCIAS E CÓPIAS")
        print("   💡 Diferença entre = e copy()")
        print("   👀 Veja: Variáveis apontando para o mesmo objeto")
        print("   🎯 Aprenda: Shallow vs deep copy")
        
        print("\n0. 🔙 VOLTAR")
        
        choice = input("\n👉 Sua escolha (0-4): ").strip()
        
        if choice == "1":
            self._explain_demo("Atribuição Básica", 
                             "Vamos ver como Python cria e modifica variáveis na memória")
            self.variable_demo.basic_assignment_demo()
        elif choice == "2":
            self._explain_demo("Strings na Memória", 
                             "Descobriremos como Python armazena caracteres e strings")
            self.variable_demo.string_memory_demo()
        elif choice == "3":
            self._explain_demo("Listas na Memória", 
                             "Acompanharemos operações em listas passo a passo")
            self.variable_demo.list_memory_demo()
        elif choice == "4":
            self._explain_demo("Referências e Cópias", 
                             "Entenderemos como Python gerencia referências de objetos")
            self._reference_demo()
        elif choice == "0":
            return
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 4.")
            self._variable_demos_menu()
    
    def _loop_demos_menu(self) -> None:
        """Menu de demos de loops"""
        self.ui.section("DEMOS: LOOPS E REPETIÇÕES", "🔄")
        
        print("\n🎓 APRENDA COMO PYTHON EXECUTA REPETIÇÕES:")
        print("=" * 50)
        print("🔄 Veja cada iteração sendo executada")
        print("📊 Acompanhe variáveis mudando a cada ciclo")
        print("🎯 Entenda condições de parada")
        
        print("\n🎯 ESCOLHA UMA DEMONSTRAÇÃO:")
        print("\n1. 🔢 LOOP FOR")
        print("   💡 Repetição com número definido")
        print("   👀 Veja: for i in range(5)")
        print("   🎯 Aprenda: Iteração, range(), variável de controle")
        
        print("\n2. ⏰ LOOP WHILE")
        print("   💡 Repetição com condição")
        print("   👀 Veja: while contador < 10")
        print("   🎯 Aprenda: Condições, incremento, loops infinitos")
        
        print("\n3. 🔗 LOOPS ANINHADOS")
        print("   💡 Loop dentro de outro loop")
        print("   👀 Veja: Tabela de multiplicação sendo criada")
        print("   🎯 Aprenda: Loops 2D, coordenadas, complexidade")
        
        print("\n4. 🛑 BREAK E CONTINUE")
        print("   💡 Controlando fluxo dos loops")
        print("   👀 Veja: Como sair ou pular iterações")
        print("   🎯 Aprenda: break, continue, else em loops")
        
        print("\n5. 📋 ITERANDO LISTAS")
        print("   💡 Percorrendo elementos de listas")
        print("   👀 Veja: for item in lista")
        print("   🎯 Aprenda: Iteração direta, enumerate(), zip()")
        
        print("\n0. 🔙 VOLTAR")
        
        choice = input("\n👉 Sua escolha (0-5): ").strip()
        
        if choice == "1":
            self._explain_demo("Loop For", 
                             "Veremos como o for executa um número específico de vezes")
            self.loop_demo.for_loop_demo()
        elif choice == "2":
            self._explain_demo("Loop While", 
                             "Acompanharemos como o while verifica condições a cada iteração")
            self.loop_demo.while_loop_demo()
        elif choice == "3":
            self._explain_demo("Loops Aninhados", 
                             "Entenderemos como loops dentro de loops funcionam")
            self.loop_demo.nested_loop_demo()
        elif choice == "4":
            self._explain_demo("Break e Continue", 
                             "Descobriremos como controlar o fluxo de loops")
            self._break_continue_demo()
        elif choice == "5":
            self._explain_demo("Iterando Listas", 
                             "Aprenderemos diferentes formas de percorrer listas")
            self._list_iteration_demo()
        elif choice == "0":
            return
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 5.")
            self._loop_demos_menu()
    
    def _conditional_demos_menu(self) -> None:
        """Menu de demos de condicionais"""
        self.ui.section("DEMOS: CONDICIONAIS", "🔀")
        
        print("1. ↔️ If/Else Básico")
        print("2. 🎯 If/Elif/Else")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self.conditional_demo.if_else_demo()
        elif choice == "2":
            self.conditional_demo.elif_demo()
    
    def _data_structure_demos_menu(self) -> None:
        """Menu de demos de estruturas de dados"""
        self.ui.section("DEMOS: ESTRUTURAS DE DADOS", "📦")
        
        print("1. 📋 Operações em Listas")
        print("2. 📖 Operações em Dicionários")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self.data_demo.list_operations_demo()
        elif choice == "2":
            self.data_demo.dictionary_demo()
    
    def _animation_settings(self) -> None:
        """Configurações de animação"""
        self.ui.section("CONFIGURAÇÕES DE ANIMAÇÃO", "⚙️")
        
        print(f"Velocidade atual: {self.animator.animation_speed:.1f}x")
        print()
        print("1. 🐌 Lenta (0.5x)")
        print("2. ⚡ Normal (1.0x)")
        print("3. 🚀 Rápida (2.0x)")
        print("4. 💨 Muito Rápida (3.0x)")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        speed_map = {
            "1": 0.5,
            "2": 1.0,
            "3": 2.0,
            "4": 3.0
        }
        
        if choice in speed_map:
            self.animator.animation_speed = speed_map[choice]
            self.ui.alert(f"✅ Velocidade alterada para {speed_map[choice]}x", "success")
    
    def _explain_demo(self, demo_name: str, description: str) -> None:
        """Explica o que a demo vai mostrar"""
        self.animator.clear_screen()
        print("=" * 60)
        print(f"🎥 DEMO: {demo_name.upper()}")
        print("=" * 60)
        print(f"\n📖 O QUE VOCÊ VAI APRENDER:")
        print(f"   {description}")
        print("\n💡 COMO FUNCIONA:")
        print("   • A demo executa código Python passo a passo")
        print("   • Você verá variáveis e estados mudando em tempo real")
        print("   • Pressione ENTER para avançar em cada etapa")
        print("   • Observe os comentários explicativos")
        print("\n🚀 VAMOS COMEÇAR!")
        input("\n⏯️ Pressione ENTER para iniciar a demonstração...")
    
    def _reference_demo(self) -> None:
        """Demo sobre referências e cópias"""
        self.animator.clear_screen()
        self.animator.print_colored("🔄 DEMO: REFERÊNCIAS E CÓPIAS", 'cyan')
        print()
        
        print("📝 Vamos ver a diferença entre = e copy()")
        print()
        
        # Demonstração com listas
        print("1️⃣ CRIANDO LISTA ORIGINAL:")
        print("   lista_a = [1, 2, 3]")
        lista_a = [1, 2, 3]
        self._draw_list_reference("lista_a", lista_a, "0x1000")
        input("⏯️ Pressione ENTER para continuar...")
        
        print("\n2️⃣ ATRIBUIÇÃO SIMPLES (REFERÊNCIA):")
        print("   lista_b = lista_a  # Mesma referência!")
        lista_b = lista_a
        self._draw_list_reference("lista_b", lista_b, "0x1000")
        print("🔗 AMBAS APONTAM PARA O MESMO OBJETO!")
        input("⏯️ Pressione ENTER para continuar...")
        
        print("\n3️⃣ MODIFICANDO lista_a:")
        print("   lista_a.append(4)")
        lista_a.append(4)
        self._draw_list_reference("lista_a", lista_a, "0x1000")
        self._draw_list_reference("lista_b", lista_b, "0x1000")
        print("😱 lista_b TAMBÉM MUDOU! (mesma referência)")
        input("⏯️ Pressione ENTER para continuar...")
        
        print("\n4️⃣ FAZENDO CÓPIA VERDADEIRA:")
        print("   lista_c = lista_a.copy()")
        lista_c = lista_a.copy()
        self._draw_list_reference("lista_c", lista_c, "0x2000")
        print("✅ Agora lista_c é INDEPENDENTE!")
        input("⏯️ Pressione ENTER para finalizar...")
    
    def _draw_list_reference(self, name: str, lista: list, address: str) -> None:
        """Desenha lista com endereço de memória"""
        print(f"\n{name} → {address}")
        items_str = " │ ".join(str(x) for x in lista)
        sep_str = "─" * (len(items_str) + 2)
        print(f"         ┌{sep_str}┐")
        print(f"         │ {items_str} │")
        print(f"         └{sep_str}┘")
    
    def _break_continue_demo(self) -> None:
        """Demo sobre break e continue"""
        self.animator.clear_screen()
        self.animator.print_colored("🛑 DEMO: BREAK E CONTINUE", 'cyan')
        print()
        
        print("🎯 Vamos ver como controlar loops:")
        print()
        
        # Demo break
        print("1️⃣ USANDO BREAK (sair do loop):")
        print("   for i in range(10):")
        print("       if i == 5:")
        print("           break")
        print("       print(i)")
        print()
        
        for i in range(10):
            if i == 5:
                print(f"   i = {i} → BREAK! Saindo do loop...")
                break
            print(f"   i = {i}")
            time.sleep(0.5)
        
        input("\n⏯️ Pressione ENTER para ver CONTINUE...")
        
        # Demo continue
        print("\n2️⃣ USANDO CONTINUE (pular iteração):")
        print("   for i in range(6):")
        print("       if i == 3:")
        print("           continue")
        print("       print(i)")
        print()
        
        for i in range(6):
            if i == 3:
                print(f"   i = {i} → CONTINUE! Pulando para próxima iteração...")
                continue
            print(f"   i = {i}")
            time.sleep(0.5)
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _list_iteration_demo(self) -> None:
        """Demo sobre iteração em listas"""
        self.animator.clear_screen()
        self.animator.print_colored("📋 DEMO: ITERANDO LISTAS", 'cyan')
        print()
        
        frutas = ['maçã', 'banana', 'laranja']
        print("🍎 Lista de frutas:", frutas)
        print()
        
        # Iteração simples
        print("1️⃣ ITERAÇÃO SIMPLES:")
        print("   for fruta in frutas:")
        print("       print(fruta)")
        print()
        
        for fruta in frutas:
            print(f"   Fruta: {fruta}")
            time.sleep(0.8)
        
        input("\n⏯️ Pressione ENTER para ver ENUMERATE...")
        
        # Com enumerate
        print("\n2️⃣ COM ENUMERATE (índice + valor):")
        print("   for i, fruta in enumerate(frutas):")
        print("       print(f'{i}: {fruta}')")
        print()
        
        for i, fruta in enumerate(frutas):
            print(f"   {i}: {fruta}")
            time.sleep(0.8)
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _advanced_demos_menu(self) -> None:
        """Menu de demos avançadas"""
        self.ui.section("DEMOS: CONCEITOS AVANÇADOS", "🎮")
        
        print("\n🎓 APRENDA CONCEITOS MAIS COMPLEXOS:")
        print("=" * 50)
        print("🧠 Visualize algoritmos em ação")
        print("🔄 Entenda recursão e complexidade")
        print("🎯 Quebra-cabeças de programação")
        
        print("\n🎯 ESCOLHA UMA DEMONSTRAÇÃO:")
        print("\n1. 🌀 RECURSÃO")
        print("   💡 Função que chama a si mesma")
        print("   👀 Veja: Factorial, Fibonacci")
        print("   🎯 Aprenda: Stack, casos base, recursão infinita")
        
        print("\n2. 🔄 ALGORITMOS DE ORDENAÇÃO")
        print("   💡 Como ordenar listas")
        print("   👀 Veja: Bubble Sort vs Quick Sort")
        print("   🎯 Aprenda: Complexidade, eficiência")
        
        print("\n3. 🔍 BUSCA EM LISTAS")
        print("   💡 Como encontrar elementos")
        print("   👀 Veja: Busca linear vs binária")
        print("   🎯 Aprenda: Big O, otimização")
        
        print("\n4. 🧮 PILHAS E FILAS")
        print("   💡 Estruturas de dados especiais")
        print("   👀 Veja: LIFO vs FIFO em ação")
        print("   🎯 Aprenda: Stack, Queue, operações")
        
        print("\n0. 🔙 VOLTAR")
        
        choice = input("\n👉 Sua escolha (0-4): ").strip()
        
        if choice == "1":
            self._explain_demo("Recursão", 
                             "Veremos como funções podem chamar a si mesmas")
            self._recursion_demo()
        elif choice == "2":
            self._explain_demo("Algoritmos de Ordenação", 
                             "Compararemos diferentes formas de ordenar listas")
            self._sorting_demo()
        elif choice == "3":
            self._explain_demo("Busca em Listas", 
                             "Aprenderemos diferentes estratégias de busca")
            self._search_demo()
        elif choice == "4":
            self._explain_demo("Pilhas e Filas", 
                             "Entenderemos estruturas de dados LIFO e FIFO")
            self._stack_queue_demo()
        elif choice == "0":
            return
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 4.")
            self._advanced_demos_menu()
    
    def _recursion_demo(self) -> None:
        """Demo sobre recursão"""
        self.animator.clear_screen()
        self.animator.print_colored("🌀 DEMO: RECURSÃO", 'cyan')
        print()
        
        print("🎯 Vamos calcular 4! (fatorial de 4):")
        print("   def factorial(n):")
        print("       if n <= 1:")
        print("           return 1")
        print("       return n * factorial(n-1)")
        print()
        
        def factorial_visual(n, depth=0):
            indent = "  " * depth
            print(f"{indent}📞 factorial({n})")
            
            if n <= 1:
                print(f"{indent}✅ Caso base: return 1")
                time.sleep(1)
                return 1
            
            print(f"{indent}🔄 {n} * factorial({n-1})")
            time.sleep(1)
            result = n * factorial_visual(n-1, depth+1)
            print(f"{indent}📤 return {result}")
            time.sleep(1)
            return result
        
        print("🚀 EXECUTANDO:")
        result = factorial_visual(4)
        print(f"\n🎉 RESULTADO: 4! = {result}")
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _sorting_demo(self) -> None:
        """Demo sobre algoritmos de ordenação"""
        self.animator.clear_screen()
        self.animator.print_colored("🔄 DEMO: ALGORITMOS DE ORDENAÇÃO", 'cyan')
        print()
        
        lista = [64, 34, 25, 12, 22, 11, 90]
        print(f"📋 Lista original: {lista}")
        print()
        
        # Bubble Sort visual
        print("🫧 BUBBLE SORT (lento mas visual):")
        lista_bubble = lista.copy()
        n = len(lista_bubble)
        
        for i in range(n):
            for j in range(0, n-i-1):
                print(f"   Comparando {lista_bubble[j]} e {lista_bubble[j+1]}")
                if lista_bubble[j] > lista_bubble[j+1]:
                    lista_bubble[j], lista_bubble[j+1] = lista_bubble[j+1], lista_bubble[j]
                    print(f"   🔄 Trocou! {lista_bubble}")
                else:
                    print(f"   ✅ Não troca")
                time.sleep(0.5)
        
        print(f"\n🎉 RESULTADO: {lista_bubble}")
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _search_demo(self) -> None:
        """Demo sobre busca"""
        self.animator.clear_screen()
        self.animator.print_colored("🔍 DEMO: BUSCA EM LISTAS", 'cyan')
        print()
        
        lista = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78]
        target = 23
        
        print(f"📋 Lista ordenada: {lista}")
        print(f"🎯 Procurando: {target}")
        print()
        
        # Busca linear
        print("🔍 BUSCA LINEAR:")
        for i, num in enumerate(lista):
            print(f"   Posição {i}: {num}", end="")
            if num == target:
                print(" ← ENCONTRADO! 🎉")
                break
            else:
                print(" (não é)")
            time.sleep(0.5)
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _stack_queue_demo(self) -> None:
        """Demo sobre pilhas e filas"""
        self.animator.clear_screen()
        self.animator.print_colored("🧮 DEMO: PILHAS E FILAS", 'cyan')
        print()
        
        # Pilha (LIFO)
        print("📚 PILHA (LIFO - Last In, First Out):")
        pilha = []
        
        print("   Adicionando elementos:")
        for item in ['A', 'B', 'C']:
            pilha.append(item)
            print(f"   push({item}) → {pilha}")
            time.sleep(0.8)
        
        print("   Removendo elementos:")
        while pilha:
            item = pilha.pop()
            print(f"   pop() → {item}, pilha: {pilha}")
            time.sleep(0.8)
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _conditional_demos_menu(self) -> None:
        """Menu de demos de condicionais"""
        self.ui.section("DEMOS: CONDICIONAIS", "🔀")
        
        print("\n🎓 APRENDA COMO PYTHON TOMA DECISÕES:")
        print("=" * 50)
        print("🧭 Veja o fluxo de decisão em ação")
        print("⚖️ Entenda condições verdadeiras e falsas")
        print("🔀 Acompanhe diferentes caminhos de execução")
        
        print("\n🎯 ESCOLHA UMA DEMONSTRAÇÃO:")
        print("\n1. ↔️ IF/ELSE BÁSICO")
        print("   💡 Tomada de decisão simples")
        print("   👀 Veja: if idade >= 18")
        print("   🎯 Aprenda: Condições, True/False, blocos")
        
        print("\n2. 🎯 IF/ELIF/ELSE")
        print("   💡 Múltiplas condições")
        print("   👀 Veja: Sistema de notas A, B, C, D, F")
        print("   🎯 Aprenda: Sequência de condições, elif")
        
        print("\n3. 🔗 OPERADORES LÓGICOS")
        print("   💡 AND, OR, NOT em ação")
        print("   👀 Veja: Combinações de condições")
        print("   🎯 Aprenda: Lógica booleana, precedência")
        
        print("\n0. 🔙 VOLTAR")
        
        choice = input("\n👉 Sua escolha (0-3): ").strip()
        
        if choice == "1":
            self._explain_demo("If/Else Básico", 
                             "Veremos como Python escolhe entre dois caminhos")
            self.conditional_demo.if_else_demo()
        elif choice == "2":
            self._explain_demo("If/Elif/Else", 
                             "Acompanharemos como Python testa múltiplas condições")
            self.conditional_demo.elif_demo()
        elif choice == "3":
            self._explain_demo("Operadores Lógicos", 
                             "Entenderemos como combinar condições")
            self._logical_operators_demo()
        elif choice == "0":
            return
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 3.")
            self._conditional_demos_menu()
    
    def _logical_operators_demo(self) -> None:
        """Demo sobre operadores lógicos"""
        self.animator.clear_screen()
        self.animator.print_colored("🔗 DEMO: OPERADORES LÓGICOS", 'cyan')
        print()
        
        print("🎯 Vamos testar operadores AND, OR, NOT:")
        print()
        
        # Testando AND
        print("1️⃣ OPERADOR AND (ambos devem ser True):")
        conditions = [
            (True, True, "True and True"),
            (True, False, "True and False"),
            (False, True, "False and True"),
            (False, False, "False and False")
        ]
        
        for a, b, desc in conditions:
            result = a and b
            color = 'green' if result else 'red'
            print(f"   {desc} = ", end="")
            self.animator.print_colored(str(result), color)
            time.sleep(1)
        
        input("\n⏯️ Pressione ENTER para continuar...")
        
        # Exemplo prático
        print("\n🏠 EXEMPLO PRÁTICO - Sistema de acesso:")
        idade = 25
        tem_cartao = True
        
        print(f"   idade = {idade}")
        print(f"   tem_cartao = {tem_cartao}")
        print("   if idade >= 18 and tem_cartao:")
        
        if idade >= 18 and tem_cartao:
            print("       ✅ ACESSO LIBERADO!")
        else:
            print("       ❌ ACESSO NEGADO!")
        
        input("\n⏯️ Pressione ENTER para finalizar...")
    
    def _data_structure_demos_menu(self) -> None:
        """Menu de demos de estruturas de dados"""
        self.ui.section("DEMOS: ESTRUTURAS DE DADOS", "📦")
        
        print("\n🎓 APRENDA COMO PYTHON ORGANIZA DADOS:")
        print("=" * 50)
        print("📋 Veja listas crescendo e diminuindo")
        print("📖 Entenda dicionários e suas chaves")
        print("🔧 Acompanhe operações sendo executadas")
        
        print("\n🎯 ESCOLHA UMA DEMONSTRAÇÃO:")
        print("\n1. 📋 OPERAÇÕES EM LISTAS")
        print("   💡 append, insert, remove, pop")
        print("   👀 Veja: Lista mudando dinamicamente")
        print("   🎯 Aprenda: Índices, métodos, mutabilidade")
        
        print("\n2. 📖 OPERAÇÕES EM DICIONÁRIOS")
        print("   💡 Chaves, valores, items")
        print("   👀 Veja: Dicionário sendo construído")
        print("   🎯 Aprenda: Chave-valor, métodos dict")
        
        print("\n3. 📊 SETS E OPERAÇÕES")
        print("   💡 Conjuntos únicos")
        print("   👀 Veja: União, interseção, diferença")
        print("   🎯 Aprenda: Unicidade, operações matemáticas")
        
        print("\n0. 🔙 VOLTAR")
        
        choice = input("\n👉 Sua escolha (0-3): ").strip()
        
        if choice == "1":
            self._explain_demo("Operações em Listas", 
                             "Veremos como modificar listas dinamicamente")
            self.data_demo.list_operations_demo()
        elif choice == "2":
            self._explain_demo("Operações em Dicionários", 
                             "Acompanharemos a construção de dicionários")
            self.data_demo.dictionary_demo()
        elif choice == "3":
            self._explain_demo("Sets e Operações", 
                             "Entenderemos conjuntos e operações matemáticas")
            self._sets_demo()
        elif choice == "0":
            return
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 3.")
            self._data_structure_demos_menu()
    
    def _sets_demo(self) -> None:
        """Demo sobre sets"""
        self.animator.clear_screen()
        self.animator.print_colored("📊 DEMO: SETS E OPERAÇÕES", 'cyan')
        print()
        
        print("🎯 Vamos trabalhar com conjuntos:")
        print()
        
        # Criando sets
        print("1️⃣ CRIANDO SETS:")
        set_a = {1, 2, 3, 4}
        set_b = {3, 4, 5, 6}
        
        print(f"   set_a = {set_a}")
        print(f"   set_b = {set_b}")
        time.sleep(1)
        
        # União
        print("\n2️⃣ UNIÃO (todos os elementos):")
        uniao = set_a | set_b
        print(f"   set_a | set_b = {uniao}")
        time.sleep(1)
        
        # Interseção
        print("\n3️⃣ INTERSEÇÃO (elementos comuns):")
        intersecao = set_a & set_b
        print(f"   set_a & set_b = {intersecao}")
        time.sleep(1)
        
        # Diferença
        print("\n4️⃣ DIFERENÇA (só em A):")
        diferenca = set_a - set_b
        print(f"   set_a - set_b = {diferenca}")
        
        input("\n⏯️ Pressione ENTER para finalizar...")