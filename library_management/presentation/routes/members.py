from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from library_management.application.member_service import MemberService
from library_management.infrastructure.repositories.Base_repository import \
    MemberRepository
from library_management.presentation.models.models import (Member,
                                                           MemberCreate,
                                                           MemberUpdate)

router = APIRouter()

# Initialize repository and service
member_repo = MemberRepository()
member_service = MemberService(member_repo)


def raise_http_exception(status_code: int, detail: str):
    """Helper function to raise HTTPException."""
    raise HTTPException(status_code=status_code, detail=detail)


@router.post("/members", response_model=Member)
def add_member(member_data: MemberCreate):
    new_member = member_service.add_member(member_data.model_dump())
    if not new_member:
        raise_http_exception(400, "Member not added.")
    return new_member


@router.get("/members", response_model=List[Member])
def get_members():
    members = member_service.list_members()
    if not members:
        raise_http_exception(404, "No members found.")
    return members


@router.get("/members/{member_id}", response_model=Member)
def get_member(member_id: UUID):
    member = member_service.get_member(member_id)
    if not member:
        raise_http_exception(404, "Member not found.")
    return member


@router.put("/members/{member_id}", response_model=Member)
def update_member(member_id: UUID, member_data: MemberUpdate):
    updated_member = member_service.update_member(
        member_id, member_data.model_dump())
    if not updated_member:
        raise_http_exception(404, "Member not found.")
    return updated_member


@router.delete("/members/{member_id}")
def delete_member(member_id: UUID):
    try:
        member_service.delete_member(member_id)
    except ValueError as e:
        raise_http_exception(404, str(e))
    return {"detail": "Member deleted successfully."}
