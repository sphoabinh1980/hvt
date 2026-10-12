import random, math
from sympy import prevprime
def fmt(L, sys_):
    return '%d %d\n' % (len(sys_), L) + ''.join('%d %d\n' % (m, a) for m, a in sys_)
def coprimes(r, k, prodlim, mlim):
    ms = []
    P = 1
    tries = 0
    while len(ms) < k and tries < 10000:
        tries += 1
        m = r.randint(1, min(mlim, prodlim // P))
        if all(math.gcd(m, x) == 1 for x in ms) and P * m <= prodlim:
            ms.append(m); P *= m
    return ms
def mk(r, k, prodlim, mlim, L):
    ms = coprimes(r, k, prodlim, mlim)
    return fmt(L, [(m, r.randrange(m)) for m in ms])
def samples():
    return [(fmt(0, [(3, 2), (5, 3), (7, 2)]), '23\n'), (fmt(100, [(3, 2), (5, 3), (7, 2), (1, 0)]), '128\n'), (fmt(0, [(10**9, 1), (999999999, 0)]), '999999998000000001\n')]
def tests():
    r = random.Random(121)
    T = {1: [mk(r, r.randint(1, 10), 10**6, 10**6, r.randint(0, 10**6)) for _ in range(5)] + [fmt(10**6, [(999983, 5), (1, 0)]), fmt(999999, [(2, 1), (3, 2), (5, 4), (7, 6), (11, 10), (13, 12), (17, 16)])],
         2: [mk(r, r.randint(1, 10), 10**18, 10**9, 0) for _ in range(5)] + [fmt(0, [(10**9, 10**9 - 1), (999999999, 999999998)]), fmt(0, [(999999937, 5), (999999929, 7)])],
         3: [mk(r, r.randint(1, 10), 10**18, 10**9, r.randint(0, 10**18)) for _ in range(5)] + [fmt(10**18, [(10**9, 1), (999999999, 0)]), fmt(10**18, [(1, 0)]), fmt(10**18, [(2, 1), (3, 0)]), fmt(999999999999999999, [(999999937, 0), (999999929, 0)])]}
    return T
def small(r):
    return mk(r, r.randint(1, 4), 3000, 100, r.randint(0, 5000))
