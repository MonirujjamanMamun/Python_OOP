class Account:
    account_number = 1000  # Initial account number

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = Account.account_number
        Account.account_number += 1
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"${amount} withdrawn successfully."
            else:
                return "Withdrawal amount exceeded."
        else:
            return "Invalid amount for withdrawal."

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def check_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            if amount > 0:
                self.loan_taken += 1
                self.balance += amount
                self.transaction_history.append(f"Took a loan of ${amount}")
                return f"Loan of ${amount} taken successfully."
            else:
                return "Invalid loan amount."
        else:
            return "You can't take more than 2 loans."

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f"Transferred ${amount} to {recipient.name}")
            recipient.transaction_history.append(
                f"Received ${amount} from {self.name}")
            return f"${amount} transferred to {recipient.name}."
        else:
            return "Insufficient balance for the transfer."


class Bank:
    def __init__(self):
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = False
        self.accounts = []

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        return f"Account created successfully. Account number: {account.account_number}"

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def show_users(self):
        for account in self.accounts:
            print(f"\tAccount Number: {account.account_number}")
            print(f"\tName: {account.name}")
            print(f"\tEmail: {account.email}")
            print(f"\tAddress: {account.address}")
            print(f"\tAccount Type: {account.account_type}")
            print(f"\tBalance: ${account.balance}")
            print(f"\tLoan Taken: ${account.loan_taken}")
            print("")

    def total_balance(self):
        # total_balance = sum(account.balance for account in self.accounts)
        total_balance = 0
        for account in self.accounts:
            total_balance = total_balance + account.balance
        self.total_balance = total_balance
        return f"Total Balance in the Bank: ${total_balance}"

    def total_loan(self):
        total_loan = sum(account.loan_taken for account in self.accounts)
        return f"Total Loan Amount: ${total_loan}"

    def off_loan(self):
        self.loan_status = False
        return "Loan feature turned off."

    def on_loan(self):
        self.loan_status = True
        return "Loan feature turned on."


# Example usage:

# bank = Bank()
# print(bank.create_account("John Doe", "john@example.com", "123 Main St", "Savings"))
# print(bank.create_account("Jane Smith", "jane@example.com", "456 Elm St", "Current"))

# user1 = bank.accounts[0]
# user2 = bank.accounts[1]

# print(user1.deposit(1000))
# print(user2.deposit(1500))

# print(user1.transfer(user2, 500))
# print(user2.withdraw(200))

# bank.show_users()
# print(bank.total_balance())
# print(bank.total_loan())


bank = Bank()
admin = Admin(bank)
while True:
    print("Select an option:")
    print("1. User Options")
    print("2. Admin Options")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nUser Options:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings or Current): ")
            print(bank.create_account(name, email, address, account_type))
        elif user_choice == "2":
            user_id = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to deposit: "))
            print(bank.deposit(user_id, amount))
        elif user_choice == "3":
            user_id = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to withdraw: "))
            print(bank.withdraw(user_id, amount))
        elif user_choice == "4":
            user_id = int(input("Enter your account number: "))
            print(bank.check_balance(user_id))
        elif user_choice == "5":
            user_id = int(input("Enter your account number: "))
            print(bank.transaction_history(user_id))
        elif user_choice == "6":
            user_id = int(input("Enter your account number: "))
            amount = float(input("Enter the loan amount: "))
            print(bank.take_loan(user_id, amount))
        elif user_choice == "7":
            sender_id = int(input("Enter your account number: "))
            receiver_id = int(input("Enter the receiver's account number: "))
            amount = float(input("Enter the amount to transfer: "))
            print(bank.transfer(sender_id, receiver_id, amount))
        elif user_choice == "8":
            break
    elif choice == "2":
        print("\nAdmin Options:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        admin_choice = input("Enter your choice: ")

        if admin_choice == "1":
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings or Current): ")
            print(admin.create_account(name, email, address, account_type))
        elif admin_choice == "2":
            user_id = int(input("Enter the account number to delete: "))
            print(admin.delete_account(user_id))
        elif admin_choice == "3":
            print(admin.view_all_accounts())
        elif admin_choice == "4":
            print(admin.check_total_balance())
        elif admin_choice == "5":
            print(admin.check_total_loan_amount())
        elif admin_choice == "6":
            print(admin.toggle_loan_feature())
        elif admin_choice == "7":
            break
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select again.")
