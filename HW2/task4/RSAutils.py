import random
import os
import sys
from decimal import Decimal

#Set recursion limit to 10 ^ 6 since the program works with such large numbers
sys.setrecursionlimit(1000000)

#
# Helper function called by generatePrime() to check for primality.uses Miller-Rabin test,
# a probabilistic method to determine whether a number is prime with near-certainty.
# Information on Miller-Rabin and pseudocode found at:
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
#
def isPrime(n):
    # 2 and 3 are prime
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find d and r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # run 100 tests
    for i in range(100):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < r and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

#
# Generates a potential prime number. Helper function called by generatePrime()
#
def generatePotentialPrime():
    # generate random 1024-bit number
    p = random.getrandbits(1024)
    # If p is even, add 1, so as to not waste time checking for primality of even number
    if p % 2 == 0:
        p += 1
    return p

#
# Generates a number which is almost certaintly prime. The probability of the number not
# being prime is significantly smaller than that of program failure due to a hardware
# malfunction
#
def generatePrime():
    # Generate potential prime number
    n = generatePotentialPrime()
    # keep generating potential candidates while the Miller-Rabin test fails
    while not isPrime(n):
        n = generatePotentialPrime()
    return n

#
# This function generates a prime number using a deterministic variant of the Miller Test
# which limits the size of the numbers it can generate, but ensures with 100% certainty that
# the number is prime. More information about the deterministic version of the Miller-Rabin
# test can be found at:
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants
#  
def isDefinitelyPrime(n):
    tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    # 2 and 3 are prime
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find d and r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for a in tests:
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < r and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generateDeterministicPrime():
    # generate a random number from 2 to 3317044064679887385961813. This number was chosen
    # because it is the largest prime number less than 3317044064679887385961981, which is
    # the smallest composite number for which the above isDefPrime function will return a
    # false positive. This was determined by running the commented-out script below this
    # function. After generating the number, while it is not prime, add 1 to number
    n = random.randint(2, 3317044064679887385961813)
    while not isDefinitelyPrime(n):
        n += 1
    return n

# This script was used to determine the largest prime less than 3317044064679887385961981
"""
n = 3317044064679887385961980
while not isDefinitelyPrime(n):
    n -= 1
print(n)
"""

# greatest common denominator between two integers
# used to find P_E (public encryption exponent) for public key
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# helper function for modinv
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Returns the modular inverse D using extended euclid's algorithm
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# generates both private key and public key
# returns a tuple (public key, private key)
def key_gen(p, q):
	# n is the mod for the RSA algorithm, and is included in both keys
    n = p * q
    print("P", p)
    print("Q", q)

	# phi is f(n), and is used to find both P_E (public encryption exponent) and P_D (private decryption exponent)
    phi = (p-1)*(q-1)
    print("Phi:", phi)

	# find any number e such that e is coprime with phi
    e = random.randrange(1,phi)
    g = gcd(e, phi)
    while g != 1:
	    e = random.randrange(1, phi)
	    g = gcd(e, phi)

	# d represents P_D (private decryption exponent)
	# find d such that (d*e)%phi = 1
    d = modinv(e, phi)

	#keys in tuple form. ((public encryption exponent,modulus),(private decryption exponent,modulus))
    return ((e,n),(d,n))

def encrypt(key, x):
    """Encrypt the number ``x``.

    The result is a number which can be decrypted only using the
    private key.
    """
    e, n = key
    return pow(x, e, n)

def decrypt(key, cipher):
	"""Decrypt the cipher.

    The result is the original plaintext
    """
	d, n = key
	return pow(cipher, d, n)

# takes an input of plain text numbers separated by spaces, as one string, reading public key given the file location as pub_key
def encryption(input_string, pub_key):
	file = open(pub_key, 'r')
	if file.mode != 'r':
		return 'The key has not yet been generated. Please generate a key before encrypting.'
	keys = file.read().split()
	key = (int(keys[0]),int(keys[1]))

	n = input_string.split()
	ciphertext = ''
	for i in n:
		plaintext = int(i)
		cipher = encrypt(key,plaintext)
		ciphertext+=str(cipher)
		ciphertext+=' '
	return ciphertext

# takes an input of ciphers separated by spaces, as one string, reading private key given the file location as priv_key
def decryption(input_string, priv_key):
	file = open(priv_key, 'r')
	if file.mode != 'r':
		return 'The key has not yet been generated. Please generate a key before decrypting.'
	keys = file.read().split()
	key = (int(keys[0]),int(keys[1]))

	ciphers = input_string.split()
	plaintext = ''
	for x in ciphers:
		c = int(x)
		p = decrypt(key,c)
		plaintext += str(p)
		plaintext += ' '
	return plaintext

# generates keys and outputs public key and private key in a specified file location
def key_generator(file_save_location, deterministic=False):
    if deterministic:
        p = generateDeterministicPrime()
        q = generateDeterministicPrime()
        while p == q:
            q = generateDeterministicPrime()
    else:
        p = generatePrime()
        q = generatePrime()
        while p == q:
            q = generatePrime()

    

    pub_key, priv_key = key_gen(p,q)
    pub_key_file = open(file_save_location + os.path.sep + 'public.key', 'w+')
    priv_key_file = open(file_save_location + os.path.sep + 'private.key', 'w+')

    pub_key_file.write(str(pub_key[0]) + ' ' + str(pub_key[1]))
    priv_key_file.write(str(priv_key[0]) + ' ' + str(priv_key[1]))

    pub_key_file.close()
    priv_key_file.close()
