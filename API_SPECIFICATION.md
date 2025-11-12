# AiElon API Specification
## Unified API for the Everything System

**Version**: 1.0.0  
**Base URL**: `https://api.aielon.global/v1`  
**Protocol**: HTTPS, HTTP/2, WebSocket

---

## Overview

The AiElon API provides a unified interface for all subsystems within the Everything System. This document specifies the complete API surface, authentication mechanisms, data formats, and usage patterns.

---

## Authentication

### OAuth 2.0 / OpenID Connect

**Authorization Endpoint**: `https://auth.aielon.global/oauth/authorize`  
**Token Endpoint**: `https://auth.aielon.global/oauth/token`

**Supported Flows**:
- Authorization Code Flow (recommended for web apps)
- Client Credentials Flow (for service-to-service)
- Refresh Token Flow

**Example Token Request**:
```http
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=AUTH_CODE&
redirect_uri=https://app.example.com/callback&
client_id=CLIENT_ID&
client_secret=CLIENT_SECRET
```

**Token Response**:
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "eyJhbGciOiJSUzI1NiIs...",
  "scope": "openid profile email"
}
```

### Using Access Tokens

Include the access token in the Authorization header:

```http
GET /api/v1/users/me
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
```

### API Keys (Service Accounts)

For service-to-service communication:

```http
GET /api/v1/system/health
X-API-Key: your_api_key_here
```

---

## Common Headers

### Request Headers

```http
Authorization: Bearer {access_token}
Content-Type: application/json
Accept: application/json
X-Request-ID: {unique_request_id}
X-Service: {calling_service_name}
Accept-Language: en-US,en;q=0.9
```

### Response Headers

```http
Content-Type: application/json
X-Request-ID: {request_id}
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1636704000
```

---

## Standard Response Format

### Success Response

```json
{
  "status": "success",
  "data": {
    // Response data
  },
  "metadata": {
    "timestamp": "2025-11-12T07:25:43.777Z",
    "requestId": "req_123456"
  }
}
```

### Error Response

```json
{
  "status": "error",
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found",
    "details": {
      "resourceType": "user",
      "resourceId": "user123"
    }
  },
  "metadata": {
    "timestamp": "2025-11-12T07:25:43.777Z",
    "requestId": "req_123456"
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `AUTHENTICATION_FAILED` | 401 | Invalid or expired token |
| `AUTHORIZATION_FAILED` | 403 | Insufficient permissions |
| `RESOURCE_NOT_FOUND` | 404 | Resource doesn't exist |
| `VALIDATION_ERROR` | 400 | Invalid input data |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily down |

---

## API Endpoints

### Core APIs

#### Health Check
```http
GET /api/v1/health
```

**Response**:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "uptime": 86400,
  "services": {
    "database": "healthy",
    "cache": "healthy",
    "messageQueue": "healthy"
  }
}
```

#### System Status
```http
GET /api/v1/system/status
```

**Response**:
```json
{
  "status": "operational",
  "subsystems": {
    "livingOS": "operational",
    "fusionUI": "operational",
    "halalWallet": "operational",
    "hcare": "operational",
    "ummahHub": "operational"
  },
  "metrics": {
    "activeUsers": 1500000,
    "requestsPerSecond": 50000,
    "averageResponseTime": 45
  }
}
```

### User Management

#### Get Current User
```http
GET /api/v1/users/me
Authorization: Bearer {token}
```

**Response**:
```json
{
  "id": "user_123",
  "email": "user@example.com",
  "name": "John Doe",
  "roles": ["user", "premium"],
  "preferences": {
    "theme": "dark",
    "language": "en-US"
  },
  "createdAt": "2025-01-01T00:00:00Z"
}
```

#### Update User Profile
```http
PATCH /api/v1/users/me
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "John Smith",
  "preferences": {
    "theme": "light"
  }
}
```

### AiElon Living OS APIs

#### Get System Metrics
```http
GET /api/v1/living-os/metrics
Authorization: Bearer {token}
```

**Response**:
```json
{
  "cpu": {
    "usage": 45.2,
    "cores": 8,
    "temperature": 65.0
  },
  "memory": {
    "total": 16384,
    "used": 8192,
    "available": 8192
  },
  "disk": {
    "total": 512000,
    "used": 256000,
    "available": 256000
  }
}
```

#### Request Resource Optimization
```http
POST /api/v1/living-os/optimize
Authorization: Bearer {token}
Content-Type: application/json

{
  "service": "hcare-service",
  "targetMetrics": {
    "responseTime": 50,
    "throughput": 10000
  }
}
```

#### AI Assistant Query
```http
POST /api/v1/living-os/assistant/query
Authorization: Bearer {token}
Content-Type: application/json

{
  "query": "What's my next appointment?",
  "context": {
    "userId": "user_123",
    "service": "hcare"
  }
}
```

**Response**:
```json
{
  "answer": "Your next appointment is with Dr. Smith on November 15th at 10:00 AM.",
  "confidence": 0.95,
  "sources": [
    {
      "type": "appointment",
      "id": "appt_456"
    }
  ]
}
```

### Fusion HD UI APIs

#### Get Theme
```http
GET /api/v1/fusion-ui/themes/{theme_id}
Authorization: Bearer {token}
```

#### Get User Preferences
```http
GET /api/v1/fusion-ui/preferences
Authorization: Bearer {token}
```

**Response**:
```json
{
  "theme": "dark",
  "fontSize": "medium",
  "animations": true,
  "accessibility": {
    "highContrast": false,
    "reducedMotion": false
  }
}
```

### Halal Wallet APIs

#### Get Balance
```http
GET /api/v1/halal-wallet/balance
Authorization: Bearer {token}
```

**Response**:
```json
{
  "userId": "user_123",
  "balances": [
    {
      "currency": "USD",
      "amount": 1250.50,
      "reserved": 50.00,
      "available": 1200.50
    }
  ]
}
```

#### Create Payment
```http
POST /api/v1/halal-wallet/payments
Authorization: Bearer {token}
Content-Type: application/json

{
  "amount": 100.00,
  "currency": "USD",
  "purpose": "healthcare_consultation",
  "recipient": "doc_456",
  "metadata": {
    "appointmentId": "appt_789"
  }
}
```

**Response**:
```json
{
  "paymentId": "pay_123",
  "status": "completed",
  "shariahCompliant": true,
  "transactionHash": "0x1234567890abcdef",
  "timestamp": "2025-11-12T07:25:43.777Z",
  "receipt": {
    "url": "https://wallet.aielon.global/receipts/pay_123"
  }
}
```

#### Get Transaction History
```http
GET /api/v1/halal-wallet/transactions
Authorization: Bearer {token}
Query Parameters:
  - limit: 20
  - offset: 0
  - startDate: 2025-01-01
  - endDate: 2025-12-31
  - type: payment,transfer,refund
```

### HCare APIs

#### Get Patient Profile
```http
GET /api/v1/hcare/patients/me
Authorization: Bearer {token}
```

**Response**:
```json
{
  "id": "patient_123",
  "personalInfo": {
    "name": "John Doe",
    "dateOfBirth": "1990-01-01",
    "gender": "male",
    "bloodType": "O+"
  },
  "contactInfo": {
    "email": "john@example.com",
    "phone": "+1234567890"
  },
  "medicalHistory": {
    "allergies": ["penicillin"],
    "chronicConditions": [],
    "medications": []
  }
}
```

#### Book Appointment
```http
POST /api/v1/hcare/appointments
Authorization: Bearer {token}
Content-Type: application/json

{
  "doctorId": "doc_456",
  "datetime": "2025-11-15T10:00:00Z",
  "type": "consultation",
  "reason": "Annual checkup",
  "symptoms": []
}
```

**Response**:
```json
{
  "appointmentId": "appt_789",
  "status": "confirmed",
  "doctor": {
    "id": "doc_456",
    "name": "Dr. Sarah Smith",
    "specialty": "Family Medicine"
  },
  "datetime": "2025-11-15T10:00:00Z",
  "location": {
    "type": "telemedicine",
    "url": "https://meet.aielon.global/appt_789"
  },
  "paymentRequired": {
    "amount": 50.00,
    "currency": "USD"
  }
}
```

#### Submit Health Data
```http
POST /api/v1/hcare/health-data
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "vital_signs",
  "timestamp": "2025-11-12T07:25:43.777Z",
  "data": {
    "heartRate": 72,
    "bloodPressure": {
      "systolic": 120,
      "diastolic": 80
    },
    "temperature": 98.6,
    "weight": 75.5
  }
}
```

#### Start Telemedicine Session
```http
POST /api/v1/hcare/telemedicine/sessions
Authorization: Bearer {token}
Content-Type: application/json

{
  "appointmentId": "appt_789"
}
```

**Response**:
```json
{
  "sessionId": "session_abc",
  "roomUrl": "https://meet.aielon.global/session_abc",
  "token": "session_token_xyz",
  "expires": "2025-11-15T11:00:00Z"
}
```

### Ummah Hub APIs

#### Create Post
```http
POST /api/v1/ummah-hub/posts
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "Excited to be part of the AiElon community!",
  "visibility": "public",
  "tags": ["introduction", "community"],
  "media": []
}
```

**Response**:
```json
{
  "postId": "post_123",
  "authorId": "user_123",
  "content": "Excited to be part of the AiElon community!",
  "visibility": "public",
  "tags": ["introduction", "community"],
  "likes": 0,
  "comments": 0,
  "createdAt": "2025-11-12T07:25:43.777Z"
}
```

#### Get Feed
```http
GET /api/v1/ummah-hub/feed
Authorization: Bearer {token}
Query Parameters:
  - limit: 20
  - offset: 0
  - filter: all,following,trending
```

#### Create Event
```http
POST /api/v1/ummah-hub/events
Authorization: Bearer {token}
Content-Type: application/json

{
  "title": "Community Health Workshop",
  "description": "Learn about preventive healthcare",
  "datetime": "2025-11-20T14:00:00Z",
  "duration": 120,
  "location": {
    "type": "virtual",
    "url": "https://meet.aielon.global/workshop"
  },
  "capacity": 100,
  "tags": ["health", "education"]
}
```

#### Join Group
```http
POST /api/v1/ummah-hub/groups/{group_id}/join
Authorization: Bearer {token}
```

### AI Engine APIs

#### Analyze Text
```http
POST /api/v1/ai/nlp/analyze
Authorization: Bearer {token}
Content-Type: application/json

{
  "text": "I really enjoyed my consultation with Dr. Smith",
  "operations": ["sentiment", "entities", "keywords"]
}
```

**Response**:
```json
{
  "sentiment": {
    "score": 0.92,
    "label": "positive"
  },
  "entities": [
    {
      "text": "Dr. Smith",
      "type": "PERSON",
      "confidence": 0.98
    }
  ],
  "keywords": ["enjoyed", "consultation", "Dr. Smith"]
}
```

#### Get Recommendations
```http
POST /api/v1/ai/recommendations
Authorization: Bearer {token}
Content-Type: application/json

{
  "userId": "user_123",
  "context": "healthcare",
  "limit": 5
}
```

**Response**:
```json
{
  "recommendations": [
    {
      "type": "doctor",
      "id": "doc_789",
      "name": "Dr. Jane Doe",
      "specialty": "Cardiology",
      "score": 0.95,
      "reason": "Based on your health profile"
    }
  ]
}
```

---

## WebSocket API

### Connection

```javascript
const ws = new WebSocket('wss://api.aielon.global/v1/ws');

ws.onopen = () => {
  ws.send(JSON.stringify({
    type: 'authenticate',
    token: 'Bearer eyJhbGciOiJSUzI1NiIs...'
  }));
};
```

### Subscribe to Events

```javascript
ws.send(JSON.stringify({
  type: 'subscribe',
  channels: [
    'notifications',
    'health-updates',
    'wallet-transactions'
  ]
}));
```

### Receive Messages

```javascript
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log('Received:', message);
};
```

**Message Format**:
```json
{
  "type": "notification",
  "channel": "notifications",
  "data": {
    "id": "notif_123",
    "title": "Appointment Reminder",
    "body": "You have an appointment in 1 hour",
    "timestamp": "2025-11-12T07:25:43.777Z"
  }
}
```

---

## Rate Limiting

### Limits

- **Authenticated Users**: 1000 requests per minute
- **API Keys**: 5000 requests per minute
- **WebSocket**: 100 messages per minute

### Headers

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950
X-RateLimit-Reset: 1636704000
```

### Response (Rate Limit Exceeded)

```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later.",
    "details": {
      "retryAfter": 60
    }
  }
}
```

---

## Pagination

### Request

```http
GET /api/v1/ummah-hub/posts?limit=20&offset=0
```

### Response

```json
{
  "data": [...],
  "pagination": {
    "total": 1000,
    "limit": 20,
    "offset": 0,
    "hasMore": true,
    "nextOffset": 20
  }
}
```

---

## Filtering & Sorting

### Query Parameters

```http
GET /api/v1/hcare/appointments?
  status=confirmed,pending&
  startDate=2025-11-01&
  endDate=2025-11-30&
  sortBy=datetime&
  sortOrder=asc
```

---

## Versioning

The API uses URL versioning:

- Current: `/api/v1/`
- Future: `/api/v2/`

Deprecated versions will be supported for 12 months after a new version is released.

---

## SDKs & Client Libraries

Official SDKs available for:
- JavaScript/TypeScript
- Python
- Java
- Go
- Swift (iOS)
- Kotlin (Android)

**Example (JavaScript)**:
```javascript
import AiElonClient from '@aielon/sdk';

const client = new AiElonClient({
  apiKey: 'your_api_key',
  environment: 'production'
});

const user = await client.users.me();
const appointments = await client.hcare.appointments.list();
```

---

## Webhooks

### Registering Webhooks

```http
POST /api/v1/webhooks
Authorization: Bearer {token}
Content-Type: application/json

{
  "url": "https://your-app.com/webhooks/aielon",
  "events": [
    "appointment.created",
    "payment.completed",
    "post.created"
  ],
  "secret": "your_webhook_secret"
}
```

### Webhook Payload

```json
{
  "id": "evt_123",
  "type": "appointment.created",
  "timestamp": "2025-11-12T07:25:43.777Z",
  "data": {
    "appointmentId": "appt_789",
    "patientId": "user_123",
    "doctorId": "doc_456",
    "datetime": "2025-11-15T10:00:00Z"
  }
}
```

### Signature Verification

```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const hash = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return hash === signature;
}
```

---

## GraphQL API

**Endpoint**: `https://api.aielon.global/graphql`

### Example Query

```graphql
query GetUserProfile {
  me {
    id
    name
    email
    appointments(limit: 5) {
      id
      datetime
      doctor {
        name
        specialty
      }
    }
    recentTransactions(limit: 10) {
      id
      amount
      currency
      timestamp
    }
  }
}
```

### Example Mutation

```graphql
mutation BookAppointment($input: AppointmentInput!) {
  bookAppointment(input: $input) {
    id
    status
    datetime
    doctor {
      name
    }
  }
}
```

---

## Best Practices

1. **Always use HTTPS** for secure communication
2. **Cache responses** where appropriate
3. **Handle errors gracefully** with proper retry logic
4. **Respect rate limits** with exponential backoff
5. **Use WebSockets** for real-time updates
6. **Validate input data** on the client side
7. **Store tokens securely** (never in localStorage for sensitive apps)
8. **Implement timeouts** for all requests
9. **Log API calls** for debugging
10. **Monitor API usage** and performance

---

## Support

- **Documentation**: https://docs.aielon.global
- **API Status**: https://status.aielon.global
- **Support Email**: api-support@aielon.global
- **Developer Forum**: https://forum.aielon.global

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-12  
**Status**: Active
