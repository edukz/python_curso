#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code Review Module - Sistema completo de análise de código Python

Este módulo fornece análise estática avançada de código Python sem dependência
de LLMs externos, incluindo:

- Análise de estilo (PEP 8)
- Detecção de problemas de lógica
- Verificação de segurança
- Análise de performance
- Avaliação de manutenibilidade
- Verificação de documentação
- Dashboard interativo
- Integração com exercícios
"""

from .analysis_engine import (
    CodeAnalysisEngine,
    CodeIssue,
    CodeMetrics,
    QualityScore,
    IssueType,
    Severity
)

from .code_review_dashboard import CodeReviewDashboard
from .exercise_integration import ExerciseCodeReviewer

__version__ = "1.0.0"
__author__ = "Python Course System"

__all__ = [
    'CodeAnalysisEngine',
    'CodeReviewDashboard', 
    'ExerciseCodeReviewer',
    'CodeIssue',
    'CodeMetrics',
    'QualityScore',
    'IssueType',
    'Severity'
]