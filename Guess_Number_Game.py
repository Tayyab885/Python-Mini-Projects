import random

num_range = input("Enter a number: ")

if num_range.isdigit():
    num_range = int(num_range)
    if num_range <= 0:
        print("Please Enter a positive number.")
else:
    print("Please Enter a number.")
    quit()

random_number = random.randint(0,num_range)
guesses = 0
while True:
    user_input = input("Enter your Guess: ")
    guesses +=1
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please Enter a number.")
        continue

    if user_input == random_number:
        print("Guessed Right.")
        break
    elif user_input > random_number:
        print("Enter a Lower Number.")
    else:
        print("Enter a Higher Number.")

print(f"You Guessed the number in {guesses} Guesses.")