/**
 * Blockchain Screen
 * Blockchain and oracle information
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  RefreshControl,
} from 'react-native';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { BlockchainService, OracleService } from '../services';

export default function BlockchainScreen() {
  const [syncData, setSyncData] = useState(null);
  const [priceFeeds, setPriceFeeds] = useState([]);
  const [marketData, setMarketData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const sync = await BlockchainService.syncBlockchain();
      if (sync.success) {
        setSyncData(sync);
      }

      const feeds = await OracleService.getMultiplePriceFeeds();
      if (feeds.success) {
        setPriceFeeds(feeds.feeds);
      }

      const market = await OracleService.getMarketData();
      if (market.success) {
        setMarketData(market);
      }
    } catch (error) {
      console.error('Error loading data:', error);
    } finally {
      setLoading(false);
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadData();
    setRefreshing(false);
  };

  return (
    <View style={styles.container}>
      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.content}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={COLORS.highlight} />
        }
      >
        {/* Blockchain Status */}
        <Card title="Blockchain Status">
          <StatusBadge status="active" label="Connected" />
          {syncData && (
            <>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Latest Block:</Text>
                <Text style={styles.infoValue}>{syncData.latestBlock}</Text>
              </View>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Transactions:</Text>
                <Text style={styles.infoValue}>{syncData.transactions}</Text>
              </View>
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Last Synced:</Text>
                <Text style={styles.infoValue}>
                  {new Date(syncData.syncedAt).toLocaleString()}
                </Text>
              </View>
            </>
          )}
          <Button
            title="Sync Now"
            onPress={loadData}
            loading={loading}
            variant="outline"
            style={styles.syncButton}
          />
        </Card>

        {/* Market Data */}
        {marketData && (
          <Card title="Market Data">
            <View style={styles.marketGrid}>
              <View style={styles.marketItem}>
                <Text style={styles.marketLabel}>Market Cap</Text>
                <Text style={styles.marketValue}>
                  ${(parseFloat(marketData.marketCap) / 1000000).toFixed(2)}M
                </Text>
              </View>
              <View style={styles.marketItem}>
                <Text style={styles.marketLabel}>24h Volume</Text>
                <Text style={styles.marketValue}>
                  ${(parseFloat(marketData.volume24h) / 1000000).toFixed(2)}M
                </Text>
              </View>
              <View style={styles.marketItem}>
                <Text style={styles.marketLabel}>Circulating Supply</Text>
                <Text style={styles.marketValue}>
                  {(parseFloat(marketData.circulatingSupply) / 1000000).toFixed(0)}M
                </Text>
              </View>
              <View style={styles.marketItem}>
                <Text style={styles.marketLabel}>Dominance</Text>
                <Text style={styles.marketValue}>{marketData.dominance}%</Text>
              </View>
            </View>
          </Card>
        )}

        {/* Price Feeds */}
        <Card title="Oracle Price Feeds">
          {priceFeeds.map((feed, index) => (
            <View key={index} style={styles.feedItem}>
              <View style={styles.feedLeft}>
                <Text style={styles.feedAsset}>{feed.asset}</Text>
                <Text style={styles.feedTime}>
                  {new Date(feed.timestamp).toLocaleTimeString()}
                </Text>
              </View>
              <View style={styles.feedRight}>
                <Text style={styles.feedPrice}>${feed.price}</Text>
                <Text
                  style={[
                    styles.feedChange,
                    { color: parseFloat(feed.change24h) >= 0 ? COLORS.success : COLORS.error },
                  ]}
                >
                  {parseFloat(feed.change24h) >= 0 ? '+' : ''}
                  {feed.change24h}%
                </Text>
              </View>
            </View>
          ))}
        </Card>

        {/* Network Info */}
        <Card title="Network Information">
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Network Name:</Text>
            <Text style={styles.infoValue}>AIELONCHAIN338</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Chain ID:</Text>
            <Text style={styles.infoValue}>338</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>RPC URL:</Text>
            <Text style={styles.rpcUrl}>https://rpc.aielon.io</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Explorer:</Text>
            <Text style={styles.rpcUrl}>https://explorer.aielon.io</Text>
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
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: SPACING.md,
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
  rpcUrl: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.highlight,
    fontFamily: 'monospace',
  },
  syncButton: {
    marginTop: SPACING.md,
  },
  marketGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginTop: SPACING.sm,
  },
  marketItem: {
    width: '48%',
    backgroundColor: COLORS.accent,
    padding: SPACING.md,
    borderRadius: 8,
    marginBottom: SPACING.sm,
  },
  marketLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginBottom: SPACING.xs,
  },
  marketValue: {
    fontSize: FONT_SIZES.lg,
    color: COLORS.text,
    fontWeight: 'bold',
  },
  feedItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  feedLeft: {
    flex: 1,
  },
  feedAsset: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  feedTime: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  feedRight: {
    alignItems: 'flex-end',
  },
  feedPrice: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  feedChange: {
    fontSize: FONT_SIZES.sm,
    fontWeight: '600',
    marginTop: SPACING.xs,
  },
});
