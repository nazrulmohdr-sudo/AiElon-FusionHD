/**
 * HomeScreen
 * Main landing screen for AiElon Premium services
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
import { HomeScreenProps } from '../navigation/types';
import { theme } from '../theme';

export default function HomeScreen({ navigation }: HomeScreenProps) {
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
          <Text style={styles.headerTitle}>AiElon</Text>
          <Text style={styles.headerSubtitle}>Premium Services</Text>
          <View style={styles.goldBar} />
        </View>

        {/* Welcome Section */}
        <View style={styles.welcomeSection}>
          <Text style={styles.welcomeText}>Welcome to</Text>
          <Text style={styles.fusionHDText}>Fusion HD</Text>
          <Text style={styles.tagline}>Living OS • Halal Wallet • HCare • Ummah Hub</Text>
        </View>

        {/* Service Cards */}
        <View style={styles.servicesContainer}>
          <TouchableOpacity 
            style={styles.serviceCard}
            onPress={() => navigation.navigate('Wallet')}
            activeOpacity={0.8}
          >
            <View style={styles.cardHeader}>
              <Text style={styles.cardIcon}>💰</Text>
              <View style={styles.goldCorner} />
            </View>
            <Text style={styles.cardTitle}>Halal Wallet</Text>
            <Text style={styles.cardDescription}>
              Secure, Shariah-compliant financial management
            </Text>
            <View style={styles.cardFooter}>
              <Text style={styles.cardAction}>Access Wallet →</Text>
            </View>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.serviceCard}
            activeOpacity={0.8}
          >
            <View style={styles.cardHeader}>
              <Text style={styles.cardIcon}>🏥</Text>
              <View style={styles.goldCorner} />
            </View>
            <Text style={styles.cardTitle}>HCare</Text>
            <Text style={styles.cardDescription}>
              Healthcare services with trust and excellence
            </Text>
            <View style={styles.cardFooter}>
              <Text style={styles.cardAction}>Coming Soon</Text>
            </View>
          </TouchableOpacity>

          <TouchableOpacity 
            style={styles.serviceCard}
            activeOpacity={0.8}
          >
            <View style={styles.cardHeader}>
              <Text style={styles.cardIcon}>🕌</Text>
              <View style={styles.goldCorner} />
            </View>
            <Text style={styles.cardTitle}>Ummah Hub</Text>
            <Text style={styles.cardDescription}>
              Connect with the global Muslim community
            </Text>
            <View style={styles.cardFooter}>
              <Text style={styles.cardAction}>Coming Soon</Text>
            </View>
          </TouchableOpacity>
        </View>

        {/* Amanah Statement */}
        <View style={styles.amanahSection}>
          <Text style={styles.amanahTitle}>Built on Amanah</Text>
          <Text style={styles.amanahText}>
            Trust, integrity, and responsibility are the foundation of everything we build
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
    paddingTop: theme.spacing['4xl'],
    paddingHorizontal: theme.spacing.lg,
    alignItems: 'center',
    marginBottom: theme.spacing.xl,
  },
  headerTitle: {
    fontSize: theme.typography.fontSize['4xl'],
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.primary.gold,
    letterSpacing: 2,
    marginBottom: theme.spacing.xs,
  },
  headerSubtitle: {
    fontSize: theme.typography.fontSize.base,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    textTransform: 'uppercase',
    letterSpacing: 4,
    marginBottom: theme.spacing.md,
  },
  goldBar: {
    width: 80,
    height: 3,
    backgroundColor: theme.colors.primary.gold,
    borderRadius: theme.borderRadius.full,
  },
  welcomeSection: {
    paddingHorizontal: theme.spacing.lg,
    alignItems: 'center',
    marginBottom: theme.spacing.xl,
  },
  welcomeText: {
    fontSize: theme.typography.fontSize.lg,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    marginBottom: theme.spacing.xs,
  },
  fusionHDText: {
    fontSize: theme.typography.fontSize['3xl'],
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.text.primary,
    marginBottom: theme.spacing.sm,
  },
  tagline: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.tertiary,
    textAlign: 'center',
    lineHeight: theme.typography.lineHeight.relaxed * theme.typography.fontSize.sm,
  },
  servicesContainer: {
    paddingHorizontal: theme.spacing.lg,
    gap: theme.spacing.md,
    marginBottom: theme.spacing.xl,
  },
  serviceCard: {
    backgroundColor: theme.colors.background.secondary,
    borderRadius: theme.borderRadius.xl,
    padding: theme.spacing.lg,
    borderWidth: 1,
    borderColor: theme.colors.border.secondary,
    ...theme.shadows.md,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: theme.spacing.md,
  },
  cardIcon: {
    fontSize: 32,
  },
  goldCorner: {
    width: 24,
    height: 24,
    backgroundColor: theme.colors.primary.gold,
    borderRadius: theme.borderRadius.sm,
    opacity: 0.3,
  },
  cardTitle: {
    fontSize: theme.typography.fontSize.xl,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.text.primary,
    marginBottom: theme.spacing.sm,
  },
  cardDescription: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    lineHeight: theme.typography.lineHeight.relaxed * theme.typography.fontSize.sm,
    marginBottom: theme.spacing.md,
  },
  cardFooter: {
    borderTopWidth: 1,
    borderTopColor: theme.colors.border.secondary,
    paddingTop: theme.spacing.md,
  },
  cardAction: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.semibold,
    color: theme.colors.primary.gold,
  },
  amanahSection: {
    marginHorizontal: theme.spacing.lg,
    padding: theme.spacing.lg,
    backgroundColor: theme.colors.background.tertiary,
    borderRadius: theme.borderRadius.lg,
    borderLeftWidth: 4,
    borderLeftColor: theme.colors.primary.gold,
  },
  amanahTitle: {
    fontSize: theme.typography.fontSize.lg,
    fontWeight: theme.typography.fontWeight.bold,
    color: theme.colors.primary.gold,
    marginBottom: theme.spacing.sm,
  },
  amanahText: {
    fontSize: theme.typography.fontSize.sm,
    fontWeight: theme.typography.fontWeight.normal,
    color: theme.colors.text.secondary,
    lineHeight: theme.typography.lineHeight.relaxed * theme.typography.fontSize.sm,
  },
});
