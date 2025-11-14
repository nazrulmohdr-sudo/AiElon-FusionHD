# AiElon FusionHD

AiElon Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub

## Overview

AiElon FusionHD is a comprehensive mobile application built with Expo and React Native, providing an all-in-one platform for:
- AiElon Living OS
- Fusion HD UI
- Halal Wallet
- HCare
- Ummah Hub

## Prerequisites

- Node.js (v18 or later)
- npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- EAS CLI (`npm install -g eas-cli`)

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
```

2. Install dependencies:
```bash
npm install
```

### Running the App

Start the development server:
```bash
npm start
```

Run on specific platforms:
```bash
npm run android  # Android
npm run ios      # iOS
npm run web      # Web
```

## Building for Production

### iOS (TestFlight)

1. Configure your Apple credentials in `eas.json`
2. Build for iOS:
```bash
eas build --platform ios --profile production
```

### Android (Play Store)

1. Configure your Google Play credentials in `eas.json`
2. Build for Android:
```bash
eas build --platform android --profile production
```

## Project Structure

```
AiElon-FusionHD/
├── App.js                  # Main entry point
├── app.json                # Expo configuration
├── eas.json                # EAS Build configuration
├── package.json            # Dependencies
├── babel.config.js         # Babel configuration
├── app/
│   ├── assets/            # Images, fonts, and static resources
│   ├── components/        # Reusable UI components
│   ├── navigation/        # Navigation configuration
│   └── screens/           # Screen components
│       ├── HomeScreen.js
│       └── AboutScreen.js
```

## Configuration

### App Identifiers

- **iOS Bundle ID**: `com.aielon.fusionhd`
- **Android Package**: `com.aielon.fusionhd`

### Build Profiles

The app includes three build profiles in `eas.json`:
- **development**: For development builds with debugging
- **preview**: For internal testing (APK for Android, simulator for iOS)
- **production**: For App Store/Play Store submission

## Contributing

Please follow the standard Git workflow:
1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

Copyright © 2024 AiElon. All rights reserved.
