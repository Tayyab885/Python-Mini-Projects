import random

COLORS = ['R','G','B','Y','W','O']
TRIES = 10
WORD_LENGTH = 4

## Generating random colors
def random_colors():
    color_code = []
    for i in range(WORD_LENGTH):
        color = random.choice(COLORS)
        color_code.append(color)
    return color_code

## Getting User Guesses
def guess_color():
    while True:
        user_guess = input("Guess: ").upper().split(" ")
        if len(user_guess) != 4:
            print("You must guess 4 colors.")
            continue
        for guess in user_guess:
            if guess not in COLORS:
                print(f"Invalid color: {guess}. Try Again.")
                break
        else:
            break
    
    return user_guess

## Checking correct and incorrect positions of guessed colors by user
def check_color(guess,real_color):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_color:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    

    for color_guess, color_real in zip(guess,real_color):
        if color_guess == color_real:
            correct_position += 1
            color_counts[color_guess] -= 1

    
    for color_guess, color_real in zip(guess,real_color):
        if color_guess in color_counts and color_counts[color_guess] > 0:
            incorrect_position += 1
            color_counts[color_guess] -= 1
    
    return correct_position, incorrect_position


def game():
    print(f"Welcome to mastermind game. You have {TRIES} tries to guess the colors..")
    print("The valid colors are: ", *COLORS)
    colors = random_colors()
    for attempts in range(1,TRIES+1):
        guess = guess_color()
        correct_pos, incorrect_pos = check_color(guess, colors)
        if correct_pos == WORD_LENGTH:
            print(f"You Guessed the code in {attempts} tries!")
            break
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}.")

    else:
        print("You ran out of tries. The Colors were: ", *colors)

if __name__ == "__main__":
    game()