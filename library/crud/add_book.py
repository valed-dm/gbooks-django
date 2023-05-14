from django.shortcuts import redirect

from api.schemas import Book
from library.helpers.authors_str import authors_string
from library.helpers.info_add import info_add
from library.helpers.info_exists import info_exists
from library.models import Author, Book as DB_Book, Category, Image
from .get_or_create import get_or_create
from .save_book import save_book_to_library


def add_book(request, book):
    # truncates names to avoid doubles in db authors, categories
    book_authors = [author.strip() for author in book["authors"]]
    book_categories = [category.strip() for category in book["categories"]]
    # gets or creates authors, categories to be filled in m-2-m Book fields
    authors = get_or_create(Author, book_authors)
    categories = get_or_create(Category, book_categories)
    # still not in use at the moment but is left for the future
    authors_str = authors_string(book_authors)
    # checks if book already added to db before
    book_exists = (
        DB_Book.objects.all().filter(google_book_id=book["google_book_id"]).exists()
    )
    # fills in Image table to provide data for 1-2-1 image_src field
    image_src = Image(image_src=book["image_src"])
    # primarily saves data to get image_src_id
    image_src.save()

    # prepares book data to be filled in books table
    if book_exists:
        info_exists(request, book["title"])
        return redirect("book/")

    book_to_library = Book()
    book_to_library.title = book["title"]
    book_to_library.description = book["description"]
    book_to_library.date = book["date"]
    book_to_library.google_book_id = book["google_book_id"]

    save_book_to_library(book_to_library, image_src, authors, categories, authors_str)
    info_add(request, book["title"])

    return book
