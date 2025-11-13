# AIELON-FUSIONHD Setup and Integration Guide

## Quick Start Guide

### Step 1: Installation

```bash
# Clone the repository
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD

# Install dependencies
npm install
```

### Step 2: Start the Development Server

```bash
npm start
# or
expo start
```

### Step 3: Run on Your Device

#### Option A: Using Expo Go (Easiest)
1. Install Expo Go app on your phone:
   - iOS: https://apps.apple.com/app/expo-go/id982107779
   - Android: https://play.google.com/store/apps/details?id=host.exp.exponent

2. Scan the QR code shown in terminal/browser
3. The app will load on your device

#### Option B: Using Emulator/Simulator
```bash
# For iOS (macOS only)
npm run ios

# For Android
npm run android

# For Web
npm run web
```

## Features Overview

### 1. Home Dashboard
- Overview of all modules
- Quick access to main features
- System status indicators
- Module initialization

### 2. Wallet Management
- Connect AIELON wallet
- View balance and transactions
- Blockchain synchronization
- Biometric authentication for security

### 3. NFT Platform
- View your NFT collection
- Mint new NFTs
- Browse collections
- Manage NFT metadata

### 4. DApp Integration
- Connect to decentralized apps
- Unified interface for multiple dApps
- Fusion mode for seamless integration
- Session management

### 5. Cross-Chain Trading
- Bridge assets between chains
- Trade cryptocurrency pairs
- View real-time price feeds
- Track trading history

### 6. Healthcare (HCARE)
- Manage health profile
- Book medical appointments
- Track health metrics
- Personalized recommendations

### 7. Security Center
- Biometric authentication
- Security audits
- Encrypted storage
- Threat monitoring

### 8. Settings
- App configuration
- Network settings
- Security preferences
- Account management

## App Architecture

### Services Layer
All business logic is organized in modular services:

```
src/services/
├── BlockchainService.js    # AIELONCHAIN338 integration
├── BiometricService.js     # Biometric authentication
├── OracleService.js        # Price feeds and data
├── NFTService.js           # NFT operations
├── WalletConnectService.js # Wallet connections
├── Trade138Service.js      # Trading and bridging
├── HCareService.js         # Healthcare management
├── SecurityService.js      # Security features
├── DAppFusionService.js    # DApp integration
└── FusionCoreService.js    # Central coordinator
```

### UI Components
Reusable components for consistent design:

```
src/components/
├── Card.js          # Container component
├── Button.js        # Action buttons
└── StatusBadge.js   # Status indicators
```

### Screens/Pages
Main app screens:

```
src/pages/
├── HomeScreen.js       # Main dashboard
├── WalletScreen.js     # Wallet management
├── NFTScreen.js        # NFT platform
├── DAppsScreen.js      # DApp browser
├── HCareScreen.js      # Healthcare
├── SettingsScreen.js   # Settings
├── BlockchainScreen.js # Blockchain info
├── TradeScreen.js      # Trading
└── SecurityScreen.js   # Security center
```

## Integration Guide

### Adding New Features

#### 1. Create a New Service

```javascript
// src/services/MyNewService.js
class MyNewService {
  constructor() {
    // Initialize state
  }

  async initialize() {
    // Setup logic
    return { success: true };
  }

  async myMethod() {
    // Your logic here
    return { success: true, data: {} };
  }
}

export default new MyNewService();
```

#### 2. Add to Fusion Core

```javascript
// src/services/FusionCoreService.js
import MyNewService from './MyNewService';

// Add to modules object
this.modules = {
  // ... existing modules
  myNew: MyNewService,
};

// Add to initialization
async initializeAll() {
  const results = await Promise.all([
    // ... existing
    this.modules.myNew.initialize(),
  ]);
}
```

#### 3. Create a Screen

```javascript
// src/pages/MyNewScreen.js
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Card, Button } from '../components';
import { COLORS, SPACING } from '../constants';
import { MyNewService } from '../services';

export default function MyNewScreen() {
  const [data, setData] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const result = await MyNewService.myMethod();
    if (result.success) {
      setData(result.data);
    }
  };

  return (
    <View style={styles.container}>
      <Card title="My New Feature">
        <Text>Content here</Text>
      </Card>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background,
  },
});
```

#### 4. Add to Navigation

```javascript
// src/navigation/AppNavigator.js
import MyNewScreen from '../pages/MyNewScreen';

// Add to Stack screens
<Stack.Screen name="MyNew" component={MyNewScreen} />
```

### Connecting to Real Blockchain

To connect to actual blockchain networks:

1. **Install Web3 libraries**:
```bash
npm install web3 @walletconnect/web3-provider
```

2. **Update BlockchainService.js**:
```javascript
import Web3 from 'web3';

class BlockchainService {
  async connectWallet() {
    const web3 = new Web3('https://rpc.aielon.io');
    // Real connection logic
  }
}
```

3. **Update configuration**:
```javascript
// src/constants/index.js
export const APP_CONFIG = {
  apiUrl: 'https://api.aielon.io',
  rpcUrl: 'https://rpc.aielon.io',
  chainId: 338,
};
```

### Security Best Practices

1. **Never commit private keys**
2. **Use environment variables** for sensitive data
3. **Enable biometric authentication** for critical operations
4. **Validate all user inputs**
5. **Use HTTPS** for all API calls
6. **Implement proper error handling**

## Testing

### Manual Testing Checklist

- [ ] App launches successfully
- [ ] Navigation works between all screens
- [ ] Module initialization completes
- [ ] Wallet connection simulates correctly
- [ ] NFT minting and viewing works
- [ ] DApp connections function
- [ ] Trading interface is responsive
- [ ] Healthcare features load
- [ ] Security features work
- [ ] Settings can be modified

### Device Testing

Test on multiple devices and orientations:
- iOS devices (iPhone, iPad)
- Android devices (various screen sizes)
- Different iOS/Android versions

## Troubleshooting

### Common Issues

**Issue: App won't start**
```bash
# Clear cache and reinstall
rm -rf node_modules
npm install
npm start -- --clear
```

**Issue: Navigation not working**
```bash
# Ensure navigation packages are installed
npx expo install @react-navigation/native @react-navigation/stack @react-navigation/bottom-tabs
```

**Issue: Biometric not working**
```bash
# Make sure the package is installed
npx expo install expo-local-authentication
```

**Issue: Build errors**
```bash
# Check Expo SDK compatibility
npx expo install --check
```

## Production Deployment

### Building for iOS

```bash
# Install EAS CLI
npm install -g eas-cli

# Login to Expo
eas login

# Configure build
eas build:configure

# Build for iOS
eas build --platform ios
```

### Building for Android

```bash
# Build for Android
eas build --platform android
```

### Publishing Updates

```bash
# Publish OTA update
eas update --branch production
```

## Environment Configuration

Create a `.env` file for environment variables:

```env
# API Configuration
API_URL=https://api.aielon.io
RPC_URL=https://rpc.aielon.io
CHAIN_ID=338

# Feature Flags
ENABLE_BIOMETRIC=true
ENABLE_NOTIFICATIONS=true
```

## Performance Optimization

1. **Use React.memo** for expensive components
2. **Implement lazy loading** for screens
3. **Optimize images** and assets
4. **Use FlatList** for long lists
5. **Minimize re-renders**

## Support and Resources

- **Documentation**: Check README.md
- **Issues**: GitHub Issues
- **Expo Docs**: https://docs.expo.dev
- **React Native Docs**: https://reactnative.dev

## Next Steps

1. Test the app thoroughly
2. Connect to real blockchain networks
3. Implement actual API integrations
4. Add push notifications
5. Implement analytics
6. Submit to app stores
7. Gather user feedback
8. Iterate and improve

## License

MIT License - See LICENSE file for details
