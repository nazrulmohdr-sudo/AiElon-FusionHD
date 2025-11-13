/**
 * WalletScreen
 * Halal Wallet screen for financial management
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  StatusBar,
} from 'react-native';
import { WalletScreenProps } from '../navigation/types';
import { theme } from '../theme';

export default function WalletScreen({ navigation }: WalletScreenProps) {
  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor={theme.colors.background.primary} />
      
      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Header Section */}
        <View style={styles.header}>
          <TouchableOpacity 
            style={styles.backButton}
            onPress={() => navigation.goBack()}
            activeOpacity={0.7}
          >
            <Text style={styles.backButtonText}>← Back</Text>
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Halal Wallet</Text>
          <Text style={styles.headerSubtitle}>Shariah-Compliant Finance</Text>
          <View style={styles.goldBar} />
        </View>

        {/* Balance Card */}
        <View style={styles.balanceCard}>
          <View style={styles.balanceHeader}>
            <Text style={styles.balanceLabel}>Total Balance</Text>
            <View style={styles.verifiedBadge}>
              <Text style={styles.verifiedText}>✓ Halal</Text>
            </View>
          </View>
          <Text style={styles.balanceAmount}>$0.00</Text>
          <Text style={styles.balanceSubtext}>Available for transactions</Text>
          
          <View style={styles.balanceActions}>
            <TouchableOpacity style={styles.actionButton} activeOpacity={0.8}>
              <Text style={styles.actionButtonIcon}>↑</Text>
              <Text style={styles.actionButtonText}>Send</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.actionButton} activeOpacity={0.8}>
              <Text style={styles.actionButtonIcon}>↓</Text>
              <Text style={styles.actionButtonText}>Receive</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.actionButton} activeOpacity={0.8}>
              <Text style={styles.actionButtonIcon}>📊</Text>
              <Text style={styles.actionButtonText}>Analytics</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Quick Stats */}
        <View style={styles.statsContainer}>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>0</Text>
            <Text style={styles.statLabel}>Transactions</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>$0</Text>
            <Text style={styles.statLabel}>This Month</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statValue}>0%</Text>
            <Text style={styles.statLabel}>Returns</Text>
          </View>
        </View>

        {/* Features Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Wallet Features</Text>
          
          <View style={styles.featuresList}>
            <View style={styles.featureItem}>
              <Text style={styles.featureIcon}>🛡️</Text>
              <View style={styles.featureContent}>
                <Text style={styles.featureTitle}>Shariah Compliance</Text>
                <Text style={styles.featureDescription}>
                  All transactions verified by Islamic finance experts
                </Text>
              </View>
            </View>

            <View style={styles.featureItem}>
              <Text style={styles.featureIcon}>🔒</Text>
              <View style={styles.featureContent}>
                <Text style={styles.featureTitle}>Secure Transactions</Text>
                <Text style={styles.featureDescription}>
                  Bank-level encryption and multi-factor authentication
                </Text>
              </View>
            </View>

            <View style={styles.featureItem}>
              <Text style={styles.featureIcon}>📈</Text>
              <View style={styles.featureContent}>
                <Text style={styles.featureTitle}>Halal Investments</Text>
                <Text style={styles.featureDescription}>
                  Access to ethical and Shariah-compliant investment opportunities
                </Text>
              </View>
            </View>

            <View style={styles.featureItem}>
              <Text style={styles.featureIcon}>💎</Text>
              <View style={styles.featureContent}>
                <Text style={styles.featureTitle}>Premium Benefits</Text>
                <Text style={styles.featureDescription}>
                  Exclusive rewards and lower fees for premium members
                </Text>
              </View>
            </View>
          </View>
        </View>

        {/* Amanah Trust Statement */}
        <View style={styles.trustSection}>
          <Text style={styles.trustTitle}>Your Trust, Our Responsibility</Text>
          <Text style={styles.trustText}>
            We uphold the principles of Amanah in every transaction, ensuring transparency, 
            security, and adherence to Islamic financial principles.
          </Text>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.background.primary,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingBottom: theme.spacing['2xl'],
  },
  header: {
    paddingTop: theme.spacing.xl,
    paddingHorizontal: theme.spacing.lg,
    alignItems: 'center',
    marginBottom: theme.spacing.xl,
  },
  backButton: {
    alignSelf: 'flex-start',
    marginBottom: theme.spacing.md,
  },
  backButtonText: {
    fontSize: theme.typography.fontSize.base,
    fontWeight: theme.typography.fontWeight.medium,
    color: theme.colors.primary.gold,
  },
  headerTitle: {
    fontSize: theme.typography.fontSize['3xl'],
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.text.primary,
    marginBottom: theme.spacing.xs,
  },
  headerSubtitle: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    textTransform: 'uppercase',
    letterSpacing: 2,
    marginBottom: theme.spacing.md,
  },
  goldBar: {
    width: 60,
    height: 3,
    backgroundColor: theme.colors.primary.gold,
    borderRadius: theme.borderRadius.full,
  },
  balanceCard: {
    marginHorizontal: theme.spacing.lg,
    backgroundColor: theme.colors.background.secondary,
    borderRadius: theme.borderRadius.xl,
    padding: theme.spacing.lg,
    borderWidth: 2,
    borderColor: theme.colors.primary.gold,
    marginBottom: theme.spacing.lg,
    ...theme.shadows.gold,
  },
  balanceHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: theme.spacing.sm,
  },
  balanceLabel: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.medium,
    color: theme.colors.text.secondary,
  },
  verifiedBadge: {
    backgroundColor: theme.colors.success,
    paddingHorizontal: theme.spacing.sm,
    paddingVertical: theme.spacing.xs,
    borderRadius: theme.borderRadius.md,
  },
  verifiedText: {
    fontSize: theme.typography.fontSize.xs,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.neutral.white,
  },
  balanceAmount: {
    fontSize: theme.typography.fontSize['4xl'],
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.primary.gold,
    marginBottom: theme.spacing.xs,
  },
  balanceSubtext: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.tertiary,
    marginBottom: theme.spacing.lg,
  },
  balanceActions: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    gap: theme.spacing.sm,
  },
  actionButton: {
    flex: 1,
    backgroundColor: theme.colors.background.tertiary,
    borderRadius: theme.borderRadius.md,
    padding: theme.spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: theme.colors.border.secondary,
  },
  actionButtonIcon: {
    fontSize: 24,
    marginBottom: theme.spacing.xs,
  },
  actionButtonText: {
    fontSize: theme.typography.fontSize.xs,
    fontWeight: theme.typography.fontWeight.medium,
    color: theme.colors.text.primary,
  },
  statsContainer: {
    flexDirection: 'row',
    paddingHorizontal: theme.spacing.lg,
    gap: theme.spacing.sm,
    marginBottom: theme.spacing.xl,
  },
  statCard: {
    flex: 1,
    backgroundColor: theme.colors.background.secondary,
    borderRadius: theme.borderRadius.lg,
    padding: theme.spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: theme.colors.border.secondary,
  },
  statValue: {
    fontSize: theme.typography.fontSize.xl,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.primary.gold,
    marginBottom: theme.spacing.xs,
  },
  statLabel: {
    fontSize: theme.typography.fontSize.xs,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.tertiary,
  },
  section: {
    paddingHorizontal: theme.spacing.lg,
    marginBottom: theme.spacing.xl,
  },
  sectionTitle: {
    fontSize: theme.typography.fontSize.xl,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.text.primary,
    marginBottom: theme.spacing.md,
  },
  featuresList: {
    gap: theme.spacing.md,
  },
  featureItem: {
    flexDirection: 'row',
    backgroundColor: theme.colors.background.secondary,
    borderRadius: theme.borderRadius.lg,
    padding: theme.spacing.md,
    borderWidth: 1,
    borderColor: theme.colors.border.secondary,
  },
  featureIcon: {
    fontSize: 28,
    marginRight: theme.spacing.md,
  },
  featureContent: {
    flex: 1,
  },
  featureTitle: {
    fontSize: theme.typography.fontSize.base,
    fontWeight: theme.typography.fontWeight.semibold,
    color: theme.colors.text.primary,
    marginBottom: theme.spacing.xs,
  },
  featureDescription: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    lineHeight: theme.typography.lineHeight.relaxed * theme.typography.fontSize.sm,
  },
  trustSection: {
    marginHorizontal: theme.spacing.lg,
    padding: theme.spacing.lg,
    backgroundColor: theme.colors.background.tertiary,
    borderRadius: theme.borderRadius.lg,
    borderLeftWidth: 4,
    borderLeftColor: theme.colors.primary.gold,
  },
  trustTitle: {
    fontSize: theme.typography.fontSize.lg,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.primary.gold,
    marginBottom: theme.spacing.sm,
  },
  trustText: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    lineHeight: theme.typography.lineHeight.relaxed * theme.typography.fontSize.sm,
  },
});
