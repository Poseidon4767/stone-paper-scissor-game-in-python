import random
options = ["rock", "paper", "scissor"]

play = 1
while play:
    ai_choice = random.choice(options)
    player = input("rock, paper or scissor? ")

    print("I chose ", ai_choice, "and you chose ", player + ".")

    if ai_choice == "rock" and player.lower() == "scissor":
        print("I won!!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "rock" and player.lower() == "paper":
        print("You won!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "rock" and player.lower() == "rock":
        print("It's a draw!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "scissor" and player.lower() == "scissor":
        print("It's a draw!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "scissor" and player.lower() == "paper":
        print("I won!!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "scissor" and player.lower() == "rock":
        print("You won!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "paper" and player.lower() == "scissor":
        print("You won!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "paper" and player.lower() == "paper":
        print("It's a draw")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0
    elif ai_choice == "paper" and player.lower() == "rock":
        print("I won!!")
        a = input("Wanna play again?\n")
        if a.lower() == "yes":
            play = 1
        else:
            play = 0