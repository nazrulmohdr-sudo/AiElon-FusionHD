/**
 * Fusion HD UI - High-Definition User Interface Components
 * Modern, responsive UI framework for AiElon Living OS
 */

import { globalState } from '../core/StateManager.js';

export class FusionHDUI {
  constructor() {
    this.theme = 'light';
    this.resolution = 'HD';
    this.components = new Map();
    this.animations = true;
    this.accessibility = {
      highContrast: false,
      largeText: false,
      screenReader: false
    };
  }

  /**
   * Initialize UI
   * @returns {Object} Initialization result
   */
  initialize() {
    this.setupTheme();
    this.registerComponents();
    
    globalState.subscribe('theme', (newTheme) => {
      this.setTheme(newTheme);
    });
    
    return {
      success: true,
      theme: this.theme,
      resolution: this.resolution
    };
  }

  /**
   * Set UI theme
   * @param {string} theme - Theme name (light/dark)
   */
  setTheme(theme) {
    this.theme = theme;
    globalState.set('uiTheme', theme);
    console.log(`Theme changed to: ${theme}`);
  }

  /**
   * Setup theme
   * @private
   */
  setupTheme() {
    const themes = {
      light: {
        primary: '#007AFF',
        secondary: '#5856D6',
        background: '#FFFFFF',
        text: '#000000',
        accent: '#FF9500'
      },
      dark: {
        primary: '#0A84FF',
        secondary: '#5E5CE6',
        background: '#000000',
        text: '#FFFFFF',
        accent: '#FF9F0A'
      }
    };
    
    globalState.set('themeColors', themes[this.theme]);
  }

  /**
   * Register UI components
   * @private
   */
  registerComponents() {
    const components = [
      'Dashboard',
      'Navigation',
      'Card',
      'Button',
      'Modal',
      'Form',
      'Table',
      'Chart',
      'Notification',
      'Sidebar'
    ];
    
    components.forEach(component => {
      this.components.set(component, {
        name: component,
        registered: true,
        version: '2.0'
      });
    });
  }

  /**
   * Render dashboard
   * @param {Object} data - Dashboard data
   * @returns {string} Dashboard HTML
   */
  renderDashboard(data) {
    return `
╔════════════════════════════════════════════════════════════╗
║           AiElon Living OS - Fusion HD Dashboard          ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  System Status: ${data.systemStatus || 'Online'}                                  ║
║  Active Users:  ${data.activeUsers || 0}                                     ║
║  Blockchain:    ${data.blockchainStatus || 'Connected'}                             ║
║  Security:      ${data.securityStatus || 'Secure'}                                ║
║                                                            ║
║  📊 Quick Stats                                            ║
║  ├─ Transactions: ${data.transactions || 0}                              ║
║  ├─ Wallets:      ${data.wallets || 0}                              ║
║  ├─ Patients:     ${data.patients || 0}                              ║
║  └─ Community:    ${data.communityUsers || 0} users                       ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    `.trim();
  }

  /**
   * Render navigation menu
   * @returns {string} Navigation HTML
   */
  renderNavigation() {
    return `
┌─────────────────────────────────┐
│      Navigation Menu            │
├─────────────────────────────────┤
│  🏠 Dashboard                   │
│  💰 Halal Wallet                │
│  ⛓️  AiElonChain338              │
│  🏥 HCare                       │
│  👥 Ummah Hub                   │
│  ⚙️  Settings                    │
│  🔒 Security                    │
│  📊 Analytics                   │
└─────────────────────────────────┘
    `.trim();
  }

  /**
   * Create notification
   * @param {string} message - Notification message
   * @param {string} type - Notification type
   * @returns {Object} Notification
   */
  createNotification(message, type = 'info') {
    const icons = {
      info: 'ℹ️',
      success: '✅',
      warning: '⚠️',
      error: '❌'
    };
    
    const notification = {
      id: `notif_${Date.now()}`,
      message,
      type,
      icon: icons[type],
      timestamp: Date.now()
    };
    
    return notification;
  }

  /**
   * Render card component
   * @param {Object} cardData - Card content
   * @returns {string} Card HTML
   */
  renderCard(cardData) {
    return `
┌─────────────────────────────────┐
│  ${cardData.title || 'Card Title'}                  │
├─────────────────────────────────┤
│                                 │
│  ${cardData.content || 'Card content goes here'}              │
│                                 │
└─────────────────────────────────┘
    `.trim();
  }

  /**
   * Show loading animation
   * @param {string} message - Loading message
   * @returns {string} Loading animation
   */
  showLoading(message = 'Loading...') {
    return `
⣾ ${message}
    `.trim();
  }

  /**
   * Enable accessibility feature
   * @param {string} feature - Feature name
   */
  enableAccessibility(feature) {
    if (this.accessibility.hasOwnProperty(feature)) {
      this.accessibility[feature] = true;
      console.log(`Accessibility feature enabled: ${feature}`);
    }
  }

  /**
   * Get component info
   * @param {string} componentName - Component name
   * @returns {Object} Component information
   */
  getComponentInfo(componentName) {
    return this.components.get(componentName) || { error: 'Component not found' };
  }

  /**
   * Get UI statistics
   * @returns {Object} UI statistics
   */
  getStatistics() {
    return {
      theme: this.theme,
      resolution: this.resolution,
      components: this.components.size,
      animations: this.animations,
      accessibility: this.accessibility
    };
  }

  /**
   * Render table
   * @param {Array} headers - Table headers
   * @param {Array} rows - Table rows
   * @returns {string} Table HTML
   */
  renderTable(headers, rows) {
    let table = '┌';
    headers.forEach(() => table += '───────────────┬');
    table = table.slice(0, -1) + '┐\n│';
    
    headers.forEach(header => {
      table += ` ${header.padEnd(13)} │`;
    });
    
    table += '\n├';
    headers.forEach(() => table += '───────────────┼');
    table = table.slice(0, -1) + '┤\n';
    
    rows.forEach(row => {
      table += '│';
      row.forEach(cell => {
        table += ` ${String(cell).padEnd(13)} │`;
      });
      table += '\n';
    });
    
    table += '└';
    headers.forEach(() => table += '───────────────┴');
    table = table.slice(0, -1) + '┘';
    
    return table;
  }
}

export const fusionHDUI = new FusionHDUI();
