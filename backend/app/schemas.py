# app/schemas.py
from pydantic import BaseModel
from typing import List

class QueryResponse(BaseModel):
    query: str
    response: str

class ConversationCreate(BaseModel):
    pass

class ConversationUpdate(BaseModel):
    query: str
    response: str
