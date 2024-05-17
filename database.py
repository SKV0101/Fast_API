from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://postgres:admin123@localhost/sachin"

engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()