class BankAccount:
    def __init__(self, full_name, account_number, balance, account_type):
        self.name = full_name
        self.accountNum = account_number
        self.balance = balance
        self.type = account_type
    
    def deposit(self,amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${round(self.balance, 2)}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance - 10
            print(f"Overdraft fee: $10 New Balance: ${round(self.balance, 2)}")
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount} new balance: ${round(self.balance, 2)}')
    
    def get_balance(self):
        print(self.balance)
        return self.balance
    
    def add_interest(self):
        if self.type == "checkings":
            interest = self.balance * 0.00083
            self.balance += interest
            print(round(self.balance, 2))
        elif self.type == "savings":
            interest = self.balance *0.001
            self.balance += interest
            print(round(self.balance, 2))
        
    def print_statement(self):
        print(self.name)
        print(f"Account No: {self.accountNum}")
        print(f"Balance: ${round(self.balance, 2)}")


        
test = BankAccount("jenn", "0123", 30, "checkings")
# test.deposit(30)
# test.withdraw(5)
# test.withdraw(100)
# test.get_balance()
# test.add_interest()
# test.print_statement()

cassidyAccount = BankAccount("Cassidy Sneed", 142353, 50, "checkings")
# cassidyAccount.deposit(40)
# cassidyAccount.add_interest()
# cassidyAccount.print_statement()

lissaAccount = BankAccount("Lissa Laymon", 392084, 80, "savings")
# lissaAccount.withdraw(20)
# lissaAccount.deposit(200)
# lissaAccount.print_statement()

mitchellAccount = BankAccount("Mitchell", 3141592, 0, "savings")
# mitchellAccount.deposit(400000)
# mitchellAccount.print_statement()
# mitchellAccount.add_interest()
# mitchellAccount.print_statement()
# mitchellAccount.withdraw(150)
# mitchellAccount.print_statement()

print("---------------------")

bank = [test, cassidyAccount, lissaAccount, mitchellAccount]

def monthly_interest():
    for i in range(len(bank)):
        
        bank[i].add_interest()

def bank_app_start():
    # welcome message
    print("Welcome to the Bank!")
    user_input = input("Enter Account Name: >> ")

    #looping through accounts
    for i in range(len(bank)):
        if bank[i].name == user_input:
            print(bank[i].name)
            print(user_input)
            account = bank[i]

            print(f"What would you like to do today, {bank[i].name}?")
            user_action = input("Deposit, Withdraw, Statement >> ")
            
            if user_action.lower() == "deposit":
                amount = input("How much would you like to deposit? >> ")
                bank[i].deposit(int(amount))

            elif user_action.lower() == "withdraw":
                amount = input("How much would you like to withdraw? >> ")
                bank[i].withdraw(int(amount))
            
            elif user_action.lower() == "statement":
                bank[i].print_statement()

            else: 
                print("error")

            



monthly_interest()
bank_app_start()

