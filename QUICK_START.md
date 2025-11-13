# Quick Launch Instructions

## 🚀 Launch AIELON-FUSIONHD in 5 Minutes

### Prerequisites Check
Before you begin, ensure you have:
- ✅ Node.js (v14+) installed
- ✅ npm or yarn installed
- ✅ Expo Go app on your phone (optional but recommended)

### Step 1: Get the Code
```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
```

### Step 2: Install Dependencies
```bash
npm install
```

This will install all required packages including:
- Expo SDK
- React Navigation
- Biometric authentication
- Security modules
- All app dependencies

### Step 3: Start the App
```bash
npm start
```

You'll see a QR code and options to launch on:
- Press `i` for iOS simulator
- Press `a` for Android emulator  
- Press `w` for web browser
- Scan QR with Expo Go app on your phone

### Step 4: Explore the App

The app will launch with the following screens accessible via bottom tabs:

1. **Home** - Main dashboard with module overview
2. **Wallet** - Connect and manage your AIELON wallet
3. **NFT** - View and mint NFTs
4. **DApps** - Browse and connect to decentralized apps
5. **HCare** - Healthcare management system

Additional screens via navigation:
- **Settings** - App configuration
- **Blockchain** - Network information
- **Trade** - Cross-chain trading
- **Security** - Security center

## 🎯 First-Time User Flow

### 1. Initialize the System
On first launch:
1. Open the Home screen
2. Tap "Initialize All Modules"
3. Wait for all services to initialize
4. You'll see green status indicators when ready

### 2. Connect Your Wallet
1. Navigate to the Wallet tab
2. Tap "Connect Wallet"
3. Authenticate with biometric (if available)
4. Your simulated wallet will be connected
5. View your balance and address

### 3. Explore NFTs
1. Navigate to the NFT tab
2. View sample NFTs in your collection
3. Tap "Mint New NFT" to create a test NFT
4. Switch to Collections tab to browse available collections

### 4. Try DApp Fusion
1. Navigate to the DApps tab
2. Browse available decentralized applications
3. Tap "Connect" on any dApp
4. See your connected dApps in the list

### 5. Test Cross-Chain Bridge
1. Navigate to Trade screen (from Home → Trade)
2. Select source and destination chains
3. Enter an amount
4. Tap "Bridge Transfer"
5. Confirm the simulated transaction

### 6. Check Healthcare Features
1. Navigate to the HCare tab
2. View your health profile and score
3. Tap "Book Appointment" to schedule
4. Explore health recommendations

### 7. Run Security Audit
1. Navigate to Settings → Security Audit
2. Or go directly to Security screen
3. Tap "Run Security Audit"
4. View your security score and recommendations

## 📱 Testing on Physical Device

### iOS (Using Expo Go)
1. Install Expo Go from App Store
2. Open Expo Go app
3. Scan QR code from terminal
4. App loads on your iPhone/iPad

### Android (Using Expo Go)
1. Install Expo Go from Play Store
2. Open Expo Go app
3. Scan QR code from terminal
4. App loads on your Android device

## 🔧 Troubleshooting

### Issue: "Unable to resolve module"
```bash
# Clear cache and restart
npm start -- --clear
```

### Issue: QR code not appearing
```bash
# Restart with reset cache
rm -rf .expo
npm start
```

### Issue: Biometric not working
- Biometrics only work on physical devices
- Ensure device has biometric hardware
- Grant biometric permissions when prompted

### Issue: App crashes on launch
```bash
# Reinstall dependencies
rm -rf node_modules
npm install
npm start
```

## 🎨 Customization Quick Tips

### Change App Colors
Edit `src/constants/index.js`:
```javascript
export const COLORS = {
  primary: '#1a1a2e',      // Your primary color
  secondary: '#16213e',    // Your secondary color
  highlight: '#00d4ff',    // Accent color
  // ... more colors
};
```

### Add New Features
1. Create service in `src/services/`
2. Create screen in `src/pages/`
3. Add to navigation in `src/navigation/AppNavigator.js`
4. Initialize in `FusionCoreService.js`

### Modify Branding
Edit `app.json`:
```json
{
  "expo": {
    "name": "Your App Name",
    "slug": "your-app-slug",
    "description": "Your app description"
  }
}
```

## 📊 App Structure Overview

```
AIELON-FUSIONHD/
│
├── src/
│   ├── components/      # Reusable UI components
│   ├── pages/           # App screens
│   ├── services/        # Business logic (9 modules)
│   ├── navigation/      # Navigation setup
│   └── constants/       # App configuration
│
├── App.js              # Entry point
├── app.json            # Expo configuration
└── package.json        # Dependencies
```

## 🔐 Security Notes

- All blockchain operations are **simulated**
- No real transactions are made
- Biometric auth is for demo purposes
- Data is stored locally on device
- No external API calls in demo mode

## 🚀 Next Steps

1. ✅ Launch and explore the app
2. ✅ Test all features and screens
3. ✅ Understand the architecture
4. ✅ Read SETUP_GUIDE.md for integration
5. ✅ Connect to real blockchain (optional)
6. ✅ Customize for your needs
7. ✅ Deploy to app stores

## 📚 Additional Resources

- **Full Setup Guide**: See SETUP_GUIDE.md
- **README**: See README.md
- **Expo Docs**: https://docs.expo.dev
- **React Navigation**: https://reactnavigation.org

## ✨ Features Summary

✅ 9 Integrated Modules
✅ Biometric Security
✅ NFT Platform
✅ DApp Browser
✅ Cross-Chain Bridge
✅ Healthcare System
✅ Wallet Management
✅ Real-time Market Data
✅ Security Auditing
✅ Unified Interface

## 🎉 Success Indicators

You've successfully launched when you see:
- ✅ App loads without errors
- ✅ Bottom navigation is visible
- ✅ Home screen shows module status
- ✅ All tabs are accessible
- ✅ Module initialization works
- ✅ No red error screens

## 💡 Pro Tips

1. **Enable Fast Refresh**: Automatically updates code changes
2. **Use Debug Menu**: Shake device or Cmd+D (iOS) / Cmd+M (Android)
3. **Check Logs**: View console.log output in terminal
4. **Hot Reload**: Save files to see changes instantly
5. **Test on Real Device**: Best experience vs simulator

## 🆘 Need Help?

- Check console logs in terminal
- Look for error messages in app
- Review SETUP_GUIDE.md for details
- Check GitHub issues
- Verify all dependencies installed

---

**Ready to Launch? Run: `npm start`** 🚀
