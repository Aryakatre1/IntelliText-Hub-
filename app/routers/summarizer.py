# routers/summarizer.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

# --- Your existing imports ---
from ..models import TextRequest, SummaryResponse
from ..services.summarization_service import summarization_service

# --- NEW: Database imports ---
# Assuming these are in your project root
from models import DBAnalysisResult
from database import get_db

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: TextRequest, db: AsyncSession = Depends(get_db)):
    """
    Summarizes the given text using a pre-trained Hugging Face model
    and saves the analysis to the database.
    """
    # 1. Your existing service call to get the summary
    summary_text = summarization_service.get_summary(request.text)

    # 2. NEW: Create a new database record object
    db_result = DBAnalysisResult(
        input_text=request.text,
        summary_output=summary_text,
        timestamp=datetime.now().isoformat()
    )

    # 3. NEW: Add to the database session and commit
    db.add(db_result)
    await db.commit()
    await db.refresh(db_result) # Optional, but useful to get the record ID

    # 4. Your existing response
    return {"summary": summary_text}