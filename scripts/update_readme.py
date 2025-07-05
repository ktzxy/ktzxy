#!/usr/bin/env python3
"""
README Updater for GitHub Profile
Updates README files with dynamic content
"""

import os
import json
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