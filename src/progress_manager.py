#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gerenciamento de Progresso do Aluno
Salva e carrega o progresso do curso em arquivo JSON
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any


class ProgressManager:
    """Gerencia o progresso do aluno no curso"""
    
    def __init__(self, progress_file: str = "data/progress.json"):
        self.progress_file = progress_file
        self.progress_data = self._load_progress()
    
    def _load_progress(self) -> Dict[str, Any]:
        """Carrega o progresso do arquivo JSON"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._create_default_progress()
        return self._create_default_progress()
    
    def _create_default_progress(self) -> Dict[str, Any]:
        """Cria estrutura padrão de progresso"""
        return {
            "user_name": "",
            "start_date": datetime.now().isoformat(),
            "last_access": datetime.now().isoformat(),
            "total_score": 0,
            "modules_completed": [],
            "mini_projetos_completos": [],
            "modules_progress": {
                f"modulo_{i}": {
                    "completed": False,
                    "score": 0,
                    "attempts": 0,
                    "last_access": None,
                    "time_spent": 0,
                    "mini_projeto_completo": False,
                    "mini_projeto_score": 0
                } for i in range(1, 31)
            },
            "achievements": [],
            "total_time_spent": 0
        }
    
    def save_progress(self) -> None:
        """Salva o progresso no arquivo JSON"""
        self.progress_data["last_access"] = datetime.now().isoformat()
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress_data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Erro ao salvar progresso: {e}")
    
    def set_user_name(self, name: str) -> None:
        """Define o nome do usuário"""
        self.progress_data["user_name"] = name
        self.save_progress()
    
    def mark_module_completed(self, module_id: str, score: int = 0) -> None:
        """Marca um módulo como completo"""
        if module_id not in self.progress_data["modules_completed"]:
            self.progress_data["modules_completed"].append(module_id)
        
        if module_id in self.progress_data["modules_progress"]:
            self.progress_data["modules_progress"][module_id]["completed"] = True
            self.progress_data["modules_progress"][module_id]["score"] = score
            self.progress_data["modules_progress"][module_id]["last_access"] = datetime.now().isoformat()
        
        self.progress_data["total_score"] += score
        self.save_progress()
    
    def complete_module(self, module_id: str, score: int = 100) -> None:
        """Alias para mark_module_completed - compatibilidade"""
        self.mark_module_completed(module_id, score)
    
    def update_module_progress(self, module_id: str, time_spent: int = 0, attempts: int = 0) -> None:
        """Atualiza o progresso de um módulo"""
        if module_id in self.progress_data["modules_progress"]:
            module = self.progress_data["modules_progress"][module_id]
            module["time_spent"] += time_spent
            module["attempts"] += attempts
            module["last_access"] = datetime.now().isoformat()
        
        self.progress_data["total_time_spent"] += time_spent
        self.save_progress()
    
    def get_completion_percentage(self) -> float:
        """Calcula a porcentagem de conclusão do curso"""
        total_modules = len(self.progress_data["modules_progress"])
        completed_modules = len(self.progress_data["modules_completed"])
        return (completed_modules / total_modules) * 100 if total_modules > 0 else 0
    
    def get_module_status(self, module_id: str) -> Dict[str, Any]:
        """Retorna o status de um módulo específico"""
        return self.progress_data["modules_progress"].get(module_id, {})
    
    def add_achievement(self, achievement: str) -> None:
        """Adiciona uma conquista ao perfil do aluno"""
        if achievement not in self.progress_data["achievements"]:
            self.progress_data["achievements"].append({
                "name": achievement,
                "date": datetime.now().isoformat()
            })
            self.save_progress()
    
    def get_progress_summary(self) -> Dict[str, Any]:
        """Retorna um resumo do progresso"""
        return {
            "user_name": self.progress_data["user_name"],
            "completion_percentage": self.get_completion_percentage(),
            "total_score": self.progress_data["total_score"],
            "modules_completed": len(self.progress_data["modules_completed"]),
            "total_modules": len(self.progress_data["modules_progress"]),
            "achievements": len(self.progress_data["achievements"]),
            "total_time_spent": self.progress_data["total_time_spent"]
        }
    
    def reset_progress(self) -> None:
        """Reseta todo o progresso"""
        self.progress_data = self._create_default_progress()
        self.save_progress()
    
    def mark_mini_project_completed(self, module_id: str, score: int = 50) -> None:
        """Marca mini projeto como completo"""
        if module_id in self.progress_data["modules_progress"]:
            self.progress_data["modules_progress"][module_id]["mini_projeto_completo"] = True
            self.progress_data["modules_progress"][module_id]["mini_projeto_score"] = score
            self.progress_data["modules_progress"][module_id]["last_access"] = datetime.now().isoformat()
        
        # Adiciona à lista global de mini projetos completos
        mini_projeto_key = f"{module_id}_mini_projeto"
        if mini_projeto_key not in self.progress_data["mini_projetos_completos"]:
            self.progress_data["mini_projetos_completos"].append(mini_projeto_key)
        
        self.progress_data["total_score"] += score
        self.save_progress()
    
    def get_mini_projects_completion_percentage(self) -> float:
        """Calcula porcentagem de mini projetos completos"""
        # Assume que módulos 1-6 e 12-23 têm mini projetos (18 total)
        total_mini_projects = 18
        completed_mini_projects = len(self.progress_data.get("mini_projetos_completos", []))
        return (completed_mini_projects / total_mini_projects) * 100 if total_mini_projects > 0 else 0
    
    def get_detailed_progress_summary(self) -> Dict[str, Any]:
        """Retorna resumo detalhado incluindo mini projetos"""
        summary = self.get_progress_summary()
        summary.update({
            "mini_projetos_completos": len(self.progress_data.get("mini_projetos_completos", [])),
            "mini_projetos_percentage": self.get_mini_projects_completion_percentage(),
            "total_mini_projects": 18  # Total de mini projetos disponíveis
        })
        return summary