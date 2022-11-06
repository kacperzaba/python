options = ("rock", "paper", "scissors")

wins_of_player1 = 0
wins_of_player2 = 0

while wins_of_player1 < 3 and wins_of_player2 < 3:

    choose_of_player1 = input("Choose rock or paper or scissors: ").lower()
    choose_of_player2 = input("Choose rock or paper or scissors: ").lower()

    if choose_of_player1 not in options or choose_of_player2 not in options:
        print(" You have only 3 opotions!")
        continue
    elif choose_of_player1 == "paper" and choose_of_player2 == "rock":
        print("Player1 won!")
        wins_of_player1 += 1
    elif choose_of_player1 == "rock" and choose_of_player2 == "scissors":
        print("Player1 won!")
        wins_of_player1 += 1
    elif choose_of_player1 == "scissors" and choose_of_player2 == "paper":
        print("Player1 won!")
        wins_of_player1 += 1
    elif choose_of_player1 == choose_of_player2:
        print("Draw")
    else:
        print("Player2 won!")
        wins_of_player2 += 1

print(f"Player1 won {wins_of_player1} times.")
print(f"Player2 won {wins_of_player2} times.")
print("Goodbye")