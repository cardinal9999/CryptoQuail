def euclid(m, n):

    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)



def exteuclid(a, b):

    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)

    while r2 > 0:

        q = r1//r2
        r = r1-q * r2
        r1 = r2
        r2 = r
        s = s1-q * s2
        s1 = s2
        s2 = s
        t = t1-q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return (r1, t1)


def verify(primes, e, message):
  p = primes[0]
  q = primes[1]
  n = p * q
  Pn = (p-1)*(q-1)
  r, d_key = exteuclid(Pn, e)
  if r == 1:
    d = int(d_key)
  else:
    raise ValueError("Invalid key")
  signature = (message**d) % n
  M1 = (signature**e) % n
  if message == M1:
    return "yes"
  else: return "no"
