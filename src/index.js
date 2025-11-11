/**
 * AiElon Living OS - Main Entry Point
 * Advanced Operating System with Blockchain, Healthcare, and Community Features
 */

import { globalState } from './core/StateManager.js';
import { scalabilityManager } from './core/ScalabilityManager.js';
import { aiElonChain338 } from './modules/blockchain/AiElonChain338.js';
import { securityManager } from './security/SecurityManager.js';
import { halalWallet } from './modules/wallet/HalalWallet.js';
import { hcare } from './modules/hcare/HCare.js';
import { ummahHub } from './modules/ummah/UmmahHub.js';
import { fusionHDUI } from './ui/FusionHDUI.js';

/**
 * AiElon Living OS - Main System Class
 */
class AiElonLivingOS {
  constructor() {
    this.version = '2.0.0';
    this.name = 'AiElon Living OS';
    this.initialized = false;
    this.modules = {};
  }

  /**
   * Initialize the operating system
   */
  async initialize() {
    console.log(`\n╔════════════════════════════════════════════════════════════╗`);
    console.log(`║     AiElon Living OS v${this.version} - Initializing...          ║`);
    console.log(`╚════════════════════════════════════════════════════════════╝\n`);

    try {
      // Initialize UI
      console.log('📱 Initializing Fusion HD UI...');
      fusionHDUI.initialize();
      this.modules.ui = fusionHDUI;

      // Initialize security
      console.log('🔒 Initializing Security Layer...');
      this.modules.security = securityManager;
      globalState.set('securityInitialized', true);

      // Initialize blockchain
      console.log('⛓️  Initializing AiElonChain338...');
      this.modules.blockchain = aiElonChain338;
      globalState.set('blockchainConnected', true);

      // Initialize scalability manager
      console.log('📈 Initializing Scalability Manager...');
      this.modules.scalability = scalabilityManager;
      
      // Initialize modules
      console.log('💰 Initializing Halal Wallet...');
      this.modules.wallet = halalWallet;
      
      console.log('🏥 Initializing HCare...');
      this.modules.hcare = hcare;
      
      console.log('👥 Initializing Ummah Hub...');
      this.modules.ummah = ummahHub;

      // Set global state
      globalState.set('osVersion', this.version);
      globalState.set('systemStatus', 'online');
      globalState.set('initTimestamp', Date.now());

      this.initialized = true;

      console.log('\n✅ System initialized successfully!\n');
      
      // Display system dashboard
      this.displayDashboard();
      
      return {
        success: true,
        version: this.version,
        modules: Object.keys(this.modules)
      };
    } catch (error) {
      console.error('❌ Initialization failed:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Display system dashboard
   */
  displayDashboard() {
    const stats = this.getSystemStats();
    const dashboard = fusionHDUI.renderDashboard({
      systemStatus: 'Online',
      activeUsers: stats.activeUsers,
      blockchainStatus: stats.blockchainValid ? 'Connected' : 'Disconnected',
      securityStatus: 'Secure',
      transactions: stats.pendingTransactions,
      wallets: 0,
      patients: stats.patients,
      communityUsers: stats.communityUsers
    });

    console.log(dashboard);
    console.log('\n' + fusionHDUI.renderNavigation());
  }

  /**
   * Get system statistics
   */
  getSystemStats() {
    const blockchainInfo = aiElonChain338.getChainInfo();
    const hcareStats = hcare.getStatistics();
    const ummahStats = ummahHub.getStatistics();
    const securityStatus = securityManager.getSecurityStatus();
    const scalabilityMetrics = scalabilityManager.getMetrics();

    return {
      version: this.version,
      uptime: Date.now() - (globalState.get('initTimestamp') || Date.now()),
      blockHeight: blockchainInfo.blockHeight,
      pendingTransactions: blockchainInfo.pendingTransactions,
      blockchainValid: blockchainInfo.isValid,
      patients: hcareStats.totalPatients,
      communityUsers: ummahStats.totalUsers,
      activeSessions: securityStatus.activeSessions,
      activeUsers: securityStatus.activeSessions,
      tasksProcessed: scalabilityMetrics.tasksProcessed,
      avgResponseTime: scalabilityMetrics.averageResponseTime
    };
  }

  /**
   * Demonstrate system capabilities
   */
  async demonstrateCapabilities() {
    console.log('\n🎯 Demonstrating AiElon Living OS Capabilities...\n');

    // 1. Global State Management
    console.log('1️⃣  Global State Management:');
    globalState.set('demoKey', 'demoValue');
    console.log('   ✓ State set:', globalState.get('demoKey'));
    console.log('   ✓ History tracking:', globalState.getHistory().length, 'entries');

    // 2. Blockchain Demo
    console.log('\n2️⃣  AiElonChain338 Blockchain:');
    const wallet1 = halalWallet.createWallet('User1');
    const wallet2 = halalWallet.createWallet('User2');
    console.log('   ✓ Created wallets:', wallet1.address, wallet2.address);
    
    aiElonChain338.addTransaction({
      from: 'system',
      to: wallet1.address,
      amount: 1000
    });
    const block = aiElonChain338.minePendingTransactions('miner1');
    console.log('   ✓ Mined block:', block.index);
    console.log('   ✓ Chain valid:', aiElonChain338.isChainValid());

    // 3. Halal Wallet Demo
    console.log('\n3️⃣  Halal Wallet (Sharia-Compliant):');
    const balance = halalWallet.getBalance(wallet1.address);
    console.log('   ✓ Wallet balance:', balance.balance);
    const zakatInfo = halalWallet.calculateZakat(wallet1.address);
    console.log('   ✓ Zakat calculation:', zakatInfo);

    // 4. HCare Demo
    console.log('\n4️⃣  HCare Healthcare System:');
    const patient = hcare.registerPatient({
      name: 'John Doe',
      dateOfBirth: '1990-01-01',
      bloodType: 'O+',
      allergies: ['penicillin']
    });
    console.log('   ✓ Patient registered:', patient.patientId);
    
    const vitals = hcare.recordVitals(patient.patientId, {
      heartRate: 75,
      bloodPressure: '120/80',
      temperature: 37.0,
      oxygenLevel: 98,
      weight: 70
    });
    console.log('   ✓ Vitals recorded, alerts:', vitals.alerts.length);

    // 5. Ummah Hub Demo
    console.log('\n5️⃣  Ummah Hub Community:');
    const user1 = ummahHub.registerUser({
      username: 'user1',
      email: 'user1@example.com',
      location: 'City'
    });
    console.log('   ✓ User registered:', user1.username);
    
    const post = ummahHub.createPost(user1.userId, {
      content: 'Welcome to Ummah Hub!',
      type: 'text',
      tags: ['welcome', 'community']
    });
    console.log('   ✓ Post created:', post.post.id);

    // 6. Security Demo
    console.log('\n6️⃣  Security System:');
    const auth = securityManager.authenticate('testuser', 'password123');
    console.log('   ✓ Authentication:', auth.success);
    const encrypted = securityManager.encrypt('sensitive data');
    console.log('   ✓ Encryption active:', encrypted.startsWith('enc:'));
    const secStatus = securityManager.getSecurityStatus();
    console.log('   ✓ Security status:', secStatus.status);

    // 7. Scalability Demo
    console.log('\n7️⃣  Scalability Management:');
    const resources = scalabilityManager.monitorResources();
    console.log('   ✓ System health:', resources.healthy ? 'Healthy' : 'Degraded');
    console.log('   ✓ CPU usage:', resources.cpu.toFixed(2) + '%');
    const metrics = scalabilityManager.getMetrics();
    console.log('   ✓ Active workers:', metrics.activeWorkers);

    console.log('\n✅ Demonstration complete!\n');
  }

  /**
   * Get module
   * @param {string} moduleName - Module name
   * @returns {Object} Module instance
   */
  getModule(moduleName) {
    return this.modules[moduleName];
  }

  /**
   * Get system status
   */
  getStatus() {
    return {
      name: this.name,
      version: this.version,
      initialized: this.initialized,
      modules: Object.keys(this.modules),
      stats: this.getSystemStats()
    };
  }
}

// Create and start the OS
const os = new AiElonLivingOS();

// Initialize and demonstrate
async function start() {
  await os.initialize();
  await os.demonstrateCapabilities();
  
  // Show final status
  console.log('\n📊 Final System Status:');
  const status = os.getStatus();
  console.log(JSON.stringify(status, null, 2));
}

start().catch(console.error);

export { AiElonLivingOS, os as aiElonOS };
