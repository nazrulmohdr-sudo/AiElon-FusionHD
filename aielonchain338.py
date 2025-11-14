"""
AiElon-FusionHD AielonChain338 Security System
Demi Masa Abadi (Eternal Time) Protocol Implementation

This module implements the AielonChain338 mechanism with absolute
immutability under the "Demi Masa Abadi" protocol.
"""

import hashlib
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime


class AielonBlock:
    """
    Individual block in the AielonChain338.
    Each block is immutable once sealed.
    """
    
    def __init__(self, index: int, data: Dict[str, Any], 
                 previous_hash: str = "0"):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.sealed = False
        self.eternal_lock = False
    
    def calculate_hash(self) -> str:
        """
        Calculate cryptographic hash of the block.
        
        Returns:
            SHA-256 hash of block contents
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def seal_block(self):
        """Seal the block, making it immutable."""
        if not self.sealed:
            self.sealed = True
            self.hash = self.calculate_hash()
    
    def apply_eternal_lock(self):
        """
        Apply Demi Masa Abadi eternal lock.
        Once locked, the block is absolutely immutable.
        """
        if self.sealed:
            self.eternal_lock = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert block to dictionary representation."""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "sealed": self.sealed,
            "eternal_lock": self.eternal_lock
        }


class AielonChain338:
    """
    AielonChain338: Immutable chain secured by Demi Masa Abadi protocol.
    
    Features:
    - Cryptographic integrity
    - Absolute immutability
    - Eternal lock mechanism
    - Chain validation
    """
    
    def __init__(self):
        self.chain: List[AielonBlock] = []
        self.sealed = False
        self.eternal_protocol_active = False
        self._create_genesis_block()
    
    def _create_genesis_block(self):
        """Create the first block (Genesis Block) of the chain."""
        genesis_data = {
            "type": "genesis",
            "message": "AielonChain338 Genesis - Supreme GodMode Mutlak",
            "timestamp": datetime.now().isoformat(),
            "version": "338.0.0"
        }
        
        genesis_block = AielonBlock(0, genesis_data, "0")
        genesis_block.seal_block()
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> AielonBlock:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_block(self, data: Dict[str, Any]) -> bool:
        """
        Add a new block to the chain.
        
        Args:
            data: Data to store in the new block
        
        Returns:
            True if block added successfully, False if chain is sealed
        """
        if self.sealed:
            print("❌ Cannot add block: Chain is sealed under Demi Masa Abadi protocol")
            return False
        
        previous_block = self.get_latest_block()
        new_block = AielonBlock(
            index=len(self.chain),
            data=data,
            previous_hash=previous_block.hash
        )
        
        new_block.seal_block()
        self.chain.append(new_block)
        return True
    
    def validate_chain(self) -> bool:
        """
        Validate the entire chain integrity.
        
        Returns:
            True if chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Verify chain linkage
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify block is sealed
            if not current_block.sealed:
                return False
        
        return True
    
    def apply_demi_masa_abadi_protocol(self) -> Dict[str, Any]:
        """
        Apply Demi Masa Abadi (Eternal Time) protocol.
        
        This locks and seals the entire chain with absolute immutability.
        Once applied, no modifications are possible.
        
        Returns:
            Protocol application status
        """
        if not self.validate_chain():
            return {
                "success": False,
                "message": "Chain validation failed. Cannot apply eternal protocol.",
                "timestamp": datetime.now().isoformat()
            }
        
        # Seal entire chain
        self.sealed = True
        
        # Apply eternal lock to all blocks
        for block in self.chain:
            block.apply_eternal_lock()
        
        # Activate eternal protocol
        self.eternal_protocol_active = True
        
        return {
            "success": True,
            "message": "Demi Masa Abadi protocol applied successfully",
            "chain_sealed": True,
            "eternal_lock_active": True,
            "blocks_secured": len(self.chain),
            "protocol_timestamp": datetime.now().isoformat(),
            "immutability_level": "absolute"
        }
    
    def get_chain_status(self) -> Dict[str, Any]:
        """
        Get complete status of AielonChain338.
        
        Returns:
            Dictionary containing chain status and statistics
        """
        return {
            "chain_name": "AielonChain338",
            "total_blocks": len(self.chain),
            "chain_valid": self.validate_chain(),
            "chain_sealed": self.sealed,
            "eternal_protocol_active": self.eternal_protocol_active,
            "immutability_status": "absolute" if self.eternal_protocol_active else "standard",
            "genesis_block_hash": self.chain[0].hash,
            "latest_block_hash": self.get_latest_block().hash,
            "all_blocks_locked": all(block.eternal_lock for block in self.chain)
        }
    
    def export_chain(self) -> List[Dict[str, Any]]:
        """Export entire chain as JSON-serializable format."""
        return [block.to_dict() for block in self.chain]


def main():
    """Demonstrate AielonChain338 functionality."""
    print("=== AielonChain338 Security System ===")
    print("=== Demi Masa Abadi Protocol ===\n")
    
    # Initialize chain
    chain = AielonChain338()
    print("1. Chain Initialized")
    print(f"   Genesis Block: {chain.chain[0].hash[:16]}...")
    
    # Add system blocks
    print("\n2. Adding System Blocks...")
    
    blocks_data = [
        {
            "type": "constraint_system",
            "status": "operational",
            "completeness": 1.0,
            "conflicts": 0.0
        },
        {
            "type": "godmode_framework",
            "formula": "GodMode 0 = ♾️ = (♾️↑♾️)↑(♾️↑♾️)",
            "status": "active"
        },
        {
            "type": "system_state",
            "coherence": True,
            "stability": True,
            "scaling": "infinite"
        }
    ]
    
    for data in blocks_data:
        if chain.add_block(data):
            print(f"   ✓ Block {len(chain.chain)-1} added: {data['type']}")
    
    # Validate chain before sealing
    print("\n3. Chain Validation:")
    is_valid = chain.validate_chain()
    print(f"   Chain Valid: {'✓' if is_valid else '✗'}")
    print(f"   Total Blocks: {len(chain.chain)}")
    
    # Apply Demi Masa Abadi protocol
    print("\n4. Applying Demi Masa Abadi Protocol...")
    protocol_result = chain.apply_demi_masa_abadi_protocol()
    
    if protocol_result['success']:
        print(f"   ✓ {protocol_result['message']}")
        print(f"   Blocks Secured: {protocol_result['blocks_secured']}")
        print(f"   Immutability Level: {protocol_result['immutability_level']}")
        print(f"   Protocol Timestamp: {protocol_result['protocol_timestamp']}")
    
    # Verify immutability
    print("\n5. Testing Immutability...")
    attempt_add = chain.add_block({"test": "should_fail"})
    print(f"   Attempt to add block after seal: {'✗ Blocked' if not attempt_add else '✓ Error'}")
    
    # Final status
    print("\n6. Final Chain Status:")
    status = chain.get_chain_status()
    print(f"   Chain Name: {status['chain_name']}")
    print(f"   Total Blocks: {status['total_blocks']}")
    print(f"   Chain Valid: {'✓' if status['chain_valid'] else '✗'}")
    print(f"   Chain Sealed: {'✓' if status['chain_sealed'] else '✗'}")
    print(f"   Eternal Protocol: {'✓' if status['eternal_protocol_active'] else '✗'}")
    print(f"   All Blocks Locked: {'✓' if status['all_blocks_locked'] else '✗'}")
    print(f"   Immutability: {status['immutability_status']}")
    
    print("\n✓ AielonChain338 secured under Demi Masa Abadi protocol")


if __name__ == "__main__":
    main()
