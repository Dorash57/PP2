class Bank_Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Not enough money.")


account = Bank_Account("Person", 100)

account.deposit(100)
account.withdraw(50)
account.withdraw(200)
