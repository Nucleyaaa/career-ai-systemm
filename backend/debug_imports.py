import sys
import os

print("Python version:", sys.version)
print("Current directory:", os.getcwd())

try:
    import fastapi
    print("FastAPI imported")
except ImportError as e:
    print("FastAPI import failed:", e)

try:
    import numpy as np
    print("Numpy imported")
except ImportError as e:
    print("Numpy import failed:", e)

try:
    from sklearn.metrics.pairwise import cosine_similarity
    print("Sklearn imported")
except ImportError as e:
    print("Sklearn import failed:", e)

# Test the path logic from routes.py
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'ai-engine')))
print("Appended to path:", sys.path[-1])

try:
    from engine import CareerIntelligence
    print("CareerIntelligence imported from engine")
except ImportError as e:
    print("CareerIntelligence import failed:", e)

try:
    from app.services.career_intelligence import CareerIntelligenceService
    print("CareerIntelligenceService imported")
    service = CareerIntelligenceService()
    print("CareerIntelligenceService initialized")
except Exception as e:
    print("CareerIntelligenceService failure:", e)
    import traceback
    traceback.print_exc()
