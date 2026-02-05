from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
from models import Profile, Skill, Project

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/profile")
def get_profile():
    db = SessionLocal()
    profile = db.query(Profile).first()
    db.close()
    return profile

@app.get("/skills")
def get_skills():
    db = SessionLocal()
    skills = db.query(Skill).all()
    db.close()
    return skills

@app.get("/skills/top")
def top_skills():
    db = SessionLocal()
    skills = db.query(Skill).limit(3).all()
    db.close()
    return skills

@app.get("/projects")
def get_projects(skill:str=None):
    db = SessionLocal()
    if skill:
        projects = db.query(Project).filter(Project.skill==skill).all()
    else:
        projects = db.query(Project).all()
    db.close()
    return projects

@app.get("/search")
def search(q:str):
    db = SessionLocal()
    results = db.query(Project).filter(
        Project.title.contains(q) |
        Project.description.contains(q)
    ).all()
    db.close()
    return results
