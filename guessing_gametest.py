import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guess_count = 0

while True:
    guess_count += 1
    users_guess = input("Guess a number: ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print("Type a number next time.")
        continue

    if users_guess == random_number:
        print("You guessed!!!")
        break
    elif users_guess > random_number:
        print("You were above the nnumber.")
    else:
        print("You were below the number.")

print("You got it in", guess_count," guesses")





