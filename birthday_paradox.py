'''
The Birthday Paradox, also called the Birthday Problem, is the surprisingly high 
probability that two people will have the same birthday even in a small group of people. 
In a group of 70 people, there's a 99.9 percent chance of two people having a matching 
birthday. But even in a group as small as 23 people, there's a 50 percent chance of a 
matching birthday. This program performs several probability experiments to determine 
the percentages for groups of different sizes. We call these types of experiments, 
in which we conduct multiple random trials to understand the likely outcomes, 
Monte Carlo experiments.
'''

import datetime
import random

## Generate the birthdays
def getBirthdays(numberOfBirthdays):
    birthdays = []
    for _ in range(numberOfBirthdays):
        startOfYear = datetime.date(2000, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None
    
    # Compare each birthday to every other birthday
    for i , a in enumerate(birthdays):
        for j, b in enumerate(birthdays[i+1:]):
            if a == b:
                return a

print('------ Birthday Paradox ------')
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
            'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    inputNumber = input('> ')
    if inputNumber.isdecimal() and (0 < int(inputNumber) <= 100):
        numofBDays = int(inputNumber)
        break
    else:
        print('Please enter a number between 1 and 100')
print()
print(f'Here are {numofBDays} birthdays:')
birthdays = getBirthdays(numofBDays)
# Display the birthdays
for i , birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()
# Determine if there are two birthdays that match.
match = getMatch(birthdays)
# Display the results
print(f'In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print(f'multiple people have a birthday on {dateText}.')
else:
    print('there are no matching birthdays.')


