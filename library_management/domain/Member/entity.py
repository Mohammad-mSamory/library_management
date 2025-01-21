
from uuid import UUID
from dataclasses import dataclass
import re

@dataclass
class Email:
    email: str

    def __post_init__(self):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.email):
            raise ValueError("Invalid email format")

@dataclass
class Member:
    member_id: UUID
    name: str
    email: Email