#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 16: Tratamento de Exceções
Aprenda a lidar com erros de forma profissional
"""

from ..shared.base_module import BaseModule


class Modulo16Excecoes(BaseModule):
    """Módulo 16: Tratamento de Exceções - Lidando com Erros"""
    
    def __init__(self):
        super().__init__("modulo_16", "Tratamento de Exceções")
        self.has_mini_project = True
        self.mini_project_points = 80
    
    def execute(self) -> None:
        """Executa o módulo sobre tratamento de exceções"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._excecoes_module()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _excecoes_module(self) -> None:
        """Conteúdo principal sobre tratamento de exceções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚠️ MÓDULO 16: TRATAMENTO DE EXCEÇÕES")
        else:
            print("\n" + "="*60)
            print("⚠️ MÓDULO 16: TRATAMENTO DE EXCEÇÕES")
            print("="*60)
        
        print("🛡️ Aprenda a lidar com erros de forma profissional!")
        print("🎯 Tópicos abordados:")
        print("• Try/except/finally")
        print("• Tipos de exceções")
        print("• Criando exceções customizadas")
        print("• Boas práticas de tratamento")
        print("• Logging de erros")
        print("• Debugging e análise de erros")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        self._conceitos_basicos()
        self._tipos_excecoes()
        self._excecoes_customizadas()
        self._boas_praticas()
        self._mini_projeto_exception_handler()
        
        # Marcar módulo como completo
        if self.progress:
            self.progress.complete_module(self.module_id)
            print(f"\n🎉 Módulo {self.module_id} concluído!")
    
    def _conceitos_basicos(self):
        """Conceitos básicos de exceções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📚 CONCEITOS BÁSICOS DE EXCEÇÕES")
        
        print("🔍 O que são exceções?")
        print("• Eventos que interrompem o fluxo normal do programa")
        print("• Sinais de que algo deu errado")
        print("• Podem ser tratadas ou propagadas")
        
        print("\n🛠️ Estrutura try/except:")
        codigo_basico = '''
try:
    # Código que pode gerar erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("❌ Erro: Você deve digitar um número válido!")
except ZeroDivisionError:
    print("❌ Erro: Não é possível dividir por zero!")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
else:
    print("✅ Operação realizada com sucesso!")
finally:
    print("🔄 Esta mensagem sempre aparece!")
'''
        
        print(codigo_basico)
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _tipos_excecoes(self):
        """Tipos comuns de exceções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🏷️ TIPOS COMUNS DE EXCEÇÕES")
        
        print("📋 Exceções mais frequentes:")
        
        tipos_excecoes = [
            ("ValueError", "Valor inválido para o tipo esperado"),
            ("TypeError", "Tipo de dados incorreto"),
            ("KeyError", "Chave não encontrada em dicionário"),
            ("IndexError", "Índice fora do range de uma lista"),
            ("FileNotFoundError", "Arquivo não encontrado"),
            ("ZeroDivisionError", "Divisão por zero"),
            ("AttributeError", "Atributo não existe no objeto"),
            ("ImportError", "Módulo não pode ser importado"),
            ("ConnectionError", "Problemas de conexão"),
            ("TimeoutError", "Operação demorou muito")
        ]
        
        for excecao, descricao in tipos_excecoes:
            print(f"• {excecao}: {descricao}")
        
        print("\n💡 Exemplo prático:")
        exemplo_tipos = '''
# Diferentes tipos de erros
def demonstrar_excecoes():
    exemplos = [
        lambda: int("abc"),           # ValueError
        lambda: "texto" + 5,          # TypeError  
        lambda: {"a": 1}["b"],        # KeyError
        lambda: [1, 2, 3][10],        # IndexError
        lambda: open("inexistente.txt"),  # FileNotFoundError
        lambda: 10 / 0,               # ZeroDivisionError
    ]
    
    for i, exemplo in enumerate(exemplos):
        try:
            resultado = exemplo()
            print(f"Exemplo {i+1}: {resultado}")
        except Exception as e:
            print(f"Exemplo {i+1}: {type(e).__name__} - {e}")

demonstrar_excecoes()
'''
        
        print(exemplo_tipos)
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _excecoes_customizadas(self):
        """Criando exceções customizadas"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("⚙️ EXCEÇÕES CUSTOMIZADAS")
        
        print("🔨 Criando suas próprias exceções:")
        
        excecoes_custom = '''
# Exceção base customizada
class MeuAppError(Exception):
    """Exceção base para erros do meu aplicativo"""
    pass

# Exceções específicas
class IdadeInvalidaError(MeuAppError):
    """Erro quando idade é inválida"""
    def __init__(self, idade, mensagem="Idade deve estar entre 0 e 150"):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class SaldoInsuficienteError(MeuAppError):
    """Erro quando saldo da conta é insuficiente"""
    def __init__(self, saldo_atual, valor_tentativa):
        self.saldo_atual = saldo_atual
        self.valor_tentativa = valor_tentativa
        mensagem = f"Saldo insuficiente: R${saldo_atual:.2f} < R${valor_tentativa:.2f}"
        super().__init__(mensagem)

# Usando exceções customizadas
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        return self.saldo

# Exemplo de uso
try:
    conta = ContaBancaria(100)
    conta.sacar(150)  # Vai gerar erro
except SaldoInsuficienteError as e:
    print(f"❌ {e}")
    print(f"💰 Saldo atual: R${e.saldo_atual:.2f}")
    print(f"💸 Tentativa: R${e.valor_tentativa:.2f}")
'''
        
        print(excecoes_custom)
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _boas_praticas(self):
        """Boas práticas no tratamento de exceções"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ BOAS PRÁTICAS")
        
        print("🎯 Regras de ouro para tratamento de exceções:")
        
        praticas = [
            "1. Seja específico: capture exceções específicas, não Exception genérica",
            "2. Falhe rápido: não mascare erros desnecessariamente", 
            "3. Log apropriado: registre erros para debugging",
            "4. Cleanup: use finally para limpeza de recursos",
            "5. Contexto: forneça informações úteis sobre o erro",
            "6. Não silencie: nunca use 'except: pass' sem motivo",
            "7. Re-raise quando necessário: propague erros que não pode tratar"
        ]
        
        for pratica in praticas:
            print(f"• {pratica}")
        
        print("\n💡 Exemplo de boas práticas:")
        
        exemplo_praticas = '''
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def processar_arquivo(nome_arquivo):
    """Exemplo de tratamento robusto de exceções"""
    arquivo = None
    try:
        # Operação que pode falhar
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.read()
        
        # Processamento que pode falhar
        resultado = processar_dados(dados)
        
        logger.info(f"Arquivo {nome_arquivo} processado com sucesso")
        return resultado
        
    except FileNotFoundError:
        logger.error(f"Arquivo {nome_arquivo} não encontrado")
        raise  # Re-propaga o erro
        
    except PermissionError:
        logger.error(f"Sem permissão para ler {nome_arquivo}")
        raise
        
    except Exception as e:
        logger.error(f"Erro inesperado ao processar {nome_arquivo}: {e}")
        raise  # Re-propaga erro não tratado
        
    finally:
        # Limpeza sempre executada
        if arquivo and not arquivo.closed:
            arquivo.close()
            logger.info(f"Arquivo {nome_arquivo} fechado")

def processar_dados(dados):
    """Simula processamento de dados"""
    if not dados.strip():
        raise ValueError("Dados vazios não podem ser processados")
    return len(dados.split())
'''
        
        print(exemplo_praticas)
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _mini_projeto_exception_handler(self):
        """Mini projeto: Sistema de Exception Handler"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 MINI PROJETO: EXCEPTION HANDLER")
        
        print("📊 Vamos criar um sistema robusto de tratamento de exceções!")
        print("🎯 Funcionalidades:")
        print("• Decorador para captura automática de exceções")
        print("• Logger personalizado para erros")
        print("• Sistema de retry automático")
        print("• Notificações de erro")
        
        input("\n🔸 Pressione ENTER para ver o código...")
        
        codigo_projeto = '''
import functools
import logging
import time
from typing import Callable, Any

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class ExceptionHandler:
    """Sistema avançado de tratamento de exceções"""
    
    def __init__(self, logger_name="ExceptionHandler"):
        self.logger = logging.getLogger(logger_name)
    
    def handle_exceptions(self, 
                         max_retries=3, 
                         delay=1, 
                         exceptions=(Exception,),
                         notify=True):
        """
        Decorador para tratamento automático de exceções
        
        Args:
            max_retries: Número máximo de tentativas
            delay: Delay entre tentativas (segundos)
            exceptions: Tupla de exceções para capturar
            notify: Se deve notificar sobre erros
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                last_exception = None
                
                for tentativa in range(max_retries + 1):
                    try:
                        result = func(*args, **kwargs)
                        
                        if tentativa > 0:
                            self.logger.info(
                                f"✅ {func.__name__} executada com sucesso "
                                f"na tentativa {tentativa + 1}"
                            )
                        
                        return result
                        
                    except exceptions as e:
                        last_exception = e
                        
                        self.logger.warning(
                            f"⚠️ Tentativa {tentativa + 1} falhou em {func.__name__}: {e}"
                        )
                        
                        if tentativa < max_retries:
                            self.logger.info(f"🔄 Tentando novamente em {delay}s...")
                            time.sleep(delay)
                        else:
                            self.logger.error(
                                f"❌ {func.__name__} falhou após {max_retries + 1} tentativas"
                            )
                            
                            if notify:
                                self.notify_error(func.__name__, last_exception)
                            
                            raise last_exception
                
            return wrapper
        return decorator
    
    def notify_error(self, function_name: str, exception: Exception):
        """Notifica sobre erro crítico"""
        message = f"""
        🚨 ERRO CRÍTICO DETECTADO 🚨
        
        Função: {function_name}
        Erro: {type(exception).__name__}
        Mensagem: {str(exception)}
        Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
        
        Ação necessária: Verificar logs e corrigir problema.
        """
        
        print(message)
        self.logger.critical(f"ERRO CRÍTICO em {function_name}: {exception}")

# Exemplo de uso
handler = ExceptionHandler()

@handler.handle_exceptions(max_retries=2, delay=0.5)
def operacao_instavel():
    """Simula operação que pode falhar"""
    import random
    
    if random.random() < 0.7:  # 70% chance de falhar
        raise ConnectionError("Falha na conexão com servidor")
    
    return "✅ Operação realizada com sucesso!"

@handler.handle_exceptions(exceptions=(ValueError, TypeError))
def calcular_media(numeros):
    """Calcula média de uma lista de números"""
    if not numeros:
        raise ValueError("Lista de números não pode estar vazia")
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise TypeError("Todos os elementos devem ser números")
    
    return sum(numeros) / len(numeros)

# Demonstração
print("=== TESTANDO SISTEMA DE EXCEPTION HANDLER ===")

# Teste 1: Operação instável
try:
    resultado = operacao_instavel()
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Falha final: {e}")

# Teste 2: Cálculo de média
try:
    media = calcular_media([1, 2, 3, 4, 5])
    print(f"Média: {media}")
    
    # Teste com erro
    media = calcular_media([])
except Exception as e:
    print(f"Erro no cálculo: {e}")
'''
        
        print(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Você criou um sistema robusto de exception handling!")
        print("🎯 Aplicação real: sistemas críticos que precisam de alta confiabilidade")
        
        # Registra conclusão do mini projeto  
        if hasattr(self, 'complete_mini_project'):
            self.complete_mini_project("Sistema de Exception Handler")
        
        input("\n🔸 Pressione ENTER para finalizar...")


# Para teste standalone
if __name__ == "__main__":
    module = Modulo16Excecoes()
    print("Teste do módulo 16 - versão standalone")
    module._excecoes_module()