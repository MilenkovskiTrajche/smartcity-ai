from fastapi import APIRouter
from app.models.ai_request import AiRequest
from app.models.ai_response import AiResponse
from app.models.ai_image_description_request import AiImageDescriptionRequest
from app.models.ai_image_description_response import AiImageDescriptionResponse
from app.services.ai_service import AiService

router = APIRouter()
service = AiService()


@router.post("/analyze", response_model=AiResponse)
def analyze(request: AiRequest):
    return service.analyze(request)

@router.post("/generate-description", response_model=AiImageDescriptionResponse)
def generate_description(request: AiImageDescriptionRequest):
    return service.generate_description(request)