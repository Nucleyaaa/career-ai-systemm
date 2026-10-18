from pydantic import BaseModel
from typing import List, Dict, Optional

class CareerRecommendation(BaseModel):
    career_id: str
    title: str
    description: str
    match_score: float
    risk_score: float
    salary_range: Dict[str, float]
    demand_trend: str
    automation_risk: float
    required_skills: List[str]
    skill_gaps: List[str]
    education_required: str

class LearningPath(BaseModel):
    career_title: str
    total_duration_weeks: int
    skills_to_learn: List[str]
    timeline: List[Dict]
    milestones: List[Dict]
    resources: List[Dict]