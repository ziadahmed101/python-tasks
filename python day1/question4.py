import random

print("Welcome to the Number Guessing Game!")

while True:
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nI have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print(" Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f" Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Invalid input. Please enter an integer number.")

    else:
        # Executed if the user runs out of attempts
        print(f"Sorry! You used all {max_attempts} attempts. The number was {secret_number}.")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print(" Thanks for playing! Goodbye.")
        break
