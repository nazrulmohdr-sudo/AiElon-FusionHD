import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import { AiButton } from '../components/AiButton';
import { colors } from '../theme/colors';
import { typography, spacing, borderRadius } from '../theme';

type RootStackParamList = {
  Home: undefined;
  Wallet: undefined;
};

type WalletScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Wallet'>;

interface WalletScreenProps {
  navigation: WalletScreenNavigationProp;
}

export const WalletScreen: React.FC<WalletScreenProps> = ({ navigation }) => {
  const handleGoBack = () => {
    navigation.goBack();
  };

  const handleSend = () => {
    console.log('Send pressed');
  };

  const handleReceive = () => {
    console.log('Receive pressed');
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Halal Wallet</Text>
          <Text style={styles.subtitle}>Your digital banking solution</Text>
        </View>

        {/* Balance Card */}
        <View style={styles.balanceCard}>
          <Text style={styles.balanceLabel}>Total Balance</Text>
          <Text style={styles.balanceAmount}>$0.00</Text>
          <View style={styles.balanceFooter}>
            <Text style={styles.balanceSubtext}>≈ 0.00 BTC</Text>
          </View>
        </View>

        {/* Action Buttons */}
        <View style={styles.actionsContainer}>
          <View style={styles.actionCard}>
            <View style={styles.actionIcon}>
              <Text style={styles.actionIconText}>📤</Text>
            </View>
            <Text style={styles.actionLabel}>Send</Text>
            <AiButton
              title="Send"
              onPress={handleSend}
              variant="primary"
              size="medium"
              style={styles.actionButton}
            />
          </View>

          <View style={styles.actionCard}>
            <View style={styles.actionIcon}>
              <Text style={styles.actionIconText}>📥</Text>
            </View>
            <Text style={styles.actionLabel}>Receive</Text>
            <AiButton
              title="Receive"
              onPress={handleReceive}
              variant="primary"
              size="medium"
              style={styles.actionButton}
            />
          </View>
        </View>

        {/* Recent Transactions */}
        <View style={styles.transactionsContainer}>
          <Text style={styles.transactionsTitle}>Recent Transactions</Text>
          <View style={styles.emptyState}>
            <Text style={styles.emptyStateText}>No transactions yet</Text>
            <Text style={styles.emptyStateSubtext}>
              Your transaction history will appear here
            </Text>
          </View>
        </View>

        {/* Back Button */}
        <View style={styles.backButtonContainer}>
          <AiButton
            title="Back to Dashboard"
            onPress={handleGoBack}
            variant="outline"
            size="large"
          />
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background,
  },
  scrollContent: {
    flexGrow: 1,
    paddingBottom: spacing.xl,
  },
  header: {
    paddingTop: spacing.xl,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.lg,
    alignItems: 'center',
  },
  title: {
    fontSize: typography.sizes.xxxl,
    fontWeight: typography.weights.bold,
    color: colors.primary,
    marginBottom: spacing.sm,
  },
  subtitle: {
    fontSize: typography.sizes.sm,
    color: colors.textSecondary,
    textAlign: 'center',
  },
  balanceCard: {
    marginHorizontal: spacing.lg,
    marginTop: spacing.lg,
    backgroundColor: colors.cardBackground,
    borderRadius: borderRadius.lg,
    padding: spacing.xl,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  balanceLabel: {
    fontSize: typography.sizes.md,
    color: colors.textSecondary,
    marginBottom: spacing.sm,
  },
  balanceAmount: {
    fontSize: typography.sizes.xxxl,
    fontWeight: typography.weights.bold,
    color: colors.primary,
    marginBottom: spacing.sm,
  },
  balanceFooter: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  balanceSubtext: {
    fontSize: typography.sizes.sm,
    color: colors.textMuted,
  },
  actionsContainer: {
    flexDirection: 'row',
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.xl,
    gap: spacing.md,
  },
  actionCard: {
    flex: 1,
    backgroundColor: colors.cardBackground,
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  actionIcon: {
    width: 50,
    height: 50,
    borderRadius: borderRadius.full,
    backgroundColor: colors.surface,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.md,
  },
  actionIconText: {
    fontSize: 24,
  },
  actionLabel: {
    fontSize: typography.sizes.md,
    fontWeight: typography.weights.semibold,
    color: colors.text,
    marginBottom: spacing.md,
  },
  actionButton: {
    width: '100%',
  },
  transactionsContainer: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.xl,
  },
  transactionsTitle: {
    fontSize: typography.sizes.xl,
    fontWeight: typography.weights.semibold,
    color: colors.text,
    marginBottom: spacing.lg,
  },
  emptyState: {
    backgroundColor: colors.cardBackground,
    borderRadius: borderRadius.lg,
    padding: spacing.xl,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  emptyStateText: {
    fontSize: typography.sizes.md,
    color: colors.textSecondary,
    marginBottom: spacing.sm,
  },
  emptyStateSubtext: {
    fontSize: typography.sizes.sm,
    color: colors.textMuted,
    textAlign: 'center',
  },
  backButtonContainer: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.xl,
  },
});
