import asyncio
import time
from time import sleep


# def generator():
#     n = 1
#     while True:
#         yield n
#         n += 1
#
# gen = generator()
# print(gen)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(555555555555555555555555555555555)
# print(next(gen))

#11111111111111111111111111111111111111111111111
# async def hello():
#     print('Hello World!')
#     await asyncio.sleep(2)
#     print("Hello again!")
#
# asyncio.run(hello())

#22222222222222222222222222222222222222222222222
async def hello():
    print('Hello World!')
    await asyncio.sleep(2)
    print("Hello again!")

async def foo(n):
    print(f'Foooooooooooooooo {n}')
    await asyncio.sleep(2)
    print(f"Fooooooooooooo again {n}!")



async def main():
    await asyncio.gather(
    foo(5), hello(), hello(), hello(), foo(2),
    foo(5), hello(), hello(), hello(), foo(2),
    foo(5), hello(), hello(), hello(), foo(2),
    foo(5), hello(), hello(), hello(), foo(2))

start = time.monotonic()
print(start)

asyncio.run(main())

end = time.monotonic()
print(end)
print(__file__, end - start)