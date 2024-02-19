'''
Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key.
'''

def main():
    number = (input("Please enter the number that you would like the square root for: "))
    if number != "":
        print("The square root of your number is: ", newton(int(number)))
        main()
    else: print("Goodbye")

def newton(number):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0
    # Perform the successive approximations
    while True:
        estimate = (estimate + number / estimate) / 2
        difference = abs(number - estimate ** 2)
        if difference <= tolerance:
          break
    return estimate

if __name__ == '__main__':
    import math
    main()