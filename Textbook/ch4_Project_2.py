plaintext = input("please enter the coded: ")
distance = int(input("please enter the distance: "))
codedPlaintext = " "
for ch in plaintext:
    ordvalue = ord(ch)
    cipheredchr = ordvalue - distance
    if cipheredchr < ord('a'):
        cipheredchr = ord('z') - distance + (ordvalue - ord('a') + 1)
    cipheredWord = chr(cipheredchr)
    codedPlaintext += cipheredWord
print(codedPlaintext)