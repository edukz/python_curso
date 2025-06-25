#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advanced Analytics System - Sistema avançado de análise de aprendizado
"""

import json
import time
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import os


@dataclass
class StudySession:
    """Representa uma sessão de estudo"""
    start_time: datetime
    end_time: datetime
    module_id: str
    topic: str
    duration_minutes: float
    exercises_completed: int
    errors_made: int
    score: float
    difficulty_level: int
    session_type: str  # "study", "exercise", "review", "project"


@dataclass
class ErrorPattern:
    """Padrão de erro identificado"""
    error_type: str
    module_id: str
    topic: str
    frequency: int
    description: str
    suggestion: str
    first_occurrence: datetime
    last_occurrence: datetime


@dataclass
class LearningMetrics:
    """Métricas de aprendizado"""
    total_study_time: float
    average_session_duration: float
    modules_completed: int
    exercises_completed: int
    average_score: float
    improvement_rate: float
    consistency_score: float
    difficulty_preference: int
    learning_velocity: float  # módulos por semana


class AdvancedAnalytics:
    """Sistema avançado de analytics de aprendizado"""
    
    def __init__(self, data_dir: str = ".analytics"):
        self.data_dir = data_dir
        self.sessions_file = os.path.join(data_dir, "study_sessions.json")
        self.errors_file = os.path.join(data_dir, "error_patterns.json")
        self.metrics_file = os.path.join(data_dir, "learning_metrics.json")
        
        # Cria diretório se não existir
        os.makedirs(data_dir, exist_ok=True)
        
        # Carrega dados existentes
        self.study_sessions: List[StudySession] = self._load_sessions()
        self.error_patterns: List[ErrorPattern] = self._load_error_patterns()
        self.current_session_start: Optional[datetime] = None
        
    def start_session(self, module_id: str, topic: str, session_type: str = "study"):
        """Inicia uma nova sessão de estudo"""
        self.current_session_start = datetime.now()
        self.current_module = module_id
        self.current_topic = topic
        self.current_session_type = session_type
        self.current_errors = 0
        self.current_exercises = 0
        
    def end_session(self, score: float = 0.0, difficulty: int = 1):
        """Finaliza a sessão atual"""
        if not self.current_session_start:
            return
            
        end_time = datetime.now()
        duration = (end_time - self.current_session_start).total_seconds() / 60
        
        session = StudySession(
            start_time=self.current_session_start,
            end_time=end_time,
            module_id=self.current_module,
            topic=self.current_topic,
            duration_minutes=duration,
            exercises_completed=self.current_exercises,
            errors_made=self.current_errors,
            score=score,
            difficulty_level=difficulty,
            session_type=self.current_session_type
        )
        
        self.study_sessions.append(session)
        self._save_sessions()
        
        # Reset
        self.current_session_start = None
        
    def log_error(self, error_type: str, description: str, module_id: str = None, topic: str = None):
        """Registra um erro cometido"""
        if self.current_session_start:
            self.current_errors += 1
            
        module_id = module_id or getattr(self, 'current_module', 'unknown')
        topic = topic or getattr(self, 'current_topic', 'unknown')
        
        # Atualiza padrões de erro
        self._update_error_pattern(error_type, module_id, topic, description)
        
    def log_exercise_completion(self, success: bool = True):
        """Registra conclusão de exercício"""
        if self.current_session_start:
            self.current_exercises += 1
            if not success:
                self.current_errors += 1
                
    def get_time_by_module(self, days: int = 30) -> Dict[str, float]:
        """Retorna tempo gasto por módulo nos últimos X dias"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        module_times = defaultdict(float)
        for session in self.study_sessions:
            if session.start_time >= cutoff_date:
                module_times[session.module_id] += session.duration_minutes
                
        return dict(module_times)
        
    def get_time_by_topic(self, module_id: str = None, days: int = 30) -> Dict[str, float]:
        """Retorna tempo gasto por tópico"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        topic_times = defaultdict(float)
        for session in self.study_sessions:
            if session.start_time >= cutoff_date:
                if module_id is None or session.module_id == module_id:
                    topic_times[session.topic] += session.duration_minutes
                    
        return dict(topic_times)
        
    def get_common_error_patterns(self, limit: int = 10) -> List[ErrorPattern]:
        """Retorna os padrões de erro mais comuns"""
        return sorted(self.error_patterns, 
                     key=lambda x: x.frequency, reverse=True)[:limit]
                     
    def get_learning_metrics(self, days: int = 30) -> LearningMetrics:
        """Calcula métricas de aprendizado"""
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_sessions = [s for s in self.study_sessions if s.start_time >= cutoff_date]
        
        if not recent_sessions:
            return LearningMetrics(0, 0, 0, 0, 0, 0, 0, 1, 0)
            
        # Métricas básicas
        total_time = sum(s.duration_minutes for s in recent_sessions)
        avg_duration = statistics.mean([s.duration_minutes for s in recent_sessions])
        modules = len(set(s.module_id for s in recent_sessions))
        exercises = sum(s.exercises_completed for s in recent_sessions)
        
        # Score médio
        scores = [s.score for s in recent_sessions if s.score > 0]
        avg_score = statistics.mean(scores) if scores else 0
        
        # Taxa de melhoria (comparação com período anterior)
        improvement_rate = self._calculate_improvement_rate(days)
        
        # Score de consistência (baseado na regularidade das sessões)
        consistency = self._calculate_consistency_score(recent_sessions)
        
        # Preferência de dificuldade
        difficulties = [s.difficulty_level for s in recent_sessions]
        difficulty_pref = int(statistics.mean(difficulties)) if difficulties else 1
        
        # Velocidade de aprendizado (módulos por semana)
        weeks = days / 7
        learning_velocity = modules / weeks if weeks > 0 else 0
        
        return LearningMetrics(
            total_study_time=total_time,
            average_session_duration=avg_duration,
            modules_completed=modules,
            exercises_completed=exercises,
            average_score=avg_score,
            improvement_rate=improvement_rate,
            consistency_score=consistency,
            difficulty_preference=difficulty_pref,
            learning_velocity=learning_velocity
        )
        
    def get_personalized_suggestions(self) -> List[str]:
        """Gera sugestões personalizadas baseadas no desempenho"""
        suggestions = []
        metrics = self.get_learning_metrics()
        common_errors = self.get_common_error_patterns(5)
        
        # Sugestões baseadas em tempo de estudo
        if metrics.total_study_time < 60:  # Menos de 1 hora
            suggestions.append("📚 Tente estudar pelo menos 15 minutos por dia para manter o ritmo")
        elif metrics.average_session_duration > 120:  # Mais de 2 horas
            suggestions.append("⏱️ Considere sessões mais curtas (60-90 min) para melhor retenção")
            
        # Sugestões baseadas em consistência
        if metrics.consistency_score < 0.5:
            suggestions.append("📅 Tente manter uma rotina de estudos mais regular")
        elif metrics.consistency_score > 0.8:
            suggestions.append("🔥 Excelente consistência! Continue assim!")
            
        # Sugestões baseadas em performance
        if metrics.average_score < 60:
            suggestions.append("💪 Foque na revisão dos conceitos básicos antes de avançar")
        elif metrics.average_score > 90:
            suggestions.append("🎯 Experimente exercícios de nível mais avançado")
            
        # Sugestões baseadas em erros comuns
        if common_errors:
            top_error = common_errors[0]
            suggestions.append(f"🐛 Erro comum: {top_error.description}. {top_error.suggestion}")
            
        # Sugestões baseadas em velocidade de aprendizado
        if metrics.learning_velocity < 0.5:
            suggestions.append("🚀 Considere aumentar a frequência de estudos")
        elif metrics.learning_velocity > 2:
            suggestions.append("🎓 Ritmo excelente! Considere projetos práticos")
            
        return suggestions[:5]  # Máximo 5 sugestões
        
    def generate_weekly_report(self) -> Dict[str, Any]:
        """Gera relatório semanal de progresso"""
        metrics_week = self.get_learning_metrics(7)
        metrics_month = self.get_learning_metrics(30)
        
        # Dados da semana
        week_sessions = [s for s in self.study_sessions 
                        if s.start_time >= datetime.now() - timedelta(days=7)]
        
        # Análise de tendências
        daily_times = self._get_daily_study_times(7)
        trend = self._calculate_trend(daily_times)
        
        # Comparação com semana anterior
        prev_week_metrics = self._get_previous_week_metrics()
        
        return {
            "period": {
                "start": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
                "end": datetime.now().strftime("%Y-%m-%d")
            },
            "summary": {
                "total_time": metrics_week.total_study_time,
                "sessions": len(week_sessions),
                "modules": metrics_week.modules_completed,
                "exercises": metrics_week.exercises_completed,
                "average_score": metrics_week.average_score
            },
            "comparison": {
                "time_change": metrics_week.total_study_time - prev_week_metrics.get("time", 0),
                "score_change": metrics_week.average_score - prev_week_metrics.get("score", 0),
                "consistency_change": metrics_week.consistency_score - prev_week_metrics.get("consistency", 0)
            },
            "trends": {
                "study_time_trend": trend,
                "daily_times": daily_times,
                "peak_day": max(daily_times.items(), key=lambda x: x[1])[0] if daily_times else None
            },
            "achievements": self._get_weekly_achievements(week_sessions),
            "suggestions": self.get_personalized_suggestions(),
            "common_errors": [asdict(e) for e in self.get_common_error_patterns(3)],
            "monthly_context": {
                "total_time": metrics_month.total_study_time,
                "learning_velocity": metrics_month.learning_velocity,
                "improvement_rate": metrics_month.improvement_rate
            }
        }
        
    def get_study_heatmap(self, days: int = 30) -> Dict[str, float]:
        """Retorna dados para heatmap de estudos"""
        cutoff_date = datetime.now() - timedelta(days=days)
        daily_times = defaultdict(float)
        
        for session in self.study_sessions:
            if session.start_time >= cutoff_date:
                date_key = session.start_time.strftime("%Y-%m-%d")
                daily_times[date_key] += session.duration_minutes
                
        return dict(daily_times)
        
    def _load_sessions(self) -> List[StudySession]:
        """Carrega sessões de estudo do arquivo"""
        if not os.path.exists(self.sessions_file):
            return []
            
        try:
            with open(self.sessions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                sessions = []
                for item in data:
                    item['start_time'] = datetime.fromisoformat(item['start_time'])
                    item['end_time'] = datetime.fromisoformat(item['end_time'])
                    sessions.append(StudySession(**item))
                return sessions
        except Exception:
            return []
            
    def _save_sessions(self):
        """Salva sessões de estudo no arquivo"""
        try:
            data = []
            for session in self.study_sessions:
                session_dict = asdict(session)
                session_dict['start_time'] = session.start_time.isoformat()
                session_dict['end_time'] = session.end_time.isoformat()
                data.append(session_dict)
                
            with open(self.sessions_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar sessões: {e}")
            
    def _load_error_patterns(self) -> List[ErrorPattern]:
        """Carrega padrões de erro do arquivo"""
        if not os.path.exists(self.errors_file):
            return []
            
        try:
            with open(self.errors_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                patterns = []
                for item in data:
                    item['first_occurrence'] = datetime.fromisoformat(item['first_occurrence'])
                    item['last_occurrence'] = datetime.fromisoformat(item['last_occurrence'])
                    patterns.append(ErrorPattern(**item))
                return patterns
        except Exception:
            return []
            
    def _save_error_patterns(self):
        """Salva padrões de erro no arquivo"""
        try:
            data = []
            for pattern in self.error_patterns:
                pattern_dict = asdict(pattern)
                pattern_dict['first_occurrence'] = pattern.first_occurrence.isoformat()
                pattern_dict['last_occurrence'] = pattern.last_occurrence.isoformat()
                data.append(pattern_dict)
                
            with open(self.errors_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar padrões de erro: {e}")
            
    def _update_error_pattern(self, error_type: str, module_id: str, topic: str, description: str):
        """Atualiza ou cria padrão de erro"""
        # Busca padrão existente
        for pattern in self.error_patterns:
            if (pattern.error_type == error_type and 
                pattern.module_id == module_id and 
                pattern.topic == topic):
                pattern.frequency += 1
                pattern.last_occurrence = datetime.now()
                self._save_error_patterns()
                return
                
        # Cria novo padrão
        suggestion = self._generate_error_suggestion(error_type, description)
        new_pattern = ErrorPattern(
            error_type=error_type,
            module_id=module_id,
            topic=topic,
            frequency=1,
            description=description,
            suggestion=suggestion,
            first_occurrence=datetime.now(),
            last_occurrence=datetime.now()
        )
        
        self.error_patterns.append(new_pattern)
        self._save_error_patterns()
        
    def _generate_error_suggestion(self, error_type: str, description: str) -> str:
        """Gera sugestão baseada no tipo de erro"""
        suggestions = {
            "syntax": "Revise a sintaxe básica do Python. Use um editor que destaque erros.",
            "indentation": "Python usa indentação para definir blocos. Use 4 espaços consistentemente.",
            "variable": "Verifique se todas as variáveis foram definidas antes do uso.",
            "type": "Revise os tipos de dados e conversões entre eles.",
            "logic": "Trace o fluxo do seu código passo a passo para encontrar a lógica incorreta.",
            "import": "Verifique se os módulos estão instalados e importados corretamente."
        }
        
        for key, suggestion in suggestions.items():
            if key in error_type.lower() or key in description.lower():
                return suggestion
                
        return "Revise o conceito relacionado e pratique exercícios similares."
        
    def _calculate_improvement_rate(self, days: int) -> float:
        """Calcula taxa de melhoria comparando com período anterior"""
        cutoff = datetime.now() - timedelta(days=days)
        prev_cutoff = cutoff - timedelta(days=days)
        
        current_sessions = [s for s in self.study_sessions if s.start_time >= cutoff]
        previous_sessions = [s for s in self.study_sessions 
                           if prev_cutoff <= s.start_time < cutoff]
        
        if not current_sessions or not previous_sessions:
            return 0.0
            
        current_avg = statistics.mean([s.score for s in current_sessions if s.score > 0] or [0])
        previous_avg = statistics.mean([s.score for s in previous_sessions if s.score > 0] or [0])
        
        if previous_avg == 0:
            return 0.0
            
        return (current_avg - previous_avg) / previous_avg
        
    def _calculate_consistency_score(self, sessions: List[StudySession]) -> float:
        """Calcula score de consistência baseado na regularidade das sessões"""
        if not sessions:
            return 0.0
            
        # Agrupa sessões por dia
        daily_counts = defaultdict(int)
        for session in sessions:
            date_key = session.start_time.strftime("%Y-%m-%d")
            daily_counts[date_key] += 1
            
        if not daily_counts:
            return 0.0
            
        # Calcula variância dos dias de estudo
        counts = list(daily_counts.values())
        if len(counts) == 1:
            return 1.0
            
        mean_count = statistics.mean(counts)
        variance = statistics.variance(counts)
        
        # Score de consistência inversamente proporcional à variância
        consistency = 1.0 / (1.0 + variance / (mean_count + 1))
        return min(1.0, consistency)
        
    def _get_daily_study_times(self, days: int) -> Dict[str, float]:
        """Retorna tempo de estudo por dia"""
        cutoff_date = datetime.now() - timedelta(days=days)
        daily_times = defaultdict(float)
        
        for session in self.study_sessions:
            if session.start_time >= cutoff_date:
                date_key = session.start_time.strftime("%Y-%m-%d")
                daily_times[date_key] += session.duration_minutes
                
        return dict(daily_times)
        
    def _calculate_trend(self, daily_times: Dict[str, float]) -> str:
        """Calcula tendência baseada nos tempos diários"""
        if len(daily_times) < 3:
            return "insufficient_data"
            
        times = list(daily_times.values())
        
        # Calcula diferenças consecutivas
        diffs = [times[i+1] - times[i] for i in range(len(times)-1)]
        avg_diff = statistics.mean(diffs)
        
        if avg_diff > 5:
            return "increasing"
        elif avg_diff < -5:
            return "decreasing"
        else:
            return "stable"
            
    def _get_previous_week_metrics(self) -> Dict[str, float]:
        """Obtém métricas da semana anterior para comparação"""
        start_date = datetime.now() - timedelta(days=14)
        end_date = datetime.now() - timedelta(days=7)
        
        week_sessions = [s for s in self.study_sessions 
                        if start_date <= s.start_time < end_date]
        
        if not week_sessions:
            return {"time": 0, "score": 0, "consistency": 0}
            
        total_time = sum(s.duration_minutes for s in week_sessions)
        scores = [s.score for s in week_sessions if s.score > 0]
        avg_score = statistics.mean(scores) if scores else 0
        consistency = self._calculate_consistency_score(week_sessions)
        
        return {
            "time": total_time,
            "score": avg_score,
            "consistency": consistency
        }
        
    def _get_weekly_achievements(self, sessions: List[StudySession]) -> List[str]:
        """Identifica conquistas da semana"""
        achievements = []
        
        if not sessions:
            return achievements
            
        total_time = sum(s.duration_minutes for s in sessions)
        total_exercises = sum(s.exercises_completed for s in sessions)
        unique_modules = len(set(s.module_id for s in sessions))
        
        # Conquistas baseadas em tempo
        if total_time >= 300:  # 5 horas
            achievements.append("🏆 Mais de 5 horas de estudo esta semana!")
        elif total_time >= 180:  # 3 horas
            achievements.append("🌟 Mais de 3 horas de estudo esta semana!")
            
        # Conquistas baseadas em exercícios
        if total_exercises >= 50:
            achievements.append("💪 Mais de 50 exercícios completados!")
        elif total_exercises >= 20:
            achievements.append("🎯 Mais de 20 exercícios completados!")
            
        # Conquistas baseadas em consistência
        if len(sessions) >= 5:
            achievements.append("🔥 Estudou 5+ dias esta semana!")
            
        # Conquistas baseadas em variedade
        if unique_modules >= 3:
            achievements.append("📚 Explorou 3+ módulos diferentes!")
            
        return achievements