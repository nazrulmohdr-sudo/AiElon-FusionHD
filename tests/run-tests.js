/**
 * Test Suite for AiElon-FusionHD System
 */

const ConstraintResolver = require('../src/core/ConstraintResolver');
const AielonChain338 = require('../src/core/AielonChain338');
const GodModeEvolution = require('../src/core/GodModeEvolution');
const AiElonFusionHDSystem = require('../src/core/AiElonFusionHDSystem');

class TestRunner {
    constructor() {
        this.tests = [];
        this.passedTests = 0;
        this.failedTests = 0;
    }

    async runTest(name, testFn) {
        try {
            await testFn();
            this.passedTests++;
            console.log(`✓ ${name}`);
            return { name, passed: true };
        } catch (error) {
            this.failedTests++;
            console.log(`✗ ${name}: ${error.message}`);
            return { name, passed: false, error: error.message };
        }
    }

    assert(condition, message) {
        if (!condition) {
            throw new Error(message || 'Assertion failed');
        }
    }

    assertEqual(actual, expected, message) {
        if (actual !== expected) {
            throw new Error(message || `Expected ${expected}, got ${actual}`);
        }
    }

    async runAllTests() {
        console.log('\n' + '='.repeat(70));
        console.log('  AiElon-FusionHD Test Suite');
        console.log('='.repeat(70) + '\n');

        // Constraint Resolver Tests
        console.log('Constraint Resolver Tests:');
        console.log('-'.repeat(70));
        await this.testConstraintResolverInitialization();
        await this.testConstraintValidation();
        await this.testPercentageConversion();
        await this.testValueConversion();

        // AielonChain338 Tests
        console.log('\nAielonChain338 Tests:');
        console.log('-'.repeat(70));
        await this.testChainCreation();
        await this.testChainLocking();
        await this.testChainSealing();
        await this.testChainIntegrity();

        // GodMode Evolution Tests
        console.log('\nGodMode Evolution Tests:');
        console.log('-'.repeat(70));
        await this.testGodModeInitialization();
        await this.testGodModeFormula();
        await this.testSupremeCommandActivation();
        await this.testSupremeGodModeActivation();

        // Integration Tests
        console.log('\nIntegration Tests:');
        console.log('-'.repeat(70));
        await this.testSystemIntegration();
        await this.testCompleteWorkflow();

        // Print summary
        console.log('\n' + '='.repeat(70));
        console.log(`Test Summary: ${this.passedTests} passed, ${this.failedTests} failed`);
        console.log('='.repeat(70) + '\n');

        return {
            total: this.passedTests + this.failedTests,
            passed: this.passedTests,
            failed: this.failedTests,
            success: this.failedTests === 0
        };
    }

    // Constraint Resolver Tests
    async testConstraintResolverInitialization() {
        await this.runTest('ConstraintResolver initialization', async () => {
            const resolver = new ConstraintResolver();
            const result = resolver.initialize();
            this.assert(result.success, 'Initialization should succeed');
            this.assert(resolver.isInitialized, 'Should be initialized');
        });
    }

    async testConstraintValidation() {
        await this.runTest('Constraint validation (100%=1, 0%=0)', async () => {
            const resolver = new ConstraintResolver();
            resolver.initialize();
            const validation = resolver.validateConsistency();
            this.assert(validation.valid, 'Validation should pass');
            this.assertEqual(validation.errorCount, 0, 'Should have zero errors');
        });
    }

    async testPercentageConversion() {
        await this.runTest('Percentage to value conversion', async () => {
            const resolver = new ConstraintResolver();
            resolver.initialize();
            
            const result0 = resolver.percentageToValue(0);
            this.assertEqual(result0.output, 0, '0% should equal 0');
            
            const result100 = resolver.percentageToValue(100);
            this.assertEqual(result100.output, 1, '100% should equal 1');
            
            const result50 = resolver.percentageToValue(50);
            this.assertEqual(result50.output, 0.5, '50% should equal 0.5');
        });
    }

    async testValueConversion() {
        await this.runTest('Value to percentage conversion', async () => {
            const resolver = new ConstraintResolver();
            resolver.initialize();
            
            const result0 = resolver.valueToPercentage(0);
            this.assertEqual(result0.output, 0, '0 should equal 0%');
            
            const result1 = resolver.valueToPercentage(1);
            this.assertEqual(result1.output, 100, '1 should equal 100%');
        });
    }

    // AielonChain338 Tests
    async testChainCreation() {
        await this.runTest('Chain genesis block creation', async () => {
            const chain = new AielonChain338();
            const genesis = chain.createGenesisBlock();
            this.assert(genesis, 'Genesis block should be created');
            this.assertEqual(genesis.index, 0, 'Genesis should have index 0');
        });
    }

    async testChainLocking() {
        await this.runTest('Chain locking mechanism', async () => {
            const chain = new AielonChain338();
            chain.createGenesisBlock();
            const lockResult = chain.lock();
            this.assert(lockResult.success, 'Lock should succeed');
            this.assert(chain.isLocked, 'Chain should be locked');
        });
    }

    async testChainSealing() {
        await this.runTest('Chain sealing (Demi Masa Abadi)', async () => {
            const chain = new AielonChain338();
            chain.createGenesisBlock();
            chain.lock();
            const sealResult = chain.seal();
            this.assert(sealResult.success, 'Seal should succeed');
            this.assert(chain.isSealed, 'Chain should be sealed');
            this.assert(sealResult.sealHash, 'Should have seal hash');
        });
    }

    async testChainIntegrity() {
        await this.runTest('Chain integrity validation', async () => {
            const chain = new AielonChain338();
            chain.createGenesisBlock();
            chain.addBlock({ data: 'test' });
            chain.lock();
            chain.seal();
            
            const integrity = chain.validateIntegrity();
            this.assert(integrity.valid, 'Integrity should be valid');
        });
    }

    // GodMode Evolution Tests
    async testGodModeInitialization() {
        await this.runTest('GodMode initialization at Level 0', async () => {
            const godMode = new GodModeEvolution();
            const result = godMode.initialize();
            this.assert(result.success, 'Initialization should succeed');
            this.assertEqual(result.level, 0, 'Should be at Level 0');
            this.assert(result.capabilities.length > 0, 'Should have capabilities');
        });
    }

    async testGodModeFormula() {
        await this.runTest('GodMode formula (∞↑∞)↑(∞↑∞)', async () => {
            const godMode = new GodModeEvolution();
            godMode.initialize();
            const validation = godMode.validateFormula();
            this.assert(validation.valid, 'Formula should be valid');
            this.assertEqual(validation.formula, '(∞↑∞)↑(∞↑∞)', 'Formula should match');
        });
    }

    async testSupremeCommandActivation() {
        await this.runTest('Supreme Command Mutlak activation', async () => {
            const godMode = new GodModeEvolution();
            godMode.initialize();
            const result = godMode.activateSupremeCommand();
            this.assert(result.success, 'Activation should succeed');
            this.assertEqual(result.authority, 'ABSOLUTE', 'Should have absolute authority');
        });
    }

    async testSupremeGodModeActivation() {
        await this.runTest('Supreme GodMode Mutlak activation', async () => {
            const godMode = new GodModeEvolution();
            godMode.initialize();
            const result = godMode.activateSupremeGodMode();
            this.assert(result.success, 'Activation should succeed');
            this.assertEqual(result.power, 'UNLIMITED', 'Should have unlimited power');
        });
    }

    // Integration Tests
    async testSystemIntegration() {
        await this.runTest('Complete system integration', async () => {
            const system = new AiElonFusionHDSystem();
            const result = await system.initialize();
            this.assert(result.success, 'System initialization should succeed');
            this.assert(system.isFullyInitialized, 'System should be fully initialized');
            this.assertEqual(system.systemStatus, 'SUPREME_ACTIVE', 'Should be SUPREME_ACTIVE');
        });
    }

    async testCompleteWorkflow() {
        await this.runTest('Complete workflow validation', async () => {
            const system = new AiElonFusionHDSystem();
            await system.initialize();
            
            // Validate system
            const validation = system.validateSystem();
            this.assert(validation.overallValid, 'System should be valid');
            
            // Test dynamic logic
            const dynamicResult = system.processDynamicLogic(75);
            this.assertEqual(dynamicResult.output, 0.75, 'Dynamic logic should work');
            
            // Get status
            const status = system.getSystemStatus();
            this.assert(status.isFullyInitialized, 'Should be initialized');
        });
    }
}

// Run tests
async function main() {
    const runner = new TestRunner();
    const results = await runner.runAllTests();
    process.exit(results.success ? 0 : 1);
}

if (require.main === module) {
    main().catch(error => {
        console.error('Test runner error:', error);
        process.exit(1);
    });
}

module.exports = TestRunner;
