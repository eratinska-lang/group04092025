import pytest
from homework15.oop_practice import Library, Book


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