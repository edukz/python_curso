#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 19: Programação Orientada a Objetos (OOP) - Avançado
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda herança, polimorfismo e classes abstratas de forma interativa
"""

from ..shared.base_module import BaseModule
import random
import time


class Modulo19OopAvancado(BaseModule):
    """Módulo 19: OOP Avançado - Herança, Polimorfismo e Classes Abstratas"""
    
    def __init__(self):
        super().__init__("modulo_19", "OOP Avançado - Herança, Polimorfismo e Abstratas")
        self.has_mini_project = True
        self.mini_project_points = 120
    
    def execute(self) -> None:
        """Executa o módulo OOP Avançado"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._oop_avancado()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _oop_avancado(self) -> None:
        """Conteúdo principal do módulo OOP Avançado"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧬 MÓDULO 19: OOP AVANÇADO - HERANÇA E POLIMORFISMO")
        else:
            print("\n" + "="*60)
            print("🧬 MÓDULO 19: OOP AVANÇADO - HERANÇA E POLIMORFISMO")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao nível avançado da Programação Orientada a Objetos!")
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
            self._mini_projeto_sistema_rpg()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (5-7 SEÇÕES RECOMENDADAS) ===
        secoes = [
            {
                'id': 'secao_conceito_heranca',
                'titulo': '🧬 O que é Herança?',
                'descricao': 'Entenda o conceito fundamental de herança em OOP',
                'funcao': self._secao_conceito_heranca
            },
            {
                'id': 'secao_polimorfismo_pratico',
                'titulo': '🎭 Como Polimorfismo funciona?',
                'descricao': 'Veja polimorfismo em ação com exemplos práticos',
                'funcao': self._secao_polimorfismo_pratico
            },
            {
                'id': 'secao_classes_abstratas_exemplos',
                'titulo': '🏛️ Classes Abstratas na prática',
                'descricao': 'Aprenda a criar contratos com classes abstratas',
                'funcao': self._secao_classes_abstratas_exemplos
            },
            {
                'id': 'secao_mundo_real',
                'titulo': '🏢 Onde usar na vida real?',
                'descricao': 'Veja OOP avançado em sistemas reais e empresas',
                'funcao': self._secao_mundo_real
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas OOP',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Aprenda com os erros mais frequentes em OOP avançado',
                'funcao': self._secao_erros_comuns
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre OOP',
                'descricao': 'Fatos interessantes e história da programação OO',
                'funcao': self._secao_curiosidades
            }
        ]

        secoes_visitadas = set()

        # === LOOP PRINCIPAL DE NAVEGAÇÃO ===
        while True:
            # Limpa tela e mostra cabeçalho
            if self.ui:
                self.ui.clear_screen()
            else:
                print("\n" + "="*50)
            
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
                    try:
                        secoes[idx]['funcao']()
                        secoes_visitadas.add(secoes[idx]['id'])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Seção interrompida. Voltando ao menu...")
                        continue
                else:
                    self.print_warning(f"❌ Opção inválida! Digite um número de 1 a {len(secoes)} ou 0.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Pulando para exercícios práticos...")
                break
            except Exception as e:
                self.print_warning(f"❌ Erro: {str(e)}. Tente novamente.")
    
    def _secao_conceito_heranca(self) -> None:
        """Seção: O que é Herança?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É HERANÇA?", "🧬")

        # === DEFINIÇÃO DO CONCEITO (SEMPRE PRIMEIRO) ===
        self.print_concept(
            "Herança em OOP",
            "Um mecanismo que permite criar uma nova classe baseada em uma classe existente, reutilizando e estendendo suas funcionalidades."
        )

        # === DICA RELACIONADA ===
        self.print_tip("Herança é como genes na biologia - filhos herdam características dos pais!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma família: os filhos herdam características dos pais (olhos, altura), mas também desenvolvem suas próprias personalidades. Na programação é igual - a classe filha herda métodos e atributos da classe pai, mas pode adicionar ou modificar comportamentos.", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você cria uma classe pai com características comuns",
            "2. Você cria classes filhas que herdam da classe pai",
            "3. As classes filhas ganham automaticamente todos os métodos do pai",
            "4. Você pode adicionar novos métodos específicos nas classes filhas",
            "5. Você pode modificar (sobrescrever) métodos herdados se necessário"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Exemplo simples de herança
class Veiculo:  # Classe pai
    def __init__(self, marca):
        self.marca = marca
    
    def acelerar(self):
        return f"{self.marca} está acelerando"

class Carro(Veiculo):  # Classe filha
    def __init__(self, marca, portas):
        super().__init__(marca)  # Chama o pai
        self.portas = portas
    
    def buzinar(self):  # Método novo
        return "Beep beep!"

# Testando
carro = Carro("Toyota", 4)
print(carro.acelerar())  # Método herdado
print(carro.buzinar())   # Método próprio'''
        
        self.exemplo(codigo_exemplo)
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Facebook: Classe User → AdminUser, RegularUser",
            "Netflix: Classe Video → Movie, Series, Documentary",
            "Uber: Classe Vehicle → Car, Motorcycle, Bike",
            "YouTube: Classe Content → Video, Short, Live"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()
    
    def _secao_polimorfismo_pratico(self) -> None:
        """Seção: Como Polimorfismo funciona?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO POLIMORFISMO FUNCIONA?", "🎭")

        self.print_concept(
            "Polimorfismo",
            "A capacidade de objetos diferentes responderem ao mesmo método de formas diferentes. 'Poly' = muitas, 'morphos' = formas."
        )

        self.print_tip("Pense em um controle remoto universal - o mesmo botão 'ligar' funciona para TV, som e DVD!")

        # Exemplo prático detalhado
        self.print_colored("\n🎵 ANALOGIA: ORQUESTRA MUSICAL", "warning")
        self.print_colored("Um maestro dá o comando 'tocar' para toda orquestra. Cada instrumento 'toca' de forma diferente: piano pressiona teclas, violino usa arco, bateria usa baquetas. Mesmo comando, ações diferentes!", "text")
        
        input("\n🔸 Pressione ENTER para ver o código...")

        codigo_polimorfismo = '''# Polimorfismo em ação
class Instrumento:
    def __init__(self, nome):
        self.nome = nome
    
    def tocar(self):
        return "Tocando instrumento"

class Piano(Instrumento):
    def tocar(self):
        return f"{self.nome}: Pressionando teclas 🎹"

class Violino(Instrumento):
    def tocar(self):
        return f"{self.nome}: Usando o arco 🎻"

class Bateria(Instrumento):
    def tocar(self):
        return f"{self.nome}: Batendo com baquetas 🥁"

# Polimorfismo - mesmo método, comportamentos diferentes
orquestra = [
    Piano("Piano de cauda"),
    Violino("Stradivarius"),
    Bateria("Kit completo")
]

print("🎼 CONCERTO DA ORQUESTRA:")
for instrumento in orquestra:
    print(instrumento.tocar())  # Mesmo método, sons diferentes!'''

        self.exemplo(codigo_polimorfismo)
        self.executar_codigo(codigo_polimorfismo)

        self.print_colored("\n🌍 APLICAÇÕES REAIS:", "accent")
        apps_reais = [
            "WhatsApp: Classe Message → TextMessage.send(), ImageMessage.send(), AudioMessage.send()",
            "Photoshop: Classe Tool → BrushTool.draw(), EraserTool.draw(), PencilTool.draw()",
            "Games: Classe Character → Warrior.attack(), Mage.attack(), Archer.attack()"
        ]
        for app in apps_reais:
            self.print_colored(f"• {app}", "primary")

        self.pausar()
    
    def _secao_classes_abstratas_exemplos(self) -> None:
        """Seção: Classes Abstratas na prática"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CLASSES ABSTRATAS NA PRÁTICA", "🏛️")

        self.print_concept(
            "Classes Abstratas",
            "São 'contratos' que definem quais métodos as classes filhas DEVEM implementar. Não podem ser instanciadas diretamente."
        )

        self.print_tip("Como uma planta arquitetônica - define o que deve existir, mas não constrói nada sozinha!")

        self.print_colored("\n🏗️ ANALOGIA: PLANTA DE CASA", "warning")
        self.print_colored("Uma planta arquitetônica define 'deve ter cozinha, banheiro, sala', mas não diz como será a cor das paredes. Cada construtor implementa os detalhes. Classes abstratas são iguais!", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")

        codigo_abstrato = '''from abc import ABC, abstractmethod

# Classe abstrata - como uma "planta de casa"
class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    @abstractmethod
    def calcular_bonus(self):  # DEVE ser implementado
        pass
    
    @abstractmethod
    def get_funcao(self):      # DEVE ser implementado
        pass
    
    def info(self):  # Método concreto - pode usar
        return f"{self.nome} - {self.get_funcao()}"

# Implementações concretas
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15  # 15% de bônus
    
    def get_funcao(self):
        return "Desenvolvedor Python"

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.25  # 25% de bônus
    
    def get_funcao(self):
        return "Gerente de Projeto"

# Testando
dev = Desenvolvedor("Ana", 5000)
gerente = Gerente("Carlos", 8000)

print(f"{dev.info()} - Bônus: R$ {dev.calcular_bonus():.2f}")
print(f"{gerente.info()} - Bônus: R$ {gerente.calcular_bonus():.2f}")

# Isso daria erro:
# func = Funcionario("Teste", 1000)  # TypeError!'''

        self.exemplo(codigo_abstrato)
        self.executar_codigo(codigo_abstrato)

        self.print_colored("\n🌍 ONDE É USADO:", "accent")
        usos = [
            "Django: Models abstratos para bancos de dados",
            "Jogos: Classes base para personagens",
            "APIs: Interfaces padronizadas para serviços",
            "Frameworks: Templates para componentes"
        ]
        for uso in usos:
            self.print_colored(f"• {uso}", "primary")

        self.pausar()
    
    def _secao_mundo_real(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("OOP AVANÇADO NO MUNDO REAL", "🏢")

        self.print_success("🌍 Vamos ver como grandes empresas usam esses conceitos!")

        casos_reais = [
            {
                'empresa': 'NETFLIX',
                'conceito': 'Herança e Polimorfismo',
                'exemplo': 'Classe Content → Movie, Series, Documentary. Cada tipo implementa play() diferente.',
                'codigo': '''class Content:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def play(self):
        pass  # Cada tipo implementa diferente

class Movie(Content):
    def play(self):
        return f"Reproduzindo filme: {self.title}"

class Series(Content):
    def __init__(self, title, episodes):
        super().__init__(title, episodes * 45)  # 45min por ep
        self.episodes = episodes
    
    def play(self):
        return f"Reproduzindo série: {self.title} ({self.episodes} eps)"

# Polimorfismo
catalogo = [Movie("Matrix", 136), Series("Stranger Things", 8)]
for item in catalogo:
    print(item.play())'''
            },
            {
                'empresa': 'UBER',
                'conceito': 'Classes Abstratas',
                'exemplo': 'Classe Vehicle abstrata força implementação de calculate_fare() para cada tipo.',
                'codigo': '''from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class UberX(Vehicle):
    def calculate_fare(self, distance):
        return distance * 1.5  # R$ 1,50 por km

class UberBlack(Vehicle):
    def calculate_fare(self, distance):
        return distance * 3.0  # R$ 3,00 por km

# Uso
ride1 = UberX("ABC-1234")
ride2 = UberBlack("XYZ-5678")

print(f"UberX 10km: R$ {ride1.calculate_fare(10):.2f}")
print(f"UberBlack 10km: R$ {ride2.calculate_fare(10):.2f}")'''
            }
        ]

        for caso in casos_reais:
            self.print_colored(f"\n🏢 {caso['empresa']}", "warning")
            self.print_colored(f"🔸 Conceito: {caso['conceito']}", "info")
            self.print_colored(f"📝 {caso['exemplo']}", "text")
            
            input("\nPressione ENTER para ver o código...")
            self.exemplo(caso['codigo'])
            self.executar_codigo(caso['codigo'])
            
            if caso != casos_reais[-1]:
                input("\nPressione ENTER para o próximo exemplo...")

        self.print_success("\n🎆 Agora você viu OOP avançado sendo usado por gigantes da tecnologia!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas OOP"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("MELHORES PRÁTICAS OOP", "⭐")

        self.print_success("🏆 Dicas de desenvolvedores seniores!")

        praticas = [
            {
                'titulo': 'Prefira Composição à Herança',
                'explicacao': 'Nem sempre herança é a melhor opção. Às vezes é melhor ter objetos como atributos.',
                'exemplo': 'Em vez de Car herdar de Engine, Car pode TER um Engine como atributo.'
            },
            {
                'titulo': 'Use Nomes Descritivos',
                'explicacao': 'Classes e métodos devem ter nomes que explicam claramente seu propósito.',
                'exemplo': 'EmailSender é melhor que ES. send_email() é melhor que send().'
            },
            {
                'titulo': 'Mantenha Classes Pequenas',
                'explicacao': 'Uma classe deve ter uma responsabilidade bem definida (Princípio da Responsabilidade Única).',
                'exemplo': 'Melhor ter UserValidator e UserSaver separados que UserManager fazendo tudo.'
            },
            {
                'titulo': 'Use Herança para Relacionamentos "is-a"',
                'explicacao': 'Herança deve representar uma relação "X é um Y".',
                'exemplo': 'Dog is-a Animal ✅. Car is-a Engine ❌ (Car HAS-A Engine).'
            }
        ]

        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{i}. {pratica['titulo']}", "warning")
            self.print_colored(f"📝 {pratica['explicacao']}", "text")
            self.print_colored(f"💡 Exemplo: {pratica['exemplo']}", "info")
            
            if i < len(praticas):
                input("\nPressione ENTER para a próxima dica...")

        self.print_tip("🚀 Estas dicas vêm da experiência de milhares de desenvolvedores!")
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ERROS COMUNS EM OOP AVANÇADO", "⚠️")

        self.print_warning("🚨 Vamos ver os erros mais comuns para você evitar!")

        erros = [
            {
                'erro': 'Esquecer de chamar super().__init__()',
                'problema': 'A classe pai não é inicializada corretamente',
                'solucao': 'Sempre chame super().__init__() no construtor da classe filha',
                'codigo_errado': '''class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # ERRO: Não chamou super()
        self.raca = raca''',
                'codigo_correto': '''class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # ✅ Correto!
        self.raca = raca'''
            },
            {
                'erro': 'Hierarquias muito profundas',
                'problema': 'Classes filhas de filhas de filhas... fica confuso de manter',
                'solucao': 'Prefira composição ou mantenha hierarquias simples (máx 3-4 níveis)',
                'codigo_errado': '''# ERRO: Hierarquia muito profunda
class Vehicle → LandVehicle → Car → SportsCar → Ferrari → LaFerrari''',
                'codigo_correto': '''# ✅ Melhor: Usar composição
class Car:
    def __init__(self, engine, brand):
        self.engine = engine
        self.brand = brand'''
            }
        ]

        for i, erro in enumerate(erros, 1):
            self.print_colored(f"\n❌ ERRO {i}: {erro['erro']}", "error")
            self.print_colored(f"💥 Problema: {erro['problema']}", "text")
            self.print_colored(f"✅ Solução: {erro['solucao']}", "success")
            
            print("\n💻 CÓDIGO ERRADO:")
            self.print_code_section("EVITE", erro['codigo_errado'])
            
            print("\n🎆 CÓDIGO CORRETO:")
            self.print_code_section("FAÇA ASSIM", erro['codigo_correto'])
            
            if i < len(erros):
                input("\nPressione ENTER para o próximo erro...")

        self.print_success("\n🏆 Agora você conhece as armadilhas mais comuns!")
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre OOP"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CURIOSIDADES SOBRE OOP", "💫")

        self.print_success("🎆 Fatos interessantes sobre Programação Orientada a Objetos!")

        curiosidades = [
            {
                'titulo': 'OOP foi inventada em 1967!',
                'fato': 'A primeira linguagem OOP foi Simula, criada na Noruega. Era usada para simulações físicas.',
                'impacto': 'Hoje, 90% dos sistemas do mundo usam OOP!'
            },
            {
                'titulo': 'Java foi criada em apenas 18 meses',
                'fato': 'James Gosling criou Java na Sun Microsystems em tempo recorde para competir com C++.',
                'impacto': 'Java popularizou OOP para milhões de desenvolvedores.'
            },
            {
                'titulo': 'Python nasceu como hobby!',
                'fato': 'Guido van Rossum criou Python nas férias de Natal de 1989, por diversão.',
                'impacto': 'Hoje é uma das linguagens mais populares do mundo!'
            },
            {
                'titulo': 'Minecraft foi feito com OOP',
                'fato': 'O jogo mais vendido da história usa herança para blocos, criaturas e itens.',
                'impacto': 'Prova que OOP pode criar experiências incríveis!'
            }
        ]

        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n🌟 {curiosidade['titulo']}", "warning")
            self.print_colored(f"📝 {curiosidade['fato']}", "text")
            self.print_colored(f"🚀 Impacto: {curiosidade['impacto']}", "success")
            
            if i < len(curiosidades):
                input("\nPressione ENTER para a próxima curiosidade...")

        self.print_success("\n🎉 OOP tem uma história rica e continua evoluindo!")
        self.print_tip("💡 Você faz parte dessa história ao aprender esses conceitos!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")

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
                'title': 'Quiz: Conhecimentos sobre OOP Avançado',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é a principal vantagem da herança em OOP?',
                        'answer': ['reutilizar código', 'reutilização', 'herdar'],
                        'hint': 'Pense em como uma classe filha pode usar o que a classe pai já tem'
                    },
                    {
                        'question': 'O que é polimorfismo?',
                        'answer': ['mesmo método comportamentos diferentes', 'uma interface várias formas', 'polimorfismo'],
                        'hint': 'Poly = muitas, morphos = formas. Objetos diferentes, mesma interface'
                    },
                    {
                        'question': 'Para que servem classes abstratas?',
                        'answer': ['definir contratos', 'forçar implementação', 'modelo'],
                        'hint': 'São como plantas arquitetônicas - definem o que deve existir'
                    },
                    {
                        'question': 'O que faz o super() em Python?',
                        'answer': ['chama método pai', 'acessa classe pai', 'super'],
                        'hint': 'Permite acessar métodos e atributos da classe pai'
                    },
                    {
                        'question': 'O que é MRO em Python?',
                        'answer': ['method resolution order', 'ordem resolução', 'mro'],
                        'hint': 'Define a ordem que Python busca métodos em herança múltipla'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a herança simples',
                        'starter': '''class Animal:
    def fazer_som(self):
        return "Som genérico"

class Cachorro(______):  # Complete aqui
    def fazer_som(self):
        return "Au au!"

# Teste
cao = Cachorro()
print(cao.fazer_som())''',
                        'solution': 'Animal',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Use super() corretamente',
                        'starter': '''class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def acelerar(self):
        return "Acelerando..."

class Carro(Veiculo):
    def __init__(self, marca, portas):
        ______.______(marca)  # Complete aqui
        self.portas = portas

# Teste
carro = Carro("Toyota", 4)
print(carro.marca)''',
                        'solution': 'super().__init__',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Implemente classe abstrata',
                        'starter': '''from abc import ABC, abstractmethod

class Forma(ABC):
    ______  # Complete aqui
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura''',
                        'solution': '@abstractmethod',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Animais do Zoo',
                'type': 'creative',
                'instruction': 'Crie um sistema de zoo com pelo menos 3 tipos de animais usando herança e polimorfismo'
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
                    self._show_help_pratica()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return  # CRÍTICO: Return em vez de break para sair completamente
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo"""
        self.print_section("QUIZ DE CONHECIMENTOS", "🧠", "info")
        self.print_colored("Responda as perguntas sobre OOP Avançado:", "text")
        
        perguntas = quiz_data['questions']
        acertos = 0
        
        for i, pergunta in enumerate(perguntas, 1):
            print(f"\n🔸 Pergunta {i}/{len(perguntas)}:")
            print(f"{pergunta['question']}")
            
            resposta = input("\n👉 Sua resposta: ").strip().lower()
            
            # Verifica se a resposta contém alguma das palavras-chave
            acertou = any(palavra in resposta for palavra in pergunta['answer'])
            
            if acertou:
                self.print_success("✅ Correto!")
                acertos += 1
            else:
                self.print_warning("❌ Ops, não foi dessa vez.")
                self.print_tip(f"Dica: {pergunta['hint']}")
            
            if i < len(perguntas):
                input("\nPressione ENTER para a próxima pergunta...")
        
        # Resultado final
        porcentagem = (acertos / len(perguntas)) * 100
        print(f"\n📊 RESULTADO: {acertos}/{len(perguntas)} ({porcentagem:.1f}%)")
        
        if porcentagem >= 80:
            self.print_success("🎆 Excelente! Você domina OOP avançado!")
        elif porcentagem >= 60:
            self.print_success("💪 Bom trabalho! Continue praticando.")
        else:
            self.print_tip("📚 Revise os conceitos e tente novamente mais tarde.")
        
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercícios de completar código"""
        self.print_section("COMPLETE O CÓDIGO", "💻", "warning")
        self.print_colored("Complete os códigos abaixo com os conceitos aprendidos:", "text")
        
        exercicios = exercise_data['exercises']
        
        for i, ex in enumerate(exercicios, 1):
            print(f"\n🔸 Exercício {i}/{len(exercicios)} - {ex['type'].upper()}:")
            print(f"{ex['instruction']}")
            print("\n" + "="*50)
            print(ex['starter'])
            print("="*50)
            
            resposta = input("\n👉 Complete com: ").strip()
            
            if ex['solution'].lower() in resposta.lower():
                self.print_success("✅ Perfeito! Código completado corretamente!")
            else:
                self.print_warning(f"❌ Quase lá! A resposta era: {ex['solution']}")
            
            if i < len(exercicios):
                input("\nPressione ENTER para o próximo exercício...")
        
        self.print_success("🎉 Exercícios de código concluídos!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section("EXERCÍCIO CRIATIVO", "🎨", "accent")
        
        self.print_colored(f"\n🎯 {exercise_data['title']}", "warning")
        self.print_colored(f"{exercise_data['instruction']}", "text")
        
        self.print_colored("\n📝 REQUISITOS:", "info")
        requisitos = [
            "1. Classe base Animal com métodos comuns",
            "2. Pelo menos 3 classes filhas (ex: Leão, Pinguim, Macaco)",
            "3. Cada animal deve ter som e movimento específicos",
            "4. Use polimorfismo em uma lista de animais",
            "5. Seja criativo com os comportamentos!"
        ]
        
        for req in requisitos:
            self.print_colored(f"  {req}", "text")
        
        self.print_colored("\n📊 EXEMPLO DE USO:", "success")
        exemplo = '''# Seu sistema deve funcionar assim:
zoo = [
    Leao("Simba"),
    Pinguim("Pingu"),
    Macaco("George")
]

for animal in zoo:
    animal.fazer_som()    # Polimorfismo!
    animal.mover()        # Cada um se move diferente'''
        
        print(exemplo)
        
        self.print_tip("💡 Este é um exercício para você implementar no seu editor favorito!")
        self.print_colored("Use os conceitos de herança, polimorfismo e seja criativo!", "text")
        
        if input("\nDeseja ver uma solução de exemplo? (s/n): ").lower().startswith('s'):
            self._mostrar_solucao_zoo()
        
        self.pausar()
    
    def _mostrar_solucao_zoo(self) -> None:
        """Mostra exemplo de solução para o exercício criativo"""
        self.print_section("🎆 EXEMPLO DE SOLUÇÃO", "🎆")
        
        codigo_zoo = '''# Sistema de Zoo com OOP Avançado
class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
    
    def fazer_som(self):
        return "Som genérico"
    
    def mover(self):
        return "Movendo-se"
    
    def info(self):
        print(f"{self.nome}: {self.fazer_som()} - {self.mover()}")

class Leao(Animal):
    def fazer_som(self):
        return "ROAAAAR!"
    
    def mover(self):
        return "Correndo pela savana"

class Pinguim(Animal):
    def fazer_som(self):
        return "Quack quack!"
    
    def mover(self):
        return "Deslizando no gelo"

class Macaco(Animal):
    def fazer_som(self):
        return "Oook ook ahh!"
    
    def mover(self):
        return "Saltando entre galhos"

# Polimorfismo em ação
zoo = [Leao("Simba"), Pinguim("Pingu"), Macaco("George")]

for animal in zoo:
    animal.info()  # Cada um se comporta diferente!'''
        
        self.exemplo(codigo_zoo)
        print("\n🚀 EXECUTANDO O EXEMPLO:")
        self.executar_codigo(codigo_zoo)
    
    def _show_help_pratica(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre OOP avançado",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de zoo com herança",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto final",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para aprender melhor!"
        ]

        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()

        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _mini_projeto_sistema_rpg(self) -> None:
        """Mini Projeto - Módulo 19: Sistema de Aventura RPG"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE AVENTURA RPG")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE AVENTURA RPG")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu projeto prático aplicando OOP avançado!")

        self.print_concept(
            "Sistema de Aventura RPG",
            "Um jogo completo onde você pode criar diferentes tipos de heróis, cada um com habilidades únicas, e fazer batalhas épicas!"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Desenvolvimento de jogos mobile (como Clash Royale)",
            "Sistemas de simulação empresarial",
            "Aplicações educacionais interativas",
            "Plataformas de treinamento gamificado"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Escolha do Herói
        self.print_section("PASSO 1: Escolha seu Herói", "📝", "info")
        self.print_tip("Vamos criar um herói personalizado para você!")

        try:
            print("\nEscolha o tipo do seu herói:")
            print("1. ⚔️ Guerreiro (forte e resistente)")
            print("2. 🧙 Mago (mágico e inteligente)")
            print("3. 🏹 Arqueiro (rápido e preciso)")
            
            escolha_heroi = input("\nSua escolha (1-3): ").strip()
            tipos_heroi = {"1": "Guerreiro", "2": "Mago", "3": "Arqueiro"}
            tipo_escolhido = tipos_heroi.get(escolha_heroi, "Guerreiro")
            
            nome_heroi = input(f"\nNome do seu {tipo_escolhido}: ").strip() or "Herói"
            
            self.print_success(f"🎆 {nome_heroi}, o {tipo_escolhido}, foi criado!")

        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Criando Inimigos
        self.print_section("PASSO 2: Gerando Inimigos", "⚙️", "success")
        self.print_colored("Criando inimigos para sua aventura...", "text")

        # PASSO 3: Batalha Épica
        self.print_section("PASSO 3: Batalha Épica!", "🎬", "warning")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo do seu jogo:", "text")

        codigo_final = f'''# 🐍 PROJETO: SISTEMA DE AVENTURA RPG
# Módulo 19: OOP Avançado

from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    """Classe abstrata base para todos os personagens"""
    
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida_max = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.defesa = defesa
    
    @abstractmethod
    def habilidade_especial(self):
        """Cada personagem tem uma habilidade única"""
        pass
    
    @abstractmethod
    def get_tipo(self):
        """Retorna o tipo do personagem"""
        pass
    
    def atacar(self, alvo):
        """Ataque básico - polimorfismo"""
        dano = max(1, self.ataque - alvo.defesa + random.randint(-2, 3))
        alvo.vida_atual = max(0, alvo.vida_atual - dano)
        return dano
    
    def esta_vivo(self):
        return self.vida_atual > 0
    
    def info(self):
        return f"{{self.nome}} ({{self.get_tipo()}}) - Vida: {{self.vida_atual}}/{{self.vida_max}}"

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=120, ataque=25, defesa=15)
    
    def habilidade_especial(self):
        return "Golpe Devastador! (+50% dano)"
    
    def get_tipo(self):
        return "Guerreiro"

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=30, defesa=8)
    
    def habilidade_especial(self):
        return "Bola de Fogo! (ignora defesa)"
    
    def get_tipo(self):
        return "Mago"

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=22, defesa=10)
    
    def habilidade_especial(self):
        return "Tiro Certeiro! (sempre acerta crítico)"
    
    def get_tipo(self):
        return "Arqueiro"

class Orc(Personagem):
    def __init__(self, nome="Orc Selvagem"):
        super().__init__(nome, vida=90, ataque=20, defesa=12)
    
    def habilidade_especial(self):
        return "Grito de Guerra!"
    
    def get_tipo(self):
        return "Orc"

class Esqueleto(Personagem):
    def __init__(self, nome="Esqueleto Guerreiro"):
        super().__init__(nome, vida=70, ataque=18, defesa=8)
    
    def habilidade_especial(self):
        return "Ossos Voadores!"
    
    def get_tipo(self):
        return "Esqueleto"

# Factory Pattern para criar heróis
class HeroiFactory:
    @staticmethod
    def criar_heroi(tipo, nome):
        if tipo == "Guerreiro":
            return Guerreiro(nome)
        elif tipo == "Mago":
            return Mago(nome)
        elif tipo == "Arqueiro":
            return Arqueiro(nome)
        else:
            return Guerreiro(nome)

class SistemaBatalha:
    @staticmethod
    def batalha(heroi, inimigo):
        print(f"\\n⚔️  {{heroi.nome}} vs {{inimigo.nome}}!")
        print("=" * 40)
        
        turno = 1
        while heroi.esta_vivo() and inimigo.esta_vivo():
            print(f"\\nTurno {{turno}}:")
            
            # Turno do herói
            if random.random() < 0.3:  # 30% chance de habilidade especial
                print(f"{{heroi.nome}} usa {{heroi.habilidade_especial()}}")
                dano = heroi.atacar(inimigo) * 1.5
            else:
                dano = heroi.atacar(inimigo)
            
            print(f"{{heroi.nome}} ataca causando {{dano:.0f}} de dano!")
            print(f"{{inimigo.info()}}")
            
            if not inimigo.esta_vivo():
                print(f"\\n🏆 {{heroi.nome}} venceu!")
                break
            
            # Turno do inimigo
            dano_inimigo = inimigo.atacar(heroi)
            print(f"{{inimigo.nome}} contra-ataca causando {{dano_inimigo}} de dano!")
            print(f"{{heroi.info()}}")
            
            if not heroi.esta_vivo():
                print(f"\\n💀 {{inimigo.nome}} venceu...")
                break
            
            turno += 1
            if turno > 10:  # Evita loops infinitos
                print("\\nBatalha muito longa! Empate!")
                break

# === JOGO PRINCIPAL ===
print("🏰 BEM-VINDO AO SISTEMA DE AVENTURA RPG!")
print("=" * 50)

# Criar herói
heroi = HeroiFactory.criar_heroi("{tipo_escolhido}", "{nome_heroi}")
print(f"\\n🎆 Herói criado: {{heroi.info()}}")

# Criar inimigos
inimigos = [Orc(), Esqueleto("Esqueleto do Mal")]

print(f"\\n👹 Inimigos apareceram: {{len(inimigos)}} criaturas!")
for inimigo in inimigos:
    print(f"  - {{inimigo.info()}}")

# Batalhas
for i, inimigo in enumerate(inimigos, 1):
    if heroi.esta_vivo():
        print(f"\\n🗡️ BATALHA {{i}}:")
        SistemaBatalha.batalha(heroi, inimigo)
        
        if heroi.esta_vivo():
            # Recupera um pouco de vida
            cura = min(20, heroi.vida_max - heroi.vida_atual)
            heroi.vida_atual += cura
            print(f"\\n💖 {{heroi.nome}} recuperou {{cura}} pontos de vida!")
    else:
        break

if heroi.esta_vivo():
    print(f"\\n🎉 PARABÉNS! {{heroi.nome}} completou a aventura!")
    print("🏆 VOCÊ É UM VERDADEIRO HERÓI!")
else:
    print(f"\\n💀 {{heroi.nome}} foi derrotado na aventura...")
    print("💪 Tente novamente, herói!")

print("\\n✨ Obrigado por jogar! ✨")'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou seu jogo de aventura RPG!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais tipos de personagens (Paladino, Necromante)",
            "Criar sistema de itens e equipamentos",
            "Implementar sistema de níveis e evolução",
            "Adicionar interface gráfica com Pygame ou Tkinter",
            "Criar multiplayer com sockets"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre em OOP Avançado!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema de Aventura RPG")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo19OopAvancado()
    print("\n" + "="*60)
    print("🚀 TESTE DO MÓDULO 19 - OOP AVANÇADO")
    print("Versão refatorada seguindo padrão pedagógico")
    print("="*60)
    try:
        module._oop_avancado()
    except KeyboardInterrupt:
        print("\n\n👋 Teste interrompido. Até mais!")
    except Exception as e:
        print(f"\n❌ Erro durante o teste: {e}")