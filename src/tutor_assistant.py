#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Tutor Assistente Offline
Fornece ajuda contextual e detecção de erros para alunos
"""

import re
from typing import Dict, List, Optional, Tuple, Any
from .utils import PythonCourseUtils
from .ui_components import UIComponents


class TutorAssistant:
    """Assistente de ensino com base de conhecimento offline"""
    
    def __init__(self):
        self.utils = PythonCourseUtils()
        self.ui = UIComponents()
        self.knowledge_base = self._build_knowledge_base()
        self.error_patterns = self._build_error_patterns()
        
    def _build_knowledge_base(self) -> Dict[str, Dict[str, Any]]:
        """Constrói base de conhecimento sobre Python"""
        return {
            # CONCEITOS FUNDAMENTAIS
            "variável": {
                "palavras_chave": ["variável", "variáveis", "var", "declarar", "criar variável"],
                "explicacao_simples": "Uma variável é como uma caixa etiquetada onde você guarda informações",
                "analogia": "Imagine gavetas organizadas: cada gaveta tem um nome (variável) e guarda algo dentro (valor)",
                "exemplos": [
                    "idade = 25        # Caixa 'idade' guarda o número 25",
                    "nome = 'João'     # Caixa 'nome' guarda o texto 'João'",
                    "preco = 19.99     # Caixa 'preco' guarda 19.99"
                ],
                "erros_comuns": [
                    "Usar espaços no nome: nome completo = 'Ana' ❌",
                    "Começar com número: 2nome = 'João' ❌",
                    "Usar palavras reservadas: for = 10 ❌"
                ],
                "dicas": [
                    "Use nomes descritivos: idade_usuario ao invés de x",
                    "Use snake_case: nome_completo ao invés de nomeCompleto",
                    "Evite acentos e caracteres especiais"
                ]
            },
            
            "print": {
                "palavras_chave": ["print", "imprimir", "mostrar", "exibir", "escrever"],
                "explicacao_simples": "print() é o comando para mostrar algo na tela",
                "analogia": "É como um alto-falante do programa - tudo que você colocar dentro, aparece na tela",
                "exemplos": [
                    'print("Olá, mundo!")     # Mostra: Olá, mundo!',
                    'print(42)                # Mostra: 42',
                    'print("Idade:", 25)      # Mostra: Idade: 25'
                ],
                "erros_comuns": [
                    'Print("olá") ❌  # P maiúsculo - Python diferencia maiúsculas',
                    'print "olá" ❌   # Esqueceu os parênteses',
                    "print('olá\") ❌  # Misturou tipos de aspas"
                ],
                "dicas": [
                    "Use vírgula para imprimir várias coisas: print('Nome:', nome)",
                    "Use f-strings para formatar: print(f'Idade: {idade}')",
                    "print() vazio pula uma linha"
                ]
            },
            
            "input": {
                "palavras_chave": ["input", "entrada", "perguntar", "ler", "pedir"],
                "explicacao_simples": "input() permite que o usuário digite algo",
                "analogia": "É como fazer uma pergunta e esperar a resposta - o programa pausa até o usuário digitar",
                "exemplos": [
                    'nome = input("Qual seu nome? ")    # Pede e guarda o nome',
                    'idade = int(input("Sua idade: "))  # Pede idade e converte para número',
                    'resposta = input()                 # Pede entrada sem mensagem'
                ],
                "erros_comuns": [
                    "Esquecer de converter para número: idade = input('Idade: ') ⚠️",
                    "Não guardar em variável: input('Nome: ') ⚠️ - perde o valor",
                    "Converter texto para int: int(input('Nome: ')) ❌"
                ],
                "dicas": [
                    "input() SEMPRE retorna texto (string)",
                    "Para números, use int() ou float()",
                    "Sempre valide entradas do usuário"
                ]
            },
            
            "if": {
                "palavras_chave": ["if", "se", "condição", "condicional", "decisão"],
                "explicacao_simples": "if permite que o programa tome decisões",
                "analogia": "Como um guarda de trânsito: SE o sinal está verde, ENTÃO pode passar",
                "exemplos": [
                    """idade = 18
if idade >= 18:
    print("Pode dirigir!")    # Só executa se idade >= 18""",
                    """senha = "123"
if senha == "123":
    print("Acesso permitido")
else:
    print("Senha incorreta")"""
                ],
                "erros_comuns": [
                    "Esquecer dois pontos: if x > 10 ❌",
                    "Não indentar: if x > 10:\\nprint('ok') ❌",
                    "Usar = ao invés de ==: if x = 10: ❌"
                ],
                "dicas": [
                    "Use == para comparar, = para atribuir",
                    "Indentação é OBRIGATÓRIA em Python",
                    "elif = else if (senão se)"
                ]
            },
            
            "loop": {
                "palavras_chave": ["loop", "for", "while", "repetir", "repetição", "laço"],
                "explicacao_simples": "Loops repetem código várias vezes",
                "analogia": "Como uma playlist no repeat - toca as músicas várias vezes",
                "exemplos": [
                    """# Loop for - repete 5 vezes
for i in range(5):
    print(f"Contando: {i}")""",
                    """# Loop while - repete enquanto verdadeiro
contador = 0
while contador < 3:
    print(contador)
    contador += 1"""
                ],
                "erros_comuns": [
                    "Loop infinito: while True: print('ops') ⚠️",
                    "Esquecer de incrementar: while x < 10: print(x) ⚠️",
                    "range(10) vai de 0 a 9, não 1 a 10"
                ],
                "dicas": [
                    "for = quando sabe quantas vezes",
                    "while = quando depende de condição",
                    "break sai do loop, continue pula para próxima"
                ]
            },
            
            "lista": {
                "palavras_chave": ["lista", "list", "array", "vetor", "coleção"],
                "explicacao_simples": "Lista é uma coleção ordenada de valores",
                "analogia": "Como uma fila de pessoas - cada uma tem sua posição (índice)",
                "exemplos": [
                    "frutas = ['maçã', 'banana', 'laranja']",
                    "numeros = [10, 20, 30, 40, 50]",
                    "mista = [1, 'dois', 3.0, True]    # Pode misturar tipos",
                    "frutas[0]     # Acessa primeiro item: 'maçã'",
                    "frutas.append('uva')    # Adiciona ao final"
                ],
                "erros_comuns": [
                    "Índice começa em 0, não 1",
                    "lista[5] em lista de 5 itens ❌ (vai de 0 a 4)",
                    "Modificar lista durante loop pode dar problema"
                ],
                "dicas": [
                    "Use len(lista) para saber o tamanho",
                    "lista[-1] acessa o último item",
                    "lista[1:3] fatia do índice 1 ao 2"
                ]
            },
            
            "função": {
                "palavras_chave": ["função", "def", "function", "método", "procedimento"],
                "explicacao_simples": "Função é um bloco de código reutilizável",
                "analogia": "Como uma receita de bolo - você cria uma vez e usa várias vezes",
                "exemplos": [
                    """def saudar(nome):
    print(f"Olá, {nome}!")
    
saudar("Maria")    # Chama a função""",
                    """def somar(a, b):
    return a + b
    
resultado = somar(5, 3)    # resultado = 8"""
                ],
                "erros_comuns": [
                    "Esquecer parênteses na chamada: saudar ❌",
                    "Não retornar valor quando necessário",
                    "Usar variável antes de definir função"
                ],
                "dicas": [
                    "Use verbos para nomear: calcular(), verificar()",
                    "Docstrings explicam o que a função faz",
                    "return encerra a função e retorna valor"
                ]
            },
            
            "tipo": {
                "palavras_chave": ["tipo", "type", "int", "str", "float", "bool"],
                "explicacao_simples": "Tipos definem que tipo de dado uma variável guarda",
                "analogia": "Como diferentes tipos de recipientes: copo para líquido, caixa para sólidos",
                "exemplos": [
                    "idade = 25           # int (número inteiro)",
                    "altura = 1.75        # float (número decimal)",
                    "nome = 'Ana'         # str (texto/string)",
                    "ativo = True         # bool (verdadeiro/falso)",
                    "type(idade)          # Mostra: <class 'int'>"
                ],
                "erros_comuns": [
                    "Somar string com número: '10' + 5 ❌",
                    "True/False com inicial maiúscula",
                    "Comparar tipos diferentes sem converter"
                ],
                "dicas": [
                    "Use int() para converter para inteiro",
                    "Use str() para converter para texto",
                    "Use float() para converter para decimal"
                ]
            }
        }
    
    def _build_error_patterns(self) -> List[Dict[str, Any]]:
        """Constrói padrões de detecção de erros comuns"""
        return [
            {
                "erro": "NameError",
                "regex": r"NameError: name '(\w+)' is not defined",
                "explicacao": "Você está tentando usar '{var}' mas ela não foi criada ainda",
                "causa_provavel": "A variável não foi declarada ou tem erro de digitação",
                "solucoes": [
                    "Verifique se digitou o nome corretamente",
                    "Declare a variável antes de usar: {var} = algum_valor",
                    "Python diferencia maiúsculas: 'Nome' é diferente de 'nome'"
                ],
                "exemplo_correto": "{var} = 'valor'  # Declare primeiro\nprint({var})     # Depois use"
            },
            
            {
                "erro": "SyntaxError",
                "regex": r"SyntaxError: invalid syntax",
                "explicacao": "Há um erro na forma como você escreveu o código",
                "causa_provavel": "Faltou algo ou tem caractere errado",
                "solucoes": [
                    "Verifique se tem : no final de if/for/while/def",
                    "Confira se fechou todos os parênteses, colchetes e aspas",
                    "Veja se não misturou aspas simples com duplas"
                ],
                "exemplo_correto": "if idade >= 18:  # Não esqueça os dois pontos\n    print('Maior')"
            },
            
            {
                "erro": "IndentationError",
                "regex": r"IndentationError: (.*)",
                "explicacao": "Problema com espaços/indentação do código",
                "causa_provavel": "Python usa espaços para organizar blocos de código",
                "solucoes": [
                    "Use 4 espaços (ou 1 tab) para cada nível",
                    "Mantenha consistência: ou sempre espaços ou sempre tabs",
                    "Código dentro de if/for/def deve estar indentado"
                ],
                "exemplo_correto": "if True:\n    print('Indentado com 4 espaços')"
            },
            
            {
                "erro": "TypeError",
                "regex": r"TypeError: (.+)",
                "explicacao": "Você está misturando tipos incompatíveis",
                "causa_provavel": "Tentando fazer operação entre tipos diferentes",
                "solucoes": [
                    "Converta os tipos: int('10') ou str(10)",
                    "Não pode somar string com número diretamente",
                    "Use vírgula no print para juntar diferentes tipos"
                ],
                "exemplo_correto": "idade = int(input('Idade: '))  # Converte para número"
            },
            
            {
                "erro": "ValueError",
                "regex": r"ValueError: (.+)",
                "explicacao": "O valor fornecido não é válido para a operação",
                "causa_provavel": "Tentando converter algo que não pode ser convertido",
                "solucoes": [
                    "int('abc') não funciona - apenas números",
                    "Valide entrada antes de converter",
                    "Use try/except para tratar erros"
                ],
                "exemplo_correto": "try:\n    num = int(input())\nexcept ValueError:\n    print('Digite um número!')"
            },
            
            {
                "erro": "IndexError",
                "regex": r"IndexError: list index out of range",
                "explicacao": "Você tentou acessar uma posição que não existe na lista",
                "causa_provavel": "A lista tem menos itens do que o índice usado",
                "solucoes": [
                    "Lembre: índices começam em 0",
                    "Lista de 5 itens vai de 0 a 4",
                    "Use len(lista) para verificar tamanho"
                ],
                "exemplo_correto": "lista = [1, 2, 3]\nif len(lista) > 3:\n    print(lista[3])"
            },
            
            {
                "erro": "AttributeError",
                "regex": r"AttributeError: '(\w+)' object has no attribute '(\w+)'",
                "explicacao": "O tipo '{tipo}' não tem o método/atributo '{attr}'",
                "causa_provavel": "Tentando usar método que não existe para esse tipo",
                "solucoes": [
                    "Verifique se digitou corretamente",
                    "Alguns métodos são específicos: append() é só de lista",
                    "Use dir(objeto) para ver métodos disponíveis"
                ],
                "exemplo_correto": "lista = []\nlista.append(10)  # append é método de lista"
            }
        ]
    
    def buscar_conceito(self, pergunta: str) -> Optional[Dict[str, Any]]:
        """Busca conceito relacionado à pergunta"""
        pergunta_lower = pergunta.lower()
        
        for conceito, info in self.knowledge_base.items():
            for palavra in info["palavras_chave"]:
                if palavra in pergunta_lower:
                    return info
        
        return None
    
    def analisar_erro(self, erro_msg: str) -> Optional[Dict[str, Any]]:
        """Analisa mensagem de erro e retorna explicação"""
        for pattern in self.error_patterns:
            match = re.search(pattern["regex"], erro_msg)
            if match:
                resultado = pattern.copy()
                
                # Substitui placeholders com valores capturados
                if match.groups():
                    grupos = match.groups()
                    if len(grupos) >= 1 and "{var}" in resultado["explicacao"]:
                        resultado["explicacao"] = resultado["explicacao"].replace("{var}", grupos[0])
                        resultado["exemplo_correto"] = resultado["exemplo_correto"].replace("{var}", grupos[0])
                    if len(grupos) >= 2:
                        resultado["explicacao"] = resultado["explicacao"].replace("{tipo}", grupos[0])
                        resultado["explicacao"] = resultado["explicacao"].replace("{attr}", grupos[1])
                
                return resultado
        
        return None
    
    def sessao_ajuda(self, modulo_atual: str = "") -> None:
        """Inicia sessão interativa de ajuda"""
        self.utils.limpar_tela()
        self.ui.header("ASSISTENTE PYTHON", "Tire suas dúvidas!", "🤖")
        
        print("👋 Olá! Sou seu assistente de Python!")
        if modulo_atual:
            print(f"📚 Vejo que você está no {modulo_atual}")
        
        print("\n🎯 COMO POSSO AJUDAR?")
        print("1. 🤔 Tenho uma dúvida sobre um conceito")
        print("2. ❌ Meu código está dando erro")
        print("3. 💡 Quero dicas sobre um tópico")
        print("4. 🔍 Ver todos os tópicos disponíveis")
        print("0. 🔙 Voltar ao menu")
        
        while True:
            try:
                escolha = input("\n👉 Escolha uma opção: ").strip()
                
                if escolha == "0":
                    break
                elif escolha == "1":
                    self._ajuda_conceito()
                elif escolha == "2":
                    self._ajuda_erro()
                elif escolha == "3":
                    self._dicas_topico()
                elif escolha == "4":
                    self._listar_topicos()
                else:
                    print("❌ Opção inválida!")
                    
            except KeyboardInterrupt:
                break
    
    def _ajuda_conceito(self) -> None:
        """Ajuda com conceitos"""
        print("\n💬 ASSISTENTE DE CONCEITOS")
        print("Exemplos de perguntas:")
        print("• O que é uma variável?")
        print("• Como funciona o if?")
        print("• Para que serve uma lista?")
        
        pergunta = input("\n❓ Sua dúvida: ").strip()
        
        if not pergunta:
            return
        
        conceito = self.buscar_conceito(pergunta)
        
        if conceito:
            self.ui.card(
                "Explicação",
                conceito["explicacao_simples"],
                "💡",
                "info"
            )
            
            print(f"\n🎯 ANALOGIA: {conceito['analogia']}")
            
            print("\n📝 EXEMPLOS:")
            for exemplo in conceito["exemplos"]:
                print(f"   {exemplo}")
            
            if conceito.get("erros_comuns"):
                print("\n⚠️ ERROS COMUNS:")
                for erro in conceito["erros_comuns"]:
                    print(f"   • {erro}")
            
            if conceito.get("dicas"):
                print("\n💡 DICAS PROFISSIONAIS:")
                for dica in conceito["dicas"]:
                    print(f"   ✨ {dica}")
        else:
            print("\n😕 Desculpe, não encontrei informações sobre esse tópico.")
            print("💡 Tente ser mais específico ou use palavras-chave como:")
            print("   variável, print, input, if, loop, lista, função, tipo")
        
        self.utils.pausar()
    
    def _ajuda_erro(self) -> None:
        """Ajuda com erros"""
        print("\n🔧 ASSISTENTE DE ERROS")
        print("Cole a mensagem de erro completa:")
        print("(Digite 'fim' em uma linha vazia para terminar)")
        
        linhas_erro = []
        while True:
            linha = input()
            if linha.lower() == 'fim':
                break
            linhas_erro.append(linha)
        
        erro_completo = "\n".join(linhas_erro)
        
        if not erro_completo:
            return
        
        analise = self.analisar_erro(erro_completo)
        
        if analise:
            self.ui.alert(f"Detectei: {analise['erro']}", "warning")
            
            self.ui.card(
                "O que aconteceu",
                analise["explicacao"],
                "🔍",
                "info"
            )
            
            print(f"\n🎯 CAUSA PROVÁVEL: {analise['causa_provavel']}")
            
            print("\n✅ COMO RESOLVER:")
            for i, solucao in enumerate(analise["solucoes"], 1):
                print(f"   {i}. {solucao}")
            
            print("\n📝 EXEMPLO CORRETO:")
            print("```python")
            print(analise["exemplo_correto"])
            print("```")
        else:
            print("\n🤔 Não consegui identificar o erro específico.")
            print("💡 DICAS GERAIS:")
            print("   • Verifique a ortografia de todas as palavras")
            print("   • Confira se fechou todos os parênteses e aspas")
            print("   • Veja se a indentação está correta")
            print("   • Certifique-se de que as variáveis foram declaradas")
        
        self.utils.pausar()
    
    def _dicas_topico(self) -> None:
        """Mostra dicas sobre um tópico"""
        print("\n✨ DICAS POR TÓPICO")
        print("Digite o tópico (ex: variável, loop, função):")
        
        topico = input("\n📚 Tópico: ").strip().lower()
        
        conceito = self.knowledge_base.get(topico)
        
        if conceito and conceito.get("dicas"):
            self.ui.card(
                f"Dicas sobre {topico.title()}",
                "\n".join(f"• {dica}" for dica in conceito["dicas"]),
                "💡",
                "success"
            )
        else:
            print("\n😕 Não encontrei dicas para esse tópico.")
            print("Tópicos disponíveis: variável, print, input, if, loop, lista, função, tipo")
        
        self.utils.pausar()
    
    def _listar_topicos(self) -> None:
        """Lista todos os tópicos disponíveis"""
        self.ui.header("TÓPICOS DISPONÍVEIS", "Base de Conhecimento", "📚")
        
        for i, (topico, info) in enumerate(self.knowledge_base.items(), 1):
            print(f"\n{i}. 📖 {topico.upper()}")
            print(f"   {info['explicacao_simples']}")
            print(f"   Palavras-chave: {', '.join(info['palavras_chave'][:3])}")
        
        self.utils.pausar()
    
    def gerar_exercicio_contextual(self, topico: str) -> Optional[str]:
        """Gera exercício baseado no tópico"""
        exercicios = {
            "variável": """🎯 EXERCÍCIO: Criando Variáveis
Crie variáveis para:
1. Sua idade (número)
2. Seu nome (texto)
3. Sua altura em metros (decimal)
4. Se você gosta de Python (verdadeiro/falso)

Depois use print() para mostrar todas!""",
            
            "if": """🎯 EXERCÍCIO: Sistema de Notas
Crie um programa que:
1. Peça a nota do aluno (0 a 10)
2. Se nota >= 7: "Aprovado!"
3. Se nota >= 5: "Recuperação"
4. Se nota < 5: "Reprovado"

Teste com diferentes valores!""",
            
            "loop": """🎯 EXERCÍCIO: Contagem Regressiva
Faça um programa que:
1. Peça um número ao usuário
2. Faça contagem regressiva até 0
3. No final mostre "🚀 Lançamento!"

Extra: pause 1 segundo entre números!""",
            
            "lista": """🎯 EXERCÍCIO: Lista de Compras
Crie um programa que:
1. Crie uma lista vazia
2. Peça 5 itens ao usuário
3. Adicione cada item à lista
4. Mostre a lista completa
5. Mostre quantos itens tem"""
        }
        
        return exercicios.get(topico)


class ErrorHelper:
    """Auxiliar específico para tratamento de erros em tempo real"""
    
    def __init__(self):
        self.tutor = TutorAssistant()
    
    def ajudar_com_erro(self, codigo: str, erro: Exception) -> None:
        """Fornece ajuda contextual para um erro específico"""
        erro_str = f"{type(erro).__name__}: {str(erro)}"
        
        print("\n" + "="*50)
        print("❌ ERRO DETECTADO!")
        print("="*50)
        
        # Analisa o erro
        analise = self.tutor.analisar_erro(erro_str)
        
        if analise:
            print(f"\n🔍 TIPO: {analise['erro']}")
            print(f"📝 EXPLICAÇÃO: {analise['explicacao']}")
            print(f"\n💡 SOLUÇÕES:")
            for sol in analise["solucoes"]:
                print(f"   • {sol}")
            
            if analise.get("exemplo_correto"):
                print(f"\n✅ EXEMPLO CORRETO:")
                print("```python")
                print(analise["exemplo_correto"])
                print("```")
        else:
            # Ajuda genérica
            print(f"\n❌ Erro: {erro_str}")
            print("\n💡 DICAS GERAIS:")
            
            if "NameError" in erro_str:
                print("   • Verifique se a variável foi declarada")
                print("   • Cuidado com maiúsculas/minúsculas")
            elif "SyntaxError" in erro_str:
                print("   • Verifique : no final de if/for/while")
                print("   • Confira parênteses e aspas")
            elif "IndentationError" in erro_str:
                print("   • Use 4 espaços para indentar")
                print("   • Mantenha consistência")
        
        print("\n🤖 Dica: Use 'A' no menu principal para mais ajuda!")
        print("="*50)