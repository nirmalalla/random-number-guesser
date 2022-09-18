import random

randomNumber = random.randint(0, 10)
guess = input("Guess a number 1-10")
guess = int(guess)

if randomNumber == guess:
    print("You got it!")
else:
    while guess != randomNumber:
        if randomNumber > guess:
            guess = int(input("You guessed too low!"))
        else:
            guess = int(input("You guessed too high!"))
    if randomNumber == guess:
        print("You got it!")
