import uvicorn
from fastapi import FastAPI
from routers import user, task

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
    # uvicorn module_17_5:app --reload


"""
1. pip install alembic
2. alembic init migration

in alembic.ini
3. sqlalchemy.url = sqlite:///taskmanager.db  (from db.py)

in env.py
4. add...
from backend.db import Base
from models.user import User
from models.task import Task
target_metadata = Base.metadata

5. alembic revision --autogenerate -m "Initial migration"
6. alembic upgrade head
"""

