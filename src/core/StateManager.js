/**
 * Global State Management System for AiElon Living OS
 * Provides centralized state management with reactive updates
 */

export class StateManager {
  constructor() {
    this.state = new Map();
    this.listeners = new Map();
    this.history = [];
    this.maxHistorySize = 100;
  }

  /**
   * Get a value from the global state
   * @param {string} key - The state key
   * @returns {*} The state value
   */
  get(key) {
    return this.state.get(key);
  }

  /**
   * Set a value in the global state with history tracking
   * @param {string} key - The state key
   * @param {*} value - The state value
   */
  set(key, value) {
    const oldValue = this.state.get(key);
    this.state.set(key, value);
    
    // Track history
    this.history.push({
      timestamp: Date.now(),
      key,
      oldValue,
      newValue: value
    });
    
    // Limit history size
    if (this.history.length > this.maxHistorySize) {
      this.history.shift();
    }
    
    // Notify listeners
    this.notifyListeners(key, value, oldValue);
  }

  /**
   * Subscribe to state changes
   * @param {string} key - The state key to watch
   * @param {Function} callback - Callback function
   */
  subscribe(key, callback) {
    if (!this.listeners.has(key)) {
      this.listeners.set(key, []);
    }
    this.listeners.get(key).push(callback);
  }

  /**
   * Unsubscribe from state changes
   * @param {string} key - The state key
   * @param {Function} callback - The callback to remove
   */
  unsubscribe(key, callback) {
    if (this.listeners.has(key)) {
      const callbacks = this.listeners.get(key);
      const index = callbacks.indexOf(callback);
      if (index > -1) {
        callbacks.splice(index, 1);
      }
    }
  }

  /**
   * Notify all listeners of a state change
   * @private
   */
  notifyListeners(key, newValue, oldValue) {
    if (this.listeners.has(key)) {
      this.listeners.get(key).forEach(callback => {
        try {
          callback(newValue, oldValue);
        } catch (error) {
          console.error(`Error in state listener for key ${key}:`, error);
        }
      });
    }
  }

  /**
   * Get state history
   * @returns {Array} State change history
   */
  getHistory() {
    return [...this.history];
  }

  /**
   * Clear all state
   */
  clear() {
    this.state.clear();
    this.listeners.clear();
    this.history = [];
  }

  /**
   * Get all state as an object
   * @returns {Object} All state data
   */
  getAll() {
    return Object.fromEntries(this.state);
  }

  /**
   * Batch update multiple state values
   * @param {Object} updates - Key-value pairs to update
   */
  batchUpdate(updates) {
    Object.entries(updates).forEach(([key, value]) => {
      this.set(key, value);
    });
  }
}

// Export singleton instance
export const globalState = new StateManager();
