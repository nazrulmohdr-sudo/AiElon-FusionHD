# API Documentation

## AiElon Living OS API Reference

This document describes the API for all modules in AiElon Living OS v2.0.0.

---

## Core Modules

### StateManager API

Global state management system.

#### `get(key: string): any`
Get a value from the global state.

```javascript
const value = globalState.get('userCount');
```

#### `set(key: string, value: any): void`
Set a value in the global state with history tracking.

```javascript
globalState.set('userCount', 100);
```

#### `subscribe(key: string, callback: Function): void`
Subscribe to state changes.

```javascript
globalState.subscribe('userCount', (newValue, oldValue) => {
  console.log(`User count changed from ${oldValue} to ${newValue}`);
});
```

#### `unsubscribe(key: string, callback: Function): void`
Unsubscribe from state changes.

#### `getHistory(): Array`
Get state change history.

```javascript
const history = globalState.getHistory();
// Returns: [{ timestamp, key, oldValue, newValue }, ...]
```

#### `getAll(): Object`
Get all state as an object.

#### `batchUpdate(updates: Object): void`
Batch update multiple state values.

```javascript
globalState.batchUpdate({
  userCount: 100,
  activeUsers: 50,
  systemStatus: 'online'
});
```

---

### ScalabilityManager API

Resource management and load balancing.

#### `monitorResources(): Object`
Monitor current resource usage.

```javascript
const resources = scalabilityManager.monitorResources();
// Returns: { cpu, memory, network, healthy }
```

#### `isHealthy(): boolean`
Check if system is healthy.

#### `addTask(task: Function, priority: number): void`
Add task to queue with priority (higher = more important).

```javascript
scalabilityManager.addTask(async () => {
  // Task code here
}, 8);
```

#### `autoScale(): void`
Auto-scale resources based on current load.

#### `getMetrics(): Object`
Get performance metrics.

```javascript
const metrics = scalabilityManager.getMetrics();
// Returns: { tasksProcessed, averageResponseTime, queueLength, ... }
```

#### `optimize(): Object`
Optimize system performance.

---

## Blockchain Module

### AiElonChain338 API

Blockchain implementation.

#### `addTransaction(transaction: Object): Object`
Add a new transaction to pending transactions.

```javascript
const tx = aiElonChain338.addTransaction({
  from: '0xABC...',
  to: '0xDEF...',
  amount: 100
});
```

**Parameters:**
- `from` (string): Sender address
- `to` (string): Recipient address
- `amount` (number): Transaction amount

#### `minePendingTransactions(minerAddress: string): Object`
Mine pending transactions into a new block.

```javascript
const block = aiElonChain338.minePendingTransactions('0xMINER...');
```

#### `getBalance(address: string): number`
Get balance for an address.

```javascript
const balance = aiElonChain338.getBalance('0xABC...');
```

#### `isChainValid(): boolean`
Validate the entire blockchain.

```javascript
const valid = aiElonChain338.isChainValid();
```

#### `getChainInfo(): Object`
Get blockchain information.

```javascript
const info = aiElonChain338.getChainInfo();
// Returns: { chainId, network, blockHeight, difficulty, ... }
```

#### `getTransactionHistory(address: string): Array`
Get transaction history for an address.

```javascript
const history = aiElonChain338.getTransactionHistory('0xABC...');
```

#### `addValidator(address: string): Object`
Add a validator to the network.

---

## Wallet Module

### HalalWallet API

Sharia-compliant digital wallet.

#### `createWallet(owner: string): Object`
Create a new Halal wallet.

```javascript
const wallet = halalWallet.createWallet('username');
// Returns: { address, owner, balance, status }
```

#### `sendTransaction(fromAddress, toAddress, amount, purpose): Object`
Send a transaction with Sharia compliance check.

```javascript
const result = halalWallet.sendTransaction(
  '0xH...',
  '0xH...',
  100,
  'halal_purchase'
);
```

**Prohibited Purposes:**
- alcohol
- gambling
- tobacco
- weapons

#### `calculateZakat(address: string): Object`
Calculate Zakat (2.5% of eligible balance).

```javascript
const zakat = halalWallet.calculateZakat('0xH...');
// Returns: { balance, zakatDue, percentage, eligible }
```

**Nisab Threshold:** 1000 units

#### `payZakat(fromAddress, charityAddress): Object`
Pay calculated Zakat to charity.

```javascript
const result = halalWallet.payZakat('0xH...', '0xCHARITY...');
```

#### `getBalance(address: string): Object`
Get wallet balance with Zakat information.

```javascript
const balance = halalWallet.getBalance('0xH...');
// Returns: { address, balance, zakatDue, complianceScore }
```

#### `getWalletInfo(address: string): Object`
Get comprehensive wallet information.

---

## Healthcare Module

### HCare API

Healthcare management system.

#### `registerPatient(patientInfo: Object): Object`
Register a new patient.

```javascript
const patient = hcare.registerPatient({
  name: 'John Doe',
  dateOfBirth: '1990-01-01',
  bloodType: 'O+',
  allergies: ['penicillin', 'peanuts']
});
// Returns: { success, patientId, message }
```

#### `recordVitals(patientId: string, vitals: Object): Object`
Record patient health vitals.

```javascript
const result = hcare.recordVitals('PAT123...', {
  heartRate: 75,
  bloodPressure: '120/80',
  temperature: 37.0,
  oxygenLevel: 98,
  weight: 70
});
// Returns: { success, vitals, alerts }
```

**Alert Thresholds:**
- Heart Rate: 60-100 bpm (normal)
- Temperature: < 37.5°C (normal)
- Oxygen: > 95% (normal)

#### `scheduleAppointment(patientId, providerId, scheduledTime, type): Object`
Schedule a medical appointment.

```javascript
const appointment = hcare.scheduleAppointment(
  'PAT123...',
  'PRV456...',
  Date.now() + 86400000, // Tomorrow
  'general'
);
```

#### `addMedicalRecord(patientId: string, record: Object): Object`
Add a medical record (encrypted).

```javascript
const result = hcare.addMedicalRecord('PAT123...', {
  diagnosis: 'Common cold',
  treatment: 'Rest and fluids',
  medications: ['Paracetamol'],
  notes: 'Follow up in 1 week'
});
```

#### `getHealthDashboard(patientId: string): Object`
Get patient health dashboard.

```javascript
const dashboard = hcare.getHealthDashboard('PAT123...');
// Returns: { patient, latestVitals, upcomingAppointments, healthScore }
```

#### `registerProvider(providerInfo: Object): Object`
Register a healthcare provider.

```javascript
const provider = hcare.registerProvider({
  name: 'Dr. Smith',
  specialty: 'General Practice',
  license: 'MED12345'
});
```

#### `getStatistics(): Object`
Get HCare system statistics.

---

## Community Module

### UmmahHub API

Islamic community social network.

#### `registerUser(userInfo: Object): Object`
Register a new user.

```javascript
const user = ummahHub.registerUser({
  username: 'user123',
  email: 'user@example.com',
  location: 'City, Country'
});
// Returns: { success, userId, username }
```

#### `createPost(userId: string, postData: Object): Object`
Create a new post.

```javascript
const post = ummahHub.createPost('USR123...', {
  content: 'Assalamu alaikum!',
  type: 'text',
  tags: ['greeting', 'community']
});
```

**Content Validation:**
Posts are checked against community standards for inappropriate content.

#### `createGroup(creatorId: string, groupData: Object): Object`
Create a community group.

```javascript
const group = ummahHub.createGroup('USR123...', {
  name: 'Quran Study Circle',
  description: 'Weekly Quran study sessions',
  category: 'education',
  privacy: 'public' // or 'private'
});
```

#### `joinGroup(userId: string, groupId: string): Object`
Join a community group.

```javascript
const result = ummahHub.joinGroup('USR123...', 'GRP456...');
```

#### `createEvent(organizerId: string, eventData: Object): Object`
Create a community event.

```javascript
const event = ummahHub.createEvent('USR123...', {
  title: 'Iftar Gathering',
  description: 'Community iftar during Ramadan',
  startTime: Date.now() + 86400000,
  endTime: Date.now() + 90000000,
  location: 'Community Center',
  category: 'religious'
});
```

#### `followUser(followerId: string, followeeId: string): Object`
Follow another user.

```javascript
const result = ummahHub.followUser('USR123...', 'USR456...');
```

#### `getFeed(userId: string, limit: number): Array`
Get user's personalized feed.

```javascript
const feed = ummahHub.getFeed('USR123...', 20);
// Returns array of posts from followed users
```

#### `likePost(userId: string, postId: string): Object`
Like a post.

```javascript
const result = ummahHub.likePost('USR123...', 'POST789...');
```

#### `addComment(userId, postId, content): Object`
Add a comment to a post.

```javascript
const comment = ummahHub.addComment(
  'USR123...',
  'POST789...',
  'Great post!'
);
```

#### `getUserProfile(userId: string): Object`
Get user profile.

```javascript
const profile = ummahHub.getUserProfile('USR123...');
// Returns: { id, username, location, stats, ... }
```

#### `getStatistics(): Object`
Get Ummah Hub statistics.

---

## Security Module

### SecurityManager API

Authentication and security services.

#### `authenticate(username: string, password: string): Object`
Authenticate user credentials.

```javascript
const auth = securityManager.authenticate('user123', 'password');
// Returns: { success, sessionId, user, permissions } or { success: false, error }
```

**Security:**
- Max 5 failed attempts before lockout
- Minimum password length: 8 characters

#### `verifySession(sessionId: string): boolean`
Verify if session is valid.

```javascript
const valid = securityManager.verifySession(sessionId);
```

#### `logout(sessionId: string): void`
Logout user and destroy session.

```javascript
securityManager.logout(sessionId);
```

#### `encrypt(data: string): string`
Encrypt sensitive data.

```javascript
const encrypted = securityManager.encrypt('sensitive data');
// Returns: 'enc:base64_encoded_string'
```

#### `decrypt(encryptedData: string): string`
Decrypt encrypted data.

```javascript
const decrypted = securityManager.decrypt('enc:...');
```

#### `validateInput(input: string): Object`
Validate input for security threats.

```javascript
const validation = securityManager.validateInput(userInput);
// Returns: { safe, threats }
```

**Detects:**
- SQL Injection
- XSS (Cross-Site Scripting)
- Path Traversal

#### `getSecurityLogs(limit: number): Array`
Get security event logs.

```javascript
const logs = securityManager.getSecurityLogs(100);
```

#### `getSecurityStatus(): Object`
Get current security status.

```javascript
const status = securityManager.getSecurityStatus();
// Returns: { activeSessions, encryptionEnabled, recentThreats, status }
```

---

## UI Module

### FusionHDUI API

User interface components.

#### `initialize(): Object`
Initialize the UI system.

```javascript
const result = fusionHDUI.initialize();
```

#### `setTheme(theme: string): void`
Set UI theme ('light' or 'dark').

```javascript
fusionHDUI.setTheme('dark');
```

#### `renderDashboard(data: Object): string`
Render system dashboard.

```javascript
const dashboard = fusionHDUI.renderDashboard({
  systemStatus: 'Online',
  activeUsers: 100,
  blockchainStatus: 'Connected',
  securityStatus: 'Secure'
});
console.log(dashboard);
```

#### `renderNavigation(): string`
Render navigation menu.

#### `createNotification(message: string, type: string): Object`
Create a notification.

```javascript
const notif = fusionHDUI.createNotification(
  'Transaction successful!',
  'success' // 'info', 'success', 'warning', 'error'
);
```

#### `renderCard(cardData: Object): string`
Render a card component.

```javascript
const card = fusionHDUI.renderCard({
  title: 'Card Title',
  content: 'Card content here'
});
```

#### `renderTable(headers: Array, rows: Array): string`
Render a table.

```javascript
const table = fusionHDUI.renderTable(
  ['Name', 'Age', 'City'],
  [
    ['John', '30', 'NYC'],
    ['Jane', '25', 'LA']
  ]
);
```

#### `enableAccessibility(feature: string): void`
Enable accessibility feature.

```javascript
fusionHDUI.enableAccessibility('highContrast');
// Options: 'highContrast', 'largeText', 'screenReader'
```

---

## Error Handling

All API methods follow consistent error handling:

**Success Response:**
```javascript
{
  success: true,
  data: { ... },
  message: 'Operation successful'
}
```

**Error Response:**
```javascript
{
  success: false,
  error: 'Error description'
}
```

---

## Rate Limits

Currently no rate limits are enforced. Production deployment should implement:
- Authentication: 5 attempts per minute
- Transactions: 10 per minute per user
- API calls: 100 per minute per user

---

## Versioning

Current API Version: **2.0.0**

Breaking changes will increment the major version.

---

## Support

For API questions or issues, please open an issue on GitHub.

---

**Last Updated:** 2024