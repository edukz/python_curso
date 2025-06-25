#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Componentes de Interface do Usuário
Sistema modular para criar interfaces bonitas e consistentes
"""

import os
import time
from typing import List, Dict, Optional, Any
from .visual_feedback import USE_COLORS, Fore, Back, Style
from .ascii_converter import ASCIIConverter


class UIComponents:
    """Componentes reutilizáveis para interface do usuário"""
    
    def __init__(self, ascii_mode: bool = False, theme_manager=None):
        self.terminal_width = self._get_terminal_width()
        self.ascii_converter = ASCIIConverter(ascii_mode)
        self.theme_manager = theme_manager
        self.themes = {
            "default": {
                "primary": Fore.CYAN if USE_COLORS else "",
                "secondary": Fore.YELLOW if USE_COLORS else "",
                "success": Fore.GREEN if USE_COLORS else "",
                "error": Fore.RED if USE_COLORS else "",
                "info": Fore.BLUE if USE_COLORS else "",
                "warning": Fore.YELLOW if USE_COLORS else "",
                "accent": Fore.MAGENTA if USE_COLORS else "",
                "reset": Style.RESET_ALL if USE_COLORS else ""
            },
            "dark": {
                "primary": Fore.WHITE if USE_COLORS else "",
                "secondary": Fore.LIGHTBLUE_EX if USE_COLORS else "",
                "success": Fore.LIGHTGREEN_EX if USE_COLORS else "",
                "error": Fore.LIGHTRED_EX if USE_COLORS else "",
                "info": Fore.LIGHTCYAN_EX if USE_COLORS else "",
                "warning": Fore.LIGHTYELLOW_EX if USE_COLORS else "",
                "accent": Fore.LIGHTMAGENTA_EX if USE_COLORS else "",
                "reset": Style.RESET_ALL if USE_COLORS else ""
            }
        }
        self.current_theme = "default"
    
    def _get_terminal_width(self) -> int:
        """Obtém a largura do terminal"""
        try:
            return os.get_terminal_size().columns
        except:
            return 80  # Largura padrão
    
    def clear_screen(self) -> None:
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def set_theme(self, theme_name: str) -> None:
        """Define o tema de cores"""
        if theme_name in self.themes:
            self.current_theme = theme_name
    
    def get_color(self, color_name: str) -> str:
        """Obtém uma cor do tema atual"""
        if self.theme_manager:
            # Usa o sistema avançado de temas
            ansi_colors = self.theme_manager.get_ansi_colors()
            return ansi_colors.get(color_name, "")
        else:
            # Fallback para sistema antigo
            return self.themes[self.current_theme].get(color_name, "")
    
    def header(self, title: str, subtitle: str = "", icon: str = "🐍") -> None:
        """Cria um cabeçalho estilizado"""
        primary = self.get_color("primary")
        secondary = self.get_color("secondary")
        reset = self.get_color("reset")
        
        # Converte para ASCII se necessário
        icon = self.ascii_converter.convert(icon)
        title = self.ascii_converter.convert(title)
        subtitle = self.ascii_converter.convert(subtitle)
        
        # Linha superior - usa configuração do tema se disponível
        if self.theme_manager:
            theme = self.theme_manager.get_current_theme()
            line_char = theme.border_style if not theme.ascii_mode else "="
            # Atualiza ascii_converter com configurações do tema
            self.ascii_converter.ascii_mode = theme.ascii_mode
        else:
            line_char = "=" if self.ascii_converter.ascii_mode else "═"
        line = line_char * self.terminal_width
        print(f"{primary}{line}{reset}")
        
        # Título principal
        title_line = f"{icon} {title} {icon}"
        padding = (self.terminal_width - len(title_line)) // 2
        print(f"{primary}{' ' * padding}{title_line}{reset}")
        
        # Subtítulo se fornecido
        if subtitle:
            sub_padding = (self.terminal_width - len(subtitle)) // 2
            print(f"{secondary}{' ' * sub_padding}{subtitle}{reset}")
        
        # Linha inferior
        print(f"{primary}{line}{reset}")
        print()
    
    def section(self, title: str, icon: str = "📋") -> None:
        """Cria uma seção com título"""
        primary = self.get_color("primary")
        reset = self.get_color("reset")
        
        print(f"\n{primary}{'─' * self.terminal_width}{reset}")
        print(f"{primary}{icon} {title.upper()}{reset}")
        print(f"{primary}{'─' * self.terminal_width}{reset}")
    
    def box(self, content: str, title: str = "", box_type: str = "info") -> None:
        """Cria uma caixa com bordas"""
        color = self.get_color(box_type)
        reset = self.get_color("reset")
        
        lines = content.split('\n')
        max_width = max(len(line) for line in lines)
        box_width = min(max_width + 4, self.terminal_width - 4)
        
        # Linha superior
        if title:
            title_line = f"┌─ {title} " + "─" * (box_width - len(title) - 4) + "┐"
        else:
            title_line = "┌" + "─" * (box_width - 2) + "┐"
        
        print(f"{color}{title_line}{reset}")
        
        # Conteúdo
        for line in lines:
            padded_line = f"│ {line:<{box_width - 4}} │"
            print(f"{color}{padded_line}{reset}")
        
        # Linha inferior
        bottom_line = "└" + "─" * (box_width - 2) + "┘"
        print(f"{color}{bottom_line}{reset}")
    
    def progress_bar(self, current: int, total: int, label: str = "", width: int = 40) -> None:
        """Cria uma barra de progresso visual"""
        if total == 0:
            percentage = 0
        else:
            percentage = (current / total) * 100
        
        filled = int((current / total) * width) if total > 0 else 0
        bar = "█" * filled + "░" * (width - filled)
        
        primary = self.get_color("primary")
        success = self.get_color("success")
        reset = self.get_color("reset")
        
        color = success if percentage == 100 else primary
        
        if label:
            print(f"{label}")
        
        print(f"{color}[{bar}] {percentage:5.1f}% ({current}/{total}){reset}")
    
    def menu(self, options: List[Dict[str, Any]], title: str = "Menu") -> None:
        """Cria um menu estilizado"""
        self.header(title, icon="📋")
        
        primary = self.get_color("primary")
        secondary = self.get_color("secondary")
        success = self.get_color("success")
        reset = self.get_color("reset")
        
        for option in options:
            key = option.get("key", "")
            text = option.get("text", "")
            icon = option.get("icon", "•")
            status = option.get("status", "")
            
            # Cor baseada no status
            if status == "completed":
                status_color = success
                status_icon = "✅"
            elif status == "in_progress":
                status_color = secondary
                status_icon = "🔄"
            else:
                status_color = primary
                status_icon = icon
            
            print(f"{status_color}{status_icon} {key}. {text}{reset}")
    
    def card(self, title: str, content: str, icon: str = "📄", card_type: str = "info") -> None:
        """Cria um cartão informativo"""
        color = self.get_color(card_type)
        reset = self.get_color("reset")
        
        # Cabeçalho do cartão
        header_line = f"┌─ {icon} {title} "
        header_line += "─" * (self.terminal_width - len(header_line) - 1) + "┐"
        
        print(f"\n{color}{header_line}{reset}")
        
        # Conteúdo
        for line in content.split('\n'):
            if line.strip():
                padded = f"│ {line}"
                padding = self.terminal_width - len(padded) - 1
                print(f"{color}{padded}{' ' * padding}│{reset}")
        
        # Rodapé
        footer_line = "└" + "─" * (self.terminal_width - 2) + "┘"
        print(f"{color}{footer_line}{reset}")
    
    def alert(self, message: str, alert_type: str = "info", icon: str = "") -> None:
        """Cria um alerta colorido"""
        color = self.get_color(alert_type)
        reset = self.get_color("reset")
        
        icons = {
            "success": "✅",
            "error": "❌",
            "warning": "⚠️",
            "info": "ℹ️"
        }
        
        alert_icon = icon or icons.get(alert_type, "•")
        
        if USE_COLORS:
            bg_color = Back.GREEN if alert_type == "success" else \
                      Back.RED if alert_type == "error" else \
                      Back.YELLOW if alert_type == "warning" else \
                      Back.BLUE
            
            text_color = Fore.BLACK if alert_type in ["success", "warning"] else Fore.WHITE
            
            print(f"\n{bg_color}{text_color} {alert_icon} {message} {reset}\n")
        else:
            print(f"\n{alert_icon} {message}\n")
    
    def table(self, headers: List[str], rows: List[List[str]], title: str = "") -> None:
        """Cria uma tabela formatada"""
        if not rows:
            return
        
        primary = self.get_color("primary")
        secondary = self.get_color("secondary")
        reset = self.get_color("reset")
        
        # Calcula larguras das colunas
        col_widths = []
        for i, header in enumerate(headers):
            max_width = len(header)
            for row in rows:
                if i < len(row):
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)
        
        if title:
            print(f"\n{primary}{title}{reset}")
        
        # Linha superior
        line = "┌" + "┬".join("─" * width for width in col_widths) + "┐"
        print(f"{primary}{line}{reset}")
        
        # Cabeçalhos
        header_row = "│" + "│".join(f" {headers[i]:<{col_widths[i]-1}}" for i in range(len(headers))) + "│"
        print(f"{secondary}{header_row}{reset}")
        
        # Separador
        sep_line = "├" + "┼".join("─" * width for width in col_widths) + "┤"
        print(f"{primary}{sep_line}{reset}")
        
        # Dados
        for row in rows:
            data_row = "│" + "│".join(f" {str(row[i]) if i < len(row) else '':<{col_widths[i]-1}}" for i in range(len(headers))) + "│"
            print(f"{primary}{data_row}{reset}")
        
        # Linha inferior
        bottom_line = "└" + "┴".join("─" * width for width in col_widths) + "┘"
        print(f"{primary}{bottom_line}{reset}")
    
    def spinner(self, message: str = "Carregando", duration: float = 2.0) -> None:
        """Exibe um spinner animado"""
        spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        primary = self.get_color("primary")
        reset = self.get_color("reset")
        
        start_time = time.time()
        i = 0
        
        while time.time() - start_time < duration:
            spinner_char = spinners[i % len(spinners)]
            print(f"\r{primary}{spinner_char} {message}...{reset}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        
        print(f"\r{' ' * (len(message) + 10)}\r", end="", flush=True)
    
    def divider(self, char: str = "─", title: str = "") -> None:
        """Cria um divisor horizontal"""
        primary = self.get_color("primary")
        reset = self.get_color("reset")
        
        if title:
            title_part = f" {title} "
            remaining = self.terminal_width - len(title_part)
            left_chars = remaining // 2
            right_chars = remaining - left_chars
            
            line = char * left_chars + title_part + char * right_chars
        else:
            line = char * self.terminal_width
        
        print(f"{primary}{line}{reset}")
    
    def countdown_visual(self, seconds: int, message: str = "Iniciando em") -> None:
        """Contagem regressiva visual aprimorada"""
        primary = self.get_color("primary")
        warning = self.get_color("warning")
        success = self.get_color("success")
        reset = self.get_color("reset")
        
        for i in range(seconds, 0, -1):
            # Cor baseada no tempo restante
            if i <= 3:
                color = warning
            else:
                color = primary
            
            # Barra visual do tempo
            bar_width = 20
            filled = int((i / seconds) * bar_width)
            bar = "█" * filled + "░" * (bar_width - filled)
            
            print(f"\r{color}{message}: {i} [{bar}]{reset}", end="", flush=True)
            time.sleep(1)
        
        print(f"\r{success}🚀 Vamos começar! {' ' * 30}{reset}")
        print()
    
    def error(self, message: str) -> None:
        """Exibe mensagem de erro"""
        error_color = self.get_color("error")
        reset = self.get_color("reset")
        print(f"\n{error_color}❌ {message}{reset}\n")
    
    def success(self, message: str) -> None:
        """Exibe mensagem de sucesso"""
        success_color = self.get_color("success")
        reset = self.get_color("reset")
        print(f"\n{success_color}✅ {message}{reset}\n")
    
    def warning(self, message: str) -> None:
        """Exibe mensagem de aviso"""
        warning_color = self.get_color("warning")
        reset = self.get_color("reset")
        print(f"\n{warning_color}⚠️ {message}{reset}\n")
    
    def info_box(self, title: str, content: str, icon: str = "ℹ️", box_type: str = "info") -> None:
        """Exibe uma caixa informativa"""
        self.box(content, title, box_type)
    
    def pause(self) -> None:
        """Pausa a execução esperando input do usuário"""
        try:
            input("\n🔸 Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            raise
    
    def alert(self, message: str, icon: str = "🔔", alert_type: str = "info") -> None:
        """Exibe um alerta destacado"""
        color_map = {
            "info": "info",
            "success": "success", 
            "error": "error",
            "warning": "warning",
            "achievement": "accent"
        }
        
        color = self.get_color(color_map.get(alert_type, "info"))
        reset = self.get_color("reset")
        
        print(f"\n{color}{'=' * 50}")
        print(f"{icon} {message}")
        print(f"{'=' * 50}{reset}\n")
        
        # Pausa para leitura
        input("🔸 Pressione ENTER para continuar...")
    
    def create_box(self, title: str, content: str, icon: str = "📦") -> str:
        """Cria uma caixa formatada e retorna como string"""
        primary = self.get_color("primary")
        reset = self.get_color("reset")
        
        lines = content.split('\n')
        max_width = max(len(line) for line in lines) if lines else 20
        box_width = min(max_width + 4, self.terminal_width - 4)
        
        result = []
        result.append(f"{primary}┌{'─' * (box_width - 2)}┐{reset}")
        result.append(f"{primary}│ {icon} {title:<{box_width - 6}} │{reset}")
        result.append(f"{primary}├{'─' * (box_width - 2)}┤{reset}")
        
        for line in lines:
            padded_line = f" {line:<{box_width - 4}} "
            result.append(f"{primary}│{padded_line}│{reset}")
        
        result.append(f"{primary}└{'─' * (box_width - 2)}┘{reset}")
        
        return '\n'.join(result)


class ThemeManager:
    """Gerenciador de temas visuais"""
    
    def __init__(self):
        self.themes = {
            "python": {
                "name": "Python Clássico",
                "colors": {
                    "primary": Fore.BLUE,
                    "secondary": Fore.YELLOW,
                    "success": Fore.GREEN,
                    "error": Fore.RED,
                    "accent": Fore.CYAN
                }
            },
            "matrix": {
                "name": "Matrix Verde",
                "colors": {
                    "primary": Fore.GREEN,
                    "secondary": Fore.LIGHTGREEN_EX,
                    "success": Fore.WHITE,
                    "error": Fore.RED,
                    "accent": Fore.GREEN
                }
            },
            "sunset": {
                "name": "Pôr do Sol",
                "colors": {
                    "primary": Fore.YELLOW,
                    "secondary": Fore.RED,
                    "success": Fore.GREEN,
                    "error": Fore.RED,
                    "accent": Fore.MAGENTA
                }
            }
        }
    
    def list_themes(self) -> List[str]:
        """Lista todos os temas disponíveis"""
        return list(self.themes.keys())
    
    def get_theme(self, theme_name: str) -> Dict[str, Any]:
        """Obtém um tema específico"""
        return self.themes.get(theme_name, self.themes["python"])