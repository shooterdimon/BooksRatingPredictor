from pydantic import BaseModel
from fastapi import File

class DataAPI(BaseModel):
    book_image_url: str
    book_genre: str
    book_authors: str
    book_pages: str
    book_review_count: int


class DataFront(BaseModel):
    book_image_url: int
    book_genre: str
    book_authors: str
    book_pages: int
    book_review_count: int