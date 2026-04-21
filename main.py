from fastapi import FastAPI
from app.api.routes import router as main_router
from app.api.webhook import router as webhook_router
app = FastAPI()
app.include_router(main_router)
app.include_router(webhook_router)
@app.get("/")
def root():
    return {"message":"AI code review Bot"}