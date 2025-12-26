from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="GenAI Image Generator")
app.include_router(router)