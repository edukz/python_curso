#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 29: APIs e Web
Aprenda a criar APIs REST, usar FastAPI e desenvolver serviços web
"""

import time
from ..shared.base_module import BaseModule


class Modulo29ApisWeb(BaseModule):
    """Módulo 29: APIs e Web - Desenvolvimento de Serviços Web"""
    
    def __init__(self):
        super().__init__("modulo_29", "APIs e Web")
        self.has_mini_project = True
        self.mini_project_points = 100
    
    def execute(self) -> None:
        """Executa o módulo sobre APIs e Web"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._apis_web_principal()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _apis_web_principal(self) -> None:
        """Conteúdo principal do módulo APIs e Web"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌐 MÓDULO 29: APIs E WEB")
        else:
            print("\n" + "="*50)
            print("🌐 MÓDULO 29: APIs E WEB")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🌐 Bem-vindo ao mundo das APIs e desenvolvimento web! 🎉")
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
            self._mini_projeto_api_completa()
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
                'id': 'secao_conceito_apis',
                'titulo': '🎯 O que são APIs?',
                'descricao': 'Entenda o conceito fundamental de APIs',
                'funcao': self._secao_conceito_apis
            },
            {
                'id': 'secao_como_funcionam',
                'titulo': '⚙️ Como APIs funcionam?',
                'descricao': 'Veja o processo de comunicação passo a passo',
                'funcao': self._secao_como_funcionam
            },
            {
                'id': 'secao_exemplos_praticos',
                'titulo': '💡 Exemplos práticos com Flask',
                'descricao': 'Veja APIs em ação com código real',
                'funcao': self._secao_exemplos_praticos
            },
            {
                'id': 'secao_fastapi_moderno',
                'titulo': '🚀 FastAPI - O futuro das APIs',
                'descricao': 'Descubra o framework mais moderno',
                'funcao': self._secao_fastapi_moderno
            },
            {
                'id': 'secao_autenticacao_seguranca',
                'titulo': '🔐 Autenticação e segurança',
                'descricao': 'Proteja suas APIs como um profissional',
                'funcao': self._secao_autenticacao_seguranca
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas de APIs',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas',
                'descricao': 'Dicas de profissionais experientes',
                'funcao': self._secao_melhores_praticas
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
    
    def _secao_conceito_apis(self) -> None:
        """Seção: O que são APIs?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO APIs?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "API (Application Programming Interface)",
            "Uma interface que permite que diferentes sistemas 'conversem' entre si, trocando informações de forma padronizada."
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("APIs são como garçons em um restaurante - eles levam seu pedido para a cozinha e trazem de volta o que você pediu!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine que você está em um restaurante:", "text")
        self.print_colored("- VOCÊ é o cliente (aplicação que faz o pedido)", "text")
        self.print_colored("- GARÇOM é a API (intermediário que leva e traz informações)", "text")
        self.print_colored("- COZINHA é o servidor (onde os dados são processados)", "text")
        self.print_colored("- PRATO é a resposta (dados que você recebe de volta)", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 📱 Aplicação faz uma REQUISIÇÃO (HTTP GET, POST, etc.)",
            "2. 🌐 API recebe e processa a requisição",
            "3. 💾 Servidor busca/modifica dados conforme necessário",
            "4. 📄 API retorna uma RESPOSTA (geralmente em JSON)"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Fazendo uma requisição para uma API simples
import requests

# Requisição GET para buscar informações
response = requests.get("https://api.github.com/users/python")

# Verificar se deu certo
if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}")
    print(f"Repositórios públicos: {dados['public_repos']}")
else:
    print(f"Erro: {response.status_code}")'''
        
        self.exemplo(codigo_exemplo)
        
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "WhatsApp - API para enviar mensagens entre dispositivos",
            "Instagram - API para carregar fotos e stories",
            "Netflix - API para buscar filmes e séries",
            "Spotify - API para reproduzir músicas",
            "Google Maps - API para calcular rotas"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_como_funcionam(self) -> None:
        """Seção: Como APIs funcionam?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO APIS FUNCIONAM?", "⚙️", "success")
        
        self.print_colored("🔍 Vamos desvendar o processo passo a passo:", "text")
        
        # === HTTP METHODS ===
        self.print_colored("\n📡 MÉTODOS HTTP - As Ações da API:", "accent")
        
        metodos = [
            ("GET", "🔍 Buscar dados", "Como pedir o cardápio"),
            ("POST", "➕ Criar novos dados", "Como fazer um novo pedido"),
            ("PUT", "✏️ Atualizar dados completos", "Como trocar todo o pedido"),
            ("DELETE", "🗑️ Remover dados", "Como cancelar o pedido")
        ]
        
        for metodo, descricao, analogia in metodos:
            self.print_colored(f"\n{metodo}: {descricao}", "warning")
            self.print_colored(f"   {analogia}", "text")
            input("   ⏳ Pressione ENTER para o próximo método...")
        
        # === STATUS CODES ===
        self.print_colored("\n📊 CÓDIGOS DE RESPOSTA - Como a API responde:", "accent")
        
        status_codes = [
            ("200 OK", "✅ Sucesso total", "Pedido servido perfeitamente!"),
            ("201 Created", "🆕 Criado com sucesso", "Novo prato adicionado ao cardápio!"),
            ("400 Bad Request", "❌ Pedido mal feito", "Você pediu pizza de chocolate..."),
            ("401 Unauthorized", "🚫 Sem permissão", "Você não tem cartão VIP"),
            ("404 Not Found", "🔍 Não encontrado", "Esse prato não existe no cardápio"),
            ("500 Internal Server Error", "💥 Erro do servidor", "A cozinha pegou fogo!")
        ]
        
        for codigo, significado, analogia in status_codes:
            self.print_colored(f"{codigo}: {significado}", "info")
            self.print_colored(f"   {analogia}", "text")
            time.sleep(0.5)
        
        # === JSON FORMAT ===
        self.print_colored("\n📄 FORMATO JSON - A Linguagem das APIs:", "accent")
        
        exemplo_json = '''{
    "usuario": {
        "id": 123,
        "nome": "João Silva",
        "email": "joao@exemplo.com",
        "ativo": true,
        "tags": ["desenvolvedor", "python", "api"]
    }
}'''
        
        self.print_code_section("EXEMPLO JSON", exemplo_json)
        
        self.print_tip("JSON é como um formulário bem organizado que computadores entendem perfeitamente!")
        
        self.pausar()
    
    def _secao_exemplos_praticos(self) -> None:
        """Seção: Exemplos práticos com Flask"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("EXEMPLOS PRÁTICOS COM FLASK", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: API Simples - Olá Mundo',
                'descricao': 'Uma API básica que responde com uma mensagem',
                'codigo': '''from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ola', methods=['GET'])
def ola_mundo():
    return jsonify({
        "mensagem": "Olá, mundo das APIs!",
        "status": "funcionando",
        "versao": "1.0"
    })

if __name__ == '__main__':
    app.run(debug=True)''',
                'explicacao': 'Esta API responde na rota /api/ola com um JSON simples'
            },
            {
                'titulo': 'EXEMPLO 2: API com Dados - Lista de Usuários',
                'descricao': 'Uma API que gerencia uma lista de usuários',
                'codigo': '''from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados
usuarios = [
    {"id": 1, "nome": "João", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria", "email": "maria@email.com"}
]

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({
        "usuarios": usuarios,
        "total": len(usuarios)
    })

@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    novo_usuario = request.json
    novo_usuario['id'] = len(usuarios) + 1
    usuarios.append(novo_usuario)
    
    return jsonify(novo_usuario), 201''',
                'explicacao': 'Esta API permite listar usuários (GET) e criar novos (POST)'
            },
            {
                'titulo': 'EXEMPLO 3: API com Validação e Erros',
                'descricao': 'Uma API robusta com tratamento de erros',
                'codigo': '''from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/calcular', methods=['POST'])
def calcular():
    try:
        dados = request.json
        
        # Validação
        if not dados or 'a' not in dados or 'b' not in dados:
            return jsonify({
                "erro": "Parâmetros 'a' e 'b' são obrigatórios"
            }), 400
        
        a = float(dados['a'])
        b = float(dados['b'])
        operacao = dados.get('operacao', 'soma')
        
        if operacao == 'soma':
            resultado = a + b
        elif operacao == 'multiplicacao':
            resultado = a * b
        else:
            return jsonify({
                "erro": "Operação não suportada"
            }), 400
        
        return jsonify({
            "resultado": resultado,
            "operacao": operacao,
            "valores": {"a": a, "b": b}
        })
        
    except ValueError:
        return jsonify({
            "erro": "Valores devem ser números"
        }), 400''',
                'explicacao': 'Esta API faz cálculos com validação completa e tratamento de erros'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Como usar esta API:")
            if i == 1:
                self.print_colored("GET http://localhost:5000/api/ola", "info")
            elif i == 2:
                self.print_colored("GET http://localhost:5000/api/usuarios", "info")
                self.print_colored("POST http://localhost:5000/api/usuarios", "info")
            else:
                self.print_colored("POST http://localhost:5000/api/calcular", "info")
                self.print_colored('{"a": 5, "b": 3, "operacao": "soma"}', "text")
            
            if exemplo['explicacao']:
                self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você viu Flask em ação! Vamos conhecer o FastAPI!")
        self.pausar()
    
    def _secao_fastapi_moderno(self) -> None:
        """Seção: FastAPI - O futuro das APIs"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("FASTAPI - O FUTURO DAS APIS", "🚀", "warning")
        
        self.print_colored("⚡ FastAPI é o framework mais moderno para criar APIs:", "text")
        
        # === VANTAGENS DO FASTAPI ===
        self.print_colored("\n🌟 POR QUE FASTAPI É INCRÍVEL:", "accent")
        
        vantagens = [
            "⚡ **Extremamente rápido** - Uma das APIs mais velozes do mundo",
            "📝 **Documentação automática** - Gera docs sem esforço extra",
            "🔍 **Validação automática** - Valida dados automaticamente",
            "💡 **Type hints** - Usa tipagem Python moderna",
            "🐞 **Menos bugs** - Detecta erros antes da execução",
            "📚 **Fácil de aprender** - Se você sabe Python, já sabe FastAPI!"
        ]
        
        for vantagem in vantagens:
            self.print_colored(f"  {vantagem}", "text")
            time.sleep(0.3)
        
        # === EXEMPLO FASTAPI ===
        self.print_colored("\n💻 EXEMPLO FASTAPI EM AÇÃO:", "success")
        
        codigo_fastapi = '''from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Minha API Incrível", version="1.0.0")

# Modelo de dados com validação automática
class Usuario(BaseModel):
    nome: str
    email: str
    idade: int
    ativo: bool = True

# Lista de usuários
usuarios_db = []

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API FastAPI!"}

@app.post("/usuarios/", response_model=Usuario)
async def criar_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario

@app.get("/usuarios/")
async def listar_usuarios():
    return {"usuarios": usuarios_db, "total": len(usuarios_db)}

# Documentação automática em: http://localhost:8000/docs'''
        
        self.exemplo(codigo_fastapi)
        
        # === COMPARAÇÃO FLASK VS FASTAPI ===
        self.print_colored("\n⚖️ FLASK VS FASTAPI:", "accent")
        
        comparacao = [
            ("📝 Validação", "Manual", "Automática"),
            ("📚 Documentação", "Manual", "Automática"),
            ("⚡ Performance", "Boa", "Excelente"),
            ("🔍 Type Hints", "Opcional", "Integrado"),
            ("📖 Curva de Aprendizado", "Simples", "Simples"),
            ("🎯 Melhor para", "APIs simples", "APIs modernas")
        ]
        
        print("\n" + "="*50)
        print(f"{'Aspecto':<15} {'Flask':<15} {'FastAPI':<15}")
        print("="*50)
        
        for aspecto, flask_val, fastapi_val in comparacao:
            print(f"{aspecto:<15} {flask_val:<15} {fastapi_val:<15}")
        
        print("="*50)
        
        # === DOCUMENTAÇÃO AUTOMÁTICA ===
        self.print_colored("\n📚 MAGIA DA DOCUMENTAÇÃO AUTOMÁTICA:", "accent")
        self.print_colored("FastAPI gera automaticamente:", "text")
        self.print_colored("• 📖 Swagger UI interativa em /docs", "info")
        self.print_colored("• 📋 ReDoc em /redoc", "info")
        self.print_colored("• 🔧 Schema OpenAPI em /openapi.json", "info")
        
        self.print_tip("Com FastAPI, você escreve código e ganha documentação de graça!")
        
        self.pausar()
    
    def _secao_autenticacao_seguranca(self) -> None:
        """Seção: Autenticação e segurança"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("AUTENTICAÇÃO E SEGURANÇA", "🔐", "warning")
        
        self.print_colored("🛡️ Proteger suas APIs é FUNDAMENTAL:", "text")
        
        # === TIPOS DE AUTENTICAÇÃO ===
        self.print_colored("\n🔑 TIPOS DE AUTENTICAÇÃO:", "accent")
        
        tipos_auth = [
            {
                'nome': 'API Key',
                'emoji': '🔑',
                'descricao': 'Chave secreta enviada no cabeçalho',
                'uso': 'APIs simples e serviços internos'
            },
            {
                'nome': 'JWT (JSON Web Token)',
                'emoji': '🎫',
                'descricao': 'Token assinado com informações do usuário',
                'uso': 'Aplicações web e mobile modernas'
            },
            {
                'nome': 'OAuth 2.0',
                'emoji': '🌐',
                'descricao': 'Padrão para login com Google, Facebook, etc.',
                'uso': 'Integração com redes sociais'
            },
            {
                'nome': 'Basic Auth',
                'emoji': '👤',
                'descricao': 'Usuário e senha em Base64',
                'uso': 'APIs internas e testes'
            }
        ]
        
        for auth in tipos_auth:
            self.print_colored(f"\n{auth['emoji']} {auth['nome']}", "warning")
            self.print_colored(f"   📝 {auth['descricao']}", "text")
            self.print_colored(f"   🎯 Usado em: {auth['uso']}", "info")
            input("   ⏳ Pressione ENTER para próximo tipo...")
        
        # === EXEMPLO JWT ===
        self.print_colored("\n💻 EXEMPLO: AUTENTICAÇÃO JWT:", "success")
        
        codigo_jwt = '''from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBearer()

# Chave secreta (em produção, use variável de ambiente!)
SECRET_KEY = "minha_chave_super_secreta"
ALGORITHM = "HS256"

def criar_token(dados: dict):
    """Cria um token JWT"""
    dados_token = dados.copy()
    expira = datetime.utcnow() + timedelta(hours=24)
    dados_token.update({"exp": expira})
    
    token = jwt.encode(dados_token, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verifica se o token é válido"""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@app.post("/login")
async def login(username: str, password: str):
    # Aqui você verificaria no banco de dados
    if username == "admin" and password == "123":
        token = criar_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/perfil")
async def perfil_usuario(username: str = Depends(verificar_token)):
    return {"username": username, "mensagem": "Dados do perfil"}'''
        
        self.exemplo(codigo_jwt)
        
        # === BOAS PRÁTICAS DE SEGURANÇA ===
        self.print_colored("\n🛡️ BOAS PRÁTICAS DE SEGURANÇA:", "accent")
        
        praticas = [
            "🔐 **Sempre use HTTPS** em produção",
            "🔑 **Nunca exponha chaves secretas** no código",
            "⏰ **Tokens devem expirar** (máximo 24h)",
            "🚫 **Valide TODAS as entradas** do usuário",
            "📝 **Log tentativas de acesso** suspeitas",
            "🔒 **Use rate limiting** para prevenir ataques",
            "💾 **Nunca salve senhas em texto puro**",
            "🎯 **Princípio do menor privilégio** - dê apenas acesso necessário"
        ]
        
        for pratica in praticas:
            self.print_colored(f"  {pratica}", "text")
            time.sleep(0.4)
        
        self.pausar()
    
    def _secao_casos_uso_reais(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR NA VIDA REAL?", "🌍", "accent")
        
        self.print_colored("🎯 APIs estão em TODOS os lugares:", "text")
        
        # === CASOS DE USO POR SETOR ===
        setores = [
            {
                'nome': 'E-commerce',
                'emoji': '🛒',
                'exemplos': [
                    'API de pagamento (Stripe, PayPal)',
                    'API de frete (Correios, transportadoras)',
                    'API de estoque (controle de produtos)',
                    'API de recomendações (produtos similares)'
                ]
            },
            {
                'nome': 'Redes Sociais',
                'emoji': '📱',
                'exemplos': [
                    'API de posts (criar, listar, curtir)',
                    'API de mensagens (chat em tempo real)',
                    'API de amigos (seguir, deixar de seguir)',
                    'API de upload (fotos e vídeos)'
                ]
            },
            {
                'nome': 'Fintech',
                'emoji': '💰',
                'exemplos': [
                    'API de transferências bancárias',
                    'API de consulta de CPF/CNPJ',
                    'API de cotações (moedas, ações)',
                    'API de histórico financeiro'
                ]
            },
            {
                'nome': 'IoT (Internet das Coisas)',
                'emoji': '🏠',
                'exemplos': [
                    'API de sensores (temperatura, umidade)',
                    'API de controle (ligar/desligar dispositivos)',
                    'API de monitoramento (consumo de energia)',
                    'API de automação (horários programados)'
                ]
            }
        ]
        
        for setor in setores:
            self.print_colored(f"\n{setor['emoji']} **{setor['nome'].upper()}**", "warning")
            for exemplo in setor['exemplos']:
                self.print_colored(f"  • {exemplo}", "text")
            input("   🔸 Pressione ENTER para próximo setor...")
        
        # === EMPRESAS FAMOSAS ===
        self.print_colored("\n🏢 EMPRESAS FAMOSAS E SUAS APIS:", "accent")
        
        empresas = [
            ("🌐 Google", "Maps, YouTube, Gmail, Drive, Translate"),
            ("📘 Facebook/Meta", "Login social, Posts, Messenger, WhatsApp Business"),
            ("🎵 Spotify", "Reproduzir músicas, Playlists, Descobrir artistas"),
            ("🎬 Netflix", "Catálogo de filmes, Recomendações, Histórico"),
            ("🛒 Amazon", "Produtos, Marketplace, AWS, Alexa"),
            ("💳 Stripe", "Pagamentos, Assinaturas, Marketplace"),
            ("🗺️ Uber", "Solicitar corrida, Rastreamento, Pagamento")
        ]
        
        for empresa, apis in empresas:
            self.print_colored(f"{empresa}: {apis}", "primary")
            time.sleep(0.3)
        
        # === OPORTUNIDADES DE CARREIRA ===
        self.print_colored("\n💼 OPORTUNIDADES DE CARREIRA:", "accent")
        
        carreiras = [
            "🧑‍💻 **Desenvolvedor Backend** - Criar e manter APIs",
            "🔧 **Arquiteto de Software** - Projetar sistemas de APIs",
            "🛡️ **Especialista em Segurança** - Proteger APIs",
            "📊 **Engenheiro de Dados** - APIs para Big Data",
            "☁️ **DevOps Engineer** - Deploy e monitoramento de APIs",
            "🎯 **Product Manager** - Definir funcionalidades de APIs"
        ]
        
        for carreira in carreiras:
            self.print_colored(f"  {carreira}", "text")
        
        self.print_success("\n🚀 O futuro é das APIs - e você pode fazer parte dele!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS", "⭐", "accent")
        
        self.print_colored("🎯 Dicas de profissionais experientes do mundo todo:", "text")
        
        praticas = [
            {
                'emoji': '📝',
                'titulo': 'DESIGN DE ENDPOINTS',
                'dica': 'Use nomes claros e consistentes para suas rotas',
                'exemplo': '/api/v1/usuarios em vez de /getUsers'
            },
            {
                'emoji': '📋',
                'titulo': 'VERSIONAMENTO',
                'dica': 'Sempre versione suas APIs para manter compatibilidade',
                'exemplo': '/api/v1/, /api/v2/ - nunca quebre APIs antigas'
            },
            {
                'emoji': '🔍',
                'titulo': 'VALIDAÇÃO RIGOROSA',
                'dica': 'Valide TODOS os dados de entrada',
                'exemplo': 'Tipos, tamanhos, formatos - não confie no frontend'
            },
            {
                'emoji': '📊',
                'titulo': 'CÓDIGOS DE STATUS CORRETOS',
                'dica': 'Use status HTTP apropriados para cada situação',
                'exemplo': '201 para criação, 400 para erro de entrada, 500 para erro interno'
            },
            {
                'emoji': '📖',
                'titulo': 'DOCUMENTAÇÃO COMPLETA',
                'dica': 'Documente como se fosse para seu futuro eu',
                'exemplo': 'Exemplos de requisições, respostas e códigos de erro'
            },
            {
                'emoji': '⚡',
                'titulo': 'PERFORMANCE',
                'dica': 'Implemente paginação e cache quando necessário',
                'exemplo': 'Limite de 50 itens por página, cache de 5 minutos'
            },
            {
                'emoji': '🛡️',
                'titulo': 'SEGURANÇA SEMPRE',
                'dica': 'Segurança não é opcional, é obrigatória',
                'exemplo': 'HTTPS, autenticação, rate limiting, validação'
            },
            {
                'emoji': '📈',
                'titulo': 'MONITORAMENTO',
                'dica': 'Monitore performance, erros e uso da API',
                'exemplo': 'Logs estruturados, métricas de latência, alertas'
            }
        ]
        
        for i, pratica in enumerate(praticas, 1):
            self.print_colored(f"\n{i}. {pratica['emoji']} {pratica['titulo']}", "warning")
            self.print_colored(f"   💡 {pratica['dica']}", "text")
            self.print_colored(f"   📝 Exemplo: {pratica['exemplo']}", "info")
            
            if i < len(praticas):
                input("   ⏳ Pressione ENTER para a próxima dica...")
        
        # === CHECKLIST FINAL ===
        self.print_colored("\n✅ CHECKLIST DE API PROFISSIONAL:", "success")
        checklist = [
            "□ Endpoints com nomes claros e consistentes",
            "□ Versionamento implementado (v1, v2, etc.)",
            "□ Validação completa de todas as entradas",
            "□ Códigos de status HTTP corretos",
            "□ Documentação detalhada e atualizada",
            "□ Autenticação e autorização implementadas",
            "□ Rate limiting para prevenir abuso",
            "□ Logs estruturados e monitoramento",
            "□ Testes automatizados (unitários e integração)",
            "□ Deploy seguro com HTTPS"
        ]
        
        for item in checklist:
            self.print_colored(f"  {item}", "text")
        
        self.print_success("\n🏆 Seguindo essas práticas, você criará APIs de nível mundial!")
        
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
                'title': 'Quiz: Conhecimentos sobre APIs e Web',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'O que significa API?',
                        'answer': ['application programming interface', 'interface de programação de aplicações', 'api'],
                        'hint': 'É uma interface que permite comunicação entre sistemas'
                    },
                    {
                        'question': 'Qual método HTTP é usado para buscar dados?',
                        'answer': ['get', 'http get'],
                        'hint': 'Método para "pegar" ou "buscar" informações'
                    },
                    {
                        'question': 'Qual código de status indica sucesso na criação de um recurso?',
                        'answer': ['201', '201 created'],
                        'hint': 'É um código que começa com 2 e indica "criado"'
                    },
                    {
                        'question': 'Qual formato de dados é mais comum em APIs REST?',
                        'answer': ['json', 'json format'],
                        'hint': 'JavaScript Object Notation'
                    },
                    {
                        'question': 'Qual framework Python é conhecido por sua alta performance e documentação automática?',
                        'answer': ['fastapi', 'fast api'],
                        'hint': 'É "rápido" em inglês + API'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código da API',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a rota Flask para listar usuários',
                        'starter': 'from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route("/api/usuarios", methods=["GET"])\ndef listar_usuarios():\n    usuarios = [{"nome": "João"}, {"nome": "Maria"}]\n    # Complete aqui\n',
                        'solution': 'return jsonify({"usuarios": usuarios, "total": len(usuarios)})',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete a validação de dados no FastAPI',
                        'starter': 'from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel\n\nclass Usuario(BaseModel):\n    nome: str\n    email: str\n\n@app.post("/usuarios")\ndef criar_usuario(usuario: Usuario):\n    if not usuario.nome or len(usuario.nome) < 2:\n        # Complete aqui\n    return {"mensagem": "Usuário criado"}',
                        'solution': 'raise HTTPException(status_code=400, detail="Nome deve ter pelo menos 2 caracteres")',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete a autenticação JWT',
                        'starter': 'import jwt\nfrom datetime import datetime, timedelta\n\ndef criar_token(usuario_id: int):\n    payload = {\n        "user_id": usuario_id,\n        "exp": datetime.utcnow() + timedelta(hours=24)\n    }\n    # Complete aqui\n    return token',
                        'solution': 'token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256")',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Projete sua API',
                'type': 'creative',
                'instruction': 'Descreva uma API que você gostaria de criar! Qual seria o tema, que endpoints teria e como funcionaria?'
            }
        ]
        
        # === MENU PRINCIPAL DE EXERCÍCIOS ===
        while True:
            print("\nEscolha uma atividade:")
            print("1. 📝 Quiz de Conhecimentos")
            print("2. 💻 Complete o Código da API")
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
                elif escolha in ["2", "codigo", "completar", "api"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício de código interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício de código. Continuando...")
                elif escolha in ["3", "criativo", "projete"]:
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
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre APIs e desenvolvimento web",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos de programação",
            "🎨 OPÇÃO 3 - Exercício Criativo: Projete sua própria API do zero",
            "🔢 OPÇÃO 0 - Continue para o Mini Projeto: Sistema completo de API E-commerce",
            "",
            "💡 DICAS:",
            "• Você pode digitar o número ou palavras como 'quiz', 'codigo', 'criativo'",
            "• Digite 'help' a qualquer momento para ver esta ajuda",
            "• Use Ctrl+C se quiser voltar ao menu principal",
            "• Recomendamos fazer todas as atividades para dominar APIs!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_quiz(self, quiz_data: dict) -> None:
        """Executa um quiz interativo sobre APIs"""
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
            self.print_success("🌟 PERFEITO! Você dominou as APIs!")
        elif percentage >= 80:
            self.print_success("🎉 MUITO BEM! Você entende bem como APIs funcionam!")
        elif percentage >= 60:
            self.print_colored("😊 BOM TRABALHO! Revise alguns conceitos e tente novamente.", "warning")
        else:
            self.print_colored("📚 Continue estudando! Releia o conteúdo sobre APIs e Web.", "info")
            
        self.pausar()
    
    def _run_code_completion(self, exercise_data: dict) -> None:
        """Executa exercício de completar código de API"""
        self.print_section(exercise_data['title'], "💻")
        
        for i, ex in enumerate(exercise_data['exercises'], 1):
            print(f"\n🎯 EXERCÍCIO {i} de {len(exercise_data['exercises'])}:")
            print(f"📝 {ex['instruction']}")
            self.print_code_section("Código Inicial", ex['starter'])
            
            # Diferentes tipos de exercícios
            exercise_type = ex.get('type', 'simple')
            
            if exercise_type == 'simple':
                print("\n✍️ Complete o retorno da função:")
                print("💡 Dica: Use jsonify() para retornar JSON no Flask")
                print("📝 Exemplo: return jsonify({\"dados\": valor})")
                
                user_input = input(">>> ").strip()
                if 'jsonify' in user_input and 'return' in user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão. Lembre-se de usar jsonify() no Flask!")
                    
            elif exercise_type == 'intermediate':
                print("\n✍️ Complete o tratamento de erro:")
                print("💡 Dica: Use HTTPException no FastAPI")
                print("📝 Exemplo: raise HTTPException(status_code=400, detail=\"mensagem\")")
                
                user_input = input(">>> ").strip()
                if 'HTTPException' in user_input and 'raise' in user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão. Use HTTPException para erros no FastAPI!")
                    
            elif exercise_type == 'advanced':
                print("\n✍️ Complete a criação do token JWT:")
                print("💡 Dica: Use jwt.encode() com payload, chave secreta e algoritmo")
                print("📝 Exemplo: jwt.encode(dados, \"CHAVE\", algorithm=\"HS256\")")
                
                user_input = input(">>> ").strip()
                if 'jwt.encode' in user_input:
                    user_code = user_input
                else:
                    user_code = ex['solution']
                    self.print_tip("Usando solução padrão. Use jwt.encode() para gerar tokens!")
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
            
            print("\n🚀 Resultado do seu código:")
            self.print_code_section("COMPLETO", complete_code)
            
            print(f"\n💡 Solução sugerida: {ex['solution']}")
            self.print_success("✅ Muito bem! Você completou o código da API!")
            
            if i < len(exercise_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo exercício...")
        
        self.pausar()
    
    def _run_creative_exercise(self, exercise_data: dict) -> None:
        """Executa exercício criativo de design de API"""
        self.print_section(exercise_data['title'], "🎨")
        print(f"\n{exercise_data['instruction']}")
        print("💡 Exemplo: 'API de uma biblioteca para gerenciar livros, empréstimos e usuários'")
        print("🎯 Pense em algo que você usa no dia a dia e como uma API poderia ajudar!")
        
        nome_api = input("\n✍️ Nome da sua API: ").strip()
        if not nome_api:
            nome_api = "Minha API Incrível"
            
        descricao = input("📝 Descrição (o que faz?): ").strip()
        if not descricao:
            descricao = "Uma API útil e interessante"
            
        print("\n🛠️ Que endpoints sua API teria? (máximo 5)")
        print("📝 Exemplo: GET /livros, POST /emprestimos, DELETE /usuarios/123")
        endpoints = []
        for i in range(5):
            endpoint = input(f"Endpoint {i+1} (ou ENTER para parar): ").strip()
            if endpoint:
                endpoints.append(endpoint)
            else:
                break
        
        if nome_api and descricao:
            print("\n🌟 Sua API ficou incrível!")
            print(f"\n🎯 API: {nome_api.upper()}")
            print(f"📝 DESCRIÇÃO: {descricao}")
            
            # Mostrar endpoints
            if endpoints:
                print(f"\n🛠️ ENDPOINTS PROJETADOS:")
                for endpoint in endpoints:
                    # Identificar método HTTP
                    if endpoint.upper().startswith(('GET', 'POST', 'PUT', 'DELETE')):
                        self.print_colored(f"  📡 {endpoint}", "info")
                    else:
                        self.print_colored(f"  📡 GET {endpoint}", "info")
            
            # Código exemplo da API
            codigo_api = f'''# 🌐 API: {nome_api.upper()}
# {descricao}

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({{
        "api": "{nome_api}",
        "descricao": "{descricao}",
        "versao": "1.0.0",
        "status": "funcionando",
        "endpoints": {len(endpoints) if endpoints else 3}
    }})

@app.route("/status")
def status():
    return jsonify({{
        "status": "✅ API funcionando perfeitamente!",
        "timestamp": "2024-01-01T12:00:00Z"
    }})

if __name__ == "__main__":
    print("🚀 Iniciando {nome_api}...")
    print("📝 {descricao}")
    print("✅ API rodando em http://localhost:5000")
    app.run(debug=True)'''
            
            print("\n💻 CÓDIGO EXEMPLO GERADO:")
            self.exemplo(codigo_api)
            
            print("\n🚀 Simulando sua API:")
            self.executar_codigo(codigo_api)
            
            self.print_success("🎉 Parabéns! Você projetou uma API completa!")
            
            # Dicas personalizadas baseadas na descrição
            if any(palavra in descricao.lower() for palavra in ['loja', 'ecommerce', 'produto', 'venda']):
                self.print_tip("💡 Para APIs de e-commerce, considere: autenticação, carrinho, pagamentos, estoque")
            elif any(palavra in descricao.lower() for palavra in ['usuario', 'perfil', 'login', 'conta']):
                self.print_tip("💡 Para APIs de usuários, considere: JWT, roles, validação de email, recuperação de senha")
            elif any(palavra in descricao.lower() for palavra in ['biblioteca', 'livro', 'emprestimo']):
                self.print_tip("💡 Para APIs de biblioteca, considere: reservas, renovações, multas, categorias")
            else:
                self.print_tip("💡 Lembre-se: APIs bem documentadas e seguras são o segredo do sucesso!")
        else:
            self.print_warning("❌ Você precisa pelo menos dar um nome e descrição à sua API!")
        
        self.pausar()
    
    def _mini_projeto_api_completa(self) -> None:
        """Mini Projeto - Módulo 29: Sistema de API E-commerce Completo"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA API E-COMMERCE")
        else:
            print("\n" + "="*60)
            print("🎯 MINI PROJETO: SISTEMA API E-COMMERCE")
            print("="*60)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar seu sistema completo de API para e-commerce!")
        
        self.print_concept(
            "Sistema API E-commerce",
            "Uma API completa que gerencia produtos, usuários, carrinho de compras e pedidos, com autenticação, validação e segurança profissional."
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado por:", "text")
        usos_praticos = [
            "Amazon - Maior e-commerce do mundo com milhões de transações",
            "Mercado Livre - Marketplace líder na América Latina",
            "Shopify - Plataforma que alimenta milhares de lojas online",
            "Magento - Sistema de e-commerce usado por grandes marcas"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Coleta de informações da loja
        self.print_section("PASSO 1: Configuração da Loja", "📝", "info")
        self.print_tip("Vamos configurar as informações básicas da sua loja!")
        
        try:
            nome_loja = input("\n🏪 Nome da sua loja (ex: TechStore): ").strip()
            if not nome_loja:
                nome_loja = "MinhaLoja"
            
            categoria = input("🏷️ Categoria principal (ex: Eletrônicos, Roupas, Livros): ").strip()
            if not categoria:
                categoria = "Produtos Gerais"
            
            moeda = input("💰 Moeda (ex: R$, US$, €): ").strip()
            if not moeda:
                moeda = "R$"
                
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Processamento e criação da API
        self.print_section("PASSO 2: Gerando Sistema de API", "⚙️", "success")
        self.print_colored("Agora vamos criar seu sistema completo:", "text")
        
        # === SIMULAÇÃO DA CRIAÇÃO ===
        componentes = [
            f"🔧 Configurando API para {nome_loja}",
            "📦 Criando sistema de produtos",
            "👥 Implementando gestão de usuários",
            "🛒 Configurando carrinho de compras",
            "💳 Integrando sistema de pedidos",
            "🔐 Adicionando autenticação JWT",
            "📊 Criando dashboard de analytics",
            "📖 Gerando documentação automática"
        ]
        
        for componente in componentes:
            self.print_colored(f"  {componente}", "text")
            time.sleep(0.4)  # Simulação de processamento
        
        # PASSO 3: Resultado final
        self.print_section("PASSO 3: Sistema Completo", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está o sistema completo que você criou:", "text")
        
        codigo_final = f'''# 🛒 SISTEMA API E-COMMERCE: {nome_loja.upper()}
# Módulo 29: APIs e Web

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime, timedelta
import jwt
import hashlib
import secrets

# ================================
# CONFIGURAÇÃO DA API
# ================================

app = FastAPI(
    title="{nome_loja} API",
    description="Sistema completo de e-commerce com {categoria.lower()}",
    version="1.0.0"
)

security = HTTPBearer()
SECRET_KEY = secrets.token_urlsafe(32)

# ================================
# MODELOS DE DADOS
# ================================

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class Produto(BaseModel):
    nome: str
    preco: float
    categoria: str
    estoque: int
    descricao: Optional[str] = None

class ItemCarrinho(BaseModel):
    produto_id: int
    quantidade: int

class Pedido(BaseModel):
    usuario_id: int
    itens: List[ItemCarrinho]
    endereco: str

# ================================
# BANCO DE DADOS SIMULADO
# ================================

usuarios_db = []
produtos_db = [
    {{"id": 1, "nome": "Produto Premium", "preco": 299.99, "categoria": "{categoria}", "estoque": 50}},
    {{"id": 2, "nome": "Produto Básico", "preco": 99.99, "categoria": "{categoria}", "estoque": 100}},
    {{"id": 3, "nome": "Produto Avançado", "preco": 499.99, "categoria": "{categoria}", "estoque": 25}}
]
pedidos_db = []
carrinho_db = {{}}

# ================================
# FUNÇÕES DE AUTENTICAÇÃO
# ================================

def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_token(usuario_id: int) -> str:
    payload = {{
        "user_id": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# ================================
# ENDPOINTS DA API
# ================================

@app.get("/")
async def home():
    return {{
        "loja": "{nome_loja}",
        "categoria": "{categoria}",
        "status": "🚀 API funcionando!",
        "endpoints": {{
            "produtos": "/produtos",
            "usuarios": "/usuarios",
            "carrinho": "/carrinho",
            "pedidos": "/pedidos"
        }}
    }}

@app.post("/usuarios/cadastro")
async def cadastrar_usuario(usuario: Usuario):
    # Verificar se email já existe
    if any(u["email"] == usuario.email for u in usuarios_db):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    novo_usuario = {{
        "id": len(usuarios_db) + 1,
        "nome": usuario.nome,
        "email": usuario.email,
        "senha": hash_senha(usuario.senha),
        "criado_em": datetime.now()
    }}
    usuarios_db.append(novo_usuario)
    
    token = criar_token(novo_usuario["id"])
    return {{"mensagem": "Usuário cadastrado!", "token": token}}

@app.get("/produtos")
async def listar_produtos(categoria: Optional[str] = None):
    produtos = produtos_db
    if categoria:
        produtos = [p for p in produtos if p["categoria"].lower() == categoria.lower()]
    
    return {{
        "produtos": produtos,
        "total": len(produtos),
        "moeda": "{moeda}"
    }}

@app.post("/carrinho/adicionar")
async def adicionar_ao_carrinho(item: ItemCarrinho, user_id: int = Depends(verificar_token)):
    if user_id not in carrinho_db:
        carrinho_db[user_id] = []
    
    # Verificar se produto existe
    produto = next((p for p in produtos_db if p["id"] == item.produto_id), None)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if produto["estoque"] < item.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")
    
    carrinho_db[user_id].append(item.dict())
    return {{"mensagem": "Item adicionado ao carrinho!"}}

@app.post("/pedidos")
async def criar_pedido(pedido: Pedido, user_id: int = Depends(verificar_token)):
    total = 0.0
    
    for item in pedido.itens:
        produto = next((p for p in produtos_db if p["id"] == item.produto_id), None)
        if produto and produto["estoque"] >= item.quantidade:
            total += produto["preco"] * item.quantidade
            produto["estoque"] -= item.quantidade
        else:
            raise HTTPException(status_code=400, detail=f"Produto {{item.produto_id}} indisponível")
    
    novo_pedido = {{
        "id": len(pedidos_db) + 1,
        "usuario_id": user_id,
        "itens": pedido.itens,
        "total": total,
        "status": "confirmado",
        "criado_em": datetime.now()
    }}
    pedidos_db.append(novo_pedido)
    
    # Limpar carrinho
    carrinho_db[user_id] = []
    
    return {{
        "pedido_id": novo_pedido["id"],
        "total": f"{moeda} {{total:.2f}}",
        "status": "confirmado"
    }}

@app.get("/dashboard")
async def dashboard(user_id: int = Depends(verificar_token)):
    total_produtos = len(produtos_db)
    total_usuarios = len(usuarios_db)
    total_pedidos = len(pedidos_db)
    receita_total = sum(p.get("total", 0) for p in pedidos_db)
    
    return {{
        "loja": "{nome_loja}",
        "estatisticas": {{
            "produtos": total_produtos,
            "usuarios": total_usuarios,
            "pedidos": total_pedidos,
            "receita": f"{moeda} {{receita_total:.2f}}"
        }},
        "produtos_populares": produtos_db[:3]
    }}

# ================================
# EXECUTAR API
# ================================

if __name__ == "__main__":
    print("🛒 Iniciando {nome_loja} API...")
    print("📦 Categoria: {categoria}")
    print("💰 Moeda: {moeda}")
    print("✅ API rodando em http://localhost:8000")
    print("📖 Documentação em http://localhost:8000/docs")
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)'''

        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("DEMONSTRAÇÃO DO SISTEMA", "🎬", "warning")
        self.print_colored("🚀 Vamos simular o funcionamento da sua API:", "text")
        
        # Simulação da execução
        print(f"\n🛒 Iniciando {nome_loja} API...")
        time.sleep(0.5)
        print(f"📦 Categoria: {categoria}")
        time.sleep(0.5)
        print(f"💰 Moeda: {moeda}")
        time.sleep(0.5)
        print("✅ API rodando em http://localhost:8000")
        time.sleep(0.5)
        print("📖 Documentação automática gerada em /docs")
        time.sleep(0.5)
        
        # Simulação de estatísticas
        print(f"\n📊 ESTATÍSTICAS DA {nome_loja.upper()}:")
        estatisticas = [
            "👥 3 usuários cadastrados",
            "📦 3 produtos em estoque", 
            "🛒 2 pedidos realizados",
            f"💰 Receita total: {moeda} 899,97"
        ]
        
        for stat in estatisticas:
            print(f"  {stat}")
            time.sleep(0.3)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você criou um sistema completo de API E-commerce!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "Integrar com banco de dados real (PostgreSQL, MongoDB)",
            "Adicionar sistema de pagamento (Stripe, PayPal)",
            "Implementar notificações em tempo real (WebSockets)",
            "Criar sistema de avaliações e comentários",
            "Adicionar busca avançada com filtros",
            "Implementar sistema de cupons e descontos",
            "Criar painel administrativo completo"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Arquiteto de APIs E-commerce!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema API E-commerce Completo")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo29ApisWeb()
    print("Teste do módulo 29 - versão standalone")
    module._apis_web_principal()