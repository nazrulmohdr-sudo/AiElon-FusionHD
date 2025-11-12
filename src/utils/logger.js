/**
 * Advanced Logging System for AiElon FusionHD
 * Provides structured logging with performance tracking and error monitoring
 * Target: 0% errors (0 ralat), 100% operational visibility
 */

class Logger {
  constructor() {
    this.logs = [];
    this.errorCount = 0;
    this.performanceMetrics = {
      totalOperations: 0,
      successfulOperations: 0,
      failedOperations: 0,
      averageResponseTime: 0
    };
    this.startTime = Date.now();
  }

  /**
   * Format timestamp for logs
   */
  getTimestamp() {
    return new Date().toISOString();
  }

  /**
   * Log info level message
   */
  info(message, metadata = {}) {
    const logEntry = {
      level: 'INFO',
      timestamp: this.getTimestamp(),
      message,
      metadata
    };
    this.logs.push(logEntry);
    console.log(`[${logEntry.timestamp}] INFO: ${message}`, metadata);
  }

  /**
   * Log warning level message
   */
  warn(message, metadata = {}) {
    const logEntry = {
      level: 'WARN',
      timestamp: this.getTimestamp(),
      message,
      metadata
    };
    this.logs.push(logEntry);
    console.warn(`[${logEntry.timestamp}] WARN: ${message}`, metadata);
  }

  /**
   * Log error level message
   */
  error(message, error = null, metadata = {}) {
    this.errorCount++;
    const logEntry = {
      level: 'ERROR',
      timestamp: this.getTimestamp(),
      message,
      error: error ? {
        name: error.name,
        message: error.message,
        stack: error.stack
      } : null,
      metadata
    };
    this.logs.push(logEntry);
    console.error(`[${logEntry.timestamp}] ERROR: ${message}`, error, metadata);
  }

  /**
   * Log debug level message
   */
  debug(message, metadata = {}) {
    const logEntry = {
      level: 'DEBUG',
      timestamp: this.getTimestamp(),
      message,
      metadata
    };
    this.logs.push(logEntry);
    if (process.env.DEBUG === 'true') {
      console.debug(`[${logEntry.timestamp}] DEBUG: ${message}`, metadata);
    }
  }

  /**
   * Track operation performance
   */
  trackOperation(operationName, duration, success = true) {
    this.performanceMetrics.totalOperations++;
    if (success) {
      this.performanceMetrics.successfulOperations++;
    } else {
      this.performanceMetrics.failedOperations++;
    }

    // Update average response time
    const currentAvg = this.performanceMetrics.averageResponseTime;
    const total = this.performanceMetrics.totalOperations;
    this.performanceMetrics.averageResponseTime = 
      (currentAvg * (total - 1) + duration) / total;

    this.info(`Operation tracked: ${operationName}`, {
      duration: `${duration}ms`,
      success,
      averageResponseTime: `${this.performanceMetrics.averageResponseTime.toFixed(2)}ms`
    });
  }

  /**
   * Get system performance report
   */
  getPerformanceReport() {
    const uptime = Date.now() - this.startTime;
    const successRate = this.performanceMetrics.totalOperations > 0
      ? (this.performanceMetrics.successfulOperations / this.performanceMetrics.totalOperations) * 100
      : 100;

    return {
      uptime: `${(uptime / 1000).toFixed(2)}s`,
      totalOperations: this.performanceMetrics.totalOperations,
      successfulOperations: this.performanceMetrics.successfulOperations,
      failedOperations: this.performanceMetrics.failedOperations,
      successRate: `${successRate.toFixed(2)}%`,
      successRateNormalized: successRate / 100, // 100% = 1
      averageResponseTime: `${this.performanceMetrics.averageResponseTime.toFixed(2)}ms`,
      errorCount: this.errorCount,
      errorRate: `${this.errorCount}`, // Target: 0 ralat
      totalLogs: this.logs.length
    };
  }

  /**
   * Get all logs
   */
  getLogs(level = null) {
    if (level) {
      return this.logs.filter(log => log.level === level);
    }
    return this.logs;
  }

  /**
   * Get error summary
   */
  getErrorSummary() {
    const errors = this.getLogs('ERROR');
    return {
      totalErrors: this.errorCount,
      targetErrors: 0, // 0% = 0 ralat
      errorRate: this.errorCount === 0 ? '0%' : `${this.errorCount} errors`,
      recentErrors: errors.slice(-10)
    };
  }

  /**
   * Clear old logs (keep last 1000)
   */
  purgeLogs() {
    if (this.logs.length > 1000) {
      const removed = this.logs.length - 1000;
      this.logs = this.logs.slice(-1000);
      this.info(`Purged ${removed} old log entries`);
    }
  }
}

// Export singleton instance
const logger = new Logger();
export default logger;
