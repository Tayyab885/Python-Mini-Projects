List = ["c","a","b","b"]
score = 0
print("Welcome To My Quiz!")

play = input("Do You Want To Play?").lower()

if play != "yes":
    quit()

print("Let's Play: )")

question1 = '''
1. What Does CPU Stand For?
a) Central Performance Unit
b) Control Processing Unit
c) Central Processing Unit
d) Common Processing Unit'''
print(question1)
answer1 = input("Choose Correct Option: ").lower()
if answer1 == List[0]:
    List.remove(answer1)
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question2 = '''
2. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned'''
print(question2)
answer2 = input("Choose Correct Option: ").lower()
if answer2 == List[1]:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question3 = '''
3. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted'''
print(question3)
answer3 = input("Choose Correct Option: ").lower()
if answer3 == List[2]:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question4 = '''
4. Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()'''
print(question4)
answer4 = input("Choose Correct Option: ").lower()
if answer4 == List[3]:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} Questions Right")
print(f"You got {(score/4)*100}%.")