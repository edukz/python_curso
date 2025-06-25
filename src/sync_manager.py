#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Sincronização e Backup
Gerencia múltiplos perfis, backup/restore e sincronização opcional
"""

import json
import os
import shutil
import zipfile
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
import csv
from pathlib import Path


class SyncManager:
    """Gerenciador de sincronização e backup"""
    
    def __init__(self):
        self.profiles_dir = "profiles"
        self.backups_dir = "backups"
        self.current_profile = "default"
        self.ensure_directories()
        
    def ensure_directories(self) -> None:
        """Garante que os diretórios necessários existem"""
        os.makedirs(self.profiles_dir, exist_ok=True)
        os.makedirs(self.backups_dir, exist_ok=True)
    
    def get_profile_path(self, profile_name: str) -> str:
        """Retorna caminho do perfil"""
        return os.path.join(self.profiles_dir, profile_name)
    
    def list_profiles(self) -> List[Dict[str, Any]]:
        """Lista todos os perfis disponíveis"""
        profiles = []
        
        if not os.path.exists(self.profiles_dir):
            return profiles
        
        for item in os.listdir(self.profiles_dir):
            profile_path = os.path.join(self.profiles_dir, item)
            if os.path.isdir(profile_path):
                # Lê informações do perfil
                info_file = os.path.join(profile_path, "profile_info.json")
                if os.path.exists(info_file):
                    try:
                        with open(info_file, 'r', encoding='utf-8') as f:
                            info = json.load(f)
                        
                        # Adiciona informações de tamanho
                        progress_file = os.path.join(profile_path, "progress.json")
                        if os.path.exists(progress_file):
                            with open(progress_file, 'r', encoding='utf-8') as f:
                                progress = json.load(f)
                                info["modules_completed"] = len(progress.get("modules_completed", []))
                                info["total_score"] = progress.get("total_score", 0)
                        
                        info["profile_name"] = item
                        profiles.append(info)
                    except:
                        # Perfil corrompido, cria info básica
                        profiles.append({
                            "profile_name": item,
                            "user_name": "Usuário Desconhecido",
                            "created_date": "Data desconhecida",
                            "modules_completed": 0,
                            "total_score": 0
                        })
        
        return sorted(profiles, key=lambda x: x.get("last_access", ""))
    
    def create_profile(self, profile_name: str, user_name: str) -> bool:
        """Cria novo perfil"""
        profile_path = self.get_profile_path(profile_name)
        
        if os.path.exists(profile_path):
            return False  # Perfil já existe
        
        os.makedirs(profile_path, exist_ok=True)
        
        # Cria arquivo de informações do perfil
        profile_info = {
            "user_name": user_name,
            "created_date": datetime.now().isoformat(),
            "last_access": datetime.now().isoformat(),
            "version": "2.0"
        }
        
        info_file = os.path.join(profile_path, "profile_info.json")
        with open(info_file, 'w', encoding='utf-8') as f:
            json.dump(profile_info, f, indent=2, ensure_ascii=False)
        
        return True
    
    def switch_profile(self, profile_name: str) -> bool:
        """Muda para outro perfil"""
        profile_path = self.get_profile_path(profile_name)
        
        if not os.path.exists(profile_path):
            return False
        
        # Salva perfil atual
        self.backup_current_session()
        
        # Muda arquivos para o novo perfil
        files_to_switch = [
            "progress.json",
            "analytics.json",
            "gamification.json",
            "code_history.json"
        ]
        
        for file_name in files_to_switch:
            profile_file = os.path.join(profile_path, file_name)
            current_file = file_name
            
            # Remove arquivo atual se existir
            if os.path.exists(current_file):
                os.remove(current_file)
            
            # Copia do perfil se existir
            if os.path.exists(profile_file):
                shutil.copy2(profile_file, current_file)
        
        # Atualiza último acesso
        self._update_profile_access(profile_name)
        
        self.current_profile = profile_name
        return True
    
    def backup_current_session(self) -> bool:
        """Faz backup da sessão atual"""
        if self.current_profile == "default":
            return True  # Não precisa fazer backup do default
        
        profile_path = self.get_profile_path(self.current_profile)
        
        files_to_backup = [
            "progress.json",
            "analytics.json", 
            "gamification.json",
            "code_history.json"
        ]
        
        for file_name in files_to_backup:
            if os.path.exists(file_name):
                dest_file = os.path.join(profile_path, file_name)
                shutil.copy2(file_name, dest_file)
        
        return True
    
    def _update_profile_access(self, profile_name: str) -> None:
        """Atualiza último acesso do perfil"""
        profile_path = self.get_profile_path(profile_name)
        info_file = os.path.join(profile_path, "profile_info.json")
        
        if os.path.exists(info_file):
            try:
                with open(info_file, 'r', encoding='utf-8') as f:
                    info = json.load(f)
                
                info["last_access"] = datetime.now().isoformat()
                
                with open(info_file, 'w', encoding='utf-8') as f:
                    json.dump(info, f, indent=2, ensure_ascii=False)
            except:
                pass
    
    def export_progress_json(self, filename: Optional[str] = None) -> str:
        """Exporta progresso para JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"backup_python_course_{timestamp}.json"
        
        backup_data = {
            "export_info": {
                "export_date": datetime.now().isoformat(),
                "version": "2.0",
                "profile": self.current_profile
            },
            "files": {}
        }
        
        # Coleta dados de todos os arquivos
        files_to_export = [
            "progress.json",
            "analytics.json",
            "gamification.json", 
            "code_history.json"
        ]
        
        for file_name in files_to_export:
            if os.path.exists(file_name):
                try:
                    with open(file_name, 'r', encoding='utf-8') as f:
                        backup_data["files"][file_name] = json.load(f)
                except:
                    backup_data["files"][file_name] = None
        
        # Salva backup
        backup_path = os.path.join(self.backups_dir, filename)
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False)
        
        return backup_path
    
    def export_progress_csv(self, filename: Optional[str] = None) -> str:
        """Exporta progresso para CSV"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"progresso_python_{timestamp}.csv"
        
        csv_path = os.path.join(self.backups_dir, filename)
        
        # Carrega dados de progresso
        progress_data = {}
        if os.path.exists("progress.json"):
            with open("progress.json", 'r', encoding='utf-8') as f:
                progress_data = json.load(f)
        
        # Cria CSV com dados dos módulos
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Cabeçalho
            writer.writerow([
                'Módulo', 'Completo', 'Pontuação', 'Tentativas', 
                'Tempo (min)', 'Último Acesso'
            ])
            
            # Dados dos módulos
            modules_progress = progress_data.get("modules_progress", {})
            for module_id in sorted(modules_progress.keys()):
                module_data = modules_progress[module_id]
                
                writer.writerow([
                    module_id,
                    "Sim" if module_data.get("completed", False) else "Não",
                    module_data.get("score", 0),
                    module_data.get("attempts", 0),
                    module_data.get("time_spent", 0) // 60,
                    module_data.get("last_access", "")
                ])
            
            # Linha de resumo
            writer.writerow([])
            writer.writerow(["RESUMO"])
            writer.writerow(["Usuário", progress_data.get("user_name", "")])
            writer.writerow(["Pontuação Total", progress_data.get("total_score", 0)])
            writer.writerow(["Módulos Completos", len(progress_data.get("modules_completed", []))])
            writer.writerow(["Data Export", datetime.now().strftime("%d/%m/%Y %H:%M")])
        
        return csv_path
    
    def import_progress(self, file_path: str) -> Tuple[bool, str]:
        """Importa progresso de arquivo"""
        if not os.path.exists(file_path):
            return False, "Arquivo não encontrado"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # Verifica formato
            if "export_info" not in backup_data or "files" not in backup_data:
                return False, "Formato de arquivo inválido"
            
            # Cria backup dos dados atuais
            self.create_auto_backup("antes_import")
            
            # Restaura arquivos
            restored_files = []
            for file_name, file_data in backup_data["files"].items():
                if file_data is not None:
                    with open(file_name, 'w', encoding='utf-8') as f:
                        json.dump(file_data, f, indent=2, ensure_ascii=False)
                    restored_files.append(file_name)
            
            export_info = backup_data["export_info"]
            return True, f"Importado com sucesso!\nData: {export_info.get('export_date', 'N/A')}\nArquivos: {', '.join(restored_files)}"
        
        except Exception as e:
            return False, f"Erro ao importar: {str(e)}"
    
    def create_auto_backup(self, reason: str = "auto") -> str:
        """Cria backup automático"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"auto_backup_{reason}_{timestamp}.json"
        return self.export_progress_json(filename)
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """Lista todos os backups disponíveis"""
        backups = []
        
        if not os.path.exists(self.backups_dir):
            return backups
        
        for file_name in os.listdir(self.backups_dir):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.backups_dir, file_name)
                file_stat = os.stat(file_path)
                
                backup_info = {
                    "filename": file_name,
                    "path": file_path,
                    "size": file_stat.st_size,
                    "created": datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                    "type": "JSON"
                }
                
                # Tenta ler informações do backup
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if "export_info" in data:
                            backup_info.update({
                                "export_date": data["export_info"].get("export_date"),
                                "profile": data["export_info"].get("profile", "unknown"),
                                "version": data["export_info"].get("version", "1.0")
                            })
                except:
                    pass
                
                backups.append(backup_info)
            
            elif file_name.endswith('.csv'):
                file_path = os.path.join(self.backups_dir, file_name)
                file_stat = os.stat(file_path)
                
                backups.append({
                    "filename": file_name,
                    "path": file_path,
                    "size": file_stat.st_size,
                    "created": datetime.fromtimestamp(file_stat.st_ctime).isoformat(),
                    "type": "CSV"
                })
        
        return sorted(backups, key=lambda x: x["created"], reverse=True)
    
    def cleanup_old_backups(self, keep_count: int = 10) -> int:
        """Remove backups antigos, mantendo apenas os mais recentes"""
        backups = self.list_backups()
        
        if len(backups) <= keep_count:
            return 0
        
        # Remove os mais antigos
        to_remove = backups[keep_count:]
        removed_count = 0
        
        for backup in to_remove:
            try:
                os.remove(backup["path"])
                removed_count += 1
            except:
                pass
        
        return removed_count
    
    def sync_with_github_gist(self, gist_token: str, gist_id: Optional[str] = None) -> Tuple[bool, str]:
        """Sincroniza com GitHub Gist (funcionalidade opcional)"""
        try:
            import requests
        except ImportError:
            return False, "Biblioteca 'requests' não instalada. Use: pip install requests"
        
        # Cria backup para upload
        backup_file = self.export_progress_json()
        
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup_content = f.read()
        
        headers = {
            "Authorization": f"token {gist_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        gist_data = {
            "description": f"Python Course Backup - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "public": False,
            "files": {
                "python_course_backup.json": {
                    "content": backup_content
                }
            }
        }
        
        try:
            if gist_id:
                # Atualiza gist existente
                url = f"https://api.github.com/gists/{gist_id}"
                response = requests.patch(url, headers=headers, json=gist_data)
            else:
                # Cria novo gist
                url = "https://api.github.com/gists"
                response = requests.post(url, headers=headers, json=gist_data)
            
            if response.status_code in [200, 201]:
                result = response.json()
                return True, f"Sincronizado com sucesso! Gist ID: {result['id']}"
            else:
                return False, f"Erro na API GitHub: {response.status_code}"
        
        except Exception as e:
            return False, f"Erro na sincronização: {str(e)}"
    
    def download_from_github_gist(self, gist_id: str, gist_token: Optional[str] = None) -> Tuple[bool, str]:
        """Baixa backup do GitHub Gist"""
        try:
            import requests
        except ImportError:
            return False, "Biblioteca 'requests' não instalada"
        
        headers = {}
        if gist_token:
            headers["Authorization"] = f"token {gist_token}"
        
        url = f"https://api.github.com/gists/{gist_id}"
        
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                gist_data = response.json()
                
                # Procura arquivo de backup
                backup_file = None
                for filename, file_data in gist_data["files"].items():
                    if "python_course" in filename.lower() or "backup" in filename.lower():
                        backup_file = file_data["content"]
                        break
                
                if backup_file:
                    # Salva temporariamente e importa
                    temp_file = os.path.join(self.backups_dir, f"temp_gist_{gist_id}.json")
                    with open(temp_file, 'w', encoding='utf-8') as f:
                        f.write(backup_file)
                    
                    success, message = self.import_progress(temp_file)
                    
                    # Remove arquivo temporário
                    try:
                        os.remove(temp_file)
                    except:
                        pass
                    
                    return success, message
                else:
                    return False, "Arquivo de backup não encontrado no Gist"
            else:
                return False, f"Erro ao acessar Gist: {response.status_code}"
        
        except Exception as e:
            return False, f"Erro no download: {str(e)}"
    
    def show_sync_menu(self, ui_components) -> None:
        """Exibe menu de sincronização"""
        ui_components.header("SISTEMA DE SINCRONIZAÇÃO", "Backup e Múltiplos Perfis", "🔄")
        
        print("📋 OPÇÕES DISPONÍVEIS:")
        print("1. 👤 Gerenciar Perfis")
        print("2. 💾 Backup e Restore")
        print("3. 📤 Exportar Dados")
        print("4. 📥 Importar Dados")
        print("5. 🌐 Sincronização GitHub (Opcional)")
        print("0. 🔙 Voltar")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            self._manage_profiles_menu(ui_components)
        elif choice == "2":
            self._backup_restore_menu(ui_components)
        elif choice == "3":
            self._export_menu(ui_components)
        elif choice == "4":
            self._import_menu(ui_components)
        elif choice == "5":
            self._github_sync_menu(ui_components)
    
    def _manage_profiles_menu(self, ui_components) -> None:
        """Menu de gerenciamento de perfis"""
        ui_components.section("GERENCIAMENTO DE PERFIS", "👤")
        
        profiles = self.list_profiles()
        
        if profiles:
            print("📁 PERFIS EXISTENTES:")
            for i, profile in enumerate(profiles, 1):
                status = "🟢 ATIVO" if profile["profile_name"] == self.current_profile else "⚪"
                print(f"{i}. {status} {profile['user_name']} ({profile['profile_name']})")
                print(f"   📊 {profile.get('modules_completed', 0)} módulos | {profile.get('total_score', 0)} pontos")
                print(f"   📅 Último acesso: {profile.get('last_access', 'N/A')[:10]}")
                print()
        
        print("🎯 AÇÕES:")
        print("N. 🆕 Criar Novo Perfil")
        print("S. 🔄 Trocar de Perfil")
        print("0. 🔙 Voltar")
        
        action = input("\n👉 Ação: ").strip().upper()
        
        if action == "N":
            self._create_new_profile()
        elif action == "S" and profiles:
            self._switch_profile_menu(profiles)
    
    def _create_new_profile(self) -> None:
        """Cria novo perfil"""
        print("\n🆕 CRIAR NOVO PERFIL")
        
        profile_name = input("Nome do perfil (sem espaços): ").strip().replace(" ", "_")
        if not profile_name:
            print("❌ Nome inválido")
            return
        
        user_name = input("Nome do usuário: ").strip()
        if not user_name:
            print("❌ Nome do usuário é obrigatório")
            return
        
        if self.create_profile(profile_name, user_name):
            print(f"✅ Perfil '{profile_name}' criado com sucesso!")
            
            switch = input("Trocar para este perfil agora? (s/n): ").strip().lower()
            if switch == 's':
                if self.switch_profile(profile_name):
                    print(f"🔄 Mudado para perfil '{profile_name}'")
                else:
                    print("❌ Erro ao trocar perfil")
        else:
            print("❌ Erro ao criar perfil (pode já existir)")
    
    def _switch_profile_menu(self, profiles: List[Dict[str, Any]]) -> None:
        """Menu para trocar perfil"""
        print("\n🔄 TROCAR PERFIL")
        
        for i, profile in enumerate(profiles, 1):
            if profile["profile_name"] != self.current_profile:
                print(f"{i}. {profile['user_name']} ({profile['profile_name']})")
        
        try:
            choice = int(input("\nEscolha o perfil: ")) - 1
            if 0 <= choice < len(profiles):
                selected_profile = profiles[choice]
                if selected_profile["profile_name"] != self.current_profile:
                    if self.switch_profile(selected_profile["profile_name"]):
                        print(f"✅ Mudado para perfil '{selected_profile['user_name']}'")
                        print("🔄 Reinicie o programa para carregar o novo perfil")
                    else:
                        print("❌ Erro ao trocar perfil")
        except ValueError:
            print("❌ Opção inválida")
    
    def _backup_restore_menu(self, ui_components) -> None:
        """Menu de backup e restore"""
        ui_components.section("BACKUP E RESTORE", "💾")
        
        backups = self.list_backups()
        
        print("1. 💾 Criar Backup Agora")
        print("2. 📥 Restaurar de Backup")
        print("3. 📋 Listar Backups")
        print("4. 🧹 Limpar Backups Antigos")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            backup_path = self.create_auto_backup("manual")
            print(f"✅ Backup criado: {backup_path}")
        
        elif choice == "2" and backups:
            self._restore_backup_menu(backups)
        
        elif choice == "3":
            self._list_backups(backups)
        
        elif choice == "4":
            removed = self.cleanup_old_backups(5)
            print(f"🧹 {removed} backups antigos removidos")
    
    def _export_menu(self, ui_components) -> None:
        """Menu de exportação"""
        ui_components.section("EXPORTAR DADOS", "📤")
        
        print("1. 📄 Exportar como JSON")
        print("2. 📊 Exportar como CSV")
        
        choice = input("\n👉 Formato: ").strip()
        
        if choice == "1":
            path = self.export_progress_json()
            print(f"✅ Exportado para: {path}")
        elif choice == "2":
            path = self.export_progress_csv()
            print(f"✅ Exportado para: {path}")
    
    def _import_menu(self, ui_components) -> None:
        """Menu de importação"""
        ui_components.section("IMPORTAR DADOS", "📥")
        
        file_path = input("Caminho do arquivo: ").strip()
        
        success, message = self.import_progress(file_path)
        
        if success:
            ui_components.alert(f"✅ {message}", "success")
            print("🔄 Reinicie o programa para carregar os dados importados")
        else:
            ui_components.alert(f"❌ {message}", "error")
    
    def _github_sync_menu(self, ui_components) -> None:
        """Menu de sincronização GitHub"""
        ui_components.section("SINCRONIZAÇÃO GITHUB GIST", "🌐")
        
        print("ℹ️  Esta funcionalidade requer um token GitHub")
        print("📝 Crie em: https://github.com/settings/tokens")
        print("🔐 Permissões necessárias: 'gist'")
        print()
        
        print("1. 📤 Upload para Gist")
        print("2. 📥 Download de Gist")
        
        choice = input("\n👉 Escolha: ").strip()
        
        if choice == "1":
            token = input("Token GitHub: ").strip()
            gist_id = input("Gist ID (deixe vazio para criar novo): ").strip() or None
            
            success, message = self.sync_with_github_gist(token, gist_id)
            
            if success:
                ui_components.alert(f"✅ {message}", "success")
            else:
                ui_components.alert(f"❌ {message}", "error")
        
        elif choice == "2":
            gist_id = input("Gist ID: ").strip()
            token = input("Token GitHub (opcional): ").strip() or None
            
            success, message = self.download_from_github_gist(gist_id, token)
            
            if success:
                ui_components.alert(f"✅ {message}", "success")
            else:
                ui_components.alert(f"❌ {message}", "error")
    
    def _restore_backup_menu(self, backups: List[Dict[str, Any]]) -> None:
        """Menu para restaurar backup"""
        print("\n📥 RESTAURAR BACKUP")
        
        for i, backup in enumerate(backups[:10], 1):  # Mostra últimos 10
            date = backup.get("export_date", backup["created"])[:16]
            print(f"{i}. {backup['filename']} ({date})")
        
        try:
            choice = int(input("\nEscolha o backup: ")) - 1
            if 0 <= choice < len(backups):
                selected_backup = backups[choice]
                
                confirm = input(f"Restaurar '{selected_backup['filename']}'? (s/n): ")
                if confirm.lower() == 's':
                    success, message = self.import_progress(selected_backup["path"])
                    if success:
                        print(f"✅ {message}")
                    else:
                        print(f"❌ {message}")
        except ValueError:
            print("❌ Opção inválida")
    
    def _list_backups(self, backups: List[Dict[str, Any]]) -> None:
        """Lista backups disponíveis"""
        print("\n📋 BACKUPS DISPONÍVEIS:")
        
        for backup in backups:
            size_mb = backup["size"] / 1024 / 1024
            date = backup.get("export_date", backup["created"])[:16]
            print(f"📄 {backup['filename']}")
            print(f"   📅 {date} | 📏 {size_mb:.2f} MB | 🏷️ {backup['type']}")
            if "profile" in backup:
                print(f"   👤 Perfil: {backup['profile']}")
            print()