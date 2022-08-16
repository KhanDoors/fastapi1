from pydantic import BaseModel
from typing import Optional, Union


class Blog(BaseModel):
    title: str
    body: str
