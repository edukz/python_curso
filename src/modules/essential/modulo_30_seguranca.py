#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 30: Segurança
Aprenda criptografia, validação, autenticação e boas práticas de segurança
"""

import time
import hashlib
import secrets
import re
import base64
from typing import Dict, List, Optional
from ..shared.base_module import BaseModule


class Modulo30Seguranca(BaseModule):
    """Módulo 30: Segurança - Programação Segura e Proteção de Dados"""
    
    def __init__(self):
        super().__init__("modulo_30", "Segurança")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo Segurança"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._seguranca_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _seguranca_principal(self) -> None:
        """Conteúdo principal do módulo Segurança"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛡️ MÓDULO 30: SEGURANÇA DIGITAL")
        else:
            print("\n" + "="*50)
            print("🛡️ MÓDULO 30: SEGURANÇA DIGITAL")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🛡️ Bem-vindo ao mundo da proteção digital! Vamos aprender a defender nossos códigos e dados!")
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
            self._mini_projeto_centro_seguranca()
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
                'titulo': '🎯 O que é segurança digital?',
                'descricao': 'Entenda os pilares da segurança na programação',
                'funcao': self._secao_conceitos_fundamentais
            },
            {
                'id': 'secao_criptografia_basica',
                'titulo': '🔐 Criptografia e hashing',
                'descricao': 'Aprenda a proteger dados com matemática avançada',
                'funcao': self._secao_criptografia_basica
            },
            {
                'id': 'secao_validacao_entrada',
                'titulo': '🔍 Validação de entrada',
                'descricao': 'Como proteger-se contra dados maliciosos',
                'funcao': self._secao_validacao_entrada
            },
            {
                'id': 'secao_geracao_senhas',
                'titulo': '🔑 Geração de senhas seguras',
                'descricao': 'Crie senhas impossíveis de quebrar',
                'funcao': self._secao_geracao_senhas
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas de segurança',
                'descricao': 'Dicas essenciais de profissionais',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros fatais de segurança',
                'descricao': 'Aprenda com os erros que custaram milhões',
                'funcao': self._secao_erros_comuns
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre hackers e segurança',
                'descricao': 'Histórias fascinantes do mundo digital',
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
        """Seção: O que é segurança digital?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É SEGURANÇA DIGITAL?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Segurança Digital",
            "É o conjunto de práticas e técnicas para proteger informações, sistemas e dados contra acessos não autorizados, ataques maliciosos e vazamentos."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Segurança não é um produto que você compra, é um processo que você implementa!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine sua casa: você tem fechaduras (autenticação), alarme (monitoramento), cofre (criptografia) e não deixa a chave embaixo do tapete (boas práticas). Segurança digital funciona igual!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 OS PILARES DA SEGURANÇA DIGITAL:", "info")
        pilares = [
            "1. 🔐 CONFIDENCIALIDADE - Só quem deve ver, vê",
            "2. 🛡️ INTEGRIDADE - Os dados não foram alterados",
            "3. ⚡ DISPONIBILIDADE - Sistema funciona quando precisa",
            "4. 🔍 AUTENTICAÇÃO - Confirma quem é o usuário",
            "5. 📋 AUTORIZAÇÃO - Define o que cada um pode fazer"
        ]
        
        for i, pilar in enumerate(pilares, 1):
            self.print_colored(pilar, "text")
            if i < len(pilares):
                input("   ⏳ Pressione ENTER para o próximo pilar...")
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏦 Bancos - Protegem bilhões em transações diárias",
            "🏥 Hospitais - Protegem dados médicos confidenciais",
            "🛒 E-commerce - Protegem dados de cartão de crédito",
            "🎮 Games - Protegem contas e conquistas dos jogadores",
            "📱 Apps - Protegem fotos, mensagens e localização",
            "🏢 Empresas - Protegem segredos industriais"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_criptografia_basica(self) -> None:
        """Seção: Criptografia e hashing"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CRIPTOGRAFIA E HASHING", "🔐", "success")
        
        # === CONCEITO PRINCIPAL ===
        self.print_concept(
            "Criptografia",
            "É a arte de transformar informações em códigos secretos, de forma que só quem tem a 'chave' pode entender o conteúdo original."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como escrever uma carta em código secreto que só seu melhor amigo entende, mas usando matemática super avançada!", "text")
        input("\n🔸 Pressione ENTER para ver exemplos...")
        
        # === EXEMPLO PRÁTICO 1: HASH ===
        self.print_colored("\n💻 EXEMPLO 1: HASHING (IMPRESSÃO DIGITAL)", "success")
        codigo_hash = '''import hashlib

# Texto original
texto = "MinhasSenhaSecreta123"
print(f"Texto original: {texto}")

# Gera hash SHA-256 (irreversível)
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"Hash SHA-256: {hash_sha256}")

# Mesmo texto sempre gera o mesmo hash
texto2 = "MinhasSenhaSecreta123"
hash2 = hashlib.sha256(texto2.encode()).hexdigest()
print(f"Mesmo texto, mesmo hash: {hash2 == hash_sha256}")'''
        
        self.exemplo(codigo_hash)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_hash)
        
        input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        # === EXEMPLO PRÁTICO 2: CODIFICAÇÃO BASE64 ===
        self.print_colored("\n💻 EXEMPLO 2: CODIFICAÇÃO BASE64", "success")
        codigo_base64 = '''import base64

# Mensagem original
mensagem = "Dados secretos da empresa!"
print(f"Mensagem original: {mensagem}")

# Codifica em Base64
mensagem_bytes = mensagem.encode('utf-8')
mensagem_codificada = base64.b64encode(mensagem_bytes).decode('utf-8')
print(f"Codificada: {mensagem_codificada}")

# Decodifica de volta
mensagem_decodificada = base64.b64decode(mensagem_codificada).decode('utf-8')
print(f"Decodificada: {mensagem_decodificada}")'''
        
        self.exemplo(codigo_base64)
        print("\n🚀 Executando exemplo:")
        self.executar_codigo(codigo_base64)
        
        # === APLICAÇÕES REAIS ===
        self.print_colored("\n🌍 ONDE É USADO:", "accent")
        usos = [
            "🔐 WhatsApp - Criptografia ponta a ponta",
            "💳 Cartões - Dados do chip são criptografados", 
            "🌐 HTTPS - Todo site seguro usa criptografia",
            "💾 Bancos de dados - Senhas são armazenadas como hash",
            "📧 Email - Gmail usa criptografia para proteger emails"
        ]
        for uso in usos:
            self.print_colored(f"• {uso}", "primary")
        
        self.pausar()
    
    def _secao_validacao_entrada(self) -> None:
        """Seção: Validação de entrada"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("VALIDAÇÃO DE ENTRADA", "🔍", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Validação de Entrada",
            "É o processo de verificar e filtrar todos os dados que entram no seu programa, garantindo que sejam seguros e válidos antes de processá-los."
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("É como ter um segurança na porta da festa: ele verifica se cada pessoa tem convite válido e não está trazendo nada perigoso!", "text")
        input("\n🔸 Pressione ENTER para ver os perigos...")
        
        # === EXEMPLO DE ATAQUE ===
        self.print_colored("\n⚠️ EXEMPLO DE ATAQUE: INJEÇÃO SQL", "error")
        self.print_colored("❌ CÓDIGO PERIGOSO (NUNCA FAÇA ISSO):", "error")
        codigo_perigoso = '''# ❌ PERIGO: Concatenação direta (vulnerável)
def buscar_usuario(nome):
    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"
    return executar_sql(query)

# Se alguém digitar: '; DROP TABLE usuarios; --
# A query fica: SELECT * FROM usuarios WHERE nome = ''; DROP TABLE usuarios; --'
# Resultado: TABELA DELETADA! 💥'''
        
        self.exemplo(codigo_perigoso)
        
        input("\n🔸 Pressione ENTER para ver a solução...")
        
        # === CÓDIGO SEGURO ===
        self.print_colored("\n✅ CÓDIGO SEGURO COM VALIDAÇÃO:", "success")
        codigo_seguro = r'''import re

def validar_entrada_segura(entrada):
    """Valida entrada do usuário de forma segura"""
    
    # 1. Verificar se não está vazio
    if not entrada or not entrada.strip():
        return False, "Entrada não pode estar vazia"
    
    # 2. Limitar tamanho
    if len(entrada.strip()) > 50:
        return False, "Entrada muito longa (máximo 50 caracteres)"
    
    # 3. Permitir apenas caracteres seguros
    if not re.match(r'^[a-zA-Z0-9\s_-]+$', entrada.strip()):
        return False, "Caracteres inválidos detectados"
    
    return True, "Entrada válida"

# Testando validação
entradas_teste = [
    "João Silva",           # ✅ Válido
    "user123",             # ✅ Válido  
    "'; DROP TABLE users;", # ❌ Inválido
    "<script>alert('hack')</script>", # ❌ Inválido
    "a" * 60,              # ❌ Muito longo
    ""                     # ❌ Vazio
]

for entrada in entradas_teste:
    valido, mensagem = validar_entrada_segura(entrada)
    status = "✅" if valido else "❌"
    print(f"{status} '{entrada[:20]}...' - {mensagem}")'''
        
        self.exemplo(codigo_seguro)
        print("\n🚀 Executando validação:")
        self.executar_codigo(codigo_seguro)
        
        # === TIPOS DE VALIDAÇÃO ===
        self.print_colored("\n🛡️ TIPOS DE VALIDAÇÃO ESSENCIAIS:", "info")
        tipos = [
            "📏 TAMANHO - Limite máximo e mínimo",
            "🔤 FORMATO - Regex para padrões válidos",
            "🚫 LISTA NEGRA - Bloquear caracteres perigosos",
            "✅ LISTA BRANCA - Permitir apenas caracteres seguros",
            "🔢 TIPO - Verificar se é número, email, etc.",
            "🧼 SANITIZAÇÃO - Limpar dados antes de usar"
        ]
        for tipo in tipos:
            self.print_colored(f"• {tipo}", "text")
        
        self.pausar()
    
    def _secao_geracao_senhas(self) -> None:
        """Seção: Geração de senhas seguras"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("GERAÇÃO DE SENHAS SEGURAS", "🔑", "accent")
        
        # === CONCEITO ===
        self.print_concept(
            "Senha Segura",
            "É uma combinação de caracteres longa, aleatória e única que serve como primeira linha de defesa contra invasores."
        )
        
        # === ESTATÍSTICAS ASSUSTADORAS ===
        self.print_colored("\n📊 ESTATÍSTICAS QUE ASSUSTAM:", "error")
        stats = [
            "😱 '123456' é ainda a senha mais usada no mundo",
            "⚡ Computador comum quebra senha de 6 dígitos em 2 segundos",
            "🏆 Senha de 12 caracteres aleatórios: 200 anos para quebrar",
            "💰 81% dos vazamentos são por senhas fracas",
            "🎯 Hackers testam milhões de senhas por segundo"
        ]
        for stat in stats:
            self.print_colored(f"• {stat}", "text")
        
        input("\n🔸 Pressione ENTER para aprender a se defender...")
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n💻 GERADOR DE SENHAS SUPER SEGURAS:", "success")
        codigo_gerador = '''import secrets
import string

def gerar_senha_segura(tamanho=12, incluir_simbolos=True):
    """Gera senha criptograficamente segura"""
    
    # Caracteres disponíveis
    letras = string.ascii_letters  # a-z, A-Z
    numeros = string.digits        # 0-9
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?" if incluir_simbolos else ""
    
    # Conjunto completo de caracteres
    todos_caracteres = letras + numeros + simbolos
    
    # Gerar senha aleatória usando secrets (mais seguro que random)
    senha = ''.join(secrets.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

def avaliar_forca_senha(senha):
    """Avalia a força da senha"""
    pontos = 0
    feedback = []
    
    # Comprimento
    if len(senha) >= 12:
        pontos += 3
        feedback.append("✅ Comprimento adequado")
    elif len(senha) >= 8:
        pontos += 2
        feedback.append("⚠️ Comprimento mínimo")
    else:
        feedback.append("❌ Muito curta")
    
    # Tipos de caracteres
    if any(c.islower() for c in senha):
        pontos += 1
        feedback.append("✅ Tem minúsculas")
    
    if any(c.isupper() for c in senha):
        pontos += 1
        feedback.append("✅ Tem maiúsculas")
    
    if any(c.isdigit() for c in senha):
        pontos += 1
        feedback.append("✅ Tem números")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in senha):
        pontos += 2
        feedback.append("✅ Tem símbolos")
    
    # Classificação
    if pontos >= 7:
        nivel = "🛡️ MUITO FORTE"
    elif pontos >= 5:
        nivel = "💪 FORTE"
    elif pontos >= 3:
        nivel = "⚠️ MÉDIA"
    else:
        nivel = "❌ FRACA"
    
    return nivel, pontos, feedback

# Gerando senhas de exemplo
print("🔑 GERADOR DE SENHAS SEGURAS")
print("=" * 40)

for i in range(3):
    senha = gerar_senha_segura(12, True)
    nivel, pontos, feedback = avaliar_forca_senha(senha)
    
    print(f"\\nSenha {i+1}: {senha}")
    print(f"Avaliação: {nivel} ({pontos}/8 pontos)")
    
# Testando senhas comuns (fracas)
print("\\n🚨 TESTANDO SENHAS FRACAS:")
senhas_fracas = ["123456", "password", "admin", "qwerty"]
for senha in senhas_fracas:
    nivel, pontos, _ = avaliar_forca_senha(senha)
    print(f"'{senha}' → {nivel} ({pontos}/8 pontos)")'''
        
        self.exemplo(codigo_gerador)
        print("\n🚀 Executando gerador:")
        self.executar_codigo(codigo_gerador)
        
        # === DICAS DE OURO ===
        self.print_colored("\n🏆 DICAS DE OURO PARA SENHAS:", "accent")
        dicas = [
            "🎲 Use geradores de senha aleatória (como o código acima)",
            "🔢 Mínimo 12 caracteres, ideal 16+",
            "🎭 Senha única para cada conta importante",
            "🗝️ Use gerenciador de senhas (1Password, Bitwarden)",
            "🔄 Ative autenticação de dois fatores sempre",
            "❌ NUNCA use dados pessoais (nome, data nascimento)"
        ]
        for dica in dicas:
            self.print_colored(f"• {dica}", "text")
        
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas de segurança"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS DE SEGURANÇA", "⭐", "success")
        
        self.print_colored("🏆 AS 10 REGRAS DE OURO DA SEGURANÇA:", "accent")
        
        praticas = [
            {
                'titulo': '1. 🔒 Princípio do Menor Privilégio',
                'descricao': 'Dê apenas as permissões mínimas necessárias',
                'exemplo': 'Usuário comum não precisa de acesso de administrador'
            },
            {
                'titulo': '2. 🔍 Validação em Camadas',
                'descricao': 'Valide dados no frontend E no backend',
                'exemplo': 'JavaScript + validação no servidor Python'
            },
            {
                'titulo': '3. 🚫 Nunca Confie no Cliente',
                'descricao': 'Toda validação importante deve ser no servidor',
                'exemplo': 'Preços, permissões, dados críticos'
            },
            {
                'titulo': '4. 🔐 Criptografia em Repouso e Trânsito',
                'descricao': 'Proteja dados parados E em movimento',
                'exemplo': 'HTTPS + banco criptografado'
            },
            {
                'titulo': '5. 📋 Logs de Segurança',
                'descricao': 'Registre todas as ações importantes',
                'exemplo': 'Login, mudanças, acessos a dados sensíveis'
            },
            {
                'titulo': '6. 🔄 Atualizações Constantes',
                'descricao': 'Mantenha tudo sempre atualizado',
                'exemplo': 'Python, bibliotecas, sistema operacional'
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{pratica['titulo']}", "warning")
            self.print_colored(f"📝 {pratica['descricao']}", "text")
            self.print_colored(f"💡 Exemplo: {pratica['exemplo']}", "info")
            
            if i < len(praticas):
                input("   ⏳ Pressione ENTER para a próxima prática...")
        
        # === CHECKLIST DE SEGURANÇA ===
        self.print_colored("\n\n📋 CHECKLIST DE PROJETO SEGURO:", "accent")
        checklist = [
            "☐ Todas as entradas são validadas?",
            "☐ Senhas são armazenadas como hash?",
            "☐ Dados sensíveis são criptografados?",
            "☐ HTTPS está habilitado?",
            "☐ Logs de segurança estão funcionando?",
            "☐ Backups estão criptografados?",
            "☐ Acesso por privilégio mínimo?",
            "☐ Bibliotecas estão atualizadas?"
        ]
        
        for item in checklist:
            self.print_colored(f"  {item}", "text")
        
        self.pausar()
    
    def _secao_erros_comuns(self) -> None:
        """Seção: Erros fatais de segurança"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ERROS FATAIS DE SEGURANÇA", "⚠️", "error")
        
        self.print_colored("💀 OS 7 PECADOS MORTAIS DA PROGRAMAÇÃO:", "error")
        
        erros = [
            {
                'titulo': '💀 1. Senhas no Código Fonte',
                'problema': 'Colocar senhas, chaves API ou tokens diretamente no código',
                'consequencia': 'Qualquer um que vê o código tem acesso total',
                'solucao': 'Use variáveis de ambiente ou arquivos de configuração'
            },
            {
                'titulo': '💀 2. SQL Injection',
                'problema': 'Concatenar strings diretamente em queries SQL',
                'consequencia': 'Hackers podem executar comandos no banco de dados',
                'solucao': 'Use prepared statements ou ORM'
            },
            {
                'titulo': '💀 3. Não Validar Entrada',
                'problema': 'Confiar cegamente nos dados enviados pelo usuário',
                'consequencia': 'XSS, injection, corrupção de dados',
                'solucao': 'Valide TUDO antes de processar'
            },
            {
                'titulo': '💀 4. Logs com Dados Sensíveis',
                'problema': 'Registrar senhas, tokens ou dados pessoais em logs',
                'consequencia': 'Vazamento de informações confidenciais',
                'solucao': 'Filtre dados sensíveis antes de logar'
            },
            {
                'titulo': '💀 5. Permissões Excessivas',
                'problema': 'Dar acesso de admin para todo mundo',
                'consequencia': 'Usuários podem fazer o que não deveriam',
                'solucao': 'Princípio do menor privilégio'
            }
        ]
        
        for i, erro in enumerate(erros, 1):
            self.print_colored(f"\n{erro['titulo']}", "error")
            self.print_colored(f"🚨 Problema: {erro['problema']}", "text")
            self.print_colored(f"💥 Consequência: {erro['consequencia']}", "warning")
            self.print_colored(f"✅ Solução: {erro['solucao']}", "success")
            
            if i < len(erros):
                input("   ⏳ Pressione ENTER para o próximo erro...")
        
        # === CASOS REAIS ===
        self.print_colored("\n\n📰 CASOS REAIS QUE CUSTARAM MILHÕES:", "warning")
        casos = [
            "🏦 Equifax (2017): 147 milhões de dados vazados por biblioteca desatualizada",
            "🏨 Marriott (2018): 500 milhões de clientes expostos por 4 anos",
            "💳 Target (2013): 40 milhões de cartões roubados via sistema de ar condicionado",
            "🎮 PlayStation (2011): 77 milhões de contas hackeadas, rede offline por 23 dias"
        ]
        
        for caso in casos:
            self.print_colored(f"• {caso}", "text")
        
        self.print_colored("\n💡 MORAL DA HISTÓRIA: Um pequeno erro pode custar TUDO!", "accent")
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre hackers e segurança"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES FASCINANTES", "💫", "accent")
        
        curiosidades = [
            {
                'titulo': '🎭 O Primeiro "Bug" da História',
                'historia': 'Em 1947, Grace Hopper encontrou uma mariposa presa no computador Harvard Mark II. Ela colou o inseto no relatório e escreveu "First actual case of bug being found". Daí vem o termo "bug"!'
            },
            {
                'titulo': '🏴‍☠️ Kevin Mitnick: O Hacker Mais Procurado',
                'historia': 'Nos anos 90, era tão procurado pelo FBI que ficou 5 anos preso. Hoje é consultor de segurança e milionário. Seu lema: "A engenharia social é a arte de hackear humanos".'
            },
            {
                'titulo': '🔐 A Senha Mais Cara do Mundo',
                'historia': 'Em 2021, um programador alemão esqueceu a senha de uma carteira Bitcoin com 7.002 bitcoins (valor: mais de 240 milhões de dólares). Ele tem apenas 2 tentativas restantes!'
            },
            {
                'titulo': '🎯 O Worm Morris de 1988',
                'historia': 'O primeiro worm da internet foi criado por um estudante de 23 anos. Infectou 6.000 computadores (10% da internet da época). O criador foi o primeiro condenado pela Lei de Fraude e Abuso Computacional dos EUA.'
            },
            {
                'titulo': '🏆 Black Hat vs White Hat',
                'historia': 'Hackers "White Hat" são os mocinhos - trabalham para empresas encontrando falhas. "Black Hat" são os vilões. "Gray Hat" ficam no meio termo. O nome vem dos filmes de faroeste!'
            },
            {
                'titulo': '💰 Bug Bounty Milionário',
                'historia': 'Em 2016, um pesquisador ganhou US$ 1,5 milhão da Uber por encontrar uma falha crítica. Hoje, empresas pagam milhões por ano em recompensas para quem encontra bugs.'
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
            "🚀 Cada segundo, 2.200 ataques cibernéticos acontecem no mundo",
            "🎯 95% dos ataques bem-sucedidos são devido a erro humano",
            "💻 Existem mais de 1 bilhão de malwares únicos no mundo",
            "⚡ Hackers levam em média 200 dias para serem detectados",
            "🏆 O mercado de segurança digital vale mais de 150 bilhões de dólares",
            "🔐 A palavra 'password' ainda é uma das senhas mais usadas"
        ]
        
        for fato in fatos:
            self.print_colored(f"• {fato}", "primary")
        
        self.print_success("\n🌟 Agora você faz parte da elite que entende o mundo da segurança digital!")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre segurança digital!", "text")
        
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
                'title': 'Quiz: Conhecimentos sobre Segurança Digital',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é o principal objetivo da criptografia?',
                        'answer': ['proteger dados', 'proteger informações', 'esconder dados', 'ocultar informações'],
                        'hint': 'Pense na função principal: manter dados seguros e inacessíveis para quem não deveria vê-los'
                    },
                    {
                        'question': 'O que significa "validação de entrada"?',
                        'answer': ['verificar dados', 'filtrar dados', 'validar dados', 'checar dados'],
                        'hint': 'É o processo de confirmar se os dados que chegam ao programa são seguros'
                    },
                    {
                        'question': 'Qual é o tamanho mínimo recomendado para senhas seguras?',
                        'answer': ['12', '12 caracteres', 'doze'],
                        'hint': 'Pense em um número que seja maior que 10 mas menor que 15'
                    },
                    {
                        'question': 'O que é SQL Injection?',
                        'answer': ['ataque sql', 'injeção sql', 'ataque banco dados', 'vulnerability'],
                        'hint': 'É um tipo de ataque que explora falhas na forma como queries são construídas'
                    },
                    {
                        'question': 'Qual o princípio que diz para dar apenas as permissões mínimas?',
                        'answer': ['menor privilégio', 'princípio menor privilégio', 'least privilege'],
                        'hint': 'Pense em dar o MÍNIMO de acesso necessário para cada usuário'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código de Segurança',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o código para gerar um hash SHA-256',
                        'starter': 'import hashlib\n\nsenha = "minha_senha"\n# Complete aqui para gerar hash SHA-256\nhash_senha = \nprint(f"Hash: {hash_senha}")',
                        'solution': 'hashlib.sha256(senha.encode()).hexdigest()',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a função de validação de senha',
                        'starter': 'def validar_senha(senha):\n    if len(senha) < 8:\n        return False\n    # Complete: verificar se tem maiúscula, minúscula e número\n    \n    return True',
                        'solution': 'if not any(c.isupper() for c in senha) or not any(c.islower() for c in senha) or not any(c.isdigit() for c in senha):\n        return False',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o validador de entrada segura',
                        'starter': 'import re\n\ndef validar_entrada(entrada):\n    # Complete: validar tamanho, caracteres seguros e não vazio\n    \n    return True, "Válido"',
                        'solution': 'if not entrada or len(entrada) > 50 or not re.match(r"^[a-zA-Z0-9\\s_-]+$", entrada):\n        return False, "Inválido"\n    ',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Construa seu Sistema de Autenticação',
                'type': 'creative',
                'instruction': 'Crie um sistema simples que cadastra usuários com senhas seguras, valida login e implementa pelo menos 3 regras de segurança que aprendemos!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre segurança digital",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios de programação segura",
            "🎨 OPÇÃO 3 - Exercício Criativo: Construa um sistema de autenticação",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: Centro de Segurança Digital",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para dominar segurança!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo"""
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
            self.print_success("🌟 PERFEITO! Você dominou completamente a segurança digital!")
        elif percentage >= 80:
            self.print_success("🎉 EXCELENTE! Você entende muito bem segurança!")
        elif percentage >= 60:
            self.print_colored("👍 BOM! Você está no caminho certo!", "info")
        else:
            self.print_colored("📚 Continue estudando! Revisite as seções se necessário.", "warning")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "success")
        
        for i, exercise in enumerate(exercise_data['exercises'], 1):
            self.print_colored(f"\n🎯 EXERCÍCIO {i}: {exercise['type'].upper()}", "warning")
            self.print_colored(exercise['instruction'], "text")
            
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercise['starter'])
            
            print("\n✍️ Digite sua solução (ou 'skip' para pular):")
            try:
                resposta = input(">>> ").strip()
                
                if resposta.lower() == 'skip':
                    self.print_colored("⏭️ Exercício pulado.", "warning")
                    continue
                    
                if resposta:
                    print("\n🚀 Testando sua solução:")
                    try:
                        # Substitui o placeholder com a resposta do usuário
                        codigo_completo = exercise['starter']
                        if '# Complete aqui' in codigo_completo:
                            codigo_completo = codigo_completo.replace('# Complete aqui', resposta)
                        elif 'hash_senha = ' in codigo_completo and not resposta.startswith('hashlib'):
                            codigo_completo = codigo_completo.replace('hash_senha = ', f'hash_senha = {resposta}')
                        else:
                            # Para casos mais complexos, tentar executar a resposta diretamente
                            exec(resposta)
                            
                        self.executar_codigo(codigo_completo)
                        self.print_success("✅ Sua solução funcionou!")
                        
                        ver_solucao = input("\n💡 Quer ver a solução sugerida? (s/n): ").lower()
                        if ver_solucao == 's':
                            self.print_colored("\n🔍 SOLUÇÃO SUGERIDA:", "info")
                            self.exemplo(exercise['solution'])
                            
                    except Exception as e:
                        self.print_warning(f"❌ Erro ao executar: {str(e)}")
                        self.print_colored("\n💡 SOLUÇÃO CORRETA:", "info")
                        self.exemplo(exercise['solution'])
                        
                        # Tentar executar a solução correta
                        try:
                            codigo_correto = exercise['starter']
                            if '# Complete aqui' in codigo_correto:
                                codigo_correto = codigo_correto.replace('# Complete aqui', exercise['solution'])
                            elif 'hash_senha = ' in codigo_correto:
                                codigo_correto = codigo_correto.replace('hash_senha = ', f'hash_senha = {exercise["solution"]}')
                            self.executar_codigo(codigo_correto)
                        except:
                            pass
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Exercício cancelado.")
                return
                
        self.print_success("\n🎉 Parabéns! Você completou todos os exercícios de código!")
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "accent")
        self.print_colored(exercise_data['instruction'], "text")
        
        print("\n💡 EXEMPLO DE SISTEMA DE AUTENTICAÇÃO:")
        exemplo_codigo = '''# Sistema básico de autenticação
import hashlib
import re

usuarios = {}

def cadastrar_usuario(nome, senha):
    # Validar nome de usuário
    if not re.match(r'^[a-zA-Z0-9_-]+$', nome):
        return False, "Nome inválido"
    
    # Validar senha
    if len(senha) < 8:
        return False, "Senha muito curta"
    
    # Hash da senha
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios[nome] = hash_senha
    return True, "Usuário cadastrado!"

def fazer_login(nome, senha):
    if nome not in usuarios:
        return False, "Usuário não encontrado"
    
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    if usuarios[nome] == hash_senha:
        return True, "Login realizado!"
    return False, "Senha incorreta"

# Teste
cadastrar_usuario("admin", "senha123!")
fazer_login("admin", "senha123!")'''
        
        self.exemplo(exemplo_codigo)
        self.executar_codigo(exemplo_codigo)
            
        print("\n✍️ Agora é sua vez! Crie seu sistema de autenticação:")
        print("Dicas:")
        print("• Use hashlib para senhas")
        print("• Valide entradas com regex")
        print("• Implemente pelo menos 3 regras de segurança")
        print("Digite 'fim' quando terminar")
        
        linhas_codigo = []
        try:
            while True:
                linha = input(">>> ")
                if linha.lower() == 'fim':
                    break
                if linha.strip():
                    linhas_codigo.append(linha)
                    
        except KeyboardInterrupt:
            self.print_warning("\n⚠️ Exercício cancelado.")
            return
            
        if linhas_codigo:
            codigo_completo = '\n'.join(linhas_codigo)
            print("\n🚀 Sua criação:")
            try:
                self.executar_codigo(codigo_completo)
                self.print_success("\n🛡️ Fantástico! Você criou um sistema de autenticação seguro!")
            except Exception as e:
                self.print_warning(f"❌ Erro na execução: {str(e)}")
                self.print_colored("💡 Continue praticando! Sistemas de segurança são complexos.", "info")
        else:
            self.print_colored("👋 Tudo bem, talvez na próxima vez!", "info")
            
        self.pausar()
    
    def _mini_projeto_centro_seguranca(self) -> None:
        """Mini Projeto - Módulo 30: Centro de Segurança Digital"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛡️ MINI PROJETO: CENTRO DE SEGURANÇA DIGITAL")
        else:
            print("\n" + "="*50)
            print("🛡️ MINI PROJETO: CENTRO DE SEGURANÇA DIGITAL")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu Centro de Segurança Digital completo!")
        
        self.print_concept(
            "Centro de Segurança Digital",
            "Um sistema completo que combina geração de senhas seguras, validação de dados, criptografia e auditoria de segurança - tudo em um só lugar!"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "🏦 Bancos - Para validar e proteger dados de clientes",
            "🏢 Empresas - Para auditoria interna de segurança",
            "🔐 Gerenciadores de senha - Como 1Password e Bitwarden",
            "🌐 Sites de e-commerce - Para proteger dados de pagamento",
            "🏥 Hospitais - Para proteger dados médicos confidenciais"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Definindo funcionalidades
        self.print_section("PASSO 1: DEFININDO AS FUNCIONALIDADES", "📝", "info")
        self.print_tip("Vamos construir um sistema com 5 funcionalidades principais!")
        
        funcionalidades = [
            "🔑 Gerador de senhas ultra-seguras",
            "🔍 Validador de entrada com múltiplas camadas",
            "🔐 Sistema de criptografia e hash",
            "⚖️ Avaliador de força de senhas",
            "📊 Dashboard de segurança com relatórios"
        ]
        
        for func in funcionalidades:
            self.print_colored(f"✅ {func}", "success")
        
        input("\n🔸 Pressione ENTER para começar a construir...")
        
        try:
            # PASSO 2: Construindo o sistema
            self.print_section("PASSO 2: CONSTRUINDO O CENTRO DE SEGURANÇA", "⚙️", "success")
            self.print_colored("Agora vamos escrever o código completo:", "text")
            
            # PASSO 3: Código final
            self.print_section("PASSO 3: SEU CENTRO DE SEGURANÇA COMPLETO", "🎬", "warning")
            
            codigo_final = r'''# 🛡️ CENTRO DE SEGURANÇA DIGITAL
# Módulo 30: Segurança

import hashlib
import secrets
import string
import re
import base64
from datetime import datetime

class CentroSeguranca:
    def __init__(self):
        self.historico_senhas = []
        self.tentativas_login = {}
        
    def gerar_senha_ultra_segura(self, tamanho=16):
        """Gera senha criptograficamente segura"""
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        self.historico_senhas.append({
            'senha': senha[:4] + '*' * (len(senha) - 4),  # Só mostra início
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'forca': self.avaliar_forca(senha)[0]
        })
        return senha
    
    def avaliar_forca(self, senha):
        """Avalia força da senha com pontuação detalhada"""
        pontos = 0
        criterios = []
        
        if len(senha) >= 12:
            pontos += 3
            criterios.append("✅ Comprimento adequado")
        elif len(senha) >= 8:
            pontos += 1
            criterios.append("⚠️ Comprimento mínimo")
        else:
            criterios.append("❌ Muito curta")
        
        if any(c.islower() for c in senha):
            pontos += 1
            criterios.append("✅ Minúsculas")
        
        if any(c.isupper() for c in senha):
            pontos += 1
            criterios.append("✅ Maiúsculas")
        
        if any(c.isdigit() for c in senha):
            pontos += 1
            criterios.append("✅ Números")
        
        if any(c in "!@#$%^&*()_+-=" for c in senha):
            pontos += 2
            criterios.append("✅ Símbolos especiais")
        
        # Classificação
        if pontos >= 7:
            nivel = "🛡️ ULTRA FORTE"
        elif pontos >= 5:
            nivel = "💪 FORTE"
        elif pontos >= 3:
            nivel = "⚠️ MÉDIA"
        else:
            nivel = "❌ FRACA"
        
        return nivel, pontos, criterios
    
    def validar_entrada_segura(self, entrada, tipo="geral"):
        """Validação multi-camada com diferentes tipos"""
        if not entrada or not entrada.strip():
            return False, "❌ Entrada vazia"
        
        entrada = entrada.strip()
        
        if tipo == "email":
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', entrada):
                return False, "❌ Email inválido"
        elif tipo == "usuario":
            if len(entrada) > 20 or not re.match(r'^[a-zA-Z0-9_-]+$', entrada):
                return False, "❌ Usuário inválido (só letras, números, _ e -)"
        elif tipo == "geral":
            if len(entrada) > 100:
                return False, "❌ Entrada muito longa"
            if re.search(r'[<>"\\'%;()&+]', entrada):
                return False, "❌ Caracteres perigosos detectados"
        
        return True, "✅ Entrada válida"
    
    def criptografar_dados(self, dados):
        """Sistema de criptografia usando hash e base64"""
        # Hash para integridade
        hash_dados = hashlib.sha256(dados.encode()).hexdigest()
        
        # Codificação base64 para "criptografia" simples
        dados_bytes = dados.encode('utf-8')
        dados_codificados = base64.b64encode(dados_bytes).decode('utf-8')
        
        return {
            'dados_codificados': dados_codificados,
            'hash_verificacao': hash_dados[:16],  # Só os primeiros 16 chars
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def dashboard_seguranca(self):
        """Mostra relatório de segurança do sistema"""
        print("\\n" + "="*50)
        print("📊 DASHBOARD DE SEGURANÇA")
        print("="*50)
        
        print(f"🔑 Senhas geradas: {len(self.historico_senhas)}")
        
        if self.historico_senhas:
            print("\\n🕐 ÚLTIMAS SENHAS GERADAS:")
            for i, entrada in enumerate(self.historico_senhas[-3:], 1):
                print(f"  {i}. {entrada['senha']} - {entrada['forca']} ({entrada['timestamp']})")
        
        print("\\n🛡️ STATUS DO SISTEMA: ✅ OPERACIONAL")
        print("🔒 NÍVEL DE SEGURANÇA: 🏆 MÁXIMO")

# === DEMONSTRAÇÃO DO SISTEMA ===
print("🚀 INICIALIZANDO CENTRO DE SEGURANÇA DIGITAL...")
centro = CentroSeguranca()

print("\\n1️⃣ GERANDO SENHAS ULTRA-SEGURAS:")
for i in range(3):
    senha = centro.gerar_senha_ultra_segura(14)
    nivel, pontos, criterios = centro.avaliar_forca(senha)
    print(f"   Senha {i+1}: {senha}")
    print(f"   Avaliação: {nivel} ({pontos}/8 pontos)")

print("\\n2️⃣ TESTANDO VALIDAÇÃO DE ENTRADA:")
testes = [
    ("usuario123", "usuario"),
    ("test@email.com", "email"),
    ("'; DROP TABLE users; --", "geral"),
    ("dados_normais", "geral")
]

for teste, tipo in testes:
    valido, msg = centro.validar_entrada_segura(teste, tipo)
    print(f"   '{teste}' ({tipo}) → {msg}")

print("\\n3️⃣ CRIPTOGRAFANDO DADOS SENSÍVEIS:")
dados_sensiveis = "Informação ultra secreta da empresa"
resultado = centro.criptografar_dados(dados_sensiveis)
print(f"   Dados originais: {dados_sensiveis}")
print(f"   Dados codificados: {resultado['dados_codificados'][:30]}...")
print(f"   Hash verificação: {resultado['hash_verificacao']}")

print("\\n4️⃣ DASHBOARD FINAL:")
centro.dashboard_seguranca()

print("\\n🎉 CENTRO DE SEGURANÇA DIGITAL OPERACIONAL!")
print("🛡️ Seus dados estão protegidos com tecnologia militar!")'''
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.print_colored("Vamos ver seu Centro de Segurança Digital em ação:", "text")
            self.executar_codigo(codigo_final)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um Centro de Segurança Digital completo!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔐 Implementar criptografia AES real para dados críticos",
            "🌐 Adicionar integração com APIs de verificação de vazamentos",
            "📊 Expandir dashboard com métricas avançadas de segurança",
            "🔄 Implementar sistema de backup automático criptografado",
            "👥 Adicionar sistema de múltiplos usuários com permissões",
            "🚨 Implementar alertas em tempo real para tentativas de invasão"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Guardião Digital!")
        self.print_colored("Você agora domina os fundamentos da segurança digital e pode proteger qualquer sistema!", "accent")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Centro de Segurança Digital")
        
        self.pausar()