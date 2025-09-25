from typing import Callable

def any_example(number1: int = 22, number2: int = 4):
    return number1 * number2

def returns_function_result(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {"result": result}
    return wrapper

main_result = (returns_function_result(func=any_example))
result = main_result()
print(result)