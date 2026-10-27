class BankAccount:
    def _init_(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        self.accounts[account_number] = {'name': name, 'balance': 0}
        print("Account created successfully.")

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Account does not exist.")

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        if account_number in self.accounts and self.accounts[account_number]['balance'] >= amount:
            self.accounts[account_number]['balance'] -= amount
            print(f"Withdrew {amount} successfully.")
        else:
            print("Insufficient balance or account does not exist.")

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            balance = self.accounts[account_number]['balance']
            print(f"Account balance: {balance}")
        else:
            print("Account does not exist.")

    def run(self):
        while True:
            print("\nBank Management System")
            print("1. Create a New Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please choose again.")

bank_system = BankAccount()
bank_system.run()
