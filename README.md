# CryptoQuail
CryptoQuail's purpose is to extend the quality and features of other Python cryptography modules.
## Why CryptoQuail?
With CryptoQuail, you can encrypt non-built-in objects like Pandas DataFrames.
CryptoQuail's encryption module lets you encrypt strings without a long ciphertext. Some cryptography modules need you to create an object to encrypt and decrypt strings. The extra code can eat some of your bytes in the server's storage. Long ciphertexts can waste even more space in your server. CryptoQuail eliminates most side effects conventional encryption creates on your server.
## Is CryptoQuail Secure?
CryptoQuail uses a XOR cipher to encrypt and decrypt strings, but keys can easily be brute-forced by a supercomputer if the keys isn't long enough. CryptoQuail doesn't solve the key distribution problem, so it's always good to have a program that encrypts the resulting ciphertext with RSA.
## A list of features
1. XOR Encryption
2. Secure Random Number Generation
3. RSA Encryption
4. A List of Weak Passwords
## Examples
Encrypt a string:
```
from cryptoquail import encryption
print(encryption.encrypt_string("strawberry", "secret-key"))

```

## How CryptoQuail Helps Bobwhites
CryptoQuail helps endangered birds like Bobwhite Quails by donating to the National Bobwhite Conservation Initiative whenever a CryptoQuail application is downloaded.
## Why is it Named "CryptoQuail"?
CryptoQuail was first named "CryptoPigeon", but the name was taken. CryptoQuail was the next best name.
