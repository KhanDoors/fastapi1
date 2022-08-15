from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"Name": "Syyad"}}


@app.get("/about")
def about():
    return {"data": "About Page"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
