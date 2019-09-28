# returns an array of possible key lengths
def determineLength(plain, cipher):
    possibleLengths = []
    for i in range(0, 7):
        if plain[i] in cipher[0]:
            possibleLengths.append(i)
    return possibleLengths

# returns a list of columns to be used in transposition given a key of length
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

# checks if the array at length matches the first letters of the cipher text
def correctLength(arrays, cipher, length):
    for i in range(len(arrays[length])):
        if arrays[length][i] != cipher[i]:
            return False
    return True

# given a correct length of key, will determine the order of columns
def keyFromArrays(arrays, cipher):
    key = []
    for i in range(len(arrays)):
        key.append(0)
    for i in range(len(arrays)):
        match = findMatch(cipher, arrays)
        print("match: ", match)
        cipher = eliminateMatch(cipher, arrays[match])
        print("new cipher: ", cipher)
        key[match] = i+1
    return key
    
# returns an index of the next matching column
def findMatch(cipher, arrays):
    # for array in arrays, but need an index
    for i in range(len(arrays)):
        array = arrays[i]
        isValid = True
        for j in range(len(array)):
            if array[j] != cipher[j]:
                isValid = False
        if isValid:
            return i
    return -1

# returns the cipher with the match removed from the front
def eliminateMatch(cipher, match):
    return cipher[len(match):]
