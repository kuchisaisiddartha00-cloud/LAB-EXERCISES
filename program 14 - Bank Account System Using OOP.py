# Program 14: Bank Account System Using OOP

class BankAccount:
    def __init__(self, account_holder, opening_balance=0.0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.account_holder = account_holder
        self.balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount:.2f}.")

    def show_balance(self):
        print(f"{self.account_holder}'s balance: {self.balance:.2f}")

name = input("Account holder name: ")
opening = float(input("Opening balance: "))
account = BankAccount(name, opening)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        account.deposit(float(input("Amount to deposit: ")))
    elif choice == "2":
        account.withdraw(float(input("Amount to withdraw: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
