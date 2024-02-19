plaintext = input("please enter a word: ")
distance = int(input("please enter the required distance: "))
codedPlaintext = " "
for ch in plaintext:
    ordvalue = ord(ch)
    cipheredchr = ordvalue + distance
    if cipheredchr > ord('z'):
        cipheredchr = ord('a') + distance - (ord('z') - ordvalue + 1)
    cipheredWord = chr(cipheredchr)
    codedPlaintext += cipheredWord
print(codedPlaintext)

