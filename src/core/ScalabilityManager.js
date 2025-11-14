/**
 * Scalability Manager for AiElon Living OS
 * Handles load balancing, resource management, and performance optimization
 */

export class ScalabilityManager {
  constructor() {
    this.resources = {
      cpu: { current: 0, max: 100, threshold: 80 },
      memory: { current: 0, max: 100, threshold: 75 },
      network: { current: 0, max: 100, threshold: 70 }
    };
    this.taskQueue = [];
    this.activeWorkers = 0;
    this.maxWorkers = 10;
    this.metrics = {
      tasksProcessed: 0,
      averageResponseTime: 0,
      peakLoad: 0
    };
  }

  /**
   * Monitor resource usage
   * @returns {Object} Current resource status
   */
  monitorResources() {
    // Simulate resource monitoring
    this.resources.cpu.current = Math.random() * 100;
    this.resources.memory.current = Math.random() * 100;
    this.resources.network.current = Math.random() * 100;
    
    return {
      cpu: this.resources.cpu.current,
      memory: this.resources.memory.current,
      network: this.resources.network.current,
      healthy: this.isHealthy()
    };
  }

  /**
   * Check if system is healthy based on thresholds
   * @returns {boolean} System health status
   */
  isHealthy() {
    return (
      this.resources.cpu.current < this.resources.cpu.threshold &&
      this.resources.memory.current < this.resources.memory.threshold &&
      this.resources.network.current < this.resources.network.threshold
    );
  }

  /**
   * Add task to queue with priority
   * @param {Function} task - Task to execute
   * @param {number} priority - Task priority (higher = more important)
   */
  addTask(task, priority = 5) {
    this.taskQueue.push({ task, priority, timestamp: Date.now() });
    this.taskQueue.sort((a, b) => b.priority - a.priority);
    this.processQueue();
  }

  /**
   * Process task queue with load balancing
   * @private
   */
  async processQueue() {
    while (this.taskQueue.length > 0 && this.activeWorkers < this.maxWorkers) {
      const { task, timestamp } = this.taskQueue.shift();
      this.activeWorkers++;
      
      try {
        const startTime = Date.now();
        await task();
        const duration = Date.now() - startTime;
        
        // Update metrics
        this.metrics.tasksProcessed++;
        this.metrics.averageResponseTime = 
          (this.metrics.averageResponseTime * (this.metrics.tasksProcessed - 1) + duration) 
          / this.metrics.tasksProcessed;
      } catch (error) {
        console.error('Task execution error:', error);
      } finally {
        this.activeWorkers--;
      }
    }
  }

  /**
   * Scale resources based on load
   * @param {string} resource - Resource type (cpu, memory, network)
   * @param {number} scale - Scale factor
   */
  scaleResource(resource, scale) {
    if (this.resources[resource]) {
      this.resources[resource].max *= scale;
      console.log(`Scaled ${resource} by ${scale}x`);
    }
  }

  /**
   * Auto-scale based on current load
   */
  autoScale() {
    const resources = this.monitorResources();
    
    if (resources.cpu > this.resources.cpu.threshold) {
      this.maxWorkers = Math.min(this.maxWorkers + 2, 20);
      console.log('Auto-scaling: Increased workers to', this.maxWorkers);
    } else if (resources.cpu < 30 && this.maxWorkers > 5) {
      this.maxWorkers = Math.max(this.maxWorkers - 1, 5);
      console.log('Auto-scaling: Decreased workers to', this.maxWorkers);
    }
  }

  /**
   * Get system metrics
   * @returns {Object} Performance metrics
   */
  getMetrics() {
    return {
      ...this.metrics,
      queueLength: this.taskQueue.length,
      activeWorkers: this.activeWorkers,
      maxWorkers: this.maxWorkers,
      resources: this.resources
    };
  }

  /**
   * Optimize performance
   */
  optimize() {
    // Clear old tasks
    const now = Date.now();
    this.taskQueue = this.taskQueue.filter(task => 
      now - task.timestamp < 300000 // Keep tasks less than 5 minutes old
    );
    
    // Auto-scale
    this.autoScale();
    
    return {
      tasksCleared: this.taskQueue.length,
      optimized: true
    };
  }
}

export const scalabilityManager = new ScalabilityManager();
