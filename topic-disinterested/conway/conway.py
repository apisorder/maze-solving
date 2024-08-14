
#   Programmer:       Cheng, Jeff
#   Last Modified:    08-11-24 10:23PM
#   Problem:          Game of Life

#   Lists are useful data types since they allow you to write code that works on a modifiable
#   number of values in a single variable..

#   Lists are a sequence data type that is mutable, meaning that their contents can change.
#   Tuples and strings, though also sequence data types, are immutable and cnanot be cahnged.

#   A varaible that contains a tuple or string value can be overwritten with a new tuple or
#   string value, but this is not the same thing as modifying the existing value in place--
#   like, say, the append() and remove() methods do on lists.

#   Lists do not store list values; they store references to lists. This is an important distinction
#   when you are copying variables or passing lists as arguments in fuction calls.

#   Because the value that is being copied is the list reference, be aware that any changes you make
#   to the list might impact another varaible in the program.

#   You can use copy() or deepcopy() if you want to make changes to a list in one varaible without
#   modifying the original list

#   Demonstrates cellular automata:
#   a set of rules governing the behavior of a field made up of discrete cells.

#   A filled-in square will be "alive" and, an empty square will be "dead."

#   If a living square has two or three living neighbors, it remains alive on the next step. 

#   If a dead square has exactly three living neighbors, it comes alive
#   on the next step.

#   Every other square dies or remains alive on the next step.

#   Conway's Game of Life

import random, time, copy
WIDTH = 60
HEIGHT = 20

#   create a list of list for the cells
#   nextCells is a list of lists (column lists)
nextCells = []

#   the very first step of the cellular automata will be completely random

#   therefore, we create a list of lists data structure to store the '#' and ' '
#   strings which represent a living or dead cell, and their places in the list of lists
#   represent their position on the screen

for x in range(WIDTH):
    #   create a new column
    column = []

    #   for the list of lists data strucutre, the x-coordinate start at 0 on the left
    #   and increase going to right, while the y-coorindate start at 0 at the top
    #   and increase going down

    #   the inner list each represent a column of cells.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            #   add a living cell
            column.append("#")
        else:
            #   add a dead cell
            column.append(" ")
    #   nextCells stores the current column list
    nextCells.append(column)

#   main program loop
while True:
    #   each iteration of the main program loop will be a single step of the cellular automata.
    #   On each step, we will copy nextCells to currentCell, print currentCells on screen, and then
    #   use the cells in currentCells to calculate the cells in nextCells.

    #   separate each step with newline
    print('\n\n\n\n\n')

    #   we put the list of lists in a variable named nextCells, because the first step
    #   in our main program loop will be to copy nextCells into currentCells
    #   copy values with lists inside
    currentCells = copy.deepcopy(nextCells)

    #   print currentCells on the screen:
    #   note it is y/x, not x/y, as indicated by the newline
    for y in range(HEIGHT):
        for x in range(WIDTH):
            #   print the # or space
            print(currentCells[x][y], end='')
        #   print a newline at the end of each row
        print()

    #   calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #   get neighboring coordinates
            #   mod WIDTH ensures left coordinate is always between 0 and WIDTH-1

            #   the % mod operator performs a "wraparound".
            #   The left neighbor of a cell in the column 0 would be 0 - 1 or -1.
            #   To wrap this around to the rightmost column's index, 59, we calculate
            #   (0 - 1 ) % WIDTH.
            #   Since WIDTH is 60, this expression evaluates to 59.
            #   This mod-warparound technique works for the right, above, and below neighbors
            #   as well.
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #   count number of living neighbors
            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                #   top-left neighbor is alive
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#': 
                #   top neighbor is alive
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                #   top-right neighbor is alive
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                #   left neighbor is alive
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                #   right neighbor is alive
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                #   bottom-left neighbor is alive
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                #   bottom neighbor is alive
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            #   set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #   living cells with 2 or 3 neighbors stay alive:
                #   this is why we needed deepcopy
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #   dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                #   everything else dies or stays dead:
                nextCells[x][y] = ' '
        
    #   add a 1-second pause to reduce flickering
    time.sleep(1)