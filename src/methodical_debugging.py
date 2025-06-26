#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Debugging Metodológico
Ensina técnicas sistemáticas de resolução de problemas
"""

import re
import sys
import traceback
import inspect
import ast
import subprocess
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class DebugPhase(Enum):
    """Fases do processo de debugging"""
    READ = "read"
    SEARCH = "search"
    ASK = "ask"
    DEBUG = "debug"
    VERIFY = "verify"

@dataclass
class BugCase:
    """Representa um caso de bug para prática"""
    id: str
    title: str
    description: str
    buggy_code: str
    error_message: str
    difficulty: str
    concepts: List[str]
    solution_steps: List[str]
    fixed_code: str
    explanation: str

@dataclass
class DebugSession:
    """Sessão de debugging do usuário"""
    session_id: str
    start_time: str
    bug_case_id: str
    current_phase: DebugPhase
    user_hypotheses: List[str]
    user_actions: List[str]
    time_per_phase: Dict[str, int]
    success: bool
    total_time: int

class MethodicalDebuggingSystem:
    """Sistema principal de debugging metodológico"""
    
    def __init__(self, ui_components=None):
        self.ui = ui_components
        self.bug_cases = self._load_bug_cases()
        self.current_session: Optional[DebugSession] = None
        self.duck_responses = self._load_duck_responses()
        
    def start_debugging_course(self):
        """Inicia o curso de debugging metodológico"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧠 DEBUGGING METODOLÓGICO", "Ciência da Resolução de Problemas")
        
        self._show_debugging_intro()
        self._show_main_menu()
    
    def _show_debugging_intro(self):
        """Introdução ao debugging metodológico"""
        print("🎯 POR QUE DEBUGGING É UMA CIÊNCIA?")
        print("=" * 50)
        print("❌ 70% do tempo de desenvolvimento é gasto debugando")
        print("❌ Debugging ad-hoc leva a frustração e perda de tempo")
        print("✅ Abordagem sistemática aumenta eficiência em 300%")
        print("✅ Desenvolve pensamento lógico e analítico")
        print("✅ Skill transferível para qualquer linguagem")
        
        print("\n🧪 MÉTODO CIENTÍFICO DE DEBUGGING:")
        print("=" * 50)
        print("1️⃣ 📖 READ:   Entender o problema completamente")
        print("2️⃣ 🔍 SEARCH: Buscar pistas e evidências")
        print("3️⃣ ❓ ASK:    Formular hipóteses específicas")  
        print("4️⃣ 🐛 DEBUG:  Testar hipóteses sistematicamente")
        print("5️⃣ ✅ VERIFY: Confirmar que o problema foi resolvido")
        
        input("\n🔸 Pressione ENTER para continuar...")
        
    def _show_main_menu(self):
        """Menu principal do sistema de debugging"""
        while True:
            if self.ui:
                self.ui.clear_screen()
                self.ui.header("🧠 DEBUGGING METODOLÓGICO", "Menu Principal")
            
            print("📚 OPÇÕES DE APRENDIZADO:")
            print("=" * 50)
            print("1. 📖 Framework RSAD - Teoria")
            print("2. 🦆 Rubber Duck Debugging")
            print("3. 📊 Análise de Stack Traces")
            print("4. 🎯 Prática com Bugs Reais")
            print("5. 🔍 Debugging Interativo")
            print("6. 📚 Biblioteca de Bugs Comuns")
            print("7. 🏆 Desafios de Debugging")
            print("8. 📈 Meu Progresso em Debugging")
            print("0. 🔙 Voltar ao menu principal")
            
            choice = input("\nEscolha uma opção: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._teach_rsad_framework()
            elif choice == "2":
                self._start_rubber_duck_session()
            elif choice == "3":
                self._teach_stack_trace_analysis()
            elif choice == "4":
                self._practice_with_real_bugs()
            elif choice == "5":
                self._interactive_debugging()
            elif choice == "6":
                self._show_bug_library()
            elif choice == "7":
                self._debugging_challenges()
            elif choice == "8":
                self._show_debugging_progress()
            else:
                print("❌ Opção inválida!")
                input("Pressione ENTER para continuar...")
    
    def _teach_rsad_framework(self):
        """Ensina o framework RSAD detalhadamente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📖 FRAMEWORK RSAD", "Read-Search-Ask-Debug")
        
        print("🎯 O FRAMEWORK RSAD EM DETALHES:")
        print("=" * 50)
        
        # Fase READ
        print("\n1️⃣ 📖 READ - ENTENDER O PROBLEMA")
        print("-" * 40)
        print("✅ Leia a mensagem de erro COMPLETAMENTE")
        print("✅ Identifique ONDE o erro ocorreu (arquivo:linha)")
        print("✅ Entenda O QUE o programa deveria fazer")
        print("✅ Reproduza o erro de forma consistente")
        print("✅ Documente os passos para reproduzir")
        
        print("\n📝 PERGUNTAS DA FASE READ:")
        read_questions = [
            "Qual é a mensagem de erro exata?",
            "Em que linha e arquivo o erro ocorre?",
            "O que o código deveria fazer nessa linha?",
            "Quando o erro acontece (sempre/às vezes)?",
            "Que dados de entrada causam o erro?"
        ]
        for q in read_questions:
            print(f"   • {q}")
        
        input("\n🔸 Pressione ENTER para fase SEARCH...")
        
        # Fase SEARCH
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔍 FASE SEARCH", "Buscar Pistas e Evidências")
        
        print("2️⃣ 🔍 SEARCH - COLETAR EVIDÊNCIAS")
        print("-" * 40)
        print("✅ Examine o stack trace linha por linha")
        print("✅ Verifique valores de variáveis importantes")
        print("✅ Analise o fluxo de execução")
        print("✅ Procure por padrões em erros similares")
        print("✅ Use prints estratégicos para investigar")
        
        print("\n🛠️ FERRAMENTAS DE SEARCH:")
        search_tools = [
            "print() para verificar valores",
            "type() para confirmar tipos de dados",
            "len() para verificar tamanhos",
            "dir() para explorar objetos",
            "debugger (pdb) para step-by-step",
            "Google/Stack Overflow para mensagens específicas"
        ]
        for tool in search_tools:
            print(f"   • {tool}")
        
        input("\n🔸 Pressione ENTER para fase ASK...")
        
        # Fase ASK
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("❓ FASE ASK", "Formular Hipóteses")
        
        print("3️⃣ ❓ ASK - FORMULAR HIPÓTESES")
        print("-" * 40)
        print("✅ Forme hipóteses ESPECÍFICAS sobre a causa")
        print("✅ Priorize hipóteses por probabilidade")
        print("✅ Cada hipótese deve ser TESTÁVEL")
        print("✅ Evite hipóteses vagas como 'algo está errado'")
        print("✅ Base hipóteses nas evidências coletadas")
        
        print("\n🎯 EXEMPLOS DE BOAS HIPÓTESES:")
        good_hypotheses = [
            "A variável 'idade' pode estar chegando como string em vez de int",
            "O índice da lista pode estar fora do range na linha 25", 
            "O arquivo pode não estar sendo encontrado no caminho especificado",
            "A divisão por zero pode estar acontecendo quando 'total' é 0",
            "O objeto pode ser None antes de chamar o método"
        ]
        for hypothesis in good_hypotheses:
            print(f"   ✅ {hypothesis}")
        
        print("\n❌ EXEMPLOS DE HIPÓTESES RUINS:")
        bad_hypotheses = [
            "O código está bugado",
            "Python não está funcionando",
            "Tem algo errado aí",
            "Não sei o que é"
        ]
        for hypothesis in bad_hypotheses:
            print(f"   ❌ {hypothesis}")
        
        input("\n🔸 Pressione ENTER para fase DEBUG...")
        
        # Fase DEBUG
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐛 FASE DEBUG", "Testar Hipóteses")
        
        print("4️⃣ 🐛 DEBUG - TESTAR HIPÓTESES")
        print("-" * 40)
        print("✅ Teste UMA hipótese por vez")
        print("✅ Faça mudanças MÍNIMAS para testar")
        print("✅ Documente o resultado de cada teste")
        print("✅ Se hipótese falhar, passe para a próxima")
        print("✅ Use debugging sistemático, não tentativa-erro")
        
        print("\n🧪 ESTRATÉGIAS DE TESTE:")
        test_strategies = [
            "Adicionar prints antes/depois da linha problemática",
            "Comentar partes do código para isolar o problema",
            "Testar com dados de entrada simplificados",
            "Usar assert statements para verificar suposições",
            "Criar caso de teste mínimo que reproduz o bug",
            "Usar debugger para step-through do código"
        ]
        for strategy in test_strategies:
            print(f"   • {strategy}")
        
        input("\n🔸 Pressione ENTER para fase VERIFY...")
        
        # Fase VERIFY
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ FASE VERIFY", "Confirmar Solução")
        
        print("5️⃣ ✅ VERIFY - CONFIRMAR SOLUÇÃO")
        print("-" * 40)
        print("✅ Teste a solução com casos originais")
        print("✅ Teste com casos extremos (edge cases)")
        print("✅ Verifique se não criou novos bugs")
        print("✅ Confirme que o comportamento está correto")
        print("✅ Documente a solução para referência futura")
        
        print("\n🎯 CHECKLIST DE VERIFICAÇÃO:")
        verify_checklist = [
            "O erro original não acontece mais?",
            "O programa produz a saída esperada?",
            "Testei com diferentes entradas?",
            "Não quebrei outras funcionalidades?",
            "O código ainda está legível e limpo?",
            "Documentei o que aprendi?"
        ]
        for item in verify_checklist:
            print(f"   □ {item}")
        
        print("\n💡 DICA PRO:")
        print("   Depois de resolver um bug, sempre reflita:")
        print("   'Como posso evitar este tipo de bug no futuro?'")
        
        input("\n🔸 Pressione ENTER para exemplo prático...")
        
        self._show_rsad_example()
    
    def _show_rsad_example(self):
        """Exemplo prático do framework RSAD"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("💻 EXEMPLO PRÁTICO", "RSAD em Ação")
        
        print("🐛 CÓDIGO COM BUG:")
        print("=" * 50)
        buggy_code = '''
def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    return media

# Teste
idades = [18, 20, "vinte e dois", 19]
resultado = calcular_media(idades)
print(f"Média: {resultado}")
        '''
        print(buggy_code)
        
        print("\n❌ ERRO OBTIDO:")
        print("TypeError: unsupported operand type(s) for +=: 'int' and 'str'")
        
        print("\n🧠 APLICANDO RSAD:")
        print("=" * 50)
        
        print("1️⃣ READ:")
        print("   • Erro: TypeError na operação +=")
        print("   • Local: linha 'total += nota'")
        print("   • Problema: tentando somar int + str")
        
        print("\n2️⃣ SEARCH:")
        print("   • Lista contém: [18, 20, 'vinte e dois', 19]")
        print("   • 'vinte e dois' é string, não número")
        print("   • Função espera apenas números")
        
        print("\n3️⃣ ASK:")
        print("   • Hipótese: A string 'vinte e dois' está causando o erro")
        print("   • Como devemos tratar strings na lista?")
        
        print("\n4️⃣ DEBUG:")
        print("   • Opção 1: Filtrar apenas números")
        print("   • Opção 2: Converter strings para números")
        print("   • Opção 3: Lançar erro informativo")
        
        print("\n5️⃣ VERIFY:")
        print("   • Testar com diferentes tipos de entrada")
        print("   • Confirmar que funciona corretamente")
        
        input("\n🔸 Pressione ENTER para ver a solução...")
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ SOLUÇÃO", "Código Corrigido")
        
        solution_code = '''
def calcular_media(notas):
    # Filtrar apenas números (int ou float)
    numeros = []
    for nota in notas:
        if isinstance(nota, (int, float)):
            numeros.append(nota)
        else:
            print(f"⚠️ Ignorando valor inválido: {nota}")
    
    if not numeros:
        raise ValueError("Nenhum número válido encontrado na lista")
    
    total = sum(numeros)
    media = total / len(numeros)
    return media

# Teste
idades = [18, 20, "vinte e dois", 19]
try:
    resultado = calcular_media(idades)
    print(f"Média: {resultado:.1f}")
except ValueError as e:
    print(f"Erro: {e}")
        '''
        
        print("💡 SOLUÇÃO ROBUSTA:")
        print(solution_code)
        
        print("\n🎓 LIÇÕES APRENDIDAS:")
        print("=" * 50)
        print("✅ Sempre validar tipos de entrada")
        print("✅ Tratar casos excepcionais graciosamente") 
        print("✅ Fornecer mensagens informativas")
        print("✅ Testar com dados 'sujos' realistas")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _start_rubber_duck_session(self):
        """Inicia sessão de rubber duck debugging"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🦆 RUBBER DUCK DEBUGGING", "Explique para o Pato")
        
        print("🦆 CONHECE O RUBBER DUCK DEBUGGING?")
        print("=" * 50)
        print("📖 ORIGEM: Programadores na universidade Carnegie Mellon")
        print("🎯 CONCEITO: Explicar código linha por linha para um pato de borracha")
        print("🧠 CIÊNCIA: Verbalizar força o cérebro a reorganizar pensamentos")
        print("⚡ RESULTADO: 60% dos bugs são descobertos apenas explicando")
        
        print("\n🎯 POR QUE FUNCIONA?")
        print("=" * 50)
        print("✅ Força você a pensar devagar e metodicamente")
        print("✅ Revela suposições incorretas sobre o código")
        print("✅ Identifica lacunas na lógica")
        print("✅ Não há julgamento - pode ser honesto sobre dúvidas")
        print("✅ Processo ativo vs passivo de debugging")
        
        input("\n🔸 Pressione ENTER para começar sessão...")
        
        self._duck_debugging_session()
    
    def _duck_debugging_session(self):
        """Sessão interativa de rubber duck debugging"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🦆 SESSÃO DE RUBBER DUCK", "Seu Pato Virtual")
        
        print("🦆 Olá! Sou seu pato de debugging. Explique-me seu problema!")
        print("=" * 60)
        print("💡 DICAS PARA UMA BOA SESSÃO:")
        print("   • Explique o que o código DEVERIA fazer")
        print("   • Descreva o que está REALMENTE acontecendo")
        print("   • Vá linha por linha através do código problema")
        print("   • Não tenha pressa - pense em voz alta")
        print("   • Questione suas suposições")
        
        print("\n🦆 'Quack! Vamos começar. Qual é o seu problema?'")
        print("(Digite 'sair' quando quiser terminar)")
        
        conversation_count = 0
        while True:
            print(f"\n👤 Você:")
            user_input = input("> ").strip()
            
            if user_input.lower() in ['sair', 'exit', 'quit', 'tchau']:
                print("\n🦆 'Quack! Foi um prazer ajudar! Lembre-se: quando")
                print("    estiver em dúvida, explique para o pato! 🦆'")
                break
            
            if not user_input:
                continue
                
            duck_response = self._get_duck_response(user_input, conversation_count)
            print(f"\n🦆 Pato: '{duck_response}'")
            
            conversation_count += 1
            
            if conversation_count >= 10:
                print("\n🦆 'Quack! Conversamos bastante! Que tal tentar")
                print("    implementar uma solução agora? 🦆'")
                break
        
        input("\nPressione ENTER para continuar...")
    
    def _get_duck_response(self, user_input: str, conversation_count: int) -> str:
        """Gera resposta inteligente do pato baseada na entrada do usuário"""
        user_lower = user_input.lower()
        
        # Respostas específicas baseadas em palavras-chave
        if any(word in user_lower for word in ['erro', 'error', 'exception']):
            return self.duck_responses['error_questions'][conversation_count % len(self.duck_responses['error_questions'])]
        
        elif any(word in user_lower for word in ['não funciona', 'not working', 'quebrado']):
            return self.duck_responses['not_working'][conversation_count % len(self.duck_responses['not_working'])]
        
        elif any(word in user_lower for word in ['deveria', 'should', 'esperava']):
            return self.duck_responses['expectations'][conversation_count % len(self.duck_responses['expectations'])]
        
        elif any(word in user_lower for word in ['linha', 'function', 'método']):
            return self.duck_responses['code_structure'][conversation_count % len(self.duck_responses['code_structure'])]
        
        elif any(word in user_lower for word in ['variável', 'variable', 'valor']):
            return self.duck_responses['variables'][conversation_count % len(self.duck_responses['variables'])]
        
        else:
            return self.duck_responses['general'][conversation_count % len(self.duck_responses['general'])]
    
    def _load_duck_responses(self) -> Dict[str, List[str]]:
        """Carrega respostas do pato de debugging"""
        return {
            'error_questions': [
                "Quack! Qual é a mensagem de erro exata? Leia ela palavra por palavra para mim.",
                "Interessante! Em que linha específica esse erro acontece?",
                "Hmm... Esse erro sempre acontece ou só às vezes? Quando exatamente?",
                "Quack quack! O que você estava tentando fazer quando o erro apareceu?",
                "E o que você acha que essa mensagem de erro está tentando te dizer?"
            ],
            'not_working': [
                "Quack! O que você esperava que acontecesse vs o que realmente acontece?",
                "Interessante! Você pode mostrar um exemplo específico do comportamento errado?",
                "Me conte: quando você diz 'não funciona', o que exatamente você observa?",
                "Quack! Já tentou testar com dados mais simples para ver o que acontece?",
                "E se você fosse explicar para sua avó o que está errado, como descreveria?"
            ],
            'expectations': [
                "Quack quack! Por que você acha que deveria funcionar assim?",
                "Interessante expectativa! Vamos rastrear: o que acontece passo a passo?",
                "Hmm... E o que o código está REALMENTE fazendo linha por linha?",
                "Quack! Suas suposições sobre o funcionamento estão corretas?",
                "Me conte: você testou cada parte separadamente para confirmar?"
            ],
            'code_structure': [
                "Quack! Pode me explicar o que essa função específica deveria fazer?",
                "Interessante! Vamos passar linha por linha - o que acontece na primeira linha?",
                "E na linha seguinte? O que deveria acontecer ali?",
                "Quack quack! Os valores estão sendo passados corretamente entre as funções?",
                "Você tem certeza de que está chamando a função com os parâmetros certos?"
            ],
            'variables': [
                "Quack! Qual é o valor dessa variável exatamente nesse ponto?",
                "Interessante! Esse valor é o que você esperava? Por quê?",
                "Hmm... E de onde vem esse valor? Você pode rastrear a origem?",
                "Quack quack! O tipo da variável está correto (string, número, lista)?",
                "Já tentou imprimir o valor da variável para ter certeza?"
            ],
            'general': [
                "Quack! Me conte mais detalhes sobre isso...",
                "Interessante! Continue explicando, estou prestando atenção.",
                "Hmm... E o que acontece se você testar isso passo a passo?",
                "Quack quack! Você já tentou reproduzir o problema de forma mais simples?",
                "Me ajude a entender: qual é a parte que te confunde mais?",
                "E se fosse para explicar isso para um colega, como você descreveria?",
                "Quack! Que tal pensar em uma hipótese específica sobre a causa?",
                "Interessante perspectiva! O que você faria para testar essa teoria?"
            ]
        }
    
    def _load_bug_cases(self) -> Dict[str, BugCase]:
        """Carrega casos de bugs para prática"""
        return {
            "index_error": BugCase(
                id="index_error",
                title="Lista fora do range",
                description="Função que acessa índice inexistente em lista",
                buggy_code='''
def get_last_items(lista, n=3):
    result = []
    for i in range(n):
        result.append(lista[-(i+1)])
    return result

# Teste
nums = [1, 2]
print(get_last_items(nums))  # Erro aqui!
                ''',
                error_message="IndexError: list index out of range",
                difficulty="beginner",
                concepts=["Índices de lista", "Range checking", "Validação de entrada"],
                solution_steps=[
                    "Identificar que n pode ser maior que len(lista)",
                    "Adicionar validação do tamanho da lista",
                    "Usar min(n, len(lista)) para limitar iterações",
                    "Testar com listas de diferentes tamanhos"
                ],
                fixed_code='''
def get_last_items(lista, n=3):
    if not lista:
        return []
    
    result = []
    items_to_get = min(n, len(lista))
    
    for i in range(items_to_get):
        result.append(lista[-(i+1)])
    return result
                ''',
                explanation="O bug ocorre quando n > len(lista). A solução limita o número de iterações."
            ),
            # Mais casos de bugs serão adicionados...
        }
    
    # Continuar implementação dos outros métodos...
    def _teach_stack_trace_analysis(self):
        """Ensina análise sistemática de stack traces"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 ANÁLISE DE STACK TRACES", "Anatomia dos Erros")
        
        print("🎯 O QUE É UM STACK TRACE?")
        print("=" * 50)
        print("📋 Stack trace = mapa do caminho do erro")
        print("🗺️ Mostra exatamente onde e como o erro aconteceu")
        print("📚 Lista as funções chamadas até chegar no erro")
        print("🎯 Sua melhor ferramenta para debugging")
        
        print("\n📖 ANATOMIA DE UM STACK TRACE:")
        print("=" * 50)
        
        # Exemplo de stack trace real
        stack_example = '''
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    resultado = processar_dados(dados_usuarios)
  File "main.py", line 10, in processar_dados
    media = calcular_media(idades)
  File "main.py", line 5, in calcular_media
    return sum(numeros) / len(numeros)
ZeroDivisionError: division by zero
        '''
        
        print("🔍 EXEMPLO DE STACK TRACE:")
        print(stack_example)
        
        print("🧠 COMO LER ESTE STACK TRACE:")
        print("=" * 50)
        print("1️⃣ COMECE DE BAIXO (linha do erro):")
        print("   • ZeroDivisionError: division by zero")
        print("   • Tipo: ZeroDivisionError")
        print("   • Causa: divisão por zero")
        
        print("\n2️⃣ LOCALIZE O ERRO (linha imediatamente acima):")
        print("   • File 'main.py', line 5, in calcular_media")
        print("   • return sum(numeros) / len(numeros)")
        print("   • Erro está na linha 5, função calcular_media")
        
        print("\n3️⃣ TRACE O CAMINHO (de baixo para cima):")
        print("   • linha 5: calcular_media() faz divisão por zero")
        print("   • linha 10: processar_dados() chama calcular_media()")
        print("   • linha 15: <module> chama processar_dados()")
        
        input("\n🔸 Pressione ENTER para técnicas avançadas...")
        
        self._advanced_stack_trace_techniques()
    
    def _advanced_stack_trace_techniques(self):
        """Técnicas avançadas de análise de stack trace"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔬 TÉCNICAS AVANÇADAS", "Stack Trace Pro")
        
        print("🎯 ESTRATÉGIA DE LEITURA SISTEMÁTICA:")
        print("=" * 50)
        
        print("1️⃣ BOTTOM-UP APPROACH (recomendado):")
        print("   • Comece sempre pela ÚLTIMA linha (mensagem de erro)")
        print("   • Suba uma linha para ver ONDE o erro aconteceu")
        print("   • Continue subindo para entender o CONTEXTO")
        
        print("\n2️⃣ IDENTIFIQUE O 'ENTRY POINT':")
        print("   • Última linha sem 'File...' = erro em si")
        print("   • Penúltima linha = local exato do erro")
        print("   • Primeira linha = onde tudo começou")
        
        print("\n3️⃣ FOQUE NO QUE IMPORTA:")
        print("   • Ignore arquivos de bibliotecas (site-packages)")
        print("   • Concentre no SEU código")
        print("   • Busque por padrões nas chamadas")
        
        print("\n🧪 EXEMPLO COMPLEXO:")
        print("=" * 50)
        
        complex_trace = '''
Traceback (most recent call last):
  File "/usr/lib/python3.9/site-packages/requests/models.py", line 910, in json
    return complexjson.loads(self.text, **kwargs)
  File "/usr/lib/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.9/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "meu_app.py", line 25, in <module>
    dados = baixar_dados_api()
  File "meu_app.py", line 15, in baixar_dados_api
    return response.json()
  File "/usr/lib/python3.9/site-packages/requests/models.py", line 912, in json
    raise RequestsJSONError(e)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        '''
        
        print(complex_trace)
        
        print("\n🔍 ANÁLISE DO EXEMPLO COMPLEXO:")
        print("=" * 50)
        print("❗ ERRO PRINCIPAL:")
        print("   • JSONDecodeError: resposta não é JSON válido")
        print("   • Local: meu_app.py, linha 15, response.json()")
        
        print("\n🎯 RACIOCÍNIO:")
        print("   • API retornou algo que não é JSON")
        print("   • Pode ser HTML de erro, texto vazio, etc.")
        print("   • Ignorar todo o trace das bibliotecas")
        print("   • Focar em: meu_app.py linha 15")
        
        print("\n💡 SOLUÇÃO:")
        print("   • Verificar response.status_code primeiro")
        print("   • Imprimir response.text para ver o conteúdo")
        print("   • Validar antes de chamar .json()")
        
        input("\n🔸 Pressione ENTER para exercício prático...")
        
        self._stack_trace_exercise()
    
    def _stack_trace_exercise(self):
        """Exercício prático de análise de stack trace"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🧪 EXERCÍCIO PRÁTICO", "Analise este Stack Trace")
        
        print("🎯 ANALISE O STACK TRACE ABAIXO:")
        print("=" * 50)
        
        exercise_trace = '''
Traceback (most recent call last):
  File "sistema_vendas.py", line 45, in <module>
    relatorio = gerar_relatorio_mensal(vendas_janeiro)
  File "sistema_vendas.py", line 35, in gerar_relatorio_mensal
    total_vendedor = calcular_total_vendedor(vendas, vendedor)
  File "sistema_vendas.py", line 28, in calcular_total_vendedor
    for venda in vendas_vendedor:
  File "sistema_vendas.py", line 20, in obter_vendas_vendedor
    return vendas[vendedor]
KeyError: 'Maria Silva'
        '''
        
        print(exercise_trace)
        
        print("\n📝 PERGUNTAS PARA VOCÊ RESPONDER:")
        print("=" * 50)
        questions = [
            "1. Qual é o tipo de erro?",
            "2. Em que linha específica o erro acontece?",
            "3. Qual é a causa provável do erro?",
            "4. Que dados estão causando o problema?",
            "5. Como você corrigiria este erro?"
        ]
        
        for question in questions:
            print(question)
        
        print("\n🤔 Pense nas respostas e pressione ENTER para ver a análise...")
        input()
        
        # Mostrar análise detalhada
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ ANÁLISE CORRETA", "Respostas do Exercício")
        
        print("📊 ANÁLISE DETALHADA:")
        print("=" * 50)
        
        answers = [
            ("1. Tipo de erro:", "KeyError - chave não encontrada em dicionário"),
            ("2. Linha do erro:", "Linha 20, função obter_vendas_vendedor"),
            ("3. Causa provável:", "vendedor 'Maria Silva' não existe no dict vendas"),
            ("4. Dados problemáticos:", "String 'Maria Silva' como chave"),
            ("5. Solução:", "Verificar se chave existe antes de acessar")
        ]
        
        for question, answer in answers:
            print(f"{question:<20} {answer}")
        
        print("\n💡 CÓDIGO CORRIGIDO:")
        print("=" * 50)
        
        fixed_code = '''
def obter_vendas_vendedor(vendas, vendedor):
    # Verificar se vendedor existe
    if vendedor not in vendas:
        print(f"⚠️ Vendedor '{vendedor}' não encontrado")
        return []
    
    return vendas[vendedor]

# Ou usando get() com valor padrão
def obter_vendas_vendedor_v2(vendas, vendedor):
    return vendas.get(vendedor, [])
        '''
        
        print(fixed_code)
        
        print("\n🎓 LIÇÕES APRENDIDAS:")
        print("=" * 50)
        print("✅ KeyError indica chave ausente em dicionário")
        print("✅ Sempre validar existência de chaves")
        print("✅ Usar .get() com valor padrão é mais seguro")
        print("✅ Stack trace mostra exatamente onde buscar")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _practice_with_real_bugs(self):
        """Prática com bugs reais"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐛 PRÁTICA COM BUGS REAIS", "Laboratório de Debugging")
        
        print("🎯 ESCOLHA UM CASO DE BUG PARA PRATICAR:")
        print("=" * 50)
        
        bug_cases = list(self.bug_cases.keys())
        for i, case_id in enumerate(bug_cases, 1):
            case = self.bug_cases[case_id]
            difficulty_icon = {"beginner": "🟢", "intermediate": "🟡", "advanced": "🔴"}.get(case.difficulty, "⚪")
            print(f"{i}. {difficulty_icon} {case.title}")
            print(f"   📝 {case.description}")
            print()
        
        print("0. 🔙 Voltar ao menu")
        
        try:
            choice = int(input("\nEscolha um caso (número): ").strip())
            if choice == 0:
                return
            elif 1 <= choice <= len(bug_cases):
                case_id = bug_cases[choice - 1]
                self._debug_case(case_id)
            else:
                print("❌ Opção inválida!")
                input("Pressione ENTER para continuar...")
        except ValueError:
            print("❌ Digite um número válido!")
            input("Pressione ENTER para continuar...")
    
    def _debug_case(self, case_id: str):
        """Guia o usuário através do debugging de um caso específico"""
        case = self.bug_cases[case_id]
        
        # Iniciar sessão de debugging
        session_id = f"debug_{case_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.current_session = DebugSession(
            session_id=session_id,
            start_time=datetime.now().isoformat(),
            bug_case_id=case_id,
            current_phase=DebugPhase.READ,
            user_hypotheses=[],
            user_actions=[],
            time_per_phase={},
            success=False,
            total_time=0
        )
        
        if self.ui:
            self.ui.clear_screen()
            self.ui.header(f"🐛 CASO: {case.title}", f"Dificuldade: {case.difficulty.title()}")
        
        print("📋 DESCRIÇÃO DO PROBLEMA:")
        print("=" * 50)
        print(case.description)
        print()
        
        print("💻 CÓDIGO COM BUG:")
        print("=" * 50)
        print(case.buggy_code)
        print()
        
        print("❌ ERRO OBTIDO:")
        print("=" * 50)
        print(case.error_message)
        
        input("\n🔸 Pressione ENTER para começar o debugging metodológico...")
        
        # Guiar através das fases RSAD
        self._guide_through_rsad(case)
    
    def _guide_through_rsad(self, case: BugCase):
        """Guia o usuário através das fases RSAD"""
        
        # Fase READ
        self._guide_read_phase(case)
        
        # Fase SEARCH  
        self._guide_search_phase(case)
        
        # Fase ASK
        self._guide_ask_phase(case)
        
        # Fase DEBUG
        self._guide_debug_phase(case)
        
        # Fase VERIFY
        self._guide_verify_phase(case)
        
        # Mostrar solução e feedback
        self._show_solution_and_feedback(case)
    
    def _guide_read_phase(self, case: BugCase):
        """Guia fase READ"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📖 FASE READ", "Entenda o Problema")
        
        print("🎯 VAMOS ENTENDER O PROBLEMA COMPLETAMENTE")
        print("=" * 50)
        
        questions = [
            "Qual é a mensagem de erro exata?",
            "Em que linha o erro acontece?", 
            "O que o código deveria fazer nessa linha?",
            "Você consegue reproduzir o erro?"
        ]
        
        for i, question in enumerate(questions, 1):
            print(f"\n{i}️⃣ {question}")
            answer = input("   Sua resposta: ").strip()
            self.current_session.user_actions.append(f"READ Q{i}: {answer}")
            
            # Dar feedback específico
            if i == 1:  # Mensagem de erro
                if case.error_message.split(':')[0] in answer:
                    print("   ✅ Correto! Você identificou o tipo de erro.")
                else:
                    print(f"   💡 Dica: O erro é do tipo '{case.error_message.split(':')[0]}'")
        
        print("\n✅ Fase READ concluída! Você entendeu o problema.")
        input("🔸 Pressione ENTER para fase SEARCH...")
    
    def _guide_search_phase(self, case: BugCase):
        """Guia fase SEARCH"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔍 FASE SEARCH", "Colete Evidências")
        
        print("🎯 VAMOS BUSCAR PISTAS E EVIDÊNCIAS")
        print("=" * 50)
        
        print("💻 CÓDIGO PARA ANÁLISE:")
        print("-" * 30)
        print(case.buggy_code)
        
        search_questions = [
            "Que variáveis estão envolvidas no erro?",
            "Quais são os valores dessas variáveis?", 
            "Existe algum padrão ou condição especial?",
            "O que você observa de diferente do esperado?"
        ]
        
        for i, question in enumerate(search_questions, 1):
            print(f"\n{i}️⃣ {question}")
            answer = input("   Sua observação: ").strip()
            self.current_session.user_actions.append(f"SEARCH Q{i}: {answer}")
        
        print("\n🔍 Dica: Use prints estratégicos para investigar!")
        debug_suggestion = input("Onde você colocaria um print() para investigar? ")
        self.current_session.user_actions.append(f"SEARCH DEBUG: {debug_suggestion}")
        
        print("\n✅ Fase search concluída! Você coletou evidências.")
        input("🔸 Pressione ENTER para fase ASK...")
    
    def _guide_ask_phase(self, case: BugCase):
        """Guia fase ASK"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("❓ FASE ASK", "Formule Hipóteses")
        
        print("🎯 AGORA VAMOS FORMAR HIPÓTESES ESPECÍFICAS")
        print("=" * 50)
        
        print("💡 LEMBRE-SE:")
        print("   • Hipóteses devem ser ESPECÍFICAS e TESTÁVEIS")
        print("   • Base suas hipóteses nas evidências coletadas")
        print("   • Evite hipóteses vagas como 'algo está errado'")
        
        print(f"\n🔍 REVISANDO O ERRO: {case.error_message}")
        
        hypotheses_count = 0
        while hypotheses_count < 3:
            hypothesis = input(f"\n💭 Hipótese {hypotheses_count + 1}: ").strip()
            if not hypothesis:
                break
                
            self.current_session.user_hypotheses.append(hypothesis)
            
            # Avaliar qualidade da hipótese
            if len(hypothesis) > 20 and any(word in hypothesis.lower() for word in ['pode', 'talvez', 'parece', 'deve']):
                print("   ✅ Boa hipótese! Específica e testável.")
            else:
                print("   💡 Tente ser mais específico sobre a causa provável.")
            
            hypotheses_count += 1
        
        print(f"\n📝 Você formulou {len(self.current_session.user_hypotheses)} hipótese(s).")
        print("✅ Fase ASK concluída!")
        input("🔸 Pressione ENTER para fase DEBUG...")
    
    def _guide_debug_phase(self, case: BugCase):
        """Guia fase DEBUG"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐛 FASE DEBUG", "Teste suas Hipóteses")
        
        print("🎯 HORA DE TESTAR SUAS HIPÓTESES")
        print("=" * 50)
        
        print("📋 SUAS HIPÓTESES:")
        for i, hypothesis in enumerate(self.current_session.user_hypotheses, 1):
            print(f"{i}. {hypothesis}")
        
        print("\n🧪 COMO VOCÊ TESTARIA A PRIMEIRA HIPÓTESE?")
        test_method = input("Descreva seu método de teste: ").strip()
        self.current_session.user_actions.append(f"DEBUG TEST: {test_method}")
        
        print("\n💻 Que mudança mínima faria no código para testar?")
        code_change = input("Sua mudança: ").strip()
        self.current_session.user_actions.append(f"DEBUG CHANGE: {code_change}")
        
        # Simular teste da hipótese
        print("\n🔄 Simulando teste...")
        print("   • Aplicando sua mudança...")
        print("   • Executando código...")
        
        # Dar feedback baseado na solução conhecida
        if any(keyword in test_method.lower() for keyword in ['print', 'debug', 'verificar', 'testar']):
            print("   ✅ Excelente abordagem de teste!")
        else:
            print("   💡 Considere usar prints ou debugger para investigar.")
        
        print("\n✅ Fase DEBUG concluída!")
        input("🔸 Pressione ENTER para fase VERIFY...")
    
    def _guide_verify_phase(self, case: BugCase):
        """Guia fase VERIFY"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("✅ FASE VERIFY", "Confirme a Solução")
        
        print("🎯 VAMOS VERIFICAR SE A SOLUÇÃO ESTÁ CORRETA")
        print("=" * 50)
        
        verify_questions = [
            "Como você testaria se o bug foi realmente corrigido?",
            "Que casos de teste usaria para ter certeza?",
            "Como garantiria que não criou novos bugs?"
        ]
        
        for i, question in enumerate(verify_questions, 1):
            print(f"\n{i}️⃣ {question}")
            answer = input("   Sua estratégia: ").strip()
            self.current_session.user_actions.append(f"VERIFY Q{i}: {answer}")
        
        print("\n✅ Fase VERIFY concluída!")
        self.current_session.success = True
        input("🔸 Pressione ENTER para ver a solução oficial...")
    
    def _show_solution_and_feedback(self, case: BugCase):
        """Mostra solução oficial e feedback personalizado"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 SOLUÇÃO OFICIAL", f"Caso: {case.title}")
        
        print("💡 SOLUÇÃO CORRETA:")
        print("=" * 50)
        print(case.fixed_code)
        
        print("\n📝 EXPLICAÇÃO:")
        print("=" * 50)
        print(case.explanation)
        
        print("\n🎯 PASSOS DA SOLUÇÃO:")
        print("=" * 50)
        for i, step in enumerate(case.solution_steps, 1):
            print(f"{i}. {step}")
        
        print("\n🧠 CONCEITOS APRENDIDOS:")
        print("=" * 50)
        for concept in case.concepts:
            print(f"   • {concept}")
        
        # Feedback personalizado baseado nas ações do usuário
        self._provide_personalized_feedback()
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _provide_personalized_feedback(self):
        """Fornece feedback personalizado baseado na sessão"""
        print("\n📊 SEU DESEMPENHO:")
        print("=" * 50)
        
        # Analisar qualidade das hipóteses
        good_hypotheses = sum(1 for h in self.current_session.user_hypotheses 
                             if len(h) > 15)
        
        if good_hypotheses >= 2:
            print("✅ Excelente formulação de hipóteses!")
        elif good_hypotheses >= 1:
            print("👍 Boas hipóteses, continue praticando!")
        else:
            print("💡 Dica: Tente ser mais específico nas hipóteses.")
        
        # Analisar uso de debugging
        debug_actions = sum(1 for action in self.current_session.user_actions
                           if any(word in action.lower() for word in ['print', 'debug', 'testar']))
        
        if debug_actions >= 2:
            print("✅ Ótimo uso de técnicas de debugging!")
        else:
            print("💡 Dica: Use mais prints e debugging para investigar.")
        
        print(f"\n📈 Total de ações realizadas: {len(self.current_session.user_actions)}")
        print("🎉 Parabéns por completar o debugging metodológico!")
    
    def _interactive_debugging(self):
        """Debugging interativo com breakpoints"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔍 DEBUGGING INTERATIVO", "Breakpoints e Step-by-Step")
        
        print("🎯 APRENDENDO DEBUGGING INTERATIVO")
        print("=" * 50)
        print("🔍 Debugging interativo permite:")
        print("   • Pausar execução em pontos específicos")
        print("   • Examinar valores de variáveis")
        print("   • Executar código passo a passo")
        print("   • Modificar valores durante execução")
        
        print("\n🛠️ FERRAMENTAS DISPONÍVEIS:")
        print("=" * 50)
        print("1. 🐍 pdb (Python Debugger) - Nativo")
        print("2. 🔧 IDE Debuggers (PyCharm, VSCode)")
        print("3. 💻 ipdb - Versão melhorada do pdb")
        print("4. 🚀 Debug prints estratégicos")
        
        print("\n📚 ESCOLHA UMA TÉCNICA PARA APRENDER:")
        print("=" * 50)
        print("1. 🐍 Tutorial PDB Interativo")
        print("2. 🔧 Breakpoints Estratégicos")
        print("3. 📊 Debugging com Prints Inteligentes")
        print("4. 🎯 Debugging de Performance")
        print("0. 🔙 Voltar")
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            self._pdb_tutorial()
        elif choice == "2":
            self._breakpoints_tutorial()
        elif choice == "3":
            self._smart_prints_tutorial()
        elif choice == "4":
            self._performance_debugging_tutorial()
    
    def _pdb_tutorial(self):
        """Tutorial interativo do PDB"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🐍 TUTORIAL PDB", "Python Debugger")
        
        print("🎯 PDB - PYTHON DEBUGGER NATIVO")
        print("=" * 50)
        
        pdb_example = '''
import pdb

def calcular_preco_total(itens):
    total = 0
    for item in itens:
        pdb.set_trace()  # BREAKPOINT aqui!
        preco = item['preco']
        quantidade = item['quantidade']
        subtotal = preco * quantidade
        total += subtotal
    return total

# Teste
produtos = [
    {'nome': 'Livro', 'preco': 25.90, 'quantidade': 2},
    {'nome': 'Caneta', 'preco': 3.50, 'quantidade': 'cinco'}  # BUG aqui!
]

resultado = calcular_preco_total(produtos)
print(f"Total: R$ {resultado}")
        '''
        
        print("💻 CÓDIGO EXEMPLO:")
        print(pdb_example)
        
        print("\n🔧 COMANDOS PDB ESSENCIAIS:")
        print("=" * 50)
        pdb_commands = [
            ("n (next)", "Próxima linha"),
            ("s (step)", "Entrar na função"),
            ("c (continue)", "Continuar execução"),
            ("l (list)", "Mostrar código atual"),
            ("p <var>", "Imprimir variável"),
            ("pp <var>", "Pretty print variável"),
            ("w (where)", "Mostrar stack trace"),
            ("q (quit)", "Sair do debugger")
        ]
        
        for command, description in pdb_commands:
            print(f"   {command:<15} - {description}")
        
        print("\n🎯 FLUXO DE DEBUGGING:")
        print("=" * 50)
        print("1. Execute o código")
        print("2. Execução para no pdb.set_trace()")
        print("3. Use 'p item' para ver o valor atual")
        print("4. Use 'n' para próxima linha")
        print("5. Observe quando o erro acontece")
        print("6. Use 'p quantidade' para ver o problema")
        
        print("\n💡 VOCÊ DESCOBRIRIA:")
        print("   • 'quantidade' é string 'cinco' em vez de número")
        print("   • Multiplicação falha: int * str")
        print("   • Solução: validar tipo ou converter")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _breakpoints_tutorial(self):
        """Tutorial sobre breakpoints estratégicos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔧 BREAKPOINTS ESTRATÉGICOS", "Onde e Quando Parar")
        
        print("🎯 ONDE COLOCAR BREAKPOINTS EFICAZES")
        print("=" * 50)
        
        strategies = [
            ("🔴 Antes do erro", "Logo antes da linha que falha"),
            ("🟡 Entrada de funções", "Primeira linha de funções suspeitas"),
            ("🟢 Loops", "Dentro de loops para ver iterações"),
            ("🔵 Condicionais", "Antes de if/else importantes"),
            ("🟣 Retornos", "Antes de return statements"),
            ("⚫ Depois de mudanças", "Após modificações de variáveis")
        ]
        
        for icon, strategy in strategies:
            print(f"   {icon} {strategy}")
        
        print("\n💻 EXEMPLO PRÁTICO:")
        print("=" * 50)
        
        example = '''
def processar_pedidos(pedidos):
    # 🔴 Breakpoint aqui para ver entrada
    total_vendas = 0
    
    for pedido in pedidos:
        # 🟢 Breakpoint para cada iteração
        if pedido['status'] == 'ativo':
            # 🔵 Breakpoint para casos ativos
            valor = calcular_valor(pedido)
            # 🟣 Breakpoint para ver valor calculado
            total_vendas += valor
    
    # ⚫ Breakpoint antes do retorno
    return total_vendas
        '''
        
        print(example)
        
        print("\n🧠 ESTRATÉGIA DE DEBUGGING:")
        print("=" * 50)
        print("1. 🎯 Comece com breakpoint geral")
        print("2. 🔍 Identifique área problemática")
        print("3. 🎪 Coloque breakpoints específicos")
        print("4. 📊 Examine variáveis em cada parada")
        print("5. 🚀 Remova breakpoints desnecessários")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _smart_prints_tutorial(self):
        """Tutorial sobre debugging com prints inteligentes"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("📊 PRINTS INTELIGENTES", "Debugging sem Debugger")
        
        print("🎯 PRINTS ESTRATÉGICOS PARA DEBUGGING")
        print("=" * 50)
        
        smart_print_techniques = '''
# 1. Print com contexto
print(f"DEBUG [linha 25]: valor_x = {valor_x}, tipo = {type(valor_x)}")

# 2. Print de entrada/saída de função
def minha_funcao(param):
    print(f"ENTRADA minha_funcao: param = {param}")
    resultado = processo(param)
    print(f"SAÍDA minha_funcao: resultado = {resultado}")
    return resultado

# 3. Print de loops
for i, item in enumerate(items):
    print(f"LOOP iteração {i}: processando {item}")
    
# 4. Print condicional
if condicao_especial:
    print(f"DEBUG: condição especial ativada com valor {valor}")

# 5. Print com timestamp
import datetime
print(f"[{datetime.datetime.now()}] Checkpoint: variável = {variável}")

# 6. Print formatado para listas/dicts
import json
print(f"DEBUG dados: {json.dumps(dados, indent=2)}")
        '''
        
        print("💻 TÉCNICAS AVANÇADAS:")
        print(smart_print_techniques)
        
        print("\n🎨 FORMATAÇÃO VISUAL:")
        print("=" * 50)
        
        visual_debugging = '''
# Separadores visuais
print("="*50)
print("DEBUG: Iniciando processamento")
print("="*50)

# Prints coloridos (terminal que suporta)
print("\\033[91mERRO: Valor inválido\\033[0m")  # Vermelho
print("\\033[92mSUCESSO: Processado\\033[0m")   # Verde
print("\\033[93mAVISO: Verificar\\033[0m")      # Amarelo

# Print com indentação para hierarquia
def debug_print(msg, level=0):
    indent = "  " * level
    print(f"{indent}DEBUG: {msg}")
        '''
        
        print(visual_debugging)
        
        print("\n💡 MELHORES PRÁTICAS:")
        print("=" * 50)
        print("✅ Use prefixo 'DEBUG:' para identificar")
        print("✅ Inclua nome da variável e valor")
        print("✅ Mostre tipo quando relevante")
        print("✅ Use prints temporários - remova depois")
        print("✅ Considere usar logging em vez de print")
        print("❌ Não deixe prints no código final")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _performance_debugging_tutorial(self):
        """Tutorial sobre debugging de performance"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🚀 DEBUGGING DE PERFORMANCE", "Otimização e Profiling")
        
        print("🎯 IDENTIFICANDO GARGALOS DE PERFORMANCE")
        print("=" * 50)
        
        print("⏱️ MEDIÇÃO DE TEMPO:")
        timing_code = '''
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tempo
def operacao_lenta():
    # Simular operação lenta
    time.sleep(1)
    return "concluído"
        '''
        
        print(timing_code)
        
        print("\n📊 PROFILING COM CPROFILE:")
        profiling_code = '''
import cProfile
import pstats

# Executar com profiling
pr = cProfile.Profile()
pr.enable()

# Código a ser analisado
resultado = minha_funcao_lenta()

pr.disable()

# Analisar resultados
stats = pstats.Stats(pr)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 funções mais lentas
        '''
        
        print(profiling_code)
        
        print("\n🔍 IDENTIFICANDO PROBLEMAS COMUNS:")
        print("=" * 50)
        common_issues = [
            "🐌 Loops ineficientes (O(n²) vs O(n))",
            "💾 Uso excessivo de memória",
            "🔄 Operações repetitivas desnecessárias",
            "📚 Imports dentro de loops",
            "🗃️ Acesso ineficiente a bancos de dados",
            "📝 Concatenação de strings em loops"
        ]
        
        for issue in common_issues:
            print(f"   {issue}")
        
        print("\n💡 DICAS DE OTIMIZAÇÃO:")
        print("=" * 50)
        print("✅ Use list comprehensions quando apropriado")
        print("✅ Cache resultados de operações caras")
        print("✅ Use generators para grandes datasets")
        print("✅ Perfil antes de otimizar")
        print("✅ Otimize apenas gargalos reais")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def _show_bug_library(self):
        """Biblioteca de bugs comuns"""
        pass
    
    def _debugging_challenges(self):
        """Desafios de debugging"""
        pass
    
    def _show_debugging_progress(self):
        """Progresso do usuário em debugging"""
        pass