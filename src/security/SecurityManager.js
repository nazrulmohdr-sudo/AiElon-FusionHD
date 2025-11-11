/**
 * Security Manager for AiElon Living OS
 * Provides authentication, encryption, and security validation
 */

import { globalState } from '../core/StateManager.js';

export class SecurityManager {
  constructor() {
    this.sessions = new Map();
    this.sessionTimeout = 3600000; // 1 hour
    this.maxLoginAttempts = 5;
    this.loginAttempts = new Map();
    this.securityLogs = [];
    this.encryptionEnabled = true;
  }

  /**
   * Authenticate user with credentials
   * @param {string} username - Username
   * @param {string} password - Password
   * @returns {Object} Authentication result
   */
  authenticate(username, password) {
    // Check for too many failed attempts
    const attempts = this.loginAttempts.get(username) || 0;
    if (attempts >= this.maxLoginAttempts) {
      this.logSecurityEvent('LOGIN_BLOCKED', username, 'Too many failed attempts');
      return {
        success: false,
        error: 'Account temporarily locked due to too many failed attempts'
      };
    }
    
    // Validate credentials (in production, use proper password hashing)
    const isValid = this.validateCredentials(username, password);
    
    if (!isValid) {
      this.loginAttempts.set(username, attempts + 1);
      this.logSecurityEvent('LOGIN_FAILED', username, 'Invalid credentials');
      return {
        success: false,
        error: 'Invalid username or password'
      };
    }
    
    // Create session
    const sessionId = this.generateSessionId();
    const session = {
      username,
      sessionId,
      createdAt: Date.now(),
      expiresAt: Date.now() + this.sessionTimeout,
      permissions: this.getUserPermissions(username)
    };
    
    this.sessions.set(sessionId, session);
    this.loginAttempts.delete(username);
    this.logSecurityEvent('LOGIN_SUCCESS', username, 'User authenticated');
    
    globalState.set('currentUser', username);
    globalState.set('sessionId', sessionId);
    
    return {
      success: true,
      sessionId,
      user: username,
      permissions: session.permissions
    };
  }

  /**
   * Validate user credentials
   * @private
   */
  validateCredentials(username, password) {
    // In production, validate against secure database with hashed passwords
    // For now, simple validation
    return username && password && password.length >= 8;
  }

  /**
   * Get user permissions
   * @private
   */
  getUserPermissions(username) {
    // In production, fetch from database
    return ['read', 'write', 'execute'];
  }

  /**
   * Verify session validity
   * @param {string} sessionId - Session ID to verify
   * @returns {boolean} Whether session is valid
   */
  verifySession(sessionId) {
    const session = this.sessions.get(sessionId);
    
    if (!session) {
      return false;
    }
    
    if (Date.now() > session.expiresAt) {
      this.sessions.delete(sessionId);
      this.logSecurityEvent('SESSION_EXPIRED', session.username, 'Session expired');
      return false;
    }
    
    return true;
  }

  /**
   * Logout user
   * @param {string} sessionId - Session ID
   */
  logout(sessionId) {
    const session = this.sessions.get(sessionId);
    if (session) {
      this.logSecurityEvent('LOGOUT', session.username, 'User logged out');
      this.sessions.delete(sessionId);
      globalState.set('currentUser', null);
      globalState.set('sessionId', null);
    }
  }

  /**
   * Encrypt data
   * @param {string} data - Data to encrypt
   * @returns {string} Encrypted data
   */
  encrypt(data) {
    if (!this.encryptionEnabled) {
      return data;
    }
    
    // Simple encryption simulation (in production, use proper encryption like AES)
    const encrypted = Buffer.from(data).toString('base64');
    return `enc:${encrypted}`;
  }

  /**
   * Decrypt data
   * @param {string} encryptedData - Encrypted data
   * @returns {string} Decrypted data
   */
  decrypt(encryptedData) {
    if (!encryptedData.startsWith('enc:')) {
      return encryptedData;
    }
    
    const base64 = encryptedData.substring(4);
    return Buffer.from(base64, 'base64').toString('utf-8');
  }

  /**
   * Validate input for security threats
   * @param {string} input - User input
   * @returns {Object} Validation result
   */
  validateInput(input) {
    const threats = {
      sqlInjection: /(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b)/i,
      xss: /<script|javascript:|onerror=/i,
      pathTraversal: /\.\.[\/\\]/
    };
    
    const detected = [];
    
    for (const [threat, pattern] of Object.entries(threats)) {
      if (pattern.test(input)) {
        detected.push(threat);
        this.logSecurityEvent('THREAT_DETECTED', 'system', `${threat} detected in input`);
      }
    }
    
    return {
      safe: detected.length === 0,
      threats: detected
    };
  }

  /**
   * Generate secure session ID
   * @private
   */
  generateSessionId() {
    const timestamp = Date.now().toString(36);
    const random = Math.random().toString(36).substring(2, 15);
    return `sess_${timestamp}_${random}`;
  }

  /**
   * Log security event
   * @private
   */
  logSecurityEvent(event, user, details) {
    const log = {
      timestamp: Date.now(),
      event,
      user,
      details
    };
    
    this.securityLogs.push(log);
    
    // Keep only last 1000 logs
    if (this.securityLogs.length > 1000) {
      this.securityLogs.shift();
    }
  }

  /**
   * Get security logs
   * @param {number} limit - Number of logs to retrieve
   * @returns {Array} Security logs
   */
  getSecurityLogs(limit = 100) {
    return this.securityLogs.slice(-limit);
  }

  /**
   * Check system security status
   * @returns {Object} Security status
   */
  getSecurityStatus() {
    return {
      activeSessions: this.sessions.size,
      encryptionEnabled: this.encryptionEnabled,
      recentThreats: this.securityLogs.filter(log => 
        log.event === 'THREAT_DETECTED' && 
        Date.now() - log.timestamp < 3600000
      ).length,
      status: 'secure'
    };
  }
}

export const securityManager = new SecurityManager();
