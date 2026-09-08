from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_db
from app.models import Book as BookModel
from app.schemas import BookCreate, BookResponse


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/search", response_model=list[BookResponse])
def search_books(title: str, db: Session = Depends(get_db)):
    found_books = (
        db.query(BookModel)
        .filter(BookModel.title.ilike(f"%{title}%"))
        .all()
    )

    if found_books:
        return found_books

    raise HTTPException(status_code=404, detail="Book not found")


@router.get("", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(
        title=book.title,
        author=book.author
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    updated_book: BookCreate,
    db: Session = Depends(get_db)
):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author

    db.commit()
    db.refresh(book)

    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}


@router.get("/count")
def count_books(db: Session = Depends(get_db)):
    count = db.query(BookModel).count()
    return {"count": count}
