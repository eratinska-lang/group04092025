from revision.hw_functions_utils import my_sentence, multiple, max_number


def main():
    result = my_sentence()
    print(result)

    print("________________________________________________")

    result2 = max_number([1, 5, 7, 9, 3])
    print(result2)

    print("________________________________________________")

    result3 = multiple(7,8)
    print(result3)

if __name__ == "__main__":
    main()