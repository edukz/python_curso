#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 30: Segurança
Aprenda criptografia, validação, autenticação e boas práticas de segurança
"""

from ..shared.base_module import BaseModule


class Modulo30Seguranca(BaseModule):
    """Módulo 30: Segurança - Programação Segura e Proteção de Dados"""
    
    def __init__(self):
        super().__init__("modulo_30", "Segurança")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre segurança"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._seguranca()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _seguranca(self) -> None:
        """Conteúdo principal sobre segurança"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛡️ MÓDULO 30: SEGURANÇA")
        else:
            print("\n" + "="*50)
            print("🛡️ MÓDULO 30: SEGURANÇA")
            print("="*50)
        
        print("🛡️ Segurança é FUNDAMENTAL no desenvolvimento moderno!")
        print("🔒 Proteger dados e sistemas é responsabilidade do programador!")
        
        print("\n═══════════════════════════════════════════════")
        print("        PRINCÍPIOS DE SEGURANÇA")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Princípios fundamentais:")
        print("• 🔒 Confidencialidade - dados protegidos")
        print("• 🔧 Integridade - dados não alterados")
        print("• 🌐 Disponibilidade - sistema acessível")
        print("• 🎫 Autenticação - verificar identidade")
        print("• 🔑 Autorização - controlar acesso")
        print("• 📝 Auditoria - registrar atividades")
        
        self.pausar()
        
        print("\n🔐 Criptografia e Hash:")
        
        codigo1 = '''# Criptografia e hash seguros
import hashlib
import secrets
import hmac
import base64
from typing import Tuple, Optional

class CryptographyManager:
    """Gerenciador de criptografia segura"""
    
    def __init__(self):
        self.pepper = "sistema_pepper_secreto_2024"  # Adicional ao salt
    
    def generate_salt(self, length: int = 32) -> str:
        """Gera salt criptograficamente seguro"""
        return secrets.token_hex(length)
    
    def hash_password(self, password: str, salt: str = None) -> Tuple[str, str]:
        """
        Cria hash seguro da senha usando PBKDF2
        
        Args:
            password: Senha em texto claro
            salt: Salt opcional (gera novo se não fornecido)
            
        Returns:
            Tuple com (hash, salt)
        """
        if salt is None:
            salt = self.generate_salt()
        
        # Combinar senha com pepper para segurança adicional
        password_with_pepper = password + self.pepper
        
        # PBKDF2 com 100.000 iterações (padrão OWASP)
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            password_with_pepper.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 100k iterações
        )
        
        # Converter para base64 para armazenamento
        password_hash = base64.b64encode(hash_obj).decode('utf-8')
        
        return password_hash, salt
    
    def verify_password(self, password: str, stored_hash: str, salt: str) -> bool:
        """
        Verifica se senha está correta
        
        Args:
            password: Senha a verificar
            stored_hash: Hash armazenado
            salt: Salt usado na criação do hash
            
        Returns:
            True se senha está correta
        """
        # Gerar hash da senha fornecida
        computed_hash, _ = self.hash_password(password, salt)
        
        # Comparação segura contra timing attacks
        return hmac.compare_digest(computed_hash, stored_hash)
    
    def generate_secure_token(self, length: int = 32) -> str:
        """Gera token criptograficamente seguro"""
        return secrets.token_urlsafe(length)
    
    def generate_api_key(self) -> str:
        """Gera chave de API segura"""
        prefix = "sk_"  # Prefixo identificador
        key_part = secrets.token_urlsafe(32)
        return f"{prefix}{key_part}"
    
    def hash_data(self, data: str, algorithm: str = 'sha256') -> str:
        """
        Cria hash de dados genéricos
        
        Args:
            data: Dados para hash
            algorithm: Algoritmo (sha256, sha512, etc.)
            
        Returns:
            Hash em hexadecimal
        """
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(data.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def verify_data_integrity(self, data: str, expected_hash: str, 
                            algorithm: str = 'sha256') -> bool:
        """Verifica integridade de dados"""
        computed_hash = self.hash_data(data, algorithm)
        return hmac.compare_digest(computed_hash, expected_hash)

class SecureSession:
    """Gerenciador de sessões seguras"""
    
    def __init__(self):
        self.sessions = {}  # session_id -> session_data
        self.crypto = CryptographyManager()
    
    def create_session(self, user_id: int, user_data: dict = None) -> str:
        """Cria sessão segura"""
        session_id = self.crypto.generate_secure_token()
        
        session_data = {
            'user_id': user_id,
            'created_at': time.time(),
            'last_accessed': time.time(),
            'user_data': user_data or {},
            'csrf_token': self.crypto.generate_secure_token(16),
            'expires_at': time.time() + 86400  # 24 horas
        }
        
        self.sessions[session_id] = session_data
        return session_id
    
    def validate_session(self, session_id: str) -> Optional[dict]:
        """Valida e atualiza sessão"""
        if session_id not in self.sessions:
            return None
        
        session = self.sessions[session_id]
        current_time = time.time()
        
        # Verificar expiração
        if current_time > session['expires_at']:
            del self.sessions[session_id]
            return None
        
        # Atualizar último acesso
        session['last_accessed'] = current_time
        
        return session
    
    def invalidate_session(self, session_id: str) -> bool:
        """Invalida sessão"""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

# Demonstração de criptografia
print("=== CRIPTOGRAFIA E HASH SEGUROS ===")
print()

crypto = CryptographyManager()

# 1. Hash de senhas
print("🔐 HASH DE SENHAS:")
senha_original = "minha_senha_super_secreta_123!"
hash_senha, salt = crypto.hash_password(senha_original)

print(f"Senha original: {senha_original}")
print(f"Salt gerado: {salt}")
print(f"Hash seguro: {hash_senha}")

# Verificar senha
print(f"\\nVerificação senha correta: {crypto.verify_password(senha_original, hash_senha, salt)}")
print(f"Verificação senha incorreta: {crypto.verify_password('senha_errada', hash_senha, salt)}")

print()

# 2. Tokens seguros
print("🎫 TOKENS SEGUROS:")
token = crypto.generate_secure_token()
api_key = crypto.generate_api_key()

print(f"Token seguro: {token}")
print(f"API Key: {api_key}")

print()

# 3. Hash de dados
print("📄 HASH DE DADOS:")
dados_importantes = "Dados confidenciais do sistema"
hash_dados = crypto.hash_data(dados_importantes)

print(f"Dados: {dados_importantes}")
print(f"Hash SHA256: {hash_dados}")
print(f"Integridade verificada: {crypto.verify_data_integrity(dados_importantes, hash_dados)}")

print()

# 4. Sessões seguras
print("👤 SESSÕES SEGURAS:")
session_mgr = SecureSession()

# Criar sessão
user_id = 123
session_id = session_mgr.create_session(user_id, {"role": "admin", "permissions": ["read", "write"]})
print(f"Sessão criada: {session_id}")

# Validar sessão
session_data = session_mgr.validate_session(session_id)
if session_data:
    print(f"Sessão válida para usuário: {session_data['user_id']}")
    print(f"CSRF Token: {session_data['csrf_token']}")

import time  # Importação necessária para o código

print("\\n✅ Sistema de criptografia implementado!")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n🔍 Validação e Sanitização:")
        
        codigo2 = '''# Validação e sanitização de dados
import re
import html
import urllib.parse
from typing import Dict, List, Any, Union
import ipaddress

class InputValidator:
    """Validador de entrada de dados"""
    
    def __init__(self):
        # Padrões de validação
        self.patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
            'phone_br': r'^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$',
            'cpf': r'^\\d{3}\\.?\\d{3}\\.?\\d{3}-?\\d{2}$',
            'cnpj': r'^\\d{2}\\.?\\d{3}\\.?\\d{3}/?\\d{4}-?\\d{2}$',
            'url': r'^https?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(?:/.*)?$',
            'username': r'^[a-zA-Z0-9_-]{3,20}$',
            'strong_password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$',
            'uuid': r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            'hex_color': r'^#?([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})$',
            'credit_card': r'^\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}$'
        }
        
        # Lista de palavras perigosas para SQL injection
        self.sql_keywords = [
            'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'CREATE',
            'ALTER', 'EXEC', 'EXECUTE', 'SCRIPT', 'UNION', 'TRUNCATE'
        ]
        
        # Lista de tags HTML perigosas
        self.dangerous_html_tags = [
            'script', 'iframe', 'object', 'embed', 'form', 'input',
            'button', 'link', 'meta', 'style', 'base'
        ]
    
    def validate_email(self, email: str) -> Dict[str, Any]:
        """Valida formato de email"""
        if not email or not isinstance(email, str):
            return {"valid": False, "error": "Email is required"}
        
        email = email.strip().lower()
        
        if len(email) > 254:  # RFC 5321 limit
            return {"valid": False, "error": "Email too long"}
        
        if re.match(self.patterns['email'], email):
            return {"valid": True, "sanitized": email}
        else:
            return {"valid": False, "error": "Invalid email format"}
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Valida força da senha"""
        if not password or not isinstance(password, str):
            return {"valid": False, "error": "Password is required"}
        
        result = {
            "valid": False,
            "score": 0,
            "criteria": {
                "length": len(password) >= 8,
                "uppercase": bool(re.search(r'[A-Z]', password)),
                "lowercase": bool(re.search(r'[a-z]', password)),
                "numbers": bool(re.search(r'\\d', password)),
                "special": bool(re.search(r'[@$!%*?&]', password)),
                "no_common": password.lower() not in ['password', '123456', 'qwerty', 'abc123']
            },
            "suggestions": []
        }
        
        # Calcular pontuação
        result["score"] = sum(result["criteria"].values())
        
        # Gerar sugestões
        if not result["criteria"]["length"]:
            result["suggestions"].append("Use pelo menos 8 caracteres")
        if not result["criteria"]["uppercase"]:
            result["suggestions"].append("Adicione pelo menos uma letra maiúscula")
        if not result["criteria"]["lowercase"]:
            result["suggestions"].append("Adicione pelo menos uma letra minúscula")
        if not result["criteria"]["numbers"]:
            result["suggestions"].append("Adicione pelo menos um número")
        if not result["criteria"]["special"]:
            result["suggestions"].append("Adicione pelo menos um caractere especial (@$!%*?&)")
        if not result["criteria"]["no_common"]:
            result["suggestions"].append("Evite senhas comuns")
        
        result["valid"] = result["score"] >= 5
        result["strength"] = "Forte" if result["score"] >= 5 else "Média" if result["score"] >= 3 else "Fraca"
        
        return result
    
    def validate_cpf(self, cpf: str) -> Dict[str, Any]:
        """Valida CPF brasileiro"""
        if not cpf or not isinstance(cpf, str):
            return {"valid": False, "error": "CPF is required"}
        
        # Remover caracteres não numéricos
        cpf_clean = re.sub(r'[^0-9]', '', cpf)
        
        if len(cpf_clean) != 11:
            return {"valid": False, "error": "CPF must have 11 digits"}
        
        # Verificar se todos os dígitos são iguais
        if cpf_clean == cpf_clean[0] * 11:
            return {"valid": False, "error": "Invalid CPF"}
        
        # Calcular primeiro dígito verificador
        soma = sum(int(cpf_clean[i]) * (10 - i) for i in range(9))
        resto = 11 - (soma % 11)
        digito1 = 0 if resto >= 10 else resto
        
        # Calcular segundo dígito verificador
        soma = sum(int(cpf_clean[i]) * (11 - i) for i in range(10))
        resto = 11 - (soma % 11)
        digito2 = 0 if resto >= 10 else resto
        
        # Verificar dígitos
        if cpf_clean[9] == str(digito1) and cpf_clean[10] == str(digito2):
            # Formatar CPF
            cpf_formatted = f"{cpf_clean[:3]}.{cpf_clean[3:6]}.{cpf_clean[6:9]}-{cpf_clean[9:]}"
            return {"valid": True, "sanitized": cpf_formatted}
        else:
            return {"valid": False, "error": "Invalid CPF"}
    
    def validate_ip_address(self, ip: str) -> Dict[str, Any]:
        """Valida endereço IP"""
        if not ip or not isinstance(ip, str):
            return {"valid": False, "error": "IP address is required"}
        
        try:
            ip_obj = ipaddress.ip_address(ip.strip())
            
            result = {
                "valid": True,
                "sanitized": str(ip_obj),
                "version": ip_obj.version,
                "is_private": ip_obj.is_private,
                "is_loopback": ip_obj.is_loopback,
                "is_multicast": ip_obj.is_multicast
            }
            
            # Verificar se é endereço potencialmente perigoso
            if ip_obj.is_loopback or ip_obj.is_multicast:
                result["warning"] = "Special use IP address"
            
            return result
            
        except ValueError:
            return {"valid": False, "error": "Invalid IP address format"}
    
    def sanitize_html(self, text: str) -> str:
        """Remove/escapa HTML perigoso"""
        if not text or not isinstance(text, str):
            return ""
        
        # Escapar caracteres HTML
        sanitized = html.escape(text)
        
        # Remover tags perigosas (caso alguém tente burlar)
        for tag in self.dangerous_html_tags:
            pattern = rf'</?{tag}[^>]*>'
            sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
        
        return sanitized
    
    def sanitize_sql(self, text: str) -> str:
        """Sanitiza entrada para prevenir SQL injection"""
        if not text or not isinstance(text, str):
            return ""
        
        # Escapar aspas
        sanitized = text.replace("'", "''").replace('"', '""')
        
        # Verificar palavras-chave perigosas
        text_upper = sanitized.upper()
        for keyword in self.sql_keywords:
            if keyword in text_upper:
                # Adicionar underscore para quebrar a palavra-chave
                sanitized = sanitized.replace(keyword, f"{keyword}_")
                sanitized = sanitized.replace(keyword.lower(), f"{keyword.lower()}_")
        
        return sanitized
    
    def validate_file_upload(self, filename: str, content_type: str, 
                           file_size: int) -> Dict[str, Any]:
        """Valida upload de arquivo"""
        result = {
            "valid": False,
            "errors": [],
            "warnings": []
        }
        
        # Extensões permitidas
        allowed_extensions = {
            'image': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
            'document': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
            'archive': ['.zip', '.rar', '.tar', '.gz']
        }
        
        # Verificar nome do arquivo
        if not filename or '..' in filename or '/' in filename or '\\\\' in filename:
            result["errors"].append("Invalid filename")
            return result
        
        # Verificar extensão
        file_ext = '.' + filename.split('.')[-1].lower() if '.' in filename else ''
        valid_ext = any(file_ext in exts for exts in allowed_extensions.values())
        
        if not valid_ext:
            result["errors"].append("File type not allowed")
        
        # Verificar tamanho (10MB max)
        max_size = 10 * 1024 * 1024  # 10MB
        if file_size > max_size:
            result["errors"].append("File too large (max 10MB)")
        
        # Verificar content-type
        safe_content_types = [
            'image/jpeg', 'image/png', 'image/gif', 'image/webp',
            'application/pdf', 'text/plain', 'application/zip'
        ]
        
        if content_type not in safe_content_types:
            result["warnings"].append("Content-type not in safe list")
        
        result["valid"] = len(result["errors"]) == 0
        result["sanitized_filename"] = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
        
        return result

class SecurityScanner:
    """Scanner de segurança para código e dados"""
    
    def __init__(self):
        self.validator = InputValidator()
    
    def scan_user_input(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Escaneia entrada do usuário"""
        results = {
            "safe": True,
            "violations": [],
            "sanitized_data": {}
        }
        
        for field, value in data.items():
            if not isinstance(value, str):
                results["sanitized_data"][field] = value
                continue
            
            # Verificar XSS
            if '<script' in value.lower() or 'javascript:' in value.lower():
                results["violations"].append({
                    "field": field,
                    "type": "XSS_ATTEMPT",
                    "value": value[:50] + "..." if len(value) > 50 else value
                })
                results["safe"] = False
            
            # Verificar SQL injection
            sql_patterns = [
                r"'\\s*(or|and)\\s*'",
                r"union\\s+select",
                r"drop\\s+table",
                r"insert\\s+into",
                r"delete\\s+from"
            ]
            
            for pattern in sql_patterns:
                if re.search(pattern, value, re.IGNORECASE):
                    results["violations"].append({
                        "field": field,
                        "type": "SQL_INJECTION_ATTEMPT",
                        "pattern": pattern
                    })
                    results["safe"] = False
            
            # Sanitizar dados
            results["sanitized_data"][field] = self.validator.sanitize_html(value)
        
        return results
    
    def generate_security_report(self, scan_results: List[Dict]) -> Dict[str, Any]:
        """Gera relatório de segurança"""
        total_scans = len(scan_results)
        safe_scans = len([r for r in scan_results if r["safe"]])
        
        violation_types = {}
        for result in scan_results:
            for violation in result["violations"]:
                v_type = violation["type"]
                violation_types[v_type] = violation_types.get(v_type, 0) + 1
        
        return {
            "summary": {
                "total_scans": total_scans,
                "safe_scans": safe_scans,
                "unsafe_scans": total_scans - safe_scans,
                "safety_rate": (safe_scans / total_scans * 100) if total_scans > 0 else 0
            },
            "violation_types": violation_types,
            "recommendations": self._generate_recommendations(violation_types)
        }
    
    def _generate_recommendations(self, violations: Dict[str, int]) -> List[str]:
        """Gera recomendações de segurança"""
        recommendations = []
        
        if violations.get("XSS_ATTEMPT", 0) > 0:
            recommendations.append("Implementar CSP (Content Security Policy)")
            recommendations.append("Validar e escapar todas as entradas do usuário")
        
        if violations.get("SQL_INJECTION_ATTEMPT", 0) > 0:
            recommendations.append("Usar prepared statements/parametrized queries")
            recommendations.append("Implementar validação rigorosa de entrada")
        
        if not violations:
            recommendations.append("Manter práticas de segurança atuais")
        
        return recommendations

# Demonstração de validação e sanitização
print("=== VALIDAÇÃO E SANITIZAÇÃO ===")
print()

validator = InputValidator()
scanner = SecurityScanner()

# 1. Validação de email
print("📧 VALIDAÇÃO DE EMAIL:")
emails_teste = [
    "usuario@exemplo.com",
    "email_invalido",
    "teste@dominio",
    "usuario.nome+tag@empresa.com.br"
]

for email in emails_teste:
    resultado = validator.validate_email(email)
    status = "✅" if resultado["valid"] else "❌"
    print(f"  {status} {email}: {resultado.get('error', 'Válido')}")

print()

# 2. Validação de senha
print("🔐 VALIDAÇÃO DE SENHA:")
senhas_teste = [
    "123456",
    "senha",
    "MinhaSenh@123",
    "SuperSenhaForte2024!"
]

for senha in senhas_teste:
    resultado = validator.validate_password(senha)
    print(f"  Senha: {'*' * len(senha)}")
    print(f"    Força: {resultado['strength']} (Score: {resultado['score']}/6)")
    if resultado['suggestions']:
        print(f"    Sugestões: {', '.join(resultado['suggestions'])}")
    print()

# 3. Validação de CPF
print("🆔 VALIDAÇÃO DE CPF:")
cpfs_teste = [
    "111.444.777-35",
    "123.456.789-00",
    "11144477735",
    "000.000.000-00"
]

for cpf in cpfs_teste:
    resultado = validator.validate_cpf(cpf)
    status = "✅" if resultado["valid"] else "❌"
    print(f"  {status} {cpf}: {resultado.get('error', resultado.get('sanitized', 'Válido'))}")

print()

# 4. Scanner de segurança
print("🔍 SCANNER DE SEGURANÇA:")
dados_teste = [
    {"nome": "João Silva", "email": "joao@exemplo.com"},
    {"busca": "<script>alert('XSS')</script>", "filtro": "categoria"},
    {"sql": "'; DROP TABLE users; --", "id": "123"},
    {"comentario": "Comentário normal", "rating": "5"}
]

scan_results = []
for i, dados in enumerate(dados_teste, 1):
    resultado = scanner.scan_user_input(dados)
    status = "✅ Seguro" if resultado["safe"] else "❌ Perigoso"
    print(f"  Scan {i}: {status}")
    
    if not resultado["safe"]:
        for violation in resultado["violations"]:
            print(f"    ⚠️ {violation['type']} no campo '{violation['field']}'")
    
    scan_results.append(resultado)

# 5. Relatório de segurança
print("\\n📊 RELATÓRIO DE SEGURANÇA:")
relatorio = scanner.generate_security_report(scan_results)

print(f"  Total de scans: {relatorio['summary']['total_scans']}")
print(f"  Scans seguros: {relatorio['summary']['safe_scans']}")
print(f"  Taxa de segurança: {relatorio['summary']['safety_rate']:.1f}%")

if relatorio['violation_types']:
    print("  Violações encontradas:")
    for tipo, count in relatorio['violation_types'].items():
        print(f"    • {tipo}: {count}")

print("  Recomendações:")
for rec in relatorio['recommendations']:
    print(f"    • {rec}")

print("\\n✅ Sistema de validação implementado!")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🛡️ Proteção Contra Ataques:")
        
        codigo3 = r'''# Proteção contra ataques comuns
import time
import json
import hashlib
from typing import Dict, List, Set, Optional
from collections import defaultdict, deque
from datetime import datetime, timedelta

class AttackDetector:
    """Detector de ataques em tempo real"""
    
    def __init__(self):
        # Configurações de detecção
        self.brute_force_threshold = 5  # tentativas por minuto
        self.ddos_threshold = 100  # requests por minuto
        self.rate_limit_window = 60  # janela em segundos
        
        # Armazenamento de tentativas
        self.login_attempts = defaultdict(deque)  # IP -> tentativas
        self.request_counts = defaultdict(deque)  # IP -> requests
        self.blocked_ips = set()  # IPs bloqueados
        self.suspicious_patterns = []  # Padrões suspeitos detectados
        
        # Honeypots
        self.honeypot_paths = ['/admin', '/wp-admin', '/phpmyadmin', '/.env']
        self.honeypot_hits = defaultdict(int)
    
    def detect_brute_force(self, ip: str, success: bool = False) -> Dict[str, any]:
        """Detecta ataques de força bruta"""
        current_time = time.time()
        
        # Limpar tentativas antigas
        while (self.login_attempts[ip] and 
               current_time - self.login_attempts[ip][0] > self.rate_limit_window):
            self.login_attempts[ip].popleft()
        
        # Adicionar nova tentativa (apenas falhas)
        if not success:
            self.login_attempts[ip].append(current_time)
        else:
            # Limpar tentativas em caso de sucesso
            self.login_attempts[ip].clear()
        
        attempts_count = len(self.login_attempts[ip])
        
        # Verificar threshold
        if attempts_count >= self.brute_force_threshold:
            self.blocked_ips.add(ip)
            self.suspicious_patterns.append({
                "type": "BRUTE_FORCE",
                "ip": ip,
                "attempts": attempts_count,
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "threat_detected": True,
                "threat_type": "BRUTE_FORCE",
                "ip": ip,
                "attempts": attempts_count,
                "action": "IP_BLOCKED"
            }
        
        return {
            "threat_detected": False,
            "attempts": attempts_count,
            "remaining": self.brute_force_threshold - attempts_count
        }
    
    def detect_ddos(self, ip: str) -> Dict[str, any]:
        """Detecta ataques DDoS"""
        current_time = time.time()
        
        # Limpar requests antigos
        while (self.request_counts[ip] and 
               current_time - self.request_counts[ip][0] > self.rate_limit_window):
            self.request_counts[ip].popleft()
        
        # Adicionar nova request
        self.request_counts[ip].append(current_time)
        requests_count = len(self.request_counts[ip])
        
        # Verificar threshold
        if requests_count >= self.ddos_threshold:
            self.blocked_ips.add(ip)
            self.suspicious_patterns.append({
                "type": "DDOS",
                "ip": ip,
                "requests": requests_count,
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "threat_detected": True,
                "threat_type": "DDOS",
                "ip": ip,
                "requests": requests_count,
                "action": "IP_BLOCKED"
            }
        
        return {
            "threat_detected": False,
            "requests": requests_count,
            "limit": self.ddos_threshold
        }
    
    def detect_honeypot_access(self, ip: str, path: str) -> Dict[str, any]:
        """Detecta acesso a honeypots"""
        if path in self.honeypot_paths:
            self.honeypot_hits[ip] += 1
            self.blocked_ips.add(ip)
            
            self.suspicious_patterns.append({
                "type": "HONEYPOT_ACCESS",
                "ip": ip,
                "path": path,
                "total_hits": self.honeypot_hits[ip],
                "timestamp": datetime.now().isoformat()
            })
            
            return {
                "threat_detected": True,
                "threat_type": "HONEYPOT_ACCESS",
                "ip": ip,
                "path": path,
                "action": "IP_BLOCKED"
            }
        
        return {"threat_detected": False}
    
    def is_ip_blocked(self, ip: str) -> bool:
        """Verifica se IP está bloqueado"""
        return ip in self.blocked_ips
    
    def unblock_ip(self, ip: str) -> bool:
        """Desbloqueia IP"""
        if ip in self.blocked_ips:
            self.blocked_ips.remove(ip)
            return True
        return False
    
    def get_threat_summary(self) -> Dict[str, any]:
        """Gera resumo de ameaças"""
        threat_counts = defaultdict(int)
        for pattern in self.suspicious_patterns:
            threat_counts[pattern["type"]] += 1
        
        return {
            "total_threats": len(self.suspicious_patterns),
            "blocked_ips": len(self.blocked_ips),
            "threat_types": dict(threat_counts),
            "recent_threats": self.suspicious_patterns[-10:],  # Últimas 10
            "top_attackers": list(self.blocked_ips)[:10]  # Top 10 IPs
        }

class WAF:
    """Web Application Firewall simulado"""
    
    def __init__(self):
        self.attack_detector = AttackDetector()
        
        # Regras de firewall
        self.xss_patterns = [
            r'<script[^>]*>.*?</script>',
            r'javascript:',
            r'on\w+\s*=',
            r'<iframe[^>]*>',
            r'eval\s*\\(',
            r'expression\s*\\('
        ]
        
        self.sqli_patterns = [
            r"'\\s*(or|and)\\s*'",
            r'\\bunion\\b.*\\bselect\\b',
            r'\\bdrop\\b.*\\btable\\b',
            r'\\binsert\\b.*\\binto\\b',
            r'\\bdelete\\b.*\\bfrom\\b',
            r'\\bupdate\\b.*\\bset\\b',
            r'--|#|/\\*'
        ]
        
        self.lfi_patterns = [
            r'\\.\\./',
            r'/etc/passwd',
            r'/etc/shadow',
            r'\\bfile:///',
            r'\\.\\.\\\\',
            r'/windows/system32'
        ]
        
        # Whitelist de IPs confiáveis
        self.whitelist_ips = {
            '127.0.0.1',
            '::1',
            '10.0.0.0/8',
            '192.168.0.0/16'
        }
    
    def analyze_request(self, request_data: Dict[str, any]) -> Dict[str, any]:
        """Analisa requisição HTTP"""
        ip = request_data.get('ip', '127.0.0.1')
        path = request_data.get('path', '/')
        headers = request_data.get('headers', {})
        body = request_data.get('body', {})
        
        analysis_result = {
            "allowed": True,
            "threats": [],
            "score": 0,
            "actions": []
        }
        
        # 1. Verificar IP bloqueado
        if self.attack_detector.is_ip_blocked(ip):
            analysis_result["allowed"] = False
            analysis_result["threats"].append("BLOCKED_IP")
            analysis_result["actions"].append("REQUEST_BLOCKED")
            return analysis_result
        
        # 2. Detectar DDoS
        ddos_result = self.attack_detector.detect_ddos(ip)
        if ddos_result["threat_detected"]:
            analysis_result["allowed"] = False
            analysis_result["threats"].append("DDOS")
            analysis_result["actions"].append("IP_BLOCKED")
            analysis_result["score"] += 100
        
        # 3. Detectar acesso a honeypot
        honeypot_result = self.attack_detector.detect_honeypot_access(ip, path)
        if honeypot_result["threat_detected"]:
            analysis_result["allowed"] = False
            analysis_result["threats"].append("HONEYPOT_ACCESS")
            analysis_result["actions"].append("IP_BLOCKED")
            analysis_result["score"] += 100
        
        # 4. Analisar payload para XSS
        all_data = json.dumps(body) + ' ' + json.dumps(headers)
        for pattern in self.xss_patterns:
            if re.search(pattern, all_data, re.IGNORECASE):
                analysis_result["threats"].append("XSS_ATTEMPT")
                analysis_result["score"] += 50
        
        # 5. Analisar payload para SQL Injection
        for pattern in self.sqli_patterns:
            if re.search(pattern, all_data, re.IGNORECASE):
                analysis_result["threats"].append("SQL_INJECTION")
                analysis_result["score"] += 75
        
        # 6. Analisar payload para LFI (Local File Inclusion)
        for pattern in self.lfi_patterns:
            if re.search(pattern, all_data, re.IGNORECASE):
                analysis_result["threats"].append("LFI_ATTEMPT")
                analysis_result["score"] += 60
        
        # 7. Verificar User-Agent suspeito
        user_agent = headers.get('User-Agent', '').lower()
        suspicious_agents = ['sqlmap', 'nmap', 'burp', 'nikto', 'metasploit']
        if any(agent in user_agent for agent in suspicious_agents):
            analysis_result["threats"].append("SUSPICIOUS_USER_AGENT")
            analysis_result["score"] += 30
        
        # Decidir se bloquear
        if analysis_result["score"] >= 50:
            analysis_result["allowed"] = False
            analysis_result["actions"].append("REQUEST_BLOCKED")
        
        return analysis_result
    
    def generate_security_log(self, request_data: Dict, analysis: Dict) -> Dict:
        """Gera log de segurança"""
        return {
            "timestamp": datetime.now().isoformat(),
            "ip": request_data.get('ip'),
            "path": request_data.get('path'),
            "method": request_data.get('method', 'GET'),
            "user_agent": request_data.get('headers', {}).get('User-Agent', ''),
            "allowed": analysis["allowed"],
            "threats": analysis["threats"],
            "risk_score": analysis["score"],
            "actions": analysis["actions"]
        }

class SecurityMonitor:
    """Monitor de segurança em tempo real"""
    
    def __init__(self):
        self.waf = WAF()
        self.security_logs = []
        self.alert_threshold = 10  # Score mínimo para alerta
        self.alerts = []
    
    def process_request(self, request_data: Dict) -> Dict:
        """Processa requisição através do WAF"""
        analysis = self.waf.analyze_request(request_data)
        
        # Gerar log
        log_entry = self.waf.generate_security_log(request_data, analysis)
        self.security_logs.append(log_entry)
        
        # Gerar alerta se necessário
        if analysis["score"] >= self.alert_threshold:
            alert = {
                "timestamp": datetime.now().isoformat(),
                "severity": "HIGH" if analysis["score"] >= 75 else "MEDIUM",
                "ip": request_data.get('ip'),
                "threats": analysis["threats"],
                "score": analysis["score"],
                "description": f"High risk request from {request_data.get('ip')}"
            }
            self.alerts.append(alert)
        
        return analysis
    
    def get_security_dashboard(self) -> Dict:
        """Gera dashboard de segurança"""
        # Estatísticas gerais
        total_requests = len(self.security_logs)
        blocked_requests = len([log for log in self.security_logs if not log["allowed"]])
        
        # Contagem de ameaças
        threat_counts = defaultdict(int)
        for log in self.security_logs:
            for threat in log["threats"]:
                threat_counts[threat] += 1
        
        # IPs mais atacantes
        ip_counts = defaultdict(int)
        for log in self.security_logs:
            if not log["allowed"]:
                ip_counts[log["ip"]] += 1
        
        top_attackers = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "overview": {
                "total_requests": total_requests,
                "blocked_requests": blocked_requests,
                "success_rate": ((total_requests - blocked_requests) / total_requests * 100) if total_requests > 0 else 0,
                "total_alerts": len(self.alerts),
                "active_threats": len(self.waf.attack_detector.blocked_ips)
            },
            "threats": dict(threat_counts),
            "top_attackers": top_attackers,
            "recent_alerts": self.alerts[-5:],
            "blocked_ips": list(self.waf.attack_detector.blocked_ips)
        }

# Demonstração de proteção contra ataques
print("=== PROTEÇÃO CONTRA ATAQUES ===")
print()

# Inicializar monitor de segurança
monitor = SecurityMonitor()

print("🛡️ WAF (Web Application Firewall) inicializado!")
print()

# Simular diferentes tipos de requisições
requests_teste = [
    {
        "ip": "192.168.1.100",
        "path": "/login",
        "method": "POST",
        "headers": {"User-Agent": "Mozilla/5.0"},
        "body": {"username": "admin", "password": "123456"}
    },
    {
        "ip": "10.0.0.50",
        "path": "/search",
        "method": "GET",
        "headers": {"User-Agent": "Mozilla/5.0"},
        "body": {"q": "<script>alert('XSS')</script>"}
    },
    {
        "ip": "203.0.113.15",
        "path": "/users",
        "method": "GET", 
        "headers": {"User-Agent": "sqlmap/1.0"},
        "body": {"id": "1'; DROP TABLE users; --"}
    },
    {
        "ip": "198.51.100.10",
        "path": "/admin",
        "method": "GET",
        "headers": {"User-Agent": "Nikto"},
        "body": {}
    },
    {
        "ip": "192.168.1.200",
        "path": "/file",
        "method": "GET",
        "headers": {"User-Agent": "Mozilla/5.0"},
        "body": {"path": "../../etc/passwd"}
    }
]

print("🧪 TESTANDO REQUISIÇÕES:")
for i, request in enumerate(requests_teste, 1):
    print(f"\\nRequisição {i}: {request['method']} {request['path']}")
    print(f"IP: {request['ip']}")
    
    # Processar através do WAF
    analysis = monitor.process_request(request)
    
    status = "✅ PERMITIDA" if analysis["allowed"] else "❌ BLOQUEADA"
    print(f"Status: {status}")
    print(f"Score de risco: {analysis['score']}")
    
    if analysis["threats"]:
        print(f"Ameaças detectadas: {', '.join(analysis['threats'])}")
    
    if analysis["actions"]:
        print(f"Ações tomadas: {', '.join(analysis['actions'])}")

# Simular ataques de força bruta
print("\\n🔨 SIMULANDO ATAQUE DE FORÇA BRUTA:")
attacker_ip = "203.0.113.50"

for i in range(7):  # Mais que o threshold de 5
    brute_force_result = monitor.waf.attack_detector.detect_brute_force(attacker_ip, success=False)
    
    if brute_force_result["threat_detected"]:
        print(f"  Tentativa {i+1}: ❌ AMEAÇA DETECTADA - IP {attacker_ip} bloqueado!")
        break
    else:
        remaining = brute_force_result["remaining"]
        print(f"  Tentativa {i+1}: {brute_force_result['attempts']} tentativas ({remaining} restantes)")

# Dashboard de segurança
print("\\n📊 DASHBOARD DE SEGURANÇA:")
dashboard = monitor.get_security_dashboard()

print(f"  📈 Total de requisições: {dashboard['overview']['total_requests']}")
print(f"  🛡️ Requisições bloqueadas: {dashboard['overview']['blocked_requests']}")
print(f"  ✅ Taxa de sucesso: {dashboard['overview']['success_rate']:.1f}%")
print(f"  🚨 Total de alertas: {dashboard['overview']['total_alerts']}")

if dashboard['threats']:
    print("\\n  🎯 Ameaças detectadas:")
    for threat, count in dashboard['threats'].items():
        print(f"    • {threat}: {count}")

if dashboard['top_attackers']:
    print("\\n  👹 Top atacantes:")
    for ip, count in dashboard['top_attackers']:
        print(f"    • {ip}: {count} ataques")

if dashboard['blocked_ips']:
    print(f"\\n  🚫 IPs bloqueados: {len(dashboard['blocked_ips'])}")

print("\\n✅ Sistema de proteção implementado!")
print("🎯 Proteções ativas:")
print("  • Detecção de força bruta")
print("  • Proteção contra DDoS")
print("  • Detecção de XSS")
print("  • Proteção contra SQL Injection")
print("  • Detecção de LFI")
print("  • Honeypots")
print("  • Monitoramento em tempo real")

import re  # Importação necessária para o código'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Qual algoritmo é recomendado para hash de senhas?",
            ["PBKDF2", "bcrypt", "scrypt"],
            "PBKDF2, bcrypt ou scrypt são algoritmos seguros para hash de senhas"
        )
        
        # Mini Projeto do Módulo 30
        self._mini_projeto_security_center()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_security_center(self) -> None:
        """Mini Projeto - Módulo 30: Centro de Segurança Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: CENTRO DE SEGURANÇA COMPLETO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: CENTRO DE SEGURANÇA COMPLETO")
            print("="*50)
        
        print("🛡️ Sistema completo de segurança com monitoramento em tempo real!")
        print("🛠️ Usando: Criptografia, WAF, IDS, Auditoria, Machine Learning")
        
        self.pausar()
        
        codigo_projeto = '''# 🛡️ CENTRO DE SEGURANÇA COMPLETO
# Sistema integrado de segurança para aplicações Python

import hashlib
import secrets
import time
import json
import re
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Set, Optional, Any, Callable
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from enum import Enum
import sqlite3
from contextlib import contextmanager

# ===============================================
# SISTEMA DE CRIPTOGRAFIA AVANÇADO
# ===============================================

class CryptoSuite:
    """Suite completa de criptografia"""
    
    def __init__(self, master_key: str = None):
        self.master_key = master_key or self._generate_master_key()
        self.pepper = "SecureApp2024_GlobalPepper_!@#$%"
    
    def _generate_master_key(self) -> str:
        """Gera chave mestra do sistema"""
        return secrets.token_urlsafe(64)
    
    def hash_password_advanced(self, password: str, salt: str = None, 
                             iterations: int = 120000) -> Dict[str, str]:
        """Hash avançado de senha com múltiplas camadas"""
        if salt is None:
            salt = secrets.token_hex(32)
        
        # Camada 1: Combinar com pepper
        password_peppered = password + self.pepper
        
        # Camada 2: PBKDF2 com alta iteração
        hash1 = hashlib.pbkdf2_hmac(
            'sha256',
            password_peppered.encode(),
            salt.encode(),
            iterations
        )
        
        # Camada 3: SHA-512 adicional com salt rotacionado
        rotated_salt = salt[16:] + salt[:16]  # Rotacionar salt
        hash2 = hashlib.sha512(hash1 + rotated_salt.encode()).digest()
        
        # Camada 4: Aplicar chave mestra
        final_hash = hashlib.sha256(hash2 + self.master_key.encode()).hexdigest()
        
        return {
            "hash": final_hash,
            "salt": salt,
            "iterations": iterations,
            "algorithm": "PBKDF2-SHA256-Multi",
            "created_at": datetime.now().isoformat()
        }
    
    def verify_password_advanced(self, password: str, stored_data: Dict[str, str]) -> bool:
        """Verifica senha com hash avançado"""
        computed = self.hash_password_advanced(
            password, 
            stored_data["salt"],
            stored_data["iterations"]
        )
        
        return secrets.compare_digest(computed["hash"], stored_data["hash"])
    
    def encrypt_data(self, data: str, key: str = None) -> Dict[str, str]:
        """Criptografia simétrica de dados (simulada)"""
        if key is None:
            key = self.master_key
        
        # Simulação de AES (em produção usar cryptography library)
        salt = secrets.token_hex(16)
        combined_key = hashlib.sha256((key + salt).encode()).hexdigest()
        
        # "Criptografar" usando XOR simples (apenas para demonstração)
        encrypted = ""
        for i, char in enumerate(data):
            key_char = combined_key[i % len(combined_key)]
            encrypted += chr(ord(char) ^ ord(key_char))
        
        encrypted_b64 = secrets.token_urlsafe(len(data))  # Simulação
        
        return {
            "encrypted": encrypted_b64,
            "salt": salt,
            "algorithm": "AES-256-GCM",
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_secure_token(self, purpose: str = "general", 
                            expiry_hours: int = 24) -> Dict[str, Any]:
        """Gera token seguro com propósito específico"""
        token_data = {
            "token": secrets.token_urlsafe(48),
            "purpose": purpose,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(hours=expiry_hours),
            "used": False
        }
        
        # Assinar token com HMAC
        token_string = f"{token_data['token']}{purpose}{token_data['created_at'].isoformat()}"
        signature = hmac.new(
            self.master_key.encode(),
            token_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
        token_data["signature"] = signature
        return token_data
    
    def validate_token(self, token_data: Dict[str, Any]) -> bool:
        """Valida token com verificação de assinatura"""
        if token_data.get("used", False):
            return False
        
        if datetime.now() > token_data["expires_at"]:
            return False
        
        # Verificar assinatura
        token_string = f"{token_data['token']}{token_data['purpose']}{token_data['created_at'].isoformat()}"
        expected_signature = hmac.new(
            self.master_key.encode(),
            token_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return secrets.compare_digest(token_data["signature"], expected_signature)

# ===============================================
# SISTEMA DE DETECÇÃO DE INTRUSÃO (IDS)
# ===============================================

class SecurityEvent(Enum):
    LOGIN_ATTEMPT = "login_attempt"
    LOGIN_SUCCESS = "login_success"
    LOGIN_FAILURE = "login_failure"
    PERMISSION_DENIED = "permission_denied"
    DATA_ACCESS = "data_access"
    SYSTEM_COMMAND = "system_command"
    FILE_ACCESS = "file_access"
    NETWORK_REQUEST = "network_request"

@dataclass
class SecurityLog:
    timestamp: datetime
    event_type: SecurityEvent
    user_id: Optional[str]
    ip_address: str
    user_agent: str
    resource: str
    action: str
    success: bool
    risk_score: int
    additional_data: Dict[str, Any]

class AdvancedIDS:
    """Sistema de Detecção de Intrusão Avançado"""
    
    def __init__(self):
        self.logs: List[SecurityLog] = []
        self.anomaly_thresholds = {
            "login_failures": 5,
            "permission_denials": 3,
            "unusual_hours": (22, 6),  # 22:00 às 06:00
            "multiple_ips": 3,
            "rapid_requests": 50  # requests por minuto
        }
        
        # Padrões comportamentais por usuário
        self.user_profiles = defaultdict(lambda: {
            "usual_ips": set(),
            "usual_hours": defaultdict(int),
            "usual_resources": defaultdict(int),
            "last_activity": None
        })
        
        # Machine Learning simples para detecção
        self.ml_features = defaultdict(list)
        
    def log_event(self, event_type: SecurityEvent, user_id: str, ip_address: str,
                  user_agent: str, resource: str, action: str, success: bool,
                  additional_data: Dict = None) -> SecurityLog:
        """Registra evento de segurança"""
        
        # Calcular score de risco
        risk_score = self._calculate_risk_score(
            event_type, user_id, ip_address, resource, success
        )
        
        log_entry = SecurityLog(
            timestamp=datetime.now(),
            event_type=event_type,
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
            resource=resource,
            action=action,
            success=success,
            risk_score=risk_score,
            additional_data=additional_data or {}
        )
        
        self.logs.append(log_entry)
        
        # Atualizar perfil do usuário
        if user_id:
            self._update_user_profile(user_id, log_entry)
        
        # Detectar anomalias
        anomalies = self._detect_anomalies(log_entry)
        
        # Gerar alertas se necessário
        if anomalies:
            self._generate_alerts(log_entry, anomalies)
        
        return log_entry
    
    def _calculate_risk_score(self, event_type: SecurityEvent, user_id: str,
                            ip_address: str, resource: str, success: bool) -> int:
        """Calcula score de risco do evento"""
        score = 0
        
        # Score base por tipo de evento
        base_scores = {
            SecurityEvent.LOGIN_FAILURE: 20,
            SecurityEvent.PERMISSION_DENIED: 30,
            SecurityEvent.SYSTEM_COMMAND: 40,
            SecurityEvent.LOGIN_SUCCESS: 5,
            SecurityEvent.DATA_ACCESS: 10,
            SecurityEvent.FILE_ACCESS: 15,
            SecurityEvent.NETWORK_REQUEST: 5
        }
        
        score += base_scores.get(event_type, 10)
        
        # Penalizar falhas
        if not success:
            score += 15
        
        # Verificar IP conhecido
        if user_id and ip_address not in self.user_profiles[user_id]["usual_ips"]:
            score += 25
        
        # Verificar horário incomum
        current_hour = datetime.now().hour
        unusual_start, unusual_end = self.anomaly_thresholds["unusual_hours"]
        if unusual_start <= current_hour or current_hour <= unusual_end:
            score += 10
        
        # Verificar recursos sensíveis
        sensitive_resources = ["/admin", "/api/system", "/config", "/users"]
        if any(sensitive in resource for sensitive in sensitive_resources):
            score += 20
        
        return min(score, 100)  # Máximo 100
    
    def _update_user_profile(self, user_id: str, log_entry: SecurityLog):
        """Atualiza perfil comportamental do usuário"""
        profile = self.user_profiles[user_id]
        
        # Atualizar IPs usuais
        profile["usual_ips"].add(log_entry.ip_address)
        
        # Atualizar horários usuais
        hour = log_entry.timestamp.hour
        profile["usual_hours"][hour] += 1
        
        # Atualizar recursos usuais
        profile["usual_resources"][log_entry.resource] += 1
        
        # Atualizar última atividade
        profile["last_activity"] = log_entry.timestamp
        
        # Limitar tamanho dos perfis
        if len(profile["usual_ips"]) > 10:
            profile["usual_ips"] = set(list(profile["usual_ips"])[-10:])
    
    def _detect_anomalies(self, log_entry: SecurityLog) -> List[str]:
        """Detecta anomalias comportamentais"""
        anomalies = []
        
        # 1. Múltiplas falhas de login
        if log_entry.event_type == SecurityEvent.LOGIN_FAILURE:
            recent_failures = len([
                log for log in self.logs[-50:]  # Últimos 50 eventos
                if (log.event_type == SecurityEvent.LOGIN_FAILURE and
                    log.ip_address == log_entry.ip_address and
                    (log_entry.timestamp - log.timestamp).seconds < 300)  # 5 minutos
            ])
            
            if recent_failures >= self.anomaly_thresholds["login_failures"]:
                anomalies.append("MULTIPLE_LOGIN_FAILURES")
        
        # 2. Atividade em horário incomum
        hour = log_entry.timestamp.hour
        unusual_start, unusual_end = self.anomaly_thresholds["unusual_hours"]
        if unusual_start <= hour or hour <= unusual_end:
            if log_entry.user_id:
                usual_hours = self.user_profiles[log_entry.user_id]["usual_hours"]
                if usual_hours[hour] < 2:  # Menos de 2 atividades neste horário
                    anomalies.append("UNUSUAL_HOUR_ACTIVITY")
        
        # 3. Novo IP para usuário
        if (log_entry.user_id and 
            log_entry.ip_address not in self.user_profiles[log_entry.user_id]["usual_ips"]):
            anomalies.append("NEW_IP_ADDRESS")
        
        # 4. Múltiplos IPs para mesmo usuário
        if log_entry.user_id:
            recent_ips = set([
                log.ip_address for log in self.logs[-20:]
                if (log.user_id == log_entry.user_id and
                    (log_entry.timestamp - log.timestamp).seconds < 3600)  # 1 hora
            ])
            
            if len(recent_ips) >= self.anomaly_thresholds["multiple_ips"]:
                anomalies.append("MULTIPLE_IP_ADDRESSES")
        
        # 5. Requests muito rápidos
        rapid_requests = len([
            log for log in self.logs[-100:]
            if (log.ip_address == log_entry.ip_address and
                (log_entry.timestamp - log.timestamp).seconds < 60)  # 1 minuto
        ])
        
        if rapid_requests >= self.anomaly_thresholds["rapid_requests"]:
            anomalies.append("RAPID_REQUESTS")
        
        return anomalies
    
    def _generate_alerts(self, log_entry: SecurityLog, anomalies: List[str]):
        """Gera alertas de segurança"""
        for anomaly in anomalies:
            alert = {
                "timestamp": datetime.now().isoformat(),
                "severity": self._get_alert_severity(anomaly),
                "type": anomaly,
                "user_id": log_entry.user_id,
                "ip_address": log_entry.ip_address,
                "resource": log_entry.resource,
                "description": self._get_alert_description(anomaly),
                "risk_score": log_entry.risk_score
            }
            
            # Em produção, enviaria para sistema de alertas
            print(f"🚨 ALERTA DE SEGURANÇA: {alert['severity']} - {alert['description']}")
    
    def _get_alert_severity(self, anomaly: str) -> str:
        """Determina severidade do alerta"""
        high_severity = ["MULTIPLE_LOGIN_FAILURES", "MULTIPLE_IP_ADDRESSES"]
        medium_severity = ["UNUSUAL_HOUR_ACTIVITY", "RAPID_REQUESTS"]
        
        if anomaly in high_severity:
            return "HIGH"
        elif anomaly in medium_severity:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _get_alert_description(self, anomaly: str) -> str:
        """Gera descrição do alerta"""
        descriptions = {
            "MULTIPLE_LOGIN_FAILURES": "Múltiplas tentativas de login falharam",
            "UNUSUAL_HOUR_ACTIVITY": "Atividade em horário incomum detectada",
            "NEW_IP_ADDRESS": "Acesso de novo endereço IP",
            "MULTIPLE_IP_ADDRESSES": "Usuário acessando de múltiplos IPs",
            "RAPID_REQUESTS": "Número excessivo de requests detectado"
        }
        return descriptions.get(anomaly, "Anomalia de segurança detectada")
    
    def get_security_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Gera resumo de segurança"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        recent_logs = [log for log in self.logs if log.timestamp > cutoff_time]
        
        # Estatísticas gerais
        total_events = len(recent_logs)
        failed_events = len([log for log in recent_logs if not log.success])
        high_risk_events = len([log for log in recent_logs if log.risk_score >= 50])
        
        # Top IPs por atividade
        ip_activity = defaultdict(int)
        for log in recent_logs:
            ip_activity[log.ip_address] += 1
        
        top_ips = sorted(ip_activity.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Eventos por tipo
        event_types = defaultdict(int)
        for log in recent_logs:
            event_types[log.event_type.value] += 1
        
        return {
            "period_hours": hours,
            "summary": {
                "total_events": total_events,
                "failed_events": failed_events,
                "success_rate": ((total_events - failed_events) / total_events * 100) if total_events > 0 else 0,
                "high_risk_events": high_risk_events,
                "risk_percentage": (high_risk_events / total_events * 100) if total_events > 0 else 0
            },
            "top_ips": top_ips,
            "event_types": dict(event_types),
            "active_users": len(set(log.user_id for log in recent_logs if log.user_id))
        }
'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Centro de Segurança completo criado!")
        print("🎯 Aplicação real: empresas, governo, sistemas críticos")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Centro de Segurança Completo")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo30Seguranca()
    print("Teste do módulo 30 - versão standalone")
    module._seguranca()

