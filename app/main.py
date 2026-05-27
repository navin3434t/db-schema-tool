from fastapi import FastAPI
from app.api.database import router as database_router

app = FastAPI(
    title="Database Schema API",
    version="1.0.0"
)

app.include_router(database_router)


@app.get("/")
def root():
    return {
        "message": "Database Schema API Running"
    }