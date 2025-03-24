from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Contact
from src.repository.contacts import ContactRepository
from src.schemas import ContactBase


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactRepository(db)

    async def create_contact(self, body: ContactBase) -> Contact:
        return await self.contact_repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int, q: str | None = None) -> Sequence[Contact]:
        return await self.contact_repository.get_contacts(skip, limit, q)

    async def get_contact(self, contact_id: int) -> Contact:
        return await self.contact_repository.get_contact_by_id(contact_id)

    async def remove_contact_by_id(self, contact_id: int) -> Contact:
        return await self.contact_repository.remove_contact(contact_id)

    async def update_contact(self, contact_id: int, body: ContactBase) -> Contact | None:
        return await self.contact_repository.update_contact(contact_id, body)

    async def birthday_reminder(self) -> Sequence[Contact]:
        return await self.contact_repository.birthday_reminder()











    # async def update_note(self, note_id: int, body: NoteUpdate):
    #     tags = await self.tag_repository.get_tags_by_ids(body.tags)
    #     return await self.note_repository.update_note(note_id, body, tags)
    #
    # async def update_status_note(self, note_id: int, body: NoteStatusUpdate):
    #     return await self.note_repository.update_status_note(note_id, body)
    #
