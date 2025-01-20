from datetime import datetime
from uuid import UUID
from typing import Optional
from dataclasses import dataclass



@dataclass
class Member:
    member_id: UUID
    name: str
    email: str