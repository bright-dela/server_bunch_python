import json
import os
import hashlib

# pin = "1234"
# hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
# print(hashed_pin)


# Load or Create users database

if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)

else:
    users = {}


print("\n====== Welcome To Server Bunch ATM ======\n")


print("Do you want to login or register?\n")
user_action = input("Enter [ 1 ] to register or [ 2 ] to login: ")

username = None
# Register
if user_action == "1":
    while True:
        username = input("\nChoose a username: ").strip().lower()

        if username in users:
            print("\nUsername already exists.")
            break

        else:
            pin = input("\nCreate your 4-digit PIN: ")

            confirm_pin = input("\nConfirm your PIN: ")

            if pin == confirm_pin and pin.isdigit() and len(pin) == 4:
                hashed_pin = hashlib.sha256(pin.encode()).hexdigest()

                users[username] = {
                    "pin": hashed_pin,
                    "balance": 1000,
                }

                with open("users.json", "w") as file:
                    json.dump(users, file)
                    print("\nRegistered successfully.")
                    break

            else:
                print("\nPIN mismatch or invalid.")
                break


# Login
elif user_action == "2":

    while True:

        username = input("\nUsername: ").strip().lower()

        if username not in users:
            print("\nUser not found!")
            continue

        else:
            attempts = 3

            while attempts > 0:

                pin = input("\nEnter your PIN: ")

                hashed_pin = hashlib.sha256(pin.encode()).hexdigest()

                if hashed_pin == users[username]["pin"]:
                    print("\nLogged in.")
                    break

                else:
                    attempts -= 1

                    if attempts == 0:
                        print("\nToo many failed attempts. Account locked.")
                        exit()

                    else:
                        print(f"\nIncorrect PIN. {attempts} tries left.")

        break


# Invalid Option
else:
    print("\nInvalid option.")


# ===== ATM Functionalities =====

deposit_attempts = 3

withdrawal_attempts = 3

options_attempts = 3

running = True

while running:

    print("\n===== ATM MENU =====")
    print("Select 1 to Check Balance.")
    print("Select 2 to Deposit Money.")
    print("Select 3 to Withdraw Money.")
    print("Select 4 to Exit.")

    user_choice = input("\nChoose an option ( 1, 2, 3, or 4 ): ")

    # Check Balance
    if user_choice == "1":
        print(f"\nYour current balance is GHC {users[username]["balance"]:,}\n")

    # Deposit Money
    elif user_choice == "2":
        amount = input("\nEnter amount to deposit: ")

        deposit_attempts -= 1

        if amount.isdigit():

            amount = float(amount)

            if amount > 0:
                users[username]["balance"] += amount

                with open("users.json", "w") as file:
                    json.dump(users, file)

                print(f"\n✅ GHC {amount:,} deposited successfully.\n")

            else:
                print("\n❌ Deposit amount must be greater than zero.\n")

        elif deposit_attempts <= 0:
            print("\nTransaction error!\n")
            running = False

        else:
            print(
                f"\nInvalid input. Please enter a valid amount.\n{deposit_attempts} attempt(s) left.\n"
            )

    # Withdraw Money
    elif user_choice == "3":

        amount = input("\nEnter amount to withdraw: ")

        if amount.isdigit():
            amount = float(amount)

            if amount <= 0:
                print("\nWithdrawal amount must be greater than 0.\n")

            elif amount > users[username]["balance"]:
                print("\nInsufficient balance.\n")

            else:
                users[username]["balance"] -= amount

                with open("users.json", "w") as file:
                    json.dump(users, file)

                print(f"\n✅ GHC {amount:,} withdrawn successfully.\n")

        else:
            withdrawal_attempts -= 1
            print("\nInvalid input. Please enter a valid number.\n")

    # Exit
    elif user_choice == "4":
        print("\nThanks for using the ATM. Goodbye!\n")
        running = False

    elif options_attempts <= 0:

        print("\nToo many attempts")
        running = False

    else:
        options_attempts -= 1
        print(f"\nPlease enter a valid option.\n{options_attempts} attempt(s) left.\n")
        continue
