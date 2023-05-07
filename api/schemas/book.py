import datetime
from dataclasses import dataclass, field


@dataclass
class Book:
    authors: list = field(default_factory=lambda: ["-no author-"])
    categories: list = field(default_factory=lambda: ["-no category-"])
    date: datetime.date = "1900-01-01"
    description: str = "no description"
    google_book_id: str = ""
    image_src: str = "/static/img/no_cover.webp"
    title: str = "no title"
    rubric: str = "read_asap"
    remark: str = ""
