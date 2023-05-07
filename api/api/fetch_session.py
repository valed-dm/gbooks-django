import json

from django.core.serializers.json import DjangoJSONEncoder

from api.helpers import prepare_list
from api.helpers.get_args import get_args_book
from api.helpers.info_search import info_search
from api.schemas import API
# from .fetch_prepare import data_prepare
from .fetch_result import fetch_result


def fetch_to_session(request):
    args = get_args_book(request)
    books_found, books = fetch_result(args)

    for book in books:
        # serializes book object
        b_dict = book.__dict__
        b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)
        b_key = book.google_book_id
        # stores serialized book object into django session
        request.session[b_key] = b_serialized
        # provides authors, categories string truncated for books.html cards
        book.authors = prepare_list(book.authors)
        book.categories = prepare_list(book.categories)

    info_search(request, args, books_found, len(books))
    # triggers no search performed info to be shown for initial page appearance
    display_start_info = args.title is None

    api = API()
    api.books = books
    api.books_found = books_found
    api.display_start_info = display_start_info

    return api
