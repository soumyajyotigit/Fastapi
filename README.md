# Enterprise FastAPI

A modern, modular FastAPI application starter designed for building scalable backend services with authentication, database integration, middleware, and AI-ready architecture. This project is actively evolving, and the README is structured to grow alongside new features.

## Overview

Enterprise FastAPI provides a clean foundation for building production-style APIs with:

- FastAPI-based REST endpoints
- Async SQLAlchemy database support
- JWT-based authentication flow
- Modular router and service structure
- Middleware for request logging and request ID tracking
- Alembic-based database migrations
- AI and RAG scaffolding for future integrations
- Docker-friendly project layout

This project is ideal for developers who want a strong backend base for SaaS products, internal tools, or AI-powered applications.

## Live Deployment

The application is deployed on Render: [https://fastapi-soumya.onrender.com](https://fastapi-soumya.onrender.com)

## Current Features

### Core API Capabilities
- Health and ping endpoints
- Authentication routes for registration and login
- User and blog route structure
- Centralized exception handling
- Request logging and request ID middleware
- Config-driven application settings

### Backend Architecture
- Clean separation of concerns with routers, services, repositories, schemas, and models
- Async database session management
- Environment-based configuration using Pydantic settings
- Extensible structure for adding business modules and integrations

### Planned / Emerging Areas
- Advanced RBAC and permission flows
- Enhanced user management
- Blog CRUD and content workflows
- AI agents and RAG integrations
- Redis caching and background job support
- Better observability, testing, and deployment automation

## Tech Stack

- FastAPI
- Python 3.10+
- SQLAlchemy (async)
- PostgreSQL
- Alembic
- Pydantic
- JWT / token-based authentication
- Docker
- Redis (configured for future use)
- pytest

## Project Structure

```text
app/
  api/
    v1/
      routers/
  core/
  db/
  middleware/
  repositories/
  schemas/
  services/
  utils/
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- PostgreSQL running locally or via Docker
- pip or poetry for dependency management

## Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd Fastapi_project
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Environment Configuration

Create a .env file in the project root with the required values:

```env
APP_NAME=Enterprise FastAPI
API_VERSION=v1
DEBUG=true
HOST=0.0.0.0
PORT=8000
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/fastapi_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
LOG_LEVEL=INFO
REDIS_URL=redis://localhost:6379/0
```

## Running the Application

Start the app locally:

```bash
python run.py
```

Or run with Uvicorn directly:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://localhost:8000/
- http://localhost:8000/docs
- http://localhost:8000/redoc

## API Endpoints

### Health
- GET /health
- GET /health/ping

### Authentication
- POST /api/v1/auth/register
- POST /api/v1/auth/login

### Users
- GET /api/v1/users/
- GET /api/v1/users/{user_id}

### Blogs
- GET /api/v1/blogs/
- GET /api/v1/blogs/{blog_id}

## Database Migrations

This project uses Alembic for schema migrations:

```bash
alembic upgrade head
```

To generate a new migration:

```bash
alembic revision --autogenerate -m "your message"
```

## Testing

Run tests with:

```bash
pytest
```

## Docker Support

A Docker-based workflow is supported for future containerized development and deployment:

```bash
docker compose up --build
```

## GitHub Actions deployment

Two image-build workflows are included in `.github/workflows`:

- **Build development image** runs on pushes to `develop` and `soumya-draft` (and can be started manually).
- **Build production image** runs on pushes to `main` (and can be started manually).

Each workflow builds the API image and pushes it to GitHub Container Registry as
`ghcr.io/<owner>/fastapi:<commit-sha>`.

For an SSH/Docker server deployment, add a separate deployment job with the
appropriate server credentials. When using Render, connect Render to the GitHub
repository and enable auto-deploy; Render builds and deploys the Dockerfile on
each push, so no SSH credentials or GitHub environment secrets are required.

The previously documented SSH deployment requires these environment secrets:

| Secret | Description |
| --- | --- |
| `DEPLOY_HOST` | Server hostname or IP address. |
| `DEPLOY_PORT` | SSH port (optional; defaults to `22`). |
| `DEPLOY_USER` | SSH user that can run Docker. |
| `DEPLOY_SSH_KEY` | Private SSH key for `DEPLOY_USER`. |
| `DEPLOY_PATH` | Absolute server directory containing `docker-compose.yml` and its `.env`. |
| `GHCR_READ_TOKEN` | GitHub PAT with `read:packages` permission, used by the server to pull the image. |

An SSH deployment server must have Docker Compose installed and a copy of this
repository's `docker-compose.yml` plus its environment-specific `.env` file at
`DEPLOY_PATH`. If the GHCR package is private, grant the PAT access to it.

## Development Notes

The current codebase follows a scalable pattern:

- Keep business logic in services
- Keep data access in repositories
- Keep request/response shape in schemas
- Keep shared infrastructure in core and middleware

This structure makes it easier to add new modules without cluttering the application entry points.

## Roadmap

Upcoming improvements include:

- Full blog CRUD operations
- Role-based access control (RBAC)
- Admin dashboards and management endpoints
- AI agent and RAG integrations
- Caching and background tasks
- Better deployment pipelines and monitoring
- Expanded automated tests and CI/CD workflows

## Contributing

Contributions are welcome. If you want to improve this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update tests where relevant
5. Submit a pull request

## License

This project is currently intended for personal and educational use unless a license is added later.

## Note

This README is designed to grow with the project. As new features are added, this document will be updated to reflect the latest architecture, capabilities, and setup instructions.
