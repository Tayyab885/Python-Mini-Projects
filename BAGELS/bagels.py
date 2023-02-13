import random

MAX_DIGITS = 3
MAX_GUESSES = 10

def secretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(MAX_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def getClues(guess,secret_num):
    if guess == secret_num:
        return 'You Won!!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    
    while True: # Main game loop
        secretnum = secretNum()
        print('I have thought up a number.')
        numGuesses = 0
        print(f'You have {MAX_GUESSES - numGuesses}-Guesses to find the number.')
        while numGuesses < MAX_GUESSES:
            user_input = input('Enter Your guess: ')
            clue = getClues(user_input,secretnum)
            print(clue)
            numGuesses+=1
            if user_input == secretnum:
                break
            if numGuesses >= MAX_GUESSES:
                print('You ran out of Guesses')
                print(f'The answer was {secretnum}.')

if __name__ =='__main__':
    main()