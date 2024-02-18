'''
Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines is found.

'''
ffilename = input("please enter the name of the first file: ")
sfilename = input("please enter the name of the second file: ")

f1 = open(ffilename, "r")
f2 = open(sfilename, "r")

text1 = f1.readlines()
text2 = f2.readlines()

for line1,line2 in zip(text1,text2):
    if line1 != line2:
        print(f"No,The differenet lines are: {line1,line2} ")
        break
    else: print("Yes")





