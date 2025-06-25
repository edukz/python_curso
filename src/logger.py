#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Logging do Curso
Registra eventos e ações para debug e análise
"""

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Optional


class CourseLogger:
    """Gerenciador de logs do curso"""
    
    def __init__(self, log_file: str = "course.log", max_size_mb: int = 10):
        self.log_file = log_file
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Configura o sistema de logging"""
        # Cria logger
        logger = logging.getLogger('PythonCourse')
        logger.setLevel(logging.DEBUG)
        
        # Remove handlers existentes para evitar duplicação
        logger.handlers = []
        
        # Formato do log
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para arquivo com rotação
        file_handler = RotatingFileHandler(
            self.log_file,
            maxBytes=self.max_size_bytes,
            backupCount=3,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        
        # Handler para console (apenas warnings e erros)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        
        # Adiciona handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def log_session_start(self, user_name: Optional[str] = None) -> None:
        """Registra início de sessão"""
        self.logger.info(f"Sessão iniciada - Usuário: {user_name or 'Anônimo'}")
    
    def log_session_end(self, duration_seconds: int) -> None:
        """Registra fim de sessão"""
        duration_min = duration_seconds // 60
        self.logger.info(f"Sessão encerrada - Duração: {duration_min} minutos")
    
    def log_module_start(self, module_id: str, module_name: str) -> None:
        """Registra início de módulo"""
        self.logger.info(f"Módulo iniciado: {module_id} - {module_name}")
    
    def log_module_completion(self, module_id: str, score: int, time_spent: int) -> None:
        """Registra conclusão de módulo"""
        self.logger.info(
            f"Módulo concluído: {module_id} - "
            f"Pontuação: {score} - Tempo: {time_spent}s"
        )
    
    def log_exercise_attempt(self, module_id: str, exercise: str, 
                           correct: bool, attempts: int) -> None:
        """Registra tentativa de exercício"""
        status = "Correto" if correct else "Incorreto"
        self.logger.info(
            f"Exercício: {exercise} - {status} - "
            f"Tentativas: {attempts} - Módulo: {module_id}"
        )
    
    def log_achievement(self, achievement: str, score: int) -> None:
        """Registra conquista desbloqueada"""
        self.logger.info(
            f"Conquista desbloqueada: {achievement} - "
            f"Pontuação total: {score}"
        )
    
    def log_error(self, error: str, module: Optional[str] = None) -> None:
        """Registra erro"""
        context = f" - Módulo: {module}" if module else ""
        self.logger.error(f"Erro: {error}{context}")
    
    def log_user_action(self, action: str, details: Optional[str] = None) -> None:
        """Registra ação do usuário"""
        message = f"Ação: {action}"
        if details:
            message += f" - {details}"
        self.logger.info(message)
    
    def log_progress_update(self, completion_percentage: float, 
                          modules_completed: int, total_score: int) -> None:
        """Registra atualização de progresso"""
        self.logger.info(
            f"Progresso atualizado: {completion_percentage:.1f}% completo - "
            f"Módulos: {modules_completed} - Pontuação: {total_score}"
        )
    
    def get_recent_logs(self, lines: int = 50) -> list:
        """Retorna as últimas linhas do log"""
        if not os.path.exists(self.log_file):
            return []
        
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                return all_lines[-lines:] if len(all_lines) > lines else all_lines
        except IOError:
            return []
    
    def clear_logs(self) -> None:
        """Limpa o arquivo de log"""
        try:
            open(self.log_file, 'w').close()
            self.logger.info("Logs limpos manualmente")
        except IOError as e:
            self.logger.error(f"Erro ao limpar logs: {e}")
    
    def get_log_size(self) -> int:
        """Retorna o tamanho do arquivo de log em bytes"""
        if os.path.exists(self.log_file):
            return os.path.getsize(self.log_file)
        return 0
    
    def create_debug_report(self) -> str:
        """Cria relatório de debug"""
        report = f"""
=== RELATÓRIO DE DEBUG ===
Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Arquivo de log: {self.log_file}
Tamanho do log: {self.get_log_size() / 1024:.2f} KB
Últimos eventos:
"""
        recent_logs = self.get_recent_logs(20)
        report += ''.join(recent_logs)
        
        return report
    
    # ============ MÉTODOS DE COMPATIBILIDADE COM LOGGING PADRÃO ============
    
    def debug(self, message: str) -> None:
        """Método de compatibilidade para debug"""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Método de compatibilidade para info"""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Método de compatibilidade para warning"""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Método de compatibilidade para error"""
        self.logger.error(message)
    
    def critical(self, message: str) -> None:
        """Método de compatibilidade para critical"""
        self.logger.critical(message)