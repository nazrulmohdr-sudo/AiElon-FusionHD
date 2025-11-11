# AiElon Living OS - User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Using the AI Engine](#using-the-ai-engine)
4. [Working with AielonChain338](#working-with-aielonchain338)
5. [Security Features](#security-features)
6. [Dashboard and UI](#dashboard-and-ui)
7. [Plugins and Extensions](#plugins-and-extensions)
8. [API Usage](#api-usage)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

## Introduction

Welcome to AiElon Living OS v2.0! This guide will help you get started with the advanced features and capabilities of the platform.

### What is AiElon Living OS?

AiElon Living OS is a comprehensive operating system platform that combines:
- **Artificial Intelligence** for intelligent automation and decision-making
- **Blockchain Technology** (AielonChain338) for secure transactions
- **Advanced Security** with enterprise-grade protection
- **Intuitive UI** with customizable dashboards
- **Modular Architecture** for easy extensibility

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the system:
```python
from core.system import AiElonLivingOS
from ai.ai_engine import AIEngine
from blockchain.aielonchain338 import AielonChain338
from security.security_framework import SecurityFramework
from ui.ui_framework import UIFramework
from plugins.plugin_system import ModularityFramework
from api.api_gateway import APIGateway

# Initialize system
system = AiElonLivingOS()

# Initialize and register modules
ai_engine = AIEngine()
blockchain = AielonChain338(difficulty=4)
security = SecurityFramework()
ui = UIFramework()
plugins = ModularityFramework()
api_gateway = APIGateway()

system.register_module("ai", ai_engine)
system.register_module("blockchain", blockchain)
system.register_module("security", security)
system.register_module("ui", ui)
system.register_module("plugins", plugins)
system.register_module("api", api_gateway)

# Start system
system.start()
```

### Basic Configuration

Create a configuration file `config.json`:
```json
{
  "system": {
    "version": "2.0.0",
    "log_level": "INFO"
  },
  "blockchain": {
    "difficulty": 4,
    "mining_reward": 10.0
  },
  "security": {
    "max_login_attempts": 5,
    "lockout_duration": 300,
    "token_expiry_hours": 24
  },
  "api": {
    "rate_limit": 100,
    "rate_window": 60
  }
}
```

## Using the AI Engine

### Processing Natural Language

The AI Engine can understand and process natural language:

```python
from ai.ai_engine import AIEngine

ai = AIEngine()
ai.initialize()

# Process a query
result = ai.process_natural_language("What is the current blockchain status?")

print(f"Intent: {result['intent']}")
print(f"Entities: {result['entities']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']}")
```

### Getting AI Recommendations

```python
# Get contextual recommendations
recommendations = ai.get_contextual_recommendation({
    "current_action": "viewing_dashboard"
})

for rec in recommendations:
    print(f"- {rec}")
```

### Learning from Interactions

```python
# Help AI learn from user interactions
ai.learn_from_interaction({
    "action": "created_transaction",
    "result": "success",
    "user_feedback": "positive"
})
```

### Predicting User Intent

```python
# Predict what user wants to do
predictions = ai.predict_user_intent("show my trans")

for prediction in predictions:
    print(f"{prediction['intent']}: {prediction['confidence']}")
```

## Working with AielonChain338

### Creating Transactions

```python
from blockchain.aielonchain338 import AielonChain338

blockchain = AielonChain338(difficulty=4)
blockchain.initialize()

# Create a transaction
tx_id = blockchain.create_transaction(
    sender="Alice",
    recipient="Bob",
    amount=50.0,
    transaction_type="transfer",
    metadata={"description": "Payment for services"}
)

print(f"Transaction created: {tx_id}")
```

### Mining Blocks

```python
# Mine pending transactions
block = blockchain.mine_pending_transactions("MinerAddress123")

print(f"Block mined: #{block.index}")
print(f"Hash: {block.hash}")
print(f"Transactions: {len(block.transactions)}")
```

### Checking Balances

```python
# Check account balance
balance = blockchain.get_balance("Alice")
print(f"Alice's balance: {balance}")
```

### Viewing Transaction History

```python
# Get transaction history for an address
history = blockchain.get_transaction_history("Alice")

for record in history:
    tx = record["transaction"]
    print(f"Block #{record['block_index']}: {tx['sender']} -> {tx['recipient']}: {tx['amount']}")
```

### Validating the Chain

```python
# Verify blockchain integrity
is_valid = blockchain.is_chain_valid()

if is_valid:
    print("Blockchain is valid ✓")
else:
    print("Blockchain has been tampered with! ✗")
```

## Security Features

### User Registration and Authentication

```python
from security.security_framework import SecurityFramework

security = SecurityFramework()
security.initialize()

# Register a new user
success = security.authentication.register_user(
    username="john_doe",
    password="SecureP@ss123",
    email="john@example.com",
    role="user"
)

if success:
    print("User registered successfully")
```

### Logging In

```python
# Authenticate user
token = security.authentication.authenticate("john_doe", "SecureP@ss123")

if token:
    print(f"Login successful! Token: {token}")
else:
    print("Login failed")
```

### Verifying Tokens

```python
# Verify JWT token
payload = security.authentication.verify_token(token)

if payload:
    print(f"Token valid for user: {payload['username']}")
    print(f"Role: {payload['role']}")
else:
    print("Token invalid or expired")
```

### Changing Passwords

```python
# Change user password
success = security.authentication.change_password(
    username="john_doe",
    old_password="SecureP@ss123",
    new_password="NewSecureP@ss456"
)

if success:
    print("Password changed successfully")
```

### Encrypting Data

```python
# Encrypt sensitive data
sensitive_data = "My secret information"
encrypted = security.encryption.encrypt_data(sensitive_data)

print(f"Encrypted: {encrypted['encrypted']}")
print(f"Key: {encrypted['key']}")

# Decrypt data
decrypted = security.encryption.decrypt_data(
    encrypted['encrypted'],
    encrypted['key']
)

print(f"Decrypted: {decrypted}")
```

### Rate Limiting

```python
# Check if request is allowed
client_id = "user_ip_192.168.1.1"

if security.rate_limiter.is_allowed(client_id):
    # Process request
    print("Request allowed")
else:
    print("Rate limit exceeded")

# Check remaining requests
remaining = security.rate_limiter.get_remaining_requests(client_id)
print(f"Remaining requests: {remaining}")
```

## Dashboard and UI

### Creating a Custom Dashboard

```python
from ui.ui_framework import UIFramework

ui = UIFramework()
ui.initialize()

# Create a new dashboard
dashboard = ui.create_dashboard(
    "portfolio",
    "Investment Portfolio"
)

# Set theme
dashboard.set_theme("dark")
```

### Adding Widgets

```python
# Create a status widget
status_widget = ui.create_widget("status_display", "portfolio_status")
status_widget.set_position(0, 0)
status_widget.set_size(400, 200)
status_widget.update_data({
    "title": "Portfolio Status",
    "total_value": "$125,000",
    "change_24h": "+2.5%"
})

# Add to dashboard
dashboard.add_widget(status_widget)

# Create a chart widget
chart_widget = ui.create_widget("chart", "performance_chart")
chart_widget.set_position(420, 0)
chart_widget.set_size(600, 400)
chart_widget.update_data({
    "type": "line",
    "data": [100, 105, 103, 108, 112, 115],
    "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
})

dashboard.add_widget(chart_widget)
```

### Rendering Dashboards

```python
# Render dashboard for display
render_data = dashboard.render()

print(f"Dashboard: {render_data['title']}")
print(f"Theme: {render_data['theme']}")
print(f"Widgets: {len(render_data['widgets'])}")

for widget in render_data['widgets']:
    print(f"  - {widget['widget_type']}: {widget['widget_id']}")
```

### Managing Themes

```python
# Get available themes
light_theme = ui.get_theme("light")
dark_theme = ui.get_theme("dark")

# Create custom theme
custom_theme = {
    "background": "#1a1a2e",
    "foreground": "#eaeaea",
    "primary": "#0f3460",
    "secondary": "#16213e",
    "accent": "#e94560"
}

ui.add_theme("custom_dark", custom_theme)

# Apply custom theme
dashboard.set_theme("custom_dark")
```

## Plugins and Extensions

### Creating a Custom Plugin

```python
from plugins.plugin_system import Plugin

class NotificationPlugin(Plugin):
    def __init__(self):
        super().__init__(
            plugin_id="notifications",
            name="Notification Plugin",
            version="1.0.0"
        )
    
    def initialize(self, config=None):
        super().initialize(config)
        
        # Register event handlers
        self.register_event_handler("transaction_created", self.on_transaction)
        self.register_event_handler("block_mined", self.on_block_mined)
        
        return True
    
    def on_transaction(self, event):
        tx = event.data.get("transaction")
        print(f"📧 New transaction: {tx['amount']} from {tx['sender']}")
    
    def on_block_mined(self, event):
        block = event.data.get("block")
        print(f"⛏️  Block #{block['index']} mined!")
```

### Registering and Enabling Plugins

```python
from plugins.plugin_system import ModularityFramework

framework = ModularityFramework()
framework.initialize()

# Create and register plugin
notification_plugin = NotificationPlugin()
framework.plugin_manager.register_plugin(notification_plugin)

# Enable plugin
framework.plugin_manager.enable_plugin("notifications")

# List enabled plugins
enabled = framework.plugin_manager.get_enabled_plugins()
print(f"Enabled plugins: {enabled}")
```

### Emitting Events

```python
from plugins.plugin_system import PluginEvent

# Create and emit event
event = PluginEvent(
    event_type="transaction_created",
    data={
        "transaction": {
            "sender": "Alice",
            "recipient": "Bob",
            "amount": 50.0
        }
    },
    source="blockchain"
)

framework.plugin_manager.emit_event(event)
```

## API Usage

### Making API Requests

```python
from api.api_gateway import APIGateway, APIRequest

gateway = APIGateway()
gateway.initialize()

# System status
request = APIRequest("GET", "/system/status")
response = gateway.handle_request(request)

print(f"Status: {response.status_code}")
print(f"Data: {response.data}")
```

### Processing Natural Language via API

```python
# AI processing
request = APIRequest(
    method="POST",
    endpoint="/ai/process",
    data={"text": "Show me the blockchain transactions"}
)

response = gateway.handle_request(request)

if response.status_code == 200:
    print(f"Result: {response.data}")
```

### Creating Blockchain Transactions via API

```python
# Create transaction
request = APIRequest(
    method="POST",
    endpoint="/blockchain/transaction",
    data={
        "sender": "Alice",
        "recipient": "Bob",
        "amount": 25.0
    }
)

response = gateway.handle_request(request)

if response.status_code == 200:
    print(f"Transaction ID: {response.data['transaction_id']}")
```

### Authentication via API

```python
# Login
request = APIRequest(
    method="POST",
    endpoint="/auth/login",
    data={
        "username": "john_doe",
        "password": "SecureP@ss123"
    }
)

response = gateway.handle_request(request)

if response.status_code == 200:
    token = response.data["token"]
    print(f"Login successful! Token: {token}")
```

## Best Practices

### Security

1. **Always use strong passwords**
   - Minimum 12 characters
   - Mix of uppercase, lowercase, numbers, and symbols
   - Never reuse passwords

2. **Protect JWT tokens**
   - Store securely (never in plain text)
   - Use HTTPS for transmission
   - Implement token refresh mechanism

3. **Regular security audits**
   - Review audit logs regularly
   - Monitor failed login attempts
   - Check for suspicious activity

### Blockchain

1. **Validate before mining**
   - Always validate transactions before mining
   - Check balances are sufficient
   - Verify sender authenticity

2. **Adjust difficulty appropriately**
   - Higher difficulty = more secure but slower
   - Lower difficulty = faster but less secure
   - Balance based on use case

3. **Regular chain validation**
   - Periodically validate entire chain
   - Detect tampering early
   - Maintain backups

### Performance

1. **Optimize queries**
   - Use pagination for large datasets
   - Cache frequently accessed data
   - Limit context memory size

2. **Monitor system resources**
   - Track memory usage
   - Monitor CPU utilization
   - Watch network bandwidth

3. **Regular maintenance**
   - Clear old logs periodically
   - Archive historical data
   - Update dependencies

## Troubleshooting

### System Won't Start

**Problem:** System fails to initialize

**Solutions:**
1. Check all modules are properly installed
2. Verify configuration file syntax
3. Check log files for error messages
4. Ensure no port conflicts

### Authentication Fails

**Problem:** Cannot login with correct credentials

**Solutions:**
1. Check if account is locked (wait 5 minutes)
2. Verify password is correct
3. Ensure user is active
4. Check token hasn't expired

### Blockchain Validation Fails

**Problem:** Chain validation returns false

**Solutions:**
1. Check for tampering in block data
2. Verify block hashes are correct
3. Ensure previous_hash links are valid
4. Rebuild chain from backup if needed

### High Memory Usage

**Problem:** System consuming too much memory

**Solutions:**
1. Clear context memory: `ai_engine.context_memory.clear()`
2. Reduce rate limiter window size
3. Limit dashboard widget count
4. Archive old blockchain data

### Rate Limit Exceeded

**Problem:** Requests being blocked

**Solutions:**
1. Reduce request frequency
2. Increase rate limit in configuration
3. Implement request queuing
4. Use batch operations where possible

## Advanced Topics

### Custom Widget Development

Create specialized widgets for your needs:

```python
class TradingWidget(Widget):
    def __init__(self, widget_id):
        super().__init__(widget_id, "trading")
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)
        self.update_data({"orders": self.orders})
    
    def render(self):
        data = super().render()
        data["active_orders"] = len(self.orders)
        return data
```

### Blockchain Smart Contracts

Extend blockchain with smart contract capabilities:

```python
class SmartContract:
    def __init__(self, contract_id, code):
        self.contract_id = contract_id
        self.code = code
        self.state = {}
    
    def execute(self, transaction):
        # Execute contract logic
        # Update state
        # Return result
        pass
```

### Custom AI Models

Integrate custom ML models:

```python
class CustomAIModel:
    def __init__(self):
        self.model = self.load_model()
    
    def load_model(self):
        # Load your custom model
        pass
    
    def predict(self, input_data):
        # Make predictions
        pass
```

## Support and Resources

- **Documentation:** `/docs` directory
- **API Reference:** See `ARCHITECTURE.md`
- **Examples:** Check test files in `/tests`
- **Community:** GitHub Issues and Discussions

## Conclusion

This guide covers the essential features of AiElon Living OS. For more advanced usage, refer to the Architecture Documentation and inline code documentation.

Happy building with AiElon Living OS! 🚀
