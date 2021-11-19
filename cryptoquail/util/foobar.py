import random, secrets

__all__ = ["crypt", "text2number", "compare_digest", "random_delay", "csprng"]

def crypt(a, key):
    return a ^ key

def text2number(string):
    _bytes = bytes(string, encoding="utf-8")
    newstring = ""
    for i in _bytes:
        newstring = f"{newstring}{i}"
    return int(newstring)

def random_delay():
    "creates lag to prevent timing attacks"
    quackit = []
    n = secrets.randbelow(99996)
    for i in range(n):
        quackit.append("quack!")
    return None

compare_digest = secrets.compare_digest
csprng = secrets.SystemRandom
