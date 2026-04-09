class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.__transactions = []

        if initial_balance > 0:
            self.__transactions.append(f"Account opened with:{initial_balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0")
            return

        self.__balance += amount
        self.__transactions.append(f"Deposited :{amount}")
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0")
            return

        if amount > self.__balance:
            print("Insufficient Balance! Please try again letter.")
            return

        self.__balance -= amount
        self.__transactions.append(f"Withdrawn : {amount}")
        print(f"{amount} withdrawn successfully")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

    def transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.__transactions:
            print(transaction)



name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))


account1 = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)

    elif choice == "3":
        account1.check_balance()

    elif choice == "4":
        account1.transaction_history()

    elif choice == "5":
        print("Thank you for using  my Bank Account System")
        break

    else:
        print("Invalid choice!  Please Try again.")