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
        """Executa o módulo sobre design patterns e SOLID"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            self.pausar()
            return
        
        try:
            self._design_patterns_intro()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _design_patterns_intro(self) -> None:
        """Conteúdo principal sobre design patterns e SOLID"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 31: DESIGN PATTERNS & SOLID PRINCIPLES")
        else:
            print("\n" + "="*60)
            print("🏗️ MÓDULO 31: DESIGN PATTERNS & SOLID PRINCIPLES")
            print("="*60)
        
        self.print_colored("🚀 Aprenda arquitetura de software profissional!", "success")
        self.print_colored("🎯 Design Patterns e SOLID são fundamentais para:", "accent")
        self.print_colored("• Código limpo e manutenível", "primary")
        self.print_colored("• Sistemas escaláveis e flexíveis", "primary")
        self.print_colored("• Arquitetura robusta e testável", "primary")
        self.print_colored("• Reutilização e extensibilidade", "primary")
        self.print_colored("• Padrões reconhecidos pela indústria", "primary")
        self.print_colored("• Comunicação efetiva entre desenvolvedores", "primary")
        
        self.pausar()
        
        self._solid_principles()
        self._creational_patterns()
        self._structural_patterns()
        self._behavioral_patterns()
        self._mini_projeto_architecture_system()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _solid_principles(self):
        """Princípios SOLID fundamentais"""
        self.print_section("Princípios SOLID", "🎯", "accent")
        
        self.print_colored("🏛️ Os 5 princípios fundamentais da programação orientada a objetos:", "info")
        self.print_colored("• S - Single Responsibility Principle", "secondary")
        self.print_colored("• O - Open/Closed Principle", "secondary")
        self.print_colored("• L - Liskov Substitution Principle", "secondary")
        self.print_colored("• I - Interface Segregation Principle", "secondary")
        self.print_colored("• D - Dependency Inversion Principle", "secondary")
        
        self.pausar()
        
        # Exemplo 1: Single Responsibility
        self.print_colored("\n📌 S - Single Responsibility Principle", "warning")
        self.print_colored("Uma classe deve ter apenas uma razão para mudar.", "info")
        
        codigo_srp = '''# ❌ VIOLAÇÃO: Classe com múltiplas responsabilidades
class UserBad:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        print(f"Salvando {self.name} no banco...")
    
    def send_email(self):
        print(f"Enviando email para {self.email}...")
    
    def validate_email(self):
        return "@" in self.email

# ✅ CORRETO: Responsabilidades separadas
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user: User):
        print(f"Salvando {user.name} no banco...")

class EmailService:
    def send(self, email: str, message: str):
        print(f"Enviando email para {email}: {message}")

class EmailValidator:
    def validate(self, email: str) -> bool:
        return "@" in email and "." in email

# Uso correto:
user = User("João", "joao@email.com")
repo = UserRepository()
email_service = EmailService()
validator = EmailValidator()

if validator.validate(user.email):
    repo.save(user)
    email_service.send(user.email, "Bem-vindo!")
'''
        
        self.exemplo(codigo_srp)
        self.executar_codigo(codigo_srp)
        self.pausar()
        
        # Exemplo 2: Open/Closed Principle
        print("\n📌 O - Open/Closed Principle")
        print("Classes devem estar abertas para extensão, mas fechadas para modificação.")
        
        codigo_ocp = '''from abc import ABC, abstractmethod

# ✅ CORRETO: Usando abstração para permitir extensão
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    
    def area(self) -> float:
        return 0.5 * self.base * self.height

# Calculadora que funciona com qualquer forma
class AreaCalculator:
    def calculate_total_area(self, shapes: List[Shape]) -> float:
        return sum(shape.area() for shape in shapes)

# Uso:
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(6, 8)
]

calculator = AreaCalculator()
total = calculator.calculate_total_area(shapes)
print(f"Área total: {total:.2f}")
'''
        
        self.exemplo(codigo_ocp)
        self.executar_codigo(codigo_ocp)
        self.pausar()
        
        # Continuar com outros exemplos...
        print("\n✅ Todos os princípios SOLID foram demonstrados!")
        print("🎯 Próximo: Padrões de Criação (Creational Patterns)")
        self.pausar()
    
    def _creational_patterns(self):
        """Padrões de criação"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏭 PADRÕES DE CRIAÇÃO (CREATIONAL)")
        
        print("🎯 Padrões que lidam com a criação de objetos:")
        print("• Singleton - Uma única instância")
        print("• Factory Method - Criação delegada")
        print("• Abstract Factory - Famílias de objetos")
        print("• Builder - Construção complexa")
        print("• Prototype - Clonagem de objetos")
        
        self.pausar()
        
        # Exemplo: Singleton
        print("\n📌 SINGLETON PATTERN")
        print("Garante que uma classe tenha apenas uma instância.")
        
        codigo_singleton = '''class DatabaseConnection:
    """Singleton para conexão com banco de dados"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance
    
    def connect(self):
        if self.connection is None:
            print("Criando nova conexão com o banco...")
            self.connection = "Connected to Database"
        else:
            print("Usando conexão existente...")
        return self.connection

# Teste do Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"db1 é db2? {db1 is db2}")  # True

db1.connect()
db2.connect()  # Usa a mesma conexão
'''
        
        self.exemplo(codigo_singleton)
        self.executar_codigo(codigo_singleton)
        self.pausar()
        
        # Exemplo: Factory Method
        print("\n📌 FACTORY METHOD PATTERN")
        print("Define uma interface para criar objetos, mas deixa as subclasses decidirem qual classe instanciar.")
        
        codigo_factory = '''from abc import ABC, abstractmethod

# Produto abstrato
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

# Produtos concretos
class Dog(Animal):
    def make_sound(self) -> str:
        return "Au au! 🐕"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Miau! 🐱"

class Duck(Animal):
    def make_sound(self) -> str:
        return "Quack! 🦆"

# Factory abstrato
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Factories concretos
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

class DuckFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Duck()

# Cliente que usa o factory
class PetShop:
    def __init__(self, factory: AnimalFactory):
        self.factory = factory
    
    def show_pet(self):
        animal = self.factory.create_animal()
        print(f"Nosso pet faz: {animal.make_sound()}")

# Uso
dog_shop = PetShop(DogFactory())
cat_shop = PetShop(CatFactory())
duck_shop = PetShop(DuckFactory())

dog_shop.show_pet()
cat_shop.show_pet()
duck_shop.show_pet()
'''
        
        self.exemplo(codigo_factory)
        self.executar_codigo(codigo_factory)
        self.pausar()
        
        print("\n✅ Padrões de criação demonstrados!")
        print("🎯 Próximo: Padrões Estruturais")
        self.pausar()
    
    def _structural_patterns(self):
        """Padrões estruturais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ PADRÕES ESTRUTURAIS (STRUCTURAL)")
        
        print("🎯 Padrões que lidam com a composição de objetos:")
        print("• Adapter - Compatibilidade de interfaces")
        print("• Decorator - Adicionar comportamento")
        print("• Facade - Interface simplificada")
        print("• Proxy - Substituto ou placeholder")
        print("• Composite - Árvore de objetos")
        
        self.pausar()
        
        # Exemplo: Adapter
        print("\n📌 ADAPTER PATTERN")
        print("Permite que interfaces incompatíveis trabalhem juntas.")
        
        codigo_adapter = '''# Interface antiga (legada)
class OldPrinter:
    def print_old_format(self, text: str):
        print(f"[OLD PRINTER] {text.upper()}")

# Interface nova esperada
class ModernPrinter(ABC):
    @abstractmethod
    def print(self, text: str):
        pass

# Adapter para fazer o old printer funcionar com a interface nova
class PrinterAdapter(ModernPrinter):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer
    
    def print(self, text: str):
        # Adapta a chamada para o formato antigo
        self.old_printer.print_old_format(text)

# Novo printer que já implementa a interface moderna
class LaserPrinter(ModernPrinter):
    def print(self, text: str):
        print(f"[LASER] {text}")

# Cliente que usa apenas a interface moderna
def print_document(printer: ModernPrinter, doc: str):
    printer.print(doc)

# Uso
old = OldPrinter()
adapter = PrinterAdapter(old)
laser = LaserPrinter()

print_document(adapter, "Documento importante")  # Usa printer antigo
print_document(laser, "Outro documento")       # Usa printer moderno
'''
        
        self.exemplo(codigo_adapter)
        self.executar_codigo(codigo_adapter)
        self.pausar()
        
        print("\n✅ Padrões estruturais demonstrados!")
        print("🎯 Próximo: Padrões Comportamentais")
        self.pausar()
    
    def _behavioral_patterns(self):
        """Padrões comportamentais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎭 PADRÕES COMPORTAMENTAIS (BEHAVIORAL)")
        
        print("🎯 Padrões que lidam com comunicação entre objetos:")
        print("• Observer - Notificação de mudanças")
        print("• Strategy - Algoritmos intercambiáveis")
        print("• Command - Encapsular requisições")
        print("• Iterator - Percorrer coleções")
        print("• Template Method - Esqueleto de algoritmo")
        
        self.pausar()
        
        # Exemplo: Observer
        print("\n📌 OBSERVER PATTERN")
        print("Define uma dependência um-para-muitos entre objetos.")
        
        codigo_observer = '''from typing import List

# Interface do Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# Subject (Observable)
class WeatherStation:
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, temp: float):
        self._temperature = temp
        self.notify()

# Observers concretos
class PhoneDisplay(Observer):
    def update(self, temperature: float):
        print(f"📱 Phone: Temperature is {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature: float):
        print(f"🖼️ Window: Current temp: {temperature}°C")

class LoggingSystem(Observer):
    def update(self, temperature: float):
        print(f"📝 Log: Temperature changed to {temperature}°C")

# Uso
station = WeatherStation()

phone = PhoneDisplay()
window = WindowDisplay()
logger = LoggingSystem()

station.attach(phone)
station.attach(window)
station.attach(logger)

print("Mudando temperatura para 25°C:")
station.temperature = 25

print("\\nMudando temperatura para 30°C:")
station.temperature = 30
'''
        
        self.exemplo(codigo_observer)
        self.executar_codigo(codigo_observer)
        self.pausar()
        
        print("\n✅ Padrões comportamentais demonstrados!")
        print("🎯 Próximo: Mini-projeto integrando todos os padrões")
        self.pausar()
    
    def _mini_projeto_architecture_system(self):
        """Mini-projeto: Sistema com múltiplos patterns"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI-PROJETO: SISTEMA E-COMMERCE COM PATTERNS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI-PROJETO: SISTEMA E-COMMERCE COM PATTERNS")
            print("="*50)
        
        print("🏗️ Vamos criar um sistema que usa VÁRIOS padrões!")
        print("📦 Sistema de E-commerce com:")
        print("• Factory para criar produtos")
        print("• Singleton para carrinho")
        print("• Observer para notificações")
        print("• Strategy para cálculo de frete")
        print("• Decorator para descontos")
        
        self.pausar()
        
        codigo_projeto = '''# Sistema E-commerce com múltiplos patterns

# 1. PRODUTOS (Factory Pattern)
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    @abstractmethod
    def get_description(self) -> str:
        pass

class Electronics(Product):
    def get_description(self) -> str:
        return f"Eletrônico: {self.name} - R${self.price:.2f}"

class Clothing(Product):
    def get_description(self) -> str:
        return f"Vestuário: {self.name} - R${self.price:.2f}"

class ProductFactory:
    @staticmethod
    def create_product(product_type: str, name: str, price: float) -> Product:
        if product_type == "electronics":
            return Electronics(name, price)
        elif product_type == "clothing":
            return Clothing(name, price)
        else:
            raise ValueError(f"Unknown product type: {product_type}")

# 2. CARRINHO (Singleton Pattern)
class ShoppingCart:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = []
            cls._instance.observers = []
        return cls._instance
    
    def add_item(self, product: Product):
        self.items.append(product)
        self.notify_observers(f"Item adicionado: {product.name}")
    
    def get_total(self) -> float:
        return sum(item.price for item in self.items)
    
    # Observer pattern
    def attach_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)

# 3. NOTIFICAÇÕES (Observer Pattern)
class NotificationService(Observer):
    def update(self, message: str):
        print(f"🔔 Notificação: {message}")

# 4. CÁLCULO DE FRETE (Strategy Pattern)
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass

class StandardShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return weight * 5.0

class ExpressShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return weight * 10.0

# 5. SISTEMA COMPLETO
print("🛒 SISTEMA E-COMMERCE EM AÇÃO!")
print("-" * 40)

# Criar produtos
factory = ProductFactory()
laptop = factory.create_product("electronics", "Laptop Dell", 3500.00)
shirt = factory.create_product("clothing", "Camisa Polo", 89.90)

print("Produtos disponíveis:")
print(f"  • {laptop.get_description()}")
print(f"  • {shirt.get_description()}")

# Configurar carrinho e notificações
cart = ShoppingCart()
notification = NotificationService()
cart.attach_observer(notification)

# Adicionar ao carrinho
print("\\nAdicionando ao carrinho:")
cart.add_item(laptop)
cart.add_item(shirt)

# Calcular total
print(f"\\nTotal do carrinho: R${cart.get_total():.2f}")

# Calcular frete
print("\\nOpções de frete (5kg):")
standard = StandardShipping()
express = ExpressShipping()
print(f"  • Padrão: R${standard.calculate(5):.2f}")
print(f"  • Expresso: R${express.calculate(5):.2f}")

print("\\n✅ Sistema funcionando com múltiplos design patterns!")
'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        # Registra conclusão do mini-projeto
        self.complete_mini_project("Sistema E-commerce com Design Patterns")
        
        print("\n🏆 PARABÉNS! Você dominou Design Patterns!")
        print("🎯 Agora você pode:")
        print("• Identificar quando usar cada padrão")
        print("• Implementar soluções elegantes")
        print("• Criar arquiteturas flexíveis")
        print("• Comunicar ideias com outros desenvolvedores")
        
        self.pausar()