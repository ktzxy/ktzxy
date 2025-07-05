#!/usr/bin/env python3
"""
Dynamic Content Generator for GitHub Profile
Generates dynamic content like current status, project updates, etc.
"""

import os
import json
from datetime import datetime
import random

class DynamicContentGenerator:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        self.data_dir = 'data'
        
        # 确保数据目录存在
        os.makedirs(self.data_dir, exist_ok=True)
        
    def get_current_status(self):
        """生成当前状态信息"""
        statuses = [
            "Currently crafting digital magic while sipping Oolong tea and planning the next mountain adventure.",
            "Deep in code meditation, with incense burning and classical music playing.",
            "Exploring new technologies while brewing the perfect cup of green tea.",
            "Balancing between coding sessions and chess strategy planning.",
            "Reading 'Guns, Germs, and Steel' while contemplating the next project architecture.",
            "Planning the next hiking trip while debugging some interesting code challenges.",
            "Watching 'The Shawshank Redemption' for the 50th time while optimizing algorithms.",
            "Brewing tea and contemplating the meaning of clean code.",
            "Between coding sprints, practicing badminton serves and chess openings.",
            "Lost in the mountains of code, finding beauty in the chaos of algorithms."
        ]
        
        return random.choice(statuses)
    
    def get_project_updates(self):
        """生成项目更新信息"""
        projects = [
            {
                'name': 'Quantum Chess AI',
                'status': 'Planning Phase',
                'description': 'Developing an AI that plays chess with quantum computing principles',
                'progress': random.randint(10, 30)
            },
            {
                'name': 'Mountain Weather Predictor',
                'status': 'Development Phase',
                'description': 'ML-based weather prediction for hiking enthusiasts',
                'progress': random.randint(40, 70)
            },
            {
                'name': 'Tea Timer App',
                'status': 'Testing Phase',
                'description': 'Perfect brewing timer with tea knowledge database',
                'progress': random.randint(60, 90)
            }
        ]
        
        return projects
    
    def get_learning_progress(self):
        """生成学习进度信息"""
        skills = {
            'Python': random.randint(80, 95),
            'C++': random.randint(70, 85),
            'Java': random.randint(75, 90),
            'Vue.js': random.randint(65, 80),
            'Docker': random.randint(80, 90),
            'Linux': random.randint(85, 95),
            'Spring Boot': random.randint(70, 85)
        }
        
        return skills
    
    def generate_content(self):
        """生成所有动态内容"""
        content = {
            'timestamp': datetime.now().isoformat(),
            'current_status': self.get_current_status(),
            'github_stats': {'public_repos': 0, 'followers': 0},
            'weather_info': {},
            'project_updates': self.get_project_updates(),
            'learning_progress': self.get_learning_progress(),
            'current_activities': [
                'Coding a new microservice',
                'Reading about quantum computing',
                'Planning weekend hiking trip',
                'Practicing chess openings',
                'Brewing different tea varieties'
            ]
        }
        
        # 保存到文件
        with open(f'{self.data_dir}/dynamic_content.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
            
        print("✅ Dynamic content generated successfully!")
        return content

def main():
    generator = DynamicContentGenerator()
    content = generator.generate_content()
    
    # 打印生成的内容摘要
    print("\n📊 Generated Content Summary:")
    print(f"Current Status: {content['current_status']}")
    print(f"Projects: {len(content['project_updates'])}")
    print(f"Skills: {len(content['learning_progress'])}")
    
if __name__ == "__main__":
    main() 