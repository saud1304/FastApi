from pydantic import BaseModel

from pydantic import BaseModel

class Note(BaseModel):
    title: str
    note_description: str
    important: bool = False
