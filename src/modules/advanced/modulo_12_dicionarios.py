#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 12: Dicionários e Sets
Aprenda sobre estruturas de dados avançadas: dicionários e conjuntos
"""

from ..shared.base_module import BaseModule


class Modulo12Dicionarios(BaseModule):
    """Módulo 12: Dominando Dicionários e Sets"""
    
    def __init__(self):
        super().__init__("modulo_12", "Dicionários e Sets")
        self.has_mini_project = True
        self.mini_project_points = 75
    
    def execute(self) -> None:
        """Executa o módulo Dicionários e Sets"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._dicionarios_sets_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _dicionarios_sets_interativo(self) -> None:
        """Conteúdo principal do módulo Dicionários e Sets"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🔑 MÓDULO 12: DOMINANDO DICIONÁRIOS E SETS")
        else:
            print("\n" + "="*50)
            print("🔑 MÓDULO 12: DOMINANDO DICIONÁRIOS E SETS")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Vamos dominar as estruturas de dados mais poderosas do Python!")
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
            self._mini_projeto_agenda_inteligente()
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
                'id': 'secao_conceito_dicionarios',
                'titulo': '🎯 O que são dicionários na programação?',
                'descricao': 'Entenda o poder dos pares chave-valor',
                'funcao': self._secao_conceito_dicionarios
            },
            {
                'id': 'secao_criando_dicionarios',
                'titulo': '⚙️ Como criar e usar dicionários?',
                'descricao': 'Domine a sintaxe e manipulação básica',
                'funcao': self._secao_criando_dicionarios
            },
            {
                'id': 'secao_metodos_dicionarios',
                'titulo': '🔧 Métodos essenciais dos dicionários',
                'descricao': 'Keys, values, items e muito mais',
                'funcao': self._secao_metodos_dicionarios
            },
            {
                'id': 'secao_conceito_sets',
                'titulo': '📦 Sets: conjuntos únicos e poderosos',
                'descricao': 'Aprenda sobre estruturas sem duplicatas',
                'funcao': self._secao_conceito_sets
            },
            {
                'id': 'secao_operacoes_sets',
                'titulo': '🔄 Operações matemáticas com sets',
                'descricao': 'União, interseção e diferença na prática',
                'funcao': self._secao_operacoes_sets
            },
            {
                'id': 'secao_casos_uso_reais',
                'titulo': '🌍 Onde usar na vida real?',
                'descricao': 'Aplicações práticas de dicionários e sets',
                'funcao': self._secao_casos_uso_reais
            },
            {
                'id': 'secao_melhores_praticas',
                'titulo': '⭐ Melhores práticas e dicas avançadas',
                'descricao': 'Técnicas de profissionais experientes',
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
                    if progresso >= 4:  # Pelo menos 4 seções visitadas
                        break
                    else:
                        self.print_warning("📚 Recomendamos visitar pelo menos 4 seções antes de continuar!")
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
    
    def _secao_conceito_dicionarios(self) -> None:
        """Seção: O que são dicionários na programação?"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("O QUE SÃO DICIONÁRIOS NA PROGRAMAÇÃO?", "🎯")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Dicionário",
            "Uma estrutura de dados que armazena pares chave-valor, onde cada chave é única e permite acesso super rápido aos valores"
        )
        
        # === DICA RELACIONADA ===
        self.print_tip("Dicionários são como uma agenda telefônica: você procura pelo nome (chave) e encontra o telefone (valor)!")
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine um armário de arquivos em um escritório:", "text")
        self.print_colored("• Cada gaveta tem uma ETIQUETA (chave) como 'Clientes', 'Fornecedores', 'Contratos'", "text")
        self.print_colored("• Dentro da gaveta estão os DOCUMENTOS (valores) organizados", "text")
        self.print_colored("• Você acha documentos rapidamente procurando pela etiqueta!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXPLICAÇÃO TÉCNICA GRADUAL ===
        self.print_colored("\n🔧 COMO FUNCIONA NA PRÁTICA:", "info")
        passos_tecnicos = [
            "1. 🏷️ Cada elemento tem uma CHAVE única (como um nome ou ID)",
            "2. 📦 Cada chave tem um VALOR associado (dados que você quer guardar)",
            "3. 🔍 Python encontra valores instantaneamente pela chave",
            "4. 🔄 Você pode adicionar, modificar ou remover pares facilmente"
        ]
        
        for i, passo in enumerate(passos_tecnicos, 1):
            self.print_colored(passo, "text")
            if i < len(passos_tecnicos):
                input("   ⏳ Pressione ENTER para o próximo passo...")
        
        # === EXEMPLO DE CÓDIGO ===
        self.print_colored("\n💻 EXEMPLO PRÁTICO:", "success")
        codigo_exemplo = '''# Criando um dicionário de informações pessoais
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Programadora",
    "salario": 8500.00
}

# Acessando valores pela chave
print(f"Nome: {pessoa['nome']}")
print(f"Profissão: {pessoa['profissao']}")
print(f"Salário: R$ {pessoa['salario']:.2f}")

# Adicionando nova informação
pessoa["cidade"] = "São Paulo"
print(f"Cidade: {pessoa['cidade']}")'''
        
        self.exemplo(codigo_exemplo)
        
        # Executa o código para mostrar resultado
        print("\n🚀 Vamos ver funcionando:")
        self.executar_codigo(codigo_exemplo)
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\n🌍 ONDE É USADO NO MUNDO REAL:", "accent")
        aplicacoes = [
            "🏪 E-commerce - dados de produtos (nome, preço, categoria, estoque)",
            "👥 Redes sociais - perfis de usuários (nome, email, bio, seguidores)",
            "🏦 Bancos - contas bancárias (número, titular, saldo, tipo)",
            "📱 Apps - configurações do usuário (tema, idioma, notificações)",
            "🎮 Jogos - estatísticas de jogadores (nivel, pontos, itens)"
        ]
        for app in aplicacoes:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_criando_dicionarios(self) -> None:
        """Seção: Como criar e usar dicionários?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO CRIAR E USAR DICIONÁRIOS?", "⚙️", "success")
        
        # === FORMAS DE CRIAR DICIONÁRIOS ===
        self.print_colored("🛠️ DIFERENTES FORMAS DE CRIAR DICIONÁRIOS:", "warning")
        
        exemplos_criacao = [
            {
                'titulo': 'FORMA 1: Sintaxe de chaves { }',
                'descricao': 'A forma mais comum e visual',
                'codigo': '''# Criando com chaves
produto = {
    "nome": "Notebook",
    "marca": "TechBrand",
    "preco": 2500.00,
    "em_estoque": True
}

print("Produto:", produto)
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']}")''',
                'explicacao': 'Use chaves { } com pares "chave": valor separados por vírgula'
            },
            {
                'titulo': 'FORMA 2: Função dict()',
                'descricao': 'Útil quando as chaves são palavras simples',
                'codigo': '''# Criando com dict()
carro = dict(
    marca="Toyota",
    modelo="Corolla",
    ano=2023,
    cor="Prata"
)

print("Carro:", carro)
print(f"Modelo: {carro['modelo']} {carro['ano']}")''',
                'explicacao': 'A função dict() permite criar sem aspas nas chaves (se forem nomes válidos)'
            },
            {
                'titulo': 'FORMA 3: Dicionário vazio + adição',
                'descricao': 'Construindo dinamicamente',
                'codigo': '''# Começando vazio e adicionando
usuario = {}
usuario["nome"] = "João"
usuario["email"] = "joao@email.com"
usuario["idade"] = 30

print("Usuário:", usuario)

# Ou usando update()
usuario.update({"telefone": "(11) 99999-9999", "ativo": True})
print("Usuário atualizado:", usuario)''',
                'explicacao': 'Útil quando você precisa construir o dicionário dinamicamente'
            }
        ]
        
        for i, exemplo in enumerate(exemplos_criacao, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos_criacao):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        # === ACESSANDO E MODIFICANDO ===
        self.print_colored("\n🔍 ACESSANDO E MODIFICANDO VALORES:", "info")
        
        codigo_acesso = '''# Diferentes formas de acessar valores
estudante = {
    "nome": "Maria",
    "curso": "Engenharia",
    "semestre": 5,
    "notas": [8.5, 9.0, 7.8]
}

# FORMA 1: Colchetes [] - mais direta
print(f"Nome: {estudante['nome']}")

# FORMA 2: Método get() - mais segura
print(f"Curso: {estudante.get('curso')}")
print(f"Idade: {estudante.get('idade', 'Não informado')}")  # Valor padrão

# MODIFICANDO valores
estudante['semestre'] = 6  # Modifica existente
estudante['media'] = 8.43  # Adiciona novo

print("\\nEstudante atualizado:", estudante)'''
        
        self.exemplo(codigo_acesso)
        print("🚀 Vamos ver a diferença entre [] e get():")
        self.executar_codigo(codigo_acesso)
        
        self.print_success("\n🎉 Agora você sabe criar e manipular dicionários básicos!")
        self.pausar()
    
    def _secao_metodos_dicionarios(self) -> None:
        """Seção: Métodos essenciais dos dicionários"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MÉTODOS ESSENCIAIS DOS DICIONÁRIOS", "🔧", "success")
        
        # === MÉTODOS DE VISUALIZAÇÃO ===
        self.print_colored("👀 MÉTODOS PARA VER O CONTEÚDO:", "warning")
        
        codigo_visualizacao = '''# Criando um dicionário de exemplo
loja = {
    "computador": 3500,
    "mouse": 45,
    "teclado": 120,
    "monitor": 800,
    "impressora": 300
}

print("📦 LOJA DE INFORMÁTICA")
print("="*30)

# keys() - todas as chaves
print("🏷️ Produtos disponíveis:")
for produto in loja.keys():
    print(f"  • {produto}")

# values() - todos os valores
print("\\n💰 Preços:")
for preco in loja.values():
    print(f"  • R$ {preco}")

# items() - pares chave-valor
print("\\n📋 CATÁLOGO COMPLETO:")
for produto, preco in loja.items():
    print(f"  • {produto}: R$ {preco}")'''
        
        self.exemplo(codigo_visualizacao)
        print("🚀 Vamos ver os métodos em ação:")
        self.executar_codigo(codigo_visualizacao)
        
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === MÉTODOS DE MODIFICAÇÃO ===
        self.print_colored("\n🛠️ MÉTODOS PARA MODIFICAR:", "info")
        
        codigo_modificacao = '''# Continuando com nossa loja
vendas = {"notebook": 2500, "tablet": 800}

print("📊 GERENCIANDO ESTOQUE")
print("="*25)

# update() - adiciona/atualiza múltiplos itens
print("\\n📦 Adicionando novos produtos...")
vendas.update({"smartphone": 1200, "fone": 150})
vendas.update(tablet=750)  # Atualizando preço existente
print("Produtos após update:", vendas)

# pop() - remove e retorna valor
print("\\n🗑️ Removendo produto...")
preco_removido = vendas.pop("fone")
print(f"Produto removido: fone (R$ {preco_removido})")
print("Produtos restantes:", vendas)

# popitem() - remove último item adicionado
print("\\n📤 Removendo último item...")
ultimo_item = vendas.popitem()
print(f"Último item removido: {ultimo_item}")

# clear() - remove tudo
backup = vendas.copy()  # Fazendo backup
print("\\n🧹 Limpando tudo...")
vendas.clear()
print("Vendas após clear:", vendas)
print("Backup salvo:", backup)'''
        
        self.exemplo(codigo_modificacao)
        print("🚀 Vamos ver as modificações:")
        self.executar_codigo(codigo_modificacao)
        
        # === MÉTODOS ÚTEIS ===
        self.print_colored("\n💡 MÉTODOS SUPER ÚTEIS:", "accent")
        
        codigo_uteis = '''# Métodos que facilitam muito a vida
funcionarios = {
    "Ana": {"cargo": "Gerente", "salario": 8000},
    "Bruno": {"cargo": "Desenvolvedor", "salario": 6000},
    "Carla": {"cargo": "Designer", "salario": 5500}
}

print("👥 SISTEMA DE RH")
print("="*20)

# get() com valor padrão
cargo_joao = funcionarios.get("João", {"cargo": "Não cadastrado", "salario": 0})
print(f"\\nCargo do João: {cargo_joao['cargo']}")

# setdefault() - adiciona se não existir
funcionarios.setdefault("Diana", {"cargo": "Estagiária", "salario": 2000})
print("\\nDiana adicionada:", funcionarios["Diana"])

# in / not in - verificar existência
print("\\n🔍 VERIFICAÇÕES:")
print(f"Ana está cadastrada? {'Ana' in funcionarios}")
print(f"Paulo está cadastrado? {'Paulo' in funcionarios}")

# len() - quantos itens
print(f"\\n📊 Total de funcionários: {len(funcionarios)}")'''
        
        self.exemplo(codigo_uteis)
        print("🚀 Vamos testar os métodos úteis:")
        self.executar_codigo(codigo_uteis)
        
        self.print_success("\n🎉 Agora você domina os métodos essenciais dos dicionários!")
        self.pausar()
    
    def _secao_conceito_sets(self) -> None:
        """Seção: Sets - conjuntos únicos e poderosos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("SETS: CONJUNTOS ÚNICOS E PODEROSOS", "📦")
        
        # === DEFINIÇÃO DO CONCEITO ===
        self.print_concept(
            "Set (Conjunto)",
            "Uma coleção de elementos únicos, sem duplicatas e sem ordem específica. Perfeito para eliminar repetições e operações matemáticas"
        )
        
        # === ANALOGIA DO COTIDIANO ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("Imagine uma cesta de frutas onde:", "text")
        self.print_colored("• Cada fruta aparece APENAS UMA VEZ (sem duplicatas)", "text")
        self.print_colored("• Não importa a ordem das frutas na cesta", "text")
        self.print_colored("• Você pode rapidamente verificar se uma fruta está lá", "text")
        self.print_colored("• Pode comparar duas cestas (união, diferença, etc.)", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === CARACTERÍSTICAS TÉCNICAS ===
        self.print_colored("\n🔧 CARACTERÍSTICAS DOS SETS:", "info")
        caracteristicas = [
            "1. 🎯 ÚNICOS: Nunca tem elementos repetidos",
            "2. 🔄 MUTÁVEIS: Pode adicionar/remover elementos",
            "3. 🚫 SEM ORDEM: Não mantém ordem específica",
            "4. ⚡ RÁPIDOS: Verificação de existência super rápida"
        ]
        
        for caracteristica in caracteristicas:
            self.print_colored(caracteristica, "text")
            input("   ⏳ Pressione ENTER para a próxima...")
        
        # === EXEMPLOS PRÁTICOS ===
        self.print_colored("\n💻 VAMOS VER SETS EM AÇÃO:", "success")
        
        exemplos_sets = [
            {
                'titulo': 'CRIANDO SETS',
                'codigo': '''# Diferentes formas de criar sets
# Forma 1: Chaves com elementos
cores = {"azul", "verde", "vermelho", "azul"}  # Note a duplicata
print("Cores:", cores)  # Duplicata foi removida!

# Forma 2: Função set() com lista
numeros = set([1, 2, 3, 2, 1, 4, 3])
print("Números únicos:", numeros)

# Forma 3: Set de caracteres únicos
letras = set("python")
print("Letras únicas em 'python':", letras)

# Set vazio (cuidado: {} cria dicionário!)
vazio = set()
print("Set vazio:", vazio)'''
            },
            {
                'titulo': 'OPERAÇÕES BÁSICAS',
                'codigo': '''# Operações básicas com sets
animais = {"gato", "cachorro", "pássaro"}
print("Animais:", animais)

# Adicionando elementos
animais.add("peixe")
print("Após adicionar peixe:", animais)

# Tentando adicionar duplicata
animais.add("gato")  # Não adiciona, já existe
print("Após tentar adicionar gato novamente:", animais)

# Removendo elementos
animais.remove("pássaro")  # Erro se não existir
print("Após remover pássaro:", animais)

# Remoção segura
animais.discard("hamster")  # Não dá erro se não existir
print("Após discard hamster:", animais)

# Verificando existência
print(f"\\nTem gato? {'gato' in animais}")
print(f"Tem hamster? {'hamster' in animais}")'''
            }
        ]
        
        for i, exemplo in enumerate(exemplos_sets, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.exemplo(exemplo['codigo'])
            print(f"\n🚀 Executando exemplo {i}:")
            self.executar_codigo(exemplo['codigo'])
            
            if i < len(exemplos_sets):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        # === APLICAÇÕES PRÁTICAS ===
        self.print_colored("\n🌍 ONDE USAR SETS NO MUNDO REAL:", "accent")
        aplicacoes_sets = [
            "🏷️ Remover tags duplicadas em um blog ou rede social",
            "👥 Lista de usuários únicos que visitaram uma página",
            "📧 Filtrar emails únicos de uma lista de contatos",
            "🎯 Verificar rapidamente se um item existe em uma coleção grande",
            "📊 Análise de dados - encontrar elementos únicos"
        ]
        for app in aplicacoes_sets:
            self.print_colored(f"• {app}", "primary")
        
        self.pausar()
    
    def _secao_operacoes_sets(self) -> None:
        """Seção: Operações matemáticas com sets"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("OPERAÇÕES MATEMÁTICAS COM SETS", "🔄", "success")
        
        # === INTRODUÇÃO ===
        self.print_colored("Sets permitem operações matemáticas como na escola!", "text")
        self.print_tip("É como trabalhar com conjuntos na matemática, mas com código!")
        
        # === OPERAÇÕES PRINCIPAIS ===
        codigo_operacoes = '''# Vamos trabalhar com dois grupos de estudantes
grupo_python = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}
grupo_javascript = {"Bruno", "Diana", "Felipe", "Gabriela", "Helena"}

print("👥 GRUPOS DE ESTUDO")
print("="*25)
print(f"🐍 Python: {grupo_python}")
print(f"🟨 JavaScript: {grupo_javascript}")

print("\\n🔄 OPERAÇÕES DE CONJUNTOS:")
print("="*30)

# UNIÃO (|) - Todos os estudantes
todos_estudantes = grupo_python | grupo_javascript
# Ou: todos_estudantes = grupo_python.union(grupo_javascript)
print(f"\\n🤝 UNIÃO - Todos os estudantes:")
print(f"   {todos_estudantes}")
print(f"   Total: {len(todos_estudantes)} pessoas")

# INTERSEÇÃO (&) - Estudantes em ambos os grupos
estudantes_ambos = grupo_python & grupo_javascript
# Ou: estudantes_ambos = grupo_python.intersection(grupo_javascript)
print(f"\\n🎯 INTERSEÇÃO - Estudam ambos:")
print(f"   {estudantes_ambos}")
print(f"   Total: {len(estudantes_ambos)} pessoas")

# DIFERENÇA (-) - Só Python, não JavaScript
so_python = grupo_python - grupo_javascript
# Ou: so_python = grupo_python.difference(grupo_javascript)
print(f"\\n🐍 DIFERENÇA - Só Python:")
print(f"   {so_python}")

# DIFERENÇA (-) - Só JavaScript, não Python  
so_javascript = grupo_javascript - grupo_python
print(f"\\n🟨 DIFERENÇA - Só JavaScript:")
print(f"   {so_javascript}")

# DIFERENÇA SIMÉTRICA (^) - Em um ou outro, mas não ambos
exclusivos = grupo_python ^ grupo_javascript
# Ou: exclusivos = grupo_python.symmetric_difference(grupo_javascript)
print(f"\\n⚡ DIFERENÇA SIMÉTRICA - Exclusivos:")
print(f"   {exclusivos}")
print(f"   Total: {len(exclusivos)} pessoas")'''
        
        self.exemplo(codigo_operacoes)
        print("🚀 Vamos ver as operações matemáticas:")
        self.executar_codigo(codigo_operacoes)
        
        input("\n🔸 Pressione ENTER para ver mais exemplos...")
        
        # === VERIFICAÇÕES ÚTEIS ===
        self.print_colored("\n🔍 VERIFICAÇÕES ÚTEIS:", "info")
        
        codigo_verificacoes = '''# Continuando com nossos grupos de estudo
A = {"Ana", "Bruno", "Carlos"}
B = {"Bruno", "Carlos", "Diana", "Eduardo"}
C = {"Bruno", "Carlos"}

print("🔍 VERIFICAÇÕES AVANÇADAS")
print("="*30)
print(f"A = {A}")
print(f"B = {B}")  
print(f"C = {C}")

# issubset() - Verifica se é subconjunto
print(f"\\n📊 SUBCONJUNTOS:")
print(f"C é subconjunto de A? {C.issubset(A)}")  # True
print(f"C é subconjunto de B? {C.issubset(B)}")  # True
print(f"A é subconjunto de B? {A.issubset(B)}")  # False

# issuperset() - Verifica se contém outro conjunto
print(f"\\n📈 SUPERCONJUNTOS:")
print(f"A contém C? {A.issuperset(C)}")  # True
print(f"B contém C? {B.issuperset(C)}")  # True
print(f"B contém A? {B.issuperset(A)}")  # False

# isdisjoint() - Verifica se não têm elementos em comum
turma_manha = {"João", "Maria", "Pedro"}
turma_tarde = {"Ana", "Carlos", "Lucia"}
print(f"\\n🕐 TURNOS DIFERENTES:")
print(f"Manhã = {turma_manha}")
print(f"Tarde = {turma_tarde}")
print(f"Turnos são disjuntos? {turma_manha.isdisjoint(turma_tarde)}")'''
        
        self.exemplo(codigo_verificacoes)
        print("🚀 Verificando relações entre conjuntos:")
        self.executar_codigo(codigo_verificacoes)
        
        # === CASO PRÁTICO ===
        self.print_colored("\n💡 CASO PRÁTICO: ANÁLISE DE VENDAS", "accent")
        
        codigo_pratico = '''# Simulando análise de vendas
vendas_janeiro = {"notebook", "mouse", "teclado", "monitor", "cabo"}
vendas_fevereiro = {"notebook", "monitor", "impressora", "scanner", "papel"}

print("📊 ANÁLISE DE VENDAS - LOJA DE INFORMÁTICA")
print("="*45)

# Produtos vendidos nos dois meses
produtos_recorrentes = vendas_janeiro & vendas_fevereiro
print(f"🔄 Produtos vendidos nos 2 meses: {produtos_recorrentes}")

# Produtos só de janeiro
so_janeiro = vendas_janeiro - vendas_fevereiro
print(f"🟦 Produtos só em Janeiro: {so_janeiro}")

# Produtos só de fevereiro  
so_fevereiro = vendas_fevereiro - vendas_janeiro
print(f"🟩 Produtos só em Fevereiro: {so_fevereiro}")

# Catálogo completo
catalogo_total = vendas_janeiro | vendas_fevereiro
print(f"📦 Catálogo completo: {catalogo_total}")
print(f"📊 Total de produtos diferentes: {len(catalogo_total)}")

# Insights para o negócio
print(f"\\n💡 INSIGHTS:")
print(f"• {len(produtos_recorrentes)} produtos têm demanda constante")
print(f"• {len(so_janeiro)} produtos saíram de linha")
print(f"• {len(so_fevereiro)} produtos são novidades")'''
        
        self.exemplo(codigo_pratico)
        print("🚀 Analisando vendas com sets:")
        self.executar_codigo(codigo_pratico)
        
        self.print_success("\n🎉 Agora você domina as operações matemáticas com sets!")
        self.pausar()
    
    def _secao_casos_uso_reais(self) -> None:
        """Seção: Onde usar na vida real?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("ONDE USAR NA VIDA REAL?", "🌍", "accent")
        
        # === APLICAÇÕES DE DICIONÁRIOS ===
        self.print_colored("🔑 DICIONÁRIOS NO MUNDO REAL:", "warning")
        
        casos_dicionarios = [
            {
                'setor': '🏪 E-COMMERCE',
                'aplicacao': 'Catálogo de Produtos',
                'exemplo': '''# Sistema de e-commerce
produto = {
    "id": "NB001",
    "nome": "Notebook Gamer",
    "preco": 3500.00,
    "categoria": "Informática",
    "tags": ["gamer", "alta performance", "RGB"],
    "especificacoes": {
        "processador": "Intel i7",
        "memoria": "16GB RAM",
        "armazenamento": "512GB SSD"
    },
    "estoque": 25,
    "avaliacoes": {"media": 4.8, "total": 152}
}'''
            },
            {
                'setor': '🏥 SAÚDE',
                'aplicacao': 'Prontuário Eletrônico',
                'exemplo': '''# Sistema hospitalar
paciente = {
    "id": "P12345",
    "nome": "Maria Silva",
    "data_nascimento": "1985-03-15",
    "contato": {
        "telefone": "(11) 99999-9999",
        "email": "maria@email.com",
        "endereco": "Rua das Flores, 123"
    },
    "historico_medico": [
        {"data": "2024-01-15", "diagnostico": "Gripe", "medico": "Dr. João"},
        {"data": "2024-03-20", "diagnostico": "Check-up", "medico": "Dra. Ana"}
    ],
    "alergias": ["penicilina", "pólen"],
    "tipo_sanguineo": "O+"
}'''
            }
        ]
        
        for caso in casos_dicionarios:
            self.print_colored(f"\n{caso['setor']}: {caso['aplicacao']}", "info")
            self.exemplo(caso['exemplo'])
            input("🔸 Pressione ENTER para o próximo caso...")
        
        # === APLICAÇÕES DE SETS ===
        self.print_colored("\n📦 SETS NO MUNDO REAL:", "warning")
        
        casos_sets = [
            {
                'setor': '📱 REDES SOCIAIS',
                'aplicacao': 'Sistema de Tags e Hashtags',
                'exemplo': '''# Removendo hashtags duplicadas em posts
post1_tags = {"python", "programacao", "tech", "codigo", "python"}
post2_tags = {"javascript", "frontend", "tech", "web"}

# Remove duplicatas automaticamente
print("Tags únicas post 1:", post1_tags)

# Tags populares (aparecem em ambos posts)
tags_populares = post1_tags & post2_tags
print("Tags populares:", tags_populares)

# Todas as tags usadas
todas_tags = post1_tags | post2_tags
print("Todas as tags:", todas_tags)'''
            },
            {
                'setor': '📧 EMAIL MARKETING',
                'aplicacao': 'Gestão de Listas de Contatos',
                'exemplo': '''# Gerenciando listas de email
lista_clientes = {"joao@email.com", "maria@email.com", "pedro@email.com"}
lista_prospects = {"ana@email.com", "maria@email.com", "carlos@email.com"}

# Clientes que também são prospects
clientes_prospects = lista_clientes & lista_prospects
print("Clientes que são prospects:", clientes_prospects)

# Todos os contatos únicos
base_total = lista_clientes | lista_prospects
print(f"Base total: {len(base_total)} emails únicos")

# Prospects que ainda não são clientes
novos_prospects = lista_prospects - lista_clientes
print("Novos prospects:", novos_prospects)'''
            }
        ]
        
        for caso in casos_sets:
            self.print_colored(f"\n{caso['setor']}: {caso['aplicacao']}", "info")
            self.exemplo(caso['exemplo'])
            print("🚀 Executando exemplo:")
            self.executar_codigo(caso['exemplo'])
            input("\n🔸 Pressione ENTER para o próximo caso...")
        
        # === CASOS COMBINADOS ===
        self.print_colored("\n🤝 DICIONÁRIOS + SETS JUNTOS:", "success")
        
        codigo_combinado = '''# Sistema de cursos online combinando ambos
sistema_cursos = {
    "Python Básico": {
        "instrutor": "Prof. Ana",
        "duracao": "40 horas",
        "estudantes": {"João", "Maria", "Pedro", "Ana", "Carlos"},
        "topicos": {"variáveis", "loops", "funções", "listas"}
    },
    "JavaScript Avançado": {
        "instrutor": "Prof. Bruno", 
        "duracao": "60 horas",
        "estudantes": {"Maria", "Pedro", "Lucia", "Rafael"},
        "topicos": {"async", "promises", "react", "nodejs"}
    }
}

# Análises interessantes
print("📚 ANÁLISE DO SISTEMA DE CURSOS")
print("="*35)

# Estudantes únicos na plataforma
todos_estudantes = set()
for curso, dados in sistema_cursos.items():
    todos_estudantes |= dados["estudantes"]  # União
print(f"👥 Total de estudantes únicos: {len(todos_estudantes)}")

# Estudantes que fazem ambos os cursos
python_students = sistema_cursos["Python Básico"]["estudantes"]
js_students = sistema_cursos["JavaScript Avançado"]["estudantes"]
estudantes_dedicados = python_students & js_students
print(f"🎯 Estudantes em ambos cursos: {estudantes_dedicados}")

# Todos os tópicos ensinados
todos_topicos = set()
for curso, dados in sistema_cursos.items():
    todos_topicos |= dados["topicos"]
print(f"📖 Total de tópicos únicos: {len(todos_topicos)}")
print(f"🔍 Tópicos: {todos_topicos}")'''
        
        self.exemplo(codigo_combinado)
        print("🚀 Sistema combinado em ação:")
        self.executar_codigo(codigo_combinado)
        
        self.print_success("\n🎉 Agora você vê o poder dos dicionários e sets em aplicações reais!")
        self.pausar()
    
    def _secao_melhores_praticas(self) -> None:
        """Seção: Melhores práticas e dicas avançadas"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("MELHORES PRÁTICAS E DICAS AVANÇADAS", "⭐")
        
        # === DICAS PARA DICIONÁRIOS ===
        self.print_colored("🔑 DICAS PROFISSIONAIS PARA DICIONÁRIOS:", "warning")
        
        dicas_dict = [
            {
                'titulo': '1. Use get() ao invés de [] para segurança',
                'bom': '''# ✅ Forma segura
usuario = {"nome": "João", "idade": 30}
email = usuario.get("email", "não informado")
print(f"Email: {email}")''',
                'ruim': '''# ❌ Pode dar erro
usuario = {"nome": "João", "idade": 30}
email = usuario["email"]  # KeyError se não existir!'''
            },
            {
                'titulo': '2. Use chaves descritivas e consistentes',
                'bom': '''# ✅ Chaves claras e padronizadas
produto = {
    "nome_produto": "Notebook",
    "preco_unitario": 2500.00,
    "categoria_principal": "Informática",
    "data_cadastro": "2024-01-15"
}''',
                'ruim': '''# ❌ Chaves inconsistentes e confusas
produto = {
    "nome": "Notebook",
    "price": 2500.00,  # Mistura português/inglês
    "cat": "Info",     # Abreviação não clara
    "dt": "2024-01-15" # Abreviação confusa
}'''
            },
            {
                'titulo': '3. Aproveite comprehensions para criar dicionários',
                'bom': '''# ✅ Dictionary comprehension elegante
numeros = [1, 2, 3, 4, 5]
quadrados = {num: num**2 for num in numeros}
print(quadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Criando dicionário com condição
pares_quadrados = {n: n**2 for n in numeros if n % 2 == 0}
print(pares_quadrados)  # {2: 4, 4: 16}''',
                'ruim': '''# ❌ Forma manual e repetitiva
quadrados = {}
for num in [1, 2, 3, 4, 5]:
    quadrados[num] = num**2'''
            }
        ]
        
        for dica in dicas_dict:
            self.print_colored(f"\n{dica['titulo']}", "info")
            self.print_colored("✅ RECOMENDADO:", "success")
            self.exemplo(dica['bom'])
            if 'ruim' in dica:
                self.print_colored("\n❌ EVITE:", "warning")
                self.exemplo(dica['ruim'])
            input("\n🔸 Pressione ENTER para a próxima dica...")
        
        # === DICAS PARA SETS ===
        self.print_colored("\n📦 DICAS PROFISSIONAIS PARA SETS:", "warning")
        
        dicas_sets = [
            {
                'titulo': '1. Use sets para remoção eficiente de duplicatas',
                'bom': '''# ✅ Remoção super rápida de duplicatas
emails_lista = ["a@test.com", "b@test.com", "a@test.com", "c@test.com"]
emails_unicos = list(set(emails_lista))
print(f"Original: {len(emails_lista)} emails")
print(f"Únicos: {len(emails_unicos)} emails")''',
                'explicacao': 'Sets são a forma mais rápida de remover duplicatas!'
            },
            {
                'titulo': '2. Use sets para verificação rápida de existência',
                'bom': '''# ✅ Verificação ultra-rápida (O(1))
usuarios_vip = {"joao", "maria", "pedro", "ana"}  # Set
usuario_atual = "maria"

if usuario_atual in usuarios_vip:  # Instantâneo!
    print("🌟 Usuário VIP detectado!")
else:
    print("👤 Usuário regular")''',
                'ruim': '''# ❌ Verificação lenta em lista grande (O(n))
usuarios_vip = ["joao", "maria", "pedro", "ana"]  # Lista
if usuario_atual in usuarios_vip:  # Lento em listas grandes!
    print("VIP")'''
            }
        ]
        
        for dica in dicas_sets:
            self.print_colored(f"\n{dica['titulo']}", "info")
            self.exemplo(dica['bom'])
            if 'ruim' in dica:
                self.print_colored("\n❌ COMPARAÇÃO - Menos eficiente:", "warning") 
                self.exemplo(dica['ruim'])
            if 'explicacao' in dica:
                self.print_tip(dica['explicacao'])
            input("\n🔸 Pressione ENTER para a próxima dica...")
        
        # === PERFORMANCE E OTIMIZAÇÃO ===
        self.print_colored("\n⚡ DICAS DE PERFORMANCE:", "success")
        
        codigo_performance = '''# Comparando performance de estruturas
import time

# Criando dados de teste
dados_lista = list(range(100000))  # Lista com 100k elementos
dados_set = set(range(100000))     # Set com 100k elementos

# Teste de busca em LISTA (lento)
inicio = time.time()
resultado = 99999 in dados_lista  # Precisa verificar item por item
tempo_lista = time.time() - inicio

# Teste de busca em SET (rápido)
inicio = time.time()
resultado = 99999 in dados_set    # Busca direta por hash
tempo_set = time.time() - inicio

print(f"⏱️  COMPARAÇÃO DE PERFORMANCE:")
print(f"📋 Busca em lista: {tempo_lista:.6f}s")
print(f"📦 Busca em set:   {tempo_set:.6f}s")
print(f"🚀 Set é {tempo_lista/tempo_set:.0f}x mais rápido!")

# Dica prática
print(f"\\n💡 DICA PRÁTICA:")
print(f"• Use LISTA quando precisar de ordem e duplicatas")
print(f"• Use SET quando precisar de busca rápida e elementos únicos")
print(f"• Use DICIONÁRIO para relacionar chaves com valores")'''
        
        self.exemplo(codigo_performance)
        print("🚀 Testando performance:")
        self.executar_codigo(codigo_performance)
        
        # === RESUMO DAS MELHORES PRÁTICAS ===
        self.print_colored("\n📋 RESUMO DAS MELHORES PRÁTICAS:", "accent")
        praticas_resumo = [
            "🔑 Dicionários: Use get() para acesso seguro",
            "📝 Nomes: Escolha chaves descritivas e consistentes",
            "⚡ Performance: Sets para buscas rápidas",
            "🔄 Duplicatas: Sets para remoção eficiente",
            "🧹 Legibilidade: Use comprehensions quando apropriado",
            "🎯 Escolha certa: Lista (ordem), Set (únicos), Dict (chave-valor)"
        ]
        
        for pratica in praticas_resumo:
            self.print_colored(f"• {pratica}", "primary")
        
        self.print_success("\n🎉 Agora você conhece as técnicas dos profissionais!")
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        if self.ui:
            self.ui.clear_screen()
        
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
                'title': 'Quiz: Conhecimentos sobre Dicionários e Sets',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual método é mais seguro para acessar um valor em um dicionário?',
                        'answer': ['get', 'get()', 'método get'],
                        'hint': 'Este método retorna None ou um valor padrão se a chave não existir'
                    },
                    {
                        'question': 'Qual estrutura automaticamente remove elementos duplicados?',
                        'answer': ['set', 'sets', 'conjunto'],
                        'hint': 'Estrutura que representa conjuntos matemáticos'
                    },
                    {
                        'question': 'Como se chama cada elemento individual de um dicionário?',
                        'answer': ['par chave-valor', 'chave-valor', 'par'],
                        'hint': 'Um dicionário armazena estes elementos que têm duas partes'
                    },
                    {
                        'question': 'Qual operação matemática com sets retorna elementos que estão em ambos os conjuntos?',
                        'answer': ['interseção', 'intersection', '&'],
                        'hint': 'Operação que encontra elementos comuns entre dois conjuntos'
                    },
                    {
                        'question': 'Em dicionários, as chaves devem ser sempre...',
                        'answer': ['únicas', 'unicas', 'única'],
                        'hint': 'Cada chave pode aparecer apenas uma vez no dicionário'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Código',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete o código para acessar o valor "idade" do dicionário com segurança',
                        'starter': '''pessoa = {"nome": "João", "cidade": "São Paulo"}
# Complete aqui para acessar idade com valor padrão "Não informado"
idade = pessoa.___("idade", "Não informado")
print(f"Idade: {idade}")''',
                        'solution': 'get',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o código para remover elementos duplicados da lista usando sets',
                        'starter': '''frutas = ["maçã", "banana", "maçã", "laranja", "banana", "uva"]
# Complete aqui para remover duplicatas
frutas_unicas = list(_____(frutas))
print(f"Frutas únicas: {frutas_unicas}")''',
                        'solution': 'set',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o código para encontrar estudantes que fazem ambos os cursos',
                        'starter': '''python_students = {"Ana", "Bruno", "Carlos", "Diana"}
javascript_students = {"Bruno", "Diana", "Eduardo", "Fernanda"}
# Complete aqui para encontrar estudantes em ambos os cursos
ambos_cursos = python_students __ javascript_students
print(f"Estudantes em ambos: {ambos_cursos}")''',
                        'solution': '&',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Sistema de Biblioteca Pessoal',
                'type': 'creative',
                'instruction': '''🎨 PROJETO CRIATIVO: Crie um sistema para sua biblioteca pessoal!

Usando dicionários e sets, crie um sistema que gerencie:
1. 📚 Informações dos livros (título, autor, gênero, ano)
2. 🏷️ Tags/categorias para organização
3. 📊 Estatísticas interessantes

Exemplo de estrutura:
biblioteca = {
    "livro1": {
        "titulo": "Python para Iniciantes",
        "autor": "João Silva", 
        "genero": "Tecnologia",
        "ano": 2023,
        "tags": {"programação", "python", "iniciante"}
    }
}

Seja criativo! Adicione funcionalidades como:
• Busca por gênero ou autor
• Lista de todos os autores únicos
• Tags mais populares
• Livros por década
• Qualquer outra ideia sua!'''
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
                return
            except Exception as e:
                self.print_warning("❌ Erro inesperado no menu. Tente novamente.")
    
    def _show_help(self) -> None:
        """Mostra ajuda sobre as opções disponíveis"""
        self.print_section("AJUDA - SEÇÃO DE PRÁTICA", "❓", "info")
        help_text = [
            "📝 OPÇÃO 1 - Quiz: Teste seus conhecimentos sobre dicionários e sets",
            "💻 OPÇÃO 2 - Complete o Código: 3 exercícios progressivos",
            "🎨 OPÇÃO 3 - Exercício Criativo: Crie um sistema de biblioteca pessoal",
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
    
    def _mini_projeto_agenda_inteligente(self) -> None:
        """Mini Projeto - Módulo 12: Agenda Inteligente com Dicionários e Sets"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: AGENDA INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: AGENDA INTELIGENTE")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Vamos criar uma agenda super inteligente usando dicionários e sets!")
        
        self.print_concept(
            "Agenda Inteligente",
            "Um sistema completo de contatos que usa dicionários para organizar dados e sets para análises rápidas"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de programa é útil para:", "text")
        usos_praticos = [
            "📱 Apps de contatos em smartphones",
            "💼 CRM empresarial para gestão de clientes",
            "👥 Redes sociais para organizar conexões",
            "📧 Sistemas de email marketing",
            "🏢 Diretórios corporativos"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Estrutura dos dados
        self.print_section("PASSO 1: Criando a Estrutura de Dados", "📝", "info")
        self.print_tip("Vamos usar dicionários aninhados e sets para organizar os contatos")
        
        try:
            nome_usuario = input("👤 Qual é o seu nome? ").strip()
            if not nome_usuario:
                nome_usuario = "Usuário"
            
            print(f"\n🎉 Olá {nome_usuario}! Vamos criar sua agenda inteligente!")
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # PASSO 2: Implementação
        self.print_section("PASSO 2: Implementando o Sistema", "⚙️", "success")
        self.print_colored("Agora vamos criar o sistema completo:", "text")
        
        # PASSO 3: Demonstração
        self.print_section("PASSO 3: Sistema em Funcionamento", "🎬", "warning")
        
        # === CÓDIGO FINAL GERADO ===
        self.print_colored("Aqui está sua Agenda Inteligente completa:", "text")
        
        codigo_final = f'''# 🐍 PROJETO: AGENDA INTELIGENTE
# Módulo 12: Dicionários e Sets
# Criado por: {nome_usuario}

class AgendaInteligente:
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = {{}}  # Dicionário principal
        self.grupos = {{}}    # Grupos organizados em sets
        self.tags_globais = set()  # Todas as tags disponíveis
        
    def adicionar_contato(self, nome, telefone, email=None, grupo="Geral"):
        """Adiciona um novo contato à agenda"""
        if nome in self.contatos:
            return f"❌ {nome} já existe na agenda!"
        
        # Criando contato como dicionário aninhado
        contato = {{
            "telefone": telefone,
            "email": email or "Não informado",
            "grupo": grupo,
            "tags": set(),  # Set para tags únicas
            "notas": [],
            "data_adicao": "2024-01-15"  # Poderia usar datetime.now()
        }}
        
        # Adicionando ao dicionário principal
        self.contatos[nome] = contato
        
        # Organizando em grupos (usando sets)
        if grupo not in self.grupos:
            self.grupos[grupo] = set()
        self.grupos[grupo].add(nome)
        
        return f"✅ {nome} adicionado com sucesso ao grupo {grupo}!"
    
    def adicionar_tag(self, nome, tag):
        """Adiciona tag a um contato"""
        if nome in self.contatos:
            self.contatos[nome]["tags"].add(tag)
            self.tags_globais.add(tag)
            return f"🏷️ Tag '{tag}' adicionada a {nome}"
        return f"❌ Contato {nome} não encontrado"
    
    def buscar_por_tag(self, tag):
        """Busca contatos que têm uma tag específica"""
        resultados = []
        for nome, dados in self.contatos.items():
            if tag in dados["tags"]:
                resultados.append(nome)
        return resultados
    
    def listar_grupo(self, grupo):
        """Lista todos os contatos de um grupo"""
        if grupo not in self.grupos:
            return []
        return list(self.grupos[grupo])
    
    def estatisticas(self):
        """Mostra estatísticas da agenda usando sets e dicionários"""
        total_contatos = len(self.contatos)
        total_grupos = len(self.grupos)
        
        # Análise de domínios de email (usando sets)
        dominios = set()
        for dados in self.contatos.values():
            email = dados["email"]
            if "@" in email:
                dominio = email.split("@")[1]
                dominios.add(dominio)
        
        # Contatos por grupo
        grupo_stats = {{grupo: len(nomes) for grupo, nomes in self.grupos.items()}}
        
        return {{
            "total_contatos": total_contatos,
            "total_grupos": total_grupos,
            "dominios_email": dominios,
            "tags_populares": self.tags_globais,
            "distribuicao_grupos": grupo_stats
        }}
    
    def analisar_conexoes(self):
        """Análise avançada usando operações de sets"""
        # Encontrar contatos com tags similares
        conexoes = {{}}
        
        for nome1, dados1 in self.contatos.items():
            conexoes[nome1] = []
            for nome2, dados2 in self.contatos.items():
                if nome1 != nome2:
                    # Interseção de tags (tags em comum)
                    tags_comuns = dados1["tags"] & dados2["tags"]
                    if tags_comuns:
                        conexoes[nome1].append((nome2, tags_comuns))
        
        return conexoes

# DEMONSTRAÇÃO PRÁTICA
print("📱 DEMONSTRAÇÃO: AGENDA INTELIGENTE")
print(f"👤 Proprietário: {nome_usuario}")
print("="*40)

# Criando a agenda
agenda = AgendaInteligente("{nome_usuario}")

# Adicionando contatos
print("\\n📝 ADICIONANDO CONTATOS:")
print(agenda.adicionar_contato("Ana Silva", "(11) 99999-1111", "ana@gmail.com", "Trabalho"))
print(agenda.adicionar_contato("Bruno Costa", "(11) 88888-2222", "bruno@hotmail.com", "Amigos"))
print(agenda.adicionar_contato("Carla Santos", "(11) 77777-3333", "carla@empresa.com", "Trabalho"))
print(agenda.adicionar_contato("Diana Lima", "(11) 66666-4444", "diana@gmail.com", "Família"))

# Adicionando tags
print("\\n🏷️ ORGANIZANDO COM TAGS:")
print(agenda.adicionar_tag("Ana Silva", "programadora"))
print(agenda.adicionar_tag("Ana Silva", "python"))
print(agenda.adicionar_tag("Bruno Costa", "designer"))
print(agenda.adicionar_tag("Bruno Costa", "criativo"))
print(agenda.adicionar_tag("Carla Santos", "gerente"))
print(agenda.adicionar_tag("Carla Santos", "programadora"))
print(agenda.adicionar_tag("Diana Lima", "família"))

# Buscas inteligentes
print("\\n🔍 BUSCAS INTELIGENTES:")
programadores = agenda.buscar_por_tag("programadora")
print(f"👨‍💻 Programadores: {programadores}")

trabalho = agenda.listar_grupo("Trabalho")
print(f"💼 Contatos do trabalho: {trabalho}")

# Estatísticas avançadas
print("\\n📊 ESTATÍSTICAS DA AGENDA:")
stats = agenda.estatisticas()
print(f"📞 Total de contatos: {stats['total_contatos']}")
print(f"👥 Grupos: {stats['total_grupos']}")
print(f"📧 Domínios de email: {stats['dominios_email']}")
print(f"🏷️ Tags disponíveis: {stats['tags_populares']}")
print(f"📈 Distribuição por grupo: {stats['distribuicao_grupos']}")

# Análise de conexões
print("\\n🤝 ANÁLISE DE CONEXÕES:")
conexoes = agenda.analisar_conexoes()
for pessoa, conexoes_pessoa in conexoes.items():
    if conexoes_pessoa:
        print(f"🔗 {pessoa} tem conexões:")
        for amigo, tags_comuns in conexoes_pessoa:
            print(f"   → {amigo} (tags: {tags_comuns})")

print("\\n🎉 Sua Agenda Inteligente está funcionando perfeitamente!")
print("💡 Conceitos aplicados:")
print("  • Dicionários aninhados para estruturar dados complexos")
print("  • Sets para tags únicas e análises rápidas")
print("  • Operações de conjuntos para encontrar conexões")
print("  • Métodos de busca e filtragem eficientes")'''
        
        self.exemplo(codigo_final)
        
        # === EXECUÇÃO DO RESULTADO ===
        self.print_section("RESULTADO FINAL", "🎬", "warning")
        self.executar_codigo(codigo_final)
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success(f"🎉 PARABÉNS {nome_usuario}! Você criou uma agenda super inteligente!")
        
        # === APLICAÇÕES AVANÇADAS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "info")
        proximos_passos = [
            "📱 Adicionar interface gráfica para facilitar o uso",
            "💾 Salvar dados em arquivo JSON para persistência",
            "🔍 Implementar busca por texto em nomes e notas",
            "📊 Criar relatórios visuais com gráficos",
            "🌐 Integrar com redes sociais e serviços web",
            "⏰ Adicionar lembretes e datas importantes"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: Mestre dos Dicionários e Sets!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Agenda Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo12Dicionarios()
    print("Teste do módulo 12 - versão refatorada")
    module.execute()