from app_17_2.backend.db import Base, engine
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship, Session
from app_17_2.models import *


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
print(CreateTable(User.__table__))

Base.metadata.create_all(bind=engine)