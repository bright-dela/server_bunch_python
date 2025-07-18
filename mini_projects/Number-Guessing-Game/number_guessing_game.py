import random
import math

# Welcoming message
# ask the user for a number
# compare user guess with secret number
# if user guess equal to the secret number then congratulate the user for guessing right
# if user guess is lower than the secret number then "Your guess is too low"
# if user is high than the secret number then "your guess is too high."


print("\n#####################################\n")

print("\nWelcome to the Number Guessing Game!")

play_again = "yes"

while play_again.lower() == "yes":

    print("\n#####################################\n")

    print("\nChoose a difficulty level:")
    print(" '1' for Easy ( 1 - 50 )")
    print(" '2' for Medium ( 1 - 100 )")
    print(" '3' for Hard ( 1 - 1000 )")

    difficulty = input("\nEnter 1, 2, or 3: ")

    if difficulty == "1":
        max_range = 50
    elif difficulty == "2":
        max_range = 100
    elif difficulty == "3":
        max_range = 1000
    else:
        print("\nInvalid choice. Please enter either 1, 2, or 3")
        continue

    max_attempts = math.ceil(math.log2(max_range))

    if max_range == 50:
        max_attempts = max_attempts + 9
        print(f"\nI'm thinking of a number between 1 and {max_range}.")
        print(f"\nYou have {max_attempts} attempts to guess it.")

    elif max_range == 100:
        max_attempts = max_attempts + 3
        print(f"\nI'm thinking of a number between 1 and {max_range}.")
        print(f"\nYou have {max_attempts} attempts to guess it.")

    else:
        print(f"\nI'm thinking of a number between 1 and {max_range}.")
        print(f"\nYou have {max_attempts} attempts to guess it.")

    secret_number = random.randint(1, max_range)

    attempts = 0
    while attempts < max_attempts:
        user_input = input(
            f"\nAttempts {attempts + 1} of {max_attempts}. Enter your guess: "
        )

        if not user_input.isdigit():
            print("\nInvalid input. Please enter a number.")
            continue

        guess = int(user_input)
        # print("guess:", guess)

        attempts = attempts + 1

        if guess < secret_number:
            print("\nYour guess is too low")

        elif guess > secret_number:
            print("\nYour guess is too high")

        elif guess == secret_number:
            print(
                f"\n🎆 Correct! You guessed it in {attempts} attempts.\n🥳🎇🎇🎇🎇🎇🎇🎇🎆🎆🎆🎆🎇🥳"
            )
            break

    else:
        print(f"\n😟 Game over! The number was {secret_number}")

    play_again = input("\nDo you want to play again? (yes / no): ")

print("\nThank you for playing! Goodbye.")

print("\n#####################################\n")
