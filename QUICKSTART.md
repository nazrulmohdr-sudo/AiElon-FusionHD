# 🚀 Quick Start Guide - AiElon Unified Brain

Get up and running with the AiElon Unified Brain system in 5 minutes!

---

## Prerequisites

Before starting, ensure you have:
- ✅ Node.js (v18 or higher)
- ✅ Python (v3.11 or higher)
- ✅ npm or yarn
- ✅ Git

Check your versions:
```bash
node --version
python --version
npm --version
```

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
```

### Step 2: Run Master Command (Recommended)

The easiest way to set up everything:

```bash
bash aielon_master_command.sh
```

This will:
- ✅ Create all necessary folders
- ✅ Install Node.js dependencies
- ✅ Install Python dependencies
- ✅ Set up configuration files
- ✅ Initialize the system

### Step 3: Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env

# Edit with your favorite editor
nano .env
# or
vim .env
# or
code .env
```

Add your API keys:
```env
OPENAI_API=https://api.openai.com/v1/chat/completions
CLAUDE_API=https://api.anthropic.com/v1/messages
DEEPSEEK_API=your_deepseek_endpoint
GROK_API=your_grok_endpoint
META_API=your_meta_ai_endpoint
GEMINI_API=https://generativelanguage.googleapis.com/v1/models
```

**Note**: You can start with just one or two APIs configured. The system will work with whatever you have set up.

---

## First Test

### Test the AI Brain

```bash
npm run brain "Hello AiElon!"
```

Expected output:
```json
{
  "query": "Hello AiElon!",
  "summary": "Unified AiElon Intelligence Response",
  "results": [
    { "engine": "ChatGPT", "response": "..." },
    { "engine": "Claude", "response": "..." },
    ...
  ]
}
```

If you see `"response": "NOT CONFIGURED"` for some engines, that's normal! Just configure those API keys when you're ready.

---

## Start the API Server

```bash
npm start
```

You should see:
```
🧠 AiElon Brain API running on port 3000
📡 Health check: http://localhost:3000/
🔍 Query endpoint: POST http://localhost:3000/api/query
```

### Test the Server

Open a new terminal and run:

```bash
# Health check
curl http://localhost:3000/

# Send a query
curl -X POST http://localhost:3000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is AI?"}'
```

---

## Manual Installation (Alternative)

If you prefer to set up manually:

```bash
# 1. Install Node.js dependencies
npm install

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Copy environment template
cp .env.example .env

# 4. Edit .env with your API keys
nano .env
```

---

## What's Next?

Now that you have the system running, you can:

### 1. Explore the Code
```bash
# View the brain orchestrator
cat aielon_core/ai_engines/brain.js

# View the API server
cat server.js
```

### 2. Run More Tests
```bash
npm run brain "Explain quantum computing"
npm run brain "What is blockchain?"
npm run brain "How does machine learning work?"
```

### 3. Build Your First Integration

Create a new file `my-app.js`:

```javascript
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

async function main() {
  const result = await AiElonBrain("What's the weather like?");
  console.log(result);
}

main();
```

Run it:
```bash
node my-app.js
```

### 4. Set Up Expo (Optional)

For mobile app development:

```bash
npx expo init my-aielon-app
cd my-aielon-app
npm install
```

---

## Troubleshooting

### Issue: "Command not found: bash"

**Windows users**: Use Git Bash or WSL, or run commands individually from the master script.

### Issue: "Permission denied"

```bash
chmod +x aielon_master_command.sh
bash aielon_master_command.sh
```

### Issue: "npm install fails"

```bash
# Clear npm cache and try again
npm cache clean --force
npm install
```

### Issue: "Python pip not found"

```bash
# Install pip
# Ubuntu/Debian:
sudo apt-get install python3-pip

# macOS:
brew install python

# Then try again
pip install -r requirements.txt
```

### Issue: Port 3000 is already in use

```bash
# Use a different port
PORT=8080 npm start
```

---

## Getting API Keys

### OpenAI (ChatGPT)
1. Visit: https://platform.openai.com/
2. Sign up/Login
3. Go to API Keys section
4. Create new key

### Anthropic (Claude)
1. Visit: https://console.anthropic.com/
2. Sign up/Login
3. Go to API Keys
4. Generate new key

### Google (Gemini)
1. Visit: https://ai.google.dev/
2. Get API key
3. Enable Gemini API

### Others
- **DeepSeek**: https://platform.deepseek.com/
- **Grok**: https://x.ai/
- **Meta AI**: Contact Meta for API access

**Note**: Some APIs may require payment or have usage limits. Check each provider's documentation.

---

## Project Structure Overview

```
AiElon-FusionHD/
├── aielon_core/
│   ├── ai_engines/
│   │   └── brain.js          # Main AI orchestrator
│   ├── config/
│   │   └── API_CONFIGURATION.md
│   └── [other folders]
├── .github/workflows/
│   └── aielon_autopilot.yml  # CI/CD configuration
├── aielon_master_command.sh  # Setup script
├── server.js                 # API server
├── package.json              # Node.js config
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
└── README.md                 # Documentation
```

---

## Useful Commands

```bash
# Test the brain
npm run brain "Your question"

# Start API server
npm start

# Install dependencies
npm install

# View logs (future feature)
tail -f aielon_core/logs/*.log

# Check git status
git status

# Update repository
git pull origin main
```

---

## Learn More

- 📖 [Full Documentation](README.md)
- 📋 [Master Command Guide](MASTER_COMMAND.md)
- 💡 [Usage Examples](USAGE_EXAMPLES.md)
- ⚙️ [API Configuration](aielon_core/config/API_CONFIGURATION.md)

---

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the documentation
3. Open a GitHub issue with details

---

**Ready to build the future with unified AI? Let's go! 🚀**

```bash
bash aielon_master_command.sh
```
