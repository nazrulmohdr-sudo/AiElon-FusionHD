/**
 * HCare Screen
 * Healthcare OS interface
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { Card, Button, StatusBadge } from '../components';
import { COLORS, SPACING, FONT_SIZES } from '../constants';
import { HCareService } from '../services';

export default function HCareScreen() {
  const [profile, setProfile] = useState(null);
  const [appointments, setAppointments] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadHealthData();
  }, []);

  const loadHealthData = async () => {
    setLoading(true);
    try {
      const profileResult = await HCareService.getHealthProfile('user123');
      if (profileResult.success) {
        setProfile(profileResult.profile);
      }

      const appointmentsResult = await HCareService.getAppointments('user123');
      if (appointmentsResult.success) {
        setAppointments(appointmentsResult.appointments);
      }

      const recsResult = await HCareService.getHealthRecommendations();
      if (recsResult.success) {
        setRecommendations(recsResult.recommendations);
      }
    } catch (error) {
      console.error('Error loading health data:', error);
    } finally {
      setLoading(false);
    }
  };

  const bookAppointment = () => {
    Alert.alert(
      'Book Appointment',
      'Schedule a health appointment',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Book',
          onPress: async () => {
            const result = await HCareService.bookAppointment({
              type: 'General Checkup',
            });
            if (result.success) {
              Alert.alert('Success', 'Appointment booked successfully');
              loadHealthData();
            }
          },
        },
      ]
    );
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Health Profile */}
        {profile && (
          <Card title="Health Profile">
            <View style={styles.profileHeader}>
              <View style={styles.healthScore}>
                <Text style={styles.scoreValue}>{profile.healthScore}</Text>
                <Text style={styles.scoreLabel}>Health Score</Text>
              </View>
              <View style={styles.profileInfo}>
                <View style={styles.infoRow}>
                  <Text style={styles.infoLabel}>Age:</Text>
                  <Text style={styles.infoValue}>{profile.age}</Text>
                </View>
                <View style={styles.infoRow}>
                  <Text style={styles.infoLabel}>Blood Type:</Text>
                  <Text style={styles.infoValue}>{profile.bloodType}</Text>
                </View>
              </View>
            </View>
          </Card>
        )}

        {/* Quick Actions */}
        <Card title="Quick Actions">
          <View style={styles.actionGrid}>
            <TouchableOpacity style={styles.actionItem} onPress={bookAppointment}>
              <View style={styles.actionIcon}>
                <Ionicons name="calendar" size={28} color={COLORS.highlight} />
              </View>
              <Text style={styles.actionText}>Book Appointment</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.actionItem}>
              <View style={styles.actionIcon}>
                <Ionicons name="fitness" size={28} color={COLORS.highlight} />
              </View>
              <Text style={styles.actionText}>Track Metrics</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.actionItem}>
              <View style={styles.actionIcon}>
                <Ionicons name="medkit" size={28} color={COLORS.highlight} />
              </View>
              <Text style={styles.actionText}>Medications</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.actionItem}>
              <View style={styles.actionIcon}>
                <Ionicons name="document-text" size={28} color={COLORS.highlight} />
              </View>
              <Text style={styles.actionText}>Records</Text>
            </TouchableOpacity>
          </View>
        </Card>

        {/* Appointments */}
        <Card title="Upcoming Appointments">
          {appointments.length > 0 ? (
            appointments.map((apt) => (
              <View key={apt.id} style={styles.appointmentItem}>
                <View style={styles.aptIcon}>
                  <Ionicons name="medical" size={24} color={COLORS.highlight} />
                </View>
                <View style={styles.aptInfo}>
                  <Text style={styles.aptType}>{apt.type}</Text>
                  <Text style={styles.aptDoctor}>{apt.doctor}</Text>
                  <Text style={styles.aptDate}>
                    {new Date(apt.date).toLocaleDateString()} at {apt.time}
                  </Text>
                </View>
                <StatusBadge status="success" label={apt.status} />
              </View>
            ))
          ) : (
            <Text style={styles.emptyText}>No upcoming appointments</Text>
          )}
        </Card>

        {/* Health Recommendations */}
        <Card title="Health Recommendations">
          {recommendations.map((rec) => (
            <View key={rec.id} style={styles.recommendationItem}>
              <View style={[styles.priorityDot, { 
                backgroundColor: rec.priority === 'high' ? COLORS.error : COLORS.warning 
              }]} />
              <View style={styles.recContent}>
                <Text style={styles.recTitle}>{rec.title}</Text>
                <Text style={styles.recDescription}>{rec.description}</Text>
                <Text style={styles.recType}>{rec.type}</Text>
              </View>
            </View>
          ))}
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
  profileHeader: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  healthScore: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: SPACING.lg,
  },
  scoreValue: {
    fontSize: FONT_SIZES.xxxl,
    fontWeight: 'bold',
    color: COLORS.success,
  },
  scoreLabel: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  profileInfo: {
    flex: 1,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: SPACING.xs,
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
  actionGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginTop: SPACING.sm,
  },
  actionItem: {
    width: '48%',
    alignItems: 'center',
    marginBottom: SPACING.md,
  },
  actionIcon: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: SPACING.xs,
  },
  actionText: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.text,
    textAlign: 'center',
  },
  appointmentItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  aptIcon: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: COLORS.accent,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: SPACING.md,
  },
  aptInfo: {
    flex: 1,
  },
  aptType: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  aptDoctor: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  aptDate: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.highlight,
    marginTop: SPACING.xs,
  },
  recommendationItem: {
    flexDirection: 'row',
    paddingVertical: SPACING.md,
    borderBottomWidth: 1,
    borderBottomColor: COLORS.border,
  },
  priorityDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    marginTop: 6,
    marginRight: SPACING.md,
  },
  recContent: {
    flex: 1,
  },
  recTitle: {
    fontSize: FONT_SIZES.md,
    fontWeight: 'bold',
    color: COLORS.text,
  },
  recDescription: {
    fontSize: FONT_SIZES.sm,
    color: COLORS.textSecondary,
    marginTop: SPACING.xs,
  },
  recType: {
    fontSize: FONT_SIZES.xs,
    color: COLORS.highlight,
    marginTop: SPACING.xs,
    fontWeight: '600',
  },
  emptyText: {
    fontSize: FONT_SIZES.md,
    color: COLORS.textSecondary,
    textAlign: 'center',
    paddingVertical: SPACING.lg,
  },
});
