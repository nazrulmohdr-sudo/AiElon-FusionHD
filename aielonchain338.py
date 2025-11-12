"""
AielonChain338 Security Module
Implements eternal and immutable security following the "Demi Masa Abadi" protocol.
"""

import hashlib
import time
from typing import List, Dict, Any, Optional
from datetime import datetime
import json


class DemiMasaAbadiProtocol:
    """
    Eternal Security Protocol - "Demi Masa Abadi"
    Ensures perpetual and immutable protection.
    """
    
    def __init__(self):
        self.protocol_name = "Demi Masa Abadi"
        self.eternal_status = True
        self.immutable = True
        self.inception_time = datetime.now().isoformat()
        
    def __repr__(self):
        return f"DemiMasaAbadiProtocol(eternal={self.eternal_status}, immutable={self.immutable})"
    
    def verify_eternality(self) -> bool:
        """Verify eternal status of the protocol."""
        return self.eternal_status and self.immutable
    
    def get_protocol_seal(self) -> str:
        """Generate unique protocol seal for verification."""
        seal_data = f"{self.protocol_name}:{self.inception_time}:ETERNAL:IMMUTABLE"
        return hashlib.sha256(seal_data.encode()).hexdigest()


class ChainBlock:
    """
    Represents a single block in AielonChain338.
    Each block is cryptographically secured and linked.
    """
    
    def __init__(self, index: int, data: Any, previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        
    def calculate_hash(self) -> str:
        """Calculate cryptographic hash for the block."""
        # Serialize data consistently
        try:
            # Try to JSON serialize if possible
            data_str = json.dumps(self.data, sort_keys=True, default=str)
        except (TypeError, ValueError):
            # Fall back to string representation
            data_str = str(self.data)
            
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': data_str,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int = 4):
        """Mine block with proof of work."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
    
    def to_dict(self) -> dict:
        """Convert block to dictionary representation."""
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }


class AielonChain338:
    """
    Supreme Blockchain Security System.
    Implements fully locked and sealed chain with eternal security.
    """
    
    def __init__(self):
        self.chain: List[ChainBlock] = []
        self.protocol = DemiMasaAbadiProtocol()
        self.locked = False
        self.sealed = False
        self.difficulty = 4
        
        # Create genesis block
        self._create_genesis_block()
        
    def _create_genesis_block(self):
        """Create the first block in the chain."""
        genesis_data = {
            'type': 'GENESIS',
            'protocol': self.protocol.protocol_name,
            'message': 'AielonChain338 Initialized - Supreme Security Enabled'
        }
        genesis_block = ChainBlock(0, genesis_data, "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> ChainBlock:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_block(self, data: Any) -> Optional[ChainBlock]:
        """
        Add a new block to the chain.
        Returns None if chain is locked.
        """
        if self.locked:
            return None
        
        # Deep copy data to prevent external mutations from affecting the block
        import copy
        data_copy = copy.deepcopy(data)
        
        previous_block = self.get_latest_block()
        new_block = ChainBlock(
            index=len(self.chain),
            data=data_copy,
            previous_hash=previous_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block
    
    def validate_chain(self) -> bool:
        """
        Validate the entire blockchain integrity.
        Checks hash linkage and block validity.
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
            
        return True
    
    def lock_chain(self) -> dict:
        """
        Lock the chain to prevent new blocks.
        Part of the sealing process.
        """
        if self.locked:
            return {
                'status': 'ALREADY_LOCKED',
                'locked': True,
                'message': 'Chain was already locked'
            }
        
        # Add locking block BEFORE setting locked flag
        lock_data = {
            'type': 'LOCK',
            'timestamp': datetime.now().isoformat(),
            'protocol': self.protocol.protocol_name,
            'message': 'AielonChain338 Locked - No more blocks can be added'
        }
        
        # This is the last block that can be added
        final_block = ChainBlock(
            index=len(self.chain),
            data=lock_data,
            previous_hash=self.get_latest_block().hash
        )
        final_block.mine_block(self.difficulty)
        self.chain.append(final_block)
        
        # NOW set the locked flag
        self.locked = True
        
        return {
            'status': 'LOCKED',
            'locked': True,
            'final_block_index': final_block.index,
            'final_block_hash': final_block.hash
        }
    
    def seal_chain(self) -> dict:
        """
        Seal the chain with Demi Masa Abadi protocol.
        Makes chain eternally immutable.
        """
        if not self.locked:
            return {
                'status': 'FAILED',
                'message': 'Chain must be locked before sealing',
                'sealed': False
            }
        
        if self.sealed:
            return {
                'status': 'ALREADY_SEALED',
                'sealed': True,
                'message': 'Chain was already sealed'
            }
        
        # Validate before sealing
        if not self.validate_chain():
            return {
                'status': 'FAILED',
                'message': 'Chain validation failed - cannot seal',
                'sealed': False
            }
        
        self.sealed = True
        
        seal_result = {
            'status': 'SEALED',
            'sealed': True,
            'protocol': self.protocol.protocol_name,
            'protocol_seal': self.protocol.get_protocol_seal(),
            'eternal_security': self.protocol.verify_eternality(),
            'chain_length': len(self.chain),
            'chain_valid': True,
            'immutable': True,
            'sealed_timestamp': datetime.now().isoformat(),
            'message': 'AielonChain338 fully locked and sealed - Eternal Security Active'
        }
        
        return seal_result
    
    def get_chain_status(self) -> dict:
        """Get comprehensive chain status."""
        return {
            'chain_length': len(self.chain),
            'locked': self.locked,
            'sealed': self.sealed,
            'valid': self.validate_chain(),
            'protocol': self.protocol.protocol_name,
            'eternal_security': self.protocol.verify_eternality(),
            'genesis_hash': self.chain[0].hash if self.chain else None,
            'latest_hash': self.get_latest_block().hash if self.chain else None
        }
    
    def get_full_chain(self) -> List[dict]:
        """Get complete chain as list of dictionaries."""
        return [block.to_dict() for block in self.chain]
    
    def export_sealed_chain(self) -> dict:
        """
        Export the sealed chain with all security metadata.
        Only works if chain is sealed.
        """
        if not self.sealed:
            return {
                'status': 'ERROR',
                'message': 'Chain must be sealed before export'
            }
        
        return {
            'chain_id': 'AielonChain338',
            'protocol': self.protocol.protocol_name,
            'protocol_seal': self.protocol.get_protocol_seal(),
            'sealed': True,
            'locked': True,
            'eternal': True,
            'immutable': True,
            'chain_length': len(self.chain),
            'blocks': self.get_full_chain(),
            'validation_status': self.validate_chain(),
            'export_timestamp': datetime.now().isoformat()
        }


# Module-level instance
supreme_chain = AielonChain338()
