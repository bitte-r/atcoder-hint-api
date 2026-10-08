from fastapi import APIRouter, Depends
from app.schemas.hint import HintRequest, HintResponse
from app.services.hint_service import HintService
from app.core.config import Settings, get_settings

router = APIRouter(prefix="/hints", tags=["hints"])

def get_hint_service(settings: Settings = Depends(get_settings)) -> HintService:
    return HintService(api_key=settings.GEMINI_API_KEY)

@router.post("", response_model=HintResponse)
def generate_hint(
    request: HintRequest,
    service: HintService = Depends(get_hint_service)
    ):
    return service.generate_hint(request)