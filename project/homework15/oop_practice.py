
class Book:
    def __init__(self, author: str, title: str, ISBN: int):
        self.author = author
        self.title = title
        self.ISBN = ISBN

    def __str__(self):
        return f"<The title of the book: {self.title}>; author: {self.author}; ISBN: {self.ISBN}> >"


class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_new_book(self, book: Book):
        self.books.append(book)
        print("Added new book")
        return book

    def remove_book_by_id(self, book_id: int):
        for book in self.books:
            if book.ISBN == book_id:
                print("Removed book")
                self.books.remove(book)

    def library_list(self):
        print(f"Фонд бібліотеки «{self.name}»:")
        for book in self.books:
            print(f" - {book}")



book1 = Book("Наталя Щєрба", "Чароділ: Чародільський браслет", 101)
book2 = Book("Ренсом Ріґґз", "Дім дивних дітей", 102)

library = Library("КСД: Клуб Сімейного Дозвілля")
library.add_new_book(book1)
library.add_new_book(book2)

library.library_list()
print("_______________________________________________________________________________")
library.remove_book_by_id(102)
library.library_list()