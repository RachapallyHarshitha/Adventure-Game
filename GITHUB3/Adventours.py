def start_game():
    print(" You’re lost in a desert. You must survive and find a way out!")

    choice1 = input("You see a camel and an oasis. Go to 'camel' or 'oasis'? ").lower()

    if choice1 == "camel":
        choice2 = input("Do you 'ride' the camel or 'rest' next to it? ").lower()
        if choice2 == "ride":
            print("The camel takes you to a village. You’re saved! ")
        else:
            print("A sandstorm hits while you rest. Game over! ️")
    
    elif choice1 == "oasis":
        choice2 = input("Drink water or look for food? Type 'drink' or 'food': ").lower()
        if choice2 == "drink":
            print("The water was fresh! You gain strength and find help nearby. You win! 🏆")
        else:
            print("You get bitten by a snake while looking for food. Game over! 🐍")
    
    else:
        print("You wander aimlessly and get lost forever. ️")

start_game()
