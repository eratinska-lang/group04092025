from typing import Callable

def round_result(ndigits: int):
    def decorator(func: Callable) -> Callable:
        def decorator_inner(*args, **kwargs):
            print("round_result was called")
            result = func(*args, **kwargs)
            if type(result) == int or type(result) == float:
                return round(result, ndigits)
            return result
        return decorator_inner
    return decorator

@round_result(3)
def get_number_pi():
    return 3.14159265359

@round_result(-2)
def foo():
    return 1125

print(get_number_pi())
print(foo())

