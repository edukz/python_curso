#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 18: Programação Orientada a Objetos (OOP) - Básico
Aprenda os fundamentos de classes, objetos e programação orientada a objetos
"""

from ..shared.base_module import BaseModule


class Modulo18OopBasico(BaseModule):
    """Módulo 18: Programação Orientada a Objetos - Básico"""
    
    def __init__(self):
        super().__init__("modulo_18", "OOP - Programação Orientada a Objetos")
        self.has_mini_project = True
        self.mini_project_points = 90
    
    def execute(self) -> None:
        """Executa o módulo sobre OOP básico"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._oop_basico()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _oop_basico(self) -> None:
        """Conteúdo principal do módulo OOP Básico"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS")
        else:
            print("\n" + "="*50)
            print("🏗️ MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo da Programação Orientada a Objetos!")
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
            self._mini_projeto_sistema_loja()
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
                'id': 'secao_conceito_oop',
                'titulo': '🎯 O que é Programação Orientada a Objetos?',
                'descricao': 'Entenda o paradigma que revolucionou a programação',
                'funcao': self._secao_conceito_oop
            },
            {
                'id': 'secao_classes_objetos',
                'titulo': '🏗️ Classes e Objetos',
                'descricao': 'Aprenda a criar moldes e instâncias',
                'funcao': self._secao_classes_objetos
            },
            {
                'id': 'secao_atributos_metodos',
                'titulo': '⚙️ Atributos e Métodos',
                'descricao': 'Características e comportamentos dos objetos',
                'funcao': self._secao_atributos_metodos
            },
            {
                'id': 'secao_construtor',
                'titulo': '🔧 O Construtor __init__',
                'descricao': 'Como inicializar objetos corretamente',
                'funcao': self._secao_construtor
            },
            {
                'id': 'secao_encapsulamento',
                'titulo': '🔒 Encapsulamento e Privacidade',
                'descricao': 'Protegendo dados e controlando acesso',
                'funcao': self._secao_encapsulamento
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 OOP no Mundo Real',
                'descricao': 'Como empresas usam OOP em seus sistemas',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores Práticas em OOP',
                'descricao': 'Dicas de desenvolvedores experientes',
                'funcao': self._secao_melhores_praticas
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
    
    def _secao_conceito_oop(self) -> None:
        """Seção: O que é Programação Orientada a Objetos?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É PROGRAMAÇÃO ORIENTADA A OBJETOS?", "🎯")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Programação Orientada a Objetos (OOP)",
            "É um paradigma de programação que organiza código em 'objetos' - estruturas que combinam dados (atributos) e funções (métodos) que operam sobre esses dados."
        )

        # === DICA RELACIONADA ===
        self.print_tip("OOP é usado em 90% dos sistemas empresariais modernos!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma fábrica de carros. A 'CLASSE' é o projeto/molde do carro.", "text")
        self.print_colored("Cada carro produzido é um 'OBJETO' - uma instância única do projeto.", "text")
        self.print_colored("Todos os carros têm as mesmas características (cor, modelo) e ações (acelerar, frear).", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 OS 4 PILARES DA OOP:", "info")
        pilares = [
            "1. 🏗️ ENCAPSULAMENTO - Agrupa dados e métodos em uma única unidade",
            "2. 🧬 HERANÇA - Classes filhas herdam características das classes pais",
            "3. 🎭 POLIMORFISMO - Objetos diferentes respondem a mesma mensagem de formas diferentes",
            "4. 🎯 ABSTRAÇÃO - Esconde complexidade interna, mostra apenas o necessário"
        ]

        for i, pilar in enumerate(pilares, 1):
            self.print_colored(pilar, "text")
            if i < len(pilares):
                input("   ⏳ Pressione ENTER para o próximo pilar...")

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏦 Sistemas bancários - Classes Conta, Cliente, Transação",
            "🛒 E-commerce - Classes Produto, Carrinho, Pedido, Usuario",
            "🎮 Jogos - Classes Personagem, Arma, Cenário, Inimigo",
            "🏥 Hospitais - Classes Paciente, Médico, Consulta, Exame",
            "🚗 Uber/99 - Classes Motorista, Passageiro, Viagem, Veiculo"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()
    
    def _secao_classes_objetos(self) -> None:
        """Seção: Classes e Objetos"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CLASSES E OBJETOS", "🏗️")

        # === DEFINIÇÃO DUPLA ===
        self.print_concept(
            "Classe",
            "É um molde, modelo ou planta baixa que define como os objetos serão criados. Define atributos e métodos que os objetos terão."
        )

        self.print_concept(
            "Objeto",
            "É uma instância de uma classe - um 'produto' criado a partir do molde. Cada objeto tem seus próprios valores para os atributos."
        )

        # === ANALOGIA VISUAL ===
        self.print_colored("\n🏭 ANALOGIA DA FÁBRICA:", "warning")
        self.print_colored("• CLASSE = Molde de biscoito (formato estrela)", "text")
        self.print_colored("• OBJETO = Cada biscoito individual feito com o molde", "text")
        self.print_colored("• Todos têm formato de estrela, mas podem ter sabores diferentes!", "text")
        input("\n🔸 Pressione ENTER para ver código...")

        # === EXEMPLO BÁSICO ===
        self.print_colored("\n💻 PRIMEIRO EXEMPLO - CLASSE PESSOA:", "success")
        codigo_pessoa = '''# Definindo uma classe
class Pessoa:
    """Classe que representa uma pessoa"""
    
    def __init__(self, nome, idade):
        """Construtor - como criar uma pessoa"""
        self.nome = nome      # Atributo
        self.idade = idade    # Atributo
    
    def cumprimentar(self):
        """Método - ação que a pessoa pode fazer"""
        return f"Olá! Eu sou {self.nome} e tenho {self.idade} anos."

# Criando objetos (instâncias da classe)
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Carlos", 30)

# Usando os objetos
print("=== OBJETOS CRIADOS ===")
print(f"Pessoa 1: {pessoa1.nome}, {pessoa1.idade} anos")
print(f"Pessoa 2: {pessoa2.nome}, {pessoa2.idade} anos")

print("\\n=== OBJETOS EM AÇÃO ===")
print(pessoa1.cumprimentar())
print(pessoa2.cumprimentar())

# Modificando atributos
pessoa1.idade = 26
print(f"\\nApós aniversário: {pessoa1.nome} agora tem {pessoa1.idade} anos")'''

        self.exemplo(codigo_pessoa)
        self.executar_codigo(codigo_pessoa)

        # === EXEMPLO MAIS PRÁTICO ===
        self.print_colored("\n🚗 EXEMPLO PRÁTICO - CLASSE CARRO:", "info")
        codigo_carro = '''class Carro:
    """Classe que representa um carro"""
    
    def __init__(self, marca, modelo, ano):
        """Inicializa um carro"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0      # Todos os carros começam parados
        self.ligado = False      # Todos começam desligados
    
    def ligar(self):
        """Liga o carro"""
        if not self.ligado:
            self.ligado = True
            print(f"🚗 {self.marca} {self.modelo} ligado! Vruuum!")
        else:
            print("🚗 Carro já está ligado!")
    
    def acelerar(self, incremento):
        """Acelera o carro"""
        if self.ligado:
            self.velocidade += incremento
            print(f"🏃 Acelerando! Velocidade: {self.velocidade} km/h")
        else:
            print("🚗 Ligue o carro primeiro!")
    
    def frear(self, decremento):
        """Freia o carro"""
        self.velocidade = max(0, self.velocidade - decremento)
        print(f"🛑 Freando! Velocidade: {self.velocidade} km/h")
    
    def status(self):
        """Mostra status do carro"""
        estado = "ligado" if self.ligado else "desligado"
        print(f"📊 {self.marca} {self.modelo} ({self.ano}) - {estado} - {self.velocidade} km/h")

# Criando uma garagem com vários carros
print("=== CRIANDO CARROS ===")
carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Honda", "Civic", 2023)
carro3 = Carro("Ford", "Mustang", 2024)

# Testando os carros
print("\\n=== TESTANDO CARRO 1 ===")
carro1.status()
carro1.acelerar(30)  # Tentativa sem ligar
carro1.ligar()
carro1.acelerar(30)
carro1.acelerar(20)
carro1.frear(15)
carro1.status()

print("\\n=== TESTANDO CARRO 2 ===")
carro2.ligar()
carro2.acelerar(60)
carro2.status()

print("\\n=== STATUS DE TODOS OS CARROS ===")
carros = [carro1, carro2, carro3]
for i, carro in enumerate(carros, 1):
    print(f"Carro {i}:")
    carro.status()'''

        self.exemplo(codigo_carro)
        self.executar_codigo(codigo_carro)

        self.print_colored("\n🎯 PONTOS IMPORTANTES:", "accent")
        pontos = [
            "• Uma classe pode gerar infinitos objetos",
            "• Cada objeto tem seus próprios valores de atributos",
            "• Todos os objetos da mesma classe têm os mesmos métodos",
            "• Modificar um objeto não afeta os outros"
        ]
        for ponto in pontos:
            self.print_colored(ponto, "primary")

        self.pausar()
    
    def _secao_atributos_metodos(self) -> None:
        """Seção: Atributos e Métodos"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ATRIBUTOS E MÉTODOS", "⚙️")

        # === DEFINIÇÕES ===
        self.print_concept(
            "Atributos",
            "São as características ou propriedades dos objetos. Como variáveis que pertencem ao objeto (ex: nome, idade, cor)."
        )

        self.print_concept(
            "Métodos",
            "São as ações ou comportamentos que os objetos podem executar. Como funções que pertencem ao objeto (ex: falar, andar, calcular)."
        )

        # === ANALOGIA ===
        self.print_colored("\n👤 ANALOGIA PESSOA:", "warning")
        self.print_colored("• ATRIBUTOS: altura, peso, cor dos olhos, nome (características)", "text")
        self.print_colored("• MÉTODOS: falar, andar, dormir, comer (ações)", "text")
        input("\n🔸 Pressione ENTER para ver tipos de atributos...")

        # === TIPOS DE ATRIBUTOS ===
        self.print_colored("\n📊 TIPOS DE ATRIBUTOS:", "info")
        tipos_atributos = [
            "1. 🏠 ATRIBUTOS DE INSTÂNCIA - Únicos para cada objeto",
            "2. 🏢 ATRIBUTOS DE CLASSE - Compartilhados por todos os objetos",
            "3. 🔒 ATRIBUTOS PRIVADOS - Começam com _ (convenção Python)"
        ]

        for tipo in tipos_atributos:
            self.print_colored(tipo, "text")

        input("\n⏳ Pressione ENTER para exemplo completo...")

        # === EXEMPLO COMPLETO ===
        self.print_colored("\n💻 EXEMPLO: CONTA BANCÁRIA COMPLETA:", "success")
        codigo_conta = '''class ContaBancaria:
    """Classe que representa uma conta bancária"""
    
    # Atributo de CLASSE - compartilhado por todas as contas
    banco = "Banco Python"
    taxa_saque = 2.50
    total_contas = 0
    
    def __init__(self, titular, saldo_inicial=0):
        """Construtor - atributos de INSTÂNCIA"""
        # Atributos públicos
        self.titular = titular
        self.numero = ContaBancaria.total_contas + 1
        
        # Atributos "privados" (convenção com _)
        self._saldo = saldo_inicial
        self._historico = []
        
        # Incrementa contador de classe
        ContaBancaria.total_contas += 1
        
        # Registra criação da conta
        self._registrar_operacao(f"Conta criada com saldo inicial: R$ {saldo_inicial}")
        
        print(f"✅ Conta {self.numero} criada para {self.titular}")
    
    # MÉTODOS DE INSTÂNCIA - operam sobre objetos específicos
    def depositar(self, valor):
        """Deposita dinheiro na conta"""
        if valor > 0:
            self._saldo += valor
            self._registrar_operacao(f"Depósito: +R$ {valor:.2f}")
            print(f"💰 Depósito realizado! Saldo: R$ {self._saldo:.2f}")
            return True
        else:
            print("❌ Valor deve ser positivo!")
            return False
    
    def sacar(self, valor):
        """Saca dinheiro da conta"""
        valor_total = valor + ContaBancaria.taxa_saque
        
        if valor <= 0:
            print("❌ Valor deve ser positivo!")
            return False
        
        if valor_total > self._saldo:
            print(f"❌ Saldo insuficiente! (Valor + taxa: R$ {valor_total:.2f})")
            return False
        
        self._saldo -= valor_total
        self._registrar_operacao(f"Saque: -R$ {valor:.2f} (taxa: R$ {ContaBancaria.taxa_saque})")
        print(f"💸 Saque realizado! Saldo: R$ {self._saldo:.2f}")
        return True
    
    def consultar_saldo(self):
        """Consulta saldo atual"""
        print(f"💰 Saldo de {self.titular}: R$ {self._saldo:.2f}")
        return self._saldo
    
    def extrato(self):
        """Mostra extrato da conta"""
        print(f"\\n📄 EXTRATO - CONTA {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Banco: {ContaBancaria.banco}")
        print("-" * 40)
        
        for operacao in self._historico[-5:]:  # Últimas 5 operações
            print(f"  {operacao}")
        
        print("-" * 40)
        print(f"Saldo atual: R$ {self._saldo:.2f}")
        print(f"Taxa de saque: R$ {ContaBancaria.taxa_saque}")
    
    # MÉTODO PRIVADO - só usado internamente
    def _registrar_operacao(self, descricao):
        """Registra operação no histórico"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m %H:%M")
        self._historico.append(f"[{timestamp}] {descricao}")
    
    # MÉTODO DE CLASSE - opera sobre a classe, não sobre instâncias
    @classmethod
    def alterar_taxa_saque(cls, nova_taxa):
        """Altera taxa de saque para todas as contas"""
        taxa_anterior = cls.taxa_saque
        cls.taxa_saque = nova_taxa
        print(f"🏦 Taxa de saque alterada: R$ {taxa_anterior} → R$ {nova_taxa}")
    
    @classmethod
    def relatorio_banco(cls):
        """Relatório geral do banco"""
        print(f"\\n🏦 RELATÓRIO {cls.banco}")
        print(f"📊 Total de contas: {cls.total_contas}")
        print(f"💳 Taxa de saque atual: R$ {cls.taxa_saque}")

# Demonstração do sistema
print("=== SISTEMA BANCÁRIO ===")

# Criando contas
conta1 = ContaBancaria("João Silva", 1000)
conta2 = ContaBancaria("Maria Santos", 500)
conta3 = ContaBancaria("Pedro Costa")

print("\\n=== OPERAÇÕES ===")
# Operações nas contas
conta1.depositar(200)
conta1.sacar(150)
conta2.depositar(300)
conta2.sacar(800)  # Vai falhar

print("\\n=== CONSULTAS ===")
conta1.consultar_saldo()
conta2.consultar_saldo()

# Extrato
conta1.extrato()

print("\\n=== ALTERANDO CONFIGURAÇÕES DO BANCO ===")
# Alterando atributo de classe
ContaBancaria.alterar_taxa_saque(3.00)
conta3.sacar(50)  # Usa nova taxa

# Relatório geral
ContaBancaria.relatorio_banco()

print("\\n🎯 RESUMO DOS CONCEITOS:")
print("✅ Atributos de instância: titular, _saldo, numero")
print("✅ Atributos de classe: banco, taxa_saque, total_contas")
print("✅ Métodos de instância: depositar, sacar, consultar_saldo")
print("✅ Métodos de classe: alterar_taxa_saque, relatorio_banco")
print("✅ Métodos privados: _registrar_operacao")'''

        self.exemplo(codigo_conta)
        self.executar_codigo(codigo_conta)

        self.pausar()
    
    def _secao_construtor(self) -> None:
        """Seção: O Construtor __init__"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("O CONSTRUTOR __init__", "🔧")

        # === DEFINIÇÃO ===
        self.print_concept(
            "Construtor __init__",
            "É um método especial que é executado automaticamente quando um objeto é criado. É onde você inicializa os atributos do objeto."
        )

        # === ANALOGIA ===
        self.print_colored("\n🏗️ ANALOGIA DA CONSTRUÇÃO:", "warning")
        self.print_colored("Quando você constrói uma casa, o construtor:", "text")
        self.print_colored("• Define as fundações (atributos básicos)", "text")
        self.print_colored("• Instala sistemas essenciais (configurações iniciais)", "text")
        self.print_colored("• Deixa a casa pronta para morar (objeto funcional)", "text")
        input("\n🔸 Pressione ENTER para ver exemplo...")

        # === EXEMPLO PROGRESSIVO ===
        self.print_colored("\n💻 EVOLUÇÃO DO CONSTRUTOR:", "success")
        
        # Construtor simples
        codigo_simples = '''# CONSTRUTOR BÁSICO
class Produto:
    def __init__(self, nome, preco):
        """Construtor simples"""
        self.nome = nome
        self.preco = preco
        print(f"✅ Produto '{nome}' criado com preço R$ {preco}")

# Testando
produto1 = Produto("Notebook", 2500)
produto2 = Produto("Mouse", 50)

print(f"Produto 1: {produto1.nome} - R$ {produto1.preco}")
print(f"Produto 2: {produto2.nome} - R$ {produto2.preco}")'''

        self.exemplo(codigo_simples)
        self.executar_codigo(codigo_simples)

        input("\n⏳ Pressione ENTER para construtor com valores padrão...")

        # Construtor com valores padrão
        codigo_padrao = '''# CONSTRUTOR COM VALORES PADRÃO
class Funcionario:
    def __init__(self, nome, cargo="Estagiário", salario=1000):
        """Construtor com valores padrão"""
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.ativo = True        # Valor sempre padrão
        self.id = id(self)       # ID único automático
        
        print(f"👤 {nome} contratado como {cargo}")

# Diferentes formas de criar funcionários
print("=== CRIANDO FUNCIONÁRIOS ===")
func1 = Funcionario("Ana")                                    # Usa padrões
func2 = Funcionario("Bruno", "Desenvolvedor")                 # Especifica cargo
func3 = Funcionario("Carla", "Gerente", 8000)                # Especifica tudo

print(f"\\n{func1.nome}: {func1.cargo} - R$ {func1.salario}")
print(f"{func2.nome}: {func2.cargo} - R$ {func2.salario}")
print(f"{func3.nome}: {func3.cargo} - R$ {func3.salario}")'''

        self.exemplo(codigo_padrao)
        self.executar_codigo(codigo_padrao)

        input("\n⏳ Pressione ENTER para construtor avançado...")

        # Construtor avançado
        codigo_avancado = '''# CONSTRUTOR AVANÇADO COM VALIDAÇÕES
class Usuario:
    total_usuarios = 0
    
    def __init__(self, nome, email, idade=18):
        """Construtor com validações e inicializações avançadas"""
        
        # Validações
        if not nome or len(nome.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        
        if idade < 13:
            raise ValueError("Idade mínima é 13 anos")
        
        # Inicializações
        self.nome = nome.strip().title()
        self.email = email.lower().strip()
        self.idade = idade
        
        # Atributos automáticos
        Usuario.total_usuarios += 1
        self.id = Usuario.total_usuarios
        
        # Configurações baseadas na idade
        if idade >= 18:
            self.tipo = "Adulto"
            self.permissoes = ["comprar", "vender", "contratar"]
        else:
            self.tipo = "Menor"
            self.permissoes = ["comprar"]
        
        # Histórico
        self.historico = []
        self._registrar_evento("Usuário criado")
        
        print(f"🎉 Usuário {self.nome} criado com sucesso!")
        print(f"📧 Email: {self.email}")
        print(f"🎂 Idade: {self.idade} anos ({self.tipo})")
        print(f"🔑 Permissões: {', '.join(self.permissoes)}")
    
    def _registrar_evento(self, evento):
        """Registra evento no histórico"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.historico.append(f"[{timestamp}] {evento}")
    
    def mostrar_info(self):
        """Mostra informações completas"""
        print(f"\\n👤 USUÁRIO #{self.id}: {self.nome}")
        print(f"📧 Email: {self.email}")
        print(f"🎂 Idade: {self.idade} anos ({self.tipo})")
        print(f"🔑 Permissões: {', '.join(self.permissoes)}")
        print(f"📋 Eventos: {len(self.historico)}")

# Testando o construtor avançado
print("=== CRIANDO USUÁRIOS COM VALIDAÇÃO ===")

try:
    user1 = Usuario("João Silva", "joao@email.com", 25)
    user2 = Usuario("Ana Costa", "ana@gmail.com", 16)
    user3 = Usuario("", "invalido")  # Vai dar erro
except ValueError as e:
    print(f"❌ Erro na criação: {e}")

print("\\n=== INFORMAÇÕES DOS USUÁRIOS ===")
user1.mostrar_info()
user2.mostrar_info()

print(f"\\n📊 Total de usuários criados: {Usuario.total_usuarios}")'''

        self.exemplo(codigo_avancado)
        self.executar_codigo(codigo_avancado)

        # === DICAS IMPORTANTES ===
        self.print_colored("\n🎯 DICAS IMPORTANTES SOBRE __init__:", "accent")
        dicas = [
            "• __init__ NÃO retorna nada (não use return)",
            "• self sempre é o primeiro parâmetro",
            "• Pode ter valores padrão nos parâmetros",
            "• Use para validar dados antes de criar o objeto",
            "• Inicialize todos os atributos necessários",
            "• Pode chamar outros métodos durante a inicialização"
        ]
        for dica in dicas:
            self.print_colored(dica, "primary")

        self.pausar()
    
    def _secao_encapsulamento(self) -> None:
        """Seção: Encapsulamento e Privacidade"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ENCAPSULAMENTO E PRIVACIDADE", "🔒")

        # === DEFINIÇÃO ===
        self.print_concept(
            "Encapsulamento",
            "É o princípio de esconder detalhes internos do objeto e controlar como os dados são acessados e modificados. Protege os dados de modificações acidentais."
        )

        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DA CASA:", "warning")
        self.print_colored("• Porta da frente = métodos públicos (qualquer um pode usar)", "text")
        self.print_colored("• Quartos privados = atributos privados (só a família acessa)", "text")
        self.print_colored("• Cofre = dados ultra-protegidos com validação", "text")
        input("\n🔸 Pressione ENTER para ver na prática...")

        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO: CONTA SEGURA COM ENCAPSULAMENTO:", "success")
        codigo_encapsulamento = '''class ContaSegura:
    """Conta bancária com encapsulamento adequado"""
    
    def __init__(self, titular, saldo_inicial=0):
        """Construtor com validação"""
        if not titular or len(titular.strip()) < 2:
            raise ValueError("Titular deve ter pelo menos 2 caracteres")
        
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        
        # Atributos PÚBLICOS - podem ser acessados diretamente
        self.titular = titular.strip().title()
        self.numero = id(self) % 100000  # Número único
        
        # Atributos PRIVADOS - convenção com _ 
        # (Python não impede acesso, mas indica que são internos)
        self._saldo = saldo_inicial
        self._historico = []
        self._limite_credito = 1000
        self._tentativas_senha = 0
        self._bloqueada = False
        
        # Atributos MUITO PRIVADOS - convenção com __
        # (Python "esconde" esses atributos)
        self.__senha = "1234"  # Senha super secreta
        
        print(f"🏦 Conta {self.numero} criada para {self.titular}")
    
    # PROPRIEDADE SOMENTE LEITURA (getter)
    @property
    def saldo(self):
        """Permite consultar saldo, mas não modificar diretamente"""
        if self._bloqueada:
            return "❌ Conta bloqueada"
        return self._saldo
    
    # PROPRIEDADE COM VALIDAÇÃO (getter + setter)
    @property
    def limite_credito(self):
        """Consulta limite de crédito"""
        return self._limite_credito
    
    @limite_credito.setter
    def limite_credito(self, novo_limite):
        """Define novo limite com validação"""
        if novo_limite < 0:
            raise ValueError("Limite não pode ser negativo")
        if novo_limite > 10000:
            raise ValueError("Limite máximo é R$ 10.000")
        
        limite_anterior = self._limite_credito
        self._limite_credito = novo_limite
        print(f"💳 Limite alterado: R$ {limite_anterior} → R$ {novo_limite}")
    
    # MÉTODOS PÚBLICOS - interface para interagir com a conta
    def depositar(self, valor):
        """Deposita dinheiro (método público)"""
        if self._bloqueada:
            print("❌ Conta bloqueada! Não é possível depositar.")
            return False
        
        if valor <= 0:
            print("❌ Valor deve ser positivo!")
            return False
        
        self._saldo += valor
        self._registrar_transacao(f"Depósito: +R$ {valor:.2f}")
        print(f"💰 Depósito realizado! Saldo: R$ {self._saldo:.2f}")
        return True
    
    def sacar(self, valor, senha):
        """Saca dinheiro com verificação de senha"""
        # Verifica se conta está bloqueada
        if self._bloqueada:
            print("❌ Conta bloqueada! Procure uma agência.")
            return False
        
        # Verifica senha
        if not self._verificar_senha(senha):
            return False
        
        # Verifica valor
        if valor <= 0:
            print("❌ Valor deve ser positivo!")
            return False
        
        # Verifica se tem saldo disponível (considerando limite)
        saldo_disponivel = self._saldo + self._limite_credito
        if valor > saldo_disponivel:
            print(f"❌ Saldo insuficiente! Disponível: R$ {saldo_disponivel:.2f}")
            return False
        
        # Realiza o saque
        self._saldo -= valor
        self._registrar_transacao(f"Saque: -R$ {valor:.2f}")
        
        if self._saldo < 0:
            print(f"💸 Saque realizado usando crédito! Saldo: R$ {self._saldo:.2f}")
        else:
            print(f"💸 Saque realizado! Saldo: R$ {self._saldo:.2f}")
        
        return True
    
    def alterar_senha(self, senha_atual, nova_senha):
        """Altera senha com verificação"""
        if not self._verificar_senha(senha_atual):
            return False
        
        if len(nova_senha) < 4:
            print("❌ Nova senha deve ter pelo menos 4 dígitos!")
            return False
        
        self.__senha = nova_senha
        print("🔐 Senha alterada com sucesso!")
        return True
    
    def extrato(self, senha):
        """Mostra extrato com verificação de senha"""
        if not self._verificar_senha(senha):
            return
        
        print(f"\\n📄 EXTRATO - CONTA {self.numero}")
        print(f"👤 Titular: {self.titular}")
        print(f"💰 Saldo atual: R$ {self._saldo:.2f}")
        print(f"💳 Limite de crédito: R$ {self._limite_credito:.2f}")
        print(f"💵 Saldo total disponível: R$ {self._saldo + self._limite_credito:.2f}")
        print("-" * 50)
        
        if self._historico:
            print("📋 Últimas transações:")
            for transacao in self._historico[-5:]:
                print(f"  {transacao}")
        else:
            print("📭 Nenhuma transação realizada")
        
        print("-" * 50)
    
    # MÉTODOS PRIVADOS - uso interno apenas
    def _verificar_senha(self, senha):
        """Verifica senha (método privado)"""
        if senha == self.__senha:
            self._tentativas_senha = 0  # Reset tentativas
            return True
        else:
            self._tentativas_senha += 1
            print(f"❌ Senha incorreta! Tentativa {self._tentativas_senha}/3")
            
            if self._tentativas_senha >= 3:
                self._bloqueada = True
                print("🚫 CONTA BLOQUEADA por excesso de tentativas!")
            
            return False
    
    def _registrar_transacao(self, descricao):
        """Registra transação no histórico (método privado)"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._historico.append(f"[{timestamp}] {descricao}")
    
    # MÉTODO ESPECIAL - representação da conta
    def __str__(self):
        """Representação em string da conta"""
        status = "🟢 Ativa" if not self._bloqueada else "🔴 Bloqueada"
        return f"Conta {self.numero} - {self.titular} - {status}"

# Demonstração do encapsulamento
print("=== CRIANDO CONTA SEGURA ===")
conta = ContaSegura("João Silva", 1000)

print("\\n=== TESTANDO ACESSO AOS DADOS ===")
# Acesso PÚBLICO - permitido
print(f"👤 Titular: {conta.titular}")
print(f"🔢 Número: {conta.numero}")
print(f"💰 Saldo (via propriedade): {conta.saldo}")

# Tentativa de modificar saldo diretamente
print("\\n=== TENTANDO MODIFICAR SALDO DIRETAMENTE ===")
print("Tentando: conta.saldo = 9999")
try:
    conta.saldo = 9999  # Vai dar erro!
except AttributeError as e:
    print(f"❌ Erro: {e}")
    print("✅ Encapsulamento funcionando! Saldo protegido.")

print("\\n=== USANDO PROPRIEDADES ===")
# Usando propriedades com validação
print(f"Limite atual: R$ {conta.limite_credito}")
conta.limite_credito = 2000  # Setter com validação
try:
    conta.limite_credito = -500  # Vai dar erro
except ValueError as e:
    print(f"❌ {e}")

print("\\n=== OPERAÇÕES BANCÁRIAS ===")
# Operações normais
conta.depositar(500)
conta.sacar(200, "1234")  # Senha correta
conta.sacar(100, "0000")  # Senha errada
conta.sacar(100, "0000")  # Senha errada
conta.sacar(100, "0000")  # Terceira tentativa - vai bloquear

print("\\n=== TENTANDO USAR CONTA BLOQUEADA ===")
conta.depositar(100)  # Vai falhar - conta bloqueada

print("\\n🔐 CONCEITOS DEMONSTRADOS:")
print("✅ Atributos públicos: titular, numero")
print("✅ Atributos privados: _saldo, _historico, _limite_credito")
print("✅ Atributos muito privados: __senha")
print("✅ Propriedades com getter/setter: saldo, limite_credito")
print("✅ Métodos públicos: depositar, sacar, extrato")
print("✅ Métodos privados: _verificar_senha, _registrar_transacao")
print("✅ Validações e proteções automáticas")'''

        self.exemplo(codigo_encapsulamento)
        self.executar_codigo(codigo_encapsulamento)

        # === RESUMO ===
        self.print_colored("\n🎯 NÍVEIS DE PRIVACIDADE EM PYTHON:", "accent")
        niveis = [
            "• atributo → PÚBLICO: acesso livre",
            "• _atributo → PRIVADO: convenção, uso interno",
            "• __atributo → MUITO PRIVADO: Python 'esconde' o nome"
        ]
        for nivel in niveis:
            self.print_colored(nivel, "primary")

        self.pausar()
    
    def _secao_casos_uso(self) -> None:
        """Seção: OOP no Mundo Real"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("OOP NO MUNDO REAL", "🌍")

        self.print_colored("Veja como grandes empresas usam OOP em seus sistemas:", "text")

        # === CASOS REAIS ===
        casos = [
            {
                'empresa': '🛒 AMAZON',
                'classes': ['Usuario', 'Produto', 'Carrinho', 'Pedido', 'Pagamento'],
                'exemplo': 'Cada produto é um objeto com preço, estoque, avaliações'
            },
            {
                'empresa': '🎮 RIOT GAMES (League of Legends)',
                'classes': ['Campeao', 'Habilidade', 'Item', 'Partida', 'Jogador'],
                'exemplo': 'Cada campeão herda de uma classe base com vida, mana, ataque'
            },
            {
                'empresa': '🏦 NUBANK',
                'classes': ['Cliente', 'Conta', 'Cartao', 'Transacao', 'Emprestimo'],
                'exemplo': 'Cada transação é um objeto com valor, data, categoria'
            },
            {
                'empresa': '🚗 UBER',
                'classes': ['Motorista', 'Passageiro', 'Viagem', 'Veiculo', 'Pagamento'],
                'exemplo': 'Cada viagem conecta motorista e passageiro com preço dinâmico'
            }
        ]

        for caso in casos:
            print(f"\n{caso['empresa']}")
            self.print_colored(f"Classes principais: {', '.join(caso['classes'])}", "accent")
            self.print_colored(f"💡 {caso['exemplo']}", "text")
            input("   ⏳ Pressione ENTER para próximo caso...")

        # === EXEMPLO PRÁTICO INSPIRADO NO MUNDO REAL ===
        self.print_colored("\n💻 EXEMPLO: SISTEMA INSPIRADO NO NETFLIX:", "success")
        codigo_netflix = '''# Sistema de streaming inspirado no Netflix
class Usuario:
    """Representa um usuário da plataforma"""
    
    def __init__(self, nome, email, plano="basico"):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.historico_assistido = []
        self.lista_favoritos = []
        self.tempo_total_assistido = 0  # em minutos
    
    def assistir(self, conteudo, minutos_assistidos):
        """Registra que o usuário assistiu um conteúdo"""
        self.historico_assistido.append({
            'conteudo': conteudo.titulo,
            'minutos': minutos_assistidos,
            'data': 'hoje'
        })
        self.tempo_total_assistido += minutos_assistidos
        conteudo.registrar_visualizacao(minutos_assistidos)
        print(f"📺 {self.nome} assistiu {minutos_assistidos} min de '{conteudo.titulo}'")
    
    def adicionar_favorito(self, conteudo):
        """Adiciona conteúdo aos favoritos"""
        if conteudo not in self.lista_favoritos:
            self.lista_favoritos.append(conteudo)
            print(f"❤️ '{conteudo.titulo}' adicionado aos favoritos de {self.nome}")

class Conteudo:
    """Classe base para filmes e séries"""
    
    def __init__(self, titulo, genero, classificacao, duracao):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao  # "Livre", "12+", "16+", "18+"
        self.duracao = duracao  # em minutos
        self.total_visualizacoes = 0
        self.tempo_total_assistido = 0
        self.avaliacoes = []
    
    def registrar_visualizacao(self, minutos):
        """Registra visualização do conteúdo"""
        self.total_visualizacoes += 1
        self.tempo_total_assistido += minutos
    
    def adicionar_avaliacao(self, nota, comentario=""):
        """Adiciona avaliação do usuário"""
        if 1 <= nota <= 5:
            self.avaliacoes.append({'nota': nota, 'comentario': comentario})
            print(f"⭐ Avaliação {nota}/5 adicionada para '{self.titulo}'")
    
    def media_avaliacoes(self):
        """Calcula média das avaliações"""
        if not self.avaliacoes:
            return 0
        return sum(av['nota'] for av in self.avaliacoes) / len(self.avaliacoes)

class Filme(Conteudo):
    """Classe específica para filmes"""
    
    def __init__(self, titulo, genero, classificacao, duracao, diretor, ano):
        super().__init__(titulo, genero, classificacao, duracao)
        self.diretor = diretor
        self.ano = ano
        self.tipo = "Filme"
    
    def info(self):
        """Informações do filme"""
        media = self.media_avaliacoes()
        return f"🎬 {self.titulo} ({self.ano}) - {self.diretor}\\n" \\
               f"   Gênero: {self.genero} | Duração: {self.duracao}min | " \\
               f"Nota: {media:.1f}/5"

class Serie(Conteudo):
    """Classe específica para séries"""
    
    def __init__(self, titulo, genero, classificacao, temporadas, episodios_por_temp):
        # Calcula duração total estimada (40 min por episódio)
        duracao_total = temporadas * episodios_por_temp * 40
        super().__init__(titulo, genero, classificacao, duracao_total)
        
        self.temporadas = temporadas
        self.episodios_por_temporada = episodios_por_temp
        self.tipo = "Série"
    
    def info(self):
        """Informações da série"""
        media = self.media_avaliacoes()
        total_eps = self.temporadas * self.episodios_por_temporada
        return f"📺 {self.titulo}\\n" \\
               f"   {self.temporadas} temporadas | {total_eps} episódios | " \\
               f"Gênero: {self.genero} | Nota: {media:.1f}/5"

class Plataforma:
    """Sistema principal da plataforma de streaming"""
    
    def __init__(self, nome):
        self.nome = nome
        self.usuarios = []
        self.catalogo = []
        self.total_minutos_assistidos = 0
    
    def adicionar_usuario(self, usuario):
        """Adiciona novo usuário"""
        self.usuarios.append(usuario)
        print(f"✅ {usuario.nome} cadastrado na {self.nome}")
    
    def adicionar_conteudo(self, conteudo):
        """Adiciona conteúdo ao catálogo"""
        self.catalogo.append(conteudo)
        print(f"➕ '{conteudo.titulo}' adicionado ao catálogo")
    
    def buscar_por_genero(self, genero):
        """Busca conteúdos por gênero"""
        resultados = [c for c in self.catalogo if genero.lower() in c.genero.lower()]
        return resultados
    
    def top_conteudos(self, limite=5):
        """Lista os conteúdos mais assistidos"""
        ordenados = sorted(self.catalogo, 
                          key=lambda c: c.total_visualizacoes, 
                          reverse=True)
        return ordenados[:limite]
    
    def relatorio_uso(self):
        """Relatório de uso da plataforma"""
        total_usuarios = len(self.usuarios)
        total_conteudos = len(self.catalogo)
        total_visualizacoes = sum(c.total_visualizacoes for c in self.catalogo)
        
        print(f"\\n📊 RELATÓRIO {self.nome}")
        print(f"👥 Usuários: {total_usuarios}")
        print(f"🎬 Conteúdos: {total_conteudos}")
        print(f"📺 Total de visualizações: {total_visualizacoes}")
        
        if self.catalogo:
            print("\\n🏆 TOP 3 MAIS ASSISTIDOS:")
            for i, conteudo in enumerate(self.top_conteudos(3), 1):
                print(f"{i}. {conteudo.titulo} - {conteudo.total_visualizacoes} views")

# Demonstração do sistema
print("=== CRIANDO PLATAFORMA DE STREAMING ===")

# Criando a plataforma
netflix_python = Plataforma("Netflix Python")

# Criando conteúdos
filme1 = Filme("O Algoritmo", "Ficção Científica", "12+", 120, "Ana Codes", 2023)
filme2 = Filme("Python: O Filme", "Documentário", "Livre", 90, "João Dev", 2024)
serie1 = Serie("House of Code", "Drama", "16+", 3, 10)
serie2 = Serie("Breaking Bug", "Suspense", "18+", 5, 12)

# Adicionando ao catálogo
for conteudo in [filme1, filme2, serie1, serie2]:
    netflix_python.adicionar_conteudo(conteudo)

# Criando usuários
user1 = Usuario("Maria Silva", "maria@email.com", "premium")
user2 = Usuario("João Santos", "joao@email.com", "básico")

for usuario in [user1, user2]:
    netflix_python.adicionar_usuario(usuario)

print("\\n=== USUÁRIOS ASSISTINDO CONTEÚDOS ===")
# Simulando uso da plataforma
user1.assistir(filme1, 120)  # Assistiu filme completo
user1.assistir(serie1, 200)  # Assistiu alguns episódios
user1.adicionar_favorito(serie1)

user2.assistir(filme2, 45)   # Assistiu parcialmente
user2.assistir(serie2, 300)  # Maratonou
user2.adicionar_favorito(filme1)

print("\\n=== AVALIAÇÕES ===")
# Avaliações
filme1.adicionar_avaliacao(5, "Incrível!")
filme1.adicionar_avaliacao(4, "Muito bom")
serie1.adicionar_avaliacao(5, "Melhor série!")

print("\\n=== INFORMAÇÕES DOS CONTEÚDOS ===")
# Mostrando informações
for conteudo in netflix_python.catalogo:
    print(conteudo.info())

# Relatório final
netflix_python.relatorio_uso()

print("\\n🎯 CONCEITOS OOP DEMONSTRADOS:")
print("✅ Herança: Filme e Serie herdam de Conteudo")
print("✅ Encapsulamento: Dados protegidos nas classes")
print("✅ Composição: Plataforma contém Usuarios e Conteudos")
print("✅ Polimorfismo: Filme e Serie implementam info() diferente")
print("✅ Abstração: Interface simples para operações complexas")'''

        self.exemplo(codigo_netflix)
        self.executar_codigo(codigo_netflix)

        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores Práticas em OOP"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("MELHORES PRÁTICAS EM OOP", "⭐")

        self.print_colored("Dicas de desenvolvedores experientes para escrever código OOP de qualidade:", "text")

        # === PRÁTICAS ESSENCIAIS ===
        praticas = [
            {
                'titulo': '📝 1. NOMES DESCRITIVOS',
                'regra': 'Use nomes que expliquem claramente o propósito',
                'bom': 'class ContaBancaria, def calcular_juros()',
                'ruim': 'class CB, def calc()'
            },
            {
                'titulo': '🔧 2. RESPONSABILIDADE ÚNICA',
                'regra': 'Cada classe deve ter apenas uma responsabilidade',
                'bom': 'class Usuario (só gerencia usuários)',
                'ruim': 'class UsuarioEmailPagamento (faz muitas coisas)'
            },
            {
                'titulo': '🔒 3. ENCAPSULAMENTO ADEQUADO',
                'regra': 'Proteja dados internos e forneça interface clara',
                'bom': 'self._saldo com métodos depositar/sacar',
                'ruim': 'self.saldo modificado diretamente'
            },
            {
                'titulo': '📚 4. DOCUMENTAÇÃO CLARA',
                'regra': 'Docstrings em classes e métodos importantes',
                'bom': '"""Classe que gerencia contas bancárias"""',
                'ruim': 'Sem documentação'
            },
            {
                'titulo': '⚡ 5. MÉTODOS PEQUENOS',
                'regra': 'Métodos devem fazer uma coisa e fazer bem',
                'bom': 'def validar_email(), def enviar_email()',
                'ruim': 'def processar_usuario() (100 linhas)'
            }
        ]

        for i, pratica in enumerate(praticas, 1):
            print(f"\n{pratica['titulo']}")
            self.print_colored(f"📋 Regra: {pratica['regra']}", "info")
            self.print_colored(f"✅ Bom: {pratica['bom']}", "success")
            self.print_colored(f"❌ Ruim: {pratica['ruim']}", "warning")
            
            if i < len(praticas):
                input("   ⏳ Pressione ENTER para próxima prática...")

        # === EXEMPLO PRÁTICO ===
        input("\n🔸 Pressione ENTER para ver exemplo prático...")
        
        self.print_colored("\n💻 EXEMPLO: REFATORAÇÃO DE CÓDIGO RUIM PARA BOM:", "success")
        codigo_praticas = '''# ❌ CÓDIGO RUIM - Violando várias práticas
class u:  # Nome não descritivo
    def __init__(self, n, e, s):  # Parâmetros não descritivos
        self.n = n
        self.e = e
        self.s = s        # Saldo público (sem proteção)
        self.h = []       # Histórico público
    
    def p(self, v):       # Nome não descritivo
        self.s += v       # Modifica saldo diretamente
        self.h.append(f"Dep: {v}")
        print(f"OK: {self.s}")
        # Enviar email (responsabilidade extra!)
        print(f"Email enviado para {self.e}")
        # Calcular impostos (responsabilidade extra!)
        imposto = v * 0.1
        print(f"Imposto: {imposto}")

# ✅ CÓDIGO BOM - Seguindo melhores práticas
class ContaBancaria:
    """
    Classe que representa uma conta bancária.
    
    Responsabilidades:
    - Gerenciar saldo da conta
    - Registrar transações
    - Validar operações
    """
    
    def __init__(self, titular: str, email: str, saldo_inicial: float = 0):
        """
        Inicializa uma nova conta bancária.
        
        Args:
            titular: Nome do titular da conta
            email: Email do titular
            saldo_inicial: Saldo inicial da conta (padrão: 0)
        """
        self._validar_dados_iniciais(titular, email, saldo_inicial)
        
        # Atributos públicos
        self.titular = titular.strip().title()
        self.email = email.lower().strip()
        self.numero_conta = self._gerar_numero_conta()
        
        # Atributos protegidos
        self._saldo = saldo_inicial
        self._historico_transacoes = []
        self._conta_ativa = True
        
        self._registrar_transacao("Conta criada", saldo_inicial)
        print(f"✅ Conta {self.numero_conta} criada para {self.titular}")
    
    @property
    def saldo(self) -> float:
        """Consulta o saldo atual da conta."""
        if not self._conta_ativa:
            raise ValueError("Conta inativa")
        return self._saldo
    
    def depositar(self, valor: float) -> bool:
        """
        Deposita dinheiro na conta.
        
        Args:
            valor: Valor a ser depositado
            
        Returns:
            True se o depósito foi realizado, False caso contrário
        """
        if not self._validar_valor_operacao(valor):
            return False
        
        if not self._conta_ativa:
            print("❌ Não é possível depositar em conta inativa")
            return False
        
        self._saldo += valor
        self._registrar_transacao("Depósito", valor)
        print(f"💰 Depósito realizado! Saldo: R$ {self._saldo:.2f}")
        return True
    
    def sacar(self, valor: float) -> bool:
        """
        Saca dinheiro da conta.
        
        Args:
            valor: Valor a ser sacado
            
        Returns:
            True se o saque foi realizado, False caso contrário
        """
        if not self._validar_valor_operacao(valor):
            return False
        
        if not self._conta_ativa:
            print("❌ Não é possível sacar de conta inativa")
            return False
        
        if valor > self._saldo:
            print(f"❌ Saldo insuficiente! Saldo: R$ {self._saldo:.2f}")
            return False
        
        self._saldo -= valor
        self._registrar_transacao("Saque", -valor)
        print(f"💸 Saque realizado! Saldo: R$ {self._saldo:.2f}")
        return True
    
    def obter_extrato(self, ultimas_transacoes: int = 10) -> list:
        """
        Retorna o extrato das transações.
        
        Args:
            ultimas_transacoes: Número de transações a retornar
            
        Returns:
            Lista com as últimas transações
        """
        return self._historico_transacoes[-ultimas_transacoes:]
    
    def desativar_conta(self) -> None:
        """Desativa a conta bancária."""
        self._conta_ativa = False
        self._registrar_transacao("Conta desativada", 0)
        print(f"🔒 Conta {self.numero_conta} desativada")
    
    # Métodos privados - uso interno apenas
    def _validar_dados_iniciais(self, titular: str, email: str, saldo: float) -> None:
        """Valida dados fornecidos na criação da conta."""
        if not titular or len(titular.strip()) < 2:
            raise ValueError("Titular deve ter pelo menos 2 caracteres")
        
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
    
    def _validar_valor_operacao(self, valor: float) -> bool:
        """Valida valor para operações bancárias."""
        if valor <= 0:
            print("❌ Valor deve ser maior que zero")
            return False
        
        if valor > 10000:
            print("❌ Valor máximo por operação: R$ 10.000")
            return False
        
        return True
    
    def _gerar_numero_conta(self) -> str:
        """Gera número único da conta."""
        import random
        return f"{random.randint(10000, 99999)}-{random.randint(0, 9)}"
    
    def _registrar_transacao(self, tipo: str, valor: float) -> None:
        """Registra transação no histórico."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        transacao = {
            'data': timestamp,
            'tipo': tipo,
            'valor': valor,
            'saldo_apos': self._saldo
        }
        
        self._historico_transacoes.append(transacao)
    
    def __str__(self) -> str:
        """Representação em string da conta."""
        status = "🟢 Ativa" if self._conta_ativa else "🔴 Inativa"
        return f"Conta {self.numero_conta} - {self.titular} - {status}"

# Classe separada para responsabilidades específicas
class NotificadorEmail:
    """Classe responsável apenas por enviar notificações por email."""
    
    @staticmethod
    def enviar_notificacao_deposito(email: str, valor: float) -> None:
        """Envia notificação de depósito por email."""
        print(f"📧 Email enviado para {email}: Depósito de R$ {valor:.2f} realizado")
    
    @staticmethod
    def enviar_notificacao_saque(email: str, valor: float) -> None:
        """Envia notificação de saque por email."""
        print(f"📧 Email enviado para {email}: Saque de R$ {valor:.2f} realizado")

class CalculadoraImpostos:
    """Classe responsável apenas por cálculos de impostos."""
    
    @staticmethod
    def calcular_imposto_deposito(valor: float) -> float:
        """Calcula imposto sobre depósito."""
        return valor * 0.001  # 0.1% sobre depósitos
    
    @staticmethod
    def calcular_imposto_saque(valor: float) -> float:
        """Calcula imposto sobre saque."""
        return valor * 0.002  # 0.2% sobre saques

# Demonstração das melhorias
print("=== COMPARANDO ABORDAGENS ===")

print("\\n❌ Código ruim em ação:")
conta_ruim = u("João", "joao@email.com", 1000)
conta_ruim.p(500)  # Método confuso que faz muitas coisas

print("\\n✅ Código bom em ação:")
conta_boa = ContaBancaria("Maria Silva", "maria@email.com", 1000)

# Operações claras e bem separadas
conta_boa.depositar(500)

# Notificação separada (responsabilidade única)
NotificadorEmail.enviar_notificacao_deposito(conta_boa.email, 500)

# Cálculo de imposto separado (responsabilidade única)
imposto = CalculadoraImpostos.calcular_imposto_deposito(500)
print(f"💰 Imposto calculado: R$ {imposto:.2f}")

# Extrato bem formatado
print(f"\\n📄 Extrato: {len(conta_boa.obter_extrato())} transações registradas")

print(f"\\n📊 Status: {conta_boa}")
print(f"💰 Saldo (seguro): R$ {conta_boa.saldo:.2f}")

print("\\n🎯 MELHORIAS APLICADAS:")
print("✅ Nomes descritivos e claros")
print("✅ Responsabilidade única por classe")
print("✅ Encapsulamento adequado")
print("✅ Documentação completa")
print("✅ Métodos pequenos e focados")
print("✅ Validações robustas")
print("✅ Separação de responsabilidades")'''

        self.exemplo(codigo_praticas)
        self.executar_codigo(codigo_praticas)

        # === CHECKLIST FINAL ===
        self.print_colored("\n✅ CHECKLIST PARA CÓDIGO OOP DE QUALIDADE:", "accent")
        checklist = [
            "□ Nomes de classes começam com maiúscula (PascalCase)",
            "□ Métodos e atributos usam snake_case",
            "□ Cada classe tem uma responsabilidade clara",
            "□ Atributos importantes são privados (_atributo)",
            "□ Métodos fazem uma coisa só",
            "□ Docstrings em classes e métodos principais",
            "□ Validações adequadas nos métodos públicos",
            "□ Uso de propriedades (@property) quando necessário"
        ]
        
        for item in checklist:
            self.print_colored(item, "primary")

        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos sobre OOP!", "text")

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
                'title': 'Quiz: Conhecimentos sobre OOP',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é o método especial usado como construtor em Python?',
                        'answer': ['__init__', '__init__()', 'init', 'init()', '__new__'],
                        'hint': 'É um método especial que começa e termina com dois underscores'
                    },
                    {
                        'question': 'O que representa "self" nos métodos de uma classe?',
                        'answer': ['instância atual', 'objeto atual', 'referência ao objeto', 'próprio objeto'],
                        'hint': 'É sempre o primeiro parâmetro dos métodos de instância'
                    },
                    {
                        'question': 'Qual convenção indica que um atributo é privado em Python?',
                        'answer': ['underscore', '_', 'começa com _', 'começar com underscore'],
                        'hint': 'É uma convenção visual que indica uso interno'
                    },
                    {
                        'question': 'Como você cria um objeto a partir de uma classe chamada "Carro"?',
                        'answer': ['Carro()', 'objeto = Carro()', 'instancia = Carro()'],
                        'hint': 'É como chamar uma função com o nome da classe'
                    },
                    {
                        'question': 'Qual é o principal benefício do encapsulamento?',
                        'answer': ['proteção de dados', 'proteger dados', 'controlar acesso', 'segurança'],
                        'hint': 'Impede modificações acidentais nos dados internos do objeto'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código OOP',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a definição da classe Pessoa',
                        'starter': 'class Pessoa:\n    def __init__(self, nome, idade):\n        # Complete aqui\n        pass\n    \n    def cumprimentar(self):\n        return f"Olá, eu sou {self.nome}"',
                        'solution': 'self.nome = nome\n        self.idade = idade',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o método depositar da classe Conta',
                        'starter': 'class Conta:\n    def __init__(self, saldo=0):\n        self._saldo = saldo\n    \n    def depositar(self, valor):\n        if valor > 0:\n            # Complete aqui\n            print(f"Depósito realizado! Saldo: R$ {self._saldo}")\n            return True\n        return False',
                        'solution': 'self._saldo += valor',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a propriedade saldo com getter',
                        'starter': '@property\ndef saldo(self):\n    # Complete aqui\n    \n@saldo.setter\ndef saldo(self, valor):\n    if valor >= 0:\n        self._saldo = valor',
                        'solution': 'return self._saldo',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Biblioteca',
                'type': 'creative',
                'instruction': 'Vamos criar um sistema de biblioteca usando OOP! Você definirá as classes Livro, Usuario e Biblioteca, aplicando conceitos de encapsulamento e métodos.'
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
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                elif escolha in ["3", "criativo"]:
                    try:
                        self._run_creative_exercise(exercicios[2])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre OOP básico",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de biblioteca com classes",
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

    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo sobre OOP"""
        self.print_section(quiz_data['title'], "📝")
        score = 0
        total_questions = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            print(f"\n📝 Pergunta {i} de {total_questions}:")
            correto = self.exercicio(
                q['question'],
                q['answer'],
                q['hint']
            )
            if correto:
                score += 1
        
        # Feedback detalhado baseado na pontuação
        percentage = (score / total_questions) * 100
        
        self.print_success(f"\n🏆 RESULTADO: {score} de {total_questions} perguntas corretas ({percentage:.0f}%)")
        
        if percentage == 100:
            self.print_success("🌟 PERFEITO! Você dominou OOP básico!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você tem um bom entendimento!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo.", "info")
            
        self.pausar()

    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código OOP"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código para Completar", ex['starter'])
            
            print("\n✍️ Complete a linha que falta:")
            print(f"💡 Dica: Complete a linha marcada com '# Complete aqui'")
            user_input = input(">>> ").strip()
            
            if user_input:
                user_code = user_input
            else:
                user_code = ex['solution']
                self.print_tip("Usando solução padrão.")
            
            # Substitui a linha que contém o comentário
            lines = ex['starter'].split('\n')
            for j, line in enumerate(lines):
                if '# Complete aqui' in line:
                    # Mantém a indentação original
                    indent = len(line) - len(line.lstrip())
                    lines[j] = ' ' * indent + user_code
                    break
            complete_code = '\n'.join(lines)
            
            print("\n🚀 Executando seu código completo:")
            self.executar_codigo(complete_code)
            
            # Verifica se a resposta está correta
            if user_input and user_input.strip() == ex['solution'].strip():
                self.print_success("✅ PERFEITO! Você acertou a solução!")
            else:
                print(f"\n💡 Solução correta: {ex['solution']}")
                self.print_colored("📚 Não se preocupe! O importante é aprender.", "info")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()

    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo de sistema de biblioteca"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        
        # Sistema interativo de biblioteca
        self.print_colored("\n📚 VAMOS CRIAR SEU SISTEMA DE BIBLIOTECA!", "success")
        
        # Criação interativa das classes
        codigo_biblioteca = '''# 📚 SISTEMA DE BIBLIOTECA - EXERCÍCIO CRIATIVO
# Criado pelo usuário aplicando conceitos de OOP

class Livro:
    """Classe que representa um livro da biblioteca"""
    
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.emprestado_para = None
        self.data_emprestimo = None
    
    def emprestar(self, usuario, data):
        """Empresta o livro para um usuário"""
        if self.disponivel:
            self.disponivel = False
            self.emprestado_para = usuario
            self.data_emprestimo = data
            print(f"📖 '{self.titulo}' emprestado para {usuario}")
            return True
        else:
            print(f"❌ '{self.titulo}' já está emprestado")
            return False
    
    def devolver(self):
        """Devolve o livro para a biblioteca"""
        if not self.disponivel:
            print(f"📚 '{self.titulo}' devolvido por {self.emprestado_para}")
            self.disponivel = True
            self.emprestado_para = None
            self.data_emprestimo = None
            return True
        else:
            print(f"⚠️ '{self.titulo}' já está disponível")
            return False
    
    def info(self):
        """Retorna informações do livro"""
        status = "📗 Disponível" if self.disponivel else f"📕 Emprestado para {self.emprestado_para}"
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao}) - {status}"

class Usuario:
    """Classe que representa um usuário da biblioteca"""
    
    def __init__(self, nome, email, tipo="comum"):
        self.nome = nome
        self.email = email
        self.tipo = tipo  # "comum" ou "premium"
        self.livros_emprestados = []
        self.historico_emprestimos = []
        
        # Limite baseado no tipo de usuário
        self.limite_emprestimos = 5 if tipo == "premium" else 3
    
    def pode_emprestar(self):
        """Verifica se o usuário pode pegar mais livros"""
        return len(self.livros_emprestados) < self.limite_emprestimos
    
    def emprestar_livro(self, livro):
        """Registra empréstimo de livro para o usuário"""
        if self.pode_emprestar():
            self.livros_emprestados.append(livro)
            self.historico_emprestimos.append(livro.titulo)
            return True
        else:
            print(f"❌ {self.nome} atingiu o limite de {self.limite_emprestimos} livros")
            return False
    
    def devolver_livro(self, livro):
        """Remove livro da lista de emprestados"""
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            return True
        return False
    
    def status(self):
        """Mostra status do usuário"""
        print(f"\\n👤 {self.nome} ({self.tipo})")
        print(f"📧 {self.email}")
        print(f"📚 Livros emprestados: {len(self.livros_emprestados)}/{self.limite_emprestimos}")
        
        if self.livros_emprestados:
            print("📖 Livros atuais:")
            for livro in self.livros_emprestados:
                print(f"  • {livro.titulo}")

class Biblioteca:
    """Sistema principal da biblioteca"""
    
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.usuarios = []
        print(f"🏛️ Biblioteca '{nome}' criada!")
    
    def adicionar_livro(self, livro):
        """Adiciona livro ao acervo"""
        self.livros.append(livro)
        print(f"➕ Livro '{livro.titulo}' adicionado ao acervo")
    
    def cadastrar_usuario(self, usuario):
        """Cadastra novo usuário"""
        self.usuarios.append(usuario)
        print(f"✅ Usuário {usuario.nome} cadastrado")
    
    def buscar_livro(self, titulo):
        """Busca livro por título"""
        for livro in self.livros:
            if titulo.lower() in livro.titulo.lower():
                return livro
        return None
    
    def buscar_usuario(self, nome):
        """Busca usuário por nome"""
        for usuario in self.usuarios:
            if nome.lower() in usuario.nome.lower():
                return usuario
        return None
    
    def emprestar_livro(self, titulo_livro, nome_usuario):
        """Realiza empréstimo de livro"""
        livro = self.buscar_livro(titulo_livro)
        usuario = self.buscar_usuario(nome_usuario)
        
        if not livro:
            print(f"❌ Livro '{titulo_livro}' não encontrado")
            return False
        
        if not usuario:
            print(f"❌ Usuário '{nome_usuario}' não encontrado")
            return False
        
        if not usuario.pode_emprestar():
            return False
        
        if livro.emprestar(usuario.nome, "hoje"):
            usuario.emprestar_livro(livro)
            return True
        
        return False
    
    def devolver_livro(self, titulo_livro, nome_usuario):
        """Realiza devolução de livro"""
        livro = self.buscar_livro(titulo_livro)
        usuario = self.buscar_usuario(nome_usuario)
        
        if livro and usuario:
            if livro.devolver():
                usuario.devolver_livro(livro)
                return True
        
        return False
    
    def relatorio_acervo(self):
        """Mostra relatório do acervo"""
        total_livros = len(self.livros)
        disponiveis = sum(1 for livro in self.livros if livro.disponivel)
        emprestados = total_livros - disponiveis
        
        print(f"\\n📊 RELATÓRIO {self.nome}")
        print(f"📚 Total de livros: {total_livros}")
        print(f"📗 Disponíveis: {disponiveis}")
        print(f"📕 Emprestados: {emprestados}")
        print(f"👥 Usuários cadastrados: {len(self.usuarios)}")

# DEMONSTRAÇÃO DO SISTEMA
print("=== CRIANDO SISTEMA DE BIBLIOTECA ===")

# Criando a biblioteca
minha_biblioteca = Biblioteca("Biblioteca Python")

# Adicionando livros
livros = [
    Livro("Clean Code", "Robert Martin", "978-0132350884", 2008),
    Livro("Python Fluente", "Luciano Ramalho", "978-8575224625", 2015),
    Livro("Design Patterns", "Gang of Four", "978-0201633612", 1994),
    Livro("Algoritmos", "Thomas Cormen", "978-8535236996", 2012)
]

for livro in livros:
    minha_biblioteca.adicionar_livro(livro)

# Cadastrando usuários
usuarios = [
    Usuario("Ana Silva", "ana@email.com", "premium"),
    Usuario("João Santos", "joao@email.com", "comum"),
    Usuario("Maria Costa", "maria@email.com", "comum")
]

for usuario in usuarios:
    minha_biblioteca.cadastrar_usuario(usuario)

print("\\n=== REALIZANDO EMPRÉSTIMOS ===")
# Empréstimos
minha_biblioteca.emprestar_livro("Clean Code", "Ana Silva")
minha_biblioteca.emprestar_livro("Python Fluente", "João Santos")
minha_biblioteca.emprestar_livro("Design Patterns", "Ana Silva")

print("\\n=== STATUS DOS USUÁRIOS ===")
# Status dos usuários
for usuario in usuarios:
    usuario.status()

print("\\n=== INFORMAÇÕES DOS LIVROS ===")
# Info dos livros
for livro in livros:
    print(livro.info())

print("\\n=== DEVOLVENDO LIVRO ===")
# Devolução
minha_biblioteca.devolver_livro("Clean Code", "Ana Silva")

# Relatório final
minha_biblioteca.relatorio_acervo()

print("\\n🎯 CONCEITOS OOP APLICADOS:")
print("✅ Classes com responsabilidades claras")
print("✅ Encapsulamento de dados")
print("✅ Métodos públicos bem definidos")
print("✅ Interação entre objetos")
print("✅ Estado dos objetos controlado")'''
        
        self.exemplo(codigo_biblioteca)
        self.executar_codigo(codigo_biblioteca)
        
        self.print_success("\n🏆 PARABÉNS! Você criou um sistema completo usando OOP!")
        self.pausar()
    
    def _mini_projeto_sistema_loja(self) -> None:
        """Mini Projeto - Módulo 18: Sistema de E-commerce com OOP"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE E-COMMERCE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE E-COMMERCE")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema de loja online completo aplicando todos os conceitos de OOP!")

        self.print_concept(
            "Sistema de E-commerce",
            "Um sistema completo de vendas online com produtos, clientes, carrinho de compras e pedidos. Usando classes, herança, encapsulamento e todas as melhores práticas de OOP."
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "🛒 Amazon, Mercado Livre, Shopee - marketplaces gigantes",
            "👕 Lojas de roupas online - Zara, C&A, Renner",
            "📱 Apple Store, Google Play - lojas de apps",
            "🍕 iFood, Uber Eats - delivery de comida",
            "🏪 Pequenos comércios locais com loja virtual"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        input("\n🔸 Pressione ENTER para começar o desenvolvimento...")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Planejamento das classes
        self.print_section("PASSO 1: Planejando as Classes", "📝", "info")
        self.print_tip("Primeiro vamos definir que classes precisamos e suas responsabilidades")

        try:
            print("📋 Classes necessárias:")
            print("• 🛍️ Produto - representa itens da loja")
            print("• 👤 Cliente - dados e histórico de clientes")
            print("• 🛒 CarrinhoCompras - itens selecionados para compra")
            print("• 📦 Pedido - compra finalizada")
            print("• 🏪 Loja - sistema principal que gerencia tudo")
            
            input("\n⏳ Pressione ENTER para começar a implementação...")

        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Implementação
        self.print_section("PASSO 2: Implementando o Sistema", "⚙️", "success")
        self.print_colored("Agora vamos criar cada classe com todos os recursos necessários:", "text")

        # PASSO 3: Código final
        self.print_section("PASSO 3: Sistema Completo", "🎬", "warning")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo do seu e-commerce:", "text")

        codigo_final = '''# 🛒 SISTEMA DE E-COMMERCE COMPLETO
# Mini Projeto - Módulo 18: OOP Básico

from datetime import datetime
from typing import List, Dict, Optional
import json

class Produto:
    """Classe que representa um produto da loja"""
    
    def __init__(self, id_produto: int, nome: str, preco: float, 
                 categoria: str, estoque: int = 0, descricao: str = ""):
        """Inicializa um produto"""
        self.id = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque
        self.descricao = descricao
        self.avaliacoes = []
        self.total_vendas = 0
        self.ativo = True
        
        print(f"✅ Produto '{nome}' cadastrado - R$ {preco:.2f}")
    
    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona produtos ao estoque"""
        if quantidade > 0:
            self.estoque += quantidade
            print(f"📦 {quantidade} unidades adicionadas. Estoque: {self.estoque}")
    
    def remover_estoque(self, quantidade: int) -> bool:
        """Remove produtos do estoque (para vendas)"""
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            self.total_vendas += quantidade
            return True
        return False
    
    def adicionar_avaliacao(self, nota: int, comentario: str = "") -> None:
        """Adiciona avaliação do produto"""
        if 1 <= nota <= 5:
            avaliacao = {
                'nota': nota,
                'comentario': comentario,
                'data': datetime.now().strftime("%d/%m/%Y")
            }
            self.avaliacoes.append(avaliacao)
            print(f"⭐ Avaliação {nota}/5 adicionada para '{self.nome}'")
    
    def media_avaliacoes(self) -> float:
        """Calcula média das avaliações"""
        if not self.avaliacoes:
            return 0.0
        return sum(av['nota'] for av in self.avaliacoes) / len(self.avaliacoes)
    
    def aplicar_desconto(self, percentual: float) -> None:
        """Aplica desconto no produto"""
        if 0 < percentual <= 100:
            desconto = self.preco * (percentual / 100)
            self.preco -= desconto
            print(f"🏷️ Desconto de {percentual}% aplicado! Novo preço: R$ {self.preco:.2f}")
    
    def info_completa(self) -> str:
        """Retorna informações completas do produto"""
        media = self.media_avaliacoes()
        status = "🟢 Disponível" if self.estoque > 0 else "🔴 Fora de estoque"
        
        return f"""
🛍️ {self.nome} (ID: {self.id})
💰 Preço: R$ {self.preco:.2f}
📂 Categoria: {self.categoria}
📦 Estoque: {self.estoque} unidades
⭐ Avaliação: {media:.1f}/5 ({len(self.avaliacoes)} avaliações)
🎯 Total de vendas: {self.total_vendas}
📝 {self.descricao}
{status}"""
    
    def __str__(self) -> str:
        return f"{self.nome} - R$ {self.preco:.2f}"

class Cliente:
    """Classe que representa um cliente da loja"""
    
    def __init__(self, nome: str, email: str, telefone: str = "", endereco: str = ""):
        """Inicializa um cliente"""
        self.id = id(self) % 100000  # ID único simples
        self.nome = nome.title()
        self.email = email.lower()
        self.telefone = telefone
        self.endereco = endereco
        self.data_cadastro = datetime.now().strftime("%d/%m/%Y")
        
        # Histórico e preferências
        self.historico_pedidos = []
        self.total_gasto = 0.0
        self.categoria_favorita = ""
        self.ativo = True
        
        # Classificação do cliente baseada em gastos
        self.tipo_cliente = "Bronze"  # Bronze, Prata, Ouro, Diamante
        
        print(f"👤 Cliente {nome} cadastrado com sucesso!")
    
    def atualizar_dados(self, telefone: str = None, endereco: str = None) -> None:
        """Atualiza dados do cliente"""
        if telefone:
            self.telefone = telefone
            print(f"📞 Telefone atualizado")
        
        if endereco:
            self.endereco = endereco
            print(f"🏠 Endereço atualizado")
    
    def adicionar_pedido(self, pedido) -> None:
        """Adiciona pedido ao histórico do cliente"""
        self.historico_pedidos.append(pedido)
        self.total_gasto += pedido.valor_total
        self._atualizar_classificacao()
    
    def _atualizar_classificacao(self) -> None:
        """Atualiza classificação do cliente baseada nos gastos"""
        tipo_anterior = self.tipo_cliente
        
        if self.total_gasto >= 10000:
            self.tipo_cliente = "Diamante"
        elif self.total_gasto >= 5000:
            self.tipo_cliente = "Ouro"
        elif self.total_gasto >= 2000:
            self.tipo_cliente = "Prata"
        else:
            self.tipo_cliente = "Bronze"
        
        if tipo_anterior != self.tipo_cliente:
            print(f"🎉 {self.nome} foi promovido para {self.tipo_cliente}!")
    
    def desconto_fidelidade(self) -> float:
        """Retorna desconto baseado na fidelidade"""
        descontos = {
            "Bronze": 0,
            "Prata": 5,
            "Ouro": 10,
            "Diamante": 15
        }
        return descontos.get(self.tipo_cliente, 0)
    
    def perfil_completo(self) -> str:
        """Retorna perfil completo do cliente"""
        return f"""
👤 {self.nome} (ID: {self.id}) - {self.tipo_cliente}
📧 {self.email}
📞 {self.telefone}
🏠 {self.endereco}
📅 Cliente desde: {self.data_cadastro}
💰 Total gasto: R$ {self.total_gasto:.2f}
📦 Pedidos realizados: {len(self.historico_pedidos)}
🎁 Desconto fidelidade: {self.desconto_fidelidade()}%"""

class CarrinhoCompras:
    """Classe que representa um carrinho de compras"""
    
    def __init__(self, cliente: Cliente):
        """Inicializa carrinho para um cliente"""
        self.cliente = cliente
        self.itens = {}  # {produto_id: {'produto': Produto, 'quantidade': int}}
        self.data_criacao = datetime.now()
        
        print(f"🛒 Carrinho criado para {cliente.nome}")
    
    def adicionar_item(self, produto: Produto, quantidade: int = 1) -> bool:
        """Adiciona item ao carrinho"""
        if not produto.ativo:
            print(f"❌ Produto '{produto.nome}' não está disponível")
            return False
        
        if quantidade > produto.estoque:
            print(f"❌ Estoque insuficiente! Disponível: {produto.estoque}")
            return False
        
        if produto.id in self.itens:
            # Produto já está no carrinho, aumenta quantidade
            nova_quantidade = self.itens[produto.id]['quantidade'] + quantidade
            if nova_quantidade <= produto.estoque:
                self.itens[produto.id]['quantidade'] = nova_quantidade
                print(f"➕ Quantidade atualizada: {nova_quantidade}x {produto.nome}")
            else:
                print(f"❌ Quantidade total excederia o estoque!")
                return False
        else:
            # Novo produto no carrinho
            self.itens[produto.id] = {
                'produto': produto,
                'quantidade': quantidade
            }
            print(f"🛒 {quantidade}x {produto.nome} adicionado ao carrinho")
        
        return True
    
    def remover_item(self, produto_id: int) -> bool:
        """Remove item completamente do carrinho"""
        if produto_id in self.itens:
            produto_nome = self.itens[produto_id]['produto'].nome
            del self.itens[produto_id]
            print(f"🗑️ {produto_nome} removido do carrinho")
            return True
        else:
            print("❌ Item não encontrado no carrinho")
            return False
    
    def alterar_quantidade(self, produto_id: int, nova_quantidade: int) -> bool:
        """Altera quantidade de um item no carrinho"""
        if produto_id not in self.itens:
            print("❌ Item não encontrado no carrinho")
            return False
        
        produto = self.itens[produto_id]['produto']
        
        if nova_quantidade <= 0:
            return self.remover_item(produto_id)
        
        if nova_quantidade > produto.estoque:
            print(f"❌ Estoque insuficiente! Disponível: {produto.estoque}")
            return False
        
        self.itens[produto_id]['quantidade'] = nova_quantidade
        print(f"✅ Quantidade alterada: {nova_quantidade}x {produto.nome}")
        return True
    
    def calcular_subtotal(self) -> float:
        """Calcula subtotal do carrinho"""
        subtotal = 0.0
        for item in self.itens.values():
            subtotal += item['produto'].preco * item['quantidade']
        return subtotal
    
    def aplicar_desconto_fidelidade(self, subtotal: float) -> tuple:
        """Aplica desconto de fidelidade"""
        desconto_percent = self.cliente.desconto_fidelidade()
        desconto_valor = subtotal * (desconto_percent / 100)
        return desconto_valor, desconto_percent
    
    def calcular_total(self) -> Dict:
        """Calcula valores totais do carrinho"""
        subtotal = self.calcular_subtotal()
        desconto_valor, desconto_percent = self.aplicar_desconto_fidelidade(subtotal)
        
        # Frete (simulado)
        frete = 15.0 if subtotal < 100 else 0.0
        
        total = subtotal - desconto_valor + frete
        
        return {
            'subtotal': subtotal,
            'desconto_percent': desconto_percent,
            'desconto_valor': desconto_valor,
            'frete': frete,
            'total': total
        }
    
    def mostrar_carrinho(self) -> None:
        """Exibe conteúdo do carrinho"""
        if not self.itens:
            print("🛒 Carrinho vazio")
            return
        
        print(f"\\n🛒 CARRINHO DE {self.cliente.nome}")
        print("-" * 50)
        
        for item in self.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal_item = produto.preco * quantidade
            
            print(f"{quantidade}x {produto.nome}")
            print(f"   R$ {produto.preco:.2f} cada = R$ {subtotal_item:.2f}")
        
        valores = self.calcular_total()
        
        print("-" * 50)
        print(f"Subtotal: R$ {valores['subtotal']:.2f}")
        
        if valores['desconto_percent'] > 0:
            print(f"Desconto ({valores['desconto_percent']}%): -R$ {valores['desconto_valor']:.2f}")
        
        print(f"Frete: R$ {valores['frete']:.2f}")
        print(f"TOTAL: R$ {valores['total']:.2f}")
    
    def limpar_carrinho(self) -> None:
        """Limpa todos os itens do carrinho"""
        self.itens.clear()
        print("🗑️ Carrinho limpo")

class Pedido:
    """Classe que representa um pedido finalizado"""
    
    def __init__(self, cliente: Cliente, carrinho: CarrinhoCompras):
        """Cria pedido a partir do carrinho"""
        self.id = id(self) % 100000
        self.cliente = cliente
        self.data_pedido = datetime.now()
        self.status = "Confirmado"
        
        # Copia itens do carrinho
        self.itens = []
        for item in carrinho.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            
            # Remove do estoque
            produto.remover_estoque(quantidade)
            
            self.itens.append({
                'produto_nome': produto.nome,
                'produto_id': produto.id,
                'preco_unitario': produto.preco,
                'quantidade': quantidade,
                'subtotal': produto.preco * quantidade
            })
        
        # Calcula valores
        valores = carrinho.calcular_total()
        self.subtotal = valores['subtotal']
        self.desconto = valores['desconto_valor']
        self.frete = valores['frete']
        self.valor_total = valores['total']
        
        # Adiciona ao histórico do cliente
        cliente.adicionar_pedido(self)
        
        print(f"✅ Pedido #{self.id} criado com sucesso!")
        print(f"💰 Valor total: R$ {self.valor_total:.2f}")
    
    def atualizar_status(self, novo_status: str) -> None:
        """Atualiza status do pedido"""
        status_validos = ["Confirmado", "Preparando", "Enviado", "Entregue", "Cancelado"]
        
        if novo_status in status_validos:
            status_anterior = self.status
            self.status = novo_status
            print(f"📋 Pedido #{self.id}: {status_anterior} → {novo_status}")
        else:
            print(f"❌ Status '{novo_status}' inválido")
    
    def resumo_pedido(self) -> str:
        """Retorna resumo do pedido"""
        resumo = f"""
📦 PEDIDO #{self.id}
👤 Cliente: {self.cliente.nome}
📅 Data: {self.data_pedido.strftime('%d/%m/%Y %H:%M')}
📋 Status: {self.status}

ITENS:"""
        
        for item in self.itens:
            resumo += f"\\n• {item['quantidade']}x {item['produto_nome']} - R$ {item['subtotal']:.2f}"
        
        resumo += f"""

💰 VALORES:
Subtotal: R$ {self.subtotal:.2f}
Desconto: R$ {self.desconto:.2f}
Frete: R$ {self.frete:.2f}
TOTAL: R$ {self.valor_total:.2f}"""
        
        return resumo

class Loja:
    """Sistema principal da loja virtual"""
    
    def __init__(self, nome: str):
        """Inicializa a loja"""
        self.nome = nome
        self.produtos = {}  # {id: Produto}
        self.clientes = {}  # {id: Cliente}
        self.pedidos = []
        self.proximo_produto_id = 1
        
        # Estatísticas
        self.total_vendas = 0.0
        self.total_pedidos = 0
        
        print(f"🏪 Loja '{nome}' criada com sucesso!")
    
    def cadastrar_produto(self, nome: str, preco: float, categoria: str, 
                         estoque: int = 0, descricao: str = "") -> Produto:
        """Cadastra novo produto"""
        produto = Produto(self.proximo_produto_id, nome, preco, categoria, estoque, descricao)
        self.produtos[self.proximo_produto_id] = produto
        self.proximo_produto_id += 1
        return produto
    
    def cadastrar_cliente(self, nome: str, email: str, telefone: str = "", endereco: str = "") -> Cliente:
        """Cadastra novo cliente"""
        cliente = Cliente(nome, email, telefone, endereco)
        self.clientes[cliente.id] = cliente
        return cliente
    
    def buscar_produto(self, termo: str) -> List[Produto]:
        """Busca produtos por nome ou categoria"""
        resultados = []
        termo_lower = termo.lower()
        
        for produto in self.produtos.values():
            if (termo_lower in produto.nome.lower() or 
                termo_lower in produto.categoria.lower() or
                termo_lower in produto.descricao.lower()):
                resultados.append(produto)
        
        return resultados
    
    def listar_produtos_categoria(self, categoria: str) -> List[Produto]:
        """Lista produtos de uma categoria"""
        return [p for p in self.produtos.values() if p.categoria.lower() == categoria.lower()]
    
    def produtos_mais_vendidos(self, limite: int = 5) -> List[Produto]:
        """Retorna produtos mais vendidos"""
        produtos_ordenados = sorted(
            self.produtos.values(),
            key=lambda p: p.total_vendas,
            reverse=True
        )
        return produtos_ordenados[:limite]
    
    def processar_pedido(self, carrinho: CarrinhoCompras) -> Optional[Pedido]:
        """Processa carrinho e cria pedido"""
        if not carrinho.itens:
            print("❌ Carrinho vazio!")
            return None
        
        # Verifica disponibilidade de todos os itens
        for item in carrinho.itens.values():
            produto = item['produto']
            quantidade = item['quantidade']
            
            if quantidade > produto.estoque:
                print(f"❌ Estoque insuficiente para {produto.nome}")
                return None
        
        # Cria pedido
        pedido = Pedido(carrinho.cliente, carrinho)
        self.pedidos.append(pedido)
        
        # Atualiza estatísticas
        self.total_vendas += pedido.valor_total
        self.total_pedidos += 1
        
        # Limpa carrinho
        carrinho.limpar_carrinho()
        
        return pedido
    
    def relatorio_vendas(self) -> str:
        """Gera relatório de vendas"""
        if not self.pedidos:
            return "📭 Nenhuma venda realizada ainda"
        
        # Estatísticas básicas
        ticket_medio = self.total_vendas / self.total_pedidos
        
        # Produtos mais vendidos
        top_produtos = self.produtos_mais_vendidos(3)
        
        # Clientes que mais compraram
        clientes_ordenados = sorted(
            self.clientes.values(),
            key=lambda c: c.total_gasto,
            reverse=True
        )[:3]
        
        relatorio = f"""
📊 RELATÓRIO DE VENDAS - {self.nome}
{'='*50}

💰 FINANCEIRO:
• Total de vendas: R$ {self.total_vendas:.2f}
• Total de pedidos: {self.total_pedidos}
• Ticket médio: R$ {ticket_medio:.2f}

🏆 TOP 3 PRODUTOS MAIS VENDIDOS:"""
        
        for i, produto in enumerate(top_produtos, 1):
            relatorio += f"\\n{i}. {produto.nome} - {produto.total_vendas} vendas"
        
        relatorio += "\\n\\n👑 TOP 3 CLIENTES:"
        
        for i, cliente in enumerate(clientes_ordenados, 1):
            relatorio += f"\\n{i}. {cliente.nome} - R$ {cliente.total_gasto:.2f}"
        
        relatorio += f"""

📈 PRODUTOS CADASTRADOS: {len(self.produtos)}
👥 CLIENTES CADASTRADOS: {len(self.clientes)}"""
        
        return relatorio

# DEMONSTRAÇÃO COMPLETA DO SISTEMA

print("=== CRIANDO LOJA VIRTUAL ===")

# Criando a loja
minha_loja = Loja("TechStore Python")

print("\\n=== CADASTRANDO PRODUTOS ===")
# Cadastrando produtos
notebook = minha_loja.cadastrar_produto("Notebook Dell", 2500.00, "Eletrônicos", 10, "Notebook para programação")
mouse = minha_loja.cadastrar_produto("Mouse Gamer", 150.00, "Eletrônicos", 25, "Mouse para jogos")
teclado = minha_loja.cadastrar_produto("Teclado Mecânico", 300.00, "Eletrônicos", 15, "Teclado para programadores")
monitor = minha_loja.cadastrar_produto("Monitor 24\"", 800.00, "Eletrônicos", 8, "Monitor Full HD")

print("\\n=== CADASTRANDO CLIENTES ===")
# Cadastrando clientes
cliente1 = minha_loja.cadastrar_cliente("Ana Silva", "ana@email.com", "(11) 99999-1111", "Rua A, 123")
cliente2 = minha_loja.cadastrar_cliente("João Santos", "joao@email.com", "(11) 88888-2222", "Rua B, 456")

print("\\n=== CLIENTE FAZENDO COMPRAS ===")
# Cliente 1 fazendo compras
carrinho1 = CarrinhoCompras(cliente1)
carrinho1.adicionar_item(notebook, 1)
carrinho1.adicionar_item(mouse, 2)
carrinho1.adicionar_item(teclado, 1)

# Mostra carrinho
carrinho1.mostrar_carrinho()

# Processa pedido
print("\\n=== FINALIZANDO PEDIDO ===")
pedido1 = minha_loja.processar_pedido(carrinho1)

print("\\n=== CLIENTE 2 FAZENDO COMPRAS ===")
# Cliente 2 fazendo compras
carrinho2 = CarrinhoCompras(cliente2)
carrinho2.adicionar_item(monitor, 1)
carrinho2.adicionar_item(mouse, 1)

# Finalizando
pedido2 = minha_loja.processar_pedido(carrinho2)

print("\\n=== ATUALIZANDO STATUS DOS PEDIDOS ===")
# Atualizando status
pedido1.atualizar_status("Enviado")
pedido2.atualizar_status("Entregue")

print("\\n=== AVALIAÇÕES DE PRODUTOS ===")
# Adicionando avaliações
notebook.adicionar_avaliacao(5, "Excelente para programar!")
mouse.adicionar_avaliacao(4, "Muito bom, recomendo")
mouse.adicionar_avaliacao(5, "Perfeito para jogos")

print("\\n=== INFORMAÇÕES DOS PRODUTOS ===")
# Mostrando info dos produtos
print(notebook.info_completa())
print(mouse.info_completa())

print("\\n=== PERFIL DOS CLIENTES ===")
# Perfil dos clientes
print(cliente1.perfil_completo())
print(cliente2.perfil_completo())

print("\\n=== BUSCA DE PRODUTOS ===")
# Busca
resultados = minha_loja.buscar_produto("mouse")
print(f"Resultados para 'mouse': {len(resultados)} produtos encontrados")
for produto in resultados:
    print(f"• {produto}")

# Relatório final
print(minha_loja.relatorio_vendas())

print("\\n✅ SISTEMA DE E-COMMERCE FUNCIONANDO PERFEITAMENTE!")
print("\\n🎯 CONCEITOS OOP APLICADOS:")
print("  • 5 classes bem estruturadas com responsabilidades claras")
print("  • Encapsulamento - dados protegidos e métodos controlados")
print("  • Composição - objetos contêm outros objetos")
print("  • Abstração - interfaces simples para operações complexas")
print("  • Herança implícita - todas as classes herdam de object")
print("  • Polimorfismo - métodos como __str__ customizados")
print("  • Estado controlado - objetos mantêm consistência")
print("  • Interação entre objetos - sistema integrado")'''

        self.exemplo(codigo_final)
        self.executar_codigo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema de e-commerce completo usando OOP!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔐 Adicionar sistema de autenticação e segurança",
            "💳 Integrar gateways de pagamento (PagSeguro, Stripe)",
            "📊 Criar dashboard administrativo com gráficos",
            "📱 Desenvolver API REST para aplicativo mobile",
            "🎨 Criar interface web com Flask/Django",
            "📈 Implementar sistema de recomendações",
            "🔍 Adicionar busca avançada com filtros",
            "📧 Sistema de notificações por email",
            "🏪 Multi-loja e marketplace",
            "📦 Integração com sistemas de logística"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre em OOP Básico!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema de E-commerce com OOP")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo18OopBasico()
    print("Teste do módulo 18 - versão standalone")
    module._oop_basico()