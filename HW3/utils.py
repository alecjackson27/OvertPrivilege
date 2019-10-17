
# can put any functions you feel the others may want to use here

# takes an array of string digits and returns an integer value
def sum_list(array):
    sum = 0
    for item in array:
        sum += ord(item)
    return sum



def decimalToBinary(deci):
    converted = bin(deci).replace('0b', '')
    while len(converted) < 8:
        converted = '0' + converted
    return converted


def binaryToDecimal(binary):
    decimal, i = 0, 0
    binary2 = int(binary)
    while binary2 != 0:
        dec = binary2 % 10
        decimal = decimal + (dec * pow(2,i))
        binary2 = binary2 // 10
        i += 1
    return decimal


def modularAddition(numList):
    number = 0
    for i in range(1, len(numList)):
        number += numList[len(numList) - i]
    number = (number + 6075380529345458860144577398704761614649) % (10 ** 32)
    for i in range(1, len(numList)):
        numList[len(numList) - i] = number % 10
        number //= 10
    return numList

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

#returns the dot product of two binary numbers, arranged in a list of characters for each byte in the binary digit
def dp(array1, array2):
    product = 0
    for i in array1:
        for j in array2:
            if (i == '1' and j == '1'):
                product += 1
    return product

#returns a final changed array after doing a dot product addition for each element in the 32-size array
def dot_product_sum(array):
    bin_array = []
    for item in array:
        binary = decimalToBinary(item)
        bin_array.append(binaryStrToCharArray(binary))
    for i in range(32):
        current_value = array[i]
        for j in range(32):
            product = dp(bin_array[i], bin_array[j])
            current_value = ((current_value + product) % 256)
            binary = decimalToBinary(current_value)
            bin_array[i] = binaryStrToCharArray(binary)
        array[i] = current_value
    return array

def dot_product_sum_string(string):
    bin_array = []
    newString = ""
    for item in string:
        binary = decimalToBinary(ord(item))
        bin_array.append(binaryStrToCharArray(binary))
    for i in range(len(string)):
        current_value = ord(string[i])
        for j in range(len(string)):
            product = dp(bin_array[i], bin_array[j])
            current_value = ((current_value + product) % 97) + 32
            binary = decimalToBinary(current_value)
            bin_array[i] = binaryStrToCharArray(binary)
        newString += chr(current_value)
    return newString