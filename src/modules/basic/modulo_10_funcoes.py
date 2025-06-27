#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 10: Funções
Aprenda a criar blocos de código reutilizáveis
"""

from ..shared.base_module import BaseModule


class Modulo10Funcoes(BaseModule):
    """Módulo 10: Funções"""
    
    def __init__(self):
        super().__init__("modulo_10", "Funções Reutilizáveis")
        self.has_mini_project = True
        self.mini_project_points = 70
    
    def execute(self) -> None:
        """Executa o módulo sobre funções"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._funcoes()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _funcoes(self) -> None:
        """Conteúdo principal sobre funções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚙️ MÓDULO 10: FUNÇÕES REUTILIZÁVEIS")
        else:
            print("\n" + "="*50)
            print("⚙️ MÓDULO 10: FUNÇÕES REUTILIZÁVEIS")
            print("="*50)
        
        self.print_concept("Funções são blocos de código que você pode usar várias vezes!")
        
        codigo = '''# Criando e usando funções
def saudacao(nome):
    """Função que saúda uma pessoa"""
    return f"Olá, {nome}! Bem-vindo ao Python!"

def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    area = largura * altura
    return area

# Usando as funções
mensagem = saudacao("Ana")
print(mensagem)

area = calcular_area_retangulo(5, 3)
print(f"Área do retângulo: {area}")

# Função com valor padrão
def apresentar(nome, idade=25):
    return f"{nome} tem {idade} anos"

print(apresentar("João"))
print(apresentar("Maria", 30))'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        # Mini Projeto
        self._mini_projeto_automacao()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_automacao(self) -> None:
        """Mini Projeto - Sistema de Automação Residencial"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: AUTOMAÇÃO RESIDENCIAL")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: AUTOMAÇÃO RESIDENCIAL")
            print("="*50)
        
        self.print_section("🏠 Vamos criar um sistema de automação residencial!")
        self.print_tip("Usado em: casas inteligentes, IoT, sistemas domóticos")
        
        codigo_projeto = '''# 🏠 SISTEMA DE AUTOMAÇÃO RESIDENCIAL
print("🏠 CENTRAL DE AUTOMAÇÃO RESIDENCIAL")
print("=" * 45)

# Estado inicial dos dispositivos
dispositivos = {
    "luzes_sala": False,
    "luzes_quarto": False,
    "ar_condicionado": False,
    "som": False,
    "cortinas": False,
    "temperatura": 22
}

def controlar_luz(ambiente, estado):
    """Controla as luzes de um ambiente"""
    chave = f"luzes_{ambiente}"
    if chave in dispositivos:
        dispositivos[chave] = estado
        status = "LIGADA" if estado else "DESLIGADA"
        return f"💡 Luz do {ambiente}: {status}"
    return f"❌ Ambiente {ambiente} não encontrado"

def controlar_ar_condicionado(temperatura=None):
    """Controla o ar condicionado"""
    if temperatura:
        dispositivos["temperatura"] = temperatura
        dispositivos["ar_condicionado"] = True
        return f"❄️ Ar condicionado LIGADO - {temperatura}°C"
    else:
        dispositivos["ar_condicionado"] = False
        return "❄️ Ar condicionado DESLIGADO"

def modo_cinema():
    """Ativa modo cinema (luzes apagadas, som ligado)"""
    dispositivos["luzes_sala"] = False
    dispositivos["luzes_quarto"] = False
    dispositivos["som"] = True
    dispositivos["cortinas"] = True
    return "🎬 MODO CINEMA ATIVADO"

def modo_dormir():
    """Ativa modo dormir (tudo desligado)"""
    dispositivos["luzes_sala"] = False
    dispositivos["luzes_quarto"] = False
    dispositivos["som"] = False
    dispositivos["ar_condicionado"] = False
    return "😴 MODO DORMIR ATIVADO"

def status_casa():
    """Mostra status completo da casa"""
    print("\\n🏠 STATUS DA CASA:")
    print("-" * 30)
    for dispositivo, estado in dispositivos.items():
        if dispositivo == "temperatura":
            print(f"🌡️ Temperatura: {estado}°C")
        else:
            status = "LIGADO" if estado else "DESLIGADO"
            emoji = "🟢" if estado else "🔴"
            nome = dispositivo.replace("_", " ").title()
            print(f"{emoji} {nome}: {status}")

# Demonstração do sistema
print("\\n🎮 DEMONSTRAÇÃO DO SISTEMA:")

# Status inicial
status_casa()

# Comandos de automação
print("\\n📱 EXECUTANDO COMANDOS:")
print("1.", controlar_luz("sala", True))
print("2.", controlar_luz("quarto", True))
print("3.", controlar_ar_condicionado(18))
print("4.", modo_cinema())

# Status após comandos
status_casa()

print("\\n5.", modo_dormir())
status_casa()

# Simulação de rotina matinal
print("\\n🌅 ROTINA MATINAL AUTOMÁTICA:")
dispositivos["luzes_quarto"] = True
dispositivos["cortinas"] = False
dispositivos["ar_condicionado"] = True
dispositivos["temperatura"] = 24
print("✅ Luzes do quarto ligadas")
print("✅ Cortinas abertas") 
print("✅ Temperatura ajustada para 24°C")

status_casa()
print("\\n🎉 SISTEMA DE AUTOMAÇÃO FUNCIONANDO!")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        self.print_success("\n🏆 CONQUISTA: Arquiteto de Automação!")
        self.complete_mini_project("Sistema de Automação Residencial")
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo10Funcoes()
    print("Teste do módulo 10 - versão standalone")
    module._funcoes()