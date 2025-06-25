#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code Review Dashboard - Interface interativa para análise de código
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from .analysis_engine import CodeAnalysisEngine, IssueType, Severity


class CodeReviewDashboard:
    """Dashboard interativo para code review"""
    
    def __init__(self, analysis_engine: CodeAnalysisEngine, ui_components):
        self.engine = analysis_engine
        self.ui = ui_components
        self.history_file = ".code_review_history.json"
        self.load_history()
        
    def show_main_dashboard(self):
        """Mostra dashboard principal de code review"""
        while True:
            self.ui.clear_screen()
            self.ui.header("🔍 CODE REVIEW DASHBOARD", "Análise Inteligente de Código Python")
            
            # Estatísticas rápidas
            self._display_quick_stats()
            
            print("\n🛠️ ANÁLISE DE CÓDIGO:")
            print("1. 📝 Analisar Código Manual")
            print("2. 📁 Analisar Arquivo Python")
            print("3. 🧪 Exercício com Code Review")
            print("4. 🔄 Comparar Versões")
            
            print("\n📊 RELATÓRIOS:")
            print("5. 📈 Histórico de Qualidade")
            print("6. 🎯 Análise de Melhorias")
            print("7. 📋 Relatório Detalhado")
            print("8. 🏆 Ranking de Códigos")
            
            print("\n⚙️ CONFIGURAÇÕES:")
            print("9. 🎚️ Configurar Análise")
            print("10. 🗑️ Limpar Histórico")
            
            print("\n0. 🔙 Voltar")
            
            choice = input("\n👉 Escolha uma opção: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._analyze_manual_code()
            elif choice == "2":
                self._analyze_file_code()
            elif choice == "3":
                self._exercise_with_review()
            elif choice == "4":
                self._compare_code_versions()
            elif choice == "5":
                self._show_quality_history()
            elif choice == "6":
                self._show_improvement_analysis()
            elif choice == "7":
                self._show_detailed_report()
            elif choice == "8":
                self._show_code_ranking()
            elif choice == "9":
                self._configure_analysis()
            elif choice == "10":
                self._clear_history()
            else:
                self.ui.error("Opção inválida!")
                self.ui.pause()
    
    def _display_quick_stats(self):
        """Exibe estatísticas rápidas"""
        history = self.engine.get_analysis_history()
        
        if not history:
            print("\n📊 ESTATÍSTICAS: Nenhuma análise realizada ainda")
            return
        
        recent_analyses = history[-5:]
        avg_score = sum(a['quality_score']['overall_score'] for a in recent_analyses) / len(recent_analyses)
        total_issues = sum(len(a['issues']) for a in recent_analyses)
        
        print(f"\n📊 ESTATÍSTICAS RÁPIDAS:")
        print(f"  📈 Score médio (últimas 5): {avg_score:.1f}")
        print(f"  🐛 Total de issues: {total_issues}")
        print(f"  🔍 Análises realizadas: {len(history)}")
        
        if recent_analyses:
            best_score = max(a['quality_score']['overall_score'] for a in recent_analyses)
            print(f"  🏆 Melhor score: {best_score:.1f}")
    
    def _analyze_manual_code(self):
        """Análise de código inserido manualmente"""
        self.ui.clear_screen()
        self.ui.header("📝 ANÁLISE MANUAL DE CÓDIGO", "Cole seu código Python para análise")
        
        print("✏️ Digite ou cole seu código Python:")
        print("💡 Digite '###END###' em uma linha vazia para finalizar")
        print("-" * 50)
        
        code_lines = []
        while True:
            try:
                line = input()
                if line.strip() == "###END###":
                    break
                code_lines.append(line)
            except EOFError:
                break
        
        code = '\n'.join(code_lines)
        
        if not code.strip():
            self.ui.warning("Nenhum código fornecido!")
            self.ui.pause()
            return
        
        # Análise
        print("\n🔍 Analisando código...")
        result = self.engine.analyze_code(code, "manual_input.py", "manual")
        
        # Salva no histórico
        self.save_analysis(result)
        
        # Mostra resultado
        self._display_analysis_result(result)
    
    def _analyze_file_code(self):
        """Análise de arquivo Python"""
        self.ui.clear_screen()
        self.ui.header("📁 ANÁLISE DE ARQUIVO", "Analisar arquivo Python existente")
        
        filename = input("\n📂 Nome do arquivo Python (ou caminho): ").strip()
        
        if not filename:
            self.ui.warning("Nome do arquivo não fornecido!")
            self.ui.pause()
            return
        
        # Verifica se arquivo existe
        if not os.path.exists(filename):
            self.ui.error(f"Arquivo '{filename}' não encontrado!")
            self.ui.pause()
            return
        
        # Lê arquivo
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
        except Exception as e:
            self.ui.error(f"Erro ao ler arquivo: {str(e)}")
            self.ui.pause()
            return
        
        # Análise
        print(f"\n🔍 Analisando '{filename}'...")
        result = self.engine.analyze_code(code, filename, "file")
        
        # Salva no histórico
        self.save_analysis(result)
        
        # Mostra resultado
        self._display_analysis_result(result)
    
    def _exercise_with_review(self):
        """Exercício com code review integrado"""
        self.ui.clear_screen()
        self.ui.header("🧪 EXERCÍCIO COM CODE REVIEW", "Prática guiada com análise")
        
        # Exercícios de exemplo
        exercises = [
            {
                "title": "Calculadora Simples",
                "description": "Crie uma função que calcula operações básicas",
                "template": '''def calculadora(a, b, operacao):
    # TODO: Implemente a calculadora
    pass

# Teste sua função
resultado = calculadora(10, 5, "+")
print(resultado)''',
                "expected_features": ["function", "conditional", "return"]
            },
            {
                "title": "Validador de Email",
                "description": "Crie uma função que valida endereços de email",
                "template": '''def validar_email(email):
    # TODO: Implemente validação de email
    pass

# Teste sua função
emails = ["test@example.com", "invalid-email", "user@domain.org"]
for email in emails:
    print(f"{email}: {validar_email(email)}")''',
                "expected_features": ["regex", "validation", "boolean_return"]
            },
            {
                "title": "Contador de Palavras",
                "description": "Conte palavras em um texto",
                "template": '''def contar_palavras(texto):
    # TODO: Implemente contador de palavras
    pass

# Teste sua função
texto = "Python é uma linguagem de programação"
resultado = contar_palavras(texto)
print(resultado)''',
                "expected_features": ["string_processing", "dictionary", "loop"]
            }
        ]
        
        print("🎯 EXERCÍCIOS DISPONÍVEIS:")
        for i, ex in enumerate(exercises, 1):
            print(f"{i}. {ex['title']} - {ex['description']}")
        
        print("0. 🔙 Voltar")
        
        try:
            choice = int(input("\n👉 Escolha um exercício: "))
            if choice == 0:
                return
            if 1 <= choice <= len(exercises):
                exercise = exercises[choice - 1]
                self._run_guided_exercise(exercise)
            else:
                self.ui.error("Exercício inválido!")
                self.ui.pause()
        except ValueError:
            self.ui.error("Entrada inválida!")
            self.ui.pause()
    
    def _run_guided_exercise(self, exercise: Dict[str, Any]):
        """Executa exercício guiado"""
        self.ui.clear_screen()
        self.ui.header(f"🧪 {exercise['title']}", exercise['description'])
        
        print("📋 TEMPLATE INICIAL:")
        print("=" * 50)
        print(exercise['template'])
        print("=" * 50)
        
        print("\n✏️ Implemente sua solução:")
        print("💡 Digite '###END###' para finalizar")
        
        code_lines = []
        while True:
            try:
                line = input()
                if line.strip() == "###END###":
                    break
                code_lines.append(line)
            except EOFError:
                break
        
        user_code = '\n'.join(code_lines)
        
        if not user_code.strip():
            user_code = exercise['template']
        
        # Análise com contexto do exercício
        print("\n🔍 Analisando sua solução...")
        result = self.engine.analyze_code(user_code, f"exercise_{exercise['title']}.py", "exercise")
        
        # Salva no histórico
        self.save_analysis(result)
        
        # Mostra resultado com dicas específicas do exercício
        self._display_exercise_result(result, exercise)
    
    def _compare_code_versions(self):
        """Compara duas versões do código"""
        self.ui.clear_screen()
        self.ui.header("🔄 COMPARAÇÃO DE VERSÕES", "Compare melhorias no código")
        
        print("📝 VERSÃO 1 (código anterior):")
        print("Digite '###NEXT###' para passar à próxima versão")
        
        code1_lines = []
        while True:
            try:
                line = input()
                if line.strip() == "###NEXT###":
                    break
                code1_lines.append(line)
            except EOFError:
                break
        
        print("\n📝 VERSÃO 2 (código melhorado):")
        print("Digite '###END###' para finalizar")
        
        code2_lines = []
        while True:
            try:
                line = input()
                if line.strip() == "###END###":
                    break
                code2_lines.append(line)
            except EOFError:
                break
        
        code1 = '\n'.join(code1_lines)
        code2 = '\n'.join(code2_lines)
        
        if not code1.strip() or not code2.strip():
            self.ui.warning("Ambas as versões devem ser fornecidas!")
            self.ui.pause()
            return
        
        # Análise de ambas as versões
        print("\n🔍 Analisando versões...")
        result1 = self.engine.analyze_code(code1, "version_1.py", "comparison")
        result2 = self.engine.analyze_code(code2, "version_2.py", "comparison")
        
        # Mostra comparação
        self._display_version_comparison(result1, result2)
    
    def _show_quality_history(self):
        """Mostra histórico de qualidade"""
        self.ui.clear_screen()
        self.ui.header("📈 HISTÓRICO DE QUALIDADE", "Evolução dos scores de código")
        
        history = self.engine.get_analysis_history()
        
        if not history:
            print("📊 Nenhuma análise no histórico")
            self.ui.pause()
            return
        
        print("📅 HISTÓRICO DE ANÁLISES:")
        print("-" * 70)
        print(f"{'Data':<19} {'Arquivo':<25} {'Score':<8} {'Grade':<6} {'Issues'}")
        print("-" * 70)
        
        for analysis in history[-15:]:  # Últimas 15
            timestamp = datetime.fromisoformat(analysis['timestamp'])
            filename = analysis['filename'][:24]
            score = analysis['quality_score']['overall_score']
            grade = analysis['quality_score']['grade']
            issues = len(analysis['issues'])
            
            print(f"{timestamp.strftime('%d/%m/%Y %H:%M'):<19} {filename:<25} {score:<8.1f} {grade:<6} {issues}")
        
        # Estatísticas
        scores = [a['quality_score']['overall_score'] for a in history]
        avg_score = sum(scores) / len(scores)
        best_score = max(scores)
        trend = "📈" if len(scores) > 1 and scores[-1] > scores[0] else "📉" if len(scores) > 1 and scores[-1] < scores[0] else "➡️"
        
        print("\n📊 ESTATÍSTICAS:")
        print(f"  📈 Score médio: {avg_score:.1f}")
        print(f"  🏆 Melhor score: {best_score:.1f}")
        print(f"  {trend} Tendência: {'Melhorando' if trend == '📈' else 'Piorando' if trend == '📉' else 'Estável'}")
        
        self.ui.pause()
    
    def _show_improvement_analysis(self):
        """Mostra análise de melhorias"""
        self.ui.clear_screen()
        self.ui.header("🎯 ANÁLISE DE MELHORIAS", "Padrões e sugestões de crescimento")
        
        history = self.engine.get_analysis_history()
        
        if len(history) < 2:
            print("📊 Histórico insuficiente para análise (mín. 2 análises)")
            self.ui.pause()
            return
        
        # Análise de tendências
        recent = history[-5:]
        
        # Issues mais comuns
        all_issues = []
        for analysis in recent:
            all_issues.extend(analysis['issues'])
        
        if not all_issues:
            print("🎉 Nenhum issue encontrado nas análises recentes!")
            self.ui.pause()
            return
        
        # Agrupa por tipo
        issue_types = {}
        for issue in all_issues:
            issue_type = issue['issue_type']
            if issue_type not in issue_types:
                issue_types[issue_type] = []
            issue_types[issue_type].append(issue)
        
        print("🔍 PADRÕES DE ISSUES (últimas 5 análises):")
        print("-" * 50)
        
        for issue_type, issues in sorted(issue_types.items(), key=lambda x: len(x[1]), reverse=True):
            count = len(issues)
            print(f"  📋 {issue_type.upper()}: {count} ocorrências")
            
            # Mostra issues mais comuns deste tipo
            issue_messages = {}
            for issue in issues:
                msg = issue['message']
                issue_messages[msg] = issue_messages.get(msg, 0) + 1
            
            top_issues = sorted(issue_messages.items(), key=lambda x: x[1], reverse=True)[:3]
            for msg, freq in top_issues:
                print(f"    • {msg} ({freq}x)")
        
        # Sugestões de melhoria
        print("\n💡 SUGESTÕES DE MELHORIA:")
        most_common_type = max(issue_types.items(), key=lambda x: len(x[1]))
        
        suggestions = {
            'style': [
                "Use um formatter automático como black ou autopep8",
                "Configure seu editor para mostrar problemas de estilo",
                "Revise as convenções PEP 8"
            ],
            'logic': [
                "Pratique pensamento algorítmico",
                "Use debugging para entender o fluxo do código",
                "Revise padrões de programação Python"
            ],
            'security': [
                "CRÍTICO: Estude práticas de segurança em Python",
                "Nunca use eval() ou exec() com dados não confiáveis",
                "Use variáveis de ambiente para senhas"
            ],
            'maintainability': [
                "Refatore funções grandes em funções menores",
                "Use nomes descritivos para variáveis",
                "Adicione comentários explicativos"
            ],
            'documentation': [
                "Adicione docstrings às suas funções",
                "Documente parâmetros e valores de retorno",
                "Use comentários para lógica complexa"
            ]
        }
        
        if most_common_type[0] in suggestions:
            for suggestion in suggestions[most_common_type[0]]:
                print(f"  • {suggestion}")
        
        self.ui.pause()
    
    def _show_detailed_report(self):
        """Mostra relatório detalhado da última análise"""
        history = self.engine.get_analysis_history()
        
        if not history:
            self.ui.error("Nenhuma análise disponível!")
            self.ui.pause()
            return
        
        latest = history[-1]
        self._display_analysis_result(latest, detailed=True)
    
    def _show_code_ranking(self):
        """Mostra ranking dos melhores códigos"""
        self.ui.clear_screen()
        self.ui.header("🏆 RANKING DE CÓDIGOS", "Seus melhores códigos por qualidade")
        
        history = self.engine.get_analysis_history()
        
        if not history:
            print("📊 Nenhuma análise disponível para ranking")
            self.ui.pause()
            return
        
        # Ordena por score
        ranked = sorted(history, key=lambda x: x['quality_score']['overall_score'], reverse=True)
        
        print("🏆 TOP 10 CÓDIGOS:")
        print("-" * 80)
        print(f"{'#':<3} {'Arquivo':<30} {'Score':<8} {'Grade':<6} {'Data':<12} {'Issues'}")
        print("-" * 80)
        
        for i, analysis in enumerate(ranked[:10], 1):
            timestamp = datetime.fromisoformat(analysis['timestamp'])
            filename = analysis['filename'][:29]
            score = analysis['quality_score']['overall_score']
            grade = analysis['quality_score']['grade']
            date = timestamp.strftime('%d/%m/%Y')
            issues = len(analysis['issues'])
            
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i:2d}"
            
            print(f"{medal:<3} {filename:<30} {score:<8.1f} {grade:<6} {date:<12} {issues}")
        
        self.ui.pause()
    
    def _configure_analysis(self):
        """Configura parâmetros de análise"""
        self.ui.clear_screen()
        self.ui.header("⚙️ CONFIGURAÇÃO DE ANÁLISE", "Personalize os critérios de review")
        
        print("🎚️ CONFIGURAÇÕES DISPONÍVEIS:")
        print("(Funcionalidade em desenvolvimento)")
        print("\nConfiguração futura incluirá:")
        print("• Severidade mínima para alertas")
        print("• Tipos de análise habilitados")
        print("• Regras personalizadas")
        print("• Limites de métricas")
        
        self.ui.pause()
    
    def _clear_history(self):
        """Limpa histórico de análises"""
        confirm = input("\n⚠️ Limpar TODO o histórico? (digite 'CONFIRMAR'): ")
        
        if confirm == "CONFIRMAR":
            self.engine.clear_history()
            if os.path.exists(self.history_file):
                os.remove(self.history_file)
            self.ui.success("✅ Histórico limpo com sucesso!")
        else:
            self.ui.info("❌ Operação cancelada")
        
        self.ui.pause()
    
    def _display_analysis_result(self, result: Dict[str, Any], detailed: bool = False):
        """Exibe resultado da análise"""
        self.ui.clear_screen()
        self.ui.header("🔍 RESULTADO DA ANÁLISE", f"Arquivo: {result['filename']}")
        
        # Erro de sintaxe
        if not result['syntax_valid']:
            self.ui.error("❌ ERRO DE SINTAXE:")
            print(f"  Linha {result['syntax_error']['line']}: {result['syntax_error']['message']}")
            self.ui.pause()
            return
        
        # Score geral
        score = result['quality_score']
        summary = result['summary']
        
        # Header com score
        score_color = "🟢" if score['overall_score'] >= 80 else "🟡" if score['overall_score'] >= 60 else "🔴"
        print(f"\n{score_color} SCORE GERAL: {score['overall_score']}/100 (Grade {score['grade']})")
        
        # Scores por categoria
        print(f"\n📊 SCORES POR CATEGORIA:")
        categories = [
            ("🎨 Estilo", score['style_score']),
            ("🧠 Lógica", score['logic_score']),
            ("🔒 Segurança", score['security_score']),
            ("⚡ Performance", score['performance_score']),
            ("🔧 Manutenibilidade", score['maintainability_score']),
            ("📚 Documentação", score['documentation_score'])
        ]
        
        for name, cat_score in categories:
            bar_length = int(cat_score / 10)
            bar = "█" * bar_length + "░" * (10 - bar_length)
            print(f"  {name:<18} {bar} {cat_score:5.1f}")
        
        # Issues
        issues = result['issues']
        if issues:
            print(f"\n🐛 PROBLEMAS ENCONTRADOS ({len(issues)}):")
            
            # Agrupa por severidade
            by_severity = {}
            for issue in issues:
                sev = issue['severity']
                if sev not in by_severity:
                    by_severity[sev] = []
                by_severity[sev].append(issue)
            
            severity_icons = {
                'critical': '🚨',
                'high': '⚠️',
                'medium': '💛',
                'low': 'ℹ️'
            }
            
            severity_order = ['critical', 'high', 'medium', 'low']
            
            for severity in severity_order:
                if severity in by_severity:
                    sev_issues = by_severity[severity]
                    print(f"\n  {severity_icons[severity]} {severity.upper()} ({len(sev_issues)}):")
                    
                    for issue in sev_issues[:5 if not detailed else None]:  # Limita se não for detalhado
                        print(f"    📍 Linha {issue['line']}: {issue['message']}")
                        print(f"       💡 {issue['suggestion']}")
                    
                    if not detailed and len(sev_issues) > 5:
                        print(f"    ... e mais {len(sev_issues) - 5} issues")
        else:
            print(f"\n✅ NENHUM PROBLEMA ENCONTRADO! Código excelente!")
        
        # Métricas
        metrics = result['metrics']
        print(f"\n📏 MÉTRICAS DO CÓDIGO:")
        print(f"  📄 Linhas de código: {metrics['lines_of_code']}")
        print(f"  🔧 Funções: {metrics['functions']}")
        print(f"  📦 Classes: {metrics['classes']}")
        print(f"  🧮 Complexidade: {metrics['cyclomatic_complexity']}")
        print(f"  📚 Documentação: {metrics['documentation_coverage']:.1%}")
        
        # Sugestões
        suggestions = result['suggestions']
        if suggestions:
            print(f"\n💡 PRINCIPAIS SUGESTÕES:")
            for suggestion in suggestions:
                print(f"  • {suggestion}")
        
        # Tempo de análise
        print(f"\n⏱️ Análise concluída em {result['analysis_time_ms']}ms")
        
        self.ui.pause()
    
    def _display_exercise_result(self, result: Dict[str, Any], exercise: Dict[str, Any]):
        """Exibe resultado específico para exercício"""
        self._display_analysis_result(result)
        
        # Feedback específico do exercício
        print(f"\n🎯 FEEDBACK DO EXERCÍCIO '{exercise['title']}':")
        
        score = result['quality_score']['overall_score']
        if score >= 90:
            print("🌟 EXCELENTE! Seu código está muito bem estruturado!")
        elif score >= 75:
            print("👍 BOM TRABALHO! Apenas pequenos ajustes necessários.")
        elif score >= 60:
            print("📚 CONTINUAR PRATICANDO! Há espaço para melhorias.")
        else:
            print("🎯 FOCO NA PRÁTICA! Revise os conceitos básicos.")
        
        # Verifica se implementou as funcionalidades esperadas
        expected = exercise.get('expected_features', [])
        if expected:
            print(f"\n✅ FUNCIONALIDADES ESPERADAS:")
            for feature in expected:
                print(f"  • {feature}")
            print("  💡 Certifique-se de implementar todas as funcionalidades!")
        
        self.ui.pause()
    
    def _display_version_comparison(self, result1: Dict[str, Any], result2: Dict[str, Any]):
        """Exibe comparação entre versões"""
        self.ui.clear_screen()
        self.ui.header("🔄 COMPARAÇÃO DE VERSÕES", "Análise de melhorias")
        
        score1 = result1['quality_score']['overall_score']
        score2 = result2['quality_score']['overall_score']
        
        diff = score2 - score1
        trend = "📈" if diff > 0 else "📉" if diff < 0 else "➡️"
        
        print(f"\n{trend} COMPARAÇÃO DE SCORES:")
        print(f"  📝 Versão 1: {score1:.1f} ({result1['quality_score']['grade']})")
        print(f"  📝 Versão 2: {score2:.1f} ({result2['quality_score']['grade']})")
        print(f"  📊 Diferença: {diff:+.1f} pontos")
        
        if diff > 0:
            print(f"\n🎉 PARABÉNS! Seu código melhorou {diff:.1f} pontos!")
        elif diff < 0:
            print(f"\n🤔 Houve uma redução de {abs(diff):.1f} pontos. Revise as mudanças.")
        else:
            print(f"\n➡️ Score mantido. Continue refinando!")
        
        # Comparação de issues
        issues1 = len(result1['issues'])
        issues2 = len(result2['issues'])
        
        print(f"\n🐛 ISSUES:")
        print(f"  📝 Versão 1: {issues1} problemas")
        print(f"  📝 Versão 2: {issues2} problemas")
        
        if issues2 < issues1:
            print(f"  ✅ Corrigiu {issues1 - issues2} problemas!")
        elif issues2 > issues1:
            print(f"  ⚠️ Introduziu {issues2 - issues1} novos problemas")
        
        # Análise por categoria
        print(f"\n📊 COMPARAÇÃO POR CATEGORIA:")
        categories = ['style_score', 'logic_score', 'security_score', 'performance_score', 'maintainability_score']
        
        for cat in categories:
            score1_cat = result1['quality_score'][cat]
            score2_cat = result2['quality_score'][cat]
            diff_cat = score2_cat - score1_cat
            
            cat_name = cat.replace('_score', '').title()
            trend_cat = "📈" if diff_cat > 0 else "📉" if diff_cat < 0 else "➡️"
            
            print(f"  {trend_cat} {cat_name}: {score1_cat:.1f} → {score2_cat:.1f} ({diff_cat:+.1f})")
        
        self.ui.pause()
    
    def save_analysis(self, result: Dict[str, Any]):
        """Salva análise no histórico persistente"""
        try:
            history = self.load_history()
            history.append(result)
            
            # Limita histórico a 100 entradas
            if len(history) > 100:
                history = history[-100:]
            
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
    
    def load_history(self) -> List[Dict[str, Any]]:
        """Carrega histórico persistente"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return []