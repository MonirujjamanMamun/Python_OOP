from abc import ABC, abstractmethod


class Account(ABC):
    accounts = []
    account_numbers = 1

    def __init__(self, name, email, address, password, accountType):
        self.name = name
        self.accountNo = Account.account_numbers
        Account.account_numbers += 1
        self.email = email
        self.address = address
        self.passW = password
        self.balance = 0
        self.type = accountType
        Account.accounts.append(self)

    def changeInfo(self, name, password):
        self.name = name
        self.passW = password
        print(
            f"\n Name and Password are changed for account {self.accountNo}")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n Deposited {amount}. New balance: {self.balance}")
        else:
            print("\nSomething is worng. Deposit right Amount.")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew {amount}. New balance: {self.balance}")
        else:
            print("\nWithdrawal amount exceeded")

    def show_curr_balance(self):
        print(f"Current Balance: {self.balance}")

    @abstractmethod
    def showInfo(self):
        pass


class SavingsAccount(Account):
    def __init__(self, name, email, address, password, interestRate):
        super().__init__(name, email, address, password, "Savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self.balance * (self.interestRate / 100)
        self.deposit(interest)

    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type: {self.type}')
        print(f'\tName: {self.name}')
        print(f'\tName: {self.email}')
        print(f'\tName: {self.address}')
        print(f'\tAccount No: {self.accountNo}')
        print(f'\tCurrent Balance: {self.balance}\n')


class CuurentAccount(Account):
    def __init__(self, name, email, address, password, overdraftLimit):
        super().__init__(name, email, address, password, "Cuurent")
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraftLimit:
            self.balance -= amount
            print(f"\n Withdrew {amount}. New balance: {self.balance}")
        else:
            print("\n Withdrawal amount exceeded")

    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type: {self.type}')
        print(f'\tName: {self.name}')
        print(f'\tName: {self.email}')
        print(f'\tName: {self.address}')
        print(f'\tAccount No: {self.accountNo}')
        print(f'\tCurrent Balance: {self.balance}\n')


class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True

    def create_account(self, name, email, address, password, accountType, interestRate=None, overdraftLimit=None):
        if accountType == "Savings":
            account = SavingsAccount(
                name, email, address, password, interestRate)
        elif accountType == "Cuurent":
            account = CuurentAccount(
                name, email, address, password, overdraftLimit)
        self.accounts.append(account)
        print(f'Welcome {name}. Now, You can Login.')

    def delete_account(self, accountNumber):
        for account in self.accounts:
            if account.accountNo == accountNumber:
                self.accounts.remove(account)
                print(f"Account {accountNumber} deleted.")

    def show_accountNumber(self):
        for account in self.accounts:
            print(
                f"MR/Miss {account.name}. Please, Remember your account number. For login you need it. Your Account No: {account.accountNo}")

    def show_users(self):
        print("")
        print("List of User Accounts:")
        for account in self.accounts:
            print(f"Account No: {account.accountNo}, Name: {account.name}")
        print("\n")

    def total_balances(self):
        total_bal = 0
        for account in self.accounts:
            total_bal = total_bal + account.total_balance
        self.total_balance = total_bal
        print(f"Total Bank Balance: {self.total_balance}")

    def total_loans(self):
        total_lon = 0
        for account in self.accounts:
            if account.balance < 0:
                total_lon = total_lon + account.balance
        self.total_loan = total_lon
        print(f"Total Bank Loan Amount: {-self.total_loan}")

    def off_loan(self):
        self.loan_status = False
        print("Loan feature turned off.")

    def on_loan(self):
        self.loan_status = True
        print("Loan feature turned on")


bank = Bank()
currentUser = None

while True:
    if currentUser is None:
        print("\n")
        print("1. For Register")
        print("2. For Admin")
        print("3. Exist")
        choice = int(input("Choose an option: "))

        if choice == 1:
            name = input("Name: ")
            email = input("E-mail: ")
            address = input("Address: ")
            password = input("Password: ")
            accountType = input("Savings Account or Cuurent Account (Sa/Ca): ")

            if accountType == "Sa":
                interestRate = int(input("Interest rate: "))
                bank.create_account(
                    name, email, address, password, "Savings", interestRate=interestRate)
            elif accountType == "Ca":
                overdraftLimit = int(input("Overdraft Limit: "))
                bank.create_account(
                    name, email, address, password, "Cuurent", overdraftLimit=overdraftLimit)
            bank.show_accountNumber()
            for account in Account.accounts:
                currentUser = account

        # --------------***************--------------------
        # For Admin login passwoard is "admin"
        # --------------***************--------------------

        elif choice == 2:
            admin_password = input("Enter Admin Password: ")
            if admin_password == "admin":
                print("\n Admin logged in!\n")
                while True:
                    print("Admin Options:")
                    print("1. Create an Account")
                    print("2. Delete an Account")
                    print("3. Show Users")
                    print("4. Total Bank Balance")
                    print("5. Total Loan Amount")
                    print("6. Turn Off Loan Feature")
                    print("7. Turn On Loan Feature")
                    print("8. Logout")
                    admin_choice = int(input("Choose an option: "))
                    if admin_choice == 1:
                        name = input("Name: ")
                        email = input("E-mail: ")
                        address = input("Address: ")
                        password = input("Password: ")
                        accountType = input(
                            "Savings Account or Cuurent Account (Sa/Ca): ")

                        if accountType == "Sa":
                            interestRate = int(input("Interest rate: "))
                            bank.create_account(
                                name, email, address, password, "Savings", interestRate=interestRate)
                        elif accountType == "Ca":
                            overdraftLimit = int(input("Overdraft Limit: "))
                            bank.create_account(
                                name, email, address, password, "Cuurent", overdraftLimit=overdraftLimit)
                    elif admin_choice == 2:
                        account_number = input(
                            "Enter Account Number to delete: ")
                        bank.delete_account(account_number)
                    elif admin_choice == 3:
                        bank.show_users()
                    elif admin_choice == 4:
                        bank.total_balances()
                    elif admin_choice == 5:
                        bank.total_loans()
                    elif admin_choice == 6:
                        bank.off_loan()
                    elif admin_choice == 7:
                        bank.on_loan()
                    elif admin_choice == 8:
                        currentUser = None
                        break
                    else:
                        print("Invalid Admin Option")
        elif choice == 3:
            break
    else:
        print(f"\nWelcome {currentUser.name}!\n")
        if currentUser.type == "Savings":
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Current Balance")
            print("4. Change Info")
            print("5. Apply Interest")
            print("6. Logout\n")
            option = int(input("Choose Option: "))
            if option == 1:
                amount = int(input("Enter withdraw amount: "))
                currentUser.withdraw(amount)
            elif option == 2:
                amount = int(input("Enter deposit amount: "))
                currentUser.deposit(amount)
            elif option == 3:
                currentUser.show_curr_balance()
            elif option == 4:
                new_name = input("Enter new name: ")
                new_password = input("Enter new password: ")
                currentUser.changeInfo(new_name, new_password)
            elif option == 5:
                currentUser.apply_interest()
            elif option == 6:
                currentUser = None
            else:
                print("Invalid Option")
        else:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. Change Info")
            print("5. Logout\n")
            option = int(input("Choose Option: "))
            if option == 1:
                amount = int(input("Enter withdraw amount: "))
                currentUser.withdraw(amount)
            elif option == 2:
                amount = int(input("Enter deposit amount: "))
                currentUser.deposit(amount)
            elif option == 3:
                currentUser.showInfo()
            elif option == 4:
                new_name = input("Enter new name: ")
                new_password = input("Enter new password: ")
                currentUser.changeInfo(new_name, new_password)
            elif option == 5:
                currentUser = None
            else:
                print("Invalid Option")
