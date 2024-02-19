'''
Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
'''

def main():
    listOFNum = input()
    print("The average of the numbers is = ", averageNum(listOFNum))


def input():
    textFile = open('1.txt','r')
    numberinFile = textFile.read().split()
    return numberinFile

def averageNum(list):
    sum=0
    numOfitems=0
    avg = 0
    for item in list:
        sum+=int(item)
        numOfitems+=1
    avg = sum / numOfitems
    return avg

if __name__ == '__main__':
    main()
