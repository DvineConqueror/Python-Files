import random

# set variables
board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - "]
currentPlayer = " X "
winner = None
gameRunning = True

# printing game board


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----------")
    print(board[6] + "|" + board[7] + "|" + board[8])

#  take player input


def playerInput(board):
    while True:
        inp = int(
            input(f"It is {currentPlayer}'s turn! \nEnter a number from 1 - 9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == " - ":
            board[inp-1] = currentPlayer
            break
        else:
            print("Invalid Choice, please select again.")
            printBoard(board)

# check for win or tie


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " - ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " - ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " - ":
        winner = board[6]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " - ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " - ":
        winner = board[2]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " - ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " - ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " - ":
        winner = board[2]
        return True


# check for win or tie again
def checkWin(board):
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        printBoard(board)
        print(f"The winner is {winner}")
        global gameRunning
        gameRunning = False


def checkTie(board):
    if " - " not in board:
        printBoard(board)
        print("It is a tie!")
        global gameRunning
        gameRunning = False

# switch the player


def switchPlayer():
    global currentPlayer
    if currentPlayer == " X ":
        currentPlayer = " O "
    else:
        currentPlayer = " X "


# AI
def computer(board):
    while currentPlayer == " O " and gameRunning:
        position = random.randint(0, 8)
        if board[position] == " - ":
            board[position] = " O "
            switchPlayer()


# Game Loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    # If the game has ended, don't let the computer make a move
    if not gameRunning:
        break
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)
