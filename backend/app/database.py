# app/database.py
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Conversation
import os

async def init_db():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL", "mongodb://mongodb:27017"))
    database = client.conversations_db
    await init_beanie(database, document_models=[Conversation])
