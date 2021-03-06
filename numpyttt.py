#Importing libraries
import numpy as np
import os 


#Global variables
#Using an array of 2s to represent an empty board
board = np.full((3,3), 2, dtype=int)
#Dictionary to convert the move input by the user into the desired matrix position
movesDict = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}


#User defined functions
def printBoard():
    print("")
    print(board)
    print("")


def playGame():
    #O -> 0  X -> 1
    print("Welcome to tic tac toe!")
    turn = 1
    count = 0

    for num in range(10):
        printBoard()
        #If the board is already full, terminate the loop
        if count==9:
            break

        move = int(input("Move to which place {}? ".format(turn)))
        if move<1 or move>9:
            print("Invalid move.")
            continue
        #Converting the user input into the matrix position
        realMove = movesDict.get(move, "Invalid move")
        row = realMove[0]
        col = realMove[1]
        
        #Checking if the place is empty or not
        if board[row][col]==2:
            board[row][col] = turn
            winner = checkWin(turn)

            #If we have a winner
            if winner!="":
                print("")
                printBoard()
                print("\nWinner is {}!".format(winner))
                break 
            #In case there is no winner after this move
            else:
                count += 1
                if turn == 1:
                    turn = 0
                else:
                    turn = 1 
        else:
            print("That place is filled. Choose another one.")
            continue
        
    print("\nGame Over!")


def checkWin(turn):
    winner = ""
    #Checking the rows
    if (board[0][0]==board[0][1]==board[0][2]==turn) or (board[1][0]==board[1][1]==board[1][2]==turn) or (board[2][0]==board[2][1]==board[2][2]==turn):
        winner = turn;
    #Checking the columns
    elif (board[0][0]==board[1][0]==board[2][0]==turn) or (board[0][1]==board[1][1]==board[2][1]==turn) or (board[0][2]==board[1][2]==board[2][2]==turn):
        winner = turn;
    #Checking diagonals
    elif (board[0][0]==board[1][1]==board[2][2]==turn) or (board[0][2]==board[1][1]==board[2][0]==turn):
        winner = turn;
    #No win
    else:
        winner = ""

    return winner


def clearScreen():
    if os.name == 'posix':
	#For UNIX Systems
        _ = os.system('clear')
    else:
	#For Windows
        _ = os.system('cls')


def restartGame():
    restart = input("Play again? (y/n) ")
    if restart == "y":
        board = np.full((3,3), 2, dtype=int)
        clearScreen()
        print("\nRestarting the game:\n")
        playGame()
    else:
        print("Thank you for playing!")


#Main function
def main():
    playGame()
    restartGame()

if __name__ == '__main__':
    main()