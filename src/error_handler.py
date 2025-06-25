#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema Centralizado de Tratamento de Erros
Fornece tratamento consistente de erros em todo o sistema
"""

import logging
import traceback
from typing import Optional, Callable, Any, Dict
from functools import wraps
from datetime import datetime


class ErrorHandler:
    """Gerenciador centralizado de erros"""
    
    def __init__(self, logger: Optional[logging.Logger] = None, 
                 error_tracker: Optional[Any] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.error_tracker = error_tracker
        self.error_handlers: Dict[type, Callable] = {}
        
        # Registra handlers padrão
        self._register_default_handlers()
    
    def _register_default_handlers(self):
        """Registra handlers padrão para tipos comuns de erro"""
        self.register_handler(FileNotFoundError, self._handle_file_error)
        self.register_handler(PermissionError, self._handle_permission_error)
        self.register_handler(ValueError, self._handle_value_error)
        self.register_handler(KeyError, self._handle_key_error)
        self.register_handler(ImportError, self._handle_import_error)
        self.register_handler(KeyboardInterrupt, self._handle_keyboard_interrupt)
    
    def register_handler(self, error_type: type, handler: Callable):
        """Registra um handler customizado para um tipo de erro"""
        self.error_handlers[error_type] = handler
    
    def handle_error(self, error: Exception, context: str = "", 
                    severity: str = "medium", reraise: bool = False) -> Optional[Any]:
        """
        Trata um erro de forma centralizada
        
        Args:
            error: Exceção a ser tratada
            context: Contexto onde ocorreu o erro
            severity: low, medium, high, critical
            reraise: Se deve relançar a exceção após tratamento
            
        Returns:
            Resultado do handler ou None
        """
        # Log do erro
        self.logger.error(
            f"[{severity.upper()}] {type(error).__name__} in {context}: {str(error)}"
        )
        
        # Rastreia erro se tracker disponível
        if self.error_tracker:
            self.error_tracker.track_error(error, context, severity)
        
        # Procura handler específico
        error_type = type(error)
        handler = self.error_handlers.get(error_type)
        
        result = None
        if handler:
            result = handler(error, context)
        else:
            # Handler genérico
            result = self._handle_generic_error(error, context)
        
        # Relança se necessário
        if reraise:
            raise error
        
        return result
    
    def _handle_file_error(self, error: FileNotFoundError, context: str) -> Dict[str, Any]:
        """Handler para erros de arquivo não encontrado"""
        return {
            "recovered": True,
            "message": f"📁 Arquivo não encontrado: {error.filename}",
            "suggestion": "Verifique se o arquivo existe e o caminho está correto",
            "action": "skip"
        }
    
    def _handle_permission_error(self, error: PermissionError, context: str) -> Dict[str, Any]:
        """Handler para erros de permissão"""
        return {
            "recovered": True,
            "message": "🔒 Erro de permissão ao acessar arquivo",
            "suggestion": "Verifique as permissões do arquivo ou execute como administrador",
            "action": "skip"
        }
    
    def _handle_value_error(self, error: ValueError, context: str) -> Dict[str, Any]:
        """Handler para erros de valor"""
        return {
            "recovered": True,
            "message": f"❌ Valor inválido: {str(error)}",
            "suggestion": "Verifique se o valor fornecido está no formato correto",
            "action": "retry"
        }
    
    def _handle_key_error(self, error: KeyError, context: str) -> Dict[str, Any]:
        """Handler para erros de chave"""
        return {
            "recovered": True,
            "message": f"🔑 Chave não encontrada: {str(error)}",
            "suggestion": "Verifique se a chave existe no dicionário/configuração",
            "action": "default"
        }
    
    def _handle_import_error(self, error: ImportError, context: str) -> Dict[str, Any]:
        """Handler para erros de importação"""
        return {
            "recovered": False,
            "message": f"📦 Erro ao importar módulo: {str(error)}",
            "suggestion": "Instale as dependências necessárias com pip install",
            "action": "abort"
        }
    
    def _handle_keyboard_interrupt(self, error: KeyboardInterrupt, context: str) -> Dict[str, Any]:
        """Handler para interrupção do usuário"""
        return {
            "recovered": True,
            "message": "⏸️  Execução interrompida pelo usuário",
            "suggestion": "Pressione Enter para continuar ou Ctrl+C novamente para sair",
            "action": "pause"
        }
    
    def _handle_generic_error(self, error: Exception, context: str) -> Dict[str, Any]:
        """Handler genérico para erros não específicos"""
        return {
            "recovered": False,
            "message": f"⚠️  Erro inesperado: {type(error).__name__}",
            "suggestion": "Consulte o log para mais detalhes",
            "action": "log",
            "details": str(error)
        }
    
    def safe_execute(self, func: Callable, *args, context: str = "", 
                    default_return: Any = None, **kwargs) -> Any:
        """
        Executa uma função com tratamento de erros
        
        Args:
            func: Função a executar
            *args: Argumentos da função
            context: Contexto para logging
            default_return: Valor a retornar em caso de erro
            **kwargs: Argumentos nomeados da função
            
        Returns:
            Resultado da função ou default_return em caso de erro
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            result = self.handle_error(e, context or func.__name__)
            
            # Se recuperou, tenta ação sugerida
            if result and result.get("recovered"):
                action = result.get("action")
                
                if action == "retry":
                    # Tenta novamente uma vez
                    try:
                        return func(*args, **kwargs)
                    except:
                        return default_return
                elif action == "default":
                    return default_return
                elif action == "skip":
                    return None
            
            return default_return


def error_handler(handler_instance: Optional[ErrorHandler] = None, 
                 context: str = "", severity: str = "medium",
                 default_return: Any = None):
    """
    Decorator para tratamento automático de erros
    
    Args:
        handler_instance: Instância do ErrorHandler
        context: Contexto do erro
        severity: Severidade do erro
        default_return: Valor a retornar em caso de erro
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if handler_instance:
                return handler_instance.safe_execute(
                    func, *args, 
                    context=context or func.__name__,
                    default_return=default_return,
                    **kwargs
                )
            else:
                # Sem handler, executa normalmente
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"❌ Erro em {func.__name__}: {str(e)}")
                    return default_return
        return wrapper
    return decorator


class UserFriendlyError:
    """Classe para exibir erros amigáveis ao usuário"""
    
    @staticmethod
    def show_error(error_result: Dict[str, Any], ui_component: Optional[Any] = None):
        """
        Exibe erro de forma amigável ao usuário
        
        Args:
            error_result: Resultado do handler de erro
            ui_component: Componente UI para exibição (opcional)
        """
        if not error_result:
            return
        
        message = error_result.get("message", "Erro desconhecido")
        suggestion = error_result.get("suggestion", "")
        
        error_display = [
            "",
            "=" * 60,
            message,
            "=" * 60
        ]
        
        if suggestion:
            error_display.extend([
                "",
                f"💡 Sugestão: {suggestion}"
            ])
        
        if error_result.get("details"):
            error_display.extend([
                "",
                f"📋 Detalhes: {error_result['details']}"
            ])
        
        error_display.append("")
        
        if ui_component and hasattr(ui_component, 'alert'):
            ui_component.alert("\n".join(error_display), "❌", "error")
        else:
            print("\n".join(error_display))
    
    @staticmethod
    def create_recovery_menu(options: list) -> str:
        """
        Cria menu de recuperação de erro
        
        Args:
            options: Lista de opções de recuperação
            
        Returns:
            Opção escolhida
        """
        print("\n🔧 OPÇÕES DE RECUPERAÇÃO:")
        print("-" * 30)
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        while True:
            try:
                choice = input("\n👉 Escolha uma opção: ").strip()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    return options[int(choice) - 1]
                print("❌ Opção inválida!")
            except KeyboardInterrupt:
                return "Cancelar"