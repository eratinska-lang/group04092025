from lesson8.models import Bank


class TestBank:
    def test_bank1(self, bank1):
        assert bank1.name
        assert not bank1.accounts
        assert bank1.name.startswith("PAT")
