#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 14: Módulos e Pacotes
Aprenda a organizar e reutilizar código com módulos e bibliotecas
"""

from ..shared.base_module import BaseModule


class Modulo14ModulosPacotes(BaseModule):
    """Módulo 14: Módulos e Pacotes - Organizando Código"""
    
    def __init__(self):
        super().__init__("modulo_14", "Módulos e Pacotes")
        self.has_mini_project = True
        self.mini_project_points = 80
    
    def execute(self) -> None:
        """Executa o módulo sobre módulos e pacotes"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._modulos_pacotes()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _modulos_pacotes(self) -> None:
        """Conteúdo principal sobre módulos e pacotes"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📦 MÓDULO 14: MÓDULOS E PACOTES")
        else:
            print("\n" + "="*50)
            print("📦 MÓDULO 14: MÓDULOS E PACOTES")
            print("="*50)
        
        print("📦 Agora vamos aprender a ORGANIZAR e REUTILIZAR código!")
        print("🔧 Módulos são a base da programação profissional!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO MÓDULOS?")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Módulo = arquivo .py com funções e classes")
        print("📚 Biblioteca = conjunto de módulos")
        print("🌟 Vantagens:")
        print("• ♻️  Reutilização de código")
        print("• 🗂️  Organização melhor")
        print("• 👥 Colaboração em equipe")
        print("• 🐛 Menos bugs")
        
        self.pausar()
        
        print("\n🔍 Importando Módulos:")
        
        codigo1 = '''# Diferentes formas de importar
import math
import random
import datetime

print("=== USANDO MÓDULO MATH ===")
print(f"Pi: {math.pi}")
print(f"Raiz quadrada de 16: {math.sqrt(16)}")
print(f"Seno de 90°: {math.sin(math.radians(90))}")
print(f"Logaritmo de 100: {math.log10(100)}")

print("\\n=== USANDO MÓDULO RANDOM ===")
print(f"Número aleatório 1-10: {random.randint(1, 10)}")
print(f"Número float aleatório: {random.random()}")

cores = ["vermelho", "azul", "verde", "amarelo"]
print(f"Cor aleatória: {random.choice(cores)}")

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista embaralhada: {numeros}")

print("\\n=== USANDO MÓDULO DATETIME ===")
agora = datetime.datetime.now()
print(f"Data e hora atual: {agora}")
print(f"Só a data: {agora.date()}")
print(f"Só a hora: {agora.time()}")
print(f"Formatado: {agora.strftime('%d/%m/%Y %H:%M')}")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n⚡ Importação Específica:")
        
        codigo2 = '''# Importando funções específicas
from math import pi, sqrt, sin, cos
from random import randint, choice
from datetime import datetime, date

print("=== IMPORT ESPECÍFICO ===")
print(f"Pi sem 'math.': {pi}")
print(f"Raiz sem 'math.': {sqrt(25)}")
print(f"Número aleatório: {randint(1, 100)}")

# Alias (apelidos) para módulos
print("\\n=== ALIASES COMUNS ===")
print("matplotlib.pyplot as plt - Gráficos")
print("pandas as pd - Análise de dados") 
print("numpy as np - Computação científica")

# From com alias
from datetime import datetime as dt
agora = dt.now()
print(f"\\nUsando alias: {agora}")

# Importando tudo (cuidado!)
from math import *
print(f"\\nTudo importado - pi: {pi}, e: {e}")
print("⚠️ Cuidado: pode sobrescrever variáveis!")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🔨 Criando Seus Próprios Módulos:")
        
        codigo3 = '''# Vamos criar funções que poderiam estar em um módulo separado
def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return imc, categoria

def converter_temperatura(temp, de, para):
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin"""
    # Primeiro converte tudo para Celsius
    if de == "F":
        celsius = (temp - 32) * 5/9
    elif de == "K":
        celsius = temp - 273.15
    else:
        celsius = temp
    
    # Depois converte para o destino
    if para == "F":
        return celsius * 9/5 + 32
    elif para == "K":
        return celsius + 273.15
    else:
        return celsius

def gerar_senha(tamanho=8):
    """Gera uma senha aleatória"""
    import random
    import string
    
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Constantes do módulo
PI = 3.14159
VERSAO = "1.0"

print("=== TESTANDO NOSSAS FUNÇÕES ===")
imc, categoria = calcular_imc(70, 1.75)
print(f"IMC: {imc:.1f} - {categoria}")

temp_f = converter_temperatura(25, "C", "F")
print(f"25°C = {temp_f:.1f}°F")

senha = gerar_senha(12)
print(f"Senha gerada: {senha}")

print(f"\\nVersão: {VERSAO}")
print(f"Valor de PI: {PI}")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.pausar()
        
        print("\n📚 Bibliotecas Úteis para Aprender:")
        
        codigo4 = '''# Principais bibliotecas Python
print("=== BIBLIOTECAS ESSENCIAIS ===")

libraries = {
    "Básicas (já instaladas)": [
        "os - Interação com sistema operacional",
        "sys - Configurações do sistema Python", 
        "json - Trabalhar com dados JSON",
        "re - Expressões regulares",
        "urllib - Requisições web básicas"
    ],
    "Análise de Dados": [
        "pandas - Manipulação de dados",
        "numpy - Computação numérica",
        "matplotlib - Gráficos e visualização",
        "seaborn - Gráficos estatísticos bonitos"
    ],
    "Web": [
        "requests - Requisições HTTP fáceis",
        "flask - Framework web simples",
        "django - Framework web completo",
        "beautifulsoup4 - Parsing de HTML"
    ],
    "Interface Gráfica": [
        "tkinter - Interface básica (já instalado)",
        "PyQt5/PySide2 - Interface profissional",
        "kivy - Apps mobile"
    ]
}

for categoria, libs in libraries.items():
    print(f"\\n🔹 {categoria}:")
    for lib in libs:
        print(f"  • {lib}")

print("\\n💡 DICA: Use 'pip install nome_biblioteca' para instalar!")
print("📖 Exemplo: pip install requests pandas matplotlib")'''
        
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        # Exercícios
        self.exercicio(
            "Como importar apenas a função sqrt do módulo math?",
            ["from math import sqrt"],
            "Use 'from modulo import funcao'"
        )
        
        self.exercicio(
            "Para que serve o comando 'pip install'?",
            ["instalar bibliotecas", "instalar pacotes", "instalar módulos"],
            "Instala bibliotecas externas no Python"
        )
        
        # Mini Projeto do Módulo 14
        self._mini_projeto_framework_plugins()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_framework_plugins(self) -> None:
        """Mini Projeto - Módulo 14: Framework de Plugins Modular"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: FRAMEWORK DE PLUGINS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: FRAMEWORK DE PLUGINS")
            print("="*50)
        
        print("🧩 Sistema completo de plugins modulares e extensíveis!")
        print("🛠️ Usando: Importação dinâmica, ABC, configuração, hooks")
        
        self.pausar()
        
        codigo_projeto = '''# 🧩 FRAMEWORK DE PLUGINS MODULAR
# Sistema profissional de plugins com importação dinâmica

import importlib
import json
import os
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime

# 1. CLASSE BASE ABSTRATA PARA PLUGINS
class PluginBase(ABC):
    """Classe base abstrata que todos os plugins devem herdar"""
    
    def __init__(self, name: str):
        self.name = name
        self.version = "1.0.0"
        self.enabled = True
        self.dependencies = []
        self.hooks = {}
    
    @abstractmethod
    def initialize(self) -> bool:
        """Inicializa o plugin - deve ser implementado"""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Executa a funcionalidade principal do plugin"""
        pass
    
    def cleanup(self) -> None:
        """Limpa recursos do plugin (opcional)"""
        pass
    
    def get_info(self) -> Dict[str, Any]:
        """Retorna informações do plugin"""
        return {
            "name": self.name,
            "version": self.version,
            "enabled": self.enabled,
            "dependencies": self.dependencies
        }

# 2. GERENCIADOR DE PLUGINS
class PluginManager:
    """Sistema central de gerenciamento de plugins"""
    
    def __init__(self):
        self.plugins: Dict[str, PluginBase] = {}
        self.loaded_modules = {}
        self.config = {}
        self.hooks: Dict[str, List[Callable]] = {}
    
    def discover_plugins(self, plugin_dir: str = "plugins") -> List[str]:
        """Descobre plugins disponíveis em um diretório"""
        discovered = []
        
        # Simula descoberta de plugins (normalmente seria em arquivos .py)
        plugin_classes = [
            ("calculator", CalculatorPlugin),
            ("text_generator", TextGeneratorPlugin),
            ("formatter", FormatterPlugin)
        ]
        
        for name, plugin_class in plugin_classes:
            try:
                # Simula carregamento dinâmico
                self.loaded_modules[name] = plugin_class
                discovered.append(name)
                print(f"✅ Plugin descoberto: {name}")
            except Exception as e:
                print(f"❌ Erro ao descobrir plugin {name}: {e}")
        
        return discovered
    
    def load_plugin(self, plugin_name: str) -> bool:
        """Carrega um plugin específico"""
        if plugin_name in self.plugins:
            print(f"⚠️ Plugin {plugin_name} já carregado")
            return True
        
        if plugin_name not in self.loaded_modules:
            print(f"❌ Plugin {plugin_name} não encontrado")
            return False
        
        try:
            # Instancia o plugin
            plugin_class = self.loaded_modules[plugin_name]
            plugin_instance = plugin_class(plugin_name)
            
            # Verifica dependências
            if not self._check_dependencies(plugin_instance):
                return False
            
            # Inicializa o plugin
            if plugin_instance.initialize():
                self.plugins[plugin_name] = plugin_instance
                self._register_hooks(plugin_instance)
                print(f"✅ Plugin {plugin_name} carregado com sucesso")
                return True
            else:
                print(f"❌ Falha na inicialização do plugin {plugin_name}")
                return False
        
        except Exception as e:
            print(f"❌ Erro ao carregar plugin {plugin_name}: {e}")
            return False
    
    def _check_dependencies(self, plugin: PluginBase) -> bool:
        """Verifica se as dependências do plugin estão satisfeitas"""
        for dep in plugin.dependencies:
            if dep not in self.plugins:
                print(f"⚠️ Dependência não satisfeita: {dep}")
                # Tenta carregar a dependência automaticamente
                if not self.load_plugin(dep):
                    return False
        return True
    
    def _register_hooks(self, plugin: PluginBase) -> None:
        """Registra hooks do plugin"""
        for hook_name, callback in plugin.hooks.items():
            if hook_name not in self.hooks:
                self.hooks[hook_name] = []
            self.hooks[hook_name].append(callback)
    
    def execute_plugin(self, plugin_name: str, *args, **kwargs) -> Any:
        """Executa um plugin específico"""
        if plugin_name not in self.plugins:
            print(f"❌ Plugin {plugin_name} não está carregado")
            return None
        
        plugin = self.plugins[plugin_name]
        if not plugin.enabled:
            print(f"⚠️ Plugin {plugin_name} está desabilitado")
            return None
        
        try:
            return plugin.execute(*args, **kwargs)
        except Exception as e:
            print(f"❌ Erro ao executar plugin {plugin_name}: {e}")
            return None
    
    def trigger_hook(self, hook_name: str, *args, **kwargs) -> List[Any]:
        """Dispara todos os callbacks de um hook específico"""
        results = []
        if hook_name in self.hooks:
            for callback in self.hooks[hook_name]:
                try:
                    result = callback(*args, **kwargs)
                    results.append(result)
                except Exception as e:
                    print(f"❌ Erro no hook {hook_name}: {e}")
        return results
    
    def list_plugins(self) -> Dict[str, Any]:
        """Lista todos os plugins carregados"""
        return {name: plugin.get_info() for name, plugin in self.plugins.items()}
    
    def save_config(self, filename: str = "plugins_config.json") -> None:
        """Salva configuração dos plugins"""
        config = {
            "plugins": {
                name: {
                    "enabled": plugin.enabled,
                    "version": plugin.version
                }
                for name, plugin in self.plugins.items()
            },
            "last_updated": datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"✅ Configuração salva em {filename}")
        except Exception as e:
            print(f"❌ Erro ao salvar configuração: {e}")

# 3. PLUGINS DE EXEMPLO

class CalculatorPlugin(PluginBase):
    """Plugin de calculadora com operações básicas"""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.version = "2.0.0"
        self.operations = {}
    
    def initialize(self) -> bool:
        """Inicializa operações da calculadora"""
        self.operations = {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "mul": lambda x, y: x * y,
            "div": lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
        }
        
        # Registra hook para logging
        self.hooks["calculation_done"] = self._log_calculation
        
        print(f"🧮 Calculadora inicializada com {len(self.operations)} operações")
        return True
    
    def execute(self, operation: str, x: float, y: float) -> Any:
        """Executa uma operação matemática"""
        if operation not in self.operations:
            return f"❌ Operação '{operation}' não suportada"
        
        result = self.operations[operation](x, y)
        
        # Dispara hook de log
        if hasattr(self, 'hooks') and 'calculation_done' in self.hooks:
            self.hooks['calculation_done'](operation, x, y, result)
        
        return result
    
    def _log_calculation(self, op: str, x: float, y: float, result: Any) -> None:
        """Log das operações realizadas"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"📊 [{timestamp}] {x} {op} {y} = {result}")

class TextGeneratorPlugin(PluginBase):
    """Plugin gerador de texto com templates"""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.version = "1.5.0"
        self.templates = {}
    
    def initialize(self) -> bool:
        """Inicializa templates de texto"""
        self.templates = {
            "email": "Olá {nome},\\n\\nEspero que esteja bem.\\n\\nAtenciosamente,\\n{remetente}",
            "carta": "Prezado(a) {destinatario},\\n\\n{conteudo}\\n\\nCordialmente,\\n{assinatura}",
            "relatorio": "RELATÓRIO: {titulo}\\n\\nData: {data}\\nAutor: {autor}\\n\\n{corpo}"
        }
        
        print(f"📝 Gerador de texto inicializado com {len(self.templates)} templates")
        return True
    
    def execute(self, template_name: str, **variables) -> str:
        """Gera texto a partir de um template"""
        if template_name not in self.templates:
            return f"❌ Template '{template_name}' não encontrado"
        
        try:
            template = self.templates[template_name]
            result = template.format(**variables)
            return result
        except KeyError as e:
            return f"❌ Variável necessária não fornecida: {e}"

class FormatterPlugin(PluginBase):
    """Plugin formatador de texto e dados"""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.version = "1.2.0"
        self.dependencies = ["text_generator"]  # Depende do gerador de texto
    
    def initialize(self) -> bool:
        """Inicializa formatadores"""
        print("🎨 Formatador de texto inicializado")
        return True
    
    def execute(self, text: str, format_type: str = "upper") -> str:
        """Formata texto de diferentes maneiras"""
        formatters = {
            "upper": text.upper,
            "lower": text.lower,
            "title": text.title,
            "reverse": lambda: text[::-1],
            "clean": lambda: " ".join(text.split())
        }
        
        if format_type not in formatters:
            return f"❌ Formato '{format_type}' não suportado"
        
        return formatters[format_type]()

# 4. DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE PLUGINS MODULAR ===\\n")

# Criar gerenciador
manager = PluginManager()

# Descobrir plugins disponíveis
print("🔍 DESCOBRINDO PLUGINS:")
discovered = manager.discover_plugins()

# Carregar plugins
print("\\n📦 CARREGANDO PLUGINS:")
for plugin_name in discovered:
    manager.load_plugin(plugin_name)

# Listar plugins carregados
print("\\n📋 PLUGINS CARREGADOS:")
plugins_info = manager.list_plugins()
for name, info in plugins_info.items():
    print(f"  • {name} v{info['version']} ({'✅' if info['enabled'] else '❌'})")

# Testar plugins
print("\\n🧮 TESTANDO CALCULADORA:")
result1 = manager.execute_plugin("calculator", "add", 15, 25)
print(f"Resultado: {result1}")

result2 = manager.execute_plugin("calculator", "div", 100, 4)
print(f"Resultado: {result2}")

print("\\n📝 TESTANDO GERADOR DE TEXTO:")
email = manager.execute_plugin("text_generator", "email", 
                              nome="João", remetente="Sistema")
print(f"Email gerado:\\n{email}")

print("\\n🎨 TESTANDO FORMATADOR:")
formatted = manager.execute_plugin("formatter", "Python é incrível!", "title")
print(f"Texto formatado: {formatted}")

# Salvar configuração
print("\\n💾 SALVANDO CONFIGURAÇÃO:")
manager.save_config()

print("\\n🎉 Framework de Plugins funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Importação dinâmica de módulos")
print("  • Classes abstratas (ABC)")
print("  • Sistema de hooks e eventos")
print("  • Gerenciamento de dependências")
print("  • Configuração persistente")
print("  • Arquitetura modular profissional")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Framework de plugins profissional criado!")
        print("🎯 Aplicação real: sistemas modulares, arquitetura de microserviços")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Framework de Plugins Modular")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo14ModulosPacotes()
    print("Teste do módulo 14 - versão standalone")
    module._modulos_pacotes()