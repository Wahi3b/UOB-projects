
import random

def generate_square_board():
    """
    change square_board above to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    """
    square_board = [0,0,0,0]
    return square_board

def print_board(square_board):
   
   """
   :param square_board:
   print the board as instructed
   """
   formatted_board ="|%-2s|%-2s|\n|%-2s|%-2s|" % (square_board[0], square_board[1], square_board[2], square_board[3])

   print(formatted_board)

def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    
    for i in range(4):
        randomNum = random.randint(1,20)
        square_board[i] = randomNum
    return square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    message = "There is a win"
    message = "No win"
   """
    sumOfitems = 0
    for i in range(4):
        sumOfitems += square_board[i]
    if sumOfitems % 10 == 0:
        message = "There is a win"
    else:
        message = "No win"
    return (message)

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)