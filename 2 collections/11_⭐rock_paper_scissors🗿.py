import random

options = ("rock", "paper", 'scissors')
is_running = True

while is_running: 

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    if not input("Play again (y/n): ").lower() == "y":
        is_running = False

    
print("Thanks for playing")