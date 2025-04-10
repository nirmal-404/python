
def show_balance(balance):
    print("**********************")
    print(f"Your balance is {balance:.2f}")
    print("*********************")

def deposit():
    print("***************************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("***************************************")

    if amount < 0:
        print("***********************************************")
        print("Invalid amount. Please enter a positive number.")
        print("***********************************************")
    
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************************")
    amount = float(input("Enter an amount to be withdraw: "))
    print("*********************************")

    if amount > balance:
        print("****************************************************")
        print("Insufficient balance. Please enter a smaller amount.")
        print("****************************************************")
        return 0;
    elif amount < 0:
        print("***********************************************")
        print("Invalid amount. Please enter a positive number.")
        print("***********************************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running =True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        print("**********************************")
        choice = input("Enter your choice (1-4): ")
        print("**********************************")


        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+= deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*********************************************")
            print("Invalid choice. Please choose a valid option.")
            print("*********************************************")


    print("***************************")
    print("Thank you! Have a nice day.")                 
    print("***************************")


if __name__ == '__main__':
    main()