from typing import Union

from fastapi import FastAPI

app = FastAPI()
#endpoints
#addnewbook
#submitreview
#Retrieve all books with an option to filter by author or publication year.
#Retrieve all reviews for a specific book.
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    book_id: int
    text: str
    rating: int

# Dummy database
books_db = {}
reviews_db = {}

book_id_counter = 0

@app.post("/books/")
def add_book(book: Book):
    global book_id_counter
    book_id_counter += 1
    books_db[book_id_counter] = book
    return {"message": "Book added successfully", "book_id": book_id_counter}

@app.post("/reviews/")
def submit_review(review: Review):
    if review.book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    if review.rating < 1 or review.rating > 5:
        raise HTTPException(status_code=400, detail="Invalid rating. Rating must be between 1 and 5")
    if review.book_id not in reviews_db:
        reviews_db[review.book_id] = []
    reviews_db[review.book_id].append(review)
    return {"message": "Review submitted successfully"}

@app.get("/books/")
def get_books(author: Optional[str] = None, publication_year: Optional[int] = None):
    filtered_books = []
    for book_id, book in books_db.items():
        if (not author or book.author == author) and (not publication_year or book.publication_year == publication_year):
            filtered_books.append({book_id: book.dict()})
    return filtered_books

@app.get("/reviews/{book_id}")
def get_reviews(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    if book_id not in reviews_db or not reviews_db[book_id]:
        raise HTTPException(status_code=404, detail="No reviews found for this book")
    return reviews_db[book_id]
