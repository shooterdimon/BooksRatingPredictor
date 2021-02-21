from pydantic import BaseModel

class Data(BaseModel):
    book_title: str
    book_image_url: str
    book_desc: str
    book_genre: str
    book_authors: str
    book_format: str
    book_pages: str
    book_review_count: int
    book_rating_count: int