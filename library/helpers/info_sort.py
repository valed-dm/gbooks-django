from django.contrib import messages


def info_sort_library(request, inp):
    if inp.rubric is None:
        messages.info(request, "Library shown in fifo order:")
    else:
        messages.info(request, "Library filtered with params: ")
        messages.info(request, f"rubric: {inp.rubric}, category: {inp.category}")
        messages.info(request, f"author: {inp.author}, sort: {inp.sort}")
