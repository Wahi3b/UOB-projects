'''
copyfile.py
'''

firstName = input("please enter the name of the first file: ")
secondName = input("please enter the name of the second file: ")
f = open(firstName, 'r')
f2 = open(secondName, 'w')
firstName = f.read()
f2.write(firstName)
f2.close()

