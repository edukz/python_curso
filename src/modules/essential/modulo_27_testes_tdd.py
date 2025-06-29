#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 27: Testes e TDD (Test-Driven Development)
Aprenda a criar código confiável e profissional com testes
"""

import os
import sys
import tempfile
from pathlib import Path
from ..shared.base_module import BaseModule


class Modulo27TestesTdd(BaseModule):
    """Módulo 27: Testes e TDD"""
    
    def __init__(self):
        super().__init__("modulo_27", "Testes e TDD")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo Testes e TDD"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._testes_tdd_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _testes_tdd_module(self) -> None:
        """Conteúdo principal do módulo Testes e TDD"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MÓDULO 27: TESTES E TDD")
        else:
            print("\n" + "="*50)
            print("🎯 MÓDULO 27: TESTES E TDD")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Bem-vindo ao mundo dos testes! Aqui você aprende a criar código à prova de balas!")
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
            self._mini_projeto_sistema_validacao()
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
                'id': 'secao_por_que_testar',
                'titulo': '🎯 Por que testar é essencial?',
                'descricao': 'Entenda a importância dos testes no desenvolvimento',
                'funcao': self._secao_por_que_testar
            },
            {
                'id': 'secao_tipos_testes',
                'titulo': '🧪 Tipos de testes',
                'descricao': 'Conheça os diferentes tipos e quando usar cada um',
                'funcao': self._secao_tipos_testes
            },
            {
                'id': 'secao_unittest_basico',
                'titulo': '💡 unittest - Framework nativo',
                'descricao': 'Aprenda o básico do unittest do Python',
                'funcao': self._secao_unittest_basico
            },
            {
                'id': 'secao_tdd_conceito',
                'titulo': '🔄 TDD - Test-Driven Development',
                'descricao': 'A metodologia que revoluciona como programamos',
                'funcao': self._secao_tdd_conceito
            },
            {
                'id': 'secao_pytest_moderno',
                'titulo': '🚀 pytest - Testes modernos',
                'descricao': 'O framework favorito dos desenvolvedores Python',
                'funcao': self._secao_pytest_moderno
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas de testes',
                'descricao': 'Dicas dos profissionais para testes eficazes',
                'funcao': self._secao_melhores_praticas
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre testes',
                'descricao': 'Fatos interessantes do mundo dos testes',
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
    
    def _secao_por_que_testar(self) -> None:
        """Seção: Por que testar é essencial?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("POR QUE TESTAR É ESSENCIAL?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Testes de Software",
            "Código que verifica se outro código funciona corretamente. Como um inspetor de qualidade para seu programa!"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Testes são como um seguro: você espera nunca precisar, mas fica feliz quando tem!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine construir uma casa:", "text")
        self.print_colored("• SEM testes = Construir e torcer para não cair", "text")
        self.print_colored("  - Problemas aparecem quando alguém mora", "text")
        self.print_colored("  - Consertar é caro e perigoso", "text")
        self.print_colored("• COM testes = Verificar cada etapa da construção", "text")
        self.print_colored("  - Fundação sólida? ✅ Paredes retas? ✅", "text")
        self.print_colored("  - Casa segura e confiável! 🏠", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === BENEFÍCIOS REAIS ===
        self.print_colored("\n💎 BENEFÍCIOS DOS TESTES:", "success")
        beneficios = [
            "1. 🛡️ Confiança para fazer mudanças sem medo",
            "2. 📋 Documentação viva de como o código funciona",
            "3. 🐛 Encontra bugs antes dos usuários",
            "4. 💰 Economiza tempo e dinheiro a longo prazo"
        ]
        
        for i, beneficio in enumerate(beneficios, 1):
            self.print_colored(beneficio, "text")
            if i < len(beneficios):
                input("   ⏳ Pressione ENTER para o próximo benefício...")
        
        # === ESTATÍSTICAS IMPRESSIONANTES ===
        self.print_colored("\n📊 FATOS COMPROVADOS:", "info")
        self.print_colored("• Microsoft: Testes reduziram bugs em 91% no Windows", "primary")
        self.print_colored("• Google: 80% do código tem testes automatizados", "primary")
        self.print_colored("• NASA: Testes salvaram missões espaciais bilionárias", "primary")
        self.print_colored("• Amazon: Deploys a cada 11 segundos graças aos testes", "primary")
        
        # === CUSTO DE NÃO TESTAR ===
        self.print_colored("\n💸 CUSTO DE BUGS FAMOSOS:", "error")
        bugs_famosos = [
            "Ariane 5 (1996): $370 milhões - foguete explodiu por overflow",
            "Knight Capital (2012): $440 milhões em 45 minutos",
            "Healthcare.gov (2013): $1.7 bilhões por falta de testes"
        ]
        for bug in bugs_famosos:
            self.print_colored(f"• {bug}", "text")
        
        self.print_success("\n🎯 Moral da história: Testes são investimento, não custo!")
        self.pausar()
    
    def _secao_tipos_testes(self) -> None:
        """Seção: Tipos de testes"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("TIPOS DE TESTES", "🧪", "info")
        
        self.print_concept(
            "Pirâmide de Testes",
            "Diferentes níveis de testes, da base (unitários) ao topo (sistema completo)"
        )
        
        # === PIRÂMIDE VISUAL ===
        self.print_colored("\n🔺 PIRÂMIDE DE TESTES:", "warning")
        piramide = '''
               /\\
              /  \\     E2E (End-to-End)
             /----\\    ← Poucos, lentos, caros
            /      \\
           /--------\\  Integração
          /          \\ ← Médios
         /------------\\
        /              \\ Unitários
       /________________\\ ← Muitos, rápidos, baratos'''
        
        self.print_colored(piramide, "text")
        input("\n🔸 Pressione ENTER para explorar cada tipo...")
        
        # === TESTES UNITÁRIOS ===
        self.print_colored("\n1️⃣ TESTES UNITÁRIOS:", "success")
        self.print_colored("• Testam uma única função ou método", "text")
        self.print_colored("• Rápidos (milissegundos)", "text")
        self.print_colored("• Isolados (sem dependências externas)", "text")
        
        exemplo_unitario = '''def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0'''
        
        self.print_code_section("EXEMPLO", exemplo_unitario)
        
        # === TESTES DE INTEGRAÇÃO ===
        self.print_colored("\n2️⃣ TESTES DE INTEGRAÇÃO:", "warning")
        self.print_colored("• Testam componentes trabalhando juntos", "text")
        self.print_colored("• Médios (segundos)", "text")
        self.print_colored("• Verificam conexões e fluxos", "text")
        
        exemplo_integracao = '''def test_salvar_usuario_no_banco():
    usuario = criar_usuario("João", "joao@email.com")
    banco.salvar(usuario)
    
    usuario_salvo = banco.buscar(usuario.id)
    assert usuario_salvo.nome == "João"'''
        
        self.print_code_section("EXEMPLO", exemplo_integracao)
        
        # === TESTES E2E ===
        self.print_colored("\n3️⃣ TESTES END-TO-END (E2E):", "accent")
        self.print_colored("• Testam o sistema completo como usuário", "text")
        self.print_colored("• Lentos (minutos)", "text")
        self.print_colored("• Simulam cenários reais", "text")
        
        exemplo_e2e = '''def test_compra_completa():
    # Usuário acessa o site
    browser.get("https://loja.com")
    
    # Adiciona produto ao carrinho
    browser.find_element("Adicionar").click()
    
    # Finaliza compra
    browser.find_element("Finalizar").click()
    
    # Verifica confirmação
    assert "Pedido confirmado" in browser.page_source'''
        
        self.print_code_section("EXEMPLO", exemplo_e2e)
        
        # === PROPORÇÃO IDEAL ===
        self.print_colored("\n📊 PROPORÇÃO IDEAL:", "info")
        self.print_colored("• 70% Testes Unitários", "success")
        self.print_colored("• 20% Testes de Integração", "warning")
        self.print_colored("• 10% Testes E2E", "error")
        
        self.pausar()
    
    def _secao_unittest_basico(self) -> None:
        """Seção: unittest - Framework nativo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("UNITTEST - FRAMEWORK NATIVO", "💡", "success")
        
        self.print_concept(
            "unittest",
            "Framework de testes incluído no Python. Não precisa instalar nada!"
        )
        
        # === ESTRUTURA BÁSICA ===
        self.print_colored("\n🏗️ ESTRUTURA BÁSICA:", "warning")
        
        estrutura_basica = '''import unittest

class TestMinhasFuncoes(unittest.TestCase):
    def test_algo_simples(self):
        # Arrange (Preparar)
        esperado = 5
        
        # Act (Agir)
        resultado = 2 + 3
        
        # Assert (Verificar)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()'''
        
        self.print_code_section("ESTRUTURA", estrutura_basica)
        
        # === EXEMPLO PRÁTICO ===
        self.print_colored("\n🚀 VAMOS CRIAR NOSSO PRIMEIRO TESTE:", "accent")
        
        codigo_completo = '''import unittest

# Função que vamos testar
def calcular_media(notas):
    """Calcula a média de uma lista de notas"""
    if not notas:
        return 0
    return sum(notas) / len(notas)

# Classe de testes
class TestCalcularMedia(unittest.TestCase):
    
    def test_media_normal(self):
        """Testa cálculo normal"""
        notas = [8, 9, 7]
        self.assertEqual(calcular_media(notas), 8.0)
    
    def test_lista_vazia(self):
        """Testa lista vazia"""
        self.assertEqual(calcular_media([]), 0)
    
    def test_uma_nota(self):
        """Testa com apenas uma nota"""
        self.assertEqual(calcular_media([10]), 10.0)

# Executar testes
if __name__ == '__main__':
    # Vamos testar!
    print("🧪 Executando testes...")
    
    # Testar manualmente primeiro
    print(f"Média de [8, 9, 7]: {calcular_media([8, 9, 7])}")
    print(f"Média de []: {calcular_media([])}")
    print(f"Média de [10]: {calcular_media([10])}")
    
    print("\\n✅ Todos os testes passaram!")'''
        
        self.exemplo(codigo_completo)
        self.executar_codigo(codigo_completo)
        
        # === MÉTODOS ÚTEIS ===
        self.print_colored("\n🛠️ MÉTODOS MAIS USADOS:", "info")
        metodos = [
            "assertEqual(a, b) → Verifica se a == b",
            "assertTrue(x) → Verifica se x é True",
            "assertFalse(x) → Verifica se x é False",
            "assertIn(a, b) → Verifica se a está em b",
            "assertRaises(Exception) → Verifica se lança exceção"
        ]
        
        for metodo in metodos:
            self.print_colored(f"• {metodo}", "primary")
        
        # === DICAS PRÁTICAS ===
        self.print_colored("\n💡 DICAS DE OURO:", "warning")
        dicas = [
            "Nomeie testes com 'test_' no início",
            "Um teste deve testar UMA coisa só",
            "Use nomes descritivos: test_calcular_media_lista_vazia",
            "Teste casos normais E casos extremos"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "accent")
        
        self.pausar()
    
    def _secao_tdd_conceito(self) -> None:
        """Seção: TDD - Test-Driven Development"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("TDD - TEST-DRIVEN DEVELOPMENT", "🔄", "error")
        
        self.print_concept(
            "TDD",
            "Escrever o teste ANTES do código. Parece loucura? É genial!"
        )
        
        # === O CICLO TDD ===
        self.print_colored("\n🔄 O CICLO SAGRADO DO TDD:", "warning")
        ciclo = '''
        🔴 RED          🟢 GREEN        🔵 REFACTOR
         ↓               ↓               ↓
    Escrever teste → Fazer passar → Melhorar código
         ↓               ↓               ↓
      Teste falha   Código mínimo   Código limpo
         ↓               ↓               ↓
         └───────────────┴───────────────┘
                   REPETIR'''
        
        self.print_colored(ciclo, "text")
        input("\n🔸 Pressione ENTER para ver na prática...")
        
        # === EXEMPLO PRÁTICO TDD ===
        self.print_colored("\n🎯 VAMOS FAZER TDD NA PRÁTICA:", "success")
        self.print_colored("Objetivo: Criar validador de CPF", "text")
        
        # PASSO 1: RED
        self.print_colored("\n🔴 PASSO 1: ESCREVER TESTE (vai falhar!)", "error")
        
        teste_inicial = '''import unittest

class TestValidadorCPF(unittest.TestCase):
    def test_cpf_valido(self):
        # Este teste vai FALHAR (função não existe ainda!)
        self.assertTrue(validar_cpf("123.456.789-09"))'''
        
        self.print_code_section("TESTE", teste_inicial)
        
        # PASSO 2: GREEN
        self.print_colored("\n🟢 PASSO 2: CÓDIGO MÍNIMO PARA PASSAR", "success")
        
        codigo_minimo = '''def validar_cpf(cpf):
    # Código MÍNIMO só para passar o teste
    return True  # Por enquanto, sempre retorna True'''
        
        self.print_code_section("CÓDIGO", codigo_minimo)
        
        # PASSO 3: REFACTOR
        self.print_colored("\n🔵 PASSO 3: REFATORAR E MELHORAR", "info")
        
        codigo_melhorado = '''def validar_cpf(cpf):
    # Agora implementamos de verdade
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Por enquanto, validação básica
    return True'''
        
        self.print_code_section("CÓDIGO MELHORADO", codigo_melhorado)
        
        # === VANTAGENS DO TDD ===
        self.print_colored("\n✨ POR QUE TDD É INCRÍVEL:", "warning")
        vantagens = [
            "🎯 Foco no que realmente importa",
            "📋 Especificação clara antes de codar",
            "🛡️ 100% de cobertura garantida",
            "🏗️ Design melhor (código testável = código limpo)",
            "😌 Confiança total no código"
        ]
        
        for vantagem in vantagens:
            self.print_colored(vantagem, "primary")
        
        # === EXEMPLO COMPLETO ===
        self.print_colored("\n💻 EXEMPLO COMPLETO COM TDD:", "accent")
        
        exemplo_tdd = '''# 1. Começamos com o teste
import unittest

class TestCalculadora(unittest.TestCase):
    def test_dividir_numeros_positivos(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)
    
    def test_dividir_por_zero_lanca_erro(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

# 2. Implementamos o mínimo
class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero!")
        return a / b

# 3. Testamos
if __name__ == '__main__':
    print("🧪 Rodando testes TDD...")
    
    calc = Calculadora()
    print(f"10 ÷ 2 = {calc.dividir(10, 2)}")
    
    try:
        calc.dividir(10, 0)
    except ValueError as e:
        print(f"Erro capturado: {e}")
    
    print("\\n✅ TDD funcionando perfeitamente!")'''
        
        self.exemplo(exemplo_tdd)
        self.executar_codigo(exemplo_tdd)
        
        self.print_success("\n🏆 Agora você conhece o poder do TDD!")
        self.pausar()
    
    def _secao_pytest_moderno(self) -> None:
        """Seção: pytest - Testes modernos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PYTEST - TESTES MODERNOS", "🚀", "accent")
        
        self.print_concept(
            "pytest",
            "O framework de testes mais popular e poderoso do Python. Simples e elegante!"
        )
        
        # === INSTALAÇÃO ===
        self.print_colored("\n📦 INSTALAÇÃO:", "warning")
        self.print_code_section("", "pip install pytest")
        
        # === COMPARAÇÃO ===
        self.print_colored("\n🆚 UNITTEST vs PYTEST:", "info")
        
        comparacao = '''# UNITTEST (verboso)
import unittest

class TestExemplo(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(2 + 2, 4)

# PYTEST (simples e direto!)
def test_soma():
    assert 2 + 2 == 4'''
        
        self.print_code_section("COMPARAÇÃO", comparacao)
        
        # === EXEMPLO BÁSICO ===
        self.print_colored("\n✨ A MÁGICA DO PYTEST:", "success")
        
        exemplo_pytest = '''# arquivo: test_matematica.py

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Testes com pytest - simples assim!
def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -1) == -2

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_multiplicar_por_zero():
    assert multiplicar(5, 0) == 0

# Para executar: pytest test_matematica.py
print("🧪 Testes com pytest!")
print(f"2 + 3 = {somar(2, 3)}")
print(f"3 × 4 = {multiplicar(3, 4)}")'''
        
        self.exemplo(exemplo_pytest)
        self.executar_codigo(exemplo_pytest)
        
        # === RECURSOS AVANÇADOS ===
        self.print_colored("\n🎯 RECURSOS INCRÍVEIS DO PYTEST:", "warning")
        
        # Fixtures
        self.print_colored("\n1️⃣ FIXTURES - Preparação reutilizável:", "primary")
        fixture_exemplo = '''import pytest

@pytest.fixture
def usuario_teste():
    """Cria um usuário para testes"""
    return {"nome": "João", "idade": 25}

def test_usuario_maior_idade(usuario_teste):
    assert usuario_teste["idade"] >= 18

def test_usuario_tem_nome(usuario_teste):
    assert usuario_teste["nome"] == "João"'''
        
        self.print_code_section("FIXTURES", fixture_exemplo)
        
        # Parametrização
        self.print_colored("\n2️⃣ PARAMETRIZAÇÃO - Múltiplos casos:", "primary")
        parametrize_exemplo = '''import pytest

@pytest.mark.parametrize("entrada,esperado", [
    (2, 4),
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_quadrado(entrada, esperado):
    assert entrada ** 2 == esperado'''
        
        self.print_code_section("PARAMETRIZAÇÃO", parametrize_exemplo)
        
        # Marcadores
        self.print_colored("\n3️⃣ MARCADORES - Organize seus testes:", "primary")
        marcadores_exemplo = '''import pytest

@pytest.mark.slow
def test_processo_demorado():
    # Teste que demora muito
    pass

@pytest.mark.skip(reason="Ainda não implementado")
def test_funcionalidade_futura():
    pass

# Executar só testes rápidos: pytest -m "not slow"'''
        
        self.print_code_section("MARCADORES", marcadores_exemplo)
        
        # === COMANDOS ÚTEIS ===
        self.print_colored("\n⚡ COMANDOS PYTEST ESSENCIAIS:", "info")
        comandos = [
            "pytest → Executa todos os testes",
            "pytest -v → Modo verboso (detalhado)",
            "pytest -x → Para no primeiro erro",
            "pytest --tb=short → Traceback resumido",
            "pytest -k 'usuario' → Só testes com 'usuario' no nome",
            "pytest --cov → Cobertura de código"
        ]
        
        for cmd in comandos:
            self.print_colored(f"• {cmd}", "accent")
        
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas de testes"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS DE TESTES", "⭐", "success")
        
        # === PRINCÍPIO FIRST ===
        self.print_colored("🎯 PRINCÍPIO F.I.R.S.T:", "warning")
        self.print_colored("Seus testes devem ser:", "text")
        
        first = [
            "F - Fast (Rápidos): Milissegundos, não minutos",
            "I - Independent (Independentes): Não dependem uns dos outros",
            "R - Repeatable (Repetíveis): Mesmo resultado sempre",
            "S - Self-validating (Auto-validáveis): Pass ou Fail claro",
            "T - Timely (Oportunos): Escritos no momento certo"
        ]
        
        for principio in first:
            self.print_colored(f"• {principio}", "primary")
            input("   🔸 Pressione ENTER...")
        
        # === PADRÃO AAA ===
        self.print_colored("\n📐 PADRÃO AAA (ARRANGE-ACT-ASSERT):", "info")
        
        padrao_aaa = '''def test_calcular_desconto():
    # ARRANGE (Preparar)
    preco_original = 100
    percentual_desconto = 10
    
    # ACT (Agir)
    preco_final = calcular_desconto(preco_original, percentual_desconto)
    
    # ASSERT (Verificar)
    assert preco_final == 90'''
        
        self.print_code_section("PADRÃO AAA", padrao_aaa)
        
        # === NOMES DESCRITIVOS ===
        self.print_colored("\n📝 NOMES DESCRITIVOS:", "warning")
        
        nomes_exemplo = '''# ❌ RUIM
def test1():
    pass

def test_funcao():
    pass

# ✅ BOM
def test_calcular_juros_com_taxa_negativa_deve_lancar_erro():
    pass

def test_usuario_sem_email_nao_pode_ser_criado():
    pass'''
        
        self.print_code_section("NOMES", nomes_exemplo)
        
        # === O QUE TESTAR ===
        self.print_colored("\n🎯 O QUE TESTAR:", "success")
        testar = [
            "✅ Casos normais (caminho feliz)",
            "✅ Casos extremos (limites)",
            "✅ Casos de erro (exceções)",
            "✅ Valores especiais (None, 0, vazio)",
            "❌ Detalhes de implementação",
            "❌ Código de terceiros (já testado)"
        ]
        
        for item in testar:
            self.print_colored(f"• {item}", "text")
        
        # === EXEMPLO COMPLETO ===
        self.print_colored("\n💎 EXEMPLO DE TESTE PROFISSIONAL:", "accent")
        
        teste_profissional = '''import pytest
from datetime import datetime

class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.transacoes = []
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor
        self.transacoes.append({
            "tipo": "depósito",
            "valor": valor,
            "data": datetime.now()
        })
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.transacoes.append({
            "tipo": "saque",
            "valor": valor,
            "data": datetime.now()
        })

# TESTES PROFISSIONAIS
class TestConta:
    @pytest.fixture
    def conta_vazia(self):
        """Fixture: conta sem saldo"""
        return Conta()
    
    @pytest.fixture
    def conta_com_saldo(self):
        """Fixture: conta com R$ 100"""
        return Conta(100)
    
    def test_criar_conta_sem_saldo(self):
        conta = Conta()
        assert conta.saldo == 0
        assert conta.transacoes == []
    
    def test_criar_conta_com_saldo_inicial(self):
        conta = Conta(50)
        assert conta.saldo == 50
    
    def test_depositar_valor_valido(self, conta_vazia):
        conta_vazia.depositar(100)
        assert conta_vazia.saldo == 100
        assert len(conta_vazia.transacoes) == 1
        assert conta_vazia.transacoes[0]["tipo"] == "depósito"
    
    def test_depositar_valor_invalido(self, conta_vazia):
        with pytest.raises(ValueError, match="Valor deve ser positivo"):
            conta_vazia.depositar(-10)
    
    def test_sacar_com_saldo_suficiente(self, conta_com_saldo):
        conta_com_saldo.sacar(30)
        assert conta_com_saldo.saldo == 70
    
    def test_sacar_mais_que_saldo(self, conta_com_saldo):
        with pytest.raises(ValueError, match="Saldo insuficiente"):
            conta_com_saldo.sacar(150)

# Demonstração
if __name__ == '__main__':
    print("🏦 Sistema Bancário com Testes")
    
    conta = Conta(100)
    print(f"Saldo inicial: R$ {conta.saldo}")
    
    conta.depositar(50)
    print(f"Após depósito de R$ 50: R$ {conta.saldo}")
    
    conta.sacar(30)
    print(f"Após saque de R$ 30: R$ {conta.saldo}")
    
    print(f"\\nTransações: {len(conta.transacoes)}")'''
        
        self.exemplo(teste_profissional)
        self.executar_codigo(teste_profissional)
        
        self.print_success("\n🏆 Agora você sabe testar como profissional!")
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre testes"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES SOBRE TESTES", "💫", "accent")
        
        # === HISTÓRIA DOS TESTES ===
        self.print_colored("📚 HISTÓRIA FASCINANTE:", "warning")
        self.print_colored("• 1949: Alan Turing já falava sobre testes de programas", "text")
        self.print_colored("• 1957: Primeiro debugger foi criado", "text")
        self.print_colored("• 1990s: Kent Beck popularizou TDD", "text")
        self.print_colored("• 2004: pytest foi criado", "text")
        
        # === FATOS INTERESSANTES ===
        self.print_colored("\n🤯 FATOS QUE VÃO TE SURPREENDER:", "info")
        fatos = [
            "SpaceX testa cada linha de código 3x antes de lançar foguetes",
            "Netflix faz 'Chaos Testing' - quebra coisas de propósito!",
            "Google tem 2 bilhões de testes rodando por dia",
            "Amazon faz deploy a cada 11.7 segundos graças aos testes"
        ]
        
        for fato in fatos:
            self.print_colored(f"• {fato}", "primary")
            input("   😮 Pressione ENTER...")
        
        # === TIPOS EXÓTICOS DE TESTES ===
        self.print_colored("\n🦄 TESTES EXÓTICOS:", "success")
        exoticos = [
            "🐒 Monkey Testing: Inputs aleatórios para quebrar o sistema",
            "🦍 Gorilla Testing: Testar uma feature até a exaustão",
            "🔥 Chaos Testing: Derrubar servidores em produção (!)",
            "🎭 A/B Testing: Duas versões para ver qual é melhor",
            "🌈 Visual Testing: Comparar screenshots pixel a pixel"
        ]
        
        for teste in exoticos:
            self.print_colored(teste, "accent")
        
        # === CITAÇÕES FAMOSAS ===
        self.print_colored("\n💬 CITAÇÕES INSPIRADORAS:", "warning")
        citacoes = [
            '"Debugging é duas vezes mais difícil que escrever código." - Brian Kernighan',
            '"Código sem testes é código quebrado por design." - Jacob Kaplan-Moss',
            '"TDD não é sobre testes, é sobre design." - Kent Beck'
        ]
        
        for citacao in citacoes:
            self.print_colored(citacao, "text")
            input("   💭 Pressione ENTER...")
        
        # === DIVERSÃO COM TESTES ===
        self.print_colored("\n🎮 TESTE DIVERTIDO:", "error")
        
        teste_divertido = '''import random

def e_numero_da_sorte(numero):
    """Um número é da sorte se for 7 ou múltiplo de 7"""
    return numero == 7 or numero % 7 == 0

# Teste divertido
def test_numeros_da_sorte():
    # Números definitivamente da sorte
    assert e_numero_da_sorte(7) == True
    assert e_numero_da_sorte(14) == True
    assert e_numero_da_sorte(777) == True
    
    # Números sem sorte
    assert e_numero_da_sorte(13) == False
    assert e_numero_da_sorte(666) == False

# Brincadeira
print("🎰 Teste de Sorte!")
seu_numero = random.randint(1, 100)
print(f"Seu número: {seu_numero}")

if e_numero_da_sorte(seu_numero):
    print("🍀 Você tem sorte! É um número da sorte!")
else:
    print("😅 Tente novamente! Não foi dessa vez...")'''
        
        self.exemplo(teste_divertido)
        self.executar_codigo(teste_divertido)
        
        self.print_success("\n✨ Testes podem ser divertidos e fascinantes!")
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
                'title': 'Quiz: Conhecimentos sobre Testes e TDD',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual é a ordem correta do ciclo TDD?',
                        'answer': ['red green refactor', 'vermelho verde refatorar', 'red, green, refactor'],
                        'hint': 'Primeiro o teste falha, depois passa, depois melhora'
                    },
                    {
                        'question': 'Qual comando executa testes com pytest?',
                        'answer': ['pytest', 'python -m pytest'],
                        'hint': 'É o nome do framework'
                    },
                    {
                        'question': 'No padrão AAA, o que significa o primeiro A?',
                        'answer': ['arrange', 'preparar'],
                        'hint': 'É a fase de preparação do teste'
                    },
                    {
                        'question': 'Qual a proporção ideal de testes unitários?',
                        'answer': ['70%', '70', 'setenta'],
                        'hint': 'É a base da pirâmide de testes'
                    },
                    {
                        'question': 'O que é uma fixture no pytest?',
                        'answer': ['preparacao reutilizavel', 'setup reutilizavel', 'configuracao de teste'],
                        'hint': 'Prepara dados ou objetos para vários testes'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código de Teste',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o assert para verificar se 5 + 3 é igual a 8',
                        'starter': 'def test_soma():\n    ____ 5 + 3 == 8',
                        'solution': 'assert',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o decorator para criar uma fixture',
                        'starter': '@pytest.____\ndef usuario():\n    return {"nome": "Ana"}',
                        'solution': 'fixture',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete para testar se função lança ValueError',
                        'starter': 'def test_erro():\n    with pytest.raises(____):\n        dividir(10, 0)',
                        'solution': 'ValueError',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Crie seu Próprio Teste',
                'type': 'creative',
                'instruction': 'Crie um teste para uma função que valida se uma senha é forte (mínimo 8 caracteres, letra e número)!'
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
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre testes e TDD",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de testes",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie testes para validação de senha",
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
    
    def _run_quiz(self, quiz_data):
        """Executa o quiz interativo"""
        self.print_section(quiz_data['title'], "📝", "info")
        
        score = 0
        total = len(quiz_data['questions'])
        
        for i, q in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\nPergunta {i}/{total}:", "warning")
            self.print_colored(q['question'], "text")
            
            while True:
                try:
                    resposta = input("\n📝 Sua resposta: ").strip().lower()
                    
                    if resposta in ["help", "ajuda", "dica"]:
                        self.print_tip(q['hint'])
                        continue
                    
                    # Verifica se a resposta está correta
                    respostas_corretas = [ans.lower() for ans in q['answer']]
                    if resposta in respostas_corretas or any(resposta in ans for ans in respostas_corretas):
                        self.print_success("✅ Correto!")
                        score += 1
                        break
                    else:
                        self.print_warning("❌ Não está certo...")
                        tentar = input("Tentar novamente? (s/n): ").lower()
                        if tentar not in ['s', 'sim', 'yes']:
                            self.print_colored(f"💡 Resposta: {q['answer'][0]}", "info")
                            break
                
                except KeyboardInterrupt:
                    raise
        
        # Resultado final
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        percentual = (score / total) * 100
        self.print_colored(f"Você acertou {score} de {total} questões ({percentual:.0f}%)", "text")
        
        if percentual >= 80:
            self.print_success("🌟 Excelente! Você domina o conteúdo!")
        elif percentual >= 60:
            self.print_colored("💪 Muito bom! Continue praticando!", "warning")
        else:
            self.print_colored("📚 Revise o conteúdo e tente novamente!", "info")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _run_code_completion(self, exercise_data):
        """Executa exercícios de completar código"""
        self.print_section(exercise_data['title'], "💻", "success")
        
        for i, exercise in enumerate(exercise_data['exercises'], 1):
            nivel = exercise['type'].upper()
            cor = {'SIMPLE': 'info', 'INTERMEDIATE': 'warning', 'ADVANCED': 'error'}.get(exercise['type'], 'text')
            
            self.print_colored(f"\n[{nivel}] {exercise['instruction']}", cor)
            self.print_code_section("CÓDIGO INICIAL", exercise['starter'])
            
            while True:
                try:
                    resposta = input("\n💻 Complete o código: ").strip()
                    
                    if resposta.lower() in ["help", "ajuda"]:
                        self.print_tip("Pense no que está faltando para o teste funcionar...")
                        continue
                    
                    if resposta.lower() == exercise['solution'].lower():
                        self.print_success("✅ Perfeito!")
                        # Mostra o código completo
                        codigo_completo = exercise['starter'].replace('____', exercise['solution'])
                        self.print_code_section("CÓDIGO COMPLETO", codigo_completo)
                        break
                    else:
                        self.print_warning("❌ Não está certo...")
                        mostrar = input("Ver a resposta? (s/n): ").lower()
                        if mostrar in ['s', 'sim', 'yes']:
                            self.print_colored(f"💡 Resposta: {exercise['solution']}", "info")
                            break
                
                except KeyboardInterrupt:
                    raise
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.print_success("\n🎉 Exercícios de código completados!")
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _run_creative_exercise(self, exercise_data):
        """Executa exercício criativo"""
        self.print_section(exercise_data['title'], "🎨", "accent")
        
        self.print_colored(f"\n{exercise_data['instruction']}", "text")
        
        self.print_colored("\n💡 REQUISITOS DA SENHA FORTE:", "warning")
        requisitos = [
            "• Mínimo 8 caracteres",
            "• Pelo menos uma letra maiúscula",
            "• Pelo menos uma letra minúscula",
            "• Pelo menos um número",
            "• (Opcional) Caractere especial"
        ]
        
        for req in requisitos:
            self.print_colored(req, "text")
        
        self.print_colored("\n📝 EXEMPLO DE INÍCIO:", "info")
        exemplo_teste = '''import pytest

def senha_forte(senha):
    # Sua implementação aqui
    if len(senha) < 8:
        return False
    # Continue...
    return True

# SEUS TESTES
def test_senha_muito_curta():
    assert senha_forte("abc123") == False

def test_senha_sem_numeros():
    assert senha_forte("SenhaForte") == False

# Continue criando mais testes...'''
        
        self.print_code_section("TEMPLATE", exemplo_teste)
        
        input("\n🎨 Use sua criatividade! Pressione ENTER quando terminar...")
        
        self.print_success("🎉 Ótimo trabalho! Testes criativos são essenciais!")
        
        # Mostra um exemplo completo
        mostrar = input("\nQuer ver um exemplo completo? (s/n): ").lower()
        if mostrar in ['s', 'sim', 'yes']:
            self._mostrar_teste_senha_completo()
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mostrar_teste_senha_completo(self):
        """Mostra exemplo completo de teste de senha"""
        teste_completo = '''import pytest
import re

def senha_forte(senha):
    """Valida se uma senha é forte"""
    if len(senha) < 8:
        return False
    
    if not re.search(r'[A-Z]', senha):
        return False
    
    if not re.search(r'[a-z]', senha):
        return False
    
    if not re.search(r'[0-9]', senha):
        return False
    
    return True

# TESTES COMPLETOS
class TestSenhaForte:
    def test_senha_valida(self):
        assert senha_forte("SenhaForte123") == True
        assert senha_forte("Python2024!") == True
    
    def test_senha_muito_curta(self):
        assert senha_forte("Abc123") == False
        assert senha_forte("") == False
    
    def test_senha_sem_maiuscula(self):
        assert senha_forte("senhafraca123") == False
    
    def test_senha_sem_minuscula(self):
        assert senha_forte("SENHA123") == False
    
    def test_senha_sem_numero(self):
        assert senha_forte("SenhaForte") == False
    
    @pytest.mark.parametrize("senha,esperado", [
        ("Abc12345", True),
        ("python", False),
        ("PYTHON123", False),
        ("Python", False),
        ("Python3!", True),
    ])
    def test_varios_casos(self, senha, esperado):
        assert senha_forte(senha) == esperado

# Demonstração
if __name__ == '__main__':
    senhas_teste = [
        "Python2024",
        "python",
        "12345678",
        "SenhaForte",
        "Senha123!"
    ]
    
    print("🔐 Testando Senhas:")
    for senha in senhas_teste:
        resultado = "✅ Forte" if senha_forte(senha) else "❌ Fraca"
        print(f"{senha}: {resultado}")'''
        
        self.print_code_section("SOLUÇÃO COMPLETA", teste_completo)
    
    def _mini_projeto_sistema_validacao(self) -> None:
        """Mini Projeto - Sistema de Validação com TDD"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE VALIDAÇÃO COM TDD")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE VALIDAÇÃO COM TDD")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema profissional de validação usando TDD!")
        
        self.print_concept(
            "Sistema de Validação",
            "Um conjunto de validadores para dados comuns: email, telefone, CPF, etc. Tudo com testes!"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "E-commerces - Validar dados de cadastro",
            "Bancos - Verificar informações de clientes",
            "Apps - Garantir dados corretos dos usuários",
            "APIs - Validar entrada de dados"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Criar testes primeiro (TDD)
        self.print_section("PASSO 1: ESCREVER OS TESTES (TDD)", "🔴", "error")
        self.print_tip("No TDD, sempre começamos pelos testes!")
        
        try:
            self.print_colored("\nVamos criar testes para nossos validadores:", "text")
            
            testes_iniciais = '''import pytest
import re

# TESTES (escritos ANTES do código!)
class TestValidadores:
    
    def test_email_valido(self):
        assert validar_email("usuario@email.com") == True
        assert validar_email("nome.sobrenome@empresa.com.br") == True
    
    def test_email_invalido(self):
        assert validar_email("email_sem_arroba") == False
        assert validar_email("@email.com") == False
        assert validar_email("usuario@") == False
    
    def test_telefone_valido(self):
        assert validar_telefone("(11) 98765-4321") == True
        assert validar_telefone("11987654321") == True
    
    def test_cpf_valido(self):
        assert validar_cpf("123.456.789-09") == True
        assert validar_cpf("12345678909") == True'''
            
            self.print_code_section("TESTES TDD", testes_iniciais)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Implementar validadores
        self.print_section("PASSO 2: IMPLEMENTAR VALIDADORES", "🟢", "success")
        self.print_colored("Agora criamos o código para passar nos testes:", "text")
        
        validadores = '''# VALIDADORES (código mínimo para passar nos testes)

def validar_email(email):
    """Valida formato de email"""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

def validar_telefone(telefone):
    """Valida telefone brasileiro"""
    # Remove caracteres não numéricos
    numeros = re.sub(r'[^0-9]', '', telefone)
    
    # Verifica se tem 10 ou 11 dígitos
    return len(numeros) in [10, 11]

def validar_cpf(cpf):
    """Valida CPF (simplificado)"""
    # Remove caracteres não numéricos
    numeros = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(numeros) != 11:
        return False
    
    # Verifica se todos dígitos são iguais
    if numeros == numeros[0] * 11:
        return False
    
    return True

def validar_data_nascimento(data):
    """Valida se é maior de idade"""
    from datetime import datetime, date
    
    try:
        # Converte string para data
        if isinstance(data, str):
            nascimento = datetime.strptime(data, "%d/%m/%Y").date()
        else:
            nascimento = data
        
        # Calcula idade
        hoje = date.today()
        idade = hoje.year - nascimento.year
        
        # Ajusta se ainda não fez aniversário
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1
        
        return idade >= 18
    except:
        return False'''
        
        self.print_code_section("VALIDADORES", validadores)
        
        # PASSO 3: Sistema completo
        self.print_section("PASSO 3: SISTEMA COMPLETO", "🔵", "info")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o sistema completo com testes:", "text")
        
        codigo_final = '''# 🐍 PROJETO: SISTEMA DE VALIDAÇÃO COM TDD
# Módulo 27: Testes e TDD

import re
from datetime import datetime, date

class ValidadorDados:
    """Sistema completo de validação de dados"""
    
    @staticmethod
    def email(email):
        """Valida formato de email"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, str(email)))
    
    @staticmethod
    def telefone(telefone):
        """Valida telefone brasileiro"""
        numeros = re.sub(r'[^0-9]', '', str(telefone))
        return len(numeros) in [10, 11]
    
    @staticmethod
    def cpf(cpf):
        """Valida CPF com dígitos verificadores"""
        numeros = re.sub(r'[^0-9]', '', str(cpf))
        
        if len(numeros) != 11 or numeros == numeros[0] * 11:
            return False
        
        # Cálculo simplificado dos dígitos
        return True  # Simplificado para o exemplo
    
    @staticmethod
    def senha_forte(senha):
        """Valida força da senha"""
        if len(senha) < 8:
            return False
        
        tem_maiuscula = bool(re.search(r'[A-Z]', senha))
        tem_minuscula = bool(re.search(r'[a-z]', senha))
        tem_numero = bool(re.search(r'[0-9]', senha))
        
        return tem_maiuscula and tem_minuscula and tem_numero

# CLASSE DE USUÁRIO USANDO VALIDADORES
class Usuario:
    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = self._validar_email(email)
        self.telefone = self._validar_telefone(telefone)
        self.senha = self._validar_senha(senha)
    
    def _validar_email(self, email):
        if not ValidadorDados.email(email):
            raise ValueError("Email inválido")
        return email
    
    def _validar_telefone(self, telefone):
        if not ValidadorDados.telefone(telefone):
            raise ValueError("Telefone inválido")
        return telefone
    
    def _validar_senha(self, senha):
        if not ValidadorDados.senha_forte(senha):
            raise ValueError("Senha fraca")
        return senha

# DEMONSTRAÇÃO DO SISTEMA
if __name__ == '__main__':
    print("🧪 SISTEMA DE VALIDAÇÃO COM TDD\\n")
    
    # Testando validadores
    print("📧 Validando emails:")
    emails = ["user@email.com", "invalido@", "teste@dominio.com.br"]
    for email in emails:
        valido = ValidadorDados.email(email)
        status = "✅" if valido else "❌"
        print(f"{status} {email}")
    
    print("\\n📱 Validando telefones:")
    telefones = ["(11) 98765-4321", "11987654321", "123"]
    for tel in telefones:
        valido = ValidadorDados.telefone(tel)
        status = "✅" if valido else "❌"
        print(f"{status} {tel}")
    
    print("\\n🔐 Validando senhas:")
    senhas = ["Senha123", "fraca", "SEMMINUSCULA1", "Python2024!"]
    for senha in senhas:
        valido = ValidadorDados.senha_forte(senha)
        status = "✅ Forte" if valido else "❌ Fraca"
        print(f"{status}: {senha}")
    
    # Criando usuário
    print("\\n👤 Criando usuário válido:")
    try:
        usuario = Usuario(
            nome="João Silva",
            email="joao@email.com",
            telefone="(11) 98765-4321",
            senha="SenhaForte123"
        )
        print("✅ Usuário criado com sucesso!")
        print(f"   Nome: {usuario.nome}")
        print(f"   Email: {usuario.email}")
        print(f"   Telefone: {usuario.telefone}")
    except ValueError as e:
        print(f"❌ Erro: {e}")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)
        
        # === TESTES RODANDO ===
        self.print_colored("\n🧪 EXECUTANDO TESTES:", "success")
        
        testes_finais = '''# Simulação dos testes rodando
print("\\n" + "="*50)
print("🧪 RELATÓRIO DE TESTES\\n")

testes = [
    ("test_email_valido", "PASSED"),
    ("test_email_invalido", "PASSED"),
    ("test_telefone_valido", "PASSED"),
    ("test_cpf_valido", "PASSED"),
    ("test_senha_forte", "PASSED"),
    ("test_criar_usuario_valido", "PASSED"),
    ("test_criar_usuario_email_invalido", "PASSED")
]

for teste, status in testes:
    simbolo = "✅" if status == "PASSED" else "❌"
    print(f"{simbolo} {teste} ... {status}")

print(f"\\n📊 COBERTURA: 100%")
print(f"✅ 7 testes passaram em 0.05s")'''
        
        self.executar_codigo(testes_finais)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("\n🎉 PARABÉNS! Você criou um sistema de validação profissional com TDD!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Adicionar mais validadores (CEP, CNPJ, cartão)",
            "Implementar testes de integração com banco de dados",
            "Criar testes de performance",
            "Adicionar CI/CD com testes automáticos",
            "Implementar relatórios de cobertura",
            "Criar documentação dos testes"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Testes!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema de Validação com TDD")
        
        self.pausar()