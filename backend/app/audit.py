from beanie import Document
from pydantic import BaseModel
from datetime import datetime

class AuditEntry(BaseModel):
    query: str
    response: str
    timestamp: datetime

class Audit(AuditEntry, Document):
    class Settings:
        collection = "audit_logs"
