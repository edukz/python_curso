#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exercise Integration - Integração do Code Review com sistema de exercícios
"""

from typing import Dict, List, Any, Optional, Tuple
from .analysis_engine import CodeAnalysisEngine
import json


class ExerciseCodeReviewer:
    """Integra code review com exercícios do curso"""
    
    def __init__(self, analysis_engine: CodeAnalysisEngine, progress_manager):
        self.engine = analysis_engine
        self.progress = progress_manager
        self.exercise_standards = self._load_exercise_standards()
        
    def review_exercise_solution(self, code: str, exercise_id: str, 
                               module_id: str) -> Dict[str, Any]:
        """
        Revisa solução de exercício com contexto específico
        
        Args:
            code: Código do aluno
            exercise_id: ID do exercício
            module_id: ID do módulo
            
        Returns:
            Resultado da análise com feedback específico do exercício
        """
        # Análise padrão
        result = self.engine.analyze_code(
            code, 
            f"{module_id}_{exercise_id}.py", 
            f"exercise_{module_id}"
        )
        
        # Adiciona feedback específico do exercício
        exercise_feedback = self._generate_exercise_feedback(
            result, exercise_id, module_id
        )
        
        # Adiciona ao resultado
        result['exercise_feedback'] = exercise_feedback
        result['learning_points'] = self._calculate_learning_points(result, exercise_id)
        result['next_steps'] = self._suggest_next_steps(result, module_id)
        
        # Atualiza progresso se score for suficiente
        if result['quality_score']['overall_score'] >= 70:
            self._update_exercise_progress(exercise_id, module_id, result)
        
        return result
    
    def review_mini_project(self, code: str, project_id: str) -> Dict[str, Any]:
        """Revisa mini projeto com critérios específicos"""
        result = self.engine.analyze_code(
            code,
            f"mini_project_{project_id}.py",
            "mini_project"
        )
        
        # Feedback específico de projeto
        project_feedback = self._generate_project_feedback(result, project_id)
        
        result['project_feedback'] = project_feedback
        result['project_score'] = self._calculate_project_score(result)
        result['portfolio_ready'] = result['quality_score']['overall_score'] >= 80
        
        return result
    
    def get_exercise_hints(self, code: str, exercise_id: str) -> List[str]:
        """Gera dicas específicas baseadas no código atual"""
        result = self.engine.analyze_code(code, "hint_analysis.py", "hint")
        
        hints = []
        
        # Dicas baseadas em issues
        critical_issues = [i for i in result['issues'] if i['severity'] == 'critical']
        if critical_issues:
            hints.append("🚨 Há problemas críticos que impedem a execução segura")
        
        # Dicas baseadas no exercício específico
        exercise_hints = self._get_exercise_specific_hints(result, exercise_id)
        hints.extend(exercise_hints)
        
        # Dicas gerais de melhoria
        if result['quality_score']['style_score'] < 70:
            hints.append("💡 Revise a formatação do código (espaços, linhas)")
        
        if result['quality_score']['logic_score'] < 70:
            hints.append("🧠 Verifique a lógica do seu algoritmo")
        
        if len(result['issues']) > 10:
            hints.append("🔧 Muitos issues detectados - foque nas correções mais importantes")
        
        return hints[:5]  # Máximo 5 dicas
    
    def analyze_learning_progress(self, student_id: str) -> Dict[str, Any]:
        """Analisa progresso de aprendizagem via code review"""
        history = self.engine.get_analysis_history()
        
        # Filtra análises do estudante (por contexto de exercício)
        student_analyses = [
            a for a in history 
            if a['context'].startswith('exercise_') or a['context'] == 'manual'
        ]
        
        if not student_analyses:
            return {"error": "Nenhuma análise encontrada"}
        
        # Análise de progresso
        scores_over_time = [a['quality_score']['overall_score'] for a in student_analyses]
        
        # Tendência
        if len(scores_over_time) >= 3:
            recent_avg = sum(scores_over_time[-3:]) / 3
            early_avg = sum(scores_over_time[:3]) / 3
            improvement = recent_avg - early_avg
        else:
            improvement = 0
        
        # Áreas de força e fraqueza
        category_scores = {
            'style': [],
            'logic': [],
            'security': [],
            'performance': [],
            'maintainability': [],
            'documentation': []
        }
        
        for analysis in student_analyses[-10:]:  # Últimas 10
            scores = analysis['quality_score']
            category_scores['style'].append(scores['style_score'])
            category_scores['logic'].append(scores['logic_score'])
            category_scores['security'].append(scores['security_score'])
            category_scores['performance'].append(scores['performance_score'])
            category_scores['maintainability'].append(scores['maintainability_score'])
            category_scores['documentation'].append(scores['documentation_score'])
        
        # Médias por categoria
        category_averages = {
            cat: sum(scores) / len(scores) if scores else 0
            for cat, scores in category_scores.items()
        }
        
        # Identifica pontos fortes e fracos
        strengths = [cat for cat, avg in category_averages.items() if avg >= 80]
        weaknesses = [cat for cat, avg in category_averages.items() if avg < 60]
        
        return {
            "total_analyses": len(student_analyses),
            "latest_score": scores_over_time[-1] if scores_over_time else 0,
            "improvement": improvement,
            "trend": "📈" if improvement > 5 else "📉" if improvement < -5 else "➡️",
            "category_averages": category_averages,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "learning_recommendations": self._generate_learning_recommendations(
                category_averages, weaknesses
            )
        }
    
    def _generate_exercise_feedback(self, result: Dict[str, Any], 
                                  exercise_id: str, module_id: str) -> Dict[str, Any]:
        """Gera feedback específico do exercício"""
        feedback = {
            "exercise_id": exercise_id,
            "module_id": module_id,
            "completion_status": "completed" if result['quality_score']['overall_score'] >= 70 else "needs_improvement",
            "specific_comments": [],
            "learning_objectives_met": [],
            "areas_to_improve": []
        }
        
        # Comentários específicos baseados no módulo
        module_feedback = {
            "modulo_1": self._feedback_modulo_1,
            "modulo_2": self._feedback_modulo_2,
            "modulo_3": self._feedback_modulo_3,
            "modulo_4": self._feedback_modulo_4,
            "modulo_7": self._feedback_modulo_7,
            "modulo_8": self._feedback_modulo_8,
            "modulo_9": self._feedback_modulo_9,
            "modulo_10": self._feedback_modulo_10
        }
        
        if module_id in module_feedback:
            module_specific = module_feedback[module_id](result)
            feedback.update(module_specific)
        
        return feedback
    
    def _feedback_modulo_1(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 1 (Introdução)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica se usou print()
        code_lines = result.get('code', '').lower()
        if 'print(' in code_lines:
            objectives_met.append("✅ Uso correto da função print()")
        else:
            improvements.append("📝 Pratique o uso da função print() para saída")
        
        # Verifica comentários
        if result['metrics']['comment_lines'] > 0:
            objectives_met.append("✅ Incluiu comentários no código")
            comments.append("💬 Bom uso de comentários!")
        else:
            improvements.append("💬 Adicione comentários explicativos ao código")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    def _feedback_modulo_3(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 3 (Variáveis)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica naming de variáveis
        naming_issues = [i for i in result['issues'] if i['issue_type'] == 'naming']
        if not naming_issues:
            objectives_met.append("✅ Nomes de variáveis seguem convenções")
        else:
            improvements.append("📝 Melhore os nomes das variáveis (use snake_case)")
        
        # Verifica se há variáveis não utilizadas
        unused_vars = [i for i in result['issues'] if 'never used' in i['message']]
        if unused_vars:
            improvements.append("🧹 Remova variáveis não utilizadas")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    def _feedback_modulo_7(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 7 (Condições)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica uso de condicionais
        issues = result['issues']
        
        # Verifica comparações com True/False
        bool_comparison_issues = [i for i in issues if 'comparison with' in i['message'] and ('True' in i['message'] or 'False' in i['message'])]
        if bool_comparison_issues:
            improvements.append("🔄 Use valores booleanos diretamente (sem comparar com True/False)")
        
        # Verifica comparações com None
        none_comparison_issues = [i for i in issues if 'None comparison' in i['message']]
        if none_comparison_issues:
            improvements.append("🔄 Use 'is' ou 'is not' para comparar com None")
        else:
            objectives_met.append("✅ Comparações com None corretas")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    def _feedback_modulo_8(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 8 (Loops)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica eficiência de loops
        performance_issues = [i for i in result['issues'] if i['issue_type'] == 'performance']
        if performance_issues:
            improvements.append("⚡ Otimize loops para melhor performance")
        
        # Verifica complexidade
        if result['metrics']['cyclomatic_complexity'] > 8:
            improvements.append("🧠 Simplifique a lógica dos loops")
        else:
            objectives_met.append("✅ Complexidade dos loops adequada")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    def _feedback_modulo_9(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 9 (Listas)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica uso eficiente de listas
        performance_issues = [i for i in result['issues'] if 'list comprehension' in i['message']]
        if performance_issues:
            improvements.append("📋 Use list comprehensions quando apropriado")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    def _feedback_modulo_10(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Feedback específico para módulo 10 (Funções)"""
        comments = []
        objectives_met = []
        improvements = []
        
        # Verifica se há funções
        if result['metrics']['functions'] > 0:
            objectives_met.append("✅ Código organizado em funções")
        else:
            improvements.append("🔧 Organize o código em funções")
        
        # Verifica documentação de funções
        doc_issues = [i for i in result['issues'] if i['issue_type'] == 'documentation' and 'function' in i['message'].lower()]
        if doc_issues:
            improvements.append("📚 Adicione docstrings às funções")
        
        # Verifica tamanho das funções
        long_function_issues = [i for i in result['issues'] if 'too long' in i['message']]
        if long_function_issues:
            improvements.append("✂️ Divida funções grandes em funções menores")
        
        return {
            "specific_comments": comments,
            "learning_objectives_met": objectives_met,
            "areas_to_improve": improvements
        }
    
    # Placeholders para outros módulos
    def _feedback_modulo_2(self, result): return {"specific_comments": [], "learning_objectives_met": [], "areas_to_improve": []}
    def _feedback_modulo_4(self, result): return {"specific_comments": [], "learning_objectives_met": [], "areas_to_improve": []}
    
    def _generate_project_feedback(self, result: Dict[str, Any], project_id: str) -> Dict[str, Any]:
        """Gera feedback específico para mini projeto"""
        feedback = {
            "project_id": project_id,
            "readiness_level": self._assess_project_readiness(result),
            "professional_aspects": [],
            "improvement_suggestions": [],
            "portfolio_recommendations": []
        }
        
        score = result['quality_score']['overall_score']
        
        # Avaliação profissional
        if score >= 90:
            feedback["professional_aspects"].append("🌟 Código de qualidade profissional")
        elif score >= 80:
            feedback["professional_aspects"].append("👍 Código bom para portfólio")
        elif score >= 70:
            feedback["professional_aspects"].append("📚 Código funcional, mas precisa refinamento")
        
        # Sugestões de melhoria
        if result['quality_score']['documentation_score'] < 70:
            feedback["improvement_suggestions"].append("📖 Melhore a documentação para uso profissional")
        
        if result['quality_score']['security_score'] < 80:
            feedback["improvement_suggestions"].append("🔒 Corrija problemas de segurança")
        
        # Recomendações de portfólio
        if score >= 80:
            feedback["portfolio_recommendations"].append("✅ Pronto para incluir no portfólio")
        else:
            feedback["portfolio_recommendations"].append("🔧 Refine antes de incluir no portfólio")
        
        return feedback
    
    def _assess_project_readiness(self, result: Dict[str, Any]) -> str:
        """Avalia prontidão do projeto"""
        score = result['quality_score']['overall_score']
        critical_issues = len([i for i in result['issues'] if i['severity'] == 'critical'])
        
        if critical_issues > 0:
            return "not_ready"
        elif score >= 85:
            return "production_ready"
        elif score >= 70:
            return "portfolio_ready"
        else:
            return "needs_improvement"
    
    def _calculate_learning_points(self, result: Dict[str, Any], exercise_id: str) -> int:
        """Calcula pontos de aprendizado baseados na qualidade"""
        base_points = 100
        score = result['quality_score']['overall_score']
        
        # Multiplicador baseado no score
        multiplier = score / 100
        
        # Bônus por não ter issues críticos
        critical_issues = len([i for i in result['issues'] if i['severity'] == 'critical'])
        if critical_issues == 0:
            multiplier += 0.1
        
        # Bônus por boa documentação
        if result['quality_score']['documentation_score'] > 80:
            multiplier += 0.05
        
        return int(base_points * multiplier)
    
    def _suggest_next_steps(self, result: Dict[str, Any], module_id: str) -> List[str]:
        """Sugere próximos passos de aprendizado"""
        steps = []
        
        # Baseado na qualidade geral
        score = result['quality_score']['overall_score']
        
        if score >= 85:
            steps.append("🎯 Tente exercícios mais avançados")
            steps.append("🚀 Considere contribuir para projetos open source")
        elif score >= 70:
            steps.append("📚 Revise conceitos específicos com issues")
            steps.append("🔄 Refatore o código aplicando as sugestões")
        else:
            steps.append("📖 Revise a teoria do módulo")
            steps.append("💪 Pratique exercícios básicos antes de avançar")
        
        # Baseado em issues específicos
        security_issues = [i for i in result['issues'] if i['issue_type'] == 'security']
        if security_issues:
            steps.append("🔒 URGENTE: Estude práticas de segurança em Python")
        
        return steps
    
    def _get_exercise_specific_hints(self, result: Dict[str, Any], exercise_id: str) -> List[str]:
        """Gera dicas específicas do exercício"""
        hints = []
        
        # Dicas baseadas no ID do exercício (exemplos)
        if "calculadora" in exercise_id.lower():
            if result['metrics']['functions'] == 0:
                hints.append("💡 Organize o código em funções para cada operação")
            
            if any("eval" in str(issue) for issue in result['issues']):
                hints.append("⚠️ Evite usar eval() - implemente as operações diretamente")
        
        elif "email" in exercise_id.lower():
            if not any("import re" in str(result) for result in [result]):
                hints.append("📧 Considere usar regex para validar emails")
        
        elif "palavra" in exercise_id.lower():
            performance_issues = [i for i in result['issues'] if i['issue_type'] == 'performance']
            if performance_issues:
                hints.append("⚡ Use métodos eficientes para processar texto")
        
        return hints
    
    def _generate_learning_recommendations(self, category_averages: Dict[str, float], 
                                         weaknesses: List[str]) -> List[str]:
        """Gera recomendações de aprendizado personalizadas"""
        recommendations = []
        
        for weakness in weaknesses:
            if weakness == 'style':
                recommendations.append("📏 Estude PEP 8 e use ferramentas de formatação")
            elif weakness == 'logic':
                recommendations.append("🧠 Pratique algoritmos e lógica de programação")
            elif weakness == 'security':
                recommendations.append("🔒 Estude segurança em Python - é fundamental!")
            elif weakness == 'performance':
                recommendations.append("⚡ Aprenda sobre otimização e estruturas de dados")
            elif weakness == 'maintainability':
                recommendations.append("🔧 Foque em código limpo e refatoração")
            elif weakness == 'documentation':
                recommendations.append("📚 Pratique escrever docstrings e comentários")
        
        return recommendations
    
    def _update_exercise_progress(self, exercise_id: str, module_id: str, result: Dict[str, Any]):
        """Atualiza progresso do exercício no sistema"""
        if hasattr(self.progress, 'update_exercise_quality'):
            quality_data = {
                'exercise_id': exercise_id,
                'module_id': module_id,
                'score': result['quality_score']['overall_score'],
                'grade': result['quality_score']['grade'],
                'issues_count': len(result['issues']),
                'analysis_timestamp': result['timestamp']
            }
            self.progress.update_exercise_quality(quality_data)
    
    def _load_exercise_standards(self) -> Dict[str, Any]:
        """Carrega padrões específicos por exercício"""
        return {
            "default": {
                "min_score": 70,
                "max_complexity": 10,
                "require_functions": False,
                "require_docstrings": False
            },
            "modulo_10": {  # Funções
                "min_score": 75,
                "max_complexity": 8,
                "require_functions": True,
                "require_docstrings": True
            }
        }