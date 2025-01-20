
from library_management.infrastructure.database.schema import MemberModel

class MemberService:
    def __init__(self, member_repo):
        self.member_repo = member_repo

    def add_member(self, member: MemberModel):
        self.member_repo.add(member)

    def update_member(self, member: MemberModel):
        self.member_repo.update(member)

    def delete_member(self, member_id: int):
        self.member_repo.delete(member_id)