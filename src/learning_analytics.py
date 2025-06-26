#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Análise de Aprendizagem
Analisa padrões, identifica dificuldades e gera relatórios personalizados
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict, Counter
import statistics


class LearningAnalytics:
    """Sistema de análise e insights de aprendizagem"""
    
    def __init__(self, progress_manager):
        self.progress = progress_manager
        self.analytics_file = "analytics.json"
        self.analytics_data = self._load_analytics()
        
    def _load_analytics(self) -> Dict[str, Any]:
        """Carrega dados de análise salvos"""
        if os.path.exists(self.analytics_file):
            try:
                with open(self.analytics_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self._create_default_analytics()
        return self._create_default_analytics()
    
    def _create_default_analytics(self) -> Dict[str, Any]:
        """Cria estrutura padrão de analytics"""
        return {
            "error_patterns": defaultdict(int),
            "module_attempts": defaultdict(list),
            "time_per_module": defaultdict(list),
            "concepts_difficulty": defaultdict(int),
            "learning_path": [],
            "daily_activity": defaultdict(int),
            "achievement_timeline": [],
            "code_submissions": [],
            "help_requests": defaultdict(int)
        }
    
    def save_analytics(self) -> None:
        """Salva dados de análise"""
        # Converter defaultdict para dict normal para JSON
        data_to_save = {
            k: dict(v) if isinstance(v, defaultdict) else v
            for k, v in self.analytics_data.items()
        }
        
        with open(self.analytics_file, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=2, ensure_ascii=False)
    
    def registrar_erro(self, tipo_erro: str, modulo: str, contexto: str = "") -> None:
        """Registra um erro para análise de padrões"""
        self.analytics_data["error_patterns"][tipo_erro] += 1
        self.analytics_data["concepts_difficulty"][modulo] += 1
        
        # Registra contexto do erro
        erro_completo = {
            "tipo": tipo_erro,
            "modulo": modulo,
            "contexto": contexto,
            "timestamp": datetime.now().isoformat()
        }
        
        if "erros_detalhados" not in self.analytics_data:
            self.analytics_data["erros_detalhados"] = []
        
        self.analytics_data["erros_detalhados"].append(erro_completo)
        self.save_analytics()
    
    def registrar_tempo_modulo(self, modulo: str, tempo_segundos: int) -> None:
        """Registra tempo gasto em um módulo"""
        self.analytics_data["time_per_module"][modulo].append(tempo_segundos)
        self.save_analytics()
    
    def registrar_tentativa(self, modulo: str, sucesso: bool, pontos: int = 0) -> None:
        """Registra tentativa em um módulo"""
        tentativa = {
            "sucesso": sucesso,
            "pontos": pontos,
            "timestamp": datetime.now().isoformat()
        }
        self.analytics_data["module_attempts"][modulo].append(tentativa)
        self.save_analytics()
    
    def registrar_ajuda(self, topico: str) -> None:
        """Registra quando aluno pede ajuda"""
        self.analytics_data["help_requests"][topico] += 1
        self.save_analytics()
    
    def registrar_atividade_diaria(self) -> None:
        """Registra atividade do dia"""
        hoje = datetime.now().strftime("%Y-%m-%d")
        self.analytics_data["daily_activity"][hoje] += 1
        self.save_analytics()
    
    def calcular_taxa_sucesso_modulo(self, modulo: str) -> float:
        """Calcula taxa de sucesso em um módulo"""
        tentativas = self.analytics_data["module_attempts"].get(modulo, [])
        if not tentativas:
            return 0.0
        
        sucessos = sum(1 for t in tentativas if t["sucesso"])
        return (sucessos / len(tentativas)) * 100
    
    def calcular_tempo_medio_modulo(self, modulo: str) -> int:
        """Calcula tempo médio gasto em um módulo (segundos)"""
        tempos = self.analytics_data["time_per_module"].get(modulo, [])
        if not tempos:
            return 0
        return int(statistics.mean(tempos))
    
    def identificar_modulos_dificeis(self, limite: int = 3) -> List[Tuple[str, int]]:
        """Identifica módulos com mais dificuldade (mais erros/ajuda)"""
        dificuldades = []
        
        for modulo, erros in self.analytics_data["concepts_difficulty"].items():
            ajudas = self.analytics_data["help_requests"].get(modulo, 0)
            score_dificuldade = erros + (ajudas * 2)  # Ajuda vale mais
            dificuldades.append((modulo, score_dificuldade))
        
        # Ordena por dificuldade (maior primeiro)
        dificuldades.sort(key=lambda x: x[1], reverse=True)
        
        return dificuldades[:limite]
    
    def calcular_velocidade_aprendizado(self) -> Dict[str, Any]:
        """Calcula velocidade de aprendizado"""
        modulos_completos = self.progress.progress_data["modules_completed"]
        
        if not modulos_completos:
            return {"status": "iniciante", "velocidade": 0}
        
        # Tempo desde o início
        inicio = datetime.fromisoformat(self.progress.progress_data["start_date"])
        agora = datetime.now()
        dias_totais = (agora - inicio).days or 1
        
        # Módulos por dia
        modulos_por_dia = len(modulos_completos) / dias_totais
        
        # Classificação
        if modulos_por_dia >= 2:
            status = "muito_rapido"
        elif modulos_por_dia >= 1:
            status = "rapido"
        elif modulos_por_dia >= 0.5:
            status = "moderado"
        else:
            status = "lento"
        
        return {
            "status": status,
            "velocidade": modulos_por_dia,
            "dias_totais": dias_totais,
            "modulos_completos": len(modulos_completos)
        }
    
    def get_learning_insights(self) -> Dict[str, List[str]]:
        """Retorna insights de aprendizado organizados por categoria"""
        insights = {
            "strongest_topics": [],
            "needs_practice": []
        }
        
        try:
            # Analisa módulos com alta taxa de sucesso (pontos fortes)
            for modulo, data in self.analytics_data.get("modules_performance", {}).items():
                tentativas = data.get("attempts", 1)
                sucessos = data.get("successes", 0)
                taxa_sucesso = (sucessos / tentativas) * 100 if tentativas > 0 else 0
                
                if taxa_sucesso >= 80 and tentativas >= 2:
                    modulo_nome = self._format_module_name(modulo)
                    insights["strongest_topics"].append(modulo_nome)
            
            # Analisa módulos com baixa taxa de sucesso (precisa praticar)
            modulos_dificeis = self.identificar_modulos_dificeis()
            for modulo, tentativas in modulos_dificeis[:3]:
                modulo_nome = self._format_module_name(modulo)
                insights["needs_practice"].append(modulo_nome)
            
            # Se não há dados suficientes, adiciona dicas gerais
            if not insights["strongest_topics"]:
                insights["strongest_topics"] = ["Continue praticando para identificar seus pontos fortes"]
            
            if not insights["needs_practice"]:
                insights["needs_practice"] = ["Mantenha a prática regular para melhor aprendizado"]
                
        except Exception as e:
            # Fallback para quando não há dados suficientes
            insights = {
                "strongest_topics": ["Continue estudando para descobrir seus pontos fortes"],
                "needs_practice": ["Pratique regularmente todos os conceitos"]
            }
        
        return insights
    
    def _format_module_name(self, modulo: str) -> str:
        """Formata nome do módulo para exibição"""
        if modulo.startswith("modulo_"):
            num = modulo.replace("modulo_", "")
            return f"Módulo {num}"
        return modulo.title()

    def gerar_insights_personalizados(self) -> List[Dict[str, str]]:
        """Gera insights personalizados baseados nos dados"""
        insights = []
        
        # 1. Padrão de erros
        if self.analytics_data["error_patterns"]:
            erro_mais_comum = max(self.analytics_data["error_patterns"].items(), 
                                 key=lambda x: x[1])
            insights.append({
                "tipo": "erro_comum",
                "titulo": "⚠️ Erro Mais Frequente",
                "descricao": f"Você tem encontrado '{erro_mais_comum[0]}' com frequência ({erro_mais_comum[1]} vezes).",
                "sugestao": "Revise o conceito relacionado e pratique mais exercícios desse tipo."
            })
        
        # 2. Módulos difíceis
        modulos_dificeis = self.identificar_modulos_dificeis()
        if modulos_dificeis:
            mod_nome = modulos_dificeis[0][0]
            insights.append({
                "tipo": "modulo_dificil",
                "titulo": "📚 Módulo Desafiador",
                "descricao": f"O módulo '{mod_nome}' parece ser o mais desafiador para você.",
                "sugestao": "Considere revisar este módulo ou usar o Assistente Python para tirar dúvidas."
            })
        
        # 3. Velocidade de aprendizado
        velocidade = self.calcular_velocidade_aprendizado()
        if velocidade["status"] == "muito_rapido":
            insights.append({
                "tipo": "velocidade",
                "titulo": "🚀 Aprendizado Acelerado!",
                "descricao": f"Você está completando {velocidade['velocidade']:.1f} módulos por dia!",
                "sugestao": "Ótimo ritmo! Certifique-se de praticar os exercícios para fixar o conteúdo."
            })
        elif velocidade["status"] == "lento":
            insights.append({
                "tipo": "velocidade",
                "titulo": "🐢 Ritmo Tranquilo",
                "descricao": "Você está indo no seu próprio ritmo, e isso é ótimo!",
                "sugestao": "Tente dedicar 15-30 minutos por dia para manter o progresso constante."
            })
        
        # 4. Padrão de atividade
        if self.analytics_data["daily_activity"]:
            dias_ativos = len(self.analytics_data["daily_activity"])
            if dias_ativos >= 7:
                insights.append({
                    "tipo": "consistencia",
                    "titulo": "🎯 Consistência é a Chave!",
                    "descricao": f"Você praticou em {dias_ativos} dias diferentes!",
                    "sugestao": "Continue assim! A prática consistente é o segredo do sucesso."
                })
        
        # 5. Uso de ajuda
        total_ajudas = sum(self.analytics_data["help_requests"].values())
        if total_ajudas > 10:
            topico_mais_ajuda = max(self.analytics_data["help_requests"].items(), 
                                  key=lambda x: x[1])
            insights.append({
                "tipo": "ajuda",
                "titulo": "🤝 Buscando Conhecimento",
                "descricao": f"Você pediu ajuda {total_ajudas} vezes, principalmente sobre '{topico_mais_ajuda[0]}'.",
                "sugestao": "Pedir ajuda é sinal de sabedoria! Continue usando o Assistente quando precisar."
            })
        
        return insights
    
    def gerar_relatorio_completo(self) -> Dict[str, Any]:
        """Gera relatório completo de análise"""
        # Dados do progresso
        summary = self.progress.get_progress_summary()
        
        # Estatísticas por módulo
        stats_modulos = {}
        for i in range(1, 27):
            modulo_id = f"modulo_{i}"
            if modulo_id in self.progress.progress_data["modules_progress"]:
                modulo_data = self.progress.progress_data["modules_progress"][modulo_id]
                
                stats_modulos[modulo_id] = {
                    "completo": modulo_data.get("completed", False),
                    "tentativas": modulo_data.get("attempts", 0),
                    "pontos": modulo_data.get("score", 0),
                    "tempo_total": modulo_data.get("time_spent", 0),
                    "taxa_sucesso": self.calcular_taxa_sucesso_modulo(modulo_id),
                    "tempo_medio": self.calcular_tempo_medio_modulo(modulo_id)
                }
        
        # Análise de erros
        erros_ordenados = sorted(
            self.analytics_data["error_patterns"].items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Recomendações
        recomendacoes = self._gerar_recomendacoes()
        
        return {
            "resumo_geral": summary,
            "estatisticas_modulos": stats_modulos,
            "padroes_erro": erros_ordenados[:5],  # Top 5 erros
            "modulos_dificeis": self.identificar_modulos_dificeis(),
            "velocidade_aprendizado": self.calcular_velocidade_aprendizado(),
            "insights": self.gerar_insights_personalizados(),
            "recomendacoes": recomendacoes,
            "tempo_total_estudo": self.progress.progress_data.get("total_time_spent", 0),
            "dias_ativos": len(self.analytics_data["daily_activity"])
        }
    
    def _gerar_recomendacoes(self) -> List[Dict[str, str]]:
        """Gera recomendações personalizadas de estudo"""
        recomendacoes = []
        
        # 1. Módulos para revisar (baixa taxa de sucesso)
        modulos_revisar = []
        for modulo_id in self.progress.progress_data["modules_completed"]:
            taxa = self.calcular_taxa_sucesso_modulo(modulo_id)
            if taxa < 70:  # Menos de 70% de sucesso
                modulos_revisar.append((modulo_id, taxa))
        
        if modulos_revisar:
            modulos_revisar.sort(key=lambda x: x[1])  # Ordena por taxa (menor primeiro)
            pior_modulo = modulos_revisar[0][0]
            recomendacoes.append({
                "tipo": "revisao",
                "prioridade": "alta",
                "titulo": "📖 Revisar Módulo",
                "descricao": f"Recomendamos revisar o {pior_modulo.replace('_', ' ').title()}",
                "acao": f"Use o Modo Revisão (R) focando em {pior_modulo}"
            })
        
        # 2. Próximo módulo recomendado
        proximo_modulo = None
        for i in range(1, 27):
            modulo_id = f"modulo_{i}"
            if modulo_id not in self.progress.progress_data["modules_completed"]:
                proximo_modulo = modulo_id
                break
        
        if proximo_modulo:
            recomendacoes.append({
                "tipo": "proximo_passo",
                "prioridade": "media",
                "titulo": "🎯 Próximo Desafio",
                "descricao": f"Continue com o {proximo_modulo.replace('_', ' ').title()}",
                "acao": f"Escolha a opção {proximo_modulo.split('_')[1]} no menu"
            })
        
        # 3. Prática de conceitos com mais erros
        if self.analytics_data["error_patterns"]:
            erro_comum = max(self.analytics_data["error_patterns"].items(), key=lambda x: x[1])
            if erro_comum[1] > 3:  # Mais de 3 ocorrências
                recomendacoes.append({
                    "tipo": "pratica",
                    "prioridade": "alta",
                    "titulo": "🔧 Praticar Conceito",
                    "descricao": f"Pratique mais sobre {erro_comum[0]}",
                    "acao": "Use o Assistente (A) para exercícios sobre este tema"
                })
        
        # 4. Manter consistência
        dias_inativos = self._calcular_dias_inativos()
        if dias_inativos > 3:
            recomendacoes.append({
                "tipo": "consistencia",
                "prioridade": "media",
                "titulo": "🔄 Retomar Estudos",
                "descricao": f"Você está há {dias_inativos} dias sem praticar",
                "acao": "Dedique 15 minutos hoje para manter o ritmo"
            })
        
        return recomendacoes
    
    def _calcular_dias_inativos(self) -> int:
        """Calcula quantos dias sem atividade"""
        if not self.analytics_data["daily_activity"]:
            return 0
        
        # Última atividade
        datas = sorted(self.analytics_data["daily_activity"].keys())
        ultima_atividade = datetime.strptime(datas[-1], "%Y-%m-%d")
        hoje = datetime.now()
        
        return (hoje - ultima_atividade).days
    
    def exibir_dashboard(self, ui_components) -> None:
        """Exibe dashboard de análise visual"""
        relatorio = self.gerar_relatorio_completo()
        
        ui_components.header("DASHBOARD DE APRENDIZAGEM", 
                           f"Análise Personalizada para {relatorio['resumo_geral']['user_name']}", 
                           "📊")
        
        # Cards principais
        ui_components.section("ESTATÍSTICAS GERAIS", "📈")
        
        # Progresso geral
        print(f"🎯 Progresso Total: {relatorio['resumo_geral']['completion_percentage']:.1f}%")
        print(f"🏆 Pontuação: {relatorio['resumo_geral']['total_score']} pontos")
        print(f"📚 Módulos Completos: {relatorio['resumo_geral']['modules_completed']}/26")
        print(f"⏱️  Tempo Total: {self._formatar_tempo(relatorio['tempo_total_estudo'])}")
        print(f"📅 Dias Ativos: {relatorio['dias_ativos']}")
        
        # Velocidade
        velocidade = relatorio['velocidade_aprendizado']
        status_emoji = {
            "muito_rapido": "🚀",
            "rapido": "✈️",
            "moderado": "🚗",
            "lento": "🚶"
        }
        
        print(f"\n{status_emoji.get(velocidade['status'], '📊')} Ritmo: {velocidade['status'].replace('_', ' ').title()}")
        print(f"   {velocidade['velocidade']:.2f} módulos/dia em {velocidade['dias_totais']} dias")
        
        # Insights
        if relatorio['insights']:
            ui_components.section("INSIGHTS PERSONALIZADOS", "💡")
            for insight in relatorio['insights']:
                ui_components.card(
                    insight['titulo'],
                    f"{insight['descricao']}\n\n💡 {insight['sugestao']}",
                    "🎯",
                    "info"
                )
        
        # Recomendações
        if relatorio['recomendacoes']:
            ui_components.section("RECOMENDAÇÕES DE ESTUDO", "🎓")
            
            # Ordena por prioridade
            recs_ordenadas = sorted(relatorio['recomendacoes'], 
                                  key=lambda x: {"alta": 0, "media": 1, "baixa": 2}[x['prioridade']])
            
            for rec in recs_ordenadas[:3]:  # Top 3 recomendações
                cor = {"alta": "error", "media": "warning", "baixa": "info"}[rec['prioridade']]
                ui_components.alert(
                    f"{rec['titulo']}: {rec['descricao']}\n→ {rec['acao']}",
                    cor
                )
        
        # Padrões de erro
        if relatorio['padroes_erro']:
            ui_components.section("ANÁLISE DE ERROS", "🔍")
            print("Erros mais frequentes:")
            for erro, count in relatorio['padroes_erro'][:3]:
                print(f"   • {erro}: {count} ocorrências")
        
        # Módulos difíceis
        if relatorio['modulos_dificeis']:
            print("\n📚 Módulos que precisam de mais atenção:")
            for modulo, score in relatorio['modulos_dificeis'][:3]:
                print(f"   • {modulo}: dificuldade {score}")
    
    def _formatar_tempo(self, segundos: int) -> str:
        """Formata segundos em formato legível"""
        if segundos < 60:
            return f"{segundos}s"
        elif segundos < 3600:
            return f"{segundos // 60}min"
        else:
            horas = segundos // 3600
            minutos = (segundos % 3600) // 60
            return f"{horas}h {minutos}min"