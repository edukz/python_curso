#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o Gerenciador de Configurações
"""

import unittest
import os
import json
import tempfile
import sys

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.config_manager import ConfigManager


class TestConfigManager(unittest.TestCase):
    """Testes para a classe ConfigManager"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        # Cria arquivo temporário para testes
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.config_manager = ConfigManager(self.temp_file.name)
    
    def tearDown(self):
        """Limpeza após cada teste"""
        # Remove arquivo temporário
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_load_default_config(self):
        """Testa carregamento de configuração padrão"""
        config = self.config_manager.config
        
        self.assertIn('course', config)
        self.assertIn('display', config)
        self.assertIn('scoring', config)
        self.assertIn('features', config)
        self.assertEqual(config['course']['name'], 'Curso Interativo de Python')
    
    def test_get_config_value(self):
        """Testa obtenção de valor de configuração"""
        # Testa acesso direto
        use_colors = self.config_manager.get('display.use_colors')
        self.assertTrue(use_colors)
        
        # Testa valor padrão
        inexistente = self.config_manager.get('config.inexistente', 'valor_padrao')
        self.assertEqual(inexistente, 'valor_padrao')
    
    def test_set_config_value(self):
        """Testa definição de valor de configuração"""
        # Define novo valor
        self.config_manager.set('display.use_colors', False)
        self.assertFalse(self.config_manager.get('display.use_colors'))
        
        # Verifica se foi salvo
        new_manager = ConfigManager(self.temp_file.name)
        self.assertFalse(new_manager.get('display.use_colors'))
    
    def test_get_section(self):
        """Testa obtenção de seção completa"""
        scoring = self.config_manager.get_section('scoring')
        
        self.assertIsInstance(scoring, dict)
        self.assertIn('points_per_correct_answer', scoring)
        self.assertEqual(scoring['points_per_correct_answer'], 10)
    
    def test_create_nested_config(self):
        """Testa criação de configuração aninhada"""
        self.config_manager.set('new_feature.enabled', True)
        self.config_manager.set('new_feature.options.timeout', 30)
        
        self.assertTrue(self.config_manager.get('new_feature.enabled'))
        self.assertEqual(self.config_manager.get('new_feature.options.timeout'), 30)
    
    def test_reload_config(self):
        """Testa recarregamento de configuração"""
        # Modifica valor
        self.config_manager.set('course.version', '3.0')
        
        # Modifica arquivo diretamente
        with open(self.temp_file.name, 'r') as f:
            config = json.load(f)
        config['course']['version'] = '4.0'
        with open(self.temp_file.name, 'w') as f:
            json.dump(config, f)
        
        # Recarrega
        self.config_manager.reload()
        self.assertEqual(self.config_manager.get('course.version'), '4.0')
    
    def test_reset_to_defaults(self):
        """Testa reset para valores padrão"""
        # Modifica algumas configurações
        self.config_manager.set('display.use_emojis', False)
        self.config_manager.set('scoring.max_score', 5000)
        
        # Reset
        self.config_manager.reset_to_defaults()
        
        # Verifica valores padrão
        self.assertTrue(self.config_manager.get('display.use_emojis'))
        self.assertEqual(self.config_manager.get('scoring.max_score'), 2000)
    
    def test_invalid_json_file(self):
        """Testa comportamento com arquivo JSON inválido"""
        # Cria arquivo com JSON inválido
        with open(self.temp_file.name, 'w') as f:
            f.write('{ invalid json }')
        
        # Deve carregar configuração padrão sem erro
        manager = ConfigManager(self.temp_file.name)
        self.assertIn('course', manager.config)
    
    def test_keyboard_shortcuts(self):
        """Testa configurações de atalhos de teclado"""
        shortcuts = self.config_manager.get_section('keyboard_shortcuts')
        
        self.assertEqual(shortcuts['next_module'], 'n')
        self.assertEqual(shortcuts['quit'], 'q')
        
        # Modifica atalho
        self.config_manager.set('keyboard_shortcuts.quit', 'x')
        self.assertEqual(self.config_manager.get('keyboard_shortcuts.quit'), 'x')


if __name__ == '__main__':
    unittest.main()