import random
import string
words = ["computer","laptop","radio","python","data","reject","secret"]

def hangman():
    word = random.choice(words)
    letters = set(word)
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set()
    guess = 10
    while len(letters) > 0 and  guess > 0:
        print(f"You got {guess} lives left.")
        print("You used the letters:"," ".join(guessed_letters))
        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print("Current Word: "," ".join(word_list))
        user_guess = input("Enter your guess letter: ")
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word:
                letters.remove(user_guess)
            else:
                guess -= 1
                print("No letter found!")
        elif user_guess in guessed_letters:
            print("Letter already guessed!")
        else:
            print("Wrong letter. Please enter Someother letter.")
    if guess == 0:
        print(f"You have {guess} Guesses left. Try again!")
    else:
        print(f"Well Guessed! The word was {word}.")


if __name__ == '__main__':
    hangman()
