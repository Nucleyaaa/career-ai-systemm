import numpy as np
from typing import Dict, List, Tuple

class PersonalityModel:
    """
    Personality assessment model using Big Five (OCEAN) and Holland Code (RIASEC)
    """
    
    def __init__(self):
        self.ocean_questions = self._initialize_ocean_questions()
        self.riasec_questions = self._initialize_riasec_questions()
        
    def _initialize_ocean_questions(self):
        """Initialize Big Five personality questions"""
        return {
            "openness": [
                "I enjoy exploring new ideas and concepts",
                "I prefer variety over routine",
                "I am interested in abstract ideas",
                "I have a rich vocabulary",
                "I enjoy philosophical discussions"
            ],
            "conscientiousness": [
                "I complete tasks thoroughly",
                "I like order and regularity",
                "I follow through on commitments",
                "I plan ahead and organize",
                "I pay attention to details"
            ],
            "extraversion": [
                "I enjoy social gatherings",
                "I feel comfortable around people",
                "I start conversations easily",
                "I talk to many people at parties",
                "I don't mind being the center of attention"
            ],
            "agreeableness": [
                "I sympathize with others' feelings",
                "I take time to help others",
                "I believe people have good intentions",
                "I respect others' decisions",
                "I make people feel at ease"
            ],
            "neuroticism": [
                "I often feel blue",
                "I get stressed out easily",
                "I worry about things",
                "I am easily disturbed",
                "I get upset easily"
            ]
        }
    
    def _initialize_riasec_questions(self):
        """Initialize Holland Code (RIASEC) questions"""
        return {
            "realistic": [
                "I enjoy working with tools and machines",
                "I prefer hands-on activities",
                "I like building or fixing things",
                "I enjoy outdoor activities",
                "I prefer physical work over desk work"
            ],
            "investigative": [
                "I enjoy solving complex problems",
                "I like conducting experiments",
                "I prefer analytical thinking",
                "I enjoy research activities",
                "I like understanding how things work"
            ],
            "artistic": [
                "I enjoy creative expression",
                "I appreciate art and music",
                "I like designing things",
                "I prefer unstructured environments",
                "I enjoy writing or performing"
            ],
            "social": [
                "I enjoy helping others",
                "I like teaching or training people",
                "I prefer collaborative work",
                "I enjoy counseling or advising",
                "I care about others' wellbeing"
            ],
            "enterprising": [
                "I enjoy leading others",
                "I like persuading people",
                "I prefer competitive environments",
                "I enjoy selling or promoting",
                "I like taking risks"
            ],
            "conventional": [
                "I enjoy organizing data",
                "I like clear procedures",
                "I prefer structured environments",
                "I enjoy working with numbers",
                "I like maintaining records"
            ]
        }
    
    def compute_ocean_scores(self, responses: Dict[str, int]) -> Dict[str, float]:
        """
        Compute Big Five scores from questionnaire responses
        
        Args:
            responses: Dictionary mapping question_id to rating (1-5)
            
        Returns:
            Dictionary of OCEAN scores (1-5 scale)
        """
        scores = {}
        for trait, questions in self.ocean_questions.items():
            trait_responses = []
            for i, _ in enumerate(questions):
                question_id = f"{trait}_{i}"
                if question_id in responses:
                    trait_responses.append(responses[question_id])
            
            if trait_responses:
                scores[trait] = np.mean(trait_responses)
            else:
                scores[trait] = 3.0  # Default neutral score
        
        return scores
    
    def compute_riasec_scores(self, responses: Dict[str, int]) -> Dict[str, float]:
        """
        Compute Holland Code scores from questionnaire responses
        
        Args:
            responses: Dictionary mapping question_id to rating (1-5)
            
        Returns:
            Dictionary of RIASEC scores (1-5 scale)
        """
        scores = {}
        for code, questions in self.riasec_questions.items():
            code_responses = []
            for i, _ in enumerate(questions):
                question_id = f"{code}_{i}"
                if question_id in responses:
                    code_responses.append(responses[question_id])
            
            if code_responses:
                scores[code] = np.mean(code_responses)
            else:
                scores[code] = 3.0
        
        return scores
    
    def get_holland_code(self, riasec_scores: Dict[str, float]) -> str:
        """
        Get top 3 Holland codes
        
        Args:
            riasec_scores: Dictionary of RIASEC scores
            
        Returns:
            Three-letter Holland code
        """
        sorted_codes = sorted(riasec_scores.items(), key=lambda x: x[1], reverse=True)
        return ''.join([code[0].upper() for code in sorted_codes[:3]])
    
    def get_personality_vector(self, ocean_scores: Dict[str, float], 
                               riasec_scores: Dict[str, float]) -> List[float]:
        """
        Combine personality scores into a single vector
        
        Args:
            ocean_scores: Big Five scores
            riasec_scores: Holland Code scores
            
        Returns:
            Combined personality vector [O, C, E, A, N, Interest]
        """
        ocean_order = ['openness', 'conscientiousness', 'extraversion', 
                      'agreeableness', 'neuroticism']
        
        ocean_vector = [ocean_scores[trait] for trait in ocean_order]
        interest_score = np.mean(list(riasec_scores.values()))
        
        return ocean_vector + [interest_score]