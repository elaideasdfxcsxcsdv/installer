import random
os.system('cls')
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts_left = 7  # Player gets 7 attempts
    
    while attempts_left > 0:
        print(f"\nYou have {attempts_left} attempts remaining.")
        try:
            # Get the player's guess
            guess = int(input("Make a guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            # Check the guess
            if guess == number_to_guess:
                print("Congratulations! You guessed the number!")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            
            attempts_left -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts_left == 0:
        print(f"\nGame Over! The number was {number_to_guess}.")


number_guessing_game()
os.system('cls')
print("-------------------------------------------------------")
print("System> Error has occured.")
print("System> Press enter to exit...")
input()
exit()
