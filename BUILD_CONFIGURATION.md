# AiElon FusionHD - Build Configuration

This document provides detailed information about the build configuration for iOS TestFlight and Android Play Store deployment.

## Configuration Files

### 1. app.json

The `app.json` file contains the core Expo configuration:

- **name**: "AiElon FusionHD" - Display name of the app
- **slug**: "aielon-fusionhd" - URL-friendly identifier
- **version**: "1.0.0" - App version
- **platforms**: ["ios", "android", "web"] - Supported platforms

#### iOS Configuration
- **bundleIdentifier**: `com.aielon.fusionhd`
- **buildNumber**: "1"
- **supportsTablet**: true

#### Android Configuration
- **package**: `com.aielon.fusionhd`
- **versionCode**: 1

### 2. eas.json

The `eas.json` file configures Expo Application Services (EAS) builds:

#### Build Profiles

**Development**
- For development builds with debugging enabled
- Distribution: internal

**Preview**
- For internal testing before production
- iOS: Real device testing (simulator: false)
- Android: APK format for easy distribution

**Production**
- For App Store/Play Store submission
- iOS: Release build configuration
- Android: App Bundle (AAB) format

#### Submit Configuration

**iOS**
- Requires Apple ID, App Store Connect App ID, and Apple Team ID
- These need to be configured before submission

**Android**
- Requires service account key JSON file
- Track: internal (can be changed to alpha, beta, or production)

## Prerequisites for Building

### iOS Build Requirements

1. **Apple Developer Account**
   - Active Apple Developer Program membership ($99/year)
   - Access to App Store Connect

2. **Credentials**
   - Apple ID
   - App Store Connect App ID
   - Apple Team ID
   - Provisioning profile and certificates (managed by EAS)

3. **App Store Connect Setup**
   - Create app listing in App Store Connect
   - Configure app information, screenshots, etc.

### Android Build Requirements

1. **Google Play Console Account**
   - One-time registration fee ($25)
   - Access to Google Play Console

2. **Service Account**
   - Create service account in Google Cloud Console
   - Download service account key JSON
   - Grant necessary permissions in Play Console

3. **Play Console Setup**
   - Create app in Play Console
   - Configure store listing, content rating, etc.

## Build Commands

### First-time Setup

```bash
# Install EAS CLI globally
npm install -g eas-cli

# Login to Expo account
eas login

# Configure project
eas build:configure
```

### Building

```bash
# Build for iOS (production)
eas build --platform ios --profile production

# Build for Android (production)
eas build --platform android --profile production

# Build for both platforms
eas build --platform all --profile production
```

### Preview Builds

```bash
# iOS preview (for internal testing)
eas build --platform ios --profile preview

# Android preview (generates APK)
eas build --platform android --profile preview
```

### Submit to Stores

```bash
# Submit to App Store
eas submit --platform ios --profile production

# Submit to Play Store
eas submit --platform android --profile production
```

## Build Process

1. **Code Preparation**
   - Ensure all code is committed
   - Update version in app.json if needed
   - Test locally on all target platforms

2. **Build**
   - Run EAS build command
   - Wait for build to complete (usually 10-20 minutes)
   - Download build artifact if needed

3. **Testing**
   - For iOS: Use TestFlight for internal/external testing
   - For Android: Use internal testing track or closed testing

4. **Submission**
   - Prepare store assets (screenshots, descriptions, etc.)
   - Submit for review
   - Monitor review status

## Updating Credentials

### iOS

Update credentials in `eas.json`:
```json
"ios": {
  "appleId": "your-apple-id@example.com",
  "ascAppId": "your-app-store-connect-app-id",
  "appleTeamId": "your-apple-team-id"
}
```

### Android

1. Place service account key JSON in project
2. Update path in `eas.json`:
```json
"android": {
  "serviceAccountKeyPath": "./path/to/service-account-key.json",
  "track": "internal"
}
```

## Version Management

### Updating Version

When releasing a new version:

1. **Update app.json**:
   - Increment `version` (e.g., "1.0.0" → "1.0.1")
   - iOS: Increment `ios.buildNumber`
   - Android: Increment `android.versionCode`

2. **Commit changes**:
   ```bash
   git add app.json
   git commit -m "Bump version to X.X.X"
   git push
   ```

3. **Build and submit**:
   ```bash
   eas build --platform all --profile production
   ```

## Troubleshooting

### Common Issues

1. **Build fails with credentials error**
   - Solution: Run `eas credentials` to configure credentials

2. **Asset loading errors**
   - Solution: Ensure all assets exist in `app/assets/`
   - Run `expo start` locally to verify

3. **Dependency conflicts**
   - Solution: Delete `node_modules` and reinstall
   ```bash
   rm -rf node_modules
   npm install
   ```

4. **iOS build fails**
   - Check Apple Developer account status
   - Verify certificates and provisioning profiles
   - Run `eas credentials` to reset if needed

5. **Android build fails**
   - Verify package name matches Google Play Console
   - Check service account permissions
   - Ensure keystore is properly configured

## Additional Resources

- [Expo Documentation](https://docs.expo.dev/)
- [EAS Build Documentation](https://docs.expo.dev/build/introduction/)
- [EAS Submit Documentation](https://docs.expo.dev/submit/introduction/)
- [App Store Guidelines](https://developer.apple.com/app-store/guidelines/)
- [Google Play Guidelines](https://play.google.com/console/about/guides/releasewithconfidence/)
