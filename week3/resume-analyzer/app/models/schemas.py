from pydantic import BaseModel
from typing import List


class Project(BaseModel):
    project_name: str
    technologies: List[str] = []


class Education(BaseModel):
    institution: str
    duration: str = ""


class ResumeData(BaseModel):
    candidate_name: str
    email: str
    phone: str

    skills: List[str]

    projects: List[Project]

    education: List[Education]

    years_experience: float

class ExperienceRequirements(BaseModel):
    minimum_years: float
    description: str


class JobDescriptionData(BaseModel):
    job_title: str

    required_skills: list[str]

    preferred_skills: list[str]

    responsibilities: list[str]

    education_requirements: list[str]

    experience_requirements: ExperienceRequirements