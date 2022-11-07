import random

user_wins = 0
computer_wins = 0

options = ("rock", "paper", "scissors")

open("file2.txt", "w")



while True:
    

    user_pick = input("Choose rock, paper, scissors or Q to quit: ").lower()
    with open("file2.txt", "a") as f:
        f.write("You pick " + user_pick + "\n")

    if user_pick == "q":
        break

    if user_pick not in options:
        print("You need to type rock, paper or scissors.")
        continue

    random_number = random.randint(0, 2)
    #rock-0, paper-1, scissors-2
    computer_pick = options[random_number]
    print(f"Computer pick {computer_pick}.")
    with open("file2.txt", "a") as f:
        f.write("Computer pick " + str(computer_pick) + "\n")

    if user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        with open("file2.txt", "a") as f:
            f.write("You won!\n")

    elif user_pick == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1
        with open("file2.txt", "a") as f:
            f.write("You won!\n")

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        with open("file2.txt", "a") as f:
            f.write("You won!\n")

    elif user_pick == computer_pick:
        print("Draw!")
        with open("file2.txt", "a") as f:
            f.write("Draw\n")

    else:
        print("Computer won!")
        computer_wins += 1
        with open("file2.txt", "a") as f:
            f.write("Computer won!\n")

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")

with open("file2.txt", "a") as f:
    f.write(f"You won {user_wins} times.\n")
    f.write(f"Computer won {computer_wins} times.")
