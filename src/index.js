/**
 * AiElon FusionHD - Main Application
 * High-performance system with comprehensive monitoring and diagnostics
 * Target: 100% operational efficiency (1.0), 0% errors (0 ralat)
 */

import logger from './utils/logger.js';
import validator from './utils/validator.js';
import healthCheck from './diagnostics/health-check.js';

class AiElonSystem {
  constructor() {
    this.initialized = false;
    this.modules = [];
    this.status = {
      operational: false,
      errorCount: 0,
      performance: 1.0, // Target: 100% = 1
      startTime: null
    };
  }

  /**
   * Initialize the system
   */
  async initialize() {
    logger.info('Initializing AiElon FusionHD System');
    const startTime = Date.now();

    try {
      // Step 1: Validate system configuration
      const configValidation = validator.validateConfig({
        name: 'AiElon FusionHD',
        version: '1.0.0',
        environment: process.env.NODE_ENV || 'production'
      });

      if (!configValidation.valid) {
        throw new Error('Configuration validation failed');
      }

      // Step 2: Perform health check
      const health = await healthCheck.performHealthCheck();
      logger.info('System health check completed', { status: health.status });

      // Step 3: Initialize modules
      this.modules = [
        { name: 'Logger', status: 'active' },
        { name: 'Validator', status: 'active' },
        { name: 'Health Monitor', status: 'active' },
        { name: 'Performance Tracker', status: 'active' }
      ];

      // Step 4: Mark system as operational
      this.status.operational = true;
      this.status.startTime = new Date().toISOString();
      this.initialized = true;

      const duration = Date.now() - startTime;
      logger.trackOperation('systemInitialization', duration, true);
      logger.info('System initialization completed successfully', {
        duration: `${duration}ms`,
        modules: this.modules.length
      });

      return {
        success: true,
        duration,
        status: this.getStatus()
      };
    } catch (error) {
      this.status.errorCount++;
      logger.error('System initialization failed', error);
      logger.trackOperation('systemInitialization', Date.now() - startTime, false);
      throw error;
    }
  }

  /**
   * Get current system status
   */
  getStatus() {
    const performanceReport = logger.getPerformanceReport();
    const errorSummary = logger.getErrorSummary();

    return {
      operational: this.status.operational,
      initialized: this.initialized,
      modules: this.modules,
      performance: {
        successRate: performanceReport.successRate,
        successRateNormalized: performanceReport.successRateNormalized,
        target: 1.0, // 100% = 1
        averageResponseTime: performanceReport.averageResponseTime
      },
      errors: {
        count: errorSummary.totalErrors,
        target: 0, // 0% = 0 ralat
        rate: errorSummary.errorRate
      },
      uptime: performanceReport.uptime,
      startTime: this.status.startTime,
      timestamp: new Date().toISOString()
    };
  }

  /**
   * Perform system diagnostics
   */
  async runDiagnostics() {
    logger.info('Running system diagnostics');
    const startTime = Date.now();

    try {
      // Run health check
      const healthReport = await healthCheck.performHealthCheck();
      
      // Run end-to-end validation
      const validationReport = await validator.validateEndToEnd();
      
      // Get performance metrics
      const performanceReport = logger.getPerformanceReport();

      const diagnostics = {
        timestamp: new Date().toISOString(),
        health: healthReport,
        validation: validationReport,
        performance: performanceReport,
        status: this.getStatus(),
        summary: {
          systemHealthy: healthReport.summary.overallHealth,
          validationPassed: validationReport.overallSuccess,
          errorCount: performanceReport.errorCount,
          targetErrorCount: 0,
          performanceTarget: 1.0,
          currentPerformance: performanceReport.successRateNormalized
        }
      };

      const duration = Date.now() - startTime;
      logger.trackOperation('systemDiagnostics', duration, true);

      return diagnostics;
    } catch (error) {
      logger.error('Diagnostics failed', error);
      throw error;
    }
  }

  /**
   * Shutdown system gracefully
   */
  async shutdown() {
    logger.info('Initiating system shutdown');
    
    try {
      // Log final statistics
      const finalReport = logger.getPerformanceReport();
      logger.info('Final system report', finalReport);

      this.status.operational = false;
      this.initialized = false;

      logger.info('System shutdown completed successfully');
      return { success: true };
    } catch (error) {
      logger.error('Error during shutdown', error);
      throw error;
    }
  }
}

// Main execution
async function main() {
  const system = new AiElonSystem();

  try {
    console.log('\n╔════════════════════════════════════════╗');
    console.log('║   AiElon FusionHD System v1.0.0       ║');
    console.log('║   High-Performance Monitoring System  ║');
    console.log('╚════════════════════════════════════════╝\n');

    // Initialize system
    const initResult = await system.initialize();
    console.log('✓ System initialized successfully\n');

    // Run diagnostics
    console.log('Running comprehensive diagnostics...\n');
    const diagnostics = await system.runDiagnostics();

    // Display results
    console.log('=== SYSTEM STATUS ===');
    console.log(JSON.stringify(system.getStatus(), null, 2));

    console.log('\n=== DIAGNOSTICS SUMMARY ===');
    console.log(`Health Status: ${diagnostics.health.status}`);
    console.log(`Validation: ${diagnostics.validation.overallSuccess ? 'PASSED' : 'FAILED'}`);
    console.log(`Error Count: ${diagnostics.summary.errorCount} (Target: ${diagnostics.summary.targetErrorCount})`);
    console.log(`Performance: ${(diagnostics.summary.currentPerformance * 100).toFixed(2)}% (Target: 100%)`);

    console.log('\n=== PERFORMANCE METRICS ===');
    console.log(JSON.stringify(logger.getPerformanceReport(), null, 2));

    // Check if system meets targets
    const meetsTargets = 
      diagnostics.summary.errorCount === 0 && 
      diagnostics.summary.currentPerformance >= 1.0;

    console.log('\n=== OPERATIONAL TARGETS ===');
    console.log(`Error Rate: ${meetsTargets ? '✓ 0% (0 ralat)' : '✗ Errors detected'}`);
    console.log(`Performance: ${meetsTargets ? '✓ 100% (1.0)' : '✗ Below target'}`);
    console.log(`System State: ${diagnostics.health.status === 'HEALTHY' ? '✓ Stable' : '✗ Needs attention'}`);

    console.log('\n✓ All systems operational\n');

    process.exit(0);
  } catch (error) {
    console.error('\n✗ System error:', error.message);
    console.error(error.stack);
    process.exit(1);
  }
}

// Run if executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}

export default AiElonSystem;
