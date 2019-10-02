from random import randint, randrange, getrandbits

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
        a = randrange(2, n - 1)
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
    p = getrandbits(1024)
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
    n = randint(2, 3317044064679887385961813)
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
