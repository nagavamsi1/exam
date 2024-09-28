from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Course(BaseModel):
    title: str
    description: str
    duration: str

courses = []

@app.post("/courses/", response_model=Course)
async def create_course(course: Course):
    courses.append(course)
    return course

@app.get("/courses/", response_model=List[Course])
async def get_courses():
    return courses

