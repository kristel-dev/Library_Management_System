class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self._book_id: str = book_id
        self._title: str = title
        self._author: str = author
        self._available: bool = True

    def get_book_id(self) -> str:
        return self._book_id

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def is_available(self) -> bool:
        return self._available

    def set_available(self, available: bool):
        self._available = available

    def __str__(self):
        status = "Available" if self._available else "Unavailable"
        return f"[{self._book_id}] {self._title} by {self._author} - {status}”
