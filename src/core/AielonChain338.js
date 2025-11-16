/**
 * AielonChain338 - Lock and Seal Mechanism
 * Implements permanent integrity and security (Demi Masa Abadi)
 */

const crypto = require('crypto');

class AielonChain338 {
    constructor() {
        this.chain = [];
        this.isLocked = false;
        this.isSealed = false;
        this.sealTimestamp = null;
        this.sealHash = null;
        this.operationalFramework = 'Demi Masa Abadi'; // For eternal time
    }

    /**
     * Create genesis block
     */
    createGenesisBlock() {
        const genesisBlock = {
            index: 0,
            timestamp: Date.now(),
            data: {
                type: 'GENESIS',
                message: 'AielonChain338 Genesis Block',
                framework: this.operationalFramework
            },
            previousHash: '0',
            hash: this.calculateHash(0, Date.now(), 'GENESIS', '0')
        };
        
        this.chain.push(genesisBlock);
        return genesisBlock;
    }

    /**
     * Calculate block hash
     */
    calculateHash(index, timestamp, data, previousHash) {
        const blockData = `${index}${timestamp}${JSON.stringify(data)}${previousHash}`;
        return crypto.createHash('sha256').update(blockData).digest('hex');
    }

    /**
     * Add block to chain
     */
    addBlock(data) {
        if (this.isLocked) {
            throw new Error('Chain is locked. Cannot add new blocks.');
        }

        const previousBlock = this.chain[this.chain.length - 1];
        const newBlock = {
            index: this.chain.length,
            timestamp: Date.now(),
            data: data,
            previousHash: previousBlock.hash,
            hash: null
        };

        newBlock.hash = this.calculateHash(
            newBlock.index,
            newBlock.timestamp,
            newBlock.data,
            newBlock.previousHash
        );

        this.chain.push(newBlock);
        return newBlock;
    }

    /**
     * Lock the chain
     * First step of Lock and Seal mechanism
     */
    lock() {
        if (this.isLocked) {
            return { success: false, message: 'Chain is already locked' };
        }

        this.isLocked = true;
        
        // Add lock block
        const lockBlock = this.addBlockWithoutValidation({
            type: 'LOCK',
            message: 'AielonChain338 Locked',
            timestamp: Date.now(),
            framework: this.operationalFramework
        });

        return {
            success: true,
            message: 'AielonChain338 locked successfully',
            block: lockBlock,
            timestamp: lockBlock.timestamp
        };
    }

    /**
     * Seal the chain
     * Final step of Lock and Seal mechanism - ensures permanent integrity
     */
    seal() {
        if (!this.isLocked) {
            return { success: false, message: 'Chain must be locked before sealing' };
        }

        if (this.isSealed) {
            return { success: false, message: 'Chain is already sealed' };
        }

        // Add seal block first (using special method since chain is locked)
        this.sealTimestamp = Date.now();
        const sealBlock = this.addBlockWithoutValidation({
            type: 'SEAL',
            message: 'AielonChain338 Sealed - Demi Masa Abadi',
            timestamp: this.sealTimestamp,
            framework: this.operationalFramework,
            permanentIntegrity: true
        });

        // Generate seal hash from entire chain including seal block
        const chainData = JSON.stringify(this.chain);
        this.sealHash = crypto.createHash('sha256').update(chainData).digest('hex');
        this.isSealed = true;

        return {
            success: true,
            message: 'AielonChain338 sealed permanently (Demi Masa Abadi)',
            sealHash: this.sealHash,
            sealTimestamp: this.sealTimestamp,
            block: sealBlock,
            totalBlocks: this.chain.length
        };
    }

    /**
     * Internal method to add block without lock validation
     */
    addBlockWithoutValidation(data) {
        const previousBlock = this.chain[this.chain.length - 1];
        const newBlock = {
            index: this.chain.length,
            timestamp: Date.now(),
            data: data,
            previousHash: previousBlock.hash,
            hash: null
        };

        newBlock.hash = this.calculateHash(
            newBlock.index,
            newBlock.timestamp,
            newBlock.data,
            newBlock.previousHash
        );

        this.chain.push(newBlock);
        return newBlock;
    }

    /**
     * Validate chain integrity
     */
    validateIntegrity() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            // Verify hash
            const calculatedHash = this.calculateHash(
                currentBlock.index,
                currentBlock.timestamp,
                currentBlock.data,
                currentBlock.previousHash
            );

            if (currentBlock.hash !== calculatedHash) {
                return {
                    valid: false,
                    error: `Block ${i} has invalid hash`
                };
            }

            // Verify chain link
            if (currentBlock.previousHash !== previousBlock.hash) {
                return {
                    valid: false,
                    error: `Block ${i} has invalid previous hash`
                };
            }
        }

        // Verify seal if sealed
        if (this.isSealed) {
            const currentChainHash = crypto.createHash('sha256')
                .update(JSON.stringify(this.chain))
                .digest('hex');
            
            if (currentChainHash !== this.sealHash) {
                return {
                    valid: false,
                    error: 'Seal has been compromised'
                };
            }
        }

        return {
            valid: true,
            message: 'Chain integrity verified',
            isLocked: this.isLocked,
            isSealed: this.isSealed,
            blocks: this.chain.length
        };
    }

    /**
     * Get chain status
     */
    getStatus() {
        return {
            isLocked: this.isLocked,
            isSealed: this.isSealed,
            sealTimestamp: this.sealTimestamp,
            sealHash: this.sealHash,
            blockCount: this.chain.length,
            framework: this.operationalFramework,
            integrity: this.validateIntegrity()
        };
    }

    /**
     * Get full chain
     */
    getChain() {
        return this.chain;
    }
}

module.exports = AielonChain338;
