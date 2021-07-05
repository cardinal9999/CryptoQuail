#CryptoQuail RSA
"""
Encrypts with the RSA cipher.
Generate keys:
https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html
Factor a number:
https://www.calculatorsoup.com/calculators/math/prime-factors.php
"""
    
def encrypt(number, encryption_key, public_key):
    f = public_key
    e = encryption_key
    c = number ** e % f
    return c
def decrypt(ciphertext, decryption_key, prime_numbers):
    public_keys = prime_numbers
    p = public_keys[0]
    q = public_keys[1]
    f = p-1 * q-1
    d = decryption_key
    m = (ciphertext ** d) % f 
    return m
