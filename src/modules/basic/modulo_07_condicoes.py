#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 7: Estruturas Condicionais (if/else)
Aprenda a tomar decisões nos seus programas
"""

from ..shared.base_module import BaseModule


class Modulo07Condicoes(BaseModule):
    """Módulo 7: Tomando Decisões (if/else)"""
    
    def __init__(self):
        super().__init__("modulo_7", "Estruturas Condicionais")
        self.has_mini_project = True
        self.mini_project_points = 60
    
    def execute(self) -> None:
        """Executa o módulo sobre condições"""
        if not self.ui or not self.progress:
            print("❌ Erro: Dependências não configuradas para este módulo")
            input("Pressione ENTER para continuar...")
            return
        
        try:
            self._condicoes()
        except Exception as e:
            self.error_handler(lambda: None)
    
    def _condicoes(self) -> None:
        """Conteúdo principal sobre condições"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🤔 MÓDULO 7: TOMANDO DECISÕES (IF/ELSE)")
        else:
            print("\n" + "="*50)
            print("🤔 MÓDULO 7: TOMANDO DECISÕES (IF/ELSE)")
            print("="*50)
        
        print("Programas precisam tomar decisões!")
        
        codigo = '''idade = 18

if idade >= 18:
    print("Você é maior de idade! 🎉")
    print("Pode tirar carteira de motorista")
else:
    print("Você é menor de idade")
    print(f"Faltam {18 - idade} anos para a maioridade")'''
        
        self.exemplo(codigo)
        self.executar_codigo(codigo)
        
        print("\n📌 Operadores de comparação:")
        print("• == (igual)")
        print("• != (diferente)")
        print("• > (maior)")
        print("• < (menor)")
        print("• >= (maior ou igual)")
        print("• <= (menor ou igual)")
        
        # Mini Projeto do Módulo 7
        self._mini_projeto_classificacao()
        
        # Marcar módulo como completo
        self.complete_module()
        
        self.pausar()
    
    def _mini_projeto_classificacao(self) -> None:
        """Mini Projeto - Sistema de Classificação Inteligente"""
        if self.ui:
            self.ui.clear_screen()
            self.ui.header("🎯 MINI PROJETO: SISTEMA DE CLASSIFICAÇÃO INTELIGENTE")
        else:
            print("\n" + "="*50)
            print("🎯 MINI PROJETO: SISTEMA DE CLASSIFICAÇÃO INTELIGENTE")
            print("="*50)
        
        print("🧠 Vamos criar um sistema que toma decisões baseadas em condições!")
        print("💼 Tipo de sistema usado em:")
        print("• Sistema de aprovação de crédito")
        print("• Classificação de produtos")
        print("• Sistemas de recomendação")
        print("• Diagnósticos automatizados")
        
        self.pausar()
        
        print("\n📝 PROJETO: Sistema de Avaliação de Candidatos")
        
        codigo_projeto = '''# 🎯 SISTEMA DE CLASSIFICAÇÃO INTELIGENTE
# Sistema de Avaliação de Candidatos para Vaga

print("🏢 SISTEMA DE AVALIAÇÃO DE CANDIDATOS")
print("=" * 50)

def avaliar_candidato(nome, idade, experiencia, formacao, nota_teste):
    """Avalia candidato baseado em critérios definidos"""
    print(f"\\n👤 Avaliando: {nome}")
    print("-" * 30)
    
    pontuacao = 0
    criterios_atendidos = []
    
    # Critério 1: Idade
    if 18 <= idade <= 65:
        pontuacao += 20
        criterios_atendidos.append("✅ Idade adequada")
    else:
        criterios_atendidos.append("❌ Idade fora do range")
    
    # Critério 2: Experiência
    if experiencia >= 3:
        pontuacao += 30
        criterios_atendidos.append("✅ Experiência suficiente")
    elif experiencia >= 1:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Experiência limitada")
    else:
        criterios_atendidos.append("❌ Sem experiência")
    
    # Critério 3: Formação
    if formacao.lower() in ["superior", "universitario", "faculdade"]:
        pontuacao += 25
        criterios_atendidos.append("✅ Formação superior")
    elif formacao.lower() in ["tecnico", "técnico"]:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Formação técnica")
    else:
        pontuacao += 5
        criterios_atendidos.append("⚠️ Formação básica")
    
    # Critério 4: Nota do teste
    if nota_teste >= 8:
        pontuacao += 25
        criterios_atendidos.append("✅ Excelente no teste")
    elif nota_teste >= 6:
        pontuacao += 15
        criterios_atendidos.append("⚠️ Bom no teste")
    else:
        criterios_atendidos.append("❌ Nota baixa no teste")
    
    # Exibe avaliação detalhada
    print("📊 CRITÉRIOS AVALIADOS:")
    for criterio in criterios_atendidos:
        print(f"  {criterio}")
    
    print(f"\\n🏆 PONTUAÇÃO TOTAL: {pontuacao}/100")
    
    # Decisão final
    if pontuacao >= 80:
        status = "APROVADO - EXCELENTE CANDIDATO"
        emoji = "🌟"
    elif pontuacao >= 60:
        status = "APROVADO - BOM CANDIDATO"
        emoji = "✅"
    elif pontuacao >= 40:
        status = "EM ANÁLISE - CANDIDATO RAZOÁVEL"
        emoji = "⚠️"
    else:
        status = "REPROVADO - NÃO ATENDE CRITÉRIOS"
        emoji = "❌"
    
    print(f"\\n{emoji} RESULTADO: {status}")
    return pontuacao, status

# Testando o sistema com candidatos
print("\\n🧪 TESTANDO O SISTEMA:")

# Candidato 1: Perfil Excelente
print("\\n" + "="*50)
pontos1, resultado1 = avaliar_candidato(
    "Ana Silva", 28, 5, "Superior", 9.2
)

# Candidato 2: Perfil Médio
print("\\n" + "="*50)
pontos2, resultado2 = avaliar_candidato(
    "Carlos Santos", 22, 1, "Técnico", 7.0
)

# Relatório final
print("\\n" + "="*60)
print("📊 RELATÓRIO FINAL DE AVALIAÇÕES")
print("="*60)
print(f"Ana Silva: {pontos1} pontos - {resultado1.split(' - ')[0]}")
print(f"Carlos Santos: {pontos2} pontos - {resultado2.split(' - ')[0]}")

print("\\n🎯 SISTEMA FUNCIONANDO PERFEITAMENTE!")'''
        
        self.exemplo(codigo_projeto)
        self.executar_codigo(codigo_projeto)
        
        print("\n🏆 PARABÉNS! Sistema de Classificação Inteligente criado!")
        print("🎯 Aplicação real: RH, sistemas de aprovação, classificadores automáticos")
        
        # Registra conclusão do mini projeto
        self.complete_mini_project("Sistema de Classificação Inteligente")
        
        self.pausar()


# Para teste standalone
if __name__ == "__main__":
    module = Modulo07Condicoes()
    print("Teste do módulo 7 - versão standalone")
    module._condicoes()