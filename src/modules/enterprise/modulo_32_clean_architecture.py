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
    """Módulo 32: Clean Architecture & Domain-Driven Design"""
    
    def __init__(self):
        super().__init__("modulo_32", "Clean Architecture & Domain-Driven Design")
        self.has_mini_project = True
        self.mini_project_points = 150
    
    def execute(self) -> None:
        """Executa o módulo sobre Clean Architecture"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            self.pausar()
            return
        
        try:
            self._clean_architecture_intro()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _clean_architecture_intro(self) -> None:
        """Conteúdo principal sobre Clean Architecture e DDD"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏛️ MÓDULO 32: CLEAN ARCHITECTURE & DOMAIN-DRIVEN DESIGN")
        else:
            print("\n" + "="*60)
            print("🏛️ MÓDULO 32: CLEAN ARCHITECTURE & DOMAIN-DRIVEN DESIGN")
            print("="*60)
        
        print("🚀 Aprenda arquitetura de software de classe mundial!")
        print("🎯 Clean Architecture e DDD são essenciais para:")
        print("• Sistemas de grande escala e complexidade")
        print("• Arquitetura independente de frameworks")
        print("• Testabilidade e manutenibilidade máximas")
        print("• Separação clara entre domínio e infraestrutura")
        print("• Modelagem precisa do domínio de negócio")
        print("• Evolução segura de sistemas legados")
        
        self.pausar()
        
        self._clean_architecture_principles()
        self._domain_driven_design()
        self._hexagonal_architecture()
        self._cqrs_pattern()
        self._mini_projeto_banking_system()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _clean_architecture_principles(self):
        """Princípios da Clean Architecture"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏛️ PRINCÍPIOS DA CLEAN ARCHITECTURE")
        
        print("📐 A Clean Architecture organiza código em camadas concêntricas:")
        print("• 🔵 Entities (Entidades) - Regras de negócio corporativas")
        print("• 🟡 Use Cases (Casos de Uso) - Regras de negócio da aplicação")
        print("• 🟠 Interface Adapters - Conversores de dados")
        print("• 🔴 Frameworks & Drivers - Detalhes externos")
        
        codigo = '''from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

# ========================================
# CAMADA 1: ENTITIES (ENTIDADES)
# ========================================
# Regras de negócio mais gerais e de alto nível
# Não dependem de nada externo

@dataclass
class Money:
    """Value Object para representar dinheiro"""
    amount: float
    currency: str = "BRL"
    
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Valor não pode ser negativo")
    
    def add(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Moedas diferentes")
        return Money(self.amount + other.amount, self.currency)
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

class AccountStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BLOCKED = "blocked"

class Account:
    """Entidade Account - Regras de negócio fundamentais"""
    def __init__(self, account_id: str, balance: Money):
        self.account_id = account_id
        self._balance = balance
        self.status = AccountStatus.ACTIVE
        self.created_at = datetime.now()
    
    def debit(self, amount: Money) -> None:
        """Regra de negócio: debitar conta"""
        if self.status != AccountStatus.ACTIVE:
            raise Exception("Conta não está ativa")
        
        if amount.amount > self._balance.amount:
            raise Exception("Saldo insuficiente")
        
        self._balance = Money(
            self._balance.amount - amount.amount,
            self._balance.currency
        )
    
    def credit(self, amount: Money) -> None:
        """Regra de negócio: creditar conta"""
        if self.status != AccountStatus.ACTIVE:
            raise Exception("Conta não está ativa")
        
        self._balance = self._balance.add(amount)
    
    @property
    def balance(self) -> Money:
        return self._balance

# Exemplo de uso das entidades
account = Account("123456", Money(1000.00))
print(f"Saldo inicial: {account.balance}")

# Creditar R$ 500
account.credit(Money(500.00))
print(f"Após crédito: {account.balance}")

# Debitar R$ 200
account.debit(Money(200.00))
print(f"Após débito: {account.balance}")
'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        self.pausar()
        
        # Use Cases Layer
        print("\n📌 CAMADA 2: USE CASES (CASOS DE USO)")
        print("Regras de negócio específicas da aplicação")
        
        codigo_usecase = '''# ========================================
# CAMADA 2: USE CASES (CASOS DE USO)
# ========================================
# Regras de negócio específicas da aplicação
# Orquestram entidades para realizar operações

# Ports (Interfaces)
class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account) -> None:
        pass
    
    @abstractmethod
    def find_by_id(self, account_id: str) -> Optional[Account]:
        pass

class TransactionLogger(ABC):
    @abstractmethod
    def log_transaction(self, from_account: str, to_account: str, amount: Money) -> None:
        pass

# Use Case
class TransferMoneyUseCase:
    """Caso de uso: Transferir dinheiro entre contas"""
    
    def __init__(self, account_repo: AccountRepository, logger: TransactionLogger):
        self.account_repo = account_repo
        self.logger = logger
    
    def execute(self, from_account_id: str, to_account_id: str, amount: Money) -> None:
        # 1. Buscar contas
        from_account = self.account_repo.find_by_id(from_account_id)
        to_account = self.account_repo.find_by_id(to_account_id)
        
        if not from_account or not to_account:
            raise Exception("Conta não encontrada")
        
        # 2. Executar transferência (regras de negócio)
        from_account.debit(amount)
        to_account.credit(amount)
        
        # 3. Persistir mudanças
        self.account_repo.save(from_account)
        self.account_repo.save(to_account)
        
        # 4. Log da transação
        self.logger.log_transaction(from_account_id, to_account_id, amount)
        
        print(f"✅ Transferência realizada: {amount} de {from_account_id} para {to_account_id}")

print("✅ Use Case definido - Separação clara de responsabilidades!")
'''
        
        self.exemplo(codigo_usecase)
        self.executar_codigo(codigo_usecase)
        self.pausar()
    
    def _domain_driven_design(self):
        """Conceitos de Domain-Driven Design"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ DOMAIN-DRIVEN DESIGN (DDD)")
        
        print("🎯 DDD foca na modelagem do domínio de negócio:")
        print("• Value Objects - Objetos sem identidade")
        print("• Entities - Objetos com identidade")
        print("• Aggregates - Grupos de entidades relacionadas")
        print("• Domain Services - Lógica que não pertence a uma entidade")
        print("• Domain Events - Eventos importantes do domínio")
        
        self.pausar()
        
        codigo_ddd = '''# ========================================
# DOMAIN-DRIVEN DESIGN PATTERNS
# ========================================

# Value Objects
@dataclass(frozen=True)
class Email:
    """Value Object - Sem identidade, apenas valor"""
    address: str
    
    def __post_init__(self):
        if "@" not in self.address:
            raise ValueError("Email inválido")

@dataclass(frozen=True)
class CPF:
    """Value Object para CPF"""
    number: str
    
    def __post_init__(self):
        if len(self.number) != 11:
            raise ValueError("CPF deve ter 11 dígitos")

# Entity
class Customer:
    """Entidade Customer - Tem identidade única"""
    def __init__(self, customer_id: str, name: str, email: Email, cpf: CPF):
        self.id = customer_id  # Identidade
        self.name = name
        self.email = email
        self.cpf = cpf
        self.accounts: List[Account] = []
    
    def add_account(self, account: Account):
        """Regra de domínio: cliente pode ter múltiplas contas"""
        self.accounts.append(account)
    
    def get_total_balance(self) -> Money:
        """Regra de domínio: saldo total do cliente"""
        total = 0.0
        for account in self.accounts:
            total += account.balance.amount
        return Money(total)

# Aggregate Root
class BankAggregate:
    """Aggregate Root - Gerencia consistência do domínio"""
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.accounts: Dict[str, Account] = {}
    
    def create_customer(self, name: str, email_addr: str, cpf_number: str) -> Customer:
        """Factory method para criar cliente"""
        customer_id = str(uuid.uuid4())
        email = Email(email_addr)
        cpf = CPF(cpf_number)
        
        customer = Customer(customer_id, name, email, cpf)
        self.customers[customer_id] = customer
        return customer
    
    def create_account_for_customer(self, customer_id: str, initial_balance: float) -> Account:
        """Cria conta para cliente existente"""
        if customer_id not in self.customers:
            raise Exception("Cliente não encontrado")
        
        account_id = str(uuid.uuid4())
        account = Account(account_id, Money(initial_balance))
        
        self.accounts[account_id] = account
        self.customers[customer_id].add_account(account)
        
        return account

# Domain Service
class FraudDetectionService:
    """Serviço de domínio - Lógica que não pertence a uma entidade específica"""
    
    def is_suspicious_transaction(self, amount: Money, account: Account) -> bool:
        """Regra de negócio: detectar transações suspeitas"""
        # Transação suspeita se > 80% do saldo
        threshold = account.balance.amount * 0.8
        return amount.amount > threshold

# Exemplo de uso
bank = BankAggregate()

# Criar cliente
customer = bank.create_customer(
    "João Silva", 
    "joao@email.com", 
    "12345678901"
)

# Criar conta
account = bank.create_account_for_customer(customer.id, 5000.00)

print(f"Cliente: {customer.name}")
print(f"Email: {customer.email.address}")
print(f"Saldo total: {customer.get_total_balance()}")

# Verificar fraude
fraud_service = FraudDetectionService()
is_suspicious = fraud_service.is_suspicious_transaction(Money(4500.00), account)
print(f"Transação suspeita: {is_suspicious}")
'''
        
        self.exemplo(codigo_ddd)
        self.executar_codigo(codigo_ddd)
        self.pausar()
    
    def _hexagonal_architecture(self):
        """Arquitetura Hexagonal (Ports & Adapters)"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔷 ARQUITETURA HEXAGONAL (PORTS & ADAPTERS)")
        
        print("🔌 Arquitetura Hexagonal isola o domínio dos detalhes externos:")
        print("• Ports - Interfaces que definem como o mundo exterior se conecta")
        print("• Adapters - Implementações concretas dos ports")
        print("• Core - Domínio puro, sem dependências externas")
        
        self.pausar()
        
        codigo_hex = '''# ========================================
# HEXAGONAL ARCHITECTURE
# ========================================

# Ports (Primary - Driving)
class BankingService(ABC):
    """Port primário - Define como aplicação é usada"""
    @abstractmethod
    def transfer_money(self, from_id: str, to_id: str, amount: float) -> bool:
        pass
    
    @abstractmethod
    def get_balance(self, account_id: str) -> float:
        pass

# Ports (Secondary - Driven)  
class AccountPersistence(ABC):
    """Port secundário - Define como aplicação persiste dados"""
    @abstractmethod
    def save_account(self, account: Account) -> None:
        pass
    
    @abstractmethod
    def load_account(self, account_id: str) -> Optional[Account]:
        pass

class NotificationService(ABC):
    """Port secundário - Define como aplicação notifica"""
    @abstractmethod
    def send_notification(self, message: str, recipient: str) -> None:
        pass

# Core Application (Hexagon Center)
class BankingApplication(BankingService):
    """Implementação do core da aplicação"""
    
    def __init__(self, persistence: AccountPersistence, notifications: NotificationService):
        self.persistence = persistence
        self.notifications = notifications
    
    def transfer_money(self, from_id: str, to_id: str, amount: float) -> bool:
        try:
            # Carregar contas
            from_account = self.persistence.load_account(from_id)
            to_account = self.persistence.load_account(to_id)
            
            if not from_account or not to_account:
                return False
            
            # Executar transferência
            money = Money(amount)
            from_account.debit(money)
            to_account.credit(money)
            
            # Persistir
            self.persistence.save_account(from_account)
            self.persistence.save_account(to_account)
            
            # Notificar
            self.notifications.send_notification(
                f"Transferência de {money} realizada",
                from_id
            )
            
            return True
        except Exception as e:
            print(f"Erro na transferência: {e}")
            return False
    
    def get_balance(self, account_id: str) -> float:
        account = self.persistence.load_account(account_id)
        return account.balance.amount if account else 0.0

# Adapters (Secondary - Implementações)
class InMemoryAccountPersistence(AccountPersistence):
    """Adapter para persistência em memória"""
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
    
    def save_account(self, account: Account) -> None:
        self.accounts[account.account_id] = account
    
    def load_account(self, account_id: str) -> Optional[Account]:
        return self.accounts.get(account_id)

class EmailNotificationService(NotificationService):
    """Adapter para notificações por email"""
    def send_notification(self, message: str, recipient: str) -> None:
        print(f"📧 Email para {recipient}: {message}")

class SMSNotificationService(NotificationService):
    """Adapter para notificações por SMS"""
    def send_notification(self, message: str, recipient: str) -> None:
        print(f"📱 SMS para {recipient}: {message}")

# Adapters (Primary - Controllers)
class WebBankingController:
    """Adapter primário - Interface web"""
    def __init__(self, banking_service: BankingService):
        self.banking_service = banking_service
    
    def handle_transfer_request(self, from_id: str, to_id: str, amount: float):
        print(f"🌐 Requisição web: Transferir {amount} de {from_id} para {to_id}")
        success = self.banking_service.transfer_money(from_id, to_id, amount)
        return {"success": success, "message": "Transferência processada"}

class MobileBankingController:
    """Adapter primário - Interface mobile"""
    def __init__(self, banking_service: BankingService):
        self.banking_service = banking_service
    
    def process_transfer(self, from_id: str, to_id: str, amount: float):
        print(f"📱 App mobile: Processar transferência")
        return self.banking_service.transfer_money(from_id, to_id, amount)

# Montagem da aplicação (Dependency Injection)
def create_banking_system():
    # Adapters secundários
    persistence = InMemoryAccountPersistence()
    notifications = EmailNotificationService()  # Pode trocar por SMS
    
    # Core da aplicação
    banking_app = BankingApplication(persistence, notifications)
    
    # Criar algumas contas para teste
    acc1 = Account("001", Money(1000.00))
    acc2 = Account("002", Money(500.00))
    persistence.save_account(acc1)
    persistence.save_account(acc2)
    
    # Adapters primários
    web_controller = WebBankingController(banking_app)
    mobile_controller = MobileBankingController(banking_app)
    
    return web_controller, mobile_controller, banking_app

# Demonstração
web, mobile, core = create_banking_system()

print("=== HEXAGONAL ARCHITECTURE EM AÇÃO ===")
print(f"Saldo conta 001: R$ {core.get_balance('001'):.2f}")
print(f"Saldo conta 002: R$ {core.get_balance('002'):.2f}")

# Via web
web.handle_transfer_request("001", "002", 300.00)

print(f"\\nApós transferência:")
print(f"Saldo conta 001: R$ {core.get_balance('001'):.2f}")
print(f"Saldo conta 002: R$ {core.get_balance('002'):.2f}")

# Via mobile
mobile.process_transfer("002", "001", 100.00)

print(f"\\nApós transferência mobile:")
print(f"Saldo conta 001: R$ {core.get_balance('001'):.2f}")
print(f"Saldo conta 002: R$ {core.get_balance('002'):.2f}")
'''
        
        self.exemplo(codigo_hex)
        self.executar_codigo(codigo_hex)
        self.pausar()
    
    def _cqrs_pattern(self):
        """Command Query Responsibility Segregation"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ CQRS - COMMAND QUERY RESPONSIBILITY SEGREGATION")
        
        print("🔄 CQRS separa operações de leitura e escrita:")
        print("• Commands - Modificam estado (Write Model)")
        print("• Queries - Leem dados (Read Model)")
        print("• Event Store - Armazena eventos que aconteceram")
        print("• Projeções - Views otimizadas para consulta")
        
        self.pausar()
        
        codigo_cqrs = '''# ========================================
# CQRS + EVENT SOURCING
# ========================================

from typing import List
from dataclasses import dataclass
from datetime import datetime
import json

# Domain Events
@dataclass
class DomainEvent:
    event_id: str
    aggregate_id: str
    event_type: str
    event_data: Dict[str, Any]
    occurred_at: datetime
    version: int

class AccountCreated(DomainEvent):
    pass

class MoneyDeposited(DomainEvent):
    pass

class MoneyWithdrawn(DomainEvent):
    pass

# Event Store
class EventStore:
    """Armazena todos os eventos que aconteceram"""
    def __init__(self):
        self.events: List[DomainEvent] = []
    
    def save_events(self, aggregate_id: str, events: List[DomainEvent], expected_version: int):
        for event in events:
            event.version = expected_version + 1
            expected_version += 1
            self.events.append(event)
    
    def get_events(self, aggregate_id: str) -> List[DomainEvent]:
        return [e for e in self.events if e.aggregate_id == aggregate_id]

# Write Model (Commands)
class CreateAccountCommand:
    def __init__(self, account_id: str, initial_balance: float):
        self.account_id = account_id
        self.initial_balance = initial_balance

class DepositMoneyCommand:
    def __init__(self, account_id: str, amount: float):
        self.account_id = account_id
        self.amount = amount

class WithdrawMoneyCommand:
    def __init__(self, account_id: str, amount: float):
        self.account_id = account_id
        self.amount = amount

# Aggregate (Write Model)
class AccountAggregate:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0.0
        self.version = 0
        self.uncommitted_events: List[DomainEvent] = []
    
    def create_account(self, initial_balance: float):
        event = DomainEvent(
            event_id=str(uuid.uuid4()),
            aggregate_id=self.account_id,
            event_type="AccountCreated",
            event_data={"initial_balance": initial_balance},
            occurred_at=datetime.now(),
            version=0
        )
        self.apply_event(event)
        self.uncommitted_events.append(event)
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Valor deve ser positivo")
        
        event = DomainEvent(
            event_id=str(uuid.uuid4()),
            aggregate_id=self.account_id,
            event_type="MoneyDeposited",
            event_data={"amount": amount},
            occurred_at=datetime.now(),
            version=self.version
        )
        self.apply_event(event)
        self.uncommitted_events.append(event)
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Valor deve ser positivo")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        
        event = DomainEvent(
            event_id=str(uuid.uuid4()),
            aggregate_id=self.account_id,
            event_type="MoneyWithdrawn",
            event_data={"amount": amount},
            occurred_at=datetime.now(),
            version=self.version
        )
        self.apply_event(event)
        self.uncommitted_events.append(event)
    
    def apply_event(self, event: DomainEvent):
        """Aplica evento ao estado atual"""
        if event.event_type == "AccountCreated":
            self.balance = event.event_data["initial_balance"]
        elif event.event_type == "MoneyDeposited":
            self.balance += event.event_data["amount"]
        elif event.event_type == "MoneyWithdrawn":
            self.balance -= event.event_data["amount"]
        
        self.version = event.version
    
    def get_uncommitted_events(self) -> List[DomainEvent]:
        return self.uncommitted_events.copy()
    
    def mark_events_as_committed(self):
        self.uncommitted_events.clear()
    
    @staticmethod
    def from_history(account_id: str, events: List[DomainEvent]) -> 'AccountAggregate':
        """Reconstrói aggregate a partir do histórico de eventos"""
        aggregate = AccountAggregate(account_id)
        for event in events:
            aggregate.apply_event(event)
        return aggregate

# Command Handlers
class AccountCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
    
    def handle_create_account(self, command: CreateAccountCommand):
        aggregate = AccountAggregate(command.account_id)
        aggregate.create_account(command.initial_balance)
        
        events = aggregate.get_uncommitted_events()
        self.event_store.save_events(command.account_id, events, aggregate.version - 1)
        aggregate.mark_events_as_committed()
    
    def handle_deposit(self, command: DepositMoneyCommand):
        events = self.event_store.get_events(command.account_id)
        aggregate = AccountAggregate.from_history(command.account_id, events)
        
        aggregate.deposit(command.amount)
        
        new_events = aggregate.get_uncommitted_events()
        self.event_store.save_events(command.account_id, new_events, aggregate.version - 1)
        aggregate.mark_events_as_committed()
    
    def handle_withdraw(self, command: WithdrawMoneyCommand):
        events = self.event_store.get_events(command.account_id)
        aggregate = AccountAggregate.from_history(command.account_id, events)
        
        aggregate.withdraw(command.amount)
        
        new_events = aggregate.get_uncommitted_events()
        self.event_store.save_events(command.account_id, new_events, aggregate.version - 1)
        aggregate.mark_events_as_committed()

# Read Model (Queries)
@dataclass
class AccountSummary:
    account_id: str
    current_balance: float
    total_deposits: float
    total_withdrawals: float
    transaction_count: int
    created_at: datetime
    last_transaction: Optional[datetime]

class AccountProjection:
    """Projeção otimizada para consultas"""
    def __init__(self):
        self.accounts: Dict[str, AccountSummary] = {}
    
    def handle_event(self, event: DomainEvent):
        """Atualiza projeção baseada em eventos"""
        account_id = event.aggregate_id
        
        if event.event_type == "AccountCreated":
            self.accounts[account_id] = AccountSummary(
                account_id=account_id,
                current_balance=event.event_data["initial_balance"],
                total_deposits=event.event_data["initial_balance"],
                total_withdrawals=0.0,
                transaction_count=1,
                created_at=event.occurred_at,
                last_transaction=event.occurred_at
            )
        
        elif event.event_type == "MoneyDeposited":
            summary = self.accounts[account_id]
            summary.current_balance += event.event_data["amount"]
            summary.total_deposits += event.event_data["amount"]
            summary.transaction_count += 1
            summary.last_transaction = event.occurred_at
        
        elif event.event_type == "MoneyWithdrawn":
            summary = self.accounts[account_id]
            summary.current_balance -= event.event_data["amount"]
            summary.total_withdrawals += event.event_data["amount"]
            summary.transaction_count += 1
            summary.last_transaction = event.occurred_at
    
    def get_account_summary(self, account_id: str) -> Optional[AccountSummary]:
        return self.accounts.get(account_id)
    
    def get_all_accounts(self) -> List[AccountSummary]:
        return list(self.accounts.values())

# Query Handlers
class AccountQueryHandler:
    def __init__(self, projection: AccountProjection):
        self.projection = projection
    
    def get_account_balance(self, account_id: str) -> Optional[float]:
        summary = self.projection.get_account_summary(account_id)
        return summary.current_balance if summary else None
    
    def get_account_history(self, account_id: str) -> Optional[AccountSummary]:
        return self.projection.get_account_summary(account_id)

# Demonstração do CQRS
print("=== CQRS + EVENT SOURCING EM AÇÃO ===")

# Setup
event_store = EventStore()
projection = AccountProjection()
command_handler = AccountCommandHandler(event_store)
query_handler = AccountQueryHandler(projection)

# Comandos (Write)
print("\\n📝 EXECUTANDO COMANDOS:")
command_handler.handle_create_account(CreateAccountCommand("ACC-001", 1000.0))
command_handler.handle_deposit(DepositMoneyCommand("ACC-001", 500.0))
command_handler.handle_withdraw(WithdrawMoneyCommand("ACC-001", 200.0))

# Atualizar projeções
print("\\n🔄 ATUALIZANDO PROJEÇÕES:")
for event in event_store.events:
    projection.handle_event(event)
    print(f"  • {event.event_type}: {event.event_data}")

# Consultas (Read)
print("\\n📊 EXECUTANDO CONSULTAS:")
balance = query_handler.get_account_balance("ACC-001")
print(f"Saldo atual: R$ {balance:.2f}")

summary = query_handler.get_account_history("ACC-001")
if summary:
    print(f"Total de depósitos: R$ {summary.total_deposits:.2f}")
    print(f"Total de saques: R$ {summary.total_withdrawals:.2f}")
    print(f"Número de transações: {summary.transaction_count}")
    print(f"Última transação: {summary.last_transaction}")

print("\\n✅ CQRS permite escalar leitura e escrita independentemente!")
'''
        
        self.exemplo(codigo_cqrs)
        self.executar_codigo(codigo_cqrs)
        self.pausar()
    
    def _mini_projeto_banking_system(self):
        """Mini-projeto: Sistema bancário completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI-PROJETO: SISTEMA BANCÁRIO ENTERPRISE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI-PROJETO: SISTEMA BANCÁRIO ENTERPRISE")
            print("="*50)
        
        print("🏦 Sistema completo integrando todas as arquiteturas!")
        print("📋 Funcionalidades:")
        print("• Clean Architecture com 4 camadas")
        print("• Domain-Driven Design com agregados")
        print("• Hexagonal Architecture com ports/adapters")
        print("• CQRS para separar leitura/escrita")
        print("• Event Sourcing para auditoria completa")
        
        self.pausar()
        
        codigo_projeto = '''# ========================================
# SISTEMA BANCÁRIO ENTERPRISE COMPLETO
# ========================================
# Integrando: Clean Architecture + DDD + Hexagonal + CQRS

print("🏦 SISTEMA BANCÁRIO ENTERPRISE")
print("=" * 50)

# Simulação de sistema completo funcionando
class EnterpriseBankingSystem:
    """Sistema bancário enterprise completo"""
    
    def __init__(self):
        self.event_store = EventStore()
        self.projection = AccountProjection()
        self.command_handler = AccountCommandHandler(self.event_store)
        self.query_handler = AccountQueryHandler(self.projection)
        
        # Setup de adaptadores
        self.persistence = InMemoryAccountPersistence()
        self.notifications = EmailNotificationService()
        self.banking_app = BankingApplication(self.persistence, self.notifications)
        
        print("✅ Sistema inicializado com todas as arquiteturas!")
    
    def create_customer_account(self, customer_name: str, email: str, initial_deposit: float):
        """Fluxo completo: criar cliente e conta"""
        print(f"\\n👤 Criando conta para {customer_name}")
        
        # 1. Domain (DDD)
        bank_aggregate = BankAggregate()
        customer = bank_aggregate.create_customer(customer_name, email, "12345678901")
        account = bank_aggregate.create_account_for_customer(customer.id, initial_deposit)
        
        # 2. Event Sourcing (CQRS)
        self.command_handler.handle_create_account(
            CreateAccountCommand(account.account_id, initial_deposit)
        )
        
        # 3. Update projections
        for event in self.event_store.get_events(account.account_id):
            self.projection.handle_event(event)
        
        print(f"   ✅ Cliente: {customer_name}")
        print(f"   ✅ Conta: {account.account_id}")
        print(f"   ✅ Saldo inicial: R$ {initial_deposit:.2f}")
        
        return customer, account
    
    def process_transfer(self, from_account_id: str, to_account_id: str, amount: float):
        """Transferência usando todas as camadas arquiteturais"""
        print(f"\\n💸 Processando transferência de R$ {amount:.2f}")
        
        # 1. Use Case (Clean Architecture)
        success = self.banking_app.transfer_money(from_account_id, to_account_id, amount)
        
        # 2. Event Sourcing para auditoria
        if success:
            self.command_handler.handle_withdraw(WithdrawMoneyCommand(from_account_id, amount))
            self.command_handler.handle_deposit(DepositMoneyCommand(to_account_id, amount))
            
            # Update projections
            for event in self.event_store.events[-2:]:  # Últimos 2 eventos
                self.projection.handle_event(event)
        
        return success
    
    def get_account_dashboard(self, account_id: str):
        """Dashboard completo da conta"""
        print(f"\\n📊 Dashboard da conta {account_id}")
        
        # Query otimizada (CQRS Read Model)
        summary = self.query_handler.get_account_history(account_id)
        
        if summary:
            print(f"   💰 Saldo atual: R$ {summary.current_balance:.2f}")
            print(f"   📈 Total depositado: R$ {summary.total_deposits:.2f}")
            print(f"   📉 Total sacado: R$ {summary.total_withdrawals:.2f}")
            print(f"   🔢 Transações: {summary.transaction_count}")
            print(f"   📅 Última transação: {summary.last_transaction}")
        else:
            print("   ❌ Conta não encontrada")
    
    def get_system_audit(self):
        """Auditoria completa do sistema"""
        print(f"\\n🔍 AUDITORIA DO SISTEMA")
        print(f"   📝 Total de eventos: {len(self.event_store.events)}")
        
        for i, event in enumerate(self.event_store.events, 1):
            print(f"   {i}. {event.event_type} - {event.aggregate_id} - {event.occurred_at.strftime('%H:%M:%S')}")

# Demonstração completa
system = EnterpriseBankingSystem()

# Criar contas
customer1, account1 = system.create_customer_account("João Silva", "joao@bank.com", 5000.0)
customer2, account2 = system.create_customer_account("Maria Santos", "maria@bank.com", 2000.0)

# Dashboards iniciais
system.get_account_dashboard(account1.account_id)
system.get_account_dashboard(account2.account_id)

# Transferência
success = system.process_transfer(account1.account_id, account2.account_id, 1000.0)
print(f"Transferência {'realizada' if success else 'falhou'}!")

# Dashboards após transferência
system.get_account_dashboard(account1.account_id)
system.get_account_dashboard(account2.account_id)

# Auditoria completa
system.get_system_audit()

print("\\n🏆 SISTEMA ENTERPRISE FUNCIONANDO!")
print("✅ Clean Architecture: Camadas bem definidas")
print("✅ DDD: Modelagem rica do domínio")
print("✅ Hexagonal: Isolamento de dependências externas") 
print("✅ CQRS: Separação otimizada de leitura/escrita")
print("✅ Event Sourcing: Auditoria completa e replay")
'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        # Registra conclusão do mini-projeto
        self.complete_mini_project("Sistema Bancário Enterprise com Clean Architecture")
        
        print("\n🏆 PARABÉNS! Você dominou arquiteturas enterprise!")
        print("🎯 Agora você pode:")
        print("• Projetar sistemas de grande escala")
        print("• Implementar Clean Architecture")
        print("• Aplicar Domain-Driven Design")
        print("• Criar arquiteturas hexagonais")
        print("• Usar CQRS e Event Sourcing")
        print("• Construir sistemas testáveis e manuteníveis")
        
        self.pausar()