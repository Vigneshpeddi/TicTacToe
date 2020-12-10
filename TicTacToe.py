from os import system, name
from time import sleep
import random

def clear():
    if name == 'nt':
        _ = system('cls')

def displayBoard(board):
    for i in range(3):
        for j in range(3):
            if (j<2):
                print(board[i][j], end="")
                print("|", end="")
            else:
                print(board[i][j])
        if (i<2):
            print("-+-+-")
    print("\n")

def updateBoard(j, cell, playerSymbol):
    if cell == 1:
        j[0][0] = playerSymbol
    if cell == 2:
        j[0][1] = playerSymbol
    if cell == 3:
        j[0][2] = playerSymbol
    if cell == 4:
        j[1][0] = playerSymbol
    if cell == 5:
        j[1][1] = playerSymbol
    if cell == 6:
        j[1][2] = playerSymbol
    if cell == 7:
        j[2][0] = playerSymbol
    if cell == 8:
        j[2][1] = playerSymbol
    if cell == 9:
        j[2][2] = playerSymbol

def isThereAWinner(j, ps):
    status = False
    if j[0][0] == ps and j[0][1] == ps and j[0][2] == ps:
        status = True
    if j[1][0] == ps and j[1][1] == ps and j[2][2] == ps:
        status = True
    if j[2][0] == ps and j[2][1] == ps and j[2][2] == ps:
        status = True
    if j[0][0] == ps and j[1][0] == ps and j[2][0] == ps:
        status = True
    if j[0][1] == ps and j[1][1] == ps and j[2][1] == ps:
        status = True
    if j[0][2] == ps and j[1][2] == ps and j[2][2] == ps:
        status = True
    if j[0][0] == ps and j[1][1] == ps and j[2][2] == ps:
        status = True
    if j[2][0] == ps and j[1][1] == ps and j[0][2] == ps:
        status = True
    return status

def getCellCoordinates(cellNumber):
    if cellNumber == 1:
        return [0, 0]
    if cellNumber == 2:
        return [0, 1]
    if cellNumber == 3:
        return [0, 2]
    if cellNumber == 4:
        return [1, 0]
    if cellNumber == 5:
        return [1, 1]
    if cellNumber == 6:
        return [1, 2]
    if cellNumber == 7:
        return [2, 0]
    if cellNumber == 8:
        return [2, 1]
    if cellNumber == 9:
        return [2, 2]

def invalidInput(j, cellNumber):
    invalid = False
    coordinates = getCellCoordinates(cellNumber)
    if j[coordinates[0]][coordinates[1]] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        invalid = True
    return invalid
    
def isThereADraw():
    if isGameOver(board):
        draw = True
        if isThereAWinner(board, 'X') or isThereAWinner(board, 'O'):
            draw = False
    else:
        draw = False
    return draw

def isGameOver(board):
    gameOver = True
    for r in range(3):
        for c in range(3):
            if board[r][c] != 'X' and board[r][c] != 'O':
                gameOver = False
    return gameOver

def Game(board):
    print("<<< TIC TAC TOE >>>")
    print("\n")
    print("How To Play: There are two players, Player X and Player O. Each player places their symbol on a cell in the grid. The objective of the game is to line up your symbols to make a horizontol, verical, or diagonal line. You cannot place your symbol in a cell where someone already placed a symbol.")
    print("Have Fun!!!")
    print("\n")
    ans = input("Play[y/n]? ")

    if ans == "y":
        clear()
        displayBoard(board)

    while ans == "y":
        cellNumber = int(input("Your Turn, Player X: "))
        while invalidInput(board, cellNumber):
            cellNumber = int(input("Your Turn, Player X: "))
        updateBoard(board, cellNumber, 'X')
        clear()
        displayBoard(board)
        if isThereAWinner(board, 'X'):
            print("Hooray, Player X Wins!!!")
            break
        if isThereADraw():
            print("There is a Draw!!!")
            break

        cellNumber = int(input("Your turn, Player O: "))
        updateBoard(board, cellNumber, 'O')
        clear()
        displayBoard(board)
        if isThereAWinner(board, 'O'):
            print("Hooray, Player O Wins!!!")
            break
        if isThereADraw():
            print("There is a Draw!!!")
            break

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

while True:
    Game(board)
    playAgain = input("Play Again[y/n]? ")
    if playAgain != 'y':
        break
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    clear()


