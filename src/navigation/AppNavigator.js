/**
 * App Navigation
 * Main navigation structure for the app
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import { Ionicons } from '@expo/vector-icons';
import { COLORS } from '../constants';

// Import pages
import HomeScreen from '../pages/HomeScreen';
import WalletScreen from '../pages/WalletScreen';
import NFTScreen from '../pages/NFTScreen';
import DAppsScreen from '../pages/DAppsScreen';
import HCareScreen from '../pages/HCareScreen';
import SettingsScreen from '../pages/SettingsScreen';
import BlockchainScreen from '../pages/BlockchainScreen';
import TradeScreen from '../pages/TradeScreen';
import SecurityScreen from '../pages/SecurityScreen';

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          switch (route.name) {
            case 'Home':
              iconName = focused ? 'home' : 'home-outline';
              break;
            case 'Wallet':
              iconName = focused ? 'wallet' : 'wallet-outline';
              break;
            case 'NFT':
              iconName = focused ? 'images' : 'images-outline';
              break;
            case 'DApps':
              iconName = focused ? 'apps' : 'apps-outline';
              break;
            case 'HCare':
              iconName = focused ? 'medical' : 'medical-outline';
              break;
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: COLORS.highlight,
        tabBarInactiveTintColor: COLORS.textSecondary,
        tabBarStyle: {
          backgroundColor: COLORS.primary,
          borderTopColor: COLORS.border,
          borderTopWidth: 1,
          paddingBottom: 5,
          paddingTop: 5,
          height: 60,
        },
        headerStyle: {
          backgroundColor: COLORS.primary,
        },
        headerTintColor: COLORS.text,
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Wallet" component={WalletScreen} />
      <Tab.Screen name="NFT" component={NFTScreen} />
      <Tab.Screen name="DApps" component={DAppsScreen} />
      <Tab.Screen name="HCare" component={HCareScreen} />
    </Tab.Navigator>
  );
}

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerStyle: {
            backgroundColor: COLORS.primary,
          },
          headerTintColor: COLORS.text,
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      >
        <Stack.Screen
          name="MainTabs"
          component={MainTabs}
          options={{ headerShown: false }}
        />
        <Stack.Screen name="Settings" component={SettingsScreen} />
        <Stack.Screen name="Blockchain" component={BlockchainScreen} />
        <Stack.Screen name="Trade" component={TradeScreen} />
        <Stack.Screen name="Security" component={SecurityScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
