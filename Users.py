import re
from BankAccount import BankAccount


class Users:
    def __init__(self, id: int, name: str, phone_number: str, email: str, yearly_income: float):
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email: {email}")

        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.yearly_income = yearly_income
        self.bank_accs = []

    def __str__(self):
        accs = [i.__str__() for i in self.bank_accs]
        return f"User: {self.id}, {self.name}, {self.phone_number}, {self.email}, {self.yearly_income}, Bank Accounts: {accs}"

    @staticmethod
    def is_valid_email(email: str) -> bool:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email) is not None

    def create_acc(self, amount:int, acc_nums):
        acc = BankAccount(self.id, amount, acc_nums)
        self.bank_accs.append(acc)
        return acc


