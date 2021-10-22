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
        print(f"Account Type: {self.type}")

# CREATING ACCOUNTS  
jenniferAccount = BankAccount("Jennifer Carreno", "0123", 5000, "checkings")
cassidyAccount = BankAccount("Cassidy Sneed", 142353, 50, "checkings")
lissaAccount = BankAccount("Lissa Laymon", 392084, 80, "savings")
mitchellAccount = BankAccount("Mitchell", 3141592, 0, "savings")


bank = [jenniferAccount, cassidyAccount, lissaAccount, mitchellAccount]

# -------------------------------FUNCTIONS------------------------------------------------

# MONTHLY INTERESTS
def monthly_interest():
    for i in range(len(bank)):
        
        bank[i].add_interest()

# BANK APP FUNTCION
def bank_app_start():

    #looping through accounts
    for i in range(len(bank)):

        # FIND MATCHING ACCONT
        if bank[i].name == user_input:
            account = bank[i]
            print(f"What would you like to do today, {account.name}?")
            user_action = input("Deposit, Withdraw, Statement >> ")
            
            # DEPOSIT
            if user_action.lower() == "deposit":
                amount = input("How much would you like to deposit? >> ")
                account.deposit(int(amount))
                user_cont = input("Anything else today? (yes/no) >> ")
                bank_app_end(user_cont)

            # WITHDRAW
            elif user_action.lower() == "withdraw":
                amount = input("How much would you like to withdraw? >> ")
                account.withdraw(int(amount))
                user_cont = input("Anything else today? (yes/no) >> ")
                bank_app_end(user_cont)
            
            # STATEMENT
            elif user_action.lower() == "statement":
                account.print_statement()
                user_cont = input("Anything else today? (yes/no) >> ")
                bank_app_end(user_cont)
            
            # ERROR MESSAGE
            else: 
                print("Try Again")
                user_cont = "error"
                bank_app_end(user_cont)

# APP END
def bank_app_end(user_cont):

    # KEEPS GOING IF USER WANTS TO DO MORE
    if user_cont.lower() == "yes":
        bank_app_start()
    elif user_cont.lower()=="no":
        print("Have a nice day")
        return
    else:
        bank_app_start()   

# ---------------------------------------------------------------------------------------
monthly_interest()

# WELCOME MESSAGE
print("Welcome to the Bank!")
user_input = input("Enter Account Name: >> ")
bank_app_start()

