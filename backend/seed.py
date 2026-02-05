from database import SessionLocal, engine, Base
from models import Profile, Skill, Project

Base.metadata.create_all(bind=engine)

db = SessionLocal()

db.query(Profile).delete()
db.query(Skill).delete()
db.query(Project).delete()

profile = Profile(
    name="Navadheer Kumar Vulli",
    email="navadheer@gmail.com",
    education="B.Tech Engineering",
    github="https://github.com/navadheer",
    linkedin="https://linkedin.com/in/navadheer",
    portfolio="https://portfolio.com"
)

skills = [
    Skill(skill="Python"),
    Skill(skill="Machine Learning"),
    Skill(skill="Backend"),
    Skill(skill="ROS")
]

projects = [
    Project(title="Sign Language Recognition",
            description="Real time gesture recognition",
            link="https://github.com/project1",
            skill="Python"),

    Project(title="Waste Segregation Bin",
            description="Smart bin using Raspberry Pi",
            link="https://github.com/project2",
            skill="IoT"),

    Project(title="Geo Attendance App",
            description="Location based attendance system",
            link="https://github.com/project3",
            skill="Backend")
]

db.add(profile)
db.add_all(skills)
db.add_all(projects)
db.commit()
db.close()

print("Database seeded successfully")
