#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 25: Terminal e Command Line Interface
Aprenda a dominar o terminal e criar CLIs eficientes
"""

import subprocess
import os
import sys
import shlex
from ..shared.base_module import BaseModule


class Modulo25TerminalCli(BaseModule):
    """Módulo 25: Terminal e Command Line Interface"""
    
    def __init__(self):
        super().__init__("modulo_25", "Terminal e Command Line Interface")
        self.has_mini_project = True
        self.mini_project_points = 90
    
    def execute(self) -> None:
        """Executa o módulo sobre Terminal e CLI"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._terminal_cli_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _terminal_cli_module(self) -> None:
        """Conteúdo principal sobre Terminal e CLI"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐧 MÓDULO 25: TERMINAL E COMMAND LINE INTERFACE")
        else:
            print("\n" + "="*60)
            print("🐧 MÓDULO 25: TERMINAL E COMMAND LINE INTERFACE")
            print("="*60)
        
        print("💻 Domine o terminal e crie ferramentas CLI profissionais!")
        print("🎯 Tópicos abordados:")
        print("• Comandos essenciais do terminal")
        print("• Navegação e manipulação de arquivos")
        print("• Pipes, redirecionamento e shell scripting")
        print("• Python argparse para CLIs")
        print("• Click framework para CLIs avançadas")
        print("• Automação de tarefas com scripts")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._comandos_essenciais()
        self._navegacao_arquivos()
        self._pipes_redirecionamento()
        self._python_argparse()
        self._click_framework()
        self._mini_projeto_cli()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _comandos_essenciais(self):
        """Comandos essenciais do terminal"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚡ COMANDOS ESSENCIAIS DO TERMINAL")
        
        print("🛠️ Comandos fundamentais para produtividade:")
        
        # Determinar sistema operacional
        sistema = "Windows" if os.name == 'nt' else "Unix/Linux/macOS"
        print(f"📋 Sistema detectado: {sistema}")
        
        comandos_basicos = [
            ("ls / dir", "Listar arquivos e diretórios", "ls -la", "dir /w"),
            ("cd", "Mudar diretório", "cd /home/user", "cd C:\\Users"),
            ("pwd / cd", "Mostrar diretório atual", "pwd", "cd"),
            ("mkdir", "Criar diretório", "mkdir nova_pasta", "mkdir nova_pasta"),
            ("rmdir / rm", "Remover diretório", "rm -rf pasta", "rmdir /s pasta"),
            ("cp / copy", "Copiar arquivos", "cp arquivo.txt backup/", "copy arquivo.txt backup\\"),
            ("mv / move", "Mover/renomear", "mv old.txt new.txt", "move old.txt new.txt"),
            ("cat / type", "Exibir conteúdo", "cat arquivo.txt", "type arquivo.txt"),
            ("grep / findstr", "Buscar texto", "grep 'python' *.py", "findstr 'python' *.py"),
            ("ps / tasklist", "Processos ativos", "ps aux", "tasklist"),
            ("kill / taskkill", "Terminar processo", "kill 1234", "taskkill /PID 1234"),
            ("which / where", "Localizar comando", "which python", "where python")
        ]
        
        print(f"\n📋 Comandos básicos:")
        for comando, descricao, exemplo_unix, exemplo_win in comandos_basicos:
            print(f"\n🔸 {comando}")
            print(f"   {descricao}")
            if sistema == "Windows":
                print(f"   💡 Exemplo: {exemplo_win}")
            else:
                print(f"   💡 Exemplo: {exemplo_unix}")
        
        print("\n🔥 Comandos avançados:")
        avancados = [
            ("find", "Buscar arquivos", "find . -name '*.py' -type f"),
            ("chmod", "Alterar permissões", "chmod +x script.py"),
            ("chown", "Alterar proprietário", "chown user:group arquivo"),
            ("df", "Espaço em disco", "df -h"),
            ("du", "Uso de diretório", "du -sh *"),
            ("top/htop", "Monitor de sistema", "top"),
            ("curl", "Requisições HTTP", "curl -X GET https://api.github.com"),
            ("wget", "Download de arquivos", "wget https://exemplo.com/arquivo.zip"),
            ("ssh", "Conexão remota", "ssh user@servidor.com"),
            ("scp", "Cópia remota", "scp arquivo.txt user@server:/path/")
        ]
        
        for comando, descricao, exemplo in avancados:
            print(f"\n🚀 {comando}")
            print(f"   {descricao}")
            print(f"   💡 Exemplo: {exemplo}")
        
        print("\n💡 Dicas de produtividade:")
        print("• Use Tab para autocompletar")
        print("• Ctrl+C para cancelar comando")
        print("• Ctrl+Z para suspender processo")
        print("• !! para repetir último comando")
        print("• !comando para repetir último comando que começou com 'comando'")
        print("• history para ver histórico")
        print("• alias para criar atalhos")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _navegacao_arquivos(self):
        """Navegação e manipulação de arquivos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📁 NAVEGAÇÃO E MANIPULAÇÃO DE ARQUIVOS")
        
        print("🗂️ Dominando o sistema de arquivos:")
        
        print("\n🧭 Navegação eficiente:")
        navegacao = '''# Navegar rapidamente
cd ~           # Ir para home
cd -           # Voltar ao diretório anterior
cd ..          # Subir um nível
cd ../..       # Subir dois níveis
cd /           # Ir para raiz (Unix)

# Atalhos úteis
~              # Diretório home do usuário
.              # Diretório atual
..             # Diretório pai
/              # Raiz do sistema (Unix)
C:\\            # Unidade C (Windows)'''
        print(navegacao)
        
        print("\n📋 Listagem avançada:")
        listagem = '''# Opções do ls (Unix) / dir (Windows)
ls -l          # Lista detalhada
ls -a          # Inclui arquivos ocultos
ls -la         # Combinação dos dois
ls -lh         # Tamanhos legíveis (KB, MB)
ls -lt         # Ordenar por data modificação
ls -lS         # Ordenar por tamanho
ls -R          # Recursivo (subdiretórios)

# Windows
dir /w         # Lista em colunas
dir /s         # Recursivo
dir /a         # Inclui ocultos
dir /o:d       # Ordenar por data'''
        print(listagem)
        
        print("\n✂️ Manipulação de arquivos:")
        manipulacao = '''# Criar arquivos
touch arquivo.txt        # Criar arquivo vazio (Unix)
echo. > arquivo.txt      # Criar arquivo vazio (Windows)
echo "texto" > arquivo.txt  # Criar com conteúdo

# Copiar e mover
cp -r pasta/ backup/     # Copiar pasta recursivamente
cp *.txt backup/         # Copiar todos .txt
mv *.log logs/           # Mover todos .log

# Remover com segurança
rm arquivo.txt           # Remover arquivo
rm -i arquivo.txt        # Confirmar antes de remover
rm -rf pasta/            # Remover pasta e conteúdo
trash arquivo.txt        # Mover para lixeira (se disponível)'''
        print(manipulacao)
        
        print("\n🔍 Busca de arquivos:")
        busca = '''# find (Unix) - muito poderoso
find . -name "*.py"                    # Buscar arquivos .py
find . -type f -size +1M               # Arquivos > 1MB
find . -mtime -7                       # Modificados nos últimos 7 dias
find . -name "*.log" -delete           # Buscar e deletar logs

# Windows - where e forfiles
where python                           # Localizar executável
forfiles /m *.log /c "cmd /c del @path"  # Deletar todos .log'''
        print(busca)
        
        print("\n📊 Visualização de conteúdo:")
        visualizacao = '''# Exibir arquivos
cat arquivo.txt          # Mostrar todo o arquivo
head -n 10 arquivo.txt   # Primeiras 10 linhas
tail -n 10 arquivo.txt   # Últimas 10 linhas
tail -f log.txt          # Seguir arquivo (logs em tempo real)
less arquivo.txt         # Paginação (q para sair)
more arquivo.txt         # Paginação simples

# Buscar dentro de arquivos
grep "erro" *.log        # Buscar "erro" em logs
grep -i "python" *.py    # Busca case-insensitive
grep -r "função" .       # Busca recursiva
grep -n "import" *.py    # Mostrar números das linhas'''
        print(visualizacao)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _pipes_redirecionamento(self):
        """Pipes e redirecionamento"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔄 PIPES E REDIRECIONAMENTO")
        
        print("⚡ Conectando comandos para máxima eficiência:")
        
        print("\n📤 Redirecionamento de saída:")
        redirecionamento = '''# Redirecionar saída
comando > arquivo.txt         # Sobrescrever arquivo
comando >> arquivo.txt        # Anexar ao arquivo
comando 2> erros.txt          # Redirecionar erros
comando > saida.txt 2>&1      # Saída e erros no mesmo arquivo
comando &> tudo.txt           # Atalho para saída e erros

# Exemplos práticos
ls -la > listagem.txt         # Salvar listagem
python script.py > log.txt 2>&1  # Capturar tudo
echo "Backup $(date)" >> backup.log  # Log com timestamp'''
        print(redirecionamento)
        
        print("\n🔗 Pipes - conectando comandos:")
        pipes = '''# Sintaxe básica: comando1 | comando2
# A saída do comando1 vira entrada do comando2

# Exemplos fundamentais
ls -la | grep ".py"           # Listar apenas arquivos .py
cat arquivo.txt | grep "erro" # Buscar "erro" no arquivo
ps aux | grep python          # Processos Python rodando
history | tail -10            # Últimos 10 comandos

# Contagem e estatísticas
ls | wc -l                    # Contar arquivos no diretório
cat arquivo.txt | wc -w       # Contar palavras
grep "função" *.py | wc -l    # Contar ocorrências

# Ordenação
ls -la | sort -k5 -n          # Ordenar por tamanho (coluna 5)
cat nomes.txt | sort          # Ordenar alfabeticamente
du -h * | sort -hr            # Ordenar por tamanho (maior primeiro)'''
        print(pipes)
        
        print("\n⚙️ Comandos para processamento:")
        processamento = '''# cut - extrair colunas
ls -la | cut -d' ' -f1        # Primeira coluna (permissões)
cut -d',' -f2 dados.csv       # Segunda coluna de CSV

# awk - processamento avançado
ls -la | awk '{print $9, $5}' # Nome e tamanho
ps aux | awk '{sum+=$3} END {print sum}' # Soma de CPU

# sed - edição de texto
cat arquivo.txt | sed 's/antigo/novo/g'  # Substituir texto
ls | sed 's/.txt/.bak/'       # Trocar extensão

# uniq - remover duplicatas
cat lista.txt | sort | uniq   # Linhas únicas
history | cut -d' ' -f2 | sort | uniq -c  # Comandos mais usados'''
        print(processamento)
        
        print("\n🎯 Exemplos práticos complexos:")
        exemplos = '''# Análise de logs
cat access.log | grep "404" | cut -d' ' -f1 | sort | uniq -c | sort -nr
# Encontra IPs com mais erros 404

# Backup inteligente
tar -czf backup_$(date +%Y%m%d).tar.gz *.py | grep -v "__pycache__"
# Compacta arquivos Python, excluindo cache

# Monitoramento de sistema
ps aux | sort -k3 -nr | head -10 | awk '{print $11, $3"%"}'
# Top 10 processos por CPU

# Limpeza de logs antigos
find /var/log -name "*.log" -mtime +30 | xargs rm -f
# Remove logs mais antigos que 30 dias'''
        print(exemplos)
        
        print("\n🚀 Shell scripting básico:")
        shell_script = '''#!/bin/bash
# Exemplo de script simples

# Variáveis
BACKUP_DIR="/home/user/backup"
DATE=$(date +%Y%m%d)

# Função
backup_python() {
    echo "Fazendo backup dos arquivos Python..."
    find . -name "*.py" -exec cp {} $BACKUP_DIR/{}_$DATE \\;
}

# Execução
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

backup_python
echo "Backup concluído!"'''
        print(shell_script)
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _python_argparse(self):
        """Python argparse para CLIs"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐍 PYTHON ARGPARSE PARA CLIS")
        
        print("🛠️ Criando ferramentas de linha de comando profissionais:")
        
        print("\n📚 Introdução ao argparse:")
        print("• Biblioteca padrão do Python para CLIs")
        print("• Parsing automático de argumentos")
        print("• Geração automática de help")
        print("• Validação de tipos e valores")
        print("• Subcomandos e grupos")
        
        codigo_basico = '''#!/usr/bin/env python3
import argparse
import sys

def main():
    # Criar parser
    parser = argparse.ArgumentParser(
        description='Minha ferramenta CLI awesome',
        epilog='Exemplo: python script.py arquivo.txt --verbose'
    )
    
    # Argumentos posicionais
    parser.add_argument('arquivo', 
                       help='Arquivo para processar')
    
    # Argumentos opcionais
    parser.add_argument('-v', '--verbose', 
                       action='store_true',
                       help='Modo verboso')
    
    parser.add_argument('-o', '--output',
                       default='output.txt',
                       help='Arquivo de saída (padrão: output.txt)')
    
    parser.add_argument('-n', '--numero',
                       type=int,
                       default=10,
                       help='Número de linhas (padrão: 10)')
    
    # Parse dos argumentos
    args = parser.parse_args()
    
    # Usar argumentos
    if args.verbose:
        print(f"Processando {args.arquivo}...")
        print(f"Saída: {args.output}")
        print(f"Número: {args.numero}")
    
    # Lógica do programa
    try:
        with open(args.arquivo, 'r') as f:
            linhas = f.readlines()[:args.numero]
        
        with open(args.output, 'w') as f:
            f.writelines(linhas)
            
        if args.verbose:
            print(f"✅ {len(linhas)} linhas processadas!")
            
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{args.arquivo}' não encontrado")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()'''
        
        if self.ui:
            self.ui.code_block(codigo_basico, "CLI básica com argparse")
        else:
            print("\n" + "="*50)
            print("EXEMPLO BÁSICO:")
            print("="*50)
            print(codigo_basico)
        
        print("\n🔧 Funcionalidades avançadas:")
        
        codigo_avancado = '''import argparse
import json
import csv
from pathlib import Path

def processar_dados(arquivo, formato, filtro=None):
    """Processa arquivo de dados"""
    dados = []
    
    if formato == 'json':
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    elif formato == 'csv':
        with open(arquivo, 'r') as f:
            reader = csv.DictReader(f)
            dados = list(reader)
    
    if filtro:
        dados = [item for item in dados if filtro in str(item)]
    
    return dados

def main():
    parser = argparse.ArgumentParser(description='Processador de dados')
    
    # Subcomandos
    subparsers = parser.add_subparsers(dest='comando', help='Comandos disponíveis')
    
    # Comando 'processar'
    proc_parser = subparsers.add_parser('processar', help='Processar arquivo')
    proc_parser.add_argument('arquivo', type=Path, help='Arquivo de entrada')
    proc_parser.add_argument('--formato', choices=['json', 'csv'], 
                            required=True, help='Formato do arquivo')
    proc_parser.add_argument('--filtro', help='Filtro para aplicar aos dados')
    proc_parser.add_argument('--saida', type=Path, help='Arquivo de saída')
    
    # Comando 'info'
    info_parser = subparsers.add_parser('info', help='Informações sobre arquivo')
    info_parser.add_argument('arquivo', type=Path, help='Arquivo para analisar')
    
    # Argumentos globais
    parser.add_argument('--config', type=Path, 
                       default='config.json',
                       help='Arquivo de configuração')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                       help='Nível de verbosidade (use -vv para mais detalhes)')
    
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
        
        dados = processar_dados(args.arquivo, args.formato, args.filtro)
        
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
            print(f"📏 Tamanho: {stat.st_size} bytes")
            print(f"📅 Modificado: {stat.st_mtime}")
        else:
            print(f"❌ Arquivo {args.arquivo} não existe")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    exit(main())'''
        
        if self.ui:
            self.ui.code_block(codigo_avancado, "CLI avançada com subcomandos")
        else:
            print("\n" + "="*50)
            print("EXEMPLO AVANÇADO:")
            print("="*50)
            print(codigo_avancado)
        
        print("\n💡 Dicas para CLIs profissionais:")
        print("• Use type= para validação automática")
        print("• choices= para limitar opções")
        print("• action='store_true' para flags booleanas")
        print("• action='count' para verbosidade (-v, -vv)")
        print("• nargs= para múltiplos valores")
        print("• required=True para argumentos obrigatórios")
        print("• default= para valores padrão")
        print("• help= sempre para documentar argumentos")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _click_framework(self):
        """Click framework para CLIs avançadas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 CLICK FRAMEWORK PARA CLIS AVANÇADAS")
        
        print("✨ Click - framework moderno para CLIs Python:")
        print("• Decorators elegantes para definir comandos")
        print("• Validação automática de tipos")
        print("• Cores e formatação automática")
        print("• Progress bars e prompts interativos")
        print("• Testing integrado")
        print("• Plugins e extensibilidade")
        
        print("\n📦 Instalação:")
        print("pip install click")
        
        codigo_click_basico = '''#!/usr/bin/env python3
import click
import os
from pathlib import Path

@click.command()
@click.argument('arquivo', type=click.Path(exists=True))
@click.option('--saida', '-o', default='resultado.txt', 
              help='Arquivo de saída')
@click.option('--linhas', '-n', default=10, type=int,
              help='Número de linhas para processar')
@click.option('--verbose', '-v', is_flag=True,
              help='Modo verboso')
@click.option('--formato', type=click.Choice(['txt', 'json', 'csv']),
              default='txt', help='Formato de saída')
def processar(arquivo, saida, linhas, verbose, formato):
    """Processa arquivo e gera saída formatada."""
    
    if verbose:
        click.echo(f"🔄 Processando {arquivo}...")
        click.echo(f"📝 Formato: {formato}")
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
        
        click.echo(f"✅ Processamento concluído: {saida}", fg='green')
        
    except Exception as e:
        click.echo(f"❌ Erro: {e}", fg='red')
        raise click.Abort()

@click.group()
@click.option('--debug', is_flag=True, help='Modo debug')
@click.pass_context
def cli(ctx, debug):
    """Minha ferramenta CLI com Click."""
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    
    if debug:
        click.echo("🐛 Modo debug ativado", fg='yellow')

@cli.command()
@click.argument('diretorio', type=click.Path(exists=True, file_okay=False))
@click.option('--extensao', '-e', default='.py', 
              help='Extensão dos arquivos para contar')
@click.pass_context
def contar(ctx, diretorio, extensao):
    """Conta arquivos em um diretório."""
    
    if ctx.obj['DEBUG']:
        click.echo(f"🔍 Procurando arquivos {extensao} em {diretorio}")
    
    path = Path(diretorio)
    arquivos = list(path.rglob(f'*{extensao}'))
    
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
    click.echo(f"📝 Total de linhas: {total_linhas}")

@cli.command()
@click.option('--nome', prompt='Seu nome', help='Nome do usuário')
@click.option('--idade', type=int, help='Sua idade')
@click.option('--senha', prompt=True, hide_input=True, 
              confirmation_prompt=True, help='Sua senha')
def cadastro(nome, idade, senha):
    """Cadastro interativo de usuário."""
    
    if not idade:
        idade = click.prompt('Sua idade', type=int)
    
    # Confirmação
    if click.confirm(f'Cadastrar {nome}, {idade} anos?'):
        click.echo(f"✅ Usuário {nome} cadastrado com sucesso!", fg='green')
        # Aqui salvaria no banco de dados
    else:
        click.echo("❌ Cadastro cancelado", fg='red')

if __name__ == '__main__':
    cli()'''
        
        if self.ui:
            self.ui.code_block(codigo_click_basico, "CLI com Click framework")
        else:
            print("\n" + "="*50)
            print("EXEMPLO COM CLICK:")
            print("="*50)
            print(codigo_click_basico)
        
        print("\n🎨 Funcionalidades especiais do Click:")
        
        funcionalidades = '''import click
from datetime import datetime
import time

# Cores e estilos
@click.command()
def cores():
    click.echo(click.style('Texto verde', fg='green'))
    click.echo(click.style('Texto vermelho bold', fg='red', bold=True))
    click.echo(click.style('Fundo azul', bg='blue'))

# Progress bar
@click.command()
def download():
    items = list(range(100))
    with click.progressbar(items, label='Downloading') as bar:
        for item in bar:
            time.sleep(0.01)  # Simula trabalho

# Pager para texto longo
@click.command()
def docs():
    texto_longo = "\\n".join([f"Linha {i}" for i in range(100)])
    click.echo_via_pager(texto_longo)

# Validação customizada
def validar_email(ctx, param, value):
    if '@' not in value:
        raise click.BadParameter('Email deve conter @')
    return value

@click.command()
@click.option('--email', callback=validar_email, prompt=True)
def usuario(email):
    click.echo(f"Email válido: {email}")

# Arquivo temporário
@click.command()
@click.option('--temp', type=click.File('w'), 
              help='Arquivo temporário para escrita')
def temp_file(temp):
    if temp:
        temp.write("Dados temporários\\n")
        click.echo(f"Escrito em: {temp.name}")

# Testing com Click
def test_comando():
    from click.testing import CliRunner
    
    runner = CliRunner()
    result = runner.invoke(cores, [])
    
    assert result.exit_code == 0
    assert 'verde' in result.output'''
        
        if self.ui:
            self.ui.code_block(funcionalidades, "Funcionalidades avançadas do Click")
        else:
            print("\n" + "="*50)
            print("FUNCIONALIDADES AVANÇADAS:")
            print("="*50)
            print(funcionalidades)
        
        print("\n🚀 Por que usar Click?")
        print("• ✨ Sintaxe mais limpa que argparse")
        print("• 🎨 Cores e formatação automática")
        print("• 📊 Progress bars integradas")
        print("• 🔧 Validação robusta")
        print("• 🧪 Testing framework incluído")
        print("• 📚 Documentação excelente")
        print("• 🔌 Ecosistema de plugins")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_cli(self):
        """Mini projeto: Sistema CLI completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: FERRAMENTA CLI COMPLETA")
        
        print("📊 Vamos criar uma ferramenta CLI profissional!")
        print("🎯 Funcionalidades:")
        print("• Gerenciamento de tarefas (TODO list)")
        print("• Múltiplos comandos e subcomandos")
        print("• Persistência em arquivo JSON")
        print("• Interface colorida e amigável")
        print("• Validação e tratamento de erros")
        
        input("\n🔸 Pressione ENTER para começar o projeto...")
        
        codigo_projeto = '''#!/usr/bin/env python3
"""
TaskCLI - Gerenciador de Tarefas via Command Line
Uma ferramenta completa para gerenciar suas tarefas
"""

import click
import json
import os
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Any

# Arquivo de dados
DATA_FILE = Path.home() / '.taskcli.json'

class TaskManager:
    """Gerenciador de tarefas"""
    
    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict[str, Any]]:
        """Carrega tarefas do arquivo"""
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_tasks(self):
        """Salva tarefas no arquivo"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=2, default=str)
    
    def add_task(self, title: str, priority: str = 'medium', 
                 category: str = 'general') -> int:
        """Adiciona nova tarefa"""
        task_id = max([t.get('id', 0) for t in self.tasks], default=0) + 1
        
        task = {
            'id': task_id,
            'title': title,
            'priority': priority,
            'category': category,
            'status': 'pending',
            'created': datetime.now().isoformat(),
            'completed': None
        }
        
        self.tasks.append(task)
        self.save_tasks()
        return task_id
    
    def complete_task(self, task_id: int) -> bool:
        """Marca tarefa como completa"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                task['completed'] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Remove tarefa"""
        original_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        
        if len(self.tasks) < original_length:
            self.save_tasks()
            return True
        return False
    
    def get_tasks(self, status: str = None, category: str = None) -> List[Dict]:
        """Filtra tarefas"""
        filtered = self.tasks
        
        if status:
            filtered = [t for t in filtered if t['status'] == status]
        
        if category:
            filtered = [t for t in filtered if t['category'] == category]
        
        return filtered

# Instância global do gerenciador
task_manager = TaskManager()

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """
    🚀 TaskCLI - Gerenciador de Tarefas Profissional
    
    Gerencie suas tarefas de forma eficiente via linha de comando.
    """
    pass

@cli.command()
@click.argument('title')
@click.option('--priority', '-p', 
              type=click.Choice(['low', 'medium', 'high']), 
              default='medium', help='Prioridade da tarefa')
@click.option('--category', '-c', default='general', 
              help='Categoria da tarefa')
def add(title, priority, category):
    """Adiciona uma nova tarefa."""
    
    task_id = task_manager.add_task(title, priority, category)
    
    priority_color = {
        'low': 'green',
        'medium': 'yellow', 
        'high': 'red'
    }
    
    click.echo(f"✅ Tarefa adicionada com ID {task_id}")
    click.echo(f"📋 Título: {title}")
    click.echo(f"🎯 Prioridade: " + 
              click.style(priority, fg=priority_color[priority]))
    click.echo(f"📁 Categoria: {category}")

@cli.command()
@click.option('--status', '-s', 
              type=click.Choice(['pending', 'completed', 'all']),
              default='all', help='Filtrar por status')
@click.option('--category', '-c', help='Filtrar por categoria')
@click.option('--format', type=click.Choice(['table', 'json']),
              default='table', help='Formato de saída')
def list(status, category, format):
    """Lista tarefas."""
    
    # Filtrar tarefas
    if status == 'all':
        tasks = task_manager.get_tasks(category=category)
    else:
        tasks = task_manager.get_tasks(status=status, category=category)
    
    if not tasks:
        click.echo("📭 Nenhuma tarefa encontrada")
        return
    
    if format == 'json':
        click.echo(json.dumps(tasks, indent=2, default=str))
        return
    
    # Formato tabela
    click.echo("\\n📋 Lista de Tarefas:")
    click.echo("=" * 80)
    
    for task in sorted(tasks, key=lambda x: x['id']):
        status_icon = "✅" if task['status'] == 'completed' else "⏳"
        
        priority_colors = {
            'low': 'green',
            'medium': 'yellow',
            'high': 'red'
        }
        
        priority_styled = click.style(
            f"[{task['priority'].upper()}]", 
            fg=priority_colors[task['priority']]
        )
        
        click.echo(f"{status_icon} #{task['id']} {priority_styled} {task['title']}")
        click.echo(f"   📁 {task['category']} | 📅 {task['created'][:10]}")
        
        if task['status'] == 'completed' and task['completed']:
            click.echo(f"   ✅ Concluída em: {task['completed'][:10]}")
        
        click.echo()

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Marca tarefa como completa."""
    
    if task_manager.complete_task(task_id):
        click.echo(f"✅ Tarefa #{task_id} marcada como completa!", fg='green')
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada", fg='red')

@cli.command()
@click.argument('task_id', type=int)
@click.confirmation_option(prompt='Tem certeza que deseja deletar?')
def delete(task_id):
    """Remove uma tarefa."""
    
    if task_manager.delete_task(task_id):
        click.echo(f"🗑️ Tarefa #{task_id} removida!", fg='yellow')
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada", fg='red')

@cli.command()
def stats():
    """Mostra estatísticas das tarefas."""
    
    all_tasks = task_manager.get_tasks()
    pending = len([t for t in all_tasks if t['status'] == 'pending'])
    completed = len([t for t in all_tasks if t['status'] == 'completed'])
    
    # Estatísticas por categoria
    categories = {}
    for task in all_tasks:
        cat = task['category']
        if cat not in categories:
            categories[cat] = {'pending': 0, 'completed': 0}
        categories[cat][task['status']] += 1
    
    # Estatísticas por prioridade
    priorities = {'low': 0, 'medium': 0, 'high': 0}
    for task in all_tasks:
        if task['status'] == 'pending':
            priorities[task['priority']] += 1
    
    click.echo("\\n📊 Estatísticas das Tarefas:")
    click.echo("=" * 40)
    click.echo(f"📋 Total: {len(all_tasks)}")
    click.echo(f"⏳ Pendentes: " + click.style(str(pending), fg='yellow'))
    click.echo(f"✅ Completas: " + click.style(str(completed), fg='green'))
    
    if len(all_tasks) > 0:
        completion_rate = (completed / len(all_tasks)) * 100
        click.echo(f"📈 Taxa de conclusão: {completion_rate:.1f}%")
    
    click.echo("\\n📁 Por categoria:")
    for cat, stats in categories.items():
        click.echo(f"   {cat}: {stats['pending']} pendentes, {stats['completed']} completas")
    
    click.echo("\\n🎯 Prioridades pendentes:")
    for prio, count in priorities.items():
        if count > 0:
            color = {'low': 'green', 'medium': 'yellow', 'high': 'red'}[prio]
            click.echo(f"   {prio}: " + click.style(str(count), fg=color))

@cli.command()
def clean():
    """Remove todas as tarefas completas."""
    
    original_count = len(task_manager.tasks)
    task_manager.tasks = [t for t in task_manager.tasks if t['status'] != 'completed']
    removed = original_count - len(task_manager.tasks)
    
    if removed > 0:
        task_manager.save_tasks()
        click.echo(f"🧹 {removed} tarefas completas removidas!", fg='green')
    else:
        click.echo("📭 Nenhuma tarefa completa para remover")

if __name__ == '__main__':
    cli()'''
        
        if self.ui:
            self.ui.code_block(codigo_projeto, "TaskCLI - Gerenciador completo")
        else:
            print("\n" + "="*50)
            print("PROJETO COMPLETO - TASKCLI:")
            print("="*50)
            print(codigo_projeto)
        
        print("\n🎯 Como usar o TaskCLI:")
        
        exemplos_uso = '''# Adicionar tarefas
python taskcli.py add "Estudar Python" --priority high --category study
python taskcli.py add "Fazer compras" --priority low --category personal

# Listar tarefas
python taskcli.py list                    # Todas as tarefas
python taskcli.py list --status pending  # Apenas pendentes
python taskcli.py list --category study  # Por categoria
python taskcli.py list --format json     # Formato JSON

# Completar tarefa
python taskcli.py complete 1

# Ver estatísticas
python taskcli.py stats

# Remover tarefa
python taskcli.py delete 2

# Limpar completas
python taskcli.py clean

# Ajuda
python taskcli.py --help
python taskcli.py add --help'''
        
        print(exemplos_uso)
        
        print("\n🎉 Funcionalidades implementadas:")
        print("• ✅ CRUD completo de tarefas")
        print("• 🎨 Interface colorida e amigável") 
        print("• 💾 Persistência em JSON")
        print("• 🔍 Filtros por status e categoria")
        print("• 📊 Estatísticas detalhadas")
        print("• 🧹 Limpeza de tarefas completas")
        print("• 📋 Múltiplos formatos de saída")
        print("• ⚡ Validação e tratamento de erros")
        
        print("\n💡 Próximas funcionalidades:")
        print("• 📅 Datas de vencimento")
        print("• 🔔 Notificações")
        print("• 📊 Gráficos de produtividade")
        print("• 🔄 Sincronização com APIs")
        print("• 📱 Interface web opcional")
        
        # Pontos do mini projeto
        if self.progress:
            self.progress.add_points(self.mini_project_points)
            print(f"\n🎁 +{self.mini_project_points} pontos pelo projeto CLI!")
        
        input("\n🔸 Pressione ENTER para finalizar o módulo...")