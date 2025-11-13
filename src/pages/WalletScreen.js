/**
 * Wallet Screen
 * Manage wallet and blockchain interactions
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { BlockchainService, BiometricService } from '../services';

export default function WalletScreen() {
  const [wallet, setWallet] = useState(null);
  const [balance, setBalance] = useState(null);
  const [loading, setLoading] = useState(false);
  const [transactions, setTransactions] = useState([]);

  const connectWallet = async () => {
    setLoading(true);
    try {
      // Authenticate with biometrics first
      const auth = await BiometricService.authenticate('Authenticate to connect wallet');
      
      if (auth.success) {
        const result = await BlockchainService.connectWallet();
        if (result.success) {
          setWallet(result);
          Alert.alert('Success', 'Wallet connected successfully');
          loadBalance();
        }
      } else {
        Alert.alert('Authentication Failed', 'Biometric authentication required');
      }
    } catch (error) {
      Alert.alert('Error', error.message);
    } finally {
      setLoading(false);
    }
  };

  const loadBalance = async () => {
    try {
      const result = await BlockchainService.getBalance();
      if (result.success) {
        setBalance(result);
      }
    } catch (error) {
      console.error('Error loading balance:', error);
    }
  };

  const syncBlockchain = async () => {
    setLoading(true);
    try {
      const result = await BlockchainService.syncBlockchain();
      if (result.success) {
        Alert.alert('Sync Complete', `Synced to block ${result.latestBlock}`);
      }
    } catch (error) {
      Alert.alert('Error', error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Wallet Status */}
        <Card title="Wallet Status">
          {wallet ? (
            <>
              <StatusBadge status="connected" label="Connected" />
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Address:</Text>
                <Text style={styles.addressText} numberOfLines={1}>
                  {wallet.address}
                </Text>
              </View>
              {balance && (
                <View style={styles.balanceContainer}>
                  <Text style={styles.balanceLabel}>Balance</Text>
                  <Text style={styles.balanceAmount}>
                    {balance.balance} {balance.currency}
                  </Text>
                </View>
              )}
            </>
          ) : (
            <>
              <StatusBadge status="disconnected" label="Not Connected" />
              <Text style={styles.helpText}>Connect your wallet to get started</Text>
            </>
          )}
        </Card>

        {/* Actions */}
        <Card title="Actions">
          {!wallet ? (
            <Button
              title="Connect Wallet"
              onPress={connectWallet}
              loading={loading}
            />
          ) : (
            <View style={styles.buttonGroup}>
              <Button
                title="Sync Blockchain"
                onPress={syncBlockchain}
                loading={loading}
                variant="secondary"
                style={styles.actionButton}
              />
              <Button
                title="Refresh Balance"
                onPress={loadBalance}
                variant="outline"
                style={styles.actionButton}
              />
            </View>
          )}
        </Card>

        {/* Network Info */}
        <Card title="Network Information">
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Network:</Text>
            <Text style={styles.infoValue}>AIELONCHAIN338</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Chain ID:</Text>
            <Text style={styles.infoValue}>338</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Status:</Text>
            <StatusBadge status="active" label="Active" />
          </View>
        </Card>

        {/* Recent Transactions */}
        <Card title="Recent Transactions">
          {transactions.length > 0 ? (
            transactions.map((tx, index) => (
              <View key={index} style={styles.transactionItem}>
                <Ionicons name="arrow-forward-circle" size={24} color={COLORS.highlight} />
                <View style={styles.transactionInfo}>
                  <Text style={styles.transactionText}>{tx.type}</Text>
                  <Text style={styles.transactionTime}>{tx.time}</Text>
                </View>
                <Text style={styles.transactionAmount}>{tx.amount}</Text>
              </View>
            ))
          ) : (
            <Text style={styles.emptyText}>No transactions yet</Text>
          )}
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
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: SPACING.md,
  },
  infoLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  infoValue: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    fontWeight: '600',
  },
  addressText: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.text,
    fontFamily: 'monospace',
    flex: 1,
    marginLeft: SPACING.sm,
  },
  balanceContainer: {
    alignItems: 'center',
    marginTop: SPACING.lg,
    padding: SPACING.md,
    backgroundColor: COLORS.accent,
    borderRadius: 8,
  },
  balanceLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
  },
  balanceAmount: {
    fontSize: FONT_SIZES.xxxl,
    color: COLORS.text,
    fontWeight: 'bold',
    marginTop: SPACING.xs,
  },
  helpText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    marginTop: SPACING.md,
    textAlign: 'center',
  },
  buttonGroup: {
    gap: SPACING.sm,
  },
  actionButton: {
    marginBottom: SPACING.sm,
  },
  transactionItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: SPACING.sm,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  transactionInfo: {
    flex: 1,
    marginLeft: SPACING.sm,
  },
  transactionText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
  },
  transactionTime: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  transactionAmount: {
    fontSize: FONT_SIZES.md,
    color: COLORS.success,
    fontWeight: 'bold',
  },
  emptyText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    textAlign: 'center',
    paddingVertical: SPACING.lg,
  },
});
