import random
 
p = 269
x = random.randint(1, p - 2)
message_number = input()

def key_generation():
    g = 7
    h = (g ** x) % p
    return h 

def encrypt_number(message, public_key):
    p, g, h = public_key
    k = random.randint(1, p - 2)
    c1 = (g ** k) % p
    c2 = (message_number * h**k ) % p
    return (c1, c2)

def decrypt_number(cipher_text, private_key, p):

    c1, c2 = cipher_text
    s = (c1 ** x) % p
    s_inverse = (s ** -1) % p
    number = (c2 * s_inverse) % p  
    return number
