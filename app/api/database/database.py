from typing import TypeVar, Generic
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

from app.core.settings import conf

T = TypeVar('T', bound=BaseModel)


class Base(DeclarativeBase):
    __table_args__ = {'extend_existing': True}


class BaseConnection(Generic[T]):
    def __init__(self):
        self.__engine = create_async_engine(url=conf.db_url,
                                            future=True,
                                            connect_args={"server_settings": {"timezone": "UTC"}},
                                            execution_options={"isolation_level": "READ COMMITTED"},
                                            pool_size=10,
                                            max_overflow=10)
        self.session = async_sessionmaker(self.__engine, expire_on_commit=False, class_=AsyncSession)

    async def set(self, params: T):
        raise NotImplementedError

    async def get_all(self):
        raise NotImplementedError

    async def get(self, book_id: UUID):
        raise NotImplementedError

    async def update(self, book_id: UUID, params: T):
        raise NotImplementedError

    async def delete(self, book_id: UUID):
        raise NotImplementedError
