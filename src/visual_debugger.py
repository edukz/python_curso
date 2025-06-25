#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Debug Visual
Ferramentas para debug step-by-step com visualização de variáveis e execução
"""

import ast
import sys
import time
import os
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import traceback


class VariableTracker:
    """Rastreador de variáveis durante execução"""
    
    def __init__(self):
        self.variable_history: List[Dict[str, Any]] = []
        self.current_line: int = 0
        self.execution_stack: List[Dict[str, Any]] = []
    
    def track_variables(self, local_vars: Dict[str, Any], line_number: int) -> None:
        """Registra estado das variáveis em uma linha"""
        # Filtra variáveis internas do Python
        filtered_vars = {
            k: v for k, v in local_vars.items() 
            if not k.startswith('__') and k not in ['annotations']
        }
        
        snapshot = {
            "line": line_number,
            "variables": filtered_vars.copy(),
            "timestamp": datetime.now().isoformat()
        }
        
        self.variable_history.append(snapshot)
        self.current_line = line_number
    
    def get_variable_changes(self, line_number: int) -> Dict[str, Any]:
        """Retorna mudanças de variáveis em uma linha específica"""
        current_snapshot = None
        previous_snapshot = None
        
        for snapshot in self.variable_history:
            if snapshot["line"] == line_number:
                current_snapshot = snapshot
            elif snapshot["line"] == line_number - 1:
                previous_snapshot = snapshot
        
        if not current_snapshot:
            return {}
        
        changes = {
            "new_variables": {},
            "modified_variables": {},
            "unchanged_variables": {}
        }
        
        current_vars = current_snapshot["variables"]
        previous_vars = previous_snapshot["variables"] if previous_snapshot else {}
        
        for var_name, var_value in current_vars.items():
            if var_name not in previous_vars:
                changes["new_variables"][var_name] = var_value
            elif previous_vars[var_name] != var_value:
                changes["modified_variables"][var_name] = {
                    "old": previous_vars[var_name],
                    "new": var_value
                }
            else:
                changes["unchanged_variables"][var_name] = var_value
        
        return changes


class CodeVisualizer:
    """Visualizador de código com destaque de execução"""
    
    def __init__(self):
        self.colors = {
            'current': '\033[43m\033[30m',  # Fundo amarelo, texto preto
            'executed': '\033[42m\033[30m',  # Fundo verde, texto preto
            'error': '\033[41m\033[37m',     # Fundo vermelho, texto branco
            'reset': '\033[0m',              # Reset
            'line_num': '\033[36m',          # Ciano
            'variable': '\033[35m',          # Magenta
            'value': '\033[32m'              # Verde
        }
    
    def display_code_with_highlights(self, code_lines: List[str], 
                                   current_line: int, 
                                   executed_lines: List[int] = None,
                                   error_line: int = None) -> None:
        """Exibe código com destacamento de linhas"""
        executed_lines = executed_lines or []
        
        print("\n" + "="*60)
        print(" " * 20 + "VISUALIZAÇÃO DO CÓDIGO")
        print("="*60)
        
        for i, line in enumerate(code_lines, 1):
            # Determina cor da linha
            line_color = ""
            if i == error_line:
                line_color = self.colors['error']
            elif i == current_line:
                line_color = self.colors['current']
            elif i in executed_lines:
                line_color = self.colors['executed']
            
            # Número da linha
            line_num = f"{self.colors['line_num']}{i:3d}{self.colors['reset']}"
            
            # Indicador de execução
            if i == current_line:
                indicator = " ➤ "
            elif i in executed_lines:
                indicator = " ✓ "
            elif i == error_line:
                indicator = " ❌ "
            else:
                indicator = "   "
            
            # Exibe linha
            print(f"{line_num}{indicator}{line_color}{line.rstrip()}{self.colors['reset']}")
        
        print("="*60)
    
    def display_variables_table(self, variables: Dict[str, Any], 
                              changes: Dict[str, Any] = None) -> None:
        """Exibe tabela de variáveis com destaque para mudanças"""
        if not variables:
            print("\n📋 Nenhuma variável definida ainda")
            return
        
        changes = changes or {}
        
        print(f"\n{self.colors['variable']}📋 ESTADO DAS VARIÁVEIS:{self.colors['reset']}")
        print("─" * 50)
        
        for var_name, var_value in variables.items():
            # Determina status da variável
            status = ""
            if var_name in changes.get("new_variables", {}):
                status = f"{self.colors['current']} NOVA {self.colors['reset']}"
            elif var_name in changes.get("modified_variables", {}):
                old_value = changes["modified_variables"][var_name]["old"]
                status = f"{self.colors['current']} ALTERADA {self.colors['reset']} (era: {old_value})"
            
            # Formata valor
            value_str = self._format_value(var_value)
            
            print(f"{self.colors['variable']}{var_name:15}{self.colors['reset']} = {self.colors['value']}{value_str}{self.colors['reset']} {status}")
        
        print("─" * 50)
    
    def _format_value(self, value: Any) -> str:
        """Formata valor para exibição"""
        if isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, list):
            if len(value) <= 5:
                return str(value)
            else:
                return f"[{', '.join(map(str, value[:3]))}, ... +{len(value)-3} itens]"
        elif isinstance(value, dict):
            if len(value) <= 3:
                return str(value)
            else:
                keys = list(value.keys())[:2]
                return f"{{{', '.join(f'{k}: {value[k]}' for k in keys)}, ... +{len(value)-2} itens}}"
        else:
            return str(value)
    
    def display_execution_arrow(self, message: str = "Executando...") -> None:
        """Exibe seta de execução com animação"""
        print(f"\n{self.colors['current']} ▶ {message} {self.colors['reset']}")


class StepByStepDebugger:
    """Debugger que executa código passo a passo"""
    
    def __init__(self, ui_components):
        self.ui = ui_components
        self.tracker = VariableTracker()
        self.visualizer = CodeVisualizer()
        self.breakpoints: List[int] = []
        self.current_namespace: Dict[str, Any] = {}
        self.executed_lines: List[int] = []
        self.paused = False
    
    def debug_code(self, code: str, auto_step: bool = False) -> None:
        """Executa código em modo debug step-by-step"""
        try:
            # Parse do código
            tree = ast.parse(code)
            code_lines = code.split('\n')
            
            # Mostra código inicial
            self.visualizer.display_code_with_highlights(code_lines, 0)
            
            if not auto_step:
                input("\n🎯 Pressione ENTER para começar o debug...")
            
            # Executa com instrumentação
            self._execute_with_instrumentation(tree, code_lines, auto_step)
            
        except SyntaxError as e:
            self._show_syntax_error(e, code.split('\n'))
        except Exception as e:
            self._show_runtime_error(e, code.split('\n'))
    
    def _execute_with_instrumentation(self, tree: ast.AST, code_lines: List[str], auto_step: bool) -> None:
        """Executa AST com instrumentação para debug"""
        
        # Adiciona instrumentação ao AST
        instrumented_tree = self._instrument_ast(tree)
        
        # Compila código instrumentado
        compiled_code = compile(instrumented_tree, '<debug>', 'exec')
        
        # Namespace para execução
        debug_namespace = {
            '__debug_tracker__': self._debug_step_callback,
            '__builtins__': __builtins__
        }
        
        try:
            # Executa código instrumentado
            exec(compiled_code, debug_namespace, debug_namespace)
            
            print(f"\n{self.visualizer.colors['executed']}✅ Execução concluída com sucesso!{self.visualizer.colors['reset']}")
            
        except Exception as e:
            self._show_runtime_error(e, code_lines)
    
    def _instrument_ast(self, tree: ast.AST) -> ast.AST:
        """Adiciona instrumentação ao AST para rastreamento"""
        
        class DebugInstrumenter(ast.NodeTransformer):
            def visit_stmt(self, node):
                # Adiciona chamada de rastreamento antes de cada statement
                if hasattr(node, 'lineno'):
                    debug_call = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id='__debug_tracker__', ctx=ast.Load()),
                            args=[ast.Constant(value=node.lineno)],
                            keywords=[]
                        )
                    )
                    debug_call.lineno = node.lineno
                    debug_call.col_offset = 0
                    
                    # Retorna sequência com debug call + statement original
                    return [debug_call, self.generic_visit(node)]
                
                return self.generic_visit(node)
            
            # Instrumenta diferentes tipos de statements
            visit_Assign = visit_stmt
            visit_AugAssign = visit_stmt
            visit_Expr = visit_stmt
            visit_If = visit_stmt
            visit_For = visit_stmt
            visit_While = visit_stmt
            visit_FunctionDef = visit_stmt
            visit_Return = visit_stmt
        
        instrumenter = DebugInstrumenter()
        return instrumenter.visit(tree)
    
    def _debug_step_callback(self, line_number: int) -> None:
        """Callback chamado a cada step do debug"""
        # Obtém frame atual
        frame = sys._getframe(1)
        local_vars = frame.f_locals.copy()
        
        # Remove variáveis internas do debug
        local_vars = {k: v for k, v in local_vars.items() 
                     if not k.startswith('__debug')}
        
        # Atualiza rastreamento
        self.tracker.track_variables(local_vars, line_number)
        self.executed_lines.append(line_number)
        
        # Obtém mudanças de variáveis
        changes = self.tracker.get_variable_changes(line_number)
        
        # Limpa tela e mostra estado atual
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Reconstrói código original do frame
        code_lines = []
        if frame.f_code.co_filename == '<debug>':
            # Tenta reconstruir do AST original (simplificado)
            code_lines = ["# Código em execução..."]
        else:
            try:
                with open(frame.f_code.co_filename, 'r') as f:
                    code_lines = f.readlines()
            except:
                code_lines = ["# Código não disponível"]
        
        # Visualiza estado atual
        self.visualizer.display_code_with_highlights(
            code_lines, line_number, self.executed_lines
        )
        
        self.visualizer.display_variables_table(local_vars, changes)
        
        # Controles do debug
        self._show_debug_controls()
        
        # Pausa para interação do usuário
        if not self.paused:
            command = input("\n🎮 Debug> ").strip().lower()
            self._process_debug_command(command, line_number)
    
    def _show_debug_controls(self) -> None:
        """Mostra controles disponíveis do debugger"""
        print(f"\n{self.visualizer.colors['variable']}🎮 CONTROLES:{self.visualizer.colors['reset']}")
        print("  ENTER/n - Próximo passo")
        print("  c - Continuar execução")
        print("  b <linha> - Adicionar breakpoint")
        print("  p <var> - Examinar variável")
        print("  l - Listar variáveis")
        print("  q - Sair do debug")
    
    def _process_debug_command(self, command: str, current_line: int) -> None:
        """Processa comandos do debug"""
        if command in ['', 'n', 'next']:
            # Próximo passo (padrão)
            pass
        
        elif command in ['c', 'continue']:
            self.paused = True
            print("▶ Continuando execução...")
        
        elif command.startswith('b '):
            # Adicionar breakpoint
            try:
                line_num = int(command.split()[1])
                self.breakpoints.append(line_num)
                print(f"🔴 Breakpoint adicionado na linha {line_num}")
            except (ValueError, IndexError):
                print("❌ Uso: b <número_da_linha>")
            input("Pressione ENTER...")
        
        elif command.startswith('p '):
            # Examinar variável
            var_name = command.split()[1]
            frame = sys._getframe(2)  # Frame do código em debug
            if var_name in frame.f_locals:
                value = frame.f_locals[var_name]
                print(f"\n🔍 {var_name} = {self.visualizer._format_value(value)}")
                print(f"   Tipo: {type(value).__name__}")
                if hasattr(value, '__len__'):
                    print(f"   Tamanho: {len(value)}")
            else:
                print(f"❌ Variável '{var_name}' não encontrada")
            input("Pressione ENTER...")
        
        elif command in ['l', 'list']:
            # Listar todas as variáveis
            frame = sys._getframe(2)
            self.visualizer.display_variables_table(frame.f_locals)
            input("Pressione ENTER...")
        
        elif command in ['q', 'quit']:
            print("🛑 Debug interrompido")
            raise KeyboardInterrupt()
        
        else:
            print("❌ Comando não reconhecido")
            input("Pressione ENTER...")
    
    def _show_syntax_error(self, error: SyntaxError, code_lines: List[str]) -> None:
        """Mostra erro de sintaxe com destacamento"""
        error_line = error.lineno or 1
        
        print(f"\n{self.visualizer.colors['error']}❌ ERRO DE SINTAXE:{self.visualizer.colors['reset']}")
        
        self.visualizer.display_code_with_highlights(
            code_lines, 0, error_line=error_line
        )
        
        print(f"\n🔍 DETALHES DO ERRO:")
        print(f"   Linha {error_line}: {error.msg}")
        if error.text:
            print(f"   Código: {error.text.strip()}")
        
        print(f"\n💡 DICAS PARA CORRIGIR:")
        self._suggest_syntax_fix(error)
    
    def _show_runtime_error(self, error: Exception, code_lines: List[str]) -> None:
        """Mostra erro de execução com contexto"""
        tb = traceback.extract_tb(error.__traceback__)
        
        # Encontra linha do erro no código do usuário
        error_line = 1
        for frame in tb:
            if frame.filename in ['<debug>', '<string>']:
                error_line = frame.lineno
                break
        
        print(f"\n{self.visualizer.colors['error']}❌ ERRO DE EXECUÇÃO:{self.visualizer.colors['reset']}")
        
        self.visualizer.display_code_with_highlights(
            code_lines, 0, self.executed_lines, error_line
        )
        
        print(f"\n🔍 DETALHES DO ERRO:")
        print(f"   Tipo: {type(error).__name__}")
        print(f"   Mensagem: {str(error)}")
        print(f"   Linha: {error_line}")
        
        # Mostra variáveis no momento do erro
        if self.tracker.variable_history:
            last_snapshot = self.tracker.variable_history[-1]
            self.visualizer.display_variables_table(last_snapshot["variables"])
        
        print(f"\n💡 SUGESTÕES DE CORREÇÃO:")
        self._suggest_runtime_fix(error)
    
    def _suggest_syntax_fix(self, error: SyntaxError) -> None:
        """Sugere correções para erro de sintaxe"""
        if "invalid syntax" in error.msg.lower():
            print("   • Verifique parênteses, colchetes e chaves")
            print("   • Confirme se tem ':' após if, for, while, def")
            print("   • Verifique se fechou todas as aspas")
        elif "unexpected indent" in error.msg.lower():
            print("   • Problema de indentação - use 4 espaços")
            print("   • Não misture tabs e espaços")
        elif "unindent" in error.msg.lower():
            print("   • Indentação inconsistente")
            print("   • Verifique o alinhamento do código")
    
    def _suggest_runtime_fix(self, error: Exception) -> None:
        """Sugere correções para erro de execução"""
        error_type = type(error).__name__
        
        if error_type == "NameError":
            print("   • Variável não foi definida antes do uso")
            print("   • Verifique a grafia do nome")
            print("   • Declare a variável primeiro")
        elif error_type == "TypeError":
            print("   • Tipos incompatíveis na operação")
            print("   • Verifique os tipos das variáveis")
            print("   • Use conversão se necessário (int, str, float)")
        elif error_type == "IndexError":
            print("   • Tentou acessar índice que não existe")
            print("   • Verifique o tamanho da lista")
            print("   • Lembre que índices começam em 0")
        elif error_type == "KeyError":
            print("   • Chave não existe no dicionário")
            print("   • Use .get() para chaves opcionais")
            print("   • Verifique se a chave está correta")
        elif error_type == "ValueError":
            print("   • Valor inválido para a operação")
            print("   • Verifique se o valor pode ser convertido")
            print("   • Valide entradas do usuário")


class CodeComparer:
    """Comparador de código esperado vs obtido"""
    
    def __init__(self, ui_components):
        self.ui = ui_components
    
    def compare_outputs(self, expected: str, actual: str, code: str) -> None:
        """Compara saída esperada com saída obtida"""
        self.ui.header("COMPARAÇÃO DE RESULTADOS", "Esperado vs Obtido", "🔍")
        
        print("📝 CÓDIGO EXECUTADO:")
        print("```python")
        print(code)
        print("```")
        
        print(f"\n✅ SAÍDA ESPERADA:")
        print(f"   {expected}")
        
        print(f"\n📤 SAÍDA OBTIDA:")
        print(f"   {actual}")
        
        if expected.strip() == actual.strip():
            self.ui.alert("🎉 Saídas coincidem perfeitamente!", "success")
        else:
            self.ui.alert("❌ Saídas diferentes - vamos analisar!", "warning")
            self._analyze_differences(expected, actual)
    
    def _analyze_differences(self, expected: str, actual: str) -> None:
        """Analisa diferenças entre saídas"""
        print(f"\n🔍 ANÁLISE DAS DIFERENÇAS:")
        
        # Diferenças básicas
        if len(expected) != len(actual):
            print(f"   📏 Tamanhos diferentes: esperado {len(expected)}, obtido {len(actual)}")
        
        # Diferenças de espaços
        if expected.strip() == actual.strip():
            print("   🔤 Conteúdo igual, mas espaços diferentes")
            print("   💡 Dica: Verifique espaços em branco extras")
        
        # Diferenças de maiúsculas
        elif expected.lower() == actual.lower():
            print("   🔤 Conteúdo igual, mas maiúsculas/minúsculas diferentes")
            print("   💡 Dica: Verifique a capitalização")
        
        # Diferenças de números
        elif expected.replace('.', '').isdigit() and actual.replace('.', '').isdigit():
            try:
                exp_num = float(expected)
                act_num = float(actual)
                diff = abs(exp_num - act_num)
                print(f"   🔢 Diferença numérica: {diff}")
                if diff < 0.01:
                    print("   💡 Diferença mínima - pode ser arredondamento")
            except ValueError:
                pass
        
        else:
            print("   📝 Conteúdos completamente diferentes")
            print("   💡 Dica: Revise a lógica do código")


class DebugSession:
    """Sessão completa de debug com interface"""
    
    def __init__(self, ui_components):
        self.ui = ui_components
        self.debugger = StepByStepDebugger(ui_components)
        self.comparer = CodeComparer(ui_components)
    
    def start_debug_session(self) -> None:
        """Inicia sessão interativa de debug"""
        self.ui.header("LABORATÓRIO DE DEBUG", "Análise Visual de Código", "🔬")
        
        print("🎯 OPÇÕES DE DEBUG:")
        print("1. 🐛 Debug Step-by-Step")
        print("2. 🔍 Comparar Saídas")
        print("3. 📝 Testar Código com Visualização")
        print("4. 🎓 Tutorial de Debug")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self._step_by_step_debug()
        elif choice == "2":
            self._compare_outputs_session()
        elif choice == "3":
            self._visual_code_test()
        elif choice == "4":
            self._debug_tutorial()
    
    def _step_by_step_debug(self) -> None:
        """Sessão de debug passo a passo"""
        print("\n🐛 DEBUG STEP-BY-STEP")
        print("Digite seu código (digite 'FIM' em uma linha para terminar):")
        
        code_lines = []
        while True:
            line = input(f"{len(code_lines)+1:2d}| ")
            if line.upper().strip() == "FIM":
                break
            code_lines.append(line)
        
        if code_lines:
            code = '\n'.join(code_lines)
            print("\n🔬 Iniciando debug...")
            self.debugger.debug_code(code)
    
    def _compare_outputs_session(self) -> None:
        """Sessão de comparação de saídas"""
        print("\n🔍 COMPARAÇÃO DE SAÍDAS")
        
        print("Digite o código:")
        code_lines = []
        while True:
            line = input(f"{len(code_lines)+1:2d}| ")
            if line.upper().strip() == "FIM":
                break
            code_lines.append(line)
        
        code = '\n'.join(code_lines)
        expected = input("\nSaída esperada: ")
        
        # Executa código e captura saída
        import io
        import contextlib
        
        output_buffer = io.StringIO()
        
        try:
            with contextlib.redirect_stdout(output_buffer):
                exec(code)
            actual = output_buffer.getvalue().strip()
            
            self.comparer.compare_outputs(expected, actual, code)
        
        except Exception as e:
            print(f"\n❌ Erro na execução: {e}")
    
    def _visual_code_test(self) -> None:
        """Teste de código com visualização"""
        print("\n📝 TESTE VISUAL DE CÓDIGO")
        
        examples = [
            ("Variáveis básicas", "nome = 'Python'\nidade = 30\nprint(f'{nome} tem {idade} anos')"),
            ("Loop simples", "for i in range(3):\n    print(f'Número: {i}')"),
            ("Condicionais", "x = 10\nif x > 5:\n    print('Maior')\nelse:\n    print('Menor')"),
            ("Lista", "frutas = ['maçã', 'banana']\nfrutas.append('laranja')\nprint(frutas)")
        ]
        
        print("Escolha um exemplo:")
        for i, (name, _) in enumerate(examples, 1):
            print(f"{i}. {name}")
        print("0. Código personalizado")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "0":
            self._step_by_step_debug()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(examples):
                    name, code = examples[idx]
                    print(f"\n🔬 Debugando: {name}")
                    self.debugger.debug_code(code, auto_step=False)
            except ValueError:
                print("❌ Opção inválida")
    
    def _debug_tutorial(self) -> None:
        """Tutorial de debug"""
        self.ui.header("TUTORIAL DE DEBUG", "Aprenda a Debugar", "🎓")
        
        print("""
🎯 O QUE É DEBUG?
Debug é o processo de encontrar e corrigir erros (bugs) no código.

🔍 TIPOS DE ERROS:
1. Erros de Sintaxe - Código mal escrito
2. Erros de Execução - Código quebra durante execução
3. Erros Lógicos - Código executa mas faz coisa errada

🛠️ FERRAMENTAS DE DEBUG:
• Step-by-step: Executa linha por linha
• Variáveis: Mostra valores em tempo real
• Breakpoints: Pausa em pontos específicos
• Stack trace: Mostra onde erro ocorreu

💡 DICAS PROFISSIONAIS:
• Use print() para rastrear valores
• Teste com dados simples primeiro
• Quebre problemas complexos em partes
• Leia mensagens de erro com atenção

🎮 COMANDOS DO DEBUGGER:
• ENTER - Próximo passo
• c - Continuar até o fim
• p <var> - Examinar variável
• b <linha> - Adicionar breakpoint
• l - Listar todas as variáveis
• q - Sair do debug
""")
        
        input("\n📚 Pressione ENTER para voltar...")