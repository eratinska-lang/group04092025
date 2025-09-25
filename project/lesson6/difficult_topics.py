from typing import Callable


def foo(number: int = 6) -> int:
    print(33333333)
    return number + 5

def foo2(arg: str = "kkkk") -> str:
    print(66666666)
    return arg * 2


def foo3() -> str:
    print(100000000000000)
    return 'Hello buddy'


def foo4(arg_1: int, arg_2: int) -> int:
    print(99999999999)
    return arg_1 + arg_2

def call_callable_function_master(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print(23232323)
        print(args, kwargs)
        print(func)
        print("before call______________________________")
        result = func(*args, **kwargs)
        if isinstance(result, int):
            result *= 1000
        print("after call______________________________")
        return result

    return inner

foo= call_callable_function_master(func=foo)
result = foo(555)
print(result)

foo2 = call_callable_function_master(func=foo2)
result = foo2(arg='555++++++++++++++++')
print(result)


################################################################
@call_callable_function_master
def final_foo(number: int = 6) -> int:
    print("function final_foo was called")
    return number + 5

@call_callable_function_master
def final_foo333(number: int = 6) -> int:
    print("function final_foo333 was called")
    return number + 666666666666

result = final_foo(23)
print(result)

result = final_foo333(346)
print(result)