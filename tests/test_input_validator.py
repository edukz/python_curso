#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o sistema de validação de inputs
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from security.input_validator import InputValidator, SecureInput


class TestInputValidator(unittest.TestCase):
    """Testes para InputValidator"""
    
    def setUp(self):
        self.validator = InputValidator()
    
    def test_sanitize_string(self):
        """Testa sanitização de strings"""
        # Testa remoção de caracteres de controle
        self.assertEqual(
            self.validator.sanitize_string("Hello\x00World\x1f"),
            "HelloWorld"
        )
        
        # Testa limite de tamanho
        long_string = "a" * 2000
        self.assertEqual(
            len(self.validator.sanitize_string(long_string, max_length=100)),
            100
        )
        
        # Testa remoção de espaços extras
        self.assertEqual(
            self.validator.sanitize_string("Hello   World   "),
            "Hello World"
        )
    
    def test_sanitize_filename(self):
        """Testa sanitização de nomes de arquivo"""
        # Remove caracteres inseguros
        self.assertEqual(
            self.validator.sanitize_filename("file<>name.txt"),
            "filename.txt"
        )
        
        # Remove path traversal
        self.assertEqual(
            self.validator.sanitize_filename("../../../etc/passwd"),
            "etcpasswd"
        )
        
        # Nome vazio retorna padrão
        self.assertEqual(
            self.validator.sanitize_filename(""),
            "unnamed_file"
        )
    
    def test_validate_path(self):
        """Testa validação de caminhos"""
        # Path traversal deve falhar
        valid, msg = self.validator.validate_path("../../../etc/passwd")
        self.assertFalse(valid)
        self.assertIn("Path traversal", msg)
        
        # Path válido
        valid, msg = self.validator.validate_path("/tmp/test.txt")
        self.assertTrue(valid)
    
    def test_validate_integer(self):
        """Testa validação de inteiros"""
        # Valor válido
        valid, value = self.validator.validate_integer("42")
        self.assertTrue(valid)
        self.assertEqual(value, 42)
        
        # Valor inválido
        valid, msg = self.validator.validate_integer("abc")
        self.assertFalse(valid)
        self.assertIn("número inteiro", msg)
        
        # Teste com limites
        valid, msg = self.validator.validate_integer("5", min_val=1, max_val=10)
        self.assertTrue(valid)
        
        valid, msg = self.validator.validate_integer("15", min_val=1, max_val=10)
        self.assertFalse(valid)
        self.assertIn("<= 10", msg)
    
    def test_validate_choice(self):
        """Testa validação de escolhas"""
        choices = ["A", "B", "C"]
        
        # Escolha válida
        valid, msg = self.validator.validate_choice("B", choices)
        self.assertTrue(valid)
        
        # Escolha inválida
        valid, msg = self.validator.validate_choice("D", choices)
        self.assertFalse(valid)
        
        # Case insensitive
        valid, msg = self.validator.validate_choice("a", choices, case_sensitive=False)
        self.assertTrue(valid)
    
    def test_detect_sql_injection(self):
        """Testa detecção de SQL injection"""
        # Padrões suspeitos
        self.assertTrue(self.validator.detect_sql_injection("'; DROP TABLE users;--"))
        self.assertTrue(self.validator.detect_sql_injection("1' OR '1'='1"))
        self.assertTrue(self.validator.detect_sql_injection("UNION SELECT * FROM"))
        
        # Input normal
        self.assertFalse(self.validator.detect_sql_injection("John Doe"))
        self.assertFalse(self.validator.detect_sql_injection("user@example.com"))
    
    def test_detect_xss(self):
        """Testa detecção de XSS"""
        # Padrões XSS
        self.assertTrue(self.validator.detect_xss("<script>alert('XSS')</script>"))
        self.assertTrue(self.validator.detect_xss("javascript:alert(1)"))
        self.assertTrue(self.validator.detect_xss("<img onerror='alert(1)'>"))
        
        # Input normal
        self.assertFalse(self.validator.detect_xss("Hello World"))
        self.assertFalse(self.validator.detect_xss("<b>Bold text</b>"))
    
    def test_validate_user_input(self):
        """Testa validação completa de input do usuário"""
        # Texto normal
        valid, value = self.validator.validate_user_input("Hello World", "text")
        self.assertTrue(valid)
        self.assertEqual(value, "Hello World")
        
        # Número
        valid, value = self.validator.validate_user_input("42", "number", min_val=0, max_val=100)
        self.assertTrue(valid)
        self.assertEqual(value, 42)
        
        # SQL injection deve falhar
        valid, msg = self.validator.validate_user_input("'; DROP TABLE;", "text")
        self.assertFalse(valid)
        self.assertIn("suspeitos", msg)


class TestSecureInput(unittest.TestCase):
    """Testes para SecureInput"""
    
    def setUp(self):
        self.secure_input = SecureInput()
    
    def test_initialization(self):
        """Testa inicialização"""
        self.assertIsNotNone(self.secure_input.validator)
        self.assertIsInstance(self.secure_input.validator, InputValidator)


if __name__ == '__main__':
    unittest.main()