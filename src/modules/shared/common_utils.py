#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utilitários Comuns para Módulos
Funções auxiliares compartilhadas entre módulos
"""

import os
import re
from typing import List, Dict, Any, Optional


class ModuleUtils:
    """Utilitários comuns para todos os módulos"""
    
    @staticmethod
    def clean_code_example(code: str) -> str:
        """
        Limpa e formata exemplos de código
        
        Args:
            code: Código para limpar
            
        Returns:
            Código formatado
        """
        # Remove espaços em branco desnecessários
        lines = code.strip().split('\n')
        
        # Remove linhas vazias no início e fim
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        
        # Normaliza indentação
        if lines:
            # Encontra a menor indentação não-zero
            min_indent = float('inf')
            for line in lines:
                if line.strip():  # Ignora linhas vazias
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)
            
            # Remove indentação comum
            if min_indent != float('inf') and min_indent > 0:
                lines = [line[min_indent:] if line.strip() else line for line in lines]
        
        return '\n'.join(lines)
    
    @staticmethod
    def validate_python_syntax(code: str) -> tuple[bool, Optional[str]]:
        """
        Valida sintaxe Python
        
        Args:
            code: Código para validar
            
        Returns:
            Tupla (is_valid, error_message)
        """
        try:
            compile(code, '<string>', 'exec')
            return True, None
        except SyntaxError as e:
            return False, f"Erro de sintaxe na linha {e.lineno}: {e.msg}"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    @staticmethod
    def format_exercise_description(description: str) -> str:
        """
        Formata descrição de exercício
        
        Args:
            description: Descrição do exercício
            
        Returns:
            Descrição formatada
        """
        # Adiciona quebras de linha se necessário
        if len(description) > 80:
            words = description.split()
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                if current_length + len(word) + 1 <= 80:
                    current_line.append(word)
                    current_length += len(word) + 1
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
                    current_length = len(word)
            
            if current_line:
                lines.append(' '.join(current_line))
            
            return '\n'.join(lines)
        
        return description
    
    @staticmethod
    def extract_module_info(module_text: str) -> Dict[str, Any]:
        """
        Extrai informações do módulo do texto
        
        Args:
            module_text: Texto do módulo
            
        Returns:
            Dicionário com informações extraídas
        """
        info = {
            'title': '',
            'description': '',
            'sections': [],
            'exercises': 0,
            'examples': 0
        }
        
        # Extrai título
        title_match = re.search(r'MÓDULO \d+[:\-]\s*(.+)', module_text, re.IGNORECASE)
        if title_match:
            info['title'] = title_match.group(1).strip()
        
        # Conta exemplos de código
        info['examples'] = len(re.findall(r'📝 EXEMPLO:', module_text))
        
        # Conta exercícios
        info['exercises'] = len(re.findall(r'🎯 EXERCÍCIO:', module_text))
        
        # Extrai seções
        sections = re.findall(r'def (_\w+)\(self\)', module_text)
        info['sections'] = [section.replace('_', ' ').title() for section in sections]
        
        return info
    
    @staticmethod
    def create_module_template(module_id: str, module_name: str, sections: List[str]) -> str:
        """
        Cria template para novo módulo
        
        Args:
            module_id: ID do módulo
            module_name: Nome do módulo
            sections: Lista de seções
            
        Returns:
            Template do módulo
        """
        template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
{module_name}
{module_id.replace('_', ' ').title()}
"""

from ..shared.base_module import BaseModule


class {module_id.replace('_', ' ').title().replace(' ', '')}(BaseModule):
    """Classe para {module_name}"""
    
    def __init__(self):
        super().__init__("{module_id}", "{module_name}")
        self.has_mini_project = True  # Ajustar conforme necessário
    
    def execute(self) -> None:
        """Executa o módulo principal"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            while True:
                self._show_menu()
                escolha = input("\\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
'''
        
        # Adiciona opções do menu
        for i, section in enumerate(sections, 1):
            template += f'''                elif escolha == "{i}":
                    self._{section.lower().replace(' ', '_')}()
'''
        
        template += '''                else:
                    if self.ui:
                        self.ui.warning("❌ Opção inválida! Tente novamente.")
                    else:
                        print("❌ Opção inválida! Tente novamente.")
        
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _show_menu(self) -> None:
        """Exibe o menu do módulo"""
        options = {
'''
        
        # Adiciona opções do menu
        for i, section in enumerate(sections, 1):
            template += f'            "{i}": "📖 {section}",\n'
        
        template += '''            "0": "🔙 Voltar ao Menu Principal"
        }
        
        self.show_menu(options, f"📚 {self.module_name.upper()}")
'''
        
        # Adiciona métodos das seções
        for section in sections:
            method_name = section.lower().replace(' ', '_')
            template += f'''
    def _{method_name}(self) -> None:
        """Implementa seção: {section}"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📖 {section.upper()}")
        
        print("🚧 Seção em desenvolvimento...")
        print("📚 Conteúdo será implementado em breve!")
        
        self.pausar()
'''
        
        return template
    
    @staticmethod
    def generate_import_statements(module_count: int, directory: str) -> str:
        """
        Gera statements de import para módulos
        
        Args:
            module_count: Número de módulos
            directory: Diretório dos módulos
            
        Returns:
            String com imports
        """
        imports = []
        for i in range(1, module_count + 1):
            module_name = f"modulo_{i:02d}"
            class_name = f"Modulo{i:02d}"
            imports.append(f"from .{directory}.{module_name} import {class_name}")
        
        return '\n'.join(imports)
    
    @staticmethod
    def calculate_complexity_score(code: str) -> int:
        """
        Calcula pontuação de complexidade do código
        
        Args:
            code: Código para analisar
            
        Returns:
            Pontuação de complexidade (0-100)
        """
        score = 0
        lines = code.split('\n')
        
        # Pontos por características
        score += len(lines) * 0.1  # Linhas de código
        score += len(re.findall(r'def \w+', code)) * 5  # Funções
        score += len(re.findall(r'class \w+', code)) * 10  # Classes
        score += len(re.findall(r'if |elif |else:', code)) * 2  # Condicionais
        score += len(re.findall(r'for |while ', code)) * 3  # Loops
        score += len(re.findall(r'try:|except:', code)) * 4  # Exception handling
        score += len(re.findall(r'import |from .+ import', code)) * 1  # Imports
        
        return min(int(score), 100)  # Cap at 100