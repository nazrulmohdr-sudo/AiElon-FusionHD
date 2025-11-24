/**
 * AiElon Living OS - Core System
 * Version: 2.0.0
 * 
 * Main entry point for the AiElon Living OS ecosystem
 * Integrates all modules: Fusion HD UI, Halal Wallet, HCare, and Ummah Hub
 */

const express = require('express');
const os = require('./core/os');
const ui = require('./ui/fusion-hd');
const wallet = require('./wallet/halal-wallet');
const hcare = require('./hcare/hcare-system');
const ummahHub = require('./ummah-hub/ummah-platform');
const blockchain = require('./blockchain/aielonchain338');
const config = require('../config/system-config');

class AiElonLivingOS {
    constructor() {
        this.version = '2.0.0';
        this.modules = {};
        this.initialized = false;
        this.app = express();
    }

    /**
     * Initialize the AiElon Living OS
     * Sets up all core modules and integrations
     */
    async initialize() {
        console.log('🚀 Initializing AiElon Living OS v' + this.version);
        
        try {
            // Initialize core OS components
            console.log('📦 Loading core system...');
            this.modules.core = await os.initialize(config.core);
            
            // Initialize AielonChain338 blockchain integration
            console.log('⛓️  Connecting to AielonChain338...');
            this.modules.blockchain = await blockchain.initialize(config.blockchain);
            
            // Initialize Fusion HD UI
            console.log('🎨 Loading Fusion HD UI...');
            this.modules.ui = await ui.initialize(config.ui, this.app);
            
            // Initialize Halal Wallet
            console.log('💰 Initializing Halal Wallet...');
            this.modules.wallet = await wallet.initialize(config.wallet, this.modules.blockchain);
            
            // Initialize HCare system
            console.log('🏥 Starting HCare System...');
            this.modules.hcare = await hcare.initialize(config.hcare);
            
            // Initialize Ummah Hub
            console.log('🌐 Launching Ummah Hub...');
            this.modules.ummahHub = await ummahHub.initialize(config.ummahHub);
            
            this.initialized = true;
            console.log('✅ AiElon Living OS initialized successfully!');
            
            return true;
        } catch (error) {
            console.error('❌ Failed to initialize AiElon Living OS:', error);
            throw error;
        }
    }

    /**
     * Start the AiElon Living OS server
     */
    async start() {
        if (!this.initialized) {
            await this.initialize();
        }

        const port = config.server.port || 3000;
        
        this.app.listen(port, () => {
            console.log(`\n🌟 AiElon Living OS is running on port ${port}`);
            console.log(`📱 Access Fusion HD UI at: http://localhost:${port}`);
            console.log(`💳 Halal Wallet API: http://localhost:${port}/wallet`);
            console.log(`🏥 HCare Portal: http://localhost:${port}/hcare`);
            console.log(`🌍 Ummah Hub: http://localhost:${port}/ummah`);
        });
    }

    /**
     * Gracefully shutdown the system
     */
    async shutdown() {
        console.log('\n🛑 Shutting down AiElon Living OS...');
        
        if (this.modules.blockchain) {
            await this.modules.blockchain.disconnect();
        }
        
        console.log('✅ Shutdown complete');
        process.exit(0);
    }

    /**
     * Get system status
     */
    getStatus() {
        return {
            version: this.version,
            initialized: this.initialized,
            modules: {
                core: !!this.modules.core,
                ui: !!this.modules.ui,
                wallet: !!this.modules.wallet,
                hcare: !!this.modules.hcare,
                ummahHub: !!this.modules.ummahHub,
                blockchain: !!this.modules.blockchain
            }
        };
    }
}

// Handle graceful shutdown
process.on('SIGINT', async () => {
    if (global.aiElonOS) {
        await global.aiElonOS.shutdown();
    }
});

process.on('SIGTERM', async () => {
    if (global.aiElonOS) {
        await global.aiElonOS.shutdown();
    }
});

// Export for use as module
module.exports = AiElonLivingOS;

// Run if executed directly
if (require.main === module) {
    const aiElonOS = new AiElonLivingOS();
    global.aiElonOS = aiElonOS;
    aiElonOS.start().catch(error => {
        console.error('Fatal error:', error);
        process.exit(1);
    });
}
