from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# --------- REQUEST ---------

class AiRequest(BaseModel):
    description: str
    category: Optional[str] = None
    imageUrl: Optional[str] = None


# --------- RESPONSE ---------

class AiResponse(BaseModel):
    category: str
    summary: str
    priority: str
    institutionCategory: str
    confidence: float
    categoryMatch: bool


# --------- CORE ENDPOINT ---------

@app.post("/analyze", response_model=AiResponse)
def analyze(request: AiRequest):

    text = request.description.lower()

    # --- simple logic (placeholder AI) ---
    category = "other"
    priority = "LOW"
    institution = "general"

    if "water" in text or "leak" in text:
        category = "water"
        institution = "water"
        priority = "HIGH"

    if "fire" in text:
        category = "electricity"
        institution = "electricity"
        priority = "CRITICAL"

    summary = request.description[:120]

    match = request.category == category if request.category else True

    return AiResponse(
        category=category,
        summary=summary,
        priority=priority,
        institutionCategory=institution,
        confidence=0.85,
        categoryMatch=match
    )