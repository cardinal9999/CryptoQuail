#CryptoQuail Encryption
"""Encrypt and decrypt strings, bytes, or Python objects.
"""

import string as string_
from warnings import warn
import pickle
import json
import base64
from cryptoquail.util import foobar, errors as exceptions

try:
    import secrets
except ModuleNotFoundError:
    warn("some features may not work because secrets module is not supported")

__all__ = ["encrypt_string", "decrypt_string", "encrypt_bytes", "decrypt_bytes",
           "encrypt_image", "decrypt_image", "encrypt_object", "decrypt_object"]

def encrypt_string(string, key):
    if secrets.compare_digest(key, "") == True or key == None:
        raise exceptions.EmptyKeyError("key must not be a null value")
    int_ = foobar.text2number(key) % 30
    keylist = []
    for i in key:
        keylist.append(ord(i) ^ int_ % 100)
    while len(keylist) < len(string):
        keylist = keylist * 2
    newstring = list(string)
    for i, char in enumerate(newstring):
        newstring[i] = chr(foobar.crypt(ord(char), keylist[i]))
    newstring = newstring[::-1]
    newstring = "".join(newstring)
    str1 = list(newstring)
    return "".join(str1)
def decrypt_string(string, key):
    if secrets.compare_digest(key, "") == True:
        raise exceptions.EmptyKeyError("key must not be a null value")
    str1 = list(string)
    string = "".join(str1)
    int_ = foobar.text2number(key) % 30
    keylist = []
    for i in key:
        keylist.append(ord(i) ^ int_ % 100)
    while len(keylist) < len(string):
        keylist = keylist * 2

    newstring = string[::-1]
    for i, num in enumerate(newstring):
        newstring[i] = foobar.crypt(num, keylist[i])
    newstring = "".join([chr(newstring[i]) for i in range(len(newstring))])
    return newstring

def encrypt_bytes(_bytes, key):
    int_ = foobar.text2number(key) % 30
    keylist = []
    for i in key:
        keylist.append(ord(i) ^ int_ % 42)
    while len(keylist) < len(_bytes):
        keylist = keylist * 2
    newbytes = bytearray(_bytes)
    for i, val in enumerate(newbytes):
        newbytes[i] = foobar.crypt(val, keylist[i])
    return bytes(newbytes)
def decrypt_bytes(_bytes, key):
    int_ = foobar.text2number(key) % 30
    keylist = []
    for i in key:
        keylist.append(ord(i) ^ int_ % 42)
    while len(keylist) < len(_bytes):
        keylist = keylist * 2
    newbytes = bytearray(_bytes)
    for i, val in enumerate(newbytes):
        newbytes[i] = foobar.crypt(val, keylist[i])
    return bytes(newbytes)
def encrypt_object(_object, key):
    if secrets.compare_digest(key, "") == True:
        raise exceptions.EmptyKeyError("key must not be empty")
    bytes_ = pickle.dumps(_object)
    list_ = list(bytes_)
    _str = json.dumps(list_)[::-1]
    _str = encrypt_string(_str, key)
    return _str
def decrypt_object(_string, key):
    if secrets.compare_digest(key, "") == True:
        raise exceptions.EmptyKeyError("key must not be empty")
    string = decrypt_string(_string, key)
    _list = json.loads(string[::-1])
    _bytes = bytes(_list)
    return pickle.loads(_bytes)
def salt(string, key=28):
    """salts a password for storing"""
    saltchar = []
    saltchar.extend(string_.digits)
    saltchar.extend(string_.ascii_letters)
    string = list(string)
    for i in range(key):
        string.append(secrets.choice(saltchar))
    string = "".join(string)
    return string
def unsalt(salted, key=28):
    """unsalts a salted password"""
    salted = list(salted)
    for i in range(key):
        salted.pop(-1)
    unsalted = "".join(salted)
    return unsalted

