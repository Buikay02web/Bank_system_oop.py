class Bankaccount:
    def __init__(self, account_number, account_name, balance = 0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.pin = "2008"

    def authenticate(self):
        attemts = 0
        while attemts < 3:
            pin = input("enter your pin: ")
            if pin == self.pin:
                return True
            else:
                attemts += 1
                print(f"incorrct pine. you have{3 - attemts} attempts left.")
        print("Account locked due to multiple incorrect pin attempts.")
        return False        
    
    def check_balance(self):
        print(f"Your current balance is #{self.balance:.2f}")

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit successful your new balance is #{self.balance:.2f}")
        else:
            print("invalide deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdraw successful !! your new balance is #{self.balance:.2f}")
        elif amount <= 0:
            print("invalide withdrawal amount!!")
        else:
            print("insufficient funds!!")

    def display_details(self):
        print(f"account_number: {self.account_number}")
        print(f"account_name: {self.account_name}")
        print(f"Balance : {self.balance}")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            recipient_account.deposit (amount)
            print(f"transfer successful !! you transfered #{amount:.2f} to {recipient_account.account_name}")
        else:
            print("transfer failed!!")
                
