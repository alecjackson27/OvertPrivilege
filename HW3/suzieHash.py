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

def suzie_hash(input):
    """
    at this point, input can be string or digits.
    if input is digits, will convert to string
    (transposition stuff is easier with strings)
    """
    if type(input) != "<class 'str'>":
        input = str(input)

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
        bits[i] = sum_list(bits[i])%10
    
    # the remaining column will be used as a key for shuffling the digits
    # if the column contains more than 32 digits
    # use the same make columns/add process
    # if the column contains less than 32 digits
    # add '0's until it is 31 digits long, then tack a '3' at the end
    transposition_key = create_key(bits.pop())
    bits = shuffle_columns(transposition_key, bits)
    return bits

# just for me conveniently testing my code rn
"""
input_text = open("text.txt", 'r')
input_text = input_text.readline()

short_text = open("shortText.txt", 'r')
short_text = short_text.readline()
"""

input_text = input()
print(suzie_hash(input_text))
print(modularAddition(suzie_hash(input_text)))

"""
print(suzie_hash(short_text))
print(modularAddition(suzie_hash(short_text)))
"""