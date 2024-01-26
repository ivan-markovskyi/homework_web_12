from repo.contacts import ContactRepo
from schemas.contact import Contact, ContactCreate, ContactUpdate


class ContactService:
    def __init__(self, db):
        self.repo = ContactRepo(db=db)

    def get_all_contacts(self, current_user) -> list[Contact]:
        all_contacts_from_db = self.repo.get_all(current_user)
        result = [Contact.from_orm(item) for item in all_contacts_from_db]
        return result

    def create_new(self, contact_item: ContactCreate, current_user) -> Contact:
        new_item_from_db = self.repo.create(contact_item, current_user)
        contact_item = Contact.from_orm(new_item_from_db)
        return contact_item

    def get_by_id(self, id: int, current_user) -> Contact:
        contact_item = self.repo.get_by_id(id, current_user)
        return Contact.from_orm(contact_item)

    def update_contact(
        self, id: int, contact_item: ContactUpdate, current_user
    ) -> Contact:
        contact_item = self.repo.update_contact(id, contact_item, current_user)
        return Contact.from_orm(contact_item)

    def contact_delete(self, id: int, current_user):
        self.repo.del_by_id(id, current_user)

    def find_contact(self, search_key: str, current_user) -> list[Contact]:
        all_found_contacts = self.repo.find_contact(search_key, current_user)
        result = [Contact.from_orm(item) for item in all_found_contacts]
        return result

    def get_birthdays(self, current_user) -> list[Contact]:
        all_contacts = self.repo.get_birthdays(current_user)
        result = [Contact.from_orm(item) for item in all_contacts]
        return result
