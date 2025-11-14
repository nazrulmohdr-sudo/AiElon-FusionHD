/**
 * AiElonChain338 - Blockchain Integration Module
 * Provides seamless blockchain connectivity and transaction management
 */

import { globalState } from '../../core/StateManager.js';

export class AiElonChain338 {
  constructor() {
    this.chainId = 338;
    this.network = 'AiElonChain338';
    this.blocks = [];
    this.pendingTransactions = [];
    this.difficulty = 2;
    this.miningReward = 100;
    this.validators = new Set();
    
    // Initialize genesis block
    this.createGenesisBlock();
  }

  /**
   * Create the genesis block
   * @private
   */
  createGenesisBlock() {
    const genesis = {
      index: 0,
      timestamp: Date.now(),
      transactions: [],
      previousHash: '0',
      hash: this.calculateHash(0, Date.now(), [], '0', 0),
      nonce: 0
    };
    this.blocks.push(genesis);
  }

  /**
   * Calculate hash for a block
   * @private
   */
  calculateHash(index, timestamp, transactions, previousHash, nonce) {
    const data = `${index}${timestamp}${JSON.stringify(transactions)}${previousHash}${nonce}`;
    // Simple hash simulation
    let hash = 0;
    for (let i = 0; i < data.length; i++) {
      hash = ((hash << 5) - hash) + data.charCodeAt(i);
      hash = hash & hash;
    }
    return Math.abs(hash).toString(16);
  }

  /**
   * Get the latest block
   * @returns {Object} Latest block
   */
  getLatestBlock() {
    return this.blocks[this.blocks.length - 1];
  }

  /**
   * Add a new transaction
   * @param {Object} transaction - Transaction details
   */
  addTransaction(transaction) {
    if (!transaction.from || !transaction.to || !transaction.amount) {
      throw new Error('Transaction must include from, to, and amount');
    }
    
    const tx = {
      ...transaction,
      timestamp: Date.now(),
      id: this.generateTransactionId()
    };
    
    this.pendingTransactions.push(tx);
    globalState.set('pendingTransactions', this.pendingTransactions.length);
    
    return tx;
  }

  /**
   * Mine pending transactions
   * @param {string} minerAddress - Address of the miner
   */
  minePendingTransactions(minerAddress) {
    const block = {
      index: this.blocks.length,
      timestamp: Date.now(),
      transactions: this.pendingTransactions,
      previousHash: this.getLatestBlock().hash,
      nonce: 0
    };
    
    // Proof of work
    while (!this.isValidHash(block.hash)) {
      block.nonce++;
      block.hash = this.calculateHash(
        block.index,
        block.timestamp,
        block.transactions,
        block.previousHash,
        block.nonce
      );
    }
    
    this.blocks.push(block);
    
    // Reward miner
    this.pendingTransactions = [{
      from: 'system',
      to: minerAddress,
      amount: this.miningReward,
      timestamp: Date.now(),
      id: this.generateTransactionId()
    }];
    
    globalState.set('blockHeight', this.blocks.length);
    
    return block;
  }

  /**
   * Check if hash is valid
   * @private
   */
  isValidHash(hash) {
    if (!hash) return false;
    return hash.substring(0, this.difficulty) === '0'.repeat(this.difficulty);
  }

  /**
   * Validate the blockchain
   * @returns {boolean} Whether the chain is valid
   */
  isChainValid() {
    for (let i = 1; i < this.blocks.length; i++) {
      const currentBlock = this.blocks[i];
      const previousBlock = this.blocks[i - 1];
      
      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }
      
      const recalculatedHash = this.calculateHash(
        currentBlock.index,
        currentBlock.timestamp,
        currentBlock.transactions,
        currentBlock.previousHash,
        currentBlock.nonce
      );
      
      if (currentBlock.hash !== recalculatedHash) {
        return false;
      }
    }
    return true;
  }

  /**
   * Get balance for an address
   * @param {string} address - Wallet address
   * @returns {number} Balance
   */
  getBalance(address) {
    let balance = 0;
    
    for (const block of this.blocks) {
      for (const tx of block.transactions) {
        if (tx.from === address) {
          balance -= tx.amount;
        }
        if (tx.to === address) {
          balance += tx.amount;
        }
      }
    }
    
    return balance;
  }

  /**
   * Generate unique transaction ID
   * @private
   */
  generateTransactionId() {
    return `tx_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  /**
   * Add validator to network
   * @param {string} address - Validator address
   */
  addValidator(address) {
    this.validators.add(address);
    return { address, status: 'validator' };
  }

  /**
   * Get blockchain info
   * @returns {Object} Chain information
   */
  getChainInfo() {
    return {
      chainId: this.chainId,
      network: this.network,
      blockHeight: this.blocks.length,
      difficulty: this.difficulty,
      pendingTransactions: this.pendingTransactions.length,
      validators: this.validators.size,
      isValid: this.isChainValid()
    };
  }

  /**
   * Get transaction history for an address
   * @param {string} address - Wallet address
   * @returns {Array} Transaction history
   */
  getTransactionHistory(address) {
    const history = [];
    
    for (const block of this.blocks) {
      for (const tx of block.transactions) {
        if (tx.from === address || tx.to === address) {
          history.push({
            ...tx,
            blockIndex: block.index,
            blockHash: block.hash
          });
        }
      }
    }
    
    return history;
  }
}

export const aiElonChain338 = new AiElonChain338();
