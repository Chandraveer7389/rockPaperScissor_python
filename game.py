import random
import pro1
choice = int(input("What do you choose?Type 0 for rock,1 for scissor or 2 for paper "))
ran = random.randint(0,2)

if choice == ran:
    if choice == 0:
        print(f"Both computer and you choose rock")
        print(pro1.rock)
    elif choice == 1:
        print(f"Both computer and you choose scissor")
        print(pro1.scissor)
    else:
        print(f"Both computer and you choose paper")
        print(pro1.paper)
    print("Draw")

if choice == 0 and ran == 1:
    print("You choose")
    print(pro1.rock)
    print("Computer choose")
    print(pro1.scissor)
    print("you won")
if choice == 1 and ran == 2:
    print("You choose")
    print(pro1.scissor)
    print("Computer choose")
    print(pro1.paper)
    print("you won")
if choice == 2 and ran == 0:
    print("You choose")
    print(pro1.paper)
    print("Computer choose")
    print(pro1.rock)
    print("you won")
if ran == 0 and choice == 1:
    print("You choose")
    print(pro1.scissor)
    print("Computer choose")
    print(pro1.rock)
    print("you loose")
if ran == 1 and choice == 2:
    print("You choose")
    print(pro1.paper)
    print("Computer choose")
    print(pro1.scissor)
    print("you loose")
if ran == 2 and choice == 0:
    print("You choose")
    print(pro1.rock)
    print("Computer choose")
    print(pro1.paper)
    print("you loose")