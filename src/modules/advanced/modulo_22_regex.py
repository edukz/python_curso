#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 22: Expressões Regulares (Regex)
Aprenda a usar expressões regulares para busca avançada em texto
"""

import re
from ..shared.base_module import BaseModule


class Modulo22Regex(BaseModule):
    """Módulo 22: Expressões Regulares - Busca Avançada em Texto"""
    
    def __init__(self):
        super().__init__("modulo_22", "Expressões Regulares (Regex)")
        self.has_mini_project = True
        self.mini_project_points = 80
    
    def execute(self) -> None:
        """Executa o módulo sobre expressões regulares"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._regex_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _regex_module(self) -> None:
        """Conteúdo principal sobre expressões regulares"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔍 MÓDULO 22: EXPRESSÕES REGULARES - BUSCA AVANÇADA EM TEXTO")
        else:
            print("\n" + "="*60)
            print("🔍 MÓDULO 22: EXPRESSÕES REGULARES - BUSCA AVANÇADA EM TEXTO")
            print("="*60)
        
        print("📝 Aprenda a usar Regex para busca avançada em texto!")
        print("🎯 Expressões regulares são uma ferramenta poderosa para:")
        print("• Validação de dados (email, telefone, CPF)")
        print("• Busca e substituição avançada em textos")
        print("• Extração de informações específicas")
        print("• Processamento de logs e dados")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._introducao_regex()
        self._metacaracteres()
        self._grupos_capturas()
        self._validacao_dados_moderna()
        self._parsing_dados_estruturados()
        self._web_scraping_basico()
        self._processamento_logs_avancado()
        self._busca_substituicao()
        self._mini_projeto_regex_avancado()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _introducao_regex(self):
        """Introdução às expressões regulares"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📖 INTRODUÇÃO ÀS EXPRESSÕES REGULARES")
        
        print("🔍 O que são Expressões Regulares (Regex)?")
        print("• Sequências de caracteres que formam padrões de busca")
        print("• Usadas para encontrar, extrair ou validar texto")
        print("• Muito poderosas mas podem ser complexas")
        
        codigo = '''import re

# Exemplo simples - buscar palavra
texto = "Python é uma linguagem de programação"
padrao = r"Python"

# Buscar padrão
resultado = re.search(padrao, texto)
if resultado:
    print(f"Encontrado: {resultado.group()}")
    print(f"Posição: {resultado.start()}-{resultado.end()}")

# Buscar todas as ocorrências
palavras = re.findall(r"\\b\\w+\\b", texto)
print(f"Palavras encontradas: {palavras}")

# Verificar se texto combina com padrão
email = "usuario@exemplo.com"
padrao_email = r"^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$"
if re.match(padrao_email, email):
    print("Email válido!")
else:
    print("Email inválido!")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Exemplo básico de Regex")
        else:
            print("\n" + "="*50)
            print("EXEMPLO BÁSICO:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _metacaracteres(self):
        """Metacaracteres e padrões básicos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 METACARACTERES E PADRÕES")
        
        print("🔤 Principais metacaracteres:")
        print("• . (ponto) - qualquer caractere")
        print("• * - zero ou mais repetições")
        print("• + - uma ou mais repetições")
        print("• ? - zero ou uma repetição")
        print("• ^ - início da string")
        print("• $ - fim da string")
        print("• \\d - dígito (0-9)")
        print("• \\w - caractere de palavra")
        print("• \\s - espaço em branco")
        
        codigo = '''import re

texto = "Telefone: (11) 99999-8888, Email: user@test.com, CEP: 12345-678"

# Buscar telefone
telefone = re.search(r"\\(\\d{2}\\) \\d{5}-\\d{4}", texto)
print(f"Telefone: {telefone.group() if telefone else 'Não encontrado'}")

# Buscar email
email = re.search(r"\\w+@\\w+\\.\\w+", texto)
print(f"Email: {email.group() if email else 'Não encontrado'}")

# Buscar CEP
cep = re.search(r"\\d{5}-\\d{3}", texto)
print(f"CEP: {cep.group() if cep else 'Não encontrado'}")

# Buscar todos os números
numeros = re.findall(r"\\d+", texto)
print(f"Números: {numeros}")

# Substituir números por XXX
texto_anonimo = re.sub(r"\\d", "X", texto)
print(f"Anônimo: {texto_anonimo}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Metacaracteres em ação")
        else:
            print("\n" + "="*50)
            print("METACARACTERES EM AÇÃO:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _grupos_capturas(self):
        """Grupos e capturas nomeadas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("👥 GRUPOS E CAPTURAS")
        
        print("📋 Grupos permitem capturar partes específicas:")
        print("• () - grupo de captura")
        print("• (?P<nome>) - grupo nomeado")
        print("• (?:) - grupo não capturante")
        
        codigo = '''import re

# Exemplo com grupos
data_texto = "Nascimento: 25/12/1990"
padrao_data = r"(\\d{2})/(\\d{2})/(\\d{4})"

match = re.search(padrao_data, data_texto)
if match:
    dia, mes, ano = match.groups()
    print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

# Grupos nomeados
padrao_nomeado = r"(?P<dia>\\d{2})/(?P<mes>\\d{2})/(?P<ano>\\d{4})"
match_nomeado = re.search(padrao_nomeado, data_texto)
if match_nomeado:
    print(f"Data: {match_nomeado.group('dia')}/{match_nomeado.group('mes')}/{match_nomeado.group('ano')}")
    print(f"Dicionário: {match_nomeado.groupdict()}")

# Exemplo com múltiplas capturas
contatos = """
João Silva: (11) 99999-1111
Maria Santos: (21) 88888-2222
Pedro Costa: (31) 77777-3333
"""

padrao_contato = r"([A-Za-z ]+): \\((\\d{2})\\) (\\d{5}-\\d{4})"
matches = re.findall(padrao_contato, contatos)

print("\\nContatos encontrados:")
for nome, ddd, telefone in matches:
    print(f"• {nome.strip()}: ({ddd}) {telefone}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Grupos e capturas")
        else:
            print("\n" + "="*50)
            print("GRUPOS E CAPTURAS:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _validacao_dados(self):
        """Validação de dados com regex"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ VALIDAÇÃO DE DADOS")
        
        print("🔐 Regex para validação comum:")
        
        codigo = '''import re

def validar_email(email):
    """Valida formato de email"""
    padrao = r"^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(padrao, email))

def validar_telefone(telefone):
    """Valida telefone brasileiro"""
    padrao = r"^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$"
    return bool(re.match(padrao, telefone))

def validar_cpf(cpf):
    """Valida formato de CPF"""
    padrao = r"^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$"
    return bool(re.match(padrao, cpf))

def validar_cep(cep):
    """Valida CEP brasileiro"""
    padrao = r"^\\d{5}-\\d{3}$"
    return bool(re.match(padrao, cep))

def validar_senha_forte(senha):
    """Valida senha forte"""
    # Pelo menos 8 caracteres, uma maiúscula, uma minúscula, um número
    padrao = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d@$!%*?&]{8,}$"
    return bool(re.match(padrao, senha))

# Testes
print("=== VALIDAÇÕES ===")
print(f"Email 'user@test.com': {validar_email('user@test.com')}")
print(f"Email 'email_inválido': {validar_email('email_inválido')}")
print(f"Telefone '(11) 99999-8888': {validar_telefone('(11) 99999-8888')}")
print(f"CPF '123.456.789-00': {validar_cpf('123.456.789-00')}")
print(f"CEP '12345-678': {validar_cep('12345-678')}")
print(f"Senha 'MinhaSenh@123': {validar_senha_forte('MinhaSenh@123')}")
print(f"Senha '123': {validar_senha_forte('123')}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Validação de dados")
        else:
            print("\n" + "="*50)
            print("VALIDAÇÃO DE DADOS:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _parsing_dados_estruturados(self):
        """Parsing de dados estruturados com regex"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 PARSING DE DADOS ESTRUTURADOS")
        
        print("🔍 Extraindo informações de dados estruturados:")
        
        codigo = '''import re
from typing import Dict, List, Optional
from datetime import datetime

class DataParser:
    """Parser avançado para extrair dados estruturados"""
    
    def parse_csv_line(self, line: str) -> List[str]:
        """Parse CSV considerando aspas e vírgulas"""
        # Regex para CSV com aspas e escape
        pattern = r'(?:^|,)("(?:[^"]|"")*"|[^,]*)'
        matches = re.findall(pattern, line)
        return [field.strip('"').replace('""', '"') for field in matches]
    
    def extract_json_values(self, json_text: str) -> Dict[str, str]:
        """Extrai valores de strings JSON simples"""
        # Pattern para chave-valor JSON
        pattern = r'"([^"]+)"\\s*:\\s*"([^"]*)"'
        matches = re.findall(pattern, json_text)
        return dict(matches)
    
    def parse_log_entry(self, log_line: str) -> Optional[Dict[str, str]]:
        """Parse detalhado de entrada de log"""
        # Apache/Nginx combined log format
        pattern = r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - - \\[([^\\]]+)\\] "(\\w+) ([^"]+) HTTP/[^"]*" (\\d{3}) (\\d+) "([^"]*)" "([^"]*)"'
        match = re.match(pattern, log_line)
        
        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'method': match.group(3),
                'url': match.group(4),
                'status': int(match.group(5)),
                'size': int(match.group(6)),
                'referer': match.group(7),
                'user_agent': match.group(8)
            }
        return None
    
    def extract_html_content(self, html: str) -> Dict[str, List[str]]:
        """Extrai conteúdo de HTML básico"""
        data = {
            'titles': re.findall(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE),
            'links': re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>', html, re.IGNORECASE),
            'images': re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html, re.IGNORECASE),
            'emails': re.findall(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', html),
            'phones': re.findall(r'\\(?\\d{2}\\)?[\\s.-]?\\d{4,5}[\\s.-]?\\d{4}', html)
        }
        return data
    
    def parse_config_file(self, config_text: str) -> Dict[str, str]:
        """Parse arquivo de configuração key=value"""
        # Remove comentários e linhas vazias
        lines = [line.strip() for line in config_text.split('\\n') 
                if line.strip() and not line.strip().startswith('#')]
        
        config = {}
        for line in lines:
            match = re.match(r'([^=]+)=(.+)', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip().strip('"')
                config[key] = value
        
        return config

# Demonstração prática
parser = DataParser()

print("=== PARSING DE DADOS ESTRUTURADOS ===\\n")

# 1. CSV com vírgulas e aspas
csv_line = 'João Silva,"Rua A, 123",São Paulo,"R$ 5.000,00"'
csv_data = parser.parse_csv_line(csv_line)
print("1. CSV PARSING:")
print(f"   Input: {csv_line}")
print(f"   Output: {csv_data}\\n")

# 2. JSON simples
json_text = '{"nome": "Maria", "cidade": "Rio de Janeiro", "profissao": "Desenvolvedora"}'
json_data = parser.extract_json_values(json_text)
print("2. JSON PARSING:")
print(f"   Input: {json_text}")
print(f"   Output: {json_data}\\n")

# 3. Log de servidor
log_line = '192.168.1.100 - - [10/Jan/2024:08:30:15 +0000] "GET /index.html HTTP/1.1" 200 1024 "https://google.com" "Mozilla/5.0"'
log_data = parser.parse_log_entry(log_line)
print("3. LOG PARSING:")
print(f"   IP: {log_data['ip'] if log_data else 'N/A'}")
print(f"   Method: {log_data['method'] if log_data else 'N/A'}")
print(f"   URL: {log_data['url'] if log_data else 'N/A'}\\n")

# 4. HTML básico
html_sample = '<title>Minha Página</title><a href="https://exemplo.com">Link</a><img src="imagem.jpg">'
html_data = parser.extract_html_content(html_sample)
print("4. HTML PARSING:")
for key, values in html_data.items():
    if values:
        print(f"   {key.title()}: {values}")

# 5. Arquivo de configuração
config_text = \\\"\\\"\\\"
# Configuração do sistema
database_host=localhost
database_port=5432
database_name=myapp
debug_mode=true
max_connections=100
\\\"\\\"\\\"
config_data = parser.parse_config_file(config_text)
print("\\n5. CONFIG PARSING:")
for key, value in config_data.items():
    print(f"   {key}: {value}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Parser de dados estruturados")
        else:
            print("\n" + "="*50)
            print("PARSER DE DADOS ESTRUTURADOS:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _web_scraping_basico(self):
        """Web scraping básico com regex"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌐 WEB SCRAPING BÁSICO COM REGEX")
        
        print("🕷️ Extraindo dados de páginas web com regex:")
        
        codigo = '''import re
from typing import Dict, List, Optional, NamedTuple

class WebScraper:
    """Web scraper básico usando regex"""
    
    def __init__(self):
        # Patterns compiladas para melhor performance
        self.email_pattern = re.compile(r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b')
        self.phone_pattern = re.compile(r'\\(?\\d{2}\\)?[\\s.-]?\\d{4,5}[\\s.-]?\\d{4}')
        self.url_pattern = re.compile(r'https?://[\\w\\.-]+\\.[a-zA-Z]{2,}(?:/[^\\s]*)?')
    
    def extract_social_links(self, html: str) -> Dict[str, List[str]]:
        """Extrai links de redes sociais"""
        patterns = {
            'facebook': r'https?://(?:www\\.)?facebook\\.com/[\\w\\.-]+',
            'twitter': r'https?://(?:www\\.)?twitter\\.com/[\\w\\.-]+',
            'instagram': r'https?://(?:www\\.)?instagram\\.com/[\\w\\.-]+',
            'linkedin': r'https?://(?:www\\.)?linkedin\\.com/[\\w\\.-/]+',
            'youtube': r'https?://(?:www\\.)?youtube\\.com/[\\w\\.-/?=]+',
            'github': r'https?://(?:www\\.)?github\\.com/[\\w\\.-]+'
        }
        
        social_links = {}
        for platform, pattern in patterns.items():
            links = re.findall(pattern, html, re.IGNORECASE)
            if links:
                social_links[platform] = list(set(links))  # Remove duplicatas
        
        return social_links
    
    def extract_contact_info(self, html: str) -> Dict[str, List[str]]:
        """Extrai informações de contato"""
        return {
            'emails': self.email_pattern.findall(html),
            'phones': self.phone_pattern.findall(html),
            'urls': self.url_pattern.findall(html)
        }
    
    def extract_meta_info(self, html: str) -> Dict[str, str]:
        """Extrai meta informações da página"""
        meta_info = {}
        
        # Title
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
        if title_match:
            meta_info['title'] = title_match.group(1).strip()
        
        # Meta description
        desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if desc_match:
            meta_info['description'] = desc_match.group(1).strip()
        
        # Meta keywords
        keywords_match = re.search(r'<meta[^>]+name=["\']keywords["\'][^>]+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if keywords_match:
            meta_info['keywords'] = keywords_match.group(1).strip()
        
        return meta_info
    
    def extract_price_info(self, html: str) -> List[Dict[str, str]]:
        """Extrai informações de preços"""
        # Padrões para preços em diferentes formatos
        price_patterns = [
            r'R\\$\\s*([\\d.,]+)',
            r'\\$([\\d.,]+)',
            r'€([\\d.,]+)',
            r'([\\d.,]+)\\s*reais?',
            r'([\\d.,]+)\\s*€',
            r'([\\d.,]+)\\s*\\$'
        ]
        
        prices = []
        for pattern in price_patterns:
            matches = re.findall(pattern, html, re.IGNORECASE)
            for match in matches:
                prices.append({
                    'value': match,
                    'pattern': pattern
                })
        
        return prices
    
    def analyze_page_structure(self, html: str) -> Dict[str, int]:
        """Analisa estrutura básica da página"""
        structure = {
            'headings_h1': len(re.findall(r'<h1[^>]*>', html, re.IGNORECASE)),
            'headings_h2': len(re.findall(r'<h2[^>]*>', html, re.IGNORECASE)),
            'headings_h3': len(re.findall(r'<h3[^>]*>', html, re.IGNORECASE)),
            'paragraphs': len(re.findall(r'<p[^>]*>', html, re.IGNORECASE)),
            'images': len(re.findall(r'<img[^>]*>', html, re.IGNORECASE)),
            'links': len(re.findall(r'<a[^>]*href', html, re.IGNORECASE)),
            'divs': len(re.findall(r'<div[^>]*>', html, re.IGNORECASE)),
            'scripts': len(re.findall(r'<script[^>]*>', html, re.IGNORECASE))
        }
        return structure

# Simulação de HTML de uma página de empresa
html_sample = \\\"\\\"\\\"
<!DOCTYPE html>
<html>
<head>
    <title>TechCorp - Soluções Tecnológicas</title>
    <meta name="description" content="Empresa líder em desenvolvimento de software">
    <meta name="keywords" content="tecnologia, software, desenvolvimento, python">
</head>
<body>
    <h1>Bem-vindos à TechCorp</h1>
    <h2>Nossos Serviços</h2>
    <p>Oferecemos desenvolvimento web por R$ 5.000,00</p>
    <p>Consultoria técnica a partir de R$ 2.500,00</p>
    
    <h2>Contato</h2>
    <p>Email: contato@techcorp.com.br</p>
    <p>Telefone: (11) 99999-8888</p>
    <p>WhatsApp: 11987654321</p>
    
    <h3>Redes Sociais</h3>
    <a href="https://www.facebook.com/techcorp">Facebook</a>
    <a href="https://www.linkedin.com/company/techcorp">LinkedIn</a>
    <a href="https://github.com/techcorp">GitHub</a>
    
    <img src="equipe.jpg" alt="Nossa equipe">
    <img src="escritorio.jpg" alt="Escritório">
</body>
</html>
\\\"\\\"\\\"

# Demonstração
scraper = WebScraper()

print("=== WEB SCRAPING COM REGEX ===\\n")

# Meta informações
meta = scraper.extract_meta_info(html_sample)
print("1. META INFORMAÇÕES:")
for key, value in meta.items():
    print(f"   {key.title()}: {value}")

# Informações de contato
contatos = scraper.extract_contact_info(html_sample)
print("\\n2. INFORMAÇÕES DE CONTATO:")
for tipo, lista in contatos.items():
    if lista:
        print(f"   {tipo.title()}: {', '.join(lista)}")

# Redes sociais
social = scraper.extract_social_links(html_sample)
print("\\n3. REDES SOCIAIS:")
for plataforma, links in social.items():
    print(f"   {plataforma.title()}: {', '.join(links)}")

# Preços
precos = scraper.extract_price_info(html_sample)
print("\\n4. PREÇOS ENCONTRADOS:")
for preco in precos:
    print(f"   Valor: R$ {preco['value']}")

# Estrutura da página
estrutura = scraper.analyze_page_structure(html_sample)
print("\\n5. ESTRUTURA DA PÁGINA:")
for elemento, qtd in estrutura.items():
    if qtd > 0:
        print(f"   {elemento.replace('_', ' ').title()}: {qtd}")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Web scraping com regex")
        else:
            print("\n" + "="*50)
            print("WEB SCRAPING COM REGEX:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _processamento_logs_avancado(self):
        """Processamento avançado de logs"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 PROCESSAMENTO AVANÇADO DE LOGS")
        
        print("🔍 Análise profissional de logs de sistema:")
        
        codigo = '''import re
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Optional, NamedTuple

class LogEntry(NamedTuple):
    """Estrutura para entrada de log"""
    timestamp: str
    level: str
    source: str
    message: str
    ip: Optional[str] = None
    user: Optional[str] = None

class AdvancedLogProcessor:
    """Processador avançado de logs"""
    
    def __init__(self):
        # Patterns para diferentes tipos de log
        self.patterns = {
            'apache': re.compile(r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - ([^\\s]+) \\[([^\\]]+)\\] "(\\w+) ([^"]+) HTTP/[^"]*" (\\d{3}) (\\d+)'),
            'syslog': re.compile(r'(\\w{3}\\s+\\d{1,2}\\s+\\d{2}:\\d{2}:\\d{2}) ([^\\s]+) ([^\\s]+): (.+)'),
            'application': re.compile(r'(\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}) \\[(\\w+)\\] ([^:]+): (.+)'),
            'nginx': re.compile(r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - - \\[([^\\]]+)\\] "(\\w+) ([^"]+) HTTP/[^"]*" (\\d{3}) (\\d+) "([^"]*)" "([^"]*)"'),
            'python': re.compile(r'(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2},\\d{3}) - ([^\\s]+) - (\\w+) - (.+)')
        }
        
        # Patterns para detecção de ataques
        self.security_patterns = {
            'sql_injection': re.compile(r'(union|select|insert|update|delete|drop|exec|script)', re.IGNORECASE),
            'xss_attempt': re.compile(r'(<script|javascript:|onload=|onerror=)', re.IGNORECASE),
            'path_traversal': re.compile(r'(\\.\\./|\\.\\.\\\\)'),
            'command_injection': re.compile(r'(;\\s*(cat|ls|pwd|whoami|id)\\s)', re.IGNORECASE),
            'brute_force': re.compile(r'(login|auth|password).*fail', re.IGNORECASE)
        }
    
    def parse_log_line(self, line: str, log_type: str = 'auto') -> Optional[LogEntry]:
        """Parse linha de log baseado no tipo"""
        if log_type == 'auto':
            # Tenta detectar automaticamente o tipo
            for log_format, pattern in self.patterns.items():
                match = pattern.search(line)
                if match:
                    log_type = log_format
                    break
        
        if log_type in self.patterns:
            match = self.patterns[log_type].search(line)
            if match:
                groups = match.groups()
                
                if log_type == 'apache':
                    return LogEntry(
                        timestamp=groups[2],
                        level='INFO',
                        source='apache',
                        message=f"{groups[3]} {groups[4]} - {groups[5]}",
                        ip=groups[0],
                        user=groups[1] if groups[1] != '-' else None
                    )
                elif log_type == 'application':
                    return LogEntry(
                        timestamp=groups[0],
                        level=groups[1],
                        source=groups[2],
                        message=groups[3]
                    )
        
        return None
    
    def detect_security_threats(self, log_text: str) -> Dict[str, List[str]]:
        """Detecta ameaças de segurança nos logs"""
        threats = defaultdict(list)
        
        for line in log_text.split('\\n'):
            if not line.strip():
                continue
                
            for threat_type, pattern in self.security_patterns.items():
                if pattern.search(line):
                    threats[threat_type].append(line.strip())
        
        return dict(threats)
    
    def analyze_traffic_patterns(self, log_text: str) -> Dict[str, any]:
        """Analisa padrões de tráfego"""
        ips = []
        user_agents = []
        methods = []
        status_codes = []
        
        for line in log_text.split('\\n'):
            # Apache/Nginx log format
            apache_match = self.patterns['apache'].search(line)
            nginx_match = self.patterns['nginx'].search(line)
            
            if apache_match:
                ips.append(apache_match.group(1))
                methods.append(apache_match.group(4))
                status_codes.append(int(apache_match.group(6)))
            elif nginx_match:
                ips.append(nginx_match.group(1))
                methods.append(nginx_match.group(3))
                status_codes.append(int(nginx_match.group(5)))
                user_agents.append(nginx_match.group(8))
        
        return {
            'total_requests': len(ips),
            'unique_ips': len(set(ips)),
            'top_ips': Counter(ips).most_common(5),
            'methods': dict(Counter(methods)),
            'status_codes': dict(Counter(status_codes)),
            'error_rate': sum(1 for code in status_codes if code >= 400) / len(status_codes) * 100 if status_codes else 0
        }
    
    def extract_error_patterns(self, log_text: str) -> Dict[str, List[str]]:
        """Extrai padrões de erro comuns"""
        error_patterns = {
            'database_errors': re.compile(r'.*(database|mysql|postgres|connection).*error', re.IGNORECASE),
            'memory_errors': re.compile(r'.*(memory|heap|stack overflow)', re.IGNORECASE),
            'timeout_errors': re.compile(r'.*(timeout|timed out)', re.IGNORECASE),
            'permission_errors': re.compile(r'.*(permission|access denied|forbidden)', re.IGNORECASE),
            'file_errors': re.compile(r'.*(file not found|no such file)', re.IGNORECASE)
        }
        
        errors = defaultdict(list)
        for line in log_text.split('\\n'):
            if not line.strip():
                continue
                
            for error_type, pattern in error_patterns.items():
                if pattern.search(line):
                    errors[error_type].append(line.strip())
        
        return dict(errors)

# Simulação de logs de diferentes sistemas
sample_logs = \\\"\\\"\\\"
192.168.1.100 - - [10/Jan/2024:08:30:15 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.101 - - [10/Jan/2024:08:31:20 +0000] "POST /login HTTP/1.1" 200 512
192.168.1.102 - - [10/Jan/2024:08:32:10 +0000] "GET /admin.php HTTP/1.1" 404 256
192.168.1.103 - - [10/Jan/2024:08:33:05 +0000] "GET /index.php?id=1' UNION SELECT * FROM users-- HTTP/1.1" 500 128
192.168.1.104 - - [10/Jan/2024:08:34:30 +0000] "GET /../../../etc/passwd HTTP/1.1" 403 64
2024-01-10 08:35:15 [ERROR] database: Connection timeout after 30 seconds
2024-01-10 08:36:20 [WARNING] auth: Failed login attempt for user admin
2024-01-10 08:37:10 [INFO] app: User john.doe logged in successfully
192.168.1.105 - - [10/Jan/2024:08:38:25 +0000] "GET /search?q=<script>alert('xss')</script> HTTP/1.1" 400 256
\\\"\\\"\\\"

# Demonstração
processor = AdvancedLogProcessor()

print("=== PROCESSAMENTO AVANÇADO DE LOGS ===\\n")

# 1. Análise de padrões de tráfego
traffic = processor.analyze_traffic_patterns(sample_logs)
print("1. ANÁLISE DE TRÁFEGO:")
print(f"   Total de requisições: {traffic['total_requests']}")
print(f"   IPs únicos: {traffic['unique_ips']}")
print(f"   Taxa de erro: {traffic['error_rate']:.1f}%")
print(f"   Métodos HTTP: {traffic['methods']}")
print(f"   Top IPs: {dict(traffic['top_ips'][:3])}")

# 2. Detecção de ameaças
threats = processor.detect_security_threats(sample_logs)
print("\\n2. AMEAÇAS DETECTADAS:")
for threat_type, occurrences in threats.items():
    print(f"   {threat_type.replace('_', ' ').title()}: {len(occurrences)} ocorrência(s)")

# 3. Padrões de erro
errors = processor.extract_error_patterns(sample_logs)
print("\\n3. PADRÕES DE ERRO:")
for error_type, error_lines in errors.items():
    if error_lines:
        print(f"   {error_type.replace('_', ' ').title()}: {len(error_lines)} erro(s)")

print("\\n💡 APLICAÇÕES PRÁTICAS:")
print("   • Monitoramento de segurança em tempo real")
print("   • Detecção de anomalias de tráfego")
print("   • Análise forense de incidentes")
print("   • Otimização de performance")
print("   • Compliance e auditoria")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Processamento avançado de logs")
        else:
            print("\n" + "="*50)
            print("PROCESSAMENTO AVANÇADO DE LOGS:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _busca_substituicao(self):
        """Busca e substituição avançada"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔄 BUSCA E SUBSTITUIÇÃO")
        
        print("✏️ Usando regex para buscar e substituir:")
        
        codigo = '''import re

texto = """
João Silva nasceu em 25/12/1990 e mora na Rua A, 123.
Maria Santos nasceu em 15/08/1985 e mora na Av. B, 456.
Pedro Costa nasceu em 30/03/1992 e mora na Rua C, 789.
"""

print("TEXTO ORIGINAL:")
print(texto)

# 1. Ocultar datas
texto_sem_datas = re.sub(r"\\d{2}/\\d{2}/\\d{4}", "XX/XX/XXXX", texto)
print("\\n1. DATAS OCULTAS:")
print(texto_sem_datas)

# 2. Padronizar telefones
texto_telefones = "Contatos: 11999998888, (21) 88888-7777, 31 77777-6666"
telefones_padronizados = re.sub(r"\\(?\\d{2}\\)?\\s?(\\d{4,5})-?(\\d{4})", r"(\\1) \\2", texto_telefones)
print("\\n2. TELEFONES PADRONIZADOS:")
print(telefones_padronizados)

# 3. Extrair e reformatar emails
texto_emails = "Contatos: joao@empresa.com, maria.santos@teste.org, pedro123@exemplo.net"
def formatar_email(match):
    email = match.group()
    usuario, dominio = email.split('@')
    return f"[{usuario.upper()}]@{dominio}"

emails_formatados = re.sub(r"\\w+@\\w+\\.\\w+", formatar_email, texto_emails)
print("\\n3. EMAILS FORMATADOS:")
print(emails_formatados)

# 4. Mascarar CPFs
texto_cpfs = "CPFs: 123.456.789-00, 987.654.321-11, 555.444.333-22"
cpfs_mascarados = re.sub(r"(\\d{3})\\.(\\d{3})\\.(\\d{3})-(\\d{2})", r"***.***.***-\\4", texto_cpfs)
print("\\n4. CPFS MASCARADOS:")
print(cpfs_mascarados)'''
        
        if self.ui:
            self.ui.code_block(codigo, "Busca e substituição")
        else:
            print("\n" + "="*50)
            print("BUSCA E SUBSTITUIÇÃO:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_regex_avancado(self):
        """Mini projeto avançado: Sistema completo de análise de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO AVANÇADO: SISTEMA DE ANÁLISE DE DADOS")
        
        print("🔍 Vamos criar um sistema completo de análise de dados!")
        print("🎯 Funcionalidades profissionais:")
        print("• Processamento de logs de múltiplos formatos")
        print("• Detecção automática de ameaças de segurança")
        print("• Web scraping de informações corporativas")
        print("• Parsing de dados estruturados (CSV, JSON, configs)")
        print("• Análise de padrões e geração de relatórios")
        print("• Dashboard com métricas em tempo real")
        
        input("\n🔸 Pressione ENTER para começar o projeto...")
        
        codigo = '''import re
from collections import Counter, defaultdict
from datetime import datetime

# Simulando logs de um servidor web
logs = """
192.168.1.100 - - [10/Jan/2024:08:30:15 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.101 - - [10/Jan/2024:08:31:20 +0000] "POST /login HTTP/1.1" 200 512
192.168.1.102 - - [10/Jan/2024:08:32:10 +0000] "GET /admin.php HTTP/1.1" 404 256
192.168.1.100 - - [10/Jan/2024:08:33:05 +0000] "GET /products.html HTTP/1.1" 200 2048
192.168.1.103 - - [10/Jan/2024:08:34:30 +0000] "GET /api/users HTTP/1.1" 500 128
192.168.1.101 - - [10/Jan/2024:08:35:15 +0000] "DELETE /user/123 HTTP/1.1" 200 64
192.168.1.102 - - [10/Jan/2024:08:36:20 +0000] "GET /backup.zip HTTP/1.1" 404 256
192.168.1.104 - - [10/Jan/2024:08:37:10 +0000] "GET /dashboard HTTP/1.1" 200 1536
"""

class LogAnalyzer:
    def __init__(self):
        # Padrão regex para logs Apache/Nginx
        self.log_pattern = r'(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}) - - \\[([^\\]]+)\\] "(\\w+) ([^"]+) HTTP/[^"]*" (\\d{3}) (\\d+)'
        
    def parse_logs(self, log_text):
        """Extrai informações dos logs"""
        matches = re.findall(self.log_pattern, log_text)
        parsed_logs = []
        
        for match in matches:
            ip, timestamp, method, url, status, size = match
            parsed_logs.append({
                'ip': ip,
                'timestamp': timestamp,
                'method': method,
                'url': url,
                'status': int(status),
                'size': int(size)
            })
        
        return parsed_logs
    
    def analyze(self, log_text):
        """Analisa os logs e gera relatório"""
        parsed = self.parse_logs(log_text)
        
        # Contadores
        ip_counter = Counter([log['ip'] for log in parsed])
        method_counter = Counter([log['method'] for log in parsed])
        status_counter = Counter([log['status'] for log in parsed])
        
        # Erros específicos
        errors_404 = [log for log in parsed if log['status'] == 404]
        errors_500 = [log for log in parsed if log['status'] == 500]
        
        # Total de bytes transferidos
        total_bytes = sum([log['size'] for log in parsed])
        
        return {
            'total_requests': len(parsed),
            'unique_ips': len(ip_counter),
            'top_ips': ip_counter.most_common(5),
            'methods': dict(method_counter),
            'status_codes': dict(status_counter),
            'errors_404': len(errors_404),
            'errors_500': len(errors_500),
            'total_bytes': total_bytes,
            'parsed_logs': parsed
        }
    
    def generate_report(self, analysis):
        """Gera relatório formatado"""
        print("\\n" + "="*50)
        print("     RELATÓRIO DE ANÁLISE DE LOGS")
        print("="*50)
        
        print(f"📊 Total de requisições: {analysis['total_requests']}")
        print(f"🔗 IPs únicos: {analysis['unique_ips']}")
        print(f"📈 Total de bytes: {analysis['total_bytes']:,}")
        
        print("\\n🔝 TOP IPs:")
        for ip, count in analysis['top_ips']:
            print(f"   • {ip}: {count} requisições")
        
        print("\\n📋 Métodos HTTP:")
        for method, count in analysis['methods'].items():
            print(f"   • {method}: {count}")
        
        print("\\n📊 Códigos de Status:")
        for status, count in analysis['status_codes'].items():
            print(f"   • {status}: {count}")
        
        print(f"\\n❌ Erros encontrados:")
        print(f"   • 404 (Não encontrado): {analysis['errors_404']}")
        print(f"   • 500 (Erro servidor): {analysis['errors_500']}")
        
        # Análise de segurança básica
        print("\\n🔒 Análise de Segurança:")
        suspicious_urls = [log for log in analysis['parsed_logs'] 
                          if re.search(r'\\.(php|jsp|asp)$', log['url']) and log['status'] == 404]
        if suspicious_urls:
            print(f"   ⚠️  {len(suspicious_urls)} tentativas de acesso suspeitas detectadas")
        else:
            print("   ✅ Nenhuma atividade suspeita detectada")

# Executar análise
analyzer = LogAnalyzer()
analysis = analyzer.analyze(logs)
analyzer.generate_report(analysis)

print("\\n🎉 Projeto concluído!")
print("💡 Você pode expandir este projeto para:")
print("   • Ler logs de arquivos reais")
print("   • Detectar ataques (SQL injection, XSS)")
print("   • Gerar gráficos de atividade")
print("   • Criar alertas em tempo real")'''
        
        if self.ui:
            self.ui.code_block(codigo, "Analisador de Logs")
        else:
            print("\n" + "="*50)
            print("MINI PROJETO - ANALISADOR DE LOGS:")
            print("="*50)
            print(codigo)
        
        try:
            exec(codigo)
        except Exception as e:
            print(f"❌ Erro na execução: {e}")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema Avançado de Análise de Dados com Regex")
        
        input("\n🔸 Pressione ENTER para finalizar o módulo...")