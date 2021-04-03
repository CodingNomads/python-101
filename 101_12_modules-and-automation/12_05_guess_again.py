# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1, 10)
count = 5
guess = None

while guess != num and count > 0:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    count -= 1
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

if not count:
    print("You're out of tries...")