/**
 * AiElon Living OS - System Configuration
 * Version: 2.0.0
 */

module.exports = {
    // Core OS Configuration
    core: {
        version: '2.0.0',
        security: {
            enabled: true,
            level: 'high',
            encryption: 'AES-256-GCM',
            authentication: 'multi-factor'
        },
        compatibility: {
            platforms: ['linux', 'darwin', 'win32', 'android', 'ios', 'web'],
            optimized: true
        }
    },

    // Blockchain Configuration
    blockchain: {
        networkId: 338,
        chainName: 'AielonChain338',
        rpcEndpoint: process.env.AIELONCHAIN_RPC || 'https://rpc.aielonchain338.network',
        wsEndpoint: process.env.AIELONCHAIN_WS || 'wss://ws.aielonchain338.network',
        gasLimit: 21000,
        confirmations: 6
    },

    // Fusion HD UI Configuration
    ui: {
        version: '2.0.0',
        defaultTheme: 'light',
        themes: ['light', 'dark', 'islamic'],
        resolution: 'HD',
        responsive: true,
        accessibility: true
    },

    // Halal Wallet Configuration
    wallet: {
        version: '2.0.0',
        shariahCompliance: true,
        security: {
            encryption: true,
            multiSig: true,
            biometric: true,
            twoFactor: true,
            coldStorage: true
        },
        zakat: {
            enabled: true,
            threshold: 85, // grams of gold equivalent
            rate: 0.025    // 2.5%
        },
        features: {
            autoZakatCalculation: true,
            shariahScreening: true,
            ethicalInvestment: true
        }
    },

    // HCare System Configuration
    hcare: {
        version: '2.0.0',
        privacy: {
            enabled: true,
            hipaaCompliant: true,
            gdprCompliant: true,
            encryption: 'AES-256-GCM'
        },
        features: {
            telemedicine: true,
            healthMonitoring: true,
            appointmentScheduling: true,
            medicationTracking: true,
            labResults: true
        },
        storage: {
            type: 'encrypted',
            retention: '7years',
            backup: true
        }
    },

    // Ummah Hub Configuration
    ummahHub: {
        version: '2.0.0',
        moderation: {
            enabled: true,
            autoFilter: true,
            islamicValues: true,
            reportSystem: true
        },
        security: {
            encryption: 'end-to-end',
            privacyControls: true,
            verifiedAccounts: true
        },
        features: {
            messaging: true,
            communities: true,
            prayerTimes: true,
            islamicCalendar: true,
            educationalContent: true
        }
    },

    // Server Configuration
    server: {
        port: process.env.PORT || 3000,
        host: process.env.HOST || '0.0.0.0',
        environment: process.env.NODE_ENV || 'development',
        cors: {
            enabled: true,
            origins: ['*']
        }
    },

    // Logging Configuration
    logging: {
        level: process.env.LOG_LEVEL || 'info',
        format: 'json',
        destination: 'console'
    }
};
