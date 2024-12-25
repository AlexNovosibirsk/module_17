from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated

from models import *
from sqlalchemy import insert, select, delete, update

from models.user import User
from schemas import CreateUser, UpdateUser
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Base of users is Empty")
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    return user


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], add_user: CreateUser):
    db.execute(insert(User).values(    username=add_user.username,
                                       firstname=add_user.firstname,
                                       lastname=add_user.lastname,
                                       age=add_user.age,
                                       slug=slugify(add_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], updt_user: UpdateUser, user_id: int):
    user_to_update = db.scalar(select(User).where(User.id == user_id))
    if user_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    db.execute(update(User).where(User.id == user_id).values(   firstname=updt_user.firstname,
                                                                lastname=updt_user.lastname,
                                                                age=updt_user.age))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}



@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
