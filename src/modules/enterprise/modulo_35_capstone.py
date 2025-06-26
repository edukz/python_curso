#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 35: Capstone Project - Projeto Final Integrado
O projeto definitivo que integra todos os conceitos do curso em uma aplicação enterprise completa
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Protocol, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid
from ..shared.base_module import BaseModule


class Modulo35Capstone(BaseModule):
    """Módulo 35: Capstone Project - Projeto Final Integrado"""
    
    def __init__(self):
        super().__init__("modulo_35", "Capstone Project - Projeto Final")
        self.has_mini_project = True
        self.mini_project_points = 200  # Pontuação máxima!
    
    def execute(self) -> None:
        """Executa o módulo Capstone Project"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            self.pausar()
            return
        
        try:
            self._capstone_intro()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _capstone_intro(self) -> None:
        """Introdução ao Capstone Project"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 MÓDULO 35: CAPSTONE PROJECT - PROJETO FINAL")
        else:
            print("\n" + "="*60)
            print("🎓 MÓDULO 35: CAPSTONE PROJECT - PROJETO FINAL")
            print("="*60)
        
        print("🏆 PARABÉNS! Chegou ao projeto FINAL do curso!")
        print("🚀 Este é o momento de demonstrar TUDO que aprendeu!")
        print("💼 Vamos criar uma aplicação ENTERPRISE COMPLETA!")
        
        print("\n🎯 O CAPSTONE PROJECT INTEGRA:")
        print("✅ Todos os 34 módulos anteriores")
        print("✅ Padrões de design profissionais")
        print("✅ Arquitetura limpa e escalável")
        print("✅ DevOps e deploy automático")
        print("✅ Database design otimizado")
        print("✅ Monitoramento e observabilidade")
        print("✅ Segurança enterprise")
        print("✅ Performance de classe mundial")
        
        self.pausar()
        
        self._project_overview()
        self._architecture_design()
        self._implementation_roadmap()
        self._capstone_project_complete()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _project_overview(self):
        """Visão Geral do Projeto - Parte 1"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏢 VISÃO GERAL: PLATAFORMA ENTERPRISE")
        
        print("🎯 PROJETO: CloudCorp Enterprise Platform")
        print("💼 Uma plataforma SaaS completa para gestão empresarial")
        
        print("\n📋 FUNCIONALIDADES PRINCIPAIS:")
        print("• 👥 Gestão de usuários e permissões")
        print("• 🏢 Multi-tenancy para empresas")
        print("• 📊 Dashboard analytics em tempo real")
        print("• 💰 Sistema financeiro completo")
        print("• 📈 CRM e gestão de clientes")
        print("• 📋 Gestão de projetos e tarefas")
        print("• 📄 Sistema de documentos")
        print("• 🔔 Notificações em tempo real")
        print("• 📱 API REST completa")
        print("• 🌐 Interface web responsiva")
        
        codigo = '''# ========================================
# CLOUDCORP ENTERPRISE PLATFORM
# ARQUITETURA DE APLICAÇÃO ENTERPRISE COMPLETA
# ========================================

"""
ESTRUTURA DO PROJETO CAPSTONE:

cloudcorp-platform/
├── backend/
│   ├── apps/
│   │   ├── authentication/      # Sistema de autenticação
│   │   ├── users/              # Gestão de usuários
│   │   ├── tenants/            # Multi-tenancy
│   │   ├── projects/           # Gestão de projetos
│   │   ├── crm/                # CRM e clientes
│   │   ├── finance/            # Sistema financeiro
│   │   ├── analytics/          # Analytics e relatórios
│   │   ├── notifications/      # Sistema de notificações
│   │   └── documents/          # Gestão de documentos
│   ├── core/
│   │   ├── database/           # Database design
│   │   ├── cache/              # Sistema de cache
│   │   ├── permissions/        # Sistema de permissões
│   │   ├── audit/              # Auditoria e logs
│   │   └── monitoring/         # Monitoramento
│   ├── api/
│   │   ├── v1/                 # API REST v1
│   │   ├── graphql/            # GraphQL API
│   │   └── webhooks/           # Webhooks
│   └── config/
│       ├── settings/           # Configurações
│       ├── middleware/         # Middlewares
│       └── security/           # Segurança
├── frontend/
│   ├── web/                    # React/TypeScript
│   ├── mobile/                 # React Native
│   └── admin/                  # Admin dashboard
├── infrastructure/
│   ├── docker/                 # Containerização
│   ├── kubernetes/             # Orquestração
│   ├── terraform/              # Infraestrutura
│   ├── monitoring/             # Prometheus/Grafana
│   └── ci-cd/                  # Pipelines
├── tests/
│   ├── unit/                   # Testes unitários
│   ├── integration/            # Testes de integração
│   ├── e2e/                    # Testes end-to-end
│   └── performance/            # Testes de performance
└── docs/
    ├── api/                    # Documentação da API
    ├── architecture/           # Documentação técnica
    └── user/                   # Manual do usuário
"""

# ========================================
# 1. ARQUITETURA DE ALTO NÍVEL
# ========================================

# Padrão Hexagonal (Ports & Adapters) + Clean Architecture
"""
┌─────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                     │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │ REST API    │ │ GraphQL API │ │ Admin Dashboard     │  │
│  │ (FastAPI)   │ │ (Strawberry)│ │ (React)             │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Use Cases / Services                   │   │
│  │  • UserService  • ProjectService  • FinanceService │   │
│  │  • AuthService  • CRMService      • AnalyticsService│   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               Domain Entities                       │   │
│  │  • User  • Tenant  • Project  • Customer  • Invoice│   │
│  │  • Task  • Document • Notification • Permission    │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   INFRASTRUCTURE LAYER                     │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐  │
│  │ PostgreSQL  │ │ Redis Cache │ │ External APIs       │  │
│  │ Database    │ │ Session     │ │ (Payment, Email)    │  │
│  └─────────────┘ └─────────────┘ └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
"""

# ========================================
# 2. TECNOLOGIAS ESCOLHIDAS
# ========================================

"""
BACKEND:
• Python 3.11+ com FastAPI
• SQLAlchemy 2.0 + Alembic
• PostgreSQL 15 + Redis 7
• Pydantic v2 para validação
• Celery para tarefas assíncronas
• Pytest para testes

FRONTEND:
• React 18 + TypeScript
• Next.js 14 para SSR
• Tailwind CSS + Shadcn/ui
• TanStack Query para state
• Socket.io para real-time

DEVOPS:
• Docker + Docker Compose
• Kubernetes + Helm
• GitHub Actions CI/CD
• Prometheus + Grafana
• ELK Stack para logs

CLOUD:
• AWS / Azure / GCP
• Terraform para IaC
• CloudFormation / ARM
• CDN para assets
• S3 para arquivos
"""

# ========================================
# 3. ESPECIFICAÇÕES TÉCNICAS
# ========================================

# Requisitos não-funcionais
PERFORMANCE_REQUIREMENTS = {
    "response_time": "< 200ms (95th percentile)",
    "throughput": "10,000 requests/second",
    "uptime": "99.9% SLA",
    "concurrent_users": "100,000+",
    "data_volume": "10TB+ database",
    "global_latency": "< 100ms worldwide"
}

SECURITY_REQUIREMENTS = {
    "authentication": "OAuth 2.0 + OIDC",
    "authorization": "RBAC + ABAC",
    "encryption": "AES-256 at rest, TLS 1.3 in transit",
    "compliance": "SOC2, GDPR, HIPAA ready",
    "audit": "Complete audit trail",
    "penetration_testing": "Quarterly security tests"
}

SCALABILITY_REQUIREMENTS = {
    "horizontal_scaling": "Auto-scaling pods",
    "database_sharding": "Tenant-based sharding",
    "caching_strategy": "Multi-level caching",
    "cdn_distribution": "Global CDN",
    "microservices": "Domain-driven microservices",
    "event_driven": "Event sourcing + CQRS"
}

# ========================================
# 4. DOMÍNIOS DE NEGÓCIO
# ========================================

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import uuid

# Domain: Authentication & Authorization
class UserRole(Enum):
    SUPER_ADMIN = "super_admin"
    TENANT_ADMIN = "tenant_admin"
    MANAGER = "manager"
    USER = "user"
    VIEWER = "viewer"

class Permission(Enum):
    # User management
    CREATE_USER = "create_user"
    UPDATE_USER = "update_user"
    DELETE_USER = "delete_user"
    VIEW_USER = "view_user"
    
    # Project management
    CREATE_PROJECT = "create_project"
    UPDATE_PROJECT = "update_project"
    DELETE_PROJECT = "delete_project"
    VIEW_PROJECT = "view_project"
    
    # Financial
    CREATE_INVOICE = "create_invoice"
    APPROVE_PAYMENT = "approve_payment"
    VIEW_FINANCIAL_REPORTS = "view_financial_reports"

@dataclass
class User:
    """Entidade de domínio: Usuário"""
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    role: UserRole
    tenant_id: uuid.UUID
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime] = None
    permissions: List[Permission] = None
    
    def __post_init__(self):
        if self.permissions is None:
            self.permissions = self._get_role_permissions()
    
    def _get_role_permissions(self) -> List[Permission]:
        """Retorna permissões baseadas no role"""
        role_permissions = {
            UserRole.SUPER_ADMIN: list(Permission),
            UserRole.TENANT_ADMIN: [
                Permission.CREATE_USER, Permission.UPDATE_USER, 
                Permission.VIEW_USER, Permission.CREATE_PROJECT,
                Permission.UPDATE_PROJECT, Permission.VIEW_PROJECT
            ],
            UserRole.MANAGER: [
                Permission.VIEW_USER, Permission.CREATE_PROJECT,
                Permission.UPDATE_PROJECT, Permission.VIEW_PROJECT
            ],
            UserRole.USER: [
                Permission.VIEW_USER, Permission.VIEW_PROJECT
            ],
            UserRole.VIEWER: [
                Permission.VIEW_USER, Permission.VIEW_PROJECT
            ]
        }
        return role_permissions.get(self.role, [])
    
    def has_permission(self, permission: Permission) -> bool:
        """Verifica se usuário tem permissão"""
        return permission in self.permissions
    
    def can_access_tenant(self, tenant_id: uuid.UUID) -> bool:
        """Verifica acesso ao tenant"""
        if self.role == UserRole.SUPER_ADMIN:
            return True
        return self.tenant_id == tenant_id

# Domain: Multi-tenancy
@dataclass
class Tenant:
    """Entidade de domínio: Tenant/Empresa"""
    id: uuid.UUID
    slug: str
    name: str
    plan: str  # basic, pro, enterprise
    max_users: int
    features: List[str]
    database_schema: str
    is_active: bool
    created_at: datetime
    subscription_expires_at: Optional[datetime] = None
    
    def can_add_user(self, current_users_count: int) -> bool:
        """Verifica se pode adicionar mais usuários"""
        return current_users_count < self.max_users
    
    def has_feature(self, feature: str) -> bool:
        """Verifica se tenant tem uma feature"""
        return feature in self.features

# Domain: Project Management
class ProjectStatus(Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

@dataclass
class Project:
    """Entidade de domínio: Projeto"""
    id: uuid.UUID
    tenant_id: uuid.UUID
    name: str
    description: str
    owner_id: uuid.UUID
    status: ProjectStatus
    start_date: datetime
    due_date: Optional[datetime]
    budget: Optional[float]
    created_at: datetime
    
    def is_overdue(self) -> bool:
        """Verifica se projeto está atrasado"""
        if not self.due_date:
            return False
        return datetime.now() > self.due_date and self.status != ProjectStatus.COMPLETED

@dataclass
class Task:
    """Entidade de domínio: Tarefa"""
    id: uuid.UUID
    project_id: uuid.UUID
    title: str
    description: str
    assignee_id: Optional[uuid.UUID]
    priority: TaskPriority
    status: str
    estimated_hours: Optional[float]
    actual_hours: Optional[float]
    due_date: Optional[datetime]
    created_at: datetime
    
    def is_overdue(self) -> bool:
        """Verifica se tarefa está atrasada"""
        if not self.due_date or self.status == "completed":
            return False
        return datetime.now() > self.due_date

print("🏢 CLOUDCORP ENTERPRISE PLATFORM:")
print("🎯 1. Plataforma SaaS multi-tenant completa")
print("👥 2. Sistema de usuários e permissões")
print("📊 3. Dashboard analytics em tempo real")
print("💰 4. Sistema financeiro integrado")
print("📈 5. CRM completo para gestão de clientes")
print("📋 6. Gestão de projetos e tarefas")
print("🔔 7. Notificações em tempo real")
print("📱 8. API REST + GraphQL")
print("🌐 9. Interface web responsiva")
print("🚀 10. DevOps e deploy automático")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _architecture_design(self):
        """Design da Arquitetura - Parte 2"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ ARQUITETURA E DESIGN PATTERNS")
        
        print("🎯 Aplicando TODOS os padrões aprendidos no curso!")
        print("🏗️ Arquitetura que escala para milhões de usuários!")
        
        codigo = '''# ========================================
# ARQUITETURA DETALHADA - BACKEND
# ========================================

# 1. ESTRUTURA DE PASTAS ENTERPRISE
"""
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py         # Configurações
│   │   ├── database.py         # Database config
│   │   └── security.py         # Security config
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py       # Exceções customizadas
│   │   ├── middleware.py       # Middlewares
│   │   ├── dependencies.py     # Dependências
│   │   ├── security.py         # Autenticação/Autorização
│   │   └── events.py           # Event handlers
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/           # Entidades de domínio
│   │   ├── value_objects/      # Value Objects
│   │   ├── repositories/       # Interfaces de repositório
│   │   └── services/           # Serviços de domínio
│   ├── application/
│   │   ├── __init__.py
│   │   ├── use_cases/          # Casos de uso
│   │   ├── dto/                # DTOs
│   │   └── services/           # Serviços de aplicação
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── database/           # SQLAlchemy models
│   │   ├── repositories/       # Implementações de repositório
│   │   ├── external/           # APIs externas
│   │   └── cache/              # Cache implementations
│   ├── presentation/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── v1/             # API v1
│   │   │   └── graphql/        # GraphQL
│   │   └── web/                # Web interface
│   └── tests/
       ├── unit/
       ├── integration/
       └── e2e/
"""

# ========================================
# 2. CONFIGURAÇÃO BASE (config/settings.py)
# ========================================

from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, computed_field
from typing import Any, Dict, Optional
import secrets

class Settings(BaseSettings):
    """Configurações da aplicação usando Pydantic Settings"""
    
    # Básico
    PROJECT_NAME: str = "CloudCorp Enterprise Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "cloudcorp"
    POSTGRES_PORT: int = 5432
    
    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_TTL: int = 300  # 5 minutos
    
    # Authentication
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"
    
    # Email
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    
    # External APIs
    STRIPE_SECRET_KEY: Optional[str] = None
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_S3_BUCKET: Optional[str] = None
    
    # Performance
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30
    
    # Security
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Monitoring
    SENTRY_DSN: Optional[str] = None
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# ========================================
# 3. DATABASE MODELS (infrastructure/database/models.py)
# ========================================

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, DateTime, Integer, Text, ForeignKey, Numeric, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class TimestampMixin:
    """Mixin para timestamps automáticos"""
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class TenantModel(Base, TimestampMixin):
    """Modelo de Tenant"""
    __tablename__ = "tenants"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    plan = Column(String(20), default="basic")
    max_users = Column(Integer, default=10)
    features = Column(JSON, default=list)
    database_schema = Column(String(50), unique=True)
    is_active = Column(Boolean, default=True)
    subscription_expires_at = Column(DateTime(timezone=True))
    
    # Relacionamentos
    users = relationship("UserModel", back_populates="tenant")
    projects = relationship("ProjectModel", back_populates="tenant")

class UserModel(Base, TimestampMixin):
    """Modelo de Usuário"""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    role = Column(String(20), default="user")
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    last_login = Column(DateTime(timezone=True))
    
    # Relacionamentos
    tenant = relationship("TenantModel", back_populates="users")
    owned_projects = relationship("ProjectModel", back_populates="owner")
    tasks = relationship("TaskModel", back_populates="assignee")

class ProjectModel(Base, TimestampMixin):
    """Modelo de Projeto"""
    __tablename__ = "projects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(String(20), default="planning")
    start_date = Column(DateTime(timezone=True))
    due_date = Column(DateTime(timezone=True))
    budget = Column(Numeric(12, 2))
    
    # Relacionamentos
    tenant = relationship("TenantModel", back_populates="projects")
    owner = relationship("UserModel", back_populates="owned_projects")
    tasks = relationship("TaskModel", back_populates="project")

class TaskModel(Base, TimestampMixin):
    """Modelo de Tarefa"""
    __tablename__ = "tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String(500), nullable=False)
    description = Column(Text)
    priority = Column(String(10), default="medium")
    status = Column(String(20), default="todo")
    estimated_hours = Column(Numeric(8, 2))
    actual_hours = Column(Numeric(8, 2))
    due_date = Column(DateTime(timezone=True))
    
    # Relacionamentos
    project = relationship("ProjectModel", back_populates="tasks")
    assignee = relationship("UserModel", back_populates="tasks")

# ========================================
# 4. REPOSITORY PATTERN (domain/repositories/)
# ========================================

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from uuid import UUID

class IUserRepository(ABC):
    """Interface do repositório de usuários"""
    
    @abstractmethod
    async def create(self, user_data: Dict[str, Any]) -> UserModel:
        pass
    
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> Optional[UserModel]:
        pass
    
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserModel]:
        pass
    
    @abstractmethod
    async def get_by_tenant(self, tenant_id: UUID, skip: int = 0, limit: int = 100) -> List[UserModel]:
        pass
    
    @abstractmethod
    async def update(self, user_id: UUID, user_data: Dict[str, Any]) -> Optional[UserModel]:
        pass
    
    @abstractmethod
    async def delete(self, user_id: UUID) -> bool:
        pass

# Implementação com SQLAlchemy
class SQLAlchemyUserRepository(IUserRepository):
    """Implementação do repositório de usuários com SQLAlchemy"""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, user_data: Dict[str, Any]) -> UserModel:
        user = UserModel(**user_data)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_by_id(self, user_id: UUID) -> Optional[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_by_tenant(self, tenant_id: UUID, skip: int = 0, limit: int = 100) -> List[UserModel]:
        result = await self.session.execute(
            select(UserModel)
            .where(UserModel.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

# ========================================
# 5. USE CASES (application/use_cases/)
# ========================================

from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateUserRequest:
    tenant_id: UUID
    email: str
    password: str
    first_name: str
    last_name: str
    role: str = "user"

@dataclass
class CreateUserResponse:
    user_id: UUID
    email: str
    first_name: str
    last_name: str
    role: str
    created_at: datetime

class CreateUserUseCase:
    """Caso de uso: Criar usuário"""
    
    def __init__(
        self,
        user_repository: IUserRepository,
        tenant_repository: ITenantRepository,
        password_service: IPasswordService,
        email_service: IEmailService
    ):
        self.user_repository = user_repository
        self.tenant_repository = tenant_repository
        self.password_service = password_service
        self.email_service = email_service
    
    async def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        """Executar caso de uso"""
        
        # 1. Validar tenant
        tenant = await self.tenant_repository.get_by_id(request.tenant_id)
        if not tenant or not tenant.is_active:
            raise TenantNotFoundError("Tenant não encontrado ou inativo")
        
        # 2. Verificar limite de usuários
        current_users_count = await self.user_repository.count_by_tenant(request.tenant_id)
        if current_users_count >= tenant.max_users:
            raise UserLimitExceededError("Limite de usuários atingido")
        
        # 3. Verificar se email já existe
        existing_user = await self.user_repository.get_by_email(request.email)
        if existing_user:
            raise EmailAlreadyExistsError("Email já cadastrado")
        
        # 4. Hash da senha
        hashed_password = self.password_service.hash_password(request.password)
        
        # 5. Criar usuário
        user_data = {
            "tenant_id": request.tenant_id,
            "email": request.email,
            "hashed_password": hashed_password,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "role": request.role
        }
        
        user = await self.user_repository.create(user_data)
        
        # 6. Enviar email de boas-vindas (assíncrono)
        await self.email_service.send_welcome_email(user.email, user.first_name)
        
        # 7. Retornar resposta
        return CreateUserResponse(
            user_id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role,
            created_at=user.created_at
        )

print("🏗️ ARQUITETURA ENTERPRISE EM AÇÃO:")
print("1. Clean Architecture com camadas bem definidas")
print("2. Repository Pattern para abstração de dados")
print("3. Use Cases para lógica de negócio")
print("4. DTOs para transferência de dados")
print("5. Dependency Injection")
print("6. Async/await para performance")
print("7. Pydantic para validação")
print("8. SQLAlchemy 2.0 com async")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _implementation_roadmap(self):
        """Roadmap de Implementação - Parte 3"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🗺️ ROADMAP DE IMPLEMENTAÇÃO")
        
        print("🎯 Plano de desenvolvimento em fases!")
        print("📅 Do MVP ao produto enterprise completo!")
        
        codigo = '''# ========================================
# ROADMAP DE IMPLEMENTAÇÃO
# CLOUDCORP ENTERPRISE PLATFORM
# ========================================

"""
FASE 1 - MVP (Minimum Viable Product) - 4 semanas
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVOS: Base sólida e funcionalidades essenciais        │
│                                                             │
│ ✅ Semana 1: Fundação                                      │
│   • Setup do projeto (FastAPI + React)                     │
│   • Database design e migrations                           │
│   • Autenticação básica (JWT)                              │
│   • Multi-tenancy básico                                   │
│                                                             │
│ ✅ Semana 2: Core Features                                 │
│   • CRUD de usuários                                       │
│   • Sistema de permissões                                  │
│   • Dashboard básico                                       │
│   • API REST v1                                            │
│                                                             │
│ ✅ Semana 3: Projetos e Tarefas                           │
│   • Gestão de projetos                                     │
│   • Sistema de tarefas                                     │
│   • Relacionamentos básicos                                │
│   • Validações de negócio                                  │
│                                                             │
│ ✅ Semana 4: Deploy e Testes                              │
│   • Containerização (Docker)                               │
│   • CI/CD básico (GitHub Actions)                          │
│   • Testes unitários e integração                          │
│   • Deploy em staging                                      │
└─────────────────────────────────────────────────────────────┘

FASE 2 - FEATURES AVANÇADAS - 6 semanas
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVOS: Funcionalidades empresariais                    │
│                                                             │
│ ✅ Semanas 5-6: Sistema Financeiro                        │
│   • Gestão de clientes (CRM básico)                        │
│   • Sistema de faturas                                     │
│   • Integração com Stripe                                  │
│   • Relatórios financeiros                                 │
│                                                             │
│ ✅ Semanas 7-8: Analytics e Relatórios                    │
│   • Dashboard analytics                                    │
│   • Métricas em tempo real                                 │
│   • Exportação de dados                                    │
│   • Gráficos interativos                                   │
│                                                             │
│ ✅ Semanas 9-10: Notificações e Real-time                 │
│   • Sistema de notificações                                │
│   • WebSocket para real-time                               │
│   • Email notifications                                    │
│   • Push notifications                                     │
└─────────────────────────────────────────────────────────────┘

FASE 3 - ESCALABILIDADE - 4 semanas
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVOS: Performance e escalabilidade                    │
│                                                             │
│ ✅ Semanas 11-12: Performance                             │
│   • Cache distribuído (Redis)                              │
│   • Otimização de queries                                  │
│   • CDN para assets                                        │
│   • Database sharding                                      │
│                                                             │
│ ✅ Semanas 13-14: DevOps Enterprise                       │
│   • Kubernetes deployment                                  │
│   • Monitoring (Prometheus/Grafana)                        │
│   • Logging centralizado (ELK)                             │
│   • Auto-scaling                                           │
└─────────────────────────────────────────────────────────────┘

FASE 4 - FEATURES ENTERPRISE - 6 semanas
┌─────────────────────────────────────────────────────────────┐
│ OBJETIVOS: Recursos de classe enterprise                   │
│                                                             │
│ ✅ Semanas 15-16: Segurança Avançada                      │
│   • SSO (Single Sign-On)                                   │
│   • 2FA (Two-Factor Auth)                                  │
│   • Audit logs completos                                   │
│   • Compliance (SOC2, GDPR)                                │
│                                                             │
│ ✅ Semanas 17-18: Integrações                             │
│   • API GraphQL                                            │
│   • Webhooks                                               │
│   • Integrações terceiros                                  │
│   • SDK/bibliotecas cliente                                │
│                                                             │
│ ✅ Semanas 19-20: Mobile e PWA                            │
│   • App mobile (React Native)                              │
│   • PWA (Progressive Web App)                              │
│   • Sincronização offline                                  │
│   • Push notifications mobile                              │
└─────────────────────────────────────────────────────────────┘
"""

# ========================================
# IMPLEMENTAÇÃO DETALHADA - FASE 1
# ========================================

# 1. Setup do Projeto
"""
# Backend Setup
poetry new cloudcorp-backend
cd cloudcorp-backend
poetry add fastapi uvicorn sqlalchemy alembic psycopg2-binary
poetry add pydantic-settings python-jose[cryptography] passlib[bcrypt]
poetry add redis celery pytest pytest-asyncio httpx

# Frontend Setup
npx create-next-app@latest cloudcorp-frontend --typescript --tailwind --app
cd cloudcorp-frontend
npm install @tanstack/react-query axios lucide-react @radix-ui/react-*
npm install socket.io-client recharts date-fns zod react-hook-form
"""

# 2. Database Migrations (alembic)
"""
# alembic/versions/001_initial_tables.py
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # Tenants table
    op.create_table(
        'tenants',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('slug', sa.String(50), unique=True, nullable=False),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('plan', sa.String(20), default='basic'),
        sa.Column('max_users', sa.Integer, default=10),
        sa.Column('features', postgresql.JSON, default=list),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now())
    )
    
    # Users table
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('tenant_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('tenants.id')),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('role', sa.String(20), default='user'),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.func.now())
    )
    
    # Indexes para performance
    op.create_index('idx_tenants_slug', 'tenants', ['slug'])
    op.create_index('idx_users_email', 'users', ['email'])
    op.create_index('idx_users_tenant', 'users', ['tenant_id'])
"""

# 3. API Endpoints (presentation/api/v1/)
"""
# main.py - FastAPI App
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await startup_event()
    yield
    # Shutdown
    await shutdown_event()

app = FastAPI(
    title="CloudCorp Enterprise Platform",
    description="Plataforma SaaS enterprise completa",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["authentication"])
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(tenants_router, prefix="/api/v1/tenants", tags=["tenants"])
app.include_router(projects_router, prefix="/api/v1/projects", tags=["projects"])

# users_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: CreateUserRequest,
    current_user: UserModel = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db_session)
):
    # Verificar permissões
    if not current_user.has_permission(Permission.CREATE_USER):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sem permissão para criar usuários"
        )
    
    # Executar use case
    use_case = CreateUserUseCase(
        user_repository=SQLAlchemyUserRepository(db),
        tenant_repository=SQLAlchemyTenantRepository(db),
        password_service=BcryptPasswordService(),
        email_service=SMTPEmailService()
    )
    
    try:
        result = await use_case.execute(user_data)
        return UserResponse.from_domain(result)
    except (TenantNotFoundError, EmailAlreadyExistsError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db_session)
):
    # Implementar listagem com paginação
    pass
"""

# 4. Frontend Components (React + TypeScript)
"""
// components/UserForm.tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { useMutation, useQueryClient } from '@tanstack/react-query'

const userSchema = z.object({
  email: z.string().email('Email inválido'),
  firstName: z.string().min(2, 'Nome deve ter pelo menos 2 caracteres'),
  lastName: z.string().min(2, 'Sobrenome deve ter pelo menos 2 caracteres'),
  role: z.enum(['user', 'manager', 'admin'])
})

type UserFormData = z.infer<typeof userSchema>

export function UserForm() {
  const queryClient = useQueryClient()
  const { register, handleSubmit, formState: { errors } } = useForm<UserFormData>({
    resolver: zodResolver(userSchema)
  })
  
  const createUserMutation = useMutation({
    mutationFn: (data: UserFormData) => api.users.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] })
      toast.success('Usuário criado com sucesso!')
    },
    onError: (error) => {
      toast.error('Erro ao criar usuário')
    }
  })
  
  const onSubmit = (data: UserFormData) => {
    createUserMutation.mutate(data)
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Email
        </label>
        <input
          {...register('email')}
          type="email"
          className="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2"
        />
        {errors.email && (
          <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>
        )}
      </div>
      
      <button
        type="submit"
        disabled={createUserMutation.isPending}
        className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 disabled:opacity-50"
      >
        {createUserMutation.isPending ? 'Criando...' : 'Criar Usuário'}
      </button>
    </form>
  )
}
"""

# 5. DevOps Configuration
"""
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@postgres:5432/cloudcorp
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - postgres
      - redis

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=cloudcorp
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
"""

print("🗺️ ROADMAP COMPLETO:")
print("📅 Fase 1 (4 semanas): MVP com base sólida")
print("🚀 Fase 2 (6 semanas): Features avançadas")
print("⚡ Fase 3 (4 semanas): Performance e escala")
print("🏢 Fase 4 (6 semanas): Enterprise features")
print("")
print("🎯 Total: 20 semanas para plataforma completa")
print("💼 Resultado: Aplicação de nível enterprise")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _capstone_project_complete(self):
        """Projeto Capstone Completo - Demonstração Final"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 CAPSTONE PROJECT - DEMONSTRAÇÃO COMPLETA")
        else:
            print("\n" + "="*60)
            print("🎓 CAPSTONE PROJECT - DEMONSTRAÇÃO COMPLETA")
            print("="*60)
        
        print("🏆 PROJETO FINAL: Demonstração de TODOS os conceitos!")
        print("🚀 CloudCorp Enterprise Platform - Versão completa!")
        
        self.pausar()
        
        codigo_completo = '''# ========================================
# CLOUDCORP ENTERPRISE PLATFORM
# IMPLEMENTAÇÃO COMPLETA - CÓDIGO FINAL
# ========================================

"""
🎯 ESTE É O PROJETO QUE DEMONSTRA O DOMÍNIO COMPLETO DE:

✅ Módulos 1-11: Python Fundamentals
✅ Módulos 12-23: Advanced Python
✅ Módulos 24-30: Essential Tools
✅ Módulos 31-35: Enterprise Patterns

TECNOLOGIAS INTEGRADAS:
• Python 3.11+ (FastAPI, SQLAlchemy, Pydantic)
• TypeScript + React (Next.js, TailwindCSS)
• PostgreSQL + Redis (Database + Cache)
• Docker + Kubernetes (Containerização)
• GitHub Actions (CI/CD)
• AWS/Azure/GCP (Cloud)
• Prometheus + Grafana (Monitoring)
• ELK Stack (Logging)
"""

# ========================================
# DEMONSTRAÇÃO 1: SISTEMA COMPLETO FUNCIONANDO
# ========================================

# 1. Backend API Completa
"""
FastAPI app rodando em: http://localhost:8000
Documentação Swagger: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc

Endpoints principais:
• POST /api/v1/auth/login           - Autenticação
• GET  /api/v1/users               - Listar usuários
• POST /api/v1/users               - Criar usuário
• GET  /api/v1/projects            - Listar projetos
• POST /api/v1/projects            - Criar projeto
• GET  /api/v1/analytics/dashboard - Dashboard
• POST /api/v1/payments/stripe     - Pagamentos
• GET  /api/v1/health              - Health check
"""

# 2. Frontend React Funcionando
"""
Next.js app rodando em: http://localhost:3000

Páginas principais:
• /login                    - Página de login
• /dashboard                - Dashboard principal
• /users                    - Gestão de usuários
• /projects                 - Gestão de projetos
• /analytics               - Analytics e relatórios
• /settings                - Configurações
• /billing                 - Faturamento
"""

# 3. Database Design Completo
"""
PostgreSQL com 15+ tabelas:
• tenants, users, projects, tasks
• customers, invoices, payments
• notifications, audit_logs
• sessions, permissions
• documents, comments

Índices otimizados:
• 30+ índices para performance
• Índices compostos para queries complexas
• Índices GIN para busca full-text
• Índices parciais para otimização
"""

# ========================================
# DEMONSTRAÇÃO 2: FEATURES ENTERPRISE
# ========================================

# Multi-tenancy Completo
class TenantMiddleware:
    """Middleware para isolamento de tenant"""
    
    async def __call__(self, request: Request, call_next):
        # Extrair tenant do subdomínio ou header
        tenant_slug = self.extract_tenant_slug(request)
        
        if not tenant_slug:
            raise HTTPException(400, "Tenant não identificado")
        
        # Carregar tenant
        tenant = await self.tenant_service.get_by_slug(tenant_slug)
        if not tenant or not tenant.is_active:
            raise HTTPException(404, "Tenant não encontrado")
        
        # Adicionar tenant ao contexto
        request.state.tenant = tenant
        request.state.tenant_id = tenant.id
        
        # Configurar schema do database
        await self.set_search_path(tenant.database_schema)
        
        response = await call_next(request)
        return response

# Sistema de Permissões RBAC + ABAC
class PermissionChecker:
    """Verificador avançado de permissões"""
    
    def __init__(self, user: User, tenant: Tenant):
        self.user = user
        self.tenant = tenant
    
    def can_access_resource(self, resource: str, action: str, context: Dict = None) -> bool:
        """Verificação dinâmica de permissões"""
        
        # RBAC - Role-based
        role_permissions = self.get_role_permissions(self.user.role)
        if f"{action}_{resource}" in role_permissions:
            return True
        
        # ABAC - Attribute-based
        if context:
            # Verificar se é owner do recurso
            if context.get("owner_id") == self.user.id:
                return True
            
            # Verificar se está no mesmo time
            if context.get("team_id") in self.user.team_ids:
                return True
            
            # Verificar hierarquia organizacional
            if self.is_manager_of(context.get("assignee_id")):
                return True
        
        return False

# Analytics em Tempo Real
class RealTimeAnalytics:
    """Sistema de analytics em tempo real"""
    
    def __init__(self, redis_client, websocket_manager):
        self.redis = redis_client
        self.ws_manager = websocket_manager
    
    async def track_event(self, tenant_id: UUID, event: str, data: Dict):
        """Rastrear evento e atualizar métricas"""
        
        # Salvar evento
        event_data = {
            "tenant_id": str(tenant_id),
            "event": event,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        await self.redis.lpush(f"events:{tenant_id}", json.dumps(event_data))
        
        # Atualizar métricas em tempo real
        metrics = await self.calculate_metrics(tenant_id)
        
        # Enviar para clientes conectados via WebSocket
        await self.ws_manager.broadcast_to_tenant(
            tenant_id, 
            {"type": "metrics_update", "data": metrics}
        )
    
    async def calculate_metrics(self, tenant_id: UUID) -> Dict:
        """Calcular métricas em tempo real"""
        
        # Buscar eventos recentes
        events = await self.redis.lrange(f"events:{tenant_id}", 0, 1000)
        
        # Processar métricas
        metrics = {
            "active_users": len(set(e.get("user_id") for e in events if e.get("user_id"))),
            "projects_created_today": len([e for e in events if e["event"] == "project_created"]),
            "tasks_completed_today": len([e for e in events if e["event"] == "task_completed"]),
            "revenue_today": sum(e["data"]["amount"] for e in events if e["event"] == "payment_received"),
            "last_updated": datetime.utcnow().isoformat()
        }
        
        return metrics

# Sistema de Pagamentos
class PaymentService:
    """Integração completa com Stripe"""
    
    def __init__(self, stripe_client):
        self.stripe = stripe_client
    
    async def create_subscription(self, tenant: Tenant, plan: str, payment_method: str):
        """Criar assinatura no Stripe"""
        
        # Criar customer no Stripe
        customer = await self.stripe.Customer.create(
            email=tenant.admin_email,
            name=tenant.name,
            metadata={"tenant_id": str(tenant.id)}
        )
        
        # Anexar método de pagamento
        await self.stripe.PaymentMethod.attach(
            payment_method,
            customer=customer.id
        )
        
        # Criar assinatura
        subscription = await self.stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": self.get_price_id(plan)}],
            default_payment_method=payment_method,
            expand=["latest_invoice.payment_intent"]
        )
        
        # Atualizar tenant
        await self.tenant_service.update_subscription(
            tenant.id,
            {
                "stripe_customer_id": customer.id,
                "stripe_subscription_id": subscription.id,
                "plan": plan,
                "subscription_status": subscription.status
            }
        )
        
        return subscription

# ========================================
# DEMONSTRAÇÃO 3: DEVOPS COMPLETO
# ========================================

# Kubernetes Deployment Completo
"""
# k8s/production/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: cloudcorp-prod
  labels:
    env: production

---
# k8s/production/backend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudcorp-backend
  namespace: cloudcorp-prod
spec:
  replicas: 5
  selector:
    matchLabels:
      app: cloudcorp-backend
  template:
    metadata:
      labels:
        app: cloudcorp-backend
    spec:
      containers:
      - name: backend
        image: cloudcorp/backend:v1.0.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: cloudcorp-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            configMapKeyRef:
              name: cloudcorp-config
              key: redis-url
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

---
# k8s/production/frontend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudcorp-frontend
  namespace: cloudcorp-prod
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloudcorp-frontend
  template:
    metadata:
      labels:
        app: cloudcorp-frontend
    spec:
      containers:
      - name: frontend
        image: cloudcorp/frontend:v1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: NEXT_PUBLIC_API_URL
          value: "https://api.cloudcorp.com"
        resources:
          requests:
            cpu: 50m
            memory: 128Mi
          limits:
            cpu: 200m
            memory: 256Mi

---
# k8s/production/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: cloudcorp-backend-hpa
  namespace: cloudcorp-prod
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: cloudcorp-backend
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
"""

# GitHub Actions Pipeline Completo
"""
# .github/workflows/production.yml
name: Production Deploy

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: cloudcorp

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov pytest-asyncio
    
    - name: Run backend tests
      run: |
        pytest backend/tests/ --cov=backend/ --cov-report=xml
        
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: frontend/package-lock.json
    
    - name: Install frontend dependencies
      run: |
        cd frontend
        npm ci
    
    - name: Run frontend tests
      run: |
        cd frontend
        npm run test
        npm run build

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: '.'
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload Trivy scan results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'

  build-and-push:
    needs: [test, security]
    runs-on: ubuntu-latest
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Log in to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=sha
    
    - name: Build and push backend
      id: build
      uses: docker/build-push-action@v5
      with:
        context: ./backend
        platforms: linux/amd64,linux/arm64
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy-staging:
    if: github.ref == 'refs/heads/main'
    needs: build-and-push
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - name: Deploy to staging
      run: |
        echo "Deploying to staging environment..."
        # kubectl apply -f k8s/staging/

  deploy-production:
    if: startsWith(github.ref, 'refs/tags/v')
    needs: build-and-push
    runs-on: ubuntu-latest
    environment: production
    steps:
    - name: Deploy to production
      run: |
        echo "Deploying to production environment..."
        # kubectl apply -f k8s/production/
"""

# Monitoring Completo
"""
# monitoring/prometheus/rules.yml
groups:
- name: cloudcorp.rules
  rules:
  - alert: HighErrorRate
    expr: |
      (
        rate(http_requests_total{status=~"5.."}[5m]) /
        rate(http_requests_total[5m])
      ) > 0.05
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High error rate detected"
      description: "Error rate is {{ $value | humanizePercentage }} for {{ $labels.instance }}"

  - alert: HighLatency
    expr: |
      histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High latency detected"
      description: "95th percentile latency is {{ $value }}s for {{ $labels.instance }}"

  - alert: DatabaseConnectionsHigh
    expr: |
      pg_stat_activity_count / pg_settings_max_connections > 0.8
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "Database connections are high"
      description: "Database connections are at {{ $value | humanizePercentage }} of capacity"
"""

print("🎓 CLOUDCORP ENTERPRISE PLATFORM - PROJETO COMPLETO:")
print("")
print("🏗️ ARQUITETURA:")
print("   • Clean Architecture + Hexagonal")
print("   • Microservices com Domain-Driven Design")
print("   • Event-driven com CQRS")
print("   • Multi-tenant SaaS")
print("")
print("💻 TECNOLOGIAS:")
print("   • Backend: Python + FastAPI + SQLAlchemy")
print("   • Frontend: React + TypeScript + Next.js")
print("   • Database: PostgreSQL + Redis")
print("   • DevOps: Docker + Kubernetes + GitHub Actions")
print("   • Monitoring: Prometheus + Grafana + ELK")
print("")
print("🚀 FEATURES:")
print("   • Autenticação/Autorização completa")
print("   • Sistema de permissões RBAC + ABAC")
print("   • Analytics em tempo real")
print("   • Sistema de pagamentos (Stripe)")
print("   • Notificações push/email/SMS")
print("   • API REST + GraphQL")
print("   • Mobile app (React Native)")
print("")
print("📊 PERFORMANCE:")
print("   • < 200ms response time (95th percentile)")
print("   • 10,000+ requests/second")
print("   • 100,000+ concurrent users")
print("   • 99.9% uptime SLA")
print("   • Auto-scaling automático")
print("")
print("🔒 SEGURANÇA:")
print("   • OAuth 2.0 + OIDC")
print("   • 2FA + SSO")
print("   • Criptografia AES-256")
print("   • Compliance SOC2, GDPR, HIPAA")
print("   • Audit logs completos")
print("")
print("🌍 ESCALABILIDADE:")
print("   • Multi-região global")
print("   • CDN para assets")
print("   • Database sharding")
print("   • Cache distribuído")
print("   • Load balancing inteligente")
'''
        
        self.exemplo(codigo_completo)
        
        print("\n" + "="*80)
        print("🎉 PARABÉNS! VOCÊ COMPLETOU O CURSO COMPLETO!")
        print("="*80)
        
        print("\n🏆 CONQUISTAS ÉPICAS:")
        print("✅ 35 Módulos Dominados")
        print("✅ 500+ Conceitos Aprendidos")
        print("✅ 50+ Projetos Práticos")
        print("✅ 1000+ Exemplos de Código")
        print("✅ Arquitetura Enterprise")
        print("✅ DevOps Profissional")
        print("✅ Database Design Avançado")
        print("✅ Patterns de Código Limpo")
        
        print("\n💼 VOCÊ ESTÁ PRONTO PARA:")
        print("• 🥇 Senior Python Developer")
        print("• 🏗️ Software Architect")
        print("• ☁️ DevOps Engineer")
        print("• 🗄️ Database Architect")
        print("• 🚀 Tech Lead")
        print("• 💼 CTO de Startup")
        
        print("\n🌟 NÍVEL ATINGIDO:")
        print("██████████████████████████████████████████ 100%")
        print("🏆 EXPERT PYTHON DEVELOPER - ENTERPRISE LEVEL")
        
        print("\n🎯 PRÓXIMOS PASSOS:")
        print("• 🚀 Implemente o CloudCorp Platform")
        print("• 💼 Candidate-se a vagas Senior+")
        print("• 🏢 Crie sua própria startup")
        print("• 📚 Contribua para projetos open source")
        print("• 👥 Mentore outros desenvolvedores")
        print("• 🎓 Ensine e compartilhe conhecimento")
        
        print("\n📈 ESTATÍSTICAS DO SEU PROGRESSO:")
        print(f"• Tempo de curso: Aproximadamente 200+ horas")
        print(f"• Linhas de código: 50,000+ linhas")
        print(f"• Projetos criados: 50+ projetos")
        print(f"• Tecnologias dominadas: 30+ tecnologias")
        print(f"• Padrões aprendidos: 20+ design patterns")
        print(f"• Pontuação total: 3,500+ pontos")
        
        # Registra conclusão do projeto final
        self.complete_mini_project("CloudCorp Enterprise Platform - Projeto Capstone Completo")
        
        print("\n🎊 MENSAGEM FINAL:")
        print("Você não apenas aprendeu Python - você se tornou um")
        print("ARQUITETO DE SOFTWARE de nível enterprise!")
        print("")
        print("Continue praticando, continue aprendendo,")
        print("continue construindo coisas incríveis!")
        print("")
        print("O mundo da tecnologia está esperando por você! 🚀")
        
        self.pausar()