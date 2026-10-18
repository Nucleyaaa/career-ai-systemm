import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from math import ceil
from typing import List, Dict, Any

class CareerIntelligence:
    def __init__(self):
        pass
    
    def calculate_match(self, user_vector, career_vector):
        """
        Calculates personality fit using Cosine Similarity.
        
        Args:
            user_vector: List of user personality traits [O, C, E, A, N, Interest]
            career_vector: List of career ideal personality traits
            
        Returns:
            float: Match percentage (0-100)
        """
        u_vec = np.array(user_vector).reshape(1, -1)
        c_vec = np.array(career_vector).reshape(1, -1)
        similarity = cosine_similarity(u_vec, c_vec)
        return float(similarity[0][0] * 100)

    def calculate_risk_score(self, current_salary, target_min_salary, market_demand_index):
        """
        Risk Score Model (0-100)
        
        Args:
            current_salary: User's current salary
            target_min_salary: Minimum salary for target career
            market_demand_index: 1.0 (Stable) to 0.1 (High Risk/Automation)
            
        Returns:
            float: Risk score (0-100, lower is better)
        """
        # Salary drop risk (if target salary is lower than current)
        salary_drop_risk = max(0, (current_salary - target_min_salary) / max(current_salary, 1))
        
        # Demand risk (inverse of demand index)
        demand_risk = 1 - market_demand_index
        
        # Weighted Risk: 60% Market Stability, 40% Financial Impact
        total_risk = (demand_risk * 0.6) + (salary_drop_risk * 0.4)
        
        # Ensure risk is between 0 and 100
        return min(100, max(0, total_risk * 100))

    def generate_timeline(self, skill_gap, hours_per_week):
        """
        Dynamically generates a learning path.
        
        Args:
            skill_gap: Dictionary of missing skills with estimated study hours
            hours_per_week: Hours user can dedicate per week
            
        Returns:
            list: Timeline with skill learning schedule
        """
        timeline = []
        current_week = 1
        
        for skill, difficulty_hours in skill_gap.items():
            # Calculate weeks needed for this skill
            weeks_needed = ceil(difficulty_hours / max(hours_per_week, 1))
            
            timeline.append({
                "skill": skill,
                "start_week": current_week,
                "end_week": current_week + weeks_needed - 1,
                "duration_weeks": weeks_needed,
                "hours_needed": difficulty_hours,
                "hours_per_week": min(hours_per_week, difficulty_hours)
            })
            
            current_week += weeks_needed
        
        return timeline
