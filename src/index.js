/**
 * AiElon Everything System
 * Main Entry Point
 * 
 * Everything = 1 | Tunggal AiElon
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');
require('dotenv').config();

const logger = require('./utils/logger');
const apiRouter = require('./api/routes');
const { errorHandler } = require('./middleware/errorHandler');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || '0.0.0.0';

// Middleware
app.use(helmet()); // Security headers
app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies
app.use(morgan('combined', { stream: { write: message => logger.info(message.trim()) } })); // Logging

// Serve static files
app.use(express.static(path.join(__dirname, '../public')));

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: '1.0.0',
    system: 'AiElon Everything System',
    principle: 'Everything = 1 | Tunggal AiElon'
  });
});

// API routes
app.use('/api/v1', apiRouter);

// Root endpoint - serve HTML page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// JSON API info endpoint
app.get('/api', (req, res) => {
  res.json({
    message: 'Welcome to AiElon Everything System API',
    principle: 'Everything = 1 | Tunggal AiElon',
    version: '1.0.0',
    documentation: '/api/v1/docs',
    health: '/health',
    subsystems: {
      livingOS: 'AiElon Living OS - AI-powered system management',
      fusionUI: 'Fusion HD UI - High-definition interface',
      halalWallet: 'Halal Wallet - Shariah-compliant finance',
      hcare: 'HCare - Healthcare management',
      ummahHub: 'Ummah Hub - Community platform'
    }
  });
});

// Error handling middleware
app.use(errorHandler);

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    status: 'error',
    message: 'Endpoint not found',
    path: req.path
  });
});

// Start server
const server = app.listen(PORT, HOST, () => {
  logger.info(`
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║            AiElon Everything System                           ║
║         Everything = 1 | Tunggal AiElon                       ║
║                                                               ║
║  Server running on: http://${HOST}:${PORT}                   ║
║  Environment: ${process.env.NODE_ENV || 'development'}       ║
║  API Version: v1                                              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
  `);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('SIGTERM signal received: closing HTTP server');
  server.close(() => {
    logger.info('HTTP server closed');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  logger.info('SIGINT signal received: closing HTTP server');
  server.close(() => {
    logger.info('HTTP server closed');
    process.exit(0);
  });
});

module.exports = app;
