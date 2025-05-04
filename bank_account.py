# Bank Account
class BankAccount:
    # Created a base class of BankAccount
    def __init__(self, account_number, balance):
        # Initialized the class constructor, with attributes of account_number, balance
        self.account_number = account_number  # Instance Variable
        self.__balance = balance  # Encapsulated balance

    def deposit(self, amount):
        # Created deposit() under base class
        if amount > 0:  # Checked condition amount > 0
            self.__balance += amount
            # Calculation is done for deposit function
            print(f"Deposited {amount}. New balance: {self.__balance}")
            # Print current amount and deposited new amount
        else:
            # if Condition not satisfied, else block will be run
            print("Deposit amount must be positive.")  # Print the statement

    def withdraw(self, amount):
        # Created withdraw() under base class
        if 0 < amount <= self.__balance:
            # Checked condition amount <= self.__balance
            self.__balance -= amount
            # Calculation is done for withdraw function
            print(f"Withdrew {amount}. New balance: {self.__balance}")
            # Print withdrawal amount and new balance
        else:
            # if Condition not satisfied, else block will be run
            print("Insufficient balance or invalid amount.")
            # Print the statement

    def get_balance(self):
        # Created get_balance() to return the balance
        return self.__balance


class SavingsAccount(BankAccount):
    # Created a child class SavingsAccount from parent BankAccount
    def __init__(self, account_number, balance, interest_rate):
        # Initialized the class constructor, with attributes of account_number, balance and interest_rate
        BankAccount.__init__(self, account_number, balance)
        # Inheriting the account_number, balance from the parent class BankAccount
        self.interest_rate = interest_rate  # Instance Variable

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100  # Calculate interest
        print(f"Interest earned: {interest}")

        # Add interest to balance
        self.deposit(interest)
        print(f"New balance after adding interest: {self.get_balance()}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        # Initialized the class constructor, with attributes of account_number, balance, min_balance
        # Directly calling the parent class constructor
        BankAccount.__init__(self, account_number, balance)
        self.min_balance = min_balance  # Instance Variable

    def withdraw(self, amount):  # Overrides method from BankAccount
        if 0 < amount <= self.get_balance() - self.min_balance:  # Withdrawal Calculation
            BankAccount.withdraw(self, amount)  # Explicitly call parent method
        else:
            # if Condition not satisfied, else block will be run
            print("Insufficient funds. Minimum balance requirement not met.")
            # Print the statement


# Example Input Values:
print("***** Type of Account- SavingsAccount Transactions ******")
print("SavingsAccount Transactions for Account number SA123, Balance-Rs.5000 with interest rate of 5% ****")
savings = SavingsAccount("SA123", 5000, 5)
savings.deposit(1000) # Savings account deposit amount is updated
savings.calculate_interest() # Savings account's interest is updated
savings.withdraw(2000) # Savings account withdrawal amount is updated
savings.deposit(-1000) # Savings account deposit amount is updated


print("***** Type of Account- CurrentAccount Transactions *****") # Print the values
print("CurrentAccount Transactions for Account number CA456, Balance-Rs.10000, Minimum_balance-Rs.2000 ****") # Print the values
current = CurrentAccount("CA456", 10000, 2000)
current.deposit(5000) # Current account deposit amount is updated
current.deposit(7000) # Current account deposit amount is updated
current.withdraw(9000) # Current account withdrawal amount is updated
current.withdraw(12000)  # Current account withdrawal amount is updated
# Should fail due to minimum balance requirement

