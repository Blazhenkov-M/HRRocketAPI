from uuid import UUID

from fastapi import APIRouter, Depends

from app.api.api_v1.schemas.books import SetBookRequest, BookResponse, UpdateBookRequest
from app.api.api_v1.services.books import BookService

router = APIRouter(
    prefix='/books',
    tags=['books'],
)


@router.post('/', summary='Добавление новой книги',
             response_model=BookResponse | None)
async def set_book(params: SetBookRequest, service: BookService = Depends()):
    res = await service.set(params)
    return BookResponse.from_orm(res) if res else None


@router.get('/all', summary='Получить все книги',
            response_model=list[BookResponse])
async def set_book(service: BookService = Depends()):
    res = await service.get_all()
    return [BookResponse.from_orm(i) for i in res if res]


@router.get('/', summary='Получить книгу по id',
            response_model=BookResponse | None)
async def set_book(book_id: UUID, service: BookService = Depends()):
    res = await service.get(book_id)
    return BookResponse.from_orm(res) if res else None


@router.put('/', summary='Обновить данные книги по id',
            response_model=BookResponse | None)
async def set_book(book_id: UUID,
                   params: UpdateBookRequest,
                   service: BookService = Depends()):
    res = await service.update(book_id=book_id, params=params)
    return BookResponse.from_orm(res) if res else None


@router.delete('/', summary='Удалить книгу по id',
               response_model=BookResponse | None)
async def set_book(book_id: UUID, service: BookService = Depends()):
    res = await service.delete(book_id)
    return BookResponse.from_orm(res) if res else None
