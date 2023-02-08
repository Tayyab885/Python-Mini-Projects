answers = ["c","a","b","b"]
score = 0

print("Welcome to the Quiz Game!!")
ready = input("Press y/n if you want to play.").lower()

if ready != 'y':
    quit()

print('Let"s play')

question1 = '''
1. What Does CPU Stand For?
a) Central Performance Unit
b) Control Processing Unit
c) Central Processing Unit
d) Common Processing Unit'''
print(question1)
answer1 = input("Whats the right answer?")
if answer1 == "c":
    answers.remove("c")
    print("Correct Answer.")
    score +=1
else:
    answers.remove("c")
    print("Wrong answer. Right answer was c.")


question2 = '''
2. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned'''
print(question2)
answer2 = input("Choose Correct Option: ").lower()

if answer2 == "a":
    answers.remove("a")
    print("Correct Answer.")
    score +=1
else:
    answers.remove("a")
    print("Wrong answer. Right answer was a.")

question3 = '''
3. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted'''
print(question3)
answer3 = input("Choose Correct Option: ").lower()
if answer3 == "b":
    answers.remove("b")
    print("Correct Answer.")
    score +=1
else:
    answers.remove("b")
    print("Wrong answer. Right answer was b.")

question4 = '''
4. Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()'''
print(question4)
answer4 = input("Choose Correct Option: ").lower()

if answer4 == "b":
    answers.remove("b")
    print("Correct Answer.")
    score +=1
else:
    answers.remove("b")
    print("Wrong answer. Right answer was b.")

print(f"You got {score} right answers.")