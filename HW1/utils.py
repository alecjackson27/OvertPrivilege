# Functions necessary
# process key into polybius part and one-time pad
def getPolyKey(key):
    return key[:(len(key)-2)]

def getPadKey(key):
    return key[(len(key)-2):]

# one-time pad, exclusive OR with key and value
# given cipher, get value out of polybius square
# given values, get cipher out of polybius square
#   may want two maps, one where the key is the two-digit key, another where the key is the value
#   whoever writes that part can decide what they want to do
# convert from 6-bit binary to decimal
# convert from decimal to 6-bit binary
#   maybe there's a library function for that, but 6 bit is weird so I'm not gonna go looking. If you just know one, use it.
