
from utils import *

# Outlining the program so we can just assign ourself parts of it

# prompt for user input
# user may want to encrypt or decrypt a message
cryption = input("Do you want to encrypt or decrypt?(E/d): ")
while cryption not in { 'E', 'e', 'D', 'd', 'Q', 'q' }:
    cryption = input("Invalid input. Type 'E' if you wish to encrypt and 'D' if you wish to decrypt. Type 'Q' to quit: ")

if cryption not in { 'Q', 'q' }:
    key = input("Enter the key: ")
    if cryption in { 'E', 'e' }:
        #Ecrypt
        plaintext = input("Enter the plaintext: ")

# steps to deal with encryption
# acquire key and plaintext
# process key into part for polybius and one-time pad
# use polybius square to get key for columnar transposition
# encrypt plaintext with columnar transposition, no padding (result is cipher1)
# use polybius square to find numerical representation for each letter in cipher1
# convert each of these numbers from decimal to 6-bit binary
# convert one-time-pad value from decimal to 6-bit binary
# use one-time pad using previous values
# convert resulting cipher from 6-bit binary to decimal
# return the decimal number to the user as the completed ciphertext

    else:
        #Decrypt
        ciphertext = input("Enter the ciphertext: ")

# steps to deal with encryption
# acquire key and plaintext
# process key into part for polybius and one-time pad
# use polybius square to get key for columnar transposition
# encrypt plaintext with columnar transposition, no padding (result is cipher1)
# use polybius square to find numerical representation for each letter in cipher1
# convert each of these numbers from decimal to 6-bit binary
# convert one-time-pad value from decimal to 6-bit binary
# use one-time pad using previous values
# convert resulting cipher from 6-bit binary to decimal
# return the decimal number to the user as the completed ciphertext

# steps to deal with decryption
# acquire key and ciphertext
# process key into part for polybius and one-time pad
# convert ciphertext from decimal to 6-bit binary
# convert one-time pad value from decimal to 6-bit binary
# do a one-time pad with previous values
# convert 6-bit binary to decimal (should all be 2 digit values)
# use polybius square on created decimal values, get letters
# use polybius square to get key for columnar transposition
# reverse columnar transposition using values from previous two steps
# return plaintext to user

    # use polybius square to get key for columnar transposition
    # encrypt plaintext with columnar transposition, no padding (result is cipher1)
    # use polybius square to find numerical representation for each letter in cipher1
    # convert each of these numbers from decimal to 6-bit binary
    # convert one-time-pad value from decimal to 6-bit binary
    # use one-time pad using previous values
    # convert resulting cipher from 6-bit binary to decimal
    # return the decimal number to the user as the completed ciphertext
# decrypting
elif not what_crypt:
    # acquire key and ciphertext
    cipher_text = input("Please enter the message you would like decoded: ")
    key = input("Please enter the key: ")

    # process key into part for polybius and one-time pad
    # convert ciphertext from decimal to 6-bit binary
    # convert one-time pad value from decimal to 6-bit binary
    # do a one-time pad with previous values
    # convert 6-bit binary to decimal (should all be 2 digit values)
    # use polybius square on created decimal values, get letters
    # use polybius square to get key for columnar transposition
    # reverse columnar transposition using values from previous two steps
    # return plaintext to user
else:
    print("good job, you broke the program")



# Required functions are written in a different file, utils.py