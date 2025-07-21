# routers/history.py
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

# --- Import from the main project directory ---
from database import get_db
from models import DBAnalysisResult
from schemas import AnalysisResult

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

@router.get("/", response_model=List[AnalysisResult])
async def get_history(db: AsyncSession = Depends(get_db)):
    """
    Retrieves the complete history of all text analysis results from the database.
    """
    # 1. Use the new asynchronous query syntax with `select`
    query_statement = select(DBAnalysisResult)
    
    # 2. Execute the query and await the result
    results = await db.execute(query_statement)
    
    # 3. Get the list of ORM objects from the result
    history_list = results.scalars().all()
    
    # FastAPI's response_model will automatically convert these to Pydantic objects.
    return history_list