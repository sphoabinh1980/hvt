import random
from sympy import prevprime
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%s %s %s\n' % x for x in qs)
def bigs(r, L):
    return str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
def samples():
    return [(fmt([(2, 12345, 1000), (3, 100, 7), (7, 0, 1)]), '832\n4\n0\n'), (fmt([(2, 100, 12), (10, 10**30, 1000000007)]), '4\n540840989\n')]
def tests():
    r = random.Random(92)
    T = {1: [fmt([(r.randint(0, 10**18), r.randint(0, 10**18), r.randint(1, 10**9)) for _ in range(10)]),
             fmt([(2, 100, 12), (6, 10**18, 36), (0, 0, 5), (10**18, 10**18, 10**9), (12, 10**18, 2**29), (3, 10**18 - 1, 1), (5, 0, 1), (999999937, 10**18, 999999937), (4, 7, 8), (10, 3, 1000)])],
         2: [fmt([(a, bigs(r, 10**5), m) for a, m in [(r.randint(1, 10**18), prevprime(r.randint(3, 10**9))) for _ in range(30)] if a % m][:10])],
         3: [fmt([(r.randint(0, 10**18), bigs(r, 10**5), r.randint(1, 10**9)) for _ in range(10)]),
             fmt([(r.choice([2, 6, 10, 12, 0, 10**18]), bigs(r, 10**5), r.choice([12, 1000, 2**29, 10**9, 1, 999999937 * 1])) for _ in range(10)])]}
    for k in range(len(T[2])):
        pass
    return T
def small(r):
    return fmt([(r.randint(0, 100), r.randint(0, 10**6), r.randint(1, 200)) for _ in range(10)])
