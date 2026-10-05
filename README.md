# FastAPI Deployment

A containerized FastAPI application demonstrating how to package, run, and deploy a backend service with **Docker, PostgreSQL, Docker Compose, Nginx, and GitHub Container Registry**.

## What this project demonstrates

- FastAPI application development
- PostgreSQL integration
- SQLAlchemy database setup
- Docker image creation
- Multi-container environments with Docker Compose
- Nginx reverse proxy
- Persistent PostgreSQL storage
- Environment-based configuration
- Production-style deployment using a published container image
- GitHub Container Registry workflow

## Architecture

```text
Client
  │
  ▼
Nginx :8080
  │
  ▼
FastAPI :8000
  │
  ▼
PostgreSQL :5432
```

The deployment Compose file pulls the API image from:

```text
ghcr.io/sfahadasif8-cyber/fastapi-deployment:latest
```

## API

### Health check

```http
GET /health
```

Returns:

```json
{"status":"API is healthy"}
```

### Book API

The application also exposes the book-management API under `/books`.

### Utility endpoints

```text
GET /add?num1=10&num2=5
GET /subtract?num1=10&num2=5
GET /multiply?num1=10&num2=5
GET /divide?num1=10&num2=5
```

## Local deployment

Create a `.env` file containing:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=fastapi
```

Then run:

```bash
docker compose up --build
```

The application is exposed through Nginx on port `8080`.

## Production-style deployment

The repository includes `docker-compose.deploy.yml`, which uses the published GHCR image instead of building the API locally.

```bash
docker compose -f docker-compose.deploy.yml up -d
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application language |
| FastAPI | REST API framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Nginx | Reverse proxy |
| GitHub Container Registry | Container image registry |

## Project Structure

```text
fastapi-deployment/
├── app/
├── nginx/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.deploy.yml
├── requirements.txt
└── README.md
```

## Learning focus

This project is part of my progression from backend development toward **DevOps and cloud engineering**, with an emphasis on understanding the complete path from application code to a reproducible deployment.
