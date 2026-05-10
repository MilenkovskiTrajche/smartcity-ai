from fastapi import APIRouter
from app.models.ai_request import AiRequest
from app.models.ai_response import AiResponse
from app.services.ai_service import AiService

router = APIRouter()
service = AiService()


@router.post("/analyze", response_model=AiResponse)
def analyze(request: AiRequest):
    return service.analyze(request)