from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

items = {
    1: {"name": "Sample Item", "description": "A starter item", "price": 9.99}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        return {"error": "Item not found"}
    return item

@app.post("/items")
def create_item(item: Item):
    new_id = max(items.keys()) + 1
    items[new_id] = item.dict()
    return {"id": new_id, **item.dict()}
