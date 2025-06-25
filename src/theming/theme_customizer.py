#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Theme Customizer - Interface para personalização de temas
"""

import re
from typing import Dict, List, Optional, Tuple
from .theme_manager import AdvancedThemeManager, FontSize, ThemeType


class ThemeCustomizer:
    """Interface para customização de temas"""
    
    def __init__(self, theme_manager: AdvancedThemeManager, ui_components):
        self.theme_manager = theme_manager
        self.ui = ui_components
        
    def show_theme_menu(self):
        """Mostra menu principal de temas"""
        while True:
            self.ui.clear_screen()
            self._display_current_theme_info()
            
            print("\n🎨 MENU DE PERSONALIZAÇÃO:")
            print("1. 🎯 Escolher Tema Predefinido")
            print("2. 🎨 Customizar Cores")
            print("3. 📝 Configurar Fonte")
            print("4. 🎭 Criar Tema Personalizado")
            print("5. 👁️ Prévia de Temas")
            print("6. 📊 Comparar Temas")
            print("7. 💾 Salvar Configurações")
            print("0. 🔙 Voltar")
            
            choice = input("\n👉 Escolha uma opção: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._theme_selector()
            elif choice == "2":
                self._color_customizer()
            elif choice == "3":
                self._font_configurator()
            elif choice == "4":
                self._create_custom_theme()
            elif choice == "5":
                self._theme_preview()
            elif choice == "6":
                self._theme_comparison()
            elif choice == "7":
                self._save_settings()
            else:
                self.ui.error("Opção inválida!")
                self.ui.pause()
                
    def _display_current_theme_info(self):
        """Exibe informações do tema atual"""
        theme = self.theme_manager.get_current_theme()
        
        self.ui.header("🎨 PERSONALIZAÇÃO DE TEMAS", f"Tema Atual: {theme.name}")
        
        print(f"\n📝 Descrição: {theme.description}")
        print(f"🎭 Tipo: {theme.type.value.title()}")
        print(f"🌈 Cores: {'Ativadas' if theme.use_colors else 'Desativadas'}")
        print(f"😊 Emojis: {'Ativados' if theme.use_emojis else 'Desativados'}")
        print(f"📐 Modo ASCII: {'Ativo' if theme.ascii_mode else 'Inativo'}")
        print(f"📝 Tamanho da Fonte: {theme.fonts.size.value.title()}")
        
    def _theme_selector(self):
        """Seletor de temas predefinidos"""
        self.ui.clear_screen()
        self.ui.header("🎯 SELEÇÃO DE TEMA", "Escolha um tema predefinido")
        
        themes = self.theme_manager.get_available_themes()
        predefined_themes = [name for name in themes 
                           if self.theme_manager.themes[name].type != ThemeType.CUSTOM]
        
        print("\n🎭 TEMAS DISPONÍVEIS:")
        for i, theme_name in enumerate(predefined_themes, 1):
            theme_info = self.theme_manager.get_theme_info(theme_name)
            current = "👉 " if theme_name == self.theme_manager.current_theme_name else "   "
            print(f"{current}{i}. {theme_info['name']} - {theme_info['description']}")
            
        print("0. 🔙 Voltar")
        
        try:
            choice = int(input("\n👉 Escolha um tema: "))
            if 1 <= choice <= len(predefined_themes):
                theme_name = predefined_themes[choice - 1]
                self.theme_manager.set_theme(theme_name)
                self.ui.success(f"✅ Tema '{theme_name}' ativado!")
        except ValueError:
            pass
            
        self.ui.pause()
        
    def _color_customizer(self):
        """Customizador de cores"""
        self.ui.clear_screen()
        self.ui.header("🎨 CUSTOMIZAÇÃO DE CORES", "Personalize as cores do tema")
        
        theme = self.theme_manager.get_current_theme()
        
        print("\n🌈 CORES DISPONÍVEIS PARA CUSTOMIZAÇÃO:")
        color_options = [
            ("primary", "Cor principal (títulos)"),
            ("secondary", "Cor secundária (subtítulos)"),
            ("accent", "Cor de destaque"),
            ("success", "Cor de sucesso"),
            ("warning", "Cor de aviso"),
            ("error", "Cor de erro"),
            ("background", "Cor de fundo"),
            ("text_primary", "Cor do texto principal")
        ]
        
        for i, (key, desc) in enumerate(color_options, 1):
            current_color = getattr(theme.colors, key)
            print(f"{i}. {desc}: {current_color}")
            
        print("9. 🎨 Preset de Cores Rápido")
        print("0. 🔙 Voltar")
        
        try:
            choice = int(input("\n👉 Escolha uma cor para customizar: "))
            
            if choice == 9:
                self._color_presets()
            elif 1 <= choice <= len(color_options):
                color_key, desc = color_options[choice - 1]
                self._edit_single_color(color_key, desc)
        except ValueError:
            pass
            
        self.ui.pause()
        
    def _edit_single_color(self, color_key: str, description: str):
        """Edita uma cor específica"""
        theme = self.theme_manager.get_current_theme()
        current_color = getattr(theme.colors, color_key)
        
        print(f"\n✏️ EDITANDO: {description}")
        print(f"Cor atual: {current_color}")
        print("\n💡 FORMATOS ACEITOS:")
        print("  • Hex: #FF0000, #ff0000")
        print("  • RGB: rgb(255, 0, 0)")
        print("  • Nome: red, blue, green")
        
        new_color = input(f"\n👉 Nova cor para {description}: ").strip()
        
        if self._validate_color(new_color):
            color_updates = {color_key: new_color}
            if self.theme_manager.customize_theme_colors(
                self.theme_manager.current_theme_name, color_updates):
                self.ui.success(f"✅ Cor {description} atualizada!")
            else:
                self.ui.error("❌ Erro ao atualizar cor!")
        else:
            self.ui.error("❌ Formato de cor inválido!")
            
    def _color_presets(self):
        """Presets de cores rápidos"""
        self.ui.clear_screen()
        self.ui.header("🎨 PRESETS DE CORES", "Esquemas prontos")
        
        presets = {
            "1": {
                "name": "🔥 Sunset",
                "colors": {
                    "primary": "#FF6B35",
                    "secondary": "#F7931E", 
                    "accent": "#FFD23F",
                    "success": "#06D6A0"
                }
            },
            "2": {
                "name": "🌊 Ocean",
                "colors": {
                    "primary": "#006BA6",
                    "secondary": "#0496FF",
                    "accent": "#FFBC42",
                    "success": "#06D6A0"
                }
            },
            "3": {
                "name": "🌸 Sakura",
                "colors": {
                    "primary": "#FF69B4",
                    "secondary": "#FFB6C1",
                    "accent": "#98FB98",
                    "success": "#32CD32"
                }
            },
            "4": {
                "name": "🍃 Nature",
                "colors": {
                    "primary": "#2D5A27",
                    "secondary": "#40916C",
                    "accent": "#95D5B2",
                    "success": "#52B788"
                }
            }
        }
        
        print("\n🎨 PRESETS DISPONÍVEIS:")
        for key, preset in presets.items():
            print(f"{key}. {preset['name']}")
            
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha um preset: ").strip()
        
        if choice in presets:
            if self.theme_manager.customize_theme_colors(
                self.theme_manager.current_theme_name, presets[choice]["colors"]):
                self.ui.success(f"✅ Preset {presets[choice]['name']} aplicado!")
            else:
                self.ui.error("❌ Erro ao aplicar preset!")
        
    def _font_configurator(self):
        """Configurador de fontes"""
        self.ui.clear_screen()
        self.ui.header("📝 CONFIGURAÇÃO DE FONTE", "Ajuste tamanho e família")
        
        theme = self.theme_manager.get_current_theme()
        
        print(f"\n📏 TAMANHO ATUAL: {theme.fonts.size.value.title()}")
        print("\n📐 TAMANHOS DISPONÍVEIS:")
        
        font_sizes = list(FontSize)
        for i, size in enumerate(font_sizes, 1):
            current = "👉 " if size == theme.fonts.size else "   "
            print(f"{current}{i}. {size.value.title()}")
            
        print("\n🎛️ OUTRAS OPÇÕES:")
        print("5. 👁️ Prévia de Tamanhos")
        print("6. 🔤 Configurações Avançadas")
        print("0. 🔙 Voltar")
        
        try:
            choice = int(input("\n👉 Escolha: "))
            
            if 1 <= choice <= len(font_sizes):
                new_size = font_sizes[choice - 1]
                self.theme_manager.set_font_size(
                    self.theme_manager.current_theme_name, new_size)
                self.ui.success(f"✅ Tamanho da fonte alterado para {new_size.value.title()}!")
                
            elif choice == 5:
                self._font_size_preview()
            elif choice == 6:
                self._advanced_font_settings()
                
        except ValueError:
            pass
            
        self.ui.pause()
        
    def _font_size_preview(self):
        """Prévia dos tamanhos de fonte"""
        self.ui.clear_screen()
        self.ui.header("👁️ PRÉVIA DE TAMANHOS", "Como ficará cada tamanho")
        
        samples = {
            FontSize.SMALL: {
                "header": "🐍 Python Course - Small",
                "text": "Este é um exemplo de texto no tamanho pequeno.",
                "code": "print('Hello, World!')"
            },
            FontSize.NORMAL: {
                "header": "🐍 Python Course - Normal",
                "text": "Este é um exemplo de texto no tamanho normal.",
                "code": "print('Hello, World!')"
            },
            FontSize.LARGE: {
                "header": "🐍 Python Course - Large",
                "text": "Este é um exemplo de texto no tamanho grande.",
                "code": "print('Hello, World!')"
            },
            FontSize.EXTRA_LARGE: {
                "header": "🐍 Python Course - Extra Large",
                "text": "Este é um exemplo de texto no tamanho extra grande.",
                "code": "print('Hello, World!')"
            }
        }
        
        for size, sample in samples.items():
            print(f"\n{'='*20} {size.value.upper()} {'='*20}")
            print(sample['header'])
            print(sample['text'])
            print(f"Código: {sample['code']}")
            
        self.ui.pause()
        
    def _advanced_font_settings(self):
        """Configurações avançadas de fonte"""
        self.ui.clear_screen()
        self.ui.header("🔤 CONFIGURAÇÕES AVANÇADAS", "Ajustes detalhados")
        
        theme = self.theme_manager.get_current_theme()
        
        print(f"\n📊 CONFIGURAÇÕES ATUAIS:")
        print(f"• Multiplicador de cabeçalho: {theme.fonts.header_multiplier}")
        print(f"• Fonte de código: {theme.fonts.code_font}")
        print(f"• Fonte da interface: {theme.fonts.ui_font}")
        
        print(f"\n🎛️ AJUSTES:")
        print("1. 📏 Ajustar multiplicador de cabeçalho")
        print("2. 💻 Escolher fonte de código")
        print("3. 🖥️ Escolher fonte da interface")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            try:
                new_mult = float(input("Novo multiplicador (ex: 1.5): "))
                if 0.8 <= new_mult <= 3.0:
                    theme.fonts.header_multiplier = new_mult
                    self.ui.success("✅ Multiplicador atualizado!")
                else:
                    self.ui.error("❌ Valor deve estar entre 0.8 e 3.0")
            except ValueError:
                self.ui.error("❌ Valor inválido!")
                
        elif choice == "2":
            fonts = [
                "Fira Code, monospace",
                "Consolas, monospace", 
                "Monaco, monospace",
                "Courier New, monospace",
                "Source Code Pro, monospace"
            ]
            
            print("\n💻 FONTES DE CÓDIGO:")
            for i, font in enumerate(fonts, 1):
                print(f"{i}. {font}")
                
            try:
                font_choice = int(input("\n👉 Escolha: "))
                if 1 <= font_choice <= len(fonts):
                    theme.fonts.code_font = fonts[font_choice - 1]
                    self.ui.success("✅ Fonte de código atualizada!")
            except ValueError:
                pass
                
        self.ui.pause()
        
    def _create_custom_theme(self):
        """Cria tema personalizado"""
        self.ui.clear_screen()
        self.ui.header("🎭 CRIAR TEMA PERSONALIZADO", "Seu tema único")
        
        print("📝 INFORMAÇÕES DO TEMA:")
        name = input("Nome do tema: ").strip()
        
        if not name:
            self.ui.error("❌ Nome é obrigatório!")
            self.ui.pause()
            return
            
        if name in self.theme_manager.themes:
            self.ui.error("❌ Tema já existe!")
            self.ui.pause()
            return
            
        print("\n🎨 TEMA BASE:")
        base_themes = ["light", "dark", "high_contrast", "retro", "matrix"]
        
        for i, theme in enumerate(base_themes, 1):
            info = self.theme_manager.get_theme_info(theme)
            print(f"{i}. {info['name']} - {info['description']}")
            
        try:
            base_choice = int(input("\n👉 Escolha tema base: "))
            if 1 <= base_choice <= len(base_themes):
                base_theme = base_themes[base_choice - 1]
                
                # Cria tema personalizado
                custom_name = self.theme_manager.create_custom_theme(name, base_theme)
                if custom_name:
                    self.theme_manager.set_theme(custom_name)
                    self.ui.success(f"✅ Tema '{name}' criado e ativado!")
                    
                    # Oferece customização imediata
                    if input("\n🎨 Customizar agora? (s/n): ").lower() == 's':
                        self._color_customizer()
                else:
                    self.ui.error("❌ Erro ao criar tema!")
                    
        except ValueError:
            self.ui.error("❌ Opção inválida!")
            
        self.ui.pause()
        
    def _theme_preview(self):
        """Prévia de todos os temas"""
        self.ui.clear_screen()
        self.ui.header("👁️ PRÉVIA DE TEMAS", "Veja como cada tema fica")
        
        themes = self.theme_manager.get_available_themes()
        current_theme = self.theme_manager.current_theme_name
        
        for theme_name in themes:
            # Temporariamente muda tema para prévia
            self.theme_manager.set_theme(theme_name)
            theme = self.theme_manager.get_current_theme()
            
            print(f"\n{'='*50}")
            print(f"🎭 TEMA: {theme.name}")
            print(f"📝 {theme.description}")
            
            # Simula elementos da interface
            print(f"✅ Sucesso: Operação concluída")
            print(f"⚠️ Aviso: Atenção necessária") 
            print(f"❌ Erro: Algo deu errado")
            print(f"ℹ️ Info: Informação importante")
            print(f"💻 Código: print('Hello, World!')")
            
        # Restaura tema original
        self.theme_manager.set_theme(current_theme)
        
        self.ui.pause()
        
    def _theme_comparison(self):
        """Comparação entre temas"""
        self.ui.clear_screen()
        self.ui.header("📊 COMPARAÇÃO DE TEMAS", "Compare características")
        
        themes = self.theme_manager.get_available_themes()
        
        print("\n📋 TABELA COMPARATIVA:")
        print(f"{'Tema':<15} {'Tipo':<12} {'Cores':<6} {'Emojis':<6} {'ASCII':<5}")
        print("-" * 50)
        
        for theme_name in themes:
            info = self.theme_manager.get_theme_info(theme_name)
            current = "👉" if theme_name == self.theme_manager.current_theme_name else "  "
            
            print(f"{current} {info['name']:<13} {info['type']:<12} "
                  f"{'✓' if info['use_colors'] else '✗':<6} "
                  f"{'✓' if info['use_emojis'] else '✗':<6} "
                  f"{'✓' if info['ascii_mode'] else '✗':<5}")
                  
        self.ui.pause()
        
    def _save_settings(self):
        """Salva configurações"""
        self.ui.clear_screen()
        self.ui.header("💾 SALVAR CONFIGURAÇÕES", "Persistir alterações")
        
        print("💾 Salvando temas customizados...")
        self.theme_manager.save_custom_themes()
        
        print("✅ Configurações salvas com sucesso!")
        print("\n📝 As seguintes configurações foram salvas:")
        print(f"• Tema atual: {self.theme_manager.current_theme_name}")
        print(f"• Temas customizados preservados")
        
        self.ui.pause()
        
    def _validate_color(self, color: str) -> bool:
        """Valida formato de cor"""
        color = color.strip()
        
        # Hex colors
        if re.match(r'^#[0-9A-Fa-f]{6}$', color):
            return True
            
        # RGB colors
        if re.match(r'^rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)$', color):
            return True
            
        # Named colors (básico)
        named_colors = [
            'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 
            'white', 'black', 'gray', 'orange', 'purple', 'pink'
        ]
        
        if color.lower() in named_colors:
            return True
            
        return False