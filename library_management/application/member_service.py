from datetime import datetime, timezone
from uuid import UUID, uuid4

from library_management.domain.Member.entity import Member


class MemberService:
    def __init__(self, repository):
        self.repo = repository

    def add_member(self, data: dict) -> Member:

        new_member = Member(
            member_id=uuid4(),
            name=data["name"],
            email=data["email"],
            created_by=data["created_by"],
            created_at=data.get("created_at", datetime.now(timezone.utc)),
            updated_by=data["updated_by"],
            updated_at=data.get("updated_at", datetime.now(timezone.utc))
        )
        return self.repo.add(new_member)

    def update_member(self, member_id: UUID, data: dict) -> Member:
        """Update member from a dictionary"""
        member = self.repo.get(member_id)
        if not member:
            raise ValueError("Member not found")

        for key, value in data.items():
            if hasattr(member, key) and value is not None:
                setattr(member, key, value)

        # Ensure that the `updated_at` field is set if not provided
        if "updated_at" not in data:
            member.updated_at = datetime.now(timezone.utc)

        return self.repo.update(member)

    def get_member(self, member_id: UUID) -> Member:
        member = self.repo.get(member_id)
        if not member:
            raise ValueError("Member not found")
        return member

    def list_members(self) -> list[Member]:
        return self.repo.list_all()

    def delete_member(self, member_id: UUID) -> None:
        if not self.repo.get(member_id):
            raise ValueError("Member not found")
        self.repo.delete(member_id)
