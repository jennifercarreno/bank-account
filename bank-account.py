class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.accountNum = account_number
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')
        
test = BankAccount("jenn", "0123", 30)
test.deposit(30)