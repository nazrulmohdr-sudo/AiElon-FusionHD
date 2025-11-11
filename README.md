# AiElon-FusionHD

AiElon Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub

## Overview

AiElon Premium is a React Native Expo application featuring a Dark Royal Gold theme that reflects prestige and Amanah (trust) values. The application provides premium services including:

- **Halal Wallet**: Shariah-compliant financial management
- **HCare**: Healthcare services with trust and excellence
- **Ummah Hub**: Global Muslim community connection platform

## Design Philosophy

Built on the principles of **Amanah** (trust, integrity, and responsibility), this application features:

- **Dark Royal Gold Theme**: Premium dark background with royal gold accents
- **Typography**: Clean, modern typography emphasizing readability
- **Consistent Spacing**: Systematic spacing using design tokens
- **Accessibility**: High contrast and clear visual hierarchy

## Tech Stack

- **React Native** (0.81.5)
- **Expo** (~54.0.23)
- **TypeScript** (~5.9.2)
- **React Navigation** (v7)
- **React** (19.1.0)

## Project Structure

```
/src
  /components     - Reusable UI components
  /screens        - Screen components
    - HomeScreen.tsx
    - WalletScreen.tsx
  /navigation     - Navigation configuration
  /theme          - Design tokens and theme configuration
    - colors.ts
    - typography.ts
    - spacing.ts
    - index.ts
```

## Getting Started

### Prerequisites

- Node.js (v20+)
- npm or yarn
- Expo CLI

### Installation

```bash
# Install dependencies
npm install

# Start the development server
npm start
```

### Running the App

```bash
# Run on Android
npm run android

# Run on iOS (macOS only)
npm run ios

# Run on Web
npm run web
```

## Theme Configuration

The app uses a comprehensive design system with the following color palette:

### Primary Colors (Royal Gold)
- Main Gold: `#D4AF37`
- Light Gold: `#F4E4B7`
- Dark Gold: `#B8941F`
- Rich Gold: `#FFD700`

### Secondary Colors (Dark Royal)
- Dark Navy: `#0A0A0A`
- Royal Blue: `#1A1A2E`
- Charcoal: `#16213E`
- Midnight: `#0F0F1E`

## Screens

### HomeScreen
Main landing screen showcasing:
- AiElon branding
- Service cards for Wallet, HCare, and Ummah Hub
- Amanah trust statement

### WalletScreen
Halal Wallet interface featuring:
- Balance display with Halal verification
- Transaction actions (Send, Receive, Analytics)
- Quick stats overview
- Shariah-compliance features
- Amanah trust principles

## Navigation

Pre-configured React Navigation with stack navigator:
- Home → Wallet navigation
- Back navigation support
- Dark theme integration

## Development Guidelines

### Adding New Screens
1. Create screen component in `/src/screens`
2. Add route to `/src/navigation/types.ts`
3. Register screen in `/src/navigation/RootNavigator.tsx`
4. Export from `/src/screens/index.ts`

### Using Theme
```typescript
import { theme } from '../theme';

// Access colors
const goldColor = theme.colors.primary.gold;

// Access spacing
const padding = theme.spacing.lg;

// Access typography
const fontSize = theme.typography.fontSize.xl;
```

## Contributing

Please ensure all contributions:
- Follow the established design system
- Maintain TypeScript type safety
- Adhere to Amanah principles (trust, transparency, responsibility)
- Use the Dark Royal Gold theme consistently

## License

Proprietary - AiElon Premium Services

## Support

For questions or support, please contact the AiElon development team.

