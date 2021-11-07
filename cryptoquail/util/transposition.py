"""
Transposition cipher.
"""

import math

def enc(msg, key):
    c = [""] * key
    for col in range(key):
        point = col
        while point < len(msg):
            c[col] += msg[point]
            point += key
    return "".join(c)

def dec(c, key):
    numcol = math.ceil(len(c) / key)
    numrow = key
    numsbox = (numcol * numrow) - len(c)
    msg = [""] * numcol
    col = 0
    row = 0
    for sym in c:
        msg[col] += sym
        col += 1
        if (
            (col == numcol)
            or (col == numcol-1)
            and (row >= numrow - numsbox)
            ):
            col = 0
            row += 1
    return "".join(msg)
