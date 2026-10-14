
bank_balance = 5000


def deposit(amount):
    global bank_balance

    if amount > 0:
        bank_balance += amount
        print("Deposit Successful")
    else:
        print("Invalid deposit amount")


def withdraw(amount):
    global bank_balance

    if amount <= 0:
        print("Invalid withdrawal amount")
    elif amount > bank_balance:
        print("Insufficient Balance")
    else:
        bank_balance -= amount
        print("Withdrawal Successful")


print("Initial Balance:", bank_balance)

deposit(1000)
print("Balance After Deposit:", bank_balance)

withdraw(2000)
print("Balance After Withdrawal:", bank_balance)
