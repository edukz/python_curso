#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o Sistema de Gerenciamento de Progresso
"""

import unittest
import os
import json
import tempfile
from datetime import datetime
import sys

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.progress_manager import ProgressManager


class TestProgressManager(unittest.TestCase):
    """Testes para a classe ProgressManager"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        # Cria arquivo temporário para testes
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.progress_manager = ProgressManager(self.temp_file.name)
    
    def tearDown(self):
        """Limpeza após cada teste"""
        # Remove arquivo temporário
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_create_default_progress(self):
        """Testa criação de progresso padrão"""
        progress = self.progress_manager._create_default_progress()
        
        self.assertIn('user_name', progress)
        self.assertIn('start_date', progress)
        self.assertIn('modules_completed', progress)
        self.assertIn('modules_progress', progress)
        self.assertEqual(len(progress['modules_progress']), 11)
        self.assertEqual(progress['total_score'], 0)
    
    def test_save_and_load_progress(self):
        """Testa salvamento e carregamento de progresso"""
        self.progress_manager.set_user_name("João Silva")
        self.progress_manager.save_progress()
        
        # Carrega novamente
        new_manager = ProgressManager(self.temp_file.name)
        self.assertEqual(new_manager.progress_data['user_name'], "João Silva")
    
    def test_mark_module_completed(self):
        """Testa marcação de módulo como completo"""
        module_id = "modulo_1"
        score = 80
        
        self.progress_manager.mark_module_completed(module_id, score)
        
        self.assertIn(module_id, self.progress_manager.progress_data['modules_completed'])
        self.assertTrue(self.progress_manager.progress_data['modules_progress'][module_id]['completed'])
        self.assertEqual(self.progress_manager.progress_data['modules_progress'][module_id]['score'], score)
        self.assertEqual(self.progress_manager.progress_data['total_score'], score)
    
    def test_update_module_progress(self):
        """Testa atualização de progresso do módulo"""
        module_id = "modulo_2"
        time_spent = 300  # 5 minutos
        attempts = 3
        
        self.progress_manager.update_module_progress(module_id, time_spent, attempts)
        
        module = self.progress_manager.progress_data['modules_progress'][module_id]
        self.assertEqual(module['time_spent'], time_spent)
        self.assertEqual(module['attempts'], attempts)
        self.assertIsNotNone(module['last_access'])
    
    def test_completion_percentage(self):
        """Testa cálculo de porcentagem de conclusão"""
        # Inicialmente 0%
        self.assertEqual(self.progress_manager.get_completion_percentage(), 0)
        
        # Completa 3 módulos
        for i in range(1, 4):
            self.progress_manager.mark_module_completed(f"modulo_{i}", 100)
        
        # Deve ser aproximadamente 27.27% (3/11)
        percentage = self.progress_manager.get_completion_percentage()
        self.assertAlmostEqual(percentage, 27.27, places=1)
    
    def test_add_achievement(self):
        """Testa adição de conquista"""
        achievement = "Primeiro Módulo Completo"
        
        self.progress_manager.add_achievement(achievement)
        
        achievements = self.progress_manager.progress_data['achievements']
        self.assertEqual(len(achievements), 1)
        self.assertEqual(achievements[0]['name'], achievement)
        
        # Testa que não adiciona duplicatas
        self.progress_manager.add_achievement(achievement)
        self.assertEqual(len(self.progress_manager.progress_data['achievements']), 1)
    
    def test_get_progress_summary(self):
        """Testa obtenção de resumo de progresso"""
        self.progress_manager.set_user_name("Maria Santos")
        self.progress_manager.mark_module_completed("modulo_1", 90)
        self.progress_manager.add_achievement("Iniciante Python")
        
        summary = self.progress_manager.get_progress_summary()
        
        self.assertEqual(summary['user_name'], "Maria Santos")
        self.assertEqual(summary['total_score'], 90)
        self.assertEqual(summary['modules_completed'], 1)
        self.assertEqual(summary['achievements'], 1)
        self.assertGreater(summary['completion_percentage'], 0)
    
    def test_reset_progress(self):
        """Testa reset de progresso"""
        # Adiciona alguns dados
        self.progress_manager.set_user_name("Pedro Lima")
        self.progress_manager.mark_module_completed("modulo_1", 100)
        
        # Reset
        self.progress_manager.reset_progress()
        
        # Verifica se foi resetado
        self.assertEqual(self.progress_manager.progress_data['user_name'], "")
        self.assertEqual(len(self.progress_manager.progress_data['modules_completed']), 0)
        self.assertEqual(self.progress_manager.progress_data['total_score'], 0)
    
    def test_invalid_module_id(self):
        """Testa comportamento com ID de módulo inválido"""
        invalid_id = "modulo_inexistente"
        
        # Não deve gerar erro
        self.progress_manager.update_module_progress(invalid_id, 100, 1)
        self.progress_manager.mark_module_completed(invalid_id, 50)
        
        # Mas deve adicionar à lista de completos
        self.assertIn(invalid_id, self.progress_manager.progress_data['modules_completed'])


if __name__ == '__main__':
    unittest.main()