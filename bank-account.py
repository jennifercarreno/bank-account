class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.accountNum = account_number
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance - 10
            print(f"Overdraft fee: $10 New Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')
    
    def get_balance(self):
        print(self.balance)
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        print(round(self.balance, 2))


        
test = BankAccount("jenn", "0123", 30)
test.deposit(30)
test.withdraw(5)
test.withdraw(100)
test.get_balance()
test.add_interest()