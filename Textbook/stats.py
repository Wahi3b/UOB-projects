"""
Chapter 5 project 1
1. A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.
"""
def main():
    testSet = [5,3,2,5,7,8,9,11]
    print("The median is: " , median(testSet))
    print("The mode is: " ,mode(testSet))
    print("The mean is: " ,mean(testSet))

def median(set):
    if set == []: return 0
    else:
        set.sort()
        a = len(set)
        if len(set) % 2 == 0:
            setMean = float((set[int(len(set)/2)] + set[int(len(set)/2 -1)]) / 2)
        else: 
            setMean = float((set[int((len(set) - 1) / 2)]))
        return setMean
    

def mode(set):
    if set == []: return 0
    else:
        diction = {}
        for num in set:
            number = diction.get(num,None)
            if number == None:
                diction[num] = 1
            else: 
                diction[num] = number + 1
        theMaximum = max(diction.values())
        for each in diction:
            if diction[each] == theMaximum:
                modeNum = each
                break
        return modeNum


def mean(set):
    if set == []: return 0
    else:
        sum = 0
        values = 0
        for ch in set:
            sum +=ch
            values += 1
        meanValue = float(sum/values)
        return meanValue

if __name__ == "__main__":
    main()


