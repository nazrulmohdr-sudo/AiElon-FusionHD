"""
AiElon-FusionHD Chain Lock and Seal System
Implements AielonChain338 lock-and-seal mechanism following "Demi Masa Abadi" principle
"""

from typing import Dict, Any, Optional, List
import hashlib
import time
import json


class AielonChain338:
    """
    AielonChain338: Eternal immutability lock-and-seal mechanism.
    
    Following "Demi Masa Abadi" (For Eternal Time) principle:
    - Immutable chain structure
    - Cryptographic sealing
    - Eternal timestamp preservation
    - Tamper-proof verification
    """
    
    def __init__(self):
        self.chain = []
        self.sealed = False
        self.seal_hash = None
        self.seal_timestamp = None
        self.genesis_timestamp = time.time()
        self._create_genesis_block()
    
    def _create_genesis_block(self):
        """Create the immutable genesis block."""
        genesis = {
            'block_id': 0,
            'timestamp': self.genesis_timestamp,
            'data': {
                'type': 'genesis',
                'principle': 'Demi Masa Abadi',
                'description': 'Eternal immutability foundation',
                'chain_id': 'AielonChain338'
            },
            'previous_hash': '0' * 64,
            'nonce': 338
        }
        genesis['hash'] = self._compute_hash(genesis)
        self.chain.append(genesis)
    
    def add_block(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a new block to the chain.
        
        Args:
            data: Data to be stored in the block
        
        Returns:
            The newly created block
        """
        if self.sealed:
            return {
                'error': 'Chain is sealed - cannot add new blocks',
                'sealed_at': self.seal_timestamp,
                'seal_hash': self.seal_hash
            }
        
        previous_block = self.chain[-1]
        new_block = {
            'block_id': len(self.chain),
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_block['hash'],
            'nonce': self._calculate_nonce(data)
        }
        new_block['hash'] = self._compute_hash(new_block)
        
        self.chain.append(new_block)
        return new_block
    
    def lock_and_seal(self) -> Dict[str, Any]:
        """
        Lock and seal the chain following Demi Masa Abadi principle.
        
        This operation is irreversible and ensures eternal immutability.
        
        Returns:
            Seal confirmation with cryptographic proof
        """
        if self.sealed:
            return {
                'status': 'ALREADY_SEALED',
                'sealed_at': self.seal_timestamp,
                'seal_hash': self.seal_hash,
                'message': 'Chain was already sealed - immutability preserved'
            }
        
        # Create comprehensive seal
        seal_data = {
            'chain_id': 'AielonChain338',
            'principle': 'Demi Masa Abadi',
            'block_count': len(self.chain),
            'genesis_timestamp': self.genesis_timestamp,
            'seal_timestamp': time.time(),
            'chain_hashes': [block['hash'] for block in self.chain],
            'final_block_hash': self.chain[-1]['hash']
        }
        
        # Compute seal hash
        seal_string = json.dumps(seal_data, sort_keys=True)
        self.seal_hash = hashlib.sha256(seal_string.encode()).hexdigest()
        self.seal_timestamp = seal_data['seal_timestamp']
        self.sealed = True
        
        seal_confirmation = {
            'status': 'SEALED',
            'seal_hash': self.seal_hash,
            'seal_timestamp': self.seal_timestamp,
            'block_count': len(self.chain),
            'principle': 'Demi Masa Abadi - Eternal Immutability Achieved',
            'verification': self._generate_seal_verification()
        }
        
        return seal_confirmation
    
    def verify_chain_integrity(self) -> Dict[str, Any]:
        """
        Verify the integrity of the entire chain.
        
        Returns:
            Verification report with detailed integrity checks
        """
        integrity_report = {
            'chain_valid': True,
            'block_count': len(self.chain),
            'sealed': self.sealed,
            'checks': []
        }
        
        # Check 1: Verify genesis block
        genesis_check = {
            'check': 'genesis_block',
            'valid': self.chain[0]['block_id'] == 0 and self.chain[0]['previous_hash'] == '0' * 64
        }
        integrity_report['checks'].append(genesis_check)
        
        # Check 2: Verify block chain linkage
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            link_check = {
                'check': f'block_{i}_linkage',
                'valid': current_block['previous_hash'] == previous_block['hash']
            }
            integrity_report['checks'].append(link_check)
            
            # Check hash integrity
            hash_check = {
                'check': f'block_{i}_hash',
                'valid': current_block['hash'] == self._compute_hash(current_block)
            }
            integrity_report['checks'].append(hash_check)
        
        # Check 3: Verify seal if sealed
        if self.sealed:
            seal_check = {
                'check': 'seal_integrity',
                'valid': self._verify_seal()
            }
            integrity_report['checks'].append(seal_check)
        
        # Overall validity
        integrity_report['chain_valid'] = all(check['valid'] for check in integrity_report['checks'])
        integrity_report['status'] = 'VALID' if integrity_report['chain_valid'] else 'INVALID'
        
        return integrity_report
    
    def _compute_hash(self, block: Dict[str, Any]) -> str:
        """Compute SHA-256 hash of a block."""
        # Create a copy without the hash field
        block_copy = {k: v for k, v in block.items() if k != 'hash'}
        block_string = json.dumps(block_copy, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def _calculate_nonce(self, data: Dict[str, Any]) -> int:
        """Calculate nonce based on data (simplified proof-of-work)."""
        data_string = json.dumps(data, sort_keys=True)
        hash_int = int(hashlib.sha256(data_string.encode()).hexdigest(), 16)
        return hash_int % 1000000
    
    def _verify_seal(self) -> bool:
        """Verify the seal integrity."""
        if not self.sealed:
            return False
        
        # Reconstruct seal data
        seal_data = {
            'chain_id': 'AielonChain338',
            'principle': 'Demi Masa Abadi',
            'block_count': len(self.chain),
            'genesis_timestamp': self.genesis_timestamp,
            'seal_timestamp': self.seal_timestamp,
            'chain_hashes': [block['hash'] for block in self.chain],
            'final_block_hash': self.chain[-1]['hash']
        }
        
        seal_string = json.dumps(seal_data, sort_keys=True)
        computed_seal = hashlib.sha256(seal_string.encode()).hexdigest()
        
        return computed_seal == self.seal_hash
    
    def _generate_seal_verification(self) -> Dict[str, Any]:
        """Generate verification data for the seal."""
        return {
            'seal_hash': self.seal_hash,
            'verifiable': True,
            'timestamp': self.seal_timestamp,
            'chain_snapshot': {
                'first_block': self.chain[0]['hash'],
                'last_block': self.chain[-1]['hash'],
                'total_blocks': len(self.chain)
            }
        }
    
    def get_chain_info(self) -> Dict[str, Any]:
        """Get comprehensive information about the chain."""
        return {
            'chain_id': 'AielonChain338',
            'principle': 'Demi Masa Abadi',
            'genesis_timestamp': self.genesis_timestamp,
            'block_count': len(self.chain),
            'sealed': self.sealed,
            'seal_timestamp': self.seal_timestamp,
            'seal_hash': self.seal_hash,
            'blocks': self.chain.copy()
        }
    
    def export_chain(self) -> str:
        """Export chain as JSON string."""
        return json.dumps(self.get_chain_info(), indent=2)


# Module-level convenience functions
def create_and_seal_chain(data_blocks: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Convenience function to create and seal a chain with optional data blocks.
    
    Args:
        data_blocks: Optional list of data blocks to add before sealing
    
    Returns:
        Seal confirmation
    """
    chain = AielonChain338()
    
    if data_blocks:
        for data in data_blocks:
            chain.add_block(data)
    
    return chain.lock_and_seal()
