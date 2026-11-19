
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def greet():
    return "FastApi Running o Uvicorn Server!"
greet()