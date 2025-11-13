# 🧠 AiElon-FusionHD
## AiElon Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub

### Unified AI Brain System - Multi-AI Orchestrator

A powerful unified intelligence system that integrates multiple AI engines into one cohesive brain:
- ChatGPT (OpenAI)
- Claude (Anthropic)
- DeepSeek
- Grok (X.AI)
- Meta AI
- Google Gemini

---

## 🚀 Quick Start

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.11 or higher)
- npm or yarn

### Installation

#### Option 1: One-Command Setup (Recommended)
```bash
bash aielon_master_command.sh
```

#### Option 2: Manual Setup
```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
```

---

## 📁 Project Structure

```
AiElon-FusionHD/
├── aielon_core/
│   ├── ai_engines/       # AI Brain orchestrators
│   │   └── brain.js      # Main AI router
│   ├── api_keys/         # API key configurations
│   ├── config/           # System configurations
│   ├── expo/             # Expo mobile app setup
│   ├── github/           # GitHub integrations
│   └── logs/             # System logs
├── .github/
│   └── workflows/
│       └── aielon_autopilot.yml  # CI/CD automation
├── aielon_master_command.sh      # Master setup script
├── package.json                  # Node.js dependencies
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
└── README.md                     # This file
```

---

## 🔧 Configuration

### API Keys Setup

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
```env
OPENAI_API=https://api.openai.com/v1/chat/completions
CLAUDE_API=https://api.anthropic.com/v1/messages
DEEPSEEK_API=your_deepseek_endpoint
GROK_API=your_grok_endpoint
META_API=your_meta_ai_endpoint
GEMINI_API=https://generativelanguage.googleapis.com/v1/models
```

---

## 💡 Usage

### Testing the AI Brain

```bash
# Run with default test query
node aielon_core/ai_engines/brain.js

# Run with custom query
node aielon_core/ai_engines/brain.js "Your question here"
```

### Using in Your Code

```javascript
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

const response = await AiElonBrain("What is the meaning of life?");
console.log(response);
```

---

## 🤖 GitHub Actions CI/CD

The system includes automated CI/CD through GitHub Actions:

- **Trigger**: Pushes to `main` branch
- **Actions**:
  - Install dependencies
  - Run AI Brain test
  - Build Expo app (if configured)

Configure in: `.github/workflows/aielon_autopilot.yml`

---

## 📱 Expo Mobile App

To initialize Expo Pro for mobile development:

```bash
npx expo init
```

Configure your app settings in `app.json`

---

## 🔒 Security

- **Never commit `.env` file** - it contains sensitive API keys
- All API keys are stored in `.env` and gitignored
- Use environment variables for all sensitive data
- Rotate API keys regularly

---

## 🛠️ Development

### Adding New AI Engines

Edit `aielon_core/ai_engines/brain.js` and add to the engines array:

```javascript
{
  name: "NewAI",
  url: process.env.NEW_AI_API
}
```

Then add the corresponding API key to `.env.example` and `.env`.

---

## 📊 Features

✅ Multi-AI orchestration  
✅ Unified API layer  
✅ GitHub CI/CD automation  
✅ Expo Pro mobile support  
✅ Environment-based configuration  
✅ Error handling and fallbacks  
✅ Extensible architecture  

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🌟 Powered by AiElon Team

Building the future of unified AI intelligence.
