# Using encapsulation, we can protect sensitive data like book availability.

"""
Definition: Encapsulation is the concept of restricting direct access to certain data and methods of a class. It protects the integrity of the object by keeping its state private.

Real-Life Example:

A Bank Account where balance is private, and it can only be accessed using methods like deposit() or withdraw().

"""


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self.__balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self.__balance}")
        else:
            print("Insufficient Balance or Invalid Amount")

    def get_balance(self):
        return self.__balance

# Creating Object
account = BankAccount("Rohit", 5000)
account.deposit(2000)
account.withdraw(3000)
print("Final Balance:", account.get_balance())


"""
✅ Explanation
__balance is a private attribute (using __).

deposit() and withdraw() methods control how the balance is accessed and modified.

Direct access to the balance is restricted.
"""