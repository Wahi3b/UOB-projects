'''
Author: Wahib Ben Said
Chapter 3 Project Q1
This program accepts three inputs of a triangle and outpots if the triangle is equilateral or not
'''

t1 = int(input("please enter the 1st traingle length:"))
t2 = int(input("please enter the 2nd traingle length:"))
t3 = int(input("please enter the 3rd traingle length:"))

if t1 == t2 == t3 :
    print("The triangle is equilateral")
else : 
    print("The triangle is not equilateral")
