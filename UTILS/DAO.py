import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

mysqlPass = os.getenv("MYSQL-PASS")
SCHEMA="clinicapp-py"
DATABASE_URL = f"mysql+pymysql://root:{mysqlPass}@localhost/{SCHEMA}?charset=utf8mb4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def createSesion():
        db = SessionLocal()
        try:
            return db
        finally:
            db.close()


def save(obj):
    session = createSesion()
    session.add(obj)
    session.flush()
    session.commit()
    session.refresh(obj)
    session.close()
    return obj

def select(clase):
    session = createSesion()
    return session.query(clase).all()
    session.close()
