from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    action_type: str
    created_at: date
    user_id: int
    information: str
