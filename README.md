# AiElon-FusionHD

**AiElon Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub**

A React Native + Expo application featuring a Dark Royal Gold theme with a dashboard layout for managing Trade, Bank, HCare, and Profile modules.

## 🚀 Features

- **Dark Royal Gold Theme**: Elegant minimalistic design with dark navy and royal gold accents
- **Dashboard Layout**: Four main navigation buttons (Trade, Bank, HCare, Me)
- **Halal Wallet**: Sharia-compliant finance module
- **Navigation Stack**: Seamless navigation between screens using React Navigation
- **Modular Architecture**: Clean folder structure with separate components and screens

## 📁 Project Structure

```
AiElon-FusionHD/
├── App.js                      # Main app component with navigation
├── app.json                    # Expo configuration
├── package.json                # Dependencies
├── babel.config.js             # Babel configuration
├── assets/                     # Images and icons
│   ├── icon.png
│   ├── splash.png
│   ├── adaptive-icon.png
│   └── favicon.png
└── src/
    ├── theme.js                # Dark Royal Gold theme configuration
    ├── components/             # Reusable components
    │   └── DashboardButton.js
    └── screens/                # Screen components
        ├── HomeScreen.js
        ├── WalletScreen.js
        ├── TradeScreen.js
        ├── BankScreen.js
        ├── HCareScreen.js
        └── MeScreen.js
```

## 🛠️ Installation

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Expo CLI (optional but recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
   cd AiElon-FusionHD
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

## 📱 Running the App

### Using Expo Go (Recommended for testing)

1. Install Expo Go on your iOS or Android device
2. Run `npm start` in the project directory
3. Scan the QR code with your device

### iOS Simulator (macOS only)

```bash
npm run ios
```

### Android Emulator

```bash
npm run android
```

### Web Browser

```bash
npm run web
```

## 🎨 Theme Configuration

The app uses a Dark Royal Gold theme defined in `src/theme.js`:

- **Primary Background**: `#1a1a2e` (Deep dark navy)
- **Accent Color**: `#d4af37` (Royal gold)
- **Card Background**: `#0f3460` (Navy blue)
- **Text Colors**: Off-white and gray variants

## 📋 Available Screens

1. **Home Screen** - Dashboard with four main buttons and quick access to Wallet
2. **Wallet Screen** - Halal Wallet with balance display and transaction actions
3. **Trade Screen** - Placeholder for trading functionality
4. **Bank Screen** - Placeholder for banking services
5. **HCare Screen** - Placeholder for healthcare services
6. **Me Screen** - Placeholder for profile and settings

## 🔄 Navigation Flow

```
Home Screen
  ├─> Trade Screen
  ├─> Bank Screen
  ├─> HCare Screen
  ├─> Me Screen
  └─> Wallet Screen
```

## 🚧 Development Status

This is the initial scaffold with core navigation and UI structure. The following modules are ready for implementation:

- [ ] Trade module functionality
- [ ] Bank module functionality
- [ ] HCare module functionality
- [ ] Profile management in Me module
- [ ] Wallet transaction features
- [ ] Authentication system
- [ ] API integration
- [ ] State management (Redux/Context)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For questions or support, please open an issue in the GitHub repository.

---

**Built with ❤️ for the Ummah**
