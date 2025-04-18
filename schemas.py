from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    user_id: int
    message: str

class ChatResponse(BaseModel):
    response: str

class MessageSchema(BaseModel):
    bot_response: str
    timestamp: datetime
    
