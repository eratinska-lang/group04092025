class TestIntegration:
    def test_create_account(self, person1, bank1):
        account = bank1.open_account(person1)
        assert account.balance == 0

    def test_account_saved(self, person1, bank1):
        assert person1.account
        assert bank1.account

    def test_deposit_account(self, person1, bank1):
        person1.get_first_account().deposit(1000)
        assert person1.total_money == 1000
        assert bank1.total_money == 1000

    def test_more_clients(self, person1, person2, bank1):
        account = bank1.open_account(person2)
        account.deposit(1000)
        assert person1.total_money == 2000
        assert bank1.total_money == 33333333333333