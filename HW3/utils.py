# can put any functions you feel the others may want to use here

# takes an array of string digits and returns an integer value
def sum_list(array):
    sum = 0
    for item in array:
        sum += int(item)
    return sum

# Function that converts an 8 bit binary string to a char array of 1's and 0's
def binaryStrToCharArray(binary):
    chars = []
    if len(binary) == 8:
        for i in range(len(binary)):
            chars.append(binary[i])
    else:
        print("The given string is too large")
    return chars
# want to return an array






