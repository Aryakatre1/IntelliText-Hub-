# schemas.py
from pydantic import BaseModel
from typing import Optional

class AnalysisResult(BaseModel):
    id: int
    input_text: str
    summary_output: Optional[str] = None
    sentiment_output: Optional[str] = None
    timestamp: str

    class Config:
        from_attributes = True # This tells Pydantic to read data from ORM models

class TextInput(BaseModel):
    text: str