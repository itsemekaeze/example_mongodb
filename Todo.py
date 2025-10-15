# Models file

from pydantic import BaseModel
from typing import Union
from datetime import datetime

class TodoModel(BaseModel):
    title: str
    desc: str
    isComplete: Union[bool, None] = False
    created_at: Union[datetime, None] = datetime.utcnow()



def TodoHelper(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "desc": todo["desc"],
        "created_at": todo["created_at"]
    }