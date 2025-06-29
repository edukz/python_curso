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
        """Executa o módulo Database Design & Performance"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._database_design_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _database_design_principal(self) -> None:
        """Conteúdo principal do módulo Database Design"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🗄️ MÓDULO 34: DATABASE DESIGN & PERFORMANCE")
        else:
            print("\n" + "="*50)
            print("🗄️ MÓDULO 34: DATABASE DESIGN & PERFORMANCE")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🗄️ Bem-vindo ao mundo do design de banco de dados! Vamos criar sistemas que escalam para milhões de usuários!")
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
            self._mini_projeto_sistema_database_enterprise()
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
                'id': 'secao_fundamentos_modelagem',
                'titulo': '🎯 Fundamentos de Modelagem',
                'descricao': 'Entenda modelagem conceitual, lógica e física',
                'funcao': self._secao_fundamentos_modelagem
            },
            {
                'id': 'secao_normalizacao_desnormalizacao',
                'titulo': '🔧 Normalização e Desnormalização',
                'descricao': 'Aprenda as formas normais e quando quebrar regras',
                'funcao': self._secao_normalizacao_desnormalizacao
            },
            {
                'id': 'secao_indices_performance',
                'titulo': '⚡ Índices e Performance',
                'descricao': 'Otimize queries com índices estratégicos',
                'funcao': self._secao_indices_performance
            },
            {
                'id': 'secao_transactions_acid',
                'titulo': '🔄 Transações e ACID',
                'descricao': 'Garanta consistência e integridade dos dados',
                'funcao': self._secao_transactions_acid
            },
            {
                'id': 'secao_escalabilidade_sharding',
                'titulo': '📈 Escalabilidade e Sharding',
                'descricao': 'Prepare-se para milhões de usuários',
                'funcao': self._secao_escalabilidade_sharding
            },
            {
                'id': 'secao_nosql_vs_sql',
                'titulo': '🗂️ NoSQL vs SQL',
                'descricao': 'Escolha a tecnologia certa para cada caso',
                'funcao': self._secao_nosql_vs_sql
            },
            {
                'id': 'secao_monitoramento_otimizacao',
                'titulo': '📊 Monitoramento e Otimização',
                'descricao': 'Monitore e otimize performance continuamente',
                'funcao': self._secao_monitoramento_otimizacao
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
    
    def _secao_fundamentos_modelagem(self) -> None:
        """Seção: Fundamentos de Modelagem"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("FUNDAMENTOS DE MODELAGEM", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Modelagem de Banco de Dados",
            "O processo de criar uma estrutura abstrata para organizar e relacionar dados de forma eficiente e consistente"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Um bom design de banco pode fazer a diferença entre um sistema lento e um sistema ultra-rápido!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Modelar um banco de dados é como projetar uma biblioteca: você precisa organizar os livros (dados) em estantes (tabelas) com um sistema de catalogação (relacionamentos) que permita encontrar qualquer informação rapidamente!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === OS 3 NÍVEIS DE MODELAGEM ===
        self.print_colored("\n🔧 OS 3 NÍVEIS DE MODELAGEM:", "info")
        niveis = [
            "1. 📋 CONCEITUAL: Identifica entidades e relacionamentos do negócio",
            "2. 🔧 LÓGICA: Define estrutura sem depender de tecnologia específica",
            "3. 💻 FÍSICA: Implementação específica do SGBD escolhido"
        ]
        
        for i, nivel in enumerate(niveis, 1):
            self.print_colored(nivel, "text")
            if i < len(niveis):
                input("   ⏳ Pressione ENTER para o próximo nível...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO: SISTEMA E-COMMERCE:", "success")
        exemplo_modelagem = '''# MODELAGEM CONCEITUAL (ERD)
# Entidades principais e relacionamentos

ENTIDADES:
- Cliente (nome, email, telefone)
- Produto (nome, preço, descrição) 
- Pedido (data, status, total)
- ItemPedido (quantidade, preço_unitário)

RELACIONAMENTOS:
- Cliente 1:N Pedido (um cliente faz vários pedidos)
- Pedido 1:N ItemPedido (um pedido tem vários itens)
- Produto 1:N ItemPedido (um produto aparece em vários itens)

# MODELAGEM LÓGICA (Normalizada)
Cliente (id_cliente, nome, email, telefone)
Produto (id_produto, nome, preco, descricao)
Pedido (id_pedido, id_cliente*, data, status, total)
ItemPedido (id_pedido*, id_produto*, quantidade, preco_unitario)

# MODELAGEM FÍSICA (PostgreSQL)
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_clientes_email ON clientes(email);'''
        
        self.exemplo(exemplo_modelagem)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix: Modela usuários, filmes, visualizações e recomendações",
            "Uber: Relaciona motoristas, passageiros, viagens e pagamentos",
            "Instagram: Organiza usuários, posts, curtidas e seguidores",
            "Spotify: Conecta usuários, músicas, playlists e reproduções"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_normalizacao_desnormalizacao(self) -> None:
        """Seção: Normalização e Desnormalização"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("NORMALIZAÇÃO E DESNORMALIZAÇÃO", "🔧", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Normalização",
            "Processo de organizar dados para eliminar redundância e garantir integridade"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Normalização é como organizar seu guarda-roupa: em vez de ter 5 camisas iguais espalhadas, você guarda uma camisa no armário e anota onde ela está. Isso economiza espaço (armazenamento) e evita inconsistências!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === AS FORMAS NORMAIS ===
        self.print_colored("\n📊 AS FORMAS NORMAIS:", "success")
        formas_normais = [
            "1️⃣ 1FN: Eliminar grupos repetitivos (atributos multivalorados)",
            "2️⃣ 2FN: Eliminar dependências parciais da chave primária",
            "3️⃣ 3FN: Eliminar dependências transitivas",
            "🏆 BCNF: Forma mais rigorosa da 3FN"
        ]
        
        for forma in formas_normais:
            self.print_colored(forma, "text")
            input("   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO DE NORMALIZAÇÃO:", "success")
        exemplo_normalizacao = '''# TABELA NÃO NORMALIZADA (problemática)
pedidos_ruins (
    id, cliente_nome, cliente_email, produto1, preco1, 
    produto2, preco2, produto3, preco3, total
)

# PROBLEMAS:
# - Desperdício de espaço (campos vazios)
# - Dificuldade para consultar produtos
# - Inconsistência de dados

# APÓS NORMALIZAÇÃO (1FN, 2FN, 3FN)
clientes (
    id PRIMARY KEY,
    nome,
    email UNIQUE
)

produtos (
    id PRIMARY KEY,
    nome,
    preco
)

pedidos (
    id PRIMARY KEY,
    cliente_id REFERENCES clientes(id),
    data_pedido,
    total
)

itens_pedido (
    pedido_id REFERENCES pedidos(id),
    produto_id REFERENCES produtos(id),
    quantidade,
    preco_unitario,
    PRIMARY KEY (pedido_id, produto_id)
)

# BENEFÍCIOS:
# ✅ Sem redundância
# ✅ Fácil manutenção
# ✅ Integridade garantida'''
        
        self.exemplo(exemplo_normalizacao)
        
        # === QUANDO DESNORMALIZAR ===
        self.print_colored("\n⚡ QUANDO DESNORMALIZAR:", "warning")
        self.print_colored("Às vezes quebrar regras de normalização melhora performance!", "text")
        
        casos_desnormalizacao = [
            "Relatórios complexos com muitos JOINs",
            "Aplicações read-heavy (mais leitura que escrita)",
            "Sistemas de analytics e data warehouses",
            "Cache de dados calculados frequentemente"
        ]
        
        for caso in casos_desnormalizacao:
            self.print_colored(f"• {caso}", "primary")
        
        self.pausar()
    
    def _secao_indices_performance(self) -> None:
        """Seção: Índices e Performance"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ÍNDICES E PERFORMANCE", "⚡", "success")
        
        # === CONCEITO ===
        self.print_concept(
            "Índice de Banco de Dados",
            "Estrutura de dados que melhora a velocidade de consultas criando um 'atalho' para encontrar registros"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Um índice é como o índice de um livro: em vez de ler página por página para encontrar um tópico, você consulta o índice que te leva direto à página certa!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === TIPOS DE ÍNDICES ===
        self.print_colored("\n🔧 TIPOS DE ÍNDICES:", "info")
        tipos_indices = [
            "🌳 B-Tree: Padrão para buscas por igualdade e range",
            "🔍 Hash: Rápido para buscas por igualdade exata",
            "📊 GIN: Para dados compostos (arrays, JSON, texto)",
            "🎯 Partial: Apenas para subset de dados",
            "🔗 Composite: Múltiplas colunas em ordem específica"
        ]
        
        for tipo in tipos_indices:
            self.print_colored(tipo, "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO DE OTIMIZAÇÃO COM ÍNDICES:", "success")
        exemplo_indices = '''-- QUERY LENTA (sem índice)
SELECT * FROM usuarios 
WHERE email = 'joao@email.com';
-- Execution time: 2.5 seconds (scan completo)

-- CRIAR ÍNDICE
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- MESMA QUERY AGORA É RÁPIDA
SELECT * FROM usuarios 
WHERE email = 'joao@email.com';
-- Execution time: 0.002 seconds (1250x mais rápido!)

-- ÍNDICE COMPOSTO PARA QUERIES COMPLEXAS
CREATE INDEX idx_pedidos_status_data ON pedidos(status, data_criacao);

-- Otimiza queries como:
SELECT * FROM pedidos 
WHERE status = 'pendente' 
  AND data_criacao >= '2024-01-01'
ORDER BY data_criacao DESC;

-- ÍNDICE PARCIAL (apenas dados relevantes)
CREATE INDEX idx_usuarios_ativos_email 
ON usuarios(email) 
WHERE status = 'ativo';

-- ÍNDICE GIN PARA BUSCA EM JSON
CREATE INDEX idx_produtos_atributos 
ON produtos USING gin(atributos);

-- Permite buscar dentro de JSON:
SELECT * FROM produtos 
WHERE atributos @> '{"cor": "azul", "tamanho": "M"}';'''
        
        self.exemplo(exemplo_indices)
        
        # === DICAS DE PERFORMANCE ===
        self.print_colored("\n💡 DICAS DE PERFORMANCE:", "accent")
        dicas = [
            "Use EXPLAIN ANALYZE para analisar planos de execução",
            "Índices únicos são mais rápidos que índices normais",
            "Evite índices em colunas com muitos UPDATEs",
            "Monitore usage dos índices - remova os não utilizados"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "primary")
        
        self.pausar()
    
    def _secao_transactions_acid(self) -> None:
        """Seção: Transações e ACID"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("TRANSAÇÕES E ACID", "🔄", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Transação",
            "Sequência de operações de banco de dados que é executada como uma unidade indivisível - ou tudo acontece, ou nada acontece"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Uma transação é como transferir dinheiro entre contas bancárias: o dinheiro precisa sair de uma conta E entrar na outra. Se qualquer parte falhar, toda a operação é cancelada!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === PROPRIEDADES ACID ===
        self.print_colored("\n🔧 PROPRIEDADES ACID:", "info")
        acid_properties = [
            "⚛️ ATOMICIDADE: Tudo ou nada - não há meio termo",
            "🔒 CONSISTÊNCIA: Dados sempre em estado válido",
            "🔐 ISOLAMENTO: Transações não interferem entre si",
            "💾 DURABILIDADE: Dados persistem mesmo com falhas"
        ]
        
        for i, prop in enumerate(acid_properties, 1):
            self.print_colored(prop, "text")
            if i < len(acid_properties):
                input("   ⏳ Pressione ENTER para a próxima propriedade...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO: TRANSFERÊNCIA BANCÁRIA:", "success")
        exemplo_transaction = '''-- TRANSFERÊNCIA DE R$ 100 DA CONTA A PARA CONTA B
BEGIN;  -- Iniciar transação

    -- 1. Verificar saldo suficiente
    SELECT saldo FROM contas WHERE id = 'conta_a' FOR UPDATE;
    -- Resultado: R$ 500
    
    -- 2. Debitar da conta origem
    UPDATE contas 
    SET saldo = saldo - 100 
    WHERE id = 'conta_a';
    
    -- 3. Creditar na conta destino
    UPDATE contas 
    SET saldo = saldo + 100 
    WHERE id = 'conta_b';
    
    -- 4. Registrar histórico
    INSERT INTO transferencias (conta_origem, conta_destino, valor, data)
    VALUES ('conta_a', 'conta_b', 100, NOW());

COMMIT;  -- Confirmar todas as operações

-- SE ALGO FALHAR:
-- ROLLBACK;  -- Desfaz todas as operações'''
        
        self.exemplo(exemplo_transaction)
        
        # === NÍVEIS DE ISOLAMENTO ===
        self.print_colored("\n🔐 NÍVEIS DE ISOLAMENTO:", "accent")
        niveis = [
            "READ uncommitted: Pode ler dados não confirmados",
            "read committed: Lê apenas dados confirmados",
            "repeatable read: Mesmo resultado em múltiplas leituras",
            "serializable: Máximo isolamento - como execução sequencial"
        ]
        
        for nivel in niveis:
            self.print_colored(f"• {nivel}", "primary")
        
        self.pausar()
    
    def _secao_escalabilidade_sharding(self) -> None:
        """Seção: Escalabilidade e Sharding"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ESCALABILIDADE E SHARDING", "📈", "info")
        
        # === CONCEITO ===
        self.print_concept(
            "Sharding",
            "Técnica de divisão horizontal de dados onde grandes tabelas são particionadas em múltiplos bancos de dados"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO COTIDIANO:", "warning")
        self.print_colored("Sharding é como dividir uma biblioteca gigante em várias filiais por bairro: cada filial tem parte dos livros, mas juntas formam a coleção completa. Isso permite atender mais pessoas simultaneamente!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === ESTRATÉGIAS DE ESCALABILIDADE ===
        self.print_colored("\n🚀 ESTRATÉGIAS DE ESCALABILIDADE:", "success")
        estrategias = [
            "📈 ESCALA VERTICAL: Mais CPU, RAM, SSD no mesmo servidor",
            "📊 ESCALA HORIZONTAL: Mais servidores trabalhando juntos",
            "🔄 READ replicas: Cópias só-leitura para distribuir consultas",
            "🗂️ PARTICIONAMENTO: Dividir tabelas por critérios específicos",
            "📡 SHARDING: Distribuir dados entre múltiplos bancos"
        ]
        
        for estrategia in estrategias:
            self.print_colored(estrategia, "text")
        
        input("\n🔸 Pressione ENTER para ver exemplo...")
        
        # === EXEMPLO DE SHARDING ===
        self.print_colored("\n💻 EXEMPLO: SHARDING POR REGIÃO:", "success")
        exemplo_sharding = '''# ESTRATÉGIA: Dividir usuários por região geográfica

# SHARD 1: Usuários do Brasil
CREATE DATABASE ecommerce_br;
-- Tabelas: usuarios_br, pedidos_br, produtos_br

# SHARD 2: Usuários dos EUA  
CREATE DATABASE ecommerce_us;
-- Tabelas: usuarios_us, pedidos_us, produtos_us

# SHARD 3: Usuários da Europa
CREATE DATABASE ecommerce_eu;
-- Tabelas: usuarios_eu, pedidos_eu, produtos_eu

# ROTEADOR DE SHARD (Python)
class ShardRouter:
    def __init__(self):
        self.shards = {
            'BR': 'postgresql://user:pass@db-br:5432/ecommerce_br',
            'US': 'postgresql://user:pass@db-us:5432/ecommerce_us', 
            'EU': 'postgresql://user:pass@db-eu:5432/ecommerce_eu'
        }
    
    def get_shard(self, user_region):
        return self.shards.get(user_region, self.shards['BR'])
    
    def create_user(self, user_data):
        shard_db = self.get_shard(user_data['region'])
        # Conectar no shard correto e inserir usuário

# VANTAGENS:
# ✅ Cada região tem latência menor
# ✅ Pode escalar independentemente  
# ✅ Falha em uma região não afeta outras

# DESAFIOS:
# ⚠️ Queries cross-shard são complexas
# ⚠️ Rebalanceamento é difícil
# ⚠️ Transações distribuídas são caras'''
        
        self.exemplo(exemplo_sharding)
        
        # === ALTERNATIVAS AO SHARDING ===
        self.print_colored("\n🔧 ALTERNATIVAS ANTES DO SHARDING:", "warning")
        alternativas = [
            "Read replicas para distribuir leitura",
            "Cache agressivo (Redis, Memcached)",
            "Índices otimizados e query tuning",
            "Particionamento dentro do mesmo BD",
            "Arquitetura de microserviços"
        ]
        
        for alt in alternativas:
            self.print_colored(f"• {alt}", "primary")
        
        self.pausar()
    
    def _secao_nosql_vs_sql(self) -> None:
        """Seção: NoSQL vs SQL"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("NOSQL VS SQL", "🗂️", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "NoSQL",
            "Bancos de dados não-relacionais que oferecem flexibilidade de schema e escalabilidade horizontal"
        )
        
        # === COMPARAÇÃO ===
        self.print_colored("\n⚖️ COMPARAÇÃO SQL vs NoSQL:", "info")
        
        self.print_colored("\n🏛️ BANCOS SQL (Relacionais):", "success")
        sql_features = [
            "✅ ACID completo e transações complexas",
            "✅ Joins eficientes entre tabelas",
            "✅ Schema rígido garante consistência",
            "✅ SQL padronizado e amplamente conhecido",
            "❌ Escalabilidade vertical limitada",
            "❌ Schema fixo pode ser limitante"
        ]
        
        for feature in sql_features:
            self.print_colored(f"  {feature}", "text")
        
        input("\n🔸 Pressione ENTER para NoSQL...")
        
        self.print_colored("\n🗄️ BANCOS NoSQL:", "accent")
        nosql_features = [
            "✅ Escalabilidade horizontal nativa",
            "✅ Schema flexível para dados variados",
            "✅ Performance alta para operações simples",
            "✅ Melhor para big data e alta concorrência",
            "❌ Consistência eventual (não ACID completo)",
            "❌ Sem joins - dados podem ser duplicados"
        ]
        
        for feature in nosql_features:
            self.print_colored(f"  {feature}", "text")
        
        # === TIPOS DE NOSQL ===
        self.print_colored("\n🔧 TIPOS DE NOSQL:", "warning")
        tipos_nosql = [
            "📄 DOCUMENTO: MongoDB, CouchDB (JSON-like)",
            "🔑 CHAVE-VALOR: Redis, DynamoDB (hash tables)",
            "📊 COLUNA: Cassandra, HBase (big data)",
            "🕸️ GRAFO: Neo4j, Amazon Neptune (relacionamentos)"
        ]
        
        for tipo in tipos_nosql:
            self.print_colored(tipo, "text")
        
        input("\n🔸 Pressione ENTER para ver casos de uso...")
        
        # === CASOS DE USO ===
        self.print_colored("\n🎯 QUANDO USAR CADA UM:", "success")
        
        casos_uso = '''
🏛️ USE SQL QUANDO:
• Dados estruturados e relacionados
• Transações complexas são críticas
• Consultas com múltiplos joins
• Consistência é mais importante que performance
• Exemplo: Sistema bancário, e-commerce

🗄️ USE NoSQL QUANDO:
• Dados não-estruturados ou semi-estruturados
• Escala massiva é necessária
• Performance é crítica
• Schema pode mudar frequentemente
• Exemplo: Redes sociais, IoT, analytics

🤝 USE AMBOS (Polyglot Persistence):
• Diferentes partes do sistema têm necessidades diferentes
• SQL para transações, NoSQL para cache/analytics
• Exemplo: Netflix usa MySQL + Cassandra + Redis'''
        
        self.exemplo(casos_uso)
        
        self.pausar()
    
    def _secao_monitoramento_otimizacao(self) -> None:
        """Seção: Monitoramento e Otimização"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MONITORAMENTO E OTIMIZAÇÃO", "📊", "success")
        
        # === CONCEITO ===
        self.print_concept(
            "Monitoramento de Database",
            "Processo contínuo de coleta e análise de métricas para identificar gargalos e otimizar performance"
        )
        
        # === MÉTRICAS IMPORTANTES ===
        self.print_colored("\n📊 MÉTRICAS ESSENCIAIS PARA MONITORAR:", "info")
        metricas = [
            "⚡ Response Time: Tempo de resposta das queries",
            "🔥 CPU Usage: Utilização do processador",
            "💾 Memory Usage: Uso de RAM e cache",
            "💿 Disk I/O: Operações de leitura/escrita",
            "🔗 Connections: Número de conexões ativas",
            "🐌 Slow Queries: Queries que demoram muito",
            "📈 Throughput: Operações por segundo"
        ]
        
        for metrica in metricas:
            self.print_colored(metrica, "text")
        
        input("\n🔸 Pressione ENTER para ver ferramentas...")
        
        # === FERRAMENTAS DE MONITORAMENTO ===
        self.print_colored("\n🛠️ FERRAMENTAS DE MONITORAMENTO:", "warning")
        ferramentas = [
            "📊 pgAdmin, phpMyAdmin (interfaces gráficas)",
            "🔍 pg_stat_statements (análise de queries)",
            "📈 Prometheus + Grafana (métricas em tempo real)",
            "🚨 New Relic, DataDog (APM profissional)",
            "⚡ EXPLAIN ANALYZE (análise de plano de execução)"
        ]
        
        for ferramenta in ferramentas:
            self.print_colored(f"• {ferramenta}", "primary")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 EXEMPLO: OTIMIZAÇÃO DE QUERY LENTA:", "success")
        exemplo_otimizacao = '''-- 1. IDENTIFICAR QUERY LENTA
SELECT query, calls, total_time, mean_time 
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;

-- 2. ANALISAR PLANO DE EXECUÇÃO
EXPLAIN ANALYZE
SELECT u.nome, COUNT(p.id) as total_pedidos
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.nome
ORDER BY total_pedidos DESC;

-- RESULTADO ANTES DA OTIMIZAÇÃO:
-- Execution Time: 2847.392 ms

-- 3. IDENTIFICAR PROBLEMA
-- ❌ Seq Scan on usuarios (cost=0.00..1234.56)
-- ❌ Hash Join (cost=5678.90..12345.67)

-- 4. CRIAR ÍNDICES ESTRATÉGICOS
CREATE INDEX idx_usuarios_created_at ON usuarios(created_at);
CREATE INDEX idx_pedidos_usuario_id ON pedidos(usuario_id);

-- 5. VERIFICAR MELHORIA
-- ✅ Index Scan using idx_usuarios_created_at
-- ✅ Execution Time: 23.456 ms (121x mais rápido!)

-- 6. MONITORAR CONTINUAMENTE
-- Configurar alerta para queries > 1 segundo'''
        
        self.exemplo(exemplo_otimizacao)
        
        # === DICAS DE OTIMIZAÇÃO ===
        self.print_colored("\n💡 DICAS DE OTIMIZAÇÃO:", "accent")
        dicas_otimizacao = [
            "Use índices nas colunas do WHERE e JOIN",
            "Evite SELECT * - busque apenas colunas necessárias",
            "Use LIMIT para evitar resultados gigantes",
            "Monitore queries que fazem Seq Scan",
            "Mantenha estatísticas atualizadas (ANALYZE)",
            "Configure connection pooling adequadamente"
        ]
        
        for dica in dicas_otimizacao:
            self.print_colored(f"• {dica}", "primary")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar seus conhecimentos de database design com exercícios práticos!", "text")
        
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
                'title': 'Quiz: Conhecimentos Database Design',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual forma normal elimina dependências transitivas?',
                        'answer': ['3nf', 'terceira forma normal', '3fn'],
                        'hint': 'É a terceira forma normal'
                    },
                    {
                        'question': 'Qual tipo de índice é melhor para buscas por igualdade exata?',
                        'answer': ['hash', 'indice hash'],
                        'hint': 'Pense em tabelas hash - muito rápidas para busca exata'
                    },
                    {
                        'question': 'O que significa ACID em bancos de dados?',
                        'answer': ['atomicidade consistencia isolamento durabilidade', 'atomicity consistency isolation durability'],
                        'hint': 'São 4 propriedades fundamentais das transações'
                    },
                    {
                        'question': 'Qual comando SQL analisa o plano de execução de uma query?',
                        'answer': ['explain', 'explain analyze'],
                        'hint': 'Comando que "explica" como a query será executada'
                    },
                    {
                        'question': 'Qual é a principal vantagem do sharding?',
                        'answer': ['escalabilidade horizontal', 'escala horizontal', 'distribuir dados'],
                        'hint': 'Permite crescer horizontalmente adicionando mais servidores'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a criação de tabela normalizada',
                        'starter': '''CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    -- Complete: adicione chave estrangeira para usuario
    
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL
);''',
                        'solution': '''usuario_id INTEGER NOT NULL REFERENCES usuarios(id),''',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a criação de índice composto',
                        'starter': '''-- Otimizar query que busca pedidos por status e data
SELECT * FROM pedidos 
WHERE status = 'pendente' 
  AND data_pedido >= '2024-01-01'
ORDER BY data_pedido DESC;

-- Complete: crie índice composto otimizado
CREATE INDEX idx_pedidos___ ON pedidos(___);''',
                        'solution': '''CREATE INDEX idx_pedidos_status_data ON pedidos(status, data_pedido);''',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a transação para transferência',
                        'starter': '''-- Transferir R$ 100 da conta A para conta B
BEGIN;
    -- Complete: verificar saldo e fazer as operações
    SELECT saldo FROM contas WHERE id = 'conta_a' FOR UPDATE;
    
    -- Debitar da conta origem
    ___
    
    -- Creditar na conta destino  
    ___
    
COMMIT;''',
                        'solution': '''UPDATE contas SET saldo = saldo - 100 WHERE id = 'conta_a';
    UPDATE contas SET saldo = saldo + 100 WHERE id = 'conta_b';''',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Projete um Sistema de Database',
                'type': 'creative',
                'instruction': 'Projete o modelo de banco de dados para um sistema de sua escolha (rede social, streaming, delivery, etc.). Inclua: entidades principais, relacionamentos, índices necessários e estratégia de escalabilidade!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre database design",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos SQL",
            "🎨 OPÇÃO 3 - Exercício Criativo: Projete um sistema completo",
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
            self.print_success("🌟 Excelente! Você domina database design!")
        elif percentage >= 60:
            self.print_colored("👍 Bom trabalho! Continue praticando!", "warning")
        else:
            self.print_colored("💪 Continue estudando! Database design requer prática!", "text")
        
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
                        self.print_tip("💡 Dica: Chaves estrangeiras garantem integridade referencial!")
                    elif ex['type'] == 'intermediate':
                        self.print_tip("💡 Dica: Ordem das colunas no índice composto importa!")
                    else:
                        self.print_tip("💡 Dica: FOR UPDATE trava registros durante a transação!")
                
                input("\n🔸 Pressione ENTER para continuar...")
                
            except KeyboardInterrupt:
                raise
            except Exception:
                self.print_warning("❌ Erro ao processar resposta.")
    
    def _run_creative_exercise(self, exercise_data: Dict[str, Any]) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "success")
        
        self.print_colored(f"\n📋 {exercise_data['instruction']}", "warning")
        
        self.print_colored("\n💡 IDEIAS PARA SEU PROJETO:", "info")
        ideias = [
            "• 📱 Rede Social: usuários, posts, curtidas, seguindo",
            "• 🎬 Streaming: filmes, usuários, visualizações, avaliações",
            "• 🛍️ E-commerce: produtos, pedidos, carrinho, pagamentos",
            "• 🚗 Delivery: restaurantes, pratos, pedidos, entregadores",
            "• 🏠 Imobiliária: imóveis, proprietários, interessados, visitas",
            "• 📚 Educação: cursos, alunos, aulas, notas, progresso"
        ]
        
        for ideia in ideias:
            self.print_colored(ideia, "text")
        
        self.print_colored("\n🎯 CONSIDERE EM SEU DESIGN:", "success")
        consideracoes = [
            "📊 Entidades principais e seus atributos",
            "🔗 Relacionamentos entre entidades (1:1, 1:N, N:N)",
            "🔑 Chaves primárias e estrangeiras",
            "📐 Normalização adequada (3FN)",
            "⚡ Índices para queries frequentes",
            "📈 Estratégia de escalabilidade",
            "🔒 Considerações de segurança",
            "💾 Estimativa de volume de dados"
        ]
        
        for consideracao in consideracoes:
            self.print_colored(consideracao, "text")
        
        self.print_colored("\n📝 EXEMPLO DE ESTRUTURA:", "accent")
        exemplo_estrutura = '''# SISTEMA: [Nome do seu sistema]

## ENTIDADES PRINCIPAIS:
- Entidade1 (atributo1, atributo2, ...)
- Entidade2 (atributo1, atributo2, ...)
- Entidade3 (atributo1, atributo2, ...)

## RELACIONAMENTOS:
- Entidade1 1:N Entidade2
- Entidade2 N:N Entidade3

## TABELAS SQL:
CREATE TABLE entidade1 (...);
CREATE TABLE entidade2 (...);

## ÍNDICES ESTRATÉGICOS:
CREATE INDEX idx_... ON tabela(coluna);

## ESCALABILIDADE:
- Estratégia para crescimento
- Possível sharding por...'''
        
        self.exemplo(exemplo_estrutura)
        
        input("\n🔸 Pressione ENTER quando terminar seu projeto...")
        
        self.print_success("🎉 Excelente! Projetar sistemas de database é uma habilidade fundamental!")
        self.print_tip("💡 Pratique modelando diferentes tipos de sistemas para ganhar experiência!")
    
    def _mini_projeto_sistema_database_enterprise(self) -> None:
        """Mini Projeto - Sistema de Database Enterprise"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DATABASE ENTERPRISE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DATABASE ENTERPRISE")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema de database enterprise completo!")
        
        self.print_concept(
            "Sistema Multi-tenant SaaS",
            "Plataforma que serve múltiplos clientes (tenants) com isolamento de dados e escalabilidade horizontal"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "Salesforce para CRM de milhares de empresas",
            "Slack para comunicação de equipes globais",
            "Shopify para e-commerce de milhões de lojas",
            "Notion para produtividade de empresas e usuários"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        input("\n🔸 Pressione ENTER para começar...")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Arquitetura do Sistema
        self.print_section("PASSO 1: ARQUITETURA MULTI-TENANT", "🏗️", "info")
        self.print_tip("Vamos projetar um sistema que isola dados de diferentes clientes!")
        
        arquitetura = '''# ARQUITETURA ESCOLHIDA: Schema por Tenant
# Cada cliente tem seu próprio schema no banco

VANTAGENS:
✅ Isolamento completo de dados
✅ Backup e restore por cliente
✅ Customização por tenant
✅ Compliance e segurança

ESTRUTURA:
- Schema "public": Tabelas globais (tenants, configurações)
- Schema "tenant_empresa_a": Dados da Empresa A
- Schema "tenant_startup_x": Dados da Startup X
- Schema "tenant_unicorp": Dados da Unicorp

TECNOLOGIAS:
🗄️ PostgreSQL (database principal)
🔄 Redis (cache distribuído)
📊 Prometheus (métricas)
🐳 Docker (containerização)'''
        
        self.exemplo(arquitetura)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 2: Modelagem de Dados
        self.print_section("PASSO 2: MODELAGEM DE DADOS", "📊", "success")
        
        modelagem = '''-- ========================================
-- TABELAS GLOBAIS (Schema: public)
-- ========================================

-- Gerenciamento de tenants
CREATE TABLE public.tenants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    schema_name VARCHAR(50) UNIQUE NOT NULL,
    
    -- Configurações do plano
    plan VARCHAR(20) DEFAULT 'basic' CHECK (plan IN ('basic', 'pro', 'enterprise')),
    max_users INTEGER DEFAULT 10,
    max_storage_gb INTEGER DEFAULT 5,
    features JSONB DEFAULT '{}',
    
    -- Status e métricas
    status VARCHAR(20) DEFAULT 'active',
    users_count INTEGER DEFAULT 0,
    storage_used_gb DECIMAL(8,2) DEFAULT 0,
    
    -- Auditoria
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_activity TIMESTAMP WITH TIME ZONE
);

-- ========================================
-- ESTRUTURA POR TENANT
-- ========================================

-- Usuários do tenant
CREATE TABLE %tenant_schema%.users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(200) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    
    -- Perfil
    avatar_url VARCHAR(500),
    phone VARCHAR(20),
    timezone VARCHAR(50) DEFAULT 'UTC',
    language VARCHAR(5) DEFAULT 'pt-BR',
    
    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    last_login TIMESTAMP WITH TIME ZONE,
    
    -- Auditoria
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Projetos
CREATE TABLE %tenant_schema%.projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    owner_id UUID NOT NULL REFERENCES %tenant_schema%.users(id),
    
    -- Configurações
    status VARCHAR(20) DEFAULT 'active',
    priority VARCHAR(10) DEFAULT 'medium',
    color VARCHAR(7), -- hex color
    
    -- Datas importantes
    start_date DATE,
    due_date DATE,
    completed_at TIMESTAMP WITH TIME ZONE,
    
    -- Auditoria
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tarefas
CREATE TABLE %tenant_schema%.tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES %tenant_schema%.projects(id) ON DELETE CASCADE,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    
    -- Atribuição
    assignee_id UUID REFERENCES %tenant_schema%.users(id),
    reporter_id UUID NOT NULL REFERENCES %tenant_schema%.users(id),
    
    -- Status e prioridade
    status VARCHAR(20) DEFAULT 'todo' CHECK (
        status IN ('todo', 'in_progress', 'review', 'done', 'cancelled')
    ),
    priority VARCHAR(10) DEFAULT 'medium' CHECK (
        priority IN ('low', 'medium', 'high', 'urgent')
    ),
    
    -- Estimativas e tempo
    estimated_hours DECIMAL(5,2),
    actual_hours DECIMAL(5,2),
    due_date TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    
    -- Metadados
    tags JSONB,
    custom_fields JSONB,
    
    -- Auditoria
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);'''
        
        self.exemplo(modelagem)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 3: Índices e Performance
        self.print_section("PASSO 3: ÍNDICES ESTRATÉGICOS", "⚡", "warning")
        
        indices = '''-- ========================================
-- ÍNDICES PARA PERFORMANCE
-- ========================================

-- Tenants (consultas globais)
CREATE INDEX idx_tenants_slug ON public.tenants(slug);
CREATE INDEX idx_tenants_status ON public.tenants(status);
CREATE INDEX idx_tenants_plan ON public.tenants(plan);

-- Usuários por tenant
CREATE INDEX idx_users_email ON %tenant_schema%.users(email);
CREATE INDEX idx_users_role_active ON %tenant_schema%.users(role, is_active);
CREATE INDEX idx_users_last_login ON %tenant_schema%.users(last_login);

-- Projetos
CREATE INDEX idx_projects_owner ON %tenant_schema%.projects(owner_id);
CREATE INDEX idx_projects_status_due ON %tenant_schema%.projects(status, due_date);

-- Tarefas (queries mais complexas)
CREATE INDEX idx_tasks_project ON %tenant_schema%.tasks(project_id);
CREATE INDEX idx_tasks_assignee_status ON %tenant_schema%.tasks(assignee_id, status);
CREATE INDEX idx_tasks_due_date ON %tenant_schema%.tasks(due_date) WHERE due_date IS NOT NULL;
CREATE INDEX idx_tasks_status_priority ON %tenant_schema%.tasks(status, priority);

-- Índice GIN para busca em JSON
CREATE INDEX idx_tasks_tags ON %tenant_schema%.tasks USING gin(tags);
CREATE INDEX idx_tasks_custom_fields ON %tenant_schema%.tasks USING gin(custom_fields);

-- Índice de texto completo
CREATE INDEX idx_tasks_search ON %tenant_schema%.tasks 
USING gin(to_tsvector('portuguese', title || ' ' || COALESCE(description, '')));'''
        
        self.exemplo(indices)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 4: Sharding e Escalabilidade
        self.print_section("PASSO 4: SHARDING E ESCALABILIDADE", "📈", "success")
        
        sharding = '''# ========================================
# ESTRATÉGIA DE SHARDING
# ========================================

# SHARD CONFIGURATION
shards = {
    'shard_0': {
        'host': 'db-shard-0.empresa.com',
        'database': 'saas_shard_0',
        'tenants': ['tenant_empresa_a', 'tenant_startup_x'],
        'max_tenants': 1000
    },
    'shard_1': {
        'host': 'db-shard-1.empresa.com', 
        'database': 'saas_shard_1',
        'tenants': ['tenant_unicorp', 'tenant_techfirm'],
        'max_tenants': 1000
    },
    'shard_2': {
        'host': 'db-shard-2.empresa.com',
        'database': 'saas_shard_2', 
        'tenants': [],
        'max_tenants': 1000
    }
}

# PYTHON: Shard Router
class TenantRouter:
    def __init__(self):
        self.shard_config = self._load_shard_config()
    
    def get_shard_for_tenant(self, tenant_slug: str) -> dict:
        """Determinar qual shard contém o tenant"""
        # Hash baseado no slug do tenant
        shard_id = hash(tenant_slug) % len(self.shard_config)
        return self.shard_config[f'shard_{shard_id}']
    
    def get_connection(self, tenant_slug: str):
        """Obter conexão para o shard correto"""
        shard = self.get_shard_for_tenant(tenant_slug)
        return create_engine(
            f"postgresql://user:pass@{shard['host']}/{shard['database']}"
        )
    
    def create_tenant_schema(self, tenant_slug: str):
        """Criar schema para novo tenant"""
        shard = self.get_shard_for_tenant(tenant_slug)
        schema_name = f"tenant_{tenant_slug}"
        
        # Executar DDL no shard correto
        with self.get_connection(tenant_slug).connect() as conn:
            conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
            # Criar todas as tabelas do tenant
            self._create_tenant_tables(conn, schema_name)'''
        
        self.exemplo(sharding)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 5: Sistema de Cache
        self.print_section("PASSO 5: CACHE DISTRIBUÍDO", "💾", "info")
        
        cache_sistema = '''# ========================================
# CACHE INTELIGENTE COM REDIS
# ========================================

import redis
import json
import hashlib
from typing import Optional, Any

class SmartCache:
    def __init__(self):
        # Redis Cluster para alta disponibilidade
        self.redis = redis.Redis(
            host='redis-cluster.empresa.com',
            port=6379,
            decode_responses=True
        )
    
    def cache_key(self, tenant: str, entity: str, *args) -> str:
        """Gerar chave de cache hierárquica"""
        key_parts = [tenant, entity] + list(map(str, args))
        return ":".join(key_parts)
    
    def get_user_projects(self, tenant: str, user_id: str) -> Optional[list]:
        """Cache de projetos do usuário"""
        key = self.cache_key(tenant, "user_projects", user_id)
        cached = self.redis.get(key)
        return json.loads(cached) if cached else None
    
    def set_user_projects(self, tenant: str, user_id: str, projects: list, ttl: int = 300):
        """Cachear projetos do usuário"""
        key = self.cache_key(tenant, "user_projects", user_id)
        self.redis.setex(key, ttl, json.dumps(projects, default=str))
    
    def invalidate_user_cache(self, tenant: str, user_id: str):
        """Invalidar todo cache do usuário"""
        pattern = self.cache_key(tenant, "*", user_id, "*")
        keys = self.redis.keys(pattern)
        if keys:
            self.redis.delete(*keys)

# CACHE INTELIGENTE COM WARMING
class CacheWarmer:
    def __init__(self, cache: SmartCache, db_router):
        self.cache = cache
        self.db = db_router
    
    def warm_tenant_data(self, tenant_slug: str):
        """Pre-aquecer cache com dados frequentes"""
        # Buscar usuários ativos
        active_users = self._get_active_users(tenant_slug)
        
        for user in active_users:
            # Cache projetos do usuário
            projects = self._get_user_projects(tenant_slug, user['id'])
            self.cache.set_user_projects(tenant_slug, user['id'], projects)
            
            # Cache tarefas pendentes
            tasks = self._get_pending_tasks(tenant_slug, user['id'])
            self.cache.set_user_tasks(tenant_slug, user['id'], tasks)'''
        
        self.exemplo(cache_sistema)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # PASSO 6: Monitoramento
        self.print_section("PASSO 6: MONITORAMENTO AVANÇADO", "📊", "warning")
        
        monitoramento = '''# ========================================
# MONITORAMENTO ENTERPRISE
# ========================================

-- Métricas por tenant
CREATE VIEW public.tenant_metrics AS
SELECT 
    t.slug as tenant_slug,
    t.name as tenant_name,
    t.plan,
    t.users_count,
    t.storage_used_gb,
    
    -- Atividade recente
    EXTRACT(DAYS FROM (CURRENT_TIMESTAMP - t.last_activity)) as days_since_activity,
    
    -- Limites
    CASE 
        WHEN t.users_count > t.max_users * 0.9 THEN 'WARNING'
        WHEN t.users_count > t.max_users THEN 'CRITICAL'
        ELSE 'OK'
    END as user_limit_status,
    
    CASE 
        WHEN t.storage_used_gb > t.max_storage_gb * 0.9 THEN 'WARNING'
        WHEN t.storage_used_gb > t.max_storage_gb THEN 'CRITICAL'
        ELSE 'OK'
    END as storage_limit_status
    
FROM public.tenants t;

# PYTHON: Sistema de Alertas
class TenantMonitor:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def check_tenant_health(self) -> List[dict]:
        """Verificar saúde de todos os tenants"""
        query = """
        SELECT * FROM public.tenant_metrics 
        WHERE user_limit_status != 'OK' 
           OR storage_limit_status != 'OK'
           OR days_since_activity > 30
        """
        return self.db.execute(query).fetchall()
    
    def get_slow_queries_by_tenant(self, tenant_schema: str) -> List[dict]:
        """Queries lentas por tenant"""
        query = f"""
        SELECT 
            query,
            calls,
            total_time,
            mean_time,
            rows
        FROM pg_stat_statements 
        WHERE query LIKE '%{tenant_schema}%'
          AND mean_time > 1000  -- > 1 segundo
        ORDER BY total_time DESC
        LIMIT 20
        """
        return self.db.execute(query).fetchall()
    
    def get_tenant_activity_summary(self, tenant_schema: str) -> dict:
        """Resumo de atividade do tenant"""
        # Usar conexão do shard correto
        queries = {
            'active_users': f"SELECT COUNT(*) FROM {tenant_schema}.users WHERE is_active = true",
            'total_projects': f"SELECT COUNT(*) FROM {tenant_schema}.projects WHERE status = 'active'",
            'pending_tasks': f"SELECT COUNT(*) FROM {tenant_schema}.tasks WHERE status IN ('todo', 'in_progress')",
            'completed_today': f"""
                SELECT COUNT(*) FROM {tenant_schema}.tasks 
                WHERE status = 'done' AND completed_at >= CURRENT_DATE
            """
        }
        
        results = {}
        for metric, query in queries.items():
            results[metric] = self.db.execute(query).scalar()
        
        return results'''
        
        self.exemplo(monitoramento)
        
        # === RESULTADO FINAL ===
        self.print_section("SISTEMA ENTERPRISE COMPLETO!", "🎉", "success")
        
        self.print_colored("\n🏆 PARABÉNS! Você criou um sistema database enterprise com:", "warning")
        componentes = [
            "✅ Arquitetura multi-tenant com isolamento completo",
            "✅ Sharding horizontal para escalabilidade massiva",
            "✅ Sistema de cache distribuído inteligente",
            "✅ Índices otimizados para performance",
            "✅ Monitoramento avançado por tenant",
            "✅ Métricas e alertas automatizados",
            "✅ Estratégia de backup por cliente",
            "✅ Escalabilidade para milhões de usuários",
            "✅ Compliance e isolamento de dados",
            "✅ Performance otimizada para SaaS"
        ]
        
        for componente in componentes:
            self.print_colored(componente, "text")
        
        # === CASOS DE USO REAIS ===
        self.print_section("APLICAÇÕES NO MUNDO REAL", "🌍", "info")
        aplicacoes_reais = [
            "🏢 SaaS com 50.000+ empresas clientes",
            "👥 10M+ usuários distribuídos globalmente",
            "📊 100GB+ de dados por cliente enterprise",
            "⚡ <50ms response time médio",
            "🔄 99.99% uptime com failover automático",
            "🌍 Deploy em múltiplas regiões (AWS/Azure)",
            "💰 Billing automático por uso e features",
            "🔒 Compliance SOC2, GDPR, HIPAA ready"
        ]
        
        for aplicacao in aplicacoes_reais:
            self.print_colored(aplicacao, "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Database Architect!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema Database Enterprise Multi-tenant")
        
        self.pausar()