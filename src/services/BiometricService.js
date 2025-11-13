/**
 * Biometric Sync Service
 * Handles biometric authentication and security
 */

import * as LocalAuthentication from 'expo-local-authentication';

class BiometricService {
  constructor() {
    this.isAvailable = false;
    this.biometricType = null;
    this.isEnrolled = false;
  }

  /**
   * Check if biometric authentication is available
   */
  async checkAvailability() {
    try {
      const compatible = await LocalAuthentication.hasHardwareAsync();
      const enrolled = await LocalAuthentication.isEnrolledAsync();
      const types = await LocalAuthentication.supportedAuthenticationTypesAsync();

      this.isAvailable = compatible;
      this.isEnrolled = enrolled;
      this.biometricType = this.getBiometricTypeName(types);

      return {
        success: true,
        available: compatible,
        enrolled: enrolled,
        types: this.biometricType,
      };
    } catch (error) {
      console.error('Biometric check error:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Authenticate user with biometrics
   */
  async authenticate(promptMessage = 'Authenticate to continue') {
    try {
      const result = await LocalAuthentication.authenticateAsync({
        promptMessage,
        fallbackLabel: 'Use Passcode',
        disableDeviceFallback: false,
      });

      return {
        success: result.success,
        authenticated: result.success,
        error: result.error,
      };
    } catch (error) {
      console.error('Biometric authentication error:', error);
      return { success: false, error: error.message };
    }
  }

  /**
   * Get biometric type name
   */
  getBiometricTypeName(types) {
    if (!types || types.length === 0) return 'None';
    
    const typeMap = {
      1: 'Fingerprint',
      2: 'Face Recognition',
      3: 'Iris',
    };

    return types.map(type => typeMap[type] || 'Unknown').join(', ');
  }

  /**
   * Simulate biometric enrollment
   */
  async enrollBiometric() {
    try {
      // In a real app, this would guide the user through enrollment
      await this.simulateDelay(2000);
      this.isEnrolled = true;
      return {
        success: true,
        message: 'Biometric enrolled successfully',
      };
    } catch (error) {
      return { success: false, error: error.message };
    }
  }

  /**
   * Simulate async delay
   */
  simulateDelay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

export default new BiometricService();
