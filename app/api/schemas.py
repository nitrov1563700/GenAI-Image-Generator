from pydantic import BaseModel
class ImageRequest(BaseModel):
    prompt: str
    style: str = "realistic"