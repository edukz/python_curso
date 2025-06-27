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
        """Conteúdo principal sobre OOP básico"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS")
        else:
            print("\n" + "="*50)
            print("🏗️ MÓDULO 18: PROGRAMAÇÃO ORIENTADA A OBJETOS")
            print("="*50)
        
        self.print_section("🎯 OOP é o paradigma de programação mais usado no mundo!")
        self.print_concept("🏗️ Vamos aprender a criar e organizar código com CLASSES!")
        
        self.print_section("\n═══════════════════════════════════════════════")
        self.print_section("        O QUE É PROGRAMAÇÃO ORIENTADA A OBJETOS?")
        self.print_section("═══════════════════════════════════════════════")
        
        self.print_concept("\n🎭 Conceitos fundamentais:")
        self.print_colored("• 🏗️ CLASSE = modelo/molde para criar objetos", "yellow")
        self.print_colored("• 🎯 OBJETO = instância de uma classe", "yellow")
        self.print_colored("• 📦 ATRIBUTOS = características do objeto", "yellow")
        self.print_colored("• ⚡ MÉTODOS = ações que o objeto pode fazer", "yellow")
        
        self.print_concept("\n🏗️ Criando sua primeira classe:")
        
        codigo1 = '''# Primeira classe em Python
class Pessoa:
    """Classe que representa uma pessoa"""
    
    def __init__(self, nome, idade):
        """Construtor - inicializa um objeto Pessoa"""
        self.nome = nome        # Atributo público
        self.idade = idade      # Atributo público
        self.energia = 100      # Atributo padrão
    
    def cumprimentar(self):
        """Método para cumprimentar"""
        return f"Olá! Eu sou {self.nome} e tenho {self.idade} anos."
    
    def aniversario(self):
        """Método para fazer aniversário"""
        self.idade += 1
        print(f"🎉 {self.nome} fez aniversário! Agora tem {self.idade} anos.")
    
    def dormir(self):
        """Método para dormir e recuperar energia"""
        self.energia = 100
        print(f"😴 {self.nome} dormiu e recuperou toda a energia!")
    
    def trabalhar(self, horas):
        """Método para trabalhar (gasta energia)"""
        energia_gasta = horas * 10
        if self.energia >= energia_gasta:
            self.energia -= energia_gasta
            print(f"💼 {self.nome} trabalhou {horas}h. Energia: {self.energia}")
        else:
            print(f"😵 {self.nome} está muito cansado para trabalhar!")

print("=== CRIANDO OBJETOS ===")
# Criando objetos (instâncias da classe)
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(f"Pessoa 1: {pessoa1.nome}, {pessoa1.idade} anos")
print(f"Pessoa 2: {pessoa2.nome}, {pessoa2.idade} anos")

print("\\n=== USANDO MÉTODOS ===")
print(pessoa1.cumprimentar())
print(pessoa2.cumprimentar())

print("\\n=== MODIFICANDO OBJETOS ===")
pessoa1.aniversario()
pessoa2.trabalhar(5)
pessoa2.trabalhar(8)  # Vai ficar cansada
pessoa2.dormir()      # Recupera energia

print("\\n=== ACESSANDO ATRIBUTOS ===")
print(f"{pessoa1.nome} tem {pessoa1.energia} de energia")
print(f"{pessoa2.nome} tem {pessoa2.energia} de energia")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.print_section("\n💰 Exemplo mais avançado - Conta Bancária:")
        
        codigo2 = '''# Classe mais sofisticada - Conta Bancária
class ContaBancaria:
    """Classe que representa uma conta bancária"""
    
    # Atributo de classe (compartilhado por todas as instâncias)
    banco = "Banco Python"
    total_contas = 0
    
    def __init__(self, titular, saldo_inicial=0):
        """Construtor da conta bancária"""
        self.titular = titular
        self._saldo = saldo_inicial      # Atributo "privado" (convenção)
        self._historico = []             # Lista de transações
        self.numero = ContaBancaria.total_contas + 1
        
        # Incrementa contador de contas
        ContaBancaria.total_contas += 1
        
        # Registra abertura da conta
        self._adicionar_historico(f"Conta aberta com saldo inicial: R$ {saldo_inicial:.2f}")
        
        print(f"✅ Conta {self.numero} criada para {self.titular}")
    
    def depositar(self, valor):
        """Deposita dinheiro na conta"""
        if valor > 0:
            self._saldo += valor
            self._adicionar_historico(f"Depósito: +R$ {valor:.2f}")
            print(f"💰 Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self._saldo:.2f}")
            return True
        else:
            print("❌ Valor de depósito deve ser positivo!")
            return False
    
    def sacar(self, valor):
        """Saca dinheiro da conta"""
        if valor <= 0:
            print("❌ Valor de saque deve ser positivo!")
            return False
        
        if valor > self._saldo:
            print(f"❌ Saldo insuficiente! Saldo atual: R$ {self._saldo:.2f}")
            return False
        
        self._saldo -= valor
        self._adicionar_historico(f"Saque: -R$ {valor:.2f}")
        print(f"💸 Saque de R$ {valor:.2f} realizado. Saldo: R$ {self._saldo:.2f}")
        return True
    
    def transferir(self, valor, conta_destino):
        """Transfere dinheiro para outra conta"""
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self._adicionar_historico(f"Transferência para {conta_destino.titular}: -R$ {valor:.2f}")
            conta_destino._adicionar_historico(f"Transferência de {self.titular}: +R$ {valor:.2f}")
            print(f"🔄 Transferência realizada para {conta_destino.titular}")
            return True
        return False
    
    def consultar_saldo(self):
        """Consulta o saldo atual"""
        print(f"💰 Saldo de {self.titular}: R$ {self._saldo:.2f}")
        return self._saldo
    
    def extrato(self):
        """Mostra o extrato da conta"""
        print(f"\\n📄 EXTRATO - CONTA {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Banco: {self.banco}")
        print("-" * 50)
        
        for transacao in self._historico[-10:]:  # Últimas 10 transações
            print(f"  {transacao}")
        
        print("-" * 50)
        print(f"Saldo atual: R$ {self._saldo:.2f}")
    
    def _adicionar_historico(self, descricao):
        """Método privado para adicionar ao histórico"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._historico.append(f"[{timestamp}] {descricao}")
    
    @classmethod
    def relatorio_banco(cls):
        """Método de classe - relatório geral do banco"""
        print(f"\\n🏦 RELATÓRIO {cls.banco}")
        print(f"Total de contas: {cls.total_contas}")

# Demonstração do sistema bancário
print("=== SISTEMA BANCÁRIO ===")

# Criando contas
conta_joao = ContaBancaria("João Silva", 1000)
conta_maria = ContaBancaria("Maria Santos", 500)

print("\\n=== OPERAÇÕES BANCÁRIAS ===")
# Operações
conta_joao.depositar(200)
conta_joao.sacar(150)
conta_maria.depositar(300)

print("\\n=== TRANSFERÊNCIA ===")
conta_joao.transferir(100, conta_maria)

print("\\n=== CONSULTAS ===")
conta_joao.consultar_saldo()
conta_maria.consultar_saldo()

# Extratos
conta_joao.extrato()

# Relatório do banco
ContaBancaria.relatorio_banco()'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("\n🎮 Exemplo de jogo - Personagem RPG:")
        
        codigo3 = '''# Sistema de personagem de jogo
class PersonagemRPG:
    """Classe para personagem de RPG"""
    
    def __init__(self, nome, classe="Guerreiro"):
        """Inicializa personagem"""
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.experiencia = 0
        self.vida_maxima = 100
        self.vida_atual = 100
        self.ataque = 20
        self.defesa = 10
        self.inventario = []
        
        print(f"⚔️ {self.nome} ({self.classe}) entrou no jogo!")
    
    def status(self):
        """Mostra status do personagem"""
        print(f"\\n👤 {self.nome} - {self.classe}")
        print(f"🔰 Nível: {self.nivel}")
        print(f"✨ Experiência: {self.experiencia}/{self.experiencia_necessaria()}")
        print(f"❤️ Vida: {self.vida_atual}/{self.vida_maxima}")
        print(f"⚔️ Ataque: {self.ataque}")
        print(f"🛡️ Defesa: {self.defesa}")
        if self.inventario:
            print(f"🎒 Inventário: {', '.join(self.inventario)}")
    
    def experiencia_necessaria(self):
        """Calcula experiência necessária para próximo nível"""
        return self.nivel * 100
    
    def ganhar_experiencia(self, exp):
        """Ganha experiência e verifica level up"""
        self.experiencia += exp
        print(f"✨ {self.nome} ganhou {exp} de experiência!")
        
        # Verifica level up
        while self.experiencia >= self.experiencia_necessaria():
            self.subir_nivel()
    
    def subir_nivel(self):
        """Sobe de nível e aumenta atributos"""
        self.experiencia -= self.experiencia_necessaria()
        self.nivel += 1
        
        # Aumenta atributos
        self.vida_maxima += 20
        self.vida_atual = self.vida_maxima  # Recupera vida completa
        self.ataque += 5
        self.defesa += 3
        
        print(f"🎉 LEVEL UP! {self.nome} subiu para o nível {self.nivel}!")
        print(f"📈 Atributos aumentaram!")
    
    def atacar(self, inimigo):
        """Ataca outro personagem"""
        dano = max(1, self.ataque - inimigo.defesa)
        inimigo.receber_dano(dano)
        print(f"⚔️ {self.nome} atacou {inimigo.nome} causando {dano} de dano!")
        
        # Ganha experiência por atacar
        self.ganhar_experiencia(10)
    
    def receber_dano(self, dano):
        """Recebe dano"""
        self.vida_atual = max(0, self.vida_atual - dano)
        print(f"💥 {self.nome} recebeu {dano} de dano! Vida: {self.vida_atual}")
        
        if self.vida_atual == 0:
            print(f"💀 {self.nome} foi derrotado!")
    
    def curar(self, pontos=None):
        """Cura o personagem"""
        if pontos is None:
            pontos = self.vida_maxima // 2
        
        vida_anterior = self.vida_atual
        self.vida_atual = min(self.vida_maxima, self.vida_atual + pontos)
        cura_real = self.vida_atual - vida_anterior
        
        print(f"💚 {self.nome} se curou em {cura_real} pontos! Vida: {self.vida_atual}")
    
    def encontrar_item(self, item):
        """Encontra um item"""
        self.inventario.append(item)
        print(f"🎁 {self.nome} encontrou: {item}!")
        
        # Alguns itens dão bônus
        if "Espada" in item:
            self.ataque += 10
            print(f"⚔️ Ataque aumentou para {self.ataque}!")
        elif "Escudo" in item:
            self.defesa += 5
            print(f"🛡️ Defesa aumentou para {self.defesa}!")

# Demonstração do sistema RPG
print("=== JOGO RPG ===")

# Criando personagens
heroi = PersonagemRPG("Conan", "Bárbaro")
inimigo = PersonagemRPG("Orc Guerreiro", "Monstro")

print("\\n=== STATUS INICIAL ===")
heroi.status()

print("\\n=== EXPLORANDO ===")
heroi.encontrar_item("Espada de Ferro")
heroi.encontrar_item("Poção de Vida")

print("\\n=== COMBATE ===")
heroi.atacar(inimigo)
inimigo.atacar(heroi)
heroi.atacar(inimigo)

print("\\n=== CURA ===")
heroi.curar()

print("\\n=== STATUS FINAL ===")
heroi.status()

print("\\n🎮 Sistema de RPG funcionando!")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Qual é o método especial usado como construtor em Python?",
            ["__init__", "__init__()", "init"],
            "__init__ é o construtor das classes"
        )
        
        self.exercicio(
            "O que representa 'self' nos métodos de uma classe?",
            ["instância atual", "objeto atual", "referência"],
            "'self' refere-se à instância atual do objeto"
        )
        
        # Mini Projeto do Módulo 18
        self._mini_projeto_sistema_funcionarios()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_funcionarios(self) -> None:
        """Mini Projeto - Módulo 18: Sistema de Gerenciamento de Funcionários"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE FUNCIONÁRIOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE FUNCIONÁRIOS")
            print("="*50)
        
        self.print_concept("🏢 Sistema completo de RH usando Orientação a Objetos!")
        self.print_tip("🛠️ Usando: Classes, Herança, Encapsulamento, Properties")
        
        self.pausar()
        
        codigo_projeto = '''# 🏢 SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS
# Projeto completo usando OOP com herança e encapsulamento

import json
from datetime import datetime, date
from typing import List, Dict, Optional

class Pessoa:
    """Classe base para representar uma pessoa"""
    
    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str = ""):
        """Inicializa uma pessoa"""
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone
        self._endereco = ""
    
    # Properties para controlar acesso aos atributos
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, valor: str):
        if len(valor.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        self._nome = valor.strip().title()
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def telefone(self) -> str:
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor: str):
        # Remove formatação
        telefone_limpo = ''.join(filter(str.isdigit, valor))
        if len(telefone_limpo) not in [10, 11]:
            raise ValueError("Telefone deve ter 10 ou 11 dígitos")
        self._telefone = valor
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor: str):
        self._endereco = valor
    
    def calcular_idade(self) -> int:
        """Calcula idade baseada na data de nascimento"""
        try:
            nascimento = datetime.strptime(self._data_nascimento, "%d/%m/%Y").date()
            hoje = date.today()
            idade = hoje.year - nascimento.year
            
            # Ajusta se ainda não fez aniversário este ano
            if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
                idade -= 1
            
            return idade
        except ValueError:
            return 0
    
    def to_dict(self) -> Dict:
        """Converte pessoa para dicionário"""
        return {
            'nome': self._nome,
            'cpf': self._cpf,
            'data_nascimento': self._data_nascimento,
            'telefone': self._telefone,
            'endereco': self._endereco,
            'idade': self.calcular_idade()
        }
    
    def __str__(self) -> str:
        return f"{self._nome} (CPF: {self._cpf})"

class Funcionario(Pessoa):
    """Classe para funcionários, herda de Pessoa"""
    
    # Contador de funcionários
    _proximo_id = 1
    
    def __init__(self, nome: str, cpf: str, data_nascimento: str, cargo: str, 
                 salario: float, departamento: str, telefone: str = ""):
        """Inicializa um funcionário"""
        super().__init__(nome, cpf, data_nascimento, telefone)
        
        self._id = Funcionario._proximo_id
        Funcionario._proximo_id += 1
        
        self._cargo = cargo
        self._salario = salario
        self._departamento = departamento
        self._data_contratacao = datetime.now().strftime("%d/%m/%Y")
        self._ativo = True
        self._historico_salario = [{'data': self._data_contratacao, 'salario': salario, 'motivo': 'Contratação inicial'}]
        self._avaliacoes = []
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def cargo(self) -> str:
        return self._cargo
    
    @cargo.setter
    def cargo(self, valor: str):
        if len(valor.strip()) < 2:
            raise ValueError("Cargo deve ter pelo menos 2 caracteres")
        antigo_cargo = self._cargo
        self._cargo = valor.strip().title()
        print(f"📋 Cargo alterado de '{antigo_cargo}' para '{self._cargo}'")
    
    @property
    def salario(self) -> float:
        return self._salario
    
    @property
    def departamento(self) -> str:
        return self._departamento
    
    @departamento.setter
    def departamento(self, valor: str):
        antigo_dept = self._departamento
        self._departamento = valor.strip().title()
        print(f"🏢 Transferido de '{antigo_dept}' para '{self._departamento}'")
    
    @property
    def ativo(self) -> bool:
        return self._ativo
    
    def ajustar_salario(self, novo_salario: float, motivo: str = "Ajuste salarial"):
        """Ajusta salário do funcionário"""
        if novo_salario <= 0:
            raise ValueError("Salário deve ser maior que zero")
        
        salario_anterior = self._salario
        self._salario = novo_salario
        
        # Registra no histórico
        self._historico_salario.append({
            'data': datetime.now().strftime("%d/%m/%Y"),
            'salario': novo_salario,
            'motivo': motivo
        })
        
        diferenca = novo_salario - salario_anterior
        sinal = "+" if diferenca > 0 else ""
        print(f"💰 Salário ajustado: R$ {salario_anterior:.2f} → R$ {novo_salario:.2f} ({sinal}R$ {diferenca:.2f})")
        print(f"📝 Motivo: {motivo}")
    
    def dar_aumento(self, percentual: float, motivo: str = "Aumento por mérito"):
        """Dá aumento percentual"""
        if percentual <= 0:
            raise ValueError("Percentual deve ser positivo")
        
        novo_salario = self._salario * (1 + percentual / 100)
        self.ajustar_salario(novo_salario, f"{motivo} ({percentual}%)")
    
    def adicionar_avaliacao(self, nota: float, comentario: str = ""):
        """Adiciona avaliação de desempenho"""
        if not 0 <= nota <= 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        
        avaliacao = {
            'data': datetime.now().strftime("%d/%m/%Y"),
            'nota': nota,
            'comentario': comentario
        }
        
        self._avaliacoes.append(avaliacao)
        print(f"📊 Avaliação registrada: {nota}/10")
        
        # Aumento automático para notas altas
        if nota >= 9.0:
            print("🌟 Excelente desempenho! Aumento automático de 5%")
            self.dar_aumento(5.0, "Aumento por excelência (nota ≥ 9.0)")
        elif nota >= 8.0:
            print("⭐ Bom desempenho! Aumento automático de 3%")
            self.dar_aumento(3.0, "Aumento por bom desempenho (nota ≥ 8.0)")
    
    def calcular_tempo_empresa(self) -> tuple:
        """Calcula tempo de empresa em anos e meses"""
        try:
            contratacao = datetime.strptime(self._data_contratacao, "%d/%m/%Y")
            hoje = datetime.now()
            
            anos = hoje.year - contratacao.year
            meses = hoje.month - contratacao.month
            
            if meses < 0:
                anos -= 1
                meses += 12
            
            return anos, meses
        except ValueError:
            return 0, 0
    
    def desligar(self, motivo: str = "Desligamento"):
        """Desliga funcionário da empresa"""
        self._ativo = False
        print(f"📤 {self.nome} foi desligado da empresa")
        print(f"📝 Motivo: {motivo}")
    
    def reativar(self):
        """Reativa funcionário"""
        self._ativo = True
        print(f"📥 {self.nome} foi reativado na empresa")
    
    def relatorio_individual(self) -> str:
        """Gera relatório individual do funcionário"""
        anos, meses = self.calcular_tempo_empresa()
        
        relatorio = f"""
📋 RELATÓRIO INDIVIDUAL - ID #{self._id}
{'='*50}
👤 Nome: {self.nome}
🆔 CPF: {self.cpf}
📞 Telefone: {self.telefone}
🏠 Endereço: {self.endereco}
🎂 Idade: {self.calcular_idade()} anos

💼 INFORMAÇÕES PROFISSIONAIS:
• Cargo: {self._cargo}
• Departamento: {self._departamento}
• Salário atual: R$ {self._salario:,.2f}
• Data de contratação: {self._data_contratacao}
• Tempo de empresa: {anos} anos e {meses} meses
• Status: {'🟢 Ativo' if self._ativo else '🔴 Inativo'}

💰 HISTÓRICO SALARIAL:
"""
        
        for registro in self._historico_salario[-5:]:  # Últimos 5 registros
            relatorio += f"• {registro['data']}: R$ {registro['salario']:,.2f} - {registro['motivo']}\\n"
        
        if self._avaliacoes:
            relatorio += "\\n📊 AVALIAÇÕES DE DESEMPENHO:\\n"
            for av in self._avaliacoes[-3:]:  # Últimas 3 avaliações
                relatorio += f"• {av['data']}: {av['nota']}/10 - {av['comentario']}\\n"
            
            # Média das avaliações
            media = sum(av['nota'] for av in self._avaliacoes) / len(self._avaliacoes)
            relatorio += f"\\n📈 Média geral: {media:.1f}/10\\n"
        
        return relatorio
    
    def to_dict(self) -> Dict:
        """Converte funcionário para dicionário"""
        data = super().to_dict()
        anos, meses = self.calcular_tempo_empresa()
        
        data.update({
            'id': self._id,
            'cargo': self._cargo,
            'salario': self._salario,
            'departamento': self._departamento,
            'data_contratacao': self._data_contratacao,
            'tempo_empresa_anos': anos,
            'tempo_empresa_meses': meses,
            'ativo': self._ativo,
            'total_avaliacoes': len(self._avaliacoes),
            'media_avaliacoes': sum(av['nota'] for av in self._avaliacoes) / len(self._avaliacoes) if self._avaliacoes else 0
        })
        
        return data

class GerenciadorRH:
    """Sistema de gerenciamento de recursos humanos"""
    
    def __init__(self):
        """Inicializa o sistema de RH"""
        self._funcionarios: List[Funcionario] = []
        self._arquivo_dados = "funcionarios.json"
        
        print("🏢 Sistema de RH inicializado!")
        self.carregar_dados()
    
    def contratar(self, nome: str, cpf: str, data_nascimento: str, cargo: str, 
                  salario: float, departamento: str, telefone: str = "") -> Funcionario:
        """Contrata novo funcionário"""
        
        # Verifica se CPF já existe
        if self.buscar_por_cpf(cpf):
            raise ValueError(f"CPF {cpf} já cadastrado!")
        
        funcionario = Funcionario(nome, cpf, data_nascimento, cargo, salario, departamento, telefone)
        self._funcionarios.append(funcionario)
        
        print(f"✅ {funcionario.nome} contratado como {cargo}")
        print(f"💰 Salário: R$ {salario:,.2f}")
        print(f"🏢 Departamento: {departamento}")
        
        self.salvar_dados()
        return funcionario
    
    def buscar_por_id(self, id_funcionario: int) -> Optional[Funcionario]:
        """Busca funcionário por ID"""
        for funcionario in self._funcionarios:
            if funcionario.id == id_funcionario:
                return funcionario
        return None
    
    def buscar_por_cpf(self, cpf: str) -> Optional[Funcionario]:
        """Busca funcionário por CPF"""
        for funcionario in self._funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None
    
    def buscar_por_nome(self, nome: str) -> List[Funcionario]:
        """Busca funcionários por nome (busca parcial)"""
        nome_lower = nome.lower()
        resultados = []
        
        for funcionario in self._funcionarios:
            if nome_lower in funcionario.nome.lower():
                resultados.append(funcionario)
        
        return resultados
    
    def listar_por_departamento(self, departamento: str) -> List[Funcionario]:
        """Lista funcionários de um departamento"""
        return [f for f in self._funcionarios if f.departamento.lower() == departamento.lower()]
    
    def listar_ativos(self) -> List[Funcionario]:
        """Lista apenas funcionários ativos"""
        return [f for f in self._funcionarios if f.ativo]
    
    def promover(self, id_funcionario: int, novo_cargo: str, novo_salario: float = None):
        """Promove funcionário para novo cargo"""
        funcionario = self.buscar_por_id(id_funcionario)
        if not funcionario:
            print(f"❌ Funcionário ID {id_funcionario} não encontrado")
            return
        
        cargo_anterior = funcionario.cargo
        funcionario.cargo = novo_cargo
        
        if novo_salario:
            funcionario.ajustar_salario(novo_salario, f"Promoção para {novo_cargo}")
        
        print(f"🎉 {funcionario.nome} promovido de {cargo_anterior} para {novo_cargo}!")
        self.salvar_dados()
    
    def dar_aumento_geral(self, departamento: str = None, percentual: float = 5.0):
        """Dá aumento para todos ou departamento específico"""
        funcionarios_alvo = self._funcionarios
        
        if departamento:
            funcionarios_alvo = self.listar_por_departamento(departamento)
            print(f"💰 Aumento de {percentual}% para o departamento {departamento}")
        else:
            funcionarios_alvo = self.listar_ativos()
            print(f"💰 Aumento geral de {percentual}% para todos os funcionários ativos")
        
        for funcionario in funcionarios_alvo:
            if funcionario.ativo:
                funcionario.dar_aumento(percentual, f"Aumento geral ({percentual}%)")
        
        print(f"✅ {len(funcionarios_alvo)} funcionários receberam aumento")
        self.salvar_dados()
    
    def relatorio_geral(self) -> str:
        """Gera relatório geral da empresa"""
        funcionarios_ativos = self.listar_ativos()
        
        if not funcionarios_ativos:
            return "📭 Nenhum funcionário ativo encontrado"
        
        # Estatísticas gerais
        total_funcionarios = len(self._funcionarios)
        funcionarios_ativos_count = len(funcionarios_ativos)
        funcionarios_inativos = total_funcionarios - funcionarios_ativos_count
        
        # Folha de pagamento
        folha_total = sum(f.salario for f in funcionarios_ativos)
        salario_medio = folha_total / funcionarios_ativos_count if funcionarios_ativos_count > 0 else 0
        
        # Por departamento
        por_departamento = {}
        for f in funcionarios_ativos:
            dept = f.departamento
            if dept not in por_departamento:
                por_departamento[dept] = {'count': 0, 'folha': 0}
            por_departamento[dept]['count'] += 1
            por_departamento[dept]['folha'] += f.salario
        
        relatorio = f"""
🏢 RELATÓRIO GERAL DA EMPRESA
{'='*60}
📊 RESUMO EXECUTIVO:
• Total de funcionários: {total_funcionarios}
• Funcionários ativos: {funcionarios_ativos_count}
• Funcionários inativos: {funcionarios_inativos}
• Folha de pagamento total: R$ {folha_total:,.2f}
• Salário médio: R$ {salario_medio:,.2f}

🏢 POR DEPARTAMENTO:
"""
        
        for dept, dados in sorted(por_departamento.items()):
            media_dept = dados['folha'] / dados['count']
            relatorio += f"• {dept}: {dados['count']} funcionários - Folha: R$ {dados['folha']:,.2f} (Média: R$ {media_dept:,.2f})\\n"
        
        # Top 5 maiores salários
        top_salarios = sorted(funcionarios_ativos, key=lambda f: f.salario, reverse=True)[:5]
        relatorio += "\\n💰 TOP 5 MAIORES SALÁRIOS:\\n"
        for i, f in enumerate(top_salarios, 1):
            relatorio += f"{i}. {f.nome} - {f.cargo} - R$ {f.salario:,.2f}\\n"
        
        return relatorio
    
    def salvar_dados(self):
        """Salva dados dos funcionários em arquivo JSON"""
        try:
            dados = [f.to_dict() for f in self._funcionarios]
            with open(self._arquivo_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            print(f"💾 Dados salvos em {self._arquivo_dados}")
        except Exception as e:
            print(f"❌ Erro ao salvar dados: {e}")
    
    def carregar_dados(self):
        """Carrega dados dos funcionários do arquivo JSON"""
        try:
            with open(self._arquivo_dados, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            
            print(f"📥 {len(dados)} registros carregados de {self._arquivo_dados}")
        except FileNotFoundError:
            print(f"📁 Arquivo {self._arquivo_dados} não encontrado. Iniciando com base vazia.")
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")

# DEMONSTRAÇÃO DO SISTEMA

print("=== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ===\\n")

# Criar sistema de RH
rh = GerenciadorRH()

print("👥 CONTRATANDO FUNCIONÁRIOS:")
# Contratando funcionários
joao = rh.contratar("João Silva", "123.456.789-01", "15/03/1990", "Desenvolvedor", 5000, "TI", "(11) 99999-1111")
maria = rh.contratar("Maria Santos", "987.654.321-01", "22/07/1985", "Analista", 4500, "Marketing", "(11) 88888-2222")
pedro = rh.contratar("Pedro Costa", "456.789.123-01", "10/12/1992", "Designer", 4000, "Criativo")

print("\\n🎯 AVALIAÇÕES E AUMENTOS:")
# Avaliações
joao.adicionar_avaliacao(9.2, "Excelente trabalho na API do produto")
maria.adicionar_avaliacao(8.5, "Ótima campanha de marketing digital")
pedro.adicionar_avaliacao(7.8, "Bom trabalho no redesign")

print("\\n🚀 PROMOÇÕES:")
# Promoções
rh.promover(joao.id, "Tech Lead", 7000)

print("\\n💰 AUMENTO GERAL:")
# Aumento geral para departamento
rh.dar_aumento_geral("TI", 10.0)

print("\\n📊 RELATÓRIOS:")
# Relatório individual
print(joao.relatorio_individual())

# Relatório geral
print(rh.relatorio_geral())

print("\\n✅ Sistema de RH funcionando perfeitamente!")
print("🎯 Conceitos OOP aplicados:")
print("  • Classes e objetos")
print("  • Herança (Funcionario herda de Pessoa)")
print("  • Encapsulamento (atributos privados com _)")
print("  • Properties (getters/setters)")
print("  • Métodos de classe e instância")
print("  • Composição (GerenciadorRH contém Funcionarios)")
print("  • Persistência de dados em JSON")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        self.print_success("\n🏆 PARABÉNS! Sistema de RH orientado a objetos criado!")
        self.print_tip("🎯 Aplicação real: sistemas corporativos, CRUD, gestão empresarial")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Gerenciamento de Funcionários")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo18OopBasico()
    print("Teste do módulo 18 - versão standalone")
    module._oop_basico()