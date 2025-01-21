from uuid import UUID


from library_management.domain.Member.entity import Member


class MemberService:
    def __init__(self, member_repository):
        self.member_repository = member_repository

    def add_member(self, member: Member):
        self.member_repository.add(member)

    def update_member(self, member: Member):
        self.member_repository.update(member)

    def delete_member(self, member_id: UUID):
        self.member_repository.delete(member_id)