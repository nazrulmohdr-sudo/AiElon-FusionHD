/**
 * Fusion Core Service
 * Central integration service for all modules
 */

import BlockchainService from './BlockchainService';
import BiometricService from './BiometricService';
import OracleService from './OracleService';
import NFTService from './NFTService';
import WalletConnectService from './WalletConnectService';
import Trade138Service from './Trade138Service';
import HCareService from './HCareService';
import SecurityService from './SecurityService';
import DAppFusionService from './DAppFusionService';

class FusionCoreService {
  constructor() {
    this.initialized = false;
    this.modules = {
      blockchain: BlockchainService,
      biometric: BiometricService,
      oracle: OracleService,
      nft: NFTService,
      walletConnect: WalletConnectService,
      trade138: Trade138Service,
      hcare: HCareService,
      security: SecurityService,
      dappFusion: DAppFusionService,
    };
    this.fusionMode = 'unified';
  }

  /**
   * Initialize all modules
   */
  async initializeAll() {
    try {
      console.log('Initializing Fusion Core...');
      
      const results = await Promise.all([
        this.modules.blockchain.initialize(),
        this.modules.biometric.checkAvailability(),
        this.modules.oracle.initialize(),
        this.modules.nft.initialize(),
        this.modules.walletConnect.initialize(),
        this.modules.trade138.initialize(),
        this.modules.hcare.initialize(),
        this.modules.security.initialize(),
        this.modules.dappFusion.initialize(),
      ]);

      this.initialized = true;

      return {
        success: true,
        message: 'All modules initialized',
        modules: results,
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
      };
    }
  }

  /**
   * Get module status
   */
  async getModuleStatus() {
    try {
      return {
        success: true,
        status: {
          blockchain: this.modules.blockchain.isConnected,
          biometric: this.modules.biometric.isAvailable,
          oracle: this.modules.oracle.isConnected,
          walletConnect: this.modules.walletConnect.isConnected,
          trade138: true,
          hcare: true,
          security: true,
          dappFusion: true,
        },
        fusionMode: this.fusionMode,
        initialized: this.initialized,
      };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Execute unified operation across modules
   */
  async executeUnifiedOperation(operation, params) {
    try {
      if (!this.initialized) {
        throw new Error('Fusion Core not initialized');
      }

      console.log(`Executing unified operation: ${operation}`);
      
      // Route operation to appropriate modules
      let result;
      switch (operation) {
        case 'wallet_connect':
          result = await this.modules.blockchain.connectWallet();
          break;
        case 'authenticate':
          result = await this.modules.biometric.authenticate();
          break;
        case 'get_market_data':
          result = await this.modules.oracle.getMarketData();
          break;
        case 'get_nfts':
          result = await this.modules.nft.getUserNFTs(params.address);
          break;
        case 'bridge_transfer':
          result = await this.modules.trade138.bridgeTransfer(
            params.fromChain,
            params.toChain,
            params.amount,
            params.asset
          );
          break;
        default:
          throw new Error(`Unknown operation: ${operation}`);
      }

      return {
        success: true,
        operation,
        result,
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
      };
    }
  }

  /**
   * Get all modules
   */
  getModules() {
    return this.modules;
  }

  /**
   * Set fusion mode
   */
  setFusionMode(mode) {
    this.fusionMode = mode;
    return { success: true, mode };
  }
}

export default new FusionCoreService();
