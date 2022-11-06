import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type number larger than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)

while True:
    users_guess = input("Make a guess: ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print("Please type a number next time.")
        continue
    

    if users_guess == random_number:
        print("You")