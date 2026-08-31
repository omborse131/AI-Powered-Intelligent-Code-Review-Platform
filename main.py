from fastapi import FastAPI

from app.database import Base, engine
from app.models.review import CodeReview
from app.routes.review import router as review_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI-Powered Intelligent Code Review Platform",
    description="AI-powered code analysis and review system",
    version="1.0.0"
)


app.include_router(review_router)


@app.get("/")
def root():
    return {
        "message": "AI Code Review Platform API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }