# API Documentation - AiElon Living OS v2.0.0

## Overview

This document provides comprehensive API documentation for integrating with AiElon Living OS.

## Base URL

```
http://localhost:3000
```

## Authentication

Most API endpoints require authentication. Include the authentication token in the request header:

```
Authorization: Bearer <your_token>
```

## Core System APIs

### Get System Status

Get the current status of the AiElon Living OS.

**Endpoint**: `GET /api/status`

**Response**:
```json
{
  "version": "2.0.0",
  "initialized": true,
  "modules": {
    "core": true,
    "ui": true,
    "wallet": true,
    "hcare": true,
    "ummahHub": true,
    "blockchain": true
  }
}
```

## Blockchain APIs

### Get Network Info

Get information about the AielonChain338 network.

**Endpoint**: `GET /api/blockchain/network`

**Response**:
```json
{
  "networkId": 338,
  "chainName": "AielonChain338",
  "blockHeight": 1000000,
  "peers": 150,
  "version": "338.2.0"
}
```

### Create Transaction

Create a new blockchain transaction.

**Endpoint**: `POST /api/blockchain/transaction`

**Request Body**:
```json
{
  "from": "0x123...",
  "to": "0x456...",
  "amount": 100,
  "data": {
    "memo": "Payment for services"
  }
}
```

**Response**:
```json
{
  "id": "tx_abc123...",
  "hash": "0xdef456...",
  "status": "pending",
  "timestamp": "2025-11-11T13:00:00.000Z"
}
```

### Get Transaction

Get transaction details by ID.

**Endpoint**: `GET /api/blockchain/transaction/:txId`

**Response**:
```json
{
  "id": "tx_abc123...",
  "hash": "0xdef456...",
  "from": "0x123...",
  "to": "0x456...",
  "amount": 100,
  "status": "confirmed",
  "timestamp": "2025-11-11T13:00:00.000Z"
}
```

## Halal Wallet APIs

### Create Wallet

Create a new Halal Wallet.

**Endpoint**: `POST /api/wallet/create`

**Request Body**:
```json
{
  "userId": "user_123",
  "options": {
    "zakatEnabled": true
  }
}
```

**Response**:
```json
{
  "walletId": "wallet_abc123",
  "address": "0x789...",
  "publicKey": "0xabc...",
  "recoveryPhrase": "word1 word2 word3 ..."
}
```

### Get Balance

Get wallet balance.

**Endpoint**: `GET /api/wallet/:walletId/balance`

**Response**:
```json
{
  "walletId": "wallet_abc123",
  "balance": 1500.50,
  "currency": "AIELON"
}
```

### Send Transaction

Send a transaction from wallet.

**Endpoint**: `POST /api/wallet/:walletId/send`

**Request Body**:
```json
{
  "to": "0x456...",
  "amount": 100,
  "memo": "Payment"
}
```

**Response**:
```json
{
  "transaction": {
    "id": "tx_abc123",
    "hash": "0xdef456",
    "status": "broadcasted"
  }
}
```

### Calculate Zakat

Calculate Zakat for a wallet.

**Endpoint**: `GET /api/wallet/:walletId/zakat`

**Response**:
```json
{
  "amount": 37.50,
  "balance": 1500,
  "threshold": 85,
  "rate": 0.025,
  "dueDate": "2026-11-11T13:00:00.000Z"
}
```

### Pay Zakat

Pay Zakat from wallet.

**Endpoint**: `POST /api/wallet/:walletId/zakat/pay`

**Request Body**:
```json
{
  "recipientAddress": "0x999..."
}
```

**Response**:
```json
{
  "transaction": {
    "id": "tx_zakat123",
    "hash": "0xzakat456"
  },
  "zakatAmount": 37.50,
  "paidAt": "2025-11-11T13:00:00.000Z"
}
```

## HCare System APIs

### Register Patient

Register a new patient.

**Endpoint**: `POST /api/hcare/patient/register`

**Request Body**:
```json
{
  "personalInfo": {
    "name": "John Doe",
    "dateOfBirth": "1990-01-01",
    "gender": "male"
  },
  "demographics": {
    "address": "123 Main St",
    "phone": "+1234567890"
  },
  "emergencyContact": {
    "name": "Jane Doe",
    "phone": "+0987654321"
  }
}
```

**Response**:
```json
{
  "patientId": "patient_abc123",
  "success": true,
  "message": "Patient registered successfully"
}
```

### Add Vitals

Add vital signs to health record.

**Endpoint**: `POST /api/hcare/patient/:patientId/vitals`

**Request Body**:
```json
{
  "bloodPressure": "120/80",
  "heartRate": 72,
  "temperature": 37.0,
  "weight": 70,
  "height": 175
}
```

**Response**:
```json
{
  "id": "vital_123",
  "timestamp": "2025-11-11T13:00:00.000Z",
  "bloodPressure": "120/80",
  "heartRate": 72
}
```

### Schedule Appointment

Schedule a medical appointment.

**Endpoint**: `POST /api/hcare/appointment/schedule`

**Request Body**:
```json
{
  "patientId": "patient_abc123",
  "provider": "Dr. Smith",
  "type": "consultation",
  "date": "2025-11-15",
  "time": "10:00",
  "telehealth": false
}
```

**Response**:
```json
{
  "id": "appt_123",
  "status": "scheduled",
  "createdAt": "2025-11-11T13:00:00.000Z"
}
```

## Ummah Hub APIs

### Register User

Register a new user on Ummah Hub.

**Endpoint**: `POST /api/ummah/user/register`

**Request Body**:
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "displayName": "John Doe",
  "location": "New York"
}
```

**Response**:
```json
{
  "userId": "user_abc123",
  "username": "johndoe",
  "success": true
}
```

### Create Post

Create a new post.

**Endpoint**: `POST /api/ummah/post/create`

**Request Body**:
```json
{
  "userId": "user_abc123",
  "content": "This is my post content",
  "visibility": "public",
  "tags": ["islam", "community"]
}
```

**Response**:
```json
{
  "id": "post_abc123",
  "userId": "user_abc123",
  "content": "This is my post content",
  "createdAt": "2025-11-11T13:00:00.000Z"
}
```

### Send Message

Send a direct message to another user.

**Endpoint**: `POST /api/ummah/message/send`

**Request Body**:
```json
{
  "from": "user_abc123",
  "to": "user_def456",
  "content": "Hello, how are you?"
}
```

**Response**:
```json
{
  "messageId": "msg_abc123",
  "sent": true,
  "encrypted": true
}
```

### Create Community

Create a new community.

**Endpoint**: `POST /api/ummah/community/create`

**Request Body**:
```json
{
  "userId": "user_abc123",
  "name": "Tech Muslims",
  "description": "Community for Muslim tech professionals",
  "category": "technology",
  "privacy": "public"
}
```

**Response**:
```json
{
  "id": "community_abc123",
  "name": "Tech Muslims",
  "creatorId": "user_abc123",
  "createdAt": "2025-11-11T13:00:00.000Z"
}
```

## Error Handling

All API endpoints follow standard HTTP status codes:

- `200 OK`: Successful request
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

**Error Response Format**:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {}
  }
}
```

## Rate Limiting

API requests are rate-limited to:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated requests

## Pagination

List endpoints support pagination:

**Parameters**:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)

**Response**:
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}
```

## Webhooks

Configure webhooks to receive real-time notifications:

**Available Events**:
- `transaction.confirmed`
- `wallet.created`
- `appointment.scheduled`
- `message.received`
- `post.created`

---

For more information, visit the [Developer Guide](DEVELOPER.md).
