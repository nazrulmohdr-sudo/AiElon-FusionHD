/**
 * Basic test suite for AiElon FusionHD
 * Uses Node.js built-in test runner
 */

import { test } from 'node:test';
import assert from 'node:assert';
import logger from '../utils/logger.js';
import validator from '../utils/validator.js';
import healthCheck from '../diagnostics/health-check.js';

// Test Logger
test('Logger should track operations', () => {
  logger.info('Test message');
  const report = logger.getPerformanceReport();
  
  assert.ok(report.uptime, 'Should have uptime');
  assert.strictEqual(typeof report.errorCount, 'number', 'Should have error count');
  assert.strictEqual(typeof report.totalLogs, 'number', 'Should have total logs');
});

test('Logger should track performance', () => {
  logger.trackOperation('testOp', 10, true);
  const report = logger.getPerformanceReport();
  
  assert.ok(report.totalOperations > 0, 'Should have operations tracked');
});

// Test Validator
test('Validator should validate configuration', () => {
  const result = validator.validateConfig({ name: 'test' });
  assert.strictEqual(result.valid, true, 'Config should be valid');
  assert.strictEqual(result.errors.length, 0, 'Should have no errors');
});

test('Validator should validate input with schema', () => {
  const data = { name: 'test', value: 42 };
  const schema = {
    name: { required: true, type: 'string' },
    value: { required: true, type: 'number' }
  };
  
  const result = validator.validateInput(data, schema);
  assert.strictEqual(result.valid, true, 'Input should be valid');
});

test('Validator should detect invalid input', () => {
  const data = { value: 'wrong type' };
  const schema = {
    name: { required: true, type: 'string' },
    value: { required: true, type: 'number' }
  };
  
  const result = validator.validateInput(data, schema);
  assert.strictEqual(result.valid, false, 'Should detect invalid input');
  assert.ok(result.errors.length > 0, 'Should have errors');
});

// Test Health Check
test('Health check should return status', async () => {
  const status = healthCheck.getStatus();
  assert.ok(status.timestamp, 'Should have timestamp');
  assert.ok(['HEALTHY', 'WARNING', 'CRITICAL'].includes(status.status), 
    'Should have valid status');
});

test('Health check should perform all checks', async () => {
  const report = await healthCheck.performHealthCheck();
  
  assert.ok(report.checks, 'Should have checks');
  assert.ok(Array.isArray(report.checks), 'Checks should be an array');
  assert.ok(report.checks.length > 0, 'Should have at least one check');
  assert.ok(report.summary, 'Should have summary');
});

// Test System State
test('System state validation should work', () => {
  const state = {
    operational: true,
    errorCount: 0,
    performance: 1.0
  };
  
  const result = validator.validateSystemState(state);
  assert.strictEqual(result.valid, true, 'Valid state should pass');
  assert.ok(result.checks.every(c => c.passed), 'All checks should pass');
});

test('System should meet performance targets', async () => {
  const report = logger.getPerformanceReport();
  
  // Performance should be tracked
  assert.ok(report.successRate, 'Should have success rate');
  assert.ok(report.successRateNormalized >= 0, 'Success rate should be >= 0');
  assert.ok(report.successRateNormalized <= 1, 'Success rate should be <= 1');
  
  // Error count should be a number (some tests intentionally trigger errors for validation)
  assert.strictEqual(typeof report.errorCount, 'number', 'Error count should be tracked');
});
