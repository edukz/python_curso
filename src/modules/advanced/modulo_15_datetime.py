#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 15: Manipulação de Arquivos
Aprenda a trabalhar com arquivos, persistência de dados e backup
"""

from ..shared.base_module import BaseModule


class Modulo15Datetime(BaseModule):
    """Módulo 15: Manipulação de Arquivos - Persistência de Dados"""
    
    def __init__(self):
        super().__init__("modulo_15", "Manipulação de Arquivos")
        self.has_mini_project = True
        self.mini_project_points = 75
    
    def execute(self) -> None:
        """Executa o módulo sobre manipulação de arquivos"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._arquivos()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _arquivos(self) -> None:
        """Conteúdo principal sobre manipulação de arquivos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📁 MÓDULO 15: MANIPULAÇÃO DE ARQUIVOS")
        else:
            print("\n" + "="*50)
            print("📁 MÓDULO 15: MANIPULAÇÃO DE ARQUIVOS")
            print("="*50)
        
        print("📁 Agora vamos aprender a SALVAR e CARREGAR dados!")
        print("💾 Arquivos são fundamentais para guardar informações!")
        
        print("\n═══════════════════════════════════════════════")
        print("        LENDO E ESCREVENDO ARQUIVOS")
        print("═══════════════════════════════════════════════")
        
        print("\n📝 Modos de abertura:")
        print("• 'r' - Leitura (read)")
        print("• 'w' - Escrita (write) - APAGA o arquivo!")
        print("• 'a' - Anexar (append) - adiciona no final")
        print("• 'r+' - Leitura e escrita")
        
        self.pausar()
        
        # Escrevendo arquivos
        codigo1 = '''# Escrevendo arquivos
# Método básico
arquivo = open("teste.txt", "w", encoding="utf-8")
arquivo.write("Olá, mundo!\\n")
arquivo.write("Este é meu primeiro arquivo em Python.\\n")
arquivo.close()

print("✅ Arquivo 'teste.txt' criado!")

# Método recomendado - with statement
with open("lista_compras.txt", "w", encoding="utf-8") as arquivo:
    compras = ["Arroz", "Feijão", "Açúcar", "Café", "Leite"]
    for item in compras:
        arquivo.write(f"- {item}\\n")

print("✅ Lista de compras salva!")

# Múltiplas linhas de uma vez
conteudo = """Este é um arquivo de múltiplas linhas.
Linha 2 do arquivo.
Linha 3 com alguns dados.
Final do arquivo."""

with open("multiplas_linhas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)

print("✅ Arquivo com múltiplas linhas criado!")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n📖 Lendo arquivos:")
        
        codigo2 = '''# Lendo arquivos
print("=== LENDO ARQUIVO COMPLETO ===")
try:
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("❌ Arquivo não encontrado! Vamos criar um.")
    with open("teste.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Arquivo de exemplo\\nSegunda linha\\n")
    print("✅ Arquivo criado. Lendo agora...")
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

print("\\n=== LENDO LINHA POR LINHA ===")
with open("teste.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas, 1):
        print(f"Linha {i}: {linha.strip()}")

print("\\n=== LENDO COM LOOP ===")
with open("teste.txt", "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, 1):
        print(f"{numero:02d}: {linha.rstrip()}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n💼 Exemplo Prático - Sistema de Cadastro:")
        
        codigo3 = '''# Sistema de cadastro em arquivo
import json
from datetime import datetime

def salvar_pessoa(nome, idade, email):
    """Salva dados de uma pessoa no arquivo"""
    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cadastrado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Lê pessoas existentes
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
    except FileNotFoundError:
        pessoas = []
    
    # Adiciona nova pessoa
    pessoas.append(pessoa)
    
    # Salva tudo de volta
    with open("pessoas.json", "w", encoding="utf-8") as arquivo:
        json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
    
    print(f"✅ {nome} cadastrado com sucesso!")

def listar_pessoas():
    """Lista todas as pessoas cadastradas"""
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
        
        print("\\n=== PESSOAS CADASTRADAS ===")
        for i, pessoa in enumerate(pessoas, 1):
            print(f"{i}. {pessoa['nome']} ({pessoa['idade']} anos)")
            print(f"   Email: {pessoa['email']}")
            print(f"   Cadastrado em: {pessoa['cadastrado_em']}")
            print()
    except FileNotFoundError:
        print("❌ Nenhuma pessoa cadastrada ainda.")

# Testando o sistema
salvar_pessoa("João Silva", 30, "joao@email.com")
salvar_pessoa("Maria Santos", 25, "maria@email.com")
salvar_pessoa("Pedro Costa", 35, "pedro@email.com")

listar_pessoas()'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.pausar()
        
        print("\n🛡️ Tratamento de Erros com Arquivos:")
        
        codigo4 = '''# Tratamento robusto de erros
def ler_arquivo_seguro(nome_arquivo):
    """Lê arquivo com tratamento completo de erros"""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado!")
        return None
    except PermissionError:
        print(f"❌ Sem permissão para ler '{nome_arquivo}'!")
        return None
    except UnicodeDecodeError:
        print(f"❌ Erro de codificação no arquivo '{nome_arquivo}'!")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

def escrever_log(mensagem):
    """Escreve no arquivo de log com timestamp"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha_log = f"[{timestamp}] {mensagem}\\n"
    
    try:
        with open("sistema.log", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha_log)
        print(f"📝 Log registrado: {mensagem}")
    except Exception as e:
        print(f"❌ Erro ao escrever log: {e}")

# Testando
conteudo = ler_arquivo_seguro("teste.txt")
if conteudo:
    print("Arquivo lido com sucesso!")

escrever_log("Sistema iniciado")
escrever_log("Usuário fez login")
escrever_log("Arquivo processado")

# Lendo o log
print("\\n=== CONTEÚDO DO LOG ===")
log_content = ler_arquivo_seguro("sistema.log")
if log_content:
    print(log_content)'''
        
        self.exemplo(codigo4)
        self.executar_codigo(codigo4)
        
        # Exercícios
        self.exercicio(
            "Qual é a forma mais segura de abrir arquivos em Python?",
            ["with open", "with statement", "context manager"],
            "Use 'with' para fechar automaticamente"
        )
        
        self.exercicio(
            "Que modo usar para adicionar texto no final de um arquivo?",
            ["'a'", "append", "modo append"],
            "Modo 'a' adiciona no final sem apagar"
        )
        
        # Mini Projeto do Módulo 15
        self._mini_projeto_backup_inteligente()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_backup_inteligente(self) -> None:
        """Mini Projeto - Módulo 15: Sistema de Backup Inteligente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE BACKUP INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE BACKUP INTELIGENTE")
            print("="*50)
        
        print("💾 Sistema completo de backup com compressão e versionamento!")
        print("🛠️ Usando: Manipulação de Arquivos, JSON, CSV, ZIP, Diretórios")
        
        self.pausar()
        
        codigo_projeto = '''# 💾 SISTEMA DE BACKUP INTELIGENTE
# Projeto completo de backup com versionamento e compressão

import os
import json
import csv
import zipfile
import shutil
from datetime import datetime, timedelta
import hashlib
from pathlib import Path

class SistemaBackupInteligente:
    def __init__(self, diretorio_backup="backups"):
        self.diretorio_backup = Path(diretorio_backup)
        self.config_file = self.diretorio_backup / "backup_config.json"
        self.log_file = self.diretorio_backup / "backup_log.csv"
        self.metadata_file = self.diretorio_backup / "metadata.json"
        
        # Criar diretório se não existir
        self.diretorio_backup.mkdir(exist_ok=True)
        
        # Configurações padrão
        self.config = {
            "max_versoes": 5,
            "compressao_ativa": True,
            "backup_automatico": False,
            "tipos_arquivo_incluir": [".py", ".txt", ".json", ".csv", ".md"],
            "pastas_ignorar": ["__pycache__", ".git", "node_modules", ".vscode"],
            "tamanho_max_arquivo_mb": 10
        }
        
        self.carregar_configuracao()
        self.inicializar_log()
    
    def carregar_configuracao(self):
        """Carrega configuração do arquivo JSON"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config_carregada = json.load(f)
                    self.config.update(config_carregada)
                print("✅ Configuração carregada")
            except Exception as e:
                print(f"⚠️ Erro ao carregar config: {e}")
        else:
            self.salvar_configuracao()
    
    def salvar_configuracao(self):
        """Salva configuração atual em JSON"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            print("✅ Configuração salva")
        except Exception as e:
            print(f"❌ Erro ao salvar config: {e}")
    
    def inicializar_log(self):
        """Inicializa arquivo de log CSV"""
        if not self.log_file.exists():
            with open(self.log_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'timestamp', 'operacao', 'origem', 'destino', 
                    'arquivos_processados', 'tamanho_total', 'status', 'observacoes'
                ])
    
    def registrar_log(self, operacao, origem, destino, arquivos, tamanho, status, obs=""):
        """Registra operação no log CSV"""
        try:
            with open(self.log_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.now().isoformat(),
                    operacao,
                    str(origem),
                    str(destino),
                    arquivos,
                    tamanho,
                    status,
                    obs
                ])
        except Exception as e:
            print(f"⚠️ Erro ao registrar log: {e}")
    
    def calcular_hash_arquivo(self, caminho_arquivo):
        """Calcula hash MD5 de um arquivo"""
        hash_md5 = hashlib.md5()
        try:
            with open(caminho_arquivo, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception:
            return None
    
    def deve_incluir_arquivo(self, caminho_arquivo):
        """Verifica se arquivo deve ser incluído no backup"""
        arquivo_path = Path(caminho_arquivo)
        
        # Verifica extensão
        if self.config["tipos_arquivo_incluir"]:
            if arquivo_path.suffix not in self.config["tipos_arquivo_incluir"]:
                return False
        
        # Verifica tamanho
        try:
            tamanho_mb = arquivo_path.stat().st_size / (1024 * 1024)
            if tamanho_mb > self.config["tamanho_max_arquivo_mb"]:
                return False
        except:
            return False
        
        # Verifica se está em pasta ignorada
        for pasta_ignorar in self.config["pastas_ignorar"]:
            if pasta_ignorar in str(arquivo_path):
                return False
        
        return True
    
    def escanear_diretorio(self, caminho_origem):
        """Escaneia diretório e retorna lista de arquivos válidos"""
        origem_path = Path(caminho_origem)
        
        if not origem_path.exists():
            print(f"❌ Diretório não existe: {caminho_origem}")
            return []
        
        arquivos_validos = []
        total_arquivos = 0
        
        print(f"🔍 Escaneando: {caminho_origem}")
        
        for arquivo in origem_path.rglob("*"):
            if arquivo.is_file():
                total_arquivos += 1
                
                if self.deve_incluir_arquivo(arquivo):
                    arquivos_validos.append(arquivo)
        
        print(f"📊 Encontrados: {len(arquivos_validos)}/{total_arquivos} arquivos válidos")
        return arquivos_validos
    
    def criar_backup(self, caminho_origem, nome_backup=None):
        """Cria backup de um diretório"""
        if nome_backup is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_backup = f"backup_{timestamp}"
        
        print(f"\\n🚀 Iniciando backup: {nome_backup}")
        
        # Escanear arquivos
        arquivos = self.escanear_diretorio(caminho_origem)
        if not arquivos:
            print("❌ Nenhum arquivo para backup")
            return False
        
        # Criar diretório de versão
        versao_dir = self.diretorio_backup / nome_backup
        versao_dir.mkdir(exist_ok=True)
        
        arquivos_copiados = 0
        tamanho_total = 0
        arquivos_com_erro = []
        
        # Copiar arquivos
        print("📁 Copiando arquivos...")
        for arquivo_origem in arquivos:
            try:
                # Manter estrutura de diretórios
                rel_path = arquivo_origem.relative_to(Path(caminho_origem))
                arquivo_destino = versao_dir / rel_path
                
                # Criar diretório pai se necessário
                arquivo_destino.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar arquivo
                shutil.copy2(arquivo_origem, arquivo_destino)
                
                arquivos_copiados += 1
                tamanho_total += arquivo_origem.stat().st_size
                
                if arquivos_copiados % 10 == 0:
                    print(f"  📁 Copiados: {arquivos_copiados}/{len(arquivos)}")
                
            except Exception as e:
                arquivos_com_erro.append(f"{arquivo_origem}: {e}")
        
        # Criar metadata
        metadata = {
            "nome_backup": nome_backup,
            "timestamp": datetime.now().isoformat(),
            "origem": str(caminho_origem),
            "arquivos_total": len(arquivos),
            "arquivos_copiados": arquivos_copiados,
            "tamanho_bytes": tamanho_total,
            "arquivos_com_erro": arquivos_com_erro,
            "hash_backup": self.calcular_hash_diretorio(versao_dir)
        }
        
        # Salvar metadata
        metadata_path = versao_dir / "backup_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        # Compressão se ativada
        if self.config["compressao_ativa"]:
            print("🗜️ Comprimindo backup...")
            zip_path = versao_dir.with_suffix('.zip')
            self.comprimir_diretorio(versao_dir, zip_path)
            
            # Remove diretório original após compressão
            shutil.rmtree(versao_dir)
            
            # Atualiza tamanho comprimido
            metadata["tamanho_comprimido"] = zip_path.stat().st_size
            metadata["comprimido"] = True
        
        # Registrar no log
        status = "SUCESSO" if not arquivos_com_erro else "SUCESSO_COM_ERROS"
        obs = f"{len(arquivos_com_erro)} erros" if arquivos_com_erro else ""
        
        self.registrar_log(
            "BACKUP",
            caminho_origem,
            nome_backup,
            arquivos_copiados,
            tamanho_total,
            status,
            obs
        )
        
        print(f"\\n✅ Backup concluído!")
        print(f"📊 Arquivos: {arquivos_copiados}/{len(arquivos)}")
        print(f"💾 Tamanho: {tamanho_total / 1024:.1f} KB")
        if arquivos_com_erro:
            print(f"⚠️ Erros: {len(arquivos_com_erro)}")
        
        # Limpeza de versões antigas
        self.limpar_versoes_antigas()
        
        return True
    
    def calcular_hash_diretorio(self, diretorio):
        """Calcula hash MD5 combinado de todos os arquivos"""
        hash_combinado = hashlib.md5()
        
        for arquivo in sorted(Path(diretorio).rglob("*")):
            if arquivo.is_file() and arquivo.name != "backup_metadata.json":
                hash_arquivo = self.calcular_hash_arquivo(arquivo)
                if hash_arquivo:
                    hash_combinado.update(hash_arquivo.encode())
        
        return hash_combinado.hexdigest()
    
    def comprimir_diretorio(self, diretorio, arquivo_zip):
        """Comprime diretório em arquivo ZIP"""
        with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for arquivo in Path(diretorio).rglob("*"):
                if arquivo.is_file():
                    arcname = arquivo.relative_to(diretorio)
                    zip_file.write(arquivo, arcname)
    
    def relatorio_backups(self):
        """Gera relatório completo dos backups"""
        print(f"\\n{'='*60}")
        print("📊 RELATÓRIO DE BACKUPS")
        print(f"{'='*60}")
        
        # Simular alguns backups para demonstração
        print(f"\\n📈 RESUMO:")
        print(f"  💾 Total de backups: 3")
        print(f"  📊 Espaço usado: 2.5 MB")
        
        print(f"\\n📋 LISTA DE BACKUPS:")
        backups_demo = [
            {"nome": "backup_demo_v2", "timestamp": "2024-01-15 14:30", "arquivos": 7, "tamanho": 1.2},
            {"nome": "backup_demo_v1", "timestamp": "2024-01-15 14:25", "arquivos": 7, "tamanho": 1.1},
            {"nome": "backup_inicial", "timestamp": "2024-01-15 14:20", "arquivos": 5, "tamanho": 0.8}
        ]
        
        for i, backup in enumerate(backups_demo, 1):
            print(f"  {i}. {backup['nome']}")
            print(f"     📅 {backup['timestamp']} | 📁 {backup['arquivos']} arquivos | 💾 {backup['tamanho']} MB")

# DEMONSTRAÇÃO DO SISTEMA
print("=== SISTEMA DE BACKUP INTELIGENTE ===\\n")

# Criar instância
backup_system = SistemaBackupInteligente("demo_backups")

# Simular criação de estrutura de exemplo
print("📁 Simulando estrutura de projeto...")
exemplo_dir = Path("exemplo_projeto")
print(f"✅ Estrutura criada: {exemplo_dir}")

# Simular arquivos de exemplo
arquivos_exemplo = [
    "main.py", "config.json", "dados.csv", 
    "README.md", "src/utils.py", "src/models.py", "docs/manual.txt"
]

print(f"✅ Simulados {len(arquivos_exemplo)} arquivos de exemplo:")
for arquivo in arquivos_exemplo:
    print(f"  📄 {arquivo}")

# Configurar sistema
print("\\n⚙️ Configurando sistema...")
backup_system.config["max_versoes"] = 3
backup_system.config["compressao_ativa"] = True
backup_system.salvar_configuracao()

# Simular criação de backup
print("\\n💾 Simulando criação de backup...")
print("🔍 Escaneando: exemplo_projeto")
print("📊 Encontrados: 7/7 arquivos válidos")
print("\\n🚀 Iniciando backup: backup_demo_v1")
print("📁 Copiando arquivos...")
print("  📁 Copiados: 7/7")
print("🗜️ Comprimindo backup...")
print("\\n✅ Backup concluído!")
print("📊 Arquivos: 7/7")
print("💾 Tamanho: 15.2 KB")

# Simular modificações e segundo backup
print("\\n📝 Simulando modificações...")
print("\\n💾 Simulando segundo backup...")
print("🔍 Escaneando: exemplo_projeto") 
print("📊 Encontrados: 7/7 arquivos válidos")
print("\\n🚀 Iniciando backup: backup_demo_v2")
print("📁 Copiando arquivos...")
print("  📁 Copiados: 7/7")
print("🗜️ Comprimindo backup...")
print("\\n✅ Backup concluído!")
print("📊 Arquivos: 7/7")
print("💾 Tamanho: 16.1 KB")

# Gerar relatório
backup_system.relatorio_backups()

print("\\n🎉 Sistema de Backup funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Manipulação avançada de arquivos e diretórios")
print("  • Serialização JSON para configuração e metadata")
print("  • Logs estruturados em CSV")
print("  • Compressão ZIP")
print("  • Hashing para integridade")
print("  • Versionamento inteligente")
print("  • Configuração flexível")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de backup inteligente criado!")
        print("🎯 Aplicação real: backup de projetos, versionamento, arquivamento")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Backup Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo15Datetime()
    print("Teste do módulo 15 - versão standalone")
    module._arquivos()