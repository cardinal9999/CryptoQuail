#CryptoQuail SecureRandom
"""Generates secure randomness for cryptographic purposes
Randomness are from the operating system instead of mathmatical formula"""

import string as string_
from warnings import warn
from os import urandom as token_bytes
from random import seed, randint as randint_, shuffle as shuffle_
import random

__all__ = ["password", "token_hex", "randbelow", "shuffle", "choice", "randint",
           "token_bytes", "randbool", "token_alphanumeric",  "xkcd"]
global using_csprng
using_csprng = 1
try:
    import secrets
except ModuleNotFoundError:
    warn("Your Python compiler doesn't support secure PRNGs. CryptoQuail will use insecure random generators instead.")
    using_csprng -= 1

def toggle_security(num):
    global using_csprng
    using_csprng = num
if using_csprng == 1:
    randbelow = secrets.randbelow
    choice = secrets.choice
else:
    def randbelow(limit):
        return random.randint(0, limit)
    def choice(seq):
        return random.choice(seq)
class SecretsObj(object):
    def __init__(self):
        self.hack = 0
    def token_hex(len2):
        a = []
        for i in range(len2 * 2):
            a.append(random.choice("abcdef1234567890"))
        return "".join(a)
if using_csprng == 0:
    secrets = SecretsObj


def password(length):
    randchar = list()
    m = []
    m += list(string_.ascii_letters)
    m += list(string_.digits)
    m += list("!@#$%^&*?.")
    for _ in range(length):
        randchar.append(choice(m))
    return "".join(randchar)
def token_hex(nbytes=32):
    return secrets.token_hex(nbytes)
def randint(a, b):
    """random number between a and b"""
    seed_0 = randbelow(999999) + 5555
    seed_1 = randbelow(999999) + 5555
    seed(seed_0 * seed_1)
    return randint_(a, b)
def shuffle(iterable):
    """shuffles an iterable"""
    seed_2 = randbelow(999999) + 5555
    seed_3 = randbelow(999999) + 5555
    seed(seed_2 * seed_3)
    shuffle_(iterable)
def randbool():
    return choice([True, False])
def token_alphanumeric(length):
    allowed = string_.ascii_letters + string_.digits
    _str = ""
    for i in range(length):
        _str = f"{_str}{choice(allowed)}"
    return _str

import cryptoquail.util.xkcd_wordlist as cq_util

def xkcd(words=6, add_numbers=1):
    """Generates secure and memorable passwords
    Go to https://xkcd.com/936/ or https://xkpasswd.net/s/ for more information.
    """
    wordlist = cq_util.wordlist.splitlines()
    a = []
    b = choice([" ", "-", "_", "&"])
    for _ in range(words):
        a.append(choice(wordlist))
    if add_numbers:
        a = a + list(str(secrets.randbelow(9999)))
    return b.join(a)
