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
            return True

        if checkForDraw():
            print("It's a draw")
            return True
        return False
    else:
        print("Position already occupied!")
        return False


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

    return insertValue(bestMove, computer)


# -------------------------------
# Main Game Loop
# -------------------------------
print("Tic Tac Toe")
print("You are O | Computer is X")
printBoard(board)

while True:
    try:
        move = int(input("Enter position (1-9): "))
        if move < 1 or move > 9:
            print("Please enter a number between 1 and 9")
            continue
        if insertValue(move, player):
            break
        if computerMove():
            break
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nGame ended")
        break
