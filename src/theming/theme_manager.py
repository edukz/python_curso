#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advanced Theme Manager - Sistema completo de temas e personalização
"""

import json
import os
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class ThemeType(Enum):
    """Tipos de tema disponíveis"""
    LIGHT = "light"
    DARK = "dark"
    HIGH_CONTRAST = "high_contrast"
    CUSTOM = "custom"
    RETRO = "retro"
    MATRIX = "matrix"


class FontSize(Enum):
    """Tamanhos de fonte disponíveis"""
    SMALL = "small"
    NORMAL = "normal"
    LARGE = "large"
    EXTRA_LARGE = "extra_large"


@dataclass
class ColorScheme:
    """Esquema de cores para um tema"""
    # Cores principais
    primary: str          # Cor principal (títulos, destaques)
    secondary: str        # Cor secundária (subtítulos)
    accent: str           # Cor de destaque (botões, links)
    
    # Estados
    success: str          # Verde para sucesso
    warning: str          # Amarelo para avisos
    error: str            # Vermelho para erros
    info: str             # Azul para informações
    
    # Interface
    background: str       # Fundo principal
    surface: str          # Fundo de cards/seções
    border: str           # Bordas
    
    # Texto
    text_primary: str     # Texto principal
    text_secondary: str   # Texto secundário
    text_muted: str       # Texto menos importante
    
    # Especiais
    code_bg: str          # Fundo de código
    code_text: str        # Texto de código
    highlight: str        # Destaque/seleção


@dataclass
class FontConfig:
    """Configuração de fontes"""
    size: FontSize
    header_multiplier: float    # Multiplicador para cabeçalhos
    code_font: str             # Fonte para código (monospace)
    ui_font: str               # Fonte para interface


@dataclass
class Theme:
    """Tema completo"""
    name: str
    type: ThemeType
    description: str
    colors: ColorScheme
    fonts: FontConfig
    use_colors: bool           # Se deve usar cores ANSI
    use_emojis: bool           # Se deve usar emojis
    ascii_mode: bool           # Modo ASCII
    
    # Configurações visuais
    border_style: str          # Estilo de borda (=, -, *, etc)
    separator_char: str        # Caractere separador
    progress_chars: Tuple[str, str]  # Caracteres para barra de progresso (filled, empty)


class AdvancedThemeManager:
    """Gerenciador avançado de temas"""
    
    def __init__(self, config_dir: str = "."):
        self.config_dir = config_dir
        self.themes_file = os.path.join(config_dir, "themes.json")
        self.current_theme_name = "light"
        
        # Carrega temas predefinidos
        self.themes = self._load_predefined_themes()
        
        # Carrega temas customizados
        self._load_custom_themes()
        
        # Define tema atual
        self.current_theme = self.themes[self.current_theme_name]
        
    def _load_predefined_themes(self) -> Dict[str, Theme]:
        """Carrega temas predefinidos"""
        themes = {}
        
        # TEMA LIGHT (Padrão)
        themes["light"] = Theme(
            name="Light",
            type=ThemeType.LIGHT,
            description="Tema claro padrão com cores suaves",
            colors=ColorScheme(
                primary="#0066CC",
                secondary="#666666", 
                accent="#FF6B35",
                success="#28A745",
                warning="#FFC107",
                error="#DC3545",
                info="#17A2B8",
                background="#FFFFFF",
                surface="#F8F9FA",
                border="#DEE2E6",
                text_primary="#212529",
                text_secondary="#6C757D",
                text_muted="#ADB5BD",
                code_bg="#F8F9FA",
                code_text="#E83E8C",
                highlight="#FFF3CD"
            ),
            fonts=FontConfig(
                size=FontSize.NORMAL,
                header_multiplier=1.2,
                code_font="Consolas, Monaco, 'Courier New'",
                ui_font="Segoe UI, Arial, sans-serif"
            ),
            use_colors=True,
            use_emojis=True,
            ascii_mode=False,
            border_style="═",
            separator_char="─",
            progress_chars=("█", "░")
        )
        
        # TEMA DARK
        themes["dark"] = Theme(
            name="Dark",
            type=ThemeType.DARK,
            description="Tema escuro para reduzir cansaço visual",
            colors=ColorScheme(
                primary="#61DAFB",
                secondary="#8B949E",
                accent="#F78166",
                success="#56D364",
                warning="#E3B341",
                error="#F85149",
                info="#58A6FF",
                background="#0D1117",
                surface="#161B22",
                border="#30363D",
                text_primary="#F0F6FC",
                text_secondary="#8B949E",
                text_muted="#656D76",
                code_bg="#161B22",
                code_text="#FF7B72",
                highlight="#1F2328"
            ),
            fonts=FontConfig(
                size=FontSize.NORMAL,
                header_multiplier=1.2,
                code_font="Fira Code, Consolas, monospace",
                ui_font="Segoe UI, Arial, sans-serif"
            ),
            use_colors=True,
            use_emojis=True,
            ascii_mode=False,
            border_style="═",
            separator_char="─",
            progress_chars=("█", "▓")
        )
        
        # TEMA HIGH CONTRAST
        themes["high_contrast"] = Theme(
            name="High Contrast",
            type=ThemeType.HIGH_CONTRAST,
            description="Alto contraste para melhor acessibilidade",
            colors=ColorScheme(
                primary="#FFFFFF",
                secondary="#CCCCCC",
                accent="#FFFF00",
                success="#00FF00",
                warning="#FFFF00",
                error="#FF0000",
                info="#00FFFF",
                background="#000000",
                surface="#111111",
                border="#FFFFFF",
                text_primary="#FFFFFF",
                text_secondary="#CCCCCC",
                text_muted="#888888",
                code_bg="#222222",
                code_text="#FFFF00",
                highlight="#333333"
            ),
            fonts=FontConfig(
                size=FontSize.LARGE,
                header_multiplier=1.5,
                code_font="Courier New, monospace",
                ui_font="Arial, sans-serif"
            ),
            use_colors=True,
            use_emojis=False,
            ascii_mode=True,
            border_style="=",
            separator_char="-",
            progress_chars=("#", "-")
        )
        
        # TEMA RETRO
        themes["retro"] = Theme(
            name="Retro",
            type=ThemeType.RETRO,
            description="Tema nostálgico inspirado em terminais antigos",
            colors=ColorScheme(
                primary="#00FF00",
                secondary="#00CC00",
                accent="#FFFF00",
                success="#00FF00",
                warning="#FFAA00",
                error="#FF0000",
                info="#00FFFF",
                background="#000000",
                surface="#001100",
                border="#00FF00",
                text_primary="#00FF00",
                text_secondary="#00CC00",
                text_muted="#006600",
                code_bg="#002200",
                code_text="#00FF00",
                highlight="#003300"
            ),
            fonts=FontConfig(
                size=FontSize.NORMAL,
                header_multiplier=1.3,
                code_font="Courier New, monospace",
                ui_font="Courier New, monospace"
            ),
            use_colors=True,
            use_emojis=False,
            ascii_mode=True,
            border_style="+",
            separator_char="-",
            progress_chars=("*", ".")
        )
        
        # TEMA MATRIX
        themes["matrix"] = Theme(
            name="Matrix",
            type=ThemeType.MATRIX,
            description="Tema inspirado no filme Matrix",
            colors=ColorScheme(
                primary="#00FF41",
                secondary="#008F11",
                accent="#00FF41",
                success="#00FF41",
                warning="#FFFF00",
                error="#FF0000",
                info="#00FFFF",
                background="#000000",
                surface="#001100",
                border="#00FF41",
                text_primary="#00FF41",
                text_secondary="#008F11",
                text_muted="#004411",
                code_bg="#001100",
                code_text="#00FF41",
                highlight="#002200"
            ),
            fonts=FontConfig(
                size=FontSize.NORMAL,
                header_multiplier=1.2,
                code_font="Courier New, monospace",
                ui_font="Courier New, monospace"
            ),
            use_colors=True,
            use_emojis=False,
            ascii_mode=True,
            border_style="=",
            separator_char="-",
            progress_chars=("█", "░")
        )
        
        return themes
        
    def _load_custom_themes(self):
        """Carrega temas customizados do arquivo"""
        if os.path.exists(self.themes_file):
            try:
                with open(self.themes_file, 'r', encoding='utf-8') as f:
                    custom_data = json.load(f)
                    
                # Converte dados JSON de volta para objetos Theme
                for name, theme_data in custom_data.items():
                    if name not in self.themes:  # Não sobrescreve predefinidos
                        self.themes[name] = self._dict_to_theme(theme_data)
                        
            except Exception as e:
                print(f"Erro ao carregar temas customizados: {e}")
                
    def _dict_to_theme(self, data: dict) -> Theme:
        """Converte dicionário para objeto Theme"""
        return Theme(
            name=data["name"],
            type=ThemeType(data["type"]),
            description=data["description"],
            colors=ColorScheme(**data["colors"]),
            fonts=FontConfig(
                size=FontSize(data["fonts"]["size"]),
                header_multiplier=data["fonts"]["header_multiplier"],
                code_font=data["fonts"]["code_font"],
                ui_font=data["fonts"]["ui_font"]
            ),
            use_colors=data["use_colors"],
            use_emojis=data["use_emojis"],
            ascii_mode=data["ascii_mode"],
            border_style=data["border_style"],
            separator_char=data["separator_char"],
            progress_chars=tuple(data["progress_chars"])
        )
        
    def save_custom_themes(self):
        """Salva temas customizados"""
        custom_themes = {
            name: asdict(theme) 
            for name, theme in self.themes.items() 
            if theme.type == ThemeType.CUSTOM
        }
        
        # Converte enums para strings
        for theme_data in custom_themes.values():
            theme_data["type"] = theme_data["type"].value if hasattr(theme_data["type"], 'value') else theme_data["type"]
            theme_data["fonts"]["size"] = theme_data["fonts"]["size"].value if hasattr(theme_data["fonts"]["size"], 'value') else theme_data["fonts"]["size"]
            
        try:
            with open(self.themes_file, 'w', encoding='utf-8') as f:
                json.dump(custom_themes, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar temas: {e}")
            
    def get_available_themes(self) -> List[str]:
        """Retorna lista de temas disponíveis"""
        return list(self.themes.keys())
        
    def get_theme_info(self, theme_name: str) -> Optional[Dict[str, Any]]:
        """Retorna informações sobre um tema"""
        if theme_name in self.themes:
            theme = self.themes[theme_name]
            return {
                "name": theme.name,
                "type": theme.type.value,
                "description": theme.description,
                "use_colors": theme.use_colors,
                "use_emojis": theme.use_emojis,
                "ascii_mode": theme.ascii_mode
            }
        return None
        
    def set_theme(self, theme_name: str) -> bool:
        """Define o tema atual"""
        if theme_name in self.themes:
            self.current_theme_name = theme_name
            self.current_theme = self.themes[theme_name]
            return True
        return False
        
    def get_current_theme(self) -> Theme:
        """Retorna o tema atual"""
        return self.current_theme
        
    def create_custom_theme(self, name: str, base_theme: str = "light") -> Optional[str]:
        """Cria um tema customizado baseado em outro"""
        if base_theme not in self.themes:
            return None
            
        # Cria cópia do tema base
        base = self.themes[base_theme]
        custom_theme = Theme(
            name=name,
            type=ThemeType.CUSTOM,
            description=f"Tema customizado baseado em {base.name}",
            colors=ColorScheme(**asdict(base.colors)),
            fonts=FontConfig(**asdict(base.fonts)),
            use_colors=base.use_colors,
            use_emojis=base.use_emojis,
            ascii_mode=base.ascii_mode,
            border_style=base.border_style,
            separator_char=base.separator_char,
            progress_chars=base.progress_chars
        )
        
        self.themes[name] = custom_theme
        return name
        
    def customize_theme_colors(self, theme_name: str, color_updates: Dict[str, str]) -> bool:
        """Customiza cores de um tema"""
        if theme_name not in self.themes:
            return False
            
        theme = self.themes[theme_name]
        
        # Atualiza cores válidas
        valid_colors = asdict(theme.colors).keys()
        for color_name, color_value in color_updates.items():
            if color_name in valid_colors:
                setattr(theme.colors, color_name, color_value)
                
        return True
        
    def set_font_size(self, theme_name: str, font_size: FontSize) -> bool:
        """Define tamanho da fonte para um tema"""
        if theme_name not in self.themes:
            return False
            
        self.themes[theme_name].fonts.size = font_size
        return True
        
    def toggle_emojis(self, theme_name: str) -> bool:
        """Alterna uso de emojis em um tema"""
        if theme_name not in self.themes:
            return False
            
        theme = self.themes[theme_name]
        theme.use_emojis = not theme.use_emojis
        theme.ascii_mode = not theme.use_emojis  # ASCII mode quando sem emojis
        return True
        
    def get_ansi_colors(self) -> Dict[str, str]:
        """Retorna cores ANSI do tema atual"""
        if not self.current_theme.use_colors:
            return {key: "" for key in asdict(self.current_theme.colors).keys()}
            
        # Mapeia cores hex para códigos ANSI (simplificado)
        color_map = {
            "primary": "\033[36m",      # Ciano
            "secondary": "\033[37m",    # Branco
            "accent": "\033[35m",       # Magenta
            "success": "\033[32m",      # Verde
            "warning": "\033[33m",      # Amarelo
            "error": "\033[31m",        # Vermelho
            "info": "\033[34m",         # Azul
            "text_primary": "\033[37m", # Branco
            "text_secondary": "\033[90m", # Cinza
            "reset": "\033[0m"          # Reset
        }
        
        return color_map