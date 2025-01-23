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


@router.post("/", response_model=Member)
def add_member(member_data: MemberCreate):
    new_member = member_service.add_member(member_data.model_dump())
    if not new_member:
        raise HTTPException(status_code=400, detail="Member not added.")
    return new_member


@router.get("/", response_model=List[Member])
def get_members():
    return member_service.list_members()


@router.get("/{member_id}", response_model=Member)
def get_member(member_id: UUID):
    member = member_service.get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member


@router.put("/{member_id}", response_model=Member)
def update_member(member_id: UUID, member_data: MemberUpdate):
    updated_member = member_service.update_member(
        member_id, member_data.model_dump())
    if not updated_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return updated_member


@router.delete("/{member_id}")
def delete_member(member_id: UUID):
    member_service.delete_member(member_id)
    return {"detail": "Member deleted successfully."}
