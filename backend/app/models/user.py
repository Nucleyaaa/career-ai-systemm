from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class UserProfile(BaseModel):
    id: str
    personality_vector: List[float]
    current_salary: float
    skills_owned: List[str]
    experience_years: int
    education_level: str
    location: str
    created_at: str

class PersonalityTestResponse(BaseModel):
    personality: Dict[str, float]
    holland_code: str
    personality_vector: List[float]
    interpretation: List[str]

class SkillProgress(BaseModel):
    skill: str
    is_completed: bool = False
    completed_at: Optional[str] = None

class UserCareerPath(BaseModel):
    user_id: str
    career_id: str
    career_title: str
    total_duration_weeks: int
    skills_progress: List[SkillProgress]
    current_week: int = 1
    status: str = "active"
    created_at: str