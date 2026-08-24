import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get('/python_to_browser')
def python_to_browser():
    return 'hello from python'

@app.post("/browser_to_python")
def browser_to_python(data:dict):
    print(data)