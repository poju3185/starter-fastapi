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
    return {"message": "Hello World"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/react-job-router/{id}")
async def read_item(id: str):
    return job_data[id]


@app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@app.post("/items/")
async def create_item(item: Item):
    return item
