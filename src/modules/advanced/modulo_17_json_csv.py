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
        """Executa o módulo JSON e CSV"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return

        try:
            self._json_csv_moderno()
        except Exception as e:
            self.error_handler(lambda: None)

    def _json_csv_moderno(self) -> None:
        """Conteúdo principal do módulo JSON e CSV"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 MÓDULO 17: JSON E CSV - PROCESSAMENTO DE DADOS")
        else:
            print("\n" + "="*50)
            print("📊 MÓDULO 17: JSON E CSV - PROCESSAMENTO DE DADOS")
            print("="*50)

        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo do processamento de dados estruturados!")
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
            self._mini_projeto_dashboard_dados()
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
                'id': 'secao_conceito_principal',
                'titulo': '🎯 O que são JSON e CSV?',
                'descricao': 'Entenda os formatos de dados mais usados no mundo',
                'funcao': self._secao_conceito_principal
            },
            {
                'id': 'secao_como_funciona',
                'titulo': '⚙️ Como JSON e CSV funcionam?',
                'descricao': 'Veja a estrutura e sintaxe de cada formato',
                'funcao': self._secao_como_funciona
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Exemplos práticos',
                'descricao': 'Veja JSON e CSV em ação com código real',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_casos_uso',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'APIs, bancos de dados, análise de dados e mais',
                'funcao': self._secao_casos_uso
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_erros_comuns',
                'titulo': '⚠️ Erros comuns e como evitar',
                'descricao': 'Aprenda com os erros mais frequentes',
                'funcao': self._secao_erros_comuns
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre dados',
                'descricao': 'Fatos interessantes sobre JSON e CSV',
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

    def _secao_conceito_principal(self) -> None:
        """Seção: O que são JSON e CSV?"""
        if self.ui:
            self.ui.clear_screen()

        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO JSON E CSV?", "🎯")

        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "JSON (JavaScript Object Notation)",
            "Formato leve para troca de dados, fácil de ler e escrever"
        )

        self.print_concept(
            "CSV (Comma-Separated Values)",
            "Formato simples para dados tabulares, como planilhas"
        )

        # === DICA RELACIONADA ===
        self.print_tip("JSON é como um dicionário Python, CSV é como uma tabela Excel!")

        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("JSON é como uma agenda telefônica digital - cada pessoa tem seus dados organizados", "text")
        self.print_colored("CSV é como uma lista de compras - itens em linhas e colunas", "text")
        input("\n🔸 Pressione ENTER para continuar...")

        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. JSON organiza dados como dicionários e listas Python",
            "2. CSV organiza dados em linhas e colunas separadas por vírgulas",
            "3. Ambos são formatos de texto simples, legíveis por humanos"
        ]

        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")

        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Exemplo simples de JSON e CSV
import json
import csv

# Dados de exemplo
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "cidade": "São Paulo"
}

# JSON - Como dicionário
print("JSON:")
print(json.dumps(pessoa, indent=2, ensure_ascii=False))

# CSV - Como tabela
print("\\nCSV:")
print("nome,idade,cidade")
print("Ana Silva,28,São Paulo")'''
        
        self.exemplo(codigo_exemplo)

        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "APIs do Twitter, Instagram, YouTube usam JSON",
            "Bancos exportam relatórios em CSV",
            "Sistemas de e-commerce trocam dados via JSON",
            "Excel e Google Sheets salvam em CSV"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")

        self.pausar()

    def _secao_como_funciona(self) -> None:
        """Seção: Como JSON e CSV funcionam?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("COMO JSON E CSV FUNCIONAM?", "⚙️", "info")

        # JSON primeiro
        self.print_colored("\n📋 ESTRUTURA DO JSON:", "warning")
        self.print_colored("JSON usa chaves e valores, como dicionários Python:", "text")
        
        exemplo_json = '''{
  "produto": "Notebook",
  "preco": 2500.99,
  "disponivel": true,
  "categorias": ["eletrônicos", "informática"],
  "fabricante": {
    "nome": "TechCorp",
    "pais": "Brasil"
  }
}'''
        
        print("\n💻 Exemplo de JSON:")
        self.print_colored(exemplo_json, "accent")
        input("\n🔸 Pressione ENTER para ver CSV...")

        # CSV depois
        self.print_colored("\n📊 ESTRUTURA DO CSV:", "success")
        self.print_colored("CSV usa vírgulas para separar dados em colunas:", "text")
        
        exemplo_csv = '''produto,preco,disponivel,categoria
Notebook,2500.99,true,eletrônicos
Mouse,89.90,true,periféricos
Monitor,1200.00,false,eletrônicos'''
        
        print("\n📋 Exemplo de CSV:")
        self.print_colored(exemplo_csv, "info")
        input("\n🔸 Pressione ENTER para ver as diferenças...")

        # Comparação
        self.print_colored("\n⚖️ PRINCIPAIS DIFERENÇAS:", "warning")
        diferencas = [
            ("JSON", "Hierárquico (aninhado)", "Mais flexível"),
            ("CSV", "Tabular (planilha)", "Mais simples")
        ]
        
        for formato, estrutura, caracteristica in diferencas:
            self.print_colored(f"\n{formato}:", "accent")
            self.print_colored(f"  • Estrutura: {estrutura}", "text")
            self.print_colored(f"  • Vantagem: {caracteristica}", "text")

        self.pausar()

    def _secao_exemplos_praticos(self) -> None:
        """Seção: Exemplos práticos de JSON e CSV"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("EXEMPLOS PRÁTICOS", "💡", "success")

        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Salvando dados pessoais em JSON',
                'descricao': 'Como organizar informações complexas',
                'codigo': '''import json

# Dados de um usuário
usuario = {
    "id": 1001,
    "nome": "Maria Santos",
    "email": "maria@email.com",
    "enderecos": [
        {"tipo": "casa", "cidade": "São Paulo"},
        {"tipo": "trabalho", "cidade": "São Paulo"}
    ],
    "ativo": True
}

# Salvando em JSON
with open("usuario.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuario, arquivo, indent=2, ensure_ascii=False)

print("✅ Dados salvos em usuario.json")

# Carregando de volta
with open("usuario.json", "r", encoding="utf-8") as arquivo:
    usuario_carregado = json.load(arquivo)

print(f"Nome: {usuario_carregado['nome']}")
print(f"Endereços: {len(usuario_carregado['enderecos'])}")''',
                'explicacao': 'JSON é perfeito para dados complexos com hierarquia'
            },
            {
                'titulo': 'EXEMPLO 2: Processando vendas em CSV',
                'descricao': 'Como trabalhar com dados tabulares',
                'codigo': '''import csv
from datetime import datetime

# Dados de vendas
vendas = [
    ["2024-01-15", "Notebook", 2, 2500.00],
    ["2024-01-15", "Mouse", 5, 50.00],
    ["2024-01-16", "Teclado", 3, 150.00]
]

# Salvando CSV
with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    # Cabeçalho
    writer.writerow(["data", "produto", "quantidade", "preco"])
    # Dados
    writer.writerows(vendas)

print("✅ Vendas salvas em vendas.csv")

# Lendo CSV
with open("vendas.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.DictReader(arquivo)
    total = 0
    for linha in reader:
        subtotal = int(linha["quantidade"]) * float(linha["preco"])
        total += subtotal
        print(f"{linha['produto']}: R$ {subtotal:.2f}")
    
print(f"\\nTotal geral: R$ {total:.2f}")''',
                'explicacao': 'CSV é ideal para dados simples em formato de tabela'
            },
            {
                'titulo': 'EXEMPLO 3: Convertendo entre formatos',
                'descricao': 'Como transformar CSV em JSON e vice-versa',
                'codigo': '''import json
import csv

# Função para converter CSV para JSON
def csv_para_json(arquivo_csv, arquivo_json):
    dados = []
    with open(arquivo_csv, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for linha in reader:
            dados.append(linha)
    
    with open(arquivo_json, "w", encoding="utf-8") as json_file:
        json.dump(dados, json_file, indent=2, ensure_ascii=False)
    
    return len(dados)

# Convertendo
if True:  # Simulando existência do arquivo
    # Criamos dados de exemplo primeiro
    dados_exemplo = [
        {"nome": "João", "idade": "30", "cidade": "Rio de Janeiro"},
        {"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
    ]
    
    # Salvando como JSON
    with open("pessoas.json", "w", encoding="utf-8") as f:
        json.dump(dados_exemplo, f, indent=2, ensure_ascii=False)
    
    print("✅ Conversão simulada com sucesso!")
    print("JSON pode conter arrays e objetos complexos")
    print("CSV é melhor para dados simples e planos")''',
                'explicacao': 'Conversão entre formatos é comum em projetos reais'
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

        self.print_success("\n🎉 Agora você viu JSON e CSV em ação! Vamos praticar!")
        self.pausar()

    def _secao_casos_uso(self) -> None:
        """Seção: Onde usar JSON e CSV na vida real?"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CASOS DE USO NO MUNDO REAL", "🌍", "accent")

        # JSON Cases
        self.print_colored("\n📋 QUANDO USAR JSON:", "warning")
        casos_json = [
            ("🌐 APIs e Web Services", "Twitter, Instagram, GitHub APIs"),
            ("⚙️ Configurações de Apps", "VS Code, Chrome Extensions"),
            ("📱 Apps Mobile", "Dados entre frontend e backend"),
            ("🎮 Jogos", "Save games, configurações de personagem"),
            ("🤖 IoT e Sensores", "Dados de temperatura, umidade, etc.")
        ]

        for caso, exemplo in casos_json:
            self.print_colored(f"\n{caso}", "accent")
            self.print_colored(f"   Exemplo: {exemplo}", "text")
            input("   🔸 Pressione ENTER para o próximo...")

        # CSV Cases
        self.print_colored("\n📊 QUANDO USAR CSV:", "success")
        casos_csv = [
            ("📈 Relatórios Financeiros", "Bancos, fintechs, contabilidade"),
            ("📋 Planilhas e Análises", "Excel, Google Sheets, BI"),
            ("📊 Big Data", "Pandas, análise de dados científicos"),
            ("📤 Exportação de Dados", "Sistemas ERP, CRM"),
            ("🔄 Migração de Dados", "Entre diferentes sistemas")
        ]

        for caso, exemplo in casos_csv:
            self.print_colored(f"\n{caso}", "success")
            self.print_colored(f"   Exemplo: {exemplo}", "text")
            input("   🔸 Pressione ENTER para o próximo...")

        # Empresas que usam
        self.print_colored("\n🏢 EMPRESAS QUE USAM:", "info")
        empresas = [
            "Netflix: JSON para streaming de dados",
            "Amazon: CSV para relatórios de vendas",
            "Google: JSON em todas as APIs",
            "Microsoft: CSV no Excel e Power BI"
        ]

        for empresa in empresas:
            self.print_colored(f"• {empresa}", "primary")

        self.pausar()

    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas com JSON e CSV"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("MELHORES PRÁTICAS", "⭐", "warning")

        # Práticas para JSON
        self.print_colored("\n📋 BOAS PRÁTICAS - JSON:", "accent")
        praticas_json = [
            "✅ Use indent=2 para deixar legível",
            "✅ Sempre use ensure_ascii=False para acentos",
            "✅ Valide dados antes de salvar",
            "✅ Use try/except para capturar erros",
            "❌ Evite JSON muito aninhado (complexo demais)"
        ]

        for pratica in praticas_json:
            self.print_colored(pratica, "text")
            input("   🔸 Pressione ENTER para a próxima...")

        # Práticas para CSV
        self.print_colored("\n📊 BOAS PRÁTICAS - CSV:", "success")
        praticas_csv = [
            "✅ Sempre use encoding='utf-8'",
            "✅ Use DictReader/DictWriter quando possível",
            "✅ Inclua cabeçalhos informativos",
            "✅ Valide dados numéricos",
            "❌ Evite vírgulas nos dados (escape adequadamente)"
        ]

        for pratica in praticas_csv:
            self.print_colored(pratica, "text")
            input("   🔸 Pressione ENTER para a próxima...")

        # Exemplo de código com boas práticas
        self.print_colored("\n💻 EXEMPLO COM BOAS PRÁTICAS:", "info")
        codigo_boas_praticas = '''import json
import csv
from typing import Dict, List, Any

def salvar_json_seguro(dados: Dict[str, Any], arquivo: str) -> bool:
    """Salva JSON com tratamento de erro"""
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar JSON: {e}")
        return False

def ler_csv_seguro(arquivo: str) -> List[Dict[str, str]]:
    """Lê CSV com tratamento de erro"""
    try:
        dados = []
        with open(arquivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for linha in reader:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"❌ Arquivo {arquivo} não encontrado")
        return []
    except Exception as e:
        print(f"❌ Erro ao ler CSV: {e}")
        return []

# Exemplo de uso
dados_teste = {"nome": "João", "idade": 30}
sucesso = salvar_json_seguro(dados_teste, "teste.json")
print(f"Salvou JSON: {sucesso}")'''

        self.exemplo(codigo_boas_praticas)
        self.executar_codigo(codigo_boas_praticas)

        self.pausar()

    def _secao_erros_comuns(self) -> None:
        """Seção: Erros comuns e como evitar"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("ERROS COMUNS E COMO EVITAR", "⚠️", "warning")

        erros = [
            {
                'tipo': 'JSON - Encoding Problem',
                'problema': 'UnicodeDecodeError com acentos',
                'solucao': 'Sempre use encoding="utf-8"',
                'codigo_erro': '''# ❌ ERRADO
with open("dados.json", "w") as f:
    json.dump({"nome": "João"}, f)''',
                'codigo_correto': '''# ✅ CORRETO
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump({"nome": "João"}, f, ensure_ascii=False)'''
            },
            {
                'tipo': 'CSV - Delimiter Confusion',
                'problema': 'Dados com vírgulas quebram o CSV',
                'solucao': 'Use quotechar ou delimiter diferente',
                'codigo_erro': '''# ❌ ERRADO - dados com vírgulas
dados = ["João Silva, Jr.", "30", "São Paulo"]
writer.writerow(dados)  # Quebra o CSV''',
                'codigo_correto': '''# ✅ CORRETO - protege vírgulas
dados = ["João Silva, Jr.", "30", "São Paulo"]
writer = csv.writer(arquivo, quoting=csv.QUOTE_ALL)
writer.writerow(dados)'''
            },
            {
                'tipo': 'JSON - Type Error',
                'problema': 'Tentar serializar objetos não JSON',
                'solucao': 'Converter para tipos básicos primeiro',
                'codigo_erro': '''# ❌ ERRADO
from datetime import datetime
dados = {"agora": datetime.now()}
json.dumps(dados)  # Erro!''',
                'codigo_correto': '''# ✅ CORRETO
from datetime import datetime
dados = {"agora": datetime.now().isoformat()}
json.dumps(dados)  # Funciona!'''
            }
        ]

        for i, erro in enumerate(erros, 1):
            self.print_colored(f"\n🚨 ERRO COMUM {i}: {erro['tipo']}", "warning")
            self.print_colored(f"Problema: {erro['problema']}", "text")
            
            self.print_colored("\n❌ CÓDIGO COM ERRO:", "warning")
            self.print_colored(erro['codigo_erro'], "text")
            
            input("\n🔸 Pressione ENTER para ver a solução...")
            
            self.print_colored(f"\n💡 SOLUÇÃO: {erro['solucao']}", "success")
            self.print_colored("\n✅ CÓDIGO CORRETO:", "success")
            self.print_colored(erro['codigo_correto'], "text")
            
            if i < len(erros):
                input("\n🔸 Pressione ENTER para o próximo erro...")

        self.print_success("\n🎯 Conhecendo esses erros, você evita horas de debug!")
        self.pausar()

    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre JSON e CSV"""
        if self.ui:
            self.ui.clear_screen()

        self.print_section("CURIOSIDADES SOBRE DADOS", "💫", "accent")

        curiosidades = [
            {
                'titulo': 'JSON foi criado em 2001',
                'detalhe': 'Douglas Crockford inventou JSON como alternativa mais simples ao XML',
                'fato': 'Hoje JSON é usado em 99% das APIs web!'
            },
            {
                'titulo': 'CSV existe desde 1972',
                'detalhe': 'É mais antigo que o Python! Criado para mainframes IBM',
                'fato': 'Excel ainda usa CSV como formato padrão de export'
            },
            {
                'titulo': 'Netflix processa 1 trilhão de eventos JSON por dia',
                'detalhe': 'Cada clique, pause, play gera dados JSON',
                'fato': 'Isso dá 11 milhões de eventos por segundo!'
            },
            {
                'titulo': 'O maior arquivo CSV já processado tinha 100GB',
                'detalhe': 'Dados de telescópio espacial da NASA',
                'fato': 'Pandas conseguiu processar usando chunks!'
            },
            {
                'titulo': 'JSON é mais rápido que XML',
                'detalhe': 'JSON é 30% menor e 50% mais rápido para parse',
                'fato': 'Por isso APIs modernas abandonaram XML'
            }
        ]

        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n💫 CURIOSIDADE {i}: {curiosidade['titulo']}", "accent")
            self.print_colored(f"   {curiosidade['detalhe']}", "text")
            self.print_colored(f"   🎯 Fato: {curiosidade['fato']}", "info")
            
            if i < len(curiosidades):
                input("\n🔸 Pressione ENTER para a próxima curiosidade...")

        self.print_success("\n🌟 JSON e CSV são realmente incríveis!")
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
                'title': 'Quiz: Conhecimentos sobre JSON e CSV',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual biblioteca Python é usada para trabalhar com JSON?',
                        'answer': ['json', 'biblioteca json'],
                        'hint': 'É uma biblioteca nativa do Python'
                    },
                    {
                        'question': 'O que significa CSV?',
                        'answer': ['comma-separated values', 'comma separated values', 'valores separados por vírgula'],
                        'hint': 'Tem a ver com vírgulas separando dados'
                    },
                    {
                        'question': 'Qual método converte dict Python para string JSON?',
                        'answer': ['json.dumps', 'dumps'],
                        'hint': 'O "s" no final indica string'
                    },
                    {
                        'question': 'Qual encoding deve sempre usar com JSON e CSV em Python?',
                        'answer': ['utf-8', 'utf8'],
                        'hint': 'Padrão universal para caracteres especiais'
                    },
                    {
                        'question': 'JSON suporta comentários? (sim/não)',
                        'answer': ['não', 'nao', 'no'],
                        'hint': 'JSON é mais restrito que JavaScript'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o código para salvar um dicionário em JSON',
                        'starter': 'import json\ndados = {"nome": "Ana", "idade": 25}\nwith open("pessoa.json", "w", encoding="utf-8") as f:\n    # Complete aqui\nprint("Arquivo salvo!")',
                        'solution': 'json.dump(dados, f, ensure_ascii=False)',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o código para ler CSV com DictReader',
                        'starter': 'import csv\nwith open("dados.csv", "r", encoding="utf-8") as f:\n    # Complete aqui\n    for linha in reader:\n        print(linha)',
                        'solution': 'reader = csv.DictReader(f)',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a conversão de JSON para CSV',
                        'starter': 'import json, csv\nwith open("dados.json", "r") as jf:\n    dados = json.load(jf)\nwith open("dados.csv", "w", newline="") as cf:\n    writer = csv.DictWriter(cf, fieldnames=dados[0].keys())\n    writer.writeheader()\n    # Complete aqui',
                        'solution': 'writer.writerows(dados)',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: API de Dados Pessoais',
                'type': 'creative',
                'instruction': 'Crie um sistema que salva seus dados pessoais em JSON e exporta relatório em CSV!'
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre JSON e CSV",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de dados pessoais",
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

    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo sobre JSON e CSV"""
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
            self.print_success("🌟 PERFEITO! Você dominou JSON e CSV!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você tem um bom entendimento dos formatos de dados!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos sobre JSON e CSV.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo e tente mais tarde.", "info")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código JSON/CSV"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código para Completar", ex['starter'])
            
            # Diferentes tipos de exercícios
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print("\n✍️ Complete a linha que falta:")
                print("💡 Dica: Pense na função que salva dados no arquivo JSON")
                user_input = input(">>> ").strip()
                if user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão.")
                    
            elif exercise_type == 'intermediate':
                print("\n✍️ Complete o código para ler CSV:")
                print("💡 Dica: Use DictReader para ler CSV como dicionários")
                user_input = input(">>> ").strip()
                if user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão.")
                    
            elif exercise_type == 'advanced':
                print("\n✍️ Complete a conversão de dados:")
                print("💡 Dica: Use um método que escreve múltiplas linhas de uma vez")
                user_input = input(">>> ").strip()
                if user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão.")
            else:
                # Tipo padrão
                print("\n✍️ Digite a linha que falta:")
                user_input = input(">>> ").strip()
                user_code = user_input if user_input else ex['solution']
            
            # Substitui a linha que contém o comentário
            lines = ex['starter'].split('\n')
            for j, line in enumerate(lines):
                if '# Complete aqui' in line:
                    lines[j] = f"    {user_code}"
                    break
            complete_code = '\n'.join(lines)
            
            print("\n🚀 Executando seu código completo:")
            self.executar_codigo(complete_code)
            
            # Verifica se a resposta está correta
            if user_input and user_input.strip() == ex['solution'].strip():
                self.print_success("✅ PERFEITO! Você acertou a solução!")
            else:
                print(f"\n💡 Solução correta: {ex['solution']}")
                self.print_colored("📚 Não se preocupe! O importante é aprender.", "info")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo de API de dados pessoais"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        print("\n💡 IDEIAS PARA SEU SISTEMA:")
        print("• Sistema de perfil pessoal com hobbies e habilidades")
        print("• Lista de contatos com informações detalhadas")
        print("• Registro de atividades diárias com categorias")
        print("• Coleção pessoal (livros, filmes, jogos)")
        
        self.print_tip("Vamos criar passo a passo!")
        
        print("\n📝 PASSO 1: Defina o tema do seu sistema")
        tema = input("🎯 Qual tema você quer (perfil/contatos/atividades/colecao): ").strip().lower()
        if not tema or tema not in ['perfil', 'contatos', 'atividades', 'colecao']:
            tema = 'perfil'
            print("📋 Usando tema padrão: perfil pessoal")
        
        print(f"\n📊 PASSO 2: Dados para sistema de {tema}")
        dados = {}
        
        if tema == 'perfil':
            dados = {
                "nome": input("👤 Seu nome: ").strip() or "João Silva",
                "idade": input("📅 Sua idade: ").strip() or "25",
                "profissao": input("💼 Sua profissão: ").strip() or "Desenvolvedor",
                "hobbies": input("🎮 Hobbies (separados por vírgula): ").strip().split(',') or ["programação", "jogos"],
                "habilidades": input("⭐ Habilidades (separadas por vírgula): ").strip().split(',') or ["Python", "JavaScript"]
            }
        elif tema == 'contatos':
            dados = {
                "contatos": [
                    {
                        "nome": input("👤 Nome do contato 1: ").strip() or "Ana Santos",
                        "telefone": input("📞 Telefone: ").strip() or "(11) 99999-9999",
                        "email": input("📧 Email: ").strip() or "ana@email.com"
                    }
                ]
            }
        elif tema == 'atividades':
            dados = {
                "atividades": [
                    {
                        "data": input("📅 Data da atividade (YYYY-MM-DD): ").strip() or "2024-01-15",
                        "tipo": input("📝 Tipo de atividade: ").strip() or "Estudo",
                        "descricao": input("📖 Descrição: ").strip() or "Estudei Python",
                        "duracao": input("⏰ Duração em minutos: ").strip() or "60"
                    }
                ]
            }
        else:  # colecao
            dados = {
                "colecao": [
                    {
                        "item": input("📚 Nome do item: ").strip() or "Clean Code",
                        "categoria": input("🏷️ Categoria: ").strip() or "Livro",
                        "status": input("✅ Status (lido/não lido): ").strip() or "lido",
                        "nota": input("⭐ Nota (1-5): ").strip() or "5"
                    }
                ]
            }
        
        print(f"\n🚀 PASSO 3: Gerando sistema completo de {tema}")
        
        # Cria o código do sistema
        codigo_sistema = f'''# 🐍 SISTEMA DE {tema.upper()} PESSOAL
# Criado com JSON e CSV - Módulo 17

import json
import csv
from datetime import datetime

# Dados do sistema
dados = {dados}

print("=" * 50)
print(f"🎯 SISTEMA DE {tema.upper()} PESSOAL")
print("=" * 50)

# 1. SALVANDO EM JSON
print("\\n📋 Salvando dados em JSON...")
with open("{tema}_dados.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, indent=2, ensure_ascii=False)
print("✅ Dados salvos em {tema}_dados.json")

# 2. CONVERTENDO PARA CSV
print("\\n📊 Convertendo para CSV...")
if "{tema}" == "perfil":
    # Para perfil, criar CSV simples
    with open("{tema}_relatorio.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["campo", "valor"])
        for chave, valor in dados.items():
            if isinstance(valor, list):
                writer.writerow([chave, "; ".join(valor)])
            else:
                writer.writerow([chave, valor])
else:
    # Para outros tipos, usar estrutura mais complexa
    with open("{tema}_relatorio.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        if dados:
            first_key = list(dados.keys())[0]
            if isinstance(dados[first_key], list) and dados[first_key]:
                # Dados são lista de dicionários
                fieldnames = dados[first_key][0].keys()
                writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(dados[first_key])

print("✅ Relatório CSV criado!")

# 3. LENDO E EXIBINDO DADOS
print("\\n🔍 CARREGANDO E EXIBINDO DADOS:")
with open("{tema}_dados.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

print("JSON carregado:")
print(json.dumps(dados_carregados, indent=2, ensure_ascii=False))

print("\\n📁 ARQUIVOS CRIADOS:")
print(f"• {tema}_dados.json (dados completos)")
print(f"• {tema}_relatorio.csv (relatório)")

print("\\n🎉 SISTEMA FUNCIONANDO PERFEITAMENTE!")
print("💡 Você pode expandir adicionando mais dados e funcionalidades!")'''
        
        print(f"\n🎨 Aqui está seu sistema de {tema} personalizado:")
        self.exemplo(codigo_sistema)
        
        print(f"\n🚀 Executando seu Sistema de {tema.title()}:")
        self.executar_codigo(codigo_sistema)
        
        self.print_success(f"\n🏆 PARABÉNS! Você criou um sistema completo de {tema}!")
        self.print_colored("💡 DICAS PARA EXPANDIR:", "info")
        print("• Adicione mais campos aos dados")
        print("• Crie funções para buscar e filtrar")
        print("• Implemente validação de dados")
        print("• Adicione interface web com Flask")
        
        self.pausar()

    def _mini_projeto_dashboard_dados(self) -> None:
        """Mini Projeto - Módulo 17: Dashboard de Análise de Dados Integrado"""

        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: DASHBOARD DE ANÁLISE DE DADOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: DASHBOARD DE ANÁLISE DE DADOS")
            print("="*50)

        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema completo de análise de dados com JSON e CSV!")

        self.print_concept(
            "Dashboard de Análise de Dados",
            "Sistema que processa dados em diferentes formatos e gera relatórios inteligentes"
        )

        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "Análise de vendas em e-commerce",
            "Relatórios financeiros em fintechs",
            "Dashboard de métricas em startups",
            "Análise de dados científicos em pesquisa"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")

        # === DESENVOLVIMENTO PASSO A PASSO ===

        # PASSO 1: Coleta de informações do dashboard
        self.print_section("PASSO 1: Configure seu Dashboard", "📝", "info")
        self.print_tip("Vamos personalizar o dashboard para sua área de interesse")

        try:
            if self.ui:
                input_color = self.ui.get_color("warning")
                reset = self.ui.get_color("reset")
                
                empresa = input(f"{input_color}🏢 Nome da sua empresa/projeto: {reset}").strip()
                if not empresa:
                    empresa = "TechCorp Analytics"
                
                area = input(f"{input_color}📊 Área de análise (vendas/marketing/financeiro): {reset}").strip()
                if not area:
                    area = "vendas"
                
                periodo = input(f"{input_color}📅 Período de análise (exemplo: Janeiro 2024): {reset}").strip()
                if not periodo:
                    periodo = "Janeiro 2024"
            else:
                empresa = input("🏢 Nome da sua empresa/projeto: ").strip()
                if not empresa:
                    empresa = "TechCorp Analytics"
                
                area = input("📊 Área de análise (vendas/marketing/financeiro): ").strip()
                if not area:
                    area = "vendas"
                
                periodo = input("📅 Período de análise (exemplo: Janeiro 2024): ").strip()
                if not periodo:
                    periodo = "Janeiro 2024"

        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return

        # PASSO 2: Processamento/Lógica
        self.print_section("PASSO 2: Gerando dados e processando", "⚙️", "success")
        self.print_colored("Agora vamos criar um sistema completo de análise:", "text")

        # PASSO 3: Resultado/Output
        self.print_section("PASSO 3: Sistema em funcionamento", "🎬", "warning")

        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o dashboard completo que você criou:", "text")

        codigo_final = f'''# 🐍 PROJETO: DASHBOARD DE ANÁLISE DE DADOS
# Módulo 17: JSON e CSV
# Empresa: {empresa}
# Área: {area.title()}
# Período: {periodo}

import json
import csv
import os
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import statistics

class DashboardAnalytics:
    """Dashboard completo para análise de dados JSON/CSV"""
    
    def __init__(self, empresa: str, area: str, periodo: str):
        self.empresa = empresa
        self.area = area
        self.periodo = periodo
        self.dados_json = []
        self.dados_csv = []
        self.relatorios = {{}}
        
        print(f"🚀 Dashboard iniciado para {{self.empresa}}")
        print(f"📊 Área: {{self.area}} | Período: {{self.periodo}}")
    
    def gerar_dados_exemplo(self):
        """Gera dados de exemplo para demonstração"""
        print("\\n📝 Gerando dados de exemplo...")
        
        # Dados JSON - Perfil detalhado de clientes
        self.dados_json = [
            {{
                "id": 1001,
                "nome": "Ana Silva",
                "email": "ana@email.com",
                "idade": 28,
                "cidade": "São Paulo",
                "compras": [
                    {{"produto": "Notebook", "valor": 2500.00, "data": "2024-01-15"}},
                    {{"produto": "Mouse", "valor": 89.90, "data": "2024-01-20"}}
                ],
                "total_gasto": 2589.90,
                "categoria": "Premium"
            }},
            {{
                "id": 1002,
                "nome": "João Santos",
                "email": "joao@email.com",
                "idade": 35,
                "cidade": "Rio de Janeiro",
                "compras": [
                    {{"produto": "Teclado", "valor": 150.00, "data": "2024-01-18"}}
                ],
                "total_gasto": 150.00,
                "categoria": "Básico"
            }},
            {{
                "id": 1003,
                "nome": "Maria Costa",
                "email": "maria@email.com",
                "idade": 42,
                "cidade": "Belo Horizonte",
                "compras": [
                    {{"produto": "Monitor", "valor": 800.00, "data": "2024-01-22"}},
                    {{"produto": "Webcam", "valor": 200.00, "data": "2024-01-25"}}
                ],
                "total_gasto": 1000.00,
                "categoria": "Intermediário"
            }}
        ]
        
        # Dados CSV - Transações simples
        self.dados_csv = [
            {{"data": "2024-01-15", "produto": "Notebook", "quantidade": 1, "preco": 2500.00, "vendedor": "Ana"}},
            {{"data": "2024-01-15", "produto": "Mouse", "quantidade": 2, "preco": 89.90, "vendedor": "João"}},
            {{"data": "2024-01-18", "produto": "Teclado", "quantidade": 1, "preco": 150.00, "vendedor": "Maria"}},
            {{"data": "2024-01-20", "produto": "Mouse", "quantidade": 1, "preco": 89.90, "vendedor": "Ana"}},
            {{"data": "2024-01-22", "produto": "Monitor", "quantidade": 1, "preco": 800.00, "vendedor": "Pedro"}},
            {{"data": "2024-01-25", "produto": "Webcam", "quantidade": 3, "preco": 200.00, "vendedor": "Maria"}}
        ]
        
        print("✅ Dados de exemplo gerados!")
    
    def salvar_dados(self):
        """Salva dados em arquivos JSON e CSV"""
        print("\\n💾 Salvando dados...")
        
        # Salvar JSON
        with open("clientes.json", "w", encoding="utf-8") as f:
            json.dump(self.dados_json, f, indent=2, ensure_ascii=False)
        
        # Salvar CSV
        with open("transacoes.csv", "w", newline="", encoding="utf-8") as f:
            if self.dados_csv:
                writer = csv.DictWriter(f, fieldnames=self.dados_csv[0].keys())
                writer.writeheader()
                writer.writerows(self.dados_csv)
        
        print("✅ Dados salvos em clientes.json e transacoes.csv")
    
    def analisar_json(self):
        """Análise avançada dos dados JSON"""
        print("\\n🔍 ANÁLISE DOS CLIENTES (JSON):")
        
        total_clientes = len(self.dados_json)
        idade_media = statistics.mean([cliente["idade"] for cliente in self.dados_json])
        gasto_total = sum([cliente["total_gasto"] for cliente in self.dados_json])
        gasto_medio = gasto_total / total_clientes
        
        # Análise por categoria
        categorias = Counter([cliente["categoria"] for cliente in self.dados_json])
        
        # Análise por cidade
        cidades = Counter([cliente["cidade"] for cliente in self.dados_json])
        
        print(f"👥 Total de clientes: {{total_clientes}}")
        print(f"📊 Idade média: {{idade_media:.1f}} anos")
        print(f"💰 Gasto total: R$ {{gasto_total:.2f}}")
        print(f"💵 Gasto médio por cliente: R$ {{gasto_medio:.2f}}")
        
        print("\\n📈 Por categoria:")
        for categoria, qtd in categorias.items():
            print(f"  {{categoria}}: {{qtd}} clientes")
        
        print("\\n🌍 Por cidade:")
        for cidade, qtd in cidades.items():
            print(f"  {{cidade}}: {{qtd}} clientes")
        
        return {{
            "total_clientes": total_clientes,
            "idade_media": idade_media,
            "gasto_total": gasto_total,
            "gasto_medio": gasto_medio,
            "categorias": dict(categorias),
            "cidades": dict(cidades)
        }}
    
    def analisar_csv(self):
        """Análise dos dados transacionais CSV"""
        print("\\n📊 ANÁLISE DE TRANSAÇÕES (CSV):")
        
        total_transacoes = len(self.dados_csv)
        
        # Análise de vendas
        vendas_por_produto = defaultdict(lambda: {{"quantidade": 0, "receita": 0}})
        vendas_por_vendedor = defaultdict(float)
        
        for transacao in self.dados_csv:
            produto = transacao["produto"]
            qtd = int(transacao["quantidade"])
            preco = float(transacao["preco"])
            vendedor = transacao["vendedor"]
            receita = qtd * preco
            
            vendas_por_produto[produto]["quantidade"] += qtd
            vendas_por_produto[produto]["receita"] += receita
            vendas_por_vendedor[vendedor] += receita
        
        receita_total = sum([dados["receita"] for dados in vendas_por_produto.values()])
        
        print(f"🛒 Total de transações: {{total_transacoes}}")
        print(f"💰 Receita total: R$ {{receita_total:.2f}}")
        print(f"💵 Receita média por transação: R$ {{receita_total/total_transacoes:.2f}}")
        
        print("\\n🏆 Top produtos:")
        top_produtos = sorted(vendas_por_produto.items(), 
                            key=lambda x: x[1]["receita"], reverse=True)
        for produto, dados in top_produtos[:3]:
            print(f"  {{produto}}: {{dados['quantidade']}} unidades, R$ {{dados['receita']:.2f}}")
        
        print("\\n👑 Top vendedores:")
        top_vendedores = sorted(vendas_por_vendedor.items(), 
                              key=lambda x: x[1], reverse=True)
        for vendedor, receita in top_vendedores[:3]:
            print(f"  {{vendedor}}: R$ {{receita:.2f}}")
        
        return {{
            "total_transacoes": total_transacoes,
            "receita_total": receita_total,
            "vendas_por_produto": dict(vendas_por_produto),
            "vendas_por_vendedor": dict(vendas_por_vendedor)
        }}
    
    def gerar_relatorio_integrado(self):
        """Gera relatório final integrando JSON e CSV"""
        print("\\n📋 RELATÓRIO INTEGRADO:")
        print("=" * 50)
        
        analise_json = self.analisar_json()
        analise_csv = self.analisar_csv()
        
        # Métricas integradas
        roi = (analise_csv["receita_total"] / analise_json["gasto_total"]) * 100 if analise_json["gasto_total"] > 0 else 0
        
        print(f"\\n🎯 MÉTRICAS INTEGRADAS:")
        print(f"💼 Empresa: {{self.empresa}}")
        print(f"📊 Área: {{self.area}}")
        print(f"📅 Período: {{self.periodo}}")
        print(f"👥 Clientes ativos: {{analise_json['total_clientes']}}")
        print(f"🛒 Transações processadas: {{analise_csv['total_transacoes']}}")
        print(f"💰 Receita total: R$ {{analise_csv['receita_total']:.2f}}")
        print(f"📈 ROI: {{roi:.1f}}%")
        
        # Salvar relatório final
        relatorio_final = {{
            "empresa": self.empresa,
            "area": self.area,
            "periodo": self.periodo,
            "timestamp": datetime.now().isoformat(),
            "metricas": {{
                "clientes": analise_json,
                "transacoes": analise_csv,
                "roi": roi
            }}
        }}
        
        with open("relatorio_final.json", "w", encoding="utf-8") as f:
            json.dump(relatorio_final, f, indent=2, ensure_ascii=False)
        
        print("\\n✅ Relatório salvo em relatorio_final.json")
        
        return relatorio_final
    
    def executar_dashboard(self):
        """Executa todo o processo do dashboard"""
        print(f"\\n🚀 EXECUTANDO DASHBOARD - {{self.empresa.upper()}}")
        print("=" * 60)
        
        self.gerar_dados_exemplo()
        self.salvar_dados()
        relatorio = self.gerar_relatorio_integrado()
        
        print("\\n🎉 DASHBOARD EXECUTADO COM SUCESSO!")
        print("\\n📁 Arquivos gerados:")
        print("  • clientes.json (dados detalhados)")
        print("  • transacoes.csv (dados transacionais)")
        print("  • relatorio_final.json (análise integrada)")
        
        return relatorio

# === EXECUÇÃO DO DASHBOARD ===
print("🎯 DASHBOARD DE ANÁLISE DE DADOS")
print("=" * 40)

# Criar instância do dashboard
dashboard = DashboardAnalytics("{empresa}", "{area}", "{periodo}")

# Executar análise completa
resultado = dashboard.executar_dashboard()

print("\\n🏆 SUCESSO! Seu dashboard está funcionando!")
print("\\n💡 APLICAÇÕES REAIS:")
print("  • Análise de vendas em tempo real")
print("  • Relatórios automáticos para gestão")
print("  • Integração com sistemas ERP/CRM")
print("  • Business Intelligence empresarial")'''

        self.exemplo(codigo_final)

        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)

        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um dashboard completo de análise de dados!")

        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Conectar com APIs reais (Twitter, Instagram)",
            "Integrar com bancos de dados (PostgreSQL, MongoDB)",
            "Criar dashboards web com Flask/Django",
            "Implementar machine learning para predições",
            "Automatizar relatórios com schedule/cron"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")

        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Master de Dados!")

        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Dashboard de Análise de Dados Integrado")

        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo17JsonCsv()
    print("Teste do módulo 17 - versão refatorada")
    module._json_csv_moderno()