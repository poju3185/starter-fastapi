from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel
import json
app = FastAPI()

with open("job_data.json", 'r', encoding='utf-8') as file:
  job_data = json.load(file)

class Item(BaseModel):
    item_id: int


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/react-job-router/job/{id}")
async def read_item(id: str):
    return job_data[id]


@app.get("/react-job-router/job")
async def list_items():
    return [job for job in job_data.values()]

