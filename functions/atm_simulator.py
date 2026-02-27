balance = 10000

#----Functions----
def check_balance():
    print(f"Current Balance: ${balance}")

def deposit(amount):
    global balance
    balace += amount
    print(f"${amount} deposited successfully.")

def withdraw(amount):
    global balance

    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"${amount} withdrawn successfully.")

#---------- MENU PROGRAM -----------
while True:
    print("\n==== ATM MENU ====")
    print("(1) Check Balance")
    print("(2) Deposit")
    print("(3) Withdraw")
    print("(4) Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        check_balance()

    elif choice =="2":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice =="3":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice =="4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")