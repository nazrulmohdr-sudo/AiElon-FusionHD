/**
 * Navigation Types
 * Type definitions for navigation throughout the app
 */

import { NativeStackScreenProps } from '@react-navigation/native-stack';

export type RootStackParamList = {
  Home: undefined;
  Wallet: undefined;
};

export type HomeScreenProps = NativeStackScreenProps<RootStackParamList, 'Home'>;
export type WalletScreenProps = NativeStackScreenProps<RootStackParamList, 'Wallet'>;

declare global {
  namespace ReactNavigation {
    interface RootParamList extends RootStackParamList {}
  }
}
