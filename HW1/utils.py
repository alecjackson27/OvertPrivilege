import math

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

# given a key, gives the order array for columnar transposition. Will be used for encrypting and decrypting
def inverseOrderArray(key):
    tempList = []

    tempKey = key
    while len(tempKey) > 0:
        temp = min(tempKey)
        j = 0
        for j in range(len(key)):
            if key[j] == temp:
                tempList.append(j);
        tempKey = tempKey.replace(temp, '')
    orderArray = [0] * len(key)
    for i in range(len(key)):
        orderArray[tempList[i]] = i
    return orderArray
    

#turn the key retrieved from cipherToValPoly into a cipher that can be encrypted.
def columnKeyToCipher(key, plainText):
    orderArray = inverseOrderArray(key)

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

"""
def cipher1ToPlainText(key, cipher1):
    orderArray = inverseOrderArray(key)
    print(cipher1)
    print(key)
    
    cipherList = []
    for i in range(len(key)):
        cipherList.append([])
    
    cipher1 = cipher1.replace(' ', '')
    cipher1 = cipher1.upper()


    plain_text = ''
    if len(cipher1) % len(key) == 0:
        for i in range(len(key)):
            for j in range(len(cipher1) // len(key)):
                cipherList[i].append(cipher1[i*len(cipher1)//len(key)+j])
        for i in range(len(cipher1)//len(key)):
            for j in range(len(key)):
                plain_text += cipherList[j][i]
    else:
        count = 0;
        for i in range(len(key)):
            if i < len(cipher1) % len(key):
                for j in range(len(cipher1) // len(key) + 1):
                    print("j: ", j)
                    #print("shorter: ", cipher1[count])
                    cipherList[i].append(cipher1[count])
                    count += 1
            else:
    
                for j in range(len(cipher1) // len(key)):
                    print("j: ", j)
                    #print("longer: ", cipher1[count])
                    cipherList[i].append(cipher1[count])
                    count += 1
        for i in range(len(cipherList)):
            for j in range(len(cipherList[i])):
                print(cipherList[i][j])
        row = 0        
        for i in range(len(cipher1)):
            if i > 0 and i % len(key) == 0:
                row += 1
            #print("row: ", row)
            #print("column: ", i%len(key))
            #print(cipherList[i%len(key)][row])
            plain_text += cipherList[i%len(key)][row]
       
    #plain_text = plain_text.replace('$', '')
    return plain_text
"""

#take a cipher text and reposition it back to its original message
def untransposeTextByColumn(key, cipher):
    col = len(key)

    #find out how many letters from the cipher will be with each column from the key (they are each different because there is no padding))
    letters_per_char = len(cipher) // len(key) #each column will have at least <letters_per_char> letters
    leftovers = len(cipher) % len(key) #the first <leftovers> columns will have 1 extra letter

    key_list = list(key)

    #join the number of letters each column will have with the associated letters from the key
    numbers_list = []
    for i in range(col):
        numbers_list.append(letters_per_char)
    for i in range(leftovers):
        numbers_list[i] += 1;

    #sort the columns back to alphabetical order to determine the block sizes from the cipher (again, different because there is no padding)
    key_numbers = list(zip(key_list,numbers_list))
    key_numbers.sort(key = lambda x: x[0])

    #remove the correct amount of letters from the cipher and arrange them into the correct amounts per column
    start_i = 0
    end_i = 0
    cipher_divide = []
    for i in key_numbers:
        end_i += int(i[1])
        cipher_divide.append(cipher[start_i:end_i])
        start_i += int(i[1])
       
    #take the new columns of letters from the cipher and put them in their associated columns with the key
    key_ordered = sorted(key)
    arranged_cipher = list(zip(key_ordered,cipher_divide))

    #put the columns back in the order to put the key letters back in place with the associated columns moving as well
    ordered_arranged_cipher = []
    for i in key:
        for j in arranged_cipher:
            if i == j[0]:
                ordered_arranged_cipher.append(j)
                arranged_cipher.remove(j)
                break

    #take the letters from each column and put them back in the original message
    message = ''
    for i in range(letters_per_char+1):
        for j in ordered_arranged_cipher:
            if i < len(j[1]):
                message += j[1][i]


    return message
# convert from 6-bit binary to decimal
# convert from decimal to 6-bit binary
def decimalToBinary(deci):
    converted = bin(deci).replace('0b', '')
    while len(converted) < 6:
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


# converts cipher1 to the final cipher
def cipher1ToCipher2(cipher1, padKey):
    cipher2 = ""
    padKey = decimalToBinary(int(padKey))

    for i in range(0, len(cipher1)):
        temp = valueToKeyPolySquare.get(cipher1[i])
        temp = decimalToBinary(int(temp))
        temp2 = ""
        for j in range(len(temp)):
            temp2 += str(int(padKey[j]) ^ int(temp[j]))
        temp2 = str(binaryToDecimal(temp2))
        if len(temp2) < 2:
            temp2 = '0' + temp2
        cipher2 += temp2
    return cipher2

# converts final cipher to cipher1
def cipher2ToCipher1(cipher2, padKey):
    cipher1 = ""
    padKey = decimalToBinary(int(padKey))

    length = len(cipher2)
    for i in range(length//2):
        temp = cipher2[:2]
        temp = decimalToBinary(int(temp))
        temp2 = ""
        for j in range(len(temp)):
            temp2 += str(int(padKey[j]) ^ int(temp[j]))
        temp2 = str(binaryToDecimal(temp2))
        if len(temp2) < 2:
            temp2 = '0' + temp2
        temp2 = keyToValuePolySquare.get(temp2)
        cipher1 += temp2
        cipher2 = cipher2[2:]
    return cipher1
