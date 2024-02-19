#plaintext = input("please enter the file name: ")
f = open("ch4.txt", 'r')
worded = f.read()
distance = int(input("please enter the required distance: "))
codedPlaintext = ""
for ch in worded:
    ordvalue = ord(ch)
    cipheredchr = ordvalue + distance
    if cipheredchr > ord('z'):
        cipheredchr = ord('a') + distance - (ord('z') - ordvalue + 1)
    cipheredWord = chr(cipheredchr)
    codedPlaintext += cipheredWord
print(codedPlaintext)