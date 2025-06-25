#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Feedback Visual e Pontuação
Melhora a interatividade do curso com elementos visuais
"""

import time
import random
import os
import sys
from typing import List, Optional

# Tenta importar colorama, mas funciona sem ela
try:
    from colorama import init, Fore, Back, Style
    # Inicializa colorama para Windows
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    # Define classes vazias se colorama não estiver disponível
    class Fore:
        GREEN = ""
        RED = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        BLACK = ""
    
    class Back:
        YELLOW = ""
        GREEN = ""
        RED = ""
        BLUE = ""
    
    class Style:
        RESET_ALL = ""
        BRIGHT = ""
    
    HAS_COLORAMA = False

# Detecta se o terminal suporta cores
def supports_color():
    """Detecta se o terminal suporta cores ANSI"""
    # Windows CMD sem colorama
    if os.name == 'nt' and not HAS_COLORAMA:
        return False
    
    # Verifica variáveis de ambiente
    if 'NO_COLOR' in os.environ:
        return False
    
    # Verifica se está rodando em terminal
    if not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
        return False
    
    # Verifica TERM
    term = os.environ.get('TERM', '')
    if term in ('dumb', 'unknown'):
        return False
    
    return True

# Define se deve usar cores
USE_COLORS = supports_color() and HAS_COLORAMA


class VisualFeedback:
    """Classe para feedback visual e sistema de pontuação"""
    
    def __init__(self):
        self.score = 0
        self.streak = 0
        self.emojis = {
            "correct": ["🎉", "✨", "🌟", "💫", "🏆", "👏", "🎯"],
            "incorrect": ["💭", "🤔", "🔄", "💪"],
            "progress": ["📈", "📊", "🚀", "⭐"],
            "achievement": ["🏅", "🥇", "🎖️", "👑"]
        }
    
    def success_animation(self, message: str = "Correto!") -> None:
        """Animação para resposta correta"""
        emoji = random.choice(self.emojis["correct"])
        
        if USE_COLORS:
            print(f"\n{Fore.GREEN}{emoji} {message} {emoji}{Style.RESET_ALL}")
            # Barra de progresso animada
            for i in range(20):
                print(f"\r{Fore.GREEN}{'█' * i}{'░' * (20-i)}{Style.RESET_ALL}", end='', flush=True)
                time.sleep(0.05)
            print()
        else:
            print(f"\n{emoji} {message} {emoji}")
            # Barra de progresso simples
            for i in range(20):
                print(f"\r{'█' * i}{'░' * (20-i)}", end='', flush=True)
                time.sleep(0.05)
            print()
    
    def error_animation(self, message: str = "Não foi dessa vez!") -> None:
        """Animação para resposta incorreta"""
        emoji = random.choice(self.emojis["incorrect"])
        
        if USE_COLORS:
            print(f"\n{Fore.YELLOW}{emoji} {message}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Dica: Tente novamente, você consegue!{Style.RESET_ALL}")
        else:
            print(f"\n{emoji} {message}")
            print("Dica: Tente novamente, você consegue!")
    
    def add_score(self, points: int, reason: str = "") -> None:
        """Adiciona pontos com feedback visual"""
        self.score += points
        self.streak += 1
        
        if USE_COLORS:
            print(f"\n{Fore.MAGENTA}+{points} pontos! {reason}{Style.RESET_ALL}")
        else:
            print(f"\n+{points} pontos! {reason}")
        self.show_score_bar()
        
        # Conquistas especiais
        if self.streak == 3:
            self.unlock_achievement("Sequência de 3!")
        elif self.streak == 5:
            self.unlock_achievement("Está pegando o jeito!")
        elif self.streak == 10:
            self.unlock_achievement("Mestre Python!")
    
    def reset_streak(self) -> None:
        """Reseta a sequência de acertos"""
        if self.streak > 0:
            if USE_COLORS:
                print(f"{Fore.YELLOW}Sequência interrompida em {self.streak} acertos{Style.RESET_ALL}")
            else:
                print(f"Sequência interrompida em {self.streak} acertos")
        self.streak = 0
    
    def show_score_bar(self) -> None:
        """Mostra barra de pontuação visual"""
        bar_length = 30
        filled = int((self.score / 1000) * bar_length)  # Assume max 1000 pontos
        filled = min(filled, bar_length)
        
        if USE_COLORS:
            bar = f"Pontuação: [{Fore.CYAN}{'█' * filled}{'░' * (bar_length - filled)}{Style.RESET_ALL}] {self.score} pts"
        else:
            bar = f"Pontuação: [{'█' * filled}{'░' * (bar_length - filled)}] {self.score} pts"
        print(bar)
    
    def unlock_achievement(self, achievement: str) -> None:
        """Mostra uma conquista desbloqueada"""
        emoji = random.choice(self.emojis["achievement"])
        
        if USE_COLORS:
            print(f"\n{Back.YELLOW}{Fore.BLACK} {emoji} CONQUISTA DESBLOQUEADA! {emoji} {Style.RESET_ALL}")
            print(f"{Fore.YELLOW}→ {achievement}{Style.RESET_ALL}\n")
        else:
            print(f"\n{emoji} CONQUISTA DESBLOQUEADA! {emoji}")
            print(f"→ {achievement}\n")
        time.sleep(1.5)
    
    def show_module_progress(self, current: int, total: int, module_name: str) -> None:
        """Mostra progresso do módulo"""
        percentage = (current / total) * 100 if total > 0 else 0
        bar_length = 40
        filled = int((percentage / 100) * bar_length)
        
        if USE_COLORS:
            print(f"\n{Fore.CYAN}📚 {module_name}{Style.RESET_ALL}")
            print(f"Progresso: [{Fore.GREEN}{'█' * filled}{'░' * (bar_length - filled)}{Style.RESET_ALL}] {percentage:.0f}%")
        else:
            print(f"\n📚 {module_name}")
            print(f"Progresso: [{'█' * filled}{'░' * (bar_length - filled)}] {percentage:.0f}%")
    
    def typing_effect(self, text: str, delay: float = 0.03) -> None:
        """Efeito de digitação para texto importante"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def celebration(self) -> None:
        """Animação de celebração para conclusão de módulo"""
        celebrations = ["🎊", "🎉", "✨", "🌟", "💫", "🏆"]
        
        print("\n" + " ".join(random.sample(celebrations, 3)))
        if USE_COLORS:
            self.typing_effect(f"{Fore.GREEN}Parabéns! Módulo concluído!{Style.RESET_ALL}", 0.05)
        else:
            self.typing_effect("Parabéns! Módulo concluído!", 0.05)
        print(" ".join(random.sample(celebrations, 3)) + "\n")
    
    def show_hint(self, hint: str, delay: int = 3) -> None:
        """Mostra uma dica após delay"""
        time.sleep(delay)
        if USE_COLORS:
            print(f"\n{Fore.CYAN}💡 Dica: {hint}{Style.RESET_ALL}")
        else:
            print(f"\n💡 Dica: {hint}")
    
    def countdown(self, seconds: int, message: str = "Começando em") -> None:
        """Contagem regressiva visual"""
        for i in range(seconds, 0, -1):
            if USE_COLORS:
                print(f"\r{message}: {Fore.YELLOW}{i}{Style.RESET_ALL}...", end='', flush=True)
            else:
                print(f"\r{message}: {i}...", end='', flush=True)
            time.sleep(1)
        
        if USE_COLORS:
            print(f"\r{Fore.GREEN}Vamos lá!{Style.RESET_ALL}          ")
        else:
            print(f"\rVamos lá!          ")
    
    def get_score_summary(self) -> str:
        """Retorna resumo da pontuação"""
        level = "Iniciante"
        if self.score >= 500:
            level = "Intermediário"
        if self.score >= 1000:
            level = "Avançado"
        if self.score >= 2000:
            level = "Expert"
        
        if USE_COLORS:
            return f"""
{Fore.MAGENTA}════════════════════════════════════
📊 RESUMO DA PONTUAÇÃO
════════════════════════════════════{Style.RESET_ALL}
Pontos Totais: {Fore.CYAN}{self.score}{Style.RESET_ALL}
Nível: {Fore.YELLOW}{level}{Style.RESET_ALL}
Sequência Atual: {Fore.GREEN}{self.streak}{Style.RESET_ALL}
"""
        else:
            return f"""
════════════════════════════════════
📊 RESUMO DA PONTUAÇÃO
════════════════════════════════════
Pontos Totais: {self.score}
Nível: {level}
Sequência Atual: {self.streak}
"""