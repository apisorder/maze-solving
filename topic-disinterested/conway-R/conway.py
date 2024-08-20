
#   Programmer:       Cheng, Jeff
#   Last Modified:    08-11-24 10:23PM
#   Problem:          Game of Life

#   Lists are a sequence data type that is mutable; tuples and strings are sequence data types 
#   which are immutable.

#   Tuples and strings can, however, be overwritten with a new tuple or string value; their values
#   cannnot be modified in place, i.e. through append() or remove methods on lists.

#   Lists do not store list values.  Instead, they store references to lists.  Therefore, since
#   the value that is being copied (or passed as aguments as function calls) is the list reference,
#   any changes which was made to the list might impact another variable in the program.

#   If we want to make changes to a list in one variable without modifying the original list,
#   the copy() or deepcopy() methods may be used.

#   Conway's Game of Life

#   The following program demonstrates cellular automata, governed by a set of rules affecting
#   the behavior of a field made up of discrete cells.

#   These rules are:
#   A filled-in square will be "alive" and, an empty square will be "dead."
#   If a living square has two or three living neighbors, it remains alive on the next step. 
#   If a dead square has exactly three living neighbors, it comes alive on the next step.
#   Every other square dies or remains alive on the next step.

import random, time, copy
WIDTH, HEIGHT = 60, 20

#   a list of of column lists
nextCells = []

#   for each of the vertical slots, create a column
for x in range(WIDTH):
    #   randomize living and dead cells
    column = []

    for y in range(HEIGHT):
        #   add a living cell
        if random.randint(0, 1) == 0:
            column.append("#")
        #   add a dead cell
        else:
            column.append(" ")

    #   add it to the list
    nextCells.append(column)

#   main program loop
while True:

    #   each iteration will be a single step of the cellular automata

    #   separate each step with newlines    
    print("\n\n\n\n\n")

    currentCells = copy.deepcopy(nextCells)

    #   print current cells on the screen

    #   layer by layer, top to bottom
    for y in range(HEIGHT):
        #   cell by cell, left to right
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        #   print a newline at the end of each layer
        print()

    #   calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):

            #   the % mod operator performs a "wraparound"
            leftCoord, rightCoord  = (x-1) % WIDTH, (x+1) % WIDTH
            aboveCoord, belowCoord = (y-1) % HEIGHT, (y+1) % HEIGHT 

            #   reset count number of living cells
            numNeighbors = 0
            
            #   note how left and right precedes top and bottom

            #   if top-left neighbor is alive
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            #   if top neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            #   if top-right neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            
            #   if left neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            #   if right neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1

            #   if bottom-left neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            #   if bottom neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            #   if bottom-right neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            #   set next cell's values based on current cell's values:

            #   if a living cell has 2 or 3 neighbors, it remains alive
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            #   if a dead cell has exactly 3 neighbors, it becomes alive:
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            #   everything else dies or remains dead
            else:
                nextCells[x][y] = ' '
        
    #   add a 1-second pause to reduce flickering
    time.sleep(1)