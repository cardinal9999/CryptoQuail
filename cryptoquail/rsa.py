#CryptoQuail RSA
"""Encrypts with the RSA cipher."""
    
def generate_d(p, q, e):
    """Generates the value of d for decryption."""
    J = (p-1)*(q-1)
    a = 0
    while (e * a) % J != 1:
        a += 1
    return a
def encrypt(m, n, e):
    return (m ** e) % n
def decrypt(c, n, d):
    return (c**n) % d
