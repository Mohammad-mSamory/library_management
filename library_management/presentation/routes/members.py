from fastapi import APIRouter, Depends, HTTPException
from typing import List
from library_management.presentation.models.models import MemberIn, MemberOut
from library_management.infrastructure.database.engine import get_db
from library_management.infrastructure.repositories.Base_repository import MemberRepository
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=MemberOut)
def add_member(member: MemberIn, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    new_member = member_repo.add(member.model_dump())
    return new_member

@router.get("/", response_model=List[MemberOut])
def list_members(db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    return member_repo.list()

@router.get("/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    member = member_repo.get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.put("/{member_id}", response_model=MemberOut)
def update_member(member_id: int, member: MemberIn, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    existing_member = member_repo.get(member_id)
    if not existing_member:
        raise HTTPException(status_code=404, detail="Member not found")
    for key, value in member.model_dump().items():
        setattr(existing_member, key, value)
    member_repo.update(existing_member)
    return existing_member

@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    member_repo.delete(member_id)
    return {"message": "Member deleted successfully"}
