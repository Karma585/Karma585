import random

secret_number = random.randint(1, 10)
max_attempts = 3

def welcome_message():
    print("\nWelcome to the number guessing game!")
    print(f"you have {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempts_left):
    guess = int(input("\nGuess the number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulation! you guessed the correct number!")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left-1}")
        if attempts_left > 1:
            guess_recursive(attempts_left - 1)
        
        else:
            print(f"\nSorry, you couldnt guess the number. the correct number was {secret_number}.")
welcome_message()
guess_recursive(max_attempts)

print(f"Memory address of secret number {secret_number} is: {id(secret_number)}")