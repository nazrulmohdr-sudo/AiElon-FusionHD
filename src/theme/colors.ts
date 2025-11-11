/**
 * AiElon Premium - Dark Royal Gold Theme
 * Reflecting prestige, trust (Amanah), and premium quality
 */

export const colors = {
  // Primary Colors - Royal Gold
  primary: {
    gold: '#D4AF37',        // Main royal gold
    lightGold: '#F4E4B7',   // Light gold accent
    darkGold: '#B8941F',    // Deep gold
    richGold: '#FFD700',    // Rich gold highlight
  },

  // Secondary Colors - Dark Royal
  secondary: {
    darkNavy: '#0A0A0A',    // Deep dark background
    royalBlue: '#1A1A2E',   // Royal dark blue
    charcoal: '#16213E',    // Charcoal accent
    midnight: '#0F0F1E',    // Midnight dark
  },

  // Neutral Colors
  neutral: {
    white: '#FFFFFF',
    offWhite: '#F5F5F5',
    lightGray: '#E0E0E0',
    gray: '#9E9E9E',
    darkGray: '#424242',
    black: '#000000',
  },

  // Semantic Colors
  success: '#4CAF50',
  warning: '#FFA726',
  error: '#EF5350',
  info: '#29B6F6',

  // Background Colors
  background: {
    primary: '#0A0A0A',     // Main background
    secondary: '#1A1A2E',   // Card background
    tertiary: '#16213E',    // Section background
  },

  // Text Colors
  text: {
    primary: '#FFFFFF',      // Main text
    secondary: '#E0E0E0',    // Secondary text
    tertiary: '#9E9E9E',     // Tertiary text
    gold: '#D4AF37',         // Gold text for emphasis
    disabled: '#616161',     // Disabled text
  },

  // Border Colors
  border: {
    primary: '#D4AF37',      // Gold border
    secondary: '#424242',    // Dark border
    light: '#616161',        // Light border
  },
};

export type Colors = typeof colors;
