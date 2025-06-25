#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Rastreamento de Erros
Monitora e registra erros durante a execução dos módulos
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import traceback


class ErrorTracker:
    """Rastreia erros durante a execução do curso"""
    
    def __init__(self):
        self.session_errors: List[Dict[str, Any]] = []
        self.module_errors: Dict[str, List[Dict[str, Any]]] = {}
        self.current_module: Optional[str] = None
        self.error_count = 0
    
    def start_module(self, module_id: str) -> None:
        """Inicia rastreamento para um módulo"""
        self.current_module = module_id
        if module_id not in self.module_errors:
            self.module_errors[module_id] = []
    
    def end_module(self, module_id: str) -> Dict[str, Any]:
        """Finaliza rastreamento e retorna estatísticas"""
        if module_id not in self.module_errors:
            return {
                "sem_erros": True,
                "total_erros": 0,
                "erros": []
            }
        
        module_error_list = self.module_errors[module_id]
        return {
            "sem_erros": len(module_error_list) == 0,
            "total_erros": len(module_error_list),
            "erros": module_error_list
        }
    
    def track_error(self, error: Exception, context: str = "", 
                   severity: str = "medium") -> None:
        """
        Registra um erro
        
        Args:
            error: Exceção capturada
            context: Contexto onde ocorreu o erro
            severity: low, medium, high, critical
        """
        error_info = {
            "timestamp": datetime.now().isoformat(),
            "type": type(error).__name__,
            "message": str(error),
            "context": context,
            "severity": severity,
            "traceback": traceback.format_exc(),
            "module": self.current_module
        }
        
        self.session_errors.append(error_info)
        self.error_count += 1
        
        if self.current_module:
            self.module_errors[self.current_module].append(error_info)
    
    def track_exercise_error(self, exercise_id: str, user_answer: str, 
                           expected_answer: str) -> None:
        """Registra erro em exercício"""
        error_info = {
            "timestamp": datetime.now().isoformat(),
            "type": "ExerciseError",
            "message": f"Resposta incorreta no exercício {exercise_id}",
            "context": "exercise",
            "severity": "low",
            "details": {
                "exercise_id": exercise_id,
                "user_answer": user_answer,
                "expected_answer": expected_answer
            },
            "module": self.current_module
        }
        
        self.session_errors.append(error_info)
        if self.current_module:
            self.module_errors[self.current_module].append(error_info)
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Retorna resumo de erros da sessão"""
        severity_count = {
            "low": 0,
            "medium": 0,
            "high": 0,
            "critical": 0
        }
        
        for error in self.session_errors:
            severity = error.get("severity", "medium")
            severity_count[severity] += 1
        
        return {
            "total_errors": self.error_count,
            "errors_by_severity": severity_count,
            "modules_with_errors": list(self.module_errors.keys()),
            "clean_modules": [
                module_id for module_id, errors in self.module_errors.items()
                if len(errors) == 0
            ]
        }
    
    def has_critical_errors(self) -> bool:
        """Verifica se houve erros críticos"""
        return any(
            error.get("severity") == "critical" 
            for error in self.session_errors
        )
    
    def clear_module_errors(self, module_id: str) -> None:
        """Limpa erros de um módulo específico"""
        if module_id in self.module_errors:
            self.module_errors[module_id] = []
    
    def get_error_report(self) -> str:
        """Gera relatório de erros formatado"""
        if not self.session_errors:
            return "✅ Nenhum erro registrado na sessão!"
        
        report = []
        report.append("📊 RELATÓRIO DE ERROS DA SESSÃO")
        report.append("=" * 50)
        
        summary = self.get_session_summary()
        report.append(f"\n📈 Total de erros: {summary['total_errors']}")
        report.append("\n🔍 Erros por severidade:")
        
        for severity, count in summary['errors_by_severity'].items():
            if count > 0:
                emoji = {
                    "low": "🟢",
                    "medium": "🟡",
                    "high": "🟠",
                    "critical": "🔴"
                }.get(severity, "⚪")
                report.append(f"  {emoji} {severity.upper()}: {count}")
        
        if summary['modules_with_errors']:
            report.append(f"\n📚 Módulos com erros: {', '.join(summary['modules_with_errors'])}")
        
        if summary['clean_modules']:
            report.append(f"\n✨ Módulos sem erros: {', '.join(summary['clean_modules'])}")
        
        return "\n".join(report)