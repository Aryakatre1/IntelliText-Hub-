# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import StaticPool
from typing import AsyncGenerator

# 1. Database URL
# This tells SQLAlchemy where your SQLite database file will be.
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./sql_app.db"

# 2. Database Engine
# `create_async_engine` is for asynchronous operations.
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True, # Set to True to see SQL queries in the console (useful for debugging)
    connect_args={"check_same_thread": False},
    poolclass=StaticPool, # Essential for SQLite with FastAPI
)

# 3. SessionLocal
# This is a factory for creating database sessions.
AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)

# 4. Base for SQLAlchemy Models
# This is the base class that your SQLAlchemy models will inherit from.
Base = declarative_base()

# 5. Dependency for getting a database session
# This function will be used by FastAPI's Dependency Injection system.
# It provides an asynchronous database session that automatically closes itself.
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session