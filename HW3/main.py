from utils import *

# takes a variable-sized input
# makes 33 columns
# adds the first 32 columns together, take the digit in ones place, get a 32 bit output
# the last column is used to create a key
# that key is used to shuffle the columns
# key only contains digits 0-9, first 0 goes before second 0, etc.

def create_key(array):
    # if the array is too long, make it exactly 32 bits
    if len(array) > 32:
        arrays = []
        for i in range(32):
            arrays.append([])
        for i in range(len(array)):
            index = i % 32
            arrays[index].append(array[i])
        for i in range(32):
            arrays[i] = sum_list(arrays[i])%10
        array = arrays
    else:
        while len(array) < 31:
            array.append('0')
        array.append('3')
    for i in range(len(array)):
        if type(array[i]) != "<class 'str'>":
            array[i] = ord(array[i])
        else:
            array[i] = int(array[i])
    return array

def shuffle_columns(key, orig):
    pairs = []
    for i in range(len(key)):
        pairs.append((key[i], orig[i]))
    pairs.sort(key=lambda x: x[0])
    newOrdered = []
    for i in range(len(pairs)):
        newOrdered.append(pairs[i][1])
    return newOrdered

def input_hash(input):
    """
    at this point, input can be string or digits.
    if input is digits, will convert to string
    (transposition stuff is easier with strings)
    """
    if type(input) != "<class 'str'>":
        input = str(input)

    input = dot_product_sum_string(input)

    # initialize the arrays
    bits = []
    for i in range(33):
        bits.append([])
    

    # add elements to array
    for i in range(len(input)):
        index = i % 33
        bits[index].append(input[i])

    # add together all elements of first 32 columns and take ones digit
    for i in range(32):
        if sum_list(bits[i]) % 10 !=  0:
            bits[i] = sum_list(bits[i])%10
        else:
            numToAdd = 0
            for j in range(i):
                numToAdd = ((numToAdd + bits[j] + j)) % 10
            bits[i] = numToAdd
    
    # the remaining column will be used as a key for shuffling the digits
    # if the column contains more than 32 digits
    # use the same make columns/add process
    # if the column contains less than 32 digits
    # add '0's until it is 31 digits long, then tack a '3' at the end
    transposition_key = create_key(bits.pop())
    bits = shuffle_columns(transposition_key, bits)
    return bits


def decimalToHex(number):
    if number < 10:
        return str(number)
    if number == 10:
        return 'a'
    if number == 11:
        return 'b'
    if number == 12:
        return 'c'
    if number == 13:
        return 'd'
    if number == 14:
        return 'e'
    if number == 15:
        return 'f'
    return 'invalid number'


if __name__ == "__main__":
    input_text = input("Enter the input you wish to hash: ")
    hashArray = input_hash(input_text)
    #hashArray = modularAddition(hashArray)
    #print("modular hash:", hashArray)
    #hashArray = shuffle_columns(hashArray, key)
    #print("shuffled:", hashArray)
    hashArray = dot_product_sum(hashArray)
    hashString = ""
    for x in hashArray:
        hashString += decimalToHex(x%16)
    print(hashString)