# AiElon FusionHD API Documentation

## System API

### System Initialization

Initialize the entire AiElon FusionHD system.

```python
from src.main import FusionHDSystem

system = FusionHDSystem(config_path="config/system.json")
initialized = system.initialize()
```

**Returns:** `bool` - True if initialization successful

### Get System Status

Retrieve comprehensive system status including all subsystems.

```python
status = system.get_system_status()
```

**Returns:** `dict` with keys:
- `system`: Core system information
- `communication`: Communication layer status
- `security`: Security manager status
- `monitoring`: Monitoring system status
- `subsystems`: All subsystem statuses
- `health_check`: Health check results

### Run Diagnostics

Execute full system diagnostics to verify all components.

```python
diagnostics = system.run_diagnostics()
```

**Returns:** `dict` with keys:
- `timestamp`: Diagnostic run time
- `tests`: Individual test results
- `overall_status`: 'pass' or 'fail'

## Communication API

### Send Message

Send encrypted message between subsystems.

```python
from src.core.communication.layer import CommunicationLayer

comm = CommunicationLayer(config)
result = comm.send_message(
    sender="subsystem1",
    recipient="subsystem2",
    message={"type": "data", "payload": {...}}
)
```

**Parameters:**
- `sender` (str): Sending subsystem identifier
- `recipient` (str): Receiving subsystem identifier
- `message` (dict): Message content

**Returns:** `dict` with keys:
- `status`: 'success' or 'error'
- `message_id`: Unique message identifier

### Broadcast Message

Broadcast message to all subscribed subsystems.

```python
result = comm.broadcast(
    sender="system",
    message={"type": "announcement", "data": "System update"}
)
```

**Returns:** `dict` with keys:
- `status`: 'success' or 'error'
- `recipients`: Number of recipients

### Subscribe to Messages

Subscribe subsystem to receive messages.

```python
def message_handler(message):
    print(f"Received: {message}")

comm.subscribe("my_subsystem", message_handler)
```

## Security API

### Register User

Register a new user with role assignment.

```python
from src.core.security.manager import SecurityManager

security = SecurityManager(config)
result = security.register_user(
    username="john_doe",
    password="secure_password_123",
    role="user"
)
```

**Parameters:**
- `username` (str): Unique username
- `password` (str): User password (will be hashed)
- `role` (str): 'admin', 'user', or 'guest'

**Returns:** `dict` with keys:
- `status`: 'success' or 'error'
- `user_id`: Username

### Authenticate User

Authenticate user and create session.

```python
result = security.authenticate(
    username="john_doe",
    password="secure_password_123",
    mfa_code="123456"  # Optional, if MFA enabled
)
```

**Returns:** `dict` with keys:
- `status`: 'success', 'error', or 'mfa_required'
- `session_token`: Session token (if successful)
- `role`: User role

### Authorize Action

Check if user is authorized for specific action.

```python
authorized = security.authorize(
    session_token="abc123...",
    action="delete"
)
```

**Returns:** `bool` - True if authorized

### Get Audit Log

Retrieve security audit log.

```python
log = security.get_audit_log(limit=100)
```

**Returns:** List of audit entries

## Monitoring API

### Record Metric

Record a system metric value.

```python
from src.core.monitoring.system import MonitoringSystem

monitoring = MonitoringSystem(config)
monitoring.record_metric("cpu_usage", 75.5)
```

### Get Metrics

Retrieve recorded metrics.

```python
# Get specific metric
metrics = monitoring.get_metrics("cpu_usage", limit=100)

# Get all metrics
all_metrics = monitoring.get_metrics()
```

**Returns:** `dict` of metric name to values list

### Get Alerts

Retrieve system alerts.

```python
alerts = monitoring.get_alerts(status="active", limit=50)
```

**Parameters:**
- `status` (str): 'active' or 'resolved'
- `limit` (int): Maximum number of alerts

**Returns:** List of alert dictionaries

### Health Check

Perform health check on subsystems.

```python
health = monitoring.health_check(subsystems)
```

**Returns:** `dict` with keys:
- `timestamp`: Check time
- `overall_health`: 0-100 score
- `subsystems`: Individual subsystem health

## Subsystem APIs

### AiElon OS

```python
from src.subsystems.aielon.os import AiElonOS

os = AiElonOS()
os.initialize()

# Process AI request
result = os.process_request({"type": "query", "data": "..."})

# Learn from data
os.learn({"interaction": "user_action", "result": "success"})

# Optimize system
optimization = os.optimize()

# Get status
status = os.get_status()
```

### Fusion HD UI

```python
from src.subsystems.fusion_ui.ui import FusionUI

ui = FusionUI()
ui.initialize()

# Render view
view = ui.render("dashboard")

# Change theme
ui.set_theme("dark")

# Adapt layout
layout = ui.adapt_layout("mobile")

# Get status
status = ui.get_status()
```

### Halal Wallet

```python
from src.subsystems.halal_wallet.wallet import HalalWallet

wallet = HalalWallet()
wallet.initialize()

# Process transaction
result = wallet.process_transaction({
    "id": "txn_001",
    "type": "credit",
    "amount": 100.0,
    "description": "Halal investment return"
})

# Get balance
balance = wallet.get_balance()

# Get status
status = wallet.get_status()
```

### HCare

```python
from src.subsystems.hcare.health import HCare

hcare = HCare()
hcare.initialize()

# Monitor health
result = hcare.monitor_health(
    patient_id="patient_001",
    vitals={
        "heart_rate": 72,
        "blood_pressure_systolic": 120,
        "blood_pressure_diastolic": 80,
        "temperature": 37.0
    }
)

# Schedule telemedicine
session = hcare.schedule_telemedicine(
    patient_id="patient_001",
    doctor_id="doctor_001"
)

# Get status
status = hcare.get_status()
```

### Ummah Hub

```python
from src.subsystems.ummah_hub.hub import UmmahHub

hub = UmmahHub()
hub.initialize()

# Add member
result = hub.add_member({
    "id": "member_001",
    "name": "John Doe",
    "email": "john@example.com"
})

# Create event
event = hub.create_event({
    "id": "event_001",
    "title": "Community Gathering",
    "date": "2025-12-01",
    "location": "Community Center"
})

# Connect members
connection = hub.connect_members("member_001", "member_002")

# Share resource
resource = hub.share_resource({
    "id": "resource_001",
    "title": "Community Guidelines",
    "type": "document",
    "url": "https://example.com/guidelines.pdf"
})

# Get status
status = hub.get_status()
```

## Error Handling

All API methods return status information and handle errors gracefully:

```python
result = some_api_method(...)

if result.get('status') == 'success':
    # Handle success
    print("Operation successful")
else:
    # Handle error
    error_reason = result.get('reason', 'Unknown error')
    print(f"Operation failed: {error_reason}")
```

## Response Codes

Standard status values:
- `success`: Operation completed successfully
- `error`: Operation failed
- `mfa_required`: Multi-factor authentication required
- `rate_limit_exceeded`: Rate limit reached

## Rate Limits

- Communication messages: 10,000 per second
- Health checks: Every 30 seconds
- Metric recording: Unlimited
- API calls: No global limit (subsystem-specific limits apply)

## Best Practices

1. **Always initialize before use:**
   ```python
   system.initialize()
   ```

2. **Check return status:**
   ```python
   if result['status'] == 'success':
       # proceed
   ```

3. **Handle exceptions:**
   ```python
   try:
       result = api_call()
   except Exception as e:
       logger.error(f"Error: {e}")
   ```

4. **Use secure sessions:**
   ```python
   # Authenticate first
   auth = security.authenticate(username, password)
   token = auth['session_token']
   
   # Use token for authorization
   security.authorize(token, action)
   ```

5. **Monitor system health:**
   ```python
   status = system.get_system_status()
   if status['health_check']['overall_health'] < 100:
       # Take action
   ```

## Integration Examples

### Complete Workflow Example

```python
from src.main import FusionHDSystem

# Initialize system
system = FusionHDSystem()
if not system.initialize():
    print("Failed to initialize")
    exit(1)

# Register user
result = system.security.register_user("user1", "pass123", "user")

# Authenticate
auth = system.security.authenticate("user1", "pass123")
token = auth['session_token']

# Send message between subsystems
system.communication.send_message(
    "fusion_ui",
    "halal_wallet",
    {"action": "get_balance"}
)

# Monitor system
system.monitoring.record_metric("cpu_usage", 65.0)

# Check health
status = system.get_system_status()
print(f"System health: {status['health_check']['overall_health']}%")

# Shutdown
system.shutdown()
```
