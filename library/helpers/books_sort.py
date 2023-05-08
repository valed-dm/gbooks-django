def sort_rubric(rubric, books):
    res = books
    if rubric != "all":
        res = [book for book in books if book.rubric == rubric]
    return res


def sort_category(category, books):
    res = books
    if category != "all":
        res = list(book.categories for book in books)
    return res


def sort_author(author, books):
    res = books
    if author != "all":
        res = list(book.authors for book in books)
    return res


def sort_date(sort, books):
    res = books
    if sort == "newest":
        res.sort(key=lambda book: book.date, reverse=True)
    return res


def sort_books(req, library_books):
    result = sort_rubric(
        req.rubric,
        sort_category(
            req.category, sort_author(req.author, sort_date(req.sort, library_books))
        ),
    )

    return result
