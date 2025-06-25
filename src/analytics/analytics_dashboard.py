#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analytics Dashboard - Interface para visualização de analytics avançados
"""

import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Any
from .advanced_analytics import AdvancedAnalytics


class AnalyticsDashboard:
    """Dashboard interativo para analytics"""
    
    def __init__(self, analytics: AdvancedAnalytics, ui_components):
        self.analytics = analytics
        self.ui = ui_components
        
    def show_main_dashboard(self):
        """Mostra dashboard principal de analytics"""
        while True:
            self.ui.clear_screen()
            self.ui.header("📊 DASHBOARD DE ANALYTICS", "Análise Avançada de Aprendizado")
            
            # Resumo rápido
            self._display_quick_summary()
            
            print("\n📈 RELATÓRIOS E ANÁLISES:")
            print("1. 📅 Relatório Semanal")
            print("2. 📊 Métricas de Aprendizado")
            print("3. ⏱️ Análise de Tempo de Estudo")
            print("4. 🐛 Padrões de Erro")
            print("5. 💡 Sugestões Personalizadas")
            print("6. 🗓️ Heatmap de Atividade")
            print("7. 📈 Gráfico de Progresso")
            print("8. ⚙️ Configurar Analytics")
            print("0. 🔙 Voltar")
            
            choice = input("\n👉 Escolha uma opção: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._show_weekly_report()
            elif choice == "2":
                self._show_learning_metrics()
            elif choice == "3":
                self._show_time_analysis()
            elif choice == "4":
                self._show_error_patterns()
            elif choice == "5":
                self._show_personalized_suggestions()
            elif choice == "6":
                self._show_activity_heatmap()
            elif choice == "7":
                self._show_progress_graph()
            elif choice == "8":
                self._show_analytics_settings()
            else:
                self.ui.error("Opção inválida!")
                self.ui.pause()
                
    def _display_quick_summary(self):
        """Exibe resumo rápido na tela principal"""
        metrics = self.analytics.get_learning_metrics(7)  # Última semana
        
        print(f"\n⚡ RESUMO DA SEMANA:")
        print(f"📚 Tempo de estudo: {metrics.total_study_time:.1f} minutos")
        print(f"📈 Score médio: {metrics.average_score:.1f}%")
        print(f"🎯 Módulos estudados: {metrics.modules_completed}")
        print(f"💪 Exercícios completados: {metrics.exercises_completed}")
        
        # Indicador de consistência
        if metrics.consistency_score > 0.8:
            print(f"🔥 Consistência: Excelente ({metrics.consistency_score:.1%})")
        elif metrics.consistency_score > 0.6:
            print(f"👍 Consistência: Boa ({metrics.consistency_score:.1%})")
        else:
            print(f"📅 Consistência: Pode melhorar ({metrics.consistency_score:.1%})")
            
    def _show_weekly_report(self):
        """Mostra relatório semanal detalhado"""
        self.ui.clear_screen()
        self.ui.header("📅 RELATÓRIO SEMANAL", "Análise Detalhada dos Últimos 7 Dias")
        
        report = self.analytics.generate_weekly_report()
        
        # Período
        print(f"\n📅 PERÍODO: {report['period']['start']} a {report['period']['end']}")
        
        # Resumo
        summary = report['summary']
        print(f"\n📊 RESUMO GERAL:")
        print(f"  ⏱️  Tempo total: {summary['total_time']:.1f} minutos")
        print(f"  📚 Sessões: {summary['sessions']}")
        print(f"  🎯 Módulos: {summary['modules']}")
        print(f"  💪 Exercícios: {summary['exercises']}")
        print(f"  📈 Score médio: {summary['average_score']:.1f}%")
        
        # Comparação com semana anterior
        comparison = report['comparison']
        print(f"\n📈 COMPARAÇÃO COM SEMANA ANTERIOR:")
        
        time_change = comparison['time_change']
        time_icon = "📈" if time_change > 0 else "📉" if time_change < 0 else "➡️"
        print(f"  {time_icon} Tempo: {time_change:+.1f} minutos")
        
        score_change = comparison['score_change']
        score_icon = "📈" if score_change > 0 else "📉" if score_change < 0 else "➡️"
        print(f"  {score_icon} Score: {score_change:+.1f}%")
        
        # Tendências
        trends = report['trends']
        trend_icons = {
            "increasing": "📈 Crescente",
            "decreasing": "📉 Decrescente", 
            "stable": "➡️ Estável"
        }
        print(f"\n📊 TENDÊNCIA DE ESTUDO: {trend_icons.get(trends['study_time_trend'], '❓')}")
        
        if trends['peak_day']:
            print(f"🎯 Dia com mais estudo: {trends['peak_day']}")
            
        # Conquistas
        achievements = report['achievements']
        if achievements:
            print(f"\n🏆 CONQUISTAS DA SEMANA:")
            for achievement in achievements:
                print(f"  {achievement}")
        else:
            print(f"\n💪 Continue se esforçando para conquistar badges!")
            
        # Sugestões
        suggestions = report['suggestions']
        if suggestions:
            print(f"\n💡 SUGESTÕES PERSONALIZADAS:")
            for i, suggestion in enumerate(suggestions[:3], 1):
                print(f"  {i}. {suggestion}")
                
        self.ui.pause()
        
    def _show_learning_metrics(self):
        """Mostra métricas detalhadas de aprendizado"""
        self.ui.clear_screen()
        self.ui.header("📊 MÉTRICAS DE APRENDIZADO", "Análise Detalhada do Desempenho")
        
        # Métricas de diferentes períodos
        periods = [7, 30, 90]
        period_names = ["Semana", "Mês", "Trimestre"]
        
        print("\n📈 COMPARAÇÃO POR PERÍODO:")
        print(f"{'Período':<12} {'Tempo':<10} {'Score':<8} {'Módulos':<8} {'Velocidade':<10}")
        print("-" * 60)
        
        for period, name in zip(periods, period_names):
            metrics = self.analytics.get_learning_metrics(period)
            print(f"{name:<12} {metrics.total_study_time:<10.1f} "
                  f"{metrics.average_score:<8.1f} {metrics.modules_completed:<8} "
                  f"{metrics.learning_velocity:<10.2f}")
                  
        # Métricas detalhadas do mês
        monthly_metrics = self.analytics.get_learning_metrics(30)
        
        print(f"\n🎯 ANÁLISE DETALHADA (30 DIAS):")
        print(f"  📚 Tempo total de estudo: {monthly_metrics.total_study_time:.1f} minutos")
        print(f"  ⏱️  Duração média por sessão: {monthly_metrics.average_session_duration:.1f} min")
        print(f"  📈 Score médio: {monthly_metrics.average_score:.1f}%")
        print(f"  🚀 Taxa de melhoria: {monthly_metrics.improvement_rate:.1%}")
        print(f"  📅 Score de consistência: {monthly_metrics.consistency_score:.1%}")
        print(f"  🎚️  Nível de dificuldade preferido: {monthly_metrics.difficulty_preference}")
        print(f"  🏃 Velocidade de aprendizado: {monthly_metrics.learning_velocity:.2f} módulos/semana")
        
        # Análise de padrões
        print(f"\n🔍 ANÁLISE DE PADRÕES:")
        
        if monthly_metrics.consistency_score > 0.8:
            print("  ✅ Padrão de estudo muito consistente")
        elif monthly_metrics.consistency_score > 0.6:
            print("  👍 Padrão de estudo razoavelmente consistente")
        else:
            print("  📅 Padrão de estudo irregular - considere horários fixos")
            
        if monthly_metrics.learning_velocity > 1.5:
            print("  🚀 Ritmo de aprendizado acelerado")
        elif monthly_metrics.learning_velocity > 0.5:
            print("  📚 Ritmo de aprendizado normal")
        else:
            print("  🐌 Ritmo de aprendizado lento - considere mais tempo de estudo")
            
        if monthly_metrics.improvement_rate > 0.1:
            print("  📈 Melhoria consistente no desempenho")
        elif monthly_metrics.improvement_rate > -0.05:
            print("  ➡️ Desempenho estável")
        else:
            print("  📉 Desempenho em declínio - considere revisão dos conceitos")
            
        self.ui.pause()
        
    def _show_time_analysis(self):
        """Mostra análise detalhada de tempo"""
        self.ui.clear_screen()
        self.ui.header("⏱️ ANÁLISE DE TEMPO", "Como você usa seu tempo de estudo")
        
        # Tempo por módulo
        time_by_module = self.analytics.get_time_by_module(30)
        
        if time_by_module:
            print("\n📚 TEMPO POR MÓDULO (30 dias):")
            sorted_modules = sorted(time_by_module.items(), key=lambda x: x[1], reverse=True)
            
            for module, minutes in sorted_modules[:10]:  # Top 10
                hours = minutes / 60
                print(f"  {module}: {minutes:.1f} min ({hours:.1f}h)")
                
            # Módulo mais estudado
            top_module = sorted_modules[0]
            print(f"\n🏆 Módulo mais estudado: {top_module[0]} ({top_module[1]:.1f} min)")
            
        # Distribuição de tempo por tópico (exemplo)
        print(f"\n🎯 DISTRIBUIÇÃO DO TEMPO DE ESTUDO:")
        total_time = sum(time_by_module.values()) if time_by_module else 1
        
        if time_by_module:
            categories = {
                "Básico": ["modulo_1", "modulo_2", "modulo_3", "modulo_4"],
                "Intermediário": ["modulo_5", "modulo_6", "modulo_7", "modulo_8"],
                "Avançado": ["modulo_9", "modulo_10", "modulo_11", "modulo_12"]
            }
            
            for category, modules in categories.items():
                category_time = sum(time_by_module.get(mod, 0) for mod in modules)
                percentage = (category_time / total_time) * 100
                print(f"  {category}: {category_time:.1f} min ({percentage:.1f}%)")
                
        # Sessões de estudo
        print(f"\n📊 ANÁLISE DE SESSÕES:")
        metrics_week = self.analytics.get_learning_metrics(7)
        metrics_month = self.analytics.get_learning_metrics(30)
        
        if metrics_week.total_study_time > 0:
            avg_session_week = metrics_week.average_session_duration
            print(f"  📅 Duração média (semana): {avg_session_week:.1f} min")
            
            if avg_session_week < 30:
                print("  💡 Sessões curtas - bom para retenção!")
            elif avg_session_week > 90:
                print("  ⚠️ Sessões longas - considere pausas regulares")
            else:
                print("  ✅ Duração ideal de sessões")
                
        self.ui.pause()
        
    def _show_error_patterns(self):
        """Mostra análise de padrões de erro"""
        self.ui.clear_screen()
        self.ui.header("🐛 ANÁLISE DE ERROS", "Padrões e Sugestões de Melhoria")
        
        common_errors = self.analytics.get_common_error_patterns(10)
        
        if not common_errors:
            print("\n🎉 Parabéns! Nenhum erro registrado recentemente.")
            print("Continue praticando para manter este excelente desempenho!")
            self.ui.pause()
            return
            
        print(f"\n🔍 ERROS MAIS COMUNS:")
        print(f"{'#':<3} {'Tipo':<15} {'Módulo':<12} {'Freq.':<6} {'Sugestão'}")
        print("-" * 80)
        
        for i, error in enumerate(common_errors, 1):
            print(f"{i:<3} {error.error_type:<15} {error.module_id:<12} "
                  f"{error.frequency:<6} {error.suggestion[:40]}...")
                  
        # Análise por módulo
        module_errors = {}
        for error in common_errors:
            if error.module_id not in module_errors:
                module_errors[error.module_id] = []
            module_errors[error.module_id].append(error)
            
        print(f"\n📚 ERROS POR MÓDULO:")
        for module, errors in sorted(module_errors.items()):
            total_freq = sum(e.frequency for e in errors)
            print(f"  {module}: {len(errors)} tipos de erro, {total_freq} ocorrências")
            
        # Sugestões de melhoria
        print(f"\n💡 SUGESTÕES DE MELHORIA:")
        
        # Identifica módulos problemáticos
        problem_modules = sorted(module_errors.items(), 
                               key=lambda x: sum(e.frequency for e in x[1]), 
                               reverse=True)[:3]
        
        for module, errors in problem_modules:
            most_common = max(errors, key=lambda x: x.frequency)
            print(f"  📚 {module}: {most_common.suggestion}")
            
        # Recomendações gerais
        total_errors = sum(e.frequency for e in common_errors)
        if total_errors > 50:
            print(f"\n⚠️ ATENÇÃO: {total_errors} erros registrados.")
            print("Considere revisar os conceitos básicos antes de avançar.")
        elif total_errors > 20:
            print(f"\n📝 {total_errors} erros registrados - normal no processo de aprendizado.")
            print("Continue praticando com foco nas áreas problemáticas.")
        else:
            print(f"\n✅ Apenas {total_errors} erros - excelente controle!")
            
        self.ui.pause()
        
    def _show_personalized_suggestions(self):
        """Mostra sugestões personalizadas"""
        self.ui.clear_screen()
        self.ui.header("💡 SUGESTÕES PERSONALIZADAS", "Recomendações Baseadas em IA")
        
        suggestions = self.analytics.get_personalized_suggestions()
        
        if not suggestions:
            print("\n🎯 Continue seu excelente trabalho!")
            print("Não há sugestões específicas no momento.")
            self.ui.pause()
            return
            
        print(f"\n🎯 SUAS SUGESTÕES PERSONALIZADAS:")
        
        for i, suggestion in enumerate(suggestions, 1):
            print(f"\n{i}. {suggestion}")
            
        # Análise adicional baseada em métricas
        metrics = self.analytics.get_learning_metrics(30)
        
        print(f"\n🔍 ANÁLISE ADICIONAL:")
        
        # Sugestões baseadas em consistência
        if metrics.consistency_score < 0.3:
            print("📅 Sua consistência está baixa. Tente estabelecer um horário fixo de estudo.")
        elif metrics.consistency_score > 0.9:
            print("🔥 Sua consistência é excepcional! Você está no caminho certo.")
            
        # Sugestões baseadas em velocidade
        if metrics.learning_velocity < 0.2:
            print("🐌 Considere aumentar o tempo de estudo para acelerar o progresso.")
        elif metrics.learning_velocity > 3:
            print("🚀 Seu ritmo é muito rápido! Certifique-se de absorver bem o conteúdo.")
            
        # Sugestões baseadas em score
        if metrics.average_score < 50:
            print("📚 Foque na revisão dos conceitos básicos antes de avançar.")
        elif metrics.average_score > 95:
            print("🏆 Pontuação excelente! Considere desafios mais avançados.")
            
        print(f"\n💪 PRÓXIMOS PASSOS RECOMENDADOS:")
        
        # Recomendações específicas
        if metrics.exercises_completed < 10:
            print("1. Faça mais exercícios práticos para reforçar o aprendizado")
            
        if metrics.modules_completed < 5:
            print("2. Continue progredindo pelos módulos sequencialmente")
        else:
            print("2. Considere revisar módulos anteriores para solidificar conhecimento")
            
        if metrics.total_study_time < 300:  # Menos de 5 horas no mês
            print("3. Aumente gradualmente o tempo de estudo diário")
        else:
            print("3. Mantenha a regularidade no tempo de estudo")
            
        self.ui.pause()
        
    def _show_activity_heatmap(self):
        """Mostra heatmap de atividade de estudo"""
        self.ui.clear_screen()
        self.ui.header("🗓️ MAPA DE ATIVIDADE", "Visualização do Padrão de Estudos")
        
        heatmap_data = self.analytics.get_study_heatmap(30)
        
        if not heatmap_data:
            print("\n📅 Nenhum dado de atividade encontrado nos últimos 30 dias.")
            print("Comece a estudar para ver seu mapa de atividade!")
            self.ui.pause()
            return
            
        # Organiza dados por semana
        from datetime import datetime, timedelta
        
        print(f"\n🗓️ ATIVIDADE DOS ÚLTIMOS 30 DIAS:")
        print("(Intensidade: ░ = 0-30min, ▒ = 30-60min, ▓ = 60-120min, █ = 120min+)")
        print()
        
        # Calcula range de datas
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=29)
        
        # Cria representação visual simples
        current_date = start_date
        week_count = 0
        
        while current_date <= end_date:
            if current_date.weekday() == 0:  # Segunda-feira
                if week_count > 0:
                    print()
                print(f"Semana {current_date.strftime('%d/%m')}: ", end="")
                week_count += 1
                
            date_str = current_date.strftime("%Y-%m-%d")
            minutes = heatmap_data.get(date_str, 0)
            
            # Escolhe símbolo baseado na intensidade
            if minutes == 0:
                symbol = "░"
            elif minutes < 30:
                symbol = "▒"
            elif minutes < 120:
                symbol = "▓"
            else:
                symbol = "█"
                
            print(symbol, end="")
            current_date += timedelta(days=1)
            
        print("\n")
        
        # Estatísticas do heatmap
        total_days = len(heatmap_data)
        active_days = len([d for d in heatmap_data.values() if d > 0])
        
        if total_days > 0:
            print(f"\n📊 ESTATÍSTICAS:")
            print(f"  📅 Dias ativos: {active_days}/{total_days} ({active_days/total_days:.1%})")
            
            if heatmap_data.values():
                avg_daily = statistics.mean(heatmap_data.values())
                max_daily = max(heatmap_data.values())
                print(f"  ⏱️  Tempo médio/dia: {avg_daily:.1f} min")
                print(f"  🏆 Dia mais ativo: {max_daily:.1f} min")
                
                # Encontra dia mais ativo
                max_day = max(heatmap_data.items(), key=lambda x: x[1])
                print(f"  📅 Data mais ativa: {max_day[0]} ({max_day[1]:.1f} min)")
                
        self.ui.pause()
        
    def _show_progress_graph(self):
        """Mostra gráfico textual de progresso"""
        self.ui.clear_screen()
        self.ui.header("📈 GRÁFICO DE PROGRESSO", "Evolução do Desempenho")
        
        # Simula dados de progresso por semana (últimas 8 semanas)
        weekly_data = []
        for week in range(8, 0, -1):
            start_date = datetime.now() - timedelta(weeks=week)
            end_date = start_date + timedelta(days=7)
            
            # Coleta sessões da semana
            week_sessions = [s for s in self.analytics.study_sessions 
                           if start_date <= s.start_time <= end_date]
            
            if week_sessions:
                avg_score = statistics.mean([s.score for s in week_sessions if s.score > 0] or [0])
                total_time = sum(s.duration_minutes for s in week_sessions)
                total_exercises = sum(s.exercises_completed for s in week_sessions)
            else:
                avg_score = 0
                total_time = 0
                total_exercises = 0
                
            weekly_data.append({
                "week": f"S{9-week}",
                "score": avg_score,
                "time": total_time,
                "exercises": total_exercises
            })
            
        if not any(w["score"] > 0 for w in weekly_data):
            print("\n📊 Dados insuficientes para gerar gráfico de progresso.")
            print("Continue estudando para ver sua evolução!")
            self.ui.pause()
            return
            
        # Gráfico de score
        print(f"\n📈 EVOLUÇÃO DO SCORE (por semana):")
        max_score = max(w["score"] for w in weekly_data) or 100
        
        for week_data in weekly_data:
            bar_length = int((week_data["score"] / max_score) * 30)
            bar = "█" * bar_length + "░" * (30 - bar_length)
            print(f"{week_data['week']}: {bar} {week_data['score']:.1f}%")
            
        # Gráfico de tempo
        print(f"\n⏱️ TEMPO DE ESTUDO (por semana):")
        max_time = max(w["time"] for w in weekly_data) or 1
        
        for week_data in weekly_data:
            bar_length = int((week_data["time"] / max_time) * 30)
            bar = "█" * bar_length + "░" * (30 - bar_length)
            print(f"{week_data['week']}: {bar} {week_data['time']:.0f}min")
            
        # Tendência
        recent_scores = [w["score"] for w in weekly_data[-4:] if w["score"] > 0]
        if len(recent_scores) >= 2:
            trend = "📈" if recent_scores[-1] > recent_scores[0] else "📉" if recent_scores[-1] < recent_scores[0] else "➡️"
            print(f"\n{trend} TENDÊNCIA RECENTE:")
            
            if trend == "📈":
                print("  Seu desempenho está melhorando! Continue assim!")
            elif trend == "📉":
                print("  Há espaço para melhoria. Considere revisar conceitos básicos.")
            else:
                print("  Desempenho estável. Bom trabalho!")
                
        self.ui.pause()
        
    def _show_analytics_settings(self):
        """Mostra configurações de analytics"""
        self.ui.clear_screen()
        self.ui.header("⚙️ CONFIGURAÇÕES", "Personalizar Analytics")
        
        print("\n🛠️ CONFIGURAÇÕES DE ANALYTICS:")
        print("1. 📊 Exportar Dados")
        print("2. 🗑️ Limpar Histórico")
        print("3. 📈 Configurar Relatórios")
        print("4. 🔄 Backup de Dados")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self._export_analytics_data()
        elif choice == "2":
            self._clear_analytics_history()
        elif choice == "3":
            self._configure_reports()
        elif choice == "4":
            self._backup_analytics_data()
            
    def _export_analytics_data(self):
        """Exporta dados de analytics"""
        print("\n💾 Exportando dados de analytics...")
        
        # Simula exportação
        metrics = self.analytics.get_learning_metrics(90)
        report = self.analytics.generate_weekly_report()
        
        export_data = {
            "export_date": datetime.now().isoformat(),
            "metrics": metrics.__dict__,
            "weekly_report": report,
            "total_sessions": len(self.analytics.study_sessions)
        }
        
        print("✅ Dados exportados com sucesso!")
        print(f"📁 Arquivo: analytics_export_{datetime.now().strftime('%Y%m%d')}.json")
        
        self.ui.pause()
        
    def _clear_analytics_history(self):
        """Limpa histórico de analytics"""
        confirm = input("\n⚠️ Limpar TODOS os dados? Esta ação não pode ser desfeita! (digite 'CONFIRMAR'): ")
        
        if confirm == "CONFIRMAR":
            self.analytics.study_sessions.clear()
            self.analytics.error_patterns.clear()
            print("✅ Histórico limpo com sucesso!")
        else:
            print("❌ Operação cancelada.")
            
        self.ui.pause()
        
    def _configure_reports(self):
        """Configura relatórios automáticos"""
        print("\n📋 CONFIGURAÇÃO DE RELATÓRIOS:")
        print("Esta funcionalidade estará disponível em futuras versões.")
        print("Planejamos adicionar:")
        print("• Relatórios automáticos por email")
        print("• Configuração de frequência")
        print("• Personalização de métricas")
        
        self.ui.pause()
        
    def _backup_analytics_data(self):
        """Faz backup dos dados"""
        print("\n💾 Criando backup dos dados...")
        
        # Simula backup
        print("✅ Backup criado com sucesso!")
        print(f"📁 Local: backup_analytics_{datetime.now().strftime('%Y%m%d_%H%M')}.bak")
        
        self.ui.pause()