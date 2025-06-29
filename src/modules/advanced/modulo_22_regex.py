#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 22: Expressões Regulares (Regex)
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda expressões regulares de forma interativa e prática
"""

from ..shared.base_module import BaseModule
import re
import sys
import time
import random
from typing import Dict, List, Optional, Any, NamedTuple
from collections import Counter, defaultdict
from datetime import datetime
import json


class Modulo22Regex(BaseModule):
    """Módulo 22: Expressões Regulares - Busca Avançada em Texto"""
    
    def __init__(self):
        super().__init__("modulo_22", "Expressões Regulares (Regex)")
        self.has_mini_project = True
        self.mini_project_points = 130
    
    def execute(self) -> None:
        """Executa o módulo Expressões Regulares"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._regex()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _regex(self) -> None:
        """Conteúdo principal do módulo Expressões Regulares"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔍 MÓDULO 22: EXPRESSÕES REGULARES")
        else:
            print("\n" + "="*60)
            print("🔍 MÓDULO 22: EXPRESSÕES REGULARES")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo das Expressões Regulares!")
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
            self._mini_projeto_analisador_texto_inteligente()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (7 SEÇÕES) ===
        secoes = [
            {
                'id': 'secao_conceito_regex',
                'titulo': '🎯 O que são Expressões Regulares?',
                'descricao': 'Entenda o poder das Regex para busca avançada em texto',
                'funcao': self._secao_conceito_regex
            },
            {
                'id': 'secao_metacaracteres',
                'titulo': '⚙️ Metacaracteres e Padrões',
                'descricao': 'Aprenda os símbolos especiais que fazem a mágica acontecer',
                'funcao': self._secao_metacaracteres
            },
            {
                'id': 'secao_grupos_capturas',
                'titulo': '📋 Grupos e Capturas',
                'descricao': 'Como capturar partes específicas do texto',
                'funcao': self._secao_grupos_capturas
            },
            {
                'id': 'secao_validacao_dados',
                'titulo': '✅ Validação de Dados',
                'descricao': 'Valide emails, telefones, CPF e outros dados',
                'funcao': self._secao_validacao_dados
            },
            {
                'id': 'secao_parsing_estruturado',
                'titulo': '📊 Parsing de Dados Estruturados',
                'descricao': 'Extraia informações de logs, CSV, JSON e HTML',
                'funcao': self._secao_parsing_estruturado
            },
            {
                'id': 'secao_busca_substituicao',
                'titulo': '🔄 Busca e Substituição Avançada',
                'descricao': 'Modifique textos com precisão cirúrgica',
                'funcao': self._secao_busca_substituicao
            },
            {
                'id': 'secao_aplicacoes_reais',
                'titulo': '🌍 Aplicações no Mundo Real',
                'descricao': 'Veja Regex sendo usado em projetos profissionais',
                'funcao': self._secao_aplicacoes_reais
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

    def _secao_conceito_regex(self) -> None:
        """Seção: O que são Expressões Regulares?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO EXPRESSÕES REGULARES?", "🎯")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Expressão Regular (Regex)", 
            "Uma sequência de caracteres que forma um padrão de busca, usado para encontrar, extrair ou validar texto de forma muito precisa"
        )

        # === DICA RELACIONADA ===
        self.print_tip("Regex é como um 'super Find' - permite buscar padrões complexos, não apenas palavras específicas!")

        # === ANALOGIA DO DIA A DIA ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você está procurando um arquivo no computador. Em vez de procurar pelo nome exato, você pode procurar por 'todos os arquivos que começam com foto_ e terminam com .jpg'. Regex faz isso com texto!", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você define um PADRÃO (como 'email que termina com .com')",
            "2. Python procura esse padrão no texto que você quer analisar",
            "3. Regex retorna todas as ocorrências encontradas ou permite validar se algo combina"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''import re

# Texto com vários emails
texto = "Contatos: joao@empresa.com, maria123@teste.org, pedro.silva@exemplo.net"

# Padrão simples para encontrar emails
padrao_email = r"\\w+@\\w+\\.\\w+"

# Buscar todos os emails
emails_encontrados = re.findall(padrao_email, texto)
print("Emails encontrados:", emails_encontrados)

# Verificar se um texto específico é um email válido
email_teste = "usuario@site.com"
if re.match(r"\\w+@\\w+\\.\\w+", email_teste):
    print(f"✅ {email_teste} é um email válido!")
else:
    print(f"❌ {email_teste} não é um email válido!")'''

        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏦 Bancos - Validar CPF, CNPJ, números de cartão",
            "📧 Gmail/Outlook - Detectar automaticamente emails e links",
            "🛡️ Empresas de segurança - Analisar logs para detectar ataques",
            "🕷️ Google - Web scraping para indexar páginas da internet",
            "💻 Microsoft - Ferramentas de busca e substituição no VS Code"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_metacaracteres(self) -> None:
        """Seção: Metacaracteres e Padrões"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("METACARACTERES E PADRÕES", "⚙️", "success")

        # === CONCEITO ===
        self.print_concept(
            "Metacaracteres",
            "Símbolos especiais que têm significados específicos em Regex, como . * + ? ^ $ e outros"
        )

        # === ANALOGIA ===
        self.print_colored("\n🎮 ANALOGIA DOS VIDEOGAMES:", "warning")
        self.print_colored("Metacaracteres são como 'power-ups' em um jogo - cada um tem um poder especial! O '.' é como uma chave-mestra que abre qualquer porta, o '*' multiplica coisas infinitas vezes!", "text")
        input("\n🔸 Pressione ENTER para aprender os poder-ups...")

        # === TABELA DE METACARACTERES ===
        self.print_colored("\n📋 METACARACTERES ESSENCIAIS:", "info")
        metacaracteres = [
            ". (ponto) - Qualquer caractere (exceto quebra de linha)",
            "* - Zero ou mais repetições do caractere anterior", 
            "+ - Uma ou mais repetições do caractere anterior",
            "? - Zero ou uma repetição (torna opcional)",
            "^ - Início da string",
            "$ - Fim da string",
            "\\d - Qualquer dígito (0-9)",
            "\\w - Qualquer caractere de palavra (letra, número, _)",
            "\\s - Qualquer espaço em branco (espaço, tab, quebra)"
        ]

        for meta in metacaracteres:
            self.print_colored(f"• {meta}", "primary")
            time.sleep(0.3)  # Pausa dramática para absorver

        # === EXEMPLOS PRÁTICOS ===
        print("\n" + "="*50)
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Encontrando Telefones',
                'descricao': 'Vamos buscar números de telefone brasileiros',
                'codigo': '''import re

texto = "Contatos: (11) 99999-8888, 21987654321, (31) 88888-7777"

# Padrão para telefone: (dd) ddddd-dddd ou dddddddddd
padrao = r"\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}"

telefones = re.findall(padrao, texto)
print("Telefones encontrados:", telefones)''',
                'explicacao': 'O padrão \\\\(? significa "parênteses opcionais", \\\\d{2} significa "exatamente 2 dígitos"'
            },
            {
                'titulo': 'EXEMPLO 2: Validando Emails',
                'descricao': 'Criando um validador básico de email',
                'codigo': '''import re

def validar_email(email):
    # ^ = início, $ = fim (email completo)
    # \\w+ = uma ou mais letras/números
    # @ = arroba literal  
    # \\. = ponto literal (escape necessário)
    padrao = r"^\\w+@\\w+\\.\\w+$"
    return bool(re.match(padrao, email))

emails_teste = ["user@site.com", "invalido@", "teste@empresa.com.br"]
for email in emails_teste:
    resultado = "✅ Válido" if validar_email(email) else "❌ Inválido"
    print(f"{email}: {resultado}")''',
                'explicacao': 'Usamos ^ e $ para garantir que o padrão corresponde ao email completo'
            },
            {
                'titulo': 'EXEMPLO 3: Extraindo Datas',
                'descricao': 'Encontrando datas no formato DD/MM/AAAA',
                'codigo': '''import re

texto = "Eventos: 25/12/2024, 01/01/2025, 15/08/2024"

# \\d{2} = exatamente 2 dígitos
# / = barra literal
# \\d{4} = exatamente 4 dígitos  
padrao = r"\\d{2}/\\d{2}/\\d{4}"

datas = re.findall(padrao, texto)
print("Datas encontradas:", datas)

# Vamos também substituir por formato americano
formato_americano = re.sub(r"(\\d{2})/(\\d{2})/(\\d{4})", r"\\3-\\2-\\1", texto)
print("Formato americano:", formato_americano)''',
                'explicacao': 'Usamos grupos (parênteses) para capturar partes e rearranjar com \\\\1, \\\\2, \\\\3'
            }
        ]

        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")

            self.print_code_section("CÓDIGO", exemplo['codigo'])

            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])

            if exemplo['explicacao']:
                self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")

            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")

        self.print_success("\n🎉 Agora você conhece os principais metacaracteres!")
        self.pausar()

    def _secao_grupos_capturas(self) -> None:
        """Seção: Grupos e Capturas"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("GRUPOS E CAPTURAS", "📋", "success")

        # === CONCEITO ===
        self.print_concept(
            "Grupos de Captura",
            "Parênteses () que permitem 'capturar' partes específicas do padrão encontrado, como se fossem gavetas organizadas"
        )

        # === ANALOGIA ===
        self.print_colored("\n🗂️ ANALOGIA DO ARQUIVO:", "warning")
        self.print_colored("Imagine que você está organizando documentos. Em vez de pegar o documento inteiro, você quer separar apenas o nome, data e número. Grupos fazem exatamente isso com texto!", "text")
        input("\n🔸 Pressione ENTER para aprender a organizar...")

        # === EXEMPLOS PRÁTICOS ===
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Separando Data em Partes',
                'descricao': 'Capturando dia, mês e ano separadamente',
                'codigo': '''import re

data_texto = "Data de nascimento: 25/12/1990"

# Grupos numerados: (dia) (mês) (ano)
padrao = r"(\\d{2})/(\\d{2})/(\\d{4})"

match = re.search(padrao, data_texto)
if match:
    dia, mes, ano = match.groups()
    print(f"Dia: {dia}")
    print(f"Mês: {mes}")
    print(f"Ano: {ano}")
    print(f"Data completa: {match.group(0)}")  # Grupo 0 = padrão inteiro
    
    # Reformatar data
    data_americana = f"{mes}/{dia}/{ano}"
    print(f"Formato americano: {data_americana}")''',
                'explicacao': 'Cada () cria um grupo numerado. group(1) = primeiro grupo, group(2) = segundo, etc.'
            },
            {
                'titulo': 'EXEMPLO 2: Grupos Nomeados',
                'descricao': 'Usando nomes em vez de números para maior clareza',
                'codigo': '''import re

contato = "Nome: João Silva, Email: joao@empresa.com, Fone: (11) 99999-8888"

# Grupos nomeados: (?P<nome>...)
padrao = r"Nome: (?P<nome>[^,]+), Email: (?P<email>[^,]+), Fone: (?P<telefone>.+)"

match = re.search(padrao, contato)
if match:
    print("=== DADOS EXTRAÍDOS ===")
    print(f"Nome: {match.group('nome')}")
    print(f"Email: {match.group('email')}")
    print(f"Telefone: {match.group('telefone')}")
    
    # Como dicionário
    dados = match.groupdict()
    print(f"\\nDicionário: {dados}")''',
                'explicacao': 'Grupos nomeados (?P<nome>...) são mais legíveis que números'
            },
            {
                'titulo': 'EXEMPLO 3: Múltiplas Capturas',
                'descricao': 'Processando uma lista de contatos',
                'codigo': '''import re

agenda = """
João Silva: (11) 99999-1111
Maria Santos: (21) 88888-2222
Pedro Costa: (31) 77777-3333
Ana Oliveira: (47) 66666-4444
"""

# Captura: nome e telefone completo
padrao = r"([A-Za-z ]+): \\((\\d{2})\\) (\\d{5}-\\d{4})"

# findall retorna lista de tuplas
contatos = re.findall(padrao, agenda)

print("=== AGENDA PROCESSADA ===")
for nome, ddd, numero in contatos:
    nome_limpo = nome.strip()
    print(f"📞 {nome_limpo}")
    print(f"   DDD: {ddd}")
    print(f"   Número: {numero}")
    print(f"   Completo: ({ddd}) {numero}")
    print()''',
                'explicacao': 'findall() com grupos retorna lista de tuplas com as capturas'
            }
        ]

        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")

            self.print_code_section("CÓDIGO", exemplo['codigo'])

            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])

            self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")

            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")

        # === DICAS AVANÇADAS ===
        self.print_colored("\n🎓 DICAS AVANÇADAS:", "accent")
        dicas = [
            "(?:...) - Grupo não capturante (agrupa sem capturar)",
            "\\1, \\2 - Referência aos grupos em substituições", 
            "(?=...) - Lookahead positivo (verifica sem consumir)",
            "(?!...) - Lookahead negativo"
        ]
        for dica in dicas:
            self.print_colored(f"• {dica}", "primary")

        self.print_success("\n🎉 Agora você domina grupos e capturas!")
        self.pausar()

    def _secao_validacao_dados(self) -> None:
        """Seção: Validação de Dados"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("VALIDAÇÃO DE DADOS", "✅", "success")

        # === CONCEITO ===
        self.print_concept(
            "Validação com Regex",
            "Usar padrões para verificar se dados estão no formato correto antes de processá-los"
        )

        # === IMPORTÂNCIA ===
        self.print_colored("\n🛡️ POR QUE VALIDAR?", "warning")
        self.print_colored("Dados incorretos podem quebrar sistemas, causar erros de segurança ou perda de informações importantes!", "text")
        input("\n🔸 Pressione ENTER para criar validadores profissionais...")

        # === CÓDIGO COMPLETO DE VALIDAÇÃO ===
        self.print_colored("\n💻 SISTEMA COMPLETO DE VALIDAÇÃO:", "success")
        codigo_validacao = '''import re

class ValidadorDados:
    """Sistema profissional de validação usando Regex"""
    
    def __init__(self):
        # Patterns compiladas para melhor performance
        self.patterns = {
            'email': re.compile(r'^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$'),
            'telefone_br': re.compile(r'^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$'),
            'cpf': re.compile(r'^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$'),
            'cnpj': re.compile(r'^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$'),
            'cep': re.compile(r'^\\d{5}-\\d{3}$'),
            'placa_carro': re.compile(r'^[A-Z]{3}-\\d{4}$|^[A-Z]{3}\\d[A-Z]\\d{2}$'),
            'senha_forte': re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$'),
            'cartao_credito': re.compile(r'^\\d{4}\\s?\\d{4}\\s?\\d{4}\\s?\\d{4}$'),
            'ip_address': re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'),
            'url': re.compile(r'^https?://[\\w\\.-]+\\.[a-zA-Z]{2,}(/.*)?$')
        }
    
    def validar(self, tipo, valor):
        """Valida valor baseado no tipo"""
        if tipo in self.patterns:
            return bool(self.patterns[tipo].match(valor))
        return False
    
    def validar_multiplos(self, dados):
        """Valida dicionário com múltiplos campos"""
        resultados = {}
        for campo, valor in dados.items():
            resultados[campo] = self.validar(campo, valor)
        return resultados
    
    def formatar_cpf(self, cpf_numeros):
        """Formata CPF apenas números para formato xxx.xxx.xxx-xx"""
        if re.match(r'^\\d{11}$', cpf_numeros):
            return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
        return cpf_numeros
    
    def limpar_telefone(self, telefone):
        """Remove formatação do telefone"""
        return re.sub(r'[^\\d]', '', telefone)

# === DEMONSTRAÇÃO PRÁTICA ===
validador = ValidadorDados()

print("🔍 SISTEMA DE VALIDAÇÃO EM AÇÃO")
print("=" * 40)

# Dados de teste (alguns válidos, outros inválidos)
dados_teste = {
    'email': 'usuario@empresa.com',
    'telefone_br': '(11) 99999-8888',
    'cpf': '123.456.789-00',
    'cep': '01234-567',
    'url': 'https://www.python.org'
}

# Validação individual
print("\\n📋 VALIDAÇÃO INDIVIDUAL:")
for tipo, valor in dados_teste.items():
    resultado = validador.validar(tipo, valor)
    status = "✅ Válido" if resultado else "❌ Inválido"
    print(f"   {tipo.replace('_', ' ').title()}: {valor} → {status}")

# Testes com dados inválidos
print("\\n❌ TESTANDO DADOS INVÁLIDOS:")
dados_invalidos = {
    'email': 'email_sem_arroba.com',
    'telefone_br': '123',
    'cpf': '123.456',
    'cep': '12345',
    'url': 'site_sem_protocolo.com'
}

for tipo, valor in dados_invalidos.items():
    resultado = validador.validar(tipo, valor)
    status = "✅ Válido" if resultado else "❌ Inválido"
    print(f"   {tipo.replace('_', ' ').title()}: {valor} → {status}")

# Exemplo de formatação
print("\\n🔧 FORMATAÇÃO AUTOMÁTICA:")
cpf_sem_formato = "12345678900"
cpf_formatado = validador.formatar_cpf(cpf_sem_formato)
print(f"   CPF: {cpf_sem_formato} → {cpf_formatado}")

telefone_com_formato = "(11) 99999-8888"
telefone_limpo = validador.limpar_telefone(telefone_com_formato)
print(f"   Telefone: {telefone_com_formato} → {telefone_limpo}")

print("\\n🎯 Use casos reais:")
print("   • Formulários web - validar antes de enviar")
print("   • APIs - validar dados recebidos")
print("   • Importação de dados - limpar e validar arquivos")
print("   • Sistemas bancários - validar documentos")'''

        self.exemplo(codigo_validacao)
        print("\n🚀 Executando validador completo:")
        self.executar_codigo(codigo_validacao)

        self.print_success("\n🎉 Sistema de validação criado com sucesso!")
        self.pausar()

    def _secao_parsing_estruturado(self) -> None:
        """Seção: Parsing de Dados Estruturados"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("PARSING DE DADOS ESTRUTURADOS", "📊", "success")

        # === CONCEITO ===
        self.print_concept(
            "Parsing com Regex",
            "Extrair informações específicas de dados estruturados como logs, CSV, JSON, HTML usando padrões"
        )

        # === EXEMPLO PRÁTICO COMPLETO ===
        codigo_parser = '''import re
from collections import defaultdict, Counter
from datetime import datetime

class DataParser:
    """Parser avançado para múltiplos formatos de dados"""
    
    def parse_log_apache(self, log_line):
        """Parse de log Apache/Nginx"""
        pattern = r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - - \\[([^\\]]+)\\] "(\\w+) ([^"]+) HTTP/[^"]*" (\\d{3}) (\\d+)'
        match = re.match(pattern, log_line)
        
        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'method': match.group(3), 
                'url': match.group(4),
                'status': int(match.group(5)),
                'size': int(match.group(6))
            }
        return None
    
    def extract_emails_from_text(self, text):
        """Extrai todos os emails de um texto"""
        pattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
        return re.findall(pattern, text)
    
    def parse_csv_line(self, csv_line):
        """Parse de linha CSV considerando aspas"""
        # Pattern para CSV com campos entre aspas
        pattern = r'(?:^|,)("(?:[^"]|"")*"|[^,]*)'
        fields = re.findall(pattern, csv_line)
        # Remove aspas e trata aspas duplas
        return [field.strip('"').replace('""', '"') for field in fields]
    
    def extract_phone_numbers(self, text):
        """Extrai números de telefone brasileiros"""
        patterns = [
            r'\\(?\\d{2}\\)?\\s?\\d{4,5}-\\d{4}',  # (11) 99999-8888
            r'\\d{2}\\s?\\d{4,5}\\s?\\d{4}',       # 11 99999 8888
            r'\\+55\\s?\\d{2}\\s?\\d{4,5}-?\\d{4}' # +55 11 99999-8888
        ]
        
        phones = []
        for pattern in patterns:
            phones.extend(re.findall(pattern, text))
        return list(set(phones))  # Remove duplicados
    
    def extract_currency_values(self, text):
        """Extrai valores monetários"""
        patterns = [
            r'R\\$\\s?([\\d.,]+)',      # R$ 1.000,50
            r'\\$([\\d.,]+)',           # $1,000.50
            r'([\\d.,]+)\\s*reais?',    # 1000 reais
            r'€\\s?([\\d.,]+)'          # € 1.000,50
        ]
        
        values = []
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            values.extend(matches)
        return values
    
    def parse_config_file(self, config_text):
        """Parse de arquivo de configuração key=value"""
        config = {}
        lines = config_text.strip().split('\\n')
        
        for line in lines:
            line = line.strip()
            # Ignora comentários e linhas vazias
            if not line or line.startswith('#'):
                continue
            
            # Pattern: chave = valor
            match = re.match(r'([^=]+)=(.+)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip().strip('"')
                config[key] = value
        
        return config

# === DEMONSTRAÇÃO COM DADOS REAIS ===
parser = DataParser()

print("📊 PARSING DE DADOS ESTRUTURADOS")
print("=" * 45)

# 1. Parse de log de servidor
print("\\n1. 📜 ANÁLISE DE LOG APACHE:")
log_sample = '192.168.1.100 - - [10/Jan/2024:08:30:15 +0000] "GET /index.html HTTP/1.1" 200 1024'
log_data = parser.parse_log_apache(log_sample)
if log_data:
    print(f"   IP: {log_data['ip']}")
    print(f"   Método: {log_data['method']}")
    print(f"   URL: {log_data['url']}")
    print(f"   Status: {log_data['status']}")

# 2. Extração de emails
print("\\n2. 📧 EXTRAÇÃO DE EMAILS:")
text_with_emails = "Contatos: joao@empresa.com, suporte@site.org, vendas@loja.com.br"
emails = parser.extract_emails_from_text(text_with_emails)
print(f"   Emails encontrados: {emails}")

# 3. Parse de CSV
print("\\n3. 📋 PARSE DE CSV:")
csv_line = 'João Silva,"Rua A, 123",São Paulo,"R$ 5.000"'
csv_fields = parser.parse_csv_line(csv_line)
print(f"   Campos: {csv_fields}")

# 4. Extração de telefones
print("\\n4. 📞 EXTRAÇÃO DE TELEFONES:")
text_with_phones = "Contatos: (11) 99999-8888, 21 88888-7777, +55 31 77777-6666"
phones = parser.extract_phone_numbers(text_with_phones)
print(f"   Telefones: {phones}")

# 5. Extração de valores monetários
print("\\n5. 💰 EXTRAÇÃO DE VALORES:")
text_with_money = "Preços: R$ 1.500,00, $50.75, 2000 reais, € 75,50"
values = parser.extract_currency_values(text_with_money)
print(f"   Valores: {values}")

# 6. Parse de configuração
print("\\n6. ⚙️ PARSE DE CONFIGURAÇÃO:")
config_text = """
# Configuração do sistema
database_host=localhost
database_port=5432
debug_mode=true
app_name="Minha Aplicação"
"""
config = parser.parse_config_file(config_text)
print("   Configurações:")
for key, value in config.items():
    print(f"     {key}: {value}")

print("\\n🎯 APLICAÇÕES PROFISSIONAIS:")
print("   • Análise de logs de servidores web")
print("   • Importação de dados de planilhas")
print("   • Extração de informações de documentos")
print("   • Monitoramento de sistemas")
print("   • Web scraping e análise de conteúdo")'''

        self.exemplo(codigo_parser)
        print("\n🚀 Executando parser completo:")
        self.executar_codigo(codigo_parser)

        self.print_success("\n🎉 Sistema de parsing criado com sucesso!")
        self.pausar()

    def _secao_busca_substituicao(self) -> None:
        """Seção: Busca e Substituição Avançada"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("BUSCA E SUBSTITUIÇÃO AVANÇADA", "🔄", "success")

        # === CONCEITO ===
        self.print_concept(
            "Busca e Substituição com Regex",
            "Encontrar padrões complexos no texto e substituí-los por outros conteúdos, mantendo partes específicas"
        )

        # === EXEMPLO PRÁTICO ===
        codigo_substituicao = '''import re

class TextProcessor:
    """Processador avançado de texto com Regex"""
    
    def __init__(self):
        self.stats = {'substituicoes': 0, 'operacoes': 0}
    
    def anonimizar_emails(self, texto):
        """Substitui emails por versão anonimizada"""
        def replacer(match):
            email = match.group()
            usuario, dominio = email.split('@')
            # Mantém primeira e última letra do usuário
            if len(usuario) > 2:
                usuario_anonimo = usuario[0] + '*' * (len(usuario) - 2) + usuario[-1]
            else:
                usuario_anonimo = '*' * len(usuario)
            return f"{usuario_anonimo}@{dominio}"
        
        resultado = re.sub(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', 
                          replacer, texto)
        self.stats['operacoes'] += 1
        return resultado
    
    def mascarar_cpfs(self, texto):
        """Mascara CPFs mantendo apenas últimos 2 dígitos"""
        def replacer(match):
            cpf = match.group()
            return re.sub(r'\\d{3}\\.\\d{3}\\.\\d{3}-(\\d{2})', r'***.***.**-\\1', cpf)
        
        resultado = re.sub(r'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}', replacer, texto)
        self.stats['operacoes'] += 1
        return resultado
    
    def padronizar_telefones(self, texto):
        """Padroniza telefones para formato (xx) xxxxx-xxxx"""
        # Pattern flexível para capturar diferentes formatos
        pattern = r'\\(?+(\\d{2})\\)?+\\s?+(\\d{4,5})-?+(\\d{4})'
        replacement = r'(\\1) \\2-\\3'
        
        resultado = re.sub(pattern, replacement, texto)
        self.stats['operacoes'] += 1
        return resultado
    
    def formatar_datas(self, texto):
        """Converte datas DD/MM/AAAA para AAAA-MM-DD"""
        pattern = r'(\\d{2})/(\\d{2})/(\\d{4})'
        replacement = r'\\3-\\2-\\1'
        
        resultado = re.sub(pattern, replacement, texto)
        self.stats['operacoes'] += 1
        return resultado
    
    def destacar_urls(self, texto):
        """Envolve URLs em tags HTML"""
        pattern = r'(https?://[\\w\\.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?)'
        replacement = r'<a href="\\1">\\1</a>'
        
        resultado = re.sub(pattern, replacement, texto)
        self.stats['operacoes'] += 1
        return resultado
    
    def limpar_espacos_extras(self, texto):
        """Remove espaços extras e normaliza quebras de linha"""
        # Remove múltiplos espaços
        texto = re.sub(r' +', ' ', texto)
        # Remove múltiplas quebras de linha
        texto = re.sub(r'\\n+', '\\n', texto)
        # Remove espaços no início e fim das linhas
        texto = re.sub(r'^ +| +$', '', texto, flags=re.MULTILINE)
        
        self.stats['operacoes'] += 1
        return texto.strip()
    
    def extrair_e_formatar_precos(self, texto):
        """Encontra preços e os formata uniformemente"""
        def replacer(match):
            valor = match.group(1)
            # Remove pontos de milhares e substitui vírgula por ponto
            valor_limpo = valor.replace('.', '').replace(',', '.')
            try:
                numero = float(valor_limpo)
                return f"R$ {numero:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            except:
                return match.group(0)
        
        patterns = [
            r'R\\$\\s*([\\d.,]+)',
            r'([\\d.,]+)\\s*reais?'
        ]
        
        resultado = texto
        for pattern in patterns:
            resultado = re.sub(pattern, replacer, resultado, flags=re.IGNORECASE)
        
        self.stats['operacoes'] += 1
        return resultado

# === DEMONSTRAÇÃO PRÁTICA ===
processor = TextProcessor()

print("🔄 PROCESSAMENTO AVANÇADO DE TEXTO")
print("=" * 40)

# Texto original com vários tipos de dados
texto_original = """
Relatório de Vendas - 25/12/2023

Contatos importantes:
- João Silva: joao.silva@empresa.com, CPF: 123.456.789-00, Tel: 11999998888
- Maria Santos: maria@vendas.com.br, CPF: 987.654.321-11, Tel: (21) 88888-7777

Vendas realizadas:
- Produto A: R$ 1500,00
- Produto B: 2500 reais  
- Produto C: R$750,50

Mais informações: https://www.empresa.com/relatorio
Suporte: https://suporte.empresa.com.br/ajuda

Data do próximo relatório: 01/01/2024
"""

print("📄 TEXTO ORIGINAL:")
print(texto_original)
print("\\n" + "="*50)

# Aplicar transformações passo a passo
print("\\n🔧 APLICANDO TRANSFORMAÇÕES:")

# 1. Anonimizar emails
print("\\n1. 📧 Anonimizando emails...")
texto_step1 = processor.anonimizar_emails(texto_original)
emails_originais = re.findall(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', texto_original)
emails_anonimos = re.findall(r'\\b[A-Za-z0-9.*_%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', texto_step1)
for orig, anon in zip(emails_originais, emails_anonimos):
    print(f"   {orig} → {anon}")

# 2. Mascarar CPFs
print("\\n2. 🆔 Mascarando CPFs...")
texto_step2 = processor.mascarar_cpfs(texto_step1)
cpfs_originais = re.findall(r'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}', texto_original)
cpfs_mascarados = re.findall(r'\\*{3}\\.\\*{3}\\.\\*{2}-\\d{2}', texto_step2)
for orig, mask in zip(cpfs_originais, cpfs_mascarados):
    print(f"   {orig} → {mask}")

# 3. Padronizar telefones
print("\\n3. 📞 Padronizando telefones...")
texto_step3 = processor.padronizar_telefones(texto_step2)
# Mostra diferença nos telefones

# 4. Formatar datas
print("\\n4. 📅 Formatando datas...")
texto_step4 = processor.formatar_datas(texto_step3)
datas_originais = re.findall(r'\\d{2}/\\d{2}/\\d{4}', texto_original)
datas_formatadas = re.findall(r'\\d{4}-\\d{2}-\\d{2}', texto_step4)
for orig, form in zip(datas_originais, datas_formatadas):
    print(f"   {orig} → {form}")

# 5. Destacar URLs
print("\\n5. 🔗 Destacando URLs...")
texto_step5 = processor.destacar_urls(texto_step4)

# 6. Formatar preços
print("\\n6. 💰 Formatando preços...")
texto_final = processor.extrair_e_formatar_precos(texto_step5)

print("\\n📄 TEXTO FINAL PROCESSADO:")
print("="*50)
print(texto_final)

print(f"\\n📊 ESTATÍSTICAS:")
print(f"   Operações realizadas: {processor.stats['operacoes']}")
print(f"   Caracteres original: {len(texto_original)}")
print(f"   Caracteres final: {len(texto_final)}")

print("\\n💡 APLICAÇÕES PRÁTICAS:")
print("   • Anonimização de dados pessoais (LGPD)")
print("   • Padronização de importações de dados")
print("   • Limpeza de textos para análise")
print("   • Formatação automática de documentos")
print("   • Preparação de dados para relatórios")'''

        self.exemplo(codigo_substituicao)
        print("\n🚀 Executando processador de texto:")
        self.executar_codigo(codigo_substituicao)

        self.print_success("\n🎉 Sistema de busca e substituição criado!")
        self.pausar()

    def _secao_aplicacoes_reais(self) -> None:
        """Seção: Aplicações no Mundo Real"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("APLICAÇÕES NO MUNDO REAL", "🌍", "success")

        # === CONCEITO ===
        self.print_concept(
            "Regex na Prática",
            "Como grandes empresas e desenvolvedores usam expressões regulares para resolver problemas reais"
        )

        # === CASOS DE USO REAIS ===
        self.print_colored("\n🏢 CASOS DE USO EM EMPRESAS:", "warning")
        casos_uso = [
            "🏦 **Bancos** - Validar CPF, CNPJ, contas bancárias",
            "📧 **Gmail/Outlook** - Detectar automaticamente links e emails",
            "🛡️ **Empresas de Segurança** - Analisar logs para detectar ataques",
            "🕷️ **Google** - Web scraping para indexar páginas",
            "💻 **Microsoft VS Code** - Busca e substituição avançada",
            "📱 **WhatsApp** - Detectar números de telefone automaticamente",
            "🛒 **E-commerce** - Validar CEP para cálculo de frete",
            "📊 **Analytics** - Processar logs de acesso de sites"
        ]

        for caso in casos_uso:
            self.print_colored(f"• {caso}", "primary")
            time.sleep(0.2)

        input("\n🔸 Pressione ENTER para ver código de aplicações reais...")

        # === EXEMPLO PRÁTICO COMPLETO ===
        codigo_aplicacoes = '''import re
from collections import Counter, defaultdict
import json

class SistemaDeteccaoFraude:
    """Sistema inspirado em detecção de fraudes bancárias"""
    
    def __init__(self):
        # Padrões suspeitos
        self.padroes_suspeitos = {
            'sql_injection': re.compile(r'(union|select|insert|drop|delete|exec)', re.IGNORECASE),
            'xss_attempt': re.compile(r'(<script|javascript:|onload=)', re.IGNORECASE),
            'path_traversal': re.compile(r'(\\.\\./|\\.\\.\\\\\\\)'),
            'tentativa_login': re.compile(r'(login|auth|password).*fail', re.IGNORECASE),
            'ip_suspeito': re.compile(r'^(10\\.|172\\.|192\\.168\\.|127\\.)')
        }
    
    def analisar_log_seguranca(self, log_text):
        """Analisa logs procurando atividades suspeitas"""
        alertas = defaultdict(list)
        linhas = log_text.split('\\n')
        
        for i, linha in enumerate(linhas, 1):
            if not linha.strip():
                continue
                
            for tipo_ameaca, pattern in self.padroes_suspeitos.items():
                if pattern.search(linha):
                    alertas[tipo_ameaca].append({
                        'linha': i,
                        'conteudo': linha.strip(),
                        'severidade': self._calcular_severidade(tipo_ameaca)
                    })
        
        return dict(alertas)
    
    def _calcular_severidade(self, tipo):
        severidades = {
            'sql_injection': 'CRÍTICA',
            'xss_attempt': 'ALTA', 
            'path_traversal': 'ALTA',
            'tentativa_login': 'MÉDIA',
            'ip_suspeito': 'BAIXA'
        }
        return severidades.get(tipo, 'BAIXA')

class ValidadorFormularioWeb:
    """Sistema de validação para formulários web"""
    
    def __init__(self):
        self.validadores = {
            'nome': re.compile(r'^[A-Za-zÀ-ÿ\\s]{2,50}$'),
            'email': re.compile(r'^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$'),
            'telefone': re.compile(r'^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$'),
            'cpf': re.compile(r'^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$'),
            'senha': re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$'),
            'cep': re.compile(r'^\\d{5}-\\d{3}$'),
            'cartao': re.compile(r'^\\d{4}\\s\\d{4}\\s\\d{4}\\s\\d{4}$')
        }
    
    def validar_formulario(self, dados):
        """Valida dados de formulário web"""
        resultados = {}
        erros = []
        
        for campo, valor in dados.items():
            if campo in self.validadores:
                is_valid = bool(self.validadores[campo].match(valor))
                resultados[campo] = {
                    'valor': valor,
                    'valido': is_valid,
                    'erro': None if is_valid else f'{campo} inválido'
                }
                
                if not is_valid:
                    erros.append(campo)
        
        return {
            'valido': len(erros) == 0,
            'erros': erros,
            'detalhes': resultados
        }

class AnalisadorRedesSociais:
    """Analisador de posts de redes sociais"""
    
    def __init__(self):
        self.patterns = {
            'mencoes': re.compile(r'@(\\w+)'),
            'hashtags': re.compile(r'#(\\w+)'),
            'urls': re.compile(r'https?://[\\w\\.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?'),
            'emojis': re.compile(r'[😀-🙏🌀-🗿🚀-🛿☀-⿿]'),
            'telefones': re.compile(r'\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}'),
            'emails': re.compile(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b')
        }
    
    def analisar_post(self, texto):
        """Analisa post extraindo informações"""
        resultado = {
            'texto_original': texto,
            'tamanho': len(texto),
            'palavras': len(texto.split())
        }
        
        for tipo, pattern in self.patterns.items():
            matches = pattern.findall(texto)
            resultado[tipo] = {
                'quantidade': len(matches),
                'itens': list(set(matches))  # Remove duplicatas
            }
        
        return resultado

# === DEMONSTRAÇÕES PRÁTICAS ===

print("🌍 APLICAÇÕES REAIS DE REGEX")
print("=" * 40)

# 1. Sistema de Detecção de Fraude
print("\\n🛡️ 1. SISTEMA DE DETECÇÃO DE FRAUDE")
detector_fraude = SistemaDeteccaoFraude()

logs_suspeitos = """
192.168.1.100 - GET /login.php - Success
192.168.1.101 - POST /admin.php?id=1' UNION SELECT * FROM users-- - Failed
10.0.0.5 - GET /config.php - Access denied
192.168.1.102 - GET /../../../etc/passwd - Blocked
172.16.0.10 - POST /login - Authentication failed
192.168.1.103 - GET /search?q=<script>alert('xss')</script> - Filtered
"""

alertas = detector_fraude.analisar_log_seguranca(logs_suspeitos)
print("   ⚠️ ALERTAS DE SEGURANÇA:")
for tipo, lista_alertas in alertas.items():
    print(f"     • {tipo.replace('_', ' ').title()}: {len(lista_alertas)} ocorrência(s)")
    for alerta in lista_alertas[:2]:  # Mostra só as primeiras 2
        print(f"       Linha {alerta['linha']}: [{alerta['severidade']}]")

# 2. Validador de Formulário Web
print("\\n📝 2. VALIDADOR DE FORMULÁRIO WEB")
validador_web = ValidadorFormularioWeb()

dados_formulario = {
    'nome': 'João Silva',
    'email': 'joao@empresa.com',
    'telefone': '(11) 99999-8888',
    'cpf': '123.456.789-00',
    'senha': 'MinhaSenh@123',
    'cep': '01234-567'
}

resultado_validacao = validador_web.validar_formulario(dados_formulario)
print(f"   ✅ Formulário válido: {resultado_validacao['valido']}")
print(f"   📊 Campos validados: {len(dados_formulario)}")
if resultado_validacao['erros']:
    print(f"   ❌ Erros encontrados: {resultado_validacao['erros']}")

# 3. Analisador de Redes Sociais
print("\\n📱 3. ANALISADOR DE REDES SOCIAIS")
analisador_social = AnalisadorRedesSociais()

post_exemplo = """
Oi pessoal! 👋 Estou lançando meu novo projeto: https://meusite.com.br
Me sigam @joaodev e usem a hashtag #programacao #python
Contato: joao@projeto.com ou (11) 99999-8888 📞
"""

analise_post = analisador_social.analisar_post(post_exemplo)
print("   📊 ANÁLISE DO POST:")
print(f"     • Tamanho: {analise_post['tamanho']} caracteres")
print(f"     • Palavras: {analise_post['palavras']}")
print(f"     • Menções: {analise_post['mencoes']['quantidade']} → {analise_post['mencoes']['itens']}")
print(f"     • Hashtags: {analise_post['hashtags']['quantidade']} → {analise_post['hashtags']['itens']}")
print(f"     • URLs: {analise_post['urls']['quantidade']}")
print(f"     • Emails: {analise_post['emails']['quantidade']} → {analise_post['emails']['itens']}")
print(f"     • Telefones: {analise_post['telefones']['quantidade']} → {analise_post['telefones']['itens']}")

print("\\n💼 COMO ESSAS APLICAÇÕES SÃO USADAS:")
print("   🛡️ Segurança: Monitoramento 24/7 de tentativas de ataque")
print("   📝 Formulários: Validação em tempo real durante digitação")
print("   📱 Social Media: Análise de engajamento e detecção de spam")
print("   🏦 Bancos: Prevenção de fraudes em transações")
print("   📊 Analytics: Processamento de milhões de logs por hora")'''

        self.exemplo(codigo_aplicacoes)
        print("\n🚀 Executando aplicações reais:")
        self.executar_codigo(codigo_aplicacoes)

        self.print_success("\n🎉 Agora você viu Regex sendo usado profissionalmente!")
        self.pausar()

    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu com exercícios práticos!", "text")

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
                'title': 'Quiz: Conhecimentos sobre Regex',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual metacaractere representa "qualquer caractere" em regex?',
                        'answer': ['.', 'ponto'],
                        'hint': 'É o símbolo que você usa para encerrar frases'
                    },
                    {
                        'question': 'O que significa \\d em uma expressão regular?',
                        'answer': ['digito', 'dígito', 'numero', 'número'],
                        'hint': 'Representa números de 0 a 9'
                    },
                    {
                        'question': 'Como criar um grupo de captura em regex?',
                        'answer': ['()', 'parenteses', 'parênteses'],
                        'hint': 'Use os símbolos que normalmente agrupam operações matemáticas'
                    },
                    {
                        'question': 'Qual função do módulo re busca TODAS as ocorrências de um padrão?',
                        'answer': ['findall', 're.findall'],
                        'hint': 'Find = encontrar, All = todas'
                    },
                    {
                        'question': 'O que significa + em regex?',
                        'answer': ['uma ou mais', '1 ou mais'],
                        'hint': 'É o contrário de * (que aceita zero), este precisa pelo menos de uma'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o padrão para encontrar emails',
                        'starter': 'import re\npadrao_email = r"________"\nemail = "user@site.com"\nif re.match(padrao_email, email):\n    print("Email válido!")',
                        'solution': '\\w+@\\w+\\.\\w+',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o padrão para capturar telefone (DDD) e número',
                        'starter': 'import re\ntelefone = "(11) 99999-8888"\npadrao = r"\\((____)\\) (__________)"\nmatch = re.match(padrao, telefone)\nif match:\n    ddd, numero = match.groups()\n    print(f"DDD: {ddd}, Número: {numero}")',
                        'solution': '\\d{2}',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o padrão para extrair dia, mês e ano de uma data',
                        'starter': 'import re\ndata = "25/12/2024"\npadrao = r"(____)/(____)/(____)"\nmatch = re.match(padrao, data)\nif match:\n    dia, mes, ano = match.groups()\n    print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")',
                        'solution': '\\d{2}',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Validador de Senhas Personalizadas',
                'type': 'creative',
                'instruction': 'Crie um padrão de regex para validar senhas com suas próprias regras! Pense em: tamanho mínimo, letras obrigatórias, números, símbolos especiais...'
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

    def _run_quiz(self, quiz_data: Dict[str, Any]) -> None:
        """Executa o quiz de conhecimentos"""
        self.print_section(f"QUIZ: {quiz_data['title']}", "📝", "warning")
        
        questions = quiz_data['questions']
        acertos = 0
        
        for i, q in enumerate(questions, 1):
            self.print_colored(f"\n🎯 PERGUNTA {i}/{len(questions)}:", "accent")
            self.print_colored(q['question'], "text")
            
            resposta = input("\n👉 Sua resposta: ").strip()
            
            if any(resposta.lower() == answer.lower() for answer in q['answer']):
                self.print_success("✅ Correto! Muito bem!")
                acertos += 1
            else:
                self.print_warning("❌ Incorreto!")
                self.print_colored(f"💡 Dica: {q['hint']}", "info")
                self.print_colored(f"✅ Resposta: {q['answer'][0]}", "success")
        
        # Resultado final
        porcentagem = (acertos / len(questions)) * 100
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        self.print_colored(f"Acertos: {acertos}/{len(questions)} ({porcentagem:.0f}%)", "text")
        
        if porcentagem >= 80:
            self.print_success("🌟 Excelente! Você domina Regex!")
        elif porcentagem >= 60:
            self.print_success("👍 Bom trabalho! Continue praticando!")
        else:
            self.print_tip("💪 Continue estudando! Você vai conseguir!")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _run_code_completion(self, exercise_data: Dict[str, Any]) -> None:
        """Executa exercícios de completar código"""
        self.print_section(f"CÓDIGO: {exercise_data['title']}", "💻", "warning")
        
        exercises = exercise_data['exercises']
        
        for i, ex in enumerate(exercises, 1):
            self.print_colored(f"\n🎯 EXERCÍCIO {i}/{len(exercises)} - {ex['type'].upper()}:", "accent")
            self.print_colored(ex['instruction'], "text")
            
            self.print_colored("\n📝 CÓDIGO PARA COMPLETAR:", "info")
            print(ex['starter'])
            
            self.print_colored(f"\n👉 Complete as partes indicadas por ____", "warning")
            resposta = input("Sua resposta: ").strip()
            
            if resposta.lower() == ex['solution'].lower():
                self.print_success("✅ Perfeito! Código completado corretamente!")
                
                # Executa o código completo
                codigo_completo = ex['starter'].replace('____', ex['solution'])
                self.print_colored("\n🚀 Executando código completo:", "success")
                try:
                    exec(codigo_completo)
                except Exception as e:
                    self.print_warning(f"Erro na execução: {e}")
            else:
                self.print_warning("❌ Não está correto. Vamos ver a solução:")
                self.print_colored(f"💡 Resposta correta: {ex['solution']}", "info")
                
                codigo_completo = ex['starter'].replace('____', ex['solution'])
                self.print_colored("\n🚀 Código correto funcionando:", "success")
                try:
                    exec(codigo_completo)
                except Exception as e:
                    self.print_warning(f"Erro na execução: {e}")
            
            if i < len(exercises):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _run_creative_exercise(self, exercise_data: Dict[str, Any]) -> None:
        """Executa exercício criativo"""
        self.print_section(f"CRIATIVO: {exercise_data['title']}", "🎨", "warning")
        
        self.print_colored(exercise_data['instruction'], "text")
        
        self.print_colored("\n💡 EXEMPLOS DE REGRAS:", "info")
        self.print_colored("• Mínimo 8 caracteres", "text")
        self.print_colored("• Pelo menos 1 letra maiúscula", "text")
        self.print_colored("• Pelo menos 1 número", "text")
        self.print_colored("• Pelo menos 1 símbolo especial", "text")
        
        self.print_colored("\n🛠️ CRIE SEU PADRÃO:", "accent")
        padrao = input("Digite seu padrão regex: ").strip()
        
        if padrao:
            self.print_colored("\n🧪 TESTANDO SEU PADRÃO:", "success")
            
            senhas_teste = [
                "123456",
                "MinhaSenh@123", 
                "senha",
                "SENHA123!",
                "MinhaSenhaSegura@2024"
            ]
            
            try:
                import re
                pattern = re.compile(padrao)
                
                for senha in senhas_teste:
                    resultado = "✅ Válida" if pattern.match(senha) else "❌ Inválida"
                    print(f"   '{senha}' → {resultado}")
                
                self.print_success("\n🎉 Ótimo trabalho criando seu próprio validador!")
                
            except re.error as e:
                self.print_warning(f"❌ Erro no padrão regex: {e}")
                self.print_tip("💡 Lembre-se: use \\ para escapar caracteres especiais")
        else:
            self.print_tip("💡 Não tem problema! Criar regex é um processo de aprendizado.")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre Regex",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie seu próprio validador de senhas",
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

    def _mini_projeto_analisador_texto_inteligente(self) -> None:
        """Mini Projeto - Módulo 22: Analisador de Texto Inteligente"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: ANALISADOR DE TEXTO INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: ANALISADOR DE TEXTO INTELIGENTE")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um analisador de texto profissional usando Regex!")

        self.print_concept(
            "Analisador de Texto Inteligente",
            "Um sistema que processa textos extraindo informações, validando dados, detectando padrões e gerando relatórios automáticos"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "🏢 Empresas - Analisar emails e documentos corporativos",
            "📱 Redes Sociais - Detectar spam e conteúdo inadequado", 
            "🏦 Bancos - Processar extratos e identificar transações",
            "📰 Jornalismo - Extrair informações de artigos e notícias",
            "🛡️ Segurança - Monitorar logs e detectar ameaças",
            "📊 Marketing - Analisar feedback de clientes"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        input("\n🔸 Pressione ENTER para começar a construção...")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o código completo que você criou:", "text")

        codigo_final = '''# 🔍 PROJETO: ANALISADOR DE TEXTO INTELIGENTE
# Módulo 22: Expressões Regulares (Regex)

import re
from collections import Counter, defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json

class AnalisadorTextoInteligente:
    """Sistema completo de análise de texto usando Regex"""
    
    def __init__(self):
        self.resultados = {}
        self.patterns = self._inicializar_patterns()
        self.stats = {
            'textos_analisados': 0,
            'padroes_encontrados': 0,
            'tempo_total': 0
        }
    
    def _inicializar_patterns(self):
        """Inicializa todos os padrões regex"""
        return {
            # Informações de contato
            'emails': re.compile(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'),
            'telefones_br': re.compile(r'\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}'),
            'urls': re.compile(r'https?://[\\w\\.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?'),
            
            # Documentos brasileiros
            'cpfs': re.compile(r'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}'),
            'cnpjs': re.compile(r'\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}'),
            'ceps': re.compile(r'\\d{5}-\\d{3}'),
            
            # Datas e horários
            'datas_br': re.compile(r'\\d{1,2}/\\d{1,2}/\\d{4}'),
            'datas_iso': re.compile(r'\\d{4}-\\d{2}-\\d{2}'),
            'horarios': re.compile(r'\\d{1,2}:\\d{2}(?::\\d{2})?'),
            
            # Valores monetários
            'valores_reais': re.compile(r'R\\$\\s?([\\d.,]+)'),
            'valores_dolares': re.compile(r'\\$([\\d.,]+)'),
            'percentuais': re.compile(r'(\\d+(?:,\\d+)?)%'),
            
            # Redes sociais
            'mencoes': re.compile(r'@(\\w+)'),
            'hashtags': re.compile(r'#(\\w+)'),
            
            # Cartões e códigos
            'cartoes_credito': re.compile(r'\\d{4}\\s?\\d{4}\\s?\\d{4}\\s?\\d{4}'),
            'ips': re.compile(r'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b'),
            
            # Padrões de segurança
            'senhas_expostas': re.compile(r'(?:senha|password|pwd)\\s*[:=]\\s*(\\S+)', re.IGNORECASE),
            'sql_injection': re.compile(r'(union|select|insert|drop|delete|exec)\\s', re.IGNORECASE),
            'xss_patterns': re.compile(r'<script[^>]*>|javascript:', re.IGNORECASE),
            
            # Análise de sentimento básica
            'palavras_positivas': re.compile(r'\\b(ótimo|excelente|maravilhoso|perfeito|adorei|amei)\\b', re.IGNORECASE),
            'palavras_negativas': re.compile(r'\\b(péssimo|terrível|horrível|odeio|detesto|ruim)\\b', re.IGNORECASE)
        }
    
    def analisar_texto_completo(self, texto: str, incluir_seguranca: bool = True) -> Dict:
        """Análise completa de um texto"""
        inicio = datetime.now()
        
        resultado = {
            'texto_original': texto,
            'estatisticas_basicas': self._analisar_estatisticas_basicas(texto),
            'contatos': self._extrair_contatos(texto),
            'documentos': self._extrair_documentos(texto),
            'datas_horarios': self._extrair_datas_horarios(texto),
            'valores_financeiros': self._extrair_valores_financeiros(texto),
            'redes_sociais': self._extrair_redes_sociais(texto),
            'codigos_tecnicos': self._extrair_codigos_tecnicos(texto),
            'analise_sentimento': self._analisar_sentimento(texto)
        }
        
        if incluir_seguranca:
            resultado['alertas_seguranca'] = self._detectar_padroes_seguranca(texto)
        
        # Atualiza estatísticas
        fim = datetime.now()
        self.stats['textos_analisados'] += 1
        self.stats['tempo_total'] += (fim - inicio).total_seconds()
        
        return resultado
    
    def _analisar_estatisticas_basicas(self, texto: str) -> Dict:
        """Análise estatística básica do texto"""
        palavras = texto.split()
        linhas = texto.split('\\n')
        
        return {
            'caracteres_total': len(texto),
            'caracteres_sem_espacos': len(texto.replace(' ', '')),
            'palavras': len(palavras),
            'linhas': len(linhas),
            'paragrafos': len([p for p in texto.split('\\n\\n') if p.strip()]),
            'palavra_mais_comum': Counter(palavras).most_common(1)[0] if palavras else None,
            'tamanho_medio_palavra': sum(len(p) for p in palavras) / len(palavras) if palavras else 0
        }
    
    def _extrair_contatos(self, texto: str) -> Dict:
        """Extrai informações de contato"""
        return {
            'emails': self.patterns['emails'].findall(texto),
            'telefones': self.patterns['telefones_br'].findall(texto),
            'urls': self.patterns['urls'].findall(texto)
        }
    
    def _extrair_documentos(self, texto: str) -> Dict:
        """Extrai documentos brasileiros"""
        return {
            'cpfs': self.patterns['cpfs'].findall(texto),
            'cnpjs': self.patterns['cnpjs'].findall(texto),
            'ceps': self.patterns['ceps'].findall(texto)
        }
    
    def _extrair_datas_horarios(self, texto: str) -> Dict:
        """Extrai datas e horários"""
        return {
            'datas_brasileiras': self.patterns['datas_br'].findall(texto),
            'datas_iso': self.patterns['datas_iso'].findall(texto),
            'horarios': self.patterns['horarios'].findall(texto)
        }
    
    def _extrair_valores_financeiros(self, texto: str) -> Dict:
        """Extrai valores monetários"""
        return {
            'valores_reais': self.patterns['valores_reais'].findall(texto),
            'valores_dolares': self.patterns['valores_dolares'].findall(texto),
            'percentuais': self.patterns['percentuais'].findall(texto)
        }
    
    def _extrair_redes_sociais(self, texto: str) -> Dict:
        """Extrai padrões de redes sociais"""
        return {
            'mencoes': self.patterns['mencoes'].findall(texto),
            'hashtags': self.patterns['hashtags'].findall(texto)
        }
    
    def _extrair_codigos_tecnicos(self, texto: str) -> Dict:
        """Extrai códigos técnicos"""
        return {
            'cartoes_credito': self.patterns['cartoes_credito'].findall(texto),
            'enderecos_ip': self.patterns['ips'].findall(texto)
        }
    
    def _detectar_padroes_seguranca(self, texto: str) -> Dict:
        """Detecta padrões de segurança problemáticos"""
        alertas = {
            'senhas_expostas': self.patterns['senhas_expostas'].findall(texto),
            'tentativas_sql_injection': self.patterns['sql_injection'].findall(texto),
            'padroes_xss': bool(self.patterns['xss_patterns'].search(texto))
        }
        
        # Contabiliza alertas
        total_alertas = sum(len(v) if isinstance(v, list) else (1 if v else 0) for v in alertas.values())
        alertas['total_alertas'] = total_alertas
        alertas['nivel_risco'] = 'ALTO' if total_alertas > 5 else 'MÉDIO' if total_alertas > 2 else 'BAIXO'
        
        return alertas
    
    def _analisar_sentimento(self, texto: str) -> Dict:
        """Análise básica de sentimento"""
        positivas = len(self.patterns['palavras_positivas'].findall(texto))
        negativas = len(self.patterns['palavras_negativas'].findall(texto))
        
        if positivas > negativas:
            sentimento = 'POSITIVO'
        elif negativas > positivas:
            sentimento = 'NEGATIVO'
        else:
            sentimento = 'NEUTRO'
        
        return {
            'sentimento_geral': sentimento,
            'palavras_positivas': positivas,
            'palavras_negativas': negativas,
            'score': positivas - negativas
        }
    
    def gerar_relatorio(self, resultado: Dict) -> str:
        """Gera relatório textual da análise"""
        relatorio = []
        relatorio.append("=" * 60)
        relatorio.append("    RELATÓRIO DE ANÁLISE DE TEXTO INTELIGENTE")
        relatorio.append("=" * 60)
        
        # Estatísticas básicas
        stats = resultado['estatisticas_basicas']
        relatorio.append(f"\\n📊 ESTATÍSTICAS BÁSICAS:")
        relatorio.append(f"   • Caracteres: {stats['caracteres_total']:,}")
        relatorio.append(f"   • Palavras: {stats['palavras']:,}")
        relatorio.append(f"   • Linhas: {stats['linhas']:,}")
        relatorio.append(f"   • Parágrafos: {stats['paragrafos']:,}")
        
        # Informações de contato
        contatos = resultado['contatos']
        if any(contatos.values()):
            relatorio.append(f"\\n📞 INFORMAÇÕES DE CONTATO:")
            if contatos['emails']:
                relatorio.append(f"   • Emails ({len(contatos['emails'])}): {', '.join(contatos['emails'][:3])}")
            if contatos['telefones']:
                relatorio.append(f"   • Telefones ({len(contatos['telefones'])}): {', '.join(contatos['telefones'][:3])}")
            if contatos['urls']:
                relatorio.append(f"   • URLs ({len(contatos['urls'])}): {', '.join(contatos['urls'][:2])}")
        
        # Documentos
        docs = resultado['documentos']
        if any(docs.values()):
            relatorio.append(f"\\n🆔 DOCUMENTOS ENCONTRADOS:")
            for tipo, lista in docs.items():
                if lista:
                    relatorio.append(f"   • {tipo.upper()}: {len(lista)} encontrado(s)")
        
        # Valores financeiros
        valores = resultado['valores_financeiros']
        if any(valores.values()):
            relatorio.append(f"\\n💰 VALORES FINANCEIROS:")
            for tipo, lista in valores.items():
                if lista:
                    relatorio.append(f"   • {tipo.replace('_', ' ').title()}: {len(lista)} encontrado(s)")
        
        # Sentimento
        sentimento = resultado['analise_sentimento']
        relatorio.append(f"\\n😊 ANÁLISE DE SENTIMENTO:")
        relatorio.append(f"   • Sentimento geral: {sentimento['sentimento_geral']}")
        relatorio.append(f"   • Score: {sentimento['score']} (positivas: {sentimento['palavras_positivas']}, negativas: {sentimento['palavras_negativas']})")
        
        # Alertas de segurança
        if 'alertas_seguranca' in resultado:
            alertas = resultado['alertas_seguranca']
            relatorio.append(f"\\n🛡️ ALERTAS DE SEGURANÇA:")
            relatorio.append(f"   • Nível de risco: {alertas['nivel_risco']}")
            relatorio.append(f"   • Total de alertas: {alertas['total_alertas']}")
        
        return "\\n".join(relatorio)
    
    def processar_multiplos_textos(self, textos: List[str]) -> Dict:
        """Processa múltiplos textos e gera análise consolidada"""
        resultados = []
        
        for i, texto in enumerate(textos, 1):
            print(f"   Processando texto {i}/{len(textos)}...")
            resultado = self.analisar_texto_completo(texto)
            resultados.append(resultado)
        
        # Consolidação
        consolidado = {
            'total_textos': len(textos),
            'total_caracteres': sum(r['estatisticas_basicas']['caracteres_total'] for r in resultados),
            'total_palavras': sum(r['estatisticas_basicas']['palavras'] for r in resultados),
            'emails_unicos': len(set([email for r in resultados for email in r['contatos']['emails']])),
            'sentimento_predominante': Counter([r['analise_sentimento']['sentimento_geral'] for r in resultados]).most_common(1)[0][0],
            'detalhes_individuais': resultados
        }
        
        return consolidado

# === DEMONSTRAÇÃO PRÁTICA ===

print("🔍 ANALISADOR DE TEXTO INTELIGENTE")
print("=" * 50)

# Criar instância do analisador
analisador = AnalisadorTextoInteligente()

# Texto de exemplo rico em informações
texto_exemplo = \"\"\"
Prezados clientes,

Gostaríamos de informar sobre as promoções de fim de ano! 
Ofertas incríveis com até 50% de desconto.

📞 Contatos:
- Email: vendas@loja.com.br
- Telefone: (11) 99999-8888
- WhatsApp: (21) 88888-7777
- Site: https://www.loja.com.br

💰 Produtos em destaque:
- Notebook por R$ 2.499,00 (antes R$ 3.500,00)
- Smartphone por R$ 899,50
- Tablet com 30% de desconto

📅 Promoção válida até 31/12/2024 às 23:59

🆔 Documentos para compra:
- CPF: 123.456.789-00
- Endereço: CEP 01234-567

Sigam nossas redes sociais @lojatecnologia #promoção #tecnologia

Atenciosamente,
Equipe de Vendas
Data: 15/12/2024
\"\"\"

print("📄 TEXTO PARA ANÁLISE:")
print(texto_exemplo[:200] + "..." if len(texto_exemplo) > 200 else texto_exemplo)

print("\\n🔄 INICIANDO ANÁLISE COMPLETA...")

# Realizar análise completa
resultado_analise = analisador.analisar_texto_completo(texto_exemplo)

# Gerar e exibir relatório
relatorio = analisador.gerar_relatorio(resultado_analise)
print(relatorio)

# Demonstrar análise de múltiplos textos
print("\\n" + "="*50)
print("📊 ANÁLISE DE MÚLTIPLOS TEXTOS")

textos_exemplo = [
    "Ótimo atendimento! Adorei o produto. Email: cliente1@test.com",
    "Péssimo serviço, detestei tudo. Telefone: (11) 98765-4321",
    "Produto ok, nada demais. Contato: suporte@empresa.com.br"
]

resultado_multiplo = analisador.processar_multiplos_textos(textos_exemplo)
print(f"\\n📈 RESULTADO CONSOLIDADO:")
print(f"   • Textos analisados: {resultado_multiplo['total_textos']}")
print(f"   • Total de palavras: {resultado_multiplo['total_palavras']}")
print(f"   • Emails únicos: {resultado_multiplo['emails_unicos']}")
print(f"   • Sentimento predominante: {resultado_multiplo['sentimento_predominante']}")

print("\\n🎯 ESTATÍSTICAS DO SISTEMA:")
print(f"   • Textos processados: {analisador.stats['textos_analisados']}")
print(f"   • Tempo total de processamento: {analisador.stats['tempo_total']:.3f}s")

print("\\n✅ ANALISADOR DE TEXTO INTELIGENTE CONCLUÍDO!")
print("🚀 Funcionalidades implementadas:")
print("   • Extração automática de contatos, documentos, datas")
print("   • Análise de sentimento em português")
print("   • Detecção de padrões de segurança")
print("   • Relatórios detalhados e estatísticas")
print("   • Processamento em lote de múltiplos textos")
print("   • Performance tracking e métricas")'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um Analisador de Texto Inteligente!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🔗 Integrar com APIs de processamento de linguagem natural",
            "📊 Adicionar gráficos e visualizações dos resultados",
            "🤖 Implementar machine learning para melhor análise de sentimento",
            "🌐 Criar interface web para upload de arquivos",
            "📱 Desenvolver aplicativo móvel para análise em tempo real",
            "🛡️ Expandir detecção de ameaças de segurança"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Padrões de Texto!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Analisador de Texto Inteligente")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo22Regex()
    print("Teste do módulo 22 - versão standalone")
    module._regex()