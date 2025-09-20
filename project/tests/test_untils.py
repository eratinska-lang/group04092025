from functions_utils import is_number_bigger_than_given, get_string_length_no_whitespaces, get_auto_distance


def test_is_number_bigger_than_given1():
    given_number = 5
    result = is_number_bigger_than_given(given_number)
    expected_result = False
    assert result == expected_result

def test_get_string_length_no_whitespaces_empty_string():
    given_number = ""
    expected_result = 0
    actual_result = get_string_length_no_whitespaces(given_number)
    assert actual_result == expected_result, "Ups"

def test_get_string_length_no_whitespaces_not_empty_string():
    given_number = "123456"
    expected_result = 6
    actual_result = get_string_length_no_whitespaces(given_number)
    assert actual_result == expected_result, "Ups"

def test_get_string_length_no_whitespaces_not_empty_string_and_spaces():
    given_number = "123 456   "
    expected_result = 10
    actual_result = get_string_length_no_whitespaces(given_number)
    assert actual_result == expected_result, "Ups"

def test_get_auto_distance():
    _speed = 80
    _time = 6
    actual_result = get_auto_distance(speed=_speed, time=_time)
    expected_result = 480
    assert actual_result == expected_result, "Ups"
