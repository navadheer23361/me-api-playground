# me-api-playground
Full-stack API playground using FastAPI, SQLite, and Node.js frontend with query endpoints and health check.

Me API Playground – Assessment Project

This project is a simple full-stack application that demonstrates:

- REST API using FastAPI
- Database using SQLite
- Query endpoints
- Health check endpoint
- Basic frontend to consume APIs


TECH STACK

Backend:
Python
FastAPI
SQLAlchemy
SQLite
Uvicorn

Frontend:
Node.js
Express
HTML
CSS
JavaScript


PROJECT STRUCTURE

ASSESSMENT/

backend/
 main.py
 database.py
 models.py
 schemas.py
 seed.py
 requirements.txt
 app.db
 .env

frontend/
 public/
  index.html
  style.css
 server.js
 package.json

.gitignore
README.md


SETUP INSTRUCTIONS

BACKEND SETUP

Open PowerShell

cd backend
python -m pip install fastapi uvicorn sqlalchemy python-dotenv
python seed.py
python -m uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000


FRONTEND SETUP

Open new terminal

cd frontend
npm install
node server.js

Frontend runs at:
http://localhost:3000


API ENDPOINTS

GET /health        -> API status
GET /profile       -> User profile
GET /skills        -> All skills
GET /skills/top    -> Top skills
GET /projects      -> All projects
GET /projects?skill=Python -> Filter by skill
GET /search?q=app  -> Search projects


DATABASE

SQLite database file: app.db
Created using SQLAlchemy
Seeded using seed.py


FEATURES

REST API
Database with schema
Seed data
Query endpoints
Health check
Frontend interface
CORS enabled


AUTHOR

Navadheer Kumar Vulli
