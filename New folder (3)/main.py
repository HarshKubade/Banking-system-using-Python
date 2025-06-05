from Banking.account import SavingAccount, CurrentAccount
from Banking.transactions import deposit, withdraw
accounts = {}

def create_account():
    name = input("Enter your name ").strip()
    acc_type = input("Enter account type (saving/current): ").strip().lower()
    initial_deposit = float(input("Enter initial deposit amount: "))
    if acc_type == 'saving':
        acc = SavingAccount(name, initial_deposit)
    elif acc_type == 'current':
        acc = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Please choose 'saving' or 'current'.")
        return None
    accounts[acc.account_number] = acc
    print(f"Account created successfully. Account Number: {acc.account_number}")
def login():
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        user_account = accounts[acc_number]
        print(f"Welcome {user_account.name}!")
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            if isinstance(user_account, SavingAccount):
                print("4. Apply Interest")
            print("5. logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                deposit(user_account, amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_account, amount)
            elif choice == '3':
                print(f"Current Balance: ₹{user_account.get_balance()}")
            elif choice == '4' and isinstance(user_account, SavingAccount):
                user_account.calculate_interest()
            elif choice == '5':
                print("Logging out...")
                break
    else:
        print("Invalid choice. Please choose a valid option.")
def main():
    print("Welcome to SBI Bank!".center(50))
    print("Nagpur SIT Branch".center(50))
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using SBI Bank! Goodbye!")
            break
        else:
            print("Thank you for using SBI Bank! Goodbye!")
            break
    else:
        print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()
