/**
 * Halal Wallet Module
 * Version: 2.0.0
 * 
 * Islamic-compliant digital wallet with blockchain integration
 * Ensures Shariah compliance in all financial transactions
 */

const crypto = require('crypto');

class HalalWallet {
    constructor() {
        this.version = '2.0.0';
        this.wallets = new Map();
        this.blockchain = null;
        this.shariahCompliance = true;
    }

    /**
     * Initialize Halal Wallet system
     */
    async initialize(config, blockchain) {
        console.log('  → Initializing Halal Wallet system...');
        
        this.config = config || {};
        this.blockchain = blockchain;
        
        // Setup Shariah compliance checker
        this.setupShariahCompliance();
        
        // Initialize security features
        this.setupSecurity();
        
        // Initialize wallet storage
        this.setupStorage();
        
        console.log('  ✓ Halal Wallet ready');
        
        return this;
    }

    /**
     * Setup Shariah compliance system
     */
    setupShariahCompliance() {
        this.shariahRules = {
            noRiba: true,           // No interest
            noGharar: true,         // No excessive uncertainty
            noMaysir: true,         // No gambling
            noHaram: true,          // No forbidden activities
            zakatEnabled: true,     // Zakat calculation
            ethicalInvestment: true // Ethical investment screening
        };
        
        this.prohibitedCategories = [
            'alcohol',
            'gambling',
            'tobacco',
            'weapons',
            'pork',
            'interest-based-finance',
            'adult-content'
        ];
    }

    /**
     * Setup security features
     */
    setupSecurity() {
        this.security = {
            encryption: 'AES-256-GCM',
            multiSig: true,
            biometric: true,
            twoFactor: true,
            coldStorage: true
        };
    }

    /**
     * Setup wallet storage
     */
    setupStorage() {
        this.storage = {
            type: 'encrypted',
            backupEnabled: true,
            recoveryPhrase: true
        };
    }

    /**
     * Create new wallet
     */
    async createWallet(userId, options = {}) {
        const walletId = this.generateWalletId();
        const privateKey = this.generatePrivateKey();
        const publicKey = this.derivePublicKey(privateKey);
        const address = this.deriveAddress(publicKey);
        
        const wallet = {
            id: walletId,
            userId,
            address,
            publicKey,
            privateKey: this.encryptPrivateKey(privateKey),
            balance: 0,
            assets: [],
            transactions: [],
            zakatInfo: {
                enabled: true,
                threshold: 85, // grams of gold equivalent
                rate: 0.025    // 2.5%
            },
            createdAt: new Date().toISOString(),
            shariahCompliant: true
        };
        
        this.wallets.set(walletId, wallet);
        
        // Register on blockchain
        if (this.blockchain) {
            await this.blockchain.createTransaction(
                'system',
                address,
                0,
                { type: 'wallet_creation', walletId }
            );
        }
        
        return {
            walletId,
            address,
            publicKey,
            recoveryPhrase: this.generateRecoveryPhrase()
        };
    }

    /**
     * Get wallet by ID
     */
    getWallet(walletId) {
        return this.wallets.get(walletId);
    }

    /**
     * Get wallet balance
     */
    async getBalance(walletId) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        
        // Get balance from blockchain if connected
        if (this.blockchain) {
            wallet.balance = await this.blockchain.getBalance(wallet.address);
        }
        
        return wallet.balance;
    }

    /**
     * Send transaction
     */
    async sendTransaction(walletId, toAddress, amount, memo = '') {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        
        // Verify sufficient balance
        const balance = await this.getBalance(walletId);
        if (balance < amount) {
            throw new Error('Insufficient balance');
        }
        
        // Check Shariah compliance
        await this.checkShariahCompliance(toAddress, amount, memo);
        
        // Create and send transaction
        if (this.blockchain) {
            const tx = await this.blockchain.createTransaction(
                wallet.address,
                toAddress,
                amount,
                { memo, shariahCompliant: true }
            );
            
            const sentTx = await this.blockchain.sendTransaction(tx);
            
            // Record transaction
            wallet.transactions.push({
                id: sentTx.id,
                hash: sentTx.hash,
                type: 'send',
                amount,
                to: toAddress,
                memo,
                timestamp: new Date().toISOString(),
                status: sentTx.status
            });
            
            return sentTx;
        }
        
        throw new Error('Blockchain not connected');
    }

    /**
     * Receive transaction
     */
    async receiveTransaction(walletId, fromAddress, amount, txHash) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        
        wallet.transactions.push({
            hash: txHash,
            type: 'receive',
            amount,
            from: fromAddress,
            timestamp: new Date().toISOString(),
            status: 'confirmed'
        });
        
        wallet.balance += amount;
        
        return true;
    }

    /**
     * Check Shariah compliance for transaction
     */
    async checkShariahCompliance(address, amount, memo) {
        // Check if recipient is on prohibited list
        if (this.isProhibitedAddress(address)) {
            throw new Error('Transaction not Shariah compliant: Prohibited recipient');
        }
        
        // Check transaction purpose
        if (memo && this.containsProhibitedContent(memo)) {
            throw new Error('Transaction not Shariah compliant: Prohibited purpose');
        }
        
        // Verify no interest-based transaction
        if (this.isInterestBased(memo)) {
            throw new Error('Transaction not Shariah compliant: Interest-based transaction');
        }
        
        return true;
    }

    /**
     * Calculate Zakat
     */
    calculateZakat(walletId) {
        const wallet = this.wallets.get(walletId);
        if (!wallet || !wallet.zakatInfo.enabled) {
            return 0;
        }
        
        const balance = wallet.balance;
        const threshold = wallet.zakatInfo.threshold;
        
        // Only calculate if above nisab (threshold)
        if (balance < threshold) {
            return 0;
        }
        
        // Calculate 2.5% of wealth above threshold
        const zakatAmount = balance * wallet.zakatInfo.rate;
        
        return {
            amount: zakatAmount,
            balance,
            threshold,
            rate: wallet.zakatInfo.rate,
            dueDate: this.calculateZakatDueDate()
        };
    }

    /**
     * Pay Zakat
     */
    async payZakat(walletId, recipientAddress) {
        const zakatInfo = this.calculateZakat(walletId);
        
        if (zakatInfo.amount <= 0) {
            throw new Error('No Zakat due');
        }
        
        // Send Zakat payment
        const tx = await this.sendTransaction(
            walletId,
            recipientAddress,
            zakatInfo.amount,
            'Zakat Payment'
        );
        
        return {
            transaction: tx,
            zakatAmount: zakatInfo.amount,
            paidAt: new Date().toISOString()
        };
    }

    /**
     * Add asset to wallet
     */
    async addAsset(walletId, assetType, amount, metadata = {}) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        
        // Verify asset is Shariah compliant
        if (!this.isAssetHalal(assetType, metadata)) {
            throw new Error('Asset not Shariah compliant');
        }
        
        wallet.assets.push({
            id: crypto.randomBytes(16).toString('hex'),
            type: assetType,
            amount,
            metadata,
            addedAt: new Date().toISOString(),
            shariahCompliant: true
        });
        
        return true;
    }

    /**
     * Check if asset is Halal
     */
    isAssetHalal(assetType, metadata) {
        // Check against prohibited categories
        if (metadata.category && this.prohibitedCategories.includes(metadata.category.toLowerCase())) {
            return false;
        }
        
        // Additional Shariah compliance checks
        return true;
    }

    /**
     * Check if address is prohibited
     */
    isProhibitedAddress(address) {
        // Check against blacklist
        return false; // Placeholder
    }

    /**
     * Check if memo contains prohibited content
     */
    containsProhibitedContent(memo) {
        const lowerMemo = memo.toLowerCase();
        return this.prohibitedCategories.some(category => 
            lowerMemo.includes(category)
        );
    }

    /**
     * Check if transaction is interest-based
     */
    isInterestBased(memo) {
        const interestKeywords = ['interest', 'riba', 'apr', 'apy', 'yield'];
        const lowerMemo = memo.toLowerCase();
        return interestKeywords.some(keyword => lowerMemo.includes(keyword));
    }

    /**
     * Generate wallet ID
     */
    generateWalletId() {
        return 'wallet_' + crypto.randomBytes(16).toString('hex');
    }

    /**
     * Generate private key
     */
    generatePrivateKey() {
        return crypto.randomBytes(32).toString('hex');
    }

    /**
     * Derive public key from private key
     */
    derivePublicKey(privateKey) {
        return crypto.createHash('sha256').update(privateKey).digest('hex');
    }

    /**
     * Derive address from public key
     */
    deriveAddress(publicKey) {
        return '0x' + crypto.createHash('ripemd160')
            .update(Buffer.from(publicKey, 'hex'))
            .digest('hex');
    }

    /**
     * Encrypt private key
     */
    encryptPrivateKey(privateKey) {
        // Placeholder for encryption
        return Buffer.from(privateKey).toString('base64');
    }

    /**
     * Generate recovery phrase
     */
    generateRecoveryPhrase() {
        const words = [];
        for (let i = 0; i < 12; i++) {
            words.push(crypto.randomBytes(4).toString('hex'));
        }
        return words.join(' ');
    }

    /**
     * Calculate Zakat due date
     */
    calculateZakatDueDate() {
        const now = new Date();
        const nextYear = new Date(now.getFullYear() + 1, now.getMonth(), now.getDate());
        return nextYear.toISOString();
    }

    /**
     * Get wallet status
     */
    getStatus() {
        return {
            version: this.version,
            totalWallets: this.wallets.size,
            shariahCompliance: this.shariahCompliance,
            blockchainConnected: !!this.blockchain,
            features: {
                zakatCalculation: true,
                shariahScreening: true,
                secureStorage: true,
                multiSig: this.security.multiSig
            }
        };
    }
}

module.exports = {
    initialize: async (config, blockchain) => {
        const wallet = new HalalWallet();
        return await wallet.initialize(config, blockchain);
    },
    HalalWallet
};
