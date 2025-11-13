/**
 * Home Screen
 * Main dashboard showing overview of all modules
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  RefreshControl,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { StatusBar } from 'expo-status-bar';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { FusionCoreService } from '../services';

export default function HomeScreen({ navigation }) {
  const [loading, setLoading] = useState(false);
  const [moduleStatus, setModuleStatus] = useState(null);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    initializeApp();
  }, []);

  const initializeApp = async () => {
    setLoading(true);
    try {
      await FusionCoreService.initializeAll();
      const status = await FusionCoreService.getModuleStatus();
      setModuleStatus(status);
    } catch (error) {
      console.error('Initialization error:', error);
    } finally {
      setLoading(false);
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await initializeApp();
    setRefreshing(false);
  };

  const quickActions = [
    { id: 'wallet', title: 'Wallet', icon: 'wallet', screen: 'Wallet' },
    { id: 'nft', title: 'NFT', icon: 'images', screen: 'NFT' },
    { id: 'trade', title: 'Trade', icon: 'swap-horizontal', screen: 'Trade' },
    { id: 'security', title: 'Security', icon: 'shield-checkmark', screen: 'Security' },
  ];

  return (
    <View style={styles.container}>
      <StatusBar style="light" />
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.content}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={COLORS.highlight} />
        }
      >
        {/* Header */}
        <View style={styles.header}>
          <View>
            <Text style={styles.headerTitle}>AIELON-FUSIONHD</Text>
            <Text style={styles.headerSubtitle}>Unified Living OS</Text>
          </View>
          <TouchableOpacity
            style={styles.settingsButton}
            onPress={() => navigation.navigate('Settings')}
          >
            <Ionicons name="settings-outline" size={24} color={COLORS.text} />
          </TouchableOpacity>
        </View>

        {/* Fusion Status Card */}
        <Card title="Fusion Core Status">
          <View style={styles.statusRow}>
            <Text style={styles.statusLabel}>Mode:</Text>
            <StatusBadge status="active" label="Unified" />
          </View>
          <View style={styles.statusRow}>
            <Text style={styles.statusLabel}>Network:</Text>
            <Text style={styles.statusValue}>AIELONCHAIN338</Text>
          </View>
          {moduleStatus && (
            <View style={styles.statusRow}>
              <Text style={styles.statusLabel}>Modules Active:</Text>
              <Text style={styles.statusValue}>
                {Object.values(moduleStatus.status || {}).filter(Boolean).length} / 9
              </Text>
            </View>
          )}
        </Card>

        {/* Quick Actions */}
        <Card title="Quick Actions">
          <View style={styles.quickActions}>
            {quickActions.map((action) => (
              <TouchableOpacity
                key={action.id}
                style={styles.actionButton}
                onPress={() => navigation.navigate(action.screen)}
              >
                <View style={styles.actionIcon}>
                  <Ionicons name={action.icon} size={28} color={COLORS.highlight} />
                </View>
                <Text style={styles.actionText}>{action.title}</Text>
              </TouchableOpacity>
            ))}
          </View>
        </Card>

        {/* Modules Overview */}
        <Card title="Available Modules">
          {[
            { name: 'Blockchain Sync', icon: 'git-network', screen: 'Blockchain' },
            { name: 'Biometric Security', icon: 'finger-print', screen: 'Security' },
            { name: 'Oracle Network', icon: 'cloud-outline', screen: 'Blockchain' },
            { name: 'NFT Platform', icon: 'images', screen: 'NFT' },
            { name: 'WalletConnect', icon: 'link', screen: 'Wallet' },
            { name: 'Trade138 Bridge', icon: 'swap-horizontal', screen: 'Trade' },
            { name: 'HCARE OS', icon: 'medical', screen: 'HCare' },
            { name: 'DApp Fusion', icon: 'apps', screen: 'DApps' },
          ].map((module, index) => (
            <TouchableOpacity
              key={index}
              style={styles.moduleItem}
              onPress={() => navigation.navigate(module.screen)}
            >
              <View style={styles.moduleIcon}>
                <Ionicons name={module.icon} size={20} color={COLORS.highlight} />
              </View>
              <Text style={styles.moduleText}>{module.name}</Text>
              <Ionicons name="chevron-forward" size={20} color={COLORS.textSecondary} />
            </TouchableOpacity>
          ))}
        </Card>

        {/* Initialize Button */}
        {!moduleStatus?.initialized && (
          <Button
            title="Initialize All Modules"
            onPress={initializeApp}
            loading={loading}
            style={styles.initButton}
          />
        )}
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
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: SPACING.lg,
    paddingTop: SPACING.md,
  },
  headerTitle: {
    fontSize: FONT_SIZES.xxl,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  headerSubtitle: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  settingsButton: {
    padding: SPACING.sm,
  },
  statusRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginVertical: SPACING.xs,
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
  quickActions: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: SPACING.sm,
  },
  actionButton: {
    alignItems: 'center',
    flex: 1,
  },
  actionIcon: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: SPACING.xs,
  },
  actionText: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.text,
    textAlign: 'center',
  },
  moduleItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: SPACING.sm,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  moduleIcon: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: SPACING.md,
  },
  moduleText: {
    flex: 1,
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
  },
  initButton: {
    marginTop: SPACING.md,
    marginBottom: SPACING.xl,
  },
});
