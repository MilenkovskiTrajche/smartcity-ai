from fastapi import FastAPI
from app.api.ai_controller import router

app = FastAPI()

app.include_router(router)