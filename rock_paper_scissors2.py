import random

user_wins = 0
computer_wins = 0

options = ("rock", "paper", "scissors")

while True:
    user_pick = input("Choose rock, paper, scissors or Q to quit: ").lower()
    
    if user_pick == "q":
        break

    if user_pick not in options:
        print("You need to type rock, paper or scissors.")
        continue

    random_number = random.randint(0, 2)
    #rock-0, paper-1, scissors-2
    computer_pick = options[random_number]
    print(f"Computer pick {computer_pick}.")

    if user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_pick == computer_pick:
        print("Draw!")
    else:
        print("Computer won!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
