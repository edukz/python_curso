#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Carregamento Dinâmico de Módulos
Carrega módulos sob demanda para melhor performance
"""

import importlib
import os
from typing import Dict, Any, Optional, Type
from pathlib import Path

from .shared.base_module import BaseModule


class ModuleLoader:
    """Carregador dinâmico de módulos do curso"""
    
    def __init__(self):
        self._loaded_modules: Dict[str, Type[BaseModule]] = {}
        self._module_cache: Dict[str, BaseModule] = {}
        self.base_path = Path(__file__).parent
        
        # Mapeamento de módulos para seus arquivos
        self._module_mapping = {
            # Módulos Básicos (1-11)
            "modulo_1": ("basic.modulo_01_introducao", "Modulo01Introducao"),
            "modulo_2": ("basic.modulo_02_primeiro_programa", "Modulo02PrimeiroPrograma"),
            "modulo_3": ("basic.modulo_03_variaveis", "Modulo03Variaveis"),
            "modulo_4": ("basic.modulo_04_tipos_dados", "Modulo04TiposDados"),
            "modulo_5": ("basic.modulo_05_entrada_dados", "Modulo05EntradaDados"),
            "modulo_6": ("basic.modulo_06_operacoes", "Modulo06Operacoes"),
            "modulo_7": ("basic.modulo_07_condicoes", "Modulo07Condicoes"),
            "modulo_8": ("basic.modulo_08_loops", "Modulo08Loops"),
            "modulo_9": ("basic.modulo_09_listas", "Modulo09Listas"),
            "modulo_10": ("basic.modulo_10_funcoes", "Modulo10Funcoes"),
            "modulo_11": ("basic.modulo_11_projeto_final", "Modulo11ProjetoFinal"),
            
            # Módulos Avançados (12-23)
            "modulo_12": ("advanced.modulo_12_dicionarios", "Modulo12Dicionarios"),
            "modulo_13": ("advanced.modulo_13_funcoes_avancadas", "Modulo13FuncoesAvancadas"),
            "modulo_14": ("advanced.modulo_14_modulos_pacotes", "Modulo14ModulosPacotes"),
            "modulo_15": ("advanced.modulo_15_datetime", "Modulo15Datetime"),
            "modulo_16": ("advanced.modulo_16_excecoes", "Modulo16Excecoes"),
            "modulo_17": ("advanced.modulo_17_json_csv", "Modulo17JsonCsv"),
            "modulo_18": ("advanced.modulo_18_oop_basico", "Modulo18OopBasico"),
            "modulo_19": ("advanced.modulo_19_oop_avancado", "Modulo19OopAvancado"),
            "modulo_20": ("advanced.modulo_20_decorators", "Modulo20Decorators"),
            "modulo_21": ("advanced.modulo_21_geradores", "Modulo21Geradores"),
            "modulo_22": ("advanced.modulo_22_regex", "Modulo22Regex"),
            "modulo_23": ("advanced.modulo_23_debugging", "Modulo23Debugging"),
            
            # Módulos Essenciais (24-30) - seguindo numeração do main.py
            "modulo_24": ("essential.modulo_24_git_github", "Modulo24GitGithub"),
            "modulo_25": ("essential.modulo_25_terminal_cli", "Modulo25TerminalCli"),
            "modulo_26": ("essential.modulo_26_ambientes_virtuais", "Modulo26AmbientesVirtuais"),
            "modulo_27": ("essential.modulo_27_testes_tdd", "Modulo27TestesTdd"),
            "modulo_28": ("essential.modulo_28_estrutura_projetos", "Modulo28EstruturaProjetos"),
            "modulo_29": ("essential.modulo_29_apis_web", "Modulo29ApisWeb"),
            "modulo_30": ("essential.modulo_30_seguranca", "Modulo30Seguranca"),
            
            # Módulos Enterprise (31-35) - Arquitetura e Padrões Avançados
            "modulo_31": ("enterprise.modulo_31_design_patterns", "Modulo31DesignPatterns"),
            "modulo_32": ("enterprise.modulo_32_clean_architecture", "Modulo32CleanArchitecture"),
            "modulo_33": ("enterprise.modulo_33_devops", "Modulo33DevOps"),
            "modulo_34": ("enterprise.modulo_34_database_design", "Modulo34DatabaseDesign"),
            "modulo_35": ("enterprise.modulo_35_capstone", "Modulo35Capstone"),
        }
    
    def get_module(self, module_id: str) -> Optional[BaseModule]:
        """
        Carrega e retorna instância do módulo
        
        Args:
            module_id: ID do módulo (ex: "modulo_1")
            
        Returns:
            Instância do módulo ou None se não encontrado
        """
        # Verifica cache primeiro
        if module_id in self._module_cache:
            return self._module_cache[module_id]
        
        # Carrega módulo se não estiver em cache
        module_class = self._load_module_class(module_id)
        if module_class:
            instance = module_class()
            self._module_cache[module_id] = instance
            return instance
        
        return None
    
    def _load_module_class(self, module_id: str) -> Optional[Type[BaseModule]]:
        """
        Carrega classe do módulo dinamicamente
        
        Args:
            module_id: ID do módulo
            
        Returns:
            Classe do módulo ou None se não encontrado
        """
        # Verifica se já foi carregado
        if module_id in self._loaded_modules:
            return self._loaded_modules[module_id]
        
        # Verifica se módulo existe no mapeamento
        if module_id not in self._module_mapping:
            print(f"⚠️ Módulo {module_id} não encontrado no mapeamento")
            return None
        
        module_path, class_name = self._module_mapping[module_id]
        
        try:
            # Importa o módulo dinamicamente
            full_module_path = f"src.modules.{module_path}"
            module = importlib.import_module(full_module_path)
            
            # Obtém a classe
            module_class = getattr(module, class_name)
            
            # Verifica se é subclasse de BaseModule
            if not issubclass(module_class, BaseModule):
                print(f"⚠️ {class_name} não é subclasse de BaseModule")
                return None
            
            # Armazena no cache
            self._loaded_modules[module_id] = module_class
            
            return module_class
            
        except ImportError as e:
            print(f"❌ Erro ao importar módulo {module_id}: {e}")
            return None
        except AttributeError as e:
            print(f"❌ Classe {class_name} não encontrada no módulo {module_path}: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado ao carregar módulo {module_id}: {e}")
            return None
    
    def preload_modules(self, module_ids: list[str]) -> None:
        """
        Pre-carrega módulos especificados
        
        Args:
            module_ids: Lista de IDs de módulos para pre-carregar
        """
        print(f"🔄 Pre-carregando {len(module_ids)} módulos...")
        
        for module_id in module_ids:
            try:
                self._load_module_class(module_id)
                print(f"✅ {module_id} carregado")
            except Exception as e:
                print(f"❌ Erro ao pre-carregar {module_id}: {e}")
    
    def unload_module(self, module_id: str) -> None:
        """
        Remove módulo do cache para liberar memória
        
        Args:
            module_id: ID do módulo para descarregar
        """
        if module_id in self._module_cache:
            del self._module_cache[module_id]
        
        if module_id in self._loaded_modules:
            del self._loaded_modules[module_id]
    
    def get_loaded_modules(self) -> list[str]:
        """
        Retorna lista de módulos carregados
        
        Returns:
            Lista de IDs de módulos carregados
        """
        return list(self._loaded_modules.keys())
    
    def get_cached_instances(self) -> list[str]:
        """
        Retorna lista de instâncias em cache
        
        Returns:
            Lista de IDs de módulos com instâncias em cache
        """
        return list(self._module_cache.keys())
    
    def clear_cache(self) -> None:
        """Limpa todo o cache de módulos"""
        self._module_cache.clear()
        self._loaded_modules.clear()
        print("🧹 Cache de módulos limpo")
    
    def get_module_info(self, module_id: str) -> Dict[str, Any]:
        """
        Retorna informações sobre um módulo
        
        Args:
            module_id: ID do módulo
            
        Returns:
            Dicionário com informações do módulo
        """
        info = {
            'id': module_id,
            'exists': module_id in self._module_mapping,
            'loaded': module_id in self._loaded_modules,
            'cached': module_id in self._module_cache,
        }
        
        if info['exists']:
            module_path, class_name = self._module_mapping[module_id]
            info.update({
                'path': module_path,
                'class_name': class_name,
                'file_path': str(self.base_path / (module_path.replace('.', '/') + '.py'))
            })
        
        return info
    
    def list_all_modules(self) -> Dict[str, Dict[str, Any]]:
        """
        Lista todos os módulos disponíveis
        
        Returns:
            Dicionário com informações de todos os módulos
        """
        return {
            module_id: self.get_module_info(module_id)
            for module_id in self._module_mapping.keys()
        }
    
    def health_check(self) -> Dict[str, Any]:
        """
        Verifica saúde do sistema de módulos
        
        Returns:
            Relatório de saúde
        """
        total_modules = len(self._module_mapping)
        loaded_count = len(self._loaded_modules)
        cached_count = len(self._module_cache)
        
        # Verifica se arquivos existem
        existing_files = 0
        missing_files = []
        
        for module_id, (module_path, class_name) in self._module_mapping.items():
            file_path = self.base_path / (module_path.replace('.', '/') + '.py')
            if file_path.exists():
                existing_files += 1
            else:
                missing_files.append(f"{module_id} -> {file_path}")
        
        return {
            'total_modules': total_modules,
            'loaded_modules': loaded_count,
            'cached_instances': cached_count,
            'existing_files': existing_files,
            'missing_files': missing_files,
            'memory_efficiency': f"{cached_count}/{total_modules} ({cached_count/total_modules*100:.1f}%)",
            'status': 'healthy' if len(missing_files) == 0 else 'warning'
        }


# Instância global do loader
module_loader = ModuleLoader()


# Funções de conveniência
def load_module(module_id: str) -> Optional[BaseModule]:
    """Função de conveniência para carregar módulo"""
    return module_loader.get_module(module_id)


def preload_basic_modules():
    """Pre-carrega módulos básicos"""
    basic_modules = [f"modulo_{i}" for i in range(1, 12)]
    module_loader.preload_modules(basic_modules)


def preload_project_modules():
    """Pre-carrega módulos de projetos"""
    project_modules = [f"modulo_{i}" for i in range(24, 27)]
    module_loader.preload_modules(project_modules)


def preload_essential_modules():
    """Pre-carrega módulos essenciais"""
    essential_modules = [f"modulo_{i}" for i in range(27, 31)]
    module_loader.preload_modules(essential_modules)


def preload_enterprise_modules():
    """Pre-carrega módulos enterprise"""
    enterprise_modules = [f"modulo_{i}" for i in range(31, 36)]
    module_loader.preload_modules(enterprise_modules)


def preload_all_modules():
    """Pre-carrega todos os módulos do curso"""
    all_modules = [f"modulo_{i}" for i in range(1, 36)]
    module_loader.preload_modules(all_modules)