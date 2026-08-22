import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get('/python_to_browser')
def python_to_browser():
    return 'hello from python'

@app.post("/browser_to_python")
def get_data(data:dict):
    print(data)

if __name__ == '__main__':
    os.system('uvicorn main:app --reload')