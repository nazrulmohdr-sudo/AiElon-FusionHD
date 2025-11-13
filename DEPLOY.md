# AiElon Everything System - Deployment Instructions

## Quick Start

### Local Development

1. **Install Dependencies**:
```bash
npm install
```

2. **Configure Environment**:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start the Server**:
```bash
npm start
```

The server will start at `http://localhost:3000`

### Using Docker

1. **Build and Run**:
```bash
docker-compose up -d
```

2. **Check Status**:
```bash
docker-compose ps
```

3. **View Logs**:
```bash
docker-compose logs -f aielon-api
```

4. **Stop Services**:
```bash
docker-compose down
```

## Deployment Options

### Option 1: Vercel (Serverless)

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel --prod
```

### Option 2: Railway

1. Install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login and Deploy:
```bash
railway login
railway init
railway up
```

### Option 3: Kubernetes

1. Build Docker Image:
```bash
docker build -t aielon/everything-system:latest .
```

2. Push to Registry:
```bash
docker push aielon/everything-system:latest
```

3. Deploy to Kubernetes:
```bash
kubectl apply -f kubernetes/deployment.yaml
```

## Testing the API

### Health Check
```bash
curl http://localhost:3000/health
```

### System Status
```bash
curl http://localhost:3000/api/v1/system/status
```

### User Profile
```bash
curl http://localhost:3000/api/v1/users/me
```

### Living OS Metrics
```bash
curl http://localhost:3000/api/v1/living-os/metrics
```

### Halal Wallet Balance
```bash
curl http://localhost:3000/api/v1/halal-wallet/balance
```

### Create Post
```bash
curl -X POST http://localhost:3000/api/v1/ummah-hub/posts \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello AiElon!", "visibility": "public"}'
```

## Environment Variables

Required environment variables:

- `NODE_ENV` - Environment (development/production)
- `PORT` - Server port (default: 3000)
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `MONGODB_URL` - MongoDB connection string

See `.env.example` for complete list.

## System Architecture

The system follows the "Everything = 1" principle with these components:

1. **API Server** - Express.js application
2. **PostgreSQL** - Primary database
3. **Redis** - Caching layer
4. **MongoDB** - Document storage

## Monitoring

Access monitoring endpoints:

- Health: `/health`
- System Status: `/api/v1/system/status`
- Metrics: `/api/v1/living-os/metrics`

## Support

For issues or questions:
- Documentation: See README.md and docs/ folder
- Email: support@aielon.global

---

**Everything = 1 | Tunggal AiElon**
