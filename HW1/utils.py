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

valueToKeyPolySquare = {'E':'00', '2':'01', 'R':'02', 'F':'03', 'Z':'04', 'M':'05'}
valueToKeyPolySquare.update({'Y':'10', 'H':'11', '3':'12', 'O':'13', 'B':'14', '7':'15'})
valueToKeyPolySquare.update({'O':'20', 'Q':'21', 'A':'22', 'N':'23', 'U':'24', 'K':'25'})
valueToKeyPolySquare.update({'P':'30', 'X':'31', 'J':'32', '4':'33', 'V':'34', 'W':'35'})
valueToKeyPolySquare.update({'D':'40', '1':'41', '8':'42', 'G':'43', 'C':'44', '6':'45'})
valueToKeyPolySquare.update({'9':'50', 'I':'51', 'S':'52', '5':'53', 'T':'54', 'L':'55'})



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

#turn the key retrieved from cipherToValPoly into a cipher that can be encrypted.
def columnKeyToCipher(key,plainText):
    tempKey = key

    orderArray = []

    while len(tempKey) > 0:
        temp = min(tempKey)
        j = 0
        for j in range(len(key)):
            if key[j] == temp:
                orderArray.append(j);
        tempKey = tempKey.replace(temp, '')

    cipherList = []
    for i in range(len(key)):
        cipherList.append([])
    
    plainText = plainText.replace(' ', '')
    plainText = plainText.upper()
    for i in range(len(plainText)):
        cipherList[orderArray[i%len(key)]].append(plainText[i])
    
    cipher1 = ''
    for i in range(len(cipherList)):
        for j in range(len(cipherList[i])):
            cipher1 += cipherList[i][j]
    return cipher1


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

def cipher1ToCipher2(cipher1, padKey):
    cipher2 = ""
    padKey = decimalToBinary(int(padKey))

    for i in range(0, len(cipher1)):
        temp = valueToKeyPolySquare.get(cipher1[i])
        temp2 = decimalToBinary(int(temp))
        temp3 = ""
        for j in range(len(temp2)):
            temp3 += str(int(padKey[j]) ^ int(temp2[j]))
        cipher2 += str(binaryToDecimal(temp3))
    return cipher2
