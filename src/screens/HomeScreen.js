import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import DashboardButton from '../components/DashboardButton';
import { theme } from '../theme';

export default function HomeScreen({ navigation }) {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>AiElon Living OS</Text>
        <Text style={styles.subtitle}>Fusion HD • Ummah Hub</Text>
      </View>

      <View style={styles.dashboardGrid}>
        <DashboardButton
          title="Trade"
          icon="📈"
          onPress={() => navigation.navigate('Trade')}
        />
        <DashboardButton
          title="Bank"
          icon="🏦"
          onPress={() => navigation.navigate('Bank')}
        />
        <DashboardButton
          title="HCare"
          icon="🏥"
          onPress={() => navigation.navigate('HCare')}
        />
        <DashboardButton
          title="Me"
          icon="👤"
          onPress={() => navigation.navigate('Me')}
        />
      </View>

      <View style={styles.walletSection}>
        <Text style={styles.walletLabel}>Quick Access</Text>
        <DashboardButton
          title="Halal Wallet"
          icon="💳"
          onPress={() => navigation.navigate('Wallet')}
        />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: theme.spacing.lg,
    backgroundColor: theme.colors.primary,
  },
  header: {
    alignItems: 'center',
    marginBottom: theme.spacing.xl,
    paddingVertical: theme.spacing.lg,
  },
  title: {
    fontSize: theme.fontSizes.xxl,
    fontWeight: 'bold',
    color: theme.colors.accent,
    marginBottom: theme.spacing.sm,
  },
  subtitle: {
    fontSize: theme.fontSizes.md,
    color: theme.colors.textSecondary,
    textAlign: 'center',
  },
  dashboardGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: theme.spacing.md,
    marginBottom: theme.spacing.xl,
  },
  walletSection: {
    alignItems: 'center',
    marginTop: theme.spacing.lg,
  },
  walletLabel: {
    fontSize: theme.fontSizes.lg,
    color: theme.colors.text,
    marginBottom: theme.spacing.md,
    fontWeight: '600',
  },
});
