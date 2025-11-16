"""
AielonChain338 - Immutable Locking and Sealing System
Demi Masa Abadi (For Eternal Time) Implementation
"""

import hashlib
import json
import time
from typing import Any, Dict, List, Optional
from datetime import datetime


class AielonChain338:
    """
    AielonChain338 Immutable Locking and Sealing System
    
    Implements:
    - Immutable locking mechanisms
    - Reinforcement protocols aligned with Demi Masa Abadi
    - Chain integrity validation
    - Eternal timestamp sealing
    """
    
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.sealed_blocks: Dict[str, Dict[str, Any]] = {}
        self.lock_state = {
            'is_locked': False,
            'is_sealed': False,
            'lock_timestamp': None,
            'seal_timestamp': None,
            'eternal_signature': None
        }
        self.reinforcement_level = 338  # AielonChain338 base level
        
        # Initialize genesis block
        self._create_genesis_block()
    
    def _create_genesis_block(self) -> None:
        """Create the genesis block for AielonChain338"""
        genesis_block = {
            'index': 0,
            'timestamp': datetime.now().isoformat(),
            'data': {
                'type': 'genesis',
                'message': 'AielonChain338 - Demi Masa Abadi',
                'supreme_command': 'Initialize Supreme GodMode Mutlak'
            },
            'previous_hash': '0' * 64,
            'hash': self._calculate_hash(0, datetime.now().isoformat(), 
                                        {'type': 'genesis'}, '0' * 64)
        }
        self.chain.append(genesis_block)
    
    def _calculate_hash(self, index: int, timestamp: str, 
                        data: Dict[str, Any], previous_hash: str) -> str:
        """
        Calculate SHA-256 hash for a block
        
        Args:
            index: Block index
            timestamp: Block timestamp
            data: Block data
            previous_hash: Previous block hash
            
        Returns:
            Hexadecimal hash string
        """
        block_string = json.dumps({
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'previous_hash': previous_hash,
            'reinforcement': self.reinforcement_level
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def add_block(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a new block to the chain
        
        Args:
            data: Data to be stored in the block
            
        Returns:
            The created block
        """
        if self.lock_state['is_locked']:
            raise RuntimeError("Chain is locked. Cannot add new blocks.")
        
        previous_block = self.chain[-1]
        new_index = previous_block['index'] + 1
        new_timestamp = datetime.now().isoformat()
        new_hash = self._calculate_hash(
            new_index, new_timestamp, data, previous_block['hash']
        )
        
        new_block = {
            'index': new_index,
            'timestamp': new_timestamp,
            'data': data,
            'previous_hash': previous_block['hash'],
            'hash': new_hash
        }
        
        self.chain.append(new_block)
        return new_block
    
    def apply_immutable_lock(self) -> bool:
        """
        Apply immutable locking to AielonChain338
        
        This prevents any further modifications to the chain structure.
        
        Returns:
            True if lock is successfully applied
        """
        if self.lock_state['is_locked']:
            print("Chain is already locked.")
            return False
        
        self.lock_state['is_locked'] = True
        self.lock_state['lock_timestamp'] = datetime.now().isoformat()
        
        # Add lock block
        lock_block_data = {
            'type': 'lock',
            'message': 'Immutable Lock Applied',
            'reinforcement_level': self.reinforcement_level,
            'timestamp': self.lock_state['lock_timestamp']
        }
        
        # Create lock block without using add_block (since chain is now locked)
        previous_block = self.chain[-1]
        lock_block = {
            'index': previous_block['index'] + 1,
            'timestamp': self.lock_state['lock_timestamp'],
            'data': lock_block_data,
            'previous_hash': previous_block['hash'],
            'hash': self._calculate_hash(
                previous_block['index'] + 1,
                self.lock_state['lock_timestamp'],
                lock_block_data,
                previous_block['hash']
            )
        }
        
        # Temporarily unlock to add the lock block
        self.lock_state['is_locked'] = False
        self.chain.append(lock_block)
        self.lock_state['is_locked'] = True
        
        return True
    
    def apply_eternal_seal(self) -> str:
        """
        Apply eternal seal to AielonChain338 (Demi Masa Abadi)
        
        This creates an eternal signature that validates the entire chain
        for all time.
        
        Returns:
            Eternal seal signature
        """
        if not self.lock_state['is_locked']:
            raise RuntimeError("Chain must be locked before sealing.")
        
        if self.lock_state['is_sealed']:
            return self.lock_state['eternal_signature']
        
        # Create eternal signature
        chain_string = json.dumps(self.chain, sort_keys=True)
        eternal_hash = hashlib.sha512(chain_string.encode()).hexdigest()
        
        # Apply reinforcement iterations
        for i in range(self.reinforcement_level):
            eternal_hash = hashlib.sha512(
                (eternal_hash + str(i)).encode()
            ).hexdigest()
        
        self.lock_state['is_sealed'] = True
        self.lock_state['seal_timestamp'] = datetime.now().isoformat()
        self.lock_state['eternal_signature'] = eternal_hash
        
        # Store sealed state
        self.sealed_blocks['eternal_seal'] = {
            'signature': eternal_hash,
            'timestamp': self.lock_state['seal_timestamp'],
            'chain_length': len(self.chain),
            'reinforcement': self.reinforcement_level,
            'demi_masa_abadi': True
        }
        
        return eternal_hash
    
    def validate_chain_integrity(self) -> bool:
        """
        Validate the integrity of the entire chain
        
        Returns:
            True if chain integrity is valid
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Validate previous hash link
            if current_block['previous_hash'] != previous_block['hash']:
                print(f"Chain broken at block {i}: previous_hash mismatch")
                return False
            
            # Validate current block hash
            calculated_hash = self._calculate_hash(
                current_block['index'],
                current_block['timestamp'],
                current_block['data'],
                current_block['previous_hash']
            )
            
            if current_block['hash'] != calculated_hash:
                print(f"Chain broken at block {i}: hash mismatch")
                return False
        
        return True
    
    def get_chain_status(self) -> Dict[str, Any]:
        """
        Get comprehensive chain status
        
        Returns:
            Dictionary containing chain status and lock state
        """
        return {
            'chain_length': len(self.chain),
            'is_locked': self.lock_state['is_locked'],
            'is_sealed': self.lock_state['is_sealed'],
            'lock_timestamp': self.lock_state['lock_timestamp'],
            'seal_timestamp': self.lock_state['seal_timestamp'],
            'eternal_signature': self.lock_state['eternal_signature'],
            'reinforcement_level': self.reinforcement_level,
            'integrity_valid': self.validate_chain_integrity(),
            'demi_masa_abadi': self.lock_state['is_sealed']
        }
    
    def display_chain(self) -> None:
        """Display the entire chain"""
        print("\n" + "=" * 60)
        print("AielonChain338 - Chain Display")
        print("=" * 60)
        
        for block in self.chain:
            print(f"\nBlock {block['index']}:")
            print(f"  Timestamp: {block['timestamp']}")
            print(f"  Data: {block['data']}")
            print(f"  Previous Hash: {block['previous_hash'][:16]}...")
            print(f"  Hash: {block['hash'][:16]}...")


def main():
    """Main execution function for testing"""
    print("=" * 60)
    print("AielonChain338 - Initialization")
    print("=" * 60)
    
    # Initialize AielonChain338
    chain = AielonChain338()
    
    # Add some blocks
    chain.add_block({
        'type': 'supreme_command',
        'action': 'Initialize GodMode',
        'status': 'active'
    })
    
    chain.add_block({
        'type': 'constraint_resolution',
        'constraints': ['100% = 1', '0% = 0', 'all = ∞'],
        'status': 'resolved'
    })
    
    # Display chain before locking
    print("\nChain Status (Before Lock):")
    status = chain.get_chain_status()
    print(f"  Chain Length: {status['chain_length']}")
    print(f"  Locked: {status['is_locked']}")
    print(f"  Sealed: {status['is_sealed']}")
    print(f"  Integrity: {status['integrity_valid']} ✓")
    
    # Apply immutable lock
    print("\n--- Applying Immutable Lock ---")
    chain.apply_immutable_lock()
    
    # Apply eternal seal
    print("--- Applying Eternal Seal (Demi Masa Abadi) ---")
    eternal_sig = chain.apply_eternal_seal()
    
    # Display final status
    print("\nChain Status (After Lock & Seal):")
    status = chain.get_chain_status()
    print(f"  Chain Length: {status['chain_length']}")
    print(f"  Locked: {status['is_locked']} ✓")
    print(f"  Sealed: {status['is_sealed']} ✓")
    print(f"  Reinforcement Level: {status['reinforcement_level']}")
    print(f"  Eternal Signature: {eternal_sig[:32]}...")
    print(f"  Integrity: {status['integrity_valid']} ✓")
    print(f"  Demi Masa Abadi: {status['demi_masa_abadi']} ✓")
    
    print("\n" + "=" * 60)
    print("AielonChain338 - Locked & Sealed for Eternity")
    print("=" * 60)


if __name__ == "__main__":
    main()
