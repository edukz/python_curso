#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Glossário de Termos Python
Fornece definições e exemplos de termos importantes
"""

import json
import os
from typing import Dict, List, Optional, Any
from .utils import PythonCourseUtils
from .visual_feedback import VisualFeedback


class Glossary:
    """Gerencia o glossário de termos Python"""
    
    def __init__(self, glossary_file: str = "glossary.json"):
        self.glossary_file = glossary_file
        self.utils = PythonCourseUtils()
        self.visual = VisualFeedback()
        self.terms = self._load_glossary()
    
    def _load_glossary(self) -> Dict[str, Any]:
        """Carrega o glossário do arquivo JSON"""
        if os.path.exists(self.glossary_file):
            try:
                with open(self.glossary_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('termos', {})
            except (json.JSONDecodeError, IOError) as e:
                print(f"Erro ao carregar glossário: {e}")
                return {}
        return {}
    
    def show_glossary_menu(self) -> None:
        """Exibe o menu principal do glossário"""
        while True:
            self.utils.limpar_tela()
            self.utils.titulo("📖 GLOSSÁRIO DE TERMOS PYTHON")
            
            print("1. Buscar termo específico")
            print("2. Listar todos os termos")
            print("3. Termos por módulo")
            print("4. Termo aleatório")
            print("0. Voltar ao menu principal")
            
            try:
                choice = input("\n👉 Escolha uma opção: ").strip()
            except KeyboardInterrupt:
                break  # Sai do menu do glossário
            
            if choice == '0':
                break
            elif choice == '1':
                self._search_term()
            elif choice == '2':
                self._list_all_terms()
            elif choice == '3':
                self._terms_by_module()
            elif choice == '4':
                self._random_term()
            else:
                print("❌ Opção inválida!")
                self.utils.pausar()
    
    def _search_term(self) -> None:
        """Busca um termo específico"""
        self.utils.limpar_tela()
        self.utils.titulo("🔍 BUSCAR TERMO")
        
        try:
            search = input("Digite o termo que deseja buscar: ").strip().lower()
        except KeyboardInterrupt:
            return
        
        if search in self.terms:
            self._display_term(search, self.terms[search])
        else:
            # Busca parcial
            matches = [term for term in self.terms if search in term]
            
            if matches:
                print(f"\n📝 Termos encontrados com '{search}':")
                for i, term in enumerate(matches, 1):
                    print(f"{i}. {term}")
                
                if len(matches) == 1:
                    self._display_term(matches[0], self.terms[matches[0]])
                else:
                    try:
                        choice = input("\n👉 Escolha um número ou 0 para voltar: ").strip()
                    except KeyboardInterrupt:
                        return
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(matches):
                            self._display_term(matches[idx], self.terms[matches[idx]])
                    except ValueError:
                        pass
            else:
                print(f"\n❌ Nenhum termo encontrado com '{search}'")
                self.utils.pausar()
    
    def _display_term(self, term: str, info: Dict[str, Any]) -> None:
        """Exibe informações detalhadas de um termo"""
        self.utils.limpar_tela()
        self.visual.typing_effect(f"📚 {term.upper()}", 0.05)
        print("=" * 50)
        
        print(f"\n📖 Definição:")
        print(f"   {info['definicao']}")
        
        print(f"\n💡 Exemplo:")
        self.utils.exemplo(info['exemplo'])
        
        if 'modulos_relacionados' in info:
            modules = info['modulos_relacionados']
            module_nums = [m.split('_')[1] for m in modules]
            print(f"\n📌 Módulos relacionados: {', '.join(module_nums)}")
        
        self.utils.pausar()
    
    def _list_all_terms(self) -> None:
        """Lista todos os termos do glossário"""
        self.utils.limpar_tela()
        self.utils.titulo("📋 TODOS OS TERMOS")
        
        sorted_terms = sorted(self.terms.keys())
        columns = 3
        terms_per_column = len(sorted_terms) // columns + 1
        
        # Exibe em colunas
        for i in range(terms_per_column):
            row = ""
            for j in range(columns):
                idx = i + j * terms_per_column
                if idx < len(sorted_terms):
                    row += f"{sorted_terms[idx]:<25}"
            print(row)
        
        print(f"\n📊 Total de termos: {len(sorted_terms)}")
        
        try:
            search = input("\n👉 Digite um termo para ver detalhes (ou Enter para voltar): ").strip().lower()
        except KeyboardInterrupt:
            return
        if search in self.terms:
            self._display_term(search, self.terms[search])
    
    def _terms_by_module(self) -> None:
        """Organiza termos por módulo"""
        self.utils.limpar_tela()
        self.utils.titulo("📚 TERMOS POR MÓDULO")
        
        # Organiza termos por módulo
        by_module = {}
        for term, info in self.terms.items():
            for module in info.get('modulos_relacionados', []):
                if module not in by_module:
                    by_module[module] = []
                by_module[module].append(term)
        
        # Exibe por módulo
        for module in sorted(by_module.keys()):
            module_num = module.split('_')[1]
            print(f"\n📖 Módulo {module_num}:")
            for term in sorted(by_module[module]):
                print(f"   • {term}")
        
        self.utils.pausar()
    
    def _random_term(self) -> None:
        """Exibe um termo aleatório"""
        import random
        
        if not self.terms:
            print("❌ Glossário vazio!")
            self.utils.pausar()
            return
        
        term = random.choice(list(self.terms.keys()))
        
        self.utils.limpar_tela()
        print("🎲 TERMO ALEATÓRIO")
        print("=" * 50)
        
        self.visual.countdown(3, "Sorteando termo em")
        
        self._display_term(term, self.terms[term])
    
    def get_term(self, term: str) -> Optional[Dict[str, Any]]:
        """Retorna informações de um termo específico"""
        return self.terms.get(term.lower())
    
    def get_terms_for_module(self, module_id: str) -> List[str]:
        """Retorna lista de termos relacionados a um módulo"""
        related_terms = []
        for term, info in self.terms.items():
            if module_id in info.get('modulos_relacionados', []):
                related_terms.append(term)
        return sorted(related_terms)
    
    def add_term(self, term: str, definition: str, example: str, 
                 related_modules: List[str]) -> None:
        """Adiciona um novo termo ao glossário"""
        self.terms[term.lower()] = {
            "definicao": definition,
            "exemplo": example,
            "modulos_relacionados": related_modules
        }
        self._save_glossary()
    
    def _save_glossary(self) -> None:
        """Salva o glossário no arquivo JSON"""
        try:
            with open(self.glossary_file, 'w', encoding='utf-8') as f:
                json.dump({"termos": self.terms}, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Erro ao salvar glossário: {e}")
    
    def search_definition(self, text: str) -> List[str]:
        """Busca termos que contenham o texto na definição"""
        matches = []
        text_lower = text.lower()
        
        for term, info in self.terms.items():
            if text_lower in info['definicao'].lower():
                matches.append(term)
        
        return matches