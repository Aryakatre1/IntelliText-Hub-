# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class DBAnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String, index=True)
    summary_output = Column(String)
    sentiment_output = Column(String)
    timestamp = Column(String)