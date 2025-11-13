import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';
import HomeScreen from './src/screens/HomeScreen';
import WalletScreen from './src/screens/WalletScreen';
import TradeScreen from './src/screens/TradeScreen';
import BankScreen from './src/screens/BankScreen';
import HCareScreen from './src/screens/HCareScreen';
import MeScreen from './src/screens/MeScreen';
import { theme } from './src/theme';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <>
      <StatusBar style="light" />
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName="Home"
          screenOptions={{
            headerStyle: {
              backgroundColor: theme.colors.secondary,
            },
            headerTintColor: theme.colors.accent,
            headerTitleStyle: {
              fontWeight: 'bold',
            },
            contentStyle: {
              backgroundColor: theme.colors.primary,
            },
          }}
        >
          <Stack.Screen 
            name="Home" 
            component={HomeScreen}
            options={{ title: 'AiElon FusionHD' }}
          />
          <Stack.Screen 
            name="Wallet" 
            component={WalletScreen}
            options={{ title: 'Halal Wallet' }}
          />
          <Stack.Screen 
            name="Trade" 
            component={TradeScreen}
            options={{ title: 'Trade' }}
          />
          <Stack.Screen 
            name="Bank" 
            component={BankScreen}
            options={{ title: 'Bank' }}
          />
          <Stack.Screen 
            name="HCare" 
            component={HCareScreen}
            options={{ title: 'HCare' }}
          />
          <Stack.Screen 
            name="Me" 
            component={MeScreen}
            options={{ title: 'Profile' }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </>
  );
}
