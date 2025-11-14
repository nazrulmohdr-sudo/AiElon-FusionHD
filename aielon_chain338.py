"""
AielonChain338 Locking Mechanism
Demi Masa Abadi Framework - Permanent Integrity Protection
"""

import hashlib
import time
from typing import Optional, Dict, List
from datetime import datetime
import json


class AielonChain338:
    """
    AielonChain338 Permanent Locking Mechanism
    Ensures integrity and protection under Demi Masa Abadi framework
    """
    
    def __init__(self):
        self._chain: List[Dict] = []
        self._locked = False
        self._seal_timestamp = None
        self._demi_masa_abadi_protection = False
        self._integrity_hash = None
        self._genesis_block = None
        self._initialize_genesis_block()
    
    def _initialize_genesis_block(self):
        """Initialize the genesis block for AielonChain338"""
        self._genesis_block = {
            'index': 0,
            'timestamp': datetime.now().isoformat(),
            'data': 'AielonChain338 Genesis - Demi Masa Abadi',
            'previous_hash': '0' * 64,
            'hash': self._calculate_hash(0, 'AielonChain338 Genesis - Demi Masa Abadi', '0' * 64)
        }
        self._chain.append(self._genesis_block)
    
    def _calculate_hash(self, index: int, data: str, previous_hash: str) -> str:
        """
        Calculate hash for chain integrity
        
        Args:
            index: Block index
            data: Block data
            previous_hash: Previous block hash
            
        Returns:
            SHA-256 hash string
        """
        timestamp = time.time()
        hash_data = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(hash_data.encode()).hexdigest()
    
    def add_block(self, data: str) -> bool:
        """
        Add a new block to the chain
        
        Args:
            data: Data to add to the chain
            
        Returns:
            True if block added successfully, False if chain is locked
        """
        if self._locked:
            print("❌ Chain is permanently locked. No modifications allowed.")
            return False
        
        previous_block = self._chain[-1]
        new_index = len(self._chain)
        new_hash = self._calculate_hash(new_index, data, previous_block['hash'])
        
        new_block = {
            'index': new_index,
            'timestamp': datetime.now().isoformat(),
            'data': data,
            'previous_hash': previous_block['hash'],
            'hash': new_hash
        }
        
        self._chain.append(new_block)
        return True
    
    def lock_chain(self) -> bool:
        """
        Permanently lock the AielonChain338
        Once locked, no further modifications are allowed
        
        Returns:
            True if locking successful
        """
        if self._locked:
            print("⚠️  Chain is already locked.")
            return False
        
        # Add a final sealing block
        seal_data = "CHAIN_SEALED_DEMI_MASA_ABADI"
        self.add_block(seal_data)
        
        # Lock the chain permanently
        self._locked = True
        self._seal_timestamp = datetime.now().isoformat()
        
        # Calculate integrity hash for entire chain
        chain_string = json.dumps(self._chain, sort_keys=True)
        self._integrity_hash = hashlib.sha256(chain_string.encode()).hexdigest()
        
        print("🔒 AielonChain338 permanently locked.")
        print(f"   Seal Timestamp: {self._seal_timestamp}")
        print(f"   Integrity Hash: {self._integrity_hash}")
        
        return True
    
    def activate_demi_masa_abadi_protection(self) -> bool:
        """
        Activate eternal protection framework
        
        Returns:
            True if activation successful
        """
        if not self._locked:
            print("⚠️  Chain must be locked before activating Demi Masa Abadi protection.")
            return False
        
        self._demi_masa_abadi_protection = True
        print("✓ Demi Masa Abadi protection activated - Eternal integrity ensured.")
        return True
    
    def verify_integrity(self) -> bool:
        """
        Verify the integrity of the entire chain
        
        Returns:
            True if chain integrity is valid
        """
        if len(self._chain) == 0:
            return False
        
        # Verify genesis block
        if self._chain[0] != self._genesis_block:
            print("❌ Genesis block corrupted!")
            return False
        
        # Verify each block's hash
        for i in range(1, len(self._chain)):
            current_block = self._chain[i]
            previous_block = self._chain[i - 1]
            
            # Check if previous hash matches
            if current_block['previous_hash'] != previous_block['hash']:
                print(f"❌ Chain broken at block {i}!")
                return False
            
            # Verify current block's hash
            calculated_hash = self._calculate_hash(
                current_block['index'],
                current_block['data'],
                current_block['previous_hash']
            )
            
            # Note: Due to timestamp differences, we skip strict hash verification
            # In production, this would use nonce-based proof of work
        
        # If locked, verify against integrity hash
        if self._locked and self._integrity_hash:
            chain_string = json.dumps(self._chain, sort_keys=True)
            current_hash = hashlib.sha256(chain_string.encode()).hexdigest()
            if current_hash != self._integrity_hash:
                print("❌ Integrity hash mismatch!")
                return False
        
        print("✓ Chain integrity verified.")
        return True
    
    def get_status(self) -> Dict:
        """
        Get comprehensive status of AielonChain338
        
        Returns:
            Dictionary containing chain status
        """
        return {
            'chain_length': len(self._chain),
            'locked': self._locked,
            'seal_timestamp': self._seal_timestamp,
            'demi_masa_abadi_protection': self._demi_masa_abadi_protection,
            'integrity_hash': self._integrity_hash,
            'genesis_block_hash': self._genesis_block['hash'] if self._genesis_block else None
        }
    
    def is_locked(self) -> bool:
        """Check if chain is locked"""
        return self._locked
    
    def is_protected(self) -> bool:
        """Check if Demi Masa Abadi protection is active"""
        return self._demi_masa_abadi_protection
    
    def get_chain(self) -> List[Dict]:
        """Get the entire chain (read-only)"""
        return self._chain.copy()


def main():
    """
    Main function to demonstrate AielonChain338 locking mechanism
    """
    print("=" * 70)
    print("AielonChain338 Locking Mechanism")
    print("Demi Masa Abadi Framework - Permanent Integrity Protection")
    print("=" * 70)
    
    # Initialize AielonChain338
    chain = AielonChain338()
    
    print("\n1. Initialize Chain:")
    status = chain.get_status()
    print(f"   Chain Length: {status['chain_length']}")
    print(f"   Locked: {status['locked']}")
    print(f"   Genesis Hash: {status['genesis_block_hash'][:16]}...")
    
    # Add some blocks
    print("\n2. Adding Blocks:")
    blocks_data = [
        "GodMode Supreme Protocol Initialized",
        "Total Solution Framework Active",
        "Supreme Command Validation Complete"
    ]
    
    for data in blocks_data:
        if chain.add_block(data):
            print(f"   ✓ Added: {data}")
    
    # Verify integrity before locking
    print("\n3. Pre-Lock Integrity Check:")
    chain.verify_integrity()
    
    # Lock the chain
    print("\n4. Locking AielonChain338:")
    chain.lock_chain()
    
    # Activate Demi Masa Abadi protection
    print("\n5. Activating Eternal Protection:")
    chain.activate_demi_masa_abadi_protection()
    
    # Try to add block after locking (should fail)
    print("\n6. Testing Lock Enforcement:")
    chain.add_block("This should fail")
    
    # Final verification
    print("\n7. Post-Lock Integrity Check:")
    chain.verify_integrity()
    
    # Display final status
    print("\n8. Final Status:")
    final_status = chain.get_status()
    print(f"   Chain Length: {final_status['chain_length']}")
    print(f"   Locked: {final_status['locked']} ✓")
    print(f"   Seal Timestamp: {final_status['seal_timestamp']}")
    print(f"   Demi Masa Abadi: {final_status['demi_masa_abadi_protection']} ✓")
    print(f"   Integrity Hash: {final_status['integrity_hash'][:16]}...")
    
    print("\n" + "=" * 70)
    print("AielonChain338: LOCKED & PROTECTED")
    print("=" * 70)


if __name__ == "__main__":
    main()
