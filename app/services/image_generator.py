import uuid
from PIL import Image
from app.models.model_loader import load_model
from app.services.prompt_engine import enhance_promt

pipe = load_model()

def generate_image(prompt: str, style: str):
    final_promt = enhance_promt(prompt, style)
    image = pipe(final_promt).images[0]
    image_id = str(uuid.uuid4())
    save_path = f"data/generated_images/{image_id}.png"
    image.save(save_path)
    return save_path