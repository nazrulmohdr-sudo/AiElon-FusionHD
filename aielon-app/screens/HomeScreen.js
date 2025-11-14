import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { Button } from '../components';

const HomeScreen = ({ navigation }) => {
  return (
    <ScrollView style={styles.container}>
      <StatusBar style="light" />
      <View style={styles.content}>
        <Text style={styles.title}>Welcome to AiElon FusionHD</Text>
        <Text style={styles.subtitle}>
          Living OS • Fusion HD UI • Halal Wallet • HCare • Ummah Hub
        </Text>
        
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Features</Text>
          <View style={styles.featureList}>
            <Text style={styles.feature}>• AiElon Living OS Integration</Text>
            <Text style={styles.feature}>• Fusion HD User Interface</Text>
            <Text style={styles.feature}>• Halal Wallet Management</Text>
            <Text style={styles.feature}>• HCare Health Services</Text>
            <Text style={styles.feature}>• Ummah Hub Community</Text>
          </View>
        </View>

        <View style={styles.buttonContainer}>
          <Button 
            title="About This App" 
            onPress={() => navigation.navigate('About')}
          />
          <Button 
            title="Get Started" 
            variant="secondary"
            onPress={() => console.log('Get Started pressed')}
          />
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  content: {
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 30,
    textAlign: 'center',
    lineHeight: 24,
  },
  section: {
    backgroundColor: '#ffffff',
    padding: 20,
    borderRadius: 12,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#2196F3',
    marginBottom: 15,
  },
  featureList: {
    gap: 10,
  },
  feature: {
    fontSize: 16,
    color: '#333',
    lineHeight: 24,
  },
  buttonContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
});

export default HomeScreen;
