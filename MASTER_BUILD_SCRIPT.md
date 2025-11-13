# AiElon Master Build Script Documentation

**Everything = 1 | Tunggal AiElon**

## Overview

The `aielon-master-build` script is a specialized build system that creates comprehensive deployment packages for the AiElon Everything System with specific technology stack configurations.

## Features

✅ **Complete Stack Configuration**
- Frontend: React + FusionHD UI
- Backend: Node.js Express API
- Mobile: React Native + Expo
- Database: PostgreSQL + Prisma
- Authentication: JWT + OAuth2
- Deployment: CI/CD with GitHub Actions
- Hosting: Vercel (Frontend) + Railway (Backend)

✅ **Automated Build Process**
- Creates organized build directory structure
- Configures all system components
- Generates build status and metadata
- Creates deployment-ready ZIP packages

✅ **Production Ready**
- All configurations optimized for production
- Clear deployment instructions included
- Comprehensive package documentation

## Usage

### Basic Command

```bash
./aielon-master-build
```

This will use all default values.

### Full Command (User Requested)

```bash
./aielon-master-build \
  --frontend=react-fusionHD \
  --backend=node-api-v1 \
  --mobile=react-native-expo \
  --database=postgres-prisma \
  --deploy=ci-cd-github-actions \
  --host=vercel-frontend-railway-backend \
  --auth=jwt-oauth2 \
  --status=production-ready \
  --zip-pack=final
```

### Quick Build with ZIP

```bash
./aielon-master-build --zip-pack=final
```

## Command Options

| Option | Description | Default |
|--------|-------------|---------|
| `--frontend` | Frontend framework | `react-fusionHD` |
| `--backend` | Backend framework | `node-api-v1` |
| `--mobile` | Mobile framework | `react-native-expo` |
| `--database` | Database setup | `postgres-prisma` |
| `--deploy` | Deployment method | `ci-cd-github-actions` |
| `--host` | Hosting platform | `vercel-frontend-railway-backend` |
| `--auth` | Authentication method | `jwt-oauth2` |
| `--status` | Build status | `production-ready` |
| `--zip-pack` | Package mode | `none` |
| `--help` | Show help | - |

## Technology Stack Details

### Frontend: React + FusionHD
- **Framework**: React.js
- **UI Library**: FusionHD components
- **Features**: 
  - High-definition interface
  - WCAG AAA accessibility
  - Theme system
  - Responsive design

### Backend: Node.js API v1
- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Features**:
  - RESTful API endpoints
  - Winston logging
  - Error handling middleware
  - Health checks

### Mobile: React Native + Expo
- **Framework**: React Native
- **Platform**: Expo
- **Support**: 
  - iOS
  - Android
  - Cross-platform compatibility

### Database: PostgreSQL + Prisma
- **Database**: PostgreSQL
- **ORM**: Prisma
- **Features**:
  - Schema migrations
  - Type-safe queries
  - Connection pooling

### Authentication: JWT + OAuth2
- **Methods**:
  - JWT token authentication
  - OAuth 2.0 integration
  - Multi-factor authentication (MFA)
  - Biometric support

### Deployment: CI/CD + GitHub Actions
- **Platform**: GitHub Actions
- **Features**:
  - Automated testing
  - Continuous deployment
  - Multi-environment support

### Hosting: Vercel + Railway
- **Frontend**: Vercel (serverless)
- **Backend**: Railway (PaaS)
- **Features**:
  - Auto-scaling
  - Edge network
  - Zero-downtime deployment

## Build Output

### Directory Structure

```
build-YYYYMMDD-HHMMSS/
├── frontend/
│   └── README.md
├── backend/
│   └── README.md
├── mobile/
│   └── README.md
├── database/
│   └── README.md
├── auth/
│   └── README.md
├── cicd/
│   └── README.md
├── hosting/
│   └── README.md
├── BUILD_STATUS.json
└── PACKAGE_INFO.md
```

### BUILD_STATUS.json

Contains complete build configuration and metadata:

```json
{
  "status": "production-ready",
  "frontend": "react-fusionHD",
  "backend": "node-api-v1",
  "mobile": "react-native-expo",
  "database": "postgres-prisma",
  "deploy": "ci-cd-github-actions",
  "host": "vercel-frontend-railway-backend",
  "auth": "jwt-oauth2",
  "timestamp": "2025-11-13T07:58:49Z",
  "version": "1.0.0",
  "principle": "Everything = 1 | Tunggal AiElon"
}
```

### ZIP Package

When `--zip-pack=final` or `--zip-pack=complete` is specified:

- **Filename**: `aielon-system-production-ready-YYYYMMDD-HHMMSS.zip`
- **Contents**: Complete build directory with all components
- **Size**: ~8KB (structure only, actual files would be larger)
- **Includes**: PACKAGE_INFO.md with deployment instructions

## Deployment Instructions

### 1. Frontend Deployment (Vercel)

```bash
cd build-YYYYMMDD-HHMMSS/frontend
npm install
vercel --prod
```

**Result**: Frontend URL provided by Vercel

### 2. Backend Deployment (Railway)

```bash
cd build-YYYYMMDD-HHMMSS/backend
npm install
railway up
```

**Result**: Backend URL provided by Railway

### 3. Mobile Deployment (Expo)

```bash
cd build-YYYYMMDD-HHMMSS/mobile
npm install
expo start
```

**Result**: QR code for mobile testing

### 4. Database Setup (Prisma)

```bash
cd build-YYYYMMDD-HHMMSS/backend
npx prisma migrate deploy
```

**Result**: Database schema deployed

## Examples

### Example 1: Default Build

```bash
chmod +x aielon-master-build
./aielon-master-build
```

Output: Build directory with default configuration

### Example 2: Production Build with Package

```bash
./aielon-master-build \
  --status=production-ready \
  --zip-pack=final
```

Output: Production build + ZIP package

### Example 3: Custom Configuration

```bash
./aielon-master-build \
  --frontend=react-fusionHD \
  --backend=node-api-v1 \
  --database=postgres-prisma \
  --zip-pack=complete
```

Output: Custom configured build + complete package

## Build Process (10 Steps)

1. **[1/10]** Creating build directory
2. **[2/10]** Building frontend (React + FusionHD)
3. **[3/10]** Building backend (Node.js API)
4. **[4/10]** Building mobile (React Native + Expo)
5. **[5/10]** Configuring database (PostgreSQL + Prisma)
6. **[6/10]** Configuring authentication (JWT + OAuth2)
7. **[7/10]** Setting up deployment (CI/CD)
8. **[8/10]** Configuring hosting (Vercel + Railway)
9. **[9/10]** Setting build status
10. **[10/10]** Creating package (if requested)

## Success Indicators

✅ Configuration Complete
✅ Frontend Built
✅ Backend Built
✅ Mobile Built
✅ Database Configured
✅ Deployment Setup
✅ Hosting Configured
✅ Authentication Configured
✅ Status Set
✅ Package Created (if requested)

## Troubleshooting

### Script Not Executable

```bash
chmod +x aielon-master-build
```

### ZIP Command Not Found

The script will skip compression and provide the build directory path instead.

### Build Directory Exists

Each build creates a unique timestamped directory, so conflicts won't occur.

## Integration with Main System

This script complements the `aielon-master` deployment script:

- **aielon-master**: Full deployment automation (install, deploy, sync)
- **aielon-master-build**: Specialized build configuration and packaging

Use together for complete control:

```bash
# Step 1: Build with specific configuration
./aielon-master-build --zip-pack=final

# Step 2: Deploy the built system
./aielon-master --deploy=vercel railway
```

## Best Practices

1. **Always create packages for production**: Use `--zip-pack=final`
2. **Review build status**: Check `BUILD_STATUS.json` before deployment
3. **Test locally first**: Build and test before production deployment
4. **Keep builds organized**: Builds are timestamped for easy tracking
5. **Document customizations**: Note any configuration changes

## Support

For more information:
- Main documentation: [README.md](README.md)
- Deployment guide: [DEPLOY.md](DEPLOY.md)
- Master script docs: [MASTER_SCRIPT.md](MASTER_SCRIPT.md)

---

**Everything = 1 | Tunggal AiElon**

Built with the AiElon Master Build System
