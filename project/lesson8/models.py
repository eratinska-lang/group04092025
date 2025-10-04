import uuid
from typing import Self



class FinancialCaculation:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    @property
    def total_money(self):
        money = 0
        for account in self.accounts:
            money += account.balance
        return money


    def get_first_account(self) -> "BankAccount":
        if self.accounts:
            return self.accounts[-1]


class Person(FinancialCaculation):
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name not provided")
        super().__init__()
        self.name = name.title()
        self.ipn = uuid.uuid4()
        self.accounts: list[BankAccount] = []
    def __str__(self):
        return f"<Person name={self.name} ipn={self.ipn}, and I have got {len(self.accounts)} accounts={self.accounts} >"

#person = Person(name="Alex")
#print(person)

#print(int("0x00000283B6A31550"))


class BankAccount:
    def __init__(self, client: Person):
        self.client = client
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def transfer(self, amount: float, other: Self):
        self.balance -= amount
        self.balance += amount


    def __str__(self):
        return f"<Account belong to {self.client.name} with balance={self.balance} >"


class Bank(FinancialCaculation):
    def __init__(self, name: str):
        super().__init__()
        self.__name: str = f"PAT {name.upper()}"
        self.account: list[BankAccount] = []

    def open_account(self, client: Person) -> BankAccount:
        new_account = BankAccount(client)
        self.account.append(new_account)
        #client.accounts.append(new_account)
        return new_account

    @property
    def name(self):
        return self.__name


    def __str__(self):
        return f"<Come to us. We are {self.name}, and we have opened {len(self.account)} account already>"

# person_alex = Person(name="Alex")
# person_marta = Person(name="Marta")
# person_bob = Person(name="Bob")
#
# print(person_alex)
# #print(int("0x00000283B6A31550"))
#
# monobank = Bank("Mono")
# monobank.open_account(person_alex)
#
# accounts = monobank.open_account(person_alex)
# accounts.deposit(5000)
# accounts.deposit(2000)
# person_alex.accounts.append(accounts)
# print(person_alex)
#
#
#
#
# print(monobank.total_money)
#
# alex_card = person_alex.get_first_account()
# alex_card.withdraw(500)
#
# #monobank.name = "fghbjklm"
# #monobank.total_money = 5555 error
# new_bank = Bank("New Bank")
# new_bank.open_account(person_alex).deposit(6000)
# new_bank.open_account(person_bob).deposit(14000)
#
#
#
# person_bob.get_first_account().transfer(4000, person_alex.get_first_account())



