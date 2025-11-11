/**
 * System Health Check and Diagnostics
 * Monitors system health and provides real-time status
 * Target: 100% system availability, 0 critical issues
 */

import logger from '../utils/logger.js';

class HealthCheck {
  constructor() {
    this.checks = [];
    this.systemStatus = 'HEALTHY';
  }

  /**
   * Check memory usage
   */
  checkMemory() {
    const memoryUsage = process.memoryUsage();
    const heapUsedMB = (memoryUsage.heapUsed / 1024 / 1024).toFixed(2);
    const heapTotalMB = (memoryUsage.heapTotal / 1024 / 1024).toFixed(2);
    const usagePercent = (memoryUsage.heapUsed / memoryUsage.heapTotal * 100).toFixed(2);

    const status = usagePercent < 90 ? 'HEALTHY' : 'WARNING';

    return {
      name: 'Memory',
      status,
      metrics: {
        heapUsed: `${heapUsedMB} MB`,
        heapTotal: `${heapTotalMB} MB`,
        usagePercent: `${usagePercent}%`
      },
      healthy: status === 'HEALTHY'
    };
  }

  /**
   * Check Node.js version
   */
  checkNodeVersion() {
    const version = process.version;
    const majorVersion = parseInt(version.slice(1).split('.')[0]);
    const status = majorVersion >= 18 ? 'HEALTHY' : 'WARNING';

    return {
      name: 'Node.js Version',
      status,
      metrics: {
        version,
        required: '>=18.0.0'
      },
      healthy: status === 'HEALTHY'
    };
  }

  /**
   * Check system uptime
   */
  checkUptime() {
    const uptime = process.uptime();
    const uptimeSeconds = uptime.toFixed(2);
    const uptimeMinutes = (uptime / 60).toFixed(2);

    return {
      name: 'System Uptime',
      status: 'HEALTHY',
      metrics: {
        seconds: uptimeSeconds,
        minutes: uptimeMinutes
      },
      healthy: true
    };
  }

  /**
   * Check logger health
   */
  checkLogger() {
    try {
      const report = logger.getPerformanceReport();
      const errorSummary = logger.getErrorSummary();
      
      // System is healthy if error count is 0 (target: 0 ralat)
      const status = errorSummary.totalErrors === 0 ? 'HEALTHY' : 'WARNING';

      return {
        name: 'Logger System',
        status,
        metrics: {
          errorCount: errorSummary.totalErrors,
          targetErrors: 0,
          successRate: report.successRate,
          totalOperations: report.totalOperations
        },
        healthy: status === 'HEALTHY'
      };
    } catch (error) {
      logger.error('Logger health check failed', error);
      return {
        name: 'Logger System',
        status: 'CRITICAL',
        error: error.message,
        healthy: false
      };
    }
  }

  /**
   * Check overall performance
   */
  checkPerformance() {
    try {
      const report = logger.getPerformanceReport();
      
      // Target: 100% success rate (1.0)
      const performanceTarget = 1.0;
      const actual = report.successRateNormalized;
      const status = actual >= performanceTarget * 0.95 ? 'HEALTHY' : 'WARNING';

      return {
        name: 'System Performance',
        status,
        metrics: {
          successRate: report.successRate,
          successRateNormalized: actual,
          target: performanceTarget,
          averageResponseTime: report.averageResponseTime
        },
        healthy: status === 'HEALTHY'
      };
    } catch (error) {
      return {
        name: 'System Performance',
        status: 'CRITICAL',
        error: error.message,
        healthy: false
      };
    }
  }

  /**
   * Perform comprehensive health check
   */
  async performHealthCheck() {
    logger.info('Starting comprehensive health check');
    const startTime = Date.now();

    this.checks = [
      this.checkMemory(),
      this.checkNodeVersion(),
      this.checkUptime(),
      this.checkLogger(),
      this.checkPerformance()
    ];

    const allHealthy = this.checks.every(check => check.healthy);
    const criticalIssues = this.checks.filter(check => check.status === 'CRITICAL');
    const warnings = this.checks.filter(check => check.status === 'WARNING');

    if (criticalIssues.length > 0) {
      this.systemStatus = 'CRITICAL';
    } else if (warnings.length > 0) {
      this.systemStatus = 'WARNING';
    } else {
      this.systemStatus = 'HEALTHY';
    }

    const duration = Date.now() - startTime;
    const report = {
      timestamp: new Date().toISOString(),
      status: this.systemStatus,
      checks: this.checks,
      summary: {
        totalChecks: this.checks.length,
        healthyChecks: this.checks.filter(c => c.healthy).length,
        warningChecks: warnings.length,
        criticalChecks: criticalIssues.length,
        overallHealth: allHealthy,
        performanceScore: `${((this.checks.filter(c => c.healthy).length / this.checks.length) * 100).toFixed(2)}%`
      },
      duration: `${duration}ms`,
      targets: {
        errorCount: 0, // 0% = 0 ralat
        performanceRate: 1.0, // 100% = 1
        systemStatus: 'HEALTHY'
      }
    };

    logger.trackOperation('healthCheck', duration, allHealthy);
    logger.info('Health check completed', report.summary);

    return report;
  }

  /**
   * Get current system status
   */
  getStatus() {
    return {
      status: this.systemStatus,
      timestamp: new Date().toISOString(),
      checksPerformed: this.checks.length
    };
  }
}

// Export singleton instance
const healthCheck = new HealthCheck();
export default healthCheck;

// CLI execution
if (import.meta.url === `file://${process.argv[1]}`) {
  healthCheck.performHealthCheck().then(report => {
    console.log('\n=== SYSTEM HEALTH CHECK REPORT ===\n');
    console.log(JSON.stringify(report, null, 2));
    process.exit(report.summary.overallHealth ? 0 : 1);
  });
}
