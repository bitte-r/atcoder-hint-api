from fastapi import FastAPI
from app.api.v1.hints import router as hints_router

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

app.include_router(hints_router, prefix="/api/v1")


# reload test