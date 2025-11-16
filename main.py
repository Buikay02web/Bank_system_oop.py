from bank_account import *

def main():
    account1 = Bankaccount("2226865667","maureen chinedu",200000)
    account2 = Bankaccount("51566113959", "Goodluck chibuike",30000000 )

    print("Welcome to our banking system!!")
    print("-------------------------------")

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. withdraw")
        print("3. check balance")
        print("4. Display Details")
        print("5. Transfer")
        print("6. Exit")

        choice = input("enter your choice: ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            if not account1.authenticate():
                print("Authentication failed. please try again later.")
                break

        if choice == "1":
            print("\nDeposite Menu:")
            print("--------------------")  
            amount = float(input("enter amount to deposit: "))
            account1.deposit(amount)
        elif choice == "2":
            print("\nWithdrawal Menu:")
            print("--------------------")  
            amount = float(input("enter amount to withdraw: "))
            account1.withdraw(amount)
        elif choice == "3":
            print("\nCheck Balance Menu:")
            print("--------------------")    
            account1.check_balance()
        elif choice == "4":
            print("\nAccount Details:")
            print("--------------------")  
            account1.display_details()
        elif choice == "5":
            print("\nTransfer Menu:")
            print("--------------------")
            amount = float(input("Enter amount to transfer: "))
            account1.transfer(amount, account2)
        elif choice == "6":
            print("\nThank you for using our bank system!")
            break          
        else:
            print("invalide choice. please try again.")    

if __name__ == "__main__":
    main()            