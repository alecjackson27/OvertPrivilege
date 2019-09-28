# import
from cryptanalysisUtils import *

# take user input
plaintext = input("Please enter the plain text: ")
ciphertext = input("Please enter the cipher text: ")

# strip spaces from the plaintext
plaintext = plaintext.replace(" ", "")

# go through all possible lengths of keys
for length in range(1, 8):
    # make a set of arrays for the potential length
    arrays = makeArrays(length, plaintext)

    # see if this is a correct length
    if correctLength(arrays, ciphertext):
        # chop up the cipher text, matching each chunk to an array
        key = keyFromArrays(arrays, ciphertext)
        print("the key is ", key)
        break

