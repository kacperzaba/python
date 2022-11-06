print("Welcome in my quiz game")
playing = input("Do you want to play?").lower()

if playing != "yes":
    quit()

score = 0

print("Let's go!")
answer1 = input("What was first capitol of Poland?").lower()
if answer1 == "gniezno":
    print("You are right!")
    score += 1
else:
    print("You are wrong!")


answer2 = input("What is the biggest city in Poland?" ).lower()
if answer2 == "warsaw":
    print("That is true!")
    score += 1
else:
    print("No it is not true!")

answer3 = input("What is teh longgest river in Poland? ").lower()
if answer3 == "wisla":
    print("You are right!")
    score += 1
else: 
    print("You are wrong!")

print(f"You score {score} points!")
print(f"You get {score * 100 / 3} %")