import random

def start_game():
    print("--- Welcome to the Number Guessing Game! ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess a number (1-100): "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You found it in {attempts} tries!")
                break
            elif guess < secret_number:
                print("Higher! ↑")
            else:
                print("Lower! ↓")
        except ValueError:
            print("Please enter a valid number.")

    if guess != secret_number:
        print(f"Game Over! The number was {secret_number}.")

if __name__ == "__main__":
    start_game()
