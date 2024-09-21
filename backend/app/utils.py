from .audit import Audit
from datetime import datetime

async def save_audit(query: str, response: str):
    audit_entry = Audit(query=query, response=response, timestamp=datetime.utcnow())
    await audit_entry.insert()
