#!/usr/bin/env python3
"""
AiElonChain338 - Blockchain Subsystem
Provides distributed ledger technology for secure transactions
"""

import hashlib
import json
import logging
from datetime import datetime
from typing import List, Dict, Any


class Block:
    """Blockchain block structure"""
    
    def __init__(self, index: int, timestamp: str, data: Dict[str, Any], 
                 previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate SHA-256 hash of the block"""
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert block to dictionary"""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }


class AiElonChain338:
    """
    AiElonChain338 - Blockchain implementation
    Secure, distributed ledger for AiElon ecosystem
    """
    
    def __init__(self):
        self.chain: List[Block] = []
        self.difficulty = 3  # Mining difficulty (338 reference)
        self.pending_transactions: List[Dict[str, Any]] = []
        self.logger = logging.getLogger('AiElonChain338')
        
        # Create genesis block
        self._create_genesis_block()
    
    def _create_genesis_block(self):
        """Create the first block in the chain"""
        genesis_block = Block(
            index=0,
            timestamp=datetime.now().isoformat(),
            data={'message': 'Genesis Block - AiElonChain338 Initialized'},
            previous_hash='0',
            nonce=0
        )
        self.chain.append(genesis_block)
        self.logger.info("Genesis block created")
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain"""
        return self.chain[-1]
    
    def add_transaction(self, transaction: Dict[str, Any]) -> bool:
        """Add a transaction to pending transactions"""
        try:
            transaction['timestamp'] = datetime.now().isoformat()
            self.pending_transactions.append(transaction)
            self.logger.info(f"Transaction added: {transaction}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to add transaction: {e}")
            return False
    
    def mine_pending_transactions(self, miner_address: str) -> bool:
        """Mine pending transactions into a new block"""
        try:
            if not self.pending_transactions:
                self.logger.warning("No pending transactions to mine")
                return False
            
            new_block = Block(
                index=len(self.chain),
                timestamp=datetime.now().isoformat(),
                data={
                    'transactions': self.pending_transactions,
                    'miner': miner_address
                },
                previous_hash=self.get_latest_block().hash
            )
            
            # Proof of work mining
            new_block = self._proof_of_work(new_block)
            
            self.chain.append(new_block)
            self.pending_transactions = []
            
            self.logger.info(f"Block {new_block.index} mined successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Mining failed: {e}")
            return False
    
    def _proof_of_work(self, block: Block) -> Block:
        """Perform proof-of-work mining"""
        target = '0' * self.difficulty
        
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        
        self.logger.info(f"Block mined with nonce: {block.nonce}")
        return block
    
    def is_chain_valid(self) -> bool:
        """Validate the entire blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block hash
            if current_block.hash != current_block.calculate_hash():
                self.logger.error(f"Block {i} hash is invalid")
                return False
            
            # Verify chain linkage
            if current_block.previous_hash != previous_block.hash:
                self.logger.error(f"Block {i} chain linkage is broken")
                return False
        
        return True
    
    def get_chain_info(self) -> Dict[str, Any]:
        """Get blockchain information"""
        return {
            'length': len(self.chain),
            'difficulty': self.difficulty,
            'pending_transactions': len(self.pending_transactions),
            'valid': self.is_chain_valid()
        }
    
    def initialize(self):
        """Initialize the blockchain subsystem"""
        self.logger.info("AiElonChain338 initialized")
        
    def health_check(self) -> Dict[str, Any]:
        """Perform health check on blockchain"""
        is_valid = self.is_chain_valid()
        return {
            'status': 'operational' if is_valid else 'error',
            'chain_length': len(self.chain),
            'chain_valid': is_valid,
            'pending_transactions': len(self.pending_transactions)
        }


if __name__ == "__main__":
    # Test the blockchain
    blockchain = AiElonChain338()
    blockchain.add_transaction({'from': 'Alice', 'to': 'Bob', 'amount': 100})
    blockchain.mine_pending_transactions('Miner1')
    print(f"Chain valid: {blockchain.is_chain_valid()}")
    print(f"Chain info: {blockchain.get_chain_info()}")
