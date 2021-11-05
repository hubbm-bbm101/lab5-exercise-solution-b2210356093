import random
randomnumber = random.randint(0,100)

while True:
    guess = int(input("Guess the number! (between 0 and 100) "))
    if guess < 0:
        print("You can't choose a number less than zero.")
    if guess < randomnumber:
        print("Increase your number.")
    elif guess > randomnumber:
        print("Decrease your number.")
    else:
        print("--- You've found it.!")
        break

input("Press any key to exit. ")
