#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 31: Design Patterns & SOLID Principles
Aprenda padrões de design e princípios fundamentais para código limpo e escalável
"""

from typing import Dict, List, Optional, Any, Protocol
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from ..shared.base_module import BaseModule


class Modulo31DesignPatterns(BaseModule):
    """Módulo 31: Design Patterns & SOLID Principles - Arquitetura de Software Profissional"""
    
    def __init__(self):
        super().__init__("modulo_31", "Design Patterns & SOLID Principles")
        self.has_mini_project = True
        self.mini_project_points = 150  # Pontuação alta para módulo avançado
    
    def execute(self) -> None:
        """Executa o módulo Design Patterns & SOLID Principles"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._design_patterns_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _design_patterns_principal(self) -> None:
        """Conteúdo principal do módulo Design Patterns & SOLID Principles"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 31: DESIGN PATTERNS & SOLID PRINCIPLES")
        else:
            print("\n" + "="*50)
            print("🏗️ MÓDULO 31: DESIGN PATTERNS & SOLID PRINCIPLES")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🏗️ Bem-vindo ao mundo da arquitetura de software profissional! Vamos construir código como os grandes mestres!")
        self.print_tip("Este módulo está dividido em seções interativas. Você controla o ritmo!")
        
        # === FLUXO PRINCIPAL COM TRATAMENTO DE CTRL+C ===
        
        # 1. Sistema de navegação por seções
        try:
            self._navegacao_secoes_interativas()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Navegação interrompida pelo usuário. Voltando ao menu principal...")
            return
        
        # 2. Seção de Prática Interativa
        try:
            self._secao_pratica_interativa()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Módulo interrompido pelo usuário. Voltando ao menu principal...")
            return
        
        # 3. Mini Projeto Prático
        try:
            self._mini_projeto_ecommerce_patterns()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return
        
        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""
        
        # === DEFINIÇÃO DAS SEÇÕES ===
        secoes = [
            {
                'id': 'secao_conceitos_fundamentais',
                'titulo': '🎯 O que são Design Patterns?',
                'descricao': 'Entenda os padrões que revolucionaram a programação',
                'funcao': self._secao_conceitos_fundamentais
            },
            {
                'id': 'secao_solid_principles',
                'titulo': '🏛️ Princípios SOLID',
                'descricao': 'Os 5 pilares do código limpo e profissional',
                'funcao': self._secao_solid_principles
            },
            {
                'id': 'secao_creational_patterns',
                'titulo': '🏭 Padrões Criacionais',
                'descricao': 'Factory, Builder, Singleton - criando objetos elegantemente',
                'funcao': self._secao_creational_patterns
            },
            {
                'id': 'secao_behavioral_patterns',
                'titulo': '🎭 Padrões Comportamentais',
                'descricao': 'Strategy, Observer, Command - controlando comportamentos',
                'funcao': self._secao_behavioral_patterns
            },
            {
                'id': 'secao_structural_patterns',
                'titulo': '🏗️ Padrões Estruturais',
                'descricao': 'Adapter, Decorator, Facade - organizando estruturas',
                'funcao': self._secao_structural_patterns
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas de arquitetura',
                'descricao': 'Dicas dos mestres da engenharia de software',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre arquitetura',
                'descricao': 'Histórias e fatos fascinantes do mundo do software',
                'funcao': self._secao_curiosidades
            }
        ]
        
        secoes_visitadas = set()
        
        # === LOOP PRINCIPAL DE NAVEGAÇÃO ===
        while True:
            # Limpa tela e mostra cabeçalho
            self.ui.clear_screen() if self.ui else print("\n" + "="*50)
            self.print_section("NAVEGAÇÃO DO MÓDULO", "📚", "accent")
            self.print_colored("Escolha uma seção para estudar:", "text")
            
            # Lista todas as seções com status
            print()
            for i, secao in enumerate(secoes, 1):
                status = "✅" if secao['id'] in secoes_visitadas else "📖"
                print(f"{status} {i}. {secao['titulo']}")
                self.print_colored(f"    {secao['descricao']}", "text")
                print()
            
            print("0. 🎯 Continuar para os Exercícios Práticos")
            
            # Mostra progresso visual
            progresso = len(secoes_visitadas)
            total = len(secoes)
            self.print_colored(f"\n📊 Progresso: {progresso}/{total} seções visitadas", "info")
            
            if progresso == total:
                self.print_success("🌟 Você completou todas as seções! Está pronto para praticar!")
            
            # Processa escolha do usuário
            try:
                escolha = input(f"\n👉 Escolha uma seção (1-{len(secoes)}) ou 0 para continuar: ").strip()
                
                if escolha == "0":
                    # Verifica se visitou seções suficientes
                    if progresso >= 3:  # Pelo menos 3 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 3 seções antes de continuar!")
                        continuar = input("Quer continuar mesmo assim? (s/n): ").lower()
                        if continuar in ['s', 'sim', 'yes']:
                            break
                elif escolha.isdigit() and 1 <= int(escolha) <= len(secoes):
                    # Executa seção escolhida
                    idx = int(escolha) - 1
                    secoes[idx]['funcao']()
                    secoes_visitadas.add(secoes[idx]['id'])
                else:
                    self.print_warning(f"❌ Opção inválida! Digite um número de 1 a {len(secoes)} ou 0.")
                    
            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Pulando para exercícios práticos...")
                break
            except Exception as e:
                self.print_warning(f"❌ Erro: {str(e)}. Tente novamente.")
    
    def _secao_conceitos_fundamentais(self) -> None:
        """Seção: O que são Design Patterns?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO DESIGN PATTERNS?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Design Patterns",
            "São soluções reutilizáveis para problemas comuns no design de software. São como receitas testadas por milhões de programadores ao longo de décadas."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Design Patterns não são código pronto, são conceitos que você adapta para seu problema!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como plantas de uma casa: você não copia exatamente a casa do vizinho, mas usa a mesma planta (padrão) e adapta para seu terreno e necessidades!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 OS 3 TIPOS DE DESIGN PATTERNS:", "info")
        tipos = [
            "1. 🏭 CRIACIONAIS - Como criar objetos de forma inteligente",
            "2. 🏗️ ESTRUTURAIS - Como organizar e compor objetos",
            "3. 🎭 COMPORTAMENTAIS - Como objetos interagem e se comportam"
        ]
        
        for i, tipo in enumerate(tipos, 1):
            self.print_colored(tipo, "text")
            if i < len(tipos):
                input("   ⏳ Pressione ENTER para o próximo tipo...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO: PADRÃO STRATEGY", "success")
        codigo_strategy = r'''# Padrão Strategy - Diferentes formas de calcular desconto
from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoVIP(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.8  # 20% desconto

class DescontoEstudante(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.9  # 10% desconto

class DescontoNormal(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.95  # 5% desconto

class Pedido:
    def __init__(self, valor, desconto_strategy):
        self.valor = valor
        self.desconto_strategy = desconto_strategy
    
    def valor_final(self):
        return self.desconto_strategy.calcular(self.valor)

# Usando o padrão
pedido_vip = Pedido(100, DescontoVIP())
pedido_estudante = Pedido(100, DescontoEstudante())

print(f"Pedido VIP: R$ {pedido_vip.valor_final()}")
print(f"Pedido Estudante: R$ {pedido_estudante.valor_final()}")'''
        
        self.exemplo(codigo_strategy)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_strategy)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏢 Netflix - Strategy para diferentes algoritmos de recomendação",
            "🚗 Uber - Factory para criar diferentes tipos de viagem",
            "📱 Instagram - Observer para notificar curtidas e comentários",
            "🛒 Amazon - Builder para construir pedidos complexos",
            "🎮 Games - Command para sistema de undo/redo",
            "🏦 Bancos - Adapter para integrar sistemas legados"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_solid_principles(self) -> None:
        """Seção: Princípios SOLID"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PRINCÍPIOS SOLID", "🏛️", "success")
        
        # === CONCEITO PRINCIPAL ===
        self.print_concept(
            "Princípios SOLID",
            "São 5 princípios fundamentais para escrever código orientado a objetos que é fácil de manter, estender e entender."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("SOLID é como as regras de engenharia civil: seguindo esses princípios, você constrói software que não desaba quando precisa fazer mudanças!", "text")
        input("\n🔸 Pressione ENTER para ver cada princípio...")
        
        # === OS 5 PRINCÍPIOS ===
        principios = [
            {
                'letra': 'S',
                'nome': 'Single Responsibility',
                'explicacao': 'Cada classe deve ter apenas uma razão para mudar',
                'exemplo': 'Uma classe User só cuida de dados do usuário, não de email ou banco de dados'
            },
            {
                'letra': 'O', 
                'nome': 'Open/Closed',
                'explicacao': 'Aberto para extensão, fechado para modificação',
                'exemplo': 'Adicione novos tipos de desconto sem modificar código existente'
            },
            {
                'letra': 'L',
                'nome': 'Liskov Substitution',
                'explicacao': 'Subclasses devem poder substituir suas classes pai',
                'exemplo': 'Se espera um Animal, pode receber Cachorro ou Gato sem problemas'
            },
            {
                'letra': 'I',
                'nome': 'Interface Segregation',
                'explicacao': 'Muitas interfaces específicas são melhores que uma geral',
                'exemplo': 'Interface Voador separada de Interface Nadador'
            },
            {
                'letra': 'D',
                'nome': 'Dependency Inversion',
                'explicacao': 'Dependa de abstrações, não de implementações concretas',
                'exemplo': 'Use interface EmailSender, não classe GmailSender diretamente'
            }
        ]
        
        for i, principio in enumerate(principios, 1):
            self.print_colored(f"\n{principio['letra']} - {principio['nome'].upper()}", "warning")
            self.print_colored(f"📝 {principio['explicacao']}", "text")
            self.print_colored(f"💡 Exemplo: {principio['exemplo']}", "info")
            
            if i < len(principios):
                input("   ⏳ Pressione ENTER para o próximo princípio...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO: VIOLANDO vs SEGUINDO SOLID", "success")
        codigo_solid = r'''# ❌ VIOLANDO SOLID
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def salvar_no_banco(self):  # Viola S - múltiplas responsabilidades
        print("Salvando no banco...")
    
    def enviar_email(self):  # Viola S - múltiplas responsabilidades
        print("Enviando email...")

# ✅ SEGUINDO SOLID
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class UsuarioRepository:  # S - Apenas uma responsabilidade
    def salvar(self, usuario):
        print(f"Salvando {usuario.nome} no banco...")

class EmailService:  # S - Apenas uma responsabilidade
    def enviar(self, email, mensagem):
        print(f"Enviando email para {email}: {mensagem}")

# Uso
usuario = Usuario("João", "joao@email.com")
repo = UsuarioRepository()
email_service = EmailService()

repo.salvar(usuario)
email_service.enviar(usuario.email, "Bem-vindo!")'''
        
        self.exemplo(codigo_solid)
        print("\n🚀 Executando comparação:")
        self.executar_codigo(codigo_solid)
        
        # === BENEFÍCIOS ===
        self.print_colored("\n🌟 BENEFÍCIOS DO SOLID:", "accent")
        beneficios = [
            "🧪 Código mais testável",
            "🔧 Fácil manutenção",
            "📈 Escalabilidade melhorada", 
            "🔄 Reutilização de código",
            "🐛 Menos bugs",
            "👥 Melhor trabalho em equipe"
        ]
        for beneficio in beneficios:
            self.print_colored(f"• {beneficio}", "primary")
        
        self.pausar()
    
    def _secao_creational_patterns(self) -> None:
        """Seção: Padrões Criacionais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PADRÕES CRIACIONAIS", "🏭", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Padrões Criacionais",
            "Focam em como criar objetos de forma flexível e reutilizável, escondendo a complexidade da criação e tornando o sistema independente de como os objetos são criados."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como diferentes tipos de fábrica: uma fábrica de carros, uma de bicicletas, uma de aviões. Cada uma sabe criar seu produto de forma especializada!", "text")
        input("\n🔸 Pressione ENTER para ver os padrões...")
        
        # === EXEMPLO 1: FACTORY ===
        self.print_colored("\n💻 EXEMPLO 1: FACTORY PATTERN", "success")
        codigo_factory = r'''# Factory Pattern - Criando diferentes tipos de animais
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Vaca(Animal):
    def fazer_som(self):
        return "Muuu!"

class AnimalFactory:
    @staticmethod
    def criar_animal(tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
        elif tipo == "vaca":
            return Vaca()
        else:
            raise ValueError(f"Animal {tipo} não existe!")

# Usando a factory
factory = AnimalFactory()
animais = ["cachorro", "gato", "vaca"]

for tipo in animais:
    animal = factory.criar_animal(tipo)
    print(f"{tipo.capitalize()}: {animal.fazer_som()}")'''
        
        self.exemplo(codigo_factory)
        print("\n🚀 Executando Factory:")
        self.executar_codigo(codigo_factory)
        
        input("\n🔸 Pressione ENTER para o próximo padrão...")
        
        # === EXEMPLO 2: BUILDER ===
        self.print_colored("\n💻 EXEMPLO 2: BUILDER PATTERN", "success")
        codigo_builder = r'''# Builder Pattern - Construindo hambúrguers personalizados
class Hamburguer:
    def __init__(self):
        self.ingredientes = []
    
    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
    
    def __str__(self):
        return f"Hambúrguer com: {', '.join(self.ingredientes)}"

class HamburguerBuilder:
    def __init__(self):
        self.hamburguer = Hamburguer()
    
    def adicionar_pao(self):
        self.hamburguer.adicionar_ingrediente("Pão")
        return self
    
    def adicionar_carne(self):
        self.hamburguer.adicionar_ingrediente("Carne")
        return self
    
    def adicionar_queijo(self):
        self.hamburguer.adicionar_ingrediente("Queijo")
        return self
    
    def adicionar_alface(self):
        self.hamburguer.adicionar_ingrediente("Alface")
        return self
    
    def adicionar_tomate(self):
        self.hamburguer.adicionar_ingrediente("Tomate")
        return self
    
    def build(self):
        return self.hamburguer

# Usando o builder
builder = HamburguerBuilder()

# Hambúrguer simples
simples = (builder
           .adicionar_pao()
           .adicionar_carne()
           .build())

# Hambúrguer completo (novo builder)
builder = HamburguerBuilder()
completo = (builder
            .adicionar_pao()
            .adicionar_carne()
            .adicionar_queijo()
            .adicionar_alface()
            .adicionar_tomate()
            .build())

print(f"Simples: {simples}")
print(f"Completo: {completo}")'''
        
        self.exemplo(codigo_builder)
        print("\n🚀 Executando Builder:")
        self.executar_codigo(codigo_builder)
        
        input("\n🔸 Pressione ENTER para o próximo padrão...")
        
        # === EXEMPLO 3: SINGLETON ===
        self.print_colored("\n💻 EXEMPLO 3: SINGLETON PATTERN", "success")
        codigo_singleton = r'''# Singleton Pattern - Apenas uma instância
class ConfiguracaoApp:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.configurado = False
        return cls._instancia
    
    def configurar(self, tema, idioma):
        self.tema = tema
        self.idioma = idioma
        self.configurado = True
    
    def obter_config(self):
        if not self.configurado:
            return "App não configurado ainda"
        return f"Tema: {self.tema}, Idioma: {self.idioma}"

# Testando Singleton
config1 = ConfiguracaoApp()
config2 = ConfiguracaoApp()

print(f"São a mesma instância? {config1 is config2}")

config1.configurar("Escuro", "Português")
print(f"Config1: {config1.obter_config()}")
print(f"Config2: {config2.obter_config()}")'''
        
        self.exemplo(codigo_singleton)
        print("\n🚀 Executando Singleton:")
        self.executar_codigo(codigo_singleton)
        
        # === APLICAÇÕES ===
        self.print_colored("\n🌍 ONDE USAR CADA PADRÃO:", "accent")
        usos = [
            "🏭 Factory - Quando não sabe exatamente qual objeto criar",
            "🔨 Builder - Para objetos complexos com muitos parâmetros",
            "👑 Singleton - Para recursos únicos (banco de dados, logger)",
            "🏗️ Abstract Factory - Para famílias de objetos relacionados",
            "📋 Prototype - Para clonar objetos caros de criar"
        ]
        for uso in usos:
            self.print_colored(f"• {uso}", "primary")
        
        self.pausar()
    
    def _secao_behavioral_patterns(self) -> None:
        """Seção: Padrões Comportamentais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PADRÕES COMPORTAMENTAIS", "🎭", "accent")
        
        # === CONCEITO ===
        self.print_concept(
            "Padrões Comportamentais",
            "Focam na comunicação entre objetos e na atribuição de responsabilidades, definindo como objetos interagem e distribuem trabalho."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como o protocolo em diferentes situações sociais: como se comportar em um casamento, em uma reunião de trabalho, ou em uma festa. Cada situação tem suas regras!", "text")
        input("\n🔸 Pressione ENTER para ver os padrões...")
        
        # === EXEMPLO 1: OBSERVER ===
        self.print_colored("\n💻 EXEMPLO 1: OBSERVER PATTERN", "success")
        codigo_observer = r'''# Observer Pattern - Sistema de notificações
class CanalYouTube:
    def __init__(self, nome):
        self.nome = nome
        self.inscritos = []
    
    def inscrever(self, usuario):
        self.inscritos.append(usuario)
        print(f"{usuario.nome} se inscreveu no canal {self.nome}")
    
    def desinscrever(self, usuario):
        if usuario in self.inscritos:
            self.inscritos.remove(usuario)
            print(f"{usuario.nome} se desinscreveu do canal {self.nome}")
    
    def postar_video(self, titulo):
        print(f"\n🎬 {self.nome} postou: '{titulo}'")
        for inscrito in self.inscritos:
            inscrito.notificar(self.nome, titulo)

class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def notificar(self, canal, video):
        print(f"📱 {self.nome} recebeu: Novo vídeo '{video}' no canal {canal}")

# Usando Observer
canal = CanalYouTube("TechMaster")
user1 = Usuario("Ana")
user2 = Usuario("Carlos")
user3 = Usuario("Beatriz")

canal.inscrever(user1)
canal.inscrever(user2)
canal.inscrever(user3)

canal.postar_video("Como usar Design Patterns em Python")

canal.desinscrever(user2)
canal.postar_video("SOLID Principles explicado")'''
        
        self.exemplo(codigo_observer)
        print("\n🚀 Executando Observer:")
        self.executar_codigo(codigo_observer)
        
        input("\n🔸 Pressione ENTER para o próximo padrão...")
        
        # === EXEMPLO 2: COMMAND ===
        self.print_colored("\n💻 EXEMPLO 2: COMMAND PATTERN", "success")
        codigo_command = r'''# Command Pattern - Sistema de comandos com undo
class Luz:
    def __init__(self):
        self.ligada = False
    
    def ligar(self):
        self.ligada = True
        print("💡 Luz ligada")
    
    def desligar(self):
        self.ligada = False
        print("🌙 Luz desligada")

class Comando:
    def executar(self):
        pass
    
    def desfazer(self):
        pass

class ComandoLigarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    
    def executar(self):
        self.luz.ligar()
    
    def desfazer(self):
        self.luz.desligar()

class ComandoDesligarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    
    def executar(self):
        self.luz.desligar()
    
    def desfazer(self):
        self.luz.ligar()

class ControleRemoto:
    def __init__(self):
        self.historico = []
    
    def executar_comando(self, comando):
        comando.executar()
        self.historico.append(comando)
    
    def desfazer_ultimo(self):
        if self.historico:
            ultimo_comando = self.historico.pop()
            ultimo_comando.desfazer()
            print("⏪ Comando desfeito")

# Usando Command
luz = Luz()
controle = ControleRemoto()

ligar = ComandoLigarLuz(luz)
desligar = ComandoDesligarLuz(luz)

controle.executar_comando(ligar)
controle.executar_comando(desligar)
controle.executar_comando(ligar)

print("\nDesfazendo comandos:")
controle.desfazer_ultimo()
controle.desfazer_ultimo()'''
        
        self.exemplo(codigo_command)
        print("\n🚀 Executando Command:")
        self.executar_codigo(codigo_command)
        
        # === OUTROS PADRÕES ===
        self.print_colored("\n🎭 OUTROS PADRÕES COMPORTAMENTAIS:", "info")
        outros_padroes = [
            "🔄 Strategy - Diferentes algoritmos intercambiáveis",
            "🎪 State - Objeto muda comportamento baseado no estado",
            "📝 Template Method - Esqueleto de algoritmo com passos customizáveis",
            "🚶 Iterator - Percorrer coleções sem expor estrutura interna",
            "🔗 Chain of Responsibility - Cadeia de handlers para processar request"
        ]
        for padrao in outros_padroes:
            self.print_colored(f"• {padrao}", "text")
        
        self.pausar()
    
    def _secao_structural_patterns(self) -> None:
        """Seção: Padrões Estruturais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PADRÕES ESTRUTURAIS", "🏗️", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Padrões Estruturais",
            "Lidam com a composição de classes e objetos, formando estruturas maiores enquanto mantêm flexibilidade e eficiência."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como um arquiteto que precisa conectar partes diferentes de um prédio: elevadores, escadas, pontes, adaptadores para conectar prédios antigos com novos!", "text")
        input("\n🔸 Pressione ENTER para ver os padrões...")
        
        # === EXEMPLO 1: ADAPTER ===
        self.print_colored("\n💻 EXEMPLO 1: ADAPTER PATTERN", "success")
        codigo_adapter = r'''# Adapter Pattern - Adaptando interfaces incompatíveis
class SistemaAntigo:
    def operacao_legada(self):
        return "Dados do sistema antigo"

class SistemaNovo:
    def operacao_moderna(self):
        return "Dados do sistema novo"

class AdapterSistemaAntigo:
    def __init__(self, sistema_antigo):
        self.sistema_antigo = sistema_antigo
    
    def operacao_moderna(self):
        # Adapta a interface antiga para a nova
        dados_antigos = self.sistema_antigo.operacao_legada()
        return f"Adaptado: {dados_antigos}"

class Cliente:
    def processar_dados(self, sistema):
        return sistema.operacao_moderna()

# Usando Adapter
sistema_novo = SistemaNovo()
sistema_antigo = SistemaAntigo()
adapter = AdapterSistemaAntigo(sistema_antigo)

cliente = Cliente()

print("Sistema novo:", cliente.processar_dados(sistema_novo))
print("Sistema antigo (via adapter):", cliente.processar_dados(adapter))'''
        
        self.exemplo(codigo_adapter)
        print("\n🚀 Executando Adapter:")
        self.executar_codigo(codigo_adapter)
        
        input("\n🔸 Pressione ENTER para o próximo padrão...")
        
        # === EXEMPLO 2: DECORATOR ===
        self.print_colored("\n💻 EXEMPLO 2: DECORATOR PATTERN", "success")
        codigo_decorator = r'''# Decorator Pattern - Adicionando funcionalidades dinamicamente
class Cafe:
    def custo(self):
        return 5.0
    
    def descricao(self):
        return "Café simples"

class DecoradorCafe:
    def __init__(self, cafe):
        self.cafe = cafe
    
    def custo(self):
        return self.cafe.custo()
    
    def descricao(self):
        return self.cafe.descricao()

class Leite(DecoradorCafe):
    def custo(self):
        return self.cafe.custo() + 2.0
    
    def descricao(self):
        return self.cafe.descricao() + " + Leite"

class Acucar(DecoradorCafe):
    def custo(self):
        return self.cafe.custo() + 0.5
    
    def descricao(self):
        return self.cafe.descricao() + " + Açúcar"

class Chocolate(DecoradorCafe):
    def custo(self):
        return self.cafe.custo() + 3.0
    
    def descricao(self):
        return self.cafe.descricao() + " + Chocolate"

# Usando Decorator
cafe = Cafe()
print(f"{cafe.descricao()} = R$ {cafe.custo()}")

cafe_com_leite = Leite(cafe)
print(f"{cafe_com_leite.descricao()} = R$ {cafe_com_leite.custo()}")

cafe_especial = Chocolate(Acucar(Leite(Cafe())))
print(f"{cafe_especial.descricao()} = R$ {cafe_especial.custo()}")'''
        
        self.exemplo(codigo_decorator)
        print("\n🚀 Executando Decorator:")
        self.executar_codigo(codigo_decorator)
        
        input("\n🔸 Pressione ENTER para o próximo padrão...")
        
        # === EXEMPLO 3: FACADE ===
        self.print_colored("\n💻 EXEMPLO 3: FACADE PATTERN", "success")
        codigo_facade = r'''# Facade Pattern - Interface simplificada para sistema complexo
class SistemaAudio:
    def ligar(self):
        print("🎵 Sistema de áudio ligado")
    
    def ajustar_volume(self, volume):
        print(f"🔊 Volume ajustado para {volume}")

class SistemaVideo:
    def ligar(self):
        print("📺 Sistema de vídeo ligado")
    
    def ajustar_resolucao(self, resolucao):
        print(f"🎬 Resolução ajustada para {resolucao}")

class SistemaLuzes:
    def diminuir(self):
        print("💡 Luzes diminuídas")
    
    def desligar(self):
        print("🌙 Luzes desligadas")

class Pipoca:
    def fazer(self):
        print("🍿 Fazendo pipoca...")

# Facade para simplificar
class HomeTheaterFacade:
    def __init__(self):
        self.audio = SistemaAudio()
        self.video = SistemaVideo()
        self.luzes = SistemaLuzes()
        self.pipoca = Pipoca()
    
    def assistir_filme(self):
        print("🎬 Preparando para assistir filme...\n")
        self.pipoca.fazer()
        self.luzes.diminuir()
        self.audio.ligar()
        self.audio.ajustar_volume(70)
        self.video.ligar()
        self.video.ajustar_resolucao("4K")
        print("\n🎉 Pronto! Pode assistir o filme!")
    
    def finalizar_filme(self):
        print("\n📺 Finalizando sessão...")
        self.luzes.desligar()
        print("💤 Boa noite!")

# Usando Facade
home_theater = HomeTheaterFacade()
home_theater.assistir_filme()
home_theater.finalizar_filme()'''
        
        self.exemplo(codigo_facade)
        print("\n🚀 Executando Facade:")
        self.executar_codigo(codigo_facade)
        
        # === BENEFÍCIOS ===
        self.print_colored("\n🌟 BENEFÍCIOS DOS PADRÕES ESTRUTURAIS:", "accent")
        beneficios = [
            "🔧 Adapter - Integra sistemas incompatíveis",
            "🎨 Decorator - Adiciona funcionalidades sem modificar código",
            "🎭 Facade - Simplifica interfaces complexas",
            "🌉 Bridge - Separa abstração de implementação",
            "🍃 Flyweight - Otimiza uso de memória",
            "🔗 Composite - Trata objetos individuais e compostos uniformemente"
        ]
        for beneficio in beneficios:
            self.print_colored(f"• {beneficio}", "primary")
        
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas de arquitetura"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS DE ARQUITETURA", "⭐", "success")
        
        self.print_colored("🏆 AS 10 REGRAS DE OURO DA ARQUITETURA:", "accent")
        
        praticas = [
            {
                'titulo': '1. 🎯 KISS - Keep It Simple, Stupid',
                'descricao': 'Prefira soluções simples sobre complexas',
                'exemplo': 'Use uma função simples antes de criar um padrão complexo'
            },
            {
                'titulo': '2. 🔄 DRY - Don\'t Repeat Yourself',
                'descricao': 'Evite duplicação de código e lógica',
                'exemplo': 'Crie uma função/classe em vez de copiar código'
            },
            {
                'titulo': '3. 📐 YAGNI - You Ain\'t Gonna Need It',
                'descricao': 'Não implemente funcionalidades que talvez precise',
                'exemplo': 'Foque no que precisa agora, não no que pode precisar'
            },
            {
                'titulo': '4. 🏗️ Separation of Concerns',
                'descricao': 'Separe responsabilidades diferentes',
                'exemplo': 'UI, lógica de negócio e banco de dados em camadas separadas'
            },
            {
                'titulo': '5. 🔍 Composition over Inheritance',
                'descricao': 'Prefira composição a herança quando possível',
                'exemplo': 'Use Strategy em vez de subclasses para diferentes comportamentos'
            },
            {
                'titulo': '6. 🎭 Program to Interfaces',
                'descricao': 'Dependa de abstrações, não de implementações',
                'exemplo': 'Use ABC e protocols em vez de classes concretas'
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{pratica['titulo']}", "warning")
            self.print_colored(f"📝 {pratica['descricao']}", "text")
            self.print_colored(f"💡 Exemplo: {pratica['exemplo']}", "info")
            
            if i < len(praticas):
                input("   ⏳ Pressione ENTER para a próxima prática...")
        
        # === QUANDO USAR DESIGN PATTERNS ===
        self.print_colored("\n\n🤔 QUANDO USAR DESIGN PATTERNS:", "accent")
        quando_usar = [
            "✅ Quando você tem um problema recorrente",
            "✅ Quando precisa de flexibilidade para futuras mudanças",
            "✅ Quando a equipe conhece os padrões",
            "✅ Quando o código ficará mais limpo e organizado",
            "❌ Não use apenas para 'parecer profissional'",
            "❌ Não use se adiciona complexidade desnecessária",
            "❌ Não force padrões onde uma solução simples funciona"
        ]
        
        for item in quando_usar:
            self.print_colored(f"  {item}", "text")
        
        # === ANTI-PATTERNS COMUNS ===
        self.print_colored("\n\n🚨 ANTI-PATTERNS PARA EVITAR:", "error")
        anti_patterns = [
            "💀 God Object - Classe que faz tudo",
            "🍝 Spaghetti Code - Código sem estrutura",
            "📚 Lava Flow - Código que ninguém mexe por medo",
            "🔁 Copy-Paste Programming - Duplicação excessiva",
            "🎯 Premature Optimization - Otimizar muito cedo",
            "🏗️ Over-Engineering - Complicar desnecessariamente"
        ]
        
        for anti in anti_patterns:
            self.print_colored(f"• {anti}", "text")
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre arquitetura"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES FASCINANTES", "💫", "accent")
        
        curiosidades = [
            {
                'titulo': '📚 A Origem dos Design Patterns',
                'historia': 'Os Design Patterns foram inspirados no trabalho do arquiteto Christopher Alexander sobre padrões na arquitetura física. A famosa "Gang of Four" (GoF) adaptou esses conceitos para software no livro de 1994 que se tornou a bíblia dos padrões.'
            },
            {
                'titulo': '🏗️ SOLID: Mais que Princípios',
                'historia': 'O acrônimo SOLID foi criado por Michael Feathers, mas os princípios foram desenvolvidos por Robert "Uncle Bob" Martin. Eles são tão fundamentais que empresas como Google, Netflix e Microsoft os usam como base para code reviews.'
            },
            {
                'titulo': '🎮 Padrões em Games',
                'historia': 'A indústria de games é pioneira no uso de Design Patterns! Command para undo/redo, Observer para eventos, State para IA de NPCs, e Factory para spawnar inimigos. Minecraft usa praticamente todos os padrões clássicos!'
            },
            {
                'titulo': '🚀 Netflix e Microservices',
                'historia': 'A Netflix revolucionou a arquitetura de software com microservices, usando intensivamente padrões como Circuit Breaker, Bulkhead, e Saga. Eles processam 1 bilhão de horas de vídeo por semana usando esses princípios!'
            },
            {
                'titulo': '🧠 Padrões Psicológicos',
                'historia': 'Design Patterns não são apenas código - são padrões de pensamento! Estudos mostram que programadores que conhecem padrões resolvem problemas 40% mais rápido e cometem 60% menos bugs.'
            },
            {
                'titulo': '🏢 Amazon e Single Responsibility',
                'historia': 'Jeff Bezos criou a regra das "duas pizzas": se uma equipe não pode ser alimentada com duas pizzas, ela é grande demais. Isso reflete o Single Responsibility Principle: cada equipe (como cada classe) deve ter uma responsabilidade bem definida.'
            }
        ]
        
        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n{curiosidade['titulo']}", "warning")
            self.print_colored(curiosidade['historia'], "text")
            
            if i < len(curiosidades):
                input("   🔸 Pressione ENTER para a próxima curiosidade...")
        
        # === FATOS IMPRESSIONANTES ===
        self.print_colored("\n\n🤯 FATOS QUE VÃO TE SURPREENDER:", "info")
        fatos = [
            "🎯 23 padrões originais da GoF ainda são usados 30 anos depois",
            "🌍 Python implementa Observer nativamente (property decorators)",
            "🏭 Django usa praticamente todos os padrões estruturais",
            "🔄 React é baseado em Observer + Component patterns",
            "📱 iOS e Android têm arquiteturas baseadas em MVC/MVP/MVVM",
            "🤖 IA moderna usa Factory para criar diferentes tipos de redes neurais"
        ]
        
        for fato in fatos:
            self.print_colored(f"• {fato}", "primary")
        
        self.print_success("\n🌟 Agora você faz parte da elite de arquitetos de software!")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre Design Patterns e SOLID!", "text")
        
        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")
        
        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Conhecimentos sobre Design Patterns & SOLID',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual princípio SOLID diz que cada classe deve ter apenas uma responsabilidade?',
                        'answer': ['single responsibility', 'srp', 's'],
                        'hint': 'É o primeiro princípio do SOLID, representado pela letra S'
                    },
                    {
                        'question': 'Que padrão é usado para criar objetos sem especificar sua classe exata?',
                        'answer': ['factory', 'factory pattern', 'factory method'],
                        'hint': 'Pense em uma fábrica que produz diferentes tipos de produtos'
                    },
                    {
                        'question': 'Qual padrão permite adicionar funcionalidades a um objeto dinamicamente?',
                        'answer': ['decorator', 'decorator pattern'],
                        'hint': 'É como decorar um bolo - você adiciona camadas sem mudar o bolo original'
                    },
                    {
                        'question': 'Que padrão notifica múltiplos objetos sobre mudanças em outro objeto?',
                        'answer': ['observer', 'observer pattern'],
                        'hint': 'É como uma lista de inscritos que são notificados sobre novos vídeos'
                    },
                    {
                        'question': 'Qual princípio SOLID diz para depender de abstrações, não de implementações?',
                        'answer': ['dependency inversion', 'dip', 'd'],
                        'hint': 'É o último princípio do SOLID, sobre inverter dependências'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código com Padrões',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o padrão Singleton',
                        'starter': 'class ConfigSingleton:\n    _instancia = None\n    \n    def __new__(cls):\n        # Complete aqui para implementar Singleton\n        pass',
                        'solution': 'if cls._instancia is None:\n            cls._instancia = super().__new__(cls)\n        return cls._instancia',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o padrão Observer',
                        'starter': 'class Subject:\n    def __init__(self):\n        self.observers = []\n    \n    def notify(self, message):\n        # Complete aqui para notificar todos os observers\n        pass',
                        'solution': 'for observer in self.observers:\n            observer.update(message)',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o padrão Strategy',
                        'starter': 'class Context:\n    def __init__(self, strategy):\n        self.strategy = strategy\n    \n    def execute_strategy(self, data):\n        # Complete aqui para usar a estratégia\n        pass',
                        'solution': 'return self.strategy.execute(data)',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Notificações',
                'type': 'creative',
                'instruction': 'Crie um sistema de notificações usando pelo menos 2 padrões: Observer para gerenciar inscritos e Strategy para diferentes tipos de notificação (email, SMS, push)!'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("0. Continuar para o Mini Projeto")
            
            try:
                escolha = input("\n👉 Sua escolha: ").strip().lower()
                
                if escolha in ["0", "continuar", "sair", "proximo"]:
                    break
                elif escolha in ["1", "quiz", "conhecimentos"]:
                    try:
                        self._run_quiz(exercicios[0])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo"]:
                    try:
                        self._run_creative_exercise(exercicios[2])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício criativo. Continuando...")
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")
                    
            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre Design Patterns e SOLID",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos com padrões",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de notificações com múltiplos padrões",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: E-commerce com Design Patterns",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para dominar os padrões!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_quiz(self, quiz_data: Dict) -> None:
        """Executa quiz interativo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section(f"QUIZ: {quiz_data['title']}", "📝", "info")
        
        questions = quiz_data['questions']
        score = 0
        total = len(questions)
        
        for i, q in enumerate(questions, 1):
            self.print_colored(f"\n📋 PERGUNTA {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            # Solicita resposta
            while True:
                try:
                    resposta = input("\n👉 Sua resposta: ").strip().lower()
                    
                    if resposta in ['sair', 'quit', 'exit']:
                        self.print_warning("Quiz cancelado pelo usuário.")
                        return
                    
                    # Verifica se a resposta está correta
                    if any(resposta in answer.lower() for answer in q['answer']):
                        self.print_success("✅ Correto!")
                        score += 1
                        break
                    else:
                        self.print_warning("❌ Incorreto.")
                        self.print_colored(f"💡 Dica: {q['hint']}", "info")
                        tentar_novamente = input("Tentar novamente? (s/n): ").lower()
                        if tentar_novamente not in ['s', 'sim', 'yes']:
                            self.print_colored(f"✅ Resposta correta: {q['answer'][0]}", "success")
                            break
                            
                except KeyboardInterrupt:
                    self.print_warning("\n\nQuiz interrompido.")
                    return
        
        # Mostra resultado final
        percentage = (score / total) * 100
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        
        if percentage >= 80:
            self.print_success(f"🌟 EXCELENTE! Você acertou {score}/{total} ({percentage:.1f}%)")
            self.print_colored("Você domina os conceitos de Design Patterns e SOLID!", "success")
        elif percentage >= 60:
            self.print_colored(f"👍 BOM! Você acertou {score}/{total} ({percentage:.1f}%)", "info")
            self.print_colored("Continue estudando para dominar totalmente!", "text")
        else:
            self.print_colored(f"📚 Você acertou {score}/{total} ({percentage:.1f}%)", "warning")
            self.print_colored("Recomendamos revisar as seções teóricas!", "text")
        
        self.pausar()
    
    def _run_code_completion(self, exercise_data: Dict) -> None:
        """Executa exercícios de completar código"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section(f"CÓDIGO: {exercise_data['title']}", "💻", "success")
        
        exercises = exercise_data['exercises']
        
        for i, ex in enumerate(exercises, 1):
            self.print_colored(f"\n🔧 EXERCÍCIO {i}/{len(exercises)}: {ex['instruction']}", "warning")
            
            # Mostra código inicial
            self.print_code_section("CÓDIGO INICIAL", ex['starter'])
            
            try:
                # Solicita completação
                self.print_colored("\n💡 Complete a parte que está faltando:", "info")
                while True:
                    try:
                        resposta = input("👉 Sua resposta: ").strip()
                        
                        if resposta.lower() in ['skip', 'pular', 'passar']:
                            self.print_colored(f"⏭️ Pulando... Resposta: {ex['solution']}", "info")
                            break
                        
                        # Simula verificação (em um sistema real, tentaria executar)
                        if any(keyword in resposta.lower() for keyword in ex['solution'].lower().split()):
                            self.print_success("✅ Código funcionou perfeitamente!")
                            break
                        else:
                            self.print_warning("❌ Código não está correto.")
                            self.print_colored(f"💡 Dica: A resposta esperada é: {ex['solution']}", "info")
                            tentar_novamente = input("Tentar novamente? (s/n): ").lower()
                            if tentar_novamente not in ['s', 'sim', 'yes']:
                                break
                                
                    except KeyboardInterrupt:
                        self.print_warning("\n\nExercício interrompido.")
                        return
                        
            except KeyboardInterrupt:
                self.print_warning("\n\nExercícios de código interrompidos.")
                return
        
        self.print_success("🎉 Parabéns! Você completou todos os exercícios de código!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: Dict) -> None:
        """Executa exercício criativo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section(f"CRIATIVO: {exercise_data['title']}", "🎨", "accent")
        
        self.print_colored("🎯 DESAFIO CRIATIVO:", "warning")
        self.print_colored(exercise_data['instruction'], "text")
        
        # Exemplo para inspiração
        self.print_colored("\n💡 EXEMPLO PARA INSPIRAÇÃO:", "info")
        exemplo_codigo = r'''# Sistema de Notificações com Observer + Strategy
from abc import ABC, abstractmethod

# Strategy para tipos de notificação
class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailStrategy(NotificationStrategy):
    def send(self, message, recipient):
        print(f"📧 Email para {recipient}: {message}")

class SMSStrategy(NotificationStrategy):
    def send(self, message, recipient):
        print(f"📱 SMS para {recipient}: {message}")

# Observer para gerenciar inscritos
class NotificationCenter:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def notify_all(self, message):
        for subscriber in self.subscribers:
            subscriber.receive_notification(message)

class User:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
    
    def receive_notification(self, message):
        self.strategy.send(message, self.name)

# Exemplo de uso
center = NotificationCenter()
user1 = User("Ana", EmailStrategy())
user2 = User("Carlos", SMSStrategy())

center.subscribe(user1)
center.subscribe(user2)
center.notify_all("Nova promoção disponível!")'''
        
        self.exemplo(exemplo_codigo)
        
        self.print_colored("\n🚀 AGORA É SUA VEZ!", "success")
        self.print_colored("Crie seu próprio sistema usando Design Patterns:", "text")
        self.print_colored("• Use pelo menos 2 padrões diferentes", "text")
        self.print_colored("• Implemente funcionalidades interessantes", "text")
        self.print_colored("• Siga os princípios SOLID", "text")
        self.print_colored("• Digite 'fim' numa linha para finalizar", "text")
        
        # Coleta código do usuário
        linhas_codigo = []
        print("\n👩‍💻 Digite seu código linha por linha:")
        
        try:
            while True:
                try:
                    linha = input(">>> ")
                    if linha.strip().lower() == 'fim':
                        break
                    linhas_codigo.append(linha)
                except KeyboardInterrupt:
                    self.print_warning("\n\nExercício criativo interrompido.")
                    return
            
            if linhas_codigo:
                codigo_usuario = '\n'.join(linhas_codigo)
                
                self.print_colored("\n🎨 SEU CÓDIGO:", "accent")
                self.exemplo(codigo_usuario)
                
                # Tentar executar o código do usuário
                try:
                    self.print_colored("\n🚀 Executando seu código:", "info")
                    self.executar_codigo(codigo_usuario)
                    self.print_success("🎉 Parabéns! Seu código funcionou!")
                except Exception as e:
                    self.print_warning(f"⚠️ Seu código tem alguns problemas: {str(e)}")
                    self.print_colored("Mas não se preocupe, o importante é praticar!", "text")
                
                self.print_success("\n🏆 EXERCÍCIO CRIATIVO CONCLUÍDO!")
                self.print_colored("Você aplicou Design Patterns na prática!", "accent")
            else:
                self.print_colored("Nenhum código foi inserido.", "warning")
                
        except KeyboardInterrupt:
            self.print_warning("\n\nExercício criativo interrompido.")
            return
        
        self.pausar()
    
    def _mini_projeto_ecommerce_patterns(self) -> None:
        """Mini Projeto - Módulo 31: Sistema de E-commerce com Design Patterns"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛍️ MINI PROJETO: E-COMMERCE COM DESIGN PATTERNS")
        else:
            print("\n" + "="*50)
            print("🛍️ MINI PROJETO: E-COMMERCE COM DESIGN PATTERNS")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema de e-commerce usando os melhores Design Patterns!")
        
        self.print_concept(
            "E-commerce Profissional",
            "Um sistema de vendas online que aplica múltiplos Design Patterns para criar uma arquitetura robusta, flexível e facilmente extensível - como os grandes do mercado!"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "🛒 Amazon - Factory para diferentes tipos de produtos",
            "🛍️ Mercado Livre - Strategy para diferentes formas de pagamento",
            "🎯 Magazine Luiza - Observer para notificações de estoque",
            "🏪 Shopify - Builder para construir lojas personalizadas",
            "💳 PayPal - Chain of Responsibility para validação de pagamentos",
            "📦 Correios - Adapter para integrar diferentes transportadoras"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Definindo a arquitetura
        self.print_section("PASSO 1: DEFININDO A ARQUITETURA", "📝", "info")
        self.print_tip("Vamos usar 6 Design Patterns diferentes em um sistema coeso!")
        
        patterns_usados = [
            "🏭 Factory - Para criar diferentes tipos de produtos",
            "🎭 Strategy - Para diferentes métodos de pagamento",
            "👀 Observer - Para notificações de pedidos",
            "🔨 Builder - Para construir pedidos complexos",
            "🎯 Singleton - Para configurações do sistema",
            "🎨 Decorator - Para adicionais e promoções"
        ]
        
        for pattern in patterns_usados:
            self.print_colored(f"✅ {pattern}", "success")
        
        input("\n🔸 Pressione ENTER para começar a construir...")
        
        try:
            # PASSO 2: Construindo o sistema
            self.print_section("PASSO 2: CONSTRUINDO O E-COMMERCE", "⚙️", "success")
            self.print_colored("Agora vamos implementar todos os padrões:", "text")
            
            # PASSO 3: Código final
            self.print_section("PASSO 3: SEU E-COMMERCE COMPLETO", "🎬", "warning")
            
            codigo_final = r'''# 🛍️ E-COMMERCE COM DESIGN PATTERNS
# Módulo 31: Design Patterns & SOLID Principles

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

# === SINGLETON: Configurações do Sistema ===
class ECommerceConfig:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.moeda = "R$"
            cls._instance.taxa_entrega = 10.0
        return cls._instance

# === FACTORY: Criação de Produtos ===
class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @abstractmethod
    def categoria(self):
        pass

class Eletronico(Produto):
    def categoria(self):
        return "Eletrônicos"

class Roupa(Produto):
    def categoria(self):
        return "Roupas"

class Livro(Produto):
    def categoria(self):
        return "Livros"

class ProdutoFactory:
    @staticmethod
    def criar_produto(tipo, nome, preco):
        if tipo == "eletronico":
            return Eletronico(nome, preco)
        elif tipo == "roupa":
            return Roupa(nome, preco)
        elif tipo == "livro":
            return Livro(nome, preco)
        else:
            raise ValueError(f"Tipo de produto {tipo} não existe!")

# === STRATEGY: Métodos de Pagamento ===
class MetodoPagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(MetodoPagamento):
    def processar(self, valor):
        return f"💳 Pagamento de R$ {valor:.2f} processado via Cartão de Crédito"

class PIX(MetodoPagamento):
    def processar(self, valor):
        return f"📱 Pagamento de R$ {valor:.2f} processado via PIX"

class Boleto(MetodoPagamento):
    def processar(self, valor):
        return f"🧾 Boleto de R$ {valor:.2f} gerado para pagamento"

# === OBSERVER: Sistema de Notificações ===
class Observer(ABC):
    @abstractmethod
    def update(self, pedido):
        pass

class Cliente(Observer):
    def __init__(self, nome):
        self.nome = nome
    
    def update(self, pedido):
        print(f"📧 {self.nome}, seu pedido #{pedido.id} foi atualizado!")

class EstoqueManager(Observer):
    def update(self, pedido):
        print(f"📦 Estoque: Pedido #{pedido.id} processado, atualizando inventário")

# === BUILDER: Construção de Pedidos ===
class Pedido:
    def __init__(self):
        self.id = None
        self.produtos = []
        self.metodo_pagamento = None
        self.desconto = 0
        self.observers = []
    
    def adicionar_observer(self, observer):
        self.observers.append(observer)
    
    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self)
    
    def total(self):
        config = ECommerceConfig()
        subtotal = sum(p.preco for p in self.produtos)
        total_com_desconto = subtotal * (1 - self.desconto)
        return total_com_desconto + config.taxa_entrega

class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()
    
    def com_id(self, id_pedido):
        self.pedido.id = id_pedido
        return self
    
    def adicionar_produto(self, produto):
        self.pedido.produtos.append(produto)
        return self
    
    def com_pagamento(self, metodo):
        self.pedido.metodo_pagamento = metodo
        return self
    
    def com_desconto(self, desconto):
        self.pedido.desconto = desconto
        return self
    
    def build(self):
        return self.pedido

# === DECORATOR: Promoções e Adicionais ===
class ProdutoDecorator(Produto):
    def __init__(self, produto):
        self.produto = produto
        super().__init__(produto.nome, produto.preco)
    
    def categoria(self):
        return self.produto.categoria()

class Promocao(ProdutoDecorator):
    def __init__(self, produto, desconto):
        super().__init__(produto)
        self.desconto = desconto
        self.nome = f"{produto.nome} (PROMOÇÃO {desconto*100:.0f}% OFF)"
        self.preco = produto.preco * (1 - desconto)

class Garantia(ProdutoDecorator):
    def __init__(self, produto, anos):
        super().__init__(produto)
        self.anos = anos
        self.nome = f"{produto.nome} + Garantia {anos} anos"
        self.preco = produto.preco + (anos * 50)

# === DEMONSTRAÇÃO DO SISTEMA ===
def demonstrar_ecommerce():
    print("🚀 INICIALIZANDO E-COMMERCE COM DESIGN PATTERNS...")
    
    # 1. Configuração (Singleton)
    config = ECommerceConfig()
    print(f"⚙️ Sistema configurado: {config.moeda}, Taxa entrega: {config.taxa_entrega}")
    
    # 2. Criando produtos (Factory)
    factory = ProdutoFactory()
    smartphone = factory.criar_produto("eletronico", "iPhone 15", 4999.00)
    camiseta = factory.criar_produto("roupa", "Camiseta Python", 89.90)
    livro = factory.criar_produto("livro", "Design Patterns GoF", 120.00)
    
    # 3. Aplicando decorators (Decorator)
    smartphone_promocao = Promocao(smartphone, 0.1)  # 10% off
    camiseta_garantia = Garantia(camiseta, 2)  # 2 anos garantia
    
    print(f"\n📱 {smartphone_promocao.nome}: {config.moeda} {smartphone_promocao.preco:.2f}")
    print(f"👕 {camiseta_garantia.nome}: {config.moeda} {camiseta_garantia.preco:.2f}")
    
    # 4. Criando observadores (Observer)
    cliente = Cliente("Maria Silva")
    estoque = EstoqueManager()
    
    # 5. Construindo pedido (Builder)
    builder = PedidoBuilder()
    pedido = (builder
              .com_id("PED001")
              .adicionar_produto(smartphone_promocao)
              .adicionar_produto(camiseta_garantia)
              .adicionar_produto(livro)
              .com_pagamento(PIX())
              .com_desconto(0.05)  # 5% desconto adicional
              .build())
    
    pedido.adicionar_observer(cliente)
    pedido.adicionar_observer(estoque)
    
    # 6. Processando pagamento (Strategy)
    total = pedido.total()
    resultado_pagamento = pedido.metodo_pagamento.processar(total)
    
    print(f"\n💰 Total do pedido: {config.moeda} {total:.2f}")
    print(f"✅ {resultado_pagamento}")
    
    # 7. Notificando observers
    print(f"\n📢 Notificando sobre o pedido #{pedido.id}:")
    pedido.notificar_observers()
    
    print(f"\n🎉 E-COMMERCE OPERACIONAL COM 6 DESIGN PATTERNS!")
    print(f"🏆 Arquitetura profissional implementada com sucesso!")

# Executando demonstração
demonstrar_ecommerce()'''
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.print_colored("Vamos ver seu E-commerce com Design Patterns em ação:", "text")
            self.executar_codigo(codigo_final)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um E-commerce com Design Patterns profissionais!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🏗️ Implementar padrão MVC/MVP para separar responsabilidades",
            "📊 Adicionar Command Pattern para histórico de ações",
            "🔄 Usar State Pattern para status de pedidos",
            "🌉 Implementar Bridge para diferentes plataformas de venda",
            "🎪 Adicionar Mediator para comunicação entre componentes",
            "🔗 Usar Chain of Responsibility para validações complexas"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de Software!")
        self.print_colored("Você agora domina os Design Patterns e SOLID Principles como um profissional!", "accent")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("E-commerce com Design Patterns")
        
        self.pausar()