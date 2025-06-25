#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Validação e Sanitização de Inputs
Garante segurança e integridade dos dados de entrada
"""

import re
import os
from typing import Any, Optional, Union, List, Tuple
from pathlib import Path


class InputValidator:
    """Classe para validação e sanitização de inputs do usuário"""
    
    # Padrões para validação
    UNSAFE_CHARS = r'[<>:"/\\|?*\x00-\x1f]'
    SQL_INJECTION_PATTERNS = [
        r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|CREATE|ALTER)\b)",
        r"(--|\||;|\/\*|\*\/|xp_|sp_)",
        r"('|(\')|\"|(\")|(\-\-)|(\;)|(\|)|(\*))"
    ]
    XSS_PATTERNS = [
        r"<script[^>]*>.*?</script>",
        r"javascript:",
        r"on\w+\s*=",
        r"<iframe",
        r"<object",
        r"<embed"
    ]
    
    @staticmethod
    def sanitize_string(value: str, max_length: int = 1000) -> str:
        """
        Sanitiza uma string removendo caracteres perigosos
        
        Args:
            value: String a ser sanitizada
            max_length: Tamanho máximo permitido
            
        Returns:
            String sanitizada
        """
        if not isinstance(value, str):
            raise TypeError(f"Expected string, got {type(value)}")
        
        # Limita o tamanho
        value = value[:max_length]
        
        # Remove caracteres nulos e de controle
        value = ''.join(char for char in value if ord(char) >= 32 or char in '\n\r\t')
        
        # Remove espaços extras
        value = ' '.join(value.split())
        
        return value
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """
        Sanitiza um nome de arquivo
        
        Args:
            filename: Nome do arquivo
            
        Returns:
            Nome de arquivo seguro
        """
        # Remove caracteres inseguros
        filename = re.sub(InputValidator.UNSAFE_CHARS, '', filename)
        
        # Remove . e .. path traversal
        filename = filename.replace('..', '')
        
        # Limita tamanho
        name, ext = os.path.splitext(filename)
        name = name[:200]
        ext = ext[:10]
        
        filename = name + ext
        
        # Não permite nomes vazios
        if not filename or filename.isspace():
            filename = "unnamed_file"
        
        return filename
    
    @staticmethod
    def validate_path(path: str, base_dir: Optional[str] = None) -> Tuple[bool, str]:
        """
        Valida se um caminho é seguro
        
        Args:
            path: Caminho a validar
            base_dir: Diretório base permitido
            
        Returns:
            Tupla (é_válido, mensagem)
        """
        try:
            path_obj = Path(path).resolve()
            
            # Verifica path traversal
            if '..' in str(path):
                return False, "Path traversal detectado"
            
            # Se base_dir fornecido, verifica se está dentro dele
            if base_dir:
                base_path = Path(base_dir).resolve()
                if not str(path_obj).startswith(str(base_path)):
                    return False, "Path fora do diretório permitido"
            
            return True, "Path válido"
            
        except Exception as e:
            return False, f"Path inválido: {str(e)}"
    
    @staticmethod
    def validate_integer(value: Any, min_val: Optional[int] = None, 
                        max_val: Optional[int] = None) -> Tuple[bool, Union[int, str]]:
        """
        Valida um valor inteiro
        
        Args:
            value: Valor a validar
            min_val: Valor mínimo permitido
            max_val: Valor máximo permitido
            
        Returns:
            Tupla (é_válido, valor_ou_mensagem)
        """
        try:
            int_value = int(value)
            
            if min_val is not None and int_value < min_val:
                return False, f"Valor deve ser >= {min_val}"
            
            if max_val is not None and int_value > max_val:
                return False, f"Valor deve ser <= {max_val}"
            
            return True, int_value
            
        except (ValueError, TypeError):
            return False, "Valor deve ser um número inteiro"
    
    @staticmethod
    def validate_choice(value: str, valid_choices: List[str], 
                       case_sensitive: bool = False) -> Tuple[bool, str]:
        """
        Valida se valor está em lista de escolhas válidas
        
        Args:
            value: Valor a validar
            valid_choices: Lista de valores permitidos
            case_sensitive: Se comparação é case sensitive
            
        Returns:
            Tupla (é_válido, mensagem)
        """
        if not case_sensitive:
            value = value.lower()
            valid_choices = [c.lower() for c in valid_choices]
        
        if value in valid_choices:
            return True, "Escolha válida"
        
        return False, f"Escolha inválida. Opções: {', '.join(valid_choices)}"
    
    @staticmethod
    def detect_sql_injection(value: str) -> bool:
        """
        Detecta possível SQL injection
        
        Args:
            value: String a verificar
            
        Returns:
            True se detectado padrão suspeito
        """
        value_upper = value.upper()
        
        for pattern in InputValidator.SQL_INJECTION_PATTERNS:
            if re.search(pattern, value_upper, re.IGNORECASE):
                return True
        
        return False
    
    @staticmethod
    def detect_xss(value: str) -> bool:
        """
        Detecta possível XSS
        
        Args:
            value: String a verificar
            
        Returns:
            True se detectado padrão suspeito
        """
        for pattern in InputValidator.XSS_PATTERNS:
            if re.search(pattern, value, re.IGNORECASE):
                return True
        
        return False
    
    @staticmethod
    def validate_user_input(value: str, input_type: str = "text", 
                           **kwargs) -> Tuple[bool, Union[Any, str]]:
        """
        Valida input do usuário baseado no tipo
        
        Args:
            value: Valor a validar
            input_type: Tipo de input (text, number, choice, filename, path)
            **kwargs: Argumentos específicos por tipo
            
        Returns:
            Tupla (é_válido, valor_processado_ou_mensagem_erro)
        """
        # Remove espaços nas extremidades
        value = value.strip()
        
        # Verifica ataques comuns
        if InputValidator.detect_sql_injection(value):
            return False, "Input contém padrões suspeitos"
        
        if InputValidator.detect_xss(value):
            return False, "Input contém código potencialmente malicioso"
        
        # Validação específica por tipo
        if input_type == "text":
            max_length = kwargs.get("max_length", 1000)
            sanitized = InputValidator.sanitize_string(value, max_length)
            return True, sanitized
        
        elif input_type == "number":
            return InputValidator.validate_integer(
                value, 
                kwargs.get("min_val"),
                kwargs.get("max_val")
            )
        
        elif input_type == "choice":
            choices = kwargs.get("choices", [])
            case_sensitive = kwargs.get("case_sensitive", False)
            return InputValidator.validate_choice(value, choices, case_sensitive)
        
        elif input_type == "filename":
            sanitized = InputValidator.sanitize_filename(value)
            return True, sanitized
        
        elif input_type == "path":
            base_dir = kwargs.get("base_dir")
            return InputValidator.validate_path(value, base_dir)
        
        else:
            return False, f"Tipo de input desconhecido: {input_type}"


class SecureInput:
    """Classe para entrada segura de dados do usuário"""
    
    def __init__(self, validator: Optional[InputValidator] = None):
        self.validator = validator or InputValidator()
    
    def get_input(self, prompt: str, input_type: str = "text", 
                  required: bool = True, **kwargs) -> Optional[Any]:
        """
        Obtém input seguro do usuário
        
        Args:
            prompt: Mensagem para o usuário
            input_type: Tipo de input esperado
            required: Se input é obrigatório
            **kwargs: Argumentos para validação
            
        Returns:
            Valor validado ou None
        """
        max_attempts = kwargs.get("max_attempts", 3)
        attempts = 0
        
        while attempts < max_attempts:
            try:
                value = input(prompt).strip()
                
                # Verifica se vazio e obrigatório
                if not value and required:
                    print("❌ Este campo é obrigatório.")
                    attempts += 1
                    continue
                
                # Se vazio e não obrigatório, retorna None
                if not value and not required:
                    return None
                
                # Valida input
                is_valid, result = self.validator.validate_user_input(
                    value, input_type, **kwargs
                )
                
                if is_valid:
                    return result
                else:
                    print(f"❌ {result}")
                    attempts += 1
                    
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"❌ Erro ao processar input: {e}")
                attempts += 1
        
        print(f"❌ Número máximo de tentativas ({max_attempts}) excedido.")
        return None
    
    def get_choice(self, prompt: str, choices: List[str], 
                   case_sensitive: bool = False) -> Optional[str]:
        """Obtém escolha segura do usuário"""
        return self.get_input(
            prompt,
            input_type="choice",
            choices=choices,
            case_sensitive=case_sensitive
        )
    
    def get_number(self, prompt: str, min_val: Optional[int] = None,
                   max_val: Optional[int] = None) -> Optional[int]:
        """Obtém número seguro do usuário"""
        return self.get_input(
            prompt,
            input_type="number",
            min_val=min_val,
            max_val=max_val
        )
    
    def get_filename(self, prompt: str) -> Optional[str]:
        """Obtém nome de arquivo seguro do usuário"""
        return self.get_input(prompt, input_type="filename")
    
    def get_path(self, prompt: str, base_dir: Optional[str] = None) -> Optional[str]:
        """Obtém caminho seguro do usuário"""
        return self.get_input(
            prompt,
            input_type="path",
            base_dir=base_dir
        )