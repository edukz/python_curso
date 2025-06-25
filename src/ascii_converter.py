#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ASCII Converter - Converte emojis e símbolos para ASCII
"""

from typing import Dict


class ASCIIConverter:
    """Converte emojis e símbolos especiais para representações ASCII"""
    
    # Mapeamento de emojis para ASCII
    EMOJI_TO_ASCII: Dict[str, str] = {
        # Navegação e UI
        "🏠": "[HOME]",
        "📍": "[>]",
        "▸": ">",
        "↩️": "<-",
        "🔙": "[BACK]",
        
        # Status e indicadores
        "✅": "[OK]",
        "❌": "[X]",
        "⚠️": "[!]",
        "📊": "[STATS]",
        "🎯": "[TARGET]",
        "🏆": "[TROPHY]",
        "⭐": "[*]",
        "💯": "[100%]",
        "🔥": "[HOT]",
        
        # Educacionais
        "🐍": "[PYTHON]",
        "📚": "[BOOKS]",
        "📖": "[BOOK]",
        "📝": "[NOTES]",
        "💡": "[IDEA]",
        "🧠": "[BRAIN]",
        "🎓": "[GRAD]",
        
        # Ações
        "👉": "->",
        "👋": "[WAVE]",
        "💾": "[SAVE]",
        "🚀": "[ROCKET]",
        "⏸️": "[PAUSE]",
        "▶️": "[PLAY]",
        "⏹️": "[STOP]",
        
        # Recursos especiais
        "🎪": "[DEMO]",
        "🔍": "[SEARCH]",
        "⚙️": "[CONFIG]",
        "🌟": "[SPECIAL]",
        "❓": "[HELP]",
        "🚪": "[EXIT]",
        
        # Progresso
        "📈": "[UP]",
        "⏱️": "[TIME]",
        "♻️": "[CYCLE]",
        
        # Emojis gerais
        "😊": ":)",
        "😎": "8)",
        "🤔": "(?)",
        "❤️": "<3",
        
        # Símbolos
        "•": "*",
        "→": "->",
        "←": "<-",
        "↑": "^",
        "↓": "v",
        "≈": "~",
        "≥": ">=",
        "≤": "<=",
    }
    
    def __init__(self, ascii_mode: bool = False):
        self.ascii_mode = ascii_mode
        
    def convert(self, text: str) -> str:
        """Converte texto com emojis para ASCII se modo ASCII ativo"""
        if not self.ascii_mode:
            return text
            
        result = text
        for emoji, ascii_rep in self.EMOJI_TO_ASCII.items():
            result = result.replace(emoji, ascii_rep)
            
        return result
        
    def convert_menu_item(self, key: str, text: str, ascii_mode: bool = None) -> str:
        """Converte item de menu para formato apropriado"""
        mode = ascii_mode if ascii_mode is not None else self.ascii_mode
        
        if mode:
            # Remove emojis e formata para ASCII
            clean_text = self.convert(text)
            return f"{key}. {clean_text}"
        else:
            return f"{key}. {text}"
            
    def get_separator(self, char: str = "=", length: int = 50) -> str:
        """Retorna separador apropriado"""
        return char * length
        
    def format_header(self, title: str, subtitle: str = "") -> str:
        """Formata cabeçalho para ASCII ou Unicode"""
        if self.ascii_mode:
            header = f"\n{self.get_separator('=')}\n"
            header += f"{self.convert(title).center(50)}\n"
            if subtitle:
                header += f"{self.convert(subtitle).center(50)}\n"
            header += f"{self.get_separator('=')}\n"
        else:
            header = f"\n{'=' * 50}\n"
            header += f"{title.center(50)}\n"
            if subtitle:
                header += f"{subtitle.center(50)}\n"
            header += f"{'=' * 50}\n"
            
        return header
        
    def format_progress_bar(self, progress: float, width: int = 30) -> str:
        """Cria barra de progresso ASCII"""
        filled = int(progress * width)
        empty = width - filled
        
        if self.ascii_mode:
            bar = "[" + "#" * filled + "-" * empty + "]"
        else:
            bar = "█" * filled + "░" * empty
            
        return f"{bar} {progress*100:.1f}%"