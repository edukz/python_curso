#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 25: Terminal e Command Line Interface
VERSÃO REFATORADA seguindo o padrão pedagógico estabelecido
Aprenda a dominar o terminal e criar CLIs profissionais de forma interativa
"""

from ..shared.base_module import BaseModule
import subprocess
import os
import sys
import shlex
import time
import random
from typing import Dict, List, Optional, Any
from pathlib import Path


class Modulo25TerminalCli(BaseModule):
    """Módulo 25: Terminal e Command Line Interface - Dominando a Linha de Comando"""
    
    def __init__(self):
        super().__init__("modulo_25", "Terminal e Command Line Interface")
        self.has_mini_project = True
        self.mini_project_points = 120
    
    def execute(self) -> None:
        """Executa o módulo Terminal e CLI"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._terminal_cli()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _terminal_cli(self) -> None:
        """Conteúdo principal do módulo Terminal e CLI"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐧 MÓDULO 25: TERMINAL E COMMAND LINE INTERFACE")
        else:
            print("\n" + "="*60)
            print("🐧 MÓDULO 25: TERMINAL E COMMAND LINE INTERFACE")
            print("="*60)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo do Terminal e CLIs!")
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
            self._mini_projeto_sistema_cli_profissional()
        except KeyboardInterrupt:
            self.print_warning("\n\n⚠️ Mini projeto interrompido. Voltando ao menu principal...")
            return

        # 4. Marcar módulo como completo
        self.complete_module()
    
    def _navegacao_secoes_interativas(self) -> None:
        """Sistema de navegação por seções do módulo"""

        # === DEFINIÇÃO DAS SEÇÕES (6 SEÇÕES) ===
        secoes = [
            {
                'id': 'secao_conceito_terminal',
                'titulo': '🎯 O que é o Terminal?',
                'descricao': 'Entenda o poder da linha de comando',
                'funcao': self._secao_conceito_terminal
            },
            {
                'id': 'secao_comandos_essenciais',
                'titulo': '⚡ Comandos Essenciais',
                'descricao': 'Domine os comandos básicos para produtividade',
                'funcao': self._secao_comandos_essenciais
            },
            {
                'id': 'secao_navegacao_arquivos',
                'titulo': '📁 Navegação e Arquivos',
                'descricao': 'Manipule arquivos como um profissional',
                'funcao': self._secao_navegacao_arquivos
            },
            {
                'id': 'secao_pipes_automacao',
                'titulo': '🔄 Pipes e Automação',
                'descricao': 'Conecte comandos e automatize tarefas',
                'funcao': self._secao_pipes_automacao
            },
            {
                'id': 'secao_cli_python',
                'titulo': '🐍 CLIs com Python',
                'descricao': 'Crie ferramentas de linha de comando em Python',
                'funcao': self._secao_cli_python
            },
            {
                'id': 'secao_ferramentas_avancadas',
                'titulo': '🚀 Ferramentas Avançadas',
                'descricao': 'Click, argumentos e CLIs profissionais',
                'funcao': self._secao_ferramentas_avancadas
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

    def _secao_conceito_terminal(self) -> None:
        """Seção: O que é o Terminal?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE É O TERMINAL?", "🎯")

        # === DEFINIÇÃO DO CONCEITO (SEMPRE PRIMEIRO) ===
        self.print_concept(
            "Terminal",
            "Uma interface de texto onde você pode dar comandos diretamente ao computador, como uma conversa com o sistema operacional"
        )

        # === DICA RELACIONADA ===
        self.print_tip("O terminal é mais rápido que interfaces gráficas para muitas tarefas!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você tem dois jeitos de pedir pizza:", "text")
        self.print_colored("• 🖱️ Interface gráfica = aplicativo com botões (fácil, mas limitado)", "text")
        self.print_colored("• ⌨️ Terminal = telefonar direto (mais rápido, mais opções)", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. Você digita um comando (ex: 'ls' para listar arquivos)",
            "2. O terminal envia o comando para o sistema operacional",
            "3. O sistema executa a ação solicitada",
            "4. O resultado é mostrado na tela em texto"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO (SE APLICÁVEL) ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        self.print_colored(f"Sistema detectado: {sistema}", "info")
        
        if sistema == "Windows":
            exemplo_cmd = """# No Windows (Command Prompt)
dir                    # Lista arquivos
cd pasta              # Entra em uma pasta  
mkdir nova_pasta      # Cria pasta
type arquivo.txt      # Mostra conteúdo do arquivo
"""
        else:
            exemplo_cmd = """# No Linux/macOS (Bash)
ls                    # Lista arquivos
cd pasta             # Entra em uma pasta
mkdir nova_pasta     # Cria pasta  
cat arquivo.txt      # Mostra conteúdo do arquivo
"""
        
        self.exemplo(exemplo_cmd)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🚀 NASA - controla missões espaciais via terminal",
            "🏦 Bancos - sistemas financeiros críticos",
            "🎮 Gaming - servidores de jogos online",
            "📱 Smartphones - Android e iOS usam terminal internamente",
            "☁️ Cloud - AWS, Google Cloud, Azure"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_comandos_essenciais(self) -> None:
        """Seção: Comandos Essenciais"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMANDOS ESSENCIAIS DO TERMINAL", "⚡", "success")

        self.print_concept(
            "Comandos Básicos",
            "Ferramentas fundamentais que todo programador precisa dominar para ser produtivo"
        )

        # Detectar sistema operacional
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        self.print_colored(f"\n🖥️ Sistema detectado: {sistema}", "info")

        # === COMANDOS POR CATEGORIA ===
        categorias = [
            {
                'nome': '📁 NAVEGAÇÃO',
                'comandos': [
                    ("ls / dir", "Lista arquivos e pastas", "ls -la", "dir /w"),
                    ("cd", "Muda de pasta", "cd /home/user", "cd C:\\Users"),
                    ("pwd / cd", "Mostra pasta atual", "pwd", "cd"),
                    ("ls .. / dir ..", "Lista pasta anterior", "ls ..", "dir ..")
                ]
            },
            {
                'nome': '📝 ARQUIVOS',
                'comandos': [
                    ("touch / echo", "Cria arquivo", "touch arquivo.txt", "echo. > arquivo.txt"),
                    ("cat / type", "Mostra conteúdo", "cat arquivo.txt", "type arquivo.txt"),
                    ("cp / copy", "Copia arquivo", "cp orig.txt copia.txt", "copy orig.txt copia.txt"),
                    ("rm / del", "Remove arquivo", "rm arquivo.txt", "del arquivo.txt")
                ]
            },
            {
                'nome': '🗂️ PASTAS',
                'comandos': [
                    ("mkdir", "Cria pasta", "mkdir nova_pasta", "mkdir nova_pasta"),
                    ("rmdir / rm -r", "Remove pasta", "rm -rf pasta", "rmdir /s pasta"),
                    ("mv / move", "Move/renomeia", "mv old.txt new.txt", "move old.txt new.txt")
                ]
            }
        ]

        for categoria in categorias:
            self.print_colored(f"\n{categoria['nome']}", "warning")
            
            for comando, descricao, exemplo_unix, exemplo_win in categoria['comandos']:
                self.print_colored(f"\n🔸 {comando}", "cyan")
                self.print_colored(f"   {descricao}", "text")
                
                if sistema == "Windows":
                    self.print_colored(f"   💡 Exemplo: {exemplo_win}", "accent")
                else:
                    self.print_colored(f"   💡 Exemplo: {exemplo_unix}", "accent")
            
            input("\n⏭️ Pressione ENTER para próxima categoria...")

        # === DICAS DE PRODUTIVIDADE ===
        self.print_colored("\n🚀 DICAS DE PRODUTIVIDADE:", "success")
        dicas = [
            "⌨️ Use Tab para autocompletar nomes",
            "🔄 Ctrl+C cancela comando atual",
            "⬆️ Use setas ↑↓ para navegar no histórico", 
            "📋 Ctrl+A seleciona toda a linha",
            "✂️ Ctrl+U apaga linha inteira",
            "🔍 Use wildcards: *.txt para todos os .txt"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "primary")

        self.pausar()

    def _secao_navegacao_arquivos(self) -> None:
        """Seção: Navegação e Arquivos"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("NAVEGAÇÃO E MANIPULAÇÃO DE ARQUIVOS", "📁", "info")

        self.print_concept(
            "Sistema de Arquivos",
            "A estrutura hierárquica onde todos os arquivos e pastas do computador são organizados, como uma árvore gigante"
        )

        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA:", "warning")
        self.print_colored("O sistema de arquivos é como um prédio de apartamentos:", "text")
        self.print_colored("• 🏢 Raiz (/) = Térreo do prédio", "text") 
        self.print_colored("• 📁 Pastas = Andares do prédio", "text")
        self.print_colored("• 📄 Arquivos = Apartamentos", "text")
        self.print_colored("• 🗺️ Caminho = Endereço completo", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === NAVEGAÇÃO EFICIENTE ===
        self.print_colored("\n🧭 NAVEGAÇÃO EFICIENTE:", "info")
        
        navegacao_exemplos = [
            {
                'titulo': 'ATALHOS ESPECIAIS',
                'codigo': '''# Símbolos especiais para navegação
~         # Sua pasta home (/home/usuario)
.         # Pasta atual (onde você está agora)
..        # Pasta pai (uma acima)
-         # Pasta anterior (onde você estava antes)

# Exemplos práticos:
cd ~          # Vai para sua pasta home
cd ..         # Sobe um nível
cd ../..      # Sobe dois níveis  
cd -          # Volta para pasta anterior'''
            },
            {
                'titulo': 'LISTAGEM AVANÇADA',
                'codigo': '''# Opções do comando ls (Linux/Mac):
ls -l         # Lista detalhada (permissões, tamanho, data)
ls -a         # Inclui arquivos ocultos (começam com .)
ls -la        # Combinação: detalhada + ocultos
ls -lh        # Tamanhos legíveis (KB, MB, GB)
ls -lt        # Ordenar por data de modificação
ls -lS        # Ordenar por tamanho

# No Windows (comando dir):
dir /w        # Lista em colunas
dir /a        # Inclui arquivos ocultos
dir /s        # Lista recursivamente (subpastas)'''
            },
            {
                'titulo': 'BUSCA DE ARQUIVOS',
                'codigo': '''# Comando find (Linux/Mac) - muito poderoso:
find . -name "*.py"           # Busca arquivos .py na pasta atual
find . -type f -size +1M      # Arquivos maiores que 1MB
find . -mtime -7              # Modificados nos últimos 7 dias
find /home -name "config*"    # Busca por nome na pasta /home

# No Windows:
where python                  # Localiza o executável python
dir *.txt /s                  # Busca todos .txt recursivamente'''
            }
        ]

        for exemplo in navegacao_exemplos:
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.exemplo(exemplo['codigo'])
            input("\n⏭️ Pressione ENTER para próximo exemplo...")

        # === MANIPULAÇÃO PRÁTICA ===
        self.print_colored("\n✂️ MANIPULAÇÃO PRÁTICA DE ARQUIVOS:", "success")
        
        manipulacao = '''# CRIAR arquivos e pastas
echo "Olá mundo" > arquivo.txt    # Cria arquivo com conteúdo
mkdir -p pasta/subpasta          # Cria estrutura de pastas

# COPIAR de forma inteligente  
cp -r pasta_origem/ backup/      # Copia pasta inteira
cp *.jpg fotos/                  # Copia todas as imagens JPG

# MOVER e RENOMEAR
mv arquivo.txt documentos/       # Move arquivo para pasta
mv nome_antigo.txt nome_novo.txt # Renomeia arquivo

# REMOVER com segurança
rm -i arquivo.txt               # Pergunta antes de remover
rm -rf pasta_vazia/             # Remove pasta e todo conteúdo'''

        self.exemplo(manipulacao)
        
        # === APLICAÇÕES REAIS ===
        self.print_colored("\n🌍 APLICAÇÕES NO MUNDO REAL:", "accent")
        aplicacoes = [
            "📊 Analistas de dados - organizam datasets gigantes",
            "🎮 Game developers - gerenciam assets de jogos", 
            "🎬 Editores de vídeo - manipulam arquivos de mídia",
            "☁️ DevOps - deployam aplicações em servidores",
            "🔬 Cientistas - processam dados de experimentos"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_pipes_automacao(self) -> None:
        """Seção: Pipes e Automação"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("PIPES E AUTOMAÇÃO", "🔄", "warning")

        self.print_concept(
            "Pipes",
            "Uma forma de conectar comandos como peças de LEGO, onde a saída de um comando vira entrada do próximo"
        )

        # === ANALOGIA ===
        self.print_colored("\n🏭 ANALOGIA DA FÁBRICA:", "warning")
        self.print_colored("Pipes são como uma linha de produção na fábrica:", "text")
        self.print_colored("• 🏭 Estação 1: comando1 (processa matéria-prima)", "text")
        self.print_colored("• 🔄 Esteira: | (pipe - transporta resultado)", "text") 
        self.print_colored("• 🏭 Estação 2: comando2 (refina o produto)", "text")
        self.print_colored("• 📦 Resultado: produto final", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXEMPLOS PROGRESSIVOS ===
        exemplos_pipes = [
            {
                'nivel': 'BÁSICO',
                'titulo': 'Conectando 2 comandos',
                'codigo': '''# Sintaxe: comando1 | comando2
# A saída do comando1 vira entrada do comando2

ls -la | grep ".py"          # Lista arquivos, depois filtra só .py
cat arquivo.txt | head -5    # Mostra arquivo, depois só 5 primeiras linhas
ps aux | grep python         # Lista processos, depois só os que têm python''',
                'explicacao': 'O pipe (|) é como um cano que conecta dois comandos'
            },
            {
                'nivel': 'INTERMEDIÁRIO', 
                'titulo': 'Contagem e estatísticas',
                'codigo': '''# Contar elementos
ls | wc -l                   # Conta quantos arquivos tem na pasta
cat arquivo.txt | wc -w      # Conta palavras no arquivo
grep "função" *.py | wc -l   # Conta quantas vezes "função" aparece

# Ordenar resultados
ls -la | sort -k5 -n         # Lista arquivos ordenados por tamanho
cat nomes.txt | sort         # Ordena lista de nomes alfabeticamente''',
                'explicacao': 'wc = word count (contador), sort = ordenador'
            },
            {
                'nivel': 'AVANÇADO',
                'titulo': 'Análise de dados complexa',
                'codigo': '''# Pipeline completo de análise
cat access.log | grep "404" | cut -d' ' -f1 | sort | uniq -c | sort -nr
# 1. Lê log de servidor
# 2. Filtra apenas erros 404  
# 3. Extrai só o IP (coluna 1)
# 4. Ordena os IPs
# 5. Conta IPs únicos
# 6. Ordena por quantidade (maior primeiro)
# RESULTADO: IPs que mais geraram erro 404!''',
                'explicacao': 'Pipeline real usado para análise de logs de servidor'
            }
        ]

        for exemplo in exemplos_pipes:
            self.print_colored(f"\n🎯 NÍVEL {exemplo['nivel']}: {exemplo['titulo']}", "info")
            self.exemplo(exemplo['codigo'])
            self.print_colored(f"💡 {exemplo['explicacao']}", "accent")
            input("\n⏭️ Pressione ENTER para próximo nível...")

        # === REDIRECIONAMENTO ===
        self.print_colored("\n📤 REDIRECIONAMENTO DE SAÍDA:", "success")
        
        redirecionamento = '''# Salvar resultados em arquivos
comando > arquivo.txt        # Sobrescreve arquivo
comando >> arquivo.txt       # Adiciona ao final do arquivo
comando 2> erros.txt         # Salva apenas erros
comando > saida.txt 2>&1     # Salva saída normal E erros

# Exemplos práticos:
ls -la > listagem.txt                    # Salva listagem de arquivos
python script.py > log.txt 2>&1         # Captura tudo do script
echo "Backup $(date)" >> backup.log     # Adiciona timestamp ao log'''

        self.exemplo(redirecionamento)

        # === AUTOMAÇÃO ===
        self.print_colored("\n🤖 AUTOMAÇÃO COM SHELL SCRIPT:", "warning")
        
        script_exemplo = '''#!/bin/bash
# Script para backup automático de arquivos Python

# Variáveis
BACKUP_DIR="$HOME/backup_python"
DATA=$(date +%Y%m%d_%H%M%S)

# Criar pasta de backup se não existir
mkdir -p "$BACKUP_DIR"

# Encontrar e copiar todos arquivos .py
echo "🔍 Procurando arquivos Python..."
find . -name "*.py" -type f | while read arquivo; do
    echo "📋 Copiando: $arquivo"
    cp "$arquivo" "$BACKUP_DIR/$(basename $arquivo)_$DATA"
done

echo "✅ Backup concluído em: $BACKUP_DIR"
echo "📊 $(ls $BACKUP_DIR | wc -l) arquivos salvos"'''

        self.exemplo(script_exemplo)

        self.print_colored("\n🌍 ONDE PIPES SÃO USADOS:", "accent")
        aplicacoes = [
            "📊 Análise de big data - processar terabytes de logs",
            "🔍 Cybersecurity - detectar ataques em tempo real", 
            "📈 Monitoramento - alertas automáticos de sistema",
            "🧬 Bioinformática - análise de sequências de DNA",
            "💰 Finanças - análise de transações e fraudes"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_cli_python(self) -> None:
        """Seção: CLIs com Python"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CRIANDO CLIS COM PYTHON", "🐍", "info")

        self.print_concept(
            "CLI (Command Line Interface)",
            "Um programa que você executa no terminal passando argumentos, como uma ferramenta profissional"
        )

        # === ANALOGIA ===
        self.print_colored("\n🛠️ ANALOGIA DA FERRAMENTA:", "warning")
        self.print_colored("Uma CLI é como uma chave de fenda profissional:", "text")
        self.print_colored("• 🔧 Ferramenta principal: seu programa Python", "text")
        self.print_colored("• 🎛️ Configurações: argumentos que você passa", "text")
        self.print_colored("• 📋 Manual: help automático", "text")
        self.print_colored("• ⚙️ Resultado: ação executada", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === ARGPARSE BÁSICO ===
        self.print_colored("\n📚 ARGPARSE - BIBLIOTECA NATIVA DO PYTHON:", "info")
        
        exemplo_basico = '''#!/usr/bin/env python3
import argparse
import sys

def main():
    # Criar o parser (analisador de argumentos)
    parser = argparse.ArgumentParser(
        description='📝 Contador de linhas em arquivos',
        epilog='Exemplo: python contador.py arquivo.txt --palavras'
    )
    
    # Argumentos posicionais (obrigatórios)
    parser.add_argument('arquivo', 
                       help='📄 Arquivo para analisar')
    
    # Argumentos opcionais
    parser.add_argument('-l', '--linhas', 
                       action='store_true',
                       help='🔢 Contar linhas')
    
    parser.add_argument('-p', '--palavras',
                       action='store_true', 
                       help='📝 Contar palavras')
    
    parser.add_argument('-v', '--verbose',
                       action='store_true',
                       help='💬 Modo verboso')
    
    # Processar argumentos
    args = parser.parse_args()
    
    # Usar os argumentos
    if args.verbose:
        print(f"🔍 Analisando arquivo: {args.arquivo}")
    
    try:
        with open(args.arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            linhas = conteudo.split('\\n')
            palavras = conteudo.split()
        
        if args.linhas:
            print(f"📏 Linhas: {len(linhas)}")
        
        if args.palavras:
            print(f"📝 Palavras: {len(palavras)}")
            
        if not args.linhas and not args.palavras:
            print(f"📏 Linhas: {len(linhas)}")
            print(f"📝 Palavras: {len(palavras)}")
            
    except FileNotFoundError:
        print(f"❌ Arquivo '{args.arquivo}' não encontrado")
        sys.exit(1)

if __name__ == '__main__':
    main()'''

        self.print_colored("🎯 CLI BÁSICA COM ARGPARSE:", "warning")
        self.exemplo(exemplo_basico)
        
        self.print_colored("\n💡 Como usar esta CLI:", "accent")
        uso_basico = '''# Exemplos de uso:
python contador.py documento.txt              # Conta linhas e palavras
python contador.py documento.txt --linhas     # Só linhas
python contador.py documento.txt -p           # Só palavras  
python contador.py documento.txt -v -l -p     # Verboso + tudo
python contador.py --help                     # Mostra ajuda'''
        
        self.exemplo(uso_basico)
        input("\n⏭️ Pressione ENTER para ver exemplo avançado...")

        # === ARGPARSE AVANÇADO ===
        self.print_colored("\n🚀 CLI AVANÇADA COM SUBCOMANDOS:", "success")
        
        exemplo_avancado = '''#!/usr/bin/env python3
import argparse
import json
import csv
from pathlib import Path

def processar_arquivo(arquivo, formato, filtro=None):
    """Processa arquivo de dados"""
    if formato == 'json':
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    elif formato == 'csv':
        with open(arquivo, 'r') as f:
            reader = csv.DictReader(f)
            dados = list(reader)
    
    if filtro:
        dados = [item for item in dados 
                if filtro.lower() in str(item).lower()]
    
    return dados

def main():
    # Parser principal
    parser = argparse.ArgumentParser(description='🔧 Processador de Dados')
    parser.add_argument('--config', type=Path,
                       help='📋 Arquivo de configuração')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                       help='💬 Nível de verbosidade (-v, -vv)')
    
    # Subcomandos
    subparsers = parser.add_subparsers(dest='comando', 
                                     help='🎯 Comandos disponíveis')
    
    # Comando 'processar'
    proc_parser = subparsers.add_parser('processar', 
                                       help='⚙️ Processar arquivo')
    proc_parser.add_argument('arquivo', type=Path, 
                           help='📄 Arquivo de entrada')
    proc_parser.add_argument('--formato', 
                           choices=['json', 'csv'], required=True,
                           help='📋 Formato do arquivo')
    proc_parser.add_argument('--filtro', 
                           help='🔍 Filtro para aplicar')
    proc_parser.add_argument('--saida', type=Path,
                           help='💾 Arquivo de saída')
    
    # Comando 'info'
    info_parser = subparsers.add_parser('info', 
                                       help='ℹ️ Info sobre arquivo')
    info_parser.add_argument('arquivo', type=Path,
                           help='📄 Arquivo para analisar')
    
    args = parser.parse_args()
    
    # Configurar verbosidade
    if args.verbose >= 2:
        print("🔧 Modo debug ativado")
    elif args.verbose >= 1:
        print("💬 Modo verboso ativado")
    
    # Executar comando
    if args.comando == 'processar':
        if not args.arquivo.exists():
            print(f"❌ Arquivo {args.arquivo} não existe")
            return 1
        
        dados = processar_arquivo(args.arquivo, args.formato, args.filtro)
        
        if args.verbose:
            print(f"📊 {len(dados)} registros processados")
        
        if args.saida:
            with open(args.saida, 'w') as f:
                json.dump(dados, f, indent=2)
            print(f"💾 Dados salvos em {args.saida}")
        else:
            print(json.dumps(dados, indent=2))
    
    elif args.comando == 'info':
        if args.arquivo.exists():
            stat = args.arquivo.stat()
            print(f"📁 Arquivo: {args.arquivo}")
            print(f"📏 Tamanho: {stat.st_size:,} bytes")
        else:
            print(f"❌ Arquivo {args.arquivo} não existe")
    
    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())'''

        self.exemplo(exemplo_avancado)
        
        self.print_colored("\n💡 Como usar a CLI avançada:", "accent")
        uso_avancado = '''# Exemplos de uso:
python processador.py processar dados.csv --formato csv --filtro "python"
python processador.py processar dados.json --formato json --saida resultado.json
python processador.py info dados.csv
python processador.py --help
python processador.py processar --help'''
        
        self.exemplo(uso_avancado)

        # === DICAS PROFISSIONAIS ===
        self.print_colored("\n🎯 DICAS PARA CLIS PROFISSIONAIS:", "warning")
        dicas = [
            "📝 Sempre adicione help= para cada argumento",
            "🔧 Use type= para validação automática (int, Path, etc)",
            "✅ choices= limita opções válidas", 
            "🚩 action='store_true' para flags booleanas",
            "📊 action='count' para níveis (-v, -vv, -vvv)",
            "⚠️ Sempre trate erros com try/except",
            "🎨 Use emojis para deixar a saída mais amigável",
            "📋 epilog= adiciona exemplos de uso"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "primary")

        self.pausar()

    def _secao_ferramentas_avancadas(self) -> None:
        """Seção: Ferramentas Avançadas"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("FERRAMENTAS AVANÇADAS PARA CLI", "🚀", "accent")

        self.print_concept(
            "Framework Click",
            "Uma biblioteca moderna que torna a criação de CLIs Python mais fácil e elegante, como um upgrade do argparse"
        )

        # === POR QUE CLICK? ===
        self.print_colored("\n⭐ POR QUE USAR CLICK?", "warning")
        vantagens = [
            "🎨 Sintaxe mais limpa com decorators",
            "🌈 Cores automáticas no terminal",
            "📊 Progress bars integradas",
            "❓ Prompts interativos",
            "🧪 Sistema de testes incluído",
            "🔌 Extensível com plugins",
            "📚 Documentação excelente"
        ]
        
        for vantagem in vantagens:
            self.print_colored(f"• {vantagem}", "primary")

        input("\n🔸 Pressione ENTER para ver Click em ação...")

        # === CLICK BÁSICO ===
        self.print_colored("\n📦 INSTALAÇÃO DO CLICK:", "info")
        self.exemplo("pip install click")
        
        self.print_colored("\n🎯 CLI BÁSICA COM CLICK:", "warning")
        
        click_basico = '''#!/usr/bin/env python3
import click
import os
from pathlib import Path

@click.command()
@click.argument('arquivo', type=click.Path(exists=True))
@click.option('--saida', '-o', default='resultado.txt',
              help='📄 Arquivo de saída')
@click.option('--linhas', '-n', default=10, type=int,
              help='🔢 Número de linhas')
@click.option('--verbose', '-v', is_flag=True,
              help='💬 Modo verboso')
@click.option('--formato', type=click.Choice(['txt', 'json']),
              default='txt', help='📋 Formato de saída')
def processar(arquivo, saida, linhas, verbose, formato):
    """🔧 Processa arquivo e gera saída formatada."""
    
    if verbose:
        click.echo(f"🔄 Processando {arquivo}...")
        click.echo(f"📋 Formato: {formato}")
        click.echo(f"📊 Linhas: {linhas}")
    
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.readlines()[:linhas]
        
        if formato == 'json':
            import json
            dados = {'linhas': [linha.strip() for linha in conteudo]}
            with open(saida, 'w') as f:
                json.dump(dados, f, indent=2)
        else:
            with open(saida, 'w') as f:
                f.writelines(conteudo)
        
        # Click colorido automático!
        click.echo(f"✅ Processamento concluído: {saida}", fg='green')
        
    except Exception as e:
        click.echo(f"❌ Erro: {e}", fg='red')
        raise click.Abort()

if __name__ == '__main__':
    processar()'''

        self.exemplo(click_basico)

        input("\n⏭️ Pressione ENTER para ver Click avançado...")

        # === CLICK AVANÇADO ===
        self.print_colored("\n🚀 CLI PROFISSIONAL COM CLICK:", "success")
        
        click_avancado = '''#!/usr/bin/env python3
import click
import time
import json
from pathlib import Path

@click.group()
@click.option('--debug', is_flag=True, help='🐛 Modo debug')
@click.pass_context
def cli(ctx, debug):
    """🎯 Minha ferramenta CLI profissional"""
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    
    if debug:
        click.echo("🐛 Modo debug ativado", fg='yellow')

@cli.command()
@click.argument('diretorio', type=click.Path(exists=True, file_okay=False))
@click.option('--extensao', '-e', default='.py',
              help='📄 Extensão dos arquivos')
@click.pass_context
def contar(ctx, diretorio, extensao):
    """📊 Conta arquivos em diretório."""
    
    if ctx.obj['DEBUG']:
        click.echo(f"🔍 Procurando {extensao} em {diretorio}")
    
    path = Path(diretorio)
    arquivos = list(path.rglob(f'*{extensao}'))
    
    # Progress bar automática!
    with click.progressbar(arquivos, label='Contando arquivos') as bar:
        total_linhas = 0
        for arquivo in bar:
            if arquivo.is_file():
                try:
                    with open(arquivo, 'r', encoding='utf-8') as f:
                        total_linhas += len(f.readlines())
                except:
                    pass
    
    click.echo(f"📊 Encontrados: {len(arquivos)} arquivos {extensao}")
    click.echo(f"📝 Total de linhas: {total_linhas:,}")

@cli.command()
@click.option('--nome', prompt='Seu nome', help='👤 Nome do usuário')
@click.option('--idade', type=int, help='🎂 Sua idade')
@click.option('--senha', prompt=True, hide_input=True, 
              confirmation_prompt=True, help='🔒 Senha')
def cadastro(nome, idade, senha):
    """📋 Cadastro interativo."""
    
    if not idade:
        idade = click.prompt('Sua idade', type=int)
    
    # Confirmação interativa
    if click.confirm(f'Cadastrar {nome}, {idade} anos?'):
        # Simulação de salvamento
        with click.progressbar(range(3), label='Salvando') as bar:
            for i in bar:
                time.sleep(0.5)
        
        click.echo(f"✅ {nome} cadastrado com sucesso!", fg='green')
    else:
        click.echo("❌ Cadastro cancelado", fg='red')

@cli.command()
def cores():
    """🎨 Demonstração de cores."""
    click.echo(click.style('Texto verde', fg='green'))
    click.echo(click.style('Texto vermelho bold', fg='red', bold=True))
    click.echo(click.style('Fundo azul', bg='blue'))
    click.echo(click.style('Texto sublinhado', underline=True))

@cli.command()
@click.argument('arquivo', type=click.File('w'))
def temp(arquivo):
    """📄 Demonstração de arquivo temporário."""
    dados = {
        'timestamp': time.time(),
        'mensagem': 'Dados de exemplo'
    }
    
    json.dump(dados, arquivo, indent=2)
    click.echo(f"💾 Dados salvos em: {arquivo.name}")

if __name__ == '__main__':
    cli()'''

        self.exemplo(click_avancado)

        # === FUNCIONALIDADES ESPECIAIS ===
        self.print_colored("\n✨ FUNCIONALIDADES ESPECIAIS DO CLICK:", "accent")
        
        funcionalidades = '''# Testing automático
from click.testing import CliRunner

def test_comando():
    runner = CliRunner()
    result = runner.invoke(cores, [])
    assert result.exit_code == 0
    assert 'verde' in result.output

# Validação customizada
def validar_email(ctx, param, value):
    if '@' not in value:
        raise click.BadParameter('Email deve conter @')
    return value

@click.option('--email', callback=validar_email)
def usuario(email):
    click.echo(f"Email válido: {email}")

# Paginação automática para texto longo
@click.command()
def docs():
    texto_longo = "\\n".join([f"Linha {i}" for i in range(100)])
    click.echo_via_pager(texto_longo)'''

        self.exemplo(funcionalidades)

        # === COMPARAÇÃO ===
        self.print_colored("\n⚖️ ARGPARSE vs CLICK:", "warning")
        comparacao = [
            "📝 Sintaxe: argparse (verbosa) vs click (decorators)",
            "🎨 Cores: argparse (manual) vs click (automática)",
            "📊 Progress: argparse (externa) vs click (integrada)",
            "🧪 Testes: argparse (manual) vs click (framework)",
            "📚 Curva: argparse (steep) vs click (gentle)",
            "⚡ Performance: argparse (rápido) vs click (elegante)"
        ]
        
        for comp in comparacao:
            self.print_colored(f"• {comp}", "primary")

        self.print_colored("\n🌍 FERRAMENTAS CLI FAMOSAS FEITAS COM CLICK:", "accent")
        ferramentas = [
            "🌐 Flask - framework web Python",
            "📦 Pip - gerenciador de pacotes Python", 
            "☁️ AWS CLI - interface da Amazon Web Services",
            "🐋 Docker Compose - orquestração de containers",
            "📊 Jupyter - notebooks interativos"
        ]
        
        for ferramenta in ferramentas:
            self.print_colored(f"• {ferramenta}", "primary")

        self.pausar()

    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar o que você aprendeu sobre Terminal e CLIs!", "text")

        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para iniciantes: Cada exercício é opcional, mas recomendamos fazer todos!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Não se preocupe se errar - faz parte do aprendizado!", "text")
        self.print_colored("• Você pode tentar quantas vezes quiser", "text")
        self.print_colored("• Digite 'help' se precisar de ajuda", "text")
        self.print_colored("• Use Ctrl+C para voltar ao menu principal se necessário", "text")

        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos sobre Terminal")
            print("2. 💻 Complete o Código CLI")
            print("3. 🎨 Exercício Criativo: CLI Personalizada")
            print("0. Continuar para o Mini Projeto")

            try:
                escolha = input("\n👉 Sua escolha: ").strip().lower()

                if escolha in ["0", "continuar", "sair", "proximo"]:
                    break
                elif escolha in ["1", "quiz", "conhecimentos"]:
                    try:
                        self._run_quiz_terminal()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                elif escolha in ["2", "codigo", "completar"]:
                    try:
                        self._run_code_completion_cli()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                elif escolha in ["3", "criativo"]:
                    try:
                        self._run_creative_cli_exercise()
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício criativo interrompido. Voltando ao menu principal...")
                        return
                elif escolha in ["help", "ajuda", "h", "?"]:
                    self._show_help()
                else:
                    self.print_warning("❌ Opção inválida! Digite 1, 2, 3, 0 ou 'help' para ajuda.")

            except KeyboardInterrupt:
                self.print_warning("\n\n⚠️ Operação cancelada pelo usuário. Voltando ao menu principal...")
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")

    def _run_quiz_terminal(self) -> None:
        """Executa quiz sobre terminal e CLI"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("QUIZ: TERMINAL E CLI", "📝", "info")
        
        perguntas = [
            {
                'pergunta': 'Qual comando lista arquivos em um diretório no Linux?',
                'opcoes': ['a) list', 'b) ls', 'c) dir', 'd) show'],
                'resposta': 'b',
                'explicacao': 'ls é o comando padrão para listar arquivos no Linux/macOS'
            },
            {
                'pergunta': 'O que faz o pipe (|) em comandos do terminal?',
                'opcoes': ['a) Lista arquivos', 'b) Conecta a saída de um comando à entrada de outro', 'c) Copia arquivos', 'd) Remove arquivos'],
                'resposta': 'b', 
                'explicacao': 'O pipe conecta comandos, passando a saída do primeiro como entrada do segundo'
            },
            {
                'pergunta': 'Qual símbolo representa a pasta home do usuário?',
                'opcoes': ['a) /', 'b) .', 'c) ~', 'd) ..'],
                'resposta': 'c',
                'explicacao': 'O til (~) é um atalho para a pasta home do usuário atual'
            },
            {
                'pergunta': 'Para que serve o argparse em Python?',
                'opcoes': ['a) Criar interfaces gráficas', 'b) Processar argumentos de linha de comando', 'c) Conectar ao banco de dados', 'd) Fazer requisições HTTP'],
                'resposta': 'b',
                'explicacao': 'argparse é a biblioteca padrão do Python para criar CLIs'
            },
            {
                'pergunta': 'Qual vantagem do Click sobre argparse?',
                'opcoes': ['a) É mais rápido', 'b) Sintaxe mais limpa com decorators', 'c) Usa menos memória', 'd) É mais antigo'],
                'resposta': 'b',
                'explicacao': 'Click oferece sintaxe mais elegante usando decorators'
            }
        ]

        acertos = 0
        for i, pergunta in enumerate(perguntas, 1):
            try:
                self.print_colored(f"\n❓ PERGUNTA {i}/5:", "cyan")
                self.print_concept(pergunta['pergunta'])
                print()
                for opcao in pergunta['opcoes']:
                    self.print_tip(opcao)
                
                while True:
                    try:
                        resposta = input("\n🤔 Sua resposta (a/b/c/d): ").lower().strip()
                        if resposta in ['a', 'b', 'c', 'd']:
                            break
                        self.print_warning("Digite apenas a, b, c ou d")
                    except KeyboardInterrupt:
                        raise
                
                if resposta == pergunta['resposta']:
                    self.print_success("✅ Correto!")
                    acertos += 1
                else:
                    self.print_warning(f"❌ Incorreto. A resposta certa é: {pergunta['resposta']}")
                
                self.print_tip(f"💡 {pergunta['explicacao']}")
                
                if i < len(perguntas):
                    try:
                        input("\n⏭️ Pressione ENTER para próxima pergunta...")
                    except KeyboardInterrupt:
                        raise
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Quiz interrompido!")
                raise

        # Resultado final
        porcentagem = (acertos / len(perguntas)) * 100
        self.print_colored(f"\n🎯 RESULTADO: {acertos}/{len(perguntas)} ({porcentagem:.0f}%)", "cyan")
        
        if porcentagem >= 80:
            self.print_success("🏆 Excelente! Você domina o terminal!")
        elif porcentagem >= 60:
            self.print_success("👍 Bom trabalho! Continue praticando!")
        else:
            self.print_warning("📚 Revise os conceitos e tente novamente!")

        if self.progress:
            self.progress.add_points(acertos * 3)
            self.print_tip(f"🎁 +{acertos * 3} pontos pelo quiz!")

    def _run_code_completion_cli(self) -> None:
        """Executa exercícios de completar código CLI"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("COMPLETE O CÓDIGO CLI", "💻", "warning")
        
        exercicios = [
            {
                'nivel': 'BÁSICO',
                'instrucao': 'Complete o código para criar uma CLI que aceita um nome como argumento',
                'codigo_inicial': '''import argparse

def main():
    parser = argparse.ArgumentParser(description='Saudação CLI')
    
    # COMPLETE: adicionar argumento 'nome'
    parser.add_argument(_____)
    
    args = parser.parse_args()
    print(f"Olá, {args.nome}!")

if __name__ == '__main__':
    main()''',
                'solucao': "parser.add_argument('nome', help='Seu nome')",
                'explicacao': 'Argumentos posicionais são obrigatórios e definidos apenas pelo nome'
            },
            {
                'nivel': 'INTERMEDIÁRIO', 
                'instrucao': 'Complete para adicionar uma flag opcional --verbose',
                'codigo_inicial': '''import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arquivo')
    
    # COMPLETE: adicionar flag --verbose
    parser.add_argument(_____)
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Processando {args.arquivo}...")

if __name__ == '__main__':
    main()''',
                'solucao': "parser.add_argument('--verbose', action='store_true', help='Modo verboso')",
                'explicacao': 'action="store_true" cria uma flag booleana'
            },
            {
                'nivel': 'AVANÇADO',
                'instrucao': 'Complete o decorator Click para aceitar um arquivo e opção de formato',
                'codigo_inicial': '''import click

# COMPLETE: decorator click.command
_____
# COMPLETE: argumento arquivo
_____
# COMPLETE: opção formato com choices
_____
def processar(arquivo, formato):
    """Processa arquivo no formato especificado"""
    click.echo(f"Processando {arquivo} como {formato}")

if __name__ == '__main__':
    processar()''',
                'solucao': '''@click.command()
@click.argument('arquivo')
@click.option('--formato', type=click.Choice(['txt', 'json']), default='txt')''',
                'explicacao': 'Click usa decorators para definir argumentos e opções'
            }
        ]

        for i, exercicio in enumerate(exercicios, 1):
            try:
                self.print_colored(f"\n🎯 EXERCÍCIO {i} - NÍVEL {exercicio['nivel']}", "cyan")
                self.print_colored(exercicio['instrucao'], "text")
                
                self.print_colored("\n📝 CÓDIGO PARA COMPLETAR:", "warning")
                self.exemplo(exercicio['codigo_inicial'])
                
                try:
                    resposta = input(f"\n💭 Sua resposta (ou 'help' para dica): ").strip()
                    
                    if resposta.lower() == 'help':
                        self.print_tip(f"💡 Dica: {exercicio['explicacao']}")
                        resposta = input("💭 Agora sua resposta: ").strip()
                    
                    # Verificação simples (contém elementos chave)
                    solucao_elementos = exercicio['solucao'].lower().split()
                    resposta_elementos = resposta.lower().split()
                    
                    acertou = any(elem in resposta_elementos for elem in solucao_elementos)
                    
                    if acertou:
                        self.print_success("✅ Correto! Bem feito!")
                    else:
                        self.print_warning("❌ Não está correto. Veja a solução:")
                    
                    self.print_colored("\n✅ SOLUÇÃO:", "success")
                    self.exemplo(exercicio['solucao'])
                    self.print_tip(f"💡 {exercicio['explicacao']}")
                    
                except KeyboardInterrupt:
                    raise
                
                if i < len(exercicios):
                    try:
                        input("\n⏭️ Pressione ENTER para próximo exercício...")
                    except KeyboardInterrupt:
                        raise
                        
            except KeyboardInterrupt:
                self.print_warning("\n⚠️ Exercícios interrompidos!")
                raise

        if self.progress:
            self.progress.add_points(20)
            self.print_success("🎁 +20 pontos pelos exercícios de código!")

    def _run_creative_cli_exercise(self) -> None:
        """Executa exercício criativo de CLI"""
        if self.ui:
            self.ui.clear_screen()
            
        self.print_section("EXERCÍCIO CRIATIVO: CLI PESSOAL", "🎨", "accent")
        
        self.print_concept(
            "Desafio Criativo",
            "Vamos criar uma CLI personalizada que reflita sua personalidade e interesses!"
        )

        # === COLETA DE INFORMAÇÕES ===
        try:
            self.print_colored("\n🎯 PRIMEIRA ETAPA: Planejamento", "warning")
            nome = input("👤 Qual seu nome? ").strip()
            if not nome:
                nome = "Programador"
            
            interesse = input("🎯 Qual seu hobby favorito? ").strip()
            if not interesse:
                interesse = "programação"
            
            funcionalidade = input("🔧 Que funcionalidade sua CLI teria? (ex: calculadora, gerador de senhas): ").strip()
            if not funcionalidade:
                funcionalidade = "calculadora"
            
            self.print_colored(f"\n✨ Perfeito! Vamos criar a CLI '{nome.upper()}_TOOL' para {interesse}!", "success")
            
        except KeyboardInterrupt:
            raise

        # === GERAÇÃO DO CÓDIGO ===
        self.print_colored("\n🎯 SEGUNDA ETAPA: Implementação", "warning")
        
        codigo_personalizado = f'''#!/usr/bin/env python3
"""
{nome.upper()}_TOOL - CLI Personalizada
Uma ferramenta criada por {nome} para {interesse}
"""

import click
import random
import time
from datetime import datetime

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """🎯 {nome.upper()}_TOOL - Sua CLI personalizada para {interesse}"""
    click.echo(f"🎉 Bem-vindo à ferramenta de {nome}!")

@cli.command()
@click.option('--nome', default='{nome}', help='👤 Seu nome')
def saudar(nome):
    """👋 Saudação personalizada"""
    hora = datetime.now().hour
    
    if hora < 12:
        periodo = "Bom dia"
    elif hora < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"
    
    click.echo(f"{periodo}, {{nome}}! 🌟")
    click.echo(f"Pronto para trabalhar com {interesse}? 🚀")

@cli.command()
@click.argument('texto')
def animar(texto):
    """✨ Anima um texto com efeitos"""
    cores = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
    
    click.echo("🎬 Animando texto...")
    for i in range(3):
        cor = random.choice(cores)
        click.echo(click.style(f"   {texto}", fg=cor, bold=True))
        time.sleep(0.5)
    
    click.echo("✨ Animação concluída!")

@cli.command()
def motivar():
    """💪 Frases motivacionais para {interesse}"""
    frases = [
        f"🌟 Você é incrível em {interesse}!",
        f"🚀 Continue praticando {interesse}, você está evoluindo!",
        f"💪 {nome}, você tem potencial ilimitado!",
        f"🎯 Foque em {interesse} e alcance seus objetivos!",
        f"✨ Cada dia de prática em {interesse} te torna melhor!"
    ]
    
    frase = random.choice(frases)
    click.echo(click.style(frase, fg='green', bold=True))

@cli.command()
@click.option('--dificuldade', type=click.Choice(['facil', 'medio', 'dificil']),
              default='medio', help='🎯 Nível de dificuldade')
def {funcionalidade.lower().replace(' ', '_')}(dificuldade):
    """🔧 {funcionalidade.title()} personalizada"""
    click.echo(f"🔧 Executando {funcionalidade} no nível {{dificuldade}}...")
    
    # Simulação de processamento
    with click.progressbar(range(3), label='Processando') as bar:
        for i in bar:
            time.sleep(0.3)
    
    resultado = random.randint(1, 100)
    click.echo(f"✅ Resultado: {{resultado}}")
    click.echo(f"🎉 {funcionalidade.title()} executada com sucesso!")

@cli.command()
def sobre():
    """ℹ️ Informações sobre esta CLI"""
    click.echo("=" * 50)
    click.echo(f"🎯 {nome.upper()}_TOOL v1.0.0")
    click.echo(f"👤 Criada por: {nome}")
    click.echo(f"💝 Foco em: {interesse}")
    click.echo(f"🔧 Funcionalidade: {funcionalidade}")
    click.echo(f"📅 Criada em: {{datetime.now().strftime('%d/%m/%Y')}}")
    click.echo("=" * 50)
    click.echo("🚀 Feito com muito ❤️ e Python!")

if __name__ == '__main__':
    cli()'''

        self.print_colored("🎨 SUA CLI PERSONALIZADA:", "success")
        self.exemplo(codigo_personalizado)
        
        # === DEMONSTRAÇÃO ===
        self.print_colored("\n🎯 TERCEIRA ETAPA: Como usar", "warning")
        
        exemplos_uso = f'''# Como usar sua CLI personalizada:
python {nome.lower()}_tool.py --help                    # Ver ajuda
python {nome.lower()}_tool.py saudar                    # Saudação
python {nome.lower()}_tool.py saudar --nome "Amigo"     # Saudação personalizada
python {nome.lower()}_tool.py animar "Olá Mundo"       # Animar texto
python {nome.lower()}_tool.py motivar                   # Frase motivacional
python {nome.lower()}_tool.py {funcionalidade.lower().replace(' ', '_')} --dificuldade facil  # Sua funcionalidade
python {nome.lower()}_tool.py sobre                     # Info sobre a CLI'''

        self.exemplo(exemplos_uso)
        
        # === FEEDBACK ===
        self.print_colored("\n🎉 QUARTA ETAPA: Expansão", "success")
        self.print_colored("Ideias para expandir sua CLI:", "text")
        expansoes = [
            f"📊 Adicionar estatísticas de uso",
            f"💾 Salvar configurações pessoais",
            f"🔗 Integrar com APIs relacionadas a {interesse}",
            f"📱 Notificações personalizadas",
            f"🎨 Mais temas e cores",
            f"🔐 Sistema de login",
            f"📈 Gráficos e relatórios"
        ]
        
        for expansao in expansoes:
            self.print_colored(f"• {expansao}", "primary")

        if self.progress:
            self.progress.add_points(25)
            self.print_success("🎁 +25 pontos pelo exercício criativo!")

    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste conhecimentos sobre terminal e CLI",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de CLI",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie sua própria CLI personalizada",
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

    def _mini_projeto_sistema_cli_profissional(self) -> None:
        """Mini Projeto: Sistema CLI Profissional Completo"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: TASKMANAGER CLI")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: TASKMANAGER CLI")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um gerenciador de tarefas profissional via linha de comando!")

        self.print_concept(
            "TaskManager CLI",
            "Uma ferramenta completa de produtividade que permite gerenciar tarefas, categorias, prioridades e estatísticas, tudo via terminal"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de ferramenta é útil para:", "text")
        usos_praticos = [
            "📊 Gerentes de projeto - acompanhar tarefas da equipe",
            "💻 Desenvolvedores - organizar features e bugs",
            "📚 Estudantes - controlar atividades acadêmicas",
            "🏢 Profissionais - gestão pessoal de produtividade"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        input("\n🔸 Pressione ENTER para começar o desenvolvimento...")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Estrutura base
        self.print_section("PASSO 1: Estrutura Base da CLI", "📝", "info")
        self.print_tip("Vamos criar a base com Click framework e gerenciamento de dados")

        codigo_estrutura = '''#!/usr/bin/env python3
"""
TaskManager CLI - Gerenciador Profissional de Tarefas
Uma ferramenta completa para produtividade via linha de comando
"""

import click
import json
import os
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Any

# Arquivo de dados
DATA_FILE = Path.home() / '.taskmanager.json'

class TaskManager:
    """Gerenciador principal de tarefas"""
    
    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict[str, Any]]:
        """Carrega tarefas do arquivo JSON"""
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """Salva tarefas no arquivo JSON"""
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False, default=str)
    
    def get_next_id(self) -> int:
        """Retorna próximo ID disponível"""
        if not self.tasks:
            return 1
        return max(task.get('id', 0) for task in self.tasks) + 1

# Instância global
task_manager = TaskManager()'''

        self.exemplo(codigo_estrutura)
        input("\n⏭️ Pressione ENTER para o próximo passo...")

        # PASSO 2: Comandos principais
        self.print_section("PASSO 2: Comandos de Gerenciamento", "⚙️", "success")
        self.print_colored("Agora vamos implementar os comandos principais:", "text")

        codigo_comandos = '''@click.group()
@click.version_option(version='2.0.0')
def cli():
    """
    🚀 TaskManager CLI - Seu Gerenciador de Tarefas Profissional
    
    Organize suas tarefas de forma eficiente via linha de comando.
    """
    pass

@cli.command()
@click.argument('titulo')
@click.option('--prioridade', '-p', 
              type=click.Choice(['baixa', 'media', 'alta']), 
              default='media', help='🎯 Prioridade da tarefa')
@click.option('--categoria', '-c', default='geral', 
              help='📁 Categoria da tarefa')
@click.option('--prazo', '-d', help='📅 Prazo (YYYY-MM-DD)')
def add(titulo, prioridade, categoria, prazo):
    """➕ Adiciona uma nova tarefa."""
    
    task_id = task_manager.get_next_id()
    
    # Validar prazo se fornecido
    prazo_obj = None
    if prazo:
        try:
            prazo_obj = datetime.strptime(prazo, '%Y-%m-%d').date()
        except ValueError:
            click.echo("❌ Formato de data inválido. Use YYYY-MM-DD", fg='red')
            return
    
    nova_tarefa = {
        'id': task_id,
        'titulo': titulo,
        'prioridade': prioridade,
        'categoria': categoria,
        'status': 'pendente',
        'criada_em': datetime.now().isoformat(),
        'prazo': prazo_obj.isoformat() if prazo_obj else None,
        'concluida_em': None
    }
    
    task_manager.tasks.append(nova_tarefa)
    task_manager.save_tasks()
    
    # Feedback colorido
    cores_prioridade = {
        'baixa': 'green',
        'media': 'yellow',
        'alta': 'red'
    }
    
    click.echo(f"✅ Tarefa #{task_id} adicionada com sucesso!")
    click.echo(f"📋 Título: {titulo}")
    click.echo(f"🎯 Prioridade: " + 
              click.style(prioridade.title(), fg=cores_prioridade[prioridade]))
    click.echo(f"📁 Categoria: {categoria}")
    if prazo_obj:
        click.echo(f"📅 Prazo: {prazo_obj.strftime('%d/%m/%Y')}")

@cli.command()
@click.option('--status', '-s', 
              type=click.Choice(['todas', 'pendente', 'concluida']),
              default='todas', help='🔍 Filtrar por status')
@click.option('--categoria', '-c', help='📁 Filtrar por categoria')
@click.option('--formato', type=click.Choice(['tabela', 'json', 'csv']),
              default='tabela', help='📊 Formato de saída')
def list(status, categoria, formato):
    """📋 Lista tarefas com filtros opcionais."""
    
    # Filtrar tarefas
    tarefas_filtradas = task_manager.tasks
    
    if status != 'todas':
        tarefas_filtradas = [t for t in tarefas_filtradas if t['status'] == status]
    
    if categoria:
        tarefas_filtradas = [t for t in tarefas_filtradas if t['categoria'].lower() == categoria.lower()]
    
    if not tarefas_filtradas:
        click.echo("📭 Nenhuma tarefa encontrada com os filtros especificados")
        return
    
    # Ordenar por prioridade e data
    def priority_key(task):
        priority_order = {'alta': 3, 'media': 2, 'baixa': 1}
        return (priority_order.get(task['prioridade'], 0), task['id'])
    
    tarefas_filtradas.sort(key=priority_key, reverse=True)
    
    if formato == 'json':
        click.echo(json.dumps(tarefas_filtradas, indent=2, ensure_ascii=False, default=str))
        return
    
    if formato == 'csv':
        import csv
        import sys
        writer = csv.DictWriter(sys.stdout, fieldnames=['id', 'titulo', 'prioridade', 'categoria', 'status'])
        writer.writeheader()
        writer.writerows(tarefas_filtradas)
        return
    
    # Formato tabela
    click.echo("\\n📋 Lista de Tarefas:")
    click.echo("=" * 80)
    
    for task in tarefas_filtradas:
        # Ícones de status
        status_icon = "✅" if task['status'] == 'concluida' else "⏳"
        
        # Cores por prioridade
        cores_prioridade = {
            'baixa': 'green',
            'media': 'yellow', 
            'alta': 'red'
        }
        
        prioridade_colorida = click.style(
            f"[{task['prioridade'].upper()}]",
            fg=cores_prioridade[task['prioridade']]
        )
        
        # Formatação principal
        click.echo(f"{status_icon} #{task['id']} {prioridade_colorida} {task['titulo']}")
        click.echo(f"   📁 {task['categoria']} | 📅 {task['criada_em'][:10]}")
        
        # Prazo
        if task.get('prazo'):
            prazo_data = datetime.fromisoformat(task['prazo']).date()
            hoje = date.today()
            
            if prazo_data < hoje:
                click.echo(f"   ⚠️ Prazo vencido: {prazo_data.strftime('%d/%m/%Y')}", fg='red')
            elif prazo_data == hoje:
                click.echo(f"   🔥 Prazo hoje: {prazo_data.strftime('%d/%m/%Y')}", fg='yellow')
            else:
                click.echo(f"   📅 Prazo: {prazo_data.strftime('%d/%m/%Y')}")
        
        # Data de conclusão
        if task['status'] == 'concluida' and task.get('concluida_em'):
            click.echo(f"   ✅ Concluída: {task['concluida_em'][:10]}")
        
        click.echo()

@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    """✅ Marca tarefa como concluída."""
    
    for task in task_manager.tasks:
        if task['id'] == task_id:
            if task['status'] == 'concluida':
                click.echo(f"ℹ️ Tarefa #{task_id} já está concluída", fg='yellow')
                return
            
            task['status'] = 'concluida'
            task['concluida_em'] = datetime.now().isoformat()
            task_manager.save_tasks()
            
            click.echo(f"✅ Tarefa #{task_id} marcada como concluída!", fg='green')
            click.echo(f"🎉 Parabéns! Você completou: {task['titulo']}")
            return
    
    click.echo(f"❌ Tarefa #{task_id} não encontrada", fg='red')

@cli.command()
@click.argument('task_id', type=int)
@click.confirmation_option(prompt='🗑️ Tem certeza que deseja deletar esta tarefa?')
def delete(task_id):
    """🗑️ Remove uma tarefa permanentemente."""
    
    tarefas_originais = len(task_manager.tasks)
    task_manager.tasks = [t for t in task_manager.tasks if t['id'] != task_id]
    
    if len(task_manager.tasks) < tarefas_originais:
        task_manager.save_tasks()
        click.echo(f"🗑️ Tarefa #{task_id} removida com sucesso!", fg='yellow')
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada", fg='red')'''

        self.exemplo(codigo_comandos)
        input("\n⏭️ Pressione ENTER para o próximo passo...")

        # PASSO 3: Funcionalidades avançadas
        self.print_section("PASSO 3: Funcionalidades Avançadas", "🎬", "warning")

        codigo_avancado = '''@cli.command()
def stats():
    """📊 Mostra estatísticas detalhadas das tarefas."""
    
    if not task_manager.tasks:
        click.echo("📭 Nenhuma tarefa cadastrada ainda")
        return
    
    # Estatísticas gerais
    total = len(task_manager.tasks)
    pendentes = len([t for t in task_manager.tasks if t['status'] == 'pendente'])
    concluidas = len([t for t in task_manager.tasks if t['status'] == 'concluida'])
    
    # Estatísticas por categoria
    categorias = {}
    for task in task_manager.tasks:
        cat = task['categoria']
        if cat not in categorias:
            categorias[cat] = {'pendentes': 0, 'concluidas': 0}
        categorias[cat][task['status'] + 's'] += 1
    
    # Estatísticas por prioridade (apenas pendentes)
    prioridades = {'baixa': 0, 'media': 0, 'alta': 0}
    for task in task_manager.tasks:
        if task['status'] == 'pendente':
            prioridades[task['prioridade']] += 1
    
    # Tarefas vencidas
    hoje = date.today()
    vencidas = 0
    for task in task_manager.tasks:
        if (task['status'] == 'pendente' and 
            task.get('prazo') and 
            datetime.fromisoformat(task['prazo']).date() < hoje):
            vencidas += 1
    
    # Exibir estatísticas
    click.echo("\\n📊 ESTATÍSTICAS DETALHADAS:")
    click.echo("=" * 50)
    
    click.echo(f"📋 Total de tarefas: {total}")
    click.echo(f"⏳ Pendentes: " + click.style(str(pendentes), fg='yellow'))
    click.echo(f"✅ Concluídas: " + click.style(str(concluidas), fg='green'))
    
    if total > 0:
        taxa_conclusao = (concluidas / total) * 100
        click.echo(f"📈 Taxa de conclusão: {taxa_conclusao:.1f}%")
    
    if vencidas > 0:
        click.echo(f"⚠️ Tarefas vencidas: " + click.style(str(vencidas), fg='red'))
    
    # Por categoria
    click.echo("\\n📁 POR CATEGORIA:")
    for categoria, stats in categorias.items():
        total_cat = stats['pendentes'] + stats['concluidas']
        click.echo(f"   {categoria}: {total_cat} total "
                  f"({stats['pendentes']} pendentes, {stats['concluidas']} concluídas)")
    
    # Por prioridade
    click.echo("\\n🎯 PRIORIDADES PENDENTES:")
    for prioridade, count in prioridades.items():
        if count > 0:
            cores = {'baixa': 'green', 'media': 'yellow', 'alta': 'red'}
            click.echo(f"   {prioridade.title()}: " + 
                      click.style(str(count), fg=cores[prioridade]))

@cli.command()
@click.option('--categoria', help='📁 Limpar apenas uma categoria')
@click.confirmation_option(prompt='🧹 Deseja remover todas as tarefas concluídas?')
def clean(categoria):
    """🧹 Remove todas as tarefas concluídas."""
    
    tarefas_originais = len(task_manager.tasks)
    
    if categoria:
        task_manager.tasks = [
            t for t in task_manager.tasks 
            if not (t['status'] == 'concluida' and t['categoria'] == categoria)
        ]
        tipo = f"da categoria '{categoria}'"
    else:
        task_manager.tasks = [
            t for t in task_manager.tasks 
            if t['status'] != 'concluida'
        ]
        tipo = "de todas as categorias"
    
    removidas = tarefas_originais - len(task_manager.tasks)
    
    if removidas > 0:
        task_manager.save_tasks()
        click.echo(f"🧹 {removidas} tarefas concluídas removidas {tipo}!", fg='green')
    else:
        click.echo(f"📭 Nenhuma tarefa concluída encontrada {tipo}")

@cli.command()
def today():
    """📅 Mostra tarefas com prazo para hoje."""
    
    hoje = date.today()
    tarefas_hoje = []
    
    for task in task_manager.tasks:
        if (task['status'] == 'pendente' and 
            task.get('prazo') and 
            datetime.fromisoformat(task['prazo']).date() == hoje):
            tarefas_hoje.append(task)
    
    if not tarefas_hoje:
        click.echo("🎉 Nenhuma tarefa com prazo para hoje!")
        return
    
    click.echo(f"🔥 TAREFAS PARA HOJE ({hoje.strftime('%d/%m/%Y')}):")
    click.echo("=" * 50)
    
    for task in tarefas_hoje:
        cores_prioridade = {
            'baixa': 'green',
            'media': 'yellow',
            'alta': 'red'
        }
        
        prioridade_colorida = click.style(
            f"[{task['prioridade'].upper()}]",
            fg=cores_prioridade[task['prioridade']]
        )
        
        click.echo(f"⏰ #{task['id']} {prioridade_colorida} {task['titulo']}")
        click.echo(f"   📁 {task['categoria']}")
        click.echo()

@cli.command()
@click.argument('backup_file', type=click.Path())
def backup(backup_file):
    """💾 Cria backup das tarefas."""
    
    try:
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump({
                'backup_date': datetime.now().isoformat(),
                'tasks': task_manager.tasks
            }, f, indent=2, ensure_ascii=False, default=str)
        
        click.echo(f"💾 Backup criado com sucesso: {backup_file}")
        click.echo(f"📊 {len(task_manager.tasks)} tarefas salvas")
        
    except Exception as e:
        click.echo(f"❌ Erro ao criar backup: {e}", fg='red')

@cli.command()
@click.argument('backup_file', type=click.Path(exists=True))
@click.confirmation_option(prompt='⚠️ Isso substituirá todas as tarefas atuais. Continuar?')
def restore(backup_file):
    """♻️ Restaura tarefas de um backup."""
    
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        
        task_manager.tasks = backup_data['tasks']
        task_manager.save_tasks()
        
        click.echo(f"♻️ Backup restaurado com sucesso!")
        click.echo(f"📊 {len(task_manager.tasks)} tarefas restauradas")
        click.echo(f"📅 Backup de: {backup_data['backup_date'][:10]}")
        
    except Exception as e:
        click.echo(f"❌ Erro ao restaurar backup: {e}", fg='red')

if __name__ == '__main__':
    cli()'''

        self.exemplo(codigo_avancado)

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("\n🎯 CÓDIGO FINAL COMPLETO:", "text")

        codigo_final = '''#!/usr/bin/env python3
"""
TaskManager CLI v2.0 - Gerenciador Profissional de Tarefas
Ferramenta completa para produtividade via linha de comando

Funcionalidades:
- ✅ CRUD completo de tarefas
- 📊 Estatísticas e relatórios
- 📅 Gestão de prazos
- 🎯 Sistema de prioridades
- 📁 Organização por categorias
- 💾 Backup e restore
- 🎨 Interface colorida
- 📋 Múltiplos formatos de saída
"""

# [CÓDIGO COMPLETO COMBINADO DOS PASSOS ANTERIORES]
# Total: ~500 linhas de código Python profissional'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("EXEMPLOS DE USO", "🎬", "warning")
        
        exemplos_uso = '''# Gerenciamento básico
python taskmanager.py add "Estudar Python" --prioridade alta --categoria estudo
python taskmanager.py add "Comprar leite" --prioridade baixa --prazo 2024-12-31
python taskmanager.py list --status pendente
python taskmanager.py done 1

# Funcionalidades avançadas  
python taskmanager.py stats                              # Estatísticas
python taskmanager.py today                             # Tarefas de hoje
python taskmanager.py list --formato json               # Saída JSON
python taskmanager.py clean --categoria trabalho        # Limpeza seletiva
python taskmanager.py backup tarefas_backup.json       # Criar backup
python taskmanager.py restore tarefas_backup.json      # Restaurar backup

# Ajuda e documentação
python taskmanager.py --help                           # Ajuda geral
python taskmanager.py add --help                       # Ajuda específica'''

        self.exemplo(exemplos_uso)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema CLI profissional completo!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "🌐 Integração com APIs (Trello, Asana, Notion)",
            "📱 Sincronização com aplicativos móveis",
            "🔔 Sistema de notificações por email/SMS",
            "📊 Dashboard web complementar",
            "🤖 Automação com IA para sugerir prioridades",
            "👥 Colaboração em equipe",
            "📈 Análises avançadas de produtividade",
            "🔐 Autenticação e múltiplos usuários"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre em CLIs Profissionais!")

        # === REGISTRO DE CONCLUSÃO ===
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            self.print_success(f"🎁 +{self.mini_project_points} pontos pelo mini projeto!")
            
        self.complete_mini_project("TaskManager CLI Profissional")

        self.pausar()

    def exemplo(self, codigo: str) -> None:
        """Exibe exemplo de código"""
        if self.ui:
            self.ui.code_block(codigo, "Código")
        else:
            print("\n" + "="*50)
            print("CÓDIGO:")
            print("="*50)
            print(codigo)

    def pausar(self) -> None:
        """Pausa para o usuário ler"""
        try:
            input("\n🔸 Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            pass


# Para teste standalone
if __name__ == "__main__":
    module = Modulo25TerminalCli()
    print("Teste do módulo 25 - versão standalone")
    module._terminal_cli()