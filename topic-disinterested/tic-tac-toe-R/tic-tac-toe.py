
#   Programmer:       Cheng, Jeff
#   Last Modified:    08-20-24 09:51AM
#   Problem:          Tic Tac Toe, by Al Sweigart

#   all keys for a Tic Tac Toe board dictionary
ALL_SPACES = list('123456789')

#   constants for string values
X, O, BLANK = 'X', 'O', ' '

def main():
    #   runs a game of Tick Tac Toe
    print("Welcome to Tic Tac Toe!")

    #   create a Tic Tac Toe board dictionary
    gameBoard = createBoard()

    #   X goes first; O goes next
    currentPlayer, nextPlayer = X, O

    while True:
        #   print the board
        drawBoard(gameBoard)

        #   get a valid move
        move = None
        while not isValidSpace(gameBoard, move):
            #   if invalid space, keep prompting user to enter a number 1-9
            print("What is " + currentPlayer + "'s move (1-9)?")
            move = input()
 
        #   move validated, now make it in effect
        updateBoard(gameBoard, move, currentPlayer)

        #   check game progress, i.e. if th game is over
        #   first check for victory
        if isWinner(gameBoard, currentPlayer):
            drawBoard(gameBoard)

            print(currentPlayer + ' has won the game!')
            break
        #   next check for a tie
        elif isBoardFull(gameBoard):
            drawBoard(gameBoard)

            print('The game is a tie!')
            break
        
        #   swap turns
        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    #   thank you message
    print("Thanks for playing")

#   create a new, blank Tic Tac Toe board
def createBoard():
    #   a dictionary that represents a board
    board = {}

    for space in ALL_SPACES:
        board[space] = BLANK

    return board

#   returns a text-representatoin of the board
def drawBoard(board):
    myBoard = str(board['1'] + '|' + board['2'] + '|' + board['3'] + "\t1 2 3\n"
                  + board['4'] + '|' + board['5'] + '|' + board['6'] + "\t4 5 6\n"
                  + board['7'] + '|' + board['8'] + '|' + board['9'] + "\t7 8 9\n")

    return print(myBoard)

#   returns True if the space on the board is a valid space number and the space is blank
def isValidSpace(board, space):
    return space in ALL_SPACES and board[space] == BLANK

#   returns True if player is a winner on this Tic Tac Toe board
def isWinner(board, player):
    b, p = board, player

    #   check for 3 marks across the 3 rows, 3 columns, and 2 diagonals
    return (
        #   across the top row
        (b['1'] == b['2'] == b['3'] == p) or
        #   across the center row
        (b['4'] == b['5'] == b['6'] == p) or
        #   across the bottom row
        (b['7'] == b['8'] == b['9'] == p) or
        #   down the left column
        (b['1'] == b['4'] == b['7'] == p) or
        #   down the center column
        (b['2'] == b['5'] == b['8'] == p) or
        #   down the right column
        (b['3'] == b['6'] == b['9'] == p) or
        #   diagonal from upper-left to lower-right
        (b['1'] == b['5'] == b['9'] == p) or
        #   diagonal from upper-right to lower-left
        (b['3'] == b['5'] == b['7'] == p)
    )

#   returns True if every space on the board has been taken
def isBoardFull(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True

#   sets the space on the board to mark
def updateBoard(board, space, mark):
    board[space] = mark

#   calls main if this module is run, but not when imported
if __name__ == '__main__':
    main()