# AiElon FusionHD

**AiElon Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub**

A modern React Native + Expo mobile application with TypeScript, featuring a stunning Dark Royal Gold theme and a modular dashboard layout.

## 🌟 Features

- **Dark Royal Gold Theme**: Elegant dark purple background with luxurious gold accents
- **Dashboard Layout**: Four main module buttons (Trade, Bank, HCare, Me)
- **Navigation Stack**: Seamless navigation between screens using React Navigation
- **Halal Wallet**: Digital banking solution with balance display and transaction history
- **TypeScript Support**: Full TypeScript integration for type safety
- **Responsive Design**: Works on iOS, Android, and Web
- **Scalable Architecture**: Modular folder structure ready for future expansion

## 📱 Screenshots

### Home Screen (Dashboard)
![Home Screen](https://github.com/user-attachments/assets/d21a6265-1d4d-4b0c-b819-1b4bd269e579)

### Wallet Screen
![Wallet Screen](https://github.com/user-attachments/assets/5935a4f1-01d7-41a6-941f-2aa61caa15c5)

## 🚀 Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Expo CLI (optional, but recommended)

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

#### Development Mode

Start the Expo development server:
```bash
npm start
```

This will open Expo DevTools. You can then:
- Scan the QR code with the Expo Go app on your mobile device
- Press `w` to open in web browser
- Press `a` to open Android emulator
- Press `i` to open iOS simulator (macOS only)

#### Platform-Specific Commands

```bash
# Run on Android
npm run android

# Run on iOS (macOS only)
npm run ios

# Run on Web
npm run web
```

### Building for Production

#### Web Build
```bash
npx expo export --platform web --output-dir web-build
```

#### Native Builds
For native iOS and Android builds, use EAS Build:
```bash
npx eas build --platform android
npx eas build --platform ios
```

## 📁 Project Structure

```
AiElon-FusionHD/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── AiButton.tsx    # Custom button component
│   │   └── index.ts
│   ├── screens/             # Application screens
│   │   ├── HomeScreen.tsx  # Dashboard with 4 main buttons
│   │   ├── WalletScreen.tsx # Halal Wallet screen
│   │   └── index.ts
│   └── theme/               # Theme configuration
│       ├── colors.ts        # Dark Royal Gold color palette
│       └── index.ts         # Typography, spacing, shadows
├── assets/                  # Images, icons, fonts
├── App.tsx                  # Main app component with navigation
├── index.ts                 # App entry point
├── app.json                 # Expo configuration
├── package.json             # Dependencies
└── tsconfig.json            # TypeScript configuration
```

## 🎨 Theme

### Color Palette

- **Background**: Deep royal purple (`#1a0f2e`)
- **Surface**: Lighter royal purple (`#2a1f4e`)
- **Primary**: Royal gold (`#d4af37`)
- **Text**: White (`#ffffff`)
- **Accents**: Various shades of purple and gold

### Design Philosophy

- **Minimalistic**: Clean, uncluttered layouts
- **Elegant**: Rounded corners and smooth shadows
- **Accessible**: High contrast for readability
- **Modern**: Contemporary UI patterns

## 🛠️ Technology Stack

- **React Native**: Cross-platform mobile framework
- **Expo**: Development platform and tools
- **TypeScript**: Type-safe JavaScript
- **React Navigation**: Navigation library
- **React Native Gesture Handler**: Touch gesture handling
- **React Native Screens**: Native screen optimization

## 🔮 Future Modules

The app is designed to be scalable with planned modules:

- **Trade**: Cryptocurrency and stock trading
- **Bank**: Full banking features (Halal Wallet expansion)
- **HCare**: Healthcare management and tracking
- **Me**: User profile and settings

## 📄 License

This project is private and proprietary.

## 👥 Contributors

- nazrulmohdr-sudo

## 🤝 Contributing

This is a private repository. Contact the repository owner for contribution guidelines.
