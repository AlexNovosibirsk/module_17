from sqlalchemy.sql.ddl import CreateTable

from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from models import *


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')

# print(CreateTable(User.__table__))
"""
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')
    
    
    
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
"""


# class User(Base):
#     __tablename__ = "user"
#     __table_args__ = {'keep_existing': True}
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     slug = Column(String, unique=True, index=True)
#     description = Column(String)
#     price = Column(Integer)
#     image_url = Column(String)
#     stock = Column(Integer)
#     category_id = Column(Integer, ForeignKey('tasks.id'))
#     rating = Column(Float)
#     is_active = Column(Boolean, default=True)
#     tasks = relationship('Task', back_populates='user')