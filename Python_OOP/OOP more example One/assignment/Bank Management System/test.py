class Bank:
    def __init__(self):
        self.users = {}
        self.account_number = 1
        self.is_bankrupt = False
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type):
        if account_type not in ["Savings", "Current"]:
            return "Invalid account type. Choose either Savings or Current."

        user_id = self.account_number
        self.account_number += 1
        user = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transaction_history': [],
            'loans_taken': 0
        }
        self.users[user_id] = user
        return f"Account created successfully. Your account number is {user_id}"

    def deposit(self, user_id, amount):
        if user_id not in self.users:
            return "Account does not exist."
        if amount <= 0:
            return "Invalid deposit amount."

        self.users[user_id]['balance'] += amount
        self.users[user_id]['transaction_history'].append(
            f"Deposited {amount}")
        self.total_balance += amount
        return f"Deposit of {amount} was successful."

    def withdraw(self, user_id, amount):
        if user_id not in self.users:
            return "Account does not exist."
        if amount <= 0:
            return "Invalid withdrawal amount."
        if self.users[user_id]['balance'] < amount:
            return "Withdrawal amount exceeded."

        self.users[user_id]['balance'] -= amount
        self.users[user_id]['transaction_history'].append(f"Withdrew {amount}")
        self.total_balance -= amount
        return f"Withdrawal of {amount} was successful."

    def check_balance(self, user_id):
        if user_id not in self.users:
            return "Account does not exist."
        return f"Available balance: {self.users[user_id]['balance']}"

    def transaction_history(self, user_id):
        if user_id not in self.users:
            return "Account does not exist."
        return self.users[user_id]['transaction_history']

    def take_loan(self, user_id, amount):
        if user_id not in self.users:
            return "Account does not exist."
        if self.users[user_id]['loans_taken'] >= 2:
            return "You have already taken the maximum number of loans."
        if not self.loan_feature_enabled:
            return "Loan feature is currently disabled."

        self.users[user_id]['balance'] += amount
        self.users[user_id]['transaction_history'].append(
            f"Loan taken: {amount}")
        self.users[user_id]['loans_taken'] += 1
        self.total_loan_amount += amount
        return f"Loan of {amount} was granted."

    def transfer(self, sender_id, receiver_id, amount):
        if sender_id not in self.users or receiver_id not in self.users:
            return "Account does not exist."
        if amount <= 0:
            return "Invalid transfer amount."
        if self.users[sender_id]['balance'] < amount:
            return "Insufficient balance for the transfer."

        self.users[sender_id]['balance'] -= amount
        self.users[receiver_id]['balance'] += amount
        self.users[sender_id]['transaction_history'].append(
            f"Transferred {amount} to account {receiver_id}")
        self.users[receiver_id]['transaction_history'].append(
            f"Received {amount} from account {sender_id}")
        return f"Transfer of {amount} was successful."


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, user_id):
        if user_id in self.bank.users:
            del self.bank.users[user_id]
            return f"Account {user_id} deleted."
        return "Account does not exist."

    def view_all_accounts(self):
        return self.bank.users

    def check_total_balance(self):
        return f"Total bank balance: {self.bank.total_balance}"

    def check_total_loan_amount(self):
        return f"Total loan amount: {self.bank.total_loan_amount}"

    def toggle_loan_feature(self):
        self.bank.loan_feature_enabled = not self.bank.loan_feature_enabled
        return "Loan feature is now " + ("enabled" if self.bank.loan_feature_enabled else "disabled")


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
