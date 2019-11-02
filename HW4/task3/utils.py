# This file will be used to create util functions, such as the hashing and the writing of 
# password and salt to their respective files

import random

def generate_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ""
    for i in range(16):
        salt += random.choice(ALPHABET)
    return salt

# TO DO: Write function which takes as parameters a password, salt, and user ID number. The function
# will the calculate the hash of (password + salt) and write the space separated user ID/hash pair
# to the password.txt file with the format: userId hash. Each row of password.txt should be
# a unique userID-hash pair