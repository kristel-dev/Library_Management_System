from book import Book
from member import Member
from library import Library
from exception import (
    BookNotFoundError, MemberNotFoundError, BookUnavailableError,
    LoanNotFoundError, InvalidInputError
)

def print_menu():
    print("\n" + "="*50)
    print("🏛️  LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add book")
    print("2. Register member")
    print("3. Borrow books")
    print("4. Return books")
    print("5. View books")
    print("6. View members")
    print("7. View loans and exit")
    print("="*50)

def get_valid_input(prompt: str, valid_options: list = None) -> str:
    while True:
        try:
            user_input = input(prompt).strip()
            if valid_options and user_input not in valid_options:
                raise InvalidInputError("Please choose 1-7 only!")
            return user_input
        except InvalidInputError as e:
            print(f"❌ {e}")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit()

def main():
    library = Library()
    
    library.add_book(Book("B001", "Python Programming", "John Doe"))
    library.add_book(Book("B002", "Data Structures", "Jane Smith"))
    library.add_member(Member("M001", "Alice Johnson", "alice@email.com"))
    
    while True:
        try:
            print_menu()
            choice = get_valid_input("Enter choice (1-7): ", ["1","2","3","4","5","6","7"])
            
            if choice == "1":  
                print("\n📚 ADD BOOK")
                book_id = input("Book ID: ").strip()
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                library.add_book(Book(book_id, title, author))
                
            elif choice == "2":  
                print("\n👤 REGISTER MEMBER")
                member_id = input("Member ID: ").strip()
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                library.add_member(Member(member_id, name, email))
                
            elif choice == "3":  
                print("\n📖 BORROW BOOK")
                loan_id = input("Loan ID: ").strip()
                book_id = input("Book ID: ").strip()
                member_id = input("Member ID: ").strip()
                library.create_loan(loan_id, book_id, member_id)
                
            elif choice == "4":  
                print("\n🔙 RETURN BOOK")
                loan_id = input("Loan ID: ").strip()
                library.return_loan(loan_id)
                
            elif choice == "5": 
                library.list_books()
                
            elif choice == "6":  
                library.list_members()
                
            elif choice == "7":  
                library.list_loans()
                print("\n👋 Thank you for using the system!")
                break
                
        except BookNotFoundError as e:
            print(f"❌ {e}")
        except MemberNotFoundError as e:
            print(f"❌ {e}")
        except BookUnavailableError as e:
            print(f"❌ {e}")
        except LoanNotFoundError as e:
            print(f"❌ {e}")
        except InvalidInputError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"💥 Error: {e}")
        input("\n Press Enter to Continue...")