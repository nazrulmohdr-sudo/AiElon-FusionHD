import express from 'express';
import { AiElonBrain } from './aielon_core/ai_engines/brain.js';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Health check endpoint
app.get('/', (req, res) => {
  res.json({
    status: 'online',
    service: 'AiElon Unified Brain API',
    version: '1.0.0'
  });
});

// AI Brain query endpoint
app.post('/api/query', async (req, res) => {
  try {
    const { query } = req.body;
    
    if (!query) {
      return res.status(400).json({
        error: 'Query parameter is required'
      });
    }

    const result = await AiElonBrain(query);
    res.json(result);
  } catch (error) {
    res.status(500).json({
      error: 'Internal server error',
      message: error.message
    });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`🧠 AiElon Brain API running on port ${PORT}`);
  console.log(`📡 Health check: http://localhost:${PORT}/`);
  console.log(`🔍 Query endpoint: POST http://localhost:${PORT}/api/query`);
});
