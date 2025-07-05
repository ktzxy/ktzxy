#!/usr/bin/env python3
"""
Dynamic Content Generator for GitHub Profile
Generates dynamic content like current status, project updates, etc.
"""

import os
import json
import requests
from datetime import datetime, timedelta
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
    
    def get_github_stats(self):
        """获取GitHub统计数据"""
        if not self.github_token:
            return {}
            
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        try:
            # 获取用户信息
            user_response = requests.get(
                'https://api.github.com/user',
                headers=headers
            )
            user_data = user_response.json()
            
            # 获取仓库信息
            repos_response = requests.get(
                'https://api.github.com/user/repos?sort=updated&per_page=5',
                headers=headers
            )
            repos_data = repos_response.json()
            
            return {
                'username': user_data.get('login', 'ktzxy'),
                'public_repos': user_data.get('public_repos', 0),
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'latest_repos': [repo['name'] for repo in repos_data[:3]]
            }
        except Exception as e:
            print(f"Error fetching GitHub stats: {e}")
            return {}
    
    def get_weather_info(self):
        """获取天气信息（用于登山计划）"""
        if not self.weather_api_key:
            return {}
            
        # 庐山天气API（示例坐标）
        lat, lon = 29.5567, 115.9853  # 庐山坐标
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.weather_api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            weather_data = response.json()
            
            return {
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed']
            }
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return {}
    
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
            'github_stats': self.get_github_stats(),
            'weather_info': self.get_weather_info(),
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
    print(f"GitHub Repos: {content['github_stats'].get('public_repos', 0)}")
    print(f"Latest Projects: {', '.join(content['project_updates'][:2])}")
    
if __name__ == "__main__":
    main() 