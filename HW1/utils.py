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
    
    keyLetters = []
    emptyLists = []
    #dictionaries can't have the same key but there may be letters that are the same in the code...
    for i in range(len(key)):
        keyLetters[i] = key[i] #I think this adds all the letters in Key to the list...
        emptyLists[i] = []

    scramble = {} #empty dict for initialization?

    for i in range(len(key)):#fill the dictionary with letters from whatever word is made using parallel lists method
        if keyLetters[i] in scramble: #letter already exists in dict
            keyletters[i] = keyletters[i] + i
            #then concatonate a number to the letter so it is a unique key but still has the right letter
            scramble[keyLetters[i]] = emptyLists[i]
        else
            scramble[keyLetters[i]] = emptyLists[i]

    #divide up the plaintext letters into columns
    #cycle = 0
    keyWord = ''
    for i in range(len(plainText)): #does it start at 0 in python?
        #if (i % len(key)) = 0: 
            #cycle++
        keyWord = keyletters[i % len(key)]
        scramble.get(keyWord).append(plaintext[i]) #I think this adds to the list value in the dictionary

    #sort the dictionary so that it is easier to concatonate the lists of strings
    sortedKeys = sorted(scramble,key=str.lower)


    cipher = ''

    #NOT SURE HOW TO CHECK IF THERE ARE 3+ of the same letter....
    for i in range(len(scramble)):
        #means it is the same letter and we need to combine those string lists differently
        if len(sortedKeys[i+1]) > 1: #I want to access the first letter of the string in the list in the next index
            cipher += horizontalCombo(scramble,sortedKeys,countLetterFreq(sortedKeys,i),i)#the list the dict and number scramble.get(sortedKeys[i]),scramble.get(sortedKeys[i+1]
        else
            cipher += concatonateList(scramble,sortedKeys,i)

    return cipher
    
def countLetterFreq(list,index):
    count = 1 #starting with the letter that is original
    for index in range(len(list)):
        if len(list[index+1]) > 1:
            count ++
        else
            return count

#if only one of that letter in the key then concatonate its list into a string 
def concatonateList(dict,keylist,index):
    combo = ''
    letterScramble = dict.get(keyList[index]) #the desired list in our dictionary
    for i in range(len(letterScramble)):
        combo += letterScramble[i]
    return combo

#if multiple of the same letter then concatonate it differently
def horizontalCombo(dict,keyList,count,index):
    combo = ''
    for i in range(len(dict.get(keyList[index])))
        for j in count: #I think this is correct but might need to check the count
            combo += dict.get(keyList[index+j])
    return combo

def cipher1ToNumPoly(cipher1):
    cipher2 = ""
    for i in range(0, len(cipher1)-1):
        cipher2 += valueToKeyPolySquare.get(cipher1[i])
    return cipher2


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
