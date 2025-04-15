# Encapsulation
# private
# protected
# public


class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner # public variable
        self.__balance=balance # private variable

    def getBalance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Deposit is possible with positive denomination.")

    def withdraw(self, amount):
        if 0< amount <=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficent funds.")


account = BankAccount("Kishore",5500)
print("My Balance = ",account.getBalance())
account.deposit(5000)
print("Amount deposited ....")
print("My Balance = ",account.getBalance())
account.withdraw(3000)
print("Amount withdrawn ....")
print("My Balance = ",account.getBalance())

# Encapsulation in Python is one of the core concepts of Object-Oriented Programming (OOP).
# It refers to bundling data (attributes) and methods (functions) that operate on the data into a single unit (a class),
# and restricting access to some of the object’s internal parts.

# What Encapsulation Achieves:
# 1. Data hiding – prevent direct access to variables.
# 2. Access control – use methods to get or update data safely.
# 3. Maintainability – makes code cleaner and easier to manage.
# 4. Security – protect internal object state from unintended changes.