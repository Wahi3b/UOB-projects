import os
def main():
    clear_screen()
    square_board = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    printBoard(square_board)
    playing = True
    turn = "X"
    while playing:
        userInput = input(f"Player {turn}, please enter which square 1~9 or q to quit: \n")
        if userInput == "q": 
            print ("Thanks for Playing")
            break
        if square_board[userInput] != "X" and square_board[userInput] != "O":
            square_board[userInput] = turn
            clear_screen()
            printBoard(square_board)
            if wonOrNot(square_board):
                playing = False
                print(f"Player {turn} have WON, Congrats")
            turn = switchTurn(turn)
        else:
            clear_screen()
            print("Please choose a square that haven't been chosen before")
            printBoard(square_board)
    return turn


def wonOrNot(square_board):
    if (square_board['1'] == square_board['2'] == square_board['3'] or 
        square_board['4'] == square_board['5'] == square_board['6'] or 
        square_board['7'] == square_board['8'] == square_board['9'] or
        square_board['1'] == square_board['4'] == square_board['7'] or
        square_board['2'] == square_board['5'] == square_board['8'] or
        square_board['1'] == square_board['5'] == square_board['9'] or
        square_board['3'] == square_board['6'] == square_board['9'] or
        square_board['3'] == square_board['5'] == square_board['7']):
        return True
    else:
        return False

def printBoard(square_board):
    print(f"|{square_board['1']}|{square_board['2']}|{square_board['3']}|\n"
        f"|{square_board['4']}|{square_board['5']}|{square_board['6']}|\n"
        f"|{square_board['7']}|{square_board['8']}|{square_board['9']}|")
    
def switchTurn(turn):
    if turn == "X":
        turn = "O"
        return turn
    else:
        turn = "X"
        return turn
    
def clear_screen():
    # Check the operating system and use the appropriate command to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
        


if __name__ == "__main__":
    main()
    







