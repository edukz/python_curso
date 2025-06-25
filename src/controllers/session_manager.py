#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerenciador de Sessão
Gerencia o ciclo de vida da sessão do curso
"""

import time
import sys
from typing import Dict, Any, Optional
from datetime import datetime

from ..ui_components import UIComponents
from ..progress_manager import ProgressManager
from ..logger import CourseLogger
from ..error_tracker import ErrorTracker
from ..sync_manager import SyncManager
from ..security import SecureInput


class SessionManager:
    """Gerencia a sessão do usuário"""
    
    def __init__(self, components: Dict[str, Any]):
        """Inicializa com componentes necessários"""
        self.ui = components['ui']
        self.progress = components['progress']
        self.logger = components['logger']
        self.error_tracker = components['error_tracker']
        self.sync_manager = components['sync_manager']
        self.secure_input = components['secure_input']
        
        self.session_start = datetime.now()
        self.session_active = True
    
    def initialize_session(self) -> bool:
        """
        Inicializa a sessão do curso
        
        Returns:
            True se inicialização bem-sucedida
        """
        try:
            self.ui.clear_screen()
            self._show_welcome_message()
            
            # Verifica se é primeira vez
            if not self.progress.progress_data.get("user_name"):
                if not self._setup_new_user():
                    return False
            
            # Log de início de sessão
            self.logger.log_session_start()
            
            # Sincronização inicial
            self._sync_data()
            
            return True
            
        except Exception as e:
            self.ui.error(f"Erro ao inicializar sessão: {str(e)}")
            return False
    
    def _show_welcome_message(self) -> None:
        """Exibe mensagem de boas-vindas"""
        welcome_message = """
        🐍✨ BEM-VINDO AO CURSO INTERATIVO DE PYTHON! ✨🐍
        
        Um curso completo e moderno para aprender Python do zero.
        
        🚀 Recursos inclusos:
        • 23 módulos progressivos (básico → intermediário → avançado)
        • 18 mini projetos práticos
        • Sistema de gamificação com XP e conquistas
        • Demos interativas e debugger visual
        • Exercícios adaptativos personalizados
        • Certificado de conclusão
        
        💡 Dica: Use 'H' para ver todos os atalhos disponíveis!
        """
        
        print(welcome_message)
        
        # Pausa para leitura
        input("🔸 Pressione ENTER para continuar...")
    
    def _setup_new_user(self) -> bool:
        """
        Configura novo usuário
        
        Returns:
            True se configuração bem-sucedida
        """
        self.ui.clear_screen()
        print("🎯 CONFIGURAÇÃO INICIAL")
        print("=" * 50)
        
        # Solicita nome do usuário
        nome = self.secure_input.get_input(
            "👤 Digite seu nome: ",
            input_type="text",
            max_length=100
        )
        
        if not nome:
            print("❌ Nome é obrigatório!")
            return False
        
        # Salva configurações
        self.progress.set_user_name(nome)
        
        # Mensagem de configuração concluída
        self.ui.success(
            f"✅ Configuração concluída!\n"
            f"👋 Olá, {nome}! Vamos começar sua jornada Python!"
        )
        
        time.sleep(2)
        return True
    
    def _sync_data(self) -> None:
        """Sincroniza dados se configurado"""
        try:
            if hasattr(self.sync_manager, 'sync_up'):
                self.sync_manager.sync_up()
        except Exception as e:
            self.logger.log_error(f"Erro na sincronização: {str(e)}")
    
    def cleanup_session(self) -> None:
        """Limpa recursos da sessão (otimizado para saída rápida)"""
        try:
            # Calcula duração da sessão
            session_duration = (datetime.now() - self.session_start).total_seconds()
            
            # Atualiza tempo total (operação crítica)
            self.progress.progress_data["total_time_spent"] += int(session_duration)
            self.progress.save_progress()
            
            # Log de fim de sessão (rápido)
            self.logger.log_session_end(session_duration)
            
            # Pula sincronização e limpeza de cache na saída para ser mais rápido
            # Estas operações serão feitas na próxima inicialização
            
        except Exception as e:
            # Falha silenciosa para não atrasar a saída
            pass
    
    def _show_error_report(self) -> None:
        """Exibe relatório de erros da sessão"""
        report = self.error_tracker.get_error_report()
        
        self.ui.warning(
            "📋 RELATÓRIO DE ERROS DA SESSÃO\n"
            f"{report}\n\n"
            "💡 Estes dados ajudam a melhorar o curso!"
        )
    
    def _cleanup_caches(self) -> None:
        """Limpa caches expirados"""
        try:
            # Cleanup de componentes que tenham cache
            for component_name in ['config', 'glossary', 'analytics']:
                component = getattr(self, component_name, None)
                if hasattr(component, 'cleanup_expired'):
                    component.cleanup_expired()
        except Exception:
            pass
    
    def handle_interruption(self) -> bool:
        """
        Trata interrupção do usuário (Ctrl+C) - Saída rápida
        
        Returns:
            True se deve continuar, False se deve sair
        """
        print("\n⏸️  Ctrl+C detectado!")
        print("💾 Salvando progresso...")
        
        # Salva progresso rapidamente
        self.progress.save_progress()
        
        print("✅ Progresso salvo. Saindo...")
        return False
    
    def _show_quick_progress(self) -> None:
        """Exibe progresso rápido"""
        completion = self.progress.get_completion_percentage()
        modules_completed = len(self.progress.progress_data["modules_completed"])
        total_score = self.progress.progress_data["total_score"]
        
        print(f"\n📊 PROGRESSO ATUAL:")
        print(f"  📚 Módulos: {modules_completed}/23")
        print(f"  📈 Conclusão: {completion:.1f}%")
        print(f"  ⭐ Pontos: {total_score}")
        
        input("\n🔸 Pressione ENTER para continuar...")
    
    def show_exit_message(self) -> None:
        """Exibe mensagem de despedida"""
        user_name = self.progress.progress_data.get("user_name", "")
        completion = self.progress.get_completion_percentage()
        session_duration = (datetime.now() - self.session_start).total_seconds()
        
        self.ui.clear_screen()
        
        farewell_message = f"""
        🐍 OBRIGADO POR USAR O CURSO DE PYTHON! 🐍
        
        👋 Até logo, {user_name}!
        
        📊 Resumo da sessão:
        • ⏱️  Tempo de estudo: {int(session_duration // 60)} minutos
        • 📈 Progresso atual: {completion:.1f}%
        • 💾 Dados salvos automaticamente
        
        💡 Dicas para continuar aprendendo:
        • Pratique regularmente (mesmo que 15 minutos por dia)
        • Aplique o conhecimento em projetos pessoais
        • Participe de comunidades Python
        • Continue explorando a documentação oficial
        
        🚀 Continue sua jornada Python!
        
        ⭐ Desenvolvido com ❤️ para facilitar seu aprendizado
        """
        
        print(farewell_message)
        
        # Pausa reduzida para leitura
        time.sleep(0.5)
    
    def is_session_active(self) -> bool:
        """Verifica se a sessão está ativa"""
        return self.session_active
    
    def end_session(self) -> None:
        """Finaliza a sessão"""
        self.session_active = False