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

type HomeScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Home'>;

interface HomeScreenProps {
  navigation: HomeScreenNavigationProp;
}

export const HomeScreen: React.FC<HomeScreenProps> = ({ navigation }) => {
  const handleTrade = () => {
    console.log('Trade pressed');
    // Navigation or action for Trade
  };

  const handleBank = () => {
    console.log('Bank pressed');
    navigation.navigate('Wallet');
  };

  const handleHCare = () => {
    console.log('HCare pressed');
    // Navigation or action for HCare
  };

  const handleMe = () => {
    console.log('Me pressed');
    // Navigation or action for Me
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>AiElon FusionHD</Text>
          <Text style={styles.subtitle}>Living OS • Halal Wallet • Ummah Hub</Text>
        </View>

        {/* Dashboard Grid */}
        <View style={styles.dashboard}>
          <Text style={styles.dashboardTitle}>Dashboard</Text>
          
          <View style={styles.buttonGrid}>
            {/* First Row */}
            <View style={styles.buttonRow}>
              <View style={styles.buttonCard}>
                <View style={styles.iconPlaceholder}>
                  <Text style={styles.iconText}>📈</Text>
                </View>
                <Text style={styles.cardLabel}>Trade</Text>
                <AiButton
                  title="Open"
                  onPress={handleTrade}
                  variant="primary"
                  size="medium"
                  style={styles.cardButton}
                />
              </View>

              <View style={styles.buttonCard}>
                <View style={styles.iconPlaceholder}>
                  <Text style={styles.iconText}>🏦</Text>
                </View>
                <Text style={styles.cardLabel}>Bank</Text>
                <AiButton
                  title="Open"
                  onPress={handleBank}
                  variant="primary"
                  size="medium"
                  style={styles.cardButton}
                />
              </View>
            </View>

            {/* Second Row */}
            <View style={styles.buttonRow}>
              <View style={styles.buttonCard}>
                <View style={styles.iconPlaceholder}>
                  <Text style={styles.iconText}>🏥</Text>
                </View>
                <Text style={styles.cardLabel}>HCare</Text>
                <AiButton
                  title="Open"
                  onPress={handleHCare}
                  variant="primary"
                  size="medium"
                  style={styles.cardButton}
                />
              </View>

              <View style={styles.buttonCard}>
                <View style={styles.iconPlaceholder}>
                  <Text style={styles.iconText}>👤</Text>
                </View>
                <Text style={styles.cardLabel}>Me</Text>
                <AiButton
                  title="Open"
                  onPress={handleMe}
                  variant="primary"
                  size="medium"
                  style={styles.cardButton}
                />
              </View>
            </View>
          </View>
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>Version 1.0.0</Text>
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
  dashboard: {
    flex: 1,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.xl,
  },
  dashboardTitle: {
    fontSize: typography.sizes.xl,
    fontWeight: typography.weights.semibold,
    color: colors.text,
    marginBottom: spacing.lg,
  },
  buttonGrid: {
    gap: spacing.lg,
  },
  buttonRow: {
    flexDirection: 'row',
    gap: spacing.md,
    marginBottom: spacing.md,
  },
  buttonCard: {
    flex: 1,
    backgroundColor: colors.cardBackground,
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  iconPlaceholder: {
    width: 60,
    height: 60,
    borderRadius: borderRadius.full,
    backgroundColor: colors.surface,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.md,
  },
  iconText: {
    fontSize: 32,
  },
  cardLabel: {
    fontSize: typography.sizes.lg,
    fontWeight: typography.weights.semibold,
    color: colors.text,
    marginBottom: spacing.md,
  },
  cardButton: {
    width: '100%',
  },
  footer: {
    paddingTop: spacing.xl,
    paddingHorizontal: spacing.lg,
    alignItems: 'center',
  },
  footerText: {
    fontSize: typography.sizes.xs,
    color: colors.textMuted,
  },
});
