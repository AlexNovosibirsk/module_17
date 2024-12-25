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
    # uvicorn module_16_5:app_17_2 --reload

# pip install alembic
# alembic init migration

""" 
in alembic.ini
sqlalchemy.url = sqlite:///taskmanager.db  (from db.py)

in env.py
from backend.db import Base
from models.user import User
from models.task import Task
target_metadata = Base.metadata
"""

# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head