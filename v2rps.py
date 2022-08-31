from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    player = input("Player, enter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    random_num = randint(0,2)

    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "scissors"
    else:
        computer = "paper"
    print(computer)

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_wins += 1
        elif computer == "paper":
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins!")
            computer_wins += 1
    else:
        print("ERROR: Please check the spelling of your choice! (it must equal rock, paper, or scissors")
if player_wins > computer_wins:
    print("YOU WIN!")
elif player_wins == computer_wins:
    print("It is a tie")
else:
    print("THE COMPUTER DEFEATED YOU!")
print(f"Final Scores:\nPlayer: {player_wins}\nComputer: {computer_wins}")