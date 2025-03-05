from Users import Users
from BankAccount import BankAccount


user = Users(1, "Alisher Hakimov", "99-999-99-99", "alisher.h@gmail.com", 50000000)
print(user)

try:
    invalid_user = Users(2, "Behruz Alisherov", "91-111-11-11", "behruz!a@gmail.com", 60000000)
except ValueError as e:
    print(e)

acc_nums = []
user_acc = user.create_acc(2000000, acc_nums)
print(user_acc)
acc_nums.append(user_acc.account_number)

try:
    invalid_user_acc = user.create_acc(-2, acc_nums)
except ValueError as e:
    print(e)

print(user_acc.balance)
user_acc.deposit(100000)
print(user_acc.balance)

user_acc.withdraw(500000)
print(user_acc.balance)

try:
    user_acc.withdraw(5000000)
except ValueError as e:
    print(e)

user_acc2 = user.create_acc(2000000, acc_nums)
print(user)

user_acc2.deposit(500000)
user_acc2.withdraw(1000000)
print(user)

user_acc.transfer(user_acc2, 1500000)

print(user_acc.get_transaction_history())
print(user_acc2.get_transaction_history())