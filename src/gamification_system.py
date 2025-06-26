#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gamificação Avançado
Níveis, badges, desafios, streaks e recompensas
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum


class PlayerLevel(Enum):
    """Níveis do jogador"""
    INICIANTE = (0, "🥚", "Ovo de Píton")
    APRENDIZ = (100, "🐣", "Filhote de Píton")
    ESTUDANTE = (300, "🐍", "Píton Jovem")
    PRATICANTE = (600, "🎓", "Píton Estudioso")
    DESENVOLVEDOR = (1000, "💻", "Píton Developer")
    EXPERT = (1500, "🏆", "Píton Expert")
    MESTRE = (2500, "🌟", "Mestre Píton")
    LENDARIO = (5000, "👑", "Píton Lendário")


class BadgeType(Enum):
    """Tipos de badges/conquistas"""
    # Progresso
    PRIMEIRO_PASSO = ("🥇", "Primeiro Passo", "Complete seu primeiro módulo")
    METADE_CAMINHO = ("🎯", "Meio Caminho", "Complete 50% do curso")
    FINALIZADOR = ("🏁", "Finalizador", "Complete todos os módulos")
    
    # Velocidade
    VELOCISTA = ("⚡", "Velocista", "Complete 3 módulos em um dia")
    MARATONISTA = ("🏃", "Maratonista", "Estude por 2 horas seguidas")
    
    # Consistência
    STREAK_7 = ("🔥", "Semana de Fogo", "7 dias consecutivos")
    STREAK_30 = ("💎", "Mês Dourado", "30 dias consecutivos")
    STREAK_100 = ("💫", "Centenário", "100 dias consecutivos")
    
    # Perfeição
    SEM_ERROS = ("✨", "Perfeição", "Complete um módulo sem erros")
    MESTRE_DEBUG = ("🔧", "Mestre do Debug", "Resolva 10 erros")
    
    # Especiais
    NOTTURNO = ("🦉", "Coruja Noturna", "Estude após 22h")
    MADRUGADOR = ("🌅", "Madrugador", "Estude antes das 6h")
    CURIOSO = ("🔍", "Curioso", "Use o Assistente 20 vezes")
    SOCIAL = ("🤝", "Social", "Compartilhe seu progresso")
    EXPLORADOR = ("🗺️", "Explorador", "Experimente todos os recursos")


class GamificationSystem:
    """Sistema completo de gamificação"""
    
    def __init__(self, progress_manager):
        self.progress = progress_manager
        self.game_file = "data/gamification.json"
        self.game_data = self._load_game_data()
        
    def _load_game_data(self) -> Dict[str, Any]:
        """Carrega dados de gamificação"""
        if os.path.exists(self.game_file):
            try:
                with open(self.game_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self._create_default_game_data()
        return self._create_default_game_data()
    
    def _create_default_game_data(self) -> Dict[str, Any]:
        """Cria estrutura padrão de gamificação"""
        return {
            "xp_total": 0,
            "nivel_atual": "INICIANTE",
            "badges_desbloqueados": [],
            "streak_atual": 0,
            "maior_streak": 0,
            "ultimo_acesso": None,
            "moedas": 100,  # Moedas iniciais
            "power_ups_comprados": [],
            "desafios_completos": [],
            "estatisticas": {
                "modulos_sem_erro": 0,
                "erros_resolvidos": 0,
                "tempo_total_estudo": 0,
                "ajudas_usadas": 0,
                "exercicios_completos": 0
            },
            "historico_xp": [],
            "ranking_local": []
        }
    
    def save_game_data(self) -> None:
        """Salva dados de gamificação"""
        with open(self.game_file, 'w', encoding='utf-8') as f:
            json.dump(self.game_data, f, indent=2, ensure_ascii=False)
    
    def adicionar_xp(self, quantidade: int, motivo: str) -> Dict[str, Any]:
        """Adiciona XP e verifica subida de nível"""
        self.game_data["xp_total"] += quantidade
        
        # Registra no histórico
        self.game_data["historico_xp"].append({
            "quantidade": quantidade,
            "motivo": motivo,
            "timestamp": datetime.now().isoformat()
        })
        
        # Verifica novo nível
        nivel_anterior = self.game_data["nivel_atual"]
        novo_nivel = self._calcular_nivel()
        
        resultado = {
            "xp_ganho": quantidade,
            "xp_total": self.game_data["xp_total"],
            "subiu_nivel": False,
            "nivel_atual": novo_nivel
        }
        
        if novo_nivel != nivel_anterior:
            self.game_data["nivel_atual"] = novo_nivel
            resultado["subiu_nivel"] = True
            resultado["nivel_anterior"] = nivel_anterior
            
            # Recompensa por subir de nível
            bonus_moedas = self._get_nivel_info(novo_nivel)[0] // 10
            self.adicionar_moedas(bonus_moedas, f"Subiu para {novo_nivel}")
            resultado["bonus_moedas"] = bonus_moedas
        
        self.save_game_data()
        return resultado
    
    def _calcular_nivel(self) -> str:
        """Calcula nível baseado no XP total"""
        xp = self.game_data["xp_total"]
        
        for nivel in reversed(list(PlayerLevel)):
            if xp >= nivel.value[0]:
                return nivel.name
        
        return PlayerLevel.INICIANTE.name
    
    def _get_nivel_info(self, nivel_nome: str) -> Tuple[int, str, str]:
        """Retorna informações do nível"""
        nivel = PlayerLevel[nivel_nome]
        return nivel.value
    
    def adicionar_moedas(self, quantidade: int, motivo: str) -> int:
        """Adiciona moedas virtuais"""
        self.game_data["moedas"] += quantidade
        self.save_game_data()
        return self.game_data["moedas"]
    
    def gastar_moedas(self, quantidade: int) -> bool:
        """Gasta moedas se disponível"""
        if self.game_data["moedas"] >= quantidade:
            self.game_data["moedas"] -= quantidade
            self.save_game_data()
            return True
        return False
    
    def verificar_e_atualizar_streak(self) -> Dict[str, Any]:
        """Verifica e atualiza streak diário"""
        hoje = datetime.now().date().isoformat()
        ultimo_acesso = self.game_data.get("ultimo_acesso")
        
        resultado = {
            "manteve_streak": False,
            "quebrou_streak": False,
            "streak_atual": self.game_data["streak_atual"]
        }
        
        if ultimo_acesso:
            ultimo_date = datetime.fromisoformat(ultimo_acesso).date()
            hoje_date = datetime.now().date()
            diferenca = (hoje_date - ultimo_date).days
            
            if diferenca == 1:  # Dia consecutivo
                self.game_data["streak_atual"] += 1
                resultado["manteve_streak"] = True
                resultado["streak_atual"] = self.game_data["streak_atual"]
                
                # Verifica badges de streak
                self._verificar_badges_streak()
                
            elif diferenca > 1:  # Quebrou streak
                self.game_data["streak_atual"] = 1
                resultado["quebrou_streak"] = True
                resultado["dias_perdidos"] = diferenca
        else:
            # Primeiro acesso
            self.game_data["streak_atual"] = 1
        
        # Atualiza maior streak
        if self.game_data["streak_atual"] > self.game_data["maior_streak"]:
            self.game_data["maior_streak"] = self.game_data["streak_atual"]
        
        self.game_data["ultimo_acesso"] = hoje
        self.save_game_data()
        
        return resultado
    
    def desbloquear_badge(self, badge_type: BadgeType) -> bool:
        """Desbloqueia um badge se ainda não tiver"""
        badge_id = badge_type.name
        
        if badge_id not in self.game_data["badges_desbloqueados"]:
            self.game_data["badges_desbloqueados"].append({
                "id": badge_id,
                "nome": badge_type.value[1],
                "descricao": badge_type.value[2],
                "icone": badge_type.value[0],
                "data": datetime.now().isoformat()
            })
            
            # Recompensa por badge
            self.adicionar_xp(50, f"Badge desbloqueado: {badge_type.value[1]}")
            self.adicionar_moedas(25, f"Badge: {badge_type.value[1]}")
            
            self.save_game_data()
            return True
        
        return False
    
    def _verificar_badges_streak(self) -> List[BadgeType]:
        """Verifica badges de streak"""
        badges_novos = []
        streak = self.game_data["streak_atual"]
        
        if streak >= 7 and not self._tem_badge(BadgeType.STREAK_7):
            if self.desbloquear_badge(BadgeType.STREAK_7):
                badges_novos.append(BadgeType.STREAK_7)
        
        if streak >= 30 and not self._tem_badge(BadgeType.STREAK_30):
            if self.desbloquear_badge(BadgeType.STREAK_30):
                badges_novos.append(BadgeType.STREAK_30)
        
        if streak >= 100 and not self._tem_badge(BadgeType.STREAK_100):
            if self.desbloquear_badge(BadgeType.STREAK_100):
                badges_novos.append(BadgeType.STREAK_100)
        
        return badges_novos
    
    def _tem_badge(self, badge_type: BadgeType) -> bool:
        """Verifica se já tem o badge"""
        return any(b["id"] == badge_type.name for b in self.game_data["badges_desbloqueados"])
    
    def verificar_conquistas_modulo(self, modulo_id: str, sem_erros: bool, tempo_segundos: int) -> List[BadgeType]:
        """Verifica conquistas ao completar módulo"""
        badges_novos = []
        
        # Primeira conquista
        if len(self.progress.progress_data["modules_completed"]) == 1:
            if self.desbloquear_badge(BadgeType.PRIMEIRO_PASSO):
                badges_novos.append(BadgeType.PRIMEIRO_PASSO)
        
        # Metade do caminho
        if len(self.progress.progress_data["modules_completed"]) == 13:
            if self.desbloquear_badge(BadgeType.METADE_CAMINHO):
                badges_novos.append(BadgeType.METADE_CAMINHO)
        
        # Finalizador
        if len(self.progress.progress_data["modules_completed"]) == 26:
            if self.desbloquear_badge(BadgeType.FINALIZADOR):
                badges_novos.append(BadgeType.FINALIZADOR)
        
        # Sem erros
        if sem_erros:
            self.game_data["estatisticas"]["modulos_sem_erro"] += 1
            if self.game_data["estatisticas"]["modulos_sem_erro"] == 1:
                if self.desbloquear_badge(BadgeType.SEM_ERROS):
                    badges_novos.append(BadgeType.SEM_ERROS)
        
        # Maratonista (2 horas = 7200 segundos)
        if tempo_segundos >= 7200:
            if self.desbloquear_badge(BadgeType.MARATONISTA):
                badges_novos.append(BadgeType.MARATONISTA)
        
        # Horário especial
        hora_atual = datetime.now().hour
        if hora_atual >= 22 or hora_atual < 5:
            if self.desbloquear_badge(BadgeType.NOTTURNO):
                badges_novos.append(BadgeType.NOTTURNO)
        elif hora_atual < 6:
            if self.desbloquear_badge(BadgeType.MADRUGADOR):
                badges_novos.append(BadgeType.MADRUGADOR)
        
        return badges_novos
    
    def criar_desafio_diario(self) -> Dict[str, Any]:
        """Cria desafio diário personalizado"""
        from random import choice, randint
        
        # Tipos de desafios baseados no progresso
        modulos_completos = len(self.progress.progress_data["modules_completed"])
        
        desafios_possiveis = []
        
        if modulos_completos < 5:
            desafios_possiveis.extend([
                {
                    "tipo": "completar_modulo",
                    "titulo": "📚 Explorador Iniciante",
                    "descricao": "Complete 1 módulo hoje",
                    "meta": 1,
                    "recompensa_xp": 100,
                    "recompensa_moedas": 50
                },
                {
                    "tipo": "sem_erros",
                    "titulo": "✨ Precisão Perfeita",
                    "descricao": "Complete exercícios sem erros",
                    "meta": 3,
                    "recompensa_xp": 150,
                    "recompensa_moedas": 75
                }
            ])
        else:
            desafios_possiveis.extend([
                {
                    "tipo": "revisar",
                    "titulo": "🔄 Mestre da Revisão",
                    "descricao": "Revise 2 módulos anteriores",
                    "meta": 2,
                    "recompensa_xp": 120,
                    "recompensa_moedas": 60
                },
                {
                    "tipo": "velocidade",
                    "titulo": "⚡ Velocista",
                    "descricao": "Complete 3 exercícios em 10 minutos",
                    "meta": 3,
                    "recompensa_xp": 200,
                    "recompensa_moedas": 100
                },
                {
                    "tipo": "ajudar",
                    "titulo": "🤝 Mentor",
                    "descricao": "Use o Assistente para aprender 2 conceitos novos",
                    "meta": 2,
                    "recompensa_xp": 80,
                    "recompensa_moedas": 40
                }
            ])
        
        # Escolhe um desafio aleatório
        desafio = choice(desafios_possiveis)
        desafio["id"] = f"daily_{datetime.now().strftime('%Y%m%d')}"
        desafio["progresso"] = 0
        desafio["completo"] = False
        
        return desafio
    
    def atualizar_ranking_local(self, nome: str, pontos: int) -> None:
        """Atualiza ranking local (para modo sala de aula)"""
        entrada = {
            "nome": nome,
            "pontos": pontos,
            "nivel": self.game_data["nivel_atual"],
            "badges": len(self.game_data["badges_desbloqueados"]),
            "data": datetime.now().isoformat()
        }
        
        # Adiciona ou atualiza entrada
        ranking = self.game_data["ranking_local"]
        existe = False
        
        for i, jogador in enumerate(ranking):
            if jogador["nome"] == nome:
                ranking[i] = entrada
                existe = True
                break
        
        if not existe:
            ranking.append(entrada)
        
        # Ordena por pontos (decrescente)
        ranking.sort(key=lambda x: x["pontos"], reverse=True)
        
        # Mantém top 10
        self.game_data["ranking_local"] = ranking[:10]
        self.save_game_data()
    
    def obter_power_ups_disponiveis(self) -> List[Dict[str, Any]]:
        """Lista power-ups disponíveis para compra"""
        return [
            {
                "id": "dica_gratis",
                "nome": "💡 Dica Grátis",
                "descricao": "Receba uma dica sem perder pontos",
                "custo": 50,
                "tipo": "consumivel"
            },
            {
                "id": "pular_exercicio",
                "nome": "⏭️ Pular Exercício",
                "descricao": "Pule um exercício difícil",
                "custo": 100,
                "tipo": "consumivel"
            },
            {
                "id": "xp_dobrado",
                "nome": "✨ XP Dobrado",
                "descricao": "Ganhe XP em dobro por 1 hora",
                "custo": 200,
                "tipo": "temporario"
            },
            {
                "id": "revelar_resposta",
                "nome": "🔍 Revelar Resposta",
                "descricao": "Veja a resposta de um exercício",
                "custo": 150,
                "tipo": "consumivel"
            },
            {
                "id": "escudo_erro",
                "nome": "🛡️ Escudo de Erro",
                "descricao": "Primeiro erro não conta",
                "custo": 75,
                "tipo": "consumivel"
            }
        ]
    
    def comprar_power_up(self, power_up_id: str) -> bool:
        """Compra um power-up com moedas"""
        power_ups = self.obter_power_ups_disponiveis()
        power_up = next((p for p in power_ups if p["id"] == power_up_id), None)
        
        if power_up and self.gastar_moedas(power_up["custo"]):
            self.game_data["power_ups_comprados"].append({
                "id": power_up_id,
                "nome": power_up["nome"],
                "data_compra": datetime.now().isoformat(),
                "usado": False
            })
            self.save_game_data()
            return True
        
        return False
    
    def usar_power_up(self, power_up_id: str) -> bool:
        """Usa um power-up comprado"""
        for power_up in self.game_data["power_ups_comprados"]:
            if power_up["id"] == power_up_id and not power_up["usado"]:
                power_up["usado"] = True
                power_up["data_uso"] = datetime.now().isoformat()
                self.save_game_data()
                return True
        
        return False
    
    def exibir_perfil_gamer(self, ui_components) -> None:
        """Exibe perfil completo do jogador"""
        nivel_info = self._get_nivel_info(self.game_data["nivel_atual"])
        xp_atual = self.game_data["xp_total"]
        
        # Calcula XP para próximo nível
        proximo_nivel = None
        xp_proximo = 0
        for nivel in PlayerLevel:
            if nivel.value[0] > xp_atual:
                proximo_nivel = nivel
                xp_proximo = nivel.value[0]
                break
        
        ui_components.header("PERFIL GAMER", "Sistema de Gamificação", "🎮")
        
        # Card principal
        ui_components.card(
            f"{nivel_info[1]} {nivel_info[2]}",
            f"XP Total: {xp_atual}\n"
            f"Próximo Nível: {xp_proximo - xp_atual} XP\n"
            f"Moedas: 🪙 {self.game_data['moedas']}\n"
            f"Streak Atual: 🔥 {self.game_data['streak_atual']} dias\n"
            f"Maior Streak: 💎 {self.game_data['maior_streak']} dias",
            "👤",
            "info"
        )
        
        # Barra de progresso para próximo nível
        if proximo_nivel:
            nivel_anterior_xp = nivel_info[0]
            progresso = xp_atual - nivel_anterior_xp
            total = xp_proximo - nivel_anterior_xp
            ui_components.progress_bar(progresso, total, "Progresso para Próximo Nível", 30)
        
        # Badges
        if self.game_data["badges_desbloqueados"]:
            ui_components.section("CONQUISTAS DESBLOQUEADAS", "🏆")
            
            for badge in self.game_data["badges_desbloqueados"][-6:]:  # Últimas 6
                print(f"{badge['icone']} {badge['nome']} - {badge['descricao']}")
            
            print(f"\nTotal de Conquistas: {len(self.game_data['badges_desbloqueados'])}")
        
        # Estatísticas
        ui_components.section("ESTATÍSTICAS DE JOGO", "📊")
        stats = self.game_data["estatisticas"]
        print(f"📚 Módulos sem erro: {stats.get('modulos_sem_erro', 0)}")
        print(f"🔧 Erros resolvidos: {stats.get('erros_resolvidos', 0)}")
        print(f"✅ Exercícios completos: {stats.get('exercicios_completos', 0)}")
        print(f"🤝 Ajudas usadas: {stats.get('ajudas_usadas', 0)}")
        
        # Power-ups disponíveis
        power_ups_ativos = [p for p in self.game_data["power_ups_comprados"] if not p["usado"]]
        if power_ups_ativos:
            ui_components.section("POWER-UPS DISPONÍVEIS", "⚡")
            for power_up in power_ups_ativos:
                print(f"• {power_up['nome']}")
    
    def award_xp(self, quantidade: int, motivo: str) -> Dict[str, Any]:
        """Adiciona XP (alias para adicionar_xp para compatibilidade)"""
        return self.adicionar_xp(quantidade, motivo)
    
    def get_estatisticas(self) -> Dict[str, Any]:
        """Retorna estatísticas completas do sistema de gamificação"""
        nivel_info = self._get_nivel_info(self.game_data["nivel_atual"])
        xp_atual = self.game_data["xp_total"]
        
        # Calcula XP para próximo nível
        proximo_nivel = None
        xp_proximo = 0
        for nivel in PlayerLevel:
            if nivel.value[0] > xp_atual:
                proximo_nivel = nivel
                xp_proximo = nivel.value[0]
                break
        
        if xp_proximo == 0:  # Já está no nível máximo
            xp_proximo = xp_atual
        
        progresso_nivel = ((xp_atual % 100) / 100) * 100 if xp_proximo > xp_atual else 100
        
        return {
            "nivel": nivel_info[0],
            "ranking": nivel_info[2],
            "xp_atual": xp_atual,
            "xp_proximo_nivel": xp_proximo,
            "progresso_nivel": progresso_nivel,
            "badges": len(self.game_data.get("badges_desbloqueados", [])),
            "moedas": self.game_data.get("moedas", 0),
            "streak_atual": self.game_data.get("streak_atual", 0),
            "melhor_streak": self.game_data.get("melhor_streak", 0)
        }

    def unlock_badge(self, badge_id: str, emoji: str, nome: str, descricao: str) -> bool:
        """Desbloqueia uma nova conquista/badge"""
        # Verifica se já possui este badge
        if any(badge["id"] == badge_id for badge in self.game_data["badges_desbloqueados"]):
            return False
        
        # Adiciona novo badge
        novo_badge = {
            "id": badge_id,
            "emoji": emoji,
            "nome": nome,
            "descricao": descricao,
            "data_desbloqueio": datetime.now().isoformat()
        }
        
        self.game_data["badges_desbloqueados"].append(novo_badge)
        
        # Recompensas por desbloquear badge
        self.adicionar_xp(50, f"Badge desbloqueado: {nome}")
        self.adicionar_moedas(25, f"Recompensa do badge: {nome}")
        
        self.save_game_data()
        return True


class AchievementNotifier:
    """Sistema de notificação de conquistas"""
    
    @staticmethod
    def notificar_conquista(badge: BadgeType, ui_components) -> None:
        """Exibe notificação especial de conquista"""
        import time
        
        # Limpa tela para efeito dramático
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Animação simples
        for i in range(3):
            print("\n" * 10)
            print("✨" * (20 + i * 5))
            time.sleep(0.2)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # Exibe conquista
        ui_components.header(
            "🎉 NOVA CONQUISTA DESBLOQUEADA! 🎉",
            "",
            badge.value[0]
        )
        
        ui_components.card(
            badge.value[1],
            badge.value[2],
            badge.value[0],
            "success"
        )
        
        print("\n" + "🌟" * 40)
        print("\n+50 XP | +25 Moedas")
        print("\n" + "🌟" * 40)
        
        time.sleep(3)