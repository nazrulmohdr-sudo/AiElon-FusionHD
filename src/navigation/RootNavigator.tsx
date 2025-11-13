/**
 * Root Navigator
 * Main navigation configuration for the app
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { RootStackParamList } from './types';
import { theme } from '../theme';

// Screens
import HomeScreen from '../screens/HomeScreen';
import WalletScreen from '../screens/WalletScreen';

const Stack = createNativeStackNavigator<RootStackParamList>();

export default function RootNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Home"
        screenOptions={{
          headerShown: false,
          contentStyle: {
            backgroundColor: theme.colors.background.primary,
          },
          animation: 'slide_from_right',
        }}
      >
        <Stack.Screen 
          name="Home" 
          component={HomeScreen}
          options={{
            title: 'AiElon Premium',
          }}
        />
        <Stack.Screen 
          name="Wallet" 
          component={WalletScreen}
          options={{
            title: 'Halal Wallet',
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
