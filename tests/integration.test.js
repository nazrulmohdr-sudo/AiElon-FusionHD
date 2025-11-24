/**
 * AiElon Living OS - Integration Tests
 * Version: 2.0.0
 */

const assert = require('assert');

// Import modules
const { CoreOS, SecurityModule, CompatibilityLayer } = require('../src/core/os');
const { AielonChain338 } = require('../src/blockchain/aielonchain338');
const { FusionHDUI } = require('../src/ui/fusion-hd');
const { HalalWallet } = require('../src/wallet/halal-wallet');
const { HCareSystem } = require('../src/hcare/hcare-system');
const { UmmahPlatform } = require('../src/ummah-hub/ummah-platform');

async function runTests() {
    console.log('🧪 Running AiElon Living OS Integration Tests\n');
    
    let passedTests = 0;
    let failedTests = 0;

    // Test 1: Core OS Initialization
    try {
        console.log('Test 1: Core OS Initialization...');
        const coreOS = new CoreOS();
        await coreOS.initialize({
            security: {},
            compatibility: {}
        });
        assert.strictEqual(coreOS.systemState, 'online');
        console.log('✅ PASSED: Core OS initialized successfully\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Core OS initialization -', error.message, '\n');
        failedTests++;
    }

    // Test 2: Security Module
    try {
        console.log('Test 2: Security Module...');
        const security = new SecurityModule({});
        await security.initialize();
        assert.strictEqual(security.encryptionEnabled, true);
        assert.strictEqual(security.authenticationEnabled, true);
        
        const encrypted = security.encrypt({ data: 'test' });
        const decrypted = security.decrypt(encrypted);
        assert.deepStrictEqual(decrypted, { data: 'test' });
        
        console.log('✅ PASSED: Security module working correctly\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Security module -', error.message, '\n');
        failedTests++;
    }

    // Test 3: Compatibility Layer
    try {
        console.log('Test 3: Compatibility Layer...');
        const compatibility = new CompatibilityLayer({});
        await compatibility.initialize();
        assert.strictEqual(compatibility.isPlatformSupported('linux'), true);
        assert.strictEqual(compatibility.isPlatformSupported('darwin'), true);
        assert.strictEqual(compatibility.isPlatformSupported('win32'), true);
        console.log('✅ PASSED: Compatibility layer supports all platforms\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Compatibility layer -', error.message, '\n');
        failedTests++;
    }

    // Test 4: Blockchain Connection
    try {
        console.log('Test 4: Blockchain Connection...');
        const blockchain = new AielonChain338();
        await blockchain.initialize({
            rpcEndpoint: 'https://rpc.aielonchain338.network',
            wsEndpoint: 'wss://ws.aielonchain338.network'
        });
        assert.strictEqual(blockchain.connected, true);
        assert.strictEqual(blockchain.networkId, 338);
        console.log('✅ PASSED: Blockchain connected successfully\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Blockchain connection -', error.message, '\n');
        failedTests++;
    }

    // Test 5: Blockchain Transaction
    try {
        console.log('Test 5: Blockchain Transaction...');
        const blockchain = new AielonChain338();
        await blockchain.initialize({});
        
        const tx = await blockchain.createTransaction(
            '0x123',
            '0x456',
            100,
            { memo: 'test' }
        );
        
        assert.strictEqual(tx.from, '0x123');
        assert.strictEqual(tx.to, '0x456');
        assert.strictEqual(tx.amount, 100);
        assert.strictEqual(tx.status, 'pending');
        
        console.log('✅ PASSED: Transaction created successfully\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Blockchain transaction -', error.message, '\n');
        failedTests++;
    }

    // Test 6: Fusion HD UI
    try {
        console.log('Test 6: Fusion HD UI...');
        const ui = new FusionHDUI();
        await ui.initialize({}, null);
        assert.strictEqual(ui.version, '2.0.0');
        assert(ui.themes.light);
        assert(ui.themes.dark);
        assert(ui.themes.islamic);
        console.log('✅ PASSED: Fusion HD UI initialized with themes\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Fusion HD UI -', error.message, '\n');
        failedTests++;
    }

    // Test 7: Halal Wallet
    try {
        console.log('Test 7: Halal Wallet...');
        const wallet = new HalalWallet();
        const blockchain = new AielonChain338();
        await blockchain.initialize({});
        await wallet.initialize({}, blockchain);
        
        assert.strictEqual(wallet.shariahCompliance, true);
        assert.strictEqual(wallet.blockchain, blockchain);
        
        console.log('✅ PASSED: Halal Wallet initialized with Shariah compliance\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Halal Wallet -', error.message, '\n');
        failedTests++;
    }

    // Test 8: Wallet Creation
    try {
        console.log('Test 8: Wallet Creation...');
        const wallet = new HalalWallet();
        await wallet.initialize({}, null);
        
        const newWallet = await wallet.createWallet('user123');
        assert(newWallet.walletId);
        assert(newWallet.address);
        assert(newWallet.publicKey);
        assert(newWallet.recoveryPhrase);
        
        console.log('✅ PASSED: Wallet created with all required fields\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Wallet creation -', error.message, '\n');
        failedTests++;
    }

    // Test 9: Zakat Calculation
    try {
        console.log('Test 9: Zakat Calculation...');
        const wallet = new HalalWallet();
        await wallet.initialize({}, null);
        
        const newWallet = await wallet.createWallet('user123');
        const walletData = wallet.getWallet(newWallet.walletId);
        walletData.balance = 1000;
        
        const zakat = wallet.calculateZakat(newWallet.walletId);
        assert.strictEqual(zakat.amount, 25); // 2.5% of 1000
        assert.strictEqual(zakat.rate, 0.025);
        
        console.log('✅ PASSED: Zakat calculated correctly (2.5%)\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Zakat calculation -', error.message, '\n');
        failedTests++;
    }

    // Test 10: Shariah Compliance Check
    try {
        console.log('Test 10: Shariah Compliance Check...');
        const wallet = new HalalWallet();
        await wallet.initialize({}, null);
        
        // Test valid transaction
        await wallet.checkShariahCompliance('0x123', 100, 'Halal payment');
        
        // Test invalid transaction (interest-based)
        let failed = false;
        try {
            await wallet.checkShariahCompliance('0x123', 100, 'Interest payment');
        } catch (e) {
            failed = true;
        }
        assert(failed, 'Should reject interest-based transaction');
        
        console.log('✅ PASSED: Shariah compliance checking works\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Shariah compliance -', error.message, '\n');
        failedTests++;
    }

    // Test 11: HCare System
    try {
        console.log('Test 11: HCare System...');
        const hcare = new HCareSystem();
        await hcare.initialize({});
        
        assert.strictEqual(hcare.privacyEnabled, true);
        assert.strictEqual(hcare.privacy.hipaaCompliant, true);
        assert.strictEqual(hcare.privacy.gdprCompliant, true);
        
        console.log('✅ PASSED: HCare system initialized with privacy compliance\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: HCare system -', error.message, '\n');
        failedTests++;
    }

    // Test 12: Patient Registration
    try {
        console.log('Test 12: Patient Registration...');
        const hcare = new HCareSystem();
        await hcare.initialize({});
        
        const patient = await hcare.registerPatient({
            personalInfo: { name: 'John Doe', dateOfBirth: '1990-01-01' },
            demographics: { address: '123 Main St' },
            emergencyContact: { name: 'Jane Doe', phone: '555-0100' }
        });
        
        assert(patient.patientId);
        assert.strictEqual(patient.success, true);
        
        console.log('✅ PASSED: Patient registered successfully\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Patient registration -', error.message, '\n');
        failedTests++;
    }

    // Test 13: Ummah Hub
    try {
        console.log('Test 13: Ummah Hub...');
        const ummah = new UmmahPlatform();
        await ummah.initialize({});
        
        assert.strictEqual(ummah.moderation.enabled, true);
        assert.strictEqual(ummah.moderation.islamicValues, true);
        
        console.log('✅ PASSED: Ummah Hub initialized with moderation\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Ummah Hub -', error.message, '\n');
        failedTests++;
    }

    // Test 14: User Registration
    try {
        console.log('Test 14: User Registration...');
        const ummah = new UmmahPlatform();
        await ummah.initialize({});
        
        const user = await ummah.registerUser({
            username: 'testuser',
            email: 'test@example.com',
            displayName: 'Test User'
        });
        
        assert(user.userId);
        assert.strictEqual(user.username, 'testuser');
        assert.strictEqual(user.success, true);
        
        console.log('✅ PASSED: User registered successfully\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: User registration -', error.message, '\n');
        failedTests++;
    }

    // Test 15: Content Moderation
    try {
        console.log('Test 15: Content Moderation...');
        const ummah = new UmmahPlatform();
        await ummah.initialize({});
        
        // Test clean content
        const cleanResult = await ummah.moderateContent('This is a clean message');
        assert.strictEqual(cleanResult.approved, true);
        
        // Test prohibited content
        const dirtyResult = await ummah.moderateContent('This contains hate speech');
        assert.strictEqual(dirtyResult.approved, false);
        
        console.log('✅ PASSED: Content moderation working correctly\n');
        passedTests++;
    } catch (error) {
        console.error('❌ FAILED: Content moderation -', error.message, '\n');
        failedTests++;
    }

    // Test Summary
    console.log('\n' + '='.repeat(50));
    console.log('📊 TEST SUMMARY');
    console.log('='.repeat(50));
    console.log(`Total Tests: ${passedTests + failedTests}`);
    console.log(`✅ Passed: ${passedTests}`);
    console.log(`❌ Failed: ${failedTests}`);
    console.log(`Success Rate: ${((passedTests / (passedTests + failedTests)) * 100).toFixed(2)}%`);
    console.log('='.repeat(50));

    if (failedTests === 0) {
        console.log('\n🎉 All tests passed! System is ready for deployment.\n');
        return 0;
    } else {
        console.log('\n⚠️  Some tests failed. Please review the failures above.\n');
        return 1;
    }
}

// Run tests if this file is executed directly
if (require.main === module) {
    runTests().then(exitCode => {
        process.exit(exitCode);
    }).catch(error => {
        console.error('Fatal error during testing:', error);
        process.exit(1);
    });
}

module.exports = { runTests };
