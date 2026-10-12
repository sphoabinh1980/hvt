import random
from sympy import prevprime
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d\n' % x for x in qs)
def samples():
    return [(fmt([(2, 9, 1000), (3, 4, 100), (1, 10**18, 10**18)]), '23\n21\n1\n'), (fmt([(0, 5, 7), (5, 3, 4), (10**18 - 1, 10**18, 10**18)]), '1\n0\n1\n')]
def tests():
    r = random.Random(93)
    T = {1: [fmt([(r.randint(0, 10**18), r.randint(0, 10**6), r.randint(1, 10**9)) for _ in range(10)]),
             fmt([(1, 10**6, 10**9), (0, 10**6, 7), (5, 10**6, 4), (7, 999999, 1), (10**9 + 8, 10**6, 10**9 + 7), (2, 10**6, 2**29), (3, 0, 5), (10**18, 10**6, 10**9), (4, 10**6, 3), (6, 10**6, 36)])],
         2: [fmt([(a, r.randint(0, 10**18), m) for a, m in [(r.randint(0, 10**18), prevprime(r.randint(3, 10**9))) for _ in range(30000)] if a % m not in (0, 1)][:10**4])],
         3: [fmt([(r.randint(0, 10**18), r.randint(0, 10**18), r.randint(1, 10**18)) for _ in range(10**4)]),
             fmt([(r.choice([0, 1, 10**18 - 1, 10**18, r.randint(0, 10**18)]), r.choice([10**18, 10**18 - 1, r.randint(0, 10**18)]), r.choice([10**18, 1, 999999999999999989, r.randint(1, 10**18)])) for _ in range(10**4)]),
             fmt([(m + 1, r.randint(0, 10**18), m) for m in [r.randint(1, 10**18) for _ in range(10**4)]])]}
    return T
def small(r):
    return fmt([(r.randint(0, 10**18), r.randint(0, 300), r.choice([r.randint(1, 100), r.randint(1, 10**18)])) for _ in range(10)])
