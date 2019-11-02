# This file will be used to create util functions, such as the hashing and the writing of password and salt to their respective files

import random

def generate_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ""
    for i in range(16):
        salt += random.choice(ALPHABET)
    return salt