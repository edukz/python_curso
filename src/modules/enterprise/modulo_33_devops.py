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
        """Executa o módulo DevOps Completo"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._devops_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _devops_principal(self) -> None:
        """Conteúdo principal do módulo DevOps"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MÓDULO 33: DEVOPS COMPLETO - DOCKER, CI/CD E CLOUD")
        else:
            print("\n" + "="*50)
            print("🚀 MÓDULO 33: DEVOPS COMPLETO - DOCKER, CI/CD E CLOUD")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🚀 Bem-vindo ao mundo DevOps! Vamos automatizar tudo e fazer deploy como os gigantes da tecnologia!")
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
            self._mini_projeto_pipeline_completo()
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
                'id': 'secao_o_que_e_devops',
                'titulo': '🎯 O que é DevOps?',
                'descricao': 'Entenda a cultura e práticas DevOps',
                'funcao': self._secao_o_que_e_devops
            },
            {
                'id': 'secao_docker_containerizacao',
                'titulo': '🐳 Docker e Containerização',
                'descricao': 'Aprenda a criar e gerenciar containers',
                'funcao': self._secao_docker_containerizacao
            },
            {
                'id': 'secao_ci_cd_pipelines',
                'titulo': '⚙️ CI/CD e Pipelines',
                'descricao': 'Automatize builds, testes e deploys',
                'funcao': self._secao_ci_cd_pipelines
            },
            {
                'id': 'secao_kubernetes_orquestracao',
                'titulo': '☸️ Kubernetes e Orquestração',
                'descricao': 'Gerencie containers em escala',
                'funcao': self._secao_kubernetes_orquestracao
            },
            {
                'id': 'secao_cloud_providers',
                'titulo': '☁️ Cloud Computing',
                'descricao': 'AWS, Azure, GCP - Deploy em nuvem',
                'funcao': self._secao_cloud_providers
            },
            {
                'id': 'secao_monitoramento_observabilidade',
                'titulo': '📊 Monitoramento e Observabilidade',
                'descricao': 'Métricas, logs e alertas',
                'funcao': self._secao_monitoramento_observabilidade
            },
            {
                'id': 'secao_seguranca_devsecops',
                'titulo': '🔒 DevSecOps',
                'descricao': 'Segurança integrada ao pipeline',
                'funcao': self._secao_seguranca_devsecops
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
    
    def _secao_o_que_e_devops(self) -> None:
        """Seção: O que é DevOps?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É DEVOPS?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "DevOps",
            "Uma cultura que une Desenvolvimento (Dev) e Operações (Ops) para entregar software mais rápido e com mais qualidade"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("DevOps não é apenas sobre ferramentas - é uma mudança de mentalidade!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("DevOps é como uma linha de montagem moderna: cada parte do processo é automatizada, testada e integrada para entregar o produto final rapidamente e sem defeitos.", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PRINCÍPIOS FUNDAMENTAIS ===
        self.print_colored("\n🔧 PRINCÍPIOS DEVOPS:", "info")
        principios = [
            "1. 🤝 COLABORAÇÃO: Desenvolvedores e operações trabalham juntos",
            "2. 🔄 AUTOMAÇÃO: Tudo que pode ser automatizado, deve ser",
            "3. 📊 MEDIÇÃO: Métricas para tudo - performance, erros, deploys",
            "4. 🚀 ENTREGA CONTÍNUA: Deploy várias vezes ao dia",
            "5. 🔍 FEEDBACK RÁPIDO: Problemas são detectados e corrigidos rapidamente"
        ]
        
        for i, principio in enumerate(principios, 1):
            self.print_colored(principio, "text")
            if i < len(principios):
                input("   ⏳ Pressione ENTER para o próximo princípio...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO DE FLUXO DEVOPS:", "success")
        exemplo_fluxo = '''# FLUXO DEVOPS TÍPICO:

1. DESENVOLVEDOR faz commit do código
   ↓
2. PIPELINE CI é acionado automaticamente
   ↓
3. TESTES automatizados são executados
   ↓
4. BUILD da aplicação é criado
   ↓
5. DEPLOY automático em staging
   ↓
6. TESTES DE ACEITAÇÃO são executados
   ↓
7. DEPLOY em produção (manual ou automático)
   ↓
8. MONITORAMENTO contínuo da aplicação'''
        self.exemplo(exemplo_fluxo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE DEVOPS É USADO:", "accent")
        aplicacoes = [
            "Netflix: Deploy milhares de vezes por dia",
            "Amazon: Uma mudança em produção a cada 11.6 segundos",
            "Facebook: Deploy contínuo com zero downtime",
            "Google: Bilhões de builds por ano automatizados"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_docker_containerizacao(self) -> None:
        """Seção: Docker e Containerização"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DOCKER E CONTAINERIZAÇÃO", "🐳", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Container",
            "Um pacote leve e portátil que contém tudo necessário para executar uma aplicação: código, runtime, bibliotecas e configurações"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Containers são como contêineres de navio: padronizados, portáteis e podem ser transportados para qualquer lugar sem se preocupar com o conteúdo interno!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === VANTAGENS DO DOCKER ===
        self.print_colored("\n✨ POR QUE USAR DOCKER?", "success")
        vantagens = [
            "⚡ VELOCIDADE: Containers iniciam em segundos",
            "📦 PORTABILIDADE: Funciona em qualquer lugar",
            "🔒 ISOLAMENTO: Cada app em seu próprio ambiente",
            "💰 ECONOMIA: Usa menos recursos que VMs",
            "🎯 CONSISTÊNCIA: Mesmo ambiente em dev e prod"
        ]
        
        for vantagem in vantagens:
            self.print_colored(vantagem, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 DOCKERFILE EXEMPLO:", "success")
        dockerfile_exemplo = '''# Dockerfile para uma aplicação Python

# Imagem base
FROM python:3.11-slim

# Informações do mantenedor
LABEL maintainer="seu-email@exemplo.com"

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos de requisitos
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "app.py"]'''
        self.exemplo(dockerfile_exemplo)
        
        # === COMANDOS ESSENCIAIS ===
        self.print_colored("\n🔧 COMANDOS DOCKER ESSENCIAIS:", "info")
        comandos = '''# Construir uma imagem
docker build -t minha-app:1.0 .

# Executar um container
docker run -d -p 8000:8000 minha-app:1.0

# Listar containers rodando
docker ps

# Ver logs
docker logs <container-id>

# Parar container
docker stop <container-id>'''
        self.exemplo(comandos)
        
        self.pausar()
    
    def _secao_ci_cd_pipelines(self) -> None:
        """Seção: CI/CD e Pipelines"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CI/CD E PIPELINES", "⚙️", "success")
        
        # === CONCEITOS ===
        self.print_concept(
            "CI (Continuous Integration)",
            "Prática de integrar código frequentemente, com builds e testes automatizados"
        )
        
        self.print_concept(
            "CD (Continuous Delivery/Deployment)",
            "Entrega automática de código testado para ambientes de staging/produção"
        )
        
        # === BENEFÍCIOS ===
        self.print_colored("\n🎯 BENEFÍCIOS DO CI/CD:", "info")
        beneficios = [
            "✅ Detecção rápida de bugs",
            "🚀 Deploy mais frequente e confiável",
            "📊 Feedback imediato sobre qualidade",
            "⏱️ Redução do time-to-market",
            "😌 Menos stress em releases"
        ]
        
        for beneficio in beneficios:
            self.print_colored(f"  {beneficio}", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO DE PIPELINE ===
        self.print_colored("\n💻 EXEMPLO DE PIPELINE CI/CD:", "success")
        pipeline_exemplo = '''# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest flake8
    
    - name: Run tests
      run: pytest
    
    - name: Lint code
      run: flake8 .
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: docker build -t app:${{ github.sha }} .
    
    - name: Push to registry
      run: docker push app:${{ github.sha }}
  
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to production
      run: |
        echo "Deploying to production..."
        # kubectl apply -f k8s/'''
        
        self.exemplo(pipeline_exemplo)
        
        # === FERRAMENTAS POPULARES ===
        self.print_colored("\n🛠️ FERRAMENTAS CI/CD POPULARES:", "accent")
        ferramentas = [
            "GitHub Actions - Integrado ao GitHub",
            "Jenkins - Open source e extensível",
            "GitLab CI - Integrado ao GitLab",
            "CircleCI - Cloud-based e rápido",
            "Travis CI - Simples e eficiente"
        ]
        
        for ferramenta in ferramentas:
            self.print_colored(f"• {ferramenta}", "primary")
        
        self.pausar()
    
    def _secao_kubernetes_orquestracao(self) -> None:
        """Seção: Kubernetes e Orquestração"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("KUBERNETES E ORQUESTRAÇÃO", "☸️", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Kubernetes (K8s)",
            "Sistema de orquestração de containers que automatiza deploy, escalonamento e gerenciamento de aplicações containerizadas"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Kubernetes é como um maestro de orquestra: coordena todos os músicos (containers) para tocar em harmonia, substituindo músicos doentes (containers com falha) automaticamente!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === RECURSOS PRINCIPAIS ===
        self.print_colored("\n🔧 RECURSOS DO KUBERNETES:", "info")
        recursos = [
            "🔄 AUTO-SCALING: Ajusta recursos baseado na demanda",
            "🏥 SELF-HEALING: Reinicia containers com falha",
            "🎯 LOAD BALANCING: Distribui tráfego entre containers",
            "🔐 SECRETS MANAGEMENT: Gerencia dados sensíveis",
            "📦 ROLLING UPDATES: Atualiza sem downtime"
        ]
        
        for recurso in recursos:
            self.print_colored(recurso, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO DE MANIFESTO ===
        self.print_colored("\n💻 EXEMPLO DE DEPLOYMENT:", "success")
        k8s_exemplo = '''# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: minha-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: minha-app
  template:
    metadata:
      labels:
        app: minha-app
    spec:
      containers:
      - name: app
        image: minha-app:1.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: minha-app-service
spec:
  selector:
    app: minha-app
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer'''
        
        self.exemplo(k8s_exemplo)
        
        self.pausar()
    
    def _secao_cloud_providers(self) -> None:
        """Seção: Cloud Computing"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CLOUD COMPUTING", "☁️", "info")
        
        # === CONCEITOS ===
        self.print_concept(
            "Cloud Computing",
            "Entrega de recursos de computação sob demanda através da internet, com pagamento conforme o uso"
        )
        
        # === MODELOS DE SERVIÇO ===
        self.print_colored("\n📊 MODELOS DE CLOUD:", "warning")
        modelos = [
            "💻 IaaS (Infrastructure as a Service): Servidores virtuais, storage",
            "🔧 PaaS (Platform as a Service): Ambientes de desenvolvimento",
            "📱 SaaS (Software as a Service): Aplicações prontas para uso"
        ]
        
        for modelo in modelos:
            self.print_colored(modelo, "text")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PRINCIPAIS PROVEDORES ===
        self.print_colored("\n🌟 PRINCIPAIS PROVEDORES:", "success")
        
        self.print_colored("\n1️⃣ AWS (Amazon Web Services):", "accent")
        self.print_colored("   • Líder de mercado", "text")
        self.print_colored("   • Maior variedade de serviços", "text")
        self.print_colored("   • EC2, S3, Lambda, RDS", "text")
        
        self.print_colored("\n2️⃣ Microsoft Azure:", "accent")
        self.print_colored("   • Integração com produtos Microsoft", "text")
        self.print_colored("   • Forte em empresas", "text")
        self.print_colored("   • VMs, App Service, Functions", "text")
        
        self.print_colored("\n3️⃣ Google Cloud Platform:", "accent")
        self.print_colored("   • Forte em Big Data e ML", "text")
        self.print_colored("   • Kubernetes nativo", "text")
        self.print_colored("   • Compute Engine, Cloud Run", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO TERRAFORM ===
        self.print_colored("\n💻 EXEMPLO DE INFRAESTRUTURA COMO CÓDIGO:", "success")
        terraform_exemplo = '''# main.tf - Criar VM na AWS
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
  
  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y nginx
    systemctl start nginx
  EOF
}

output "public_ip" {
  value = aws_instance.web_server.public_ip
}'''
        
        self.exemplo(terraform_exemplo)
        
        self.pausar()
    
    def _secao_monitoramento_observabilidade(self) -> None:
        """Seção: Monitoramento e Observabilidade"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MONITORAMENTO E OBSERVABILIDADE", "📊", "success")
        
        # === CONCEITOS ===
        self.print_concept(
            "Observabilidade",
            "Capacidade de entender o estado interno de um sistema através de suas saídas externas"
        )
        
        # === OS 3 PILARES ===
        self.print_colored("\n🏛️ OS 3 PILARES DA OBSERVABILIDADE:", "warning")
        pilares = [
            "📊 MÉTRICAS: Dados numéricos sobre o sistema (CPU, memória, latência)",
            "📝 LOGS: Registros detalhados de eventos",
            "🔍 TRACES: Rastreamento de requisições através do sistema"
        ]
        
        for pilar in pilares:
            self.print_colored(pilar, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === STACK DE MONITORAMENTO ===
        self.print_colored("\n🛠️ STACK POPULAR:", "info")
        self.print_colored("• Prometheus: Coleta de métricas", "text")
        self.print_colored("• Grafana: Visualização de dados", "text")
        self.print_colored("• ELK Stack: Logs (Elasticsearch, Logstash, Kibana)", "text")
        self.print_colored("• Jaeger: Distributed tracing", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO PROMETHEUS ===
        self.print_colored("\n💻 EXEMPLO DE ALERTA:", "success")
        prometheus_exemplo = '''# prometheus-rules.yml
groups:
- name: example
  rules:
  - alert: HighMemoryUsage
    expr: (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes > 0.9
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High memory usage detected"
      description: "Memory usage is above 90% (current value: {{ $value }})"
  
  - alert: ServiceDown
    expr: up == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Service {{ $labels.job }} is down"'''
        
        self.exemplo(prometheus_exemplo)
        
        self.pausar()
    
    def _secao_seguranca_devsecops(self) -> None:
        """Seção: DevSecOps"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DEVSECOPS", "🔒", "error")
        
        # === CONCEITO ===
        self.print_concept(
            "DevSecOps",
            "Integração de práticas de segurança em todas as fases do desenvolvimento e operações"
        )
        
        # === SHIFT LEFT ===
        self.print_colored("\n⬅️ SHIFT LEFT SECURITY:", "warning")
        self.print_colored("Mover a segurança para o início do ciclo de desenvolvimento, não apenas no final!", "text")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PRÁTICAS DEVSECOPS ===
        self.print_colored("\n🛡️ PRÁTICAS ESSENCIAIS:", "info")
        praticas = [
            "🔍 SAST: Análise estática de código",
            "🧪 DAST: Testes dinâmicos de segurança",
            "📦 SCA: Análise de dependências",
            "🐳 Container scanning",
            "🔐 Secrets management",
            "📋 Compliance as code"
        ]
        
        for pratica in praticas:
            self.print_colored(pratica, "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO DE PIPELINE SEGURO ===
        self.print_colored("\n💻 PIPELINE COM SEGURANÇA:", "success")
        security_pipeline = '''# .github/workflows/security.yml
name: Security Pipeline

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    # Análise de código estático
    - name: Run Bandit (Python Security)
      run: |
        pip install bandit
        bandit -r . -f json -o bandit-report.json
    
    # Scan de dependências
    - name: Check dependencies
      run: |
        pip install safety
        safety check
    
    # Scan de secrets
    - name: Scan for secrets
      uses: trufflesecurity/trufflehog@main
      with:
        path: ./
    
    # Container scan
    - name: Scan Docker image
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: 'myapp:latest'
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    # Upload results
    - name: Upload SARIF results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif' '''
        
        self.exemplo(security_pipeline)
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar seus conhecimentos DevOps com exercícios práticos!", "text")
        
        # === INSTRUÇÕES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")
        
        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Conhecimentos DevOps',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'O que significa CI/CD?',
                        'answer': ['continuous integration continuous delivery', 'continuous integration continuous deployment', 'integração contínua entrega contínua'],
                        'hint': 'CI = Integração Contínua, CD = Entrega/Deploy Contínuo'
                    },
                    {
                        'question': 'Qual comando Docker cria uma imagem?',
                        'answer': ['docker build', 'build'],
                        'hint': 'Comando que "constrói" a imagem a partir do Dockerfile'
                    },
                    {
                        'question': 'Qual porta padrão o Kubernetes API server usa?',
                        'answer': ['6443', 'porta 6443'],
                        'hint': 'É uma porta na faixa 6000+'
                    },
                    {
                        'question': 'Qual é o nome do arquivo de configuração do Docker Compose?',
                        'answer': ['docker-compose.yml', 'docker-compose.yaml', 'compose.yml', 'compose.yaml'],
                        'hint': 'docker-compose seguido de uma extensão YAML'
                    },
                    {
                        'question': 'O que é um Pod no Kubernetes?',
                        'answer': ['menor unidade', 'unidade mínima', 'grupo de containers', 'conjunto de containers'],
                        'hint': 'É a menor unidade que pode ser criada no K8s'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o Dockerfile para uma aplicação Python',
                        'starter': '''FROM python:3.11-slim
WORKDIR /app
# Complete: copie o arquivo requirements.txt

# Complete: instale as dependências

COPY . .
EXPOSE 8000
CMD ["python", "app.py"]''',
                        'solution': '''COPY requirements.txt .
RUN pip install -r requirements.txt''',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o docker-compose.yml',
                        'starter': '''version: '3.8'
services:
  web:
    build: .
    # Complete: mapeie a porta 8000 do container para 8000 do host
    
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    # Complete: defina que depende do serviço 'db'
    
  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=pass''',
                        'solution': '''ports:
      - "8000:8000"
    depends_on:
      - db''',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o deployment Kubernetes',
                        'starter': '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  # Complete: defina 3 réplicas
  
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: app
        image: myapp:1.0
        # Complete: defina recursos (100m CPU, 128Mi memória)''',
                        'solution': '''replicas: 3
        resources:
          requests:
            cpu: 100m
            memory: 128Mi''',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Crie seu Pipeline DevOps',
                'type': 'creative',
                'instruction': 'Crie um pipeline CI/CD completo para uma aplicação simples. Inclua: build, testes, análise de segurança e deploy. Use GitHub Actions, GitLab CI ou qualquer ferramenta que preferir!'
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
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre DevOps",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um pipeline completo",
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
    
    def _run_quiz(self, quiz_data: Dict[str, Any]) -> None:
        """Executa o quiz interativo"""
        self.print_section(quiz_data['title'], "📝", "info")
        
        score = 0
        total = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\nPergunta {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            attempts = 0
            max_attempts = 3
            
            while attempts < max_attempts:
                try:
                    resposta = input("\n👉 Sua resposta: ").strip().lower()
                    
                    if any(ans.lower() in resposta or resposta in ans.lower() 
                          for ans in q['answer']):
                        self.print_success("✅ Correto!")
                        score += 1
                        break
                    else:
                        attempts += 1
                        if attempts < max_attempts:
                            self.print_warning(f"❌ Incorreto. Tentativas restantes: {max_attempts - attempts}")
                            if attempts == 2:
                                self.print_tip(f"💡 Dica: {q['hint']}")
                        else:
                            self.print_warning(f"❌ Resposta correta: {q['answer'][0]}")
                
                except KeyboardInterrupt:
                    raise
                except Exception:
                    self.print_warning("❌ Resposta inválida. Tente novamente.")
        
        # Resultado final
        percentage = (score / total) * 100
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        self.print_colored(f"Você acertou {score} de {total} perguntas ({percentage:.0f}%)", "info")
        
        if percentage >= 80:
            self.print_success("🌟 Excelente! Você domina DevOps!")
        elif percentage >= 60:
            self.print_colored("👍 Bom trabalho! Continue praticando!", "warning")
        else:
            self.print_colored("💪 Continue estudando! DevOps requer prática!", "text")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _run_code_completion(self, exercise_data: Dict[str, Any]) -> None:
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "info")
        
        for ex in exercise_data['exercises']:
            self.print_colored(f"\n{'='*50}", "text")
            self.print_colored(f"📝 {ex['instruction']}", "warning")
            self.print_colored("\nCódigo inicial:", "text")
            self.exemplo(ex['starter'])
            
            self.print_colored("\n✏️ Digite sua solução (ou 'pular' para próximo):", "info")
            
            try:
                solucao = []
                print("(Digite 'fim' quando terminar)")
                while True:
                    linha = input()
                    if linha.lower() == 'fim':
                        break
                    if linha.lower() == 'pular':
                        self.print_warning("⏭️ Pulando para próximo exercício...")
                        break
                    solucao.append(linha)
                
                if linha.lower() != 'pular' and solucao:
                    # Mostra solução esperada
                    self.print_colored("\n✅ Solução esperada:", "success")
                    self.exemplo(ex['solution'])
                    
                    # Feedback baseado no tipo
                    if ex['type'] == 'simple':
                        self.print_tip("💡 Dica: Sempre copie dependências antes de instalar!")
                    elif ex['type'] == 'intermediate':
                        self.print_tip("💡 Dica: depends_on garante ordem de inicialização!")
                    else:
                        self.print_tip("💡 Dica: Recursos limitam uso de CPU/memória!")
                
                input("\n🔸 Pressione ENTER para continuar...")
                
            except KeyboardInterrupt:
                raise
            except Exception:
                self.print_warning("❌ Erro ao processar resposta.")
    
    def _run_creative_exercise(self, exercise_data: Dict[str, Any]) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "success")
        
        self.print_colored(f"\n📋 {exercise_data['instruction']}", "warning")
        
        self.print_colored("\n💡 SUGESTÕES PARA SEU PIPELINE:", "info")
        sugestoes = [
            "• Use múltiplos stages: build, test, security, deploy",
            "• Inclua testes unitários e de integração",
            "• Adicione scanning de vulnerabilidades",
            "• Configure diferentes ambientes (dev, staging, prod)",
            "• Implemente rollback automático",
            "• Adicione notificações (Slack, email)",
            "• Use cache para acelerar builds",
            "• Implemente aprovação manual para produção"
        ]
        
        for sugestao in sugestoes:
            self.print_colored(sugestao, "text")
        
        self.print_colored("\n🎯 EXEMPLO DE ESTRUTURA:", "success")
        exemplo_pipeline = '''name: Complete DevOps Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # 1. Build & Test
  build-test:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Setup environment
      - Install dependencies
      - Run unit tests
      - Run integration tests
      - Build application
      - Upload artifacts
  
  # 2. Security Scan
  security:
    needs: build-test
    steps:
      - Dependency check
      - Static code analysis
      - Container scan
      - Secrets scan
  
  # 3. Deploy Staging
  deploy-staging:
    needs: security
    if: branch == develop
    steps:
      - Deploy to staging
      - Run smoke tests
      - Performance tests
  
  # 4. Deploy Production
  deploy-prod:
    needs: security
    if: branch == main
    environment: production
    steps:
      - Manual approval
      - Blue-green deployment
      - Health checks
      - Rollback if needed'''
        
        self.exemplo(exemplo_pipeline)
        
        input("\n🔸 Pressione ENTER quando terminar seu pipeline...")
        
        self.print_success("🎉 Excelente! Criar pipelines é uma habilidade essencial em DevOps!")
        self.print_tip("💡 Pratique criando pipelines para diferentes tipos de aplicações!")
    
    def _mini_projeto_pipeline_completo(self) -> None:
        """Mini Projeto - Pipeline DevOps Completo"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: PIPELINE DEVOPS COMPLETO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: PIPELINE DEVOPS COMPLETO")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um pipeline DevOps completo do zero!")
        
        self.print_concept(
            "Pipeline DevOps End-to-End",
            "Um sistema automatizado que leva código do desenvolvimento até produção com segurança, testes e monitoramento"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de pipeline é usado por:", "text")
        usos_praticos = [
            "Netflix para fazer milhares de deploys por dia",
            "Spotify para entregar features rapidamente",
            "Uber para manter serviços sempre disponíveis",
            "Startups para competir com grandes empresas"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        input("\n🔸 Pressione ENTER para começar...")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Estrutura do Projeto
        self.print_section("PASSO 1: ESTRUTURA DO PROJETO", "📁", "info")
        self.print_tip("Vamos criar a estrutura de uma aplicação web com DevOps completo!")
        
        estrutura = '''# Estrutura do Projeto DevOps
project-devops/
├── app/
│   ├── app.py              # Aplicação Flask
│   ├── requirements.txt    # Dependências Python
│   └── tests/             # Testes automatizados
├── docker/
│   ├── Dockerfile         # Imagem da aplicação
│   └── docker-compose.yml # Orquestração local
├── k8s/
│   ├── deployment.yaml    # Deploy Kubernetes
│   ├── service.yaml       # Service K8s
│   └── ingress.yaml       # Ingress para acesso
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # Pipeline completo
├── terraform/
│   └── main.tf           # Infraestrutura como código
└── monitoring/
    ├── prometheus.yml     # Configuração métricas
    └── grafana/          # Dashboards'''
        
        self.exemplo(estrutura)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 2: Aplicação
        self.print_section("PASSO 2: CRIANDO A APLICAÇÃO", "💻", "success")
        
        app_code = '''# app/app.py - API REST com Flask
from flask import Flask, jsonify, request
import os
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Dados em memória para exemplo
tasks = []

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': os.getenv('APP_VERSION', '1.0.0')
    })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Listar todas as tarefas"""
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Criar nova tarefa"""
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task)
    logging.info(f"Task created: {task['id']}")
    return jsonify(task), 201

@app.route('/metrics')
def metrics():
    """Métricas para Prometheus"""
    return f"""# HELP tasks_total Total number of tasks
# TYPE tasks_total counter
tasks_total {len(tasks)}
# HELP tasks_completed Total completed tasks
# TYPE tasks_completed counter
tasks_completed {len([t for t in tasks if t.get('done')])}
"""

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)'''
        
        self.exemplo(app_code)
        
        # Testes
        self.print_colored("\n🧪 TESTES AUTOMATIZADOS:", "warning")
        test_code = '''# app/tests/test_app.py
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_create_task(client):
    """Test task creation"""
    response = client.post('/api/tasks',
        json={'title': 'Test Task'},
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Task'
    assert data['done'] == False'''
        
        self.exemplo(test_code)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 3: Containerização
        self.print_section("PASSO 3: CONTAINERIZAÇÃO", "🐳", "info")
        
        dockerfile = '''# docker/Dockerfile
FROM python:3.11-slim

# Metadados
LABEL maintainer="devops@exemplo.com"
LABEL version="1.0.0"

# Criar usuário não-root
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar dependências primeiro (cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY --chown=appuser:appuser . .

# Mudar para usuário não-root
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')"

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]'''
        
        self.exemplo(dockerfile)
        
        docker_compose = '''# docker/docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - APP_VERSION=1.0.0
      - DATABASE_URL=postgresql://user:pass@db:5432/tasks
    depends_on:
      - db
      - redis
    restart: unless-stopped
    networks:
      - app-network

  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=tasks
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

  redis:
    image: redis:6-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    networks:
      - app-network

volumes:
  postgres_data:
  redis_data:

networks:
  app-network:
    driver: bridge'''
        
        self.exemplo(docker_compose)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 4: Pipeline CI/CD
        self.print_section("PASSO 4: PIPELINE CI/CD", "⚙️", "success")
        
        pipeline = '''# .github/workflows/ci-cd.yml
name: DevOps Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ========== BUILD & TEST ==========
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    
    - name: Install dependencies
      run: |
        pip install -r app/requirements.txt
        pip install pytest pytest-cov flake8 bandit safety
    
    - name: Lint code
      run: flake8 app/ --max-line-length=88
    
    - name: Security scan
      run: |
        bandit -r app/
        safety check
    
    - name: Run tests
      run: |
        cd app
        pytest tests/ -v --cov=. --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3

  # ========== BUILD DOCKER ==========
  build:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Log in to Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: ./app
        push: true
        tags: |
          ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
          ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
    
    - name: Scan image for vulnerabilities
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload Trivy scan results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'

  # ========== DEPLOY STAGING ==========
  deploy-staging:
    if: github.ref == 'refs/heads/develop'
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to Kubernetes Staging
      run: |
        echo "Deploying to staging..."
        # kubectl apply -f k8s/ -n staging
        # kubectl set image deployment/app app=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} -n staging
        # kubectl rollout status deployment/app -n staging

  # ========== DEPLOY PRODUCTION ==========
  deploy-production:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to Production with Canary
      run: |
        echo "Starting canary deployment..."
        # Scripts de deploy canário
        # 10% -> 50% -> 100% do tráfego'''
        
        self.exemplo(pipeline)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 5: Kubernetes
        self.print_section("PASSO 5: DEPLOY KUBERNETES", "☸️", "warning")
        
        k8s_deployment = '''# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devops-app
  labels:
    app: devops-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: devops-app
  template:
    metadata:
      labels:
        app: devops-app
    spec:
      containers:
      - name: app
        image: ghcr.io/user/devops-app:latest
        ports:
        - containerPort: 5000
        env:
        - name: APP_VERSION
          value: "1.0.0"
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
apiVersion: v1
kind: Service
metadata:
  name: devops-app-service
spec:
  selector:
    app: devops-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: devops-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: devops-app
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
        averageUtilization: 80'''
        
        self.exemplo(k8s_deployment)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 6: Monitoramento
        self.print_section("PASSO 6: MONITORAMENTO", "📊", "success")
        
        monitoring = '''# monitoring/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'devops-app'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        action: keep
        regex: devops-app
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace

# Alertas
rule_files:
  - 'alerts.yml'

# alerts.yml
groups:
  - name: devops-app
    rules:
    - alert: HighErrorRate
      expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High error rate detected"
        description: "Error rate is {{ $value }} errors per second"
    
    - alert: PodDown
      expr: up{job="devops-app"} == 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "Pod is down"
        description: "Pod {{ $labels.pod }} is down"'''
        
        self.exemplo(monitoring)
        
        # === RESULTADO FINAL ===
        self.print_section("PIPELINE COMPLETO CRIADO!", "🎉", "success")
        
        self.print_colored("\n🏆 PARABÉNS! Você criou um pipeline DevOps profissional com:", "warning")
        componentes = [
            "✅ Aplicação containerizada com Docker",
            "✅ Testes automatizados (unit + security)",
            "✅ CI/CD com GitHub Actions",
            "✅ Build e push automático de imagens",
            "✅ Scan de vulnerabilidades",
            "✅ Deploy automatizado em Kubernetes",
            "✅ Auto-scaling baseado em métricas",
            "✅ Monitoramento com Prometheus",
            "✅ Alertas configurados",
            "✅ Ambientes separados (staging/prod)"
        ]
        
        for componente in componentes:
            self.print_colored(componente, "text")
        
        # === PRÓXIMOS PASSOS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar GitOps com ArgoCD",
            "Implementar service mesh (Istio)",
            "Adicionar tracing distribuído (Jaeger)",
            "Configurar backup automatizado",
            "Implementar disaster recovery",
            "Adicionar testes de carga (K6)",
            "Configurar WAF e proteção DDoS"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: DevOps Engineer!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Pipeline DevOps Completo")
        
        self.pausar()