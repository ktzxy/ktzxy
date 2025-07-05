# 🤖 GitHub Profile Automation

This repository includes automated workflows to keep your GitHub profile dynamic and engaging!

## 🚀 Features

### 📊 **Dynamic Statistics**
- **GitHub Stats**: Real-time repository and follower statistics
- **Activity Graph**: Beautiful contribution heatmap
- **Language Stats**: Top programming languages with usage percentages
- **Trophy Collection**: GitHub achievements and milestones
- **Streak Counter**: Daily contribution streaks

### 🎭 **Dynamic Content**
- **Current Status**: Randomly generated status messages
- **Project Updates**: Dynamic project progress and descriptions
- **Learning Progress**: Skill development tracking with progress bars
- **Weather Integration**: Mountain weather for hiking planning
- **Activity Updates**: Current activities and interests

## ⚙️ Automation Workflows

### 1. **Update GitHub Profile** (`.github/workflows/update-profile.yml`)
- **Schedule**: Daily at 2:00 AM UTC
- **Triggers**: Manual dispatch, README changes
- **Features**:
  - Updates GitHub statistics
  - Generates activity graphs
  - Updates profile view counter
  - Refreshes contribution data

### 2. **Generate Dynamic Content** (`.github/workflows/dynamic-content.yml`)
- **Schedule**: Weekly on Mondays at 3:00 AM UTC
- **Triggers**: Manual dispatch, script changes
- **Features**:
  - Generates random status messages
  - Updates project progress
  - Fetches weather data for hiking
  - Updates learning progress bars

## 🛠️ Scripts

### `scripts/generate_dynamic_content.py`
Generates dynamic content including:
- Current status messages
- GitHub API statistics
- Weather information (requires API key)
- Project updates with progress
- Learning progress tracking

### `scripts/update_readme.py`
Updates README files with:
- Dynamic status updates
- Project progress information
- Learning progress bars
- Timestamp updates

## 🔧 Setup Instructions

### 1. **Repository Setup**
```bash
# Clone this repository
git clone https://github.com/AtticusWilde/AtticusWilde.git
cd AtticusWilde

# Make scripts executable
chmod +x scripts/*.py
```

### 2. **Environment Variables**
Add these secrets to your GitHub repository:
- `GITHUB_TOKEN`: Your GitHub personal access token
- `WEATHER_API_KEY`: OpenWeatherMap API key (optional)

### 3. **Manual Execution**
```bash
# Generate dynamic content
python scripts/generate_dynamic_content.py

# Update README files
python scripts/update_readme.py
```

## 📊 Available Statistics

### GitHub Stats Cards
- **Profile Views**: `https://komarev.com/ghpvc/?username=ktzxy`
- **GitHub Stats**: `https://github-readme-stats.vercel.app/api?username=ktzxy`
- **Top Languages**: `https://github-readme-stats.vercel.app/api/top-langs/?username=ktzxy`
- **Streak Stats**: `https://github-readme-streak-stats.herokuapp.com/?user=ktzxy`
- **Activity Graph**: `https://github-readme-activity-graph.vercel.app/graph?username=ktzxy`
- **Trophies**: `https://github-profile-trophy.vercel.app/?username=ktzxy`
- **Contribution Stats**: `https://github-contribution-stats.vercel.app/api/?username=ktzxy`

## 🎨 Customization

### Themes
All statistics cards support various themes:
- `radical` (default)
- `dark`
- `tokyonight`
- `dracula`
- `nord`
- `synthwave`

### Colors
Customize colors with parameters:
- `bg_color`: Background color
- `title_color`: Title text color
- `text_color`: Body text color
- `icon_color`: Icon color

### Status Messages
Edit `scripts/generate_dynamic_content.py` to customize:
- Current status messages
- Project descriptions
- Activity updates
- Learning progress ranges

## 🔄 Workflow Triggers

### Automatic Triggers
- **Daily**: Statistics and activity updates
- **Weekly**: Dynamic content generation
- **On Push**: When README files change

### Manual Triggers
- **GitHub Actions**: Use "workflow_dispatch" to run manually
- **Local Scripts**: Run Python scripts directly

## 📝 File Structure

```
.
├── .github/
│   └── workflows/
│       ├── update-profile.yml
│       └── dynamic-content.yml
├── scripts/
│   ├── generate_dynamic_content.py
│   └── update_readme.py
├── data/
│   └── dynamic_content.json
├── README.md
├── README_CN.md
├── requirements.txt
└── AUTOMATION.md
```

## 🎯 Benefits

1. **Always Fresh**: Content updates automatically
2. **Engaging**: Dynamic elements keep visitors interested
3. **Professional**: Automated maintenance looks polished
4. **Personalized**: Reflects your current activities and progress
5. **Multilingual**: Supports both English and Chinese versions

## 🚨 Troubleshooting

### Common Issues
1. **Workflow not running**: Check GitHub Actions permissions
2. **API rate limits**: GitHub API has hourly limits
3. **Missing secrets**: Ensure all required secrets are set
4. **Script errors**: Check Python dependencies in requirements.txt

### Debug Mode
Enable debug logging by setting environment variable:
```bash
export DEBUG=1
python scripts/generate_dynamic_content.py
```

---

*"Automation is the art of making the complex simple, and the mundane magical." - Atticus Wilde* 