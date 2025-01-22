
from uuid import UUID
from dataclasses import dataclass



@dataclass
class Member:
    member_id: UUID
    name: str
    email: str