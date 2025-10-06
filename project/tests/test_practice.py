import pytest
from homework15.oop_practice import Book, Library

class TestBook:
    @pytest.mark.parametrize("title, author, isbn", [("title", "author", 1),("title", "author", 2),("title", "author", 3)])
    def test_book_arguments(self, title, author, isbn):
        book = Book(author, title, isbn)
        assert book.title == title
        assert book.author == author
        assert book.ISBN == isbn

@pytest.fixture
def library():
    return Library("КСД: Клуб Сімейного Дозвілля")

@pytest.fixture
def books():
    return [
        Book("Автор 1", "Книга 1", 1),
        Book("Автор 2", "Книга 2", 2),
        Book("Автор 3", "Книга 3", 3)
    ]

class TestLibrary:
    def test_add_book(self, library, books):
        library.add_new_book(books[0])
        assert len(library.books) == 1
        assert library.books[0] == books[0]

    def test_remove_existing_book(self, library, books):
        library.add_new_book(books[1])
        #print(library.books[1], 9999999999999999999)
        library.remove_book_by_id(library.books[0].ISBN)
        assert len(library.books) == 0

    def test_remove_non_existing_book(self, library, books):
        library.add_new_book(books[2])
        library.remove_book_by_id(500000000000)
        assert len(library.books) == 1

