class Account:
    def __init__(self, account_id, starting_balance):
        self.account_id = account_id
        self.balance = starting_balance

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
    #USER INTERFACE
    def __init__(self):
        self.accounts = []
        self.current_account = None

    def initialize_accounts(self):
        print("--- WELCOME ---")
        while len(self.accounts) < 5:
            try:
                val = input(f"Enter starting balance for account {len(self.accounts)+1}: ").strip()
                balance = int(val)
                if balance < 0:
                    print("Balance cannot be negative.")
                    continue
                # Create and store an Account object
                new_account = Account(len(self.accounts) + 1, balance)
                self.accounts.append(new_account)
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def select_account(self):
        while True:
            try:
                choice = int(input(f"\nSelect account (1-5): "))
                if 1 <= choice <= 5:
                    self.current_account = self.accounts[choice - 1]
                    print(f"Switched to Account {choice}")
                    break
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