
from utils import *

# Outlining the program so we can just assign ourself parts of it

def encrypt():
    # acquire key and plaintext
    key = input("Enter the key: ")
    plain_text = input("Enter the message you would like encoded: ")

    # process key into part for polybius and one-time pad
    poly_key = getPolyKey(key)
    pad_key = getPadKey(key)

    # use polybius square to get key for columnar transposition
    col_key = cipherToValPoly(poly_key)

    # encrypt plaintext with columnar transposition, no padding (result is cipher1)
    
    
    # use polybius square to find numerical representation for each letter in cipher1
    # convert each of these numbers from decimal to 6-bit binary
    # convert one-time-pad value from decimal to 6-bit binary
    # use one-time pad using previous values
    # convert resulting cipher from 6-bit binary to decimal
    # return the decimal number to the user as the completed ciphertext

def decrypt():
    # acquire key and ciphertext
    key = input("Enter the key: ")
    cipher_text = input("Enter the message you would like decoded: ")

    # process key into part for polybius and one-time pad
    poly_key = getPolyKey(key)
    pad_key = getPadKey(key)

    # convert ciphertext from decimal to 6-bit binary
    # convert one-time pad value from decimal to 6-bit binary
    # do a one-time pad with previous values
    # convert 6-bit binary to decimal (should all be 2 digit values)
    # use polybius square on created decimal values, get letters
    # use polybius square to get key for columnar transposition
    # reverse columnar transposition using values from previous two steps
    # return plaintext to user

# prompt for user input
# user may want to encrypt or decrypt a message
cryption = input("Do you want to encrypt or decrypt?(E/d): ")
while cryption not in { 'E', 'e', 'D', 'd', 'Q', 'q' }:
    cryption = input("Invalid input. Type 'E' if you wish to encrypt and 'D' if you wish to decrypt. Type 'Q' to quit: ")

if cryption not in { 'Q', 'q' }:
    if cryption in { 'E', 'e' }:
        encrypt()
    elif cryption in { 'D', 'd' }:
        decrypt()
    else:
        print("Something has gone terribly wrong")


# Required functions are written in a different file, utils.py