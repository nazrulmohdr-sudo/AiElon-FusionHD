#!/bin/bash

echo "🧠 AIELON UNIFIED BRAIN INITIALISATION — STARTING"
echo "=============================================="
echo "MODE: SUPREME FUSION • ONE INTELLIGENCE • ONE COMMAND"

# 1 — CREATE CORE FOLDER
mkdir -p aielon_core/{ai_engines,api_keys,github,expo,config,logs}

# 2 — INSTALL BASE ORCHESTRATOR (Node + Python)
npm init -y
npm install axios express dotenv

# Check if Python is available and install dependencies
if command -v pip &> /dev/null; then
    pip install requests fastapi uvicorn
elif command -v pip3 &> /dev/null; then
    pip3 install requests fastapi uvicorn
else
    echo "⚠️  Python pip not found. Please install Python dependencies manually."
fi

# 3 — SETUP UNIFIED AI ENGINE (ChatGPT + Claude + Grok + DeepSeek + Gemini + Meta)
echo "CONFIGURING MULTI-AI ORCHESTRATOR…"

cat << 'EOF' > aielon_core/ai_engines/brain.js
import axios from 'axios';
import dotenv from 'dotenv';
dotenv.config();

// UNIVERSAL BRAIN ROUTER
export async function AiElonBrain(query) {
  const engines = [
    { name: "ChatGPT",  url: process.env.OPENAI_API },
    { name: "Claude",   url: process.env.CLAUDE_API },
    { name: "DeepSeek", url: process.env.DEEPSEEK_API },
    { name: "Grok",     url: process.env.GROK_API },
    { name: "Meta",     url: process.env.META_API },
    { name: "Gemini",   url: process.env.GEMINI_API }
  ];

  let results = [];
  for (const e of engines) {
    try {
      const res = await axios.post(e.url, { prompt: query });
      results.push({ engine: e.name, response: res.data });
    } catch {
      results.push({ engine: e.name, response: "OFFLINE / SKIP" });
    }
  }

  return {
    query,
    summary: "Unified AiElon Intelligence Response",
    results
  };
}
EOF

# 4 — SETUP EXPO PRO (Mobile App Brain)
echo "INITIALIZING EXPO PRO…"
if command -v npx &> /dev/null; then
    npx expo install
else
    echo "⚠️  npx not found. Please install Expo manually with: npx expo install"
fi

# 5 — SETUP GITHUB AUTO-SYNC (CI/CD BRAIN)
echo "SETTING UP GITHUB AUTOPILOT…"
mkdir -p .github/workflows
cat << 'EOF' > .github/workflows/aielon_autopilot.yml
name: AIELON_AUTOPILOT

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Dependencies
        run: npm install
      - name: Run Orchestrator
        run: node aielon_core/ai_engines/brain.js
      - name: Expo Build
        run: npx expo build
EOF

# 6 — ENV FILE (API KEYS)
echo "CREATING .env.example…"

cat << 'EOF' > .env.example
OPENAI_API=your_openai_key
CLAUDE_API=your_claude_key
DEEPSEEK_API=your_deepseek_key
GROK_API=your_grok_key
META_API=your_meta_ai_key
GEMINI_API=your_gemini_api
EOF

echo "=============================================="
echo "🧠 AIELON ONE-BRAIN SYSTEM — COMPLETE"
echo "READY TO UPGRADE IN ONE COMMAND."
echo ""
echo "⚠️  NEXT STEPS:"
echo "1. Copy .env.example to .env and add your API keys"
echo "2. Run: npm install"
echo "3. Configure your AI engine endpoints"
echo "=============================================="
