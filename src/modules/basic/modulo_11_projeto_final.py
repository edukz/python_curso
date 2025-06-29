#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 11: Projeto Final
Integração de todos os conceitos aprendidos em um projeto completo
"""

from ..shared.base_module import BaseModule


class Modulo11ProjetoFinal(BaseModule):
    """Módulo 11: Projeto Final - Sistema Completo de Gestão"""
    
    def __init__(self):
        super().__init__("modulo_11", "Projeto Final Integrado")
        self.has_mini_project = True
        self.mini_project_points = 150
    
    def execute(self) -> None:
        """Executa o módulo Projeto Final Integrado"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._projeto_final_interativo()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _projeto_final_interativo(self) -> None:
        """Conteúdo principal do módulo Projeto Final Integrado"""
        # === CABEÇALHO VISUAL ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎓 MÓDULO 11: PROJETO FINAL - INTEGRANDO TUDO QUE VOCÊ APRENDEU")
        else:
            print("\n" + "="*50)
            print("🎓 MÓDULO 11: PROJETO FINAL - INTEGRANDO TUDO QUE VOCÊ APRENDEU")
            print("="*50)
        
        # === MENSAGENS MOTIVACIONAIS ===
        self.print_success("🎉 Parabéns! Você chegou ao grande projeto final!")
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
            self._mini_projeto_sistema_gestao()
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
                'id': 'secao_revisao_conceitos',
                'titulo': '🎯 Revisão dos conceitos aprendidos',
                'descricao': 'Relembre tudo que você dominou até aqui',
                'funcao': self._secao_revisao_conceitos
            },
            {
                'id': 'secao_integracao_conceitos',
                'titulo': '⚙️ Como integrar todos os conceitos?',
                'descricao': 'Aprenda a combinar diferentes técnicas',
                'funcao': self._secao_integracao_conceitos
            },
            {
                'id': 'secao_planejamento_projeto',
                'titulo': '📋 Planejando um projeto completo',
                'descricao': 'Do conceito à implementação profissional',
                'funcao': self._secao_planejamento_projeto
            },
            {
                'id': 'secao_boas_praticas',
                'titulo': '⭐ Boas práticas de programação',
                'descricao': 'Escreva código limpo e profissional',
                'funcao': self._secao_boas_praticas
            },
            {
                'id': 'secao_exemplos_sistemas',
                'titulo': '💡 Exemplos de sistemas completos',
                'descricao': 'Veja projetos reais funcionando',
                'funcao': self._secao_exemplos_sistemas
            },
            {
                'id': 'secao_proximos_passos',
                'titulo': '🚀 Seus próximos passos como desenvolvedor',
                'descricao': 'O que estudar depois deste módulo',
                'funcao': self._secao_proximos_passos
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
                self.print_success("🌟 Você completou todas as seções! Está pronto para o projeto final!")
            
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
    
    def _secao_revisao_conceitos(self) -> None:
        """Seção: Revisão dos conceitos aprendidos"""
        if self.ui:
            self.ui.clear_screen()
        
        # === CABEÇALHO ATRATIVO ===
        self.print_section("REVISÃO DOS CONCEITOS APRENDIDOS", "🎯")
        
        # === JORNADA DO APRENDIZADO ===
        self.print_concept(
            "Sua Jornada Python",
            "Você percorreu 10 módulos e dominou os fundamentos da programação!"
        )
        
        # === CONCEITOS DOMINADOS ===
        self.print_colored("\n🏆 CONCEITOS QUE VOCÊ DOMINOU:", "success")
        
        conceitos = [
            {
                'modulo': 'Módulo 1',
                'conceito': 'Introdução ao Python',
                'habilidades': ['Instalação', 'Primeiro contato', 'Ambiente de desenvolvimento']
            },
            {
                'modulo': 'Módulo 2',
                'conceito': 'Primeiro Programa',
                'habilidades': ['print()', 'Sintaxe básica', 'Execução de código']
            },
            {
                'modulo': 'Módulo 3',
                'conceito': 'Variáveis',
                'habilidades': ['Criação de variáveis', 'Atribuição', 'Nomes válidos']
            },
            {
                'modulo': 'Módulo 4',
                'conceito': 'Tipos de Dados',
                'habilidades': ['int, float, str, bool', 'Conversões', 'type()']
            },
            {
                'modulo': 'Módulo 5',
                'conceito': 'Entrada de Dados',
                'habilidades': ['input()', 'Interação com usuário', 'Validação']
            },
            {
                'modulo': 'Módulo 6',
                'conceito': 'Operações',
                'habilidades': ['Matemáticas', 'Strings', 'Comparação']
            },
            {
                'modulo': 'Módulo 7',
                'conceito': 'Condições',
                'habilidades': ['if/else/elif', 'Operadores lógicos', 'Decisões']
            },
            {
                'modulo': 'Módulo 8',
                'conceito': 'Loops',
                'habilidades': ['for', 'while', 'range()', 'break/continue']
            },
            {
                'modulo': 'Módulo 9',
                'conceito': 'Listas',
                'habilidades': ['Criação', 'Métodos', 'Iteração', 'List comprehension']
            },
            {
                'modulo': 'Módulo 10',
                'conceito': 'Funções',
                'habilidades': ['def', 'Parâmetros', 'return', 'Reutilização']
            }
        ]
        
        for conceito in conceitos:
            self.print_colored(f"\n📘 {conceito['modulo']}: {conceito['conceito']}", "warning")
            for habilidade in conceito['habilidades']:
                self.print_colored(f"   ✅ {habilidade}", "text")
        
        # === ESTATÍSTICAS ===
        self.print_colored("\n📊 SUAS CONQUISTAS:", "accent")
        self.print_colored("• 10 módulos completados", "primary")
        self.print_colored("• 50+ conceitos dominados", "primary")
        self.print_colored("• 100+ exercícios resolvidos", "primary")
        self.print_colored("• 10 mini projetos criados", "primary")
        
        self.print_success("\n🎉 Você está pronto para criar sistemas completos!")
        self.pausar()
    
    def _secao_integracao_conceitos(self) -> None:
        """Seção: Como integrar todos os conceitos?"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("COMO INTEGRAR TODOS OS CONCEITOS?", "⚙️", "success")
        
        # === CONCEITO DE INTEGRAÇÃO ===
        self.print_concept(
            "Integração de Conceitos",
            "Combinar diferentes técnicas para criar soluções completas e poderosas"
        )
        
        # === ANALOGIA ===
        self.print_colored("\n🏠 ANALOGIA DO DIA A DIA:", "warning")
        self.print_colored("É como cozinhar um prato elaborado: você usa diferentes ingredientes "
                          "(conceitos) e técnicas culinárias (programação) para criar algo delicioso "
                          "(sistema completo)!", "text")
        input("\n🔸 Pressione ENTER para continuar...")
        
        # === EXEMPLO DE INTEGRAÇÃO ===
        self.print_colored("\n💡 EXEMPLO PRÁTICO DE INTEGRAÇÃO:", "info")
        codigo_integracao = '''# Sistema que integra múltiplos conceitos
def sistema_completo():
    # LISTAS para armazenar dados
    usuarios = []
    
    # LOOP principal do sistema
    while True:
        # FUNÇÃO para mostrar menu
        print("\\n=== SISTEMA DE GESTÃO ===")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário")
        print("0. Sair")
        
        # ENTRADA de dados
        opcao = input("\\nEscolha: ")
        
        # CONDIÇÕES para cada opção
        if opcao == "1":
            # VARIÁVEIS para dados
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            
            # OPERAÇÕES com dados
            usuario = {"nome": nome, "idade": idade}
            usuarios.append(usuario)
            print("✅ Cadastrado!")
            
        elif opcao == "2":
            # LOOP para listar
            for i, user in enumerate(usuarios, 1):
                print(f"{i}. {user['nome']} - {user['idade']} anos")
                
        elif opcao == "0":
            break

# Executando o sistema
print("🚀 Sistema integrando todos os conceitos!")'''
        
        self.exemplo(codigo_integracao)
        
        # === PADRÕES DE INTEGRAÇÃO ===
        self.print_colored("\n🔧 PADRÕES COMUNS DE INTEGRAÇÃO:", "accent")
        padroes = [
            "📊 Dados + Loops = Processamento de informações",
            "🎮 Input + Condições = Interatividade",
            "📝 Listas + Funções = Organização de código",
            "🔄 While + If/Else = Menus interativos",
            "💾 Variáveis + Funções = Estado do sistema"
        ]
        
        for padrao in padroes:
            self.print_colored(f"• {padrao}", "primary")
        
        self.print_tip("A chave é pensar em cada conceito como uma ferramenta em sua caixa!")
        self.pausar()
    
    def _secao_planejamento_projeto(self) -> None:
        """Seção: Planejando um projeto completo"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PLANEJANDO UM PROJETO COMPLETO", "📋", "info")
        
        # === ETAPAS DO PLANEJAMENTO ===
        self.print_concept(
            "Planejamento Profissional",
            "Todo grande projeto começa com um bom planejamento"
        )
        
        self.print_colored("\n📐 ETAPAS DO PLANEJAMENTO:", "warning")
        
        etapas = [
            {
                'numero': '1',
                'titulo': 'Definir o Problema',
                'descricao': 'O que o sistema vai resolver?',
                'exemplo': 'Sistema para gerenciar tarefas diárias'
            },
            {
                'numero': '2',
                'titulo': 'Listar Funcionalidades',
                'descricao': 'O que o sistema precisa fazer?',
                'exemplo': 'Adicionar, listar, marcar como concluída, deletar'
            },
            {
                'numero': '3',
                'titulo': 'Escolher Estruturas',
                'descricao': 'Quais conceitos usar?',
                'exemplo': 'Lista para tarefas, funções para cada ação'
            },
            {
                'numero': '4',
                'titulo': 'Desenhar o Fluxo',
                'descricao': 'Como o usuário interage?',
                'exemplo': 'Menu → Escolha → Ação → Feedback'
            },
            {
                'numero': '5',
                'titulo': 'Implementar Passo a Passo',
                'descricao': 'Construir incrementalmente',
                'exemplo': 'Primeiro o menu, depois cada funcionalidade'
            }
        ]
        
        for etapa in etapas:
            self.print_colored(f"\n{etapa['numero']}. {etapa['titulo']}", "accent")
            self.print_colored(f"   📝 {etapa['descricao']}", "text")
            self.print_colored(f"   💡 Exemplo: {etapa['exemplo']}", "info")
            input("   ⏳ Pressione ENTER para próxima etapa...")
        
        # === EXEMPLO DE PLANEJAMENTO ===
        self.print_colored("\n📊 EXEMPLO: Planejando um Sistema de Biblioteca", "success")
        exemplo_plano = '''# PLANEJAMENTO: Sistema de Biblioteca

## 1. PROBLEMA:
   - Gerenciar livros de uma biblioteca pessoal

## 2. FUNCIONALIDADES:
   - Cadastrar livros
   - Listar todos os livros
   - Buscar por título/autor
   - Emprestar/devolver livros
   - Ver estatísticas

## 3. ESTRUTURAS NECESSÁRIAS:
   - Lista: armazenar livros
   - Dicionários: dados de cada livro
   - Funções: cada funcionalidade
   - Loops: menu e listagens
   - Condições: validações

## 4. FLUXO:
   Menu Principal
   ├── Cadastrar → Input dados → Adicionar lista
   ├── Listar → Loop na lista → Mostrar dados
   ├── Buscar → Input termo → Filtrar lista
   └── Sair → Encerrar programa'''
        
        self.print_code_section("PLANEJAMENTO", exemplo_plano)
        
        self.print_success("\n🎯 Com um bom plano, programar fica muito mais fácil!")
        self.pausar()
    
    def _secao_boas_praticas(self) -> None:
        """Seção: Boas práticas de programação"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("BOAS PRÁTICAS DE PROGRAMAÇÃO", "⭐", "warning")
        
        # === CONCEITO ===
        self.print_concept(
            "Código Profissional",
            "Escrever código que seja fácil de ler, manter e expandir"
        )
        
        # === COMPARAÇÃO ===
        self.print_colored("\n❌ CÓDIGO RUIM vs ✅ CÓDIGO BOM:", "accent")
        
        # Exemplo 1: Nomes de variáveis
        self.print_colored("\n📝 NOMES DE VARIÁVEIS:", "info")
        comparacao1 = '''# ❌ Ruim
x = 25
y = "João"
z = x * 1.1

# ✅ Bom
idade = 25
nome = "João"
idade_com_bonus = idade * 1.1'''
        self.exemplo(comparacao1)
        
        # Exemplo 2: Funções
        self.print_colored("\n🔧 ORGANIZAÇÃO COM FUNÇÕES:", "info")
        comparacao2 = '''# ❌ Ruim - Tudo junto
nome = input("Nome: ")
idade = int(input("Idade: "))
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

# ✅ Bom - Organizado em funções
def obter_dados_usuario():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    return nome, idade

def verificar_maioridade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade"
    else:
        return f"{nome} é menor de idade"

# Uso limpo
nome, idade = obter_dados_usuario()
resultado = verificar_maioridade(nome, idade)
print(resultado)'''
        self.exemplo(comparacao2)
        
        # === DICAS DE OURO ===
        self.print_colored("\n💎 DICAS DE OURO:", "success")
        dicas = [
            "📝 Use nomes descritivos para variáveis e funções",
            "🔧 Uma função = uma responsabilidade",
            "💬 Comente código complexo, não o óbvio",
            "📏 Mantenha linhas com menos de 80 caracteres",
            "🧹 Delete código morto (não usado)",
            "🎯 Seja consistente no estilo",
            "🐛 Trate erros adequadamente",
            "📚 Organize código em seções lógicas"
        ]
        
        for dica in dicas:
            self.print_colored(f"• {dica}", "primary")
        
        self.print_tip("Código limpo é um presente para o seu eu futuro!")
        self.pausar()
    
    def _secao_exemplos_sistemas(self) -> None:
        """Seção: Exemplos de sistemas completos"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("EXEMPLOS DE SISTEMAS COMPLETOS", "💡", "success")
        
        exemplos = [
            {
                'titulo': 'EXEMPLO 1: Sistema de Vendas Simples',
                'descricao': 'Gerencia produtos e calcula totais',
                'codigo': '''# Sistema de Vendas
produtos = []
vendas = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    produtos.append({"nome": nome, "preco": preco})
    print("✅ Produto cadastrado!")

def realizar_venda():
    if not produtos:
        print("❌ Nenhum produto cadastrado!")
        return
    
    print("\\nProdutos disponíveis:")
    for i, prod in enumerate(produtos):
        print(f"{i+1}. {prod['nome']} - R$ {prod['preco']:.2f}")
    
    escolha = int(input("Escolha o produto: ")) - 1
    quantidade = int(input("Quantidade: "))
    
    total = produtos[escolha]['preco'] * quantidade
    vendas.append({
        "produto": produtos[escolha]['nome'],
        "quantidade": quantidade,
        "total": total
    })
    print(f"✅ Venda realizada! Total: R$ {total:.2f}")

def relatorio_vendas():
    if not vendas:
        print("❌ Nenhuma venda realizada!")
        return
    
    total_geral = 0
    print("\\n📊 RELATÓRIO DE VENDAS:")
    for venda in vendas:
        print(f"• {venda['produto']} x{venda['quantidade']} = R$ {venda['total']:.2f}")
        total_geral += venda['total']
    print(f"\\nTOTAL GERAL: R$ {total_geral:.2f}")

# Demonstração
print("🛒 SISTEMA DE VENDAS")
cadastrar_produto()  # Simula cadastro
realizar_venda()     # Simula venda
relatorio_vendas()   # Mostra relatório''',
                'explicacao': 'Integra listas, dicionários, funções, loops e cálculos'
            },
            {
                'titulo': 'EXEMPLO 2: Gerenciador de Contatos',
                'descricao': 'Agenda telefônica com busca',
                'codigo': '''# Gerenciador de Contatos
contatos = []

def adicionar_contato(nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)
    return f"✅ Contato {nome} adicionado!"

def buscar_contato(termo):
    encontrados = []
    for contato in contatos:
        if termo.lower() in contato["nome"].lower():
            encontrados.append(contato)
    return encontrados

def listar_contatos():
    if not contatos:
        return "📭 Nenhum contato cadastrado"
    
    resultado = "📱 LISTA DE CONTATOS:\\n"
    for i, contato in enumerate(contatos, 1):
        resultado += f"{i}. {contato['nome']}\\n"
        resultado += f"   📞 {contato['telefone']}\\n"
        resultado += f"   ✉️  {contato['email']}\\n"
    return resultado

# Demonstração
print("📱 GERENCIADOR DE CONTATOS")
print(adicionar_contato("João Silva", "(11) 98765-4321", "joao@email.com"))
print(adicionar_contato("Maria Santos", "(21) 91234-5678", "maria@email.com"))
print(listar_contatos())''',
                'explicacao': 'Usa funções com return, listas de dicionários e busca'
            }
        ]
        
        for i, exemplo in enumerate(exemplos, 1):
            self.print_colored(f"\n{exemplo['titulo']}", "warning")
            self.print_colored(f"📝 {exemplo['descricao']}", "text")
            
            self.print_code_section("CÓDIGO", exemplo['codigo'])
            
            print("\n🚀 Executando exemplo:")
            self.executar_codigo(exemplo['codigo'])
            
            if exemplo['explicacao']:
                self.print_colored(f"\n💡 EXPLICAÇÃO: {exemplo['explicacao']}", "info")
            
            if i < len(exemplos):
                input("\n🔸 Pressione ENTER para o próximo exemplo...")
        
        self.print_success("\n🎉 Agora você viu sistemas completos em ação!")
        self.pausar()
    
    def _secao_proximos_passos(self) -> None:
        """Seção: Seus próximos passos como desenvolvedor"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("SEUS PRÓXIMOS PASSOS COMO DESENVOLVEDOR", "🚀", "accent")
        
        # === PARABÉNS ===
        self.print_success("🎊 PARABÉNS! Você completou os módulos básicos!")
        self.print_colored("Você tem uma base sólida e está pronto para avançar!", "text")
        
        # === O QUE VEM DEPOIS ===
        self.print_colored("\n📚 MÓDULOS AVANÇADOS (12-23):", "warning")
        topicos_avancados = [
            "📖 Dicionários e estruturas complexas",
            "🔧 Funções avançadas e decoradores",
            "📦 Módulos e pacotes",
            "📅 Manipulação de datas e tempo",
            "📄 Trabalho com arquivos",
            "📊 JSON e CSV",
            "🎯 Orientação a Objetos",
            "🎨 Classes e herança",
            "⚡ Geradores e iteradores",
            "🔍 Expressões regulares",
            "🐛 Debugging profissional"
        ]
        
        for topico in topicos_avancados:
            self.print_colored(f"  • {topico}", "text")
        
        # === MÓDULOS ESSENCIAIS ===
        self.print_colored("\n⚡ MÓDULOS ESSENCIAIS (24-30):", "info")
        topicos_essenciais = [
            "🧪 Testes e TDD",
            "📡 Async/await",
            "🌐 APIs e Web",
            "🛠️ Ambientes virtuais",
            "🎯 Type hints",
            "📊 Análise de dados",
            "🔐 Segurança"
        ]
        
        for topico in topicos_essenciais:
            self.print_colored(f"  • {topico}", "text")
        
        # === PROJETOS SUGERIDOS ===
        self.print_colored("\n💼 PROJETOS PARA PRATICAR:", "success")
        projetos = [
            "🎮 Jogo da Velha com IA",
            "📝 To-Do List com persistência",
            "💰 Sistema bancário completo",
            "🌐 Web scraper simples",
            "📊 Analisador de dados CSV",
            "🤖 Bot para automação",
            "📱 Agenda com banco de dados"
        ]
        
        for projeto in projetos:
            self.print_colored(f"  • {projeto}", "primary")
        
        # === COMUNIDADE ===
        self.print_colored("\n👥 JUNTE-SE À COMUNIDADE:", "accent")
        self.print_colored("• Participe de fóruns Python", "text")
        self.print_colored("• Contribua em projetos open source", "text")
        self.print_colored("• Compartilhe seus projetos", "text")
        self.print_colored("• Ajude outros iniciantes", "text")
        
        self.print_success("\n🌟 O céu é o limite! Continue aprendendo e criando!")
        self.print_tip("Lembre-se: todo expert já foi iniciante. Persistência é a chave!")
        
        self.pausar()
    
    def _secao_pratica_interativa(self) -> None:
        """Seção de prática interativa do módulo"""
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_section("HORA DE PRATICAR!", "🎯", "success")
        self.print_colored("Vamos testar sua capacidade de integrar todos os conceitos!", "text")
        
        # === INSTRUÇÕES PARA INICIANTES ===
        self.print_tip("Para este projeto final, você usará TUDO que aprendeu!")
        self.print_colored("\n🎓 SOBRE OS EXERCÍCIOS:", "info")
        self.print_colored("• Integre múltiplos conceitos em cada solução", "text")
        self.print_colored("• Pense em soluções completas, não apenas funcionais", "text")
        self.print_colored("• Use funções para organizar seu código", "text")
        self.print_colored("• Aplique as boas práticas aprendidas", "text")
        
        # === DEFINIÇÃO DOS EXERCÍCIOS ===
        exercicios = [
            {
                'title': 'Quiz: Integrando Conceitos',
                'type': 'quiz',
                'questions': [
                    {
                        'question': 'Qual estrutura é melhor para armazenar múltiplos dados do mesmo tipo?',
                        'answer': ['lista', 'listas', 'list'],
                        'hint': 'Pense em uma coleção ordenada de elementos'
                    },
                    {
                        'question': 'Como você repetiria uma ação 10 vezes em Python?',
                        'answer': ['for', 'loop for', 'for loop'],
                        'hint': 'Use uma estrutura de repetição com range'
                    },
                    {
                        'question': 'Qual comando retorna um valor de uma função?',
                        'answer': ['return'],
                        'hint': 'Palavra em inglês que significa "retornar"'
                    },
                    {
                        'question': 'Como verificar se um número é par?',
                        'answer': ['numero % 2 == 0', '% 2 == 0', 'modulo 2'],
                        'hint': 'Use o operador de resto da divisão'
                    },
                    {
                        'question': 'Qual estrutura permite tomar decisões no código?',
                        'answer': ['if', 'if else', 'condicional'],
                        'hint': 'Estrutura que testa condições'
                    }
                ]
            },
            {
                'title': 'Desafio: Complete o Sistema',
                'type': 'code_completion',
                'exercises': [
                    {
                        'instruction': 'BÁSICO: Complete a função que calcula média de uma lista',
                        'starter': '''def calcular_media(numeros):
    # Complete aqui
    total = ___
    quantidade = ___
    return ___

print(calcular_media([10, 20, 30, 40, 50]))''',
                        'solution': 'sum(numeros)\nlen(numeros)\ntotal / quantidade',
                        'type': 'simple'
                    },
                    {
                        'instruction': 'INTERMEDIÁRIO: Complete o sistema de login',
                        'starter': '''usuarios = [{"nome": "admin", "senha": "123"}]

def fazer_login(nome, senha):
    for usuario in usuarios:
        if ___ and ___:
            return "Login realizado!"
    return ___

print(fazer_login("admin", "123"))''',
                        'solution': 'usuario["nome"] == nome\nusuario["senha"] == senha\n"Login falhou!"',
                        'type': 'intermediate'
                    },
                    {
                        'instruction': 'AVANÇADO: Complete o sistema de busca',
                        'starter': '''produtos = [
    {"nome": "Notebook", "preco": 3000},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150}
]

def buscar_por_preco_maximo(preco_max):
    encontrados = []
    for produto in produtos:
        if ___:
            ___
    return ___

print(buscar_por_preco_maximo(200))''',
                        'solution': 'produto["preco"] <= preco_max\nencontrados.append(produto)\nencontrados',
                        'type': 'advanced'
                    }
                ]
            },
            {
                'title': 'Exercício Criativo: Seu Próprio Sistema',
                'type': 'creative',
                'instruction': 'Crie um mini sistema que use: variáveis, input, listas, loops, condições e funções. '
                             'Pode ser um jogo, calculadora especial, gerenciador de algo, ou qualquer ideia sua!'
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
                elif escolha in ["1", "quiz", "integracao"]:
                    try:
                        self._run_quiz(exercicios[0])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Quiz interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no quiz. Continuando...")
                elif escolha in ["2", "sistema", "completar"]:
                    try:
                        self._run_code_completion(exercicios[1])
                    except KeyboardInterrupt:
                        self.print_warning("\n\n⚠️ Exercício interrompido. Voltando ao menu principal...")
                        return
                    except Exception as e:
                        self.print_warning("❌ Erro no exercício. Continuando...")
                elif escolha in ["3", "criativo", "projeto"]:
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
            "📝 OPÇÃO 1 - Quiz: Teste integração de conceitos",
            "💻 OPÇÃO 2 - Complete o Sistema: 3 desafios progressivos",
            "🎨 OPÇÃO 3 - Projeto Criativo: Crie seu próprio sistema",
            "🔢 OPÇÃO 0 - Continue para o Projeto Final completo",
            "",
            "💡 DICAS:",
            "• Este é o módulo final - use TODOS os conceitos!",
            "• Pense em soluções completas e organizadas",
            "• Aplique as boas práticas aprendidas",
            "• Seja criativo mas mantenha o código limpo!"
        ]
        
        for line in help_text:
            if line:
                self.print_colored(f"  {line}", "text")
            else:
                print()
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_quiz(self, quiz_data) -> None:
        """Executa o quiz de integração"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("QUIZ: INTEGRANDO CONCEITOS", "📝", "warning")
        self.print_colored("Teste seu conhecimento integrado!", "text")
        
        acertos = 0
        total_perguntas = len(quiz_data['questions'])
        
        for i, pergunta in enumerate(quiz_data['questions'], 1):
            self.print_colored(f"\n📝 PERGUNTA {i}/{total_perguntas}:", "accent")
            if self.exercicio(pergunta['question'], pergunta['answer'], pergunta['hint']):
                acertos += 1
            
            input("\n🔸 Pressione ENTER para continuar...")
        
        # Resultado final
        self.print_section("RESULTADO DO QUIZ", "🏆", "success")
        percentual = (acertos / total_perguntas) * 100
        
        if percentual >= 80:
            self.print_success(f"🎉 EXCELENTE! Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)")
            self.print_colored("Você domina a integração de conceitos!", "success")
        elif percentual >= 60:
            self.print_colored(f"👍 BOM! Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)", "warning")
            self.print_colored("Continue praticando a integração!", "text")
        else:
            self.print_colored(f"💪 Você acertou {acertos}/{total_perguntas} ({percentual:.0f}%)", "error")
            self.print_colored("Revise os módulos anteriores!", "text")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_code_completion(self, code_data) -> None:
        """Executa exercícios de completar sistema"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("DESAFIO: COMPLETE O SISTEMA", "💻", "accent")
        self.print_colored("Complete sistemas que integram múltiplos conceitos!", "text")
        
        for i, exercicio in enumerate(code_data['exercises'], 1):
            self.print_colored(f"\n💻 EXERCÍCIO {i}/{len(code_data['exercises'])}: {exercicio['instruction']}", "warning")
            
            self.print_code_section("CÓDIGO PARA COMPLETAR", exercicio['starter'])
            
            self.print_colored("\n✍️ Complete onde está '___' (múltiplas linhas se necessário)", "info")
            
            # Para exercícios com múltiplas lacunas
            if exercicio['type'] != 'simple':
                self.print_colored("DICA: Este exercício tem múltiplas lacunas. Complete uma por vez!", "info")
            
            resposta = input("👉 Sua resposta: ").strip()
            
            # Verifica se a resposta contém os elementos essenciais
            solucao_partes = exercicio['solution'].split('\n')
            resposta_correta = all(parte.strip() in resposta for parte in solucao_partes if parte.strip())
            
            if resposta_correta:
                self.print_success("✅ CORRETO! Excelente integração de conceitos!")
                
                # Mostra código funcionando
                codigo_completo = exercicio['starter']
                for parte in solucao_partes:
                    codigo_completo = codigo_completo.replace('___', parte, 1)
                
                self.print_colored("\n🚀 Veja o sistema funcionando:", "success")
                self.executar_codigo(codigo_completo)
            else:
                self.print_warning(f"❌ Não foi dessa vez. A solução era:\n{exercicio['solution']}")
                
                # Mostra código correto
                codigo_completo = exercicio['starter']
                for parte in solucao_partes:
                    codigo_completo = codigo_completo.replace('___', parte, 1)
                
                self.print_colored("\n💡 Veja como fica o sistema completo:", "info")
                self.executar_codigo(codigo_completo)
            
            if i < len(code_data['exercises']):
                input("\n🔸 Pressione ENTER para o próximo desafio...")
        
        self.print_success("\n🎉 Parabéns por completar os desafios de integração!")
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _run_creative_exercise(self, creative_data) -> None:
        """Executa exercício criativo final"""
        if self.ui:
            self.ui.clear_screen()
        
        self.print_section("PROJETO CRIATIVO: SEU PRÓPRIO SISTEMA", "🎨", "success")
        self.print_colored(creative_data['instruction'], "text")
        
        self.print_colored("\n💡 REQUISITOS MÍNIMOS:", "info")
        requisitos = [
            "📝 Use variáveis para armazenar dados",
            "⌨️ Use input() para interação",
            "📋 Use lista para múltiplos itens",
            "🔄 Use loop para repetições",
            "❓ Use if/else para decisões",
            "🔧 Use pelo menos 2 funções"
        ]
        
        for req in requisitos:
            self.print_colored(f"  {req}", "primary")
        
        self.print_colored("\n🎯 IDEIAS DE PROJETOS:", "warning")
        ideias = [
            "🎮 Jogo de adivinhação com níveis",
            "📚 Sistema de biblioteca pessoal",
            "💰 Controle de gastos mensais",
            "📝 Lista de tarefas inteligente",
            "🎬 Catálogo de filmes favoritos",
            "🍕 Sistema de pedidos de restaurante"
        ]
        
        for ideia in ideias:
            self.print_colored(f"  • {ideia}", "accent")
        
        self.print_colored("\n🖥️ DIGITE SEU CÓDIGO:", "success")
        self.print_colored("(Digite 'fim' em uma linha vazia para terminar)", "text")
        
        codigo_usuario = []
        while True:
            linha = input()
            if linha.lower() == 'fim':
                break
            codigo_usuario.append(linha)
        
        codigo_completo = '\n'.join(codigo_usuario)
        
        if codigo_completo.strip():
            self.print_colored("\n🚀 EXECUTANDO SEU SISTEMA:", "success")
            try:
                exec(codigo_completo)
                self.print_success("\n🎉 INCRÍVEL! Seu sistema funcionou perfeitamente!")
                self.print_colored("Você demonstrou domínio de todos os conceitos!", "success")
                
                # Análise do código
                conceitos_usados = []
                if 'def ' in codigo_completo:
                    conceitos_usados.append("✅ Funções")
                if 'for ' in codigo_completo or 'while ' in codigo_completo:
                    conceitos_usados.append("✅ Loops")
                if 'if ' in codigo_completo:
                    conceitos_usados.append("✅ Condições")
                if '[' in codigo_completo:
                    conceitos_usados.append("✅ Listas")
                if 'input(' in codigo_completo:
                    conceitos_usados.append("✅ Entrada de dados")
                
                if conceitos_usados:
                    self.print_colored("\n📊 CONCEITOS IDENTIFICADOS:", "info")
                    for conceito in conceitos_usados:
                        self.print_colored(f"  {conceito}", "primary")
                
            except Exception as e:
                self.print_warning(f"\n❌ Erro: {e}")
                self.print_colored("Continue praticando! Erros fazem parte do aprendizado.", "info")
        else:
            self.print_colored("\nNenhum código foi digitado. Tente novamente quando estiver pronto!", "text")
        
        input("\n🔸 Pressione ENTER para voltar ao menu...")
    
    def _mini_projeto_sistema_gestao(self) -> None:
        """Mini Projeto - Módulo 11: Sistema Completo de Gestão"""
        
        # === CABEÇALHO IMPACTANTE ===
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 PROJETO FINAL: SISTEMA DE GESTÃO PESSOAL COMPLETO")
        else:
            print("\n" + "="*50)
            print("🎯 PROJETO FINAL: SISTEMA DE GESTÃO PESSOAL COMPLETO")
            print("="*50)
        
        # === INTRODUÇÃO MOTIVACIONAL ===
        self.print_success("🎉 Este é o momento! Vamos criar um sistema profissional completo!")
        
        self.print_concept(
            "Sistema de Gestão Pessoal",
            "Um sistema completo que integra TODOS os conceitos aprendidos para gerenciar sua vida"
        )
        
        # === APLICAÇÕES NO MUNDO REAL ===
        self.print_colored("\nEste tipo de sistema é usado para:", "text")
        usos_praticos = [
            "Organizar tarefas e compromissos diários",
            "Controlar finanças pessoais",
            "Gerenciar contatos importantes",
            "Acompanhar metas e objetivos"
        ]
        for uso in usos_praticos:
            self.print_colored(f"• {uso}", "accent")
        
        # === DESENVOLVIMENTO PASSO A PASSO ===
        
        # PASSO 1: Estrutura do Sistema
        self.print_section("PASSO 1: Planejando a Estrutura", "📝", "info")
        self.print_tip("Vamos criar um sistema modular com várias funcionalidades!")
        
        try:
            # PASSO 2: Implementação
            self.print_section("PASSO 2: Implementando o Sistema", "⚙️", "success")
            self.print_colored("Integrando todos os conceitos aprendidos:", "text")
            
            # PASSO 3: Sistema Funcionando
            self.print_section("PASSO 3: Sistema em Ação", "🎬", "warning")
            
            # === CÓDIGO FINAL GERADO ===
            self.print_colored("Aqui está seu Sistema de Gestão Pessoal Completo:", "text")
            
            codigo_final = f'''# 🐍 PROJETO FINAL: SISTEMA DE GESTÃO PESSOAL
# Módulo 11: Integrando TODOS os conceitos Python

import datetime

# ========== ESTRUTURAS DE DADOS ==========
tarefas = []
financas = []
contatos = []
metas = []

# ========== FUNÇÕES DO SISTEMA ==========

def exibir_menu_principal():
    """Exibe o menu principal do sistema"""
    print("\\n" + "="*50)
    print("🏠 SISTEMA DE GESTÃO PESSOAL")
    print("="*50)
    print("1. 📝 Gerenciar Tarefas")
    print("2. 💰 Controle Financeiro")
    print("3. 📱 Agenda de Contatos")
    print("4. 🎯 Metas e Objetivos")
    print("5. 📊 Relatórios")
    print("0. 🚪 Sair")
    print("="*50)

# === MÓDULO DE TAREFAS ===
def adicionar_tarefa():
    """Adiciona nova tarefa"""
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")
    prazo = input("Prazo (dd/mm/aaaa): ")
    prioridade = input("Prioridade (alta/média/baixa): ")
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "concluida": False,
        "data_criacao": datetime.datetime.now().strftime("%d/%m/%Y")
    }
    
    tarefas.append(tarefa)
    return "✅ Tarefa adicionada com sucesso!"

def listar_tarefas():
    """Lista todas as tarefas"""
    if not tarefas:
        return "📭 Nenhuma tarefa cadastrada"
    
    print("\\n📋 SUAS TAREFAS:")
    print("-" * 50)
    
    for i, tarefa in enumerate(tarefas, 1):
        status = "✅" if tarefa["concluida"] else "⏳"
        prioridade_emoji = {"alta": "🔴", "média": "🟡", "baixa": "🟢"}
        emoji = prioridade_emoji.get(tarefa["prioridade"], "⚪")
        
        print(f"{i}. {status} {tarefa['titulo']} {emoji}")
        print(f"   📅 Prazo: {tarefa['prazo']}")
        print(f"   📝 {tarefa['descricao']}")
        print("-" * 50)

# === MÓDULO FINANCEIRO ===
def adicionar_transacao():
    """Adiciona transação financeira"""
    tipo = input("Tipo (receita/despesa): ").lower()
    categoria = input("Categoria: ")
    valor = float(input("Valor: R$ "))
    descricao = input("Descrição: ")
    
    transacao = {
        "tipo": tipo,
        "categoria": categoria,
        "valor": valor,
        "descricao": descricao,
        "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    financas.append(transacao)
    return f"✅ {tipo.capitalize()} de R$ {valor:.2f} registrada!"

def resumo_financeiro():
    """Mostra resumo financeiro"""
    if not financas:
        return "📊 Nenhuma transação registrada"
    
    receitas = sum(t["valor"] for t in financas if t["tipo"] == "receita")
    despesas = sum(t["valor"] for t in financas if t["tipo"] == "despesa")
    saldo = receitas - despesas
    
    print("\\n💰 RESUMO FINANCEIRO:")
    print("="*40)
    print(f"📈 Total de Receitas: R$ {receitas:.2f}")
    print(f"📉 Total de Despesas: R$ {despesas:.2f}")
    print(f"💵 Saldo Atual: R$ {saldo:.2f}")
    
    # Análise por categoria
    print("\\n📊 DESPESAS POR CATEGORIA:")
    categorias = {{}}
    for t in financas:
        if t["tipo"] == "despesa":
            if t["categoria"] not in categorias:
                categorias[t["categoria"]] = 0
            categorias[t["categoria"]] += t["valor"]
    
    for cat, valor in categorias.items():
        print(f"• {cat}: R$ {valor:.2f}")

# === MÓDULO DE CONTATOS ===
def adicionar_contato():
    """Adiciona novo contato"""
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    aniversario = input("Aniversário (dd/mm): ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "aniversario": aniversario
    }
    
    contatos.append(contato)
    return f"✅ Contato {nome} adicionado!"

def buscar_contato(termo):
    """Busca contatos por nome"""
    encontrados = []
    for contato in contatos:
        if termo.lower() in contato["nome"].lower():
            encontrados.append(contato)
    
    if encontrados:
        print(f"\\n🔍 Encontrados {len(encontrados)} contatos:")
        for c in encontrados:
            print(f"👤 {c['nome']}")
            print(f"📞 {c['telefone']} | ✉️ {c['email']}")
    else:
        print("❌ Nenhum contato encontrado")

# === MÓDULO DE METAS ===
def criar_meta():
    """Cria nova meta"""
    titulo = input("Título da meta: ")
    descricao = input("Descrição detalhada: ")
    prazo = input("Prazo para alcançar (dd/mm/aaaa): ")
    
    meta = {
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo,
        "progresso": 0,
        "concluida": False
    }
    
    metas.append(meta)
    return f"🎯 Meta '{titulo}' criada!"

def atualizar_progresso_meta():
    """Atualiza progresso de uma meta"""
    if not metas:
        return "❌ Nenhuma meta cadastrada"
    
    print("\\n🎯 SUAS METAS:")
    for i, meta in enumerate(metas):
        if not meta["concluida"]:
            print(f"{i+1}. {meta['titulo']} - {meta['progresso']}%")
    
    escolha = int(input("\\nEscolha a meta: ")) - 1
    novo_progresso = int(input("Novo progresso (%): "))
    
    metas[escolha]["progresso"] = novo_progresso
    if novo_progresso >= 100:
        metas[escolha]["concluida"] = True
        return f"🎉 PARABÉNS! Meta '{metas[escolha]['titulo']}' concluída!"
    
    return f"✅ Progresso atualizado: {novo_progresso}%"

# === RELATÓRIOS INTEGRADOS ===
def gerar_relatorio_geral():
    """Gera relatório completo do sistema"""
    print("\\n" + "="*60)
    print("📊 RELATÓRIO GERAL DO SISTEMA")
    print("="*60)
    
    # Estatísticas de Tarefas
    total_tarefas = len(tarefas)
    tarefas_concluidas = sum(1 for t in tarefas if t["concluida"])
    tarefas_pendentes = total_tarefas - tarefas_concluidas
    
    print("\\n📝 TAREFAS:")
    print(f"• Total: {total_tarefas}")
    print(f"• Concluídas: {tarefas_concluidas}")
    print(f"• Pendentes: {tarefas_pendentes}")
    
    # Resumo Financeiro
    if financas:
        receitas = sum(t["valor"] for t in financas if t["tipo"] == "receita")
        despesas = sum(t["valor"] for t in financas if t["tipo"] == "despesa")
        print(f"\\n💰 FINANÇAS:")
        print(f"• Saldo: R$ {receitas - despesas:.2f}")
    
    # Contatos
    print(f"\\n📱 CONTATOS: {len(contatos)} cadastrados")
    
    # Metas
    metas_ativas = sum(1 for m in metas if not m["concluida"])
    print(f"\\n🎯 METAS: {metas_ativas} em andamento")

# === DEMONSTRAÇÃO DO SISTEMA ===
print("🎬 DEMONSTRAÇÃO DO SISTEMA DE GESTÃO PESSOAL")

# Adicionando dados de exemplo
print("\\n📝 Adicionando tarefa de exemplo...")
tarefas.append({
    "titulo": "Estudar Python",
    "descricao": "Completar módulo 11",
    "prazo": "31/12/2024",
    "prioridade": "alta",
    "concluida": False,
    "data_criacao": "28/06/2025"
})

print("💰 Adicionando transação de exemplo...")
financas.append({
    "tipo": "receita",
    "categoria": "Salário",
    "valor": 5000.00,
    "descricao": "Pagamento mensal",
    "data": "28/06/2025 10:00"
})

print("📱 Adicionando contato de exemplo...")
contatos.append({
    "nome": "Python Master",
    "telefone": "(11) 98765-4321",
    "email": "python@master.com",
    "aniversario": "01/01"
})

print("🎯 Adicionando meta de exemplo...")
metas.append({
    "titulo": "Dominar Python",
    "descricao": "Completar todos os módulos do curso",
    "prazo": "31/12/2024",
    "progresso": 90,
    "concluida": False
})

# Mostrando o sistema funcionando
exibir_menu_principal()
print("\\n📋 Listando tarefas...")
listar_tarefas()
print("\\n💰 Resumo financeiro...")
resumo_financeiro()
print("\\n📊 Relatório geral...")
gerar_relatorio_geral()

print("\\n🎉 SISTEMA DE GESTÃO PESSOAL COMPLETO!")
print("🏆 PARABÉNS! Você criou um sistema profissional!")'''
            
            self.exemplo(codigo_final)
            
            # === EXECUÇÃO DO RESULTADO ===
            self.print_section("RESULTADO FINAL", "🎬", "warning")
            self.executar_codigo(codigo_final)
            
        except KeyboardInterrupt:
            self.print_warning("Projeto cancelado pelo usuário")
            return
        
        # === MENSAGEM DE CONQUISTA ===
        self.print_success("🎉 PARABÉNS! Você completou o PROJETO FINAL!")
        
        # === ESTATÍSTICAS FINAIS ===
        self.print_section("SUAS CONQUISTAS", "🏆", "info")
        conquistas = [
            "✅ Dominou todos os conceitos básicos de Python",
            "✅ Criou um sistema completo e funcional",
            "✅ Integrou múltiplos módulos em um projeto",
            "✅ Aplicou boas práticas de programação",
            "✅ Desenvolveu pensamento computacional"
        ]
        for conquista in conquistas:
            self.print_colored(f"  {conquista}", "success")
        
        # === PRÓXIMOS PASSOS ===
        self.print_section("PRÓXIMOS PASSOS", "🚀", "accent")
        proximos_passos = [
            "Adicionar persistência de dados (salvar em arquivos)",
            "Criar interface gráfica com Tkinter",
            "Implementar banco de dados SQLite",
            "Adicionar gráficos e visualizações",
            "Transformar em aplicação web"
        ]
        for passo in proximos_passos:
            self.print_colored(f"• {passo}", "primary")
        
        self.print_success("\n🏆 CONQUISTA DESBLOQUEADA: DESENVOLVEDOR PYTHON!")
        
        # === REGISTRO DE CONCLUSÃO ===
        self.complete_mini_project("Sistema de Gestão Pessoal Completo")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo11ProjetoFinal()
    print("Teste do módulo 11 - versão standalone")
    module._projeto_final_interativo()