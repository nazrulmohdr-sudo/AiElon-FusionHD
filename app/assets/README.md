# AiElon FusionHD Assets

This directory contains static assets for the AiElon FusionHD application.

## Required Assets (Placeholders)

The following asset files are referenced in app.json but need to be created:

- `icon.png` - App icon (1024x1024px)
- `splash.png` - Splash screen image (1284x2778px recommended)
- `adaptive-icon.png` - Android adaptive icon (1024x1024px)
- `favicon.png` - Web favicon (48x48px)

## Generating Assets

You can use Expo's asset generation tools or create these manually:

```bash
# After creating a base icon.png file, you can generate all required assets
npx expo-optimize
```

For now, placeholder assets should be created to allow the app to build successfully.
