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
def ψ_hash(string):
    if len(string) % 2 == 1:
        string = string + "d"
    a = ""
    def xor_fold(s):
        b = []
        c = 0
        d = []
        #Prepare numbers
        for _ in range(int(len(s) / 2)):
            e=(ord(s[c]) ^ ord(s[c+1])) % 254
            b.append(e)
            c += 2
        for i in b:
            d.append(chr(i))
        if not len(d) >= 36:
            for x in string:
                d.append(chr((ord(x) + 32 * 23) % 255))
        return "".join(d).encode()
    def PRNG(seed):
        f = []
        for _ in range(36):
            g = 1234567890 ^ (_+34)
            h = seed ^ g
            h = h + 118
            if h % 3 == 0:
                h = h ^ 324
                f.append(h % 251)
            elif h % 3 == 1:
                h = h ^ 280
                f.append(h % 254)
            else:
                f.append( h % 255)
        return bytes(f)
            
    if len(string) > 36:
        a = xor_fold(string)
    else:
        a = PRNG(int.from_bytes(string.encode("utf-8"), 'little'))
    return a
