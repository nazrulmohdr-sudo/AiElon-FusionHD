import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { theme } from '../theme';

export default function WalletScreen({ navigation }) {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Halal Wallet</Text>
        <Text style={styles.subtitle}>Sharia-Compliant Finance</Text>
      </View>

      <View style={styles.balanceCard}>
        <Text style={styles.balanceLabel}>Total Balance</Text>
        <Text style={styles.balanceAmount}>$0.00</Text>
        <Text style={styles.balanceSubtext}>Available for transactions</Text>
      </View>

      <View style={styles.actionsContainer}>
        <TouchableOpacity style={styles.actionButton}>
          <Text style={styles.actionIcon}>💸</Text>
          <Text style={styles.actionText}>Send</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.actionButton}>
          <Text style={styles.actionIcon}>📥</Text>
          <Text style={styles.actionText}>Receive</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.actionButton}>
          <Text style={styles.actionIcon}>🔄</Text>
          <Text style={styles.actionText}>Exchange</Text>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.actionButton}>
          <Text style={styles.actionIcon}>📊</Text>
          <Text style={styles.actionText}>History</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.infoSection}>
        <Text style={styles.infoTitle}>Recent Transactions</Text>
        <View style={styles.placeholderBox}>
          <Text style={styles.placeholderText}>No transactions yet</Text>
          <Text style={styles.placeholderSubtext}>Your transaction history will appear here</Text>
        </View>
      </View>

      <TouchableOpacity 
        style={styles.backButton}
        onPress={() => navigation.goBack()}
      >
        <Text style={styles.backButtonText}>← Back to Home</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.primary,
  },
  header: {
    padding: theme.spacing.lg,
    alignItems: 'center',
  },
  title: {
    fontSize: theme.fontSizes.xl,
    fontWeight: 'bold',
    color: theme.colors.accent,
    marginBottom: theme.spacing.xs,
  },
  subtitle: {
    fontSize: theme.fontSizes.sm,
    color: theme.colors.textSecondary,
  },
  balanceCard: {
    backgroundColor: theme.colors.cardBackground,
    margin: theme.spacing.lg,
    padding: theme.spacing.xl,
    borderRadius: theme.borderRadius.lg,
    borderWidth: 2,
    borderColor: theme.colors.accent,
    alignItems: 'center',
  },
  balanceLabel: {
    fontSize: theme.fontSizes.sm,
    color: theme.colors.textSecondary,
    marginBottom: theme.spacing.sm,
  },
  balanceAmount: {
    fontSize: 48,
    fontWeight: 'bold',
    color: theme.colors.accent,
    marginBottom: theme.spacing.xs,
  },
  balanceSubtext: {
    fontSize: theme.fontSizes.xs,
    color: theme.colors.textSecondary,
  },
  actionsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingHorizontal: theme.spacing.lg,
    marginBottom: theme.spacing.xl,
  },
  actionButton: {
    alignItems: 'center',
    padding: theme.spacing.md,
  },
  actionIcon: {
    fontSize: 32,
    marginBottom: theme.spacing.xs,
  },
  actionText: {
    color: theme.colors.text,
    fontSize: theme.fontSizes.sm,
  },
  infoSection: {
    padding: theme.spacing.lg,
  },
  infoTitle: {
    fontSize: theme.fontSizes.lg,
    fontWeight: 'bold',
    color: theme.colors.text,
    marginBottom: theme.spacing.md,
  },
  placeholderBox: {
    backgroundColor: theme.colors.secondary,
    padding: theme.spacing.xl,
    borderRadius: theme.borderRadius.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: theme.colors.cardBackground,
  },
  placeholderText: {
    color: theme.colors.text,
    fontSize: theme.fontSizes.md,
    marginBottom: theme.spacing.xs,
  },
  placeholderSubtext: {
    color: theme.colors.textSecondary,
    fontSize: theme.fontSizes.sm,
    textAlign: 'center',
  },
  backButton: {
    margin: theme.spacing.lg,
    padding: theme.spacing.md,
    alignItems: 'center',
  },
  backButtonText: {
    color: theme.colors.accent,
    fontSize: theme.fontSizes.md,
    fontWeight: '600',
  },
});
