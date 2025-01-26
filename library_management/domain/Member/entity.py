
from dataclasses import dataclass
from uuid import UUID

from library_management.domain.shared.base_entity import BaseEntity


@dataclass
class Member(BaseEntity):
    member_id: UUID
    name: str
    email: str
