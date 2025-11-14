/**
 * Halal Wallet Module
 * Sharia-compliant digital wallet with ethical transaction management
 */

import { aiElonChain338 } from '../blockchain/AiElonChain338.js';
import { securityManager } from '../../security/SecurityManager.js';
import { globalState } from '../../core/StateManager.js';

export class HalalWallet {
  constructor() {
    this.wallets = new Map();
    this.complianceRules = {
      prohibitedSectors: ['alcohol', 'gambling', 'tobacco', 'weapons'],
      maxInterestRate: 0, // No interest allowed in Islamic finance
      requiresZakat: true
    };
  }

  /**
   * Create a new Halal wallet
   * @param {string} owner - Wallet owner
   * @returns {Object} Wallet details
   */
  createWallet(owner) {
    const address = this.generateWalletAddress();
    const wallet = {
      address,
      owner,
      balance: 0,
      createdAt: Date.now(),
      transactions: [],
      zakatDue: 0,
      complianceScore: 100
    };
    
    this.wallets.set(address, wallet);
    globalState.set(`wallet_${owner}`, address);
    
    return {
      address,
      owner,
      balance: 0,
      status: 'active'
    };
  }

  /**
   * Send transaction (with Sharia compliance check)
   * @param {string} fromAddress - Sender address
   * @param {string} toAddress - Recipient address
   * @param {number} amount - Amount to send
   * @param {string} purpose - Transaction purpose
   * @returns {Object} Transaction result
   */
  sendTransaction(fromAddress, toAddress, amount, purpose = 'transfer') {
    const wallet = this.wallets.get(fromAddress);
    
    if (!wallet) {
      return { success: false, error: 'Wallet not found' };
    }
    
    // Check compliance
    const compliance = this.checkCompliance(purpose);
    if (!compliance.compliant) {
      return {
        success: false,
        error: `Transaction not Sharia-compliant: ${compliance.reason}`
      };
    }
    
    // Check balance
    const currentBalance = aiElonChain338.getBalance(fromAddress);
    if (currentBalance < amount) {
      return { success: false, error: 'Insufficient balance' };
    }
    
    // Create blockchain transaction
    const transaction = aiElonChain338.addTransaction({
      from: fromAddress,
      to: toAddress,
      amount,
      purpose,
      compliant: true
    });
    
    // Update wallet records
    wallet.transactions.push(transaction);
    this.updateZakatCalculation(wallet);
    
    return {
      success: true,
      transaction,
      message: 'Transaction submitted successfully'
    };
  }

  /**
   * Check if transaction is Sharia-compliant
   * @private
   */
  checkCompliance(purpose) {
    for (const prohibited of this.complianceRules.prohibitedSectors) {
      if (purpose.toLowerCase().includes(prohibited)) {
        return {
          compliant: false,
          reason: `Transactions related to ${prohibited} are not permitted`
        };
      }
    }
    
    return { compliant: true };
  }

  /**
   * Calculate Zakat (Islamic charity obligation)
   * @param {string} address - Wallet address
   * @returns {Object} Zakat calculation
   */
  calculateZakat(address) {
    const wallet = this.wallets.get(address);
    if (!wallet) {
      return { error: 'Wallet not found' };
    }
    
    const balance = aiElonChain338.getBalance(address);
    const nisabThreshold = 1000; // Minimum threshold for Zakat
    
    if (balance >= nisabThreshold) {
      const zakatAmount = balance * 0.025; // 2.5% for Zakat
      wallet.zakatDue = zakatAmount;
      
      return {
        balance,
        zakatDue: zakatAmount,
        percentage: 2.5,
        eligible: true
      };
    }
    
    return {
      balance,
      zakatDue: 0,
      eligible: false,
      reason: 'Balance below Nisab threshold'
    };
  }

  /**
   * Pay Zakat
   * @param {string} fromAddress - Wallet address
   * @param {string} charityAddress - Charity recipient
   * @returns {Object} Payment result
   */
  payZakat(fromAddress, charityAddress) {
    const zakatInfo = this.calculateZakat(fromAddress);
    
    if (!zakatInfo.eligible) {
      return { success: false, error: 'No Zakat due' };
    }
    
    return this.sendTransaction(
      fromAddress,
      charityAddress,
      zakatInfo.zakatDue,
      'zakat_payment'
    );
  }

  /**
   * Get wallet balance
   * @param {string} address - Wallet address
   * @returns {Object} Balance information
   */
  getBalance(address) {
    const blockchainBalance = aiElonChain338.getBalance(address);
    const wallet = this.wallets.get(address);
    
    return {
      address,
      balance: blockchainBalance,
      zakatDue: wallet ? wallet.zakatDue : 0,
      complianceScore: wallet ? wallet.complianceScore : 0
    };
  }

  /**
   * Get wallet transaction history
   * @param {string} address - Wallet address
   * @returns {Array} Transaction history
   */
  getTransactionHistory(address) {
    return aiElonChain338.getTransactionHistory(address);
  }

  /**
   * Update Zakat calculation
   * @private
   */
  updateZakatCalculation(wallet) {
    const balance = aiElonChain338.getBalance(wallet.address);
    if (balance >= 1000) {
      wallet.zakatDue = balance * 0.025;
    }
  }

  /**
   * Generate wallet address
   * @private
   */
  generateWalletAddress() {
    const prefix = '0xH'; // H for Halal
    const random = Math.random().toString(36).substring(2, 15) +
                   Math.random().toString(36).substring(2, 15);
    return prefix + random.toUpperCase();
  }

  /**
   * Get wallet info
   * @param {string} address - Wallet address
   * @returns {Object} Wallet information
   */
  getWalletInfo(address) {
    const wallet = this.wallets.get(address);
    if (!wallet) {
      return { error: 'Wallet not found' };
    }
    
    const balance = aiElonChain338.getBalance(address);
    const zakatInfo = this.calculateZakat(address);
    
    return {
      ...wallet,
      currentBalance: balance,
      zakatInfo,
      transactionCount: wallet.transactions.length
    };
  }
}

export const halalWallet = new HalalWallet();
