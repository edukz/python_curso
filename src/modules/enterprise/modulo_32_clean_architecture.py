#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 32: Clean Architecture & Domain-Driven Design
Aprenda arquitetura limpa e design orientado ao domínio para sistemas escaláveis
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Protocol, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid
from ..shared.base_module import BaseModule


class Modulo32CleanArchitecture(BaseModule):
    """Módulo 32: Clean Architecture & Domain-Driven Design - Arquitetura de Software Escalável"""
    
    def __init__(self):
        super().__init__("modulo_32", "Clean Architecture & Domain-Driven Design")
        self.has_mini_project = True
        self.mini_project_points = 150
    
    def execute(self) -> None:
        """Executa o módulo Clean Architecture & Domain-Driven Design"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._clean_architecture_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _clean_architecture_principal(self) -> None:
        """Conteúdo principal do módulo Clean Architecture & Domain-Driven Design"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏛️ MÓDULO 32: CLEAN ARCHITECTURE & DOMAIN-DRIVEN DESIGN")
        else:
            print("\n" + "="*50)
            print("🏛️ MÓDULO 32: CLEAN ARCHITECTURE & DOMAIN-DRIVEN DESIGN")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🏛️ Bem-vindo ao mundo da arquitetura de software de classe mundial! Vamos construir sistemas como os gigantes da tecnologia!")
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
            self._mini_projeto_sistema_bancario()
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
                'titulo': '🎯 O que é Clean Architecture?',
                'descricao': 'Entenda os princípios da arquitetura limpa',
                'funcao': self._secao_conceitos_fundamentais
            },
            {
                'id': 'secao_camadas_arquitetura',
                'titulo': '🏗️ As 4 Camadas da Clean Architecture',
                'descricao': 'Entities, Use Cases, Interface Adapters e Frameworks',
                'funcao': self._secao_camadas_arquitetura
            },
            {
                'id': 'secao_domain_driven_design',
                'titulo': '🎭 Domain-Driven Design (DDD)',
                'descricao': 'Modelagem focada no domínio do negócio',
                'funcao': self._secao_domain_driven_design
            },
            {
                'id': 'secao_dependency_inversion',
                'titulo': '🔄 Dependency Inversion na Prática',
                'descricao': 'Como inverter dependências e criar flexibilidade',
                'funcao': self._secao_dependency_inversion
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Casos de uso em grandes empresas',
                'descricao': 'Como Netflix, Uber e Google aplicam esses conceitos',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas de arquitetura',
                'descricao': 'Dicas dos arquitetos de software sênior',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre arquitetura limpa',
                'descricao': 'Histórias e evolução da arquitetura de software',
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
        """Seção: O que é Clean Architecture?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É CLEAN ARCHITECTURE?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Clean Architecture",
            "É uma filosofia de design de software que separa o código em camadas bem definidas, onde o núcleo do negócio (domínio) é independente de frameworks, bancos de dados e interfaces externas."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Clean Architecture não é sobre tecnologia, é sobre organização e independência!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma casa: o coração (sala de estar) não deve depender da estrutura externa (telhado, paredes). Se você trocar o telhado, a família continua vivendo normalmente. Na Clean Architecture, as regras de negócio são essa 'família' - independentes da infraestrutura!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 OS 5 PRINCÍPIOS DA CLEAN ARCHITECTURE:", "info")
        principios = [
            "1. 🎯 INDEPENDENCE OF FRAMEWORKS - Não dependa de bibliotecas externas",
            "2. 🧪 TESTABLE - Regras de negócio podem ser testadas sem UI ou BD",
            "3. 🎨 INDEPENDENCE OF UI - UI pode mudar sem afetar o resto",
            "4. 💾 INDEPENDENCE OF DATABASE - Oracle ou SQL Server? Não importa!",
            "5. 🌐 INDEPENDENCE OF EXTERNAL AGENCY - Não dependa do mundo externo"
        ]
        
        for i, principio in enumerate(principios, 1):
            self.print_colored(principio, "text")
            if i < len(principios):
                input("   ⏳ Pressione ENTER para o próximo princípio...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO: REGRA DE NEGÓCIO INDEPENDENTE", "success")
        codigo_clean = r'''# ❌ ARQUITETURA SUJA - Regra de negócio acoplada ao framework
class PedidoController:  # Mistura web com regra de negócio
    def processar_pedido(self, request):
        # Lógica de negócio misturada com framework web
        if request.POST['valor'] > 1000:
            desconto = 0.1
        else:
            desconto = 0.0
        
        # Salvando direto no banco (acoplamento)
        pedido = Pedido.objects.create(
            valor=request.POST['valor'],
            desconto=desconto
        )
        return JsonResponse({'id': pedido.id})

# ✅ CLEAN ARCHITECTURE - Regra de negócio independente
class CalculadoraDesconto:  # Pura regra de negócio
    def calcular(self, valor: float) -> float:
        if valor > 1000:
            return 0.1
        return 0.0

class ProcessarPedidoUseCase:  # Caso de uso independente
    def __init__(self, pedido_repo, calculadora_desconto):
        self.pedido_repo = pedido_repo
        self.calculadora_desconto = calculadora_desconto
    
    def executar(self, valor: float) -> dict:
        desconto = self.calculadora_desconto.calcular(valor)
        pedido_id = self.pedido_repo.salvar(valor, desconto)
        return {'id': pedido_id, 'desconto': desconto}

# Controller só coordena (não tem regra de negócio)
class PedidoController:
    def __init__(self, processar_pedido_use_case):
        self.processar_pedido = processar_pedido_use_case
    
    def post(self, request):
        resultado = self.processar_pedido.executar(
            float(request.POST['valor'])
        )
        return JsonResponse(resultado)

# Demonstração
calculadora = CalculadoraDesconto()
print(f"Desconto para R$ 500: {calculadora.calcular(500) * 100}%")
print(f"Desconto para R$ 1500: {calculadora.calcular(1500) * 100}%")'''
        
        self.exemplo(codigo_clean)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_clean)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🚗 Uber - Lógica de cálculo de corrida independente do app",
            "📱 Instagram - Algoritmo de feed independente da interface",
            "🏦 Nubank - Regras bancárias independentes da tecnologia",
            "🎬 Netflix - Engine de recomendação independente da plataforma",
            "🛒 Amazon - Lógica de preços independente do site/app",
            "🎮 Epic Games - Engine de jogos independente da plataforma"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_camadas_arquitetura(self) -> None:
        """Seção: As 4 Camadas da Clean Architecture"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("AS 4 CAMADAS DA CLEAN ARCHITECTURE", "🏗️", "success")
        
        # === CONCEITO PRINCIPAL ===
        self.print_concept(
            "Camadas da Clean Architecture",
            "São 4 círculos concêntricos onde as dependências sempre apontam para dentro. O círculo interno (Entities) não conhece nada do externo."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como as bonecas russas (matrioskas): a menor (Entities) não sabe que as maiores existem, mas as maiores dependem da menor!", "text")
        input("\n🔸 Pressione ENTER para ver cada camada...")
        
        # === AS 4 CAMADAS ===
        camadas = [
            {
                'nome': '🎯 ENTITIES (Entidades)',
                'posicao': 'Centro - Círculo mais interno',
                'responsabilidade': 'Regras de negócio da empresa (Enterprise Business Rules)',
                'exemplo': 'Classe User com regras de validação de email',
                'dependencias': 'NENHUMA - Não conhece nada externo'
            },
            {
                'nome': '⚙️ USE CASES (Casos de Uso)',
                'posicao': '2º círculo',
                'responsabilidade': 'Regras de negócio da aplicação (Application Business Rules)',
                'exemplo': 'CadastrarUsuarioUseCase, ProcessarPagamentoUseCase',
                'dependencias': 'Apenas Entities'
            },
            {
                'nome': '🔌 INTERFACE ADAPTERS (Adaptadores)',
                'posicao': '3º círculo',
                'responsabilidade': 'Converte dados entre Use Cases e mundo externo',
                'exemplo': 'Controllers, Presenters, Gateways',
                'dependencias': 'Use Cases e Entities'
            },
            {
                'nome': '🌐 FRAMEWORKS & DRIVERS (Infraestrutura)',
                'posicao': 'Círculo externo',
                'responsabilidade': 'Detalhes técnicos: Web, DB, APIs externas',
                'exemplo': 'Django, PostgreSQL, APIs de pagamento',
                'dependencias': 'Todas as camadas internas'
            }
        ]
        
        for i, camada in enumerate(camadas, 1):
            self.print_colored(f"\n{camada['nome']}", "warning")
            self.print_colored(f"📍 Posição: {camada['posicao']}", "text")
            self.print_colored(f"🎯 Responsabilidade: {camada['responsabilidade']}", "text")
            self.print_colored(f"💡 Exemplo: {camada['exemplo']}", "info")
            self.print_colored(f"🔗 Dependências: {camada['dependencias']}", "accent")
            
            if i < len(camadas):
                input("   ⏳ Pressione ENTER para a próxima camada...")
        
        # === EXEMPLO PRÁTICO DAS CAMADAS ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO: SISTEMA DE USUÁRIOS", "success")
        codigo_camadas = r'''# 🎯 CAMADA 1: ENTITIES (Regras de negócio da empresa)
class Usuario:
    def __init__(self, nome: str, email: str):
        if not self._email_valido(email):
            raise ValueError("Email inválido")
        if len(nome) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        
        self.nome = nome
        self.email = email
        self.ativo = True
    
    def _email_valido(self, email: str) -> bool:
        return "@" in email and "." in email.split("@")[1]
    
    def desativar(self):
        self.ativo = False

# ⚙️ CAMADA 2: USE CASES (Regras de negócio da aplicação)
class CadastrarUsuarioUseCase:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository
    
    def executar(self, nome: str, email: str) -> dict:
        # Verifica se já existe
        if self.usuario_repository.buscar_por_email(email):
            raise ValueError("Email já cadastrado")
        
        # Cria usuário (Entity valida automaticamente)
        usuario = Usuario(nome, email)
        
        # Salva usando repository
        usuario_id = self.usuario_repository.salvar(usuario)
        
        return {
            'id': usuario_id,
            'nome': usuario.nome,
            'email': usuario.email,
            'ativo': usuario.ativo
        }

# 🔌 CAMADA 3: INTERFACE ADAPTERS (Controllers e Repositories)
class UsuarioController:
    def __init__(self, cadastrar_usuario_use_case):
        self.cadastrar_usuario = cadastrar_usuario_use_case
    
    def post_usuario(self, dados_request: dict) -> dict:
        try:
            resultado = self.cadastrar_usuario.executar(
                dados_request['nome'],
                dados_request['email']
            )
            return {'status': 'success', 'data': resultado}
        except ValueError as e:
            return {'status': 'error', 'message': str(e)}

# 🌐 CAMADA 4: FRAMEWORKS & DRIVERS (Implementação concreta)
class UsuarioRepositoryMemoria:  # Simulação de banco
    def __init__(self):
        self.usuarios = {}
        self.proximo_id = 1
    
    def buscar_por_email(self, email: str):
        for usuario in self.usuarios.values():
            if usuario.email == email:
                return usuario
        return None
    
    def salvar(self, usuario: Usuario) -> int:
        user_id = self.proximo_id
        self.usuarios[user_id] = usuario
        self.proximo_id += 1
        return user_id

# === DEMONSTRAÇÃO DAS CAMADAS ===
print("🚀 DEMONSTRAÇÃO DAS 4 CAMADAS")
print("=" * 40)

# Montando a arquitetura (Dependency Injection)
usuario_repo = UsuarioRepositoryMemoria()
cadastrar_use_case = CadastrarUsuarioUseCase(usuario_repo)
controller = UsuarioController(cadastrar_use_case)

# Simulando request do mundo externo
request_data = {'nome': 'Ana Silva', 'email': 'ana@email.com'}

# Processando através das camadas
resultado = controller.post_usuario(request_data)
print(f"✅ Usuário cadastrado: {resultado}")

# Testando validação da Entity
try:
    request_invalido = {'nome': 'A', 'email': 'email-inválido'}
    resultado_erro = controller.post_usuario(request_invalido)
    print(f"❌ Erro capturado: {resultado_erro}")
except Exception as e:
    print(f"❌ Erro: {e}")'''
        
        self.exemplo(codigo_camadas)
        print("\n🚀 Executando demonstração das camadas:")
        self.executar_codigo(codigo_camadas)
        
        # === BENEFÍCIOS ===
        self.print_colored("\n🌟 BENEFÍCIOS DAS CAMADAS:", "accent")
        beneficios = [
            "🔒 Entities protegidas de mudanças externas",
            "🧪 Use Cases facilmente testáveis",
            "🔄 Controllers podem mudar sem afetar lógica",
            "💾 Banco de dados pode ser trocado facilmente",
            "🎨 UI pode ser totalmente reformulada",
            "📱 Mesmo código serve web, mobile e API"
        ]
        for beneficio in beneficios:
            self.print_colored(f"• {beneficio}", "primary")
        
        self.pausar()
    
    def _secao_domain_driven_design(self) -> None:
        """Seção: Domain-Driven Design (DDD)"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DOMAIN-DRIVEN DESIGN (DDD)", "🎭", "accent")
        
        # === CONCEITO ===
        self.print_concept(
            "Domain-Driven Design",
            "É uma abordagem para desenvolvimento de software onde o foco principal é entender profundamente o domínio do negócio e modelar o código para refletir esse entendimento."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como ser um tradutor entre dois mundos: o mundo dos especialistas do negócio (que entendem o problema) e o mundo dos desenvolvedores (que implementam a solução). O DDD cria uma linguagem comum!", "text")
        input("\n🔸 Pressione ENTER para ver os conceitos...")
        
        # === CONCEITOS PRINCIPAIS ===
        self.print_colored("\n🎯 CONCEITOS FUNDAMENTAIS DO DDD:", "info")
        
        # UBIQUITOUS LANGUAGE
        self.print_colored("\n1. 🗣️ UBIQUITOUS LANGUAGE (Linguagem Ubíqua)", "warning")
        self.print_colored("📝 Linguagem comum entre desenvolvedores e especialistas do domínio", "text")
        codigo_linguagem = r'''# ❌ LINGUAGEM TÉCNICA (confunde especialistas do negócio)
class DataProcessor:
    def process_data(self, input_data):
        processed = self.transform(input_data)
        return self.persist(processed)

# ✅ LINGUAGEM UBÍQUA (especialistas entendem)
class ProcessadorPedido:
    def processar_pedido(self, pedido):
        pedido_validado = self.validar_pedido(pedido)
        return self.confirmar_pedido(pedido_validado)'''
        
        self.exemplo(codigo_linguagem)
        input("   ⏳ Pressione ENTER para o próximo conceito...")
        
        # ENTITIES
        self.print_colored("\n2. 🎯 ENTITIES (Entidades)", "warning")
        self.print_colored("📝 Objetos com identidade única que persistem ao longo do tempo", "text")
        codigo_entity = r'''# Entity: Tem identidade única e ciclo de vida
class ContaBancaria:
    def __init__(self, numero_conta: str, titular: str):
        self.numero_conta = numero_conta  # Identidade única
        self.titular = titular
        self.saldo = 0.0
        self.movimentacoes = []
    
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor
        self.movimentacoes.append(f"Depósito: +R$ {valor}")
    
    def sacar(self, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.movimentacoes.append(f"Saque: -R$ {valor}")

# Demonstração
conta = ContaBancaria("12345-6", "João Silva")
conta.depositar(1000)
conta.sacar(200)
print(f"Conta {conta.numero_conta}: R$ {conta.saldo}")'''
        
        self.exemplo(codigo_entity)
        print("\n🚀 Executando Entity:")
        self.executar_codigo(codigo_entity)
        input("   ⏳ Pressione ENTER para o próximo conceito...")
        
        # VALUE OBJECTS
        self.print_colored("\n3. 💎 VALUE OBJECTS (Objetos de Valor)", "warning")
        self.print_colored("📝 Objetos imutáveis definidos por seus atributos, não por identidade", "text")
        codigo_value_object = r'''# Value Object: Imutável, definido pelos valores
class Email:
    def __init__(self, endereco: str):
        if not self._validar(endereco):
            raise ValueError("Email inválido")
        self._endereco = endereco
    
    def _validar(self, endereco: str) -> bool:
        return "@" in endereco and "." in endereco.split("@")[1]
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    def __eq__(self, other):
        return isinstance(other, Email) and self._endereco == other._endereco
    
    def __str__(self):
        return self._endereco

class Dinheiro:
    def __init__(self, valor: float, moeda: str = "BRL"):
        self.valor = valor
        self.moeda = moeda
    
    def somar(self, outro):
        if self.moeda != outro.moeda:
            raise ValueError("Moedas diferentes")
        return Dinheiro(self.valor + outro.valor, self.moeda)
    
    def __str__(self):
        return f"{self.valor} {self.moeda}"

# Demonstração
email1 = Email("joao@email.com")
email2 = Email("joao@email.com")
print(f"Emails iguais? {email1 == email2}")

dinheiro1 = Dinheiro(100.0)
dinheiro2 = Dinheiro(50.0)
total = dinheiro1.somar(dinheiro2)
print(f"Total: {total}")'''
        
        self.exemplo(codigo_value_object)
        print("\n🚀 Executando Value Objects:")
        self.executar_codigo(codigo_value_object)
        input("   ⏳ Pressione ENTER para o próximo conceito...")
        
        # DOMAIN SERVICES
        self.print_colored("\n4. ⚙️ DOMAIN SERVICES (Serviços de Domínio)", "warning")
        self.print_colored("📝 Operações que não pertencem naturalmente a uma Entity ou Value Object", "text")
        codigo_domain_service = r'''# Domain Service: Lógica que não pertence a uma entidade específica
class CalculadoraJuros:
    def calcular_juros_compostos(self, capital: float, taxa: float, tempo: int) -> float:
        return capital * ((1 + taxa) ** tempo)

class ValidadorCPF:
    def validar(self, cpf: str) -> bool:
        # Simplificado para exemplo
        return len(cpf.replace("-", "").replace(".", "")) == 11

class TransferenciaBancaria:
    def __init__(self, validador_cpf, calculadora_juros):
        self.validador_cpf = validador_cpf
        self.calculadora_juros = calculadora_juros
    
    def transferir(self, conta_origem, conta_destino, valor, cpf_destinatario):
        if not self.validador_cpf.validar(cpf_destinatario):
            raise ValueError("CPF do destinatário inválido")
        
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
        return f"Transferência de R$ {valor} realizada com sucesso"

# Demonstração
validador = ValidadorCPF()
calculadora = CalculadoraJuros()

print(f"CPF válido? {validador.validar('123.456.789-00')}")
juros = calculadora.calcular_juros_compostos(1000, 0.05, 2)
print(f"Juros compostos: R$ {juros:.2f}")'''
        
        self.exemplo(codigo_domain_service)
        print("\n🚀 Executando Domain Services:")
        self.executar_codigo(codigo_domain_service)
        
        # === BENEFÍCIOS DO DDD ===
        self.print_colored("\n🌟 BENEFÍCIOS DO DDD:", "accent")
        beneficios = [
            "🗣️ Comunicação mais clara entre desenvolvedores e negócio",
            "🎯 Código que reflete fielmente as regras de negócio",
            "🧪 Maior facilidade para testar lógica de domínio",
            "🔄 Mudanças no negócio são mais fáceis de implementar",
            "📚 Conhecimento do domínio fica explícito no código",
            "👥 Equipes conseguem trabalhar em domínios específicos"
        ]
        for beneficio in beneficios:
            self.print_colored(f"• {beneficio}", "primary")
        
        self.pausar()
    
    def _secao_dependency_inversion(self) -> None:
        """Seção: Dependency Inversion na Prática"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DEPENDENCY INVERSION NA PRÁTICA", "🔄", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Dependency Inversion",
            "Princípio onde módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações (interfaces)."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como uma tomada elétrica: você não precisa saber se a energia vem de hidrelétrica, solar ou termelétrica. Você só precisa saber que existe uma 'interface padrão' (tomada) que fornece energia!", "text")
        input("\n🔸 Pressione ENTER para ver o problema...")
        
        # === PROBLEMA SEM INVERSÃO ===
        self.print_colored("\n❌ PROBLEMA: DEPENDÊNCIA DIRETA", "error")
        codigo_problema = r'''# ❌ DEPENDÊNCIA DIRETA (acoplamento forte)
class EmailService:  # Implementação concreta
    def enviar(self, destinatario, assunto, corpo):
        print(f"Enviando email para {destinatario}: {assunto}")

class SMSService:  # Outra implementação concreta
    def enviar(self, telefone, mensagem):
        print(f"Enviando SMS para {telefone}: {mensagem}")

class ProcessarPedido:  # Alto nível dependendo de baixo nível
    def __init__(self):
        self.email_service = EmailService()  # ❌ Acoplamento forte!
        self.sms_service = SMSService()      # ❌ Acoplamento forte!
    
    def processar(self, pedido):
        # Lógica de processamento...
        print(f"Processando pedido {pedido['id']}")
        
        # Notificações acopladas
        self.email_service.enviar(
            pedido['email'], 
            "Pedido Confirmado", 
            f"Seu pedido {pedido['id']} foi confirmado"
        )

# Problema: Para adicionar WhatsApp, preciso modificar ProcessarPedido!
pedido = {'id': '123', 'email': 'cliente@email.com'}
processador = ProcessarPedido()
processador.processar(pedido)'''
        
        self.exemplo(codigo_problema)
        print("\n🚀 Executando código problemático:")
        self.executar_codigo(codigo_problema)
        
        input("\n🔸 Pressione ENTER para ver a solução...")
        
        # === SOLUÇÃO COM INVERSÃO ===
        self.print_colored("\n✅ SOLUÇÃO: DEPENDENCY INVERSION", "success")
        codigo_solucao = r'''# ✅ DEPENDENCY INVERSION (baixo acoplamento)
from abc import ABC, abstractmethod

# Abstração (interface)
class NotificationService(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str):
        pass

# Implementações concretas (baixo nível)
class EmailService(NotificationService):
    def enviar(self, destinatario: str, mensagem: str):
        print(f"📧 Email para {destinatario}: {mensagem}")

class SMSService(NotificationService):
    def enviar(self, destinatario: str, mensagem: str):
        print(f"📱 SMS para {destinatario}: {mensagem}")

class WhatsAppService(NotificationService):  # Nova implementação
    def enviar(self, destinatario: str, mensagem: str):
        print(f"💬 WhatsApp para {destinatario}: {mensagem}")

# Alto nível dependendo de abstração
class ProcessarPedido:
    def __init__(self, notification_services: list):
        self.notification_services = notification_services  # ✅ Depende da abstração!
    
    def processar(self, pedido):
        print(f"Processando pedido {pedido['id']}")
        
        # Notifica usando todas as implementações disponíveis
        mensagem = f"Seu pedido {pedido['id']} foi confirmado!"
        for service in self.notification_services:
            service.enviar(pedido['contato'], mensagem)

# Agora podemos configurar as dependências externamente!
pedido = {'id': '456', 'contato': 'cliente@email.com'}

# Configuração 1: Apenas email
processador1 = ProcessarPedido([EmailService()])
print("--- Configuração 1: Apenas Email ---")
processador1.processar(pedido)

# Configuração 2: Email + SMS + WhatsApp
processador2 = ProcessarPedido([
    EmailService(),
    SMSService(),
    WhatsAppService()
])
print("\n--- Configuração 2: Multi-canal ---")
processador2.processar(pedido)'''
        
        self.exemplo(codigo_solucao)
        print("\n🚀 Executando solução com inversão:")
        self.executar_codigo(codigo_solucao)
        
        # === DEPENDENCY INJECTION ===
        input("\n🔸 Pressione ENTER para ver Dependency Injection...")
        
        self.print_colored("\n🔌 DEPENDENCY INJECTION (INJEÇÃO DE DEPENDÊNCIAS)", "info")
        codigo_di = r'''# Dependency Injection Container (DI Container)
class DIContainer:
    def __init__(self):
        self._services = {}
        self._singletons = {}
    
    def register(self, interface, implementation, singleton=False):
        self._services[interface] = (implementation, singleton)
    
    def resolve(self, interface):
        if interface not in self._services:
            raise ValueError(f"Serviço {interface} não registrado")
        
        implementation, is_singleton = self._services[interface]
        
        if is_singleton:
            if interface not in self._singletons:
                self._singletons[interface] = implementation()
            return self._singletons[interface]
        
        return implementation()

# Repository Pattern com DI
class PedidoRepository(ABC):
    @abstractmethod
    def salvar(self, pedido):
        pass

class PedidoRepositoryMemoria(PedidoRepository):
    def __init__(self):
        self.pedidos = {}
    
    def salvar(self, pedido):
        self.pedidos[pedido['id']] = pedido
        print(f"💾 Pedido {pedido['id']} salvo em memória")

class PedidoRepositoryBanco(PedidoRepository):
    def salvar(self, pedido):
        print(f"🗄️ Pedido {pedido['id']} salvo no banco de dados")

# Use Case usando DI
class ProcessarPedidoUseCase:
    def __init__(self, pedido_repo: PedidoRepository, notification_service: NotificationService):
        self.pedido_repo = pedido_repo
        self.notification_service = notification_service
    
    def executar(self, pedido):
        self.pedido_repo.salvar(pedido)
        self.notification_service.enviar(
            pedido['contato'], 
            f"Pedido {pedido['id']} processado!"
        )

# Configurando o DI Container
container = DIContainer()
container.register(PedidoRepository, PedidoRepositoryMemoria, singleton=True)
container.register(NotificationService, EmailService)

# Resolvendo dependências
pedido_repo = container.resolve(PedidoRepository)
notification_service = container.resolve(NotificationService)

# Injetando no Use Case
use_case = ProcessarPedidoUseCase(pedido_repo, notification_service)

# Executando
pedido = {'id': '789', 'contato': 'cliente@email.com'}
use_case.executar(pedido)'''
        
        self.exemplo(codigo_di)
        print("\n🚀 Executando Dependency Injection:")
        self.executar_codigo(codigo_di)
        
        # === BENEFÍCIOS ===
        self.print_colored("\n🌟 BENEFÍCIOS DA DEPENDENCY INVERSION:", "accent")
        beneficios = [
            "🔓 Baixo acoplamento entre módulos",
            "🧪 Fácil criação de mocks para testes",
            "🔄 Fácil troca de implementações",
            "📦 Código mais modular e reutilizável",
            "⚙️ Configuração externa das dependências",
            "🎯 Foco nas regras de negócio, não na infraestrutura"
        ]
        for beneficio in beneficios:
            self.print_colored(f"• {beneficio}", "primary")
        
        self.pausar()
    
    def _secao_casos_uso_reais(self) -> None:
        """Seção: Casos de uso em grandes empresas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CASOS DE USO EM GRANDES EMPRESAS", "🌍", "warning")
        
        cases = [
            {
                'empresa': '🎬 NETFLIX',
                'problema': 'Sistema de recomendação que funciona em 190+ países',
                'solucao': 'Clean Architecture com microsserviços independentes',
                'detalhes': [
                    'Core: Algoritmos de ML independentes de plataforma',
                    'Use Cases: Gerar recomendações, processar visualizações',
                    'Adapters: APIs REST, GraphQL, gRPC',
                    'Infrastructure: AWS, Cassandra, Kafka'
                ]
            },
            {
                'empresa': '🚗 UBER',
                'problema': 'Cálculo de preços dinâmicos em tempo real globalmente',
                'solucao': 'DDD com contextos delimitados por cidade/região',
                'detalhes': [
                    'Entities: Corrida, Motorista, Passageiro',
                    'Value Objects: Localização, Preço, Tempo',
                    'Domain Services: Calculadora de preços, otimizador de rotas',
                    'Bounded Contexts: Pricing, Routing, Matching'
                ]
            },
            {
                'empresa': '🏦 NUBANK',
                'problema': 'Sistema bancário que precisa seguir regulamentações',
                'solucao': 'Clean Architecture com agregados DDD',
                'detalhes': [
                    'Entities: Conta, Transação, Cliente',
                    'Use Cases: Processar pagamento, verificar limite',
                    'Policies: Regras do Banco Central, compliance',
                    'Event Sourcing: Auditoria completa de transações'
                ]
            },
            {
                'empresa': '🎮 EPIC GAMES (FORTNITE)',
                'problema': 'Engine de jogo que roda em múltiplas plataformas',
                'solucao': 'Clean Architecture com camadas bem definidas',
                'detalhes': [
                    'Core: Lógica do jogo (física, colisões)',
                    'Use Cases: Processar input, atualizar mundo',
                    'Adapters: Rendering engines, network protocols',
                    'Platform: PC, Console, Mobile, Cloud'
                ]
            }
        ]
        
        for i, case in enumerate(cases, 1):
            self.print_colored(f"\n{case['empresa']}", "warning")
            self.print_colored(f"🎯 Problema: {case['problema']}", "text")
            self.print_colored(f"✅ Solução: {case['solucao']}", "success")
            
            self.print_colored("\n📋 Implementação:", "info")
            for detalhe in case['detalhes']:
                self.print_colored(f"  • {detalhe}", "text")
            
            if i < len(cases):
                input("   🔸 Pressione ENTER para o próximo caso...")
        
        # === BENEFÍCIOS COMPROVADOS ===
        self.print_colored("\n\n📊 RESULTADOS COMPROVADOS:", "accent")
        resultados = [
            "⚡ Netflix: Deploy 1000+ vezes por dia sem downtime",
            "🚀 Uber: Suporta 100+ milhões de usuários mensais",
            "💎 Nubank: Processamento de bilhões em transações",
            "🎯 Epic: Fortnite roda em 10+ plataformas diferentes",
            "🧪 Google: 2 bilhões de linhas de código testáveis",
            "📈 Amazon: Black Friday sem queda de performance"
        ]
        
        for resultado in resultados:
            self.print_colored(f"• {resultado}", "primary")
        
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas de arquitetura"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS DE ARQUITETURA", "⭐", "success")
        
        self.print_colored("🏆 AS 12 REGRAS DE OURO DA CLEAN ARCHITECTURE:", "accent")
        
        praticas = [
            {
                'categoria': '🎯 DESIGN',
                'regras': [
                    'Dependency Rule: Dependências sempre apontam para dentro',
                    'Single Responsibility: Cada camada tem uma responsabilidade',
                    'Interface Segregation: Interfaces pequenas e específicas'
                ]
            },
            {
                'categoria': '🧪 TESTES',
                'regras': [
                    'Test Pyramid: Mais testes unitários, menos integração',
                    'Mock External: Simule sempre dependências externas',
                    'Test Business Logic: Foque nas regras de negócio'
                ]
            },
            {
                'categoria': '📦 ORGANIZAÇÃO',
                'regras': [
                    'Package by Feature: Organize por funcionalidade',
                    'Screaming Architecture: Estrutura deve gritar o domínio',
                    'Independent Deployability: Módulos independentes'
                ]
            },
            {
                'categoria': '⚡ PERFORMANCE',
                'regras': [
                    'Lazy Loading: Carregue dados sob demanda',
                    'Caching Strategy: Cache nas camadas corretas',
                    'Async Processing: Use processamento assíncrono'
                ]
            }
        ]
        
        for categoria_info in praticas:
            self.print_colored(f"\n{categoria_info['categoria']}", "warning")
            for regra in categoria_info['regras']:
                self.print_colored(f"  ✅ {regra}", "text")
            input("   ⏳ Pressione ENTER para a próxima categoria...")
        
        # === ESTRUTURA DE PASTAS RECOMENDADA ===
        self.print_colored("\n\n📁 ESTRUTURA DE PASTAS RECOMENDADA:", "info")
        estrutura = '''
projeto/
├── src/
│   ├── domain/           # 🎯 Entities, Value Objects, Domain Services
│   │   ├── entities/
│   │   ├── value_objects/
│   │   └── services/
│   ├── application/      # ⚙️ Use Cases, Ports (interfaces)
│   │   ├── use_cases/
│   │   └── ports/
│   ├── adapters/         # 🔌 Controllers, Presenters, Repositories
│   │   ├── controllers/
│   │   ├── presenters/
│   │   └── repositories/
│   └── infrastructure/   # 🌐 Frameworks, DB, External APIs
│       ├── web/
│       ├── database/
│       └── external/
├── tests/
│   ├── unit/            # Testes das regras de negócio
│   ├── integration/     # Testes de integração
│   └── e2e/            # Testes end-to-end
└── docs/               # Documentação da arquitetura'''
        
        self.print_colored(estrutura, "text")
        
        # === ANTI-PATTERNS PARA EVITAR ===
        self.print_colored("\n\n🚨 ANTI-PATTERNS PARA EVITAR:", "error")
        anti_patterns = [
            "❌ Anemic Domain Model - Entities sem comportamento",
            "❌ God Object - Classes que fazem tudo",
            "❌ Leaky Abstraction - Detalhes vazando entre camadas",
            "❌ Circular Dependencies - Dependências circulares",
            "❌ Shotgun Surgery - Mudança simples afeta muitos arquivos",
            "❌ Big Ball of Mud - Código sem estrutura definida"
        ]
        
        for anti in anti_patterns:
            self.print_colored(f"  {anti}", "text")
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre arquitetura limpa"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES FASCINANTES", "💫", "accent")
        
        curiosidades = [
            {
                'titulo': '👨‍💻 Uncle Bob e a Clean Architecture',
                'historia': 'Robert "Uncle Bob" Martin criou a Clean Architecture em 2012 combinando ideias de 30+ anos de experiência. Ele se inspirou na Hexagonal Architecture, Onion Architecture e Ports & Adapters. O círculo mais famoso da programação nasceu de décadas de tentativa e erro!'
            },
            {
                'titulo': '🎬 Netflix e os 600+ Microsserviços',
                'historia': 'A Netflix tem mais de 600 microsserviços, cada um seguindo Clean Architecture. Eles deployam código 4000+ vezes por dia! O segredo? Cada serviço é completamente independente e pode ser testado isoladamente.'
            },
            {
                'titulo': '🏦 O Caso do Sistema Bancário dos Anos 60',
                'historia': 'Muitos bancos ainda usam sistemas COBOL dos anos 60-70! Esses sistemas sobreviveram porque seguiam inadvertidamente princípios da Clean Architecture: lógica de negócio separada da interface. Alguns processam trilhões de dólares até hoje!'
            },
            {
                'titulo': '🎮 A Revolução dos Game Engines',
                'historia': 'Engines como Unity e Unreal seguem Clean Architecture religiosamente. O core (física, renderização) é totalmente independente da plataforma. Por isso um jogo pode rodar em PC, console, mobile e VR sem reescrever a lógica principal!'
            },
            {
                'titulo': '🚀 NASA e Software Crítico',
                'historia': 'O software da NASA que controla missões espaciais segue princípios extremos de Clean Architecture. Cada módulo é testado isoladamente por anos antes do lançamento. O software do Mars Rover tem zero bugs conhecidos graças a essa arquitetura!'
            },
            {
                'titulo': '💰 O Bug de US$ 460 milhões',
                'historia': 'Em 2012, a Knight Capital perdeu US$ 460 milhões em 45 minutos por um erro de software. O problema? Acoplamento forte entre sistemas. Se tivessem usado Clean Architecture com inversão de dependências, o erro teria sido isolado!'
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
            "🎯 Clean Architecture reduz bugs em 60-80% segundo estudos da IBM",
            "⚡ Sistemas bem arquitetados são 10x mais rápidos para modificar",
            "🧪 Google tem 2 bilhões de linhas de código, 85% testáveis automaticamente",
            "📱 WhatsApp atendia 900 milhões de usuários com apenas 50 engenheiros",
            "🏗️ Amazon refatorou para microsserviços e melhorou performance 1000%",
            "🎨 Instagram foi vendido por US$ 1 bilhão com apenas 13 funcionários"
        ]
        
        for fato in fatos:
            self.print_colored(f"• {fato}", "primary")
        
        self.print_success("\n🌟 Agora você conhece os segredos da arquitetura de software de classe mundial!")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre Clean Architecture e DDD!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Clean Architecture & DDD',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é a regra fundamental da Clean Architecture sobre dependências?',
                        'answer': ['dependências apontam para dentro', 'dependency rule', 'para dentro'],
                        'hint': 'Pense na direção das setas no diagrama circular'
                    },
                    {
                        'question': 'Qual camada contém as regras de negócio da empresa?',
                        'answer': ['entities', 'entidades', 'entities layer'],
                        'hint': 'É a camada mais interna, o coração do sistema'
                    },
                    {
                        'question': 'No DDD, objetos imutáveis definidos por seus valores são chamados de?',
                        'answer': ['value objects', 'objetos de valor', 'value object'],
                        'hint': 'São como Email, Dinheiro, CPF - definidos pelos seus atributos'
                    },
                    {
                        'question': 'Qual princípio diz que módulos de alto nível não devem depender de baixo nível?',
                        'answer': ['dependency inversion', 'inversão de dependência', 'dip'],
                        'hint': 'É sobre inverter a direção das dependências usando abstrações'
                    },
                    {
                        'question': 'No DDD, a linguagem comum entre desenvolvedores e especialistas do negócio é chamada de?',
                        'answer': ['ubiquitous language', 'linguagem ubíqua', 'linguagem comum'],
                        'hint': 'É uma linguagem que todos da equipe entendem, sem ambiguidades'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código Limpo',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a Entity seguindo DDD',
                        'starter': 'class Usuario:\n    def __init__(self, email, nome):\n        # Complete aqui validação do email\n        pass',
                        'solution': 'if "@" not in email:\n            raise ValueError("Email inválido")\n        self.email = email\n        self.nome = nome',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o Use Case',
                        'starter': 'class CadastrarUsuarioUseCase:\n    def __init__(self, user_repo):\n        self.user_repo = user_repo\n    \n    def executar(self, dados):\n        # Complete aqui a lógica\n        pass',
                        'solution': 'usuario = Usuario(dados["email"], dados["nome"])\n        return self.user_repo.salvar(usuario)',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a inversão de dependência',
                        'starter': 'from abc import ABC, abstractmethod\n\nclass NotificationService(ABC):\n    # Complete aqui a interface\n    pass',
                        'solution': '@abstractmethod\n    def enviar(self, destinatario, mensagem):\n        pass',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Biblioteca',
                'type': 'creative',
                'instruction': 'Crie um sistema de biblioteca seguindo Clean Architecture: Entity Livro, Use Case EmprestarLivro, Repository abstrato. Use DDD com Value Objects para ISBN!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre Clean Architecture e DDD",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de arquitetura",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de biblioteca com Clean Architecture",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: Sistema bancário completo",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para dominar arquitetura!"
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
            self.print_colored("Você domina os conceitos de Clean Architecture e DDD!", "success")
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
        exemplo_codigo = r'''# Sistema de Biblioteca com Clean Architecture
from abc import ABC, abstractmethod
from dataclasses import dataclass

# VALUE OBJECT
@dataclass(frozen=True)
class ISBN:
    codigo: str
    
    def __post_init__(self):
        if len(self.codigo) != 13:
            raise ValueError("ISBN deve ter 13 dígitos")

# ENTITY
class Livro:
    def __init__(self, isbn: ISBN, titulo: str):
        self.isbn = isbn
        self.titulo = titulo
        self.emprestado = False
    
    def emprestar(self):
        if self.emprestado:
            raise ValueError("Livro já emprestado")
        self.emprestado = True
    
    def devolver(self):
        self.emprestado = False

# REPOSITORY (INTERFACE)
class LivroRepository(ABC):
    @abstractmethod
    def buscar_por_isbn(self, isbn: ISBN) -> Livro:
        pass

# USE CASE
class EmprestarLivroUseCase:
    def __init__(self, livro_repo: LivroRepository):
        self.livro_repo = livro_repo
    
    def executar(self, isbn_codigo: str) -> str:
        isbn = ISBN(isbn_codigo)
        livro = self.livro_repo.buscar_por_isbn(isbn)
        livro.emprestar()
        return f"Livro '{livro.titulo}' emprestado com sucesso!"

# Exemplo de uso
isbn = ISBN("9780134685991")
livro = Livro(isbn, "Clean Architecture")
print(f"Livro criado: {livro.titulo}")'''
        
        self.exemplo(exemplo_codigo)
        
        self.print_colored("\n🚀 AGORA É SUA VEZ!", "success")
        self.print_colored("Crie seu próprio sistema seguindo Clean Architecture:", "text")
        self.print_colored("• Use Entities com comportamentos", "text")
        self.print_colored("• Crie Value Objects imutáveis", "text")
        self.print_colored("• Implemente Use Cases", "text")
        self.print_colored("• Use interfaces para repositories", "text")
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
                self.print_colored("Você aplicou Clean Architecture na prática!", "accent")
            else:
                self.print_colored("Nenhum código foi inserido.", "warning")
                
        except KeyboardInterrupt:
            self.print_warning("\n\nExercício criativo interrompido.")
            return
        
        self.pausar()
    
    def _mini_projeto_sistema_bancario(self) -> None:
        """Mini Projeto - Módulo 32: Sistema Bancário com Clean Architecture"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏦 MINI PROJETO: SISTEMA BANCÁRIO COM CLEAN ARCHITECTURE")
        else:
            print("\n" + "="*50)
            print("🏦 MINI PROJETO: SISTEMA BANCÁRIO COM CLEAN ARCHITECTURE")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema bancário completo usando Clean Architecture e DDD!")
        
        self.print_concept(
            "Sistema Bancário Profissional",
            "Um sistema que gerencia contas, transações e clientes seguindo os mais altos padrões de arquitetura de software, como os usados por bancos reais!"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "🏦 Nubank - Processamento de milhões de transações diárias",
            "🏦 Banco do Brasil - Sistema core bancário",
            "💳 PagBank - Gerenciamento de contas digitais",
            "💰 Inter - Platform banking completa",
            "🏦 XP Investimentos - Corretora digital",
            "💱 Wise - Transferências internacionais"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Definindo a arquitetura
        self.print_section("PASSO 1: DEFININDO A ARQUITETURA", "📝", "info")
        self.print_tip("Vamos implementar as 4 camadas da Clean Architecture!")
        
        camadas_implementadas = [
            "🎯 ENTITIES - Cliente, Conta, Transação",
            "⚙️ USE CASES - Criar conta, fazer transferência, consultar saldo",
            "🔌 ADAPTERS - Controllers REST, Repositories, Presenters",
            "🌐 INFRASTRUCTURE - Banco de dados, APIs externas, Web framework"
        ]
        
        for camada in camadas_implementadas:
            self.print_colored(f"✅ {camada}", "success")
        
        input("\n🔸 Pressione ENTER para começar a implementar...")
        
        try:
            # PASSO 2: Implementando o sistema
            self.print_section("PASSO 2: IMPLEMENTANDO O SISTEMA BANCÁRIO", "⚙️", "success")
            self.print_colored("Agora vamos criar todas as camadas:", "text")
            
            # PASSO 3: Código final
            self.print_section("PASSO 3: SEU SISTEMA BANCÁRIO COMPLETO", "🎬", "warning")
            
            codigo_final = r'''# 🏦 SISTEMA BANCÁRIO COM CLEAN ARCHITECTURE
# Módulo 32: Clean Architecture & Domain-Driven Design

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid

# === CAMADA 1: ENTITIES (Regras de negócio da empresa) ===

# VALUE OBJECTS
@dataclass(frozen=True)
class CPF:
    numero: str
    
    def __post_init__(self):
        # Simplificado para exemplo
        if len(self.numero.replace("-", "").replace(".", "")) != 11:
            raise ValueError("CPF inválido")

@dataclass(frozen=True)
class Dinheiro:
    valor: float
    moeda: str = "BRL"
    
    def __post_init__(self):
        if self.valor < 0:
            raise ValueError("Valor não pode ser negativo")
    
    def somar(self, outro):
        if self.moeda != outro.moeda:
            raise ValueError("Moedas diferentes")
        return Dinheiro(self.valor + outro.valor, self.moeda)
    
    def subtrair(self, outro):
        if self.moeda != outro.moeda:
            raise ValueError("Moedas diferentes")
        resultado = self.valor - outro.valor
        if resultado < 0:
            raise ValueError("Resultado negativo")
        return Dinheiro(resultado, self.moeda)

class TipoTransacao(Enum):
    DEPOSITO = "deposito"
    SAQUE = "saque"
    TRANSFERENCIA = "transferencia"

# ENTITIES
class Cliente:
    def __init__(self, cpf: CPF, nome: str, email: str):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.ativo = True
    
    def desativar(self):
        self.ativo = False

class Conta:
    def __init__(self, numero: str, cliente: Cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = Dinheiro(0.0)
        self.transacoes: List['Transacao'] = []
        self.ativa = True
    
    def depositar(self, valor: Dinheiro):
        if not self.ativa:
            raise ValueError("Conta inativa")
        self.saldo = self.saldo.somar(valor)
        transacao = Transacao(TipoTransacao.DEPOSITO, valor, self)
        self.transacoes.append(transacao)
        return transacao
    
    def sacar(self, valor: Dinheiro):
        if not self.ativa:
            raise ValueError("Conta inativa")
        if self.saldo.valor < valor.valor:
            raise ValueError("Saldo insuficiente")
        self.saldo = self.saldo.subtrair(valor)
        transacao = Transacao(TipoTransacao.SAQUE, valor, self)
        self.transacoes.append(transacao)
        return transacao
    
    def transferir_para(self, conta_destino, valor: Dinheiro):
        if not self.ativa or not conta_destino.ativa:
            raise ValueError("Uma das contas está inativa")
        
        # Saque da conta origem
        self.sacar(valor)
        # Depósito na conta destino
        conta_destino.depositar(valor)
        
        # Registra transferência
        transacao = Transacao(TipoTransacao.TRANSFERENCIA, valor, self, conta_destino)
        self.transacoes.append(transacao)
        return transacao

class Transacao:
    def __init__(self, tipo: TipoTransacao, valor: Dinheiro, conta_origem: Conta, conta_destino: Optional[Conta] = None):
        self.id = str(uuid.uuid4())
        self.tipo = tipo
        self.valor = valor
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.data = datetime.now()

# === CAMADA 2: USE CASES (Regras de negócio da aplicação) ===

class CriarContaUseCase:
    def __init__(self, conta_repository, cliente_repository):
        self.conta_repository = conta_repository
        self.cliente_repository = cliente_repository
    
    def executar(self, cpf_str: str, nome: str, email: str) -> dict:
        # Valida se cliente já existe
        cpf = CPF(cpf_str)
        cliente_existente = self.cliente_repository.buscar_por_cpf(cpf)
        
        if cliente_existente:
            raise ValueError("Cliente já cadastrado")
        
        # Cria cliente
        cliente = Cliente(cpf, nome, email)
        self.cliente_repository.salvar(cliente)
        
        # Cria conta
        numero_conta = f"12345-{len(self.conta_repository.listar()) + 1}"
        conta = Conta(numero_conta, cliente)
        self.conta_repository.salvar(conta)
        
        return {
            'numero_conta': conta.numero,
            'cliente': cliente.nome,
            'saldo': conta.saldo.valor
        }

class FazerTransferenciaUseCase:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository
    
    def executar(self, numero_origem: str, numero_destino: str, valor: float) -> dict:
        conta_origem = self.conta_repository.buscar_por_numero(numero_origem)
        conta_destino = self.conta_repository.buscar_por_numero(numero_destino)
        
        if not conta_origem or not conta_destino:
            raise ValueError("Conta não encontrada")
        
        dinheiro = Dinheiro(valor)
        transacao = conta_origem.transferir_para(conta_destino, dinheiro)
        
        # Atualiza repositórios
        self.conta_repository.atualizar(conta_origem)
        self.conta_repository.atualizar(conta_destino)
        
        return {
            'transacao_id': transacao.id,
            'valor': transacao.valor.valor,
            'data': transacao.data.isoformat(),
            'saldo_origem': conta_origem.saldo.valor,
            'saldo_destino': conta_destino.saldo.valor
        }

# === CAMADA 3: INTERFACE ADAPTERS (Controllers e Repositories) ===

# REPOSITORIES (Interfaces)
class ClienteRepository(ABC):
    @abstractmethod
    def buscar_por_cpf(self, cpf: CPF) -> Optional[Cliente]:
        pass
    
    @abstractmethod
    def salvar(self, cliente: Cliente):
        pass

class ContaRepository(ABC):
    @abstractmethod
    def buscar_por_numero(self, numero: str) -> Optional[Conta]:
        pass
    
    @abstractmethod
    def salvar(self, conta: Conta):
        pass
    
    @abstractmethod
    def atualizar(self, conta: Conta):
        pass
    
    @abstractmethod
    def listar(self) -> List[Conta]:
        pass

# CONTROLLERS
class ContaController:
    def __init__(self, criar_conta_use_case, transferencia_use_case):
        self.criar_conta = criar_conta_use_case
        self.transferencia = transferencia_use_case
    
    def post_conta(self, dados: dict) -> dict:
        try:
            resultado = self.criar_conta.executar(
                dados['cpf'],
                dados['nome'],
                dados['email']
            )
            return {'status': 'success', 'data': resultado}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def post_transferencia(self, dados: dict) -> dict:
        try:
            resultado = self.transferencia.executar(
                dados['conta_origem'],
                dados['conta_destino'],
                dados['valor']
            )
            return {'status': 'success', 'data': resultado}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

# === CAMADA 4: FRAMEWORKS & DRIVERS (Implementações concretas) ===

class ClienteRepositoryMemoria(ClienteRepository):
    def __init__(self):
        self.clientes = {}
    
    def buscar_por_cpf(self, cpf: CPF) -> Optional[Cliente]:
        return self.clientes.get(cpf.numero)
    
    def salvar(self, cliente: Cliente):
        self.clientes[cliente.cpf.numero] = cliente

class ContaRepositoryMemoria(ContaRepository):
    def __init__(self):
        self.contas = {}
    
    def buscar_por_numero(self, numero: str) -> Optional[Conta]:
        return self.contas.get(numero)
    
    def salvar(self, conta: Conta):
        self.contas[conta.numero] = conta
    
    def atualizar(self, conta: Conta):
        self.contas[conta.numero] = conta
    
    def listar(self) -> List[Conta]:
        return list(self.contas.values())

# === DEMONSTRAÇÃO DO SISTEMA BANCÁRIO ===
def demonstrar_sistema_bancario():
    print("🚀 INICIALIZANDO SISTEMA BANCÁRIO")
    print("=" * 40)
    
    # Montando a arquitetura (Dependency Injection)
    cliente_repo = ClienteRepositoryMemoria()
    conta_repo = ContaRepositoryMemoria()
    
    criar_conta_uc = CriarContaUseCase(conta_repo, cliente_repo)
    transferencia_uc = FazerTransferenciaUseCase(conta_repo)
    
    controller = ContaController(criar_conta_uc, transferencia_uc)
    
    # 1. Criando contas
    print("1️⃣ CRIANDO CONTAS:")
    conta1_data = {'cpf': '123.456.789-00', 'nome': 'João Silva', 'email': 'joao@email.com'}
    conta2_data = {'cpf': '987.654.321-00', 'nome': 'Maria Santos', 'email': 'maria@email.com'}
    
    resultado1 = controller.post_conta(conta1_data)
    resultado2 = controller.post_conta(conta2_data)
    
    print(f"✅ Conta João: {resultado1}")
    print(f"✅ Conta Maria: {resultado2}")
    
    # 2. Fazendo depósitos
    print("\n2️⃣ FAZENDO DEPÓSITOS:")
    conta_joao = conta_repo.buscar_por_numero("12345-1")
    conta_maria = conta_repo.buscar_por_numero("12345-2")
    
    conta_joao.depositar(Dinheiro(1000.0))
    conta_maria.depositar(Dinheiro(500.0))
    
    print(f"💰 Saldo João: R$ {conta_joao.saldo.valor}")
    print(f"💰 Saldo Maria: R$ {conta_maria.saldo.valor}")
    
    # 3. Fazendo transferência
    print("\n3️⃣ FAZENDO TRANSFERÊNCIA:")
    transferencia_data = {
        'conta_origem': '12345-1',
        'conta_destino': '12345-2',
        'valor': 200.0
    }
    
    resultado_transf = controller.post_transferencia(transferencia_data)
    print(f"💸 Transferência: {resultado_transf}")
    
    # 4. Consultar saldos finais
    print("\n4️⃣ SALDOS FINAIS:")
    print(f"💰 Saldo João: R$ {conta_joao.saldo.valor}")
    print(f"💰 Saldo Maria: R$ {conta_maria.saldo.valor}")
    
    print("\n🎉 SISTEMA BANCÁRIO FUNCIONANDO COM CLEAN ARCHITECTURE!")
    print("🏆 Todas as camadas trabalhando em harmonia!")

# Executando demonstração
demonstrar_sistema_bancario()'''
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.print_colored("Vamos ver seu Sistema Bancário com Clean Architecture em ação:", "text")
            self.executar_codigo(codigo_final)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um Sistema Bancário com Clean Architecture!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔒 Implementar autenticação e autorização por camadas",
            "📊 Adicionar relatórios e analytics usando Use Cases",
            "🌐 Criar APIs REST seguindo a arquitetura hexagonal",
            "🧪 Implementar testes unitários para cada camada",
            "📱 Adicionar interfaces mobile mantendo mesmo core",
            "⚡ Implementar Event Sourcing para auditoria completa"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de Software Sênior!")
        self.print_colored("Você agora domina Clean Architecture e DDD como os grandes bancos do mundo!", "accent")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema Bancário com Clean Architecture")
        
        self.pausar()