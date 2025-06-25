#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Editor de Código Integrado
Editor simples no terminal com syntax highlighting e funcionalidades básicas
"""

import os
import sys
import time
from typing import List, Optional, Tuple, Dict, Any
from datetime import datetime
import re


class SyntaxHighlighter:
    """Highlighter simples para Python"""
    
    # Cores ANSI
    COLORS = {
        'keyword': '\033[94m',      # Azul
        'string': '\033[92m',       # Verde
        'comment': '\033[90m',      # Cinza
        'number': '\033[93m',       # Amarelo
        'function': '\033[96m',     # Ciano
        'error': '\033[91m',        # Vermelho
        'reset': '\033[0m'          # Reset
    }
    
    # Palavras-chave Python
    KEYWORDS = [
        'def', 'class', 'import', 'from', 'if', 'else', 'elif', 'for', 'while',
        'return', 'break', 'continue', 'pass', 'try', 'except', 'finally',
        'with', 'as', 'lambda', 'yield', 'global', 'nonlocal', 'assert',
        'True', 'False', 'None', 'and', 'or', 'not', 'in', 'is'
    ]
    
    @classmethod
    def highlight_line(cls, line: str) -> str:
        """Aplica syntax highlighting a uma linha"""
        if not line.strip():
            return line
        
        # Salva indentação original
        indent = len(line) - len(line.lstrip())
        indent_str = line[:indent]
        line_content = line[indent:]
        
        # Comentários
        if line_content.strip().startswith('#'):
            return indent_str + cls.COLORS['comment'] + line_content + cls.COLORS['reset']
        
        # Strings (simples e duplas)
        def replace_strings(match):
            return cls.COLORS['string'] + match.group(0) + cls.COLORS['reset']
        
        line_content = re.sub(r'"[^"]*"', replace_strings, line_content)
        line_content = re.sub(r"'[^']*'", replace_strings, line_content)
        
        # Números
        def replace_numbers(match):
            return cls.COLORS['number'] + match.group(0) + cls.COLORS['reset']
        
        line_content = re.sub(r'\b\d+\.?\d*\b', replace_numbers, line_content)
        
        # Palavras-chave
        for keyword in cls.KEYWORDS:
            pattern = r'\b' + keyword + r'\b'
            replacement = cls.COLORS['keyword'] + keyword + cls.COLORS['reset']
            line_content = re.sub(pattern, replacement, line_content)
        
        # Funções (palavra seguida de '(')
        def replace_functions(match):
            return cls.COLORS['function'] + match.group(1) + cls.COLORS['reset'] + match.group(2)
        
        line_content = re.sub(r'(\w+)(\s*\()', replace_functions, line_content)
        
        return indent_str + line_content


class CodeEditor:
    """Editor de código integrado no terminal"""
    
    def __init__(self):
        self.lines: List[str] = []
        self.cursor_row: int = 0
        self.cursor_col: int = 0
        self.filename: Optional[str] = None
        self.modified: bool = False
        self.history: List[List[str]] = []
        self.history_index: int = -1
        self.clipboard: Optional[str] = None
        self.syntax_highlight: bool = True
        self.show_line_numbers: bool = True
        self.tab_size: int = 4
        self.auto_indent: bool = True
        
        # Armazena códigos executados
        self.execution_history: List[Dict[str, Any]] = []
        self.load_execution_history()
    
    def load_execution_history(self) -> None:
        """Carrega histórico de execuções"""
        history_file = "code_history.json"
        if os.path.exists(history_file):
            try:
                import json
                with open(history_file, 'r', encoding='utf-8') as f:
                    self.execution_history = json.load(f)
            except:
                self.execution_history = []
    
    def save_execution_history(self) -> None:
        """Salva histórico de execuções"""
        import json
        history_file = "code_history.json"
        
        # Mantém apenas últimas 50 execuções
        self.execution_history = self.execution_history[-50:]
        
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(self.execution_history, f, indent=2, ensure_ascii=False)
    
    def clear_screen(self) -> None:
        """Limpa a tela"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def new_file(self) -> None:
        """Cria novo arquivo"""
        if self.modified and self.lines:
            confirm = input("Descartar alterações não salvas? (s/n): ")
            if confirm.lower() != 's':
                return
        
        self.lines = [""]
        self.cursor_row = 0
        self.cursor_col = 0
        self.filename = None
        self.modified = False
        self.history = []
        self.history_index = -1
    
    def load_file(self, filename: str) -> bool:
        """Carrega arquivo"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                self.lines = content.split('\n')
                if not self.lines:
                    self.lines = [""]
            
            self.filename = filename
            self.modified = False
            self.cursor_row = 0
            self.cursor_col = 0
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar arquivo: {e}")
            return False
    
    def save_file(self, filename: Optional[str] = None) -> bool:
        """Salva arquivo"""
        if filename:
            self.filename = filename
        
        if not self.filename:
            self.filename = input("Nome do arquivo: ").strip()
            if not self.filename:
                return False
        
        try:
            content = '\n'.join(self.lines)
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.modified = False
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar: {e}")
            return False
    
    def display(self) -> None:
        """Exibe o editor"""
        self.clear_screen()
        
        # Cabeçalho
        title = f"📝 EDITOR PYTHON - {self.filename or 'Novo Arquivo'}"
        if self.modified:
            title += " *"
        
        print("=" * 80)
        print(title.center(80))
        print("=" * 80)
        
        # Área de edição
        terminal_height = 20  # Altura fixa para simplicidade
        start_line = max(0, self.cursor_row - terminal_height // 2)
        end_line = min(len(self.lines), start_line + terminal_height)
        
        for i in range(start_line, end_line):
            # Número da linha
            if self.show_line_numbers:
                line_num = f"{i + 1:4d} │ "
                print(line_num, end='')
            
            # Conteúdo da linha
            if i < len(self.lines):
                line = self.lines[i]
                
                # Syntax highlighting
                if self.syntax_highlight:
                    line = SyntaxHighlighter.highlight_line(line)
                
                # Marca a linha do cursor
                if i == self.cursor_row:
                    # Mostra cursor
                    if self.cursor_col <= len(self.lines[i]):
                        display_line = line[:self.cursor_col] + "▌" + line[self.cursor_col:]
                    else:
                        display_line = line + "▌"
                    print(display_line)
                else:
                    print(line)
            else:
                print()
        
        # Barra de status
        print("=" * 80)
        status = f"Linha {self.cursor_row + 1}, Coluna {self.cursor_col + 1}"
        if self.syntax_highlight:
            status += " | Syntax: ON"
        status += f" | Tab: {self.tab_size}"
        
        print(status)
        
        # Mini ajuda
        print("Ctrl+S: Salvar | Ctrl+R: Executar | Ctrl+Q: Sair | Ctrl+H: Ajuda")
    
    def insert_char(self, char: str) -> None:
        """Insere caractere na posição do cursor"""
        if self.cursor_row >= len(self.lines):
            self.lines.append("")
        
        line = self.lines[self.cursor_row]
        self.lines[self.cursor_row] = line[:self.cursor_col] + char + line[self.cursor_col:]
        self.cursor_col += len(char)
        self.modified = True
    
    def delete_char(self) -> None:
        """Deleta caractere antes do cursor (backspace)"""
        if self.cursor_col > 0:
            line = self.lines[self.cursor_row]
            self.lines[self.cursor_row] = line[:self.cursor_col-1] + line[self.cursor_col:]
            self.cursor_col -= 1
            self.modified = True
        elif self.cursor_row > 0:
            # Junta com linha anterior
            self.cursor_col = len(self.lines[self.cursor_row - 1])
            self.lines[self.cursor_row - 1] += self.lines[self.cursor_row]
            del self.lines[self.cursor_row]
            self.cursor_row -= 1
            self.modified = True
    
    def new_line(self) -> None:
        """Insere nova linha"""
        if self.cursor_row >= len(self.lines):
            self.lines.append("")
        
        line = self.lines[self.cursor_row]
        current_line = line[:self.cursor_col]
        next_line = line[self.cursor_col:]
        
        # Auto-indentação
        indent = ""
        if self.auto_indent:
            # Calcula indentação da linha atual
            indent_match = re.match(r'^(\s*)', current_line)
            if indent_match:
                indent = indent_match.group(1)
            
            # Se termina com ':', adiciona indentação extra
            if current_line.rstrip().endswith(':'):
                indent += " " * self.tab_size
        
        self.lines[self.cursor_row] = current_line
        self.lines.insert(self.cursor_row + 1, indent + next_line)
        self.cursor_row += 1
        self.cursor_col = len(indent)
        self.modified = True
    
    def move_cursor(self, direction: str) -> None:
        """Move o cursor"""
        if direction == "up" and self.cursor_row > 0:
            self.cursor_row -= 1
            self.cursor_col = min(self.cursor_col, len(self.lines[self.cursor_row]))
        elif direction == "down" and self.cursor_row < len(self.lines) - 1:
            self.cursor_row += 1
            self.cursor_col = min(self.cursor_col, len(self.lines[self.cursor_row]))
        elif direction == "left" and self.cursor_col > 0:
            self.cursor_col -= 1
        elif direction == "right":
            if self.cursor_row < len(self.lines):
                if self.cursor_col < len(self.lines[self.cursor_row]):
                    self.cursor_col += 1
        elif direction == "home":
            self.cursor_col = 0
        elif direction == "end":
            if self.cursor_row < len(self.lines):
                self.cursor_col = len(self.lines[self.cursor_row])
    
    def execute_code(self) -> None:
        """Executa o código atual"""
        code = '\n'.join(self.lines)
        
        # Salva no histórico
        self.execution_history.append({
            "code": code,
            "timestamp": datetime.now().isoformat(),
            "filename": self.filename
        })
        self.save_execution_history()
        
        print("\n" + "="*80)
        print("▶️  EXECUTANDO CÓDIGO...")
        print("="*80)
        
        # Namespace para execução
        namespace = {}
        
        try:
            exec(code, namespace)
            print("\n✅ Código executado com sucesso!")
        except Exception as e:
            print(f"\n❌ Erro: {type(e).__name__}: {e}")
            
            # Destaca linha do erro se possível
            import traceback
            tb = traceback.extract_tb(e.__traceback__)
            for frame in tb:
                if frame.filename == "<string>":
                    print(f"   → Erro na linha {frame.lineno}")
                    if 0 < frame.lineno <= len(self.lines):
                        print(f"   → {self.lines[frame.lineno-1].strip()}")
        
        print("="*80)
        input("\nPressione ENTER para continuar...")
    
    def show_help(self) -> None:
        """Mostra ajuda do editor"""
        self.clear_screen()
        print("=" * 80)
        print("📝 AJUDA DO EDITOR".center(80))
        print("=" * 80)
        print("""
COMANDOS BÁSICOS:
  Ctrl+S    - Salvar arquivo
  Ctrl+O    - Abrir arquivo
  Ctrl+N    - Novo arquivo
  Ctrl+R    - Executar código
  Ctrl+Q    - Sair do editor

NAVEGAÇÃO:
  Setas     - Mover cursor
  Home      - Início da linha
  End       - Fim da linha
  Page Up   - Página acima
  Page Down - Página abaixo

EDIÇÃO:
  Tab       - Inserir tabulação
  Enter     - Nova linha (com auto-indentação)
  Backspace - Apagar caractere
  Ctrl+Z    - Desfazer
  Ctrl+Y    - Refazer
  Ctrl+L    - Limpar linha

RECURSOS:
  Ctrl+H    - Mostrar/ocultar esta ajuda
  Ctrl+T    - Alternar syntax highlighting
  Ctrl+M    - Alternar números de linha
  
DICAS:
  • O editor salva automaticamente o histórico de execuções
  • Use Tab para auto-indentar após ':' 
  • Syntax highlighting destaca palavras-chave Python
""")
        input("\nPressione ENTER para voltar ao editor...")
    
    def run_editor(self) -> Optional[str]:
        """Loop principal do editor - retorna código editado"""
        self.new_file()
        
        # Modo simplificado para terminal
        print("\n📝 EDITOR PYTHON SIMPLIFICADO")
        print("Digite seu código (digite 'FIM' em uma linha vazia para terminar):")
        print("Comandos: EXECUTAR, SALVAR, CARREGAR, LIMPAR, SAIR\n")
        
        while True:
            # Mostra código atual com números de linha
            if self.lines and any(line.strip() for line in self.lines):
                print("\n--- CÓDIGO ATUAL ---")
                for i, line in enumerate(self.lines, 1):
                    highlighted = SyntaxHighlighter.highlight_line(line) if self.syntax_highlight else line
                    print(f"{i:3d} | {highlighted}")
                print("-------------------\n")
            
            # Input
            try:
                entrada = input(f"{len(self.lines)+1:3d} | ")
            except KeyboardInterrupt:
                print("\n⚠️ Use 'SAIR' para sair do editor")
                continue
            
            # Comandos especiais
            comando_upper = entrada.upper().strip()
            
            if comando_upper == "FIM":
                return '\n'.join(self.lines)
            
            elif comando_upper == "EXECUTAR":
                self.execute_code()
            
            elif comando_upper == "SALVAR":
                filename = input("Nome do arquivo (.py): ").strip()
                if not filename.endswith('.py'):
                    filename += '.py'
                if self.save_file(filename):
                    print(f"✅ Salvo como {filename}")
                else:
                    print("❌ Erro ao salvar")
            
            elif comando_upper == "CARREGAR":
                filename = input("Nome do arquivo: ").strip()
                if self.load_file(filename):
                    print(f"✅ Arquivo {filename} carregado")
                else:
                    print("❌ Erro ao carregar")
            
            elif comando_upper == "LIMPAR":
                self.lines = []
                print("✅ Editor limpo")
            
            elif comando_upper == "SAIR":
                if self.modified:
                    confirm = input("Há alterações não salvas. Sair mesmo assim? (s/n): ")
                    if confirm.lower() != 's':
                        continue
                return None
            
            elif comando_upper.startswith("DELETAR "):
                try:
                    linha_num = int(comando_upper.split()[1]) - 1
                    if 0 <= linha_num < len(self.lines):
                        del self.lines[linha_num]
                        print(f"✅ Linha {linha_num + 1} deletada")
                    else:
                        print("❌ Linha inválida")
                except (ValueError, IndexError):
                    print("❌ Use: DELETAR <número da linha>")
            
            elif comando_upper == "HISTORICO":
                if self.execution_history:
                    print("\n--- HISTÓRICO DE EXECUÇÕES ---")
                    for i, h in enumerate(self.execution_history[-5:], 1):
                        timestamp = datetime.fromisoformat(h['timestamp']).strftime("%H:%M:%S")
                        print(f"{i}. {timestamp} - {h.get('filename', 'Sem nome')}")
                    
                    try:
                        escolha = int(input("Carregar qual? (0 para cancelar): "))
                        if 1 <= escolha <= min(5, len(self.execution_history)):
                            hist = self.execution_history[-(6-escolha)]
                            self.lines = hist['code'].split('\n')
                            print("✅ Código carregado do histórico")
                    except ValueError:
                        pass
                else:
                    print("📭 Histórico vazio")
            
            elif comando_upper == "AJUDA":
                print("""
COMANDOS DO EDITOR:
  FIM       - Finalizar edição e retornar código
  EXECUTAR  - Executar o código atual
  SALVAR    - Salvar em arquivo
  CARREGAR  - Carregar de arquivo
  LIMPAR    - Limpar editor
  DELETAR n - Deletar linha n
  HISTORICO - Ver/carregar histórico
  SAIR      - Sair sem salvar
  
DICAS:
  • Digite normalmente para adicionar linhas
  • Use espaços para indentação
  • O editor destaca sintaxe Python automaticamente
""")
            
            else:
                # Adiciona linha normal
                self.lines.append(entrada)
                self.modified = True


class CodePlayground:
    """Ambiente de experimentação de código"""
    
    def __init__(self):
        self.editor = CodeEditor()
        self.snippets = self._load_snippets()
    
    def _load_snippets(self) -> Dict[str, str]:
        """Carrega snippets de exemplo"""
        return {
            "hello": "print('Olá, Mundo!')",
            "variavel": "nome = 'Python'\nidade = 30\nprint(f'Linguagem: {nome}, Anos: {idade}')",
            "if": "idade = 18\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')",
            "for": "for i in range(5):\n    print(f'Número: {i}')",
            "while": "contador = 0\nwhile contador < 5:\n    print(contador)\n    contador += 1",
            "lista": "frutas = ['maçã', 'banana', 'laranja']\nfor fruta in frutas:\n    print(f'Fruta: {fruta}')",
            "funcao": "def saudar(nome):\n    return f'Olá, {nome}!'\n\nprint(saudar('Python'))",
            "input": "nome = input('Qual seu nome? ')\nprint(f'Prazer, {nome}!')"
        }
    
    def start_playground(self, ui_components) -> None:
        """Inicia o playground de código"""
        ui_components.header("PLAYGROUND DE CÓDIGO", "Experimente Python!", "🎮")
        
        print("\n🎯 OPÇÕES:")
        print("1. 📝 Editor Livre")
        print("2. 📚 Carregar Exemplo")
        print("3. 📂 Abrir Arquivo")
        print("4. 🕐 Histórico Recente")
        print("0. 🔙 Voltar")
        
        escolha = input("\n👉 Escolha: ").strip()
        
        if escolha == "1":
            codigo = self.editor.run_editor()
            if codigo:
                self._salvar_na_sessao(codigo)
        
        elif escolha == "2":
            self._carregar_exemplo()
        
        elif escolha == "3":
            filename = input("Nome do arquivo: ").strip()
            if self.editor.load_file(filename):
                codigo = self.editor.run_editor()
                if codigo:
                    self._salvar_na_sessao(codigo)
        
        elif escolha == "4":
            self._mostrar_historico()
    
    def _carregar_exemplo(self) -> None:
        """Carrega exemplo pré-definido"""
        print("\n📚 EXEMPLOS DISPONÍVEIS:")
        for i, (nome, _) in enumerate(self.snippets.items(), 1):
            print(f"{i}. {nome}")
        
        try:
            escolha = int(input("\n👉 Escolha o exemplo: ")) - 1
            nome_exemplo = list(self.snippets.keys())[escolha]
            codigo = self.snippets[nome_exemplo]
            
            self.editor.lines = codigo.split('\n')
            print(f"\n✅ Exemplo '{nome_exemplo}' carregado!")
            
            codigo_editado = self.editor.run_editor()
            if codigo_editado:
                self._salvar_na_sessao(codigo_editado)
                
        except (ValueError, IndexError):
            print("❌ Opção inválida")
    
    def _salvar_na_sessao(self, codigo: str) -> None:
        """Salva código da sessão atual"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"playground_{timestamp}.py"
        
        resposta = input(f"\n💾 Salvar como {filename}? (s/n): ")
        if resposta.lower() == 's':
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(codigo)
                print(f"✅ Salvo como {filename}")
            except Exception as e:
                print(f"❌ Erro ao salvar: {e}")
    
    def _mostrar_historico(self) -> None:
        """Mostra histórico de códigos executados"""
        if self.editor.execution_history:
            print("\n🕐 HISTÓRICO RECENTE:")
            for i, hist in enumerate(self.editor.execution_history[-10:], 1):
                timestamp = datetime.fromisoformat(hist['timestamp'])
                print(f"\n{i}. {timestamp.strftime('%d/%m %H:%M')} - {hist.get('filename', 'Sem nome')}")
                # Mostra primeiras 3 linhas
                linhas = hist['code'].split('\n')[:3]
                for linha in linhas:
                    print(f"   {linha}")
                if len(hist['code'].split('\n')) > 3:
                    print("   ...")
        else:
            print("\n📭 Histórico vazio")