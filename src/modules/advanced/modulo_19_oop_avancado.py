#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 19: Programação Orientada a Objetos (OOP) - Avançado
Aprenda herança, polimorfismo e classes abstratas
"""

from ..shared.base_module import BaseModule


class Modulo19OopAvancado(BaseModule):
    """Módulo 19: OOP Avançado - Herança e Polimorfismo"""
    
    def __init__(self):
        super().__init__("modulo_19", "OOP Avançado - Herança e Polimorfismo")
        self.has_mini_project = True
        self.mini_project_points = 90
    
    def execute(self) -> None:
        """Executa o módulo sobre OOP avançado"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._oop_avancado()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _oop_avancado(self) -> None:
        """Conteúdo principal sobre OOP avançado"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧬 MÓDULO 19: OOP AVANÇADO")
        else:
            print("\n" + "="*50)
            print("🧬 MÓDULO 19: OOP AVANÇADO")
            print("="*50)
        
        print("🧬 Agora vamos aprender os conceitos AVANÇADOS de OOP!")
        print("👑 Herança e Polimorfismo são o coração da programação orientada a objetos!")
        
        print("\n═══════════════════════════════════════════════")
        print("        HERANÇA - REUTILIZANDO CLASSES")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Herança = uma classe 'filha' herda de uma classe 'pai'")
        print("📚 Vantagens:")
        print("• ♻️  Reutilização de código")
        print("• 🏗️  Hierarquia organizada")
        print("• 🔧 Especialização de comportamentos")
        
        self.pausar()
        
        codigo1 = '''# Exemplo de Herança - Sistema de Veículos
class Veiculo:
    """Classe pai - características gerais"""
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, incremento=10):
        """Método que será herdado"""
        self.velocidade += incremento
        print(f"🚗 {self.marca} {self.modelo} acelerou para {self.velocidade} km/h")
    
    def frear(self, decremento=10):
        """Método que será herdado"""
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"🚗 {self.marca} {self.modelo} freou para {self.velocidade} km/h")
    
    def info(self):
        """Informações gerais"""
        print(f"Veículo: {self.marca} {self.modelo} ({self.ano})")

# Classe filha - herda de Veiculo
class Carro(Veiculo):
    """Especialização de Veiculo"""
    
    def __init__(self, marca, modelo, ano, portas):
        # Chama o construtor da classe pai
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def buzinar(self):
        """Método específico de Carro"""
        print("🔊 Beep beep!")
    
    def info(self):
        """Sobrescreve o método da classe pai"""
        super().info()  # Chama o método pai
        print(f"Portas: {self.portas}")

# Outra classe filha
class Moto(Veiculo):
    """Outra especialização de Veiculo"""
    
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def empinar(self):
        """Método específico de Moto"""
        print("🏍️ Empinando! Vroooom!")
    
    def acelerar(self, incremento=15):
        """Sobrescreve - motos aceleram mais"""
        super().acelerar(incremento)
        print("💨 Moto é mais rápida!")

print("=== TESTANDO HERANÇA ===")
carro = Carro("Toyota", "Corolla", 2023, 4)
moto = Moto("Honda", "CB600", 2023, 600)

print("\\nInformações:")
carro.info()
print()
moto.info()

print("\\n=== MÉTODOS HERDADOS ===")
carro.acelerar()
moto.acelerar()

print("\\n=== MÉTODOS ESPECÍFICOS ===")
carro.buzinar()
moto.empinar()'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n🎭 POLIMORFISMO - Múltiplas Formas:")
        
        codigo2 = '''# Polimorfismo - mesma interface, comportamentos diferentes
class Animal:
    """Classe base para animais"""
    
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        """Método que será sobrescrito"""
        pass
    
    def mover(self):
        """Método que será sobrescrito"""
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
    
    def mover(self):
        return "correndo com as patas"

class Passaro(Animal):
    def fazer_som(self):
        return "Piu piu!"
    
    def mover(self):
        return "voando com as asas"

class Peixe(Animal):
    def fazer_som(self):
        return "... (silêncio)"
    
    def mover(self):
        return "nadando com as nadadeiras"

# Lista de animais diferentes
animais = [
    Cachorro("Rex", "Labrador"),
    Passaro("Piu", "Bem-te-vi"),
    Peixe("Nemo", "Palhaço")
]

print("=== POLIMORFISMO EM AÇÃO ===")
for animal in animais:
    print(f"\\n{animal.nome} ({animal.especie}):")
    print(f"  Som: {animal.fazer_som()}")
    print(f"  Movimento: {animal.mover()}")

# Função que funciona com qualquer animal
def apresentar_animal(animal):
    """Polimorfismo - funciona com qualquer Animal"""
    print(f"Este é {animal.nome}, ele faz {animal.fazer_som()}")

print("\\n=== FUNÇÃO POLIMÓRFICA ===")
for animal in animais:
    apresentar_animal(animal)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🏛️ Classes Abstratas:")
        
        codigo3 = '''# Classes abstratas - não podem ser instanciadas
from abc import ABC, abstractmethod

class Forma(ABC):
    """Classe abstrata - modelo para outras formas"""
    
    def __init__(self, cor):
        self.cor = cor
    
    @abstractmethod
    def calcular_area(self):
        """Método abstrato - deve ser implementado nas filhas"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        """Outro método abstrato"""
        pass
    
    def info(self):
        """Método concreto - pode ser usado"""
        print(f"Forma de cor {self.cor}")

class Retangulo(Forma):
    """Implementa todos os métodos abstratos"""
    
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    """Outra implementação"""
    
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.raio

print("=== CLASSES ABSTRATAS ===")
retangulo = Retangulo("azul", 5, 3)
circulo = Circulo("vermelho", 4)

formas = [retangulo, circulo]

for forma in formas:
    forma.info()
    print(f"  Área: {forma.calcular_area():.2f}")
    print(f"  Perímetro: {forma.calcular_perimetro():.2f}")
    print()

# Isso daria erro - não pode instanciar classe abstrata:
# forma_generica = Forma("verde")  # TypeError!'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "O que é herança em programação orientada a objetos?",
            ["classe filha herda da pai", "reutilização de código", "herança"],
            "Uma classe filha herda atributos e métodos da classe pai"
        )
        
        # Mini Projeto do Módulo 19
        self._mini_projeto_sistema_rpg()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_rpg(self) -> None:
        """Mini Projeto - Módulo 19: Sistema de Jogos RPG (Herança e Polimorfismo)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE JOGOS RPG")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE JOGOS RPG")
            print("="*50)
        
        print("⚔️ Sistema de RPG usando Herança e Polimorfismo!")
        print("🛠️ Usando: Herança, Polimorfismo, Classes Abstratas, Super()")
        
        self.pausar()
        
        codigo_projeto = '''# ⚔️ SISTEMA DE JOGOS RPG
# Sistema completo usando Herança e Polimorfismo

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from enum import Enum
import random

class TipoElemento(Enum):
    FOGO = "fogo"
    AGUA = "agua"
    TERRA = "terra"
    AR = "ar"
    NEUTRO = "neutro"

class Personagem(ABC):
    """Classe abstrata base para todos os personagens"""
    
    def __init__(self, nome: str, vida: int, mana: int, forca: int, defesa: int):
        self._nome = nome
        self._vida_maxima = vida
        self._vida_atual = vida
        self._mana_maxima = mana
        self._mana_atual = mana
        self._forca = forca
        self._defesa = defesa
        self._nivel = 1
        self._experiencia = 0
        self._vivo = True
    
    # Properties
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def vida_atual(self) -> int:
        return self._vida_atual
    
    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima
    
    @property
    def vivo(self) -> bool:
        return self._vivo and self._vida_atual > 0
    
    @property
    def nivel(self) -> int:
        return self._nivel
    
    # Métodos abstratos - devem ser implementados pelas subclasses
    @abstractmethod
    def atacar(self, alvo: 'Personagem') -> int:
        """Método abstrato para atacar"""
        pass
    
    @abstractmethod
    def habilidade_especial(self, alvo: 'Personagem') -> str:
        """Método abstrato para habilidade especial"""
        pass
    
    @abstractmethod
    def get_tipo(self) -> str:
        """Retorna o tipo do personagem"""
        pass
    
    # Métodos concretos
    def receber_dano(self, dano: int) -> int:
        """Recebe dano considerando defesa"""
        dano_real = max(1, dano - self._defesa)
        self._vida_atual = max(0, self._vida_atual - dano_real)
        
        if self._vida_atual <= 0:
            self._vivo = False
            print(f"💀 {self._nome} foi derrotado!")
        
        return dano_real
    
    def curar(self, quantidade: int):
        """Cura o personagem"""
        cura_real = min(quantidade, self._vida_maxima - self._vida_atual)
        self._vida_atual += cura_real
        print(f"💚 {self._nome} recuperou {cura_real} pontos de vida!")
        return cura_real
    
    def ganhar_experiencia(self, xp: int):
        """Ganha experiência e pode subir de nível"""
        self._experiencia += xp
        print(f"⭐ {self._nome} ganhou {xp} XP!")
        
        # Verifica se subiu de nível
        xp_necessario = self._nivel * 100
        if self._experiencia >= xp_necessario:
            self._subir_nivel()
    
    def _subir_nivel(self):
        """Sobe de nível"""
        self._nivel += 1
        self._experiencia = 0
        
        # Aumenta atributos
        self._vida_maxima += 20
        self._vida_atual = self._vida_maxima  # Cura completa
        self._mana_maxima += 10
        self._mana_atual = self._mana_maxima
        self._forca += 5
        self._defesa += 3
        
        print(f"🎉 {self._nome} subiu para o nível {self._nivel}!")
        print(f"   Vida: {self._vida_maxima}, Força: {self._forca}, Defesa: {self._defesa}")
    
    def __str__(self) -> str:
        status = "Vivo" if self.vivo else "Morto"
        return f"{self._nome} (Nv.{self._nivel}) - {self._vida_atual}/{self._vida_maxima} HP - {status}"

class Guerreiro(Personagem):
    """Classe Guerreiro - especialista em combate corpo a corpo"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=120, mana=30, forca=25, defesa=20)
        self._ira = 0  # Atributo especial
    
    def atacar(self, alvo) -> int:
        """Ataque básico do guerreiro"""
        dano_base = self._forca + random.randint(5, 15)
        
        # Bônus de ira
        if self._ira > 0:
            dano_base += self._ira * 2
            print(f"🔥 {self._nome} ataca com fúria! (+{self._ira * 2} dano)")
            self._ira = max(0, self._ira - 1)
        
        print(f"⚔️ {self._nome} ataca {alvo.nome} causando {dano_base} de dano!")
        return alvo.receber_dano(dano_base)
    
    def habilidade_especial(self, alvo) -> str:
        """Golpe Devastador - ataque poderoso"""
        if self._mana_atual < 15:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 15
        dano = self._forca * 2 + random.randint(10, 20)
        self._ira += 2  # Ganha ira
        
        print(f"💥 {self._nome} usa GOLPE DEVASTADOR!")
        alvo.receber_dano(dano)
        return f"Dano causado: {dano}"
    
    def get_tipo(self) -> str:
        return "Guerreiro"

class Mago(Personagem):
    """Classe Mago - especialista em magia"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=80, mana=100, forca=15, defesa=10)
        self._elemento = random.choice(list(TipoElemento))
    
    def atacar(self, alvo) -> int:
        """Míssil mágico"""
        if self._mana_atual < 5:
            # Ataque físico fraco se não tem mana
            dano = self._forca + random.randint(1, 5)
            print(f"🔮 {self._nome} ataca com cajado causando {dano} de dano!")
        else:
            self._mana_atual -= 5
            dano = self._forca + 10 + random.randint(5, 15)
            print(f"✨ {self._nome} lança míssil mágico de {self._elemento.value} causando {dano} de dano!")
        
        return alvo.receber_dano(dano)
    
    def habilidade_especial(self, alvo) -> str:
        """Explosão Elemental"""
        if self._mana_atual < 25:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 25
        dano = 30 + random.randint(15, 25)
        
        print(f"🌟 {self._nome} conjura EXPLOSÃO DE {self._elemento.value.upper()}!")
        alvo.receber_dano(dano)
        
        # Chance de efeito adicional
        if random.random() < 0.3:
            if self._elemento == TipoElemento.FOGO:
                dano_extra = 10
                print(f"🔥 {alvo.nome} está queimando! (+{dano_extra} dano)")
                alvo.receber_dano(dano_extra)
            elif self._elemento == TipoElemento.AGUA:
                print(f"💧 {self._nome} recupera 15 pontos de mana!")
                self._mana_atual = min(self._mana_maxima, self._mana_atual + 15)
        
        return f"Dano causado: {dano}"
    
    def get_tipo(self) -> str:
        return f"Mago ({self._elemento.value})"

class Ladino(Personagem):
    """Classe Ladino - especialista em velocidade e furtividade"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=90, mana=50, forca=20, defesa=15)
        self._furtivo = False
    
    def atacar(self, alvo) -> int:
        """Ataque rápido"""
        dano_base = self._forca + random.randint(8, 12)
        
        # Bônus se estiver furtivo
        if self._furtivo:
            dano_base *= 2
            self._furtivo = False
            print(f"🗡️ {self._nome} ataca pelas costas! DANO CRÍTICO!")
        else:
            print(f"🗡️ {self._nome} ataca rapidamente {alvo.nome}!")
        
        print(f"   Dano causado: {dano_base}")
        return alvo.receber_dano(dano_base)
    
    def habilidade_especial(self, alvo) -> str:
        """Fica invisível para próximo ataque"""
        if self._mana_atual < 20:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 20
        self._furtivo = True
        
        print(f"👻 {self._nome} entra em modo FURTIVO!")
        print("   Próximo ataque causará dano crítico!")
        return "Modo furtivo ativado"
    
    def get_tipo(self) -> str:
        return "Ladino"

class Curandeiro(Personagem):
    """Classe Curandeiro - especialista em cura e suporte"""
    
    def __init__(self, nome: str):
        super().__init__(nome, vida=100, mana=80, forca=12, defesa=18)
    
    def atacar(self, alvo) -> int:
        """Ataque com luz sagrada"""
        if self._mana_atual >= 8:
            self._mana_atual -= 8
            dano = self._forca + 8 + random.randint(3, 10)
            print(f"✨ {self._nome} ataca com luz sagrada causando {dano} de dano!")
        else:
            dano = self._forca + random.randint(1, 6)
            print(f"🔨 {self._nome} ataca com cajado causando {dano} de dano!")
        
        return alvo.receber_dano(dano)
    
    def habilidade_especial(self, alvo) -> str:
        """Cura Divina"""
        if self._mana_atual < 20:
            return f"❌ {self._nome} não tem mana suficiente!"
        
        self._mana_atual -= 20
        cura = 40 + random.randint(10, 20)
        
        print(f"✨ {self._nome} conjura CURA DIVINA!")
        if alvo == self:
            self.curar(cura)
            return f"Auto-cura: {cura} HP"
        else:
            alvo.curar(cura)
            return f"Curou {alvo.nome}: {cura} HP"
    
    def get_tipo(self) -> str:
        return "Curandeiro"

class SistemaCombate:
    """Sistema de combate do jogo"""
    
    @staticmethod
    def combate_turno(atacante, defensor):
        """Executa um turno de combate"""
        if not atacante.vivo:
            return
        
        print(f"\\n--- Turno de {atacante.nome} ---")
        print(f"Status: {atacante}")
        print(f"Alvo: {defensor}")
        
        # Decide ação (70% ataque normal, 30% habilidade especial)
        if random.random() < 0.7 or atacante._mana_atual < 15:
            atacante.atacar(defensor)
        else:
            result = atacante.habilidade_especial(defensor)
            print(f"Resultado: {result}")
    
    @staticmethod
    def batalha_completa(personagem1, personagem2):
        """Executa uma batalha completa"""
        print(f"\\n⚔️ BATALHA: {personagem1.nome} vs {personagem2.nome}")
        print("=" * 50)
        
        turno = 0
        while personagem1.vivo and personagem2.vivo and turno < 10:
            turno += 1
            print(f"\\n🎲 TURNO {turno}")
            
            # Turno do personagem 1
            if personagem1.vivo:
                SistemaCombate.combate_turno(personagem1, personagem2)
            
            # Turno do personagem 2
            if personagem2.vivo:
                SistemaCombate.combate_turno(personagem2, personagem1)
        
        # Determina vencedor
        if personagem1.vivo and not personagem2.vivo:
            vencedor = personagem1
            print(f"\\n🏆 {vencedor.nome} venceu a batalha!")
            vencedor.ganhar_experiencia(50)
        elif personagem2.vivo and not personagem1.vivo:
            vencedor = personagem2
            print(f"\\n🏆 {vencedor.nome} venceu a batalha!")
            vencedor.ganhar_experiencia(50)
        else:
            print("\\n🤝 Batalha terminou em empate!")
            return None
        
        return vencedor

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE JOGOS RPG ===")
print()

# Criando personagens de diferentes classes
print("👥 CRIANDO HERÓIS:")
herois = [
    Guerreiro("Conan"),
    Mago("Gandalf"),
    Ladino("Robin"),
    Curandeiro("Zelda")
]

for heroi in herois:
    print(f"  ✅ {heroi.get_tipo()}: {heroi}")

print()

# Demonstração de polimorfismo
print("🎭 DEMONSTRAÇÃO DE POLIMORFISMO:")
print("(Cada classe implementa atacar() de forma diferente)")
print()

for heroi in herois:
    print(f"--- {heroi.nome} ({heroi.get_tipo()}) ---")
    # Todos têm o método atacar, mas comportamentos diferentes
    dummy_target = Guerreiro("Dummy")
    dummy_target._vida_atual = 1000  # Para não morrer
    heroi.atacar(dummy_target)
    print()

# Batalha épica
print("⚔️ BATALHA ÉPICA:")
guerreiro = herois[0]  # Conan
mago = herois[1]       # Gandalf

vencedor = SistemaCombate.batalha_completa(guerreiro, mago)

print()
print("✅ Sistema de RPG implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Herança (Personagem -> Guerreiro, Mago, etc.)")
print("  • Polimorfismo (mesmo método, comportamentos diferentes)")
print("  • Classes abstratas (ABC)")
print("  • Métodos abstratos (@abstractmethod)")
print("  • Super() para chamar métodos da classe pai")
print("  • Enums para constantes")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de RPG criado!")
        print("🎯 Aplicação real: jogos, simulações, sistemas com hierarquias")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Jogos RPG")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo19OopAvancado()
    print("Teste do módulo 19 - versão standalone")
    module._oop_avancado()