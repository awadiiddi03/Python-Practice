class Account:
#     making the pin
    def __init__(self, account_id, initial_balance, pin):
        self.account_id = account_id
        self.balance = initial_balance
        self.pin = pin  # Storing the pin for a specific account

    def verify_pin(self, entered_pin):
        #chech if the pin matches the account
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class ATM:
    """Manages secure access to multiple Account objects."""
    def __init__(self):
        self.accounts = []
        self.current_account = None

    def initialize_accounts(self):
        print("--- WELCOME ---")
        while len(self.accounts) < 5:
            try:
                print(f"\nSetting up Account {len(self.accounts)+1}")
                bal_val = input("Enter starting balance: ").strip()
                balance = int(bal_val)
                if balance < 0:
                    print("Balance cannot be negative.")
                    continue
                
                pin = input("Set a 4-digit PIN for this account: ").strip()
                if len(pin) != 4 or not pin.isdigit():
                    print("PIN must be exactly 4 digits.")
                    continue

                self.accounts.append(Account(len(self.accounts) + 1, balance, pin))
            except ValueError:
                print("Invalid input. Please enter a whole number for the balance.")

    def select_account(self):
        while True:
            try:
                choice = int(input(f"\nSelect account (1-5): "))
                if 1 <= choice <= 5:
                    selected = self.accounts[choice - 1]
                    
                    # Check: make sure the PIN is correct before giving access
                    attempts = 0
                    authenticated = False
                    while attempts < 3:
                        entered_pin = input(f"Enter PIN for Account {choice}: ").strip()
                        if selected.verify_pin(entered_pin):
                            self.current_account = selected
                            print("Access Granted.")
                            authenticated = True
                            break
                        else:
                            attempts += 1
                            print(f"Incorrect PIN. Attempts remaining: {3 - attempts}")
                    
                    if authenticated:
                        break
                    else:
                        print("Too many failed attempts. Please select a different account or try again later.")
                else:
                    print("Invalid selection. Choose 1-5.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        self.initialize_accounts()
        self.select_account()

        while True:
            print("\n" + "="*20)
            print(f"ACCOUNT {self.current_account.account_id} ACTIVE")
            print("1) Check Balance")
            print("2) Deposit")
            print("3) Withdraw")
            print("4) Switch Account")
            print("5) Quit")
            
            choice = input("Choose an option: ").strip()

            if choice == "1":
                print(f"Current Balance: R{self.current_account.balance}")

            elif choice == "2":
                try:
                    amt = int(input("Enter deposit amount: "))
                    if self.current_account.deposit(amt):
                        print(f"Success! New balance: R{self.current_account.balance}")
                    else:
                        print("Invalid amount.")
                except ValueError:
                    print("Please enter a whole number.")

            elif choice == "3":
                try:
                    amt = int(input("Enter withdrawal amount: "))
                    if self.current_account.withdraw(amt):
                        print(f"Success! New balance: R{self.current_account.balance}")
                    else:
                        print("Insufficient funds or invalid amount.")
                except ValueError:
                    print("Please enter a whole number.")

            elif choice == "4":
                self.select_account()

            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    my_atm = ATM()
    my_atm.run()