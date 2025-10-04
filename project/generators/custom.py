def get_sequence(start: int = 0):

    while True:
        yield start
        print("bla bla bla")
        start + 1

sequence = get_sequence()
print(sequence)

print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print("do something")
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))