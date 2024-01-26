from datetime import datetime
from models.contact import ContactDB
from sqlalchemy import or_, and_


class ContactRepo:
    def __init__(self, db) -> None:
        self.db = db

    def get_all(self, current_user) -> list[ContactDB]:
        return (
            self.db.query(ContactDB).filter(ContactDB.user_id == current_user.id).all()
        )

    def create(self, contact_item, current_user):
        new_item = ContactDB(
            first_name=contact_item.first_name,
            last_name=contact_item.last_name,
            email=contact_item.email,
            phone_number=contact_item.phone_number,
            birthday=contact_item.birthday,
            discription=contact_item.discription,
            user_id=current_user.id,
        )
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def get_by_id(self, id, current_user):
        return (
            self.db.query(ContactDB)
            .filter(and_(ContactDB.id == id, ContactDB.user_id == current_user.id))
            .first()
        )

    def update_contact(self, id, contact_item, current_user):
        current_contact = (
            self.db.query(ContactDB)
            .filter(and_(ContactDB.id == id, ContactDB.user_id == current_user.id))
            .first()
        )

        if current_contact:
            current_contact.first_name = contact_item.first_name
            current_contact.last_name = contact_item.last_name
            current_contact.email = contact_item.email
            current_contact.phone_number = contact_item.phone_number
            current_contact.birthday = contact_item.birthday
            current_contact.description = contact_item.description
        self.db.add(current_contact)
        self.db.commit()
        self.db.refresh(current_contact)
        return current_contact

    def del_by_id(self, id, current_user):
        current_contact = (
            self.db.query(ContactDB)
            .filter(and_(ContactDB.id == id, ContactDB.user_id == current_user.id))
            .first()
        )
        self.db.delete(current_contact)
        self.db.commit()

    def find_contact(self, search_key, current_user):
        contacts = (
            self.db.query(ContactDB)
            .filter(
                or_(
                    and_(
                        ContactDB.first_name.ilike(f"%{search_key}%"),
                        ContactDB.user_id == current_user.id,
                    ),
                    and_(
                        ContactDB.last_name.ilike(f"%{search_key}%"),
                        ContactDB.user_id == current_user.id,
                    ),
                    and_(
                        ContactDB.email.ilike(f"%{search_key}%"),
                        ContactDB.user_id == current_user.id,
                    ),
                )
            )
            .all()
        )

        return contacts

    def get_birthdays(self, current_user):
        result = []
        current_date = datetime.now()
        contacts = self.db.query(ContactDB).filter(ContactDB.user_id == current_user.id)
        for contact in contacts:
            contact_bd = datetime.strptime(contact.birthday, "%Y-%m-%d")
            contact_bd = contact_bd.replace(year=current_date.year)
            delta_days = contact_bd - current_date

            if (delta_days.days <= 6) and (delta_days.days >= 0):
                result.append(contact)
        return result
