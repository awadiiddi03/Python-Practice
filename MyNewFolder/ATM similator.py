print("WELCOME")

# Collect 5 account balances from the user
accounts = []
while len(accounts) < 5:
    try:
        balance_input = input(f"Enter starting balance for account {len(accounts)+1}: ").strip()
        balance = int(balance_input)
        if balance < 0:
            print("Balance cannot be negative. Try again.")
            continue
        accounts.append(balance)
    except ValueError:
        print("Please enter a valid whole number.")


def select_account() -> int:
    while True:
        try:
            acc_number_input = input("Select your account (1-5): ").strip()
            acc_number = int(acc_number_input)
            if 1 <= acc_number <= 5:
                return acc_number - 1
            print("Please choose a number from 1 to 5.")
        except ValueError:
            print("Please enter a valid number from 1 to 5.")


current_index = select_account()


def show_menu() -> None:
    print("\nMenu:")
    print("1) Check balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Switch account")
    print("5) Quit")


choice = ""
while choice != "5":
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print(f"Current balance: {accounts[current_index]}")

    elif choice == "2":
        try:
            amount_input = input("Enter amount to deposit: ").strip()
            amount = int(amount_input)
            if amount <= 0:
                print("Deposit amount must be greater than 0.")
                continue
            accounts[current_index] += amount
            print(f"Deposited {amount}. New balance: {accounts[current_index]}")
        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "3":
        try:
            amount_input = input("Enter amount to withdraw: ").strip()
            amount = int(amount_input)
            if amount <= 0:
                print("Withdrawal amount must be greater than 0.")
                continue
            if amount > accounts[current_index]:
                print("Insufficient funds.")
                continue
            accounts[current_index] -= amount
            print(f"Withdrew {amount}. New balance: {accounts[current_index]}")
        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "4":
        current_index = select_account()
        print(f"Switched to account {current_index + 1}.")

    elif choice == "5":
        print("Goodbye!")

    else:
        print("Invalid option. Please choose 1-5.")
     