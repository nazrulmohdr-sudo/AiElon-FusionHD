# AiElon FusionHD - Expo Application

This is the main Expo application for the AiElon FusionHD project, providing a comprehensive ecosystem for Living OS, Fusion HD UI, Halal Wallet, HCare, and Ummah Hub.

## 📁 Project Structure

```
aielon-app/
├── App.js                 # Main application entry point
├── app.json              # Expo configuration
├── package.json          # Dependencies and scripts
├── eas.json              # EAS Build configuration
├── assets/               # Static assets (icons, images, fonts)
├── components/           # Reusable UI components
│   ├── Header.js
│   ├── Button.js
│   └── index.js
├── screens/              # Application screens
│   ├── HomeScreen.js
│   ├── AboutScreen.js
│   └── index.js
├── navigation/           # Navigation configuration
│   ├── AppNavigator.js
│   └── index.js
├── utils/                # Utility functions
│   ├── helpers.js
│   └── index.js
└── theme/                # Theme constants and styling
    ├── colors.js
    └── index.js
```

## 🚀 Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- EAS CLI (`npm install -g eas-cli`)

### Installation

1. Navigate to the app directory:
   ```bash
   cd aielon-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

### Running the App

- **iOS Simulator**: `npm run ios`
- **Android Emulator**: `npm run android`
- **Web Browser**: `npm run web`

## 📱 Building for Production

### iOS (TestFlight)

1. Configure your Apple Developer account in `eas.json`
2. Build for iOS:
   ```bash
   npm run build:ios
   ```
3. Submit to TestFlight:
   ```bash
   npm run submit:ios
   ```

### Android (Play Store)

1. Configure your Google Play service account in `eas.json`
2. Build for Android:
   ```bash
   npm run build:android
   ```
3. Submit to Play Store:
   ```bash
   npm run submit:android
   ```

## 🔧 Configuration

### App Metadata

Edit `app.json` to customize:
- App name and slug
- Bundle identifiers
- App icons and splash screens
- Version numbers

### Build Settings

Edit `eas.json` to configure:
- Development builds
- Preview builds
- Production builds
- Submission settings

## 📦 Dependencies

- **expo**: ~50.0.0
- **react**: 18.2.0
- **react-native**: 0.73.0
- **@react-navigation/native**: ^6.1.9
- **@react-navigation/native-stack**: ^6.9.17

## 🎨 Theming

The app uses a centralized theme system located in the `theme/` directory:
- Colors
- Spacing
- Font sizes
- Border radius
- Shadows

## 🧩 Components

Reusable components are located in the `components/` directory:
- **Header**: Page header component
- **Button**: Customizable button with variants

## 📄 Screens

Main application screens:
- **HomeScreen**: Main landing screen with app features
- **AboutScreen**: Information about the app and its components

## 🧭 Navigation

The app uses React Navigation with a native stack navigator for iOS and Android navigation patterns.

## 🛠️ Utilities

Helper functions are available in the `utils/` directory:
- Date formatting
- Email validation
- ID generation
- Text truncation

## 🔗 Integration with PRs

This structure is designed to integrate seamlessly with:
- **PR #33**: Additional modules
- **PR #34**: Orchestrator logic

## 📝 Next Steps

1. Add your app assets (icons, splash screens) to the `assets/` directory
2. Configure your Apple Developer and Google Play accounts
3. Customize the theme to match your brand
4. Add additional screens and components as needed
5. Implement business logic and API integrations

## 📚 Documentation

- [Expo Documentation](https://docs.expo.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [React Navigation Documentation](https://reactnavigation.org/)
- [EAS Build Documentation](https://docs.expo.dev/build/introduction/)

## 🤝 Contributing

Please ensure all changes follow the existing code structure and style guidelines.

## 📄 License

Copyright © 2024 AiElon FusionHD
