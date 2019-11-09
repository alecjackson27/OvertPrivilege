# This file will be used to create util functions, such as the hashing and the writing of 
# password and salt to their respective files

import random
import hashlib

def generate_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ""
    for i in range(16):
        salt += random.choice(ALPHABET)
    return salt

# concatonate the salt to the password
def calculate_hash(password, salt, userID):
    passSalt = password + str(salt)

    shaw1 = hashlib.sha1()
    shaw1.update(passSalt.encode('utf-8'))
    theHash = shaw1.hexdigest()
    combo = userID + " " + theHash
    theFile = open("passwords.txt","a") #not sure if it gets to the file or not
    theFile.write(combo + "\n")
    theFile.close()


#
# TO DO: Write function which takes as parameters a password, salt, and user ID number. The function
# will the calculate the hash of (password + salt) and write the space separated user ID/hash pair
# to the password.txt file with the format: userId hash. Each row of password.txt should be
# a unique userID-hash pair