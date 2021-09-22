"""
CryptoQuail block cipher
----------------------------
This cipher increases the security of the cipher by hiding the length of a message.
However, the output will be larger than the original CryptoQuail encryption.
"""
__all__ = ["encrypt", "decrypt"]
from .encryption import encrypt_string as _encrypt, decrypt_string as _decrypt
def encrypt(string, key, block_size):
    ciphertext = []
    for i in range(len(string) // block_size + 1):
        block = ""
        for _ in range(block_size):
            try:
                block = block + string[_ + i * block_size]
            except:
                block = block + chr(8)
        ciphertext.append(_encrypt(block, key))
    return "".join(ciphertext)
def decrypt(string, key, block_size):
    plaintext = []
    for i in range(len(string) // block_size + 1):
        block = ""
        for _ in range(block_size):
             block = block + string[_ + i * block_size]
             block = block.replace(chr(8), "")
        plaintext.append(_decrypt(block, key))
    return "".join(plaintext)
