from typing import TypeVar
from uuid import UUID

from sqlalchemy import select, update, delete
from pydantic import BaseModel

from app.api.database import Book
from app.api.database.database import BaseConnection

T = TypeVar('T', bound=BaseModel)


class BookService(BaseConnection[T]):

    async def set(self, params: T):
        async with self.session() as session:
            async with session.begin():
                new_book = Book(**params.dict())
                session.add(new_book)
                await session.commit()
                return new_book

    async def get_all(self):
        async with self.session() as session:
            async with session.begin():
                query = select(Book)
                res = await session.execute(query)
                return res.scalars().all()

    async def get(self, book_id: UUID):
        async with self.session() as session:
            async with session.begin():
                query = select(Book).where(Book.id == book_id)
                res = await session.execute(query)
                return res.scalar()

    async def update(self, book_id: UUID, params: T):
        async with (self.session() as session):
            async with session.begin():
                query = update(Book).where(Book.id == book_id).values(**params.dict()).returning(Book)
                res = await session.execute(query)
                return res.scalar()

    async def delete(self, book_id: UUID):
        async with self.session() as session:
            async with session.begin():
                query = delete(Book).where(Book.id == book_id).returning(Book)
                res = await session.execute(query)
                return res.scalar()
