#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code Analysis Engine - Sistema de análise de código Python
Análise estática sem dependência de LLM externa
"""

import ast
import re
import keyword
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime
import json
import os


class IssueType(Enum):
    """Tipos de problemas de código"""
    STYLE = "style"
    LOGIC = "logic"
    SECURITY = "security"
    PERFORMANCE = "performance"
    MAINTAINABILITY = "maintainability"
    NAMING = "naming"
    DOCUMENTATION = "documentation"


class Severity(Enum):
    """Severidade dos problemas"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class CodeIssue:
    """Representa um problema encontrado no código"""
    line: int
    column: int
    issue_type: IssueType
    severity: Severity
    message: str
    suggestion: str
    rule_id: str
    code_snippet: Optional[str] = None


@dataclass
class CodeMetrics:
    """Métricas do código analisado"""
    lines_of_code: int
    blank_lines: int
    comment_lines: int
    functions: int
    classes: int
    imports: int
    cyclomatic_complexity: int
    maintainability_index: float
    documentation_coverage: float


@dataclass
class QualityScore:
    """Score de qualidade do código"""
    overall_score: float
    grade: str
    style_score: float
    logic_score: float
    security_score: float
    performance_score: float
    maintainability_score: float
    documentation_score: float


class CodeAnalysisEngine:
    """Engine principal de análise de código"""
    
    def __init__(self):
        self.rules = self._load_analysis_rules()
        self.analysis_history = []
        
    def analyze_code(self, code: str, filename: str = "user_code.py", 
                    context: str = "exercise") -> Dict[str, Any]:
        """
        Analisa código Python completo
        
        Args:
            code: Código Python para análise
            filename: Nome do arquivo (para contexto)
            context: Contexto da análise (exercise, project, etc.)
            
        Returns:
            Resultado completo da análise
        """
        analysis_start = datetime.now()
        
        # Validação básica
        if not code.strip():
            return self._empty_analysis_result()
        
        # Parse do AST
        try:
            tree = ast.parse(code)
            syntax_valid = True
            syntax_error = None
        except SyntaxError as e:
            return self._syntax_error_result(str(e), e.lineno or 1)
        
        # Executa todas as análises
        issues = []
        issues.extend(self._analyze_style(code))
        issues.extend(self._analyze_logic(tree, code))
        issues.extend(self._analyze_security(tree, code))
        issues.extend(self._analyze_performance(tree, code))
        issues.extend(self._analyze_maintainability(tree, code))
        issues.extend(self._analyze_naming(tree, code))
        issues.extend(self._analyze_documentation(tree, code))
        
        # Calcula métricas
        metrics = self._calculate_metrics(tree, code)
        
        # Calcula scores
        quality_score = self._calculate_quality_score(issues, metrics, code)
        
        # Gera sugestões
        suggestions = self._generate_improvement_suggestions(issues, metrics)
        
        # Monta resultado
        result = {
            "timestamp": analysis_start.isoformat(),
            "filename": filename,
            "context": context,
            "syntax_valid": syntax_valid,
            "syntax_error": syntax_error,
            "issues": [asdict(issue) for issue in issues],
            "metrics": asdict(metrics),
            "quality_score": asdict(quality_score),
            "suggestions": suggestions,
            "summary": self._generate_summary(issues, quality_score),
            "analysis_time_ms": int((datetime.now() - analysis_start).total_seconds() * 1000)
        }
        
        # Salva no histórico
        self.analysis_history.append(result)
        
        return result
    
    def _analyze_style(self, code: str) -> List[CodeIssue]:
        """Análise de estilo (PEP 8 e convenções)"""
        issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            original_line = line
            line_stripped = line.strip()
            
            # Linha muito longa
            if len(line) > 79:
                issues.append(CodeIssue(
                    line=i, column=80,
                    issue_type=IssueType.STYLE,
                    severity=Severity.LOW,
                    message=f"Line too long ({len(line)} > 79 characters)",
                    suggestion="Break line using parentheses or backslash",
                    rule_id="E501",
                    code_snippet=line[:50] + "..." if len(line) > 50 else line
                ))
            
            # Trailing whitespace
            if original_line != original_line.rstrip():
                issues.append(CodeIssue(
                    line=i, column=len(original_line.rstrip()) + 1,
                    issue_type=IssueType.STYLE,
                    severity=Severity.LOW,
                    message="Trailing whitespace",
                    suggestion="Remove trailing spaces and tabs",
                    rule_id="W291"
                ))
            
            # Tabs e espaços misturados
            if '\t' in original_line and '    ' in original_line:
                issues.append(CodeIssue(
                    line=i, column=1,
                    issue_type=IssueType.STYLE,
                    severity=Severity.MEDIUM,
                    message="Mixed tabs and spaces in indentation",
                    suggestion="Use only spaces (4 spaces per indentation level)",
                    rule_id="E101"
                ))
            
            # Múltiplas linhas em branco consecutivas
            if i > 1 and not line_stripped and not lines[i-2].strip():
                issues.append(CodeIssue(
                    line=i, column=1,
                    issue_type=IssueType.STYLE,
                    severity=Severity.LOW,
                    message="Too many blank lines",
                    suggestion="Use maximum 2 consecutive blank lines",
                    rule_id="E303"
                ))
            
            # Espaços ao redor de operadores
            if '=' in line_stripped and not line_stripped.lstrip().startswith('#'):
                # Verifica assignment sem espaços
                if re.search(r'\w=[^=]', line_stripped) or re.search(r'[^=!<>]=\w', line_stripped):
                    issues.append(CodeIssue(
                        line=i, column=line.find('=') + 1,
                        issue_type=IssueType.STYLE,
                        severity=Severity.LOW,
                        message="Missing whitespace around operator",
                        suggestion="Add spaces around = operator",
                        rule_id="E225"
                    ))
        
        return issues
    
    def _analyze_logic(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de lógica e boas práticas"""
        issues = []
        
        for node in ast.walk(tree):
            # Funções muito longas
            if isinstance(node, ast.FunctionDef):
                func_lines = (node.end_lineno or node.lineno) - node.lineno + 1
                if func_lines > 50:
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.MAINTAINABILITY,
                        severity=Severity.MEDIUM,
                        message=f"Function '{node.name}' is too long ({func_lines} lines)",
                        suggestion="Break into smaller, focused functions",
                        rule_id="C901"
                    ))
                
                # Muitos parâmetros
                if len(node.args.args) > 7:
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.MAINTAINABILITY,
                        severity=Severity.MEDIUM,
                        message=f"Function '{node.name}' has too many parameters ({len(node.args.args)})",
                        suggestion="Consider using a config object or reducing parameters",
                        rule_id="C902"
                    ))
            
            # Comparação com None usando ==
            if isinstance(node, ast.Compare):
                for i, comparator in enumerate(node.comparators):
                    if isinstance(comparator, ast.Constant) and comparator.value is None:
                        op = node.ops[i]
                        if isinstance(op, (ast.Eq, ast.NotEq)):
                            op_str = "==" if isinstance(op, ast.Eq) else "!="
                            replacement = "is" if isinstance(op, ast.Eq) else "is not"
                            issues.append(CodeIssue(
                                line=node.lineno, column=node.col_offset,
                                issue_type=IssueType.LOGIC,
                                severity=Severity.MEDIUM,
                                message=f"Use '{replacement}' instead of '{op_str}' for None comparison",
                                suggestion=f"Replace '{op_str} None' with '{replacement} None'",
                                rule_id="E711"
                            ))
                
                # Comparação com True/False
                for i, comparator in enumerate(node.comparators):
                    if isinstance(comparator, ast.Constant) and isinstance(comparator.value, bool):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.LOGIC,
                            severity=Severity.LOW,
                            message=f"Avoid explicit comparison with {comparator.value}",
                            suggestion="Use the boolean value directly",
                            rule_id="E712"
                        ))
            
            # Argumentos padrão mutáveis
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.LOGIC,
                            severity=Severity.HIGH,
                            message="Mutable default argument",
                            suggestion="Use None as default and create object inside function",
                            rule_id="B006"
                        ))
            
            # Exception catching muito amplo
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.LOGIC,
                        severity=Severity.MEDIUM,
                        message="Bare except clause",
                        suggestion="Catch specific exceptions instead of using bare except",
                        rule_id="E722"
                    ))
                elif isinstance(node.type, ast.Name) and node.type.id == "Exception":
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.LOGIC,
                        severity=Severity.LOW,
                        message="Too broad exception clause",
                        suggestion="Catch more specific exceptions when possible",
                        rule_id="B902"
                    ))
        
        return issues
    
    def _analyze_security(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de segurança"""
        issues = []
        
        for node in ast.walk(tree):
            # Uso de eval()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == 'eval':
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.SECURITY,
                        severity=Severity.CRITICAL,
                        message="Use of eval() is dangerous",
                        suggestion="Use ast.literal_eval() for safe evaluation of literals",
                        rule_id="S307"
                    ))
                
                # Uso de exec()
                elif node.func.id == 'exec':
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.SECURITY,
                        severity=Severity.CRITICAL,
                        message="Use of exec() is dangerous",
                        suggestion="Avoid dynamic code execution",
                        rule_id="S102"
                    ))
                
                # Subprocess sem shell=False
                elif node.func.id in ['subprocess', 'os.system', 'os.popen']:
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.SECURITY,
                        severity=Severity.HIGH,
                        message="Potentially unsafe subprocess call",
                        suggestion="Use subprocess with shell=False and validate inputs",
                        rule_id="S602"
                    ))
            
            # Hardcoded secrets
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id.lower()
                        sensitive_words = ['password', 'secret', 'key', 'token', 'api_key', 'auth']
                        if any(word in var_name for word in sensitive_words):
                            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                if len(node.value.value) > 3:  # Ignore placeholder values
                                    issues.append(CodeIssue(
                                        line=node.lineno, column=node.col_offset,
                                        issue_type=IssueType.SECURITY,
                                        severity=Severity.HIGH,
                                        message=f"Hardcoded {var_name.replace('_', ' ')} detected",
                                        suggestion="Use environment variables or secure config files",
                                        rule_id="S105"
                                    ))
            
            # SQL string concatenation
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                if isinstance(node.left, ast.Constant) and isinstance(node.left.value, str):
                    if any(keyword in node.left.value.upper() for keyword in ['SELECT', 'INSERT', 'UPDATE', 'DELETE']):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.SECURITY,
                            severity=Severity.HIGH,
                            message="Potential SQL injection vulnerability",
                            suggestion="Use parameterized queries instead of string concatenation",
                            rule_id="S608"
                        ))
        
        return issues
    
    def _analyze_performance(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de performance"""
        issues = []
        
        for node in ast.walk(tree):
            # String concatenation em loops
            if isinstance(node, (ast.For, ast.While)):
                for child in ast.walk(node):
                    if isinstance(child, ast.AugAssign) and isinstance(child.op, ast.Add):
                        if isinstance(child.target, ast.Name):
                            issues.append(CodeIssue(
                                line=child.lineno, column=child.col_offset,
                                issue_type=IssueType.PERFORMANCE,
                                severity=Severity.MEDIUM,
                                message="String concatenation in loop is inefficient",
                                suggestion="Use join() method or list comprehension",
                                rule_id="P101"
                            ))
            
            # List comprehension desnecessária para contagem
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == 'len':
                    if len(node.args) == 1 and isinstance(node.args[0], ast.ListComp):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.PERFORMANCE,
                            severity=Severity.LOW,
                            message="Inefficient list comprehension for counting",
                            suggestion="Use sum() with generator expression instead",
                            rule_id="P102"
                        ))
            
            # Uso de keys() desnecessário
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr == 'keys':
                    # Verifica se está sendo usado em 'in' ou loop
                    parent = getattr(node, 'parent', None)
                    if isinstance(parent, (ast.Compare, ast.For)):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.PERFORMANCE,
                            severity=Severity.LOW,
                            message="Unnecessary use of .keys()",
                            suggestion="Iterate over dictionary directly",
                            rule_id="P103"
                        ))
        
        return issues
    
    def _analyze_maintainability(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de manutenibilidade"""
        issues = []
        
        # Complexidade ciclomática
        complexity = self._calculate_cyclomatic_complexity(tree)
        if complexity > 10:
            issues.append(CodeIssue(
                line=1, column=1,
                issue_type=IssueType.MAINTAINABILITY,
                severity=Severity.HIGH,
                message=f"High cyclomatic complexity ({complexity})",
                suggestion="Break down complex logic into smaller functions",
                rule_id="C901"
            ))
        
        # Nesting muito profundo
        max_nesting = self._calculate_max_nesting(tree)
        if max_nesting > 4:
            issues.append(CodeIssue(
                line=1, column=1,
                issue_type=IssueType.MAINTAINABILITY,
                severity=Severity.MEDIUM,
                message=f"Deep nesting detected ({max_nesting} levels)",
                suggestion="Reduce nesting using early returns or helper functions",
                rule_id="C902"
            ))
        
        # Duplicação de código (strings literais repetidas)
        string_constants = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if len(node.value) > 10:  # Apenas strings longas
                    string_constants.append((node.value, node.lineno))
        
        # Verifica duplicações
        seen = {}
        for value, line in string_constants:
            if value in seen:
                issues.append(CodeIssue(
                    line=line, column=1,
                    issue_type=IssueType.MAINTAINABILITY,
                    severity=Severity.LOW,
                    message="Duplicated string literal",
                    suggestion="Consider using a constant or configuration",
                    rule_id="C903"
                ))
            seen[value] = line
        
        return issues
    
    def _analyze_naming(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de convenções de nomenclatura"""
        issues = []
        
        for node in ast.walk(tree):
            # Nomes de funções
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.NAMING,
                        severity=Severity.LOW,
                        message=f"Function name '{node.name}' should be snake_case",
                        suggestion="Use lowercase with underscores (snake_case)",
                        rule_id="N802"
                    ))
            
            # Nomes de classes
            if isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.NAMING,
                        severity=Severity.LOW,
                        message=f"Class name '{node.name}' should be PascalCase",
                        suggestion="Use PascalCase (first letter uppercase)",
                        rule_id="N801"
                    ))
            
            # Variáveis com nomes muito curtos
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if len(node.id) == 1 and node.id not in ['i', 'j', 'k', 'x', 'y', 'z', '_']:
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.NAMING,
                        severity=Severity.LOW,
                        message=f"Variable name '{node.id}' is too short",
                        suggestion="Use descriptive variable names",
                        rule_id="N803"
                    ))
                
                # Palavras reservadas como nomes
                if keyword.iskeyword(node.id):
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.NAMING,
                        severity=Severity.HIGH,
                        message=f"'{node.id}' is a Python keyword",
                        suggestion="Choose a different variable name",
                        rule_id="N804"
                    ))
        
        return issues
    
    def _analyze_documentation(self, tree: ast.AST, code: str) -> List[CodeIssue]:
        """Análise de documentação"""
        issues = []
        
        for node in ast.walk(tree):
            # Funções sem docstring
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    # Ignora funções muito simples (menos de 3 linhas)
                    func_lines = (node.end_lineno or node.lineno) - node.lineno + 1
                    if func_lines > 3 and not node.name.startswith('_'):
                        issues.append(CodeIssue(
                            line=node.lineno, column=node.col_offset,
                            issue_type=IssueType.DOCUMENTATION,
                            severity=Severity.LOW,
                            message=f"Function '{node.name}' missing docstring",
                            suggestion="Add docstring explaining function purpose",
                            rule_id="D100"
                        ))
            
            # Classes sem docstring
            if isinstance(node, ast.ClassDef):
                if not ast.get_docstring(node):
                    issues.append(CodeIssue(
                        line=node.lineno, column=node.col_offset,
                        issue_type=IssueType.DOCUMENTATION,
                        severity=Severity.MEDIUM,
                        message=f"Class '{node.name}' missing docstring",
                        suggestion="Add docstring explaining class purpose",
                        rule_id="D101"
                    ))
        
        # Módulo sem docstring
        module_docstring = ast.get_docstring(tree)
        if not module_docstring:
            lines = code.split('\n')
            if len(lines) > 10:  # Apenas para códigos mais longos
                issues.append(CodeIssue(
                    line=1, column=1,
                    issue_type=IssueType.DOCUMENTATION,
                    severity=Severity.LOW,
                    message="Module missing docstring",
                    suggestion="Add module-level docstring",
                    rule_id="D100"
                ))
        
        return issues
    
    def _calculate_metrics(self, tree: ast.AST, code: str) -> CodeMetrics:
        """Calcula métricas do código"""
        lines = code.split('\n')
        
        lines_of_code = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        blank_lines = len([l for l in lines if not l.strip()])
        comment_lines = len([l for l in lines if l.strip().startswith('#')])
        
        functions = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
        classes = len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
        imports = len([n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))])
        
        cyclomatic_complexity = self._calculate_cyclomatic_complexity(tree)
        maintainability_index = self._calculate_maintainability_index(tree, lines_of_code, cyclomatic_complexity)
        documentation_coverage = self._calculate_documentation_coverage(tree)
        
        return CodeMetrics(
            lines_of_code=lines_of_code,
            blank_lines=blank_lines,
            comment_lines=comment_lines,
            functions=functions,
            classes=classes,
            imports=imports,
            cyclomatic_complexity=cyclomatic_complexity,
            maintainability_index=maintainability_index,
            documentation_coverage=documentation_coverage
        )
    
    def _calculate_quality_score(self, issues: List[CodeIssue], 
                                metrics: CodeMetrics, code: str) -> QualityScore:
        """Calcula scores de qualidade"""
        if not code.strip():
            return QualityScore(0, "F", 0, 0, 0, 0, 0, 0)
        
        # Penalidades por severidade
        severity_penalties = {
            Severity.LOW: 1,
            Severity.MEDIUM: 3,
            Severity.HIGH: 8,
            Severity.CRITICAL: 15
        }
        
        # Penalidades por tipo
        type_penalties = {}
        for issue_type in IssueType:
            type_issues = [i for i in issues if i.issue_type == issue_type]
            penalty = sum(severity_penalties[i.severity] for i in type_issues)
            type_penalties[issue_type] = penalty
        
        # Calcula scores por categoria (0-100)
        base_score = 100
        lines_factor = max(metrics.lines_of_code, 1)
        
        style_score = max(0, base_score - (type_penalties[IssueType.STYLE] * 10 / lines_factor))
        logic_score = max(0, base_score - (type_penalties[IssueType.LOGIC] * 15 / lines_factor))
        security_score = max(0, base_score - (type_penalties[IssueType.SECURITY] * 20 / lines_factor))
        performance_score = max(0, base_score - (type_penalties[IssueType.PERFORMANCE] * 12 / lines_factor))
        maintainability_score = max(0, base_score - (type_penalties[IssueType.MAINTAINABILITY] * 10 / lines_factor))
        documentation_score = metrics.documentation_coverage * 100
        
        # Score geral (média ponderada)
        overall_score = (
            style_score * 0.15 +
            logic_score * 0.25 +
            security_score * 0.25 +
            performance_score * 0.15 +
            maintainability_score * 0.15 +
            documentation_score * 0.05
        )
        
        grade = self._score_to_grade(overall_score)
        
        return QualityScore(
            overall_score=round(overall_score, 1),
            grade=grade,
            style_score=round(style_score, 1),
            logic_score=round(logic_score, 1),
            security_score=round(security_score, 1),
            performance_score=round(performance_score, 1),
            maintainability_score=round(maintainability_score, 1),
            documentation_score=round(documentation_score, 1)
        )
    
    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calcula complexidade ciclomática"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With)):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
            elif isinstance(node, (ast.Break, ast.Continue)):
                complexity += 1
        
        return complexity
    
    def _calculate_max_nesting(self, tree: ast.AST) -> int:
        """Calcula nível máximo de aninhamento"""
        max_depth = 0
        
        def get_depth(node, current_depth=0):
            nonlocal max_depth
            max_depth = max(max_depth, current_depth)
            
            if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.FunctionDef, ast.ClassDef)):
                for child in ast.iter_child_nodes(node):
                    get_depth(child, current_depth + 1)
            else:
                for child in ast.iter_child_nodes(node):
                    get_depth(child, current_depth)
        
        get_depth(tree)
        return max_depth
    
    def _calculate_maintainability_index(self, tree: ast.AST, loc: int, complexity: int) -> float:
        """Calcula índice de manutenibilidade simplificado"""
        if loc == 0:
            return 100.0
        
        # Fórmula simplificada baseada em LOC e complexidade
        halstead_volume = loc * 4  # Aproximação simples
        mi = 171 - 5.2 * (halstead_volume ** 0.23) - 0.23 * complexity - 16.2 * (loc ** 0.5)
        return max(0, min(100, mi))
    
    def _calculate_documentation_coverage(self, tree: ast.AST) -> float:
        """Calcula cobertura de documentação"""
        total_items = 0
        documented_items = 0
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                total_items += 1
                if ast.get_docstring(node):
                    documented_items += 1
        
        return documented_items / total_items if total_items > 0 else 1.0
    
    def _score_to_grade(self, score: float) -> str:
        """Converte score numérico em grade"""
        if score >= 95: return "A+"
        elif score >= 90: return "A"
        elif score >= 85: return "A-"
        elif score >= 80: return "B+"
        elif score >= 75: return "B"
        elif score >= 70: return "B-"
        elif score >= 65: return "C+"
        elif score >= 60: return "C"
        elif score >= 55: return "C-"
        elif score >= 50: return "D"
        else: return "F"
    
    def _generate_improvement_suggestions(self, issues: List[CodeIssue], 
                                        metrics: CodeMetrics) -> List[str]:
        """Gera sugestões de melhoria prioritárias"""
        suggestions = []
        
        # Agrupa issues por severidade
        critical_issues = [i for i in issues if i.severity == Severity.CRITICAL]
        high_issues = [i for i in issues if i.severity == Severity.HIGH]
        
        # Sugestões críticas
        if critical_issues:
            suggestions.append("🚨 CRÍTICO: Corrija problemas de segurança imediatamente")
        
        if high_issues:
            suggestions.append("⚠️ IMPORTANTE: Resolva problemas de alta severidade")
        
        # Sugestões por tipo
        type_counts = {}
        for issue in issues:
            typ = issue.issue_type.value
            type_counts[typ] = type_counts.get(typ, 0) + 1
        
        if type_counts.get('style', 0) > 5:
            suggestions.append("📏 ESTILO: Use um formatter automático (black, autopep8)")
        
        if type_counts.get('maintainability', 0) > 3:
            suggestions.append("🔧 MANUTENÇÃO: Refatore código complexo em funções menores")
        
        if type_counts.get('documentation', 0) > 2:
            suggestions.append("📚 DOCUMENTAÇÃO: Adicione docstrings às funções principais")
        
        if metrics.cyclomatic_complexity > 10:
            suggestions.append("🧠 COMPLEXIDADE: Simplifique a lógica do código")
        
        if metrics.documentation_coverage < 0.5:
            suggestions.append("📖 DOCS: Melhore a documentação do código")
        
        return suggestions[:5]  # Máximo 5 sugestões
    
    def _generate_summary(self, issues: List[CodeIssue], quality_score: QualityScore) -> Dict[str, Any]:
        """Gera resumo da análise"""
        by_severity = {}
        by_type = {}
        
        for issue in issues:
            # Por severidade
            sev = issue.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + 1
            
            # Por tipo
            typ = issue.issue_type.value
            by_type[typ] = by_type.get(typ, 0) + 1
        
        return {
            "total_issues": len(issues),
            "overall_score": quality_score.overall_score,
            "grade": quality_score.grade,
            "by_severity": by_severity,
            "by_type": by_type,
            "top_issue_types": sorted(by_type.items(), key=lambda x: x[1], reverse=True)[:3]
        }
    
    def _empty_analysis_result(self) -> Dict[str, Any]:
        """Resultado para código vazio"""
        return {
            "timestamp": datetime.now().isoformat(),
            "filename": "empty",
            "context": "empty",
            "syntax_valid": True,
            "syntax_error": None,
            "issues": [],
            "metrics": asdict(CodeMetrics(0, 0, 0, 0, 0, 0, 0, 100.0, 1.0)),
            "quality_score": asdict(QualityScore(100, "A+", 100, 100, 100, 100, 100, 100)),
            "suggestions": [],
            "summary": {"total_issues": 0, "overall_score": 100, "grade": "A+", "by_severity": {}, "by_type": {}},
            "analysis_time_ms": 0
        }
    
    def _syntax_error_result(self, error_msg: str, line: int) -> Dict[str, Any]:
        """Resultado para erro de sintaxe"""
        return {
            "timestamp": datetime.now().isoformat(),
            "filename": "syntax_error",
            "context": "error",
            "syntax_valid": False,
            "syntax_error": {"message": error_msg, "line": line},
            "issues": [],
            "metrics": asdict(CodeMetrics(0, 0, 0, 0, 0, 0, 0, 0.0, 0.0)),
            "quality_score": asdict(QualityScore(0, "F", 0, 0, 0, 0, 0, 0)),
            "suggestions": ["🚨 Corrija o erro de sintaxe antes de continuar"],
            "summary": {"total_issues": 1, "overall_score": 0, "grade": "F", "by_severity": {"critical": 1}, "by_type": {"syntax": 1}},
            "analysis_time_ms": 0
        }
    
    def _load_analysis_rules(self) -> Dict[str, Any]:
        """Carrega regras de análise customizáveis"""
        return {
            "max_line_length": 79,
            "max_function_length": 50,
            "max_parameters": 7,
            "max_complexity": 10,
            "max_nesting": 4,
            "require_docstrings": True
        }
    
    def get_analysis_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Retorna histórico de análises"""
        return self.analysis_history[-limit:]
    
    def clear_history(self):
        """Limpa histórico de análises"""
        self.analysis_history.clear()