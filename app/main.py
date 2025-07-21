# main.py
from fastapi import FastAPI
from .routers import summarizer, sentiment, history  # Line 1: Add 'history' here
from database import engine, Base

app = FastAPI(
    title="AI Text Analysis API",
    description="A backend API for text summarization and sentiment analysis using Hugging Face models.",
    version="0.1.0",
)

# --- NEW: Asynchronous Startup Event ---
# This will create the database tables once the app starts.
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully!")

# Your existing router includes
app.include_router(summarizer.router)
app.include_router(sentiment.router)
app.include_router(history.router)  # Line 2: Add this line to include the history router