# ===============================
# Tic Tac Toe with Minimax
# ===============================

board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

player = "O"
computer = "X"


# -------------------------------
# Print Board
# -------------------------------
def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print()


# -------------------------------
# Insert Value
# -------------------------------
def insertValue(position, symbol):
    if board[position] == " ":
        board[position] = symbol
        printBoard(board)

        if checkWhoWin(symbol):
            if symbol == computer:
                print("Computer wins")
            else:
                print("You win")
            exit()

        if checkForDraw():
            print("It's a draw")
            exit()
    else:
        print("Position already occupied!")


# -------------------------------
# Check Win
# -------------------------------
def checkWhoWin(symbol):
    return (
        (board[1] == board[2] == board[3] == symbol) or
        (board[4] == board[5] == board[6] == symbol) or
        (board[7] == board[8] == board[9] == symbol) or
        (board[1] == board[4] == board[7] == symbol) or
        (board[2] == board[5] == board[8] == symbol) or
        (board[3] == board[6] == board[9] == symbol) or
        (board[1] == board[5] == board[9] == symbol) or
        (board[3] == board[5] == board[7] == symbol)
    )


# -------------------------------
# Check Draw
# -------------------------------
def checkForDraw():
    for key in board.keys():
        if board[key] == " ":
            return False
    return True


# -------------------------------
# Minimax Algorithm
# -------------------------------
def minimax(board, isMaximizing):

    if checkWhoWin(computer):
        return 1
    elif checkWhoWin(player):
        return -1
    elif checkForDraw():
        return 0

    if isMaximizing:
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = computer
                score = minimax(board, False)
                board[key] = " "
                bestScore = max(bestScore, score)
        return bestScore

    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = player
                score = minimax(board, True)
                board[key] = " "
                bestScore = min(bestScore, score)
        return bestScore


# -------------------------------
# Computer Move
# -------------------------------
def computerMove():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = computer
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertValue(bestMove, computer)


# -------------------------------
# Main Game Loop
# -------------------------------
print("Tic Tac Toe")
print("You are O | Computer is X")
printBoard(board)

while True:
    move = int(input("Enter position (1-9): "))
    insertValue(move, player)
    computerMove()
