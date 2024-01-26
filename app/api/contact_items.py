from fastapi import APIRouter, Depends
from schemas.contact import Contact, ContactCreate, ContactUpdate
from depenedencies.database import get_db, SessionLocal
from services.contacts import ContactService
from depenedencies.auth import get_current_user


from schemas.user import User

router = APIRouter()


@router.get("/")
async def list_contacts(
    current_user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)
) -> list[Contact]:
    contact_items = ContactService(db=db).get_all_contacts(current_user)
    return contact_items


@router.get("/{id}")
async def get_detail(
    id: int,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
) -> Contact:
    contact_item = ContactService(db=db).get_by_id(id, current_user)
    return contact_item


@router.post("/")
async def create_contact(
    contact_item: ContactCreate,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
) -> Contact:
    new_item = ContactService(db=db).create_new(contact_item, current_user)
    return new_item


@router.put("/update/{id}")
async def update_contact(
    id: int,
    contact_item: ContactUpdate,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
) -> Contact:
    updated_item = ContactService(db=db).update_contact(id, contact_item, current_user)
    return updated_item


@router.delete("/{id}")
async def contact_delete(
    id: int,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
):
    ContactService(db=db).contact_delete(id, current_user)


@router.get("/search/")
async def find_contact(
    search_key: str,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
) -> list[Contact]:
    contact_items = ContactService(db=db).find_contact(search_key, current_user)
    return contact_items


@router.get("/birthdays/")
async def get_birthdays(
    current_user: User = Depends(get_current_user), db: SessionLocal = Depends(get_db)
) -> list[Contact]:
    contact_items = ContactService(db=db).get_birthdays(current_user)
    return contact_items
