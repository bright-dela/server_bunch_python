import random
import math

# Welcoming message
# ask the user for a number
# compare user guess with secret number
# if user guess equal to the secret number then congratulate the user for guessing right
# if user guess is lower than the secret number then "Your guess is too low"
# if user is high than the secret number then "your guess is too high."


print("\nWelcome to the Number Guessing Game!")

play_again = "yes"

while play_again.lower() == "yes":

    print("\nChoose a difficulty level:")
    print(" '1' for Easy ( 1 - 50 )")
    print(" '2' for Medium ( 1 - 100 )")
    print(" '3' for Hard ( 1 - 1000 )")

    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        max_range = 50
    elif difficulty == "2":
        max_range = 100
    elif difficulty == "3":
        max_range = 1000
    else:
        print("Invalid choice. Please enter either 1, 2, or 3")
        continue

    max_attempts = math.ceil(math.log2(max_range))

    print(f"\nThinking of a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts to guess it.")

    secret_number = random.randint(1, max_range)
    # print("secret number:", secret_number)

    attempts = 0
    while attempts < max_attempts:
        user_input = input(
            f"Attempts {attempts + 1} of {max_attempts}. Enter your guess: "
        )

        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(user_input)
        # print("guess:", guess)

        attempts = attempts + 1

        if guess < secret_number:
            print("Too low")

        elif guess > secret_number:
            print("Too high")

        elif guess == secret_number:
            print(f"🎆 Correct! You guessed it in {attempts} attempts.")
            break

    print(f"😟 Game over! The number was {secret_number}")

    play_again = input("Do you want to play again? (yes / no): ")

print("Thank you for playing! Goodbye.")
