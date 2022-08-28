print("Rock...")
print("Paper...")
print("Scissors...")
import random
player = input("Player, enter your choice: ").lower()
random_num = random.randint(0,2)

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
    elif computer == "paper":
        print("Computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins!")
    elif computer == "paper":
        print("Player wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
else:
    print("ERROR: Please check the spelling of your choice! (it must equal rock, paper, or scissors")