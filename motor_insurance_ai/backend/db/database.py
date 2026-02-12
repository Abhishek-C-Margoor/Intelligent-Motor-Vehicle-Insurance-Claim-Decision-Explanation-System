import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    # Fallback for local development if not set, but generally better to enforce env var or .env file
    # For a "GitHub ready" project, we might want to default to empty and raise error, 
    # or default to a local standard if documented. 
    # Let's stick to the plan: enforce it or warn.
    # The original code raised RuntimeError. I will keep it but make it clearer.
    raise RuntimeError(
        "DATABASE_URL environment variable is not set. "
        "Please set it to your PostgreSQL connection string. "
        "Example: postgresql://user:password@localhost:5432/motor_insurance_db"
    )

_lower = DATABASE_URL.lower()
if not (_lower.startswith("postgresql://") or _lower.startswith("postgres://") or "postgresql" in _lower or "postgres" in _lower):
    raise RuntimeError("DATABASE_URL must be a PostgreSQL URL (postgresql://...).")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    from . import models
    # Create tables defined in models (idempotent)
    Base.metadata.create_all(bind=engine)

    # Ensure schema parity: add missing columns required by ORM (safe, idempotent)
    with engine.begin() as conn:
        # Ensure claims.user_id exists
        conn.execute(text("ALTER TABLE claims ADD COLUMN IF NOT EXISTS user_id INTEGER"))
        # Ensure users.hashed_password exists (for migration from mock auth)
        conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS hashed_password VARCHAR"))
