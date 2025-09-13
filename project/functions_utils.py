from uuid import uuid4

def is_number_bigger_than_given(candidate_number: float, threshold: float = 10) -> bool:
    """according to the task #6556565"""
    return candidate_number > threshold

def add_salt_too_list(given_list: list) -> None:
    identifier = uuid4().hex
    print(identifier)
    given_list.append(identifier)