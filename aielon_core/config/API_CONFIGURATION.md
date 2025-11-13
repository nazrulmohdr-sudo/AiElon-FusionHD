# AiElon Unified Brain - Example Configuration

## API Endpoints Configuration

This file contains example configurations for all supported AI engines.

### OpenAI (ChatGPT)
```
Endpoint: https://api.openai.com/v1/chat/completions
API Key Format: sk-proj-...
Documentation: https://platform.openai.com/docs
```

### Anthropic (Claude)
```
Endpoint: https://api.anthropic.com/v1/messages
API Key Format: sk-ant-...
Documentation: https://docs.anthropic.com
```

### DeepSeek
```
Endpoint: https://api.deepseek.com/v1/chat/completions
API Key Format: [Contact DeepSeek]
Documentation: https://platform.deepseek.com/docs
```

### X.AI (Grok)
```
Endpoint: https://api.x.ai/v1/chat/completions
API Key Format: xai-...
Documentation: https://docs.x.ai
```

### Meta AI
```
Endpoint: [Contact Meta for API access]
API Key Format: [Contact Meta]
Documentation: https://ai.meta.com
```

### Google (Gemini)
```
Endpoint: https://generativelanguage.googleapis.com/v1/models
API Key Format: AIza...
Documentation: https://ai.google.dev/docs
```

## Environment Variables

Copy `.env.example` to `.env` and update with your actual API keys:

```bash
cp .env.example .env
```

Then edit `.env` with your credentials.

## Security Notes

1. Never commit your `.env` file to version control
2. Keep API keys secure and rotate regularly
3. Use environment-specific configurations
4. Monitor API usage for anomalies
5. Implement rate limiting in production

## Testing Configuration

To test if your configuration is correct:

```bash
node aielon_core/ai_engines/brain.js "Test query"
```

You should see responses from all configured engines.
