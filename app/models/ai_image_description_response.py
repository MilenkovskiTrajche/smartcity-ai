from pydantic import BaseModel

class AiImageDescriptionResponse(BaseModel):
    description: str