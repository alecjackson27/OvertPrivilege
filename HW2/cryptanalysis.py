# imports


def determineLength(plain, cipher):
    possibleLengths = []
    for i in range(0, 7):
        if plain[i] in cipher[0]:
            possibleLengths.append(i)
    return possibleLengths

def makeArrays(length, plain):
    index = 0
    arrays = []
    for i in range(length+1):
        arrays.append([])

    for letter in plain:
        if index <= length:
            arrays[index].append(letter)
            index += 1
        else:
            arrays[0].append(letter)
            index = 1
    return arrays
def findMatch(arrays, cipher):
    # stuff and things

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


