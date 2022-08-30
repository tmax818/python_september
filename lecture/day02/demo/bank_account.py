from tabnanny import check


class BankAccount:

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        pass

    def display_account_info(self):
        pass

    def yield_interest(self):
        pass

checking = BankAccount()
savings = BankAccount(.1, 200000)

checking.deposit(1000)

print(checking.balance)