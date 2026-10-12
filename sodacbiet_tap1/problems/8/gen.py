import random
from sympy import randprime, isprime
def F(q): return '%d\n' % len(q) + ''.join('%d\n' % x for x in q)
def samples():
    return [(F([7, 12, 8, 2026]), '0 6\n2 1\n3 0\n1 253\n')]
def tests():
    r = random.Random(8)
    big = [randprime(10**11, 10**12) for _ in range(300)] + [r.randint(1, 10**12) for _ in range(500)] + [2**20 * 5**10, 999999999989, 10**12, 1, 3, 9, 81 * 37]
    big += [randprime(10**5, 10**6) * randprime(10**5, 10**6) for _ in range(199)]
    return {1: [F([r.randint(1, 10**6) for _ in range(10)])], 2: [F(big[:1000])]}
def small(r):
    return F([r.randint(1, 5000) for _ in range(30)])
