from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


sqlite_database = "sqlite:///taskmanager.db"
engine = create_engine(sqlite_database, echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
# pip install alembic
# alembic init module_17_3/migrations
# in alembic.ini -> sqlalchemy.url = sqlite:///taskmanager.db

# in env.py
# from module_17_3.backend.db import Base
# from module_17_3.models.user import User
# from module_17_3.models.task import Task
# target_metadata = Base.metadata

# alembic revision --autogenerate -m "initial migration"
# alembic upgrade head