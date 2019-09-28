# import
from cryptanalysisUtils import *

# take user input
plaintext = "you need to find the key" #input("Please enter the plain text: ")
ciphertext = "ntneudihyyeodkoefte" #input("Please enter the cipher text: ")

# strip spaces from the plaintext
plaintext = plaintext.replace(" ", "")

# determine the possible lengths of the key
lengths = determineLength(plaintext, ciphertext)
print("lengths: ", lengths)

# following steps will need to be repeated for all possible key lengths
# but for now I'm going to pretend it only turned up one

# make a set of arrays for the lengths
arrays = makeArrays(lengths[0], plaintext)

print(arrays)

# check if any of the arrays match the first letters of the cipher
indexOfFirstGroup = findMatch(arrays, ciphertext)

