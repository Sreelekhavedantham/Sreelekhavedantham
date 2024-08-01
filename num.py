import random

def number_guess_game():
    
    lower_bound = 1
    upper_bound = 100
    
   
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    guessed = False

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while not guessed:
        try:
            
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guess_game()