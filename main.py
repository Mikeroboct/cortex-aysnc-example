# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Data(BaseModel):
    msg: str


class EnrichData():
    msg: str
    results: str


@app.post("/")
def handle_post(data: Data):
    result = EnrichData()
    result.msg = data.msg
    result.results = "New Value Here"
    return result


@app.get("/health")
def heath_check():
    return True
