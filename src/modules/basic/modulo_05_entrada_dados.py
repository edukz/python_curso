#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 5: Entrada de Dados - VERSÃO MELHORADA
Aprenda validação robusta, tratamento de erros e boas práticas modernas
"""

import re
from typing import Union, Optional, Callable, List
from ..shared.base_module import BaseModule


class Modulo05EntradaDados(BaseModule):
    """Módulo 5: Entrada de Dados - Validação e Tratamento Profissional"""
    
    def __init__(self):
        super().__init__("modulo_5", "Entrada de Dados Profissional")
        self.has_mini_project = True
        self.mini_project_points = 75  # Aumentado de 50 para 75
    
    def execute(self) -> None:
        """Executa o módulo sobre entrada de dados"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._entrada_dados_moderna()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _entrada_dados_moderna(self) -> None:
        """Conteúdo principal sobre entrada de dados moderna"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📝 MÓDULO 5: ENTRADA DE DADOS PROFISSIONAL")
        else:
            print("\n" + "="*60)
            print("📝 MÓDULO 5: ENTRADA DE DADOS PROFISSIONAL")
            print("="*60)
        
        print("🚀 Aprenda validação robusta e tratamento de erros profissional!")
        print("🎯 Tópicos avançados:")
        print("• Validação de entrada com regex")
        print("• Tratamento de exceções")
        print("• Sanitização de dados")
        print("• Type hints e validação de tipos")
        print("• Patterns de validação (email, telefone, CPF)")
        print("• Sistema de retry automático")
        
        self._conceitos_basicos()
        self._validacao_robusta()
        self._tratamento_excecoes()
        self._sanitizacao_dados()
        self._patterns_validacao()
        self._sistema_validacao_avancado()
        self._mini_projeto_cadastro_completo()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _conceitos_basicos(self):
        """Conceitos básicos melhorados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📚 CONCEITOS BÁSICOS MODERNOS")
        
        print("🔍 Input básico vs Input profissional:")
        
        print("\n❌ Forma básica (problemática):")
        codigo_basico = '''
# Problemático - sem validação
nome = input("Nome: ")
idade = int(input("Idade: "))  # Pode crashar!
email = input("Email: ")       # Sem validação!
'''
        
        print(codigo_basico)
        
        print("\n✅ Forma profissional:")
        codigo_profissional = '''
from typing import Optional

def input_seguro(prompt: str, tipo: type = str, validador: Optional[callable] = None) -> any:
    """Input com validação e tratamento de erros"""
    while True:
        try:
            valor = input(prompt).strip()
            
            # Conversão de tipo
            if tipo != str:
                valor = tipo(valor)
            
            # Validação customizada
            if validador and not validador(valor):
                print("❌ Valor inválido. Tente novamente.")
                continue
                
            return valor
            
        except ValueError as e:
            print(f"❌ Erro: {e}. Tente novamente.")
        except KeyboardInterrupt:
            print("\\n⚠️ Operação cancelada pelo usuário.")
            return None

# Uso profissional
def validar_idade(idade: int) -> bool:
    return 0 <= idade <= 150

nome = input_seguro("Nome: ", str, lambda x: len(x.strip()) > 0)
idade = input_seguro("Idade: ", int, validar_idade)
print(f"✅ Dados válidos: {nome}, {idade} anos")
'''
        
        print(codigo_profissional)
    
    def _validacao_robusta(self):
        """Validação robusta de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛡️ VALIDAÇÃO ROBUSTA")
        
        print("🔒 Sistema de validação por camadas:")
        
        codigo_validacao = '''
import re
from typing import Union, List

class ValidadorDados:
    """Sistema profissional de validação de dados"""
    
    @staticmethod
    def validar_nome(nome: str) -> tuple[bool, str]:
        """Valida nome com regras específicas"""
        nome = nome.strip()
        
        if not nome:
            return False, "Nome não pode estar vazio"
        
        if len(nome) < 2:
            return False, "Nome deve ter pelo menos 2 caracteres"
        
        if len(nome) > 100:
            return False, "Nome muito longo (máximo 100 caracteres)"
        
        if not re.match(r"^[a-zA-ZÀ-ÿ\\s]+$", nome):
            return False, "Nome deve conter apenas letras e espaços"
        
        return True, "✅ Nome válido"
    
    @staticmethod
    def validar_idade(idade: Union[str, int]) -> tuple[bool, str]:
        """Valida idade com diferentes tipos de entrada"""
        try:
            idade_int = int(idade)
            
            if idade_int < 0:
                return False, "Idade não pode ser negativa"
            
            if idade_int > 150:
                return False, "Idade deve ser menor que 150 anos"
            
            if idade_int > 100:
                return True, "⚠️ Idade muito alta, mas válida"
            
            return True, "✅ Idade válida"
            
        except ValueError:
            return False, "Idade deve ser um número inteiro"
    
    @staticmethod
    def validar_email(email: str) -> tuple[bool, str]:
        """Validação completa de email"""
        email = email.strip().lower()
        
        if not email:
            return False, "Email não pode estar vazio"
        
        # Regex profissional para email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        
        if not re.match(pattern, email):
            return False, "Formato de email inválido"
        
        # Validações adicionais
        local, domain = email.split('@')
        
        if len(local) > 64:
            return False, "Parte local do email muito longa"
        
        if len(domain) > 255:
            return False, "Domínio do email muito longo"
        
        # Verificar domínios suspeitos (exemplo)
        dominios_temporarios = ['tempmail.org', '10minutemail.com']
        if any(temp in domain for temp in dominios_temporarios):
            return True, "⚠️ Email temporário detectado, mas válido"
        
        return True, "✅ Email válido"

# Demonstração de uso
def input_com_validacao(prompt: str, validador: callable) -> str:
    """Input com validação automática"""
    max_tentativas = 3
    tentativa = 0
    
    while tentativa < max_tentativas:
        valor = input(f"{prompt}")
        valido, mensagem = validador(valor)
        
        print(mensagem)
        
        if valido:
            return valor
        
        tentativa += 1
        if tentativa < max_tentativas:
            print(f"Tentativa {tentativa + 1} de {max_tentativas}")
    
    raise ValueError("Número máximo de tentativas excedido")

# Exemplo de uso
try:
    nome = input_com_validacao("Nome completo: ", ValidadorDados.validar_nome)
    idade = input_com_validacao("Idade: ", ValidadorDados.validar_idade)
    email = input_com_validacao("Email: ", ValidadorDados.validar_email)
    
    print("\\n🎉 Todos os dados foram validados com sucesso!")
    print(f"Nome: {nome.title()}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    
except ValueError as e:
    print(f"❌ Erro na validação: {e}")
'''
        
        print(codigo_validacao)
    
    def _tratamento_excecoes(self):
        """Tratamento profissional de exceções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚠️ TRATAMENTO PROFISSIONAL DE EXCEÇÕES")
        
        print("🛠️ Lidar com erros de forma elegante:")
        
        codigo_excecoes = '''
import logging
from typing import Optional, Any, Dict

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InputHandler:
    """Manipulador profissional de entrada com logging"""
    
    def __init__(self):
        self.tentativas = {}
        self.max_tentativas = 3
    
    def input_com_retry(self, 
                       prompt: str, 
                       tipo: type = str,
                       validador: Optional[callable] = None,
                       mensagem_erro: str = "Entrada inválida") -> Optional[Any]:
        """
        Input com sistema de retry automático e logging
        """
        campo = prompt.strip().rstrip(':').lower()
        
        if campo not in self.tentativas:
            self.tentativas[campo] = 0
        
        while self.tentativas[campo] < self.max_tentativas:
            try:
                # Capturar entrada
                valor_str = input(f"{prompt} ")
                
                # Log da tentativa
                logger.info(f"Tentativa de entrada para '{campo}': {len(valor_str)} chars")
                
                # Tratar entrada vazia
                if not valor_str.strip() and tipo != str:
                    raise ValueError("Entrada não pode estar vazia")
                
                # Conversão de tipo
                if tipo == str:
                    valor = valor_str.strip()
                else:
                    valor = tipo(valor_str.strip())
                
                # Validação customizada
                if validador:
                    if callable(validador):
                        if not validador(valor):
                            raise ValueError(mensagem_erro)
                    elif hasattr(validador, '__contains__'):
                        if valor not in validador:
                            raise ValueError(f"Valor deve ser um de: {list(validador)}")
                
                # Sucesso - resetar tentativas
                self.tentativas[campo] = 0
                logger.info(f"Entrada válida para '{campo}': {valor}")
                
                return valor
                
            except ValueError as e:
                self.tentativas[campo] += 1
                tentativas_restantes = self.max_tentativas - self.tentativas[campo]
                
                logger.warning(f"Erro na entrada '{campo}': {e}")
                
                print(f"❌ {e}")
                
                if tentativas_restantes > 0:
                    print(f"🔄 Tentativas restantes: {tentativas_restantes}")
                else:
                    logger.error(f"Máximo de tentativas excedido para '{campo}'")
                    print("❌ Número máximo de tentativas excedido")
                    return None
                    
            except KeyboardInterrupt:
                logger.info("Operação cancelada pelo usuário")
                print("\\n⚠️ Operação cancelada pelo usuário")
                return None
            
            except EOFError:
                logger.warning("EOF detectado na entrada")
                print("\\n⚠️ Fim de entrada detectado")
                return None
        
        return None
    
    def coletar_dados_usuario(self) -> Optional[Dict[str, Any]]:
        """Coleta dados do usuário com tratamento completo de erros"""
        dados = {}
        
        print("📋 Sistema de Coleta de Dados com Validação")
        print("=" * 50)
        
        # Nome
        nome = self.input_com_retry(
            "Nome completo:",
            str,
            lambda x: len(x) >= 2 and x.replace(' ', '').isalpha(),
            "Nome deve ter pelo menos 2 caracteres e apenas letras"
        )
        if nome is None:
            return None
        dados['nome'] = nome.title()
        
        # Idade
        idade = self.input_com_retry(
            "Idade:",
            int,
            lambda x: 0 <= x <= 150,
            "Idade deve estar entre 0 e 150 anos"
        )
        if idade is None:
            return None
        dados['idade'] = idade
        
        # Sexo
        sexo = self.input_com_retry(
            "Sexo (M/F/O):",
            str,
            ['M', 'F', 'O', 'm', 'f', 'o'],
            "Sexo deve ser M, F ou O"
        )
        if sexo is None:
            return None
        dados['sexo'] = sexo.upper()
        
        print("\\n✅ Dados coletados com sucesso!")
        return dados

# Demonstração
handler = InputHandler()

print("=== DEMONSTRAÇÃO DE COLETA ROBUSTA ===")
dados_usuario = handler.coletar_dados_usuario()

if dados_usuario:
    print("\\n📊 Resumo dos dados:")
    for chave, valor in dados_usuario.items():
        print(f"  {chave.title()}: {valor}")
else:
    print("\\n❌ Falha na coleta de dados")
'''
        
        print(codigo_excecoes)
    
    def _sanitizacao_dados(self):
        """Sanitização e limpeza de dados"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧹 SANITIZAÇÃO DE DADOS")
        
        print("🔐 Limpeza e segurança de dados de entrada:")
        
        codigo_sanitizacao = '''
import html
import re
from typing import Union

class SanitizadorDados:
    """Sistema profissional de sanitização de dados"""
    
    @staticmethod
    def limpar_texto_basico(texto: str) -> str:
        """Limpeza básica de texto"""
        if not isinstance(texto, str):
            return str(texto)
        
        # Remover espaços extras
        texto = texto.strip()
        
        # Remover múltiplos espaços
        texto = re.sub(r'\\s+', ' ', texto)
        
        return texto
    
    @staticmethod
    def sanitizar_nome(nome: str) -> str:
        """Sanitização específica para nomes"""
        nome = SanitizadorDados.limpar_texto_basico(nome)
        
        # Remover caracteres especiais perigosos
        nome = re.sub(r'[<>"\\'&]', '', nome)
        
        # Capitalizar corretamente
        # Exemplo: "maria da silva" -> "Maria da Silva"
        palavras = nome.split()
        palavras_capitalizadas = []
        
        preposicoes = {'da', 'de', 'do', 'das', 'dos', 'e'}
        
        for i, palavra in enumerate(palavras):
            if i == 0 or palavra.lower() not in preposicoes:
                palavras_capitalizadas.append(palavra.capitalize())
            else:
                palavras_capitalizadas.append(palavra.lower())
        
        return ' '.join(palavras_capitalizadas)
    
    @staticmethod
    def sanitizar_email(email: str) -> str:
        """Sanitização de email"""
        email = SanitizadorDados.limpar_texto_basico(email)
        
        # Converter para minúsculo
        email = email.lower()
        
        # Remover caracteres perigosos
        email = re.sub(r'[<>"\\'&]', '', email)
        
        return email
    
    @staticmethod
    def sanitizar_telefone(telefone: str) -> str:
        """Sanitização de telefone"""
        # Remover tudo que não é número
        apenas_numeros = re.sub(r'\\D', '', telefone)
        
        # Formatação brasileira
        if len(apenas_numeros) == 11:  # Celular com 9
            return f"({apenas_numeros[:2]}) {apenas_numeros[2:7]}-{apenas_numeros[7:]}"
        elif len(apenas_numeros) == 10:  # Fixo
            return f"({apenas_numeros[:2]}) {apenas_numeros[2:6]}-{apenas_numeros[6:]}"
        else:
            return apenas_numeros
    
    @staticmethod
    def prevenir_injecao(texto: str) -> str:
        """Prevenção básica contra injeção"""
        # Escape HTML
        texto = html.escape(texto)
        
        # Remover tentativas de script
        texto = re.sub(r'<script.*?</script>', '', texto, flags=re.IGNORECASE | re.DOTALL)
        
        # Remover SQL injection básico
        padroes_sql = [
            r'(\\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER)\\b)',
            r'(--|#|/\\*|\\*/)',
            r'(\\bOR\\b.*?=.*?=)',
            r'(\\bUNION\\b.*?\\bSELECT\\b)'
        ]
        
        for padrao in padroes_sql:
            texto = re.sub(padrao, '', texto, flags=re.IGNORECASE)
        
        return texto
    
    @classmethod
    def processar_dados_completo(cls, dados_brutos: dict) -> dict:
        """Processamento completo de dados com sanitização"""
        dados_limpos = {}
        
        for chave, valor in dados_brutos.items():
            if not isinstance(valor, str):
                dados_limpos[chave] = valor
                continue
            
            # Aplicar sanitização baseada no tipo de campo
            if 'nome' in chave.lower():
                dados_limpos[chave] = cls.sanitizar_nome(valor)
            elif 'email' in chave.lower():
                dados_limpos[chave] = cls.sanitizar_email(valor)
            elif 'telefone' in chave.lower() or 'fone' in chave.lower():
                dados_limpos[chave] = cls.sanitizar_telefone(valor)
            else:
                # Sanitização geral
                valor = cls.limpar_texto_basico(valor)
                valor = cls.prevenir_injecao(valor)
                dados_limpos[chave] = valor
        
        return dados_limpos

# Demonstração
dados_problematicos = {
    'nome': '  joaO   DA    silva  ',
    'email': '  JOAO.SILVA@GMAIL.COM  ',
    'telefone': '(11) 99999-9999',
    'observacoes': '<script>alert("hack")</script>Observações normais',
    'idade': 25
}

print("📥 Dados antes da sanitização:")
for chave, valor in dados_problematicos.items():
    print(f"  {chave}: '{valor}'")

dados_limpos = SanitizadorDados.processar_dados_completo(dados_problematicos)

print("\\n🧹 Dados após sanitização:")
for chave, valor in dados_limpos.items():
    print(f"  {chave}: '{valor}'")
'''
        
        print(codigo_sanitizacao)
    
    def _patterns_validacao(self):
        """Patterns de validação comuns"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 PATTERNS DE VALIDAÇÃO BRASILEIROS")
        
        print("🇧🇷 Validadores específicos para dados brasileiros:")
        
        codigo_patterns = '''
import re
from typing import Union

class ValidadorBrasileiro:
    """Validadores específicos para dados brasileiros"""
    
    @staticmethod
    def validar_cpf(cpf: str) -> tuple[bool, str]:
        """Validação completa de CPF"""
        # Remover formatação
        cpf = re.sub(r'\\D', '', cpf)
        
        # Verificar tamanho
        if len(cpf) != 11:
            return False, "CPF deve ter 11 dígitos"
        
        # Verificar sequências inválidas
        if cpf in ['00000000000', '11111111111', '22222222222', 
                   '33333333333', '44444444444', '55555555555',
                   '66666666666', '77777777777', '88888888888', '99999999999']:
            return False, "CPF com sequência inválida"
        
        # Calcular primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        if int(cpf[9]) != digito1:
            return False, "CPF com dígito verificador inválido"
        
        # Calcular segundo dígito verificador  
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        if int(cpf[10]) != digito2:
            return False, "CPF com dígito verificador inválido"
        
        return True, "✅ CPF válido"
    
    @staticmethod
    def validar_cnpj(cnpj: str) -> tuple[bool, str]:
        """Validação completa de CNPJ"""
        # Remover formatação
        cnpj = re.sub(r'\\D', '', cnpj)
        
        if len(cnpj) != 14:
            return False, "CNPJ deve ter 14 dígitos"
        
        # Verificar sequências inválidas
        if cnpj in ['00000000000000', '11111111111111']:
            return False, "CNPJ com sequência inválida"
        
        # Calcular primeiro dígito
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(12))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        if int(cnpj[12]) != digito1:
            return False, "CNPJ com dígito verificador inválido"
        
        # Calcular segundo dígito
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(13))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        if int(cnpj[13]) != digito2:
            return False, "CNPJ com dígito verificador inválido"
        
        return True, "✅ CNPJ válido"
    
    @staticmethod
    def validar_cep(cep: str) -> tuple[bool, str]:
        """Validação de CEP brasileiro"""
        # Remover formatação
        cep = re.sub(r'\\D', '', cep)
        
        if len(cep) != 8:
            return False, "CEP deve ter 8 dígitos"
        
        # Verificar se não é sequência óbvia
        if cep == '00000000':
            return False, "CEP inválido"
        
        return True, "✅ CEP válido"
    
    @staticmethod
    def validar_telefone_brasileiro(telefone: str) -> tuple[bool, str]:
        """Validação de telefone brasileiro"""
        # Remover formatação
        apenas_numeros = re.sub(r'\\D', '', telefone)
        
        # Verificar tamanho
        if len(apenas_numeros) not in [10, 11]:
            return False, "Telefone deve ter 10 ou 11 dígitos"
        
        # Verificar DDD válido (11-99)
        ddd = int(apenas_numeros[:2])
        if not (11 <= ddd <= 99):
            return False, "DDD inválido"
        
        # Para números de 11 dígitos, o terceiro deve ser 9
        if len(apenas_numeros) == 11 and apenas_numeros[2] != '9':
            return False, "Celular deve começar com 9 após o DDD"
        
        return True, "✅ Telefone válido"
    
    @staticmethod
    def formatador_brasileiro(tipo: str, valor: str) -> str:
        """Formatador para documentos brasileiros"""
        apenas_numeros = re.sub(r'\\D', '', valor)
        
        if tipo.upper() == 'CPF' and len(apenas_numeros) == 11:
            return f"{apenas_numeros[:3]}.{apenas_numeros[3:6]}.{apenas_numeros[6:9]}-{apenas_numeros[9:]}"
        
        elif tipo.upper() == 'CNPJ' and len(apenas_numeros) == 14:
            return f"{apenas_numeros[:2]}.{apenas_numeros[2:5]}.{apenas_numeros[5:8]}/{apenas_numeros[8:12]}-{apenas_numeros[12:]}"
        
        elif tipo.upper() == 'CEP' and len(apenas_numeros) == 8:
            return f"{apenas_numeros[:5]}-{apenas_numeros[5:]}"
        
        elif tipo.upper() == 'TELEFONE':
            if len(apenas_numeros) == 11:
                return f"({apenas_numeros[:2]}) {apenas_numeros[2:7]}-{apenas_numeros[7:]}"
            elif len(apenas_numeros) == 10:
                return f"({apenas_numeros[:2]}) {apenas_numeros[2:6]}-{apenas_numeros[6:]}"
        
        return valor

# Demonstração
documentos_teste = [
    ('CPF', '12345678909'),
    ('CNPJ', '11222333000181'),
    ('CEP', '01310100'),
    ('TELEFONE', '11999887766')
]

print("🧪 Testando validadores brasileiros:")
print("=" * 50)

for tipo, documento in documentos_teste:
    validador = getattr(ValidadorBrasileiro, f'validar_{tipo.lower()}')
    valido, mensagem = validador(documento)
    
    documento_formatado = ValidadorBrasileiro.formatador_brasileiro(tipo, documento)
    
    print(f"{tipo}: {documento} -> {documento_formatado}")
    print(f"Status: {mensagem}")
    print("-" * 30)
'''
        
        print(codigo_patterns)
    
    def _sistema_validacao_avancado(self):
        """Sistema avançado de validação"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏗️ SISTEMA AVANÇADO DE VALIDAÇÃO")
        
        print("⚙️ Sistema completo de validação orientado a objetos:")
        
        codigo_sistema = '''
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import json

class TipoValidacao(Enum):
    """Tipos de validação disponíveis"""
    OBRIGATORIO = "obrigatorio"
    EMAIL = "email"
    TELEFONE = "telefone"
    CPF = "cpf"
    IDADE = "idade"
    NUMERO = "numero"
    TEXTO = "texto"

@dataclass
class ResultadoValidacao:
    """Resultado de uma validação"""
    valido: bool
    mensagem: str
    valor_sanitizado: Optional[Any] = None
    detalhes: Optional[Dict] = None

class ValidadorBase(ABC):
    """Classe base para validadores"""
    
    @abstractmethod
    def validar(self, valor: Any) -> ResultadoValidacao:
        pass

class ValidadorObrigatorio(ValidadorBase):
    """Validador para campos obrigatórios"""
    
    def validar(self, valor: Any) -> ResultadoValidacao:
        if valor is None or (isinstance(valor, str) and not valor.strip()):
            return ResultadoValidacao(False, "Campo obrigatório não pode estar vazio")
        
        return ResultadoValidacao(True, "✅ Campo preenchido", valor)

class ValidadorEmail(ValidadorBase):
    """Validador avançado de email"""
    
    def validar(self, valor: str) -> ResultadoValidacao:
        if not isinstance(valor, str):
            return ResultadoValidacao(False, "Email deve ser texto")
        
        email = valor.strip().lower()
        
        # Usar validação da classe anterior
        from email_validator import validate_email, EmailNotValidError
        
        try:
            # Validação básica com regex
            import re
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
            if not re.match(pattern, email):
                return ResultadoValidacao(False, "Formato de email inválido")
            
            return ResultadoValidacao(True, "✅ Email válido", email)
            
        except Exception as e:
            return ResultadoValidacao(False, f"Erro na validação: {e}")

class CampoFormulario:
    """Representa um campo de formulário com suas validações"""
    
    def __init__(self, nome: str, label: str, tipos_validacao: List[TipoValidacao]):
        self.nome = nome
        self.label = label
        self.validadores = []
        
        # Mapeamento de tipos para validadores
        mapeamento = {
            TipoValidacao.OBRIGATORIO: ValidadorObrigatorio(),
            TipoValidacao.EMAIL: ValidadorEmail(),
            # Adicionar outros validadores...
        }
        
        for tipo in tipos_validacao:
            if tipo in mapeamento:
                self.validadores.append(mapeamento[tipo])
    
    def validar_campo(self, valor: Any) -> List[ResultadoValidacao]:
        """Valida o campo com todos os validadores"""
        resultados = []
        
        for validador in self.validadores:
            resultado = validador.validar(valor)
            resultados.append(resultado)
            
            # Se falhou em validação obrigatória, parar
            if not resultado.valido and isinstance(validador, ValidadorObrigatorio):
                break
        
        return resultados

class FormularioAvancado:
    """Sistema completo de formulário com validação"""
    
    def __init__(self, nome: str):
        self.nome = nome
        self.campos: Dict[str, CampoFormulario] = {}
        self.dados: Dict[str, Any] = {}
        self.erros: Dict[str, List[str]] = {}
    
    def adicionar_campo(self, campo: CampoFormulario):
        """Adiciona um campo ao formulário"""
        self.campos[campo.nome] = campo
    
    def coletar_dados(self) -> bool:
        """Coleta dados do usuário com validação completa"""
        print(f"📋 {self.nome}")
        print("=" * 50)
        
        for nome_campo, campo in self.campos.items():
            sucesso = False
            tentativas = 0
            max_tentativas = 3
            
            while not sucesso and tentativas < max_tentativas:
                try:
                    valor = input(f"{campo.label}: ")
                    
                    # Validar campo
                    resultados = campo.validar_campo(valor)
                    
                    # Verificar se todas as validações passaram
                    erros_campo = [r.mensagem for r in resultados if not r.valido]
                    
                    if erros_campo:
                        print("\\n".join(f"❌ {erro}" for erro in erros_campo))
                        tentativas += 1
                        
                        if tentativas < max_tentativas:
                            print(f"🔄 Tentativa {tentativas + 1} de {max_tentativas}")
                        continue
                    
                    # Sucesso - usar valor sanitizado se disponível
                    valor_final = valor
                    for resultado in resultados:
                        if resultado.valor_sanitizado is not None:
                            valor_final = resultado.valor_sanitizado
                    
                    self.dados[nome_campo] = valor_final
                    sucesso = True
                    
                    # Mostrar confirmações
                    confirmacoes = [r.mensagem for r in resultados if r.valido]
                    if confirmacoes:
                        print(confirmacoes[-1])  # Mostrar última confirmação
                
                except KeyboardInterrupt:
                    print("\\n⚠️ Operação cancelada")
                    return False
            
            if not sucesso:
                print(f"❌ Falha ao validar campo '{campo.label}'")
                return False
        
        return True
    
    def exibir_resumo(self):
        """Exibe resumo dos dados coletados"""
        print("\\n📊 RESUMO DOS DADOS COLETADOS:")
        print("=" * 40)
        
        for nome_campo, valor in self.dados.items():
            campo = self.campos[nome_campo]
            print(f"{campo.label}: {valor}")
    
    def exportar_json(self) -> str:
        """Exporta dados para JSON"""
        return json.dumps(self.dados, indent=2, ensure_ascii=False)

# Demonstração de uso
def criar_formulario_cadastro() -> FormularioAvancado:
    """Cria formulário de cadastro completo"""
    form = FormularioAvancado("Cadastro de Usuário Avançado")
    
    # Adicionar campos
    form.adicionar_campo(CampoFormulario(
        "nome", 
        "Nome completo", 
        [TipoValidacao.OBRIGATORIO, TipoValidacao.TEXTO]
    ))
    
    form.adicionar_campo(CampoFormulario(
        "email", 
        "Email", 
        [TipoValidacao.OBRIGATORIO, TipoValidacao.EMAIL]
    ))
    
    form.adicionar_campo(CampoFormulario(
        "idade", 
        "Idade", 
        [TipoValidacao.OBRIGATORIO, TipoValidacao.IDADE]
    ))
    
    return form

# Exemplo de uso
print("🚀 DEMONSTRAÇÃO DO SISTEMA AVANÇADO:")
formulario = criar_formulario_cadastro()

if formulario.coletar_dados():
    formulario.exibir_resumo()
    
    print("\\n💾 Dados em JSON:")
    print(formulario.exportar_json())
else:
    print("❌ Falha na coleta de dados")
'''
        
        print(codigo_sistema)
    
    def _mini_projeto_cadastro_completo(self):
        """Mini projeto: Sistema completo de cadastro"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: SISTEMA DE CADASTRO PROFISSIONAL")
        
        print("📊 Vamos criar um sistema completo de cadastro empresarial!")
        print("🎯 Funcionalidades do projeto:")
        print("• Validação robusta de todos os campos")
        print("• Sanitização automática de dados")
        print("• Sistema de retry inteligente")
        print("• Logging de operações")
        print("• Exportação para JSON")
        print("• Interface profissional")
        
        input("\n🔸 Pressione ENTER para ver o projeto...")
        
        codigo_projeto = '''
#!/usr/bin/env python3
"""
🏢 SISTEMA PROFISSIONAL DE CADASTRO EMPRESARIAL
Projeto completo com validação, sanitização e logging
"""

import json
import logging
import re
from datetime import datetime
from typing import Dict, Optional, Any
from dataclasses import dataclass, asdict

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cadastro.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class UsuarioEmpresarial:
    """Modelo de dados para usuário empresarial"""
    nome_completo: str
    email_corporativo: str
    cpf: str
    telefone: str
    cargo: str
    departamento: str
    data_nascimento: str
    endereco_completo: str
    data_cadastro: str = None
    
    def __post_init__(self):
        if self.data_cadastro is None:
            self.data_cadastro = datetime.now().isoformat()

class SistemaCadastroEmpresarial:
    """Sistema completo de cadastro para ambiente empresarial"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.usuarios_cadastrados = []
        self.sessao_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        self.logger.info(f"Sistema iniciado - Sessão: {self.sessao_id}")
    
    def validar_email_corporativo(self, email: str) -> tuple[bool, str]:
        """Valida email corporativo"""
        email = email.strip().lower()
        
        # Domínios pessoais não permitidos
        dominios_pessoais = [
            'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
            'uol.com.br', 'bol.com.br', 'terra.com.br'
        ]
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$', email):
            return False, "Formato de email inválido"
        
        dominio = email.split('@')[1]
        if dominio in dominios_pessoais:
            return False, "Email pessoal não permitido. Use email corporativo."
        
        return True, "✅ Email corporativo válido"
    
    def validar_cpf_completo(self, cpf: str) -> tuple[bool, str]:
        """Validação completa de CPF (implementação anterior)"""
        cpf = re.sub(r'\\D', '', cpf)
        
        if len(cpf) != 11:
            return False, "CPF deve ter 11 dígitos"
        
        if cpf in ['00000000000', '11111111111', '22222222222', 
                   '33333333333', '44444444444', '55555555555',
                   '66666666666', '77777777777', '88888888888', '99999999999']:
            return False, "CPF inválido"
        
        # Validação dos dígitos verificadores
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        if int(cpf[9]) != digito1:
            return False, "CPF inválido"
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        if int(cpf[10]) != digito2:
            return False, "CPF inválido"
        
        return True, "✅ CPF válido"
    
    def coletar_dados_usuario(self) -> Optional[UsuarioEmpresarial]:
        """Coleta dados completos do usuário"""
        print("\\n🏢 SISTEMA DE CADASTRO EMPRESARIAL")
        print("=" * 50)
        print("📋 Preencha todos os campos obrigatórios")
        print("⚠️  Máximo 3 tentativas por campo\\n")
        
        dados = {}
        
        # Campos e suas validações
        campos_config = [
            {
                'chave': 'nome_completo',
                'prompt': 'Nome completo',
                'validador': lambda x: (len(x.strip()) >= 5, "Nome deve ter pelo menos 5 caracteres"),
                'sanitizador': lambda x: ' '.join(word.capitalize() for word in x.split())
            },
            {
                'chave': 'email_corporativo',
                'prompt': 'Email corporativo',
                'validador': self.validar_email_corporativo,
                'sanitizador': lambda x: x.strip().lower()
            },
            {
                'chave': 'cpf',
                'prompt': 'CPF (apenas números)',
                'validador': self.validar_cpf_completo,
                'sanitizador': lambda x: re.sub(r'\\D', '', x)
            },
            {
                'chave': 'telefone',
                'prompt': 'Telefone (com DDD)',
                'validador': lambda x: (len(re.sub(r'\\D', '', x)) in [10, 11], 
                                      "Telefone deve ter 10 ou 11 dígitos"),
                'sanitizador': self.formatar_telefone
            },
            {
                'chave': 'cargo',
                'prompt': 'Cargo/Função',
                'validador': lambda x: (len(x.strip()) >= 2, "Cargo deve ter pelo menos 2 caracteres"),
                'sanitizador': lambda x: x.strip().title()
            },
            {
                'chave': 'departamento',
                'prompt': 'Departamento',
                'validador': lambda x: (len(x.strip()) >= 2, "Departamento deve ter pelo menos 2 caracteres"),
                'sanitizador': lambda x: x.strip().title()
            }
        ]
        
        # Coletar cada campo
        for config in campos_config:
            valor = self.coletar_campo_com_validacao(
                config['prompt'],
                config['validador'],
                config['sanitizador']
            )
            
            if valor is None:
                self.logger.warning(f"Cadastro cancelado no campo: {config['chave']}")
                return None
            
            dados[config['chave']] = valor
        
        # Campos adicionais (opcionais ou com validação mais simples)
        try:
            dados['data_nascimento'] = input("Data de nascimento (DD/MM/AAAA): ").strip()
            dados['endereco_completo'] = input("Endereço completo: ").strip()
        except (EOFError, KeyboardInterrupt):
            self.logger.info("Campos opcionais pulados")
            dados['data_nascimento'] = "Não informado"
            dados['endereco_completo'] = "Não informado"
        
        # Criar objeto usuário
        try:
            usuario = UsuarioEmpresarial(**dados)
            self.logger.info(f"Usuário criado com sucesso: {usuario.email_corporativo}")
            return usuario
            
        except Exception as e:
            self.logger.error(f"Erro ao criar usuário: {e}")
            return None
    
    def coletar_campo_com_validacao(self, prompt: str, validador: callable, 
                                  sanitizador: callable) -> Optional[str]:
        """Coleta um campo com validação e sanitização"""
        tentativas = 0
        max_tentativas = 3
        
        while tentativas < max_tentativas:
            try:
                valor = input(f"{prompt}: ").strip()
                
                if not valor:
                    print("❌ Campo não pode estar vazio")
                    tentativas += 1
                    continue
                
                # Aplicar sanitização
                valor_limpo = sanitizador(valor)
                
                # Validar
                valido, mensagem = validador(valor_limpo)
                
                if valido:
                    print(mensagem)
                    return valor_limpo
                else:
                    print(f"❌ {mensagem}")
                    tentativas += 1
                    
                    if tentativas < max_tentativas:
                        print(f"🔄 Tentativa {tentativas + 1} de {max_tentativas}")
            
            except (EOFError, KeyboardInterrupt):
                print("\\n⚠️ Operação cancelada")
                return None
        
        print("❌ Número máximo de tentativas excedido")
        return None
    
    def formatar_telefone(self, telefone: str) -> str:
        """Formata telefone brasileiro"""
        numeros = re.sub(r'\\D', '', telefone)
        
        if len(numeros) == 11:
            return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
        elif len(numeros) == 10:
            return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
        
        return numeros
    
    def salvar_usuario(self, usuario: UsuarioEmpresarial) -> bool:
        """Salva usuário em arquivo JSON"""
        try:
            self.usuarios_cadastrados.append(usuario)
            
            # Salvar em arquivo
            dados_para_salvar = [asdict(u) for u in self.usuarios_cadastrados]
            
            nome_arquivo = f"usuarios_cadastrados_{self.sessao_id}.json"
            
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_para_salvar, arquivo, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Usuário salvo em {nome_arquivo}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao salvar usuário: {e}")
            return False
    
    def exibir_resumo_cadastro(self, usuario: UsuarioEmpresarial):
        """Exibe resumo do cadastro realizado"""
        print("\\n" + "="*60)
        print("📊 RESUMO DO CADASTRO REALIZADO")
        print("="*60)
        
        print(f"👤 Nome: {usuario.nome_completo}")
        print(f"📧 Email: {usuario.email_corporativo}")
        print(f"🆔 CPF: {self.formatar_cpf(usuario.cpf)}")
        print(f"📱 Telefone: {usuario.telefone}")
        print(f"💼 Cargo: {usuario.cargo}")
        print(f"🏢 Departamento: {usuario.departamento}")
        print(f"📅 Data do cadastro: {datetime.fromisoformat(usuario.data_cadastro).strftime('%d/%m/%Y %H:%M')}")
        
        print("\\n✅ Cadastro realizado com sucesso!")
        print(f"💾 Dados salvos no sistema")
    
    def formatar_cpf(self, cpf: str) -> str:
        """Formata CPF para exibição"""
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    def executar_cadastro_completo(self) -> bool:
        """Executa o processo completo de cadastro"""
        print("🚀 Iniciando processo de cadastro empresarial...")
        
        # Coletar dados
        usuario = self.coletar_dados_usuario()
        
        if usuario is None:
            print("❌ Cadastro não foi concluído")
            return False
        
        # Salvar usuário
        if self.salvar_usuario(usuario):
            self.exibir_resumo_cadastro(usuario)
            return True
        else:
            print("❌ Erro ao salvar cadastro")
            return False

# Executar demonstração
if __name__ == "__main__":
    sistema = SistemaCadastroEmpresarial()
    
    print("🏢 DEMONSTRAÇÃO DO SISTEMA EMPRESARIAL")
    print("=" * 50)
    
    sucesso = sistema.executar_cadastro_completo()
    
    if sucesso:
        print("\\n🎉 Demonstração concluída com sucesso!")
        print("📄 Verifique o arquivo JSON gerado com os dados")
    else:
        print("\\n⚠️ Demonstração não foi concluída")
'''
        
        print(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Você criou um sistema empresarial completo!")
        print("🎯 Recursos implementados:")
        print("• ✅ Validação robusta de todos os dados")
        print("• ✅ Sanitização automática")
        print("• ✅ Logging profissional")
        print("• ✅ Tratamento de exceções")
        print("• ✅ Persistência em JSON")
        print("• ✅ Interface amigável")
        print("• ✅ Validação de documentos brasileiros")
        print("• ✅ Sistema de retry inteligente")
        
        print("\n💼 Aplicação real: sistemas de RH, CRM empresarial, cadastros corporativos")
        
        # Registra conclusão do mini projeto
        if hasattr(self, 'complete_mini_project'):
            self.complete_mini_project("Sistema de Cadastro Empresarial Completo")
        
        input("\n🔸 Pressione ENTER para finalizar...")


# Para teste standalone
if __name__ == "__main__":
    module = Modulo05EntradaDados()
    print("Teste do módulo 5 - versão melhorada")
    module._entrada_dados_moderna()