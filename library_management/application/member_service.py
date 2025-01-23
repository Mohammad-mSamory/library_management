from library_management.infrastructure.repositories.Base_repository import \
    MemberRepository


class MemberService:
    def __init__(self, member_repo: MemberRepository):
        self.member_repo = member_repo

    def add_member(self, member_data: dict):
        return self.member_repo.add(member_data)

    def get_member(self, member_id: int):
        return self.member_repo.get(member_id)

    def list_members(self):
        return self.member_repo.list()

    def update_member(self, member_id: int, member_data: dict):
        return self.member_repo.update(member_id, member_data)

    def delete_member(self, member_id: int):
        return self.member_repo.delete(member_id)
