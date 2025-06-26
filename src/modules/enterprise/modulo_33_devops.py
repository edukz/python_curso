#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 33: DevOps Completo - Docker, CI/CD e Cloud
Aprenda DevOps profissional: containerização, integração contínua e deploy em cloud
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Protocol, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid
from ..shared.base_module import BaseModule


class Modulo33DevOps(BaseModule):
    """Módulo 33: DevOps Completo - Docker, CI/CD e Cloud"""
    
    def __init__(self):
        super().__init__("modulo_33", "DevOps Completo - Docker, CI/CD e Cloud")
        self.has_mini_project = True
        self.mini_project_points = 150
    
    def execute(self) -> None:
        """Executa o módulo sobre DevOps"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            self.pausar()
            return
        
        try:
            self._devops_intro()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _devops_intro(self) -> None:
        """Conteúdo principal sobre DevOps"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MÓDULO 33: DEVOPS COMPLETO - DOCKER, CI/CD E CLOUD")
        else:
            print("\n" + "="*60)
            print("🚀 MÓDULO 33: DEVOPS COMPLETO - DOCKER, CI/CD E CLOUD")
            print("="*60)
        
        print("🎯 DevOps é fundamental para desenvolvimento moderno!")
        print("🛠️ Domine as ferramentas que empresas reais usam:")
        print("• 🐳 Docker para containerização")
        print("• ⚙️ CI/CD para automação")
        print("• ☁️ Cloud para deploy e escala")
        print("• 📊 Monitoramento e observabilidade")
        print("• 🔒 Segurança e compliance")
        print("• 🚀 DevSecOps e GitOps")
        
        self.pausar()
        
        self._docker_containerization()
        self._ci_cd_pipeline()
        self._cloud_deployment()
        self._mini_projeto_devops_pipeline()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _docker_containerization(self):
        """Docker e Containerização - Parte 1"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐳 DOCKER E CONTAINERIZAÇÃO")
        
        print("📦 Docker revolucionou o desenvolvimento de software!")
        print("🎯 Benefícios da containerização:")
        print("• ⚡ Portabilidade entre ambientes")
        print("• 🔒 Isolamento de aplicações")
        print("• 📈 Escalabilidade horizontal")
        print("• 🚀 Deploy rápido e consistente")
        print("• 💰 Otimização de recursos")
        
        codigo = '''# ========================================
# DOCKER FUNDAMENTALS
# ========================================

# 1. DOCKERFILE - Receita para criar imagem
# Dockerfile para aplicação Python Flask

FROM python:3.11-slim

# Metadados da imagem
LABEL maintainer="dev@empresa.com"
LABEL version="1.0"
LABEL description="API Python com Flask"

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar usuário não-root (segurança)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expor porta da aplicação
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]

# ========================================
# APLICAÇÃO FLASK EXEMPLO
# ========================================

# app.py
from flask import Flask, jsonify, request
import os
import redis
import json
from datetime import datetime
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Conectar ao Redis (se disponível)
try:
    redis_client = redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        decode_responses=True
    )
    redis_client.ping()
    logger.info("✅ Conectado ao Redis")
except:
    redis_client = None
    logger.warning("⚠️ Redis não disponível")

@app.route('/health')
def health_check():
    """Endpoint para verificação de saúde"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'redis': 'connected' if redis_client else 'disconnected'
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    """API para listar usuários"""
    if redis_client:
        # Tentar buscar do cache
        cached_users = redis_client.get('users')
        if cached_users:
            return jsonify(json.loads(cached_users))
    
    # Dados mock para exemplo
    users = [
        {'id': 1, 'name': 'João Silva', 'email': 'joao@email.com'},
        {'id': 2, 'name': 'Maria Santos', 'email': 'maria@email.com'},
        {'id': 3, 'name': 'Pedro Lima', 'email': 'pedro@email.com'}
    ]
    
    # Salvar no cache (se disponível)
    if redis_client:
        redis_client.setex('users', 300, json.dumps(users))
    
    return jsonify(users)

@app.route('/api/metrics')
def get_metrics():
    """Endpoint para métricas da aplicação"""
    import psutil
    
    return jsonify({
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

# ========================================
# REQUIREMENTS.TXT
# ========================================
"""
Flask==2.3.2
redis==4.6.0
psutil==5.9.5
gunicorn==21.2.0
"""

# ========================================
# DOCKER COMPOSE - ORQUESTRAÇÃO DE CONTAINERS
# ========================================

# docker-compose.yml
version: '3.8'

services:
  # Serviço da aplicação Python
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - PORT=5000
    depends_on:
      - redis
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
    networks:
      - app-network

  # Serviço Redis para cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped
    networks:
      - app-network

  # Nginx como proxy reverso
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web
    restart: unless-stopped
    networks:
      - app-network

  # Monitoramento com Prometheus
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    networks:
      - app-network

volumes:
  redis_data:

networks:
  app-network:
    driver: bridge

# ========================================
# COMANDOS DOCKER ESSENCIAIS
# ========================================

# Construir imagem
docker build -t minha-app:1.0 .

# Executar container
docker run -d -p 5000:5000 --name minha-app minha-app:1.0

# Ver containers rodando
docker ps

# Ver logs do container
docker logs minha-app

# Executar comando dentro do container
docker exec -it minha-app bash

# Parar container
docker stop minha-app

# Remover container
docker rm minha-app

# Usar Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# ========================================
# CONFIGURAÇÃO NGINX
# ========================================

# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream webapp {
        server web:5000;
    }

    server {
        listen 80;
        
        location / {
            proxy_pass http://webapp;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        
        location /health {
            proxy_pass http://webapp/health;
        }
    }
}

print("🐳 DOCKER EM AÇÃO:")
print("1. Dockerfile define a imagem")
print("2. Docker Compose orquestra múltiplos containers")
print("3. Nginx como proxy reverso")
print("4. Redis para cache e sessões")
print("5. Prometheus para monitoramento")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _ci_cd_pipeline(self):
        """CI/CD Pipeline - Parte 2"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚙️ CI/CD - INTEGRAÇÃO E ENTREGA CONTÍNUA")
        
        print("🔄 CI/CD automatiza todo o ciclo de desenvolvimento!")
        print("🎯 Benefícios da automação:")
        print("• ✨ Testes automáticos a cada commit")
        print("• 🚀 Deploy automático em produção")
        print("• 🔒 Verificações de segurança")
        print("• 📊 Qualidade de código garantida")
        print("• ⚡ Feedback rápido para desenvolvedores")
        
        codigo = '''# ========================================
# GITHUB ACTIONS - CI/CD PIPELINE
# ========================================

# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ========================================
  # JOB 1: TESTES E QUALIDADE DE CÓDIGO
  # ========================================
  test:
    runs-on: ubuntu-latest
    
    services:
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - name: 📥 Checkout do código
      uses: actions/checkout@v3

    - name: 🐍 Configurar Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        cache: 'pip'

    - name: 📦 Instalar dependências
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov flake8 black isort safety bandit

    - name: 🧹 Verificar formatação (Black)
      run: black --check .

    - name: 📝 Verificar importações (isort)
      run: isort --check-only .

    - name: 🔍 Análise estática (Flake8)
      run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

    - name: 🔒 Verificar vulnerabilidades (Safety)
      run: safety check

    - name: 🛡️ Análise de segurança (Bandit)
      run: bandit -r . -f json -o bandit-report.json

    - name: 🧪 Executar testes
      run: |
        pytest --cov=. --cov-report=xml --cov-report=html
      env:
        REDIS_HOST: localhost
        REDIS_PORT: 6379

    - name: 📊 Upload cobertura para Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  # ========================================
  # JOB 2: BUILD E PUSH DA IMAGEM DOCKER
  # ========================================
  build:
    needs: test
    runs-on: ubuntu-latest
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
    
    steps:
    - name: 📥 Checkout do código
      uses: actions/checkout@v3

    - name: 🔐 Login no Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: 📝 Extrair metadados
      id: meta
      uses: docker/metadata-action@v4
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=sha,prefix={{branch}}-

    - name: 🏗️ Build e Push da imagem
      id: build
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}

  # ========================================
  # JOB 3: DEPLOY EM STAGING
  # ========================================
  deploy-staging:
    if: github.ref == 'refs/heads/develop'
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    
    steps:
    - name: 🚀 Deploy para Staging
      run: |
        echo "Deploying to staging environment..."
        # Aqui você adicionaria comandos específicos do seu provedor
        # Exemplos: kubectl, terraform, ansible, etc.

  # ========================================
  # JOB 4: DEPLOY EM PRODUÇÃO
  # ========================================
  deploy-production:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    environment: production
    
    steps:
    - name: 🎯 Deploy para Produção
      run: |
        echo "Deploying to production environment..."
        # Deploy em produção com aprovação manual

# ========================================
# TESTES AUTOMATIZADOS
# ========================================

# tests/test_app.py
import pytest
import json
from app import app

@pytest.fixture
def client():
    """Cliente de teste para Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Teste do endpoint de saúde"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_get_users(client):
    """Teste da API de usuários"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'email' in data[0]

def test_metrics_endpoint(client):
    """Teste do endpoint de métricas"""
    response = client.get('/api/metrics')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'cpu_percent' in data
    assert 'memory_percent' in data

# ========================================
# CONFIGURAÇÃO PYTEST
# ========================================

# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --tb=short
    --strict-markers
    --cov-report=term-missing
    --cov-fail-under=80

# ========================================
# CONFIGURAÇÃO DE QUALIDADE DE CÓDIGO
# ========================================

# .flake8
[flake8]
max-line-length = 88
exclude = .git,__pycache__,venv
ignore = E203,W503

# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
multi_line_output = 3

print("⚙️ CI/CD EM AÇÃO:")
print("1. Testes automáticos a cada push")
print("2. Verificação de qualidade de código")
print("3. Análise de segurança")
print("4. Build automático da imagem Docker")
print("5. Deploy automático por ambiente")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _cloud_deployment(self):
        """Cloud e Deploy - Parte 3"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("☁️ CLOUD E DEPLOY EM PRODUÇÃO")
        
        print("🌩️ Deploy em cloud é essencial para aplicações modernas!")
        print("🎯 Estratégias de deploy:")
        print("• 🚀 Kubernetes para orquestração")
        print("• 📈 Auto-scaling baseado em demanda")
        print("• 🔄 Load balancing inteligente")
        print("• 📊 Monitoramento e observabilidade")
        print("• 🔒 Segurança e compliance")
        
        codigo = '''# ========================================
# KUBERNETES DEPLOYMENT
# ========================================

# k8s/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: minha-app
  labels:
    name: minha-app

---
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp-deployment
  namespace: minha-app
  labels:
    app: webapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        image: ghcr.io/usuario/minha-app:latest
        ports:
        - containerPort: 5000
        env:
        - name: REDIS_HOST
          value: "redis-service"
        - name: REDIS_PORT
          value: "6379"
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5

---
# k8s/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
  namespace: minha-app
spec:
  selector:
    app: webapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: ClusterIP

---
# k8s/redis.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-deployment
  namespace: minha-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 256Mi

---
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: minha-app
spec:
  selector:
    app: redis
  ports:
  - protocol: TCP
    port: 6379
    targetPort: 6379

---
# k8s/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-ingress
  namespace: minha-app
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - minha-app.exemplo.com
    secretName: webapp-tls
  rules:
  - host: minha-app.exemplo.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: webapp-service
            port:
              number: 80

# ========================================
# HORIZONTAL POD AUTOSCALER
# ========================================

# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: minha-app
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: webapp-deployment
  minReplicas: 2
  maxReplicas: 10
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

# ========================================
# TERRAFORM PARA INFRAESTRUTURA COMO CÓDIGO
# ========================================

# terraform/main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC e Networking
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "minha-app-vpc"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet ${count.index + 1}"
  }
}

# EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = "minha-app-cluster"
  role_arn = aws_iam_role.cluster.arn

  vpc_config {
    subnet_ids = aws_subnet.public[*].id
  }

  depends_on = [
    aws_iam_role_policy_attachment.cluster_policy,
  ]
}

# EKS Node Group
resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "main-nodes"
  node_role_arn   = aws_iam_role.node.arn
  subnet_ids      = aws_subnet.public[*].id

  scaling_config {
    desired_size = 2
    max_size     = 4
    min_size     = 1
  }

  instance_types = ["t3.medium"]

  depends_on = [
    aws_iam_role_policy_attachment.node_policy,
    aws_iam_role_policy_attachment.cni_policy,
    aws_iam_role_policy_attachment.registry_policy,
  ]
}

# ========================================
# MONITORAMENTO COM PROMETHEUS E GRAFANA
# ========================================

# monitoring/prometheus-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    
    scrape_configs:
    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)

    - job_name: 'minha-app'
      static_configs:
      - targets: ['webapp-service.minha-app.svc.cluster.local:80']
        labels:
          service: 'webapp'

---
# monitoring/grafana-dashboard.json
{
  "dashboard": {
    "title": "Minha App Dashboard",
    "panels": [
      {
        "title": "CPU Usage",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(container_cpu_usage_seconds_total[5m])",
            "legendFormat": "{{pod}}"
          }
        ]
      },
      {
        "title": "Memory Usage",
        "type": "graph", 
        "targets": [
          {
            "expr": "container_memory_usage_bytes",
            "legendFormat": "{{pod}}"
          }
        ]
      },
      {
        "title": "HTTP Requests",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{status}}"
          }
        ]
      }
    ]
  }
}

# ========================================
# SCRIPTS DE DEPLOY
# ========================================

#!/bin/bash
# scripts/deploy.sh

set -e

echo "🚀 Iniciando deploy da aplicação..."

# Variáveis
NAMESPACE="minha-app"
IMAGE_TAG=${1:-latest}
CLUSTER_NAME="minha-app-cluster"

# Verificar se kubectl está configurado
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ kubectl não está configurado"
    exit 1
fi

# Criar namespace se não existir
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# Aplicar configurações do Kubernetes
echo "📝 Aplicando configurações do Kubernetes..."
kubectl apply -f k8s/ -n $NAMESPACE

# Atualizar imagem do deployment
echo "🔄 Atualizando imagem para $IMAGE_TAG..."
kubectl set image deployment/webapp-deployment webapp=ghcr.io/usuario/minha-app:$IMAGE_TAG -n $NAMESPACE

# Aguardar rollout
echo "⏳ Aguardando rollout..."
kubectl rollout status deployment/webapp-deployment -n $NAMESPACE

# Verificar saúde da aplicação
echo "🏥 Verificando saúde da aplicação..."
EXTERNAL_IP=$(kubectl get service webapp-service -n $NAMESPACE -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

if [ ! -z "$EXTERNAL_IP" ]; then
    curl -f http://$EXTERNAL_IP/health || {
        echo "❌ Aplicação não está respondendo"
        exit 1
    }
    echo "✅ Deploy concluído com sucesso!"
    echo "🌐 Aplicação disponível em: http://$EXTERNAL_IP"
else
    echo "⚠️ IP externo ainda não disponível"
fi

print("☁️ CLOUD EM AÇÃO:")
print("1. Kubernetes para orquestração")
print("2. Auto-scaling baseado em CPU/Memória")
print("3. Load balancing automático")
print("4. Monitoramento com Prometheus/Grafana")
print("5. Infraestrutura como código com Terraform")
'''
        
        self.exemplo(codigo)
        self.pausar()
    
    def _mini_projeto_devops_pipeline(self):
        """Mini Projeto - Pipeline DevOps Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI-PROJETO: PIPELINE DEVOPS COMPLETO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI-PROJETO: PIPELINE DEVOPS COMPLETO")
            print("="*50)
        
        print("🚀 DESAFIO ÉPICO: Criar um pipeline DevOps do zero ao deploy!")
        print("🏆 Este projeto integra TODOS os conceitos de DevOps moderno!")
        
        self.pausar()
        
        print("\n🎯 OBJETIVOS DO PROJETO:")
        print("✅ Aplicação web com API REST")
        print("✅ Containerização com Docker")
        print("✅ Pipeline CI/CD com GitHub Actions")
        print("✅ Testes automatizados")
        print("✅ Deploy em Kubernetes")
        print("✅ Monitoramento e métricas")
        print("✅ Segurança e compliance")
        
        codigo_projeto = '''# ========================================
# PROJETO DEVOPS COMPLETO
# E-COMMERCE MICROSERVICES COM FULL DEVOPS
# ========================================

# Estrutura do projeto:
"""
ecommerce-devops/
├── services/
│   ├── user-service/          # Microserviço de usuários
│   ├── product-service/       # Microserviço de produtos
│   ├── order-service/         # Microserviço de pedidos
│   └── api-gateway/           # Gateway principal
├── infrastructure/
│   ├── terraform/             # Infraestrutura como código
│   ├── kubernetes/            # Manifestos K8s
│   └── monitoring/            # Prometheus/Grafana
├── .github/workflows/         # CI/CD pipelines
├── docker-compose.yml         # Desenvolvimento local
└── README.md
"""

# ========================================
# 1. MICROSERVIÇO DE USUÁRIOS
# ========================================

# services/user-service/app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import os
from datetime import datetime, timedelta
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://user:pass@localhost/users'
)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')

db = SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'user-service'})

@app.route('/api/users/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email já cadastrado'}), 400
    
    user = User(
        email=data['email'],
        name=data['name'],
        password_hash=generate_password_hash(data['password'])
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'Usuário criado com sucesso'}), 201

@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'error': 'Credenciais inválidas'}), 401

# services/user-service/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]

# ========================================
# 2. MICROSERVIÇO DE PRODUTOS
# ========================================

# services/product-service/app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import logging
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://user:pass@localhost/products'
)

db = SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'product-service'})

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.filter_by(active=True).all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': float(p.price),
        'stock': p.stock,
        'category': p.category
    } for p in products])

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data.get('stock', 0),
        category=data.get('category', 'general')
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({'message': 'Produto criado com sucesso'}), 201

# ========================================
# 3. API GATEWAY
# ========================================

# services/api-gateway/app.py
from flask import Flask, request, jsonify
import requests
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# URLs dos microserviços
USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user-service:5001')
PRODUCT_SERVICE_URL = os.getenv('PRODUCT_SERVICE_URL', 'http://product-service:5002')
ORDER_SERVICE_URL = os.getenv('ORDER_SERVICE_URL', 'http://order-service:5003')

@app.route('/health')
def health():
    # Verificar saúde de todos os serviços
    services_health = {}
    
    try:
        resp = requests.get(f'{USER_SERVICE_URL}/health', timeout=5)
        services_health['user-service'] = resp.json()
    except:
        services_health['user-service'] = {'status': 'unhealthy'}
    
    try:
        resp = requests.get(f'{PRODUCT_SERVICE_URL}/health', timeout=5)
        services_health['product-service'] = resp.json()
    except:
        services_health['product-service'] = {'status': 'unhealthy'}
    
    return jsonify({
        'status': 'healthy',
        'service': 'api-gateway',
        'services': services_health
    })

@app.route('/api/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_users(path):
    url = f'{USER_SERVICE_URL}/api/users/{path}'
    return proxy_request(url)

@app.route('/api/products/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_products(path):
    url = f'{PRODUCT_SERVICE_URL}/api/products/{path}'
    return proxy_request(url)

def proxy_request(url):
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers=dict(request.headers),
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=30
        )
        
        return resp.content, resp.status_code, resp.headers.items()
    
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Service timeout'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Service unavailable'}), 503

# ========================================
# 4. PIPELINE CI/CD AVANÇADO
# ========================================

# .github/workflows/microservices-ci-cd.yml
name: Microservices CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_PREFIX: ${{ github.repository }}/

jobs:
  # ========================================
  # DETECTAR MUDANÇAS EM SERVIÇOS
  # ========================================
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      user-service: ${{ steps.changes.outputs.user-service }}
      product-service: ${{ steps.changes.outputs.product-service }}
      api-gateway: ${{ steps.changes.outputs.api-gateway }}
    steps:
    - uses: actions/checkout@v3
    - uses: dorny/paths-filter@v2
      id: changes
      with:
        filters: |
          user-service:
            - 'services/user-service/**'
          product-service:
            - 'services/product-service/**'
          api-gateway:
            - 'services/api-gateway/**'

  # ========================================
  # TESTES E BUILD PARALELO POR SERVIÇO
  # ========================================
  build-user-service:
    needs: detect-changes
    if: needs.detect-changes.outputs.user-service == 'true'
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: 🧪 Testes do User Service
      run: |
        cd services/user-service
        pip install -r requirements.txt
        pytest tests/ --cov=. --cov-report=xml
    
    - name: 🐳 Build e Push User Service
      uses: docker/build-push-action@v4
      with:
        context: services/user-service
        push: true
        tags: ${{ env.REGISTRY }}${{ env.IMAGE_PREFIX }}user-service:${{ github.sha }}

  build-product-service:
    needs: detect-changes
    if: needs.detect-changes.outputs.product-service == 'true'
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: 🧪 Testes do Product Service
      run: |
        cd services/product-service
        pip install -r requirements.txt
        pytest tests/ --cov=. --cov-report=xml
    
    - name: 🐳 Build e Push Product Service
      uses: docker/build-push-action@v4
      with:
        context: services/product-service
        push: true
        tags: ${{ env.REGISTRY }}${{ env.IMAGE_PREFIX }}product-service:${{ github.sha }}

  # ========================================
  # TESTES DE INTEGRAÇÃO
  # ========================================
  integration-tests:
    needs: [build-user-service, build-product-service]
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: 🚀 Subir ambiente de teste
      run: |
        docker-compose -f docker-compose.test.yml up -d
        sleep 30  # Aguardar serviços subirem
    
    - name: 🧪 Executar testes de integração
      run: |
        pytest tests/integration/ --verbose
    
    - name: 📊 Testes de carga com K6
      run: |
        docker run --rm -i grafana/k6 run - <tests/load/api-test.js

  # ========================================
  # ANÁLISE DE SEGURANÇA
  # ========================================
  security-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: 🔒 Scan de vulnerabilidades
      uses: anchore/scan-action@v3
      with:
        image: ${{ env.REGISTRY }}${{ env.IMAGE_PREFIX }}user-service:${{ github.sha }}
    
    - name: 🛡️ Análise de código com CodeQL
      uses: github/codeql-action/analyze@v2

  # ========================================
  # DEPLOY STAGING
  # ========================================
  deploy-staging:
    if: github.ref == 'refs/heads/develop'
    needs: [integration-tests, security-scan]
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - name: 🚀 Deploy para Staging
      run: |
        echo "Deploying to staging with GitOps..."
        # Atualizar manifesto no repositório GitOps
        
  # ========================================
  # DEPLOY PRODUÇÃO COM CANARY
  # ========================================
  deploy-production:
    if: github.ref == 'refs/heads/main'
    needs: [integration-tests, security-scan]
    runs-on: ubuntu-latest
    environment: production
    steps:
    - name: 🎯 Canary Deploy
      run: |
        # Deploy canário com 10% do tráfego
        kubectl patch deployment user-service \\
          -p '{"spec":{"template":{"spec":{"containers":[{"name":"user-service","image":"'${{ env.REGISTRY }}${{ env.IMAGE_PREFIX }}user-service:${{ github.sha }}'"}]}}}}'
        
        # Aguardar métricas
        sleep 300
        
        # Se métricas OK, deploy completo
        kubectl scale deployment user-service-canary --replicas=0

# ========================================
# 5. MONITORAMENTO AVANÇADO
# ========================================

# monitoring/prometheus-rules.yml
groups:
- name: ecommerce.rules
  rules:
  - alert: ServiceDown
    expr: up == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Service {{ $labels.job }} is down"
      
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High error rate on {{ $labels.service }}"
      
  - alert: HighLatency
    expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High latency on {{ $labels.service }}"

print("🎯 PROJETO DEVOPS ÉPICO:")
print("🏗️ 1. Arquitetura de microserviços")
print("🐳 2. Containerização completa")
print("⚙️ 3. CI/CD com deploy canário")
print("🧪 4. Testes automatizados (unit + integration + load)")
print("🔒 5. Análise de segurança automática")
print("☁️ 6. Kubernetes com auto-scaling")
print("📊 7. Monitoramento full-stack")
print("🚨 8. Alertas inteligentes")
print("📈 9. Métricas de negócio")
print("🔄 10. GitOps para deploy")
print("")
print("🏆 ESTE É O NÍVEL DE UM SENIOR DEVOPS ENGINEER!")
'''
        
        self.exemplo(codigo_projeto)
        
        print("\n🎊 CARACTERÍSTICAS DO PROJETO:")
        print("✅ Microserviços em Python/Flask")
        print("✅ API Gateway para roteamento")
        print("✅ Banco PostgreSQL por serviço")
        print("✅ Redis para cache distribuído")
        print("✅ Docker Compose para desenvolvimento")
        print("✅ Kubernetes para produção")
        print("✅ Pipeline CI/CD com GitHub Actions")
        print("✅ Testes automatizados em 3 níveis")
        print("✅ Deploy canário para zero downtime")
        print("✅ Monitoramento com Prometheus/Grafana")
        print("✅ Alertas inteligentes")
        print("✅ Logs centralizados")
        print("✅ Métricas de negócio")
        
        print("\n🚀 TECNOLOGIAS ENTERPRISE:")
        print("• 🐳 Docker & Docker Compose")
        print("• ☸️ Kubernetes")
        print("• ⚙️ GitHub Actions")
        print("• 🏗️ Terraform")
        print("• 📊 Prometheus & Grafana")
        print("• 🔍 Jaeger (tracing)")
        print("• 📝 ELK Stack (logs)")
        print("• 🔒 OWASP ZAP (security)")
        print("• 🧪 Jest & K6 (testing)")
        print("• 🌐 Nginx (load balancer)")
        
        # Registra conclusão do projeto
        self.complete_mini_project("Pipeline DevOps Completo - E-commerce Microservices")
        
        print("\n🏆 PARABÉNS! Você dominou DevOps de nível SENIOR!")
        print("🎯 Este projeto demonstra capacidade técnica para:")
        print("• 💼 Senior DevOps Engineer")
        print("• 🏗️ Platform Engineer")
        print("• ☁️ Cloud Architect")
        print("• 🔧 Site Reliability Engineer (SRE)")
        
        self.pausar()
