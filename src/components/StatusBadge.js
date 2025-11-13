/**
 * StatusBadge Component
 * Shows status indicators
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { COLORS, SPACING, FONT_SIZES } from '../constants';

export default function StatusBadge({ status, label }) {
  const getStatusColor = () => {
    switch (status) {
      case 'active':
      case 'connected':
      case 'success':
        return COLORS.success;
      case 'pending':
      case 'processing':
        return COLORS.warning;
      case 'failed':
      case 'error':
      case 'disconnected':
        return COLORS.error;
      default:
        return COLORS.textSecondary;
    }
  };

  return (
    <View style={[styles.badge, { backgroundColor: getStatusColor() + '20' }]}>
      <View style={[styles.dot, { backgroundColor: getStatusColor() }]} />
      <Text style={[styles.text, { color: getStatusColor() }]}>
        {label || status}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: SPACING.sm,
    paddingVertical: SPACING.xs,
    borderRadius: 12,
    alignSelf: 'flex-start',
  },
  dot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    marginRight: SPACING.xs,
  },
  text: {
    fontSize: FONT_SIZES.sm,
    fontWeight: '600',
  },
});
