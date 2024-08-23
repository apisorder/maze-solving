
# Programmer:       Cheng, Jeff
# Last Modified:    07-18-24 08:38PM
# Problem:          Rock, Paper, Scissor Game

import random, sys

print('Rock, Paper, Scissors')

#   variables to keep track of basic stats
wins, losses, ties = 0, 0, 0

#   the main game loop
while True:
    print("Current progress: " + str(wins) + " wins, " + str(losses) + " losses, " + str(ties) + " ties.")

    #   player input loop
    while True:
        print("Enter your move : (r)ock, (p)aper, (s)cissors, or (q)uit.")
        playerMove = input()

        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break

        #   invalid input
        print('Valid input:  r, p, s, or q.')

    #   echo what the player chose:

    if playerMove == 'r':
        print(' Rock versus ... ')
    elif playerMove == 'p':
        print(' Paper versus ... ')
    elif playerMove == 's':
        print(' Scissors versus ... ')

    #   echo what the computer chose:
    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print(' Rock.')
    elif randomNumber == 2:
        computerMove = 'p'
        print(' Paper.')
    elif randomNumber == 3:
        computerMove = 's'
        print(' Scissors.')

    #   show match results and record them
    
    if playerMove == computerMove:
        print('It is a tie.')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win! ')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win! ')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win! ')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose! ')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose! ')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose! ')
        losses += 1