from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel
from app.services.career_intelligence import CareerIntelligenceService

router = APIRouter()
service = CareerIntelligenceService()

# ── Request Models ──────────────────────────────────────────────────────────

class UserProfileInput(BaseModel):
    personality_vector: List[float]
    current_salary: float
    skills_owned: List[str]
    experience_years: int
    education_level: str
    location: str
    hours_available: int

class PersonalityTestInput(BaseModel):
    responses: Dict[str, int]

# ── Response Models ─────────────────────────────────────────────────────────

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

class CareerPathSaveInput(BaseModel):
    user_id: str
    career_id: str
    learning_path: Dict[str, Any]

class SkillUpdateInput(BaseModel):
    user_id: str
    skill_name: str
    is_completed: bool

# ── Endpoints ───────────────────────────────────────────────────────────────

@router.post("/personality-test")
async def analyze_personality(test_data: PersonalityTestInput):
    """Analyze personality based on test responses"""
    try:
        result = await service.analyze_personality(test_data.responses)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/recommendations", response_model=List[CareerRecommendation])
async def get_career_recommendations(user_profile: UserProfileInput):
    """Get personalized career recommendations"""
    try:
        recommendations = await service.get_recommendations(user_profile)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/profile")
async def create_profile(user_profile: UserProfileInput):
    """Create / store a user profile"""
    try:
        profile = await service.create_profile(user_profile)
        return profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/career/{career_id}")
async def get_career_details(career_id: str):
    """Get detailed information about a specific career"""
    try:
        career = await service.get_career_details(career_id)
        if not career:
            raise HTTPException(status_code=404, detail="Career not found")
        return career
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/learning-path/{career_id}")
async def generate_learning_path(career_id: str, user_profile: UserProfileInput):
    """Generate personalized learning path for a career"""
    try:
        learning_path = await service.generate_learning_path(career_id, user_profile)
        if not learning_path:
            raise HTTPException(status_code=404, detail="Career not found")
        return learning_path
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/market-trends/{career_id}")
async def get_market_trends(career_id: str):
    """Get market demand and salary trends for a career"""
    try:
        trends = await service.get_market_trends(career_id)
        if not trends:
            raise HTTPException(status_code=404, detail="Career not found")
        return trends
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/career-path")
async def save_career_path(data: CareerPathSaveInput):
    """Save user's selected career path"""
    try:
        path = await service.save_career_path(data.user_id, data.career_id, data.learning_path)
        return path
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/career-path/{user_id}")
async def get_user_path(user_id: str):
    """Get active career path for a user"""
    try:
        path = await service.get_user_path(user_id)
        if not path:
            raise HTTPException(status_code=404, detail="No active path found")
        return path
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/career-path/skill")
async def update_skill_progress(data: SkillUpdateInput):
    """Update progress for a specific skill"""
    try:
        path = await service.update_skill_progress(data.user_id, data.skill_name, data.is_completed)
        if not path:
            raise HTTPException(status_code=404, detail="User path not found")
        return path
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
