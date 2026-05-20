from book import Book
from member import Member
from exception import BookUnavailableError

class Loan:
    def __init__(self, loan_id: str, book: Book, member: Member):
        self._loan_id: str = loan_id
        self._book: Book = book
        self._member: Member = member
        self._is_active: bool = True

    def get_loan_id(self) -> str:
        return self._loan_id

    def get_book(self) -> Book:
        return self._book

    def get_member(self) -> Member:
        return self._member

    def is_active(self) -> bool:
        return self._is_active

    def activate(self):
        if self._book.is_available():
            self._book.set_available(False)
            self._is_active = True
        else:
            raise BookUnavailableError(f"Book {self._book.get_book_id()} is not available!")

    def deactivate(self):
        self._book.set_available(True)
        self._is_active = False

    def __str__(self):
        status = "Active" if self._is_active else "Returned"
        return f"[{self._loan_id}] {self._book.get_title()} → {self._member.get_name()} [{status}]”