"""
AielonChain338 Security Module

This module implements the AielonChain338 locking and security mechanism with:
- Immutable locking system (Demi Masa Abadi - For Eternal Time)
- Cryptographic sealing
- Chain integrity validation
"""

import hashlib
import time
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ChainBlock:
    """Represents a single block in the AielonChain338"""
    index: int
    timestamp: float
    data: Dict[str, Any]
    previous_hash: str
    hash: str = field(default="")
    locked: bool = field(default=False)
    seal: Optional[str] = field(default=None)
    
    def calculate_hash(self) -> str:
        """
        Calculate hash for this block
        
        Returns:
            SHA-256 hash of block contents
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert block to dictionary representation"""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'locked': self.locked,
            'seal': self.seal
        }


class AielonChain338:
    """
    AielonChain338 - Immutable security and locking system
    
    Implements:
    - Demi Masa Abadi (For Eternal Time) immutability principle
    - Secure locking and sealing mechanisms
    - Chain integrity validation
    """
    
    # Chain identifier
    CHAIN_ID = "AielonChain338"
    CHAIN_VERSION = "1.0.0"
    
    def __init__(self):
        """Initialize AielonChain338"""
        self.chain: List[ChainBlock] = []
        self.locked_blocks: set = set()
        self.master_lock = False
        self.master_seal = None
        
        # Create genesis block
        self._create_genesis_block()
    
    def _create_genesis_block(self) -> ChainBlock:
        """
        Create the genesis (first) block
        
        Returns:
            Genesis block
        """
        genesis_block = ChainBlock(
            index=0,
            timestamp=time.time(),
            data={'message': 'AielonChain338 Genesis Block - Demi Masa Abadi'},
            previous_hash='0'
        )
        genesis_block.hash = genesis_block.calculate_hash()
        genesis_block.locked = True  # Genesis block is always locked
        genesis_block.seal = self._generate_seal(genesis_block)
        self.chain.append(genesis_block)
        self.locked_blocks.add(0)
        return genesis_block
    
    def _generate_seal(self, block: ChainBlock) -> str:
        """
        Generate cryptographic seal for a block
        
        Args:
            block: Block to seal
            
        Returns:
            Seal string
        """
        seal_string = f"SEAL:{block.hash}:{block.timestamp}:DEMI_MASA_ABADI"
        return hashlib.sha512(seal_string.encode()).hexdigest()
    
    def add_block(self, data: Dict[str, Any]) -> ChainBlock:
        """
        Add a new block to the chain
        
        Args:
            data: Data to store in the block
            
        Returns:
            Created block
        """
        if self.master_lock:
            raise RuntimeError("Chain is master locked - cannot add new blocks")
        
        previous_block = self.chain[-1]
        new_block = ChainBlock(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        new_block.hash = new_block.calculate_hash()
        
        self.chain.append(new_block)
        return new_block
    
    def lock_block(self, index: int) -> bool:
        """
        Lock a specific block (Demi Masa Abadi immutability)
        
        Args:
            index: Index of block to lock
            
        Returns:
            True if successfully locked
        """
        if index < 0 or index >= len(self.chain):
            raise ValueError(f"Block index {index} out of range")
        
        if index in self.locked_blocks:
            return True  # Already locked
        
        block = self.chain[index]
        block.locked = True
        block.seal = self._generate_seal(block)
        self.locked_blocks.add(index)
        
        return True
    
    def lock_all_blocks(self) -> int:
        """
        Lock all blocks in the chain
        
        Returns:
            Number of blocks locked
        """
        locked_count = 0
        for i in range(len(self.chain)):
            if i not in self.locked_blocks:
                self.lock_block(i)
                locked_count += 1
        return locked_count
    
    def apply_master_lock(self) -> bool:
        """
        Apply master lock to entire chain (Demi Masa Abadi)
        
        This prevents any new blocks from being added and locks all existing blocks.
        
        Returns:
            True if master lock applied successfully
        """
        if self.master_lock:
            return True  # Already locked
        
        # Lock all existing blocks
        self.lock_all_blocks()
        
        # Apply master lock
        self.master_lock = True
        
        # Generate master seal
        chain_string = ''.join([block.hash for block in self.chain])
        seal_string = f"MASTER_SEAL:{chain_string}:DEMI_MASA_ABADI"
        self.master_seal = hashlib.sha512(seal_string.encode()).hexdigest()
        
        return True
    
    def verify_block_integrity(self, index: int) -> bool:
        """
        Verify integrity of a specific block
        
        Args:
            index: Index of block to verify
            
        Returns:
            True if block integrity is valid
        """
        if index < 0 or index >= len(self.chain):
            return False
        
        block = self.chain[index]
        
        # Verify hash
        calculated_hash = block.calculate_hash()
        if calculated_hash != block.hash:
            return False
        
        # Verify chain linkage (except genesis block)
        if index > 0:
            previous_block = self.chain[index - 1]
            if block.previous_hash != previous_block.hash:
                return False
        
        # Verify seal if locked
        if block.locked:
            expected_seal = self._generate_seal(block)
            if block.seal != expected_seal:
                return False
        
        return True
    
    def verify_chain_integrity(self) -> Dict[str, Any]:
        """
        Verify integrity of entire chain
        
        Returns:
            Dictionary with verification results
        """
        results = {
            'valid': True,
            'total_blocks': len(self.chain),
            'locked_blocks': len(self.locked_blocks),
            'invalid_blocks': [],
            'master_locked': self.master_lock
        }
        
        for i in range(len(self.chain)):
            if not self.verify_block_integrity(i):
                results['valid'] = False
                results['invalid_blocks'].append(i)
        
        return results
    
    def get_block(self, index: int) -> Optional[Dict[str, Any]]:
        """
        Get block by index
        
        Args:
            index: Block index
            
        Returns:
            Block data or None if not found
        """
        if index < 0 or index >= len(self.chain):
            return None
        return self.chain[index].to_dict()
    
    def get_chain_status(self) -> Dict[str, Any]:
        """
        Get comprehensive chain status
        
        Returns:
            Dictionary with chain information
        """
        return {
            'chain_id': self.CHAIN_ID,
            'version': self.CHAIN_VERSION,
            'total_blocks': len(self.chain),
            'locked_blocks': len(self.locked_blocks),
            'master_locked': self.master_lock,
            'master_seal': self.master_seal,
            'integrity': self.verify_chain_integrity(),
            'principle': 'Demi Masa Abadi (For Eternal Time)'
        }
    
    def get_full_chain(self) -> List[Dict[str, Any]]:
        """
        Get complete chain data
        
        Returns:
            List of all blocks
        """
        return [block.to_dict() for block in self.chain]


# Singleton instance
_chain_instance = None


def get_chain_instance() -> AielonChain338:
    """Get or create singleton instance of AielonChain338"""
    global _chain_instance
    if _chain_instance is None:
        _chain_instance = AielonChain338()
    return _chain_instance
