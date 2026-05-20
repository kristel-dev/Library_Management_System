from book import Book
from member import Member
from loan import Loan
from exception import (
    BookNotFoundError, MemberNotFoundError, BookUnavailableError, 
    InvalidInputError, LoanNotFoundError
)

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = {}

    def add_book(self, book: Book):
        self.books[book.get_book_id()] = book
        print(f"✅ Book '{book.get_title()}' added!")

    def add_member(self, member: Member):
        self.members[member.get_member_id()] = member
        print(f"✅ Member '{member.get_name()}' registered!")

    def create_loan(self, loan_id: str, book_id: str, member_id: str):
        if book_id not in self.books:
            raise BookNotFoundError(f"Book '{book_id}' not found!")
        
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member '{member_id}' not found!")
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not book.is_available():
            raise BookUnavailableError(f"Book '{book.get_title()}' is unavailable!")
        
        loan = Loan(loan_id, book, member)
        loan.activate()
        self.loans[loan_id] = loan
        print(f"✅ Book borrowed! Loan ID: {loan_id}")

    def return_loan(self, loan_id: str):
        if loan_id not in self.loans:
            raise LoanNotFoundError(f"Loan '{loan_id}' not found!")
        
        loan = self.loans[loan_id]
        loan.deactivate()
        print(f"✅ Book returned! Loan ID: {loan_id}")

    def list_books(self):
        if not self.books:
            print("📚 No books available.")
            return
        print("\n📚 Books:")
        for book in self.books.values():
            print(f"  {book}")

    def list_members(self):
        if not self.members:
            print("👥 No members registered.")
            return
        print("\n👥 Members:")
        for member in self.members.values():
            print(f"  {member}")

    def list_loans(self):
        if not self.loans:
            print("📋 No loans recorded.")
            return
        print("\n📋 Loans:")
        for loan in self.loans.values():
            if loan.is_active():
                print(f"  {loan}")