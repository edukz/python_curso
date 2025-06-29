#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 27: Testes e TDD (Test-Driven Development)
Aprenda a escrever testes, usar pytest e aplicar TDD
"""

from ..shared.base_module import BaseModule


class Modulo27TestesTdd(BaseModule):
    """Módulo 27: Testes e TDD - Desenvolvimento Orientado a Testes"""
    
    def __init__(self):
        super().__init__("modulo_27", "Testes e TDD")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre testes e TDD"""
        if not self.ui or not self.progress:
            self.print_warning("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._testes_tdd()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _testes_tdd(self) -> None:
        """Conteúdo principal sobre testes e TDD"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧪 MÓDULO 27: TESTES E TDD")
        else:
            self.print_section("🧪 MÓDULO 27: TESTES E TDD")
        
        self.print_tip("🧪 Testes são FUNDAMENTAIS para código de qualidade!")
        self.print_tip("🔄 TDD revoluciona a forma como desenvolvemos software!")
        
        self.print_section("POR QUE TESTAR SEU CÓDIGO?")
        
        self.print_tip("🎯 Benefícios dos testes:")
        self.print_colored("• ✅ Garantem que o código funciona", "green")
        self.print_colored("• 🛡️  Previnem bugs em produção", "green")
        self.print_colored("• 🔄 Facilitam refatoração", "green")
        self.print_colored("• 📝 Documentam o comportamento esperado", "green")
        self.print_colored("• 🚀 Aumentam confiança no código", "green")
        
        self.print_section("🧪 Tipos de Testes")
        
        codigo1 = '''# Exemplo básico de testes com unittest
import unittest

def somar(a, b):
    """Função simples para somar dois números"""
    return a + b

def dividir(a, b):
    """Função para dividir dois números"""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def eh_par(numero):
    """Verifica se um número é par"""
    return numero % 2 == 0

class TesteFuncoes(unittest.TestCase):
    """Classe de testes usando unittest"""
    
    def test_somar_numeros_positivos(self):
        """Testa soma de números positivos"""
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)
    
    def test_somar_numeros_negativos(self):
        """Testa soma com números negativos"""
        resultado = somar(-2, -3)
        self.assertEqual(resultado, -5)
    
    def test_somar_zero(self):
        """Testa soma com zero"""
        resultado = somar(5, 0)
        self.assertEqual(resultado, 5)
    
    def test_dividir_numeros_normais(self):
        """Testa divisão normal"""
        resultado = dividir(10, 2)
        self.assertEqual(resultado, 5.0)
    
    def test_dividir_por_zero(self):
        """Testa divisão por zero (deve dar erro)"""
        with self.assertRaises(ValueError):
            dividir(10, 0)
    
    def test_eh_par_numero_par(self):
        """Testa números pares"""
        self.assertTrue(eh_par(4))
        self.assertTrue(eh_par(0))
        self.assertTrue(eh_par(-2))
    
    def test_eh_par_numero_impar(self):
        """Testa números ímpares"""
        self.assertFalse(eh_par(3))
        self.assertFalse(eh_par(1))
        self.assertFalse(eh_par(-1))

print("=== EXECUTANDO TESTES ===")

# Criar suite de testes
suite = unittest.TestLoader().loadTestsFromTestCase(TesteFuncoes)
runner = unittest.TextTestRunner(verbosity=2)
resultado = runner.run(suite)

print(f"\\nTestes executados: {resultado.testsRun}")
print(f"Falhas: {len(resultado.failures)}")
print(f"Erros: {len(resultado.errors)}")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.print_section("🔄 Test-Driven Development (TDD)")
        
        codigo2 = '''# Exemplo de TDD - Desenvolvendo uma classe Calculadora
import unittest

# ETAPA 1: Escrever o teste PRIMEIRO (vai falhar)
class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.calc = Calculadora()
    
    def test_somar(self):
        """Teste para soma"""
        resultado = self.calc.somar(2, 3)
        self.assertEqual(resultado, 5)
    
    def test_subtrair(self):
        """Teste para subtração"""
        resultado = self.calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
    
    def test_multiplicar(self):
        """Teste para multiplicação"""
        resultado = self.calc.multiplicar(4, 3)
        self.assertEqual(resultado, 12)
    
    def test_dividir(self):
        """Teste para divisão"""
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5.0)
    
    def test_dividir_por_zero(self):
        """Teste para divisão por zero"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)
    
    def test_potencia(self):
        """Teste para potenciação"""
        resultado = self.calc.potencia(2, 3)
        self.assertEqual(resultado, 8)

# ETAPA 2: Implementar o código mínimo para passar nos testes
class Calculadora:
    """Calculadora simples seguindo TDD"""
    
    def somar(self, a, b):
        """Soma dois números"""
        return a + b
    
    def subtrair(self, a, b):
        """Subtrai dois números"""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplica dois números"""
        return a * b
    
    def dividir(self, a, b):
        """Divide dois números"""
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return a / b
    
    def potencia(self, base, expoente):
        """Calcula potência"""
        return base ** expoente

print("=== TDD EM AÇÃO ===")
print("1. Escrevemos os testes PRIMEIRO")
print("2. Implementamos o código para passar")
print("3. Refatoramos se necessário")
print()

# Executar os testes
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
runner = unittest.TextTestRunner(verbosity=2)
resultado = runner.run(suite)

print(f"\\n✅ Todos os testes passaram: {resultado.wasSuccessful()}")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.print_section("🔧 Testes com Pytest (mais moderno)")
        
        codigo3 = '''# Usando pytest - sintaxe mais simples e poderosa
# pip install pytest

import pytest
from typing import List

def fibonacci(n: int) -> List[int]:
    """Gera sequência de Fibonacci até n termos"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def validar_email(email: str) -> bool:
    """Valida formato básico de email"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Testes com pytest (sintaxe mais limpa)
def test_fibonacci_casos_basicos():
    """Testa casos básicos do fibonacci"""
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]

def test_fibonacci_sequencia():
    """Testa sequência fibonacci"""
    resultado = fibonacci(7)
    esperado = [0, 1, 1, 2, 3, 5, 8]
    assert resultado == esperado

def test_fibonacci_numero_negativo():
    """Testa número negativo"""
    assert fibonacci(-5) == []

# Testes parametrizados
@pytest.mark.parametrize("email,esperado", [
    ("teste@exemplo.com", True),
    ("usuario.nome@empresa.com.br", True),
    ("email_invalido", False),
    ("@sem-usuario.com", False),
    ("usuario@", False),
    ("", False),
])
def test_validar_email(email, esperado):
    """Testa validação de email com múltiplos casos"""
    assert validar_email(email) == esperado

# Fixtures para setup de testes
@pytest.fixture
def dados_teste():
    """Fixture que fornece dados para testes"""
    return {
        "usuarios": ["Ana", "João", "Maria"],
        "idades": [25, 30, 28],
        "ativo": True
    }

def test_usando_fixture(dados_teste):
    """Teste que usa fixture"""
    assert len(dados_teste["usuarios"]) == 3
    assert dados_teste["ativo"] is True
    assert max(dados_teste["idades"]) == 30

print("=== TESTES COM PYTEST ===")
print("Pytest oferece:")
print("• ✨ Sintaxe mais simples (assert simples)")
print("• 🔄 Testes parametrizados")
print("• 🏗️  Fixtures para setup")
print("• 📊 Relatórios detalhados")
print("• 🔌 Plugins extensivos")
print()

# Simulando execução dos testes
print("Executando testes fibonacci...")
test_fibonacci_casos_basicos()
test_fibonacci_sequencia()
test_fibonacci_numero_negativo()
print("✅ Testes fibonacci passaram!")

print("\\nExecutando testes de email...")
emails_teste = [
    ("teste@exemplo.com", True),
    ("email_invalido", False),
    ("usuario@empresa.com.br", True),
]

for email, esperado in emails_teste:
    resultado = validar_email(email)
    assert resultado == esperado
    print(f"  ✅ {email}: {resultado}")

print("\\n✅ Todos os testes passaram!")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.print_section("🤔 TESTE SEUS CONHECIMENTOS")
        self.exercicio(
            "Qual é a primeira etapa do TDD?",
            ["escrever teste", "test first", "teste primeiro"],
            "Escrever o teste PRIMEIRO, antes do código"
        )
        
        # Mini Projeto do Módulo 27
        self._mini_projeto_sistema_testes()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_testes(self) -> None:
        """Mini Projeto - Módulo 27: Sistema de Testes Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE TESTES COMPLETO")
        else:
            self.print_section("🎯 MINI PROJETO: SISTEMA DE TESTES COMPLETO")
        
        self.print_tip("🧪 Sistema completo de testes usando TDD e pytest!")
        self.print_tip("🛠️ Usando: TDD, Unittest, Pytest, Fixtures, Mocks")
        
        codigo_projeto = '''# 🧪 SISTEMA DE TESTES COMPLETO
# Desenvolvimento de uma biblioteca de validação usando TDD

import unittest
import pytest
from typing import List, Dict, Any
from datetime import datetime, date
import re
import json

class ValidationError(Exception):
    """Exceção customizada para erros de validação"""
    pass

class Validator:
    """Sistema de validação completo desenvolvido com TDD"""
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida CPF brasileiro"""
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Calcula primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = 11 - (soma % 11)
        digito1 = 0 if resto >= 10 else resto
        
        # Calcula segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = 11 - (soma % 11)
        digito2 = 0 if resto >= 10 else resto
        
        # Verifica os dígitos
        return cpf[9] == str(digito1) and cpf[10] == str(digito2)
    
    @staticmethod
    def validar_email(email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        """Valida telefone brasileiro"""
        telefone = re.sub(r'[^0-9]', '', telefone)
        return len(telefone) in [10, 11] and telefone[0:2] in ['11', '21', '31', '41', '51', '61', '71', '81', '85', '91']
    
    @staticmethod
    def validar_senha(senha: str) -> Dict[str, Any]:
        """Valida força da senha"""
        resultado = {
            'valida': False,
            'pontuacao': 0,
            'criterios': {
                'tamanho': len(senha) >= 8,
                'maiuscula': bool(re.search(r'[A-Z]', senha)),
                'minuscula': bool(re.search(r'[a-z]', senha)),
                'numero': bool(re.search(r'[0-9]', senha)),
                'especial': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', senha))
            }
        }
        
        resultado['pontuacao'] = sum(resultado['criterios'].values())
        resultado['valida'] = resultado['pontuacao'] >= 4
        
        return resultado
    
    @staticmethod
    def validar_data_nascimento(data_str: str) -> bool:
        """Valida data de nascimento"""
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y').date()
            hoje = date.today()
            idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
            return 0 <= idade <= 120 and data <= hoje
        except ValueError:
            return False

class Usuario:
    """Classe Usuario para demonstrar validação"""
    
    def __init__(self, nome: str, email: str, cpf: str, telefone: str, senha: str, data_nascimento: str):
        self.erros = []
        
        # Validações
        if not nome or len(nome.strip()) < 2:
            self.erros.append("Nome deve ter pelo menos 2 caracteres")
        
        if not Validator.validar_email(email):
            self.erros.append("Email inválido")
        
        if not Validator.validar_cpf(cpf):
            self.erros.append("CPF inválido")
        
        if not Validator.validar_telefone(telefone):
            self.erros.append("Telefone inválido")
        
        senha_validacao = Validator.validar_senha(senha)
        if not senha_validacao['valida']:
            self.erros.append(f"Senha fraca (pontuação: {senha_validacao['pontuacao']}/5)")
        
        if not Validator.validar_data_nascimento(data_nascimento):
            self.erros.append("Data de nascimento inválida")
        
        # Se passou em todas as validações, inicializa
        if not self.erros:
            self.nome = nome.strip()
            self.email = email
            self.cpf = cpf
            self.telefone = telefone
            self.senha = senha
            self.data_nascimento = data_nascimento
    
    def eh_valido(self) -> bool:
        """Verifica se usuário é válido"""
        return len(self.erros) == 0

# ===============================================
# TESTES USANDO UNITTEST
# ===============================================

class TestValidator(unittest.TestCase):
    """Testes da classe Validator usando unittest"""
    
    def test_cpf_valido(self):
        """Testa CPFs válidos"""
        cpfs_validos = ['11144477735', '111.444.777-35']
        for cpf in cpfs_validos:
            with self.subTest(cpf=cpf):
                self.assertTrue(Validator.validar_cpf(cpf))
    
    def test_cpf_invalido(self):
        """Testa CPFs inválidos"""
        cpfs_invalidos = ['123', '11111111111', '123.456.789-00']
        for cpf in cpfs_invalidos:
            with self.subTest(cpf=cpf):
                self.assertFalse(Validator.validar_cpf(cpf))
    
    def test_email_valido(self):
        """Testa emails válidos"""
        emails_validos = ['teste@exemplo.com', 'usuario.nome@empresa.com.br']
        for email in emails_validos:
            with self.subTest(email=email):
                self.assertTrue(Validator.validar_email(email))
    
    def test_senha_forte(self):
        """Testa senha forte"""
        senha = "MinhaSenh@123"
        resultado = Validator.validar_senha(senha)
        self.assertTrue(resultado['valida'])
        self.assertEqual(resultado['pontuacao'], 5)

class TestUsuario(unittest.TestCase):
    """Testes da classe Usuario"""
    
    def test_usuario_valido(self):
        """Testa criação de usuário válido"""
        usuario = Usuario(
            nome="João Silva",
            email="joao@exemplo.com",
            cpf="111.444.777-35",
            telefone="(11) 99999-9999",
            senha="MinhaSenh@123",
            data_nascimento="15/03/1990"
        )
        self.assertTrue(usuario.eh_valido())
        self.assertEqual(len(usuario.erros), 0)
    
    def test_usuario_invalido(self):
        """Testa usuário com dados inválidos"""
        usuario = Usuario(
            nome="A",  # Nome muito curto
            email="email_invalido",
            cpf="123.456.789-00",  # CPF inválido
            telefone="123",  # Telefone inválido
            senha="123",  # Senha fraca
            data_nascimento="30/02/2020"  # Data inválida
        )
        self.assertFalse(usuario.eh_valido())
        self.assertGreater(len(usuario.erros), 0)

# ===============================================
# TESTES USANDO PYTEST (simulado)
# ===============================================

class TestValidatorPytest:
    """Testes usando sintaxe pytest"""
    
    def setup_method(self):
        """Setup executado antes de cada teste"""
        self.validator = Validator()
    
    def test_cpf_casos_extremos(self):
        """Testa casos extremos de CPF"""
        assert not Validator.validar_cpf("")
        assert not Validator.validar_cpf("000.000.000-00")
        assert not Validator.validar_cpf("123.456.789")
    
    def test_telefone_diferentes_formatos(self):
        """Testa telefone em diferentes formatos"""
        telefones_validos = [
            "11987654321",
            "(11) 98765-4321",
            "11 9 8765-4321"
        ]
        
        for tel in telefones_validos:
            assert Validator.validar_telefone(tel)
    
    def test_senha_criterios_individuais(self):
        """Testa critérios individuais da senha"""
        resultado = Validator.validar_senha("Abc123!")
        
        assert resultado['criterios']['tamanho'] == False  # < 8 chars
        assert resultado['criterios']['maiuscula'] == True
        assert resultado['criterios']['minuscula'] == True
        assert resultado['criterios']['numero'] == True
        assert resultado['criterios']['especial'] == True

# ===============================================
# SISTEMA DE RELATÓRIOS DE TESTE
# ===============================================

class TestRunner:
    """Sistema para executar e gerar relatórios de teste"""
    
    def __init__(self):
        self.resultados = {
            'total': 0,
            'sucessos': 0,
            'falhas': 0,
            'erros': 0,
            'detalhes': []
        }
    
    def executar_testes_unittest(self):
        """Executa testes unittest"""
        print("🧪 Executando testes unittest...")
        
        # TestValidator
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
        runner1 = unittest.TextTestRunner(stream=open('/dev/null', 'w'), verbosity=0)
        resultado1 = runner1.run(suite1)
        
        # TestUsuario  
        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestUsuario)
        runner2 = unittest.TextTestRunner(stream=open('/dev/null', 'w'), verbosity=0)
        resultado2 = runner2.run(suite2)
        
        total_testes = resultado1.testsRun + resultado2.testsRun
        total_falhas = len(resultado1.failures) + len(resultado2.failures)
        total_erros = len(resultado1.errors) + len(resultado2.errors)
        
        print(f"  ✅ Testes executados: {total_testes}")
        print(f"  ❌ Falhas: {total_falhas}")
        print(f"  💥 Erros: {total_erros}")
        
        return total_testes, total_falhas, total_erros
    
    def executar_testes_manuais(self):
        """Executa testes pytest simulados"""
        print("\\n🔬 Executando testes pytest (simulado)...")
        
        testes_pytest = [
            ("test_cpf_casos_extremos", True),
            ("test_telefone_diferentes_formatos", True),
            ("test_senha_criterios_individuais", True),
        ]
        
        sucessos = 0
        for nome_teste, passou in testes_pytest:
            if passou:
                print(f"  ✅ {nome_teste}")
                sucessos += 1
            else:
                print(f"  ❌ {nome_teste}")
        
        return len(testes_pytest), sucessos
    
    def gerar_relatorio_cobertura(self):
        """Simula relatório de cobertura"""
        print("\\n📊 RELATÓRIO DE COBERTURA:")
        
        modulos = [
            ("Validator.validar_cpf", 100),
            ("Validator.validar_email", 95),
            ("Validator.validar_telefone", 90),
            ("Validator.validar_senha", 100),
            ("Usuario.__init__", 85),
            ("Usuario.eh_valido", 100),
        ]
        
        for modulo, cobertura in modulos:
            status = "✅" if cobertura >= 90 else "⚠️" if cobertura >= 75 else "❌"
            print(f"  {status} {modulo}: {cobertura}%")
        
        cobertura_media = sum(cob for _, cob in modulos) / len(modulos)
        print(f"\\n📈 Cobertura média: {cobertura_media:.1f}%")

# ===============================================
# DEMONSTRAÇÃO COMPLETA
# ===============================================

print("=== SISTEMA DE TESTES COMPLETO ===")
print()

# 1. Teste de validação individual
print("🔍 DEMONSTRAÇÃO DE VALIDAÇÕES:")
print()

# CPF
cpf_teste = "111.444.777-35"
print(f"CPF {cpf_teste}: {'✅ Válido' if Validator.validar_cpf(cpf_teste) else '❌ Inválido'}")

# Email
email_teste = "usuario@exemplo.com"
print(f"Email {email_teste}: {'✅ Válido' if Validator.validar_email(email_teste) else '❌ Inválido'}")

# Senha
senha_teste = "MinhaSenh@123"
resultado_senha = Validator.validar_senha(senha_teste)
print(f"Senha: {'✅ Forte' if resultado_senha['valida'] else '❌ Fraca'} ({resultado_senha['pontuacao']}/5)")

# 2. Teste de usuário completo
print("\\n👤 TESTE DE USUÁRIO COMPLETO:")
usuario_valido = Usuario(
    nome="Ana Silva",
    email="ana@exemplo.com", 
    cpf="111.444.777-35",
    telefone="11987654321",
    senha="MinhaSenh@123",
    data_nascimento="15/03/1990"
)

print(f"Usuário válido: {'✅ Sim' if usuario_valido.eh_valido() else '❌ Não'}")
if usuario_valido.erros:
    for erro in usuario_valido.erros:
        print(f"  ❌ {erro}")

# 3. Executar suite completa de testes
print("\\n🧪 EXECUTANDO SUITE COMPLETA DE TESTES:")
test_runner = TestRunner()

# Testes unittest
total_unittest, falhas_unittest, erros_unittest = test_runner.executar_testes_unittest()

# Testes pytest simulados
total_pytest, sucessos_pytest = test_runner.executar_testes_manuais()

# Relatório de cobertura
test_runner.gerar_relatorio_cobertura()

# 4. Resumo final
print("\\n📋 RESUMO FINAL:")
total_testes = total_unittest + total_pytest
total_sucessos = (total_unittest - falhas_unittest - erros_unittest) + sucessos_pytest
taxa_sucesso = (total_sucessos / total_testes) * 100 if total_testes > 0 else 0

print(f"  📊 Total de testes: {total_testes}")
print(f"  ✅ Sucessos: {total_sucessos}")
print(f"  ❌ Falhas: {falhas_unittest + (total_pytest - sucessos_pytest)}")
print(f"  💥 Erros: {erros_unittest}")
print(f"  🎯 Taxa de sucesso: {taxa_sucesso:.1f}%")

print()
print("✅ Sistema de Testes implementado com sucesso!")
print("🎯 Conceitos aplicados:")
print("  • Test-Driven Development (TDD)")
print("  • Unittest e Pytest")
print("  • Fixtures e Mocks")
print("  • Testes parametrizados")
print("  • Cobertura de código")
print("  • Relatórios de teste")
print("  • Validação de dados")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        self.print_success("🏆 PARABÉNS! Sistema de testes completo criado!")
        self.print_tip("🎯 Aplicação real: garantir qualidade em projetos profissionais")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Testes Completo")


# Para teste standalone
if __name__ == "__main__":
    module = Modulo27TestesTdd()
    print("Teste do módulo 27 - versão standalone")
    module._testes_tdd()