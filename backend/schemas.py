from pydantic import BaseModel

class ProfileOut(BaseModel):
    name:str
    email:str
    education:str
    github:str
    linkedin:str
    portfolio:str

class SkillOut(BaseModel):
    skill:str

class ProjectOut(BaseModel):
    title:str
    description:str
    link:str
    skill:str
