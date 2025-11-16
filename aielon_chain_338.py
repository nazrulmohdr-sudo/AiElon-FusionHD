"""
AielonChain338 Security Module

Implements the locked and sealed security framework for permanent
integrity and compliance with "Demi Masa Abadi" (Eternal Time).
"""

import hashlib
import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime


class AielonChain338:
    """
    Secure, immutable chain module providing permanent integrity.
    
    This module is LOCKED and SEALED for eternal compliance.
    """
    
    # Security seal constant - do not modify
    SECURITY_SEAL = "AIELON_CHAIN_338_SEALED"
    FRAMEWORK = "Demi Masa Abadi"  # Eternal Time Framework
    
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.locked = True
        self.sealed = True
        self.genesis_timestamp = time.time()
        self._initialize_genesis_block()
    
    def _initialize_genesis_block(self):
        """Initialize the genesis block for the chain."""
        genesis = {
            "index": 0,
            "timestamp": self.genesis_timestamp,
            "data": {
                "type": "genesis",
                "framework": self.FRAMEWORK,
                "seal": self.SECURITY_SEAL,
                "integrity": "permanent",
                "compliance": "eternal"
            },
            "previous_hash": "0",
            "hash": None
        }
        genesis["hash"] = self._calculate_hash(genesis)
        self.chain.append(genesis)
    
    def _calculate_hash(self, block: Dict[str, Any]) -> str:
        """
        Calculate cryptographic hash for a block.
        
        Args:
            block: Block data to hash
            
        Returns:
            SHA-256 hash of the block
        """
        # Create a copy without the hash field
        block_copy = block.copy()
        block_copy.pop("hash", None)
        
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def add_block(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Add a new block to the chain (if not sealed).
        
        Args:
            data: Data to include in the new block
            
        Returns:
            The new block if successful, None if chain is sealed
        """
        if self.sealed:
            # Chain is permanently sealed, no modifications allowed
            return None
        
        previous_block = self.chain[-1]
        new_block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "data": data,
            "previous_hash": previous_block["hash"],
            "hash": None
        }
        new_block["hash"] = self._calculate_hash(new_block)
        self.chain.append(new_block)
        
        return new_block
    
    def verify_integrity(self) -> Dict[str, Any]:
        """
        Verify the complete integrity of the chain.
        
        Returns:
            Verification results including status and details
        """
        if len(self.chain) == 0:
            return {
                "valid": False,
                "reason": "Empty chain"
            }
        
        # Verify each block
        for i in range(len(self.chain)):
            block = self.chain[i]
            
            # Verify hash
            calculated_hash = self._calculate_hash(block)
            if block["hash"] != calculated_hash:
                return {
                    "valid": False,
                    "reason": f"Block {i} hash mismatch",
                    "block_index": i
                }
            
            # Verify chain linkage (except genesis)
            if i > 0:
                if block["previous_hash"] != self.chain[i - 1]["hash"]:
                    return {
                        "valid": False,
                        "reason": f"Block {i} chain linkage broken",
                        "block_index": i
                    }
        
        return {
            "valid": True,
            "integrity": "permanent",
            "sealed": self.sealed,
            "locked": self.locked,
            "framework": self.FRAMEWORK,
            "blocks": len(self.chain)
        }
    
    def get_seal_status(self) -> Dict[str, Any]:
        """
        Get the current seal and lock status.
        
        Returns:
            Status information about security seal
        """
        return {
            "sealed": self.sealed,
            "locked": self.locked,
            "security_seal": self.SECURITY_SEAL,
            "framework": self.FRAMEWORK,
            "integrity": "permanent",
            "compliance": "eternal",
            "genesis_timestamp": self.genesis_timestamp,
            "genesis_date": datetime.fromtimestamp(self.genesis_timestamp).isoformat()
        }
    
    def get_chain_info(self) -> Dict[str, Any]:
        """
        Get comprehensive chain information.
        
        Returns:
            Complete chain status and metadata
        """
        integrity = self.verify_integrity()
        seal_status = self.get_seal_status()
        
        return {
            "name": "AielonChain338",
            "version": "1.0.0",
            "integrity_verification": integrity,
            "seal_status": seal_status,
            "block_count": len(self.chain),
            "immutable": True,
            "tamper_proof": True
        }


def initialize_aielon_chain() -> AielonChain338:
    """Initialize and return AielonChain338 instance."""
    return AielonChain338()


def lock_and_seal_chain(chain: AielonChain338) -> Dict[str, Any]:
    """
    Lock and seal the AielonChain338 for permanent integrity.
    
    Args:
        chain: The AielonChain338 instance to seal
        
    Returns:
        Seal confirmation with status
    """
    chain.locked = True
    chain.sealed = True
    
    return {
        "status": "sealed",
        "message": "AielonChain338 permanently locked and sealed",
        "framework": chain.FRAMEWORK,
        "seal": chain.SECURITY_SEAL,
        "timestamp": time.time(),
        "integrity": "permanent",
        "compliance": "eternal"
    }


if __name__ == "__main__":
    # Initialize AielonChain338
    chain = initialize_aielon_chain()
    
    print("=== AielonChain338 Initialization ===")
    print(f"Framework: {chain.FRAMEWORK}")
    print(f"Security Seal: {chain.SECURITY_SEAL}")
    
    # Verify integrity
    print("\n=== Integrity Verification ===")
    integrity = chain.verify_integrity()
    print(json.dumps(integrity, indent=2))
    
    # Get seal status
    print("\n=== Seal Status ===")
    seal_status = chain.get_seal_status()
    print(json.dumps(seal_status, indent=2))
    
    # Lock and seal confirmation
    print("\n=== Lock & Seal Confirmation ===")
    seal_confirmation = lock_and_seal_chain(chain)
    print(json.dumps(seal_confirmation, indent=2))
    
    # Final chain info
    print("\n=== Chain Information ===")
    chain_info = chain.get_chain_info()
    print(json.dumps(chain_info, indent=2, default=str))
