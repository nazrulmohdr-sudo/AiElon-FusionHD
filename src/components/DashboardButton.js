import React from 'react';
import { TouchableOpacity, Text, StyleSheet } from 'react-native';
import { theme } from '../theme';

export default function DashboardButton({ title, onPress, icon }) {
  return (
    <TouchableOpacity 
      style={styles.button}
      onPress={onPress}
      activeOpacity={0.8}
    >
      <Text style={styles.icon}>{icon}</Text>
      <Text style={styles.title}>{title}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    backgroundColor: theme.colors.cardBackground,
    borderRadius: theme.borderRadius.lg,
    borderWidth: 2,
    borderColor: theme.colors.accent,
    padding: theme.spacing.xl,
    alignItems: 'center',
    justifyContent: 'center',
    width: '45%',
    aspectRatio: 1,
    shadowColor: theme.colors.accent,
    shadowOffset: {
      width: 0,
      height: 4,
    },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  icon: {
    fontSize: 48,
    marginBottom: theme.spacing.sm,
  },
  title: {
    color: theme.colors.accent,
    fontSize: theme.fontSizes.lg,
    fontWeight: 'bold',
    textAlign: 'center',
  },
});
