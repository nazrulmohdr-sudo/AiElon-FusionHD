/**
 * DApps Screen
 * Browse and connect to decentralized applications
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Image,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { DAppFusionService } from '../services';

export default function DAppsScreen() {
  const [dapps, setDapps] = useState([]);
  const [connectedDapps, setConnectedDapps] = useState([]);
  const [loading, setLoading] = useState(false);
  const [stats, setStats] = useState(null);

  useEffect(() => {
    loadDApps();
    loadStats();
  }, []);

  const loadDApps = async () => {
    setLoading(true);
    try {
      const result = await DAppFusionService.getAvailableDApps();
      if (result.success) {
        setDapps(result.dapps);
      }
      
      const connected = DAppFusionService.getConnectedDApps();
      if (connected.success) {
        setConnectedDapps(connected.dapps);
      }
    } catch (error) {
      console.error('Error loading dApps:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadStats = async () => {
    try {
      const result = await DAppFusionService.getFusionStats();
      if (result.success) {
        setStats(result.stats);
      }
    } catch (error) {
      console.error('Error loading stats:', error);
    }
  };

  const connectDApp = async (dappId, dappName) => {
    Alert.alert(
      'Connect to DApp',
      `Connect to ${dappName}?`,
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Connect',
          onPress: async () => {
            setLoading(true);
            try {
              const result = await DAppFusionService.connectDApp(dappId);
              if (result.success) {
                Alert.alert('Success', result.message);
                loadDApps();
              }
            } catch (error) {
              Alert.alert('Error', error.message);
            } finally {
              setLoading(false);
            }
          },
        },
      ]
    );
  };

  const disconnectDApp = async (dappId) => {
    try {
      const result = await DAppFusionService.disconnectDApp(dappId);
      if (result.success) {
        loadDApps();
      }
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };

  const isConnected = (dappId) => {
    return connectedDapps.some(d => d.id === dappId);
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Stats Card */}
        {stats && (
          <Card title="DApp Fusion Stats">
            <View style={styles.statsGrid}>
              <View style={styles.statItem}>
                <Text style={styles.statValue}>{stats.totalDApps}</Text>
                <Text style={styles.statLabel}>Available</Text>
              </View>
              <View style={styles.statDivider} />
              <View style={styles.statItem}>
                <Text style={styles.statValue}>{stats.connectedDApps}</Text>
                <Text style={styles.statLabel}>Connected</Text>
              </View>
              <View style={styles.statDivider} />
              <View style={styles.statItem}>
                <Text style={styles.statValue}>{stats.uptime}</Text>
                <Text style={styles.statLabel}>Uptime</Text>
              </View>
            </View>
            <View style={styles.fusionMode}>
              <Text style={styles.fusionLabel}>Fusion Mode:</Text>
              <StatusBadge status="active" label={stats.fusionMode} />
            </View>
          </Card>
        )}

        {/* Connected DApps */}
        {connectedDapps.length > 0 && (
          <Card title="Connected DApps">
            {connectedDapps.map((dapp) => (
              <View key={dapp.id} style={styles.connectedItem}>
                <View style={styles.dappIcon}>
                  <Ionicons name="checkmark-circle" size={24} color={COLORS.success} />
                </View>
                <View style={styles.dappInfo}>
                  <Text style={styles.dappName}>{dapp.name}</Text>
                  <Text style={styles.dappCategory}>{dapp.category}</Text>
                </View>
                <TouchableOpacity onPress={() => disconnectDApp(dapp.id)}>
                  <Ionicons name="close-circle" size={24} color={COLORS.error} />
                </TouchableOpacity>
              </View>
            ))}
          </Card>
        )}

        {/* Available DApps */}
        <Card title="Available DApps">
          {dapps.map((dapp) => (
            <View key={dapp.id} style={styles.dappCard}>
              <View style={styles.dappHeader}>
                <View style={styles.dappIconLarge}>
                  <Image source={{ uri: dapp.icon }} style={styles.iconImage} />
                </View>
                <View style={styles.dappDetails}>
                  <Text style={styles.dappName}>{dapp.name}</Text>
                  <Text style={styles.dappDescription} numberOfLines={2}>
                    {dapp.description}
                  </Text>
                  <View style={styles.dappMeta}>
                    <Text style={styles.dappCategory}>{dapp.category}</Text>
                    <StatusBadge
                      status={isConnected(dapp.id) ? 'connected' : 'active'}
                      label={isConnected(dapp.id) ? 'Connected' : 'Available'}
                    />
                  </View>
                </View>
              </View>
              {!isConnected(dapp.id) && (
                <Button
                  title="Connect"
                  onPress={() => connectDApp(dapp.id, dapp.name)}
                  variant="outline"
                  style={styles.connectButton}
                />
              )}
            </View>
          ))}
        </Card>

        {dapps.length === 0 && !loading && (
          <Card>
            <Text style={styles.emptyText}>No DApps available</Text>
          </Card>
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
  statsGrid: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: SPACING.md,
  },
  statItem: {
    alignItems: 'center',
  },
  statDivider: {
    width: 1,
    backgroundColor: COLORS.border,
  },
  statValue: {
    fontSize: FONT_SIZES.xl,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  statLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  fusionMode: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: SPACING.md,
    borderTopWidth: 1,
    borderTopColor: COLORS.border,
  },
  fusionLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  connectedItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: SPACING.sm,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  dappIcon: {
    marginRight: SPACING.sm,
  },
  dappInfo: {
    flex: 1,
  },
  dappName: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  dappCategory: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  dappCard: {
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  dappHeader: {
    flexDirection: 'row',
    marginBottom: SPACING.md,
  },
  dappIconLarge: {
    width: 64,
    height: 64,
    borderRadius: 12,
    backgroundColor: COLORS.accent,
    overflow: 'hidden',
    marginRight: SPACING.md,
  },
  iconImage: {
    width: '100%',
    height: '100%',
  },
  dappDetails: {
    flex: 1,
  },
  dappDescription: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  dappMeta: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: SPACING.sm,
  },
  connectButton: {
    marginTop: SPACING.sm,
  },
  emptyText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    textAlign: 'center',
    paddingVertical: SPACING.lg,
  },
});
