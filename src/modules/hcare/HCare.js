/**
 * HCare - Healthcare Management Module
 * Comprehensive health monitoring and care management system
 */

import { globalState } from '../../core/StateManager.js';
import { securityManager } from '../../security/SecurityManager.js';

export class HCare {
  constructor() {
    this.patients = new Map();
    this.appointments = [];
    this.healthRecords = new Map();
    this.providers = new Map();
  }

  /**
   * Register a new patient
   * @param {Object} patientInfo - Patient information
   * @returns {Object} Registration result
   */
  registerPatient(patientInfo) {
    const { name, dateOfBirth, bloodType, allergies = [] } = patientInfo;
    
    const patientId = this.generatePatientId();
    const patient = {
      id: patientId,
      name,
      dateOfBirth,
      bloodType,
      allergies,
      registeredAt: Date.now(),
      medicalHistory: [],
      vitals: {}
    };
    
    // Encrypt sensitive data
    patient.nameEncrypted = securityManager.encrypt(name);
    
    this.patients.set(patientId, patient);
    globalState.set('totalPatients', this.patients.size);
    
    return {
      success: true,
      patientId,
      message: 'Patient registered successfully'
    };
  }

  /**
   * Record health vitals
   * @param {string} patientId - Patient ID
   * @param {Object} vitals - Health vitals
   * @returns {Object} Recording result
   */
  recordVitals(patientId, vitals) {
    const patient = this.patients.get(patientId);
    if (!patient) {
      return { success: false, error: 'Patient not found' };
    }
    
    const vitalRecord = {
      timestamp: Date.now(),
      heartRate: vitals.heartRate,
      bloodPressure: vitals.bloodPressure,
      temperature: vitals.temperature,
      oxygenLevel: vitals.oxygenLevel,
      weight: vitals.weight
    };
    
    patient.vitals = vitalRecord;
    
    // Analyze vitals for alerts
    const alerts = this.analyzeVitals(vitalRecord);
    
    return {
      success: true,
      vitals: vitalRecord,
      alerts
    };
  }

  /**
   * Analyze vitals for health alerts
   * @private
   */
  analyzeVitals(vitals) {
    const alerts = [];
    
    if (vitals.heartRate > 100 || vitals.heartRate < 60) {
      alerts.push({
        severity: 'warning',
        message: 'Abnormal heart rate detected'
      });
    }
    
    if (vitals.temperature > 37.5) {
      alerts.push({
        severity: 'warning',
        message: 'Elevated body temperature'
      });
    }
    
    if (vitals.oxygenLevel < 95) {
      alerts.push({
        severity: 'critical',
        message: 'Low oxygen saturation'
      });
    }
    
    return alerts;
  }

  /**
   * Schedule appointment
   * @param {string} patientId - Patient ID
   * @param {string} providerId - Healthcare provider ID
   * @param {number} scheduledTime - Appointment time
   * @param {string} type - Appointment type
   * @returns {Object} Appointment details
   */
  scheduleAppointment(patientId, providerId, scheduledTime, type = 'general') {
    const patient = this.patients.get(patientId);
    const provider = this.providers.get(providerId);
    
    if (!patient) {
      return { success: false, error: 'Patient not found' };
    }
    
    if (!provider) {
      return { success: false, error: 'Provider not found' };
    }
    
    const appointment = {
      id: this.generateAppointmentId(),
      patientId,
      providerId,
      scheduledTime,
      type,
      status: 'scheduled',
      createdAt: Date.now()
    };
    
    this.appointments.push(appointment);
    globalState.set('totalAppointments', this.appointments.length);
    
    return {
      success: true,
      appointment
    };
  }

  /**
   * Add medical record
   * @param {string} patientId - Patient ID
   * @param {Object} record - Medical record
   * @returns {Object} Result
   */
  addMedicalRecord(patientId, record) {
    const patient = this.patients.get(patientId);
    if (!patient) {
      return { success: false, error: 'Patient not found' };
    }
    
    const medicalRecord = {
      id: this.generateRecordId(),
      timestamp: Date.now(),
      diagnosis: securityManager.encrypt(record.diagnosis),
      treatment: securityManager.encrypt(record.treatment),
      medications: record.medications || [],
      notes: securityManager.encrypt(record.notes || '')
    };
    
    patient.medicalHistory.push(medicalRecord);
    
    return {
      success: true,
      recordId: medicalRecord.id
    };
  }

  /**
   * Get patient health dashboard
   * @param {string} patientId - Patient ID
   * @returns {Object} Health dashboard
   */
  getHealthDashboard(patientId) {
    const patient = this.patients.get(patientId);
    if (!patient) {
      return { error: 'Patient not found' };
    }
    
    const upcomingAppointments = this.appointments.filter(
      apt => apt.patientId === patientId && apt.status === 'scheduled'
    );
    
    return {
      patient: {
        id: patient.id,
        name: patient.name,
        bloodType: patient.bloodType
      },
      latestVitals: patient.vitals,
      upcomingAppointments,
      recordCount: patient.medicalHistory.length,
      healthScore: this.calculateHealthScore(patient)
    };
  }

  /**
   * Calculate health score
   * @private
   */
  calculateHealthScore(patient) {
    if (!patient.vitals || !patient.vitals.heartRate) {
      return 85; // Default score
    }
    
    let score = 100;
    const vitals = patient.vitals;
    
    if (vitals.heartRate > 100 || vitals.heartRate < 60) score -= 10;
    if (vitals.temperature > 37.5) score -= 15;
    if (vitals.oxygenLevel < 95) score -= 20;
    
    return Math.max(score, 0);
  }

  /**
   * Register healthcare provider
   * @param {Object} providerInfo - Provider information
   * @returns {Object} Registration result
   */
  registerProvider(providerInfo) {
    const providerId = this.generateProviderId();
    const provider = {
      id: providerId,
      name: providerInfo.name,
      specialty: providerInfo.specialty,
      license: providerInfo.license,
      registeredAt: Date.now()
    };
    
    this.providers.set(providerId, provider);
    
    return {
      success: true,
      providerId
    };
  }

  /**
   * Generate patient ID
   * @private
   */
  generatePatientId() {
    return `PAT${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate appointment ID
   * @private
   */
  generateAppointmentId() {
    return `APT${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate record ID
   * @private
   */
  generateRecordId() {
    return `REC${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Generate provider ID
   * @private
   */
  generateProviderId() {
    return `PRV${Date.now()}${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Get system statistics
   * @returns {Object} HCare statistics
   */
  getStatistics() {
    return {
      totalPatients: this.patients.size,
      totalProviders: this.providers.size,
      totalAppointments: this.appointments.length,
      scheduledAppointments: this.appointments.filter(a => a.status === 'scheduled').length
    };
  }
}

export const hcare = new HCare();
