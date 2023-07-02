import random
import os

def numDice():
    while True:
        try:
            num_dice = input("How many dice would you like to roll? ")
            valid_response = ['1','one','2','two']
            if num_dice not in valid_response:
                raise ValueError("1 or 2 only please")
            else:
                return num_dice
        except ValueError as e:
            print("Please enter a valid number")
            print(e)
            
            
def dice():
    min_val = 1
    max_val = 6
    roll_again = "y"
    
    while roll_again.lower() == "y" or roll_again.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        dice_number = numDice()
        
        if dice_number == '2' or dice_number == 'two':
            print("Rolling the dice...")
            dice1 = random.randint(min_val, max_val)
            dice2 = random.randint(min_val, max_val)
            
            print("The values are: ")
            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            print(f"Total: {dice1 + dice2}")
            
            roll_again = input('Roll Again?')
            
        else:
            print("Rolling the dice...")
            dice1 = random.randint(min_val,max_val)
            print(f'The value is: {dice1}')

            roll_again = input('Roll Again? ')
        
if __name__ == '__main__':
    dice()
        