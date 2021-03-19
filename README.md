# This project

A FastAPI project to explore this framework and other libs

## Steps to run

### 1. Building and running services
docker-compose up -d

### 2. Creating tables
docker-compose exec web alembic upgrade head

### 3. Populating with initial data
docker-compose exec database psql -U postgres -d postgres -f /backup/initial_data.sql

**Ready to go!**
