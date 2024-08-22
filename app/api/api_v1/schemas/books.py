from uuid import UUID

from pydantic import BaseModel, Field


class BaseSchemas(BaseModel):
    class Config:
        from_attributes = True


class BookSchema(BaseSchemas):
    title: str = Field(..., min_length=1, max_length=255, description='Title of the book')
    author: str = Field(..., min_length=1, max_length=255, description='Author of the book')
    published_year: int | None = Field(None, description='Published year')
    summary: str | None = Field(None, min_length=1, max_length=255, description='Summary')


class UUIDSchemas(BaseModel):
    id: UUID = Field(..., description='UUID of the book')


class SetBookRequest(BookSchema):
    ...

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Три мушкетёра",
                "author": "А. Дюма",
                "published_year": 1844,
                "summary": "Интересная книга"
            }
        }


class UpdateBookRequest(BookSchema):
    ...

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Мастер и Маргарита",
                "author": "Михаил Булгаков",
                "published_year": 1967,
                "summary": "Очень интересная книга"
            }
        }


class BookResponse(UUIDSchemas, BookSchema):
    ...
