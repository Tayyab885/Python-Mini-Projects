import random
user_win = 0
comp_win = 0
options = ["rock","paper","secissor"]
while True:
    user_pick = input("Pick Rock/Paper/Secissor or (q) to Quit: ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        continue

    random_number = random.randint(0,2) #rock:0,paper:1,secissor:2
    computer_pick = options[random_number] #computer_pick = options[1] = paper
    print(f"Computer Picked {computer_pick}.")

    if user_pick == "rock" and computer_pick == "secissor":
        print("You won!")
        user_win += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1
    elif user_pick == "secissor" and computer_pick == "paper":
        print("You won!")
        user_win += 1
    elif user_pick == computer_pick:
        print("Tie!")
    
    else:
        print("You lost!")
        comp_win += 1

print(f"You Won {user_win} times.")
print(f"Computer Won {comp_win} times.")
print("Goodbye!")
    



