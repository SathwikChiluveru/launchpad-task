# app/models.py
from beanie import Document
from pydantic import BaseModel
from typing import List

class QueryResponse(BaseModel):
    query: str
    response: str

class Conversation(Document):
    history: List[QueryResponse]

    class Settings:
        collection = "conversations"  # Make sure the collection name is correct
