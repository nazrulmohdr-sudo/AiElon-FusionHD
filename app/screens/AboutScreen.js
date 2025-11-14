import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';

export default function AboutScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>About AiElon FusionHD</Text>
      <Text style={styles.version}>Version 1.0.0</Text>
      <Text style={styles.description}>
        AiElon FusionHD is a comprehensive platform that brings together:
      </Text>
      <Text style={styles.feature}>• AiElon Living OS</Text>
      <Text style={styles.feature}>• Fusion HD UI</Text>
      <Text style={styles.feature}>• Halal Wallet</Text>
      <Text style={styles.feature}>• HCare</Text>
      <Text style={styles.feature}>• Ummah Hub</Text>
      <Button
        title="Go Back"
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#333',
  },
  version: {
    fontSize: 16,
    marginBottom: 20,
    color: '#666',
  },
  description: {
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 20,
    color: '#888',
  },
  feature: {
    fontSize: 16,
    marginBottom: 8,
    color: '#555',
  },
});
