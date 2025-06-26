#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 12: Dicionários e Sets
Aprenda sobre estruturas de dados avançadas: dicionários e conjuntos
"""

from ..shared.base_module import BaseModule


class Modulo12Dicionarios(BaseModule):
    """Módulo 12: Dicionários e Sets - Estruturas Avançadas"""
    
    def __init__(self):
        super().__init__("modulo_12", "Dicionários e Sets")
        self.has_mini_project = True
        self.mini_project_points = 70
    
    def execute(self) -> None:
        """Executa o módulo sobre dicionários e sets"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._dicionarios_sets()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _dicionarios_sets(self) -> None:
        """Conteúdo principal sobre dicionários e sets"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔑 MÓDULO 12: DICIONÁRIOS E SETS - ESTRUTURAS AVANÇADAS")
        else:
            print("\n" + "="*50)
            print("🔑 MÓDULO 12: DICIONÁRIOS E SETS - ESTRUTURAS AVANÇADAS")
            print("="*50)
        
        print("📚 Vamos aprender sobre Dicionários e Sets!")
        print("🔑 Estruturas de dados fundamentais para programação avançada!")
        
        print("\n═══════════════════════════════════════════════")
        print("        DICIONÁRIOS - CHAVE:VALOR")
        print("═══════════════════════════════════════════════")
        
        print("\n🎯 Dicionário = coleção de pares chave:valor")
        print("📋 Características:")
        print("• 🔑 Chaves únicas")
        print("• 📦 Valores podem ser qualquer tipo")
        print("• 🚀 Busca muito rápida")
        print("• 🔄 Mutável (pode ser modificado)")
        
        self.pausar()
        
        codigo1 = '''# Criando e usando dicionários
# Diferentes formas de criar
dicionario1 = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
dicionario2 = dict(nome="Maria", idade=30, cidade="Rio de Janeiro")
dicionario3 = {}  # Dicionário vazio

print("Dicionário 1:", dicionario1)
print("Dicionário 2:", dicionario2)

# Acessando valores
print("\\nNome:", dicionario1["nome"])
print("Idade:", dicionario1["idade"])

# Método get() - mais seguro
print("Cidade:", dicionario1.get("cidade"))
print("País:", dicionario1.get("pais", "Brasil"))  # Valor padrão

# Adicionando/modificando
dicionario1["profissao"] = "Programador"
dicionario1["idade"] = 26  # Modifica valor existente

print("\\nDicionário atualizado:", dicionario1)'''
        
        self.exemplo(codigo1)
        self.executar_codigo(codigo1)
        
        self.pausar()
        
        print("\n🛠️ Métodos de Dicionários:")
        
        codigo2 = '''# Métodos importantes de dicionários
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Engenheira",
    "salario": 8000,
    "hobbies": ["leitura", "natação", "culinária"]
}

print("=== MÉTODOS DE DICIONÁRIOS ===")

# keys(), values(), items()
print("Chaves:", list(pessoa.keys()))
print("Valores:", list(pessoa.values()))
print("Itens:", list(pessoa.items()))

# Iterando sobre dicionário
print("\\n=== ITERAÇÃO ===")
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")

print("\\n=== ITERAÇÃO COM ITEMS ===")
for chave, valor in pessoa.items():
    print(f"{chave} -> {valor}")

# Removendo elementos
print("\\n=== REMOÇÃO ===")
# pop() - remove e retorna valor
salario = pessoa.pop("salario")
print(f"Salário removido: {salario}")

# del - remove chave
del pessoa["hobbies"]
print("Após remoções:", pessoa)

# clear() - remove tudo
copia = pessoa.copy()
copia.clear()
print("Dicionário limpo:", copia)'''
        
        self.exemplo(codigo2)
        self.executar_codigo(codigo2)
        
        self.pausar()
        
        print("\n📦 SETS - Conjuntos:")
        
        codigo3 = '''# Sets - conjuntos únicos
# Criando sets
set1 = {1, 2, 3, 4, 5}
set2 = set([2, 3, 4, 5, 6])
set3 = set("python")  # Set de caracteres

print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)

# Sets removem duplicatas automaticamente
numeros_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set_unicos = set(numeros_duplicados)
print("\\nNúmeros únicos:", set_unicos)

# Operações de conjuntos
print("\\n=== OPERAÇÕES DE CONJUNTOS ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A: {A}")
print(f"B: {B}")

# União
print(f"A ∪ B (união): {A | B}")
print(f"A ∪ B (union): {A.union(B)}")

# Interseção
print(f"A ∩ B (interseção): {A & B}")
print(f"A ∩ B (intersection): {A.intersection(B)}")

# Diferença
print(f"A - B (diferença): {A - B}")
print(f"B - A (diferença): {B - A}")

# Diferença simétrica
print(f"A △ B (dif. simétrica): {A ^ B}")

# Verificações
print(f"\\n4 está em A? {4 in A}")
print(f"9 está em B? {9 in B}")'''
        
        self.exemplo(codigo3)
        self.executar_codigo(codigo3)
        
        self.exercicio(
            "Como acessar um valor de dicionário com segurança?",
            ["get()", "método get", ".get()"],
            "Use o método get() que retorna None se a chave não existir"
        )
        
        # Mini Projeto do Módulo 12
        self._mini_projeto_sistema_contatos()
        
        # Marcar módulo como completo
        self.complete_module()
    
    def _mini_projeto_sistema_contatos(self) -> None:
        """Mini Projeto - Módulo 12: Sistema de Gerenciamento de Contatos"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE CONTATOS")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE CONTATOS")
            print("="*50)
            
        print("📱 Vamos criar um sistema completo de gerenciamento de contatos!")
        print("🛠️ Usando: Dicionários, Sets e Manipulação de Dados")
        
        self.pausar()
        
        codigo_projeto = '''# 📱 SISTEMA DE GERENCIAMENTO DE CONTATOS
# Projeto prático usando dicionários e sets

import json
from datetime import datetime

class SistemaContatos:
    def __init__(self):
        self.contatos = {}  # Dicionário principal
        self.grupos = {}    # Grupos de contatos
        self.historico = [] # Histórico de operações
    
    def adicionar_contato(self, nome, telefone, email=None, grupo="Geral"):
        """Adiciona um novo contato"""
        if nome in self.contatos:
            print(f"❌ Contato {nome} já existe!")
            return False
        
        # Criando contato como dicionário
        contato = {
            "telefone": telefone,
            "email": email or "Não informado",
            "grupo": grupo,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "tags": set()  # Set para tags únicas
        }
        
        self.contatos[nome] = contato
        
        # Adiciona ao grupo
        if grupo not in self.grupos:
            self.grupos[grupo] = set()
        self.grupos[grupo].add(nome)
        
        # Registra no histórico
        self.historico.append(f"Adicionado: {nome} em {contato['data_criacao']}")
        
        print(f"✅ Contato {nome} adicionado com sucesso!")
        return True
    
    def buscar_contato(self, termo):
        """Busca contatos por nome, telefone ou email"""
        resultados = []
        termo_lower = termo.lower()
        
        for nome, dados in self.contatos.items():
            if (termo_lower in nome.lower() or 
                termo in dados["telefone"] or 
                termo_lower in dados["email"].lower()):
                resultados.append((nome, dados))
        
        return resultados
    
    def listar_por_grupo(self, grupo):
        """Lista contatos de um grupo específico"""
        if grupo not in self.grupos:
            return []
        
        contatos_grupo = []
        for nome in self.grupos[grupo]:
            if nome in self.contatos:
                contatos_grupo.append((nome, self.contatos[nome]))
        
        return contatos_grupo
    
    def adicionar_tag(self, nome, tag):
        """Adiciona tag a um contato (usando set)"""
        if nome in self.contatos:
            self.contatos[nome]["tags"].add(tag)
            print(f"🏷️ Tag '{tag}' adicionada ao contato {nome}")
            return True
        return False
    
    def buscar_por_tags(self, tags_buscadas):
        """Busca contatos que tenham todas as tags especificadas"""
        tags_set = set(tags_buscadas)
        resultados = []
        
        for nome, dados in self.contatos.items():
            if tags_set.issubset(dados["tags"]):
                resultados.append((nome, dados))
        
        return resultados
    
    def estatisticas(self):
        """Mostra estatísticas do sistema"""
        total_contatos = len(self.contatos)
        total_grupos = len(self.grupos)
        
        # Conta contatos por grupo
        contatos_por_grupo = {}
        for grupo, nomes in self.grupos.items():
            contatos_por_grupo[grupo] = len(nomes)
        
        # Todas as tags únicas
        todas_tags = set()
        for dados in self.contatos.values():
            todas_tags.update(dados["tags"])
        
        return {
            "total_contatos": total_contatos,
            "total_grupos": total_grupos,
            "contatos_por_grupo": contatos_por_grupo,
            "tags_disponiveis": todas_tags,
            "total_operacoes": len(self.historico)
        }

# DEMONSTRAÇÃO DO SISTEMA
print("=== DEMONSTRAÇÃO: SISTEMA DE CONTATOS ===\\n")

# Criando instância
sistema = SistemaContatos()

# Adicionando contatos
print("📝 ADICIONANDO CONTATOS:")
sistema.adicionar_contato("João Silva", "(11) 99999-1111", "joao@email.com", "Trabalho")
sistema.adicionar_contato("Maria Santos", "(11) 88888-2222", "maria@email.com", "Família")
sistema.adicionar_contato("Pedro Costa", "(11) 77777-3333", "pedro@email.com", "Amigos")
sistema.adicionar_contato("Ana Lima", "(11) 66666-4444", "ana@email.com", "Trabalho")

print("\\n🏷️ ADICIONANDO TAGS:")
sistema.adicionar_tag("João Silva", "programador")
sistema.adicionar_tag("João Silva", "python")
sistema.adicionar_tag("Maria Santos", "família")
sistema.adicionar_tag("Pedro Costa", "faculdade")
sistema.adicionar_tag("Ana Lima", "gerente")
sistema.adicionar_tag("Ana Lima", "programador")

print("\\n🔍 BUSCANDO CONTATOS:")
resultados = sistema.buscar_contato("João")
for nome, dados in resultados:
    print(f"✅ Encontrado: {nome} - {dados['telefone']}")

print("\\n👥 CONTATOS DO GRUPO 'Trabalho':")
trabalho = sistema.listar_por_grupo("Trabalho")
for nome, dados in trabalho:
    print(f"💼 {nome}: {dados['telefone']} ({dados['email']})")

print("\\n🏷️ BUSCA POR TAGS 'programador':")
programadores = sistema.buscar_por_tags(["programador"])
for nome, dados in programadores:
    tags = ", ".join(dados["tags"])
    print(f"👨‍💻 {nome}: Tags [{tags}]")

print("\\n📊 ESTATÍSTICAS DO SISTEMA:")
stats = sistema.estatisticas()
print(f"📱 Total de contatos: {stats['total_contatos']}")
print(f"👥 Total de grupos: {stats['total_grupos']}")
print(f"🏷️ Tags disponíveis: {', '.join(stats['tags_disponiveis'])}")

print("\\n🎉 Sistema de Contatos funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Dicionários para estruturar dados")
print("  • Sets para tags únicas e operações de conjunto")
print("  • Métodos de busca e filtragem")
print("  • Manipulação de dados complexos")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Você criou um sistema completo de contatos!")
        print("🎯 Aplicação real: CRM, agenda pessoal, sistema corporativo")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Contatos Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo12Dicionarios()
    print("Teste do módulo 12 - versão standalone")
    module._dicionarios_sets()