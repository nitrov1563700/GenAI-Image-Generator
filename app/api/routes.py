from fastapi import APIRouter
from app.api.schemas import ImageRequest
from app.services.image_generator import generate_image

router = APIRouter()

@router.post("/generate-image")
def generate_image_api(request: ImageRequest):
    path = generate_image(request.prompt, style=request.style)
    return {"status": "success", "image_path": path}