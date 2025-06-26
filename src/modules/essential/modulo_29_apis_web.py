#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 29: APIs e Web
Aprenda a criar APIs REST, usar FastAPI e desenvolver serviços web
"""

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
            self._apis_web()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _apis_web(self) -> None:
        """Conteúdo principal sobre APIs e Web"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🌐 MÓDULO 29: APIs E WEB")
        else:
            print("\n" + "="*50)
            print("🌐 MÓDULO 29: APIs E WEB")
            print("="*50)
        
        print("🌐 APIs são a BASE da comunicação moderna entre sistemas!")
        print("🚀 FastAPI e Flask permitem criar serviços web profissionais!")
        
        print("\n═══════════════════════════════════════════════")
        print("        O QUE SÃO APIs?")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 API (Application Programming Interface):")
        print("• 🔗 Interface para comunicação entre sistemas")
        print("• 📡 REST - Representational State Transfer")
        print("• 🌍 HTTP - protocolo de comunicação web")
        print("• 📄 JSON - formato de troca de dados")
        print("• 🔐 Autenticação e autorização")
        
        self.pausar()
        
        print("\n🌐 Criando API com Flask:")
        
        codigo1 = '''# API REST básica com Flask
from flask import Flask, jsonify, request
from datetime import datetime
import json

# Simulando banco de dados em memória
usuarios_db = [
    {"id": 1, "nome": "João Silva", "email": "joao@exemplo.com", "ativo": True},
    {"id": 2, "nome": "Maria Santos", "email": "maria@exemplo.com", "ativo": True},
    {"id": 3, "nome": "Carlos Lima", "email": "carlos@exemplo.com", "ativo": False},
]

produtos_db = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "categoria": "Eletrônicos"},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "categoria": "Acessórios"},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "categoria": "Acessórios"},
]

app = Flask(__name__)

# Middleware para CORS (Cross-Origin Resource Sharing)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# ===============================================
# ROTAS DE USUÁRIOS (CRUD Completo)
# ===============================================

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    """Listar todos os usuários"""
    # Filtro opcional por status
    ativo = request.args.get('ativo')
    if ativo is not None:
        ativo_bool = ativo.lower() == 'true'
        usuarios_filtrados = [u for u in usuarios_db if u['ativo'] == ativo_bool]
        return jsonify({
            "usuarios": usuarios_filtrados,
            "total": len(usuarios_filtrados),
            "filtro": f"ativo={ativo}"
        })
    
    return jsonify({
        "usuarios": usuarios_db,
        "total": len(usuarios_db),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/usuarios/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    """Obter usuário específico por ID"""
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    return jsonify(usuario)

@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    """Criar novo usuário"""
    dados = request.get_json()
    
    # Validação básica
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400
    
    # Verificar se email já existe
    if any(u['email'] == dados['email'] for u in usuarios_db):
        return jsonify({"erro": "Email já cadastrado"}), 409
    
    # Criar novo usuário
    novo_id = max(u['id'] for u in usuarios_db) + 1 if usuarios_db else 1
    novo_usuario = {
        "id": novo_id,
        "nome": dados['nome'],
        "email": dados['email'],
        "ativo": dados.get('ativo', True)
    }
    
    usuarios_db.append(novo_usuario)
    
    return jsonify({
        "mensagem": "Usuário criado com sucesso",
        "usuario": novo_usuario
    }), 201

@app.route('/api/usuarios/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    """Atualizar usuário existente"""
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400
    
    # Atualizar campos fornecidos
    if 'nome' in dados:
        usuario['nome'] = dados['nome']
    if 'email' in dados:
        # Verificar se novo email já existe em outro usuário
        if any(u['email'] == dados['email'] and u['id'] != user_id for u in usuarios_db):
            return jsonify({"erro": "Email já está em uso"}), 409
        usuario['email'] = dados['email']
    if 'ativo' in dados:
        usuario['ativo'] = dados['ativo']
    
    return jsonify({
        "mensagem": "Usuário atualizado com sucesso",
        "usuario": usuario
    })

@app.route('/api/usuarios/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    """Deletar usuário"""
    global usuarios_db
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    usuarios_db = [u for u in usuarios_db if u['id'] != user_id]
    
    return jsonify({"mensagem": f"Usuário {usuario['nome']} deletado com sucesso"})

# ===============================================
# ROTAS DE PRODUTOS
# ===============================================

@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    """Listar produtos com filtros opcionais"""
    categoria = request.args.get('categoria')
    preco_min = request.args.get('preco_min', type=float)
    preco_max = request.args.get('preco_max', type=float)
    
    produtos_filtrados = produtos_db.copy()
    
    # Aplicar filtros
    if categoria:
        produtos_filtrados = [p for p in produtos_filtrados if p['categoria'].lower() == categoria.lower()]
    
    if preco_min is not None:
        produtos_filtrados = [p for p in produtos_filtrados if p['preco'] >= preco_min]
    
    if preco_max is not None:
        produtos_filtrados = [p for p in produtos_filtrados if p['preco'] <= preco_max]
    
    return jsonify({
        "produtos": produtos_filtrados,
        "total": len(produtos_filtrados),
        "filtros_aplicados": {
            "categoria": categoria,
            "preco_min": preco_min,
            "preco_max": preco_max
        }
    })

@app.route('/api/produtos/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    """Obter produto específico"""
    produto = next((p for p in produtos_db if p['id'] == produto_id), None)
    
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    
    return jsonify(produto)

# ===============================================
# ROTAS DE ESTATÍSTICAS
# ===============================================

@app.route('/api/stats', methods=['GET'])
def estatisticas():
    """Retorna estatísticas gerais da API"""
    usuarios_ativos = len([u for u in usuarios_db if u['ativo']])
    total_produtos = len(produtos_db)
    categorias = list(set(p['categoria'] for p in produtos_db))
    
    preco_medio = sum(p['preco'] for p in produtos_db) / len(produtos_db) if produtos_db else 0
    
    return jsonify({
        "usuarios": {
            "total": len(usuarios_db),
            "ativos": usuarios_ativos,
            "inativos": len(usuarios_db) - usuarios_ativos
        },
        "produtos": {
            "total": total_produtos,
            "categorias": categorias,
            "preco_medio": round(preco_medio, 2)
        },
        "timestamp": datetime.now().isoformat()
    })

# ===============================================
# TRATAMENTO DE ERROS
# ===============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": "Endpoint não encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"erro": "Erro interno do servidor"}), 500

# ===============================================
# DOCUMENTAÇÃO DA API
# ===============================================

@app.route('/api', methods=['GET'])
def documentacao_api():
    """Documentação básica da API"""
    endpoints = {
        "usuarios": {
            "GET /api/usuarios": "Listar todos os usuários",
            "GET /api/usuarios/<id>": "Obter usuário específico",
            "POST /api/usuarios": "Criar novo usuário",
            "PUT /api/usuarios/<id>": "Atualizar usuário",
            "DELETE /api/usuarios/<id>": "Deletar usuário"
        },
        "produtos": {
            "GET /api/produtos": "Listar produtos (com filtros)",
            "GET /api/produtos/<id>": "Obter produto específico"
        },
        "estatisticas": {
            "GET /api/stats": "Estatísticas gerais"
        }
    }
    
    return jsonify({
        "nome": "API de Exemplo",
        "versao": "1.0.0",
        "descricao": "API REST para gerenciamento de usuários e produtos",
        "endpoints": endpoints,
        "exemplos": {
            "criar_usuario": {
                "url": "/api/usuarios",
                "metodo": "POST",
                "body": {
                    "nome": "João Silva",
                    "email": "joao@exemplo.com",
                    "ativo": True
                }
            },
            "filtrar_produtos": {
                "url": "/api/produtos?categoria=Eletrônicos&preco_min=100",
                "metodo": "GET"
            }
        }
    })

# Demonstração da API
print("=== API REST COM FLASK ===")
print()
print("🌐 API criada com sucesso!")
print("📋 Endpoints disponíveis:")
print("  • GET  /api/usuarios - Listar usuários")
print("  • POST /api/usuarios - Criar usuário")
print("  • GET  /api/produtos - Listar produtos")
print("  • GET  /api/stats - Estatísticas")
print()

# Simulação de requisições (sem executar o servidor)
print("🧪 SIMULAÇÃO DE REQUISIÇÕES:")
print()

# Simular GET usuarios
print("📡 GET /api/usuarios")
with app.test_client() as client:
    response = client.get('/api/usuarios')
    print(f"Status: {response.status_code}")
    data = response.get_json()
    print(f"Total de usuários: {data['total']}")
    print(f"Primeiro usuário: {data['usuarios'][0]['nome']}")

print()

# Simular POST usuario
print("📡 POST /api/usuarios")
with app.test_client() as client:
    novo_usuario = {
        "nome": "Ana Costa",
        "email": "ana@exemplo.com"
    }
    response = client.post('/api/usuarios', 
                          json=novo_usuario,
                          content_type='application/json')
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        data = response.get_json()
        print(f"Usuário criado: {data['usuario']['nome']}")

print()

# Simular GET produtos com filtro
print("📡 GET /api/produtos?categoria=Eletrônicos")
with app.test_client() as client:
    response = client.get('/api/produtos?categoria=Eletrônicos')
    data = response.get_json()
    print(f"Produtos encontrados: {data['total']}")
    if data['produtos']:
        print(f"Primeiro produto: {data['produtos'][0]['nome']}")

print()
print("✅ API Flask testada com sucesso!")
print("💡 Para executar: python app.py (em ambiente real)")'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n🚀 FastAPI - Framework Moderno:")
        
        codigo2 = '''# API moderna com FastAPI
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
import json

# Simulando FastAPI (sem instalação real)
class FastAPISimulator:
    """Simulador do FastAPI para demonstração"""
    
    def __init__(self):
        self.routes = {}
        self.middleware = []
    
    def get(self, path: str):
        def decorator(func):
            self.routes[f"GET {path}"] = func
            return func
        return decorator
    
    def post(self, path: str):
        def decorator(func):
            self.routes[f"POST {path}"] = func
            return func
        return decorator
    
    def put(self, path: str):
        def decorator(func):
            self.routes[f"PUT {path}"] = func
            return func
        return decorator
    
    def delete(self, path: str):
        def decorator(func):
            self.routes[f"DELETE {path}"] = func
            return func
        return decorator

# Simulação dos modelos Pydantic
class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

# Modelos de dados com Pydantic
class UsuarioBase(BaseModel):
    nome: str
    email: str
    ativo: bool = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    ativo: Optional[bool] = None

class Usuario(UsuarioBase):
    id: int
    data_criacao: datetime
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(self, 'data_criacao'):
            self.data_criacao = datetime.now()

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    categoria: str
    descricao: Optional[str] = None

class Produto(ProdutoBase):
    id: int
    data_criacao: datetime
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(self, 'data_criacao'):
            self.data_criacao = datetime.now()

# Resposta padronizada
class APIResponse(BaseModel):
    sucesso: bool
    mensagem: str
    dados: Optional[dict] = None
    timestamp: datetime
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(self, 'timestamp'):
            self.timestamp = datetime.now()

# Criando aplicação FastAPI (simulada)
app = FastAPISimulator()

# Banco de dados em memória
usuarios_db = []
produtos_db = []
proximo_id_usuario = 1
proximo_id_produto = 1

# ===============================================
# MIDDLEWARE E CONFIGURAÇÕES
# ===============================================

class AuthMiddleware:
    """Middleware de autenticação simulado"""
    
    @staticmethod
    def verificar_token(token: str) -> bool:
        # Simulação simples de verificação de token
        return token == "Bearer token_valido_123"
    
    @staticmethod
    def obter_usuario_do_token(token: str) -> dict:
        if AuthMiddleware.verificar_token(token):
            return {"id": 1, "nome": "Admin", "role": "admin"}
        return None

# ===============================================
# ENDPOINTS DE USUÁRIOS
# ===============================================

@app.get("/usuarios")
def listar_usuarios(ativo: Optional[bool] = None, limite: int = 10, offset: int = 0):
    """
    Listar usuários com paginação e filtros
    
    - **ativo**: Filtrar por status (True/False)
    - **limite**: Número máximo de resultados (padrão: 10)
    - **offset**: Número de registros para pular (padrão: 0)
    """
    usuarios_filtrados = usuarios_db.copy()
    
    # Aplicar filtro de status
    if ativo is not None:
        usuarios_filtrados = [u for u in usuarios_filtrados if u['ativo'] == ativo]
    
    # Aplicar paginação
    total = len(usuarios_filtrados)
    usuarios_paginados = usuarios_filtrados[offset:offset + limite]
    
    return APIResponse(
        sucesso=True,
        mensagem="Usuários listados com sucesso",
        dados={
            "usuarios": usuarios_paginados,
            "total": total,
            "limite": limite,
            "offset": offset,
            "tem_proximo": offset + limite < total
        }
    ).dict()

@app.get("/usuarios/{user_id}")
def obter_usuario(user_id: int):
    """Obter usuário específico por ID"""
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return {
            "sucesso": False,
            "mensagem": "Usuário não encontrado",
            "codigo_erro": "USER_NOT_FOUND"
        }
    
    return APIResponse(
        sucesso=True,
        mensagem="Usuário encontrado",
        dados={"usuario": usuario}
    ).dict()

@app.post("/usuarios")
def criar_usuario(usuario_data: dict):
    """Criar novo usuário com validação completa"""
    global proximo_id_usuario
    
    # Validação de dados obrigatórios
    if 'nome' not in usuario_data or 'email' not in usuario_data:
        return {
            "sucesso": False,
            "mensagem": "Nome e email são obrigatórios",
            "codigo_erro": "MISSING_REQUIRED_FIELDS"
        }
    
    # Validação de email único
    if any(u['email'] == usuario_data['email'] for u in usuarios_db):
        return {
            "sucesso": False,
            "mensagem": "Email já está em uso",
            "codigo_erro": "EMAIL_ALREADY_EXISTS"
        }
    
    # Criar usuário
    novo_usuario = {
        "id": proximo_id_usuario,
        "nome": usuario_data['nome'],
        "email": usuario_data['email'],
        "ativo": usuario_data.get('ativo', True),
        "data_criacao": datetime.now().isoformat(),
        "ultimo_acesso": None
    }
    
    usuarios_db.append(novo_usuario)
    proximo_id_usuario += 1
    
    return APIResponse(
        sucesso=True,
        mensagem="Usuário criado com sucesso",
        dados={"usuario": novo_usuario}
    ).dict()

@app.put("/usuarios/{user_id}")
def atualizar_usuario(user_id: int, usuario_update: dict):
    """Atualizar usuário existente"""
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return {
            "sucesso": False,
            "mensagem": "Usuário não encontrado",
            "codigo_erro": "USER_NOT_FOUND"
        }
    
    # Atualizar apenas campos fornecidos
    campos_atualizados = []
    
    if 'nome' in usuario_update:
        usuario['nome'] = usuario_update['nome']
        campos_atualizados.append('nome')
    
    if 'email' in usuario_update:
        # Verificar se email não está em uso por outro usuário
        if any(u['email'] == usuario_update['email'] and u['id'] != user_id for u in usuarios_db):
            return {
                "sucesso": False,
                "mensagem": "Email já está em uso por outro usuário",
                "codigo_erro": "EMAIL_ALREADY_EXISTS"
            }
        usuario['email'] = usuario_update['email']
        campos_atualizados.append('email')
    
    if 'ativo' in usuario_update:
        usuario['ativo'] = usuario_update['ativo']
        campos_atualizados.append('ativo')
    
    usuario['data_atualizacao'] = datetime.now().isoformat()
    
    return APIResponse(
        sucesso=True,
        mensagem=f"Usuário atualizado com sucesso. Campos: {', '.join(campos_atualizados)}",
        dados={"usuario": usuario}
    ).dict()

@app.delete("/usuarios/{user_id}")
def deletar_usuario(user_id: int):
    """Deletar usuário (soft delete)"""
    global usuarios_db
    usuario = next((u for u in usuarios_db if u['id'] == user_id), None)
    
    if not usuario:
        return {
            "sucesso": False,
            "mensagem": "Usuário não encontrado",
            "codigo_erro": "USER_NOT_FOUND"
        }
    
    # Soft delete (marcar como inativo) ao invés de deletar fisicamente
    usuario['ativo'] = False
    usuario['data_delecao'] = datetime.now().isoformat()
    
    return APIResponse(
        sucesso=True,
        mensagem=f"Usuário {usuario['nome']} desativado com sucesso",
        dados={"usuario_id": user_id}
    ).dict()

# ===============================================
# ENDPOINTS DE PRODUTOS
# ===============================================

@app.get("/produtos")
def listar_produtos(categoria: Optional[str] = None, 
                   preco_min: Optional[float] = None,
                   preco_max: Optional[float] = None,
                   busca: Optional[str] = None):
    """
    Listar produtos com filtros avançados
    
    - **categoria**: Filtrar por categoria
    - **preco_min**: Preço mínimo
    - **preco_max**: Preço máximo  
    - **busca**: Busca no nome ou descrição
    """
    produtos_filtrados = produtos_db.copy()
    
    # Aplicar filtros
    if categoria:
        produtos_filtrados = [p for p in produtos_filtrados 
                            if p['categoria'].lower() == categoria.lower()]
    
    if preco_min is not None:
        produtos_filtrados = [p for p in produtos_filtrados if p['preco'] >= preco_min]
    
    if preco_max is not None:
        produtos_filtrados = [p for p in produtos_filtrados if p['preco'] <= preco_max]
    
    if busca:
        busca_lower = busca.lower()
        produtos_filtrados = [p for p in produtos_filtrados 
                            if busca_lower in p['nome'].lower() or 
                               (p.get('descricao') and busca_lower in p['descricao'].lower())]
    
    return APIResponse(
        sucesso=True,
        mensagem="Produtos listados com sucesso",
        dados={
            "produtos": produtos_filtrados,
            "total": len(produtos_filtrados),
            "filtros_aplicados": {
                "categoria": categoria,
                "preco_min": preco_min,
                "preco_max": preco_max,
                "busca": busca
            }
        }
    ).dict()

@app.post("/produtos")
def criar_produto(produto_data: dict):
    """Criar novo produto"""
    global proximo_id_produto
    
    # Validações obrigatórias
    campos_obrigatorios = ['nome', 'preco', 'categoria']
    campos_faltando = [campo for campo in campos_obrigatorios if campo not in produto_data]
    
    if campos_faltando:
        return {
            "sucesso": False,
            "mensagem": f"Campos obrigatórios faltando: {', '.join(campos_faltando)}",
            "codigo_erro": "MISSING_REQUIRED_FIELDS"
        }
    
    # Validação de preço
    if produto_data['preco'] <= 0:
        return {
            "sucesso": False,
            "mensagem": "Preço deve ser maior que zero",
            "codigo_erro": "INVALID_PRICE"
        }
    
    # Criar produto
    novo_produto = {
        "id": proximo_id_produto,
        "nome": produto_data['nome'],
        "preco": float(produto_data['preco']),
        "categoria": produto_data['categoria'],
        "descricao": produto_data.get('descricao'),
        "data_criacao": datetime.now().isoformat(),
        "disponivel": produto_data.get('disponivel', True)
    }
    
    produtos_db.append(novo_produto)
    proximo_id_produto += 1
    
    return APIResponse(
        sucesso=True,
        mensagem="Produto criado com sucesso",
        dados={"produto": novo_produto}
    ).dict()

# ===============================================
# ENDPOINTS DE ANÁLISE
# ===============================================

@app.get("/analytics/dashboard")
def dashboard_analytics():
    """Endpoint com analytics avançadas"""
    # Estatísticas de usuários
    total_usuarios = len(usuarios_db)
    usuarios_ativos = len([u for u in usuarios_db if u.get('ativo', True)])
    
    # Estatísticas de produtos
    total_produtos = len(produtos_db)
    categorias = list(set(p['categoria'] for p in produtos_db)) if produtos_db else []
    
    # Cálculos de preços
    if produtos_db:
        precos = [p['preco'] for p in produtos_db]
        preco_medio = sum(precos) / len(precos)
        preco_min = min(precos)
        preco_max = max(precos)
    else:
        preco_medio = preco_min = preco_max = 0
    
    # Produtos por categoria
    produtos_por_categoria = {}
    for produto in produtos_db:
        categoria = produto['categoria']
        produtos_por_categoria[categoria] = produtos_por_categoria.get(categoria, 0) + 1
    
    return APIResponse(
        sucesso=True,
        mensagem="Dashboard analytics gerado",
        dados={
            "usuarios": {
                "total": total_usuarios,
                "ativos": usuarios_ativos,
                "inativos": total_usuarios - usuarios_ativos,
                "taxa_ativacao": (usuarios_ativos / total_usuarios * 100) if total_usuarios > 0 else 0
            },
            "produtos": {
                "total": total_produtos,
                "categorias_total": len(categorias),
                "categorias": categorias,
                "preco_estatisticas": {
                    "medio": round(preco_medio, 2),
                    "minimo": preco_min,
                    "maximo": preco_max
                },
                "distribuicao_categorias": produtos_por_categoria
            },
            "sistema": {
                "versao_api": "2.0.0",
                "uptime": "99.9%",
                "data_relatorio": datetime.now().isoformat()
            }
        }
    ).dict()

# ===============================================
# DEMONSTRAÇÃO DA API FASTAPI
# ===============================================

print("=== API MODERNA COM FASTAPI ===")
print()

# Adicionar dados de exemplo
usuarios_exemplo = [
    {"nome": "João Silva", "email": "joao@exemplo.com", "ativo": True},
    {"nome": "Maria Santos", "email": "maria@exemplo.com", "ativo": True},
    {"nome": "Carlos Lima", "email": "carlos@exemplo.com", "ativo": False},
]

produtos_exemplo = [
    {"nome": "Smartphone", "preco": 899.99, "categoria": "Eletrônicos", "descricao": "Smartphone moderno"},
    {"nome": "Notebook", "preco": 2499.99, "categoria": "Eletrônicos", "descricao": "Notebook para trabalho"},
    {"nome": "Mesa", "preco": 299.99, "categoria": "Móveis", "descricao": "Mesa de escritório"},
]

print("📊 Populando banco de dados...")
for usuario in usuarios_exemplo:
    resultado = criar_usuario(usuario)
    if resultado['sucesso']:
        print(f"  ✅ Usuário criado: {usuario['nome']}")

for produto in produtos_exemplo:
    resultado = criar_produto(produto)
    if resultado['sucesso']:
        print(f"  ✅ Produto criado: {produto['nome']}")

print()
print("🧪 TESTANDO ENDPOINTS:")

# Teste 1: Listar usuários
print("\\n📡 GET /usuarios")
resultado_usuarios = listar_usuarios()
if resultado_usuarios['sucesso']:
    total = resultado_usuarios['dados']['total']
    print(f"  ✅ {total} usuários encontrados")

# Teste 2: Filtrar produtos por categoria
print("\\n📡 GET /produtos?categoria=Eletrônicos")
resultado_produtos = listar_produtos(categoria="Eletrônicos")
if resultado_produtos['sucesso']:
    total = resultado_produtos['dados']['total']
    print(f"  ✅ {total} produtos na categoria Eletrônicos")

# Teste 3: Analytics dashboard
print("\\n📡 GET /analytics/dashboard")
resultado_analytics = dashboard_analytics()
if resultado_analytics['sucesso']:
    dados = resultado_analytics['dados']
    print(f"  ✅ Dashboard gerado:")
    print(f"    👥 Usuários: {dados['usuarios']['total']} (ativos: {dados['usuarios']['ativos']})")
    print(f"    📦 Produtos: {dados['produtos']['total']} em {dados['produtos']['categorias_total']} categorias")
    print(f"    💰 Preço médio: R$ {dados['produtos']['preco_estatisticas']['medio']}")

print()
print("✅ API FastAPI simulada com sucesso!")
print("🎯 Recursos demonstrados:")
print("  • Modelos Pydantic para validação")
print("  • Respostas padronizadas")
print("  • Filtros e paginação")
print("  • Validações de negócio")
print("  • Analytics e dashboard")
print("  • Documentação automática")'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n🔐 Autenticação e Segurança:")
        
        codigo3 = '''# Sistema de autenticação e segurança para APIs
import hashlib
import secrets
import jwt
import time
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

class PasswordManager:
    """Gerenciador de senhas com hash seguro"""
    
    @staticmethod
    def gerar_salt() -> str:
        """Gera salt aleatório para hash"""
        return secrets.token_hex(32)
    
    @staticmethod
    def hash_senha(senha: str, salt: str) -> str:
        """Cria hash seguro da senha com salt"""
        return hashlib.pbkdf2_hmac('sha256', 
                                 senha.encode('utf-8'), 
                                 salt.encode('utf-8'), 
                                 100000)  # 100k iterações
    
    @staticmethod
    def verificar_senha(senha: str, hash_armazenado: bytes, salt: str) -> bool:
        """Verifica se senha está correta"""
        hash_teste = PasswordManager.hash_senha(senha, salt)
        return hash_teste == hash_armazenado
    
    @staticmethod
    def criar_senha_segura(senha: str) -> Dict[str, Any]:
        """Cria hash completo para armazenamento"""
        salt = PasswordManager.gerar_salt()
        hash_senha = PasswordManager.hash_senha(senha, salt)
        
        return {
            "hash": hash_senha,
            "salt": salt,
            "criado_em": datetime.now().isoformat()
        }

class JWTManager:
    """Gerenciador de tokens JWT"""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.algoritmo = "HS256"
        self.tempo_expiracao = timedelta(hours=24)
    
    def gerar_token(self, user_id: int, dados_extras: Dict = None) -> str:
        """Gera token JWT para usuário"""
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + self.tempo_expiracao,
            "iat": datetime.utcnow(),
            "tipo": "access_token"
        }
        
        if dados_extras:
            payload.update(dados_extras)
        
        # Simulação do JWT (sem biblioteca real)
        token_simulado = f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.user_{user_id}_exp_{int(payload['exp'].timestamp())}.signature_hash"
        return token_simulado
    
    def validar_token(self, token: str) -> Optional[Dict]:
        """Valida e decodifica token JWT"""
        try:
            # Simulação de validação
            if not token.startswith("eyJ"):
                return None
            
            # Extrair user_id do token simulado
            parts = token.split('.')
            if len(parts) != 3:
                return None
            
            payload_part = parts[1]
            if "user_" in payload_part:
                user_id = int(payload_part.split("user_")[1].split("_")[0])
                exp_timestamp = int(payload_part.split("exp_")[1])
                
                # Verificar expiração
                if exp_timestamp < time.time():
                    return None
                
                return {
                    "user_id": user_id,
                    "exp": exp_timestamp,
                    "valido": True
                }
        except:
            return None
        
        return None
    
    def gerar_refresh_token(self, user_id: int) -> str:
        """Gera token de refresh (validade maior)"""
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(days=30),
            "tipo": "refresh_token"
        }
        
        token_simulado = f"refresh_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.user_{user_id}_refresh.signature"
        return token_simulado

class RateLimiter:
    """Limitador de taxa de requisições"""
    
    def __init__(self):
        self.requests = {}  # IP -> [timestamps]
        self.limite_por_minuto = 60
        self.limite_por_hora = 1000
    
    def verificar_limite(self, ip: str) -> Dict[str, Any]:
        """Verifica se IP está dentro dos limites"""
        agora = time.time()
        
        if ip not in self.requests:
            self.requests[ip] = []
        
        # Limpar requests antigos (mais de 1 hora)
        self.requests[ip] = [ts for ts in self.requests[ip] if agora - ts < 3600]
        
        # Contar requests no último minuto
        requests_ultimo_minuto = len([ts for ts in self.requests[ip] if agora - ts < 60])
        
        # Contar requests na última hora
        requests_ultima_hora = len(self.requests[ip])
        
        # Verificar limites
        limite_atingido = (
            requests_ultimo_minuto >= self.limite_por_minuto or
            requests_ultima_hora >= self.limite_por_hora
        )
        
        if not limite_atingido:
            # Registrar nova request
            self.requests[ip].append(agora)
        
        return {
            "permitido": not limite_atingido,
            "requests_minuto": requests_ultimo_minuto,
            "requests_hora": requests_ultima_hora,
            "limite_minuto": self.limite_por_minuto,
            "limite_hora": self.limite_por_hora,
            "reset_em": 60 - (agora % 60)  # segundos até reset
        }

class APIKeyManager:
    """Gerenciador de chaves de API"""
    
    def __init__(self):
        self.api_keys = {}  # key -> metadata
    
    def gerar_api_key(self, user_id: int, nome: str, permissoes: list = None) -> str:
        """Gera nova chave de API"""
        api_key = f"sk_{''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(32))}"
        
        self.api_keys[api_key] = {
            "user_id": user_id,
            "nome": nome,
            "permissoes": permissoes or ["read"],
            "criado_em": datetime.now().isoformat(),
            "ultimo_uso": None,
            "uso_total": 0,
            "ativo": True
        }
        
        return api_key
    
    def validar_api_key(self, api_key: str) -> Optional[Dict]:
        """Valida chave de API"""
        if api_key not in self.api_keys:
            return None
        
        key_data = self.api_keys[api_key]
        
        if not key_data["ativo"]:
            return None
        
        # Atualizar estatísticas de uso
        key_data["ultimo_uso"] = datetime.now().isoformat()
        key_data["uso_total"] += 1
        
        return key_data
    
    def revogar_api_key(self, api_key: str) -> bool:
        """Revoga chave de API"""
        if api_key in self.api_keys:
            self.api_keys[api_key]["ativo"] = False
            return True
        return False

class SecurityMiddleware:
    """Middleware de segurança completo"""
    
    def __init__(self):
        self.jwt_manager = JWTManager("secret_key_super_secreta_123")
        self.rate_limiter = RateLimiter()
        self.api_key_manager = APIKeyManager()
        self.blocked_ips = set()
    
    def verificar_requisicao(self, request_data: Dict) -> Dict[str, Any]:
        """Verifica segurança completa da requisição"""
        ip = request_data.get("ip", "127.0.0.1")
        headers = request_data.get("headers", {})
        
        resultado = {
            "autorizado": False,
            "usuario": None,
            "motivo_bloqueio": None,
            "rate_limit": None
        }
        
        # 1. Verificar IP bloqueado
        if ip in self.blocked_ips:
            resultado["motivo_bloqueio"] = "IP_BLOCKED"
            return resultado
        
        # 2. Verificar rate limiting
        rate_check = self.rate_limiter.verificar_limite(ip)
        resultado["rate_limit"] = rate_check
        
        if not rate_check["permitido"]:
            resultado["motivo_bloqueio"] = "RATE_LIMIT_EXCEEDED"
            return resultado
        
        # 3. Verificar autenticação
        auth_header = headers.get("Authorization", "")
        api_key_header = headers.get("X-API-Key", "")
        
        if auth_header.startswith("Bearer "):
            # Autenticação JWT
            token = auth_header[7:]  # Remove "Bearer "
            token_data = self.jwt_manager.validar_token(token)
            
            if token_data:
                resultado["autorizado"] = True
                resultado["usuario"] = {"id": token_data["user_id"], "tipo": "jwt"}
                return resultado
            else:
                resultado["motivo_bloqueio"] = "INVALID_JWT_TOKEN"
                return resultado
        
        elif api_key_header:
            # Autenticação por API Key
            key_data = self.api_key_manager.validar_api_key(api_key_header)
            
            if key_data:
                resultado["autorizado"] = True
                resultado["usuario"] = {
                    "id": key_data["user_id"], 
                    "tipo": "api_key",
                    "permissoes": key_data["permissoes"]
                }
                return resultado
            else:
                resultado["motivo_bloqueio"] = "INVALID_API_KEY"
                return resultado
        
        else:
            resultado["motivo_bloqueio"] = "NO_AUTHENTICATION"
            return resultado
    
    def bloquear_ip(self, ip: str):
        """Bloqueia IP específico"""
        self.blocked_ips.add(ip)
    
    def desbloquear_ip(self, ip: str):
        """Desbloqueia IP"""
        self.blocked_ips.discard(ip)

# ===============================================
# DEMONSTRAÇÃO DO SISTEMA DE SEGURANÇA
# ===============================================

print("=== SISTEMA DE SEGURANÇA PARA APIs ===")
print()

# 1. Demonstração de password hashing
print("🔐 GERENCIAMENTO DE SENHAS:")
password_mgr = PasswordManager()

senha_original = "minha_senha_super_secreta_123"
dados_senha = password_mgr.criar_senha_segura(senha_original)

print(f"  Senha original: {senha_original}")
print(f"  Salt gerado: {dados_senha['salt'][:16]}...")
print(f"  Hash seguro: {str(dados_senha['hash'])[:32]}...")

# Verificar senha
senha_correta = password_mgr.verificar_senha(senha_original, dados_senha['hash'], dados_senha['salt'])
senha_incorreta = password_mgr.verificar_senha("senha_errada", dados_senha['hash'], dados_senha['salt'])

print(f"  Verificação senha correta: {'✅' if senha_correta else '❌'}")
print(f"  Verificação senha incorreta: {'❌' if not senha_incorreta else '✅'}")

print()

# 2. Demonstração de JWT
print("🎫 GERENCIAMENTO DE TOKENS JWT:")
jwt_mgr = JWTManager("chave_secreta_jwt_123")

user_id = 123
token = jwt_mgr.gerar_token(user_id, {"role": "admin", "permissions": ["read", "write"]})
refresh_token = jwt_mgr.gerar_refresh_token(user_id)

print(f"  Token gerado: {token[:50]}...")
print(f"  Refresh token: {refresh_token[:40]}...")

# Validar token
token_data = jwt_mgr.validar_token(token)
print(f"  Token válido: {'✅' if token_data and token_data['valido'] else '❌'}")
if token_data:
    print(f"  User ID: {token_data['user_id']}")

print()

# 3. Demonstração de Rate Limiting
print("⏱️ LIMITADOR DE TAXA:")
rate_limiter = RateLimiter()

test_ip = "192.168.1.100"
print(f"  Testando IP: {test_ip}")

# Simular várias requisições
for i in range(5):
    resultado = rate_limiter.verificar_limite(test_ip)
    print(f"  Requisição {i+1}: {'✅ Permitida' if resultado['permitido'] else '❌ Bloqueada'}")
    print(f"    Requests no minuto: {resultado['requests_minuto']}/{resultado['limite_minuto']}")

print()

# 4. Demonstração de API Keys
print("🗝️ GERENCIAMENTO DE API KEYS:")
api_mgr = APIKeyManager()

# Gerar API keys
api_key_admin = api_mgr.gerar_api_key(user_id=1, nome="Admin Key", permissoes=["read", "write", "delete"])
api_key_readonly = api_mgr.gerar_api_key(user_id=2, nome="ReadOnly Key", permissoes=["read"])

print(f"  API Key Admin: {api_key_admin[:20]}...")
print(f"  API Key ReadOnly: {api_key_readonly[:20]}...")

# Validar API keys
key_data_admin = api_mgr.validar_api_key(api_key_admin)
key_data_readonly = api_mgr.validar_api_key(api_key_readonly)

print(f"  Validação Admin Key: {'✅' if key_data_admin else '❌'}")
if key_data_admin:
    print(f"    Permissões: {key_data_admin['permissoes']}")
    print(f"    Uso total: {key_data_admin['uso_total']}")

print()

# 5. Demonstração de Middleware Completo
print("🛡️ MIDDLEWARE DE SEGURANÇA:")
security = SecurityMiddleware()

# Testar diferentes cenários
cenarios_teste = [
    {
        "nome": "Request com JWT válido",
        "request": {
            "ip": "10.0.0.1",
            "headers": {"Authorization": f"Bearer {token}"}
        }
    },
    {
        "nome": "Request com API Key válida",
        "request": {
            "ip": "10.0.0.2", 
            "headers": {"X-API-Key": api_key_readonly}
        }
    },
    {
        "nome": "Request sem autenticação",
        "request": {
            "ip": "10.0.0.3",
            "headers": {}
        }
    },
    {
        "nome": "Request com token inválido",
        "request": {
            "ip": "10.0.0.4",
            "headers": {"Authorization": "Bearer token_invalido_123"}
        }
    }
]

for cenario in cenarios_teste:
    print(f"\\n  📋 {cenario['nome']}:")
    resultado = security.verificar_requisicao(cenario['request'])
    
    if resultado['autorizado']:
        print(f"    ✅ Autorizado")
        print(f"    👤 Usuário: ID {resultado['usuario']['id']} ({resultado['usuario']['tipo']})")
    else:
        print(f"    ❌ Bloqueado: {resultado['motivo_bloqueio']}")
    
    if resultado['rate_limit']:
        rl = resultado['rate_limit']
        print(f"    ⏱️ Rate Limit: {rl['requests_minuto']}/{rl['limite_minuto']} por minuto")

print()
print("✅ Sistema de segurança implementado com sucesso!")
print("🎯 Recursos de segurança:")
print("  • Hash seguro de senhas (PBKDF2)")
print("  • Tokens JWT com expiração")
print("  • Rate limiting por IP")
print("  • API Keys com permissões")
print("  • Middleware de segurança integrado")
print("  • Bloqueio de IPs maliciosos")
print("  • Refresh tokens para sessões longas")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        # Exercícios
        self.exercicio(
            "Qual é o método HTTP usado para criar um novo recurso?",
            ["POST", "post"],
            "POST é usado para criar novos recursos em APIs REST"
        )
        
        # Mini Projeto do Módulo 29
        self._mini_projeto_sistema_api_completo()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_api_completo(self) -> None:
        """Mini Projeto - Módulo 29: Sistema de API Completo"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE API COMPLETO")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE API COMPLETO")
            print("="*50)
        
        print("🌐 API REST completa com autenticação, documentação e monitoramento!")
        print("🛠️ Usando: FastAPI, JWT, Rate Limiting, OpenAPI, WebSockets")
        
        self.pausar()
        
        codigo_projeto = '''# 🌐 SISTEMA DE API COMPLETO
# API REST profissional com todos os recursos modernos

import json
import time
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from enum import Enum
import asyncio
import websockets

# ===============================================
# MODELOS DE DADOS E ENUMS
# ===============================================

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

class StatusEnum(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    SUSPENDED = "suspended"

@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str
    salt: str
    role: UserRole
    status: StatusEnum
    created_at: datetime
    last_login: Optional[datetime] = None
    api_key: Optional[str] = None
    
    def to_dict(self, include_sensitive=False):
        data = asdict(self)
        data['role'] = self.role.value
        data['status'] = self.status.value
        data['created_at'] = self.created_at.isoformat()
        data['last_login'] = self.last_login.isoformat() if self.last_login else None
        
        if not include_sensitive:
            del data['password_hash']
            del data['salt']
        
        return data

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    category_id: int
    stock: int
    created_at: datetime
    updated_at: datetime
    active: bool = True
    
    def to_dict(self):
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

@dataclass
class Category:
    id: int
    name: str
    description: str
    parent_id: Optional[int] = None
    
    def to_dict(self):
        return asdict(self)

@dataclass
class Order:
    id: int
    user_id: int
    products: List[Dict]  # [{"product_id": int, "quantity": int, "price": float}]
    total_amount: float
    status: str
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self):
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

# ===============================================
# SISTEMA DE AUTENTICAÇÃO AVANÇADO
# ===============================================

class AuthenticationSystem:
    """Sistema completo de autenticação"""
    
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.sessions: Dict[str, Dict] = {}  # token -> session_data
        self.api_keys: Dict[str, int] = {}  # api_key -> user_id
        self.login_attempts: Dict[str, List[datetime]] = {}  # IP -> attempts
        self.secret_key = "super_secret_key_for_jwt_2024"
        self.next_user_id = 1
    
    def hash_password(self, password: str, salt: str = None) -> tuple:
        """Cria hash seguro da senha"""
        if salt is None:
            salt = secrets.token_hex(32)
        
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 100k iterations
        )
        
        return password_hash.hex(), salt
    
    def verify_password(self, password: str, stored_hash: str, salt: str) -> bool:
        """Verifica senha"""
        hash_to_check, _ = self.hash_password(password, salt)
        return hash_to_check == stored_hash
    
    def generate_api_key(self) -> str:
        """Gera chave de API única"""
        return f"sk_{''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(48))}"
    
    def register_user(self, username: str, email: str, password: str, role: UserRole = UserRole.USER) -> Dict:
        """Registra novo usuário"""
        # Verificar se username ou email já existem
        for user in self.users.values():
            if user.username == username:
                return {"success": False, "error": "USERNAME_EXISTS"}
            if user.email == email:
                return {"success": False, "error": "EMAIL_EXISTS"}
        
        # Criar hash da senha
        password_hash, salt = self.hash_password(password)
        
        # Criar usuário
        user = User(
            id=self.next_user_id,
            username=username,
            email=email,
            password_hash=password_hash,
            salt=salt,
            role=role,
            status=StatusEnum.ACTIVE,
            created_at=datetime.now(),
            api_key=self.generate_api_key()
        )
        
        self.users[self.next_user_id] = user
        self.api_keys[user.api_key] = self.next_user_id
        self.next_user_id += 1
        
        return {
            "success": True,
            "user": user.to_dict(),
            "api_key": user.api_key
        }
    
    def authenticate_user(self, username: str, password: str, ip: str) -> Dict:
        """Autentica usuário"""
        # Verificar tentativas de login
        if not self.check_login_attempts(ip):
            return {"success": False, "error": "TOO_MANY_ATTEMPTS"}
        
        # Encontrar usuário
        user = None
        for u in self.users.values():
            if u.username == username or u.email == username:
                user = u
                break
        
        if not user:
            self.record_failed_login(ip)
            return {"success": False, "error": "INVALID_CREDENTIALS"}
        
        # Verificar senha
        if not self.verify_password(password, user.password_hash, user.salt):
            self.record_failed_login(ip)
            return {"success": False, "error": "INVALID_CREDENTIALS"}
        
        # Verificar status do usuário
        if user.status != StatusEnum.ACTIVE:
            return {"success": False, "error": f"USER_{user.status.value.upper()}"}
        
        # Gerar token de sessão
        session_token = self.generate_session_token(user.id)
        
        # Atualizar último login
        user.last_login = datetime.now()
        
        return {
            "success": True,
            "user": user.to_dict(),
            "token": session_token,
            "expires_in": 86400  # 24 horas
        }
    
    def generate_session_token(self, user_id: int) -> str:
        """Gera token de sessão"""
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {
            "user_id": user_id,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(hours=24),
            "last_used": datetime.now()
        }
        return token
    
    def validate_token(self, token: str) -> Optional[User]:
        """Valida token de sessão"""
        if token not in self.sessions:
            return None
        
        session = self.sessions[token]
        
        # Verificar expiração
        if datetime.now() > session["expires_at"]:
            del self.sessions[token]
            return None
        
        # Atualizar último uso
        session["last_used"] = datetime.now()
        
        return self.users.get(session["user_id"])
    
    def validate_api_key(self, api_key: str) -> Optional[User]:
        """Valida chave de API"""
        user_id = self.api_keys.get(api_key)
        if user_id:
            return self.users.get(user_id)
        return None
    
    def check_login_attempts(self, ip: str) -> bool:
        """Verifica se IP não excedeu tentativas de login"""
        now = datetime.now()
        if ip not in self.login_attempts:
            return True
        
        # Remover tentativas antigas (últimas 15 minutos)
        self.login_attempts[ip] = [
            attempt for attempt in self.login_attempts[ip]
            if now - attempt < timedelta(minutes=15)
        ]
        
        # Verificar se excedeu 5 tentativas
        return len(self.login_attempts[ip]) < 5
    
    def record_failed_login(self, ip: str):
        """Registra tentativa de login falhada"""
        if ip not in self.login_attempts:
            self.login_attempts[ip] = []
        self.login_attempts[ip].append(datetime.now())

# ===============================================
# SISTEMA DE RATE LIMITING AVANÇADO
# ===============================================

class AdvancedRateLimiter:
    """Rate limiter com diferentes tipos de limite"""
    
    def __init__(self):
        self.requests = {}  # endpoint -> ip -> timestamps
        self.global_requests = {}  # ip -> timestamps
        
        # Configurações de limite por endpoint
        self.endpoint_limits = {
            "/auth/login": {"per_minute": 5, "per_hour": 20},
            "/auth/register": {"per_minute": 2, "per_hour": 10},
            "/api/users": {"per_minute": 30, "per_hour": 1000},
            "/api/products": {"per_minute": 60, "per_hour": 5000},
            "default": {"per_minute": 100, "per_hour": 10000}
        }
    
    def check_rate_limit(self, endpoint: str, ip: str, user_role: str = "user") -> Dict:
        """Verifica limite de taxa para endpoint específico"""
        now = time.time()
        
        # Obter configuração de limite
        limits = self.endpoint_limits.get(endpoint, self.endpoint_limits["default"])
        
        # Ajustar limites baseado no role do usuário
        if user_role == "admin":
            limits = {k: v * 5 for k, v in limits.items()}  # Admins têm 5x mais limite
        elif user_role == "moderator":
            limits = {k: v * 2 for k, v in limits.items()}  # Moderadores têm 2x mais
        
        # Inicializar estruturas se necessário
        if endpoint not in self.requests:
            self.requests[endpoint] = {}
        if ip not in self.requests[endpoint]:
            self.requests[endpoint][ip] = []
        
        # Limpar requests antigos
        self.requests[endpoint][ip] = [
            ts for ts in self.requests[endpoint][ip] if now - ts < 3600
        ]
        
        # Contar requests
        requests_last_minute = len([
            ts for ts in self.requests[endpoint][ip] if now - ts < 60
        ])
        requests_last_hour = len(self.requests[endpoint][ip])
        
        # Verificar limites
        minute_exceeded = requests_last_minute >= limits["per_minute"]
        hour_exceeded = requests_last_hour >= limits["per_hour"]
        
        if minute_exceeded or hour_exceeded:
            return {
                "allowed": False,
                "reason": "minute_limit" if minute_exceeded else "hour_limit",
                "requests_minute": requests_last_minute,
                "requests_hour": requests_last_hour,
                "limits": limits,
                "reset_in": 60 - (now % 60) if minute_exceeded else 3600 - (now % 3600)
            }
        
        # Registrar nova request
        self.requests[endpoint][ip].append(now)
        
        return {
            "allowed": True,
            "requests_minute": requests_last_minute + 1,
            "requests_hour": requests_last_hour + 1,
            "limits": limits
        }

# ===============================================
# SISTEMA DE DADOS E CRUD
# ===============================================

class DatabaseManager:
    """Gerenciador de dados em memória"""
    
    def __init__(self):
        self.categories: Dict[int, Category] = {}
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}
        
        self.next_category_id = 1
        self.next_product_id = 1
        self.next_order_id = 1
        
        # Dados iniciais
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Inicializa dados de exemplo"""
        # Categorias
        categories_data = [
            {"name": "Eletrônicos", "description": "Produtos eletrônicos"},
            {"name": "Roupas", "description": "Vestuário em geral"},
            {"name": "Livros", "description": "Livros e publicações"},
            {"name": "Casa", "description": "Produtos para casa"},
        ]
        
        for cat_data in categories_data:
            category = Category(
                id=self.next_category_id,
                name=cat_data["name"],
                description=cat_data["description"]
            )
            self.categories[self.next_category_id] = category
            self.next_category_id += 1
        
        # Produtos
        products_data = [
            {"name": "Smartphone", "description": "Smartphone moderno", "price": 899.99, "category_id": 1, "stock": 50},
            {"name": "Notebook", "description": "Notebook para trabalho", "price": 2499.99, "category_id": 1, "stock": 20},
            {"name": "Camiseta", "description": "Camiseta de algodão", "price": 29.99, "category_id": 2, "stock": 100},
            {"name": "Calça Jeans", "description": "Calça jeans masculina", "price": 79.99, "category_id": 2, "stock": 75},
            {"name": "Python Cookbook", "description": "Livro sobre Python", "price": 49.99, "category_id": 3, "stock": 30},
        ]
        
        for prod_data in products_data:
            product = Product(
                id=self.next_product_id,
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                category_id=prod_data["category_id"],
                stock=prod_data["stock"],
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            self.products[self.next_product_id] = product
            self.next_product_id += 1
    
    def get_products(self, category_id: int = None, search: str = None, 
                    min_price: float = None, max_price: float = None) -> List[Product]:
        """Busca produtos com filtros"""
        products = list(self.products.values())
        
        if category_id:
            products = [p for p in products if p.category_id == category_id]
        
        if search:
            search_lower = search.lower()
            products = [p for p in products if 
                       search_lower in p.name.lower() or 
                       search_lower in p.description.lower()]
        
        if min_price is not None:
            products = [p for p in products if p.price >= min_price]
        
        if max_price is not None:
            products = [p for p in products if p.price <= max_price]
        
        return [p for p in products if p.active]
    
    def create_product(self, product_data: Dict) -> Product:
        """Cria novo produto"""
        product = Product(
            id=self.next_product_id,
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            category_id=product_data["category_id"],
            stock=product_data["stock"],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        self.products[self.next_product_id] = product
        self.next_product_id += 1
        
        return product
    
    def create_order(self, user_id: int, order_items: List[Dict]) -> Dict:
        """Cria novo pedido"""
        total_amount = 0
        processed_items = []
        
        # Validar e processar itens
        for item in order_items:
            product_id = item["product_id"]
            quantity = item["quantity"]
            
            if product_id not in self.products:
                return {"success": False, "error": f"Product {product_id} not found"}
            
            product = self.products[product_id]
            
            if product.stock < quantity:
                return {"success": False, "error": f"Insufficient stock for {product.name}"}
            
            item_total = product.price * quantity
            total_amount += item_total
            
            processed_items.append({
                "product_id": product_id,
                "quantity": quantity,
                "price": product.price,
                "total": item_total
            })
            
            # Atualizar estoque
            product.stock -= quantity
        
        # Criar pedido
        order = Order(
            id=self.next_order_id,
            user_id=user_id,
            products=processed_items,
            total_amount=total_amount,
            status="pending",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        
        return {"success": True, "order": order}

# ===============================================
# API REST COMPLETA
# ===============================================

class ECommerceAPI:
    """API completa de e-commerce"""
    
    def __init__(self):
        self.auth = AuthenticationSystem()
        self.rate_limiter = AdvancedRateLimiter()
        self.db = DatabaseManager()
        self.websocket_clients = set()
        
        # Criar usuário admin padrão
        self.auth.register_user("admin", "admin@sistema.com", "admin123", UserRole.ADMIN)
        
        # Rotas e handlers
        self.routes = {
            "GET /api/health": self.health_check,
            "POST /auth/register": self.register,
            "POST /auth/login": self.login,
            "GET /api/profile": self.get_profile,
            "GET /api/categories": self.get_categories,
            "GET /api/products": self.get_products,
            "POST /api/products": self.create_product,
            "GET /api/products/{id}": self.get_product,
            "POST /api/orders": self.create_order,
            "GET /api/orders": self.get_orders,
            "GET /api/analytics": self.get_analytics,
            "GET /api/docs": self.get_api_docs,
        }
    
    def process_request(self, method: str, path: str, headers: Dict, 
                       body: Dict = None, query_params: Dict = None, ip: str = "127.0.0.1") -> Dict:
        """Processa requisição HTTP"""
        route_key = f"{method} {path}"
        
        # Verificar se rota existe
        if route_key not in self.routes:
            return {"status": 404, "body": {"error": "Route not found"}}
        
        # Rate limiting
        user_role = "user"
        if "Authorization" in headers or "X-API-Key" in headers:
            user = self.authenticate_request(headers)
            if user:
                user_role = user.role.value
        
        rate_check = self.rate_limiter.check_rate_limit(path, ip, user_role)
        if not rate_check["allowed"]:
            return {
                "status": 429,
                "body": {
                    "error": "Rate limit exceeded",
                    "reason": rate_check["reason"],
                    "reset_in": rate_check["reset_in"]
                },
                "headers": {
                    "X-RateLimit-Limit": str(rate_check["limits"]["per_minute"]),
                    "X-RateLimit-Remaining": str(max(0, rate_check["limits"]["per_minute"] - rate_check["requests_minute"])),
                    "X-RateLimit-Reset": str(int(time.time() + rate_check.get("reset_in", 60)))
                }
            }
        
        # Executar handler
        try:
            handler = self.routes[route_key]
            result = handler(headers, body, query_params)
            
            # Adicionar headers de rate limit
            if "headers" not in result:
                result["headers"] = {}
            result["headers"].update({
                "X-RateLimit-Limit": str(rate_check["limits"]["per_minute"]),
                "X-RateLimit-Remaining": str(rate_check["limits"]["per_minute"] - rate_check["requests_minute"]),
            })
            
            return result
            
        except Exception as e:
            return {"status": 500, "body": {"error": f"Internal server error: {str(e)}"}}
    
    def authenticate_request(self, headers: Dict) -> Optional[User]:
        """Autentica requisição"""
        # JWT Token
        auth_header = headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
            return self.auth.validate_token(token)
        
        # API Key
        api_key = headers.get("X-API-Key", "")
        if api_key:
            return self.auth.validate_api_key(api_key)
        
        return None
    
    def require_auth(self, headers: Dict, required_role: UserRole = None) -> tuple:
        """Verifica autenticação obrigatória"""
        user = self.authenticate_request(headers)
        if not user:
            return None, {"status": 401, "body": {"error": "Authentication required"}}
        
        if required_role and user.role.value != required_role.value and user.role != UserRole.ADMIN:
            return None, {"status": 403, "body": {"error": "Insufficient permissions"}}
        
        return user, None
    
    # ===============================================
    # HANDLERS DE ENDPOINTS
    # ===============================================
    
    def health_check(self, headers, body, query_params):
        """Endpoint de saúde"""
        return {
            "status": 200,
            "body": {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0",
                "services": {
                    "auth": "operational",
                    "database": "operational",
                    "rate_limiter": "operational"
                }
            }
        }
    
    def register(self, headers, body, query_params):
        """Registro de usuário"""
        if not body or not all(k in body for k in ["username", "email", "password"]):
            return {"status": 400, "body": {"error": "Missing required fields"}}
        
        result = self.auth.register_user(
            body["username"], 
            body["email"], 
            body["password"]
        )
        
        if result["success"]:
            return {"status": 201, "body": result}
        else:
            return {"status": 409, "body": {"error": result["error"]}}
    
    def login(self, headers, body, query_params):
        """Login de usuário"""
        if not body or not all(k in body for k in ["username", "password"]):
            return {"status": 400, "body": {"error": "Missing username or password"}}
        
        ip = "127.0.0.1"  # Simulado
        result = self.auth.authenticate_user(body["username"], body["password"], ip)
        
        if result["success"]:
            return {"status": 200, "body": result}
        else:
            status_code = 429 if result["error"] == "TOO_MANY_ATTEMPTS" else 401
            return {"status": status_code, "body": {"error": result["error"]}}
    
    def get_profile(self, headers, body, query_params):
        """Perfil do usuário"""
        user, error = self.require_auth(headers)
        if error:
            return error
        
        return {"status": 200, "body": {"user": user.to_dict()}}
    
    def get_categories(self, headers, body, query_params):
        """Listar categorias"""
        categories = [cat.to_dict() for cat in self.db.categories.values()]
        return {"status": 200, "body": {"categories": categories}}
    
    def get_products(self, headers, body, query_params):
        """Listar produtos com filtros"""
        filters = query_params or {}
        
        products = self.db.get_products(
            category_id=filters.get("category_id", type=int),
            search=filters.get("search"),
            min_price=filters.get("min_price", type=float),
            max_price=filters.get("max_price", type=float)
        )
        
        return {
            "status": 200,
            "body": {
                "products": [p.to_dict() for p in products],
                "total": len(products),
                "filters": filters
            }
        }
    
    def create_product(self, headers, body, query_params):
        """Criar produto (admin only)"""
        user, error = self.require_auth(headers, UserRole.ADMIN)
        if error:
            return error
        
        if not body or not all(k in body for k in ["name", "price", "category_id"]):
            return {"status": 400, "body": {"error": "Missing required fields"}}
        
        try:
            product = self.db.create_product(body)
            
            # Notificar via WebSocket
            self.notify_websocket_clients({
                "type": "product_created",
                "product": product.to_dict()
            })
            
            return {"status": 201, "body": {"product": product.to_dict()}}
        except Exception as e:
            return {"status": 400, "body": {"error": str(e)}}
    
    def get_product(self, headers, body, query_params):
        """Obter produto específico"""
        # Extrair ID do path (simulado)
        product_id = 1  # Seria extraído da URL real
        
        if product_id not in self.db.products:
            return {"status": 404, "body": {"error": "Product not found"}}
        
        product = self.db.products[product_id]
        return {"status": 200, "body": {"product": product.to_dict()}}
    
    def create_order(self, headers, body, query_params):
        """Criar pedido"""
        user, error = self.require_auth(headers)
        if error:
            return error
        
        if not body or "items" not in body:
            return {"status": 400, "body": {"error": "Missing order items"}}
        
        result = self.db.create_order(user.id, body["items"])
        
        if result["success"]:
            # Notificar via WebSocket
            self.notify_websocket_clients({
                "type": "order_created",
                "order": result["order"].to_dict()
            })
            
            return {"status": 201, "body": result}
        else:
            return {"status": 400, "body": {"error": result["error"]}}
    
    def get_orders(self, headers, body, query_params):
        """Listar pedidos do usuário"""
        user, error = self.require_auth(headers)
        if error:
            return error
        
        user_orders = [
            order.to_dict() for order in self.db.orders.values()
            if order.user_id == user.id
        ]
        
        return {"status": 200, "body": {"orders": user_orders}}
    
    def get_analytics(self, headers, body, query_params):
        """Analytics (admin only)"""
        user, error = self.require_auth(headers, UserRole.ADMIN)
        if error:
            return error
        
        # Calcular estatísticas
        total_users = len(self.auth.users)
        total_products = len(self.db.products)
        total_orders = len(self.db.orders)
        
        revenue = sum(order.total_amount for order in self.db.orders.values())
        
        # Top produtos
        product_sales = {}
        for order in self.db.orders.values():
            for item in order.products:
                pid = item["product_id"]
                product_sales[pid] = product_sales.get(pid, 0) + item["quantity"]
        
        top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "status": 200,
            "body": {
                "analytics": {
                    "users": {
                        "total": total_users,
                        "active": len([u for u in self.auth.users.values() if u.status == StatusEnum.ACTIVE])
                    },
                    "products": {
                        "total": total_products,
                        "active": len([p for p in self.db.products.values() if p.active])
                    },
                    "orders": {
                        "total": total_orders,
                        "revenue": revenue
                    },
                    "top_products": [
                        {
                            "product_id": pid,
                            "product_name": self.db.products[pid].name if pid in self.db.products else "Unknown",
                            "sales": sales
                        }
                        for pid, sales in top_products
                    ]
                }
            }
        }
    
    def get_api_docs(self, headers, body, query_params):
        """Documentação da API"""
        docs = {
            "openapi": "3.0.0",
            "info": {
                "title": "E-Commerce API",
                "version": "1.0.0",
                "description": "API completa para sistema de e-commerce"
            },
            "servers": [
                {"url": "https://api.exemplo.com", "description": "Produção"},
                {"url": "http://localhost:8000", "description": "Desenvolvimento"}
            ],
            "paths": {
                "/auth/register": {
                    "post": {
                        "summary": "Registrar usuário",
                        "requestBody": {
                            "required": True,
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "username": {"type": "string"},
                                            "email": {"type": "string"},
                                            "password": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "/api/products": {
                    "get": {
                        "summary": "Listar produtos",
                        "parameters": [
                            {"name": "category_id", "in": "query", "schema": {"type": "integer"}},
                            {"name": "search", "in": "query", "schema": {"type": "string"}},
                            {"name": "min_price", "in": "query", "schema": {"type": "number"}},
                            {"name": "max_price", "in": "query", "schema": {"type": "number"}}
                        ]
                    },
                    "post": {
                        "summary": "Criar produto (admin)",
                        "security": [{"Bearer": []}],
                        "requestBody": {
                            "required": True,
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "name": {"type": "string"},
                                            "description": {"type": "string"},
                                            "price": {"type": "number"},
                                            "category_id": {"type": "integer"},
                                            "stock": {"type": "integer"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "components": {
                "securitySchemes": {
                    "Bearer": {
                        "type": "http",
                        "scheme": "bearer"
                    },
                    "ApiKey": {
                        "type": "apiKey",
                        "in": "header",
                        "name": "X-API-Key"
                    }
                }
            }
        }
        
        return {"status": 200, "body": docs}
    
    def notify_websocket_clients(self, message: Dict):
        """Notifica clientes WebSocket"""
        if self.websocket_clients:
            print(f"📡 WebSocket broadcast: {message['type']}")
            # Em implementação real, enviaria para todos os clientes conectados

# ===============================================
# DEMONSTRAÇÃO COMPLETA
# ===============================================

def demonstrar_api_completa():
    """Demonstração da API completa"""
    print("=== SISTEMA DE API COMPLETO ===")
    print()
    
    # Inicializar API
    api = ECommerceAPI()
    
    print("🏗️ API inicializada com:")
    print(f"  👥 {len(api.auth.users)} usuários")
    print(f"  📂 {len(api.db.categories)} categorias")
    print(f"  📦 {len(api.db.products)} produtos")
    print()
    
    # Teste 1: Health Check
    print("🧪 TESTE 1: Health Check")
    response = api.process_request("GET", "/api/health", {})
    print(f"  Status: {response['status']}")
    print(f"  Health: {response['body']['status']}")
    
    # Teste 2: Registro de usuário
    print("\\n🧪 TESTE 2: Registro de usuário")
    register_data = {
        "username": "joao_cliente",
        "email": "joao@cliente.com",
        "password": "senha123"
    }
    response = api.process_request("POST", "/auth/register", {}, register_data)
    print(f"  Status: {response['status']}")
    if response['status'] == 201:
        print(f"  Usuário criado: {response['body']['user']['username']}")
        api_key = response['body']['api_key']
        print(f"  API Key: {api_key[:20]}...")
    
    # Teste 3: Login
    print("\\n🧪 TESTE 3: Login de usuário")
    login_data = {"username": "joao_cliente", "password": "senha123"}
    response = api.process_request("POST", "/auth/login", {}, login_data)
    print(f"  Status: {response['status']}")
    if response['status'] == 200:
        token = response['body']['token']
        print(f"  Token: {token[:20]}...")
        
        # Teste 4: Perfil autenticado
        print("\\n🧪 TESTE 4: Obter perfil")
        headers = {"Authorization": f"Bearer {token}"}
        response = api.process_request("GET", "/api/profile", headers)
        print(f"  Status: {response['status']}")
        if response['status'] == 200:
            user = response['body']['user']
            print(f"  Usuário: {user['username']} ({user['email']})")
    
    # Teste 5: Listar produtos
    print("\\n🧪 TESTE 5: Listar produtos")
    response = api.process_request("GET", "/api/products", {})
    print(f"  Status: {response['status']}")
    if response['status'] == 200:
        products = response['body']['products']
        print(f"  Total de produtos: {len(products)}")
        if products:
            print(f"  Primeiro produto: {products[0]['name']} - R$ {products[0]['price']}")
    
    # Teste 6: Criar produto (como admin)
    print("\\n🧪 TESTE 6: Criar produto (admin)")
    admin_headers = {"Authorization": f"Bearer {api.auth.generate_session_token(1)}"}  # Admin é ID 1
    product_data = {
        "name": "Produto Teste",
        "description": "Produto criado via API",
        "price": 99.99,
        "category_id": 1,
        "stock": 10
    }
    response = api.process_request("POST", "/api/products", admin_headers, product_data)
    print(f"  Status: {response['status']}")
    if response['status'] == 201:
        product = response['body']['product']
        print(f"  Produto criado: {product['name']}")
    
    # Teste 7: Analytics (admin)
    print("\\n🧪 TESTE 7: Analytics")
    response = api.process_request("GET", "/api/analytics", admin_headers)
    print(f"  Status: {response['status']}")
    if response['status'] == 200:
        analytics = response['body']['analytics']
        print(f"  Total usuários: {analytics['users']['total']}")
        print(f"  Total produtos: {analytics['products']['total']}")
        print(f"  Total pedidos: {analytics['orders']['total']}")
    
    # Teste 8: Rate limiting
    print("\\n🧪 TESTE 8: Rate limiting")
    test_ip = "192.168.1.100"
    
    for i in range(3):
        response = api.process_request("GET", "/api/products", {}, ip=test_ip)
        rate_headers = response.get('headers', {})
        print(f"  Request {i+1}: Status {response['status']}")
        if 'X-RateLimit-Remaining' in rate_headers:
            print(f"    Rate limit remaining: {rate_headers['X-RateLimit-Remaining']}")
    
    # Teste 9: Documentação OpenAPI
    print("\\n🧪 TESTE 9: Documentação da API")
    response = api.process_request("GET", "/api/docs", {})
    print(f"  Status: {response['status']}")
    if response['status'] == 200:
        docs = response['body']
        print(f"  API: {docs['info']['title']} v{docs['info']['version']}")
        print(f"  Endpoints documentados: {len(docs['paths'])}")
    
    print("\\n✅ Demonstração completa da API!")
    print("🎯 Recursos implementados:")
    print("  • Autenticação JWT e API Keys")
    print("  • Rate limiting avançado")
    print("  • CRUD completo de produtos")
    print("  • Sistema de pedidos")
    print("  • Analytics e relatórios")
    print("  • Documentação OpenAPI")
    print("  • Middleware de segurança")
    print("  • WebSocket notifications")
    print("  • Health checks")
    print("  • Controle de acesso por roles")

# Executar demonstração
demonstrar_api_completa()'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de API completo criado!")
        print("🎯 Aplicação real: e-commerce, SaaS, sistemas empresariais")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de API Completo")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo29ApisWeb()
    print("Teste do módulo 29 - versão standalone")
    module._apis_web()