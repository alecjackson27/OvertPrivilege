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
    for i in range(len(numList)):
        number += numList[len(numList) - 1 - i] * 10 ** i
    number = (number + 6075380529345458860144577398704761614649) % (10 ** 31)
    for i in range(1, len(numList) + 1):
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

