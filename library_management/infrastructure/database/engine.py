from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Database Configuration (SQLAlchemy)
DATABASE_URL =  "postgresql+psycopg2://mohasam:pass@db:5432/my_database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get the database session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()