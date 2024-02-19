'''
numberlines.py
Write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text.
'''
ffilename = input("please enter the name of the first file: ")
sfilename = input("please enter the name of the second file: ")

f1 = open(ffilename, 'r')
f2 = open(sfilename, 'w')
n=1
for line in f1:
    linenumber =str(n) + ">" + line 
    f2.write(linenumber)
    #print(f"{n}>, {line}")
    n+=1
f2.close()



