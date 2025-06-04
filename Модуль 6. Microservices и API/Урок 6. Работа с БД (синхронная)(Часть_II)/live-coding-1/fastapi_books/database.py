from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/books_db_ref"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Создаём зависимость для работы с БД в FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
