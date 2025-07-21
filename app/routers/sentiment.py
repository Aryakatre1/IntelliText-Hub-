# routers/sentiment.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

# --- Your existing imports ---
from ..models import TextRequest, SentimentResponse
from ..services.sentiment_service import sentiment_service

# --- NEW: Database imports ---
# Assuming these are in your project root
from models import DBAnalysisResult
from database import get_db

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: TextRequest, db: AsyncSession = Depends(get_db)):
    """
    Analyzes the sentiment of the given text and saves the analysis to the database.
    """
    # 1. Your existing service call to get the sentiment
    sentiment_result = sentiment_service.get_sentiment(request.text)

    # 2. NEW: Create a new database record object
    db_result = DBAnalysisResult(
        input_text=request.text,
        sentiment_output=sentiment_result['label'], # Assuming your service returns a dictionary
        timestamp=datetime.now().isoformat()
    )

    # 3. NEW: Add to the database session and commit
    db.add(db_result)
    await db.commit()
    await db.refresh(db_result)

    # 4. Your existing response
    return sentiment_result