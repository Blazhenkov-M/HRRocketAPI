from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

from app.api.database.database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    published_year: Mapped[int] = mapped_column(nullable=True)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
