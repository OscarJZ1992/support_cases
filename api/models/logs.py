from pydantic import BaseModel

class Log(BaseModel):
    id: int
    data: str