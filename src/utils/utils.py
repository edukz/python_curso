#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utilitários para o Curso Interativo de Python
Funções auxiliares para interface e interação com o usuário
"""

import os
from typing import Optional, Dict, Any, Union, List


class PythonCourseUtils:
    """Classe com utilitários para o curso de Python"""
    
    def __init__(self):
        self.progress_manager = None
        self.gamification_system = None
    
    @staticmethod
    def limpar_tela() -> None:
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def pausar() -> None:
        """Pausa a execução e espera o usuário pressionar Enter"""
        try:
            input("\n🔸 Pressione ENTER para continuar...")
        except KeyboardInterrupt:
            # Re-lança a exceção para ser tratada no nível superior
            raise
    
    @staticmethod
    def titulo(texto: str) -> None:
        """Exibe um título formatado"""
        print("\n" + "=" * 50)
        print(f"🐍 {texto}")
        print("=" * 50 + "\n")
    
    @staticmethod
    def exemplo(codigo: str) -> None:
        """Exibe um exemplo de código"""
        print("\n📝 EXEMPLO:")
        print("-" * 40)
        print(codigo)
        print("-" * 40)
    
    @staticmethod
    def executar_codigo(codigo: str, namespace: Optional[Dict[str, Any]] = None, ajuda_erros: bool = True) -> None:
        """Executa um código e mostra o resultado com ajuda para erros"""
        print("\n▶️  EXECUTANDO:")
        print("-" * 40)
        try:
            if namespace is None:
                namespace = {}
            exec(codigo, namespace)
        except Exception as e:
            print(f"❌ Erro: {e}")
            
            # Oferece ajuda automática para erros
            if ajuda_erros:
                try:
                    from ..tutor_assistant import ErrorHelper
                    helper = ErrorHelper()
                    helper.ajudar_com_erro(codigo, e)
                except:
                    # Se não conseguir carregar o helper, ignora
                    pass
        print("-" * 40)
    
    @staticmethod
    def exercicio(descricao: str, resposta_esperada: Union[str, List[str]], dica: str = "") -> bool:
        """Propõe um exercício ao aluno"""
        print("\n🎯 EXERCÍCIO:")
        print(descricao)
        if dica:
            print(f"💡 Dica: {dica}")
        
        # Normalizar respostas esperadas para lista
        if isinstance(resposta_esperada, str):
            respostas_validas = [resposta_esperada]
        else:
            respostas_validas = resposta_esperada
        
        tentativas = 0
        max_tentativas = 3
        
        while tentativas < max_tentativas:
            try:
                resposta = input("\n👉 Sua resposta: ").strip()
            except KeyboardInterrupt:
                # Re-lança a exceção para ser tratada no nível superior
                raise
            
            # Verificar se a resposta coincide com qualquer resposta válida
            resposta_correta = any(
                resposta.lower() == resp.lower() 
                for resp in respostas_validas
            )
            
            if resposta_correta:
                print("✅ Correto! Muito bem!")
                return True
            else:
                tentativas += 1
                if tentativas < max_tentativas:
                    print(f"❌ Tente novamente. Tentativas restantes: {max_tentativas - tentativas}")
                else:
                    print(f"❌ Resposta incorreta!")
                    if len(respostas_validas) == 1:
                        print(f"💡 A resposta correta era: {respostas_validas[0]}")
                    else:
                        print(f"💡 Respostas possíveis: {', '.join(respostas_validas)}")
                    print("📚 Não se preocupe, continue estudando!")
                    return False
        
        return False
    
    def set_managers(self, progress_manager, gamification_system):
        """Define os gerenciadores de progresso e gamificação"""
        self.progress_manager = progress_manager
        self.gamification_system = gamification_system
    
    def mini_projeto_completo(self, modulo_id: str, nome_projeto: str, pontos: int = 50) -> None:
        """Registra conclusão de mini projeto com pontuação"""
        print(f"\n🎉 MINI PROJETO CONCLUÍDO!")
        print(f"📚 Módulo: {modulo_id}")
        print(f"🚀 Projeto: {nome_projeto}")
        print(f"⭐ Pontos ganhos: {pontos}")
        
        # Atualiza progresso se gerenciador estiver disponível
        if self.progress_manager:
            self.progress_manager.mark_mini_project_completed(modulo_id, pontos)
        
        # Atualiza gamificação se sistema estiver disponível
        if self.gamification_system:
            self.gamification_system.award_xp(pontos, f"Mini Projeto: {nome_projeto}")
            
            # Conquistas especiais para mini projetos
            mini_projetos_count = len(self.progress_manager.progress_data.get("mini_projetos_completos", []))
            if mini_projetos_count == 1:
                self.gamification_system.unlock_badge("PRIMEIRO_MINI_PROJETO", "🎯", "Primeiro Mini Projeto", "Complete seu primeiro mini projeto")
            elif mini_projetos_count == 5:
                self.gamification_system.unlock_badge("CINCO_PROJETOS", "🏆", "Cinco Projetos", "Complete 5 mini projetos")
            elif mini_projetos_count == 10:
                self.gamification_system.unlock_badge("DEZ_PROJETOS", "💎", "Dez Projetos", "Complete 10 mini projetos")
            elif mini_projetos_count >= 15:
                self.gamification_system.unlock_badge("MESTRE_PROJETOS", "👑", "Mestre dos Projetos", "Complete 15+ mini projetos")
    
    def complete_module(self, module_id: str, pontos: int = 100) -> None:
        """Marca um módulo como completo"""
        print(f"\n🎉 MÓDULO CONCLUÍDO!")
        print(f"📚 {module_id}")
        print(f"⭐ Pontos ganhos: {pontos}")
        print("🚀 Continue para o próximo módulo!")
        
        # Atualiza progresso se gerenciador estiver disponível
        if self.progress_manager:
            self.progress_manager.complete_module(module_id, pontos)
        
        # Atualiza gamificação se sistema estiver disponível
        if self.gamification_system:
            self.gamification_system.award_xp(pontos, f"Módulo {module_id} completo")
            
            # Conquistas especiais para módulos
            completed_count = len(self.progress_manager.progress_data.get("modules_completed", []))
            if completed_count == 1:
                self.gamification_system.unlock_badge("PRIMEIRO_MODULO", "🥇", "Primeiro Módulo", "Complete seu primeiro módulo")
            elif completed_count == 5:
                self.gamification_system.unlock_badge("CINCO_MODULOS", "🏅", "Cinco Módulos", "Complete 5 módulos")
            elif completed_count == 10:
                self.gamification_system.unlock_badge("DEZ_MODULOS", "🏆", "Dez Módulos", "Complete 10 módulos")
            elif completed_count == 20:
                self.gamification_system.unlock_badge("VINTE_MODULOS", "💎", "Vinte Módulos", "Complete 20 módulos")
            elif completed_count >= 30:
                self.gamification_system.unlock_badge("MESTRE_PYTHON", "👑", "Mestre Python", "Complete todos os módulos")
        
        print(f"📈 Progresso atualizado!")
        input("\n⏭️ Pressione ENTER para continuar...")
    
    def exercicio_com_pontuacao(self, descricao: str, resposta_esperada: Union[str, List[str]], 
                               dica: str = "", pontos: int = 10) -> bool:
        """Exercício com sistema de pontuação integrado"""
        resultado = self.exercicio(descricao, resposta_esperada, dica)
        
        if resultado and self.gamification_system:
            self.gamification_system.award_xp(pontos, "Exercício correto")
            if self.progress_manager:
                self.progress_manager.progress_data["total_score"] += pontos
                self.progress_manager.save_progress()
        
        return resultado