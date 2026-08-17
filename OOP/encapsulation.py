class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance       # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 10000)

print("Owner:", account.owner)
print("Balance:", account.get_balance())

account.deposit(5000)
print("Balance:", account.get_balance())

account.withdraw(3000)
print("Balance:", account.get_balance())
