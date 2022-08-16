from typing import Optional, Union
from fastapi import FastAPI
from . import schemas


app = FastAPI()


@app.post("/blog")
async def create(blog: schemas.Blog):
    return {f"blog returned with {blog.title} title"}
