from library.models import Book


def save_book_to_library(
    book,
    image_src,
    authors,
    categories,
    authors_str="-no author-",
):
    book_to_library = Book(
        authors_str=authors_str,
        title=book.title,
        description=book.description,
        date=book.date,
        google_book_id=book.google_book_id,
        rubric="read_asap",
        remark="no remark added",
        image_src=image_src,
    )

    # primarily saves book_to_library data into db
    # for a reason that book_id is necessary to perform coming next m2m operations
    book_to_library.save()
    # m-2-m operations on book object in db are performed
    # m-2-m association tables are filled in automatically
    book_to_library.authors.set(authors)
    book_to_library.categories.set(categories)
