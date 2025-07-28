#Guessing Game - Calleigh, Oliver, Melanie, Karla

import random

def generate_random_number():
    '''Generate a random number between 1-100'''
    return random.randint(0,100)

def get_user_guess():
    while True:
        guess = int(input("Guess a random number between 1-100: "))
        if guess >= 1 and guess <= 100:
            print(f"{guess} is a valid guess")
            return guess
        else:
            print(f"{guess} is invalid")

get_user_guess()

def play_guessing_game():
    secret_number = generate_random_number()
    attempts = 0 

    while True:
        guess = get_user_guess()
        attempts += 1
        
        if guess < secret_number:
            print("Too Low")
        elif guess > secret_number:
            print("Too High")
        else:
            print(f"Correct! You guessed the number in {attempts} tries.")
            break

def game_loop():
    print("Welcome to the Guessing Game!")

    while True:
        play_guessing_game()
        guess_again = input("\nWould you like to guess another number? (yes/no): ").lower()
        if guess_again not in ("yes"):
            print("Thank you for playing the Guessing Game!")
            break

if __name__ == "__main__": 
    game_loop()





            


