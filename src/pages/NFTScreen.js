/**
 * NFT Screen
 * View and manage NFTs
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Image,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { NFTService } from '../services';

export default function NFTScreen() {
  const [nfts, setNfts] = useState([]);
  const [collections, setCollections] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedTab, setSelectedTab] = useState('my-nfts');

  useEffect(() => {
    loadNFTs();
    loadCollections();
  }, []);

  const loadNFTs = async () => {
    setLoading(true);
    try {
      const result = await NFTService.getUserNFTs('user_address');
      if (result.success) {
        setNfts(result.nfts);
      }
    } catch (error) {
      console.error('Error loading NFTs:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadCollections = async () => {
    try {
      const result = await NFTService.getCollections();
      if (result.success) {
        setCollections(result.collections);
      }
    } catch (error) {
      console.error('Error loading collections:', error);
    }
  };

  const mintNFT = async () => {
    Alert.alert(
      'Mint NFT',
      'This will create a new NFT in your collection',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Mint',
          onPress: async () => {
            setLoading(true);
            try {
              const result = await NFTService.mintNFT({
                name: 'New NFT #' + Date.now(),
                description: 'A unique digital asset',
                owner: 'user_address',
              });
              if (result.success) {
                Alert.alert('Success', 'NFT minted successfully!');
                loadNFTs();
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

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Tabs */}
        <View style={styles.tabs}>
          <TouchableOpacity
            style={[styles.tab, selectedTab === 'my-nfts' && styles.tabActive]}
            onPress={() => setSelectedTab('my-nfts')}
          >
            <Text style={[styles.tabText, selectedTab === 'my-nfts' && styles.tabTextActive]}>
              My NFTs
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, selectedTab === 'collections' && styles.tabActive]}
            onPress={() => setSelectedTab('collections')}
          >
            <Text style={[styles.tabText, selectedTab === 'collections' && styles.tabTextActive]}>
              Collections
            </Text>
          </TouchableOpacity>
        </View>

        {selectedTab === 'my-nfts' ? (
          <>
            {/* Summary */}
            <Card>
              <View style={styles.summaryRow}>
                <View style={styles.summaryItem}>
                  <Text style={styles.summaryValue}>{nfts.length}</Text>
                  <Text style={styles.summaryLabel}>Total NFTs</Text>
                </View>
                <View style={styles.summaryDivider} />
                <View style={styles.summaryItem}>
                  <Text style={styles.summaryValue}>{collections.length}</Text>
                  <Text style={styles.summaryLabel}>Collections</Text>
                </View>
              </View>
            </Card>

            {/* Mint Button */}
            <Button
              title="Mint New NFT"
              onPress={mintNFT}
              loading={loading}
              style={styles.mintButton}
            />

            {/* NFT Grid */}
            <View style={styles.nftGrid}>
              {nfts.map((nft) => (
                <TouchableOpacity key={nft.id} style={styles.nftCard}>
                  <Image source={{ uri: nft.image }} style={styles.nftImage} />
                  <View style={styles.nftInfo}>
                    <Text style={styles.nftName} numberOfLines={1}>
                      {nft.name}
                    </Text>
                    <Text style={styles.nftCollection} numberOfLines={1}>
                      {nft.collection}
                    </Text>
                    <StatusBadge status="success" label={nft.rarity} />
                  </View>
                </TouchableOpacity>
              ))}
            </View>

            {nfts.length === 0 && !loading && (
              <Card>
                <Text style={styles.emptyText}>No NFTs yet. Mint your first NFT!</Text>
              </Card>
            )}
          </>
        ) : (
          <>
            {/* Collections List */}
            {collections.map((collection) => (
              <Card key={collection.id} style={styles.collectionCard}>
                <View style={styles.collectionHeader}>
                  <View style={styles.collectionIcon}>
                    <Ionicons name="images" size={24} color={COLORS.highlight} />
                  </View>
                  <View style={styles.collectionInfo}>
                    <Text style={styles.collectionName}>{collection.name}</Text>
                    <Text style={styles.collectionDescription}>{collection.description}</Text>
                  </View>
                </View>
                <View style={styles.collectionStats}>
                  <View style={styles.stat}>
                    <Text style={styles.statLabel}>Supply:</Text>
                    <Text style={styles.statValue}>{collection.totalSupply}</Text>
                  </View>
                  <View style={styles.stat}>
                    <Text style={styles.statLabel}>Floor:</Text>
                    <Text style={styles.statValue}>{collection.floorPrice}</Text>
                  </View>
                </View>
              </Card>
            ))}
          </>
        )}
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
  tabs: {
    flexDirection: 'row',
    backgroundColor: COLORS.card,
    borderRadius: 8,
    padding: SPACING.xs,
    marginBottom: SPACING.md,
  },
  tab: {
    flex: 1,
    paddingVertical: SPACING.sm,
    alignItems: 'center',
    borderRadius: 6,
  },
  tabActive: {
    backgroundColor: COLORS.highlight,
  },
  tabText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
  },
  tabTextActive: {
    color: COLORS.text,
    fontWeight: 'bold',
  },
  summaryRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
  },
  summaryItem: {
    alignItems: 'center',
    flex: 1,
  },
  summaryDivider: {
    width: 1,
    height: 40,
    backgroundColor: COLORS.border,
  },
  summaryValue: {
    fontSize: FONT_SIZES.xxl,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  summaryLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  mintButton: {
    marginBottom: SPACING.md,
  },
  nftGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: SPACING.md,
    justifyContent: 'space-between',
  },
  nftCard: {
    width: '48%',
    backgroundColor: COLORS.card,
    borderRadius: 12,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: COLORS.border,
  },
  nftImage: {
    width: '100%',
    height: 150,
    backgroundColor: COLORS.accent,
  },
  nftInfo: {
    padding: SPACING.sm,
  },
  nftName: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
    marginBottom: SPACING.xs,
  },
  nftCollection: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginBottom: SPACING.xs,
  },
  emptyText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    textAlign: 'center',
    paddingVertical: SPACING.lg,
  },
  collectionCard: {
    marginBottom: SPACING.md,
  },
  collectionHeader: {
    flexDirection: 'row',
    marginBottom: SPACING.md,
  },
  collectionIcon: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: SPACING.md,
  },
  collectionInfo: {
    flex: 1,
  },
  collectionName: {
    fontSize: FONT_SIZES.lg,
    fontWeight: 'bold',
    color: COLORS.text,
    marginBottom: SPACING.xs,
  },
  collectionDescription: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
  },
  collectionStats: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingTop: SPACING.md,
    borderTopWidth: 1,
    borderTopColor: COLORS.border,
  },
  stat: {
    alignItems: 'center',
  },
  statLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
  },
  statValue: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
    marginTop: SPACING.xs,
  },
});
