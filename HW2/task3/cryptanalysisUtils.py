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
    print("not implemented yet")