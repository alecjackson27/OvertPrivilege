# can put any functions you feel the others may want to use here

# takes an array of string digits and returns an integer value
def sum_list(array):
    sum = 0
    for item in array:
        sum += int(item)
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
