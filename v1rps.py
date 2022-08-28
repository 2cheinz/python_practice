print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, enter your choice: ")
player2 = input("Player 2, enter your choice: ")

if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Please check your choices, something went wrong! :(")