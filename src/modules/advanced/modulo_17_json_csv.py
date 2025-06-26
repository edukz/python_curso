#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 17: JSON e CSV
Aprenda a trabalhar com dados estruturados em JSON e CSV
"""

from ..shared.base_module import BaseModule


class Modulo17JsonCsv(BaseModule):
    """Módulo 17: JSON e CSV - Processamento de Dados Estruturados"""
    
    def __init__(self):
        super().__init__("modulo_17", "JSON e CSV")
        self.has_mini_project = True
        self.mini_project_points = 85
    
    def execute(self) -> None:
        """Executa o módulo sobre JSON e CSV"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._json_csv()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _json_csv(self) -> None:
        """Conteúdo principal sobre JSON e CSV"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📋 MÓDULO 17: JSON E CSV")
        else:
            print("\n" + "="*50)
            print("📋 MÓDULO 17: JSON E CSV")
            print("="*50)
        
        print("📊 Vamos aprender a trabalhar com dados estruturados!")
        print("🔄 JSON e CSV são formatos essenciais para troca de dados!")
        
        print("\n═══════════════════════════════════════════════")
        print("        TRABALHANDO COM JSON")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 JSON = JavaScript Object Notation")
        print("✅ Vantagens:")
        print("• 📱 Usado em APIs e web")
        print("• 🔤 Fácil de ler e escrever")
        print("• 🐍 Nativo no Python")
        print("• 🏗️ Suporta estruturas complexas")
        
        self.pausar()
        
        codigo1 = '''# Trabalhando com JSON
import json
from datetime import datetime

# Criando dados para demonstração
dados_pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "email": "joao@email.com",
    "enderecos": [
        {
            "tipo": "residencial",
            "rua": "Rua das Flores, 123",
            "cidade": "São Paulo",
            "cep": "01234-567"
        },
        {
            "tipo": "comercial", 
            "rua": "Av. Paulista, 1000",
            "cidade": "São Paulo",
            "cep": "01310-100"
        }
    ],
    "ativo": True,
    "salario": 5000.50,
    "cadastrado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print("=== CONVERTENDO PARA JSON ===")
# Python dict -> JSON string
json_string = json.dumps(dados_pessoa, indent=2, ensure_ascii=False)
print("JSON String:")
print(json_string)

print("\\n=== SALVANDO EM ARQUIVO ===")
# Salvando em arquivo
with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_pessoa, arquivo, indent=2, ensure_ascii=False)
print("✅ Dados salvos em pessoa.json")

print("\\n=== CARREGANDO DE ARQUIVO ===")
# Carregando de arquivo
try:
    with open("pessoa.json", "r", encoding="utf-8") as arquivo:
        pessoa_carregada = json.load(arquivo)
    
    print("Dados carregados:")
    print(f"Nome: {pessoa_carregada['nome']}")
    print(f"Email: {pessoa_carregada['email']}")
    print(f"Quantidade de endereços: {len(pessoa_carregada['enderecos'])}")
    
    for i, endereco in enumerate(pessoa_carregada['enderecos'], 1):
        print(f"  Endereço {i}: {endereco['tipo']} - {endereco['cidade']}")

except FileNotFoundError:
    print("❌ Arquivo não encontrado")

print("\\n=== CONVERTENDO DE JSON STRING ===")
# JSON string -> Python dict
json_exemplo = '{"produto": "Notebook", "preco": 2500.99, "disponivel": true}'
produto = json.loads(json_exemplo)
print(f"Produto: {produto['produto']}")
print(f"Preço: R$ {produto['preco']}")
print(f"Disponível: {'Sim' if produto['disponivel'] else 'Não'}")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n📊 TRABALHANDO COM CSV:")
        
        codigo2 = '''# Trabalhando com CSV
import csv
from datetime import datetime
import json

print("=== CRIANDO DADOS CSV ===")
# Dados de exemplo - vendas
vendas = [
    {"data": "2024-01-15", "produto": "Notebook", "quantidade": 2, "preco": 2500.00, "vendedor": "João"},
    {"data": "2024-01-15", "produto": "Mouse", "quantidade": 5, "preco": 50.00, "vendedor": "Maria"},
    {"data": "2024-01-16", "produto": "Teclado", "quantidade": 3, "preco": 150.00, "vendedor": "João"},
    {"data": "2024-01-16", "produto": "Monitor", "quantidade": 1, "preco": 800.00, "vendedor": "Pedro"},
    {"data": "2024-01-17", "produto": "Notebook", "quantidade": 1, "preco": 2500.00, "vendedor": "Maria"}
]

# Escrevendo CSV
print("📝 Escrevendo arquivo CSV...")
with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    # Usando DictWriter para escrever dicionários
    colunas = ["data", "produto", "quantidade", "preco", "vendedor", "total"]
    writer = csv.DictWriter(arquivo, fieldnames=colunas)
    
    # Escreve cabeçalho
    writer.writeheader()
    
    # Escreve dados
    for venda in vendas:
        venda["total"] = venda["quantidade"] * venda["preco"]
        writer.writerow(venda)

print("✅ Arquivo vendas.csv criado")

print("\\n=== LENDO ARQUIVO CSV ===")
# Lendo CSV
vendas_lidas = []
try:
    with open("vendas.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        
        print("Dados do CSV:")
        print("-" * 80)
        print(f"{'Data':<12} {'Produto':<12} {'Qtd':<5} {'Preço':<10} {'Vendedor':<10} {'Total':<10}")
        print("-" * 80)
        
        for linha in reader:
            vendas_lidas.append(linha)
            data = linha["data"]
            produto = linha["produto"]
            qtd = linha["quantidade"]
            preco = float(linha["preco"])
            vendedor = linha["vendedor"]
            total = float(linha["total"])
            
            print(f"{data:<12} {produto:<12} {qtd:<5} R${preco:<9.2f} {vendedor:<10} R${total:<9.2f}")

except FileNotFoundError:
    print("❌ Arquivo CSV não encontrado")

print(f"\\n📊 Total de vendas carregadas: {len(vendas_lidas)}")

print("\\n=== ESTATÍSTICAS DO CSV ===")
if vendas_lidas:
    # Calculando estatísticas
    total_geral = sum(float(venda["total"]) for venda in vendas_lidas)
    qtd_total = sum(int(venda["quantidade"]) for venda in vendas_lidas)
    
    # Vendas por vendedor
    vendas_por_vendedor = {}
    for venda in vendas_lidas:
        vendedor = venda["vendedor"]
        total = float(venda["total"])
        vendas_por_vendedor[vendedor] = vendas_por_vendedor.get(vendedor, 0) + total
    
    print(f"💰 Faturamento total: R$ {total_geral:.2f}")
    print(f"📦 Quantidade total vendida: {qtd_total}")
    print(f"💵 Ticket médio: R$ {total_geral/len(vendas_lidas):.2f}")
    
    print("\\n👥 Vendas por vendedor:")
    for vendedor, total in sorted(vendas_por_vendedor.items(), key=lambda x: x[1], reverse=True):
        print(f"  {vendedor}: R$ {total:.2f}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🔄 CONVERSÃO ENTRE FORMATOS:")
        
        codigo3 = '''# Convertendo entre JSON e CSV
import json
import csv
from collections import defaultdict

def csv_para_json(arquivo_csv, arquivo_json):
    """Converte arquivo CSV para JSON"""
    dados = []
    
    try:
        with open(arquivo_csv, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for linha in reader:
                # Converte tipos de dados
                linha_processada = {}
                for chave, valor in linha.items():
                    # Tenta converter números
                    try:
                        if '.' in valor:
                            linha_processada[chave] = float(valor)
                        else:
                            linha_processada[chave] = int(valor)
                    except ValueError:
                        # Mantém como string se não for número
                        linha_processada[chave] = valor
                
                dados.append(linha_processada)
        
        # Salva como JSON
        with open(arquivo_json, 'w', encoding='utf-8') as json_file:
            json.dump(dados, json_file, indent=2, ensure_ascii=False)
        
        print(f"✅ Convertido {arquivo_csv} -> {arquivo_json}")
        return len(dados)
    
    except FileNotFoundError:
        print(f"❌ Arquivo {arquivo_csv} não encontrado")
        return 0

def json_para_csv(arquivo_json, arquivo_csv):
    """Converte arquivo JSON para CSV"""
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as json_file:
            dados = json.load(json_file)
        
        if not dados:
            print("❌ Arquivo JSON vazio")
            return 0
        
        # Obtém todas as chaves possíveis
        chaves = set()
        for item in dados:
            if isinstance(item, dict):
                chaves.update(item.keys())
        
        chaves = sorted(list(chaves))
        
        # Escreve CSV
        with open(arquivo_csv, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=chaves)
            writer.writeheader()
            
            for item in dados:
                if isinstance(item, dict):
                    # Preenche valores faltantes com string vazia
                    linha = {chave: item.get(chave, '') for chave in chaves}
                    writer.writerow(linha)
        
        print(f"✅ Convertido {arquivo_json} -> {arquivo_csv}")
        return len(dados)
    
    except FileNotFoundError:
        print(f"❌ Arquivo {arquivo_json} não encontrado")
        return 0
    except json.JSONDecodeError:
        print(f"❌ Erro ao decodificar JSON em {arquivo_json}")
        return 0

print("=== CONVERTENDO CSV -> JSON ===")
# Converte vendas.csv para vendas.json
registros = csv_para_json("vendas.csv", "vendas.json")
print(f"📊 {registros} registros convertidos")

print("\\n=== CONVERTENDO JSON -> CSV ===")
# Converte pessoa.json para pessoa.csv
registros = json_para_csv("pessoa.json", "pessoa.csv")
print(f"📊 {registros} registros convertidos")

print("\\n=== VERIFICANDO ARQUIVOS CRIADOS ===")
import os
arquivos = ["vendas.csv", "vendas.json", "pessoa.json", "pessoa.csv"]
for arquivo in arquivos:
    if os.path.exists(arquivo):
        tamanho = os.path.getsize(arquivo)
        print(f"✅ {arquivo} - {tamanho} bytes")
    else:
        print(f"❌ {arquivo} não encontrado")

print("\\n=== ANÁLISE COMBINADA ===")
# Exemplo: carrega JSON, processa e salva estatísticas em CSV
try:
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        vendas_json = json.load(arquivo)
    
    # Agrupa vendas por produto
    vendas_por_produto = defaultdict(lambda: {"quantidade": 0, "faturamento": 0})
    
    for venda in vendas_json:
        produto = venda["produto"]
        qtd = int(venda["quantidade"])
        total = float(venda["total"])
        
        vendas_por_produto[produto]["quantidade"] += qtd
        vendas_por_produto[produto]["faturamento"] += total
    
    # Salva relatório em CSV
    with open("relatorio_produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        colunas = ["produto", "quantidade_total", "faturamento_total", "ticket_medio"]
        writer = csv.DictWriter(arquivo, fieldnames=colunas)
        writer.writeheader()
        
        for produto, dados in vendas_por_produto.items():
            ticket_medio = dados["faturamento"] / dados["quantidade"]
            writer.writerow({
                "produto": produto,
                "quantidade_total": dados["quantidade"],
                "faturamento_total": dados["faturamento"],
                "ticket_medio": round(ticket_medio, 2)
            })
    
    print("✅ Relatório de produtos salvo em relatorio_produtos.csv")

except Exception as e:
    print(f"❌ Erro na análise: {e}")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Qual função usa para converter Python dict para JSON string?",
            ["json.dumps", "json.dumps()"],
            "json.dumps() converte dict para string JSON"
        )
        
        self.exercicio(
            "Como ler um CSV como dicionários em Python?",
            ["csv.DictReader", "DictReader"],
            "csv.DictReader lê CSV como dicionários"
        )
        
        # Mini Projeto do Módulo 17
        self._mini_projeto_sistema_dados()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_dados(self) -> None:
        """Mini Projeto - Módulo 17: Sistema de Análise de Dados Integrado"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE ANÁLISE DE DADOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE ANÁLISE DE DADOS")
            print("="*50)
        
        print("📊 Sistema completo de processamento de dados JSON e CSV!")
        print("🛠️ Usando: JSON, CSV, Análises Estatísticas, Relatórios")
        
        self.pausar()
        
        codigo_projeto = '''# 📊 SISTEMA DE ANÁLISE DE DADOS INTEGRADO
# Projeto completo de processamento JSON/CSV com análises

import json
import csv
import os
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Any, Optional
import statistics

class DataProcessor:
    """Processador principal de dados JSON/CSV"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.datasets = {}
        self.reports = {}
        
        # Criar diretório se não existir
        os.makedirs(data_dir, exist_ok=True)
        
        print(f"✅ DataProcessor inicializado - Diretório: {data_dir}")
    
    def load_json(self, filename: str, dataset_name: str = None) -> bool:
        """Carrega dados de arquivo JSON"""
        if dataset_name is None:
            dataset_name = os.path.splitext(filename)[0]
        
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            self.datasets[dataset_name] = {
                'data': data,
                'type': 'json',
                'filename': filename,
                'loaded_at': datetime.now().isoformat(),
                'records_count': len(data) if isinstance(data, list) else 1
            }
            
            print(f"✅ JSON carregado: {dataset_name} ({self.datasets[dataset_name]['records_count']} registros)")
            return True
        
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {filepath}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ Erro ao decodificar JSON: {e}")
            return False
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return False
    
    def load_csv(self, filename: str, dataset_name: str = None) -> bool:
        """Carrega dados de arquivo CSV"""
        if dataset_name is None:
            dataset_name = os.path.splitext(filename)[0]
        
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            data = []
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Converte números automaticamente
                    converted_row = {}
                    for key, value in row.items():
                        converted_row[key] = self._convert_value(value)
                    data.append(converted_row)
            
            self.datasets[dataset_name] = {
                'data': data,
                'type': 'csv',
                'filename': filename,
                'loaded_at': datetime.now().isoformat(),
                'records_count': len(data)
            }
            
            print(f"✅ CSV carregado: {dataset_name} ({len(data)} registros)")
            return True
        
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {filepath}")
            return False
        except Exception as e:
            print(f"❌ Erro ao carregar CSV: {e}")
            return False
    
    def _convert_value(self, value: str) -> Any:
        """Converte string para tipo apropriado"""
        if not value or value.lower() in ['', 'null', 'none']:
            return None
        
        # Tenta converter para número
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            pass
        
        # Tenta converter para booleano
        if value.lower() in ['true', 'yes', 'sim']:
            return True
        elif value.lower() in ['false', 'no', 'não']:
            return False
        
        # Mantém como string
        return value
    
    def save_json(self, dataset_name: str, filename: str = None) -> bool:
        """Salva dataset como JSON"""
        if dataset_name not in self.datasets:
            print(f"❌ Dataset '{dataset_name}' não encontrado")
            return False
        
        if filename is None:
            filename = f"{dataset_name}.json"
        
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(
                    self.datasets[dataset_name]['data'], 
                    file, 
                    indent=2, 
                    ensure_ascii=False,
                    default=str  # Para converter datetime, etc.
                )
            
            print(f"✅ Dataset salvo como JSON: {filepath}")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao salvar JSON: {e}")
            return False
    
    def save_csv(self, dataset_name: str, filename: str = None) -> bool:
        """Salva dataset como CSV"""
        if dataset_name not in self.datasets:
            print(f"❌ Dataset '{dataset_name}' não encontrado")
            return False
        
        data = self.datasets[dataset_name]['data']
        if not isinstance(data, list) or not data:
            print(f"❌ Dataset vazio ou não é uma lista")
            return False
        
        if filename is None:
            filename = f"{dataset_name}.csv"
        
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            # Obtém todas as chaves possíveis
            all_keys = set()
            for record in data:
                if isinstance(record, dict):
                    all_keys.update(record.keys())
            
            fieldnames = sorted(list(all_keys))
            
            with open(filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for record in data:
                    if isinstance(record, dict):
                        # Preenche valores faltantes
                        row = {key: record.get(key, '') for key in fieldnames}
                        writer.writerow(row)
            
            print(f"✅ Dataset salvo como CSV: {filepath}")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao salvar CSV: {e}")
            return False
    
    def analyze_dataset(self, dataset_name: str) -> Dict[str, Any]:
        """Analisa um dataset e gera estatísticas"""
        if dataset_name not in self.datasets:
            print(f"❌ Dataset '{dataset_name}' não encontrado")
            return {}
        
        data = self.datasets[dataset_name]['data']
        
        if not isinstance(data, list):
            print(f"⚠️ Análise limitada - dataset não é uma lista")
            return {'type': type(data).__name__, 'sample': str(data)[:100]}
        
        analysis = {
            'dataset_name': dataset_name,
            'total_records': len(data),
            'data_types': {},
            'numeric_stats': {},
            'categorical_stats': {},
            'missing_data': {},
            'sample_records': data[:3] if data else []
        }
        
        if not data:
            return analysis
        
        # Analisa campos
        all_keys = set()
        for record in data:
            if isinstance(record, dict):
                all_keys.update(record.keys())
        
        for key in sorted(all_keys):
            values = []
            missing_count = 0
            types_count = Counter()
            
            for record in data:
                if isinstance(record, dict):
                    value = record.get(key)
                    if value is None or value == '':
                        missing_count += 1
                    else:
                        values.append(value)
                        types_count[type(value).__name__] += 1
            
            analysis['missing_data'][key] = missing_count
            analysis['data_types'][key] = dict(types_count)
            
            # Análise numérica
            numeric_values = [v for v in values if isinstance(v, (int, float))]
            if numeric_values:
                analysis['numeric_stats'][key] = {
                    'count': len(numeric_values),
                    'mean': statistics.mean(numeric_values),
                    'median': statistics.median(numeric_values),
                    'min': min(numeric_values),
                    'max': max(numeric_values),
                    'std_dev': statistics.stdev(numeric_values) if len(numeric_values) > 1 else 0
                }
            
            # Análise categórica
            string_values = [str(v) for v in values if v is not None]
            if string_values:
                value_counts = Counter(string_values)
                analysis['categorical_stats'][key] = {
                    'unique_values': len(value_counts),
                    'top_values': dict(value_counts.most_common(5))
                }
        
        # Salva análise
        self.reports[f"{dataset_name}_analysis"] = analysis
        
        return analysis
    
    def cross_analysis(self, dataset1: str, dataset2: str, join_key: str) -> Dict[str, Any]:
        """Análise cruzada entre dois datasets"""
        if dataset1 not in self.datasets or dataset2 not in self.datasets:
            print(f"❌ Um ou ambos datasets não encontrados")
            return {}
        
        data1 = self.datasets[dataset1]['data']
        data2 = self.datasets[dataset2]['data']
        
        if not (isinstance(data1, list) and isinstance(data2, list)):
            print(f"❌ Ambos datasets devem ser listas")
            return {}
        
        # Cria índices para join
        index1 = {record.get(join_key): record for record in data1 if isinstance(record, dict)}
        index2 = {record.get(join_key): record for record in data2 if isinstance(record, dict)}
        
        # Análise de matching
        keys1 = set(index1.keys())
        keys2 = set(index2.keys())
        
        intersection = keys1 & keys2
        only_in_1 = keys1 - keys2
        only_in_2 = keys2 - keys1
        
        cross_analysis = {
            'dataset1': dataset1,
            'dataset2': dataset2,
            'join_key': join_key,
            'total_keys_dataset1': len(keys1),
            'total_keys_dataset2': len(keys2),
            'matching_keys': len(intersection),
            'only_in_dataset1': len(only_in_1),
            'only_in_dataset2': len(only_in_2),
            'match_percentage': (len(intersection) / max(len(keys1), len(keys2))) * 100,
            'sample_matches': list(intersection)[:5],
            'sample_only_1': list(only_in_1)[:5],
            'sample_only_2': list(only_in_2)[:5]
        }
        
        return cross_analysis
    
    def generate_report(self, report_name: str = None) -> str:
        """Gera relatório completo em texto"""
        if report_name is None:
            report_name = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        report_lines = [
            "📊 RELATÓRIO DE ANÁLISE DE DADOS",
            "=" * 50,
            f"🕐 Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            f"📁 Diretório: {self.data_dir}",
            "",
            "📋 DATASETS CARREGADOS:",
        ]
        
        for name, info in self.datasets.items():
            report_lines.extend([
                f"  • {name}:",
                f"    - Tipo: {info['type'].upper()}",
                f"    - Arquivo: {info['filename']}",
                f"    - Registros: {info['records_count']}",
                f"    - Carregado em: {info['loaded_at'][:19]}",
                ""
            ])
        
        # Adiciona análises se existirem
        for report_key, analysis in self.reports.items():
            if 'dataset_name' in analysis:
                report_lines.extend([
                    f"📊 ANÁLISE: {analysis['dataset_name'].upper()}",
                    "-" * 30,
                    f"Total de registros: {analysis['total_records']}",
                    ""
                ])
                
                if analysis['numeric_stats']:
                    report_lines.append("📈 ESTATÍSTICAS NUMÉRICAS:")
                    for field, stats in analysis['numeric_stats'].items():
                        report_lines.extend([
                            f"  {field}:",
                            f"    - Média: {stats['mean']:.2f}",
                            f"    - Mediana: {stats['median']:.2f}",
                            f"    - Min/Max: {stats['min']:.2f} / {stats['max']:.2f}",
                            ""
                        ])
                
                if analysis['categorical_stats']:
                    report_lines.append("📊 ESTATÍSTICAS CATEGÓRICAS:")
                    for field, stats in analysis['categorical_stats'].items():
                        report_lines.extend([
                            f"  {field}:",
                            f"    - Valores únicos: {stats['unique_values']}",
                            f"    - Top valores: {list(stats['top_values'].keys())[:3]}",
                            ""
                        ])
        
        report_content = "\\n".join(report_lines)
        
        # Salva relatório
        report_file = os.path.join(self.data_dir, f"{report_name}.txt")
        try:
            with open(report_file, 'w', encoding='utf-8') as file:
                file.write(report_content)
            print(f"✅ Relatório salvo: {report_file}")
        except Exception as e:
            print(f"❌ Erro ao salvar relatório: {e}")
        
        return report_content
    
    def list_datasets(self) -> None:
        """Lista todos os datasets carregados"""
        if not self.datasets:
            print("📭 Nenhum dataset carregado")
            return
        
        print("📋 DATASETS CARREGADOS:")
        for name, info in self.datasets.items():
            print(f"  • {name}: {info['records_count']} registros ({info['type'].upper()})")

# DEMONSTRAÇÃO DO SISTEMA

print("=== SISTEMA DE ANÁLISE DE DADOS INTEGRADO ===\\n")

# Criar instância do processador
processor = DataProcessor("demo_data")

# Criar dados de exemplo
print("📝 Criando dados de exemplo...")

# Dataset 1: Vendas
vendas_data = [
    {"id": 1, "data": "2024-01-15", "produto": "Notebook", "quantidade": 2, "preco": 2500.00, "vendedor_id": 101},
    {"id": 2, "data": "2024-01-15", "produto": "Mouse", "quantidade": 5, "preco": 50.00, "vendedor_id": 102},
    {"id": 3, "data": "2024-01-16", "produto": "Teclado", "quantidade": 3, "preco": 150.00, "vendedor_id": 101},
    {"id": 4, "data": "2024-01-16", "produto": "Monitor", "quantidade": 1, "preco": 800.00, "vendedor_id": 103},
    {"id": 5, "data": "2024-01-17", "produto": "Notebook", "quantidade": 1, "preco": 2500.00, "vendedor_id": 102}
]

# Dataset 2: Vendedores
vendedores_data = [
    {"id": 101, "nome": "João Silva", "departamento": "Eletrônicos", "comissao": 0.05},
    {"id": 102, "nome": "Maria Santos", "departamento": "Informática", "comissao": 0.08},
    {"id": 103, "nome": "Pedro Costa", "departamento": "Eletrônicos", "comissao": 0.06}
]

# Salvando dados de exemplo
with open("demo_data/vendas.json", "w", encoding="utf-8") as f:
    json.dump(vendas_data, f, indent=2)

with open("demo_data/vendedores.json", "w", encoding="utf-8") as f:
    json.dump(vendedores_data, f, indent=2)

print("✅ Dados de exemplo criados")

# Carregando datasets
print("\\n📥 CARREGANDO DATASETS:")
processor.load_json("vendas.json", "vendas")
processor.load_json("vendedores.json", "vendedores")

# Listando datasets
print("\\n📋 DATASETS DISPONÍVEIS:")
processor.list_datasets()

# Análise individual
print("\\n📊 ANÁLISE DE VENDAS:")
vendas_analysis = processor.analyze_dataset("vendas")
print(f"• Total de vendas: {vendas_analysis['total_records']}")
print(f"• Campos numéricos analisados: {len(vendas_analysis['numeric_stats'])}")

if 'preco' in vendas_analysis['numeric_stats']:
    preco_stats = vendas_analysis['numeric_stats']['preco']
    print(f"• Preço médio: R$ {preco_stats['mean']:.2f}")
    print(f"• Faixa de preços: R$ {preco_stats['min']:.2f} - R$ {preco_stats['max']:.2f}")

print("\\n📊 ANÁLISE DE VENDEDORES:")
vendedores_analysis = processor.analyze_dataset("vendedores")
print(f"• Total de vendedores: {vendedores_analysis['total_records']}")

# Análise cruzada
print("\\n🔄 ANÁLISE CRUZADA:")
cross_result = processor.cross_analysis("vendas", "vendedores", "vendedor_id")
if cross_result:
    print(f"• Vendas com vendedor correspondente: {cross_result['matching_keys']}")
    print(f"• Taxa de matching: {cross_result['match_percentage']:.1f}%")

# Conversão de formatos
print("\\n🔄 CONVERSÃO DE FORMATOS:")
processor.save_csv("vendas", "vendas_export.csv")
processor.save_csv("vendedores", "vendedores_export.csv")

# Gerando relatório final
print("\\n📋 GERANDO RELATÓRIO FINAL:")
relatorio = processor.generate_report("relatorio_completo")

print("\\n✅ Sistema de Análise de Dados funcionando perfeitamente!")
print("🎯 Funcionalidades implementadas:")
print("  • Carregamento automático JSON/CSV")
print("  • Conversão entre formatos")
print("  • Análise estatística automática")
print("  • Análise cruzada de datasets")
print("  • Geração de relatórios")
print("  • Detecção de tipos de dados")
print("  • Tratamento de dados faltantes")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de análise de dados criado!")
        print("🎯 Aplicação real: business intelligence, ETL, análise de dados")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Análise de Dados Integrado")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo17JsonCsv()
    print("Teste do módulo 17 - versão standalone")
    module._json_csv()