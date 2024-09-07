from pydantic import BaseModel
from datetime import date

class Support(BaseModel):
    case_name: str
    description: str
    created_at: date
    event_id: int
    user_id: int