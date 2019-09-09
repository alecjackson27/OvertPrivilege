# Functions necessary
# process key into polybius part and one-time pad
def getPolyKey(key):
    return key[:(len(key)-2)]

def getPadKey(key):
    return key[(len(key)-2):]

# one-time pad, exclusive OR with key and value
# given cipher (edge numbers), get value (inside numbers/letters) out of polybius square
# given values (inside numbers/letters), get cipher (edge numbers) out of polybius square
#   may want two maps, one where the key is the two-digit key, another where the key is the value?
#   whoever writes that part can decide what they want to do
keyToValuePolySquare = {'00':'E', '01':'2', '02':'R', '03':'F', '04':'Z', '05':'M'}
keyToValuePolySquare.update({'10':'Y', '11':'H', '12':'3', '13':'0', '14':'B', '15':'7'})
keyToValuePolySquare.update({'20':'O', '21':'Q', '22':'A', '23':'N', '24':'U', '25':'K'})
keyToValuePolySquare.update({'30':'P', '31':'X', '32':'J', '33':'4', '34':'V', '35':'W'})
keyToValuePolySquare.update({'40':'D', '41':'1', '42':'8', '43':'G', '44':'C', '45':'6'})
keyToValuePolySquare.update({'50':'9', '51':'I', '52':'S', '53':'5', '54':'T', '55':'L'})

def cipherToValPoly(cipher):
    # take two digits at a time, use as key in dict, add result to result string, return when cipher is used up
    start_i = 0
    end_i = 2
    end = len(cipher)
    retVal = ''
    while end_i <= end:
        retVal += keyToValuePolySquare.get(cipher[start_i:end_i])
        start_i += 2
        end_i += 2
    return retVal

# convert from 6-bit binary to decimal
# convert from decimal to 6-bit binary
def decimalToBinary(deci):
    converted = bin(deci).replace('0b', '')
    while len(converted) < 6:
        converted = '0' + converted
    return converted

def binaryToDecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + (dec * pow(2,i))
        binary = binary // 10
        i += 1
    return decimal