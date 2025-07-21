from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

# We'll add sentiment models here later!
class SentimentResponse(BaseModel):
    label: str # e.g., "POSITIVE", "NEGATIVE", "NEUTRAL"
    score: float # confidence score