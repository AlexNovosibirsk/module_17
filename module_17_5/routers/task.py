from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated

from models import *
from sqlalchemy import insert, select, update, delete

from models.task import Task
from models.user import User
from schemas import CreateTask, UpdateTask

from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], add_t: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    db.execute(insert(Task).values(title=add_t.title,
                                   content=add_t.content,
                                   priority=add_t.priority,
                                   slug=slugify(add_t.title),
                                   user_id=user_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.query(Task).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Base of tasks is Empty")
    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    return task


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], upd_task: UpdateTask, task_id: int):
    task_to_update = db.scalar(select(Task).where(User.id == task_id))
    if task_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")
    db.execute(update(Task).where(User.id == task_id).values(   title=upd_task.title,
                                                                content=upd_task.content,
                                                                priority=upd_task.priority))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_delete = db.scalar(select(Task).where(Task.id == task_id))
    if task_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

