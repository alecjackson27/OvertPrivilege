import random
import os

# greatest common denominator between two integers
# used to find P_E (public encryption exponent) for public key
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# generates both private key and public key
# returns a tuple (public key, private key)
def key_gen(p, q):
	# n is the mod for the RSA algorithm, and is included in both keys
	n = p * q

	# phi is f(n), and is used to find both P_E (public encryption exponent) and P_D (private decryption exponent)
	phi = (p-1)*(q-1)

	# find any number e such that e is coprime with phi
	e = random.randrange(1,phi)
	g = gcd(e, phi)
	while g != 1:
		e = random.randrange(1, phi)
		g = gcd(e, phi)

	# d represents P_D (private decryption exponent)
	# find d such that (d*e)%phi = 1
	for d in range(3, phi, 2):
		if (d*e)%phi == 1:
			break

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
def key_generator(file_save_location):
	'''
	p = generate_prime()
	q = generate_prime()
	while q != p:
		q = generate_prime()
	'''
	p=677
	q=2939

	pub_key, priv_key = key_gen(p,q)
	pub_key_file = open(file_save_location + os.path.sep + 'RSA_public_key.txt', 'w+')
	priv_key_file = open(file_save_location + os.path.sep + 'RSA_private_key.txt', 'w+')

	pub_key_file.write(str(pub_key[0]) + ' ' + str(pub_key[1]))
	priv_key_file.write(str(priv_key[0]) + ' ' + str(priv_key[1]))

	pub_key_file.close()
	priv_key_file.close()

	




