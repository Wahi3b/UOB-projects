'''Define and test a function myRange. This function should behave like Python’s
standard range function, with the required and optional arguments, but it should
return a list. Do not use the range function in your implementation! (Hints:
Study Python’s help on range to determine the names, positions, and what to do
with your function’s parameters. Use a default value of None for the two optional
parameters. If these parameters both equal None, then the function has been
called with just the stop value. If just the third parameter equals None, then the
function has been called with a start value as well. Thus, the first part of the function’s
code establishes what the values of the parameters are or should be. The
rest of the code uses those values to build a list by counting up or down.)
Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.
Copyright
'''

def main():
    lower = 1
    upper = 10
    step = 2
    myList = rangeByme(upper)
    print(myList)

def rangeByme(upper,lower = 0, step =1):
    rangeList = []
    while upper !=lower :
        rangeList.append(lower)
        lower += step
    return rangeList
if __name__ == '__main__':
    main()


