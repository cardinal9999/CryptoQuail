#CryptoQuail RSA
"""
Encrypts with the RSA cipher.
Generate keys:
https://www.cs.drexel.edu/~jpopyack/IntroCS/HW/RSAWorksheet.html
Factor a number:
https://www.calculatorsoup.com/calculators/math/prime-factors.php
"""
    
def generate_d(p, q, e):
    J = (p-1)*(q-1)
    a = 0
    while (e * a) % J != 1:
        a += 1
    return a
def encrypt(m, n, e):
    return (m ** e) % n
def decrypt(c, d, n):
    return (c**d) % n
