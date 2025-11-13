/**
 * Card Component
 * Reusable card component for consistent styling
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { COLORS, SPACING, FONT_SIZES } from '../constants';

export default function Card({ title, children, onPress, style }) {
  const Container = onPress ? TouchableOpacity : View;

  return (
    <Container style={[styles.card, style]} onPress={onPress} activeOpacity={0.7}>
      {title && <Text style={styles.title}>{title}</Text>}
      {children}
    </Container>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: COLORS.card,
    borderRadius: 12,
    padding: SPACING.md,
    marginVertical: SPACING.sm,
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  title: {
    fontSize: FONT_SIZES.lg,
    fontWeight: 'bold',
    color: COLORS.text,
    marginBottom: SPACING.sm,
  },
});
