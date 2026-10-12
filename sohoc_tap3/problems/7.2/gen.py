import random
from sympy import prevprime
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def samples():
    return [(fmt([(10, 10), (10, 12), (5, 2), (0, 7), (100, 10)]), '2\n4\n3\n0\n24\n'),
            (fmt([(10**18, 2), (10**18, 999999999989), (2026, 360)]), '999999999999999976\n1000000\n505\n')]
def tests():
    r = random.Random(72)
    T = {1: [fmt([(r.randint(0, 20), r.randint(2, 100)) for _ in range(100)]), fmt([(n, b) for n in range(0, 21) for b in (12, 18, 50, 72, 96)][:100])],
         2: [fmt([(r.randint(0, 10**18), 10) for _ in range(100)]), fmt([(10**18 - k, 10) for k in range(100)])],
         3: [fmt([(r.randint(0, 10**18), r.randint(2, 10**12)) for _ in range(100)]),
             fmt([(r.randint(0, 10**18), prevprime(r.randint(3, 10**12))) for _ in range(100)]),
             fmt([(r.randint(0, 10**18), b) for b in [12, 18, 360, 2**39, 3**25, 999999999989 * 1, 999983 * 999979, 2 * 999999999989 // 2, 10**12, 963761198400] * 10]),
             fmt([(n, 12) for n in range(8, 108)])]}
    return T
def small(r):
    return fmt([(r.randint(0, 60), r.randint(2, 200)) for _ in range(20)])
