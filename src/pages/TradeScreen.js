/**
 * Trade Screen
 * Trading and bridge interface
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { Trade138Service } from '../services';

export default function TradeScreen() {
  const [tradingPairs, setTradingPairs] = useState([]);
  const [chains, setChains] = useState([]);
  const [selectedFromChain, setSelectedFromChain] = useState('AIELONCHAIN338');
  const [selectedToChain, setSelectedToChain] = useState('ETH');
  const [amount, setAmount] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const pairsResult = await Trade138Service.getTradingPairs();
      if (pairsResult.success) {
        setTradingPairs(pairsResult.pairs);
      }

      const chainsResult = Trade138Service.getSupportedChains();
      if (chainsResult.success) {
        setChains(chainsResult.chains);
      }
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  const handleBridge = async () => {
    if (!amount || parseFloat(amount) <= 0) {
      Alert.alert('Error', 'Please enter a valid amount');
      return;
    }

    Alert.alert(
      'Confirm Bridge Transfer',
      `Transfer ${amount} AIELON from ${selectedFromChain} to ${selectedToChain}?`,
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Confirm',
          onPress: async () => {
            setLoading(true);
            try {
              const result = await Trade138Service.bridgeTransfer(
                selectedFromChain,
                selectedToChain,
                amount,
                'AIELON'
              );
              if (result.success) {
                Alert.alert(
                  'Success',
                  `Bridge transfer initiated!\nTx: ${result.transfer.transactionHash.substring(0, 10)}...`
                );
                setAmount('');
              }
            } catch (error) {
              Alert.alert('Error', error.message);
            } finally {
              setLoading(false);
            }
          },
        },
      ]
    );
  };

  const handleTrade = async (pair) => {
    Alert.alert(
      'Execute Trade',
      `Trade ${pair.pair}?`,
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Buy',
          onPress: async () => {
            const result = await Trade138Service.executeTrade(pair.pair, '100', 'buy');
            if (result.success) {
              Alert.alert('Success', `Trade executed! Order ID: ${result.orderId}`);
            }
          },
        },
      ]
    );
  };

  const swapChains = () => {
    const temp = selectedFromChain;
    setSelectedFromChain(selectedToChain);
    setSelectedToChain(temp);
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Bridge Section */}
        <Card title="Cross-Chain Bridge">
          <Text style={styles.sectionLabel}>From Chain</Text>
          <View style={styles.chainSelector}>
            {chains.map((chain) => (
              <TouchableOpacity
                key={chain.id}
                style={[
                  styles.chainOption,
                  selectedFromChain === chain.name && styles.chainOptionActive,
                ]}
                onPress={() => setSelectedFromChain(chain.name)}
              >
                <Text
                  style={[
                    styles.chainText,
                    selectedFromChain === chain.name && styles.chainTextActive,
                  ]}
                >
                  {chain.name}
                </Text>
              </TouchableOpacity>
            ))}
          </View>

          <TouchableOpacity style={styles.swapButton} onPress={swapChains}>
            <Ionicons name="swap-vertical" size={24} color={COLORS.highlight} />
          </TouchableOpacity>

          <Text style={styles.sectionLabel}>To Chain</Text>
          <View style={styles.chainSelector}>
            {chains.map((chain) => (
              <TouchableOpacity
                key={chain.id}
                style={[
                  styles.chainOption,
                  selectedToChain === chain.name && styles.chainOptionActive,
                ]}
                onPress={() => setSelectedToChain(chain.name)}
              >
                <Text
                  style={[
                    styles.chainText,
                    selectedToChain === chain.name && styles.chainTextActive,
                  ]}
                >
                  {chain.name}
                </Text>
              </TouchableOpacity>
            ))}
          </View>

          <Text style={styles.sectionLabel}>Amount</Text>
          <TextInput
            style={styles.input}
            placeholder="Enter amount"
            placeholderTextColor={COLORS.textSecondary}
            value={amount}
            onChangeText={setAmount}
            keyboardType="numeric"
          />

          <Button
            title="Bridge Transfer"
            onPress={handleBridge}
            loading={loading}
            style={styles.bridgeButton}
          />

          <View style={styles.feeInfo}>
            <Text style={styles.feeLabel}>Bridge Fee:</Text>
            <Text style={styles.feeValue}>0.1%</Text>
          </View>
          <View style={styles.feeInfo}>
            <Text style={styles.feeLabel}>Estimated Time:</Text>
            <Text style={styles.feeValue}>5-10 minutes</Text>
          </View>
        </Card>

        {/* Trading Pairs */}
        <Card title="Trading Pairs">
          {tradingPairs.map((pair, index) => (
            <TouchableOpacity
              key={index}
              style={styles.pairItem}
              onPress={() => handleTrade(pair)}
            >
              <View style={styles.pairLeft}>
                <Text style={styles.pairName}>{pair.pair}</Text>
                <Text
                  style={[
                    styles.pairChange,
                    { color: parseFloat(pair.change24h) >= 0 ? COLORS.success : COLORS.error },
                  ]}
                >
                  {parseFloat(pair.change24h) >= 0 ? '+' : ''}
                  {pair.change24h}%
                </Text>
              </View>
              <View style={styles.pairRight}>
                <Text style={styles.pairPrice}>${pair.price}</Text>
                <StatusBadge status="active" label="Active" />
              </View>
            </TouchableOpacity>
          ))}
        </Card>

        {/* Bridge Info */}
        <Card title="Bridge Information">
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Supported Chains:</Text>
            <Text style={styles.infoValue}>{chains.length}</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Total Volume:</Text>
            <Text style={styles.infoValue}>$1.2M</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Bridge Status:</Text>
            <StatusBadge status="active" label="Online" />
          </View>
        </Card>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: COLORS.background,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: SPACING.md,
  },
  sectionLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    marginTop: SPACING.md,
    marginBottom: SPACING.sm,
  },
  chainSelector: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: SPACING.sm,
  },
  chainOption: {
    paddingVertical: SPACING.sm,
    paddingHorizontal: SPACING.md,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: COLORS.border,
    backgroundColor: COLORS.accent,
  },
  chainOptionActive: {
    borderColor: COLORS.highlight,
    backgroundColor: COLORS.highlight + '20',
  },
  chainText: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    fontWeight: '600',
  },
  chainTextActive: {
    color: COLORS.highlight,
  },
  swapButton: {
    alignSelf: 'center',
    marginVertical: SPACING.md,
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    backgroundColor: COLORS.accent,
    borderRadius: 8,
    padding: SPACING.md,
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  bridgeButton: {
    marginTop: SPACING.md,
  },
  feeInfo: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: SPACING.sm,
  },
  feeLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
  },
  feeValue: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.text,
    fontWeight: '600',
  },
  pairItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  pairLeft: {
    flex: 1,
  },
  pairName: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  pairChange: {
    fontSize: FONT_SIZES.sm,
    fontWeight: '600',
    marginTop: SPACING.xs,
  },
  pairRight: {
    alignItems: 'flex-end',
  },
  pairPrice: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
    marginBottom: SPACING.xs,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginVertical: SPACING.sm,
  },
  infoLabel: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  infoValue: {
    fontSize: FONT_SIZES.md,
    color: COLORS.text,
    fontWeight: '600',
  },
});
