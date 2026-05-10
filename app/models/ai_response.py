from pydantic import BaseModel

class AiResponse(BaseModel):
    category: str
    summary: str
    priority: str
    confidence: float
    categoryMatch: bool