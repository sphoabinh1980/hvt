import random
from sympy import isprime, nextprime, prevprime
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
SPSP = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 3825123056546413051]
CARM = [561, 1105, 1729, 2465, 2821, 6601, 8911, 41041, 825265, 321197185, 5394826801, 232250619601, 9746347772161]
def mix(r, lim, Q, hard):
    xs = []
    for _ in range(Q):
        t = r.random()
        if t < 0.3:
            xs.append(prevprime(r.randint(3, lim)))
        elif t < 0.45 and hard:
            xs.append(r.choice([x for x in SPSP + CARM if x <= lim]))
        elif t < 0.6:
            p = prevprime(r.randint(3, int(lim ** 0.5)))
            xs.append(p * p)
        elif t < 0.75:
            a = prevprime(r.randint(3, int(lim ** 0.5))); b = prevprime(r.randint(3, lim // a))
            xs.append(a * b)
        else:
            xs.append(r.randint(1, lim))
    return xs
_cache = {}
def primes_near(r, lim, k):
    out = []
    x = lim
    while len(out) < k:
        x = prevprime(x); out.append(x)
    return out
def samples():
    return [(fmt([1, 2, 97, 561, 1000000007, 999966000289]), 'NO\nYES\nYES\nNO\nYES\nNO\n'),
            (fmt([25326001, 3825123056546413051, 18446744073709551557, 18446744073709551615]), 'NO\nNO\nYES\nNO\n')]
def tests():
    r = random.Random(53)
    T = {1: [fmt(mix(r, 10**12, 100, True)), fmt(primes_near(r, 10**12, 100)), fmt(list(range(1, 101)))],
         2: [fmt(mix(r, 10**18, 10**5, True)), fmt(primes_near(r, 10**18, 2000) * 50), fmt([x for x in SPSP + CARM if x <= 10**18] * 5000)],
         3: [fmt(mix(r, 2**64 - 1, 10**5, True)), fmt(primes_near(r, 2**64 - 1, 2000) * 50),
             fmt(([3825123056546413051] * 10 + [2**64 - 1, 2**64 - 59, 2**63, 2**63 + 1]) * 7000 + [18446744030759878681] * 2000)]}
    return T
def small(r):
    return fmt(mix(r, r.choice([10**4, 10**9, 10**18, 2**64 - 1]), 50, True))
