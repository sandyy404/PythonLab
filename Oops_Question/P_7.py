# Banking Transaction using Multilevel Inheritance.
class Bank:
    def bank(self):
        print("Welcome to SBI")
class Account(Bank):
    def account_info(self):
        print("Savings Account")
class Transaction(Account):
    def deposit(self, amount):
        print(f"₹{amount} deposited successfully")
t = Transaction()
t.bank()
t.account_info()
t.deposit(5000)