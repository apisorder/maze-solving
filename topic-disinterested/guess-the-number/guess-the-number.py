
# Programmer:       Cheng, Jeff
# Last Modified:    07-18-24 08:38PM
# Problem:          Guess the number

#   This is a guess the number game
import random

secretNumber = random.randint(1, 20)
print(' I am thinking of a number between 1 and 20. ')

#   ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print(' Take a guess. ')
    guess = int(input())

    if guess < secretNumber:
        print(' Your guess is too low. ')
    elif guess > secretNumber:
        print(' Your guess is too high. ')
    else:
        #   This conditon is the correct guess!
        break

if guess == secretNumber:
    print(' Good job! You guessed my number in ' + str(guessesTaken) + ' guesses! ')
else:
    print(' Nope. The number I am thinking of was ' + str(secretNumber))
