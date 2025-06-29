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
import time
import json
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
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._capstone_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _capstone_principal(self) -> None:
        """Conteúdo principal do módulo Capstone Project"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 MÓDULO 35: CAPSTONE PROJECT - PROJETO FINAL")
        else:
            print("\n" + "="*50)
            print("🎓 MÓDULO 35: CAPSTONE PROJECT - PROJETO FINAL")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎓 PARABÉNS! Você chegou ao projeto FINAL do curso! Vamos integrar TODOS os conceitos aprendidos!")
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
            self._mini_projeto_cloudcorp_platform()
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
                'id': 'secao_visao_projeto',
                'titulo': '🎯 Visão Geral do Projeto Final',
                'descricao': 'Conheça o CloudCorp Enterprise Platform',
                'funcao': self._secao_visao_projeto
            },
            {
                'id': 'secao_arquitetura_enterprise',
                'titulo': '🏗️ Arquitetura Enterprise',
                'descricao': 'Clean Architecture + Design Patterns',
                'funcao': self._secao_arquitetura_enterprise
            },
            {
                'id': 'secao_integracao_conceitos',
                'titulo': '🔗 Integração de Todos os Conceitos',
                'descricao': 'Como tudo se conecta no projeto final',
                'funcao': self._secao_integracao_conceitos
            },
            {
                'id': 'secao_desenvolvimento_fases',
                'titulo': '📅 Desenvolvimento em Fases',
                'descricao': 'Roadmap do MVP ao Enterprise',
                'funcao': self._secao_desenvolvimento_fases
            },
            {
                'id': 'secao_tecnologias_stack',
                'titulo': '💻 Stack Tecnológico Completo',
                'descricao': 'Todas as tecnologias integradas',
                'funcao': self._secao_tecnologias_stack
            },
            {
                'id': 'secao_devops_deploy',
                'titulo': '🚀 DevOps e Deploy Enterprise',
                'descricao': 'Kubernetes, CI/CD e Monitoramento',
                'funcao': self._secao_devops_deploy
            },
            {
                'id': 'secao_resultado_final',
                'titulo': '🏆 Resultado Final e Próximos Passos',
                'descricao': 'Sua jornada como desenvolvedor expert',
                'funcao': self._secao_resultado_final
            }
        ]
        
        secoes_visitadas = set()
        
        # === LOOP PRINCIPAL DE NAVEGAÇÃO ===
        while True:
            # Limpa tela e mostra cabeçalho
            self.ui.clear_screen() if self.ui else print("\n" + "="*50)
            self.print_section("NAVEGAÇÃO DO CAPSTONE PROJECT", "🎓", "accent")
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
                self.print_success("🌟 Você completou todas as seções! Está pronto para o projeto final!")
            
            # Processa escolha do usuário
            try:
                escolha = input(f"\n👉 Escolha uma seção (1-{len(secoes)}) ou 0 para continuar: ").strip()
                
                if escolha == "0":
                    # Verifica se visitou seções suficientes
                    if progresso >= 4:  # Pelo menos 4 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 4 seções antes de continuar!")
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
    
    def _secao_visao_projeto(self) -> None:
        """Seção: Visão Geral do Projeto Final"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("VISÃO GERAL DO PROJETO FINAL", "🎯")
        
        self.print_concept(
            "CloudCorp Enterprise Platform",
            "Uma plataforma SaaS completa que integra TODOS os conceitos aprendidos no curso em uma aplicação de nível enterprise"
        )
        
        self.print_tip("Este projeto demonstra sua evolução de iniciante a desenvolvedor expert!")
        
        self.print_colored("\\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como construir uma cidade completa depois de aprender a fazer tijolos, paredes, portas e janelas - agora você junta tudo em uma obra-prima!", "text")
        input("\\n🔸 Pressione ENTER para continuar...")
        
        self.print_colored("\\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Integra todos os 34 módulos anteriores em um sistema único",
            "2. Aplica arquitetura enterprise com Clean Architecture",
            "3. Usa padrões de design profissionais em produção",
            "4. Implementa DevOps completo com deploy automático"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        self.print_colored("\\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Startups unicórnios como Notion, Slack, Stripe",
            "Empresas Fortune 500 para gestão interna",
            "Agências digitais para clientes enterprise",
            "Consultores para projetos de transformação digital"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_arquitetura_enterprise(self) -> None:
        """Seção: Arquitetura Enterprise"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ARQUITETURA ENTERPRISE", "🏗️")
        
        self.print_concept(
            "Clean Architecture + Hexagonal",
            "Uma arquitetura que separa completamente a lógica de negócio da infraestrutura, permitindo que o código seja testável, flexível e escalável"
        )
        
        self.print_tip("Esta arquitetura é usada por gigantes como Netflix, Uber e Amazon!")
        
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como um prédio bem planejado: fundação sólida (domínio), estrutura (casos de uso), acabamento (interface) e instalações (infraestrutura) - cada parte tem sua responsabilidade!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        codigo_exemplo = '''# Exemplo de Clean Architecture em ação
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
import uuid

# === CAMADA DE DOMÍNIO ===
@dataclass
class User:
    """Entidade de domínio - regras de negócio puras"""
    id: uuid.UUID
    email: str
    name: str
    
    def is_valid_email(self) -> bool:
        return "@" in self.email and "." in self.email

# === CAMADA DE APLICAÇÃO ===
class IUserRepository(ABC):
    """Interface do repositório - não depende de infraestrutura"""
    @abstractmethod
    async def save(self, user: User) -> User:
        pass
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        pass

class CreateUserUseCase:
    """Caso de uso - orquestra a lógica de negócio"""
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
    
    async def execute(self, email: str, name: str) -> User:
        # Validações de negócio
        if await self.user_repo.find_by_email(email):
            raise ValueError("Email já existe")
        
        # Criar entidade
        user = User(id=uuid.uuid4(), email=email, name=name)
        
        if not user.is_valid_email():
            raise ValueError("Email inválido")
        
        # Persistir
        return await self.user_repo.save(user)

# === CAMADA DE INFRAESTRUTURA ===
class PostgreSQLUserRepository(IUserRepository):
    """Implementação específica - pode ser trocada facilmente"""
    async def save(self, user: User) -> User:
        # Código do PostgreSQL aqui
        return user
    
    async def find_by_email(self, email: str) -> Optional[User]:
        # Query no PostgreSQL aqui
        return None

# === CAMADA DE APRESENTAÇÃO ===
# FastAPI, Flask, Django, etc.
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/users")
async def create_user_endpoint(email: str, name: str):
    # Dependency Injection
    user_repo = PostgreSQLUserRepository()
    use_case = CreateUserUseCase(user_repo)
    
    try:
        user = await use_case.execute(email, name)
        return {"id": str(user.id), "email": user.email, "name": user.name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

print("🏗️ VANTAGENS DA CLEAN ARCHITECTURE:")
print("✅ Testabilidade - fácil de testar cada camada")
print("✅ Flexibilidade - trocar banco sem afetar regras")
print("✅ Manutenibilidade - código organizado e limpo")
print("✅ Escalabilidade - fácil adicionar novas features")
print("✅ Independência - não depende de frameworks")
'''
        
        self.print_code_section("EXEMPLO PRÁTICO", codigo_exemplo)
        self.executar_codigo(codigo_exemplo)
        
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix - para gerenciar bilhões de streams",
            "Uber - para coordenar milhões de corridas",
            "Amazon - para processar milhões de pedidos",
            "Google - para indexar toda a internet"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_integracao_conceitos(self) -> None:
        """Seção: Integração de Todos os Conceitos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("INTEGRAÇÃO DE TODOS OS CONCEITOS", "🔗")
        
        self.print_concept(
            "Sinergismo dos Módulos",
            "Como todos os 34 módulos anteriores trabalham juntos para criar uma aplicação enterprise completa e profissional"
        )
        
        self.print_tip("É aqui que você vê que Python não é só uma linguagem - é um ecossistema completo!")
        
        # Mapeamento dos módulos
        modulos_mapeamento = {
            "Básicos (1-11)": [
                "Variáveis e tipos → Estado da aplicação",
                "Condições → Lógica de negócio",
                "Loops → Processamento em lote",
                "Listas → Coleções de dados",
                "Funções → Casos de uso",
                "Dicionários → Configurações e cache"
            ],
            "Avançados (12-23)": [
                "OOP → Modelagem de domínio",
                "Decorators → Middleware e aspectos",
                "Geradores → Streaming de dados",
                "Regex → Validação de entrada",
                "Debugging → Monitoramento e logs",
                "Exceções → Tratamento de erros"
            ],
            "Essenciais (24-30)": [
                "APIs → Interface externa",
                "Testes → Qualidade e confiabilidade",
                "Performance → Otimização e cache",
                "Async → Concorrência e escala",
                "Segurança → Proteção e compliance"
            ],
            "Enterprise (31-35)": [
                "Design Patterns → Arquitetura sólida",
                "Clean Architecture → Organização",
                "DevOps → Deploy e operação",
                "Database Design → Persistência",
                "Capstone → Integração total"
            ]
        }
        
        for categoria, conceitos in modulos_mapeamento.items():
            self.print_colored(f"\n📚 {categoria}:", "warning")
            for conceito in conceitos:
                self.print_colored(f"  • {conceito}", "text")
            input("   ⏳ Pressione ENTER para a próxima categoria...")
        
        self.print_colored("\n🌍 RESULTADO FINAL NO MUNDO REAL:", "accent")
        resultados = [
            "Sistema que processa 100,000+ usuários simultâneos",
            "API que responde em menos de 200ms",
            "Database otimizado para TBs de dados",
            "Deploy automático com zero downtime",
            "Monitoramento 24/7 com alertas inteligentes"
        ]
        for resultado in resultados:
            self.print_colored(f"• {resultado}", "primary")
        
        self.pausar()
    
    def _secao_desenvolvimento_fases(self) -> None:
        """Seção: Desenvolvimento em Fases"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DESENVOLVIMENTO EM FASES", "📅")
        
        self.print_concept(
            "Roadmap Estratégico",
            "Como construir uma aplicação enterprise de forma incremental, do MVP à solução completa em 20 semanas"
        )
        
        fases = {
            "Fase 1 - MVP (4 semanas)": [
                "Setup inicial e autenticação",
                "CRUD básico de usuários",
                "Multi-tenancy simples",
                "Deploy básico com Docker"
            ],
            "Fase 2 - Features (6 semanas)": [
                "Sistema financeiro",
                "CRM e gestão de clientes",
                "Analytics em tempo real",
                "Notificações e email"
            ],
            "Fase 3 - Escala (4 semanas)": [
                "Cache distribuído",
                "Otimização de performance",
                "Kubernetes e auto-scaling",
                "Monitoramento avançado"
            ],
            "Fase 4 - Enterprise (6 semanas)": [
                "SSO e autenticação avançada",
                "API GraphQL",
                "Mobile app",
                "Compliance e auditoria"
            ]
        }
        
        for fase, features in fases.items():
            self.print_colored(f"\n🚀 {fase}:", "warning")
            for feature in features:
                self.print_colored(f"  ✅ {feature}", "text")
            input("   ⏳ Pressione ENTER para a próxima fase...")
        
        self.pausar()
    
    def _secao_tecnologias_stack(self) -> None:
        """Seção: Stack Tecnológico Completo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("STACK TECNOLÓGICO COMPLETO", "💻")
        
        self.print_concept(
            "Full Stack Enterprise",
            "Todas as tecnologias modernas trabalhando em harmonia para criar uma solução de classe mundial"
        )
        
        stack = {
            "Backend 🐍": [
                "Python 3.11+ (FastAPI, SQLAlchemy)",
                "PostgreSQL 15 + Redis 7",
                "Pydantic v2 para validação",
                "Celery para tarefas assíncronas"
            ],
            "Frontend ⚛️": [
                "React 18 + TypeScript",
                "Next.js 14 (SSR/SSG)",
                "TailwindCSS + Shadcn/ui",
                "TanStack Query (estado)"
            ],
            "DevOps 🚀": [
                "Docker + Kubernetes",
                "GitHub Actions (CI/CD)",
                "Prometheus + Grafana",
                "ELK Stack (logs)"
            ],
            "Cloud ☁️": [
                "AWS/Azure/GCP",
                "Terraform (IaC)",
                "CDN global",
                "Auto-scaling"
            ]
        }
        
        for categoria, tecnologias in stack.items():
            self.print_colored(f"\n{categoria}:", "warning")
            for tech in tecnologias:
                self.print_colored(f"  • {tech}", "text")
            input("   ⏳ Pressione ENTER para a próxima categoria...")
        
        self.pausar()
    
    def _secao_devops_deploy(self) -> None:
        """Seção: DevOps e Deploy Enterprise"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DEVOPS E DEPLOY ENTERPRISE", "🚀")
        
        self.print_concept(
            "CI/CD Profissional",
            "Pipeline completo que automatiza testes, build, deploy e monitoramento com zero downtime e rollback automático"
        )
        
        pipeline_exemplo = '''# Pipeline CI/CD Enterprise
name: Production Deploy

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Run tests
      run: |
        pytest backend/tests/ --cov=80%
        npm test frontend/
  
  security:
    runs-on: ubuntu-latest
    steps:
    - name: Security scan
      uses: aquasecurity/trivy-action@master
  
  build:
    needs: [test, security]
    runs-on: ubuntu-latest
    steps:
    - name: Build Docker images
      run: |
        docker build -t cloudcorp/backend:${{ github.sha }} .
        docker push cloudcorp/backend:${{ github.sha }}
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
    - name: Deploy to Kubernetes
      run: |
        kubectl set image deployment/backend \
          backend=cloudcorp/backend:${{ github.sha }}
        kubectl rollout status deployment/backend
  
  monitor:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
    - name: Health check
      run: |
        curl -f https://api.cloudcorp.com/health
        # Alertas automáticos se falhar

print("🚀 BENEFITS DO CI/CD ENTERPRISE:")
print("⚡ Deploy em segundos, não horas")
print("🔒 Zero chance de deploy quebrado")
print("📊 Monitoramento em tempo real")
print("🔄 Rollback automático se algo falhar")
print("🎯 99.9% uptime garantido")
'''
        
        self.print_code_section("PIPELINE EXEMPLO", pipeline_exemplo)
        self.executar_codigo(pipeline_exemplo)
        
        self.pausar()
    
    def _secao_resultado_final(self) -> None:
        """Seção: Resultado Final e Próximos Passos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("RESULTADO FINAL E PRÓXIMOS PASSOS", "🏆")
        
        self.print_concept(
            "Desenvolvedor Expert",
            "Você não é mais um iniciante - é um arquiteto de software capaz de criar soluções enterprise de classe mundial"
        )
        
        self.print_colored("\n🎯 O QUE VOCÊ CONQUISTOU:", "success")
        conquistas = [
            "Domínio completo do Python (básico ao avançado)",
            "Arquitetura enterprise com padrões profissionais",
            "DevOps e deploy em produção",
            "Database design otimizado",
            "APIs REST e GraphQL",
            "Testes automatizados",
            "Monitoramento e observabilidade",
            "Segurança de nível enterprise"
        ]
        
        for conquista in conquistas:
            self.print_colored(f"✅ {conquista}", "primary")
        
        self.print_colored("\n💼 VAGAS PARA AS QUAIS VOCÊ ESTÁ PREPARADO:", "warning")
        vagas = [
            "Senior Python Developer (R$ 8.000 - 15.000)",
            "Software Architect (R$ 12.000 - 20.000)",
            "DevOps Engineer (R$ 10.000 - 18.000)",
            "Tech Lead (R$ 15.000 - 25.000)",
            "CTO de Startup (equity + salário)",
            "Consultant/Freelancer (R$ 150-300/hora)"
        ]
        
        for vaga in vagas:
            self.print_colored(f"💰 {vaga}", "accent")
        
        self.print_colored("\n🚀 PRÓXIMOS PASSOS RECOMENDADOS:", "info")
        proximos_passos = [
            "Implemente o CloudCorp Platform completo",
            "Contribua para projetos open source",
            "Crie seu portfólio no GitHub",
            "Candidate-se a vagas senior",
            "Considere criar sua própria startup",
            "Mentore outros desenvolvedores"
        ]
        
        for passo in proximos_passos:
            self.print_colored(f"🎯 {passo}", "text")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre desenvolvimento enterprise!", "text")
        
        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para especialistas: Cada exercício testa conceitos avançados do capstone project!")
        self.print_colored("\\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Testam sua compreensão da arquitetura enterprise", "text")
        self.print_colored("• Avaliam seu conhecimento de integração de sistemas", "text")
        self.print_colored("• Verificam seu domínio de padrões profissionais", "text")
        self.print_colored("• Use Ctrl+C se quiser voltar ao menu principal", "text")
        
        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Arquitetura Enterprise',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual a principal vantagem da Clean Architecture?',
                        'answer': ['independencia', 'flexibilidade', 'testabilidade', 'isolamento'],
                        'hint': 'Pense na capacidade de trocar componentes sem afetar o core'
                    },
                    {
                        'question': 'Em qual camada ficam as regras de negócio na Clean Architecture?',
                        'answer': ['dominio', 'domain', 'entidades', 'entities'],
                        'hint': 'É a camada mais interna e independente'
                    },
                    {
                        'question': 'Qual padrão permite trocar implementações facilmente?',
                        'answer': ['repository', 'dependency injection', 'interface'],
                        'hint': 'Usado para abstrair acesso a dados'
                    },
                    {
                        'question': 'O que significa CI/CD?',
                        'answer': ['continuous integration continuous deployment', 'integracao continua deploy continuo'],
                        'hint': 'Automatização do pipeline de desenvolvimento'
                    },
                    {
                        'question': 'Qual ferramenta orquestra containers em produção?',
                        'answer': ['kubernetes', 'k8s'],
                        'hint': 'Sistema de orquestração da Google'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código Enterprise',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o Use Case para criar usuário',
                        'starter': '''class CreateUserUseCase:\n    def __init__(self, user_repo: IUserRepository):\n        self.user_repo = user_repo\n    \n    async def execute(self, email: str, name: str) -> User:\n        # Verificar se email já existe\n        if await self.user_repo._____(email):\n            raise ValueError("Email já existe")\n        \n        # Criar usuário\n        user = User(id=uuid.uuid4(), email=email, name=name)\n        return await self.user_repo._____(user)''',
                        'solution': 'find_by_email',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o middleware de tenant',
                        'starter': '''class TenantMiddleware:\n    async def __call__(self, request: Request, call_next):\n        # Extrair tenant do subdomínio\n        tenant_slug = request.headers.get("X-Tenant-Slug")\n        \n        if not tenant_slug:\n            raise HTTPException(400, "_____ não identificado")\n        \n        # Carregar tenant\n        tenant = await self.tenant_service.get_by_slug(_____)\n        request.state.tenant = tenant\n        \n        return await call_next(request)''',
                        'solution': 'tenant_slug',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a configuração Kubernetes',
                        'starter': '''apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: cloudcorp-backend\nspec:\n  replicas: 5\n  selector:\n    matchLabels:\n      app: cloudcorp-backend\n  template:\n    spec:\n      containers:\n      - name: backend\n        image: cloudcorp/backend:v1.0.0\n        ports:\n        - containerPort: _____\n        resources:\n          limits:\n            cpu: 500m\n            memory: _____''',
                        'solution': '8000',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Projete seu próprio microserviço',
                'type': 'creative',
                'instruction': 'Descreva um microserviço que você adicionaria ao CloudCorp Platform. Inclua: propósito, API endpoints, tecnologias e como se integra com o sistema.'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\\nEscolha uma atividade:")
            print("1. 📝 Quiz de Arquitetura Enterprise")
            print("2. 💻 Complete o Código Enterprise")
            print("3. 🎨 Exercício Criativo")
            print("0. Continuar para o Projeto Capstone")
            
            try:
                escolha = input("\\n👉 Sua escolha: ").strip().lower()
                
                if escolha in ["0", "continuar", "sair", "proximo"]:
                    break
                elif escolha in ["1", "quiz", "arquitetura"]:
                    try:
                        self._run_quiz(exercicios[0])
                    except KeyboardInterrupt:
                        self.print_warning("\\n\\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\\n\\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo"]:
                    try:
                        self._run_creative_exercise(exercicios[2])
                    except KeyboardInterrupt:
                        self.print_warning("\\n\\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício criativo. Continuando...")
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")
            
            except KeyboardInterrupt:
                self.print_warning("\\n\\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre arquitetura enterprise",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios de código progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Projete um microserviço",
            "🔢 OPÇÃO 0 - Continue para o Projeto Capstone final",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Estes exercícios testam conceitos avançados do curso!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _mini_projeto_cloudcorp_platform(self) -> None:
        """Mini Projeto - Módulo 35: CloudCorp Enterprise Platform"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 CAPSTONE PROJECT: CLOUDCORP ENTERPRISE PLATFORM")
        else:
            print("\\n" + "="*50)
            print("🎯 CAPSTONE PROJECT: CLOUDCORP ENTERPRISE PLATFORM")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar o projeto FINAL que demonstra TODOS os conceitos aprendidos!")
        
        self.print_concept(
            "CloudCorp Enterprise Platform",
            "Uma plataforma SaaS completa que integra arquitetura enterprise, DevOps, segurança e performance de classe mundial"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\\nEste tipo de projeto é usado por:", "text")
        usos_praticos = [
            "Startups unicórnios para escalar rapidamente",
            "Empresas Fortune 500 para modernização",
            "Consultores para transformação digital",
            "Desenvolvedores senior em big techs"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Arquitetura e Setup
        self.print_section("PASSO 1: Arquitetura Enterprise", "🏗️", "info")
        self.print_tip("Vamos criar a base sólida com Clean Architecture e padrões profissionais!")
        
        try:
            codigo_arquitetura = '''# 🏗️ CLOUDCORP PLATFORM - ARQUITETURA ENTERPRISE
# Clean Architecture + Domain-Driven Design + Microservices

# ========================================
# 1. ESTRUTURA DE PROJETO ENTERPRISE
# ========================================

"""
cloudcorp-platform/
├── backend/                    # Python + FastAPI
│   ├── src/
│   │   ├── domain/            # Entidades e regras de negócio
│   │   │   ├── entities/      # User, Tenant, Project
│   │   │   ├── repositories/  # Interfaces abstratas
│   │   │   └── services/      # Serviços de domínio
│   │   ├── application/       # Casos de uso
│   │   │   ├── use_cases/     # CreateUser, UpdateProject
│   │   │   └── dto/           # Data Transfer Objects
│   │   ├── infrastructure/    # Implementações concretas
│   │   │   ├── database/      # SQLAlchemy, PostgreSQL
│   │   │   ├── cache/         # Redis
│   │   │   └── external/      # APIs externas
│   │   └── presentation/      # APIs e interfaces
│   │       ├── api/           # FastAPI endpoints
│   │       └── web/           # Web interface
│   ├── tests/                 # Testes automatizados
│   └── Dockerfile             # Containerização
├── frontend/                   # React + TypeScript
│   ├── src/
│   │   ├── components/        # Componentes reutilizáveis
│   │   ├── pages/             # Páginas da aplicação
│   │   ├── hooks/             # Custom hooks
│   │   └── services/          # API clients
│   └── Dockerfile
├── infrastructure/             # DevOps e infraestrutura
│   ├── kubernetes/            # Manifests K8s
│   ├── terraform/             # Infrastructure as Code
│   └── monitoring/            # Prometheus + Grafana
└── docker-compose.yml         # Ambiente local
"""

# ========================================
# 2. DOMAIN ENTITIES (Clean Architecture)
# ========================================

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

class ProjectStatus(Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class User:
    """Entidade de domínio: Usuário"""
    id: uuid.UUID
    tenant_id: uuid.UUID
    email: str
    name: str
    role: UserRole
    is_active: bool
    created_at: datetime
    
    def can_manage_project(self, project: 'Project') -> bool:
        """Regra de negócio: quem pode gerenciar projeto"""
        return (
            self.role == UserRole.ADMIN or
            (self.role == UserRole.MANAGER and project.tenant_id == self.tenant_id)
        )
    
    def is_tenant_admin(self) -> bool:
        """Verifica se é admin do tenant"""
        return self.role == UserRole.ADMIN

@dataclass
class Tenant:
    """Entidade de domínio: Empresa/Organização"""
    id: uuid.UUID
    slug: str
    name: str
    plan: str  # basic, pro, enterprise
    max_users: int
    is_active: bool
    created_at: datetime
    
    def can_add_user(self, current_users_count: int) -> bool:
        """Regra de negócio: limite de usuários por plano"""
        return current_users_count < self.max_users

@dataclass
class Project:
    """Entidade de domínio: Projeto"""
    id: uuid.UUID
    tenant_id: uuid.UUID
    name: str
    description: str
    owner_id: uuid.UUID
    status: ProjectStatus
    budget: Optional[float]
    created_at: datetime
    due_date: Optional[datetime]
    
    def is_overdue(self) -> bool:
        """Regra de negócio: projeto atrasado"""
        if not self.due_date:
            return False
        return datetime.now() > self.due_date and self.status != ProjectStatus.COMPLETED

# ========================================
# 3. REPOSITORY INTERFACES (Ports)
# ========================================

from abc import ABC, abstractmethod

class IUserRepository(ABC):
    """Interface do repositório de usuários"""
    
    @abstractmethod
    async def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    async def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        pass
    
    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass
    
    @abstractmethod
    async def list_by_tenant(self, tenant_id: uuid.UUID) -> List[User]:
        pass

class ITenantRepository(ABC):
    """Interface do repositório de tenants"""
    
    @abstractmethod
    async def create(self, tenant: Tenant) -> Tenant:
        pass
    
    @abstractmethod
    async def get_by_slug(self, slug: str) -> Optional[Tenant]:
        pass

# ========================================
# 4. USE CASES (Application Layer)
# ========================================

class CreateUserUseCase:
    """Caso de uso: Criar usuário com validações de negócio"""
    
    def __init__(
        self, 
        user_repo: IUserRepository,
        tenant_repo: ITenantRepository
    ):
        self.user_repo = user_repo
        self.tenant_repo = tenant_repo
    
    async def execute(
        self, 
        tenant_id: uuid.UUID,
        email: str, 
        name: str, 
        role: UserRole
    ) -> User:
        """Executar caso de uso com validações"""
        
        # 1. Validar tenant
        tenant = await self.tenant_repo.get_by_id(tenant_id)
        if not tenant or not tenant.is_active:
            raise ValueError("Tenant não encontrado ou inativo")
        
        # 2. Verificar limite de usuários
        current_users = await self.user_repo.list_by_tenant(tenant_id)
        if not tenant.can_add_user(len(current_users)):
            raise ValueError("Limite de usuários atingido para este plano")
        
        # 3. Verificar email único
        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("Email já cadastrado")
        
        # 4. Criar usuário
        user = User(
            id=uuid.uuid4(),
            tenant_id=tenant_id,
            email=email,
            name=name,
            role=role,
            is_active=True,
            created_at=datetime.now()
        )
        
        return await self.user_repo.create(user)

print("🏗️ ARQUITETURA ENTERPRISE IMPLEMENTADA:")
print("✅ Domain Entities com regras de negócio")
print("✅ Repository Pattern para abstração")
print("✅ Use Cases para orquestração")
print("✅ Clean Architecture respeitada")
print("✅ Separation of Concerns aplicado")
'''
            
            self.print_code_section("CÓDIGO DA ARQUITETURA", codigo_arquitetura)
            self.executar_codigo(codigo_arquitetura)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: API e Endpoints
        self.print_section("PASSO 2: APIs REST + GraphQL", "🌐", "success")
        self.print_colored("Agora vamos criar as APIs que conectam tudo:", "text")
        
        codigo_api = '''# 🌐 CLOUDCORP PLATFORM - APIs ENTERPRISE

# ========================================
# 1. FASTAPI + DEPENDENCY INJECTION
# ========================================

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(
    title="CloudCorp Enterprise Platform",
    description="Plataforma SaaS enterprise completa",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS para frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================================
# 2. PYDANTIC MODELS (DTOs)
# ========================================

class UserCreateRequest(BaseModel):
    email: str
    name: str
    role: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    role: str
    is_active: bool
    created_at: str

class TenantResponse(BaseModel):
    id: str
    slug: str
    name: str
    plan: str
    max_users: int

# ========================================
# 3. DEPENDENCY INJECTION
# ========================================

async def get_user_repository() -> IUserRepository:
    """Injeta repositório de usuários"""
    # Em produção, vem do container IoC
    return PostgreSQLUserRepository()

async def get_tenant_repository() -> ITenantRepository:
    """Injeta repositório de tenants"""
    return PostgreSQLTenantRepository()

async def get_current_user() -> User:
    """Obtém usuário autenticado do token JWT"""
    # Validação de JWT aqui
    return User(
        id=uuid.uuid4(),
        tenant_id=uuid.uuid4(),
        email="admin@cloudcorp.com",
        name="Admin",
        role=UserRole.ADMIN,
        is_active=True,
        created_at=datetime.now()
    )

# ========================================
# 4. API ENDPOINTS
# ========================================

@app.get("/")
async def root():
    """Health check"""
    return {"message": "CloudCorp Platform API v1.0", "status": "healthy"}

@app.post("/api/v1/users", response_model=UserResponse)
async def create_user(
    user_data: UserCreateRequest,
    current_user: User = Depends(get_current_user),
    user_repo: IUserRepository = Depends(get_user_repository),
    tenant_repo: ITenantRepository = Depends(get_tenant_repository)
):
    """Criar usuário com validações enterprise"""
    
    # Verificar permissões
    if not current_user.is_tenant_admin():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Apenas admins podem criar usuários"
        )
    
    # Executar use case
    use_case = CreateUserUseCase(user_repo, tenant_repo)
    
    try:
        user = await use_case.execute(
            tenant_id=current_user.tenant_id,
            email=user_data.email,
            name=user_data.name,
            role=UserRole(user_data.role)
        )
        
        return UserResponse(
            id=str(user.id),
            email=user.email,
            name=user.name,
            role=user.role.value,
            is_active=user.is_active,
            created_at=user.created_at.isoformat()
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/api/v1/users", response_model=List[UserResponse])
async def list_users(
    current_user: User = Depends(get_current_user),
    user_repo: IUserRepository = Depends(get_user_repository)
):
    """Listar usuários do tenant"""
    
    users = await user_repo.list_by_tenant(current_user.tenant_id)
    
    return [
        UserResponse(
            id=str(user.id),
            email=user.email,
            name=user.name,
            role=user.role.value,
            is_active=user.is_active,
            created_at=user.created_at.isoformat()
        )
        for user in users
    ]

@app.get("/api/v1/tenants/current", response_model=TenantResponse)
async def get_current_tenant(
    current_user: User = Depends(get_current_user),
    tenant_repo: ITenantRepository = Depends(get_tenant_repository)
):
    """Obter dados do tenant atual"""
    
    tenant = await tenant_repo.get_by_id(current_user.tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant não encontrado")
    
    return TenantResponse(
        id=str(tenant.id),
        slug=tenant.slug,
        name=tenant.name,
        plan=tenant.plan,
        max_users=tenant.max_users
    )

# ========================================
# 5. MIDDLEWARE PERSONALIZADO
# ========================================

@app.middleware("http")
async def tenant_isolation_middleware(request, call_next):
    """Middleware para isolamento de tenant"""
    
    # Extrair tenant do header
    tenant_slug = request.headers.get("X-Tenant-Slug")
    
    if tenant_slug:
        # Configurar contexto do tenant
        request.state.tenant_slug = tenant_slug
    
    response = await call_next(request)
    
    # Adicionar headers de segurança
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    
    return response

print("🌐 API ENTERPRISE IMPLEMENTADA:")
print("✅ FastAPI com documentação automática")
print("✅ Dependency Injection profissional")
print("✅ Validação com Pydantic")
print("✅ Tratamento de erros robusto")
print("✅ Middleware de segurança")
print("✅ Multi-tenancy integrado")
print("\\n🚀 API rodando em: http://localhost:8000")
print("📚 Documentação em: http://localhost:8000/docs")
'''
        
        self.exemplo(codigo_api)
        print("\\n🚀 Executando simulação da API:")
        self.executar_codigo(codigo_api)
        
        # PASSO 3: DevOps e Deploy
        self.print_section("PASSO 3: DevOps Enterprise", "🚀", "warning")
        
        codigo_devops = '''# 🚀 CLOUDCORP PLATFORM - DEVOPS ENTERPRISE

# ========================================
# 1. DOCKER MULTI-STAGE BUILD
# ========================================

"""
# Dockerfile.backend
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runtime

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# ========================================
# 2. KUBERNETES DEPLOYMENT
# ========================================

kubernetes_manifests = """
# backend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudcorp-backend
  labels:
    app: cloudcorp-backend
spec:
  replicas: 3
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
        image: cloudcorp/backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: cloudcorp-secrets
              key: database-url
        - name: REDIS_URL
          value: "redis://redis-service:6379"
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
apiVersion: v1
kind: Service
metadata:
  name: cloudcorp-backend-service
spec:
  selector:
    app: cloudcorp-backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer

---
# Auto-scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: cloudcorp-backend-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: cloudcorp-backend
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
"""

# ========================================
# 3. CI/CD PIPELINE (GITHUB ACTIONS)
# ========================================

github_actions_pipeline = """
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: cloudcorp/platform

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
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
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src/ --cov-report=xml --cov-fail-under=80
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run security scan
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: '.'

  build-and-push:
    needs: [test, security]
    runs-on: ubuntu-latest
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Login to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Build and push
      id: build
      uses: docker/build-push-action@v5
      with:
        context: .
        platforms: linux/amd64,linux/arm64
        push: true
        tags: |
          ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
          ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    environment: production
    
    steps:
    - name: Deploy to Kubernetes
      run: |
        echo "Deploying to production cluster..."
        kubectl set image deployment/cloudcorp-backend \\
          backend=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        kubectl rollout status deployment/cloudcorp-backend
    
    - name: Run smoke tests
      run: |
        curl -f https://api.cloudcorp.com/health
        echo "✅ Health check passed"

  notify:
    needs: deploy
    runs-on: ubuntu-latest
    if: always()
    
    steps:
    - name: Notify team
      run: |
        echo "🚀 Deploy completed successfully!"
        echo "📊 Monitoring dashboard: https://grafana.cloudcorp.com"
"""

# ========================================
# 4. MONITORING E OBSERVABILIDADE
# ========================================

monitoring_config = """
# Prometheus configuration
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert_rules.yml"

scrape_configs:
  - job_name: 'cloudcorp-backend'
    static_configs:
      - targets: ['backend-service:8000']
    metrics_path: /metrics
    scrape_interval: 10s

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

# Alert rules
groups:
- name: cloudcorp.rules
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High error rate detected"
  
  - alert: HighLatency
    expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High latency detected"
"""

print("🚀 DEVOPS ENTERPRISE IMPLEMENTADO:")
print("✅ Docker multi-stage otimizado")
print("✅ Kubernetes com auto-scaling")
print("✅ CI/CD pipeline completo")
print("✅ Testes automatizados (80%+ coverage)")
print("✅ Security scanning integrado")
print("✅ Monitoring e alertas")
print("✅ Zero-downtime deployment")
print("\\n📊 Monitoramento: https://grafana.cloudcorp.com")
print("🔍 Logs: https://kibana.cloudcorp.com")
print("📈 Métricas: https://prometheus.cloudcorp.com")
'''
        
        self.exemplo(codigo_devops)
        self.executar_codigo(codigo_devops)
        
        # === RESULTADO FINAL ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        
        print("\\n" + "="*80)
        print("🎉 PARABÉNS! VOCÊ CRIOU UMA APLICAÇÃO ENTERPRISE COMPLETA!")
        print("="*80)
        
        resultado_final = f'''
📊 ESTATÍSTICAS DO PROJETO CLOUDCORP:

🏗️ ARQUITETURA:
• Clean Architecture com 4 camadas
• Domain-Driven Design (DDD)
• Microservices ready
• Event-driven architecture

💻 TECNOLOGIAS:
• Backend: Python + FastAPI + SQLAlchemy
• Frontend: React + TypeScript + Next.js
• Database: PostgreSQL + Redis
• Infraestrutura: Docker + Kubernetes

🚀 DEVOPS:
• CI/CD automatizado
• Testes com 80%+ coverage
• Security scanning
• Auto-scaling
• Zero-downtime deployment

📈 PERFORMANCE:
• < 200ms response time
• 10,000+ requests/second
• Auto-scaling de 3-10 pods
• Cache distribuído

🔒 SEGURANÇA:
• JWT authentication
• RBAC + ABAC authorization
• Security headers
• Input validation
• Audit logging

🌍 ESCALABILIDADE:
• Multi-tenant SaaS
• Horizontal scaling
• Load balancing
• Global CDN ready

🏆 NÍVEL CONQUISTADO: EXPERT ENTERPRISE DEVELOPER
'''
        
        print(resultado_final)
        
        self.print_success("\\n🎊 CONQUISTA ÉPICA DESBLOQUEADA: Arquiteto de Software Enterprise!")
        
        # === PRÓXIMOS PASSOS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Implemente o CloudCorp Platform completo",
            "Publique no GitHub como portfólio",
            "Candidate-se a vagas Senior/Staff/Principal",
            "Inicie sua própria startup SaaS",
            "Contribua para projetos open source",
            "Torne-se mentor de outros desenvolvedores"
        ]
        for passo in proximos_passos:
            self.print_colored(f"🎯 {passo}", "primary")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("CloudCorp Enterprise Platform - Capstone Project Completo")
        
        self.pausar()
