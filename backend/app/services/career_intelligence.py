import numpy as np
from typing import List, Dict, Any
from datetime import datetime, timedelta
import sys
import os

# Add ai-engine to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../ai-engine')))
from engine import CareerIntelligence

class CareerIntelligenceService:
    def __init__(self):
        self.engine = CareerIntelligence()
        self.career_database = self._load_career_database()
        self.user_paths = {} # In-memory storage for user career paths
        
    def _load_career_database(self):
        """Load career profiles and market data with categories"""
        return {
            # ── Technology Category ────────────────────────────────────────────────
            "data_scientist": {
                "id": "data_scientist",
                "title": "Data Scientist",
                "category": "Technology",
                "description": "Analyze and interpret complex data to help companies make decisions",
                "personality_vector": [0.9, 0.8, 0.4, 0.5, 0.3, 0.9],
                "required_skills": ["Python", "Machine Learning", "Statistics", "SQL", "Data Visualization"],
                "avg_salary": 120000,
                "growth_rate": 0.15,
                "automation_risk": 0.1,
                "education_required": "Bachelor's Degree"
            },
            "devops_engineer": {
                "id": "devops_engineer",
                "title": "DevOps Engineer",
                "category": "Technology",
                "description": "Bridge development and operations for efficient software delivery",
                "personality_vector": [0.7, 0.9, 0.5, 0.6, 0.4, 0.8],
                "required_skills": ["Docker", "Kubernetes", "CI/CD", "Cloud Platforms", "Infrastructure as Code"],
                "avg_salary": 115000,
                "growth_rate": 0.18,
                "automation_risk": 0.12,
                "education_required": "Bachelor's Degree"
            },
            "cybersecurity_analyst": {
                "id": "cybersecurity_analyst",
                "title": "Cybersecurity Analyst",
                "category": "Technology",
                "description": "Protect an organization's computer networks and systems",
                "personality_vector": [0.8, 0.95, 0.4, 0.5, 0.6, 0.85],
                "required_skills": ["Network Security", "Ethical Hacking", "Cryptography", "Incident Response"],
                "avg_salary": 105000,
                "growth_rate": 0.25,
                "automation_risk": 0.05,
                "education_required": "Bachelor's Degree"
            },
            "fullstack_developer": {
                "id": "fullstack_developer",
                "title": "Full Stack Developer",
                "category": "Technology",
                "description": "Develop both client and server software",
                "personality_vector": [0.85, 0.8, 0.6, 0.6, 0.4, 0.9],
                "required_skills": ["JavaScript", "React", "Node.js", "SQL", "CSS"],
                "avg_salary": 110000,
                "growth_rate": 0.12,
                "automation_risk": 0.08,
                "education_required": "Bachelor's Degree"
            },

            # ── Business & Management Category ──────────────────────────────────────
            "sales_manager": {
                "id": "sales_manager",
                "title": "Sales Manager",
                "category": "Business",
                "description": "Plan, direct, or coordinate the delivery of products or services",
                "personality_vector": [0.6, 0.7, 0.9, 0.8, 0.4, 0.7],
                "required_skills": ["Sales Strategy", "Leadership", "Communication", "CRM", "Negotiation"],
                "avg_salary": 95000,
                "growth_rate": 0.05,
                "automation_risk": 0.3,
                "education_required": "Bachelor's Degree"
            },
            "product_manager": {
                "id": "product_manager",
                "title": "Product Manager",
                "category": "Business",
                "description": "Define product strategy and roadmap",
                "personality_vector": [0.8, 0.9, 0.8, 0.7, 0.3, 0.85],
                "required_skills": ["Product Strategy", "Agile", "Market Research", "Analytics", "Communication"],
                "avg_salary": 110000,
                "growth_rate": 0.12,
                "automation_risk": 0.2,
                "education_required": "Bachelor's Degree"
            },
            "business_analyst": {
                "id": "business_analyst",
                "title": "Business Analyst",
                "category": "Business",
                "description": "Help businesses improve their processes and systems",
                "personality_vector": [0.75, 0.85, 0.65, 0.75, 0.45, 0.8],
                "required_skills": ["Requirements Gathering", "Data Analysis", "Process Mapping", "Communication"],
                "avg_salary": 85000,
                "growth_rate": 0.08,
                "automation_risk": 0.15,
                "education_required": "Bachelor's Degree"
            },
            "hr_specialist": {
                "id": "hr_specialist",
                "title": "HR Specialist",
                "category": "Business",
                "description": "Manage recruitment, employee relations, and labor laws",
                "personality_vector": [0.6, 0.75, 0.85, 0.95, 0.35, 0.65],
                "required_skills": ["Recruitment", "Employee Relations", "Communication", "Labor Law"],
                "avg_salary": 65000,
                "growth_rate": 0.04,
                "automation_risk": 0.4,
                "education_required": "Bachelor's Degree"
            },

            # ── Design & Creative Category ──────────────────────────────────────────
            "ux_designer": {
                "id": "ux_designer",
                "title": "UX Designer",
                "category": "Creative",
                "description": "Create meaningful and relevant experiences for users",
                "personality_vector": [0.9, 0.6, 0.7, 0.8, 0.3, 0.8],
                "required_skills": ["User Research", "Wireframing", "Prototyping", "UI Design", "Usability Testing"],
                "avg_salary": 85000,
                "growth_rate": 0.1,
                "automation_risk": 0.15,
                "education_required": "Bachelor's Degree"
            },
            "graphic_designer": {
                "id": "graphic_designer",
                "title": "Graphic Designer",
                "category": "Creative",
                "description": "Create visual concepts to communicate ideas",
                "personality_vector": [0.95, 0.55, 0.6, 0.7, 0.4, 0.85],
                "required_skills": ["Adobe Creative Suite", "Typography", "Branding", "Visual Communication"],
                "avg_salary": 55000,
                "growth_rate": 0.02,
                "automation_risk": 0.25,
                "education_required": "Bachelor's Degree"
            },
            "content_writer": {
                "id": "content_writer",
                "title": "Content Writer",
                "category": "Creative",
                "description": "Produce engaging content for various channels",
                "personality_vector": [0.9, 0.65, 0.55, 0.75, 0.4, 0.7],
                "required_skills": ["Copywriting", "SEO", "Editing", "Storytelling"],
                "avg_salary": 60000,
                "growth_rate": 0.06,
                "automation_risk": 0.35,
                "education_required": "Bachelor's Degree"
            },

            # ── Healthcare & Science Category ───────────────────────────────────────
            "medical_assistant": {
                "id": "medical_assistant",
                "title": "Medical Assistant",
                "category": "Healthcare",
                "description": "Support doctors and other healthcare professionals",
                "personality_vector": [0.55, 0.85, 0.75, 0.98, 0.45, 0.6],
                "required_skills": ["Patient Care", "Medical Records", "Vital Signs", "Empathy"],
                "avg_salary": 40000,
                "growth_rate": 0.15,
                "automation_risk": 0.45,
                "education_required": "Associate's Degree"
            },
            "data_analyst_healthcare": {
                "id": "data_analyst_healthcare",
                "title": "Healthcare Data Analyst",
                "category": "Healthcare",
                "description": "Analyze medical data to improve patient outcomes",
                "personality_vector": [0.8, 0.9, 0.45, 0.55, 0.3, 0.95],
                "required_skills": ["Python", "SQL", "Statistics", "Healthcare Systems"],
                "avg_salary": 85000,
                "growth_rate": 0.12,
                "automation_risk": 0.1,
                "education_required": "Bachelor's Degree"
            },
            
            # ── Marketing category ───────────────────────────────────────
            "marketing_manager": {
                "id": "marketing_manager",
                "title": "Marketing Manager",
                "category": "Business",
                "description": "Develop pricing strategies and direct marketing campaigns",
                "personality_vector": [0.8, 0.7, 0.9, 0.8, 0.4, 0.75],
                "required_skills": ["Marketing Strategy", "SEO", "Content Marketing", "Analytics"],
                "avg_salary": 90000,
                "growth_rate": 0.1,
                "automation_risk": 0.2,
                "education_required": "Bachelor's Degree"
            },
            
            # ── Gaming category ───────────────────────────────────────
            "game_developer": {
                "id": "game_developer",
                "title": "Game Developer",
                "category": "Technology",
                "description": "Design and develop video games for various platforms",
                "personality_vector": [0.9, 0.6, 0.5, 0.6, 0.4, 0.85],
                "required_skills": ["C++", "C#", "Unity", "Unreal Engine", "3D Math"],
                "avg_salary": 95000,
                "growth_rate": 0.12,
                "automation_risk": 0.1,
                "education_required": "Bachelor's Degree"
            }
        }
    
    async def create_profile(self, profile_data):
        """Create user profile"""
        return {
            "id": "user_123",
            "personality_vector": profile_data.personality_vector,
            "current_salary": profile_data.current_salary,
            "skills_owned": profile_data.skills_owned,
            "experience_years": profile_data.experience_years,
            "education_level": profile_data.education_level,
            "location": profile_data.location,
            "created_at": datetime.now().isoformat()
        }
    
    async def analyze_personality(self, responses):
        """Analyze personality from test responses"""
        # Calculate OCEAN scores from responses (4 questions per trait, 0-indexed)
        openness = np.mean([responses.get(f"openness_{i}", 3) for i in range(4)])
        conscientiousness = np.mean([responses.get(f"conscientiousness_{i}", 3) for i in range(4)])
        extraversion = np.mean([responses.get(f"extraversion_{i}", 3) for i in range(4)])
        agreeableness = np.mean([responses.get(f"agreeableness_{i}", 3) for i in range(4)])
        neuroticism = np.mean([responses.get(f"neuroticism_{i}", 3) for i in range(4)])
        
        # Calculate Holland code (simplified)
        realistic = np.mean([responses.get("realistic_1", 3), responses.get("realistic_2", 3)])
        investigative = np.mean([responses.get("investigative_1", 3), responses.get("investigative_2", 3)])
        artistic = np.mean([responses.get("artistic_1", 3), responses.get("artistic_2", 3)])
        social = np.mean([responses.get("social_1", 3), responses.get("social_2", 3)])
        enterprising = np.mean([responses.get("enterprising_1", 3), responses.get("enterprising_2", 3)])
        conventional = np.mean([responses.get("conventional_1", 3), responses.get("conventional_2", 3)])
        
        # Get top 3 Holland codes
        holland_scores = {
            'R': realistic, 'I': investigative, 'A': artistic,
            'S': social, 'E': enterprising, 'C': conventional
        }
        top_codes = sorted(holland_scores, key=holland_scores.get, reverse=True)[:3]
        holland_code = ''.join(top_codes)
        
        personality_vector = [openness, conscientiousness, extraversion, agreeableness, neuroticism, np.mean(list(holland_scores.values()))]
        
        return {
            "personality": {
                "openness": round(openness, 2),
                "conscientiousness": round(conscientiousness, 2),
                "extraversion": round(extraversion, 2),
                "agreeableness": round(agreeableness, 2),
                "neuroticism": round(neuroticism, 2)
            },
            "holland_code": holland_code,
            "personality_vector": personality_vector,
            "interpretation": self._get_personality_interpretation(openness, conscientiousness, extraversion, agreeableness, neuroticism)
        }
    
    def _get_personality_interpretation(self, o, c, e, a, n):
        """Generate personality interpretation"""
        traits = []
        if o > 3.5:
            traits.append("You're curious and open to new experiences")
        if c > 3.5:
            traits.append("You're organized and dependable")
        if e > 3.5:
            traits.append("You're outgoing and energetic")
        if a > 3.5:
            traits.append("You're cooperative and compassionate")
        if n < 2.5:
            traits.append("You're emotionally stable and resilient")
        
        return traits
    
    async def get_recommendations(self, user_profile):
        """Get career recommendations"""
        recommendations = []
        
        for career_id, career_data in self.career_database.items():
            # Calculate match score using engine
            match_score = self.engine.calculate_match(
                user_profile.personality_vector,
                career_data["personality_vector"]
            )
            
            # Calculate risk score
            risk_score = self.engine.calculate_risk_score(
                user_profile.current_salary,
                career_data["avg_salary"],
                1 - career_data["automation_risk"]  # demand index
            )
            
            # Calculate salary projection
            salary_projection = self._project_salary(
                career_data["avg_salary"],
                user_profile.experience_years,
                career_data["growth_rate"]
            )
            
            # Identify skill gaps
            skill_gaps = self._identify_skill_gaps(
                user_profile.skills_owned,
                career_data["required_skills"]
            )
            
            recommendations.append({
                "career_id": career_id,
                "title": career_data["title"],
                "description": career_data["description"],
                "match_score": round(match_score, 2),
                "risk_score": round(risk_score, 2),
                "salary_range": {
                    "min": int(career_data["avg_salary"] * 0.8),
                    "max": int(career_data["avg_salary"] * 1.2),
                    "projected": int(salary_projection)
                },
                "demand_trend": "Rising" if career_data["growth_rate"] > 0.1 else "Stable",
                "automation_risk": career_data["automation_risk"],
                "required_skills": career_data["required_skills"],
                "skill_gaps": skill_gaps,
                "education_required": career_data["education_required"]
            })
        
        # Sort by match score
        recommendations.sort(key=lambda x: x["match_score"], reverse=True)
        return recommendations
    
    def _project_salary(self, base_salary, experience_years, growth_rate):
        """Project salary based on experience and growth"""
        experience_multiplier = 1 + (experience_years * 0.05)  # 5% increase per year
        growth_multiplier = 1 + growth_rate
        return base_salary * experience_multiplier * growth_multiplier
    
    def _identify_skill_gaps(self, owned_skills, required_skills):
        """Identify skills user needs to acquire"""
        owned_set = set(skill.lower() for skill in owned_skills)
        required_set = set(skill.lower() for skill in required_skills)
        return list(required_set - owned_set)
    
    async def get_career_details(self, career_id):
        """Get detailed career information"""
        if career_id not in self.career_database:
            return None
        return self.career_database[career_id]
    
    async def generate_learning_path(self, career_id, user_profile):
        """Generate personalized learning path"""
        career = self.career_database.get(career_id)
        if not career:
            return None
        
        skill_gaps = self._identify_skill_gaps(user_profile.skills_owned, career["required_skills"])
        
        # Estimated hours for each skill
        skill_hours = {
            "python": 40,
            "machine learning": 80,
            "statistics": 60,
            "sql": 30,
            "data visualization": 35,
            "docker": 25,
            "kubernetes": 40,
            "ci/cd": 30,
            "cloud platforms": 50,
            "infrastructure as code": 35,
            "user research": 30,
            "wireframing": 25,
            "prototyping": 30,
            "ui design": 40,
            "usability testing": 25,
            "product strategy": 35,
            "agile": 20,
            "market research": 30,
            "analytics": 40,
            "communication": 20,
            "sales strategy": 30,
            "leadership": 35,
            "crm": 20,
            "negotiation": 25
        }
        
        # Generate timeline using engine
        gaps_with_hours = {}
        for skill in skill_gaps:
            skill_lower = skill.lower()
            gaps_with_hours[skill] = skill_hours.get(skill_lower, 40)
        
        timeline = self.engine.generate_timeline(gaps_with_hours, user_profile.hours_available)
        
        # Calculate total duration
        total_weeks = timeline[-1]["end_week"] if timeline else 0
        
        return {
            "career_title": career["title"],
            "total_duration_weeks": total_weeks,
            "skills_to_learn": skill_gaps,
            "timeline": timeline,
            "milestones": self._generate_milestones(timeline, total_weeks),
            "resources": self._get_learning_resources(skill_gaps)
        }
    
    def _generate_milestones(self, timeline, total_weeks):
        """Generate learning milestones"""
        milestones = []
        if total_weeks > 0:
            milestones.append({
                "week": min(4, total_weeks // 3),
                "description": "Complete foundation courses",
                "type": "foundation"
            })
            milestones.append({
                "week": min(8, total_weeks // 2),
                "description": "Build first project",
                "type": "project"
            })
            milestones.append({
                "week": total_weeks - 4,
                "description": "Portfolio preparation",
                "type": "portfolio"
            })
        return milestones
    
    def _get_learning_resources(self, skills):
        """Get learning resources for skills"""
        resources = {
            "python": [
                {"platform": "Coursera", "course": "Python for Everybody", "url": "https://coursera.org/python"},
                {"platform": "Udemy", "course": "Complete Python Bootcamp", "url": "https://udemy.com/python"}
            ],
            "machine learning": [
                {"platform": "Coursera", "course": "Machine Learning by Andrew Ng", "url": "https://coursera.org/ml"},
                {"platform": "Fast.ai", "course": "Practical Deep Learning", "url": "https://fast.ai"}
            ]
        }
        
        result = []
        for skill in skills:
            skill_lower = skill.lower()
            if skill_lower in resources:
                result.extend(resources[skill_lower])
            else:
                result.append({
                    "platform": "Various",
                    "course": f"{skill} Fundamentals",
                    "url": "#"
                })
        
        return result
    
    async def get_market_trends(self, career_id):
        """Get market demand and salary trends"""
        career = self.career_database.get(career_id)
        if not career:
            return None
        
        # Generate mock time series data
        dates = [(datetime.now() - timedelta(days=30*i)).strftime("%Y-%m") for i in range(12, 0, -1)]
        demand = [0.7 + 0.02*i + np.random.normal(0, 0.05) for i in range(12)]
        salaries = [career["avg_salary"] * (0.9 + 0.01*i + np.random.normal(0, 0.02)) for i in range(12)]
        
        return {
            "career_id": career_id,
            "title": career["title"],
            "historical_demand": [{"date": dates[i], "value": demand[i]} for i in range(12)],
            "historical_salaries": [{"date": dates[i], "value": salaries[i]} for i in range(12)],
            "forecast_demand": self._forecast_values(demand[-3:], 6),
            "forecast_salaries": self._forecast_values(salaries[-3:], 6),
            "market_insights": {
                "growth_rate": career["growth_rate"],
                "automation_risk": career["automation_risk"],
                "emerging_trends": ["AI Integration", "Remote Work", "Data-Driven Decision Making"],
                "top_locations": ["San Francisco", "New York", "London", "Bangalore"]
            }
        }
    
    def _forecast_values(self, recent_values, periods):
        """Simple forecast using linear trend"""
        if len(recent_values) < 2:
            return [recent_values[-1]] * periods
        
        x = list(range(len(recent_values)))
        y = recent_values
        slope = (y[-1] - y[0]) / (len(y) - 1) if len(y) > 1 else 0
        
        forecast = []
        for i in range(periods):
            forecast.append(y[-1] + slope * (i + 1))
        
        return forecast

    async def save_career_path(self, user_id: str, career_id: str, learning_path: dict):
        """Save a user's selected career path"""
        career = self.career_database.get(career_id)
        if not career:
            raise ValueError("Career not found")
            
        skills_progress = []
        for skill in learning_path.get("skills_to_learn", []):
            skills_progress.append({
                "skill": skill,
                "is_completed": False,
                "completed_at": None
            })
            
        user_path = {
            "user_id": user_id,
            "career_id": career_id,
            "career_title": career["title"],
            "total_duration_weeks": learning_path.get("total_duration_weeks", 0),
            "skills_progress": skills_progress,
            "current_week": 1,
            "status": "active",
            "created_at": datetime.now().isoformat()
        }
        
        self.user_paths[user_id] = user_path
        return user_path

    async def get_user_path(self, user_id: str):
        """Get active career path for a user"""
        return self.user_paths.get(user_id)

    async def update_skill_progress(self, user_id: str, skill_name: str, is_completed: bool):
        """Update progress for a specific skill"""
        path = self.user_paths.get(user_id)
        if not path:
            return None
            
        for skill_prog in path["skills_progress"]:
            if skill_prog["skill"].lower() == skill_name.lower():
                skill_prog["is_completed"] = is_completed
                skill_prog["completed_at"] = datetime.now().isoformat() if is_completed else None
                break
                
        # Optional: update current_week or status based on progress
        return path