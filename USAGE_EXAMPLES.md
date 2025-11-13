# AiElon Unified Brain - Usage Examples

This document provides practical examples of using the AiElon Unified Brain system.

## Table of Contents
1. [Basic Usage](#basic-usage)
2. [API Server Usage](#api-server-usage)
3. [Programmatic Usage](#programmatic-usage)
4. [Configuration Examples](#configuration-examples)

---

## Basic Usage

### Running the Brain from Command Line

```bash
# Test with default query
node aielon_core/ai_engines/brain.js

# Test with custom query
node aielon_core/ai_engines/brain.js "What is artificial intelligence?"

# Using npm script
npm run brain "Explain quantum computing"
```

### Expected Output

```json
{
  "query": "What is artificial intelligence?",
  "summary": "Unified AiElon Intelligence Response",
  "results": [
    {
      "engine": "ChatGPT",
      "response": "NOT CONFIGURED"
    },
    {
      "engine": "Claude",
      "response": "NOT CONFIGURED"
    },
    ...
  ]
}
```

---

## API Server Usage

### Starting the Server

```bash
# Start the server
npm start

# Server will run on http://localhost:3000
```

### Health Check

```bash
curl http://localhost:3000/
```

Response:
```json
{
  "status": "online",
  "service": "AiElon Unified Brain API",
  "version": "1.0.0"
}
```

### Sending a Query

```bash
curl -X POST http://localhost:3000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?"}'
```

Response:
```json
{
  "query": "What is machine learning?",
  "summary": "Unified AiElon Intelligence Response",
  "results": [
    {
      "engine": "ChatGPT",
      "response": { ... }
    },
    {
      "engine": "Claude",
      "response": { ... }
    },
    ...
  ]
}
```

---

## Programmatic Usage

### Using in Your Node.js Application

```javascript
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

// Single query
async function askQuestion() {
  const result = await AiElonBrain("Explain blockchain technology");
  console.log(result);
}

// Multiple queries
async function askMultipleQuestions() {
  const questions = [
    "What is AI?",
    "Explain neural networks",
    "What is deep learning?"
  ];
  
  for (const question of questions) {
    const result = await AiElonBrain(question);
    console.log(`Q: ${question}`);
    console.log(`A:`, result.results);
    console.log('---');
  }
}

// Error handling
async function safeQuery(query) {
  try {
    const result = await AiElonBrain(query);
    return result;
  } catch (error) {
    console.error('Query failed:', error);
    return null;
  }
}

askQuestion();
```

### Using with Express in Your App

```javascript
import express from 'express';
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

const app = express();
app.use(express.json());

app.post('/ask', async (req, res) => {
  const { question } = req.body;
  const answer = await AiElonBrain(question);
  res.json(answer);
});

app.listen(3000);
```

---

## Configuration Examples

### Environment Setup (.env)

```env
# OpenAI ChatGPT
OPENAI_API=https://api.openai.com/v1/chat/completions
OPENAI_KEY=sk-proj-xxxxxxxxxxxxx

# Anthropic Claude
CLAUDE_API=https://api.anthropic.com/v1/messages
CLAUDE_KEY=sk-ant-xxxxxxxxxxxxx

# DeepSeek
DEEPSEEK_API=https://api.deepseek.com/v1/chat/completions
DEEPSEEK_KEY=xxxxxxxxxxxxx

# X.AI Grok
GROK_API=https://api.x.ai/v1/chat/completions
GROK_KEY=xai-xxxxxxxxxxxxx

# Meta AI
META_API=https://api.meta.ai/v1/query
META_KEY=xxxxxxxxxxxxx

# Google Gemini
GEMINI_API=https://generativelanguage.googleapis.com/v1/models
GEMINI_KEY=AIzaxxxxxxxxxxxxx
```

### Custom Engine Configuration

To add a new AI engine, edit `aielon_core/ai_engines/brain.js`:

```javascript
const engines = [
  { name: "ChatGPT",  url: process.env.OPENAI_API },
  { name: "Claude",   url: process.env.CLAUDE_API },
  { name: "DeepSeek", url: process.env.DEEPSEEK_API },
  { name: "Grok",     url: process.env.GROK_API },
  { name: "Meta",     url: process.env.META_API },
  { name: "Gemini",   url: process.env.GEMINI_API },
  // Add your custom engine here
  { name: "MyAI",     url: process.env.MY_AI_API }
];
```

---

## Advanced Examples

### Filtering Results

```javascript
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

async function getOnlineEnginesOnly(query) {
  const result = await AiElonBrain(query);
  
  // Filter out offline engines
  const onlineResults = result.results.filter(
    r => r.response !== "NOT CONFIGURED" && 
         r.response !== "OFFLINE / SKIP"
  );
  
  return {
    ...result,
    results: onlineResults
  };
}
```

### Parallel Processing

```javascript
async function batchProcess(queries) {
  const promises = queries.map(q => AiElonBrain(q));
  const results = await Promise.all(promises);
  return results;
}

// Usage
const queries = [
  "What is AI?",
  "What is ML?",
  "What is DL?"
];

const results = await batchProcess(queries);
```

### Response Aggregation

```javascript
async function getConsensus(query) {
  const result = await AiElonBrain(query);
  
  // Count how many engines gave similar responses
  // (This is a simplified example)
  const responses = result.results
    .filter(r => typeof r.response === 'object')
    .map(r => r.response);
  
  return {
    query: result.query,
    totalEngines: result.results.length,
    activeEngines: responses.length,
    responses: responses
  };
}
```

---

## Testing Examples

### Unit Test Example

```javascript
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';

async function testBrain() {
  console.log('Testing AiElon Brain...');
  
  const result = await AiElonBrain("Test query");
  
  // Verify structure
  if (!result.query || !result.summary || !result.results) {
    throw new Error('Invalid response structure');
  }
  
  // Verify all engines are present
  const engineNames = result.results.map(r => r.engine);
  const expectedEngines = ['ChatGPT', 'Claude', 'DeepSeek', 'Grok', 'Meta', 'Gemini'];
  
  for (const engine of expectedEngines) {
    if (!engineNames.includes(engine)) {
      throw new Error(`Missing engine: ${engine}`);
    }
  }
  
  console.log('✅ All tests passed!');
}

testBrain();
```

---

## Troubleshooting

### Common Issues and Solutions

**Issue**: "Cannot find module"
```bash
# Solution: Install dependencies
npm install
```

**Issue**: All engines return "NOT CONFIGURED"
```bash
# Solution: Set up your .env file
cp .env.example .env
# Edit .env with your API keys
```

**Issue**: Port 3000 already in use
```bash
# Solution: Use a different port
PORT=8080 npm start
```

**Issue**: API timeout
```javascript
// Solution: Add timeout configuration
const res = await axios.post(e.url, 
  { prompt: query },
  { timeout: 10000 } // 10 seconds
);
```

---

## Best Practices

1. **Always use environment variables** for API keys
2. **Implement rate limiting** in production
3. **Cache responses** when appropriate
4. **Log errors** for debugging
5. **Monitor API usage** to avoid exceeding quotas
6. **Handle errors gracefully** with fallbacks
7. **Test with mock data** before using real APIs

---

## Next Steps

- Implement response caching
- Add retry logic with exponential backoff
- Create a web dashboard for visualization
- Add authentication for the API server
- Implement request queuing for rate limiting
- Add metrics and monitoring

---

For more information, see:
- [README.md](../README.md)
- [MASTER_COMMAND.md](../MASTER_COMMAND.md)
- [API_CONFIGURATION.md](aielon_core/config/API_CONFIGURATION.md)
