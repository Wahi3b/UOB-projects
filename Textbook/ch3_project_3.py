'''
Author: Wahib Ben Said
Chapter 3 Project Q3
This program accepts three inputs of a triangle and outpots if the triangle is equilateral or not
'''
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count,"tries!")
        break
