"""
В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/',
по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI,
объединив все маршруты в одно приложение.
"""
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
    # uvicorn module_16_5:app_17_3 --reload
