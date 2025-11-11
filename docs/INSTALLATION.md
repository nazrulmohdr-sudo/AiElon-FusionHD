# Installation Guide - AiElon Living OS v2.0.0

## System Requirements

### Minimum Requirements
- **CPU**: Dual-core processor (2.0 GHz)
- **RAM**: 4 GB
- **Storage**: 10 GB available space
- **Node.js**: Version 14.0.0 or higher
- **NPM**: Version 6.0.0 or higher

### Recommended Requirements
- **CPU**: Quad-core processor (3.0 GHz)
- **RAM**: 8 GB or more
- **Storage**: 20 GB SSD
- **Node.js**: Version 18.0.0 or higher
- **NPM**: Version 8.0.0 or higher

## Installation Steps

### 1. Install Node.js and NPM

#### Linux (Ubuntu/Debian)
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### macOS
```bash
brew install node
```

#### Windows
Download and install from [nodejs.org](https://nodejs.org/)

### 2. Clone the Repository

```bash
git clone https://github.com/nazrulmohdr-sudo/AiElon-FusionHD.git
cd AiElon-FusionHD
```

### 3. Install Dependencies

```bash
npm install
```

This will install all required dependencies including:
- Express.js for server
- Crypto-js for encryption
- Web3 for blockchain integration

### 4. Configuration

Create a `.env` file in the root directory:

```env
# Server Configuration
PORT=3000
HOST=0.0.0.0
NODE_ENV=production

# Blockchain Configuration
AIELONCHAIN_RPC=https://rpc.aielonchain338.network
AIELONCHAIN_WS=wss://ws.aielonchain338.network

# Security
ENCRYPTION_KEY=your-secure-encryption-key-here
JWT_SECRET=your-jwt-secret-here

# Logging
LOG_LEVEL=info
```

**Important**: Replace placeholder values with your actual configuration.

### 5. Verify Installation

```bash
node -v  # Should show v14.0.0 or higher
npm -v   # Should show v6.0.0 or higher
```

### 6. Start the System

```bash
npm start
```

You should see:
```
🚀 Initializing AiElon Living OS v2.0.0
📦 Loading core system...
⛓️  Connecting to AielonChain338...
🎨 Loading Fusion HD UI...
💰 Initializing Halal Wallet...
🏥 Starting HCare System...
🌐 Launching Ummah Hub...
✅ AiElon Living OS initialized successfully!

🌟 AiElon Living OS is running on port 3000
```

### 7. Access the System

Open your web browser and navigate to:
- Main Dashboard: http://localhost:3000
- Halal Wallet: http://localhost:3000/wallet
- HCare: http://localhost:3000/hcare
- Ummah Hub: http://localhost:3000/ummah

## Platform-Specific Installation

### Docker Installation

```bash
# Build Docker image
docker build -t aielon-living-os .

# Run container
docker run -p 3000:3000 aielon-living-os
```

### Mobile Installation (Android/iOS)

Mobile builds require additional configuration. Please refer to the mobile development documentation.

## Troubleshooting

### Common Issues

#### Port Already in Use
If port 3000 is already in use, change the PORT in your `.env` file:
```env
PORT=3001
```

#### Dependencies Installation Failed
Try clearing npm cache:
```bash
npm cache clean --force
npm install
```

#### Permission Errors (Linux/macOS)
If you encounter permission errors, you may need to use sudo:
```bash
sudo npm install
```

#### Node Version Issues
Ensure you're using Node.js 14.0.0 or higher:
```bash
node -v
```

If your version is older, upgrade Node.js.

## Next Steps

After successful installation:

1. Read the [User Guide](USER_GUIDE.md) to learn how to use the system
2. Check the [API Documentation](API.md) for integration
3. Review [Security Guide](SECURITY.md) for best practices
4. Explore [Developer Guide](DEVELOPER.md) for customization

## Support

If you encounter any issues during installation:

1. Check the [FAQ](FAQ.md)
2. Search existing [GitHub Issues](https://github.com/nazrulmohdr-sudo/AiElon-FusionHD/issues)
3. Open a new issue with detailed information about your problem

## Updates

To update to the latest version:

```bash
git pull origin main
npm install
npm start
```

---

**Installation complete! Welcome to AiElon Living OS v2.0.0** 🎉
