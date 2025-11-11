# Developer Guide - AiElon Living OS v2.0.0

## Welcome, Developers!

This guide provides technical information for developers who want to contribute to or extend AiElon Living OS.

## Table of Contents

1. [Development Environment Setup](#development-environment-setup)
2. [Architecture Overview](#architecture-overview)
3. [Module Development](#module-development)
4. [API Integration](#api-integration)
5. [Testing Guidelines](#testing-guidelines)
6. [Deployment](#deployment)
7. [Contributing](#contributing)

## Development Environment Setup

### Prerequisites

- Node.js >= 14.0.0
- NPM >= 6.0.0
- Git
- Code editor (VS Code recommended)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
   cd AiElon-FusionHD
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create environment file**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run in development mode**:
   ```bash
   npm run dev
   ```

### Recommended Tools

- **IDE**: Visual Studio Code
- **Extensions**:
  - ESLint
  - Prettier
  - GitLens
  - Node.js Extension Pack
- **Database Tools**: (if using external DB)
- **API Testing**: Postman or Insomnia

## Architecture Overview

### System Structure

```
AiElon-FusionHD/
├── src/                    # Source code
│   ├── index.js           # Main entry point
│   ├── core/              # Core OS modules
│   │   └── os.js          # Core OS implementation
│   ├── blockchain/        # Blockchain integration
│   │   └── aielonchain338.js
│   ├── ui/                # User interface
│   │   └── fusion-hd.js
│   ├── wallet/            # Halal Wallet
│   │   └── halal-wallet.js
│   ├── hcare/             # Health management
│   │   └── hcare-system.js
│   └── ummah-hub/         # Social platform
│       └── ummah-platform.js
├── config/                 # Configuration files
│   └── system-config.js
├── tests/                  # Test files
│   └── integration.test.js
├── docs/                   # Documentation
└── package.json            # Project metadata
```

### Module Architecture

Each module follows a consistent pattern:

```javascript
class ModuleName {
    constructor() {
        // Initialize properties
    }

    async initialize(config) {
        // Setup module
        // Return this for chaining
        return this;
    }

    // Public methods
    async someMethod() {
        // Implementation
    }

    // Status method
    getStatus() {
        // Return module status
    }
}

module.exports = {
    initialize: async (config) => {
        const module = new ModuleName();
        return await module.initialize(config);
    },
    ModuleName
};
```

## Module Development

### Creating a New Module

1. **Create module directory**:
   ```bash
   mkdir src/my-module
   ```

2. **Create main module file**:
   ```javascript
   // src/my-module/my-module.js
   class MyModule {
       constructor() {
           this.version = '1.0.0';
           this.initialized = false;
       }

       async initialize(config) {
           console.log('  → Initializing MyModule...');
           this.config = config || {};
           this.initialized = true;
           console.log('  ✓ MyModule ready');
           return this;
       }

       getStatus() {
           return {
               version: this.version,
               initialized: this.initialized
           };
       }
   }

   module.exports = {
       initialize: async (config) => {
           const module = new MyModule();
           return await module.initialize(config);
       },
       MyModule
   };
   ```

3. **Integrate with main system**:
   ```javascript
   // src/index.js
   const myModule = require('./my-module/my-module');

   // In initialize method
   this.modules.myModule = await myModule.initialize(config.myModule);
   ```

4. **Add configuration**:
   ```javascript
   // config/system-config.js
   module.exports = {
       // ...
       myModule: {
           version: '1.0.0',
           enabled: true,
           // Add your config
       }
   };
   ```

### Module Best Practices

1. **Asynchronous Initialization**: Use async/await for initialization
2. **Error Handling**: Always wrap risky operations in try-catch
3. **Logging**: Use consistent logging format
4. **Status Methods**: Implement getStatus() for monitoring
5. **Configuration**: Accept configuration object in initialize()
6. **Documentation**: Add JSDoc comments

### Example: Adding a Feature to Halal Wallet

```javascript
// src/wallet/halal-wallet.js

/**
 * Export wallet data
 */
async exportWalletData(walletId, format = 'json') {
    const wallet = this.wallets.get(walletId);
    if (!wallet) {
        throw new Error('Wallet not found');
    }

    // Remove sensitive data
    const exportData = {
        address: wallet.address,
        balance: wallet.balance,
        transactions: wallet.transactions,
        createdAt: wallet.createdAt
    };

    if (format === 'json') {
        return JSON.stringify(exportData, null, 2);
    } else if (format === 'csv') {
        // Convert to CSV
        return this.convertToCSV(exportData);
    }

    throw new Error('Unsupported format');
}
```

## API Integration

### Adding New API Endpoints

1. **Create route handler**:
   ```javascript
   // In src/ui/fusion-hd.js setupRoutes()
   this.app.post('/api/mymodule/action', async (req, res) => {
       try {
           const result = await this.handleAction(req.body);
           res.json({ success: true, data: result });
       } catch (error) {
           res.status(400).json({ 
               success: false, 
               error: error.message 
           });
       }
   });
   ```

2. **Add middleware**:
   ```javascript
   const authenticate = (req, res, next) => {
       // Authentication logic
       if (req.headers.authorization) {
           next();
       } else {
           res.status(401).json({ error: 'Unauthorized' });
       }
   };

   this.app.post('/api/protected', authenticate, handler);
   ```

3. **Document the API**:
   Add to `docs/API.md`

### API Response Format

```javascript
// Success response
{
    "success": true,
    "data": {
        // Response data
    },
    "meta": {
        "timestamp": "2025-11-11T13:00:00.000Z"
    }
}

// Error response
{
    "success": false,
    "error": {
        "code": "ERROR_CODE",
        "message": "Human readable message",
        "details": {}
    }
}
```

## Testing Guidelines

### Test Structure

```javascript
// tests/my-feature.test.js
const assert = require('assert');
const { MyModule } = require('../src/my-module/my-module');

describe('MyModule', () => {
    it('should initialize correctly', async () => {
        const module = new MyModule();
        await module.initialize({});
        assert.strictEqual(module.initialized, true);
    });

    it('should handle errors gracefully', async () => {
        const module = new MyModule();
        await module.initialize({});
        
        try {
            await module.methodThatShouldFail();
            assert.fail('Should have thrown error');
        } catch (error) {
            assert(error.message);
        }
    });
});
```

### Running Tests

```bash
# Run all tests
npm test

# Run specific test file
node tests/integration.test.js

# Run with coverage
npm run test:coverage
```

### Test Coverage Goals

- Unit tests: > 80% coverage
- Integration tests: All critical paths
- E2E tests: Main user flows

### Writing Good Tests

1. **Test one thing at a time**
2. **Use descriptive test names**
3. **Arrange, Act, Assert pattern**
4. **Clean up after tests**
5. **Mock external dependencies**

## Deployment

### Production Build

```bash
# Build for production
npm run build

# Set environment to production
export NODE_ENV=production

# Start production server
npm start
```

### Environment Variables

Create `.env` file:

```env
NODE_ENV=production
PORT=3000
HOST=0.0.0.0

# Blockchain
AIELONCHAIN_RPC=https://rpc.aielonchain338.network
AIELONCHAIN_WS=wss://ws.aielonchain338.network

# Security
ENCRYPTION_KEY=your-key
JWT_SECRET=your-secret

# Logging
LOG_LEVEL=info
```

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

Build and run:

```bash
docker build -t aielon-living-os .
docker run -p 3000:3000 aielon-living-os
```

### Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: aielon-living-os
spec:
  replicas: 3
  selector:
    matchLabels:
      app: aielon-living-os
  template:
    metadata:
      labels:
        app: aielon-living-os
    spec:
      containers:
      - name: aielon-living-os
        image: aielon-living-os:latest
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
```

## Contributing

### Code Style

We use ESLint and Prettier:

```bash
# Check code style
npm run lint

# Fix automatically
npm run lint:fix

# Format code
npm run format
```

### Git Workflow

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Make changes and commit**:
   ```bash
   git add .
   git commit -m "Add my feature"
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature/my-feature
   ```
5. **Create Pull Request**

### Commit Message Format

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style
- `refactor`: Code refactoring
- `test`: Tests
- `chore`: Maintenance

Example:
```
feat(wallet): add export functionality

Add ability to export wallet data in JSON and CSV formats.
Includes proper data sanitization and format validation.

Closes #123
```

### Pull Request Guidelines

1. **Update documentation**
2. **Add tests for new features**
3. **Ensure all tests pass**
4. **Keep PRs focused and small**
5. **Respond to code review feedback**

### Code Review Checklist

- [ ] Code follows project style
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No security vulnerabilities
- [ ] Performance considered
- [ ] Backward compatibility maintained

## Advanced Topics

### Custom Blockchain Integration

See [BLOCKCHAIN.md](BLOCKCHAIN.md) for details on:
- Custom smart contracts
- Event handling
- Transaction optimization

### Security Hardening

See [SECURITY.md](SECURITY.md) for:
- Security best practices
- Vulnerability testing
- Incident response

### Performance Optimization

Tips:
- Use connection pooling
- Implement caching
- Optimize database queries
- Use CDN for static assets
- Enable compression

### Monitoring and Logging

```javascript
// Add structured logging
const logger = {
    info: (msg, meta) => console.log(JSON.stringify({ level: 'info', msg, ...meta })),
    error: (msg, meta) => console.error(JSON.stringify({ level: 'error', msg, ...meta }))
};

logger.info('Transaction processed', {
    txId: tx.id,
    amount: tx.amount,
    timestamp: new Date()
});
```

## Resources

### Documentation
- [User Guide](USER_GUIDE.md)
- [API Documentation](API.md)
- [Security Guide](SECURITY.md)
- [Blockchain Integration](BLOCKCHAIN.md)

### Community
- GitHub: https://github.com/nazrulmohdr-sudo/AiElon-FusionHD
- Discord: (Join our server)
- Forum: (Coming soon)

### Support
- Email: dev-support@aielon.network
- Issue Tracker: GitHub Issues

---

**Happy Coding! Build amazing features for the Ummah!** 🚀
