from move import isValidMove
def createBoard():
    board = [['R', 'K', 'B', 'Q', 'M', 'B', 'K', 'R'], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ["X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X", "X", "X"],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['r', 'k', 'b', 'm', 'q', 'b', 'k', 'r']]
    return board


def printBoard(board):
    print(" - - - - - - - - -")
    for i in range(8):
        print('|', end=' ')
        for j in range(8):
            print(board[i][j], end=' ')
        print('|', end=' ')
        print()
    print(" - - - - - - - - -")


def promptMove(check):
    onBoard = False
    while onBoard == False:
        move = input("Enter move if format(piece, move, original")
        move_array = move.split(", ")
        if isValidMove(move_array[0],move_array[2],move_array[1]):
            return move_array



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = createBoard()
    printBoard(board)
    whiteMove = True
    winner = False
    promptMove(True)
    while winner == False:
        winner = True
        if whiteMove == True:
            print(1)
        else:
            print(1)
        printBoard(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
