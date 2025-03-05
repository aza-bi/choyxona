import random

class BankAccount:
    def __init__(self, user_id: int, balance: float, acc_numbers: list):
        self.user_id = user_id
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance
        self.account_number = self.generate_acc_number(acc_numbers)
        self.transaction_history = []

    def __str__(self):
        return f"{self.balance}, {self.account_number}"

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")

    def transfer(self, target_account, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transaction_history.append(f"Transferred {amount} to {target_account.account_number}")
        target_account.transaction_history.append(f"Received {amount} from {self.account_number}")

    @staticmethod
    def generate_acc_number(acc_nums):
        while True:
            group1 = "9860" if random.randint(1, 2) == 1 else "8600"
            group2 = str(random.randint(1000, 9999))
            group3 = str(random.randint(1000, 9999))
            group4 = str(random.randint(1000, 9999))
            acc_num = f"{group1}-{group2}-{group3}-{group4}"
            if acc_num not in acc_nums:
                return acc_num

    def get_transaction_history(self):
        return self.transaction_history
