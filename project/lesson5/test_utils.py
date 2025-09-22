from lesson5.homework9 import get_ticket_price


def test_get_ticket_price():
    assert get_ticket_price(3) == 0.0
    assert get_ticket_price(12) == 75.0
    assert get_ticket_price(43) == 150.0
    assert get_ticket_price(60) == 105.0
    print("All tests passed")