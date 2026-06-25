                

from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Resume Screener API")

app.include_router(router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Resume Screener API"}
