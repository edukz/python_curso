#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testes para o sistema de gamificação
"""

import unittest
import sys
import os
import json
import tempfile

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from gamification_system import GamificationSystem, BadgeType
from progress_manager import ProgressManager


class TestGamificationSystem(unittest.TestCase):
    """Testes para GamificationSystem"""
    
    def setUp(self):
        # Cria arquivo temporário para progresso
        self.temp_progress = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_progress.close()
        
        # Cria arquivo temporário para gamificação
        self.temp_gamification = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_gamification.close()
        
        # Inicializa managers
        self.progress = ProgressManager(self.temp_progress.name)
        self.gamification = GamificationSystem(
            self.progress, 
            gamification_file=self.temp_gamification.name
        )
    
    def tearDown(self):
        # Remove arquivos temporários
        try:
            os.unlink(self.temp_progress.name)
            os.unlink(self.temp_gamification.name)
        except:
            pass
    
    def test_initialization(self):
        """Testa inicialização do sistema"""
        self.assertEqual(self.gamification.get_nivel_atual(), 1)
        self.assertEqual(self.gamification.get_xp_atual(), 0)
        self.assertEqual(self.gamification.get_pontos_totais(), 0)
        self.assertEqual(len(self.gamification.get_badges_desbloqueados()), 0)
    
    def test_adicionar_xp(self):
        """Testa adição de XP"""
        # Adiciona XP sem subir de nível
        result = self.gamification.adicionar_xp(50, "Teste XP")
        
        self.assertEqual(result["xp_ganho"], 50)
        self.assertEqual(result["xp_atual"], 50)
        self.assertEqual(result["nivel_atual"], 1)
        self.assertFalse(result["subiu_nivel"])
        
        # Adiciona XP suficiente para subir de nível
        result = self.gamification.adicionar_xp(60, "Mais XP")
        
        self.assertEqual(result["xp_ganho"], 60)
        self.assertEqual(result["xp_atual"], 10)  # 110 total - 100 do nível 1
        self.assertEqual(result["nivel_atual"], 2)
        self.assertTrue(result["subiu_nivel"])
    
    def test_adicionar_pontos(self):
        """Testa adição de pontos"""
        inicial = self.gamification.get_pontos_totais()
        
        self.gamification.adicionar_pontos(100, "Módulo completo")
        self.assertEqual(self.gamification.get_pontos_totais(), inicial + 100)
        
        self.gamification.adicionar_pontos(50, "Exercício")
        self.assertEqual(self.gamification.get_pontos_totais(), inicial + 150)
    
    def test_desbloquear_badge(self):
        """Testa desbloqueio de badges"""
        # Desbloqueia novo badge
        desbloqueado = self.gamification.desbloquear_badge(
            BadgeType.FIRST_MODULE,
            "Primeira Conquista",
            "Completou o primeiro módulo"
        )
        self.assertTrue(desbloqueado)
        
        badges = self.gamification.get_badges_desbloqueados()
        self.assertEqual(len(badges), 1)
        self.assertEqual(badges[0]["tipo"], BadgeType.FIRST_MODULE)
        
        # Tenta desbloquear o mesmo badge
        desbloqueado = self.gamification.desbloquear_badge(
            BadgeType.FIRST_MODULE,
            "Primeira Conquista",
            "Completou o primeiro módulo"
        )
        self.assertFalse(desbloqueado)
        self.assertEqual(len(self.gamification.get_badges_desbloqueados()), 1)
    
    def test_verificar_conquistas_modulo(self):
        """Testa verificação de conquistas por módulo"""
        # Completa primeiro módulo
        badges = self.gamification.verificar_conquistas_modulo(
            "modulo_1",
            sem_erros=True,
            tempo_segundos=300
        )
        
        # Deve ganhar badge de primeiro módulo
        self.assertTrue(any(b["tipo"] == BadgeType.FIRST_MODULE for b in badges))
        
        # Completa vários módulos rapidamente
        for i in range(2, 6):
            self.gamification.verificar_conquistas_modulo(
                f"modulo_{i}",
                sem_erros=True,
                tempo_segundos=200
            )
        
        # Deve ter badge de velocidade
        all_badges = self.gamification.get_badges_desbloqueados()
        self.assertTrue(any(b["tipo"] == BadgeType.SPEED_DEMON for b in all_badges))
    
    def test_xp_para_proximo_nivel(self):
        """Testa cálculo de XP para próximo nível"""
        # Nível 1, sem XP
        self.assertEqual(self.gamification.get_xp_para_proximo_nivel(), 100)
        
        # Adiciona 30 XP
        self.gamification.adicionar_xp(30, "Teste")
        self.assertEqual(self.gamification.get_xp_para_proximo_nivel(), 70)
        
        # Sobe para nível 2
        self.gamification.adicionar_xp(80, "Teste")
        self.assertEqual(self.gamification.get_nivel_atual(), 2)
        # Nível 2 precisa de 150 XP
        self.assertEqual(self.gamification.get_xp_para_proximo_nivel(), 140)
    
    def test_progresso_nivel(self):
        """Testa cálculo de progresso do nível"""
        # Sem XP
        self.assertEqual(self.gamification.get_progresso_nivel(), 0.0)
        
        # 50% do nível 1
        self.gamification.adicionar_xp(50, "Teste")
        self.assertEqual(self.gamification.get_progresso_nivel(), 50.0)
        
        # 100% do nível 1 (sobe para 2)
        self.gamification.adicionar_xp(50, "Teste")
        self.assertEqual(self.gamification.get_progresso_nivel(), 0.0)
    
    def test_estatisticas(self):
        """Testa obtenção de estatísticas"""
        # Adiciona dados
        self.gamification.adicionar_xp(150, "XP teste")
        self.gamification.adicionar_pontos(500, "Pontos teste")
        self.gamification.desbloquear_badge(
            BadgeType.PERFECT_SCORE,
            "Perfeito",
            "Pontuação perfeita"
        )
        
        stats = self.gamification.get_estatisticas()
        
        self.assertEqual(stats["nivel"], 2)
        self.assertEqual(stats["xp_atual"], 50)
        self.assertEqual(stats["xp_total"], 150)
        self.assertEqual(stats["pontos"], 500)
        self.assertEqual(stats["badges"], 1)
        self.assertEqual(stats["ranking"], "Aprendiz")
    
    def test_titulo_por_nivel(self):
        """Testa títulos por nível"""
        titulos = [
            (1, "Iniciante"),
            (5, "Aprendiz"),
            (10, "Estudante"),
            (15, "Praticante"),
            (20, "Conhecedor"),
            (25, "Experiente"),
            (30, "Avançado"),
            (40, "Expert"),
            (50, "Mestre"),
            (75, "Grão-Mestre"),
            (100, "Lenda")
        ]
        
        for nivel, titulo_esperado in titulos:
            # Força o nível
            self.gamification.game_data["nivel"] = nivel
            self.assertEqual(self.gamification.get_titulo(), titulo_esperado)
    
    def test_persistencia(self):
        """Testa persistência dos dados"""
        # Adiciona dados
        self.gamification.adicionar_xp(250, "XP teste")
        self.gamification.adicionar_pontos(1000, "Pontos teste")
        self.gamification.desbloquear_badge(
            BadgeType.CODING_STREAK,
            "Sequência",
            "7 dias seguidos"
        )
        
        # Cria nova instância com mesmo arquivo
        gamification2 = GamificationSystem(
            self.progress,
            gamification_file=self.temp_gamification.name
        )
        
        # Verifica se dados foram carregados
        self.assertEqual(gamification2.get_nivel_atual(), 3)
        self.assertEqual(gamification2.get_xp_atual(), 0)
        self.assertEqual(gamification2.get_pontos_totais(), 1000)
        self.assertEqual(len(gamification2.get_badges_desbloqueados()), 1)


if __name__ == '__main__':
    unittest.main()