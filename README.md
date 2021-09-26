# CryptoQuail

![Stars](https://img.shields.io/github/stars/cardinal9999/cryptoquail?style=social) [![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

CryptoQuail's purpose is to extend the quality and features of other Python cryptography modules.
## Why CryptoQuail?
With CryptoQuail, you can encrypt non-built-in objects like Pandas DataFrames.
CryptoQuail's encryption module lets you encrypt strings without a long ciphertext. Some cryptography modules require you to create an object to encrypt and decrypt strings. The extra code can eat some of your bytes in the server's storage. Long ciphertexts can waste even more space in your server. CryptoQuail eliminates most side effects conventional encryptions affect your server.
## Is CryptoQuail Secure?
CryptoQuail uses a XOR cipher to encrypt and decrypt strings, but keys can easily be brute-forced by a supercomputer if the keys isn't long enough. CryptoQuail doesn't solve the key distribution problem, so it's always good to have a program that encrypts the resulting ciphertext with RSA.

CryptoQuail also has a block cipher. You can use it for more secure encryption.
## A list of features
1. XOR Encryption
2. Secure Random Number Generation
3. RSA Encryption
4. A List of Weak Passwords
5. Secure Hashing
6. Prime Number Generation
7. Block Ciphers (new!)
8. Dogescript (unfinished)
## Examples
Encrypt a string:
```py
from cryptoquail import encryption
print(encryption.encrypt_string("strawberry", "secret-key"))

```
## Required Modules
To access the XKCD password generator, you must have requests installed.

## The CryptoQuail Website
Instead of creating a GitHub pages website (which can also eat lots of space in the package), I created some pages in a GitHub wiki.

It has a CryptoQuail tutorial for Python CryptoQuail and CryptoQuail.js.

[Visit the CryptoQuail Wiki](https://github.com/cardinal9999/CryptoQuail/wiki)

```diff
- Warning: When a message is encrypted with Python CryptoQuail, it can not be recovered with CryptoQuail in any other programming language.
```
## Why is it Named "CryptoQuail"?
CryptoQuail was first named "CryptoPigeon", but the name was taken. CryptoQuail was the next best name.
## Bugs and Glitches
CryptoQuail has a lot of bugs. You can help by posting an issue at https://github.com/cardinal9999/CryptoQuail/issues.

