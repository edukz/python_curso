#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o sistema de rastreamento de erros
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from error_tracker import ErrorTracker


class TestErrorTracker(unittest.TestCase):
    """Testes para ErrorTracker"""
    
    def setUp(self):
        self.tracker = ErrorTracker()
    
    def test_module_tracking(self):
        """Testa rastreamento por módulo"""
        # Inicia módulo
        self.tracker.start_module("modulo_1")
        self.assertEqual(self.tracker.current_module, "modulo_1")
        
        # Adiciona erro
        try:
            raise ValueError("Test error")
        except ValueError as e:
            self.tracker.track_error(e, "test context")
        
        # Finaliza módulo
        stats = self.tracker.end_module("modulo_1")
        self.assertFalse(stats["sem_erros"])
        self.assertEqual(stats["total_erros"], 1)
        
        # Módulo sem erros
        self.tracker.start_module("modulo_2")
        stats = self.tracker.end_module("modulo_2")
        self.assertTrue(stats["sem_erros"])
        self.assertEqual(stats["total_erros"], 0)
    
    def test_error_tracking(self):
        """Testa registro de erros"""
        # Registra erro simples
        try:
            raise RuntimeError("Test runtime error")
        except RuntimeError as e:
            self.tracker.track_error(e, "runtime test", "high")
        
        self.assertEqual(self.tracker.error_count, 1)
        self.assertEqual(len(self.tracker.session_errors), 1)
        
        # Verifica detalhes do erro
        error = self.tracker.session_errors[0]
        self.assertEqual(error["type"], "RuntimeError")
        self.assertEqual(error["message"], "Test runtime error")
        self.assertEqual(error["context"], "runtime test")
        self.assertEqual(error["severity"], "high")
    
    def test_exercise_error_tracking(self):
        """Testa registro de erros em exercícios"""
        self.tracker.start_module("modulo_3")
        self.tracker.track_exercise_error(
            "ex_001",
            "print('Hello')",
            "print('Hello World')"
        )
        
        stats = self.tracker.end_module("modulo_3")
        self.assertFalse(stats["sem_erros"])
        self.assertEqual(stats["total_erros"], 1)
        
        # Verifica detalhes
        error = stats["erros"][0]
        self.assertEqual(error["type"], "ExerciseError")
        self.assertEqual(error["details"]["exercise_id"], "ex_001")
    
    def test_session_summary(self):
        """Testa resumo da sessão"""
        # Adiciona vários erros com diferentes severidades
        severities = ["low", "medium", "high", "critical"]
        
        for i, severity in enumerate(severities):
            try:
                raise Exception(f"Error {i}")
            except Exception as e:
                self.tracker.track_error(e, f"context {i}", severity)
        
        summary = self.tracker.get_session_summary()
        
        self.assertEqual(summary["total_errors"], 4)
        self.assertEqual(summary["errors_by_severity"]["low"], 1)
        self.assertEqual(summary["errors_by_severity"]["medium"], 1)
        self.assertEqual(summary["errors_by_severity"]["high"], 1)
        self.assertEqual(summary["errors_by_severity"]["critical"], 1)
    
    def test_critical_errors_detection(self):
        """Testa detecção de erros críticos"""
        # Sem erros críticos
        self.assertFalse(self.tracker.has_critical_errors())
        
        # Com erro crítico
        try:
            raise Exception("Critical error")
        except Exception as e:
            self.tracker.track_error(e, "critical context", "critical")
        
        self.assertTrue(self.tracker.has_critical_errors())
    
    def test_clear_module_errors(self):
        """Testa limpeza de erros de módulo"""
        self.tracker.start_module("modulo_4")
        
        # Adiciona erro
        try:
            raise ValueError("Error to clear")
        except ValueError as e:
            self.tracker.track_error(e)
        
        # Verifica que tem erro
        stats = self.tracker.end_module("modulo_4")
        self.assertEqual(stats["total_erros"], 1)
        
        # Limpa erros
        self.tracker.clear_module_errors("modulo_4")
        
        # Verifica que foi limpo
        stats = self.tracker.end_module("modulo_4")
        self.assertEqual(stats["total_erros"], 0)
    
    def test_error_report(self):
        """Testa geração de relatório"""
        # Sem erros
        report = self.tracker.get_error_report()
        self.assertIn("Nenhum erro registrado", report)
        
        # Com erros
        self.tracker.start_module("modulo_5")
        try:
            raise Exception("Report test error")
        except Exception as e:
            self.tracker.track_error(e, severity="medium")
        
        report = self.tracker.get_error_report()
        self.assertIn("RELATÓRIO DE ERROS", report)
        self.assertIn("Total de erros: 1", report)
        self.assertIn("MEDIUM: 1", report)


if __name__ == '__main__':
    unittest.main()