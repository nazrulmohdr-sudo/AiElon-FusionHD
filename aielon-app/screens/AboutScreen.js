import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { Button } from '../components';

const AboutScreen = ({ navigation }) => {
  return (
    <ScrollView style={styles.container}>
      <StatusBar style="light" />
      <View style={styles.content}>
        <Text style={styles.title}>About AiElon FusionHD</Text>
        
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Our Mission</Text>
          <Text style={styles.text}>
            AiElon FusionHD is a comprehensive ecosystem designed to provide 
            innovative solutions for the modern Muslim community, combining 
            technology, finance, healthcare, and community engagement.
          </Text>
        </View>

        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Core Components</Text>
          <View style={styles.componentList}>
            <View style={styles.component}>
              <Text style={styles.componentTitle}>Living OS</Text>
              <Text style={styles.componentDesc}>
                An intelligent operating system for seamless daily management
              </Text>
            </View>
            
            <View style={styles.component}>
              <Text style={styles.componentTitle}>Fusion HD UI</Text>
              <Text style={styles.componentDesc}>
                Beautiful, intuitive interface with HD visual experience
              </Text>
            </View>
            
            <View style={styles.component}>
              <Text style={styles.componentTitle}>Halal Wallet</Text>
              <Text style={styles.componentDesc}>
                Shariah-compliant financial management and transactions
              </Text>
            </View>
            
            <View style={styles.component}>
              <Text style={styles.componentTitle}>HCare</Text>
              <Text style={styles.componentDesc}>
                Comprehensive healthcare services and wellness tracking
              </Text>
            </View>
            
            <View style={styles.component}>
              <Text style={styles.componentTitle}>Ummah Hub</Text>
              <Text style={styles.componentDesc}>
                Community platform for connection and collaboration
              </Text>
            </View>
          </View>
        </View>

        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Version Information</Text>
          <Text style={styles.text}>Version: 1.0.0</Text>
          <Text style={styles.text}>Build: Production</Text>
        </View>

        <View style={styles.buttonContainer}>
          <Button 
            title="Back to Home" 
            onPress={() => navigation.goBack()}
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
    marginBottom: 20,
    textAlign: 'center',
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
    marginBottom: 12,
  },
  text: {
    fontSize: 16,
    color: '#333',
    lineHeight: 24,
    marginBottom: 8,
  },
  componentList: {
    gap: 15,
  },
  component: {
    borderLeftWidth: 4,
    borderLeftColor: '#2196F3',
    paddingLeft: 15,
  },
  componentTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#333',
    marginBottom: 5,
  },
  componentDesc: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  buttonContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
});

export default AboutScreen;
