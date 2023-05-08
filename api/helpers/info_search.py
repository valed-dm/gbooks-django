from django.contrib import messages


def info_search(request, inp, books_found, qty):
    if inp.title is not None:
        sorting = "sorted by 'newest'" if inp.sort == "newest" else ""
        messages.info(request, f"{qty} books displayed on page.")
        messages.info(request, f"{books_found} books found upon request.")
        messages.info(
            request,
            f"API was searched for '{inp.title}' with '{inp.category}'"
            f"category {sorting} among first {inp.pace} items.",
        )
