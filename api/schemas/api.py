from dataclasses import dataclass, field


@dataclass
class API:
    books: list = field(default_factory=lambda: [])
    books_found: str = ""
    display_start_info: bool = True
