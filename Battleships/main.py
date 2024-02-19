def gameBoard():
    board = [['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '']]
    return board

def hiddenBoard(userinput):
    import random
    hiddenBoard = [['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '']]
    count = userinput
    while count >=0:
        randomrow = random.randint(0,userinput)
        randomcol = random.randint(0,userinput)
        if hiddenBoard[randomrow][randomcol] == 'X':
            continue
        else:
            hiddenBoard[randomrow][randomcol] = 'X'
            count -=1
    
    return hiddenBoard


def printGameBoard(board):
    formattedOutput = (
        "  A B C D E F G H I\n"
        "9|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "8|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "7|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "6|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "5|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "4|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "3|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "2|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|\n"
        "1|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|%-2s|"
    ) % tuple(
        [
            board[8][0], board[8][1], board[8][2], board[8][3], board[8][4], board[8][5], board[8][6], board[8][7], board[8][8],
            board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7], board[7][8],
            board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7], board[6][8],
            board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7], board[5][8],
            board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7], board[4][8],
            board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7], board[3][8],
            board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7], board[2][8],
            board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7], board[1][8],
            board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7], board[0][8]
        ]
    )
    print(formattedOutput)


def playing():
    playing = True
    actualB = gameBoard()
    userinput = int(input("Please enter number of ships (1~9) \n")) -1
    hiddenB = hiddenBoard(userinput)
    printGameBoard(hiddenB)
    printGameBoard(actualB)
    while playing:
        myDic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}
        userRow = int(input("Please enter the row (1-9): \n")) - 1
        userColumn = input("Please enter the column (A-I) for the ship location: \n")
        userColumn = myDic[userColumn]
        userGuess = [userRow,userColumn]
        actualB = updateActualBoard(actualB,hiddenB,userGuess)
        hiddenB = updateHiddenBoard(actualB,hiddenB,userGuess)
        gameDone = doneOrNot(hiddenB)
        if gameDone:
            print("Congrats, all ships are destroyed")
            playing = False


def updateActualBoard(actualB,hiddenB,userGuess):
    if hiddenB[userGuess[0]][userGuess[1]] == "X":
        print("Bravo you've hit a ship")
        actualB[userGuess[0]][userGuess[1]] = "X"
        printGameBoard(actualB)
        return actualB
    else:
        print("You missed!")
        actualB[userGuess[0]][userGuess[1]] = "-"
        printGameBoard(actualB)
        return actualB

def updateHiddenBoard(actualB,hiddenB,userGuess):
    if hiddenB[userGuess[0]][userGuess[1]] == "X":
        hiddenB[userGuess[0]][userGuess[1]] = ''
    return hiddenB

def doneOrNot(hiddenB):
    doneornot = False
    for i in range(9):
        for j in range(9):
            if hiddenB[i][j] != '':
                return doneornot
            j +=1
        i+=1
    doneornot = True
    return doneornot
        
playing()




