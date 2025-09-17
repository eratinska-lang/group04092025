from service.logger import logger


def my_sentence():
    return "Hello, buddy!"

def max_number(list_with_numbers: list) -> float:
    list_with_only_numbers = []
    for number in list_with_numbers:
        if type(number) is int or type(number) is float:
            list_with_only_numbers.append(number)
    if not list_with_only_numbers:
        return 0
    logger.info(f"Max_number: {max(list_with_only_numbers)=}")
    return max(list_with_only_numbers)


def multiple(number_one: float,number_two: float) -> float:
    return number_one * number_two
