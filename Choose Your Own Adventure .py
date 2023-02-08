name = input("Enter Your Name: ")
print(f"Welcome {name} to this Advanture!")

user_input = input("You are lost in a Jungle and now there are Two ways ahead left and right. Type left or right: ").lower()
if user_input == "left":
    q1 = input("Okay theres a river ahead how you want to cross it by swim or bridge. Type bridge or swim: ").lower()
    if q1 == "swim":
        print("You are drowned. You Lost!")
    elif q1 == "bridge":
        print("The bridge break you Lost!")
    else:
        print("Invalid input you lost!")

elif user_input == "right":
    q2 = input("Now there is a mountain ahead. How you want to cross it. Type cave or climb:").lower()
    if q2 == "cave":
        print("You Lost Yourself and Die. You Lost!")
    elif q2 == "climb":
        print("Congrats You find the civilization ahead. You Won!!")
    else:
        print("Invalid input you lost!")
else:
    print("Invalid input you lost!")