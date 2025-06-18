import random

user_score = 0
comp_score = 0
choices = ["rock", "paper", "scissors"]

while True:
    user = input("rock, paper, scissors or q to quit: ").lower()
    if user == "q":
        break
    if user not in choices:
        continue

    comp = random.choice(choices)
    print("Computer chose:", comp)

    if user == comp:
        print("Tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print("You:", user_score, "| Computer:", comp_score)
