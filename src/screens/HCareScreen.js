import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { theme } from '../theme';

export default function HCareScreen({ navigation }) {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.icon}>🏥</Text>
        <Text style={styles.title}>HCare Module</Text>
        <Text style={styles.description}>
          Your healthcare services will be available here soon.
        </Text>
        
        <View style={styles.featureList}>
          <Text style={styles.featureTitle}>Coming Soon:</Text>
          <Text style={styles.featureItem}>• Health records management</Text>
          <Text style={styles.featureItem}>• Appointment scheduling</Text>
          <Text style={styles.featureItem}>• Telemedicine services</Text>
          <Text style={styles.featureItem}>• Wellness tracking</Text>
        </View>

        <TouchableOpacity 
          style={styles.backButton}
          onPress={() => navigation.goBack()}
        >
          <Text style={styles.backButtonText}>← Back to Home</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.primary,
  },
  content: {
    padding: theme.spacing.xl,
    alignItems: 'center',
  },
  icon: {
    fontSize: 80,
    marginBottom: theme.spacing.lg,
  },
  title: {
    fontSize: theme.fontSizes.xxl,
    fontWeight: 'bold',
    color: theme.colors.accent,
    marginBottom: theme.spacing.md,
  },
  description: {
    fontSize: theme.fontSizes.md,
    color: theme.colors.textSecondary,
    textAlign: 'center',
    marginBottom: theme.spacing.xl,
  },
  featureList: {
    backgroundColor: theme.colors.cardBackground,
    padding: theme.spacing.xl,
    borderRadius: theme.borderRadius.lg,
    borderWidth: 2,
    borderColor: theme.colors.accent,
    width: '100%',
    marginBottom: theme.spacing.xl,
  },
  featureTitle: {
    fontSize: theme.fontSizes.lg,
    fontWeight: 'bold',
    color: theme.colors.text,
    marginBottom: theme.spacing.md,
  },
  featureItem: {
    fontSize: theme.fontSizes.md,
    color: theme.colors.text,
    marginBottom: theme.spacing.sm,
  },
  backButton: {
    marginTop: theme.spacing.xl,
    padding: theme.spacing.md,
  },
  backButtonText: {
    color: theme.colors.accent,
    fontSize: theme.fontSizes.md,
    fontWeight: '600',
  },
});
