from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
class BankAccount:
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType.name
        self.balance = 0
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def __str__(self):
        return "{} has a {} account with balance of {}".format(self.owner, self.accountType, self.balance)

    def __len__(self):
        return self.balance


class BankUser:
    def __init__(self, owner):
        self.owner = owner
        self.checking = 0
        self.savings = 0
        self.accountType = None
        self.accountDict = {AccountType.CHECKING: 0, AccountType.SAVINGS: 0}
    
    def addAccount(self, accountType):
        self.accountType = accountType
        self.accountDict[self.accountType] += 1
        if self.accountDict[self.accountType] > 1:
            raise ValueError("You already have an account.")
    
    def getBalance(self, accountType):
        if accountType == AccountType.CHECKING:
            return self.checking
        else:
            return self.savings
    
    def deposit(self, accountType, amount):
        if accountType == AccountType.CHECKING:
            self.checking += amount
        else:
            self.savings += amount
    
    def withdraw(self, accountType, amount):
        if accountType == AccountType.CHECKING:
            if amount > self.checking:
                raise ValueError("insufficient funds")
            self.checking -= amount
        else:
            if amount > self.savings:
                raise ValueError("insufficient funds")
            self.savings -= amount
    
    def __str__(self):
        S1 = ""
        S2 = ""
        if self.accountDict[AccountType.CHECKING] == 1:
            S1 = "{}: your checking account has ${}\n".format(self.owner, self.checking)
        if self.accountDict[AccountType.SAVINGS] == 1:
            S2 = "{}: your savings account has ${}".format(self.owner, self.savings)
        return S1 + S2
    

def ATMSession(bankUser):
    
    def interface():
        command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))

        while command1 != 1:

            if command1 == 2:
                command2 = int(input("Creat Account -- Enter Option:\n1)Checking\n2)Savings\n"))
                if command2 == 1:
                    bankUser.addAccount(AccountType.CHECKING)
                elif command2 == 2:
                    bankUser.addAccount(AccountType.SAVINGS)
                else:
                    print("Please enter a valid command")
                command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))

            elif command1 == 3:
                command2 = int(input("Check Balance -- Enter Option:\n1)Checking\n2)Savings\n"))
                if command2 == 1:
                    if bankUser.accountDict[AccountType.CHECKING] == 0:
                        print("You do not have a checking account yet. Choose another option.")
                    else:
                        print(bankUser)
                elif command2 == 2:
                    if bankUser.accountDict[AccountType.SAVINGS] == 0:
                        print("You do not have a savings account yet. Choose another option.")
                    else:
                        print(bankUser)
                else:
                    print("Please enter a valid command")
                command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))

            elif command1 == 4:
                command2 = int(input("Deposit -- Enter Option:\n1)Checking\n2)Savings\n"))
                if command2 == 1:
                    if bankUser.accountDict[AccountType.CHECKING] == 0:
                        print("You do not have a checking account yet. Choose another option.")
                    else:
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        bankUser.deposit(AccountType.CHECKING, amount)
                        print(bankUser)
                elif command2 == 2:
                    if bankUser.accountDict[AccountType.SAVINGS] == 0:
                        print("You do not have a savings account yet. Choose another option.")
                    else:
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        bankUser.deposit(AccountType.SAVINGS, amount)
                        print(bankUser)
                else:
                    print("Please enter a valid command")
                command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))

            elif command1 == 5:
                command2 = int(input("Withdraw -- Enter Option:\n1)Checking\n2)Savings\n"))
                if command2 == 1:
                    if bankUser.accountDict[AccountType.CHECKING] == 0:
                        print("You do not have a checking account yet. Choose another option.")
                    else:
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        bankUser.withdraw(AccountType.CHECKING, amount)
                        print(bankUser)
                elif command2 == 2:
                    if bankUser.accountDict[AccountType.SAVINGS] == 0:
                        print("You do not have a savings account yet. Choose another option.")
                    else:
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        bankUser.withdraw(AccountType.SAVINGS, amount)
                        print(bankUser)
                else:
                    print("Please enter a valid command")
                command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))
            else:
                print("Please enter a valid command")
                command1 = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))
        print("Goodbye!")
        
    return interface