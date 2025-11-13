/**
 * Settings Screen
 * App settings and configuration
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Switch,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button } from '../components';
import { COLORS, SPACING, FONT_SIZES, APP_CONFIG } from '../constants';
import { BiometricService, SecurityService } from '../services';

export default function SettingsScreen({ navigation }) {
  const [biometricsEnabled, setBiometricsEnabled] = useState(true);
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);
  const [darkMode, setDarkMode] = useState(true);

  const runSecurityAudit = async () => {
    Alert.alert(
      'Security Audit',
      'Run a comprehensive security audit?',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Run Audit',
          onPress: async () => {
            const result = await SecurityService.performSecurityAudit();
            if (result.success) {
              Alert.alert(
                'Audit Complete',
                `Security Score: ${result.audit.score}\nStatus: ${result.audit.status}`,
              );
            }
          },
        },
      ]
    );
  };

  const enrollBiometric = async () => {
    const result = await BiometricService.enrollBiometric();
    if (result.success) {
      Alert.alert('Success', 'Biometric enrolled successfully');
    }
  };

  const settingsSections = [
    {
      title: 'Security',
      items: [
        {
          label: 'Biometric Authentication',
          icon: 'finger-print',
          type: 'switch',
          value: biometricsEnabled,
          onValueChange: setBiometricsEnabled,
        },
        {
          label: 'Security Audit',
          icon: 'shield-checkmark',
          type: 'action',
          onPress: runSecurityAudit,
        },
        {
          label: 'Enroll Biometric',
          icon: 'scan',
          type: 'action',
          onPress: enrollBiometric,
        },
      ],
    },
    {
      title: 'Preferences',
      items: [
        {
          label: 'Notifications',
          icon: 'notifications',
          type: 'switch',
          value: notificationsEnabled,
          onValueChange: setNotificationsEnabled,
        },
        {
          label: 'Dark Mode',
          icon: 'moon',
          type: 'switch',
          value: darkMode,
          onValueChange: setDarkMode,
        },
      ],
    },
    {
      title: 'Network',
      items: [
        {
          label: 'Network Settings',
          icon: 'settings',
          type: 'navigate',
          screen: 'Blockchain',
        },
        {
          label: 'Connected Networks',
          icon: 'git-network',
          type: 'info',
          value: 'AIELONCHAIN338',
        },
      ],
    },
    {
      title: 'About',
      items: [
        {
          label: 'App Version',
          icon: 'information-circle',
          type: 'info',
          value: APP_CONFIG.version,
        },
        {
          label: 'Network',
          icon: 'cloud',
          type: 'info',
          value: APP_CONFIG.network,
        },
      ],
    },
  ];

  const renderSettingItem = (item, index) => {
    switch (item.type) {
      case 'switch':
        return (
          <View key={index} style={styles.settingItem}>
            <View style={styles.settingLeft}>
              <Ionicons name={item.icon} size={24} color={COLORS.highlight} />
              <Text style={styles.settingLabel}>{item.label}</Text>
            </View>
            <Switch
              value={item.value}
              onValueChange={item.onValueChange}
              trackColor={{ false: COLORS.border, true: COLORS.highlight }}
              thumbColor={COLORS.text}
            />
          </View>
        );
      case 'action':
        return (
          <TouchableOpacity
            key={index}
            style={styles.settingItem}
            onPress={item.onPress}
          >
            <View style={styles.settingLeft}>
              <Ionicons name={item.icon} size={24} color={COLORS.highlight} />
              <Text style={styles.settingLabel}>{item.label}</Text>
            </View>
            <Ionicons name="chevron-forward" size={20} color={COLORS.textSecondary} />
          </TouchableOpacity>
        );
      case 'navigate':
        return (
          <TouchableOpacity
            key={index}
            style={styles.settingItem}
            onPress={() => navigation.navigate(item.screen)}
          >
            <View style={styles.settingLeft}>
              <Ionicons name={item.icon} size={24} color={COLORS.highlight} />
              <Text style={styles.settingLabel}>{item.label}</Text>
            </View>
            <Ionicons name="chevron-forward" size={20} color={COLORS.textSecondary} />
          </TouchableOpacity>
        );
      case 'info':
        return (
          <View key={index} style={styles.settingItem}>
            <View style={styles.settingLeft}>
              <Ionicons name={item.icon} size={24} color={COLORS.highlight} />
              <Text style={styles.settingLabel}>{item.label}</Text>
            </View>
            <Text style={styles.settingValue}>{item.value}</Text>
          </View>
        );
      default:
        return null;
    }
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {settingsSections.map((section, sectionIndex) => (
          <Card key={sectionIndex} title={section.title}>
            {section.items.map((item, itemIndex) => renderSettingItem(item, itemIndex))}
          </Card>
        ))}

        {/* Danger Zone */}
        <Card title="Danger Zone">
          <Button
            title="Clear All Data"
            onPress={() => Alert.alert('Warning', 'This will clear all app data')}
            variant="outline"
            style={styles.dangerButton}
          />
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
  settingItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  settingLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  settingLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    marginLeft: SPACING.md,
  },
  settingValue: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  dangerButton: {
    borderColor: COLORS.error,
  },
});
