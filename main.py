import random

while True:
    Player = input("Enter a choice (R, P, S): ")
    #R for rock; P for paper; S for scissors.
    possible_options = ["R", "P", "S"]
    CPU = random.choice(possible_options)
    print(f"\nPlayer {Player}: CPU {CPU}.\n")

    if Player == CPU:
        print(f"Both players selected {Player}. It's a tie!")
        input_again = input("Play again? (y/n): ")
        if input_again.lower() != "y":
            break
    elif Player == "R":
        if CPU == "S":
            print("Player")
        else:
            print("CPU")
    elif Player == "P":
        if CPU == "R":
            print("Player")
        else:
            print("CPU")
    elif Player == "S":
        if CPU == "R":
            print("Player")
        else:
            print("CPU")
    else:
        print("Error")
        input_again = input("Play again? (y/n): ")
        if input_again.lower() != "y":
            break
