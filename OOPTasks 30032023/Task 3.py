# 3. Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. It should also have methods called deposit() and withdraw() that update the balance accordingly.

class BankAccount:
     def __init__(self, account_number, balance, owner_name):
         self.account_number = account_number
         self.balance = balance
         self.owner_name = owner_name

     def deposit(self):
         income = input("Please enter the amount of the deposit: ")
         new_balance = self.balance + int(income)
         return new_balance

     def withdraw(self):
         withdrawal = input("Enter the amount of the withdrawal: ")
         new_balance = self.balance - int(withdrawal)
         return new_balance

BankAccount1=BankAccount("1234567", 250, "Peter Smith")
BankAccount2=BankAccount("7654321", 500, "Anna Brown")

print(f'Current balance in your Bank account is: {BankAccount1.deposit()}')
print(f'Current balance in your Bank account is: {BankAccount2.withdraw()}')
