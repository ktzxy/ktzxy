#!/usr/bin/env python3
"""
README Updater for GitHub Profile
Updates README files with dynamic content
"""

import os
import json
import re
from datetime import datetime

class ReadmeUpdater:
    def __init__(self):
        self.data_dir = 'data'
        self.content_file = f'{self.data_dir}/dynamic_content.json'
        
    def load_dynamic_content(self):
        """加载动态内容"""
        try:
            with open(self.content_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Dynamic content file not found, using default content")
            return self.get_default_content()
    
    def get_default_content(self):
        """获取默认内容"""
        return {
            'current_status': "Currently crafting digital magic while sipping Oolong tea and planning the next mountain adventure.",
            'github_stats': {'public_repos': 0, 'followers': 0},
            'project_updates': [],
            'learning_progress': {}
        }
    
    def update_current_status_section(self, content, readme_content, lang='en'):
        """更新当前状态部分"""
        status = content.get('current_status', '')
        
        if lang == 'en':
            pattern = r'(## 🎭 Current Status\s*\n\s*<div align="center">\s*\n\s*> \*).*?(\* \n\s*</div>)'
            replacement = r'\1' + status + r'\2'
        else:
            pattern = r'(## 🎭 当前状态\s*\n\s*<div align="center">\s*\n\s*> \*).*?(\* \n\s*</div>)'
            replacement = r'\1' + status + r'\2'
        
        return re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    def update_project_section(self, content, readme_content, lang='en'):
        """更新项目部分"""
        projects = content.get('project_updates', [])
        
        if not projects:
            return readme_content
        
        if lang == 'en':
            # 更新英文版本的项目部分
            project_section = "### 🛠️ **Latest Creations**\n"
            for project in projects[:3]:
                project_section += f"- **{project['name']}** - {project['description']} (Progress: {project['progress']}%)\n"
            
            pattern = r'(### 🛠️ \*\*Latest Creations\*\*\n)(.*?)(\n\s*### 🎯 \*\*In the Pipeline\*\*)'
            replacement = r'\1' + project_section + r'\3'
        else:
            # 更新中文版本的项目部分
            project_section = "### 🛠️ **最新作品**\n"
            for project in projects[:3]:
                project_section += f"- **{project['name']}** - {project['description']} (进度: {project['progress']}%)\n"
            
            pattern = r'(### 🛠️ \*\*最新作品\*\*\n)(.*?)(\n\s*### 🎯 \*\*计划中\*\*)'
            replacement = r'\1' + project_section + r'\3'
        
        return re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    def add_learning_progress_section(self, content, readme_content, lang='en'):
        """添加学习进度部分"""
        skills = content.get('learning_progress', {})
        
        if not skills:
            return readme_content
        
        if lang == 'en':
            progress_section = "\n### 📚 **Learning Progress**\n\n"
            for skill, progress in skills.items():
                progress_bar = "█" * (progress // 10) + "░" * (10 - progress // 10)
                progress_section += f"**{skill}**: {progress_bar} {progress}%\n\n"
        else:
            progress_section = "\n### 📚 **学习进度**\n\n"
            for skill, progress in skills.items():
                progress_bar = "█" * (progress // 10) + "░" * (10 - progress // 10)
                progress_section += f"**{skill}**: {progress_bar} {progress}%\n\n"
        
        # 在GitHub统计部分之前插入
        if lang == 'en':
            pattern = r'(### 🎪 \*\*GitHub Stats\*\*)'
            replacement = progress_section + r'\1'
        else:
            pattern = r'(### 🎪 \*\*GitHub统计\*\*)'
            replacement = progress_section + r'\1'
        
        return re.sub(pattern, replacement, readme_content)
    
    def update_readme_file(self, filename, lang='en'):
        """更新README文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"⚠️ File {filename} not found")
            return
        
        # 加载动态内容
        dynamic_content = self.load_dynamic_content()
        
        # 更新各个部分
        content = self.update_current_status_section(dynamic_content, content, lang)
        content = self.update_project_section(dynamic_content, content, lang)
        content = self.add_learning_progress_section(dynamic_content, content, lang)
        
        # 添加更新时间戳
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if lang == 'en':
            content += f"\n---\n\n*Last updated: {timestamp}*"
        else:
            content += f"\n---\n\n*最后更新: {timestamp}*"
        
        # 写回文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {filename} successfully!")
    
    def update_all_readmes(self):
        """更新所有README文件"""
        self.update_readme_file('README.md', 'en')
        self.update_readme_file('README_CN.md', 'cn')

def main():
    updater = ReadmeUpdater()
    updater.update_all_readmes()
    print("🎭 All README files updated successfully!")

if __name__ == "__main__":
    main() 