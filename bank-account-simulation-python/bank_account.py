class BankAccount:
    """
    A simple Bank Account simulation system.
    Supports deposit, withdrawal, and balance checking.
    """

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


def main():
    print("===== BANK ACCOUNT SIMULATION =====")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid option! Please choose between 1-4.")


if __name__ == "__main__":
    main()
