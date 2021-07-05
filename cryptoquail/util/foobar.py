import random
import secrets

__all__ = ["crypt", "text2number", "hash_", "compare_digest", "random_delay"]


def crypt(a, key):
    return a ^ key

def text2number(string):
    _bytes = bytes(string, encoding="utf-8")
    newstring = ""
    for i in _bytes:
        newstring = f"{newstring}{i}"
    return int(newstring)

def hash_(data, salt="random"):
    """Experimental hash function"""
    if salt == "random":
        salt = secrets.token_urlsafe(10)
    if salt == "none":
        salt = ""
    else:
        pass
    data = data + salt
    _data = int(data.encode('utf-8').hex(), 16)
    pseudorandom = random.Random()
    pseudorandom.seed(_data)
    hashed = pseudorandom.getrandbits(32 * 8).to_bytes(32, 'little')
    return {"hash": hashed, "salt": salt}

def random_delay():
    "creates lag to prevent timing attacks"
    quackit = []
    n = secrets.randbelow(99996)
    for i in range(n):
        quackit.append("quack!")
    return None

compare_digest = secrets.compare_digest
