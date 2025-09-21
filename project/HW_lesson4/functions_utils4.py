def greet_person(my_name: str = "Гість") -> str:
    return f"Hello {my_name}!"

def is_even(random_number: int) -> bool:
    if random_number % 2 == 0:
        return True
    else:
        return False

def reverse_string(text: str) -> str:
    return text[::-1]

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

def add_person_to_list(people: list[str], person: str) -> list[str]:
    if not person.strip():
        print(person.strip())
        return []
    people.append(person)
    return people


def count_vowels(text: str) -> int:
    all_vowels = "аАоОеЕіІїЇиИяЯюЮуУaAoOuUyYiIeE"
    count=0
    for char in text:
        if char in all_vowels:
            count += 1
    return count

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9