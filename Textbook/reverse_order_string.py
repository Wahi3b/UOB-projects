'''
This solves question 3 & 4 of chapter 3 page 102
'''
myString = "Wahib"
n = 0
reversedStirng = ""
for ch in range(len(myString)) :
    n +=1
    char = myString[len(myString) - n]
    reversedStirng += char
    print(char)
print(reversedStirng)