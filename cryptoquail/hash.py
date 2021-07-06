from hashlib import md5, sha256 as sha256_, sha512 as sha512_, shake as shake_
def crc32(input_):
    from zlib import crc32 as crc32_
    return hex(crc32_(input_))
def shake(input_):
    return shake_.digest(input_)
def sha256(string):
    return sha256_(string.encode()).hexdigest()
def sha512(string):
    return sha512_(string.encode()).hexdigest()
