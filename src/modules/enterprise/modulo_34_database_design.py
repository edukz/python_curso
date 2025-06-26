#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 34: Database Design & Performance
Aprenda design de banco de dados profissional, otimização e performance
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Protocol, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid
from ..shared.base_module import BaseModule


class Modulo34DatabaseDesign(BaseModule):
    """Módulo 34: Database Design & Performance"""
    
    def __init__(self):
        super().__init__("modulo_34", "Database Design & Performance")
        self.has_mini_project = True
        self.mini_project_points = 150
    
    def execute(self) -> None:
        """Executa o módulo sobre Database Design"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            self.pausar()
            return
        
        try:
            self._database_design_intro()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _database_design_intro(self) -> None:
        """Conteúdo principal sobre Database Design"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🗄️ MÓDULO 34: DATABASE DESIGN & PERFORMANCE")
        else:
            print("\n" + "="*60)
            print("🗄️ MÓDULO 34: DATABASE DESIGN & PERFORMANCE")
            print("="*60)
        
        print("🎯 Database Design é fundamental para aplicações escaláveis!")
        print("🏗️ Domine design de banco de dados profissional:")
        print("• 📊 Modelagem conceitual, lógica e física")
        print("• 🔧 Normalização e desnormalização")
        print("• ⚡ Índices e otimização de queries")
        print("• 🔄 Transactions e ACID")
        print("• 📈 Sharding e replicação")
        print("• 🚀 NoSQL vs SQL")
        
        self.pausar()
        
        self._database_fundamentals()
        self._performance_optimization()
        self._mini_projeto_enterprise_database()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _database_fundamentals(self):
        """Database Design Fundamentals - Parte 1"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ FUNDAMENTOS DE DATABASE DESIGN")
        
        print("📐 Design de banco de dados é uma arte e ciência!")
        print("🎯 Princípios fundamentais:")
        print("• 📊 Modelagem conceitual (ERD)")
        print("• 🔧 Normalização (1NF, 2NF, 3NF, BCNF)")
        print("• ⚡ Performance e escalabilidade")
        print("• 🔒 Integridade e consistência")
        print("• 🚀 Flexibilidade para evolução")
        
        codigo = '''# ========================================
# DATABASE DESIGN FUNDAMENTALS
# ========================================

# 1. MODELAGEM CONCEITUAL - SISTEMA E-COMMERCE
# Entidades e relacionamentos principais

"""
ENTIDADES PRINCIPAIS:
- User (Usuário)
- Category (Categoria)
- Product (Produto)
- Order (Pedido)
- OrderItem (Item do Pedido)
- Address (Endereço)
- Payment (Pagamento)
- Review (Avaliação)
- Cart (Carrinho)
- CartItem (Item do Carrinho)

RELACIONAMENTOS:
- User 1:N Address
- User 1:N Order
- User 1:1 Cart
- Category 1:N Product
- Product 1:N OrderItem
- Product 1:N Review
- Order 1:N OrderItem
- Order 1:1 Payment
- Cart 1:N CartItem
"""

# ========================================
# 2. MODELAGEM FÍSICA - POSTGRESQL
# ========================================

-- Extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Schema para organização
CREATE SCHEMA ecommerce;
SET search_path TO ecommerce;

-- ========================================
-- TABELA: USERS
-- ========================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    
    -- Índices para performance
    CONSTRAINT users_email_check CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')
);

-- Índices otimizados
CREATE INDEX idx_users_email ON users USING btree (email);
CREATE INDEX idx_users_status ON users USING btree (status);
CREATE INDEX idx_users_created_at ON users USING btree (created_at);
CREATE INDEX idx_users_email_trgm ON users USING gin (email gin_trgm_ops);

-- Trigger para updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ========================================
-- TABELA: ADDRESSES
-- ========================================
CREATE TABLE addresses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    street_address VARCHAR(255) NOT NULL,
    street_number VARCHAR(20),
    complement VARCHAR(100),
    neighborhood VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(2) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    country VARCHAR(2) DEFAULT 'BR',
    address_type VARCHAR(20) DEFAULT 'home' CHECK (address_type IN ('home', 'work', 'other')),
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_addresses_user_id ON addresses (user_id);
CREATE INDEX idx_addresses_postal_code ON addresses (postal_code);
CREATE INDEX idx_addresses_city_state ON addresses (city, state);

-- Constraint: apenas um endereço padrão por usuário
CREATE UNIQUE INDEX idx_addresses_user_default ON addresses (user_id) 
WHERE is_default = TRUE;

-- ========================================
-- TABELA: CATEGORIES
-- ========================================
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    parent_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    image_url VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Evitar hierarquia circular
    CONSTRAINT categories_no_self_parent CHECK (id != parent_id)
);

-- Índices
CREATE INDEX idx_categories_parent_id ON categories (parent_id);
CREATE INDEX idx_categories_slug ON categories (slug);
CREATE INDEX idx_categories_active_sort ON categories (is_active, sort_order);

-- ========================================
-- TABELA: PRODUCTS
-- ========================================
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE RESTRICT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    slug VARCHAR(200) UNIQUE NOT NULL,
    short_description VARCHAR(500),
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    cost_price DECIMAL(10,2) CHECK (cost_price >= 0),
    weight DECIMAL(8,3) CHECK (weight >= 0),
    dimensions JSONB, -- {length, width, height}
    stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
    min_stock_level INTEGER DEFAULT 0,
    max_stock_level INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_digital BOOLEAN DEFAULT FALSE,
    requires_shipping BOOLEAN DEFAULT TRUE,
    meta_title VARCHAR(60),
    meta_description VARCHAR(160),
    images JSONB, -- Array de URLs de imagens
    attributes JSONB, -- Atributos flexíveis (cor, tamanho, etc.)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT products_price_cost_check CHECK (price >= cost_price OR cost_price IS NULL)
);

-- Índices otimizados para e-commerce
CREATE INDEX idx_products_category ON products (category_id);
CREATE INDEX idx_products_sku ON products (sku);
CREATE INDEX idx_products_slug ON products (slug);
CREATE INDEX idx_products_active_featured ON products (is_active, is_featured);
CREATE INDEX idx_products_price ON products (price) WHERE is_active = TRUE;
CREATE INDEX idx_products_stock ON products (stock_quantity) WHERE is_active = TRUE;
CREATE INDEX idx_products_name_trgm ON products USING gin (name gin_trgm_ops);

-- Índice GIN para busca em atributos JSON
CREATE INDEX idx_products_attributes ON products USING gin (attributes);

-- ========================================
-- TABELA: CARTS
-- ========================================
CREATE TABLE carts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    session_id VARCHAR(100), -- Para usuários não logados
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE DEFAULT (CURRENT_TIMESTAMP + INTERVAL '30 days'),
    
    -- Usuário logado OU sessão
    CONSTRAINT carts_user_or_session CHECK (
        (user_id IS NOT NULL AND session_id IS NULL) OR 
        (user_id IS NULL AND session_id IS NOT NULL)
    )
);

CREATE INDEX idx_carts_user_id ON carts (user_id);
CREATE INDEX idx_carts_session_id ON carts (session_id);
CREATE INDEX idx_carts_expires_at ON carts (expires_at);

-- ========================================
-- TABELA: CART_ITEMS
-- ========================================
CREATE TABLE cart_items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cart_id UUID NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price >= 0),
    added_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Um produto por carrinho (atualizar quantidade)
    UNIQUE(cart_id, product_id)
);

CREATE INDEX idx_cart_items_cart_id ON cart_items (cart_id);
CREATE INDEX idx_cart_items_product_id ON cart_items (product_id);

-- ========================================
-- TABELA: ORDERS
-- ========================================
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN (
        'pending', 'confirmed', 'processing', 'shipped', 
        'delivered', 'cancelled', 'refunded'
    )),
    
    -- Valores do pedido
    subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0),
    shipping_cost DECIMAL(10,2) DEFAULT 0 CHECK (shipping_cost >= 0),
    tax_amount DECIMAL(10,2) DEFAULT 0 CHECK (tax_amount >= 0),
    discount_amount DECIMAL(10,2) DEFAULT 0 CHECK (discount_amount >= 0),
    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
    
    -- Endereço de entrega (desnormalizado para histórico)
    shipping_address JSONB NOT NULL,
    billing_address JSONB NOT NULL,
    
    -- Metadados
    notes TEXT,
    shipped_at TIMESTAMP WITH TIME ZONE,
    delivered_at TIMESTAMP WITH TIME ZONE,
    cancelled_at TIMESTAMP WITH TIME ZONE,
    cancellation_reason TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Validação: total = subtotal + shipping + tax - discount
    CONSTRAINT orders_total_check CHECK (
        total_amount = (subtotal + shipping_cost + tax_amount - discount_amount)
    )
);

-- Índices para relatórios e consultas
CREATE INDEX idx_orders_user_id ON orders (user_id);
CREATE INDEX idx_orders_status ON orders (status);
CREATE INDEX idx_orders_created_at ON orders (created_at);
CREATE INDEX idx_orders_order_number ON orders (order_number);
CREATE INDEX idx_orders_status_created ON orders (status, created_at);

-- Sequência para número do pedido
CREATE SEQUENCE order_number_seq START 1000;

-- Função para gerar número do pedido
CREATE OR REPLACE FUNCTION generate_order_number()
RETURNS TEXT AS $$
BEGIN
    RETURN 'ORD-' || LPAD(nextval('order_number_seq')::TEXT, 6, '0');
END;
$$ LANGUAGE plpgsql;

-- Trigger para gerar número do pedido
CREATE OR REPLACE FUNCTION set_order_number()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.order_number IS NULL THEN
        NEW.order_number := generate_order_number();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_set_order_number
    BEFORE INSERT ON orders
    FOR EACH ROW
    EXECUTE FUNCTION set_order_number();

# ========================================
# 3. PYTHON ORM COM SQLALCHEMY
# ========================================

from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, Text, Numeric, ForeignKey, CheckConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'ecommerce'}
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20))
    date_of_birth = Column(DateTime)
    status = Column(String(20), default='active')
    email_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime)
    
    # Relacionamentos
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user", uselist=False)
    
    __table_args__ = (
        CheckConstraint("status IN ('active', 'inactive', 'suspended')", name='check_user_status'),
        {'schema': 'ecommerce'}
    )

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'ecommerce'}
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey('ecommerce.categories.id'), nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    images = Column(JSONB)
    attributes = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    
    __table_args__ = (
        CheckConstraint('price >= 0', name='check_product_price'),
        CheckConstraint('stock_quantity >= 0', name='check_product_stock'),
        Index('idx_products_active_price', 'is_active', 'price'),
        {'schema': 'ecommerce'}
    )

# Repository Pattern para acesso a dados
class UserRepository:
    def __init__(self, session):
        self.session = session
    
    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user
    
    def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()
    
    def get_active_users(self, limit: int = 100) -> List[User]:
        return self.session.query(User).filter(
            User.status == 'active'
        ).limit(limit).all()
    
    def search_users(self, query: str) -> List[User]:
        return self.session.query(User).filter(
            User.first_name.ilike(f'%{query}%') |
            User.last_name.ilike(f'%{query}%') |
            User.email.ilike(f'%{query}%')
        ).all()

# Service Layer para lógica de negócio
class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    def register_user(self, email: str, password: str, first_name: str, last_name: str) -> User:
        # Verificar se usuário já existe
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("Email já cadastrado")
        
        # Hash da senha (usar bcrypt em produção)
        password_hash = self._hash_password(password)
        
        # Criar usuário
        user_data = {
            'email': email,
            'password_hash': password_hash,
            'first_name': first_name,
            'last_name': last_name
        }
        
        return self.user_repo.create_user(user_data)
    
    def _hash_password(self, password: str) -> str:
        # Implementar hash seguro (bcrypt, scrypt, argon2)
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

print("🏗️ DATABASE DESIGN EM AÇÃO:")
print("1. Modelagem conceitual (ERD)")
print("2. Modelagem física otimizada")
print("3. Índices para performance")
print("4. Constraints para integridade")
print("5. Triggers para automação")
print("6. ORM com SQLAlchemy")
print("7. Repository Pattern")
print("8. Service Layer")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _performance_optimization(self):
        """Performance e Otimização - Parte 2"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ PERFORMANCE E OTIMIZAÇÃO")
        
        print("🚀 Performance é crítica para aplicações de alta escala!")
        print("🎯 Estratégias de otimização:")
        print("• 📊 Query optimization e EXPLAIN")
        print("• 🔍 Índices estratégicos")
        print("• 💾 Caching inteligente")
        print("• 🔄 Connection pooling")
        print("• 📈 Particionamento e sharding")
        print("• 🔄 Read replicas")
        
        codigo = '''# ========================================
# DATABASE PERFORMANCE & OPTIMIZATION
# ========================================

# 1. ANÁLISE DE PERFORMANCE COM EXPLAIN
# Como identificar gargalos de performance

-- Analisar plano de execução
EXPLAIN ANALYZE
SELECT u.email, u.first_name, COUNT(o.id) as order_count
FROM ecommerce.users u
LEFT JOIN ecommerce.orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.email, u.first_name
ORDER BY order_count DESC
LIMIT 100;

-- Exemplo de output:
/*
GroupAggregate  (cost=15234.56..15534.78 rows=100 width=45) (actual time=123.456..134.567 rows=85 loops=1)
  Group Key: u.id, u.email, u.first_name
  ->  Sort  (cost=15234.56..15284.67 rows=20044 width=37) (actual time=120.123..125.456 rows=18567 loops=1) 
        Sort Key: (count(o.id)) DESC
        Sort Method: quicksort  Memory: 1456kB
        ->  Hash Left Join  (cost=823.45..13456.78 rows=20044 width=37) (actual time=12.345..98.765 rows=18567 loops=1)
              Hash Cond: (u.id = o.user_id)
              ->  Seq Scan on users u  (cost=0.00..567.89 rows=18567 width=29) (actual time=0.012..8.456 rows=18567 loops=1)
                    Filter: (created_at >= '2024-01-01'::date)
                    Rows Removed by Filter: 2433
              ->  Hash  (cost=456.78..456.78 rows=12345 width=16) (actual time=11.234..11.234 rows=12345 loops=1)
                    Buckets: 16384  Batches: 1  Memory Usage: 567kB
                    ->  Seq Scan on orders o  (cost=0.00..456.78 rows=12345 width=16) (actual time=0.023..5.678 rows=12345 loops=1)
Planning Time: 0.234 ms
Execution Time: 136.789 ms
*/

# ========================================
# 2. OTIMIZAÇÃO DE QUERIES COMPLEXAS
# ========================================

-- PROBLEMA: Query lenta para relatório de vendas
-- Query original (LENTA - 2.5 segundos)
SELECT 
    p.name,
    c.name as category_name,
    SUM(oi.quantity) as total_sold,
    SUM(oi.quantity * oi.unit_price) as total_revenue,
    AVG(r.rating) as avg_rating,
    COUNT(DISTINCT o.user_id) as unique_customers
FROM ecommerce.products p
JOIN ecommerce.categories c ON p.category_id = c.id
JOIN ecommerce.order_items oi ON p.id = oi.product_id
JOIN ecommerce.orders o ON oi.order_id = o.id
LEFT JOIN ecommerce.reviews r ON p.id = r.product_id
WHERE o.created_at >= '2024-01-01'
    AND o.status IN ('delivered', 'shipped')
GROUP BY p.id, p.name, c.name
HAVING SUM(oi.quantity) >= 10
ORDER BY total_revenue DESC;

-- SOLUÇÃO 1: Índices compostos otimizados
CREATE INDEX idx_orders_status_created_at ON ecommerce.orders (status, created_at) 
WHERE status IN ('delivered', 'shipped');

CREATE INDEX idx_order_items_product_order ON ecommerce.order_items (product_id, order_id);

CREATE INDEX idx_reviews_product_rating ON ecommerce.reviews (product_id, rating) 
WHERE rating IS NOT NULL;

-- SOLUÇÃO 2: Query reescrita (RÁPIDA - 0.3 segundos)
WITH order_stats AS (
    SELECT 
        oi.product_id,
        SUM(oi.quantity) as total_sold,
        SUM(oi.quantity * oi.unit_price) as total_revenue,
        COUNT(DISTINCT o.user_id) as unique_customers
    FROM ecommerce.order_items oi
    JOIN ecommerce.orders o ON oi.order_id = o.id
    WHERE o.created_at >= '2024-01-01'
        AND o.status IN ('delivered', 'shipped')
    GROUP BY oi.product_id
    HAVING SUM(oi.quantity) >= 10
),
review_stats AS (
    SELECT 
        product_id,
        AVG(rating) as avg_rating
    FROM ecommerce.reviews
    WHERE rating IS NOT NULL
    GROUP BY product_id
)
SELECT 
    p.name,
    c.name as category_name,
    os.total_sold,
    os.total_revenue,
    COALESCE(rs.avg_rating, 0) as avg_rating,
    os.unique_customers
FROM order_stats os
JOIN ecommerce.products p ON os.product_id = p.id
JOIN ecommerce.categories c ON p.category_id = c.id
LEFT JOIN review_stats rs ON p.id = rs.product_id
ORDER BY os.total_revenue DESC;

# ========================================
# 3. MATERIALISED VIEWS PARA PERFORMANCE
# ========================================

-- View materializada para dashboard de vendas
CREATE MATERIALIZED VIEW ecommerce.mv_daily_sales AS
SELECT 
    DATE(o.created_at) as sale_date,
    COUNT(*) as order_count,
    SUM(o.total_amount) as total_revenue,
    AVG(o.total_amount) as avg_order_value,
    COUNT(DISTINCT o.user_id) as unique_customers,
    
    -- Métricas por categoria
    jsonb_object_agg(
        c.name, 
        jsonb_build_object(
            'orders', cat_stats.order_count,
            'revenue', cat_stats.revenue
        )
    ) as category_breakdown
FROM ecommerce.orders o
JOIN (
    SELECT 
        o.id as order_id,
        c.name,
        COUNT(*) as order_count,
        SUM(oi.quantity * oi.unit_price) as revenue
    FROM ecommerce.orders o
    JOIN ecommerce.order_items oi ON o.id = oi.order_id
    JOIN ecommerce.products p ON oi.product_id = p.id
    JOIN ecommerce.categories c ON p.category_id = c.id
    GROUP BY o.id, c.name
) cat_stats ON o.id = cat_stats.order_id
JOIN ecommerce.categories c ON TRUE
WHERE o.status IN ('delivered', 'shipped')
GROUP BY DATE(o.created_at);

-- Índice na view materializada
CREATE INDEX idx_mv_daily_sales_date ON ecommerce.mv_daily_sales (sale_date);

-- Função para refresh automático
CREATE OR REPLACE FUNCTION refresh_daily_sales_mv()
RETURNS void AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY ecommerce.mv_daily_sales;
END;
$$ LANGUAGE plpgsql;

-- Agendar refresh (usar pg_cron ou cron do sistema)
-- SELECT cron.schedule('refresh-daily-sales', '0 1 * * *', 'SELECT refresh_daily_sales_mv();');

# ========================================
# 4. PARTICIONAMENTO PARA ESCALABILIDADE
# ========================================

-- Particionamento por data da tabela orders
CREATE TABLE ecommerce.orders_partitioned (
    LIKE ecommerce.orders INCLUDING ALL
) PARTITION BY RANGE (created_at);

-- Partições mensais
CREATE TABLE ecommerce.orders_2024_01 PARTITION OF ecommerce.orders_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE ecommerce.orders_2024_02 PARTITION OF ecommerce.orders_partitioned
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- Função para criar partições automaticamente
CREATE OR REPLACE FUNCTION create_monthly_partition(table_name text, start_date date)
RETURNS void AS $$
DECLARE
    partition_name text;
    end_date date;
BEGIN
    end_date := start_date + INTERVAL '1 month';
    partition_name := table_name || '_' || to_char(start_date, 'YYYY_MM');
    
    EXECUTE format('CREATE TABLE IF NOT EXISTS ecommerce.%I PARTITION OF ecommerce.%I
                    FOR VALUES FROM (%L) TO (%L)',
                   partition_name, table_name, start_date, end_date);
END;
$$ LANGUAGE plpgsql;

# ========================================
# 5. CACHING ESTRATÉGICO COM REDIS
# ========================================

import redis
import json
import hashlib
from typing import Optional, Any
from functools import wraps

class CacheManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)
    
    def get(self, key: str) -> Optional[Any]:
        """Buscar valor do cache"""
        try:
            value = self.redis.get(key)
            return json.loads(value) if value else None
        except:
            return None
    
    def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """Salvar valor no cache"""
        try:
            return self.redis.setex(key, ttl, json.dumps(value, default=str))
        except:
            return False
    
    def delete(self, key: str) -> bool:
        """Remover valor do cache"""
        return bool(self.redis.delete(key))
    
    def cache_key(self, prefix: str, *args, **kwargs) -> str:
        """Gerar chave de cache consistente"""
        key_data = f"{prefix}:{args}:{sorted(kwargs.items())}"
        return hashlib.md5(key_data.encode()).hexdigest()

# Decorator para cache automático
def cached(prefix: str, ttl: int = 3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache = CacheManager()
            cache_key = cache.cache_key(prefix, *args, **kwargs)
            
            # Tentar buscar do cache
            result = cache.get(cache_key)
            if result is not None:
                return result
            
            # Executar função e cachear resultado
            result = func(*args, **kwargs)
            cache.set(cache_key, result, ttl)
            return result
        return wrapper
    return decorator

# Exemplo de uso do cache
class ProductService:
    @cached("product_details", ttl=1800)  # 30 minutos
    def get_product_details(self, product_id: str):
        # Query complexa que busca produto + reviews + relacionados
        return self._fetch_product_from_db(product_id)
    
    @cached("category_products", ttl=600)  # 10 minutos
    def get_products_by_category(self, category_id: str, page: int = 1):
        return self._fetch_category_products(category_id, page)
    
    def invalidate_product_cache(self, product_id: str):
        """Invalidar cache quando produto é atualizado"""
        cache = CacheManager()
        # Invalidar caches relacionados
        patterns = [
            f"product_details:*{product_id}*",
            f"category_products:*",
            f"search_results:*"
        ]
        for pattern in patterns:
            keys = cache.redis.keys(pattern)
            if keys:
                cache.redis.delete(*keys)

# ========================================
# 6. CONNECTION POOLING
# ========================================

from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

class DatabaseManager:
    def __init__(self):
        # Connection pool otimizado
        self.engine = create_engine(
            'postgresql://user:pass@localhost/ecommerce',
            poolclass=QueuePool,
            pool_size=20,        # Conexões ativas
            max_overflow=30,     # Conexões extras em picos
            pool_pre_ping=True,  # Verificar conexões
            pool_recycle=3600,   # Reciclar conexões a cada hora
            echo=False           # Log de queries (dev only)
        )
        
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_session(self):
        """Context manager para sessões"""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

# ========================================
# 7. MONITORAMENTO DE PERFORMANCE
# ========================================

-- Query para identificar queries lentas
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows,
    100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 20;

-- Monitorar locks e bloqueios
SELECT 
    blocked_locks.pid AS blocked_pid,
    blocked_activity.usename AS blocked_user,
    blocking_locks.pid AS blocking_pid,
    blocking_activity.usename AS blocking_user,
    blocked_activity.query AS blocked_statement,
    blocking_activity.query AS current_statement_in_blocking_process
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks 
    ON blocking_locks.locktype = blocked_locks.locktype
    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;

# Classe para métricas de performance
class PerformanceMonitor:
    def __init__(self, db_session):
        self.session = db_session
    
    def get_slow_queries(self, min_duration_ms: int = 1000):
        """Queries que demoram mais que X ms"""
        query = """
        SELECT query, calls, total_time, mean_time, rows
        FROM pg_stat_statements 
        WHERE mean_time > :min_duration
        ORDER BY total_time DESC 
        LIMIT 50
        """
        return self.session.execute(query, {"min_duration": min_duration_ms}).fetchall()
    
    def get_table_stats(self):
        """Estatísticas de uso das tabelas"""
        query = """
        SELECT 
            schemaname,
            tablename,
            n_tup_ins as inserts,
            n_tup_upd as updates,
            n_tup_del as deletes,
            seq_scan as sequential_scans,
            seq_tup_read as sequential_reads,
            idx_scan as index_scans,
            idx_tup_fetch as index_reads
        FROM pg_stat_user_tables 
        ORDER BY seq_scan DESC
        """
        return self.session.execute(query).fetchall()

print("⚡ PERFORMANCE EM AÇÃO:")
print("1. Análise com EXPLAIN ANALYZE")
print("2. Índices compostos estratégicos")
print("3. Materialized Views para agregações")
print("4. Particionamento por data")
print("5. Cache inteligente com Redis")
print("6. Connection pooling otimizado")
print("7. Monitoramento contínuo")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _mini_projeto_enterprise_database(self):
        """Mini Projeto - Sistema de Database Enterprise Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI-PROJETO: SISTEMA ENTERPRISE DATABASE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI-PROJETO: SISTEMA ENTERPRISE DATABASE")
            print("="*50)
        
        print("🚀 DESAFIO ÉPICO: Sistema completo de database enterprise!")
        print("🏆 Este projeto demonstra expertise em database de nível SENIOR!")
        
        self.pausar()
        
        print("\n🎯 OBJETIVOS DO PROJETO:")
        print("✅ Sistema multi-tenant SaaS")
        print("✅ Sharding e particionamento")
        print("✅ Read/Write replicas")
        print("✅ Cache distribuído")
        print("✅ Monitoramento avançado")
        print("✅ Backup e disaster recovery")
        print("✅ Performance tuning")
        
        codigo_projeto = '''# ========================================
# PROJETO ENTERPRISE DATABASE
# SISTEMA MULTI-TENANT SAAS COMPLETO
# ========================================

# Estrutura do projeto:
"""
enterprise-saas/
├── database/
│   ├── migrations/           # Migrações versionadas
│   ├── seeds/               # Dados iniciais
│   ├── schemas/             # Schemas por tenant
│   └── partitions/          # Scripts de particionamento
├── replication/
│   ├── master-config/       # Configuração master
│   ├── slave-config/        # Configuração slaves
│   └── failover/            # Scripts de failover
├── monitoring/
│   ├── grafana/             # Dashboards
│   ├── prometheus/          # Métricas
│   └── alerts/              # Regras de alerta
├── backup/
│   ├── scripts/             # Scripts de backup
│   ├── restore/             # Scripts de restore
│   └── policies/            # Políticas de retenção
└── performance/
    ├── benchmarks/          # Testes de performance
    ├── optimization/        # Scripts de otimização
    └── analysis/            # Análise de queries
"""

# ========================================
# 1. ARQUITETURA MULTI-TENANT
# ========================================

-- Estratégia 1: Schema por Tenant (isolamento máximo)
CREATE SCHEMA tenant_empresa_a;
CREATE SCHEMA tenant_empresa_b;
CREATE SCHEMA tenant_startup_x;

-- Tabela global de tenants
CREATE TABLE public.tenants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    schema_name VARCHAR(50) UNIQUE NOT NULL,
    plan VARCHAR(20) DEFAULT 'basic' CHECK (plan IN ('basic', 'pro', 'enterprise')),
    max_users INTEGER DEFAULT 10,
    max_storage_gb INTEGER DEFAULT 5,
    features JSONB DEFAULT '{}',
    
    -- Configurações de database
    db_host VARCHAR(100) DEFAULT 'localhost',
    db_name VARCHAR(50) DEFAULT 'saas_db',
    read_replica_host VARCHAR(100),
    
    -- Status e limites
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'cancelled')),
    users_count INTEGER DEFAULT 0,
    storage_used_gb DECIMAL(8,2) DEFAULT 0,
    
    -- Auditoria
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_activity TIMESTAMP WITH TIME ZONE
);

-- Função para criar schema de tenant
CREATE OR REPLACE FUNCTION create_tenant_schema(tenant_slug TEXT)
RETURNS TEXT AS $$
DECLARE
    schema_name TEXT;
BEGIN
    schema_name := 'tenant_' || tenant_slug;
    
    -- Criar schema
    EXECUTE 'CREATE SCHEMA IF NOT EXISTS ' || quote_ident(schema_name);
    
    -- Criar tabelas do tenant
    EXECUTE format('
        CREATE TABLE %I.users (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            email VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            name VARCHAR(200) NOT NULL,
            role VARCHAR(50) DEFAULT ''user'',
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )', schema_name);
    
    EXECUTE format('
        CREATE TABLE %I.projects (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(200) NOT NULL,
            description TEXT,
            owner_id UUID NOT NULL REFERENCES %I.users(id),
            status VARCHAR(20) DEFAULT ''active'',
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )', schema_name, schema_name);
    
    EXECUTE format('
        CREATE TABLE %I.tasks (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            project_id UUID NOT NULL REFERENCES %I.projects(id) ON DELETE CASCADE,
            title VARCHAR(500) NOT NULL,
            description TEXT,
            assignee_id UUID REFERENCES %I.users(id),
            status VARCHAR(20) DEFAULT ''todo'',
            priority VARCHAR(10) DEFAULT ''medium'',
            due_date TIMESTAMP WITH TIME ZONE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        )', schema_name, schema_name, schema_name);
    
    -- Criar índices por tenant
    EXECUTE format('CREATE INDEX idx_%s_users_email ON %I.users (email)', 
                   replace(schema_name, '.', '_'), schema_name);
    EXECUTE format('CREATE INDEX idx_%s_tasks_project ON %I.tasks (project_id, status)', 
                   replace(schema_name, '.', '_'), schema_name);
    
    RETURN schema_name;
END;
$$ LANGUAGE plpgsql;

# ========================================
# 2. SHARDING HORIZONTAL
# ========================================

-- Configuração para sharding por hash do tenant_id
CREATE TABLE public.shard_config (
    shard_id INTEGER PRIMARY KEY,
    shard_name VARCHAR(50) NOT NULL,
    db_host VARCHAR(100) NOT NULL,
    db_port INTEGER DEFAULT 5432,
    db_name VARCHAR(50) NOT NULL,
    db_user VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    tenant_count INTEGER DEFAULT 0,
    max_tenants INTEGER DEFAULT 1000,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Inserir shards
INSERT INTO public.shard_config (shard_id, shard_name, db_host, db_name, db_user) VALUES
(0, 'shard_0', 'db-shard-0.empresa.com', 'saas_shard_0', 'shard_user'),
(1, 'shard_1', 'db-shard-1.empresa.com', 'saas_shard_1', 'shard_user'),
(2, 'shard_2', 'db-shard-2.empresa.com', 'saas_shard_2', 'shard_user');

-- Função para determinar shard
CREATE OR REPLACE FUNCTION get_tenant_shard(tenant_id UUID)
RETURNS INTEGER AS $$
BEGIN
    -- Hash simples para distribuir tenants
    RETURN hashtext(tenant_id::TEXT) % 3;
END;
$$ LANGUAGE plpgsql;

# Python: Shard Router
class ShardRouter:
    def __init__(self):
        self.shards = self._load_shard_config()
    
    def _load_shard_config(self) -> Dict[int, dict]:
        """Carregar configuração dos shards do banco"""
        # Query da tabela shard_config
        return {
            0: {'host': 'db-shard-0.empresa.com', 'db': 'saas_shard_0'},
            1: {'host': 'db-shard-1.empresa.com', 'db': 'saas_shard_1'},
            2: {'host': 'db-shard-2.empresa.com', 'db': 'saas_shard_2'}
        }
    
    def get_shard_for_tenant(self, tenant_id: str) -> dict:
        """Determinar shard para um tenant"""
        shard_id = hash(tenant_id) % len(self.shards)
        return self.shards[shard_id]
    
    def get_connection(self, tenant_id: str):
        """Obter conexão para o shard correto"""
        shard = self.get_shard_for_tenant(tenant_id)
        return create_engine(f"postgresql://user:pass@{shard['host']}/{shard['db']}")

# ========================================
# 3. READ/WRITE REPLICAS
# ========================================

# Configuração de replicação
class DatabaseRouter:
    def __init__(self):
        self.master = create_engine("postgresql://user:pass@master-db:5432/saas")
        self.read_replicas = [
            create_engine("postgresql://user:pass@replica-1:5432/saas"),
            create_engine("postgresql://user:pass@replica-2:5432/saas"),
            create_engine("postgresql://user:pass@replica-3:5432/saas")
        ]
        self.current_replica = 0
    
    def get_write_connection(self):
        """Conexão para escrita (sempre master)"""
        return self.master
    
    def get_read_connection(self):
        """Conexão para leitura (round-robin nas replicas)"""
        replica = self.read_replicas[self.current_replica]
        self.current_replica = (self.current_replica + 1) % len(self.read_replicas)
        return replica
    
    def execute_write(self, query: str, params: dict = None):
        """Executar query de escrita"""
        with self.get_write_connection().connect() as conn:
            return conn.execute(query, params or {})
    
    def execute_read(self, query: str, params: dict = None):
        """Executar query de leitura"""
        with self.get_read_connection().connect() as conn:
            return conn.execute(query, params or {})

# Repository com read/write separation
class UserRepository:
    def __init__(self, db_router: DatabaseRouter, tenant_schema: str):
        self.db = db_router
        self.schema = tenant_schema
    
    def create_user(self, user_data: dict) -> dict:
        """Criar usuário (WRITE)"""
        query = f"""
        INSERT INTO {self.schema}.users (email, password_hash, name, role)
        VALUES (:email, :password_hash, :name, :role)
        RETURNING id, email, name, created_at
        """
        result = self.db.execute_write(query, user_data)
        return result.fetchone()._asdict()
    
    def get_user_by_email(self, email: str) -> Optional[dict]:
        """Buscar usuário por email (READ)"""
        query = f"""
        SELECT id, email, name, role, is_active, created_at
        FROM {self.schema}.users 
        WHERE email = :email
        """
        result = self.db.execute_read(query, {"email": email})
        row = result.fetchone()
        return row._asdict() if row else None
    
    def get_users_stats(self) -> dict:
        """Estatísticas de usuários (READ - query pesada)"""
        query = f"""
        SELECT 
            COUNT(*) as total_users,
            COUNT(*) FILTER (WHERE is_active = true) as active_users,
            COUNT(*) FILTER (WHERE created_at >= CURRENT_DATE - INTERVAL '30 days') as new_users_month,
            COUNT(DISTINCT role) as total_roles
        FROM {self.schema}.users
        """
        result = self.db.execute_read(query)
        return result.fetchone()._asdict()

# ========================================
# 4. CACHE DISTRIBUÍDO AVANÇADO
# ========================================

import redis.sentinel
import pickle
import zlib
from typing import Union

class DistributedCache:
    def __init__(self):
        # Redis Sentinel para alta disponibilidade
        sentinel = redis.sentinel.Sentinel([
            ('sentinel-1', 26379),
            ('sentinel-2', 26379),
            ('sentinel-3', 26379)
        ])
        
        self.master = sentinel.master_for('mymaster', socket_timeout=0.1)
        self.slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
    
    def get(self, key: str, use_slave: bool = True) -> Any:
        """Buscar do cache"""
        try:
            redis_conn = self.slave if use_slave else self.master
            data = redis_conn.get(key)
            if data:
                # Descomprimir e deserializar
                return pickle.loads(zlib.decompress(data))
            return None
        except Exception:
            return None
    
    def set(self, key: str, value: Any, ttl: int = 3600, compress: bool = True) -> bool:
        """Salvar no cache"""
        try:
            # Serializar e comprimir
            data = pickle.dumps(value)
            if compress and len(data) > 1024:  # Comprimir se > 1KB
                data = zlib.compress(data)
            
            return self.master.setex(key, ttl, data)
        except Exception:
            return False
    
    def invalidate_pattern(self, pattern: str):
        """Invalidar cache por padrão"""
        try:
            keys = self.master.keys(pattern)
            if keys:
                self.master.delete(*keys)
        except Exception:
            pass

# Cache inteligente com warming
class SmartCache:
    def __init__(self, cache: DistributedCache):
        self.cache = cache
    
    def get_or_compute(self, key: str, compute_func, ttl: int = 3600, 
                      warm_threshold: int = 300):
        """Cache com warming automático"""
        # Verificar cache
        result = self.cache.get(key)
        if result is not None:
            # Verificar se precisa warming (TTL baixo)
            remaining_ttl = self.cache.master.ttl(key)
            if remaining_ttl < warm_threshold:
                # Agendar warming em background
                self._schedule_warming(key, compute_func, ttl)
            return result
        
        # Cache miss - computar valor
        result = compute_func()
        self.cache.set(key, result, ttl)
        return result
    
    def _schedule_warming(self, key: str, compute_func, ttl: int):
        """Agendar warming em background (usar Celery em produção)"""
        import threading
        
        def warm_cache():
            try:
                result = compute_func()
                self.cache.set(key, result, ttl)
            except Exception:
                pass  # Log error
        
        thread = threading.Thread(target=warm_cache)
        thread.daemon = True
        thread.start()

# ========================================
# 5. MONITORAMENTO AVANÇADO
# ========================================

-- View para métricas de performance
CREATE OR REPLACE VIEW public.database_metrics AS
SELECT 
    'connections' as metric_name,
    COUNT(*) as value,
    CURRENT_TIMESTAMP as timestamp
FROM pg_stat_activity
WHERE state = 'active'

UNION ALL

SELECT 
    'slow_queries' as metric_name,
    COUNT(*) as value,
    CURRENT_TIMESTAMP as timestamp
FROM pg_stat_activity 
WHERE state = 'active' 
    AND query_start < CURRENT_TIMESTAMP - INTERVAL '5 seconds'

UNION ALL

SELECT 
    'database_size_mb' as metric_name,
    pg_database_size(current_database()) / 1024 / 1024 as value,
    CURRENT_TIMESTAMP as timestamp

UNION ALL

SELECT 
    'cache_hit_ratio' as metric_name,
    ROUND(
        100.0 * sum(blks_hit) / (sum(blks_hit) + sum(blks_read)), 2
    ) as value,
    CURRENT_TIMESTAMP as timestamp
FROM pg_stat_database;

# Python: Monitor de Performance
class DatabaseMonitor:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_connection_stats(self) -> dict:
        """Estatísticas de conexões"""
        query = """
        SELECT 
            state,
            COUNT(*) as count
        FROM pg_stat_activity 
        WHERE datname = current_database()
        GROUP BY state
        """
        result = self.db.execute(query).fetchall()
        return {row.state: row.count for row in result}
    
    def get_slow_queries(self, min_duration: int = 1000) -> List[dict]:
        """Queries lentas ativas"""
        query = """
        SELECT 
            pid,
            usename,
            datname,
            query,
            state,
            EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - query_start)) * 1000 as duration_ms
        FROM pg_stat_activity 
        WHERE state = 'active'
            AND query_start < CURRENT_TIMESTAMP - INTERVAL '%s milliseconds'
        ORDER BY query_start
        """ % min_duration
        
        result = self.db.execute(query).fetchall()
        return [row._asdict() for row in result]
    
    def get_table_bloat(self) -> List[dict]:
        """Detectar bloat nas tabelas"""
        query = """
        SELECT 
            schemaname,
            tablename,
            pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size,
            n_dead_tup,
            n_live_tup,
            ROUND(100.0 * n_dead_tup / (n_live_tup + n_dead_tup), 2) as dead_ratio
        FROM pg_stat_user_tables
        WHERE n_live_tup > 0
        ORDER BY dead_ratio DESC
        """
        result = self.db.execute(query).fetchall()
        return [row._asdict() for row in result]
    
    def get_index_usage(self) -> List[dict]:
        """Análise de uso dos índices"""
        query = """
        SELECT 
            schemaname,
            tablename,
            indexname,
            idx_tup_read,
            idx_tup_fetch,
            pg_size_pretty(pg_relation_size(indexrelname)) as index_size,
            CASE WHEN idx_tup_read = 0 THEN 'UNUSED' ELSE 'USED' END as status
        FROM pg_stat_user_indexes
        JOIN pg_stat_user_tables ON pg_stat_user_indexes.relid = pg_stat_user_tables.relid
        ORDER BY idx_tup_read DESC
        """
        result = self.db.execute(query).fetchall()
        return [row._asdict() for row in result]

# ========================================
# 6. BACKUP E DISASTER RECOVERY
# ========================================

#!/bin/bash
# Script de backup automático

BACKUP_DIR="/backups/postgresql"
DB_NAME="saas_production"
S3_BUCKET="empresa-db-backups"
RETENTION_DAYS=30

# Criar backup com pg_dump
echo "$(date): Iniciando backup de $DB_NAME"

pg_dump -h localhost -U postgres -d $DB_NAME \\
    --format=custom \\
    --compress=9 \\
    --verbose \\
    --file="$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).dump"

if [ $? -eq 0 ]; then
    echo "$(date): Backup concluído com sucesso"
    
    # Upload para S3
    aws s3 cp $BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).dump \\
        s3://$S3_BUCKET/daily/
    
    # Limpar backups antigos
    find $BACKUP_DIR -name "backup_*.dump" -mtime +$RETENTION_DAYS -delete
    
    echo "$(date): Backup enviado para S3 e limpeza concluída"
else
    echo "$(date): ERRO no backup!"
    # Enviar alerta (Slack, email, etc.)
fi

# Python: Backup Manager
class BackupManager:
    def __init__(self, db_config: dict, s3_config: dict):
        self.db_config = db_config
        self.s3_config = s3_config
    
    def create_logical_backup(self, tables: List[str] = None) -> str:
        """Criar backup lógico específico"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"logical_backup_{timestamp}.sql"
        
        cmd = [
            "pg_dump",
            f"--host={self.db_config['host']}",
            f"--username={self.db_config['user']}",
            f"--dbname={self.db_config['database']}",
            "--format=plain",
            "--inserts",
            f"--file={backup_file}"
        ]
        
        if tables:
            for table in tables:
                cmd.extend(["--table", table])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return backup_file
        else:
            raise Exception(f"Backup failed: {result.stderr}")
    
    def restore_from_backup(self, backup_file: str, target_db: str):
        """Restaurar backup"""
        cmd = [
            "pg_restore",
            f"--host={self.db_config['host']}",
            f"--username={self.db_config['user']}",
            f"--dbname={target_db}",
            "--clean",
            "--if-exists",
            backup_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise Exception(f"Restore failed: {result.stderr}")

print("🎯 PROJETO ENTERPRISE DATABASE ÉPICO:")
print("🏗️ 1. Arquitetura multi-tenant com isolamento")
print("📊 2. Sharding horizontal para escalabilidade")
print("🔄 3. Read/Write replicas com failover")
print("💾 4. Cache distribuído com Redis Sentinel")
print("📈 5. Monitoramento avançado de performance")
print("🛡️ 6. Backup automatizado e disaster recovery")
print("⚡ 7. Otimização contínua de queries")
print("🚀 8. Auto-scaling baseado em métricas")
print("")
print("🏆 ESTE É O NÍVEL DE UM DATABASE ARCHITECT!")
'''
        
        self.exemplo(codigo_projeto)
        
        print("\n🎊 CARACTERÍSTICAS DO PROJETO:")
        print("✅ Multi-tenant SaaS com isolamento completo")
        print("✅ Sharding horizontal para milhões de usuários")
        print("✅ Read/Write replicas com load balancing")
        print("✅ Cache distribuído com Redis Sentinel")
        print("✅ Monitoramento em tempo real")
        print("✅ Backup automatizado com retenção")
        print("✅ Disaster recovery testado")
        print("✅ Performance tuning automático")
        
        print("\n🚀 TECNOLOGIAS ENTERPRISE:")
        print("• 🗄️ PostgreSQL com extensões")
        print("• 🔄 Redis Sentinel para HA")
        print("• 📊 Prometheus + Grafana")
        print("• ☁️ AWS S3 para backups")
        print("• 🐳 Docker para isolamento")
        print("• 🔧 Ansible para automação")
        print("• 🚨 PagerDuty para alertas")
        print("• 📈 New Relic para APM")
        
        print("\n🎯 CASOS DE USO REAIS:")
        print("• 🏢 SaaS com 10.000+ tenants")
        print("• 📈 100M+ registros por dia")
        print("• ⚡ < 100ms response time")
        print("• 🔄 99.99% uptime")
        print("• 💾 Petabytes de dados")
        print("• 🌍 Deploy multi-região")
        
        # Registra conclusão do projeto
        self.complete_mini_project("Sistema Enterprise Database - Multi-tenant SaaS")
        
        print("\n🏆 PARABÉNS! Você dominou Database Design de nível ARCHITECT!")
        print("🎯 Este projeto demonstra expertise para:")
        print("• 💼 Database Architect")
        print("• 🏗️ Senior Database Engineer")
        print("• ☁️ Data Platform Engineer")
        print("• 🔧 Database Reliability Engineer (DBRE)")
        
        self.pausar()