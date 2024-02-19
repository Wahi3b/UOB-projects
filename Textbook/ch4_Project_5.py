def shift_left(bit_string):
    shifted_string = bit_string[1:] + bit_string[0]
    return shifted_string


bit_string = input("Enter a bit string: ")
result = shift_left(bit_string)
print("Result after left shift:", result)