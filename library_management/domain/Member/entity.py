
from dataclasses import dataclass
from uuid import UUID


@dataclass
class Member:
    member_id: UUID
    name: str
    email: str
