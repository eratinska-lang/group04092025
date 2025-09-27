import datetime as dt
from typing import Callable
from functools import wraps



def make_result_as_string(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        print("make_result_as_string before")
        result = func(*args, **kwargs)
        print(type(result))
        result = str(result)
        print("make_result_as_string after")
        print(type(result))
        return result
    return inner


def make_result_as_zero_counter(func: Callable) -> Callable:
    @wraps(func)
    def inner2(*args, **kwargs):
        print(func, 55555555555555555)
        print("make_result_as_zero_counter before")
        result = func(*args, **kwargs)
        print("make_result_as_zero_counter after")
        result_str = str(result)
        zero_in_result = result_str.count('0')
        print(f"{zero_in_result}")
        return result
    return inner2


def log_decorator(file_name: str = "general.log"):
    def log_decorator_inner(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            print("log_decorator before")
            result = func(*args, **kwargs)
            print("log_decorator after")


            now = dt.datetime.now()
            with open(file_name, "a", mode="a", encoding="utf-8") as file:
                file.write(f'{now}:{func.__name__},{args=},{kwargs=},{result=}\n'"")





            return result
        return inner
    return log_decorator_inner




@log_decorator()
@make_result_as_zero_counter
@make_result_as_string
def get_number_powered(number: int) -> int:
    print("get_number_powered was called")
    return number ** 2




@log_decorator()
@make_result_as_string
def multiply_numbers(number1: float, number2: float) -> float:
    print("multiply_numbers was called")
    return float(number1 * number2)

@log_decorator(file_name="sum_numbers.log")
def sum_numbers(list_of_numbers: list[float]) -> float:
    print("sum_numbers was called")
    return sum(list_of_numbers)


print(get_number_powered(10))
print(multiply_numbers(1, 2))
print(sum_numbers([1, 2]))