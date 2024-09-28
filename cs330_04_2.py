global balance
balance = 500

def atm():
    print("Welcome to the ATM.")
    pin = input("Enter your 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Exiting.")
        return

    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        global balance
        print(f"Your current balance is ${balance}")
    elif choice == "2":
        dep = input("Enter amount to deposit: ")
        if dep.isdigit():
            balance += int(dep)
            print(f"${dep} has been deposited. Your new balance is ${balance}")
        else:
            print("Invalid amount")
    elif choice == "3":
        withdraw = input("Enter amount to withdraw: ")
        if withdraw.isdigit():
            if int(withdraw) <= balance:
                balance -= int(withdraw)
                print(f"${withdraw} has been withdrawn. Your new balance is ${balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")
    elif choice == "4":
        acc = input("Enter the account number you want to transfer to: ")
        if not acc.isdigit() or len(acc) != 10:
            print("Invalid account number.")
            return
        amount = input("Enter the amount to transfer: ")
        if not amount.isdigit():
            print("Invalid amount.")
            return
        if int(amount) <= balance:
            balance -= int(amount)
            print(f"${amount} has been transferred to account {acc}. Your new balance is ${balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid choice")

atm()
#Issues: The global variable balance is not being updated after the first transaction.
#        The program does not loop back to the main menu after a transaction.
#        The program does not check for invalid input in the account number and amount fields.
#        The program does not check for invalid input in the choice field.
#        The program does not check for invalid input in the deposit and withdraw fields.
#        The program does not check for invalid input in the PIN field.
#        The program does not check for insufficient balance before withdrawing or transferring.
#        The program does not check for a 4-digit PIN.
#       No encapsulation of the global variable balance.
#       No encapsulation of the atm function.
#       No encapsulation of the main menu.
#       No encapsulation of the transaction functions.
#       No encapsulation of the input validation.
#       No encapsulation of the balance variable.
#       Input validation is not encapsulated.
#       Improved version:
class atm:
    def __init__(self):
        self.balance = 500
    def validate_pin(self, pin):
        if len(pin) != 4 or not pin.isdigit():
            return False
        return True
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount.isdigit():
            self.balance += int(amount)
            return True
        return False
    def withdraw(self, amount):
        if amount.isdigit():
            if int(amount) <= self.balance:
                self.balance -= int(amount)
                return True
        return False
    def transfer(self, acc, amount):
        if not acc.isdigit() or len(acc) != 10 or not amount.isdigit():
            return False
        if int(amount) <= self.balance:
            self.balance -= int(amount)
            print(f"${amount} has been transferred to account {acc}. Your new balance is ${self.balance}")
            return True
        return False
        print("Insufficient balance.")
    def main_menu(self):
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print(f"Your current balance is ${self.check_balance()}")
        elif choice == "2":
            dep = input("Enter amount to deposit: ")
            if self.deposit(dep):
                print(f"${dep} has been deposited. Your new balance is ${self.check_balance()}")
            else:
                print("Invalid amount")
        elif choice == "3":
            withdraw = input("Enter amount to withdraw: ")
            if self.withdraw(withdraw):
                print(f"${withdraw} has been withdrawn. Your new balance is ${self.check_balance()}")
            else:
                print("Invalid amount")
        elif choice == "4":
            acc = input("Enter the account number you want to transfer to: ")
            amount = input("Enter the amount to transfer: ")
            if self.transfer(acc, amount):
                pass
            else:
                print("Invalid input.")
        else:
            print("Invalid choice")
        self.main_menu()
a = atm()
a.main_menu()

"""Output:
cs330_04_2.py:48:0: C0301: Line too long (101/100) (line-too-long)
cs330_04_2.py:96:0: C0301: Line too long (106/100) (line-too-long)
cs330_04_2.py:117:0: C0301: Line too long (101/100) (line-too-long)
cs330_04_2.py:132:0: C0305: Trailing newlines (trailing-newlines)
cs330_04_2.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cs330_04_2.py:1:0: W0604: Using the global statement at the module level (global-at-module-level)
cs330_04_2.py:2:0: C0103: Constant name "balance" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_2.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:18:8: W0603: Using the global statement (global-statement)
cs330_04_2.py:4:0: R0912: Too many branches (16/12) (too-many-branches)
cs330_04_2.py:71:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_2.py:71:0: C0103: Class name "atm" doesn't conform to PascalCase naming style (invalid-name)
cs330_04_2.py:71:0: E0102: class already defined line 4 (function-redefined)
cs330_04_2.py:74:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:78:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:80:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:91:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_2.py:99:8: W0101: Unreachable code (unreachable)
cs330_04_2.py:100:4: C0116: Missing function or method docstring (missing-function-docstring)"""
#pycodestyle
"""cs330_04_2.py:4:1: E302 expected 2 blank lines, found 1
cs330_04_2.py:32:80: E501 line too long (88 > 79 characters)
cs330_04_2.py:48:80: E501 line too long (101 > 79 characters)
cs330_04_2.py:54:1: E305 expected 2 blank lines after class or function definition, found 1
cs330_04_2.py:55:1: E265 block comment should start with '# '
cs330_04_2.py:55:80: E501 line too long (86 > 79 characters)
cs330_04_2.py:57:80: E501 line too long (94 > 79 characters)
cs330_04_2.py:59:80: E501 line too long (89 > 79 characters)
cs330_04_2.py:61:80: E501 line too long (96 > 79 characters)
cs330_04_2.py:71:1: E302 expected 2 blank lines, found 0
cs330_04_2.py:74:5: E301 expected 1 blank line, found 0
cs330_04_2.py:78:5: E301 expected 1 blank line, found 0
cs330_04_2.py:80:5: E301 expected 1 blank line, found 0
cs330_04_2.py:85:5: E301 expected 1 blank line, found 0
cs330_04_2.py:91:5: E301 expected 1 blank line, found 0
cs330_04_2.py:96:80: E501 line too long (106 > 79 characters)
cs330_04_2.py:100:5: E301 expected 1 blank line, found 0
cs330_04_2.py:111:80: E501 line too long (96 > 79 characters)
cs330_04_2.py:117:80: E501 line too long (101 > 79 characters)
cs330_04_2.py:130:1: E305 expected 2 blank lines after class or function definition, found 0
cs330_04_2.py:132:1: W391 blank line at end of file

"""
#pep8
"""pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead.

$ pip install pycodestyle
$ pycodestyle ...

  warnings.warn(
cs330_04_2.py:4:1: E302 expected 2 blank lines, found 1
cs330_04_2.py:32:80: E501 line too long (88 > 79 characters)
cs330_04_2.py:48:80: E501 line too long (101 > 79 characters)
cs330_04_2.py:55:1: E265 block comment should start with '# '
cs330_04_2.py:55:80: E501 line too long (86 > 79 characters)
cs330_04_2.py:57:80: E501 line too long (94 > 79 characters)
cs330_04_2.py:59:80: E501 line too long (89 > 79 characters)
cs330_04_2.py:61:80: E501 line too long (96 > 79 characters)
cs330_04_2.py:71:1: E302 expected 2 blank lines, found 0
cs330_04_2.py:74:5: E301 expected 1 blank line, found 0
cs330_04_2.py:78:5: E301 expected 1 blank line, found 0
cs330_04_2.py:80:5: E301 expected 1 blank line, found 0
cs330_04_2.py:85:5: E301 expected 1 blank line, found 0
cs330_04_2.py:91:5: E301 expected 1 blank line, found 0
cs330_04_2.py:96:80: E501 line too long (106 > 79 characters)
cs330_04_2.py:100:5: E301 expected 1 blank line, found 0
cs330_04_2.py:111:80: E501 line too long (96 > 79 characters)
cs330_04_2.py:117:80: E501 line too long (101 > 79 characters)
cs330_04_2.py:132:1: W391 blank line at end of file
"""