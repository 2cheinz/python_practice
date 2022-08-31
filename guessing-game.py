# Guessing game, have a user try to guess a random number imported by the computer
import random

random_number = random.randint(1,10)    # Represents the numbers 1-10 that the computer will be randomly generating

user_guesses = None

while True:
    user_guesses = int(input("Guess a number between 1-10: "))
    if user_guesses < random_number:
        print("Too low - try again!")
    elif user_guesses > random_number:
        print("Too high - try again!")
    else:
        print("Congratulations, you win!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)
            user_guesses = None
        else:
            print("Thank you for playing")
            break


#  if user_tries >= 3:
#             print(input("Would you like to keep playing? (y/n)"))
#             if 