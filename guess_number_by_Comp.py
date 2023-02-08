import random
def GuessNum():
    low = 1
    high = 100
    user = ""
    while user != "c":
        if low != high:
            num = random.randint(low,high)
        else:
            num = low
        user = input(f"{num}.Enter (s) for smaller (l) or larger and (c) for correct: ").lower()
        if user == "s":
            low = num + 1
        elif user == "l":
            high = num - 1
    print(f"Correct Number is {num}.")
if __name__ == "__main__":
    GuessNum()