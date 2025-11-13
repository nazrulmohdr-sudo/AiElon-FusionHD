/**
 * Security Screen
 * Security and biometric management
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { SecurityService, BiometricService } from '../services';

export default function SecurityScreen() {
  const [securityStatus, setSecurityStatus] = useState(null);
  const [biometricInfo, setBiometricInfo] = useState(null);
  const [auditResults, setAuditResults] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadSecurityData();
  }, []);

  const loadSecurityData = async () => {
    setLoading(true);
    try {
      const statusResult = await SecurityService.getSecurityStatus();
      if (statusResult.success) {
        setSecurityStatus(statusResult.status);
      }

      const bioResult = await BiometricService.checkAvailability();
      if (bioResult.success) {
        setBiometricInfo(bioResult);
      }
    } catch (error) {
      console.error('Error loading security data:', error);
    } finally {
      setLoading(false);
    }
  };

  const runSecurityAudit = async () => {
    setLoading(true);
    try {
      const result = await SecurityService.performSecurityAudit();
      if (result.success) {
        setAuditResults(result.audit);
        Alert.alert(
          'Audit Complete',
          `Security Score: ${result.audit.score}/100\nStatus: ${result.audit.status}`
        );
      }
    } catch (error) {
      Alert.alert('Error', error.message);
    } finally {
      setLoading(false);
    }
  };

  const testBiometric = async () => {
    const result = await BiometricService.authenticate('Test biometric authentication');
    if (result.success) {
      Alert.alert('Success', 'Biometric authentication successful!');
    } else {
      Alert.alert('Failed', 'Biometric authentication failed');
    }
  };

  const generateToken = async () => {
    const result = await SecurityService.generateSecureToken();
    if (result.success) {
      Alert.alert(
        'Token Generated',
        `Token: ${result.token.substring(0, 20)}...\nExpires: ${new Date(result.expiresAt).toLocaleString()}`
      );
    }
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Security Status */}
        {securityStatus && (
          <Card title="Security Status">
            <View style={styles.statusHeader}>
              <View style={styles.securityLevel}>
                <Ionicons name="shield-checkmark" size={48} color={COLORS.success} />
                <Text style={styles.levelText}>{securityStatus.level.toUpperCase()}</Text>
              </View>
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Encryption:</Text>
              <StatusBadge
                status={securityStatus.encryptionEnabled ? 'active' : 'error'}
                label={securityStatus.encryptionEnabled ? 'Enabled' : 'Disabled'}
              />
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Secure Storage:</Text>
              <StatusBadge
                status={securityStatus.secureStorageAvailable ? 'active' : 'error'}
                label={securityStatus.secureStorageAvailable ? 'Available' : 'Unavailable'}
              />
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Threats Detected:</Text>
              <Text style={styles.statusValue}>{securityStatus.threats}</Text>
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Last Check:</Text>
              <Text style={styles.statusValue}>
                {new Date(securityStatus.lastSecurityCheck).toLocaleString()}
              </Text>
            </View>
          </Card>
        )}

        {/* Biometric Security */}
        {biometricInfo && (
          <Card title="Biometric Security">
            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Available:</Text>
              <StatusBadge
                status={biometricInfo.available ? 'active' : 'error'}
                label={biometricInfo.available ? 'Yes' : 'No'}
              />
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Enrolled:</Text>
              <StatusBadge
                status={biometricInfo.enrolled ? 'active' : 'error'}
                label={biometricInfo.enrolled ? 'Yes' : 'No'}
              />
            </View>

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Type:</Text>
              <Text style={styles.statusValue}>{biometricInfo.types}</Text>
            </View>

            <Button
              title="Test Biometric"
              onPress={testBiometric}
              variant="outline"
              style={styles.actionButton}
            />
          </Card>
        )}

        {/* Security Actions */}
        <Card title="Security Actions">
          <Button
            title="Run Security Audit"
            onPress={runSecurityAudit}
            loading={loading}
            style={styles.actionButton}
          />
          <Button
            title="Generate Secure Token"
            onPress={generateToken}
            variant="secondary"
            style={styles.actionButton}
          />
          <Button
            title="Refresh Status"
            onPress={loadSecurityData}
            variant="outline"
            style={styles.actionButton}
          />
        </Card>

        {/* Audit Results */}
        {auditResults && (
          <Card title="Last Audit Results">
            <View style={styles.scoreContainer}>
              <Text style={styles.scoreLabel}>Security Score</Text>
              <Text style={styles.scoreValue}>{auditResults.score}/100</Text>
              <StatusBadge status="success" label={auditResults.status} />
            </View>

            <Text style={styles.sectionTitle}>Recommendations:</Text>
            {auditResults.recommendations.map((rec, index) => (
              <View key={index} style={styles.recommendationItem}>
                <Ionicons name="checkmark-circle" size={20} color={COLORS.highlight} />
                <Text style={styles.recommendationText}>{rec}</Text>
              </View>
            ))}

            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Audit Time:</Text>
              <Text style={styles.statusValue}>
                {new Date(auditResults.timestamp).toLocaleString()}
              </Text>
            </View>
          </Card>
        )}

        {/* Security Features */}
        <Card title="Security Features">
          {[
            { icon: 'lock-closed', label: 'End-to-End Encryption', status: 'active' },
            { icon: 'finger-print', label: 'Biometric Authentication', status: 'active' },
            { icon: 'shield-checkmark', label: 'Secure Storage', status: 'active' },
            { icon: 'key', label: 'Token Management', status: 'active' },
            { icon: 'scan', label: 'Threat Detection', status: 'active' },
          ].map((feature, index) => (
            <View key={index} style={styles.featureItem}>
              <View style={styles.featureLeft}>
                <Ionicons name={feature.icon} size={24} color={COLORS.highlight} />
                <Text style={styles.featureLabel}>{feature.label}</Text>
              </View>
              <StatusBadge status={feature.status} label="Active" />
            </View>
          ))}
        </Card>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: SPACING.md,
  },
  statusHeader: {
    alignItems: 'center',
    marginBottom: SPACING.lg,
  },
  securityLevel: {
    alignItems: 'center',
  },
  levelText: {
    fontSize: FONT_SIZES.xl,
    fontWeight: 'bold',
    color: COLORS.success,
    marginTop: SPACING.sm,
  },
  statusRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginVertical: SPACING.sm,
  },
  statusLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  statusValue: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    fontWeight: '600',
  },
  actionButton: {
    marginBottom: SPACING.sm,
  },
  scoreContainer: {
    alignItems: 'center',
    padding: SPACING.lg,
    backgroundColor: COLORS.accent,
    borderRadius: 8,
    marginBottom: SPACING.md,
  },
  scoreLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
  },
  scoreValue: {
    fontSize: FONT_SIZES.xxxl,
    fontWeight: 'bold',
    color: COLORS.success,
    marginVertical: SPACING.sm,
  },
  sectionTitle: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
    marginTop: SPACING.md,
    marginBottom: SPACING.sm,
  },
  recommendationItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: SPACING.sm,
  },
  recommendationText: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.text,
    marginLeft: SPACING.sm,
    flex: 1,
  },
  featureItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  featureLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  featureLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    marginLeft: SPACING.md,
  },
});
