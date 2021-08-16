def generate(range_, start):
  count = range_
  primes = []
  for p in range(count):
    i = p + start
    prime  = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    a = 0
    for x in prime:
        if (x ** (i-1)) % i == 1:
            a += 1
    if a == len(prime):
        primes.append(i)
  return primes
