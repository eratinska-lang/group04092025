from HW_lesson4.functions_utils4 import greet_person, is_even, reverse_string, calculate_average, add_person_to_list, \
    count_vowels, fahrenheit_to_celsius


def main_utils():
    result = greet_person("Tom")
    print(result)

    print("________________________________________________")

    result2 = is_even(6)
    print(result2)

    print("________________________________________________")

    result3 = reverse_string("Hello my friend!")
    print(result3)

    print("________________________________________________")

    result4 = calculate_average([3, 7, 8, 2, 6, 10, 1])
    print(result4)

    print("________________________________________________")

    result5 = add_person_to_list(["Zoy"], "Mark")
    print(result5)

    print("________________________________________________")

    result6 = count_vowels("Їжак, dog, cat і папугай")
    print(result6)

    print("________________________________________________")

    result7 = fahrenheit_to_celsius(54)
    print(result7)

if __name__ == "__main__":
    main_utils()