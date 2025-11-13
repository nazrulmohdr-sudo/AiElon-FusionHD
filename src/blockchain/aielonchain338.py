"""
AiElon Living OS - AielonChain338 Blockchain Module

This module provides optimized blockchain capabilities for AielonChain338:
- Block creation and validation
- Transaction processing with enhanced security
- Consensus mechanism
- Smart contract support
"""

import hashlib
import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime


class Block:
    """Individual block in the AielonChain338"""
    
    def __init__(self, index: int, transactions: List[Dict[str, Any]], 
                 previous_hash: str, timestamp: float = None):
        """
        Initialize a new block
        
        Args:
            index: Block index in the chain
            transactions: List of transactions
            previous_hash: Hash of the previous block
            timestamp: Block creation timestamp
        """
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the hash of the block"""
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block with proof of work
        
        Args:
            difficulty: Mining difficulty level
        """
        target = "0" * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert block to dictionary"""
        return {
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash
        }


class Transaction:
    """Transaction in AielonChain338"""
    
    def __init__(self, sender: str, recipient: str, amount: float, 
                 transaction_type: str = "transfer", metadata: Dict[str, Any] = None):
        """
        Initialize a transaction
        
        Args:
            sender: Transaction sender address
            recipient: Transaction recipient address
            amount: Transaction amount
            transaction_type: Type of transaction
            metadata: Additional metadata
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_type = transaction_type
        self.metadata = metadata or {}
        self.timestamp = time.time()
        self.transaction_id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate unique transaction ID"""
        transaction_string = json.dumps({
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }, sort_keys=True)
        
        return hashlib.sha256(transaction_string.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary"""
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "metadata": self.metadata,
            "timestamp": self.timestamp
        }
    
    def is_valid(self) -> bool:
        """Validate transaction"""
        if self.amount <= 0:
            return False
        if not self.sender or not self.recipient:
            return False
        return True


class AielonChain338:
    """
    AielonChain338 Blockchain Implementation
    Optimized for high-performance transaction processing with enhanced security
    """
    
    def __init__(self, difficulty: int = 4):
        """
        Initialize AielonChain338
        
        Args:
            difficulty: Mining difficulty level
        """
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = difficulty
        self.mining_reward = 10.0
        self.network_stats = {
            "total_transactions": 0,
            "total_blocks": 0,
            "total_mining_time": 0
        }
        
        # Create genesis block
        self._create_genesis_block()
    
    def initialize(self) -> None:
        """Initialize the blockchain"""
        if not self.chain:
            self._create_genesis_block()
    
    def _create_genesis_block(self) -> None:
        """Create the first block in the chain"""
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
        self.network_stats["total_blocks"] = 1
    
    def get_latest_block(self) -> Block:
        """Get the latest block in the chain"""
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """
        Add a transaction to pending transactions
        
        Args:
            transaction: Transaction to add
            
        Returns:
            bool: True if transaction added successfully
        """
        if not transaction.is_valid():
            return False
        
        self.pending_transactions.append(transaction)
        return True
    
    def create_transaction(self, sender: str, recipient: str, amount: float,
                          transaction_type: str = "transfer", 
                          metadata: Dict[str, Any] = None) -> Optional[str]:
        """
        Create and add a new transaction
        
        Args:
            sender: Sender address
            recipient: Recipient address
            amount: Transaction amount
            transaction_type: Type of transaction
            metadata: Additional metadata
            
        Returns:
            str: Transaction ID if successful, None otherwise
        """
        transaction = Transaction(sender, recipient, amount, transaction_type, metadata)
        
        if self.add_transaction(transaction):
            self.network_stats["total_transactions"] += 1
            return transaction.transaction_id
        
        return None
    
    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Mine pending transactions into a new block
        
        Args:
            miner_address: Address to receive mining reward
            
        Returns:
            Block: The newly mined block
        """
        start_time = time.time()
        
        # Create reward transaction
        reward_transaction = Transaction(
            "SYSTEM",
            miner_address,
            self.mining_reward,
            "mining_reward"
        )
        
        # Add pending transactions to block
        transactions = [tx.to_dict() for tx in self.pending_transactions]
        transactions.append(reward_transaction.to_dict())
        
        # Create and mine new block
        new_block = Block(
            len(self.chain),
            transactions,
            self.get_latest_block().hash
        )
        new_block.mine_block(self.difficulty)
        
        # Add block to chain
        self.chain.append(new_block)
        self.pending_transactions = []
        
        # Update statistics
        mining_time = time.time() - start_time
        self.network_stats["total_blocks"] += 1
        self.network_stats["total_mining_time"] += mining_time
        
        return new_block
    
    def is_chain_valid(self) -> bool:
        """
        Validate the entire blockchain
        
        Returns:
            bool: True if chain is valid
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Verify link to previous block
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify proof of work
            if not current_block.hash.startswith("0" * self.difficulty):
                return False
        
        return True
    
    def get_balance(self, address: str) -> float:
        """
        Get balance for an address
        
        Args:
            address: Address to check
            
        Returns:
            float: Address balance
        """
        balance = 0.0
        
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.get("sender") == address:
                    balance -= transaction.get("amount", 0)
                if transaction.get("recipient") == address:
                    balance += transaction.get("amount", 0)
        
        return balance
    
    def get_transaction_history(self, address: str) -> List[Dict[str, Any]]:
        """
        Get transaction history for an address
        
        Args:
            address: Address to check
            
        Returns:
            list: List of transactions
        """
        history = []
        
        for block in self.chain:
            for transaction in block.transactions:
                if (transaction.get("sender") == address or 
                    transaction.get("recipient") == address):
                    history.append({
                        "block_index": block.index,
                        "transaction": transaction,
                        "block_hash": block.hash
                    })
        
        return history
    
    def get_chain_info(self) -> Dict[str, Any]:
        """Get blockchain information"""
        return {
            "chain_length": len(self.chain),
            "difficulty": self.difficulty,
            "pending_transactions": len(self.pending_transactions),
            "is_valid": self.is_chain_valid(),
            "statistics": self.network_stats,
            "average_mining_time": (
                self.network_stats["total_mining_time"] / 
                max(self.network_stats["total_blocks"] - 1, 1)
            )
        }
    
    def export_chain(self) -> List[Dict[str, Any]]:
        """Export entire blockchain"""
        return [block.to_dict() for block in self.chain]
    
    def health_check(self) -> bool:
        """Check blockchain health"""
        return self.is_chain_valid() and len(self.chain) > 0
    
    def shutdown(self) -> None:
        """Shutdown blockchain operations"""
        # Could save chain state to persistent storage
        pass
