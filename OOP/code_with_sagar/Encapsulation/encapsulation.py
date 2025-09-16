# Encapsulation- mean internal details hide krna kisi ki object ki and direct access krne se rokna 
# eg

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance   #private variable (directly access nhi kr sakte)

    def deposite (self,amount):
        self.__balance += amount
        print(f"Deposited {amount} , new balance{self.__balance} ")


    def get_balance (self):
        return self.__balance  #conrolled access 
    
account = BankAccount('123456789',5000)

account.deposite(2000)
print (account.get_balance())

print(account.__balance)

