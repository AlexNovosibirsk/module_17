from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


sqlite_database = "sqlite:///taskmanager.db"
engine = create_engine(sqlite_database, echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
