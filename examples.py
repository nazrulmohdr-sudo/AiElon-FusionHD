"""
Example Usage: Supreme GodMode Mutlak System
Demonstrates how to use the system in your applications
"""

from supreme_command import SupremeCommand
from supreme_godmode import SupremeGodMode
from aielonchain338 import AielonChain338


def example_complete_system():
    """Example: Complete system upgrade"""
    print("=" * 70)
    print("Example 1: Complete System Upgrade")
    print("=" * 70)
    
    supreme = SupremeCommand()
    success = supreme.execute_supreme_upgrade()
    
    if success:
        print("\n✓ System upgrade completed successfully!")
    else:
        print("\n✗ System upgrade failed!")
    
    return success


def example_godmode_only():
    """Example: Using GodMode component only"""
    print("\n" + "=" * 70)
    print("Example 2: GodMode Component Only")
    print("=" * 70)
    
    godmode = SupremeGodMode()
    
    # Resolve constraints
    print("\n1. Resolving Constraints:")
    print(f"   100% = {godmode.resolve_constraint_full()}")
    print(f"   0% = {godmode.resolve_constraint_zero()}")
    print(f"   all = {godmode.resolve_constraint_all()}")
    
    # Apply percentage logic
    print("\n2. Percentage Logic Examples:")
    values = [0.0, 0.33, 0.5, 0.67, 1.0]
    for val in values:
        result = godmode.apply_percentage_logic(val)
        print(f"   {val:.2f} → {result:.1f}%")
    
    # Get GodMode state
    print("\n3. GodMode Formula State:")
    state = godmode.get_godmode_state()
    print(f"   Formula: {state['formula']}")
    print(f"   Active: {state['active']}")
    print(f"   Integrity: {state['integrity']}")
    
    # Validate system
    print("\n4. System Validation:")
    valid = godmode.validate_total_solution_framework()
    print(f"   Framework Valid: {valid} ✓")
    
    return valid


def example_chain_only():
    """Example: Using AielonChain338 component only"""
    print("\n" + "=" * 70)
    print("Example 3: AielonChain338 Component Only")
    print("=" * 70)
    
    chain = AielonChain338()
    
    # Add some blocks
    print("\n1. Adding Blocks:")
    for i in range(3):
        block = chain.add_block({
            'type': f'data_block_{i}',
            'content': f'Example data {i}',
            'sequence': i
        })
        print(f"   ✓ Block {block['index']} added")
    
    # Validate chain
    print("\n2. Validating Chain Integrity:")
    valid = chain.validate_chain_integrity()
    print(f"   Chain Valid: {valid} ✓")
    
    # Lock the chain
    print("\n3. Applying Immutable Lock:")
    chain.apply_immutable_lock()
    print(f"   Chain Locked: {chain.lock_state['is_locked']} ✓")
    
    # Seal the chain
    print("\n4. Applying Eternal Seal:")
    signature = chain.apply_eternal_seal()
    print(f"   Eternal Signature: {signature[:32]}...")
    print(f"   Demi Masa Abadi: {chain.lock_state['is_sealed']} ✓")
    
    # Get chain status
    print("\n5. Chain Status:")
    status = chain.get_chain_status()
    print(f"   Chain Length: {status['chain_length']}")
    print(f"   Reinforcement Level: {status['reinforcement_level']}")
    print(f"   Integrity Valid: {status['integrity_valid']} ✓")
    
    return True


def example_custom_integration():
    """Example: Custom integration with your application"""
    print("\n" + "=" * 70)
    print("Example 4: Custom Application Integration")
    print("=" * 70)
    
    # Initialize components
    godmode = SupremeGodMode()
    chain = AielonChain338()
    
    print("\n1. Processing Custom Business Logic:")
    
    # Example: Process user action with constraint validation
    user_progress = 0.85  # 85% complete
    validated_progress = godmode.apply_percentage_logic(user_progress)
    print(f"   User Progress: {validated_progress}%")
    
    # Record action in immutable chain
    chain.add_block({
        'type': 'user_action',
        'action': 'task_completion',
        'progress': validated_progress,
        'validated': True
    })
    print(f"   ✓ Action recorded in chain (Block {len(chain.chain) - 1})")
    
    # Validate constraints
    print("\n2. Validating Business Constraints:")
    if validated_progress >= 100.0:
        print(f"   ✓ Task fully complete (100% = {godmode.resolve_constraint_full()})")
    elif validated_progress == 0.0:
        print(f"   ✓ Task not started (0% = {godmode.resolve_constraint_zero()})")
    else:
        print(f"   ⚙ Task in progress ({validated_progress}%)")
    
    # Check system integrity
    print("\n3. System Integrity Check:")
    godmode_valid = godmode.validate_total_solution_framework()
    chain_valid = chain.validate_chain_integrity()
    print(f"   GodMode Valid: {godmode_valid} ✓")
    print(f"   Chain Valid: {chain_valid} ✓")
    print(f"   System Ready: {godmode_valid and chain_valid} ✓")
    
    return godmode_valid and chain_valid


def example_error_handling():
    """Example: Error handling and edge cases"""
    print("\n" + "=" * 70)
    print("Example 5: Error Handling")
    print("=" * 70)
    
    godmode = SupremeGodMode()
    chain = AielonChain338()
    
    print("\n1. Testing Percentage Logic Boundaries:")
    
    # Valid cases
    try:
        result = godmode.apply_percentage_logic(0.0)
        print(f"   ✓ Valid: 0.0 → {result}%")
        
        result = godmode.apply_percentage_logic(1.0)
        print(f"   ✓ Valid: 1.0 → {result}%")
    except ValueError as e:
        print(f"   ✗ Error: {e}")
    
    # Invalid cases
    print("\n2. Testing Invalid Values:")
    
    try:
        godmode.apply_percentage_logic(-0.1)
        print("   ✗ Should have raised ValueError")
    except ValueError:
        print("   ✓ Correctly rejected: -0.1 (below range)")
    
    try:
        godmode.apply_percentage_logic(1.1)
        print("   ✗ Should have raised ValueError")
    except ValueError:
        print("   ✓ Correctly rejected: 1.1 (above range)")
    
    print("\n3. Testing Chain Lock Protection:")
    
    # Lock the chain
    chain.apply_immutable_lock()
    
    try:
        chain.add_block({'type': 'test'})
        print("   ✗ Should have raised RuntimeError")
    except RuntimeError:
        print("   ✓ Correctly rejected: Cannot add blocks after lock")
    
    print("\n4. Testing Seal Order:")
    
    chain2 = AielonChain338()
    try:
        chain2.apply_eternal_seal()
        print("   ✗ Should have raised RuntimeError")
    except RuntimeError:
        print("   ✓ Correctly rejected: Must lock before seal")
    
    return True


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "SUPREME GODMODE MUTLAK" + " " * 31 + "║")
    print("║" + " " * 20 + "Usage Examples" + " " * 34 + "║")
    print("╚" + "=" * 68 + "╝")
    
    examples = [
        ("Complete System Upgrade", example_complete_system),
        ("GodMode Component Only", example_godmode_only),
        ("AielonChain338 Component Only", example_chain_only),
        ("Custom Application Integration", example_custom_integration),
        ("Error Handling", example_error_handling)
    ]
    
    results = []
    for name, example_func in examples:
        try:
            result = example_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ Example '{name}' failed with error: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 70)
    print("EXAMPLES SUMMARY")
    print("=" * 70)
    
    for name, result in results:
        status = "✓" if result else "✗"
        print(f"{status} {name}: {'Success' if result else 'Failed'}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "=" * 70)
    if all_passed:
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY ✓")
    else:
        print("SOME EXAMPLES FAILED ✗")
    print("=" * 70)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
