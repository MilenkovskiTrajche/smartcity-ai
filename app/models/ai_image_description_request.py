from pydantic import BaseModel
from typing import Optional

class AiImageDescriptionRequest(BaseModel):
    imageUrl: str
