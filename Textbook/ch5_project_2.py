"""
Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.

"""

fileName = input("Please input the file name: ")

lineNumber = 0
lineList = []

# Open the file and iterate through its lines
with open(fileName, 'r') as file:
    for line in file:
        lineNumber += 1
        lineList.append(line.strip())  # Append each line to lineList after stripping whitespace
lineN = int(input("please enter the required line number: "))
if lineN == 0: quit
else: print(lineList[int(lineN-1)])



