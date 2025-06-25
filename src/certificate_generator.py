#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Certificados
Cria certificados de conclusão em HTML e PDF
"""

import os
import uuid
from datetime import datetime
from typing import Dict, Any, Optional
import webbrowser
import tempfile


class CertificateGenerator:
    """Gera certificados de conclusão do curso"""
    
    def __init__(self, template_file: str = "certificate_template.html"):
        self.template_file = template_file
        self.template_content = self._load_template()
    
    def _load_template(self) -> str:
        """Carrega o template HTML do certificado"""
        if os.path.exists(self.template_file):
            try:
                with open(self.template_file, 'r', encoding='utf-8') as f:
                    return f.read()
            except IOError as e:
                print(f"Erro ao carregar template: {e}")
                return self._get_default_template()
        return self._get_default_template()
    
    def _get_default_template(self) -> str:
        """Retorna um template padrão simples"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Certificado - Curso de Python</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                h1 { color: #3776ab; }
                .student-name { font-size: 32px; color: #3776ab; margin: 20px 0; }
                .info { margin: 20px 0; }
            </style>
        </head>
        <body>
            <h1>CERTIFICADO DE CONCLUSÃO</h1>
            <p>Certificamos que</p>
            <p class="student-name">{{NOME_ALUNO}}</p>
            <p>concluiu com êxito o Curso Interativo de Python</p>
            <div class="info">
                <p>Módulos Completos: {{MODULOS_COMPLETOS}}</p>
                <p>Pontuação Total: {{PONTUACAO_TOTAL}}</p>
                <p>Aproveitamento: {{PERCENTUAL}}%</p>
                <p>Data: {{DATA_CONCLUSAO}}</p>
            </div>
            <p>ID: {{CERTIFICADO_ID}}</p>
        </body>
        </html>
        """
    
    def generate_certificate(self, user_data: Dict[str, Any]) -> str:
        """
        Gera o certificado com os dados do usuário
        Retorna o caminho do arquivo gerado
        """
        # Prepara os dados para substituição
        certificate_data = {
            'NOME_ALUNO': user_data.get('user_name', 'Aluno'),
            'MODULOS_COMPLETOS': str(user_data.get('modules_completed', 0)),
            'PONTUACAO_TOTAL': str(user_data.get('total_score', 0)),
            'PERCENTUAL': str(int(user_data.get('completion_percentage', 0))),
            'DATA_CONCLUSAO': datetime.now().strftime('%d de %B de %Y'),
            'CERTIFICADO_ID': self._generate_certificate_id()
        }
        
        # Substitui os placeholders
        html_content = self.template_content
        for key, value in certificate_data.items():
            html_content = html_content.replace(f'{{{{{key}}}}}', value)
        
        # Traduz o mês para português
        months_pt = {
            'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
            'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
            'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
            'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
        }
        
        for en, pt in months_pt.items():
            html_content = html_content.replace(en, pt)
        
        # Salva o certificado
        filename = f"certificado_{user_data.get('user_name', 'aluno').replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.html"
        filepath = os.path.join(os.getcwd(), filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            return filepath
        except IOError as e:
            print(f"Erro ao salvar certificado: {e}")
            return ""
    
    def _generate_certificate_id(self) -> str:
        """Gera um ID único para o certificado"""
        return f"PY-{datetime.now().strftime('%Y%m')}-{str(uuid.uuid4())[:8].upper()}"
    
    def preview_certificate(self, user_data: Dict[str, Any]) -> None:
        """Gera e abre o certificado no navegador para visualização"""
        filepath = self.generate_certificate(user_data)
        if filepath and os.path.exists(filepath):
            # Abre no navegador padrão
            webbrowser.open(f'file://{os.path.abspath(filepath)}')
            print(f"\n✅ Certificado gerado: {filepath}")
            print("📄 O certificado foi aberto no seu navegador.")
            print("💡 Dica: Use Ctrl+P para imprimir ou salvar como PDF")
        else:
            print("\n❌ Erro ao gerar o certificado")
    
    def can_generate_certificate(self, progress_data: Dict[str, Any]) -> bool:
        """Verifica se o aluno pode gerar certificado"""
        # Requer pelo menos 80% de conclusão
        completion = progress_data.get('completion_percentage', 0)
        return completion >= 80
    
    def export_to_pdf(self, html_filepath: str) -> Optional[str]:
        """
        Exporta o certificado HTML para PDF
        Requer biblioteca adicional (weasyprint ou similar)
        """
        try:
            # Tenta usar weasyprint se disponível
            from weasyprint import HTML
            
            pdf_filepath = html_filepath.replace('.html', '.pdf')
            HTML(filename=html_filepath).write_pdf(pdf_filepath)
            
            print(f"\n✅ PDF gerado: {pdf_filepath}")
            return pdf_filepath
            
        except ImportError:
            print("\n⚠️  Para exportar em PDF, instale: pip install weasyprint")
            print("💡 Alternativamente, use Ctrl+P no navegador e escolha 'Salvar como PDF'")
            return None
        except Exception as e:
            print(f"\n❌ Erro ao gerar PDF: {e}")
            return None
    
    def generate_completion_report(self, progress_data: Dict[str, Any]) -> str:
        """Gera relatório de conclusão em texto"""
        report = f"""
╔══════════════════════════════════════════════════════════╗
║           RELATÓRIO DE CONCLUSÃO DO CURSO                ║
╚══════════════════════════════════════════════════════════╝

👤 Aluno: {progress_data.get('user_name', 'Não informado')}
📅 Data de Início: {progress_data.get('start_date', 'N/A')[:10]}
📅 Data de Conclusão: {datetime.now().strftime('%Y-%m-%d')}

📊 ESTATÍSTICAS DO CURSO:
├─ Módulos Completados: {progress_data.get('modules_completed', 0)} de 11
├─ Percentual de Conclusão: {progress_data.get('completion_percentage', 0):.1f}%
├─ Pontuação Total: {progress_data.get('total_score', 0)} pontos
├─ Tempo Total de Estudo: {progress_data.get('total_time_spent', 0) // 60} minutos
└─ Conquistas Desbloqueadas: {progress_data.get('achievements', 0)}

📈 DESEMPENHO POR MÓDULO:
"""
        
        # Adiciona detalhes dos módulos
        modules_progress = progress_data.get('modules_progress', {})
        for module_id, module_data in modules_progress.items():
            if module_data.get('completed'):
                module_num = module_id.split('_')[1]
                score = module_data.get('score', 0)
                attempts = module_data.get('attempts', 0)
                report += f"├─ Módulo {module_num}: ✅ Completo | Pontos: {score} | Tentativas: {attempts}\n"
        
        report += f"""
🏆 CONQUISTAS:
"""
        achievements = progress_data.get('achievements_list', [])
        if achievements:
            for achievement in achievements:
                report += f"├─ {achievement.get('name', 'Conquista')}\n"
        else:
            report += "└─ Nenhuma conquista registrada\n"
        
        report += """
═══════════════════════════════════════════════════════════
        """
        
        return report