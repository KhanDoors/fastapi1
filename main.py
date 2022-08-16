from typing import Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All unpub blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"id": id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    return {"data": {"1", "2"}}


@app.post("/blog")
async def create_item(blog: Blog):
    return {f"blog returned with {blog.title} title"}
