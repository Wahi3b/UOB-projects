'''
A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.
(Hint: For a list of length 2 or greater, loop through the list and compare pairs of
items, from left to right, and return False if the first item in a pair is greater.)
'''
def main():
    listInput = [1,3,5,4]
    if isSorted(listInput) == True:
        print("The list was sorted in ascending order")
    else: print("The list was not sorted in ascending order")



def isSorted(list):
    if list == []: return True
    else:
        n=0
        for x in range(len(list)-1):
            if list[n] <= list[n+1]:
                n+=1
                pass
            else: 
                sortedList = False
                break
            sortedList = True
    return sortedList

if __name__ == '__main__':
    main()