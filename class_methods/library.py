class LibraryAccount:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.count = 0

    def borrow_book(self, book_name):
        if book_name in self.books:
            print("It seems like you already have ", book_name)
        elif self.count >= 3:
            print("Limit reached!")
        else:
            self.books.append(book_name)
            self.count += 1
            print("Borrowed: ", book_name)

    def return_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.count -= 1
            print("Returned: ", book_name)
        else:
            print("Book not found: ", book_name)
    
    def list_books(self):
        if self.count == 0:
            print("No books borrowed...")
        else:
            print("Your books:")
            for i in self.books:
                print(i)

name = input("Enter name: ")
account = LibraryAccount(name)
opt = 0

while opt != 4:
    print("\n1. Borrow book")
    print("2. Return book")
    print("3. List books")
    print("4. Exit")

    opt = int(input("Enter option (1-4): "))
    if opt < 3:
        book_name = input("Enter book name: ")

        if opt == 1:
            account.borrow_book(book_name)
        else:
            account.return_book(book_name)
    elif opt == 3:
        account.list_books()
    elif opt == 4:
        print("Exited...")
        break