from pydantic import BaseModel
from typing import Optional

class AiRequest(BaseModel):
    description: str
    category: Optional[str] = None
    imageUrl: Optional[str] = None