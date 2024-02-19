plaintext = input("please enter a string:")
final = ""
for ch in plaintext:
    ordvalue = ord(ch)
    bitString = ""
    while ordvalue > 0:
        remainder = ordvalue % 2
        ordvalue = ordvalue // 2
        bitString = str(remainder) + bitString
    codedword = bitString[1:] + bitString[0]
    final += codedword + " "
print(final)

 

        