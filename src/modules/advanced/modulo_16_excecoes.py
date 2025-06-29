#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 16: Tratamento de Exceções
Aprenda a lidar com erros de forma profissional
"""

from ..shared.base_module import BaseModule


class Modulo16Excecoes(BaseModule):
    """Módulo 16: Dominando Tratamento de Exceções"""
    
    def __init__(self):
        super().__init__("modulo_16", "Tratamento de Exceções")
        self.has_mini_project = True
        self.mini_project_points = 90
    
    def execute(self) -> None:
        """Executa o módulo Tratamento de Exceções"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._excecoes_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _excecoes_interativo(self) -> None:
        """Conteúdo principal do módulo Tratamento de Exceções"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🛡️ MÓDULO 16: DOMINANDO TRATAMENTO DE EXCEÇÕES")
        else:
            print("\n" + "="*50)
            print("🛡️ MÓDULO 16: DOMINANDO TRATAMENTO DE EXCEÇÕES")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos aprender a transformar erros em oportunidades como os profissionais!")
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
            self._mini_projeto_sistema_robusto_excecoes()
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
                'id': 'secao_conceito_excecoes',
                'titulo': '🎯 O que são exceções na programação?',
                'descricao': 'Entenda como erros se transformam em oportunidades',
                'funcao': self._secao_conceito_excecoes
            },
            {
                'id': 'secao_try_except_finally',
                'titulo': '⚙️ Como capturar e tratar erros?',
                'descricao': 'Domine try, except, else e finally',
                'funcao': self._secao_try_except_finally
            },
            {
                'id': 'secao_tipos_excecoes',
                'titulo': '🏷️ Tipos de exceções mais comuns',
                'descricao': 'ValueError, TypeError, KeyError e muito mais',
                'funcao': self._secao_tipos_excecoes
            },
            {
                'id': 'secao_excecoes_customizadas',
                'titulo': '🔧 Criando exceções personalizadas',
                'descricao': 'Desenvolva seus próprios tipos de erro',
                'funcao': self._secao_excecoes_customizadas
            },
            {
                'id': 'secao_boas_praticas',
                'titulo': '⭐ Boas práticas e patterns profissionais',
                'descricao': 'Como os experts tratam erros em sistemas reais',
                'funcao': self._secao_boas_praticas
            },
            {
                'id': 'secao_debugging_logging',
                'titulo': '🔍 Debugging e logging de erros',
                'descricao': 'Técnicas para rastrear e registrar problemas',
                'funcao': self._secao_debugging_logging
            },
            {
                'id': 'secao_curiosidades',
                'titulo': '💫 Curiosidades sobre exceções',
                'descricao': 'Fatos interessantes do mundo da programação',
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
    
    def _secao_conceito_excecoes(self) -> None:
        """Seção: O que são exceções na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("CONCEITO DE EXCEÇÕES", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Exceção",
            "Um evento que interrompe o fluxo normal do programa quando algo inesperado acontece"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Exceções não são o fim do mundo - são oportunidades para criar programas mais robustos!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você está dirigindo e de repente encontra uma rua bloqueada. ", "text")
        self.print_colored("Você tem duas opções: parar o carro e desistir, ou encontrar uma rota alternativa.", "text")
        self.print_colored("Exceções em Python funcionam igual: quando algo dá errado, você pode ", "text")
        self.print_colored("'capturar' o problema e definir o que fazer em seguida!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 🏃 Python executa o código linha por linha normalmente",
            "2. 💥 Quando encontra um problema, 'levanta' (raise) uma exceção",
            "3. 🛡️ Se você colocou um 'try/except', ele captura o erro",
            "4. 🔄 Seu programa continua executando com o plano alternativo",
            "5. 🚀 Resultado: programa resiliente que não quebra facilmente"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Sem tratamento de exceção - PERIGOSO!
idade = int(input("Sua idade: "))  # E se alguém digitar "abc"?
print(f"Você nasceu em {2024 - idade}")

# Com tratamento de exceção - SEGURO!
try:
    idade = int(input("Sua idade: "))
    print(f"Você nasceu em {2024 - idade}")
except ValueError:
    print("❌ Por favor, digite apenas números!")'''
        self.exemplo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "Netflix: tratamento de falhas de conexão durante streaming",
            "Bancos: proteção contra transações inválidas ou falhas de sistema",
            "WhatsApp: recuperação quando mensagens não conseguem ser enviadas",
            "Jogos: prevenção de crashes quando arquivos estão corrompidos"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_try_except_finally(self) -> None:
        """Seção: Como capturar e tratar erros?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("TRY, EXCEPT, ELSE E FINALLY", "⚙️", "success")
        
        # === EXPLICAÇÃO DA ESTRUTURA ===
        self.print_concept(
            "Bloco Try/Except",
            "Uma estrutura que permite 'tentar' executar código e reagir se algo der errado"
        )
        
        self.print_colored("\n🏗️ ANATOMIA COMPLETA:", "info")
        self.print_colored("• TRY: 'Tente executar este código'", "text")
        self.print_colored("• EXCEPT: 'Se der erro X, faça isso'", "text")
        self.print_colored("• ELSE: 'Se não deu nenhum erro, faça isso'", "text")
        self.print_colored("• FINALLY: 'Sempre execute isso, dê certo ou errado'", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplos...")
        
        # === EXEMPLO SIMPLES ===
        self.print_colored("\n📝 EXEMPLO BÁSICO:", "warning")
        exemplo_basico = '''try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"10 ÷ {numero} = {resultado}")
except ValueError:
    print("❌ Isso não é um número válido!")
except ZeroDivisionError:
    print("❌ Não posso dividir por zero!")
else:
    print("✅ Cálculo realizado com sucesso!")
finally:
    print("🏁 Operação finalizada.")'''
        
        self.print_code_section("CÓDIGO", exemplo_basico)
        
        print("\n🚀 Vamos simular diferentes cenários:")
        input("🔸 Pressione ENTER para continuar...")
        
        # === MÚLTIPLAS EXCEÇÕES ===
        self.print_colored("\n🎯 CAPTURANDO MÚLTIPLAS EXCEÇÕES:", "info")
        exemplo_multiplo = '''# Método 1: Exceções separadas
try:
    dados = {"nome": "João", "idade": 25}
    chave = input("Que informação quer? ")
    valor = dados[chave]
    numero = int(valor)
except KeyError:
    print("❌ Essa informação não existe!")
except ValueError:
    print("❌ Não consegui converter para número!")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")

# Método 2: Múltiplas exceções juntas
try:
    # código que pode falhar
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"❌ Erro conhecido: {e}")'''
        
        self.exemplo(exemplo_multiplo)
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === DICAS PROFISSIONAIS ===
        self.print_colored("\n⭐ DICAS DE PROFISSIONAIS:", "accent")
        dicas = [
            "Sempre capture exceções específicas primeiro, genéricas depois",
            "Use 'as e' para acessar detalhes do erro",
            "FINALLY é perfeito para limpar recursos (fechar arquivos, conexões)",
            "ELSE só executa se NÃO houve exceções - ótimo para logs de sucesso"
        ]
        for dica in dicas:
            self.print_colored(f"💡 {dica}", "text")
        
        self.pausar()
    
    def _secao_tipos_excecoes(self) -> None:
        """Seção: Tipos de exceções mais comuns"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("GUIA DAS EXCEÇÕES MAIS COMUNS", "🏷️", "success")
        
        # === INTRODUÇÃO ===
        self.print_colored("Python tem dezenas de tipos de exceções diferentes!", "text")
        self.print_colored("Vamos conhecer as mais importantes para seu dia a dia:", "text")
        
        input("\n🔸 Pressione ENTER para ver os 'Top 10' mais comuns...")
        
        # === TOP 10 EXCEÇÕES ===
        tipos_excecoes = [
            {
                'nome': 'ValueError',
                'descricao': 'Valor correto, mas conteúdo inválido',
                'exemplo': 'int("abc")  # String não é número',
                'situacao': 'Conversão de tipos com dados inválidos'
            },
            {
                'nome': 'TypeError',
                'descricao': 'Operação incompatível com o tipo',
                'exemplo': '"texto" + 5  # Não pode somar string com número',
                'situacao': 'Misturar tipos incompatíveis'
            },
            {
                'nome': 'KeyError',
                'descricao': 'Chave não existe no dicionário',
                'exemplo': 'pessoa["altura"]  # Se "altura" não existe',
                'situacao': 'Acessar dados que podem não existir'
            },
            {
                'nome': 'IndexError',
                'descricao': 'Posição fora dos limites da lista',
                'exemplo': 'lista[10]  # Se lista tem só 5 itens',
                'situacao': 'Acessar posições dinâmicas em listas'
            },
            {
                'nome': 'FileNotFoundError',
                'descricao': 'Arquivo ou diretório não encontrado',
                'exemplo': 'open("arquivo_inexistente.txt")',
                'situacao': 'Trabalhar com arquivos do usuário'
            },
            {
                'nome': 'ZeroDivisionError',
                'descricao': 'Tentativa de dividir por zero',
                'exemplo': '10 / 0  # Matemática não permite!',
                'situacao': 'Cálculos com dados do usuário'
            },
            {
                'nome': 'AttributeError',
                'descricao': 'Atributo/método não existe no objeto',
                'exemplo': '"texto".append("x")  # Strings não têm append',
                'situacao': 'Usar métodos em tipos diferentes'
            },
            {
                'nome': 'ImportError',
                'descricao': 'Módulo não pode ser importado',
                'exemplo': 'import modulo_inexistente',
                'situacao': 'Dependências opcionais ou faltando'
            },
            {
                'nome': 'ConnectionError',
                'descricao': 'Problemas de rede/conexão',
                'exemplo': 'requests.get("site_offline.com")',
                'situacao': 'Comunicação com APIs e serviços'
            },
            {
                'nome': 'PermissionError',
                'descricao': 'Sem permissão para acessar recurso',
                'exemplo': 'open("/sistema/arquivo_protegido.txt")',
                'situacao': 'Trabalhar com arquivos do sistema'
            }
        ]
        
        for i, excecao in enumerate(tipos_excecoes, 1):
            self.print_colored(f"\n{i}. {excecao['nome']} 🔥", "warning")
            self.print_colored(f"   📝 {excecao['descricao']}", "text")
            self.print_colored(f"   💻 Exemplo: {excecao['exemplo']}", "accent")
            self.print_colored(f"   🌍 Quando: {excecao['situacao']}", "info")
            
            if i % 3 == 0 and i < len(tipos_excecoes):
                input("\n   ⏳ Pressione ENTER para continuar...")
        
        # === DEMONSTRAÇÃO PRÁTICA ===
        input("\n🔸 Pressione ENTER para ver todas em ação...")
        
        self.print_colored("\n🚀 DEMONSTRAÇÃO AO VIVO:", "success")
        codigo_demonstracao = '''def demonstrar_excecoes():
    """Mostra diferentes tipos de exceções"""
    
    exemplos = [
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: "texto" + 5),
        ("KeyError", lambda: {"nome": "João"}["idade"]),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("AttributeError", lambda: "texto".append("x"))
    ]
    
    for nome, funcao in exemplos:
        try:
            resultado = funcao()
            print(f"✅ {nome}: {resultado}")
        except Exception as e:
            print(f"❌ {nome}: {type(e).__name__} - {e}")

# Executando demonstração
demonstrar_excecoes()'''
        
        self.exemplo(codigo_demonstracao)
        
        print("\n🔥 Executando demonstração:")
        # Simula a execução mostrando os erros
        resultados = [
            "❌ ValueError: invalid literal for int() with base 10: 'abc'",
            "❌ TypeError: can only concatenate str (not \"int\") to str",
            "❌ KeyError: 'idade'",
            "❌ IndexError: list index out of range",
            "❌ ZeroDivisionError: division by zero",
            "❌ AttributeError: 'str' object has no attribute 'append'"
        ]
        
        for resultado in resultados:
            print(f"  {resultado}")
        
        self.print_success("\n🎯 Agora você reconhece os erros mais comuns em Python!")
        self.pausar()
    
    def _secao_excecoes_customizadas(self) -> None:
        """Seção: Criando exceções personalizadas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CRIANDO SUAS PRÓPRIAS EXCEÇÕES", "🔧", "success")
        
        # === CONCEITO ===
        self.print_concept(
            "Exceção Customizada",
            "Uma classe de erro criada por você para situações específicas do seu programa"
        )
        
        self.print_tip("Exceções customizadas tornam seu código mais profissional e fácil de debugar!")
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como criar placas personalizadas para sua casa:", "text")
        self.print_colored("• Em vez de 'ERRO GENÉRICO', você coloca 'SALDO INSUFICIENTE'", "text")
        self.print_colored("• Em vez de 'PROBLEMA', você explica 'IDADE DEVE SER ENTRE 18 E 65'", "text")
        self.print_colored("Assim, quem vê o erro entende exatamente o que aconteceu!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === ESTRUTURA BÁSICA ===
        self.print_colored("\n🏗️ ESTRUTURA BÁSICA:", "info")
        
        estrutura_basica = '''# 1. Exceção base para seu projeto
class MeuProjetoError(Exception):
    """Exceção base para todos os erros do meu projeto"""
    pass

# 2. Exceções específicas
class IdadeInvalidaError(MeuProjetoError):
    """Quando idade não atende os critérios"""
    pass

class SaldoInsuficienteError(MeuProjetoError):
    """Quando não há dinheiro suficiente"""
    pass'''
        
        self.print_code_section("ESTRUTURA BASE", estrutura_basica)
        input("\n🔸 Pressione ENTER para exemplo avançado...")
        
        # === EXEMPLO AVANÇADO ===
        self.print_colored("\n🚀 EXEMPLO PROFISSIONAL - SISTEMA BANCÁRIO:", "success")
        
        exemplo_avancado = '''class SistemaBancarioError(Exception):
    """Exceção base para o sistema bancário"""
    def __init__(self, mensagem, codigo_erro=None):
        super().__init__(mensagem)
        self.codigo_erro = codigo_erro
        self.timestamp = datetime.now()

class SaldoInsuficienteError(SistemaBancarioError):
    """Saldo insuficiente para operação"""
    def __init__(self, saldo_atual, valor_tentativa):
        self.saldo_atual = saldo_atual
        self.valor_tentativa = valor_tentativa
        mensagem = f"Saldo R${saldo_atual:.2f} insuficiente para R${valor_tentativa:.2f}"
        super().__init__(mensagem, codigo_erro="SALDO_INSUF")

class ContaInexistenteError(SistemaBancarioError):
    """Conta não encontrada no sistema"""
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        mensagem = f"Conta {numero_conta} não encontrada"
        super().__init__(mensagem, codigo_erro="CONTA_N_ENCONTRADA")

# Usando no código
class ContaBancaria:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        return self.saldo
    
    def transferir(self, valor, conta_destino):
        if not conta_destino:
            raise ContaInexistenteError("N/A")
        # Lógica de transferência...

# Tratamento inteligente
try:
    conta = ContaBancaria("12345-6", 100)
    conta.sacar(150)
except SaldoInsuficienteError as e:
    print(f"❌ {e}")
    print(f"📊 Código: {e.codigo_erro}")
    print(f"💰 Saldo: R${e.saldo_atual:.2f}")
    print(f"💸 Tentativa: R${e.valor_tentativa:.2f}")
except SistemaBancarioError as e:
    print(f"❌ Erro do sistema: {e}")
    print(f"📊 Código: {e.codigo_erro}")
    print(f"⏰ Timestamp: {e.timestamp}")'''
        
        self.exemplo(exemplo_avancado)
        
        # === VANTAGENS ===
        self.print_colored("\n⭐ VANTAGENS DAS EXCEÇÕES CUSTOMIZADAS:", "accent")
        vantagens = [
            "🎯 Erros específicos e claros para o usuário",
            "🔍 Mais fácil de debugar e encontrar problemas",
            "📊 Dados extras (códigos, timestamps, contexto)",
            "🏢 Código mais profissional e organizando",
            "🔧 Tratamento diferenciado para cada tipo de erro"
        ]
        for vantagem in vantagens:
            self.print_colored(f"  {vantagem}", "text")
        
        self.pausar()
    
    def _secao_boas_praticas(self) -> None:
        """Seção: Boas práticas e patterns profissionais"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("BOAS PRÁTICAS PROFISSIONAIS", "⭐", "success")
        
        # === INTRODUÇÃO ===
        self.print_colored("Como os experts do Vale do Silício tratam exceções:", "text")
        self.print_tip("Estas práticas são usadas em empresas como Google, Facebook e Netflix!")
        
        input("\n🔸 Pressione ENTER para conhecer as regras de ouro...")
        
        # === REGRAS DE OURO ===
        self.print_colored("\n🏆 AS 7 REGRAS DE OURO:", "warning")
        
        regras = [
            {
                'numero': '1',
                'titulo': 'Seja Específico',
                'descricao': 'Capture exceções específicas, não Exception genérica',
                'ruim': 'except Exception:',
                'bom': 'except (ValueError, TypeError):'
            },
            {
                'numero': '2',
                'titulo': 'Falhe Rápido',
                'descricao': 'Não mascare erros que não consegue resolver',
                'ruim': 'except Exception: pass',
                'bom': 'except ValueError: raise  # Re-propaga'
            },
            {
                'numero': '3',
                'titulo': 'Log Inteligente',
                'descricao': 'Registre erros com contexto útil para debugging',
                'ruim': 'print("Erro!")',
                'bom': 'logger.error(f"Erro ao processar {arquivo}: {e}")'
            },
            {
                'numero': '4',
                'titulo': 'Cleanup Automático',
                'descricao': 'Use finally para limpeza garantida de recursos',
                'ruim': 'arquivo.close() # Pode não executar',
                'bom': 'finally: arquivo.close() # Sempre executa'
            },
            {
                'numero': '5',
                'titulo': 'Contexto Rico',
                'descricao': 'Forneça informações úteis sobre o erro',
                'ruim': 'ValueError("Erro")',
                'bom': 'ValueError(f"Idade {idade} inválida (deve ser 0-150)")'
            },
            {
                'numero': '6',
                'titulo': 'Nunca Silencie',
                'descricao': 'Sempre documente por que está ignorando um erro',
                'ruim': 'except: pass  # Silencia tudo',
                'bom': 'except ImportError: pass  # Módulo opcional'
            },
            {
                'numero': '7',
                'titulo': 'Re-raise Inteligente',
                'descricao': 'Propague erros que sua função não pode resolver',
                'ruim': 'except FileNotFoundError: return None',
                'bom': 'except FileNotFoundError: raise  # Deixa caller decidir'
            }
        ]
        
        for regra in regras:
            self.print_colored(f"\n{regra['numero']}. {regra['titulo']} 🎯", "accent")
            self.print_colored(f"   📝 {regra['descricao']}", "text")
            self.print_colored(f"   ❌ Ruim: {regra['ruim']}", "error")
            self.print_colored(f"   ✅ Bom: {regra['bom']}", "success")
            
            if int(regra['numero']) % 2 == 0:
                input("\n   ⏳ Pressione ENTER para continuar...")
        
        # === EXEMPLO PRÁTICO ===
        input("\n🔸 Pressione ENTER para ver exemplo prático...")
        
        self.print_colored("\n🚀 EXEMPLO PROFISSIONAL COMPLETO:", "success")
        
        exemplo_profissional = '''import logging
from pathlib import Path
from typing import Optional, List

# Configuração profissional de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class DataProcessorError(Exception):
    """Exceção base para processamento de dados"""
    pass

class InvalidDataError(DataProcessorError):
    """Dados inválidos ou corrompidos"""
    pass

def processar_arquivos_seguro(arquivos: List[str]) -> List[dict]:
    """
    Processa lista de arquivos com tratamento robusto
    
    Returns:
        Lista de resultados processados
    
    Raises:
        DataProcessorError: Para erros de processamento
        FileNotFoundError: Quando arquivos não existem
    """
    resultados = []
    arquivos_processados = 0
    
    try:
        logger.info(f"Iniciando processamento de {len(arquivos)} arquivos")
        
        for arquivo in arquivos:
            try:
                resultado = processar_arquivo_unico(arquivo)
                resultados.append(resultado)
                arquivos_processados += 1
                
                logger.debug(f"Arquivo {arquivo} processado com sucesso")
                
            except FileNotFoundError:
                logger.warning(f"Arquivo {arquivo} não encontrado - pulando")
                continue  # Arquivo opcional
                
            except PermissionError:
                logger.error(f"Sem permissão para ler {arquivo}")
                raise  # Erro crítico, interrompe processamento
                
            except InvalidDataError as e:
                logger.error(f"Dados inválidos em {arquivo}: {e}")
                # Adiciona erro aos resultados para análise
                resultados.append({
                    'arquivo': arquivo,
                    'erro': str(e),
                    'processado': False
                })
        
        logger.info(f"Processamento concluído: {arquivos_processados}/{len(arquivos)} arquivos")
        return resultados
        
    except Exception as e:
        logger.error(f"Erro inesperado no processamento: {e}")
        logger.info(f"Arquivos processados antes do erro: {arquivos_processados}")
        raise DataProcessorError(f"Falha no processamento após {arquivos_processados} arquivos") from e

def processar_arquivo_unico(caminho_arquivo: str) -> dict:
    """Processa um único arquivo com validação"""
    arquivo = None
    
    try:
        # Validação inicial
        path = Path(caminho_arquivo)
        if not path.exists():
            raise FileNotFoundError(f"Arquivo {caminho_arquivo} não encontrado")
        
        if path.stat().st_size == 0:
            raise InvalidDataError(f"Arquivo {caminho_arquivo} está vazio")
        
        # Processamento
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            
            if not conteudo:
                raise InvalidDataError("Conteúdo do arquivo está vazio")
            
            # Simula processamento
            return {
                'arquivo': caminho_arquivo,
                'tamanho': len(conteudo),
                'linhas': len(conteudo.split('\\n')),
                'processado': True
            }
            
    except UnicodeDecodeError:
        raise InvalidDataError(f"Arquivo {caminho_arquivo} não está em UTF-8")
    
    # Note: não precisa de finally pois usamos 'with' para o arquivo'''
        
        self.exemplo(exemplo_profissional)
        
        # === DICAS EXTRAS ===
        self.print_colored("\n💡 DICAS EXTRAS DOS PROFISSIONAIS:", "accent")
        dicas_extras = [
            "Use 'with' statements para gerenciamento automático de recursos",
            "Documente exceções que sua função pode levantar",
            "Crie hierarquias de exceções para diferentes módulos",
            "Use 'raise ... from e' para preservar stack trace original",
            "Configure logging estruturado para ambientes de produção"
        ]
        for dica in dicas_extras:
            self.print_colored(f"⚡ {dica}", "text")
        
        self.pausar()
    
    def _secao_debugging_logging(self) -> None:
        """Seção: Debugging e logging de erros"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DEBUGGING E LOGGING PROFISSIONAL", "🔍", "success")
        
        # === CONCEITO ===
        self.print_concept(
            "Logging",
            "Sistema de registro de eventos que ajuda a entender o que aconteceu no seu programa"
        )
        
        self.print_tip("Logs são como uma 'caixa preta' do seu programa - essencial para debugging!")
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você está dirigindo e o carro quebra.", "text")
        self.print_colored("Sem logs: 'O carro parou' - você não sabe o que aconteceu", "text")
        self.print_colored("Com logs: 'Motor aqueceu → Radiador vazou → Temperatura crítica'", "text")
        self.print_colored("Agora você sabe exatamente onde está o problema!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === NÍVEIS DE LOG ===
        self.print_colored("\n📊 NÍVEIS DE LOG (DO MENOS CRÍTICO AO MAIS CRÍTICO):", "info")
        
        niveis = [
            ('DEBUG', '🔍', 'Informações detalhadas para desenvolvimento'),
            ('INFO', '📝', 'Informações gerais sobre funcionamento'),
            ('WARNING', '⚠️', 'Algo pode estar errado, mas não quebrou'),
            ('ERROR', '❌', 'Erro que impediu uma operação'),
            ('CRITICAL', '🚨', 'Erro grave que pode parar o sistema')
        ]
        
        for nivel, emoji, descricao in niveis:
            self.print_colored(f"{emoji} {nivel}: {descricao}", "text")
        
        input("\n🔸 Pressione ENTER para ver exemplos práticos...")
        
        # === EXEMPLO PRÁTICO ===
        exemplo_logging = '''import logging
import traceback
from datetime import datetime

# Configuração profissional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def calcular_media_com_logs(numeros):
    """Calcula média com logging detalhado"""
    
    # Log de início
    logger.info(f"Iniciando cálculo de média para {len(numeros)} números")
    logger.debug(f"Números recebidos: {numeros}")
    
    try:
        # Validação com logs
        if not numeros:
            logger.warning("Lista vazia recebida para cálculo de média")
            raise ValueError("Lista não pode estar vazia")
        
        if not all(isinstance(n, (int, float)) for n in numeros):
            invalidos = [n for n in numeros if not isinstance(n, (int, float))]
            logger.error(f"Tipos inválidos encontrados: {invalidos}")
            raise TypeError(f"Todos os valores devem ser números. Inválidos: {invalidos}")
        
        # Cálculo
        logger.debug("Iniciando cálculo da soma")
        soma = sum(numeros)
        media = soma / len(numeros)
        
        # Log de sucesso
        logger.info(f"Média calculada com sucesso: {media:.2f}")
        logger.debug(f"Soma: {soma}, Quantidade: {len(numeros)}, Média: {media}")
        
        return media
        
    except (ValueError, TypeError) as e:
        # Log de erro específico
        logger.error(f"Erro de validação: {e}")
        logger.debug(f"Stack trace: {traceback.format_exc()}")
        raise
        
    except Exception as e:
        # Log de erro inesperado com stack trace completo
        logger.critical(f"Erro inesperado no cálculo de média: {e}")
        logger.critical(f"Stack trace completo:\\n{traceback.format_exc()}")
        raise
    
    finally:
        logger.debug("Finalizando função calcular_media_com_logs")

# Exemplo de uso com diferentes cenários
print("=== TESTE COM LOGGING ===\\n")

# Caso de sucesso
try:
    resultado = calcular_media_com_logs([1, 2, 3, 4, 5])
    print(f"✅ Média: {resultado}")
except Exception as e:
    print(f"❌ Erro: {e}")

# Caso com erro
try:
    resultado = calcular_media_com_logs([1, "abc", 3])
except Exception as e:
    print(f"❌ Erro: {e}")

# Caso com lista vazia
try:
    resultado = calcular_media_com_logs([])
except Exception as e:
    print(f"❌ Erro: {e}")'''
        
        self.exemplo(exemplo_logging)
        
        # === FERRAMENTAS DE DEBUGGING ===
        self.print_colored("\n🛠️ FERRAMENTAS DE DEBUGGING:", "accent")
        ferramentas = [
            "📊 logging: Sistema profissional de logs",
            "🔍 traceback: Stack trace detalhado de erros",
            "🐛 pdb: Debugger interativo do Python",
            "📈 monitoring: Sentry, DataDog para produção",
            "📝 IDEs: PyCharm, VSCode com debugging visual"
        ]
        for ferramenta in ferramentas:
            self.print_colored(f"  {ferramenta}", "text")
        
        self.pausar()
    
    def _secao_curiosidades(self) -> None:
        """Seção: Curiosidades sobre exceções"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("CURIOSIDADES FASCINANTES", "💫", "success")
        
        # === INTRODUÇÃO ===
        self.print_colored("Fatos interessantes sobre exceções que poucos conhecem!", "text")
        
        curiosidades = [
            {
                'titulo': '🐍 Python vs Outras Linguagens',
                'fato': 'Python usa "exceções" onde outras linguagens usam "erros"',
                'detalhe': 'Java: try/catch, Python: try/except. Python é mais legível!'
            },
            {
                'titulo': '⚡ Performance de Exceções',
                'fato': 'Exceções em Python são "caras" computacionalmente',
                'detalhe': 'Use validação prévia quando possível: if/else é mais rápido que try/except'
            },
            {
                'titulo': '🌍 Exceções no Mundo Real',
                'fato': 'Netflix usa exceções para fallback entre servidores',
                'detalhe': 'Se servidor 1 falha → exceção → tenta servidor 2 automaticamente'
            },
            {
                'titulo': '🎮 Exceções em Jogos',
                'fato': 'Games online usam exceções para não desconectar players',
                'detalhe': 'Lag de rede → TimeoutException → reconecta automaticamente'
            },
            {
                'titulo': '🚀 Space Exception',
                'fato': 'NASA programa sondas espaciais com milhares de exceções',
                'detalhe': 'Cada sensor pode falhar → exceção específica → protocolo de backup'
            },
            {
                'titulo': '💰 Exceções Milionárias',
                'fato': 'Uma exceção não tratada custou US$ 460 milhões',
                'detalhe': 'Foguete Ariane 5 explodiu em 1996 por overflow não tratado!'
            },
            {
                'titulo': '🤖 AI e Exceções',
                'fato': 'Inteligências artificiais aprendem com exceções',
                'detalhe': 'ChatGPT usa padrões de erro para melhorar respostas'
            },
            {
                'titulo': '🔒 Segurança via Exceções',
                'fato': 'Bancos usam exceções para detectar fraudes',
                'detalhe': 'Transação estranha → SecurityException → bloqueia cartão'
            }
        ]
        
        for i, curiosidade in enumerate(curiosidades, 1):
            self.print_colored(f"\n{i}. {curiosidade['titulo']}", "warning")
            self.print_colored(f"   💡 {curiosidade['fato']}", "text")
            self.print_colored(f"   📝 {curiosidade['detalhe']}", "accent")
            
            if i % 2 == 0 and i < len(curiosidades):
                input("\n   ⏳ Pressione ENTER para mais curiosidades...")
        
        # === EASTER EGGS ===
        input("\n🔸 Pressione ENTER para ver easter eggs do Python...")
        
        self.print_colored("\n🥚 EASTER EGGS COM EXCEÇÕES:", "success")
        
        easter_eggs = '''# 1. Exceção mais engraçada
try:
    import antigravity  # Abre xkcd sobre Python!
except ImportError:
    print("Gravity still works!")

# 2. Exceção filosófica
try:
    import this  # Zen do Python
except ImportError:
    print("Enlightenment not found")

# 3. Exceção impossível
try:
    assert False, "Esta exceção sempre acontece"
except AssertionError as e:
    print(f"Filosófico: {e}")

# 4. Exceção recursiva (CUIDADO!)
class RecursiveError(Exception):
    def __str__(self):
        raise RecursiveError("Inception error!")  # Não faça isso!'''
        
        self.exemplo(easter_eggs)
        
        self.print_success("\n🎉 Agora você é um expert em exceções Python!")
        self.print_colored("💡 Use esse conhecimento para criar programas mais robustos e profissionais!", "accent")
        
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
                'title': 'Quiz: Conhecimentos sobre Tratamento de Exceções',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual palavra-chave usamos para capturar exceções em Python?',
                        'answer': ['except', 'EXCEPT', 'Except'],
                        'hint': 'É a palavra que vem depois de "try"...'
                    },
                    {
                        'question': 'Que tipo de exceção acontece quando tentamos converter "abc" para int?',
                        'answer': ['ValueError', 'valueerror', 'VALUE_ERROR'],
                        'hint': 'É sobre o valor estar no formato errado...'
                    },
                    {
                        'question': 'Qual bloco SEMPRE executa, dê certo ou errado?',
                        'answer': ['finally', 'FINALLY', 'Finally'],
                        'hint': 'Mesmo que tudo dê errado, este bloco nunca desiste!'
                    },
                    {
                        'question': 'Que exceção acontece quando acessamos uma chave inexistente no dicionário?',
                        'answer': ['KeyError', 'keyerror', 'KEY_ERROR'],
                        'hint': 'É sobre a chave não ser encontrada...'
                    },
                    {
                        'question': 'Como criamos nossas próprias exceções personalizadas?',
                        'answer': ['class MinhaExcecao(Exception)', 'herdando de Exception', 'herança'],
                        'hint': 'Precisamos criar uma classe que herda de...'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o try/except para capturar erro de conversão',
                        'starter': 'try:\n    numero = int(input("Digite um número: "))\n    print(f"Número: {numero}")\n# Complete aqui\n    print("❌ Por favor, digite apenas números!")',
                        'solution': 'except ValueError:',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o código para capturar múltiplas exceções',
                        'starter': 'try:\n    lista = [1, 2, 3]\n    indice = int(input("Índice: "))\n    print(lista[indice])\n# Complete aqui\n    print("❌ Erro nos dados fornecidos")',
                        'solution': 'except (ValueError, IndexError):',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a exceção customizada',
                        'starter': 'class IdadeInvalidaError(Exception):\n    def __init__(self, idade):\n        self.idade = idade\n        # Complete aqui\n        super().__init__(mensagem)',
                        'solution': 'mensagem = f"Idade {idade} é inválida"',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Validação Robusto',
                'type': 'creative',
                'instruction': 'Crie um sistema que valida dados de cadastro (nome, idade, email) com exceções personalizadas e mensagens claras. Seja criativo com as validações!'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            # Limpa tela antes do menu
            if self.ui:
                self.ui.clear_screen()
            
            self.print_section("MENU DE EXERCÍCIOS", "📚", "accent")
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código")
            print("3. 🎨 Exercício Criativo")
            print("\n" + "─" * 40)
            print("0. 🎯 Continuar para o Mini Projeto")
            print("─" * 40)
            
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre exceções",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de try/except",
            "🎨 OPÇÃO 3 - Exercício Criativo: Sistema de validação com exceções personalizadas",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: Sistema Robusto de Exceções",
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
    
    def _mini_projeto_sistema_robusto_excecoes(self) -> None:
        """Mini Projeto - Módulo 16: Sistema Robusto de Tratamento de Exceções"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA ROBUSTO DE EXCEÇÕES")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA ROBUSTO DE EXCEÇÕES")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar um sistema profissional de tratamento de exceções!")
        
        self.print_concept(
            "Sistema Guardian",
            "Um sistema inteligente que protege aplicações de falhas, com retry automático, logging detalhado e notificações de erro"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "Netflix: para recuperar automaticamente de falhas de servidor durante streaming",
            "Bancos: para proteger transações contra falhas de rede e hardware",
            "Tesla: para lidar com falhas de sensores em carros autônomos",
            "Spotify: para manter música tocando mesmo com problemas de conexão"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Configuração e Conceito
        self.print_section("PASSO 1: Configurando o Sistema Guardian", "📝", "info")
        self.print_tip("Vamos criar um decorador inteligente que monitora funções automaticamente!")
        
        try:
            input("\n🔸 Pressione ENTER para começar a construir...")
            
            # PASSO 2: Implementação
            self.print_section("PASSO 2: Implementando o Núcleo do Sistema", "⚙️", "success")
            self.print_colored("Criando o sistema que nunca desiste:", "text")
            
            input("\n🔸 Pressione ENTER para ver o código...")
            
            # PASSO 3: Código Final
            self.print_section("PASSO 3: Sistema Guardian Completo", "🎬", "warning")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o sistema completo que você criou:", "text")
        
        codigo_final = '''# 🛡️ PROJETO: SISTEMA GUARDIAN - PROTEÇÃO INTELIGENTE
# Módulo 16: Tratamento de Exceções

import functools
import logging
import time
import json
from datetime import datetime
from typing import Callable, Any, Dict, List

# === CONFIGURAÇÃO PROFISSIONAL DE LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler('guardian_system.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class SystemGuardian:
    """Sistema inteligente de proteção contra falhas"""
    
    def __init__(self, system_name: str = "Guardian"):
        self.logger = logging.getLogger(system_name)
        self.failure_stats = {}
        self.success_count = 0
        self.failure_count = 0
    
    def protect(
        self, 
        max_retries: int = 3,
        delay: float = 1.0,
        exponential_backoff: bool = True,
        exceptions: tuple = (Exception,),
        notify_on_failure: bool = True,
        log_success: bool = True
    ):
        """
        Decorador que protege funções contra falhas
        
        Args:
            max_retries: Tentativas máximas antes de desistir
            delay: Tempo base entre tentativas (segundos)
            exponential_backoff: Aumenta delay exponencialmente
            exceptions: Tipos de exceção para capturar
            notify_on_failure: Envia notificação em falha crítica
            log_success: Registra sucessos nos logs
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                func_name = func.__name__
                start_time = time.time()
                
                for tentativa in range(max_retries + 1):
                    try:
                        # Executa função protegida
                        result = func(*args, **kwargs)
                        
                        # Registra sucesso
                        execution_time = time.time() - start_time
                        self._log_success(func_name, tentativa, execution_time, log_success)
                        self.success_count += 1
                        
                        return result
                        
                    except exceptions as e:
                        self._log_failure(func_name, tentativa, e)
                        
                        if tentativa < max_retries:
                            # Calcula delay (com backoff exponencial se habilitado)
                            current_delay = delay
                            if exponential_backoff:
                                current_delay = delay * (2 ** tentativa)
                            
                            self.logger.info(
                                f"🔄 Tentativa {tentativa + 2} em {current_delay:.1f}s..."
                            )
                            time.sleep(current_delay)
                        else:
                            # Falha final
                            self._handle_final_failure(func_name, e, notify_on_failure)
                            self.failure_count += 1
                            raise
                
            return wrapper
        return decorator
    
    def _log_success(self, func_name: str, tentativa: int, execution_time: float, log_success: bool):
        """Registra execução bem-sucedida"""
        if log_success:
            if tentativa > 0:
                self.logger.info(
                    f"✅ {func_name} recuperada com sucesso na tentativa {tentativa + 1} "
                    f"({execution_time:.2f}s)"
                )
            else:
                self.logger.debug(f"✅ {func_name} executada ({execution_time:.2f}s)")
    
    def _log_failure(self, func_name: str, tentativa: int, exception: Exception):
        """Registra tentativa falhada"""
        error_type = type(exception).__name__
        
        # Atualiza estatísticas
        if func_name not in self.failure_stats:
            self.failure_stats[func_name] = {}
        if error_type not in self.failure_stats[func_name]:
            self.failure_stats[func_name][error_type] = 0
        self.failure_stats[func_name][error_type] += 1
        
        self.logger.warning(
            f"⚠️ {func_name} falhou na tentativa {tentativa + 1}: {error_type} - {exception}"
        )
    
    def _handle_final_failure(self, func_name: str, exception: Exception, notify: bool):
        """Trata falha final após todas as tentativas"""
        self.logger.error(f"❌ {func_name} falhou definitivamente: {exception}")
        
        if notify:
            self._send_failure_notification(func_name, exception)
    
    def _send_failure_notification(self, func_name: str, exception: Exception):
        """Envia notificação de falha crítica"""
        notification = {
            "timestamp": datetime.now().isoformat(),
            "function": func_name,
            "error_type": type(exception).__name__,
            "error_message": str(exception),
            "total_failures": self.failure_count + 1,
            "total_successes": self.success_count
        }
        
        print("\\n" + "="*60)
        print("🚨 ALERTA DE FALHA CRÍTICA 🚨")
        print("="*60)
        print(f"📍 Função: {func_name}")
        print(f"💥 Erro: {type(exception).__name__}")
        print(f"📝 Mensagem: {exception}")
        print(f"⏰ Timestamp: {notification['timestamp']}")
        print(f"📊 Status: {self.success_count} sucessos, {self.failure_count + 1} falhas")
        print("="*60)
        
        # Em produção, aqui enviaria email, Slack, etc.
        self.logger.critical(f"FALHA CRÍTICA: {json.dumps(notification, indent=2)}")
    
    def get_statistics(self) -> Dict:
        """Retorna estatísticas do sistema"""
        return {
            "successes": self.success_count,
            "failures": self.failure_count,
            "failure_rate": self.failure_count / (self.success_count + self.failure_count) if (self.success_count + self.failure_count) > 0 else 0,
            "failure_breakdown": self.failure_stats
        }

# === DEMONSTRAÇÃO DO SISTEMA ===

# Inicializa o Guardian
guardian = SystemGuardian("MeuSistema")

# Função que simula operação instável (conexão de rede)
@guardian.protect(max_retries=3, delay=0.5, exponential_backoff=True)
def conectar_api_externa():
    """Simula conexão com API externa"""
    import random
    
    if random.random() < 0.6:  # 60% chance de falhar
        errors = [
            ConnectionError("Timeout na conexão"),
            TimeoutError("Servidor não respondeu"),
            ValueError("Resposta inválida da API")
        ]
        raise random.choice(errors)
    
    return {"status": "success", "data": "Dados importantes da API"}

# Função que processa dados críticos
@guardian.protect(max_retries=2, exceptions=(ValueError, TypeError))
def processar_dados_criticos(dados):
    """Processa dados importantes do sistema"""
    if not dados:
        raise ValueError("Dados não podem estar vazios")
    
    if not isinstance(dados, dict):
        raise TypeError("Dados devem ser um dicionário")
    
    return f"Processado: {len(dados)} campos"

# Função que sempre funciona
@guardian.protect(log_success=False)  # Não loga sucessos para reduzir ruído
def operacao_simples(x, y):
    """Operação matemática simples"""
    return x + y

# === TESTE DO SISTEMA ===

print("🛡️ SISTEMA GUARDIAN EM AÇÃO\\n")

# Teste 1: Conexão instável
print("📡 Testando conexão com API externa...")
try:
    resultado = conectar_api_externa()
    print(f"✅ Sucesso: {resultado}")
except Exception as e:
    print(f"❌ Falha final: {e}")

print("\\n" + "-"*50 + "\\n")

# Teste 2: Processamento de dados
print("📊 Testando processamento de dados...")
for dados_teste in [{"nome": "João"}, None, "dados_inválidos"]:
    try:
        resultado = processar_dados_criticos(dados_teste)
        print(f"✅ Processado: {resultado}")
    except Exception as e:
        print(f"❌ Erro: {e}")

print("\\n" + "-"*50 + "\\n")

# Teste 3: Operação simples (sempre funciona)
print("🔢 Testando operação simples...")
resultado = operacao_simples(5, 3)
print(f"✅ 5 + 3 = {resultado}")

# Estatísticas finais
print("\\n" + "="*50)
print("📊 ESTATÍSTICAS DO SISTEMA GUARDIAN")
print("="*50)
stats = guardian.get_statistics()
print(f"✅ Sucessos: {stats['successes']}")
print(f"❌ Falhas: {stats['failures']}")
print(f"📈 Taxa de sucesso: {(1 - stats['failure_rate']) * 100:.1f}%")
if stats['failure_breakdown']:
    print("\\n🔍 Detalhamento de falhas:")
    for func, errors in stats['failure_breakdown'].items():
        print(f"  📍 {func}:")
        for error_type, count in errors.items():
            print(f"    • {error_type}: {count}x")
print("="*50)'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        print("\n🚀 Simulando execução do Sistema Guardian:")
        
        # Simula saída do sistema
        resultados_simulados = [
            "🛡️ SISTEMA GUARDIAN EM AÇÃO",
            "",
            "📡 Testando conexão com API externa...",
            "⚠️ conectar_api_externa falhou na tentativa 1: ConnectionError - Timeout na conexão",
            "🔄 Tentativa 2 em 0.5s...",
            "⚠️ conectar_api_externa falhou na tentativa 2: TimeoutError - Servidor não respondeu",
            "🔄 Tentativa 3 em 1.0s...",
            "✅ conectar_api_externa recuperada com sucesso na tentativa 3",
            "✅ Sucesso: {'status': 'success', 'data': 'Dados importantes da API'}",
            "",
            "📊 Testando processamento de dados...",
            "✅ Processado: Processado: 1 campos",
            "❌ processar_dados_criticos falhou definitivamente: Dados não podem estar vazios",
            "❌ Erro: Dados não podem estar vazios",
            "❌ processar_dados_criticos falhou definitivamente: Dados devem ser um dicionário",
            "❌ Erro: Dados devem ser um dicionário",
            "",
            "🔢 Testando operação simples...",
            "✅ 5 + 3 = 8",
            "",
            "📊 ESTATÍSTICAS DO SISTEMA GUARDIAN",
            "✅ Sucessos: 2",
            "❌ Falhas: 2",
            "📈 Taxa de sucesso: 50.0%"
        ]
        
        for linha in resultados_simulados:
            if linha.startswith("⚠️"):
                self.print_colored(linha, "warning")
            elif linha.startswith("✅"):
                self.print_colored(linha, "success")
            elif linha.startswith("❌"):
                self.print_colored(linha, "error")
            elif linha.startswith("🔄"):
                self.print_colored(linha, "info")
            else:
                print(linha)
            time.sleep(0.1)  # Simula execução em tempo real
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("\n🎉 PARABÉNS! Você criou um Sistema Guardian profissional!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Integrar com sistemas de monitoramento (Prometheus, Grafana)",
            "Adicionar notificações via email, Slack ou Discord",
            "Implementar circuit breaker para falhas consecutivas",
            "Criar dashboard web para visualizar estatísticas em tempo real",
            "Adicionar métricas de performance e alertas inteligentes"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Guardian Master - Protetor de Sistemas!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema Guardian de Exceções")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo16Excecoes()
    print("Teste do módulo 16 - versão standalone")
    module._excecoes_interativo()