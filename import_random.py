import random
 
def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime(start, end):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

def find_prime_factors(n):
    """Find all prime factors of a number."""
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def find_primitive_root(p):
    """Find a primitive root modulo p."""
    if p == 2:
        return 1
    phi = p - 1
    factors = find_prime_factors(phi)
    for g in range(2, p):
        is_primitive = True
        for factor in factors:
            if pow(g, phi // factor, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g

def key_generation(g, x, p):
    h = (g ** x) % p
    return h 

def encrypt_number(message, public_key):
    p, g, h = public_key
    k = random.randint(1, p - 2)
    c1 = (g ** k) % p
    c2 = (message * h**k ) % p
    return (c1, c2)

def decrypt_number(cipher_text, private_key, p):

    c1, c2 = cipher_text
    s = (c1 ** x) % p
    s_inverse = pow(s,-1,p)
    number = (c2 * s_inverse) % p  
    return number

# Generate initial prime, generator, and keys
p = generate_random_prime(100, 1000)
g = find_primitive_root(p)
x = random.randint(1, p - 2)
h = key_generation(g, x, p)
public_key = (p, g, h)
private_key = x

print(f"Prime (p): {p}")
print(f"Generator (g): {g}")
print(f"Public Key (h): {h}")
print(f"Private Key (x): {private_key}")

# Main menu
while True:
    print("\nElGamal Cryptography Application")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            # Encryption process
            try:
                message_number = int(input("Enter the message number to encrypt: "))

                if message_number < 0:
                    print("Error: Negative numbers are not allowed, Please enter a positive number.")
                    continue

                # Regenerate keys if the message exceeds the current prime field
                if message_number >= p:
                    print("Message is too large. Generating a larger prime number.")
                    p = generate_random_prime(message_number + 10, message_number + 100)
                    g = find_primitive_root(p)
                    x = random.randint(1, p - 2)
                    h = key_generation(g, x, p)
                    public_key = (p, g, h)
                    private_key = x
                    print(f"New Prime (p): {p}")
                    print(f"New Generator (g): {g}")
                    print(f"New Public Key (h): {h}")
                    print(f"New Private Key (x): {private_key}")

                cipher_text = encrypt_number(message_number, public_key)
                print(f"Ciphertext: {cipher_text}")
            except Exception as e:  # Sets any errors as "e"
                print("Error:", e)  # Displays the error message

        elif choice == '2':
        # Decryption process
            try:
                c1 = int(input("Enter ciphertext part 1 (c1): "))
                c2 = int(input("Enter ciphertext part 2 (c2): "))

                if c1 < 0 or c2 < 0:
                    print("Error: Negative numbers are not allowed in ciphertext, Please enter positive numbers.")
                    continue

                cipher_text = (c1, c2)

                decrypted_message = decrypt_number(cipher_text, private_key, p)
                print(f"Decrypted Message: {decrypted_message}")
            except Exception as e: #Sets any errors as "e"
                print("Error:", e) #Displays the error message

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")