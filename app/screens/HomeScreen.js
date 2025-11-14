import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>AiElon FusionHD</Text>
      <Text style={styles.subtitle}>Welcome to AiElon Living OS</Text>
      <Text style={styles.description}>
        Your all-in-one platform for Halal Wallet, HCare, and Ummah Hub
      </Text>
      <Button
        title="About"
        onPress={() => navigation.navigate('About')}
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
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#333',
  },
  subtitle: {
    fontSize: 20,
    marginBottom: 10,
    color: '#666',
  },
  description: {
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 30,
    color: '#888',
  },
});
