import uvicorn
from fastapi import FastAPI
from routers import task, user


app = FastAPI()
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
    # uvicorn.run(app_17_3, host="10.0.0.135", port=4100) # 37.192.207.115


# pip install alembic
# alembic init migrations
# in alembic.ini -> sqlalchemy.url = sqlite:///taskmanager.db

# in env.py
# from backend.db import Base
# from models.user import User
# from models.task import Task
# target_metadata = Base.metadata

# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head
